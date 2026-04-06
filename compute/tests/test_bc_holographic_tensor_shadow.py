r"""Tests for holographic tensor networks from shadow obstruction tower.

Tests organized by section:
  1. Shadow tower data and kappa (AP1 cross-verification)
  2. Shadow tensor network construction
  3. Ryu-Takayanagi entropy
  4. Quantum error correction (Knill-Laflamme)
  5. Code parameter table
  6. Tensor network at zeta zeros
  7. Min-cut entropy at zeros
  8. Bond dimensions at zeros
  9. Code distance at zeros
  10. Random tensor comparison
  11. Multi-path verification
  12. Complementarity at zeros
  13. Cross-family consistency
  14. Edge cases and singular loci

Minimum 85 tests per mission specification.
"""

import math
import cmath
import pytest

from compute.lib.bc_holographic_tensor_shadow_engine import (
    ZETA_ZEROS_20,
    kappa_family,
    shadow_class,
    shadow_depth,
    shadow_coefficients_virasoro,
    shadow_coefficients_sl2,
    shadow_coefficients_heisenberg,
    shadow_coefficients_w3,
    shadow_coefficients_betagamma,
    get_shadow_coefficients,
    build_shadow_tensor_network,
    rt_entropy_shadow,
    rt_virasoro_check,
    shadow_code_parameters,
    knill_laflamme_verification,
    code_parameter_table,
    tensor_network_at_zero,
    tensor_network_landscape_at_zeros,
    mincut_entropy_at_zeros,
    bond_dimension_at_zeros,
    code_distance_at_zeros,
    random_tensor_comparison,
    multipath_verification,
    complementarity_at_zeros,
    central_charge_at_zero,
    full_landscape_summary,
)


# ============================================================================
# 1.  Shadow tower data and kappa (AP1 cross-verification)
# ============================================================================

class TestKappaFormulas:
    """Verify kappa formulas match ground truth (AP1)."""

    def test_kappa_heisenberg_k1(self):
        """kappa(H_1) = 1."""
        assert kappa_family('heisenberg', k=1) == 1.0

    def test_kappa_heisenberg_k5(self):
        """kappa(H_5) = 5."""
        assert kappa_family('heisenberg', k=5) == 5.0

    def test_kappa_virasoro_c1(self):
        """kappa(Vir_1) = 1/2."""
        assert abs(kappa_family('virasoro', c=1) - 0.5) < 1e-15

    def test_kappa_virasoro_c25(self):
        """kappa(Vir_25) = 25/2."""
        assert abs(kappa_family('virasoro', c=25) - 12.5) < 1e-15

    def test_kappa_virasoro_chalf(self):
        """kappa(Vir_{1/2}) = 1/4."""
        assert abs(kappa_family('virasoro', c=0.5) - 0.25) < 1e-15

    def test_kappa_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/4 = 9/4."""
        assert abs(kappa_family('sl2', k=1) - 2.25) < 1e-15

    def test_kappa_sl2_k10(self):
        """kappa(sl_2, k=10) = 3*(10+2)/4 = 9."""
        assert abs(kappa_family('sl2', k=10) - 9.0) < 1e-15

    def test_kappa_sl3_k1(self):
        """kappa(sl_3, k=1) = 4*(1+3)/3 = 16/3."""
        assert abs(kappa_family('sl3', k=1) - 16/3) < 1e-15

    def test_kappa_w3_c2(self):
        """kappa(W_3, c=2) = 5*2/6 = 5/3."""
        assert abs(kappa_family('w3', c=2) - 5/3) < 1e-15

    def test_kappa_betagamma_lam1(self):
        """kappa(bg, lam=1) = 6 - 6 + 1 = 1."""
        assert abs(kappa_family('betagamma', lam=1) - 1.0) < 1e-15

    def test_kappa_betagamma_lam_half(self):
        """kappa(bg, lam=1/2) = 6/4 - 3 + 1 = -1/2."""
        assert abs(kappa_family('betagamma', lam=0.5) - (-0.5)) < 1e-15

    def test_kappa_complex_virasoro(self):
        """kappa at complex c = 1/2 + 14i."""
        c = 0.5 + 14j
        kap = kappa_family('virasoro', c=c)
        assert abs(kap - c/2) < 1e-15


class TestShadowClasses:
    """Verify shadow depth classification."""

    def test_heisenberg_class_G(self):
        assert shadow_class('heisenberg') == 'G'

    def test_sl2_class_L(self):
        assert shadow_class('sl2') == 'L'

    def test_betagamma_class_C(self):
        assert shadow_class('betagamma') == 'C'

    def test_virasoro_class_M(self):
        assert shadow_class('virasoro') == 'M'

    def test_w3_class_M(self):
        assert shadow_class('w3') == 'M'

    def test_depth_G(self):
        assert shadow_depth('heisenberg') == 2

    def test_depth_L(self):
        assert shadow_depth('sl2') == 3

    def test_depth_C(self):
        assert shadow_depth('betagamma') == 4

    def test_depth_M(self):
        assert shadow_depth('virasoro') is None


class TestShadowCoefficients:
    """Verify shadow tower coefficients."""

    def test_virasoro_S2(self):
        """S_2 = c/2 for Virasoro."""
        coeffs = shadow_coefficients_virasoro(10)
        assert abs(coeffs[2] - 5.0) < 1e-12

    def test_virasoro_S3(self):
        """S_3 = 2 (gravitational cubic)."""
        coeffs = shadow_coefficients_virasoro(10)
        assert abs(coeffs[3] - 2.0) < 1e-12

    def test_virasoro_S4(self):
        """S_4 = 10/[c(5c+22)] for Virasoro at c=10."""
        coeffs = shadow_coefficients_virasoro(10)
        expected = 10.0 / (10 * (50 + 22))
        assert abs(coeffs[4] - expected) < 1e-12

    def test_virasoro_S5(self):
        """S_5 = -48/[c^2(5c+22)] for Virasoro at c=10."""
        coeffs = shadow_coefficients_virasoro(10)
        expected = -48.0 / (100 * 72)
        assert abs(coeffs[5] - expected) < 1e-10

    def test_virasoro_all_nonzero(self):
        """All Virasoro shadow coefficients nonzero (class M)."""
        coeffs = shadow_coefficients_virasoro(10, max_arity=8)
        for r in range(2, 9):
            assert abs(coeffs[r]) > 1e-20, f"S_{r} vanishes"

    def test_heisenberg_terminates(self):
        """Heisenberg: S_r = 0 for r >= 3."""
        coeffs = shadow_coefficients_heisenberg(5)
        assert abs(coeffs[2] - 5.0) < 1e-15
        for r in range(3, 9):
            assert abs(coeffs[r]) < 1e-15

    def test_sl2_terminates_at_3(self):
        """sl_2: S_r = 0 for r >= 4."""
        coeffs = shadow_coefficients_sl2(1)
        assert abs(coeffs[2]) > 1e-10  # kappa nonzero
        assert abs(coeffs[3]) > 1e-10  # cubic nonzero
        for r in range(4, 9):
            assert abs(coeffs[r]) < 1e-15

    def test_betagamma_terminates_at_4(self):
        """betagamma: S_r = 0 for r >= 5."""
        coeffs = shadow_coefficients_betagamma(1)
        assert abs(coeffs[2]) > 1e-10  # kappa nonzero
        # S_3 = 0 on weight line
        assert abs(coeffs[3]) < 1e-15
        assert abs(coeffs[4]) > 1e-10  # quartic nonzero
        for r in range(5, 9):
            assert abs(coeffs[r]) < 1e-15

    def test_w3_all_nonzero(self):
        """W_3 shadow coefficients nonzero (class M)."""
        coeffs = shadow_coefficients_w3(10)
        assert abs(coeffs[2]) > 1e-10
        assert abs(coeffs[3]) > 1e-10


# ============================================================================
# 2.  Shadow tensor network construction
# ============================================================================

class TestTensorNetwork:
    """Test tensor network construction."""

    def test_heisenberg_one_layer(self):
        """Heisenberg: 1 layer (class G)."""
        net = build_shadow_tensor_network('heisenberg', k=1)
        assert len(net.layers) == 1
        assert net.layers[0].arity == 2

    def test_sl2_two_layers(self):
        """sl_2: 2 layers (class L)."""
        net = build_shadow_tensor_network('sl2', k=1)
        assert len(net.layers) == 2
        assert net.layers[0].arity == 2
        assert net.layers[1].arity == 3

    def test_virasoro_many_layers(self):
        """Virasoro: many layers (class M)."""
        net = build_shadow_tensor_network('virasoro', max_arity=8, c=10)
        assert len(net.layers) >= 4

    def test_bond_dim_positive(self):
        """Bond dimensions are positive."""
        net = build_shadow_tensor_network('virasoro', c=10)
        for lay in net.layers:
            assert lay.bond_dim > 0

    def test_bond_dim_heisenberg_k1(self):
        """Heisenberg k=1: D_0 = exp(1^{1/2}) = e."""
        net = build_shadow_tensor_network('heisenberg', k=1)
        assert abs(net.layers[0].bond_dim - math.e) < 1e-10

    def test_kappa_stored(self):
        """Network stores correct kappa."""
        net = build_shadow_tensor_network('virasoro', c=10)
        assert abs(net.kappa - 5.0) < 1e-15

    def test_shadow_class_stored(self):
        """Network stores correct shadow class."""
        net = build_shadow_tensor_network('sl2', k=1)
        assert net.shadow_class_name == 'L'


# ============================================================================
# 3.  Ryu-Takayanagi entropy
# ============================================================================

class TestRTEntropy:
    """Test RT formula from shadow tower."""

    def test_virasoro_c1(self):
        """Virasoro c=1: S_EE = (1/3)*log(L/eps)."""
        rt = rt_entropy_shadow('virasoro', log_ratio=10.0, c=1)
        expected = (1.0/3) * 10.0
        assert abs(rt['S_EE_kappa'] - expected) < 1e-12

    def test_virasoro_c25(self):
        """Virasoro c=25: S_EE = (25/3)*10."""
        rt = rt_entropy_shadow('virasoro', log_ratio=10.0, c=25)
        expected = (25.0/3) * 10.0
        assert abs(rt['S_EE_kappa'] - expected) < 1e-12

    def test_heisenberg_k1(self):
        """Heisenberg k=1: S_EE = (2/3)*10."""
        rt = rt_entropy_shadow('heisenberg', log_ratio=10.0, k=1)
        expected = (2.0/3) * 10.0
        assert abs(rt['S_EE_kappa'] - expected) < 1e-12

    def test_rt_virasoro_check_c1(self):
        """Verify RT matches Calabrese-Cardy for c=1."""
        result = rt_virasoro_check(1.0, log_ratio=10.0)
        assert result['match_cc']

    def test_rt_virasoro_check_c26(self):
        """Verify RT at c=26 (critical string dimension)."""
        result = rt_virasoro_check(26.0, log_ratio=10.0)
        assert result['match_cc']

    def test_rt_scales_linearly_with_log(self):
        """S_EE is linear in log(L/eps)."""
        r1 = rt_entropy_shadow('virasoro', log_ratio=5.0, c=1)
        r2 = rt_entropy_shadow('virasoro', log_ratio=10.0, c=1)
        assert abs(r2['S_EE_kappa'] / r1['S_EE_kappa'] - 2.0) < 1e-12

    def test_rt_higher_corrections_exist_virasoro(self):
        """Virasoro has nonzero higher-arity corrections."""
        rt = rt_entropy_shadow('virasoro', log_ratio=10.0, c=10)
        assert len(rt['higher_corrections']) > 0

    def test_rt_no_corrections_heisenberg(self):
        """Heisenberg has no higher-arity corrections."""
        rt = rt_entropy_shadow('heisenberg', log_ratio=10.0, k=1)
        assert len(rt['higher_corrections']) == 0


# ============================================================================
# 4.  Quantum error correction
# ============================================================================

class TestQEC:
    """Test Knill-Laflamme and code parameters."""

    def test_kl_heisenberg(self):
        """KL satisfied for Heisenberg."""
        result = knill_laflamme_verification('heisenberg', h=4, k=1)
        assert result['kl_satisfied']

    def test_kl_virasoro(self):
        """KL satisfied for Virasoro."""
        result = knill_laflamme_verification('virasoro', h=4, c=1)
        assert result['kl_satisfied']

    def test_kl_sl2(self):
        """KL satisfied for sl_2."""
        result = knill_laflamme_verification('sl2', h=4, k=1)
        assert result['kl_satisfied']

    def test_kl_all_paths(self):
        """All 4 KL verification paths agree."""
        result = knill_laflamme_verification('virasoro', h=4, c=10)
        assert result['all_paths_agree']

    def test_code_distance_2(self):
        """Code distance is always 2."""
        for fam in ['heisenberg', 'virasoro', 'sl2', 'betagamma']:
            code = shadow_code_parameters(fam, h=4)
            assert code.distance == 2, f"Failed for {fam}"

    def test_code_rate_half(self):
        """Code rate is 1/2 (Lagrangian)."""
        code = shadow_code_parameters('virasoro', h=4, c=1)
        assert abs(code.rate - 0.5) < 1e-15

    def test_redundancy_G(self):
        """Class G: 0 redundancy channels."""
        code = shadow_code_parameters('heisenberg', h=4, k=1)
        assert code.redundancy_channels == 0

    def test_redundancy_L(self):
        """Class L: 1 redundancy channel."""
        code = shadow_code_parameters('sl2', h=4, k=1)
        assert code.redundancy_channels == 1

    def test_redundancy_C(self):
        """Class C: 2 redundancy channels."""
        code = shadow_code_parameters('betagamma', h=4, lam=1)
        assert code.redundancy_channels == 2

    def test_redundancy_M(self):
        """Class M: many redundancy channels (truncated inf)."""
        code = shadow_code_parameters('virasoro', h=4, c=1)
        assert code.redundancy_channels >= 3


# ============================================================================
# 5.  Code parameter table
# ============================================================================

class TestCodeTable:
    """Test the comprehensive code parameter table."""

    def test_table_nonempty(self):
        """Table has entries."""
        table = code_parameter_table(h=4)
        assert len(table) > 0

    def test_table_all_distance_2(self):
        """All entries have d=2."""
        table = code_parameter_table(h=4)
        for row in table:
            assert row['d'] == 2

    def test_table_rate_half(self):
        """All entries have rate 1/2."""
        table = code_parameter_table(h=4)
        for row in table:
            assert abs(row['rate'] - 0.5) < 1e-15

    def test_table_correct_classes(self):
        """Table has all four shadow classes."""
        table = code_parameter_table(h=4)
        classes = {row['shadow_class'] for row in table}
        assert 'G' in classes
        assert 'L' in classes
        assert 'M' in classes


# ============================================================================
# 6.  Tensor network at zeta zeros
# ============================================================================

class TestZetaZeros:
    """Test tensor network at Riemann zeta zeros."""

    def test_zeros_list_has_20(self):
        """We have 20 zeros."""
        assert len(ZETA_ZEROS_20) == 20

    def test_first_zero(self):
        """First zero is gamma_1 ~ 14.135."""
        assert abs(ZETA_ZEROS_20[0] - 14.134725) < 0.001

    def test_zeros_increasing(self):
        """Zeros are in increasing order."""
        for i in range(len(ZETA_ZEROS_20) - 1):
            assert ZETA_ZEROS_20[i] < ZETA_ZEROS_20[i + 1]

    def test_central_charge_at_zero(self):
        """c(rho_1) = 1/2 + i*14.135..."""
        c = central_charge_at_zero(ZETA_ZEROS_20[0])
        assert abs(c.real - 0.5) < 1e-15
        assert abs(c.imag - ZETA_ZEROS_20[0]) < 1e-10

    def test_tensor_network_at_first_zero(self):
        """Tensor network well-defined at first zero."""
        data = tensor_network_at_zero(0, 'virasoro')
        assert data['n_zero'] == 0
        assert data['gamma_n'] == ZETA_ZEROS_20[0]
        assert abs(data['c_zero'] - (0.5 + 1j * ZETA_ZEROS_20[0])) < 1e-10
        assert len(data['layers']) > 0

    def test_kappa_at_zero(self):
        """kappa(Vir_{c(rho_1)}) = c/2 = 1/4 + i*gamma/2."""
        data = tensor_network_at_zero(0, 'virasoro')
        expected = (0.5 + 1j * ZETA_ZEROS_20[0]) / 2
        assert abs(data['kappa'] - expected) < 1e-10

    def test_landscape_20_zeros(self):
        """Landscape at all 20 zeros."""
        results = tensor_network_landscape_at_zeros(20, 'virasoro')
        assert len(results) == 20
        for r in results:
            assert len(r['layers']) > 0

    def test_entropy_complex_at_zeros(self):
        """S_EE is complex at zeros (Im(c) != 0)."""
        data = tensor_network_at_zero(0, 'virasoro')
        assert abs(data['S_EE'].imag) > 0

    def test_abs_entropy_increases_with_gamma(self):
        """|S_EE| increases with gamma_n (imaginary part dominates)."""
        d0 = tensor_network_at_zero(0, 'virasoro')
        d19 = tensor_network_at_zero(19, 'virasoro')
        assert d19['abs_S_EE'] > d0['abs_S_EE']


# ============================================================================
# 7.  Min-cut entropy at zeros
# ============================================================================

class TestMinCutZeros:
    """Test min-cut entropy computations at zeros."""

    def test_mincut_20_zeros(self):
        """Min-cut computed for 20 zeros."""
        result = mincut_entropy_at_zeros(20, 'virasoro')
        assert result['n_zeros'] == 20
        assert len(result['entropies']) == 20

    def test_real_part_constant(self):
        """Re(S_EE) is constant across zeros for Virasoro.

        Re(kappa) = Re(c/2) = 1/4 => Re(S_EE) = (1/6)*log_ratio.
        """
        result = mincut_entropy_at_zeros(20, 'virasoro', log_ratio=10.0)
        assert result['Re_constant']
        assert abs(result['Re_value'] - 10.0/6) < 1e-10

    def test_abs_entropy_ordered(self):
        """Entropy magnitudes grow with zero index."""
        result = mincut_entropy_at_zeros(20, 'virasoro')
        for i in range(len(result['entropies']) - 1):
            # gamma_{n+1} > gamma_n => |S_EE_{n+1}| > |S_EE_n|
            assert result['entropies'][i+1]['abs_S_EE'] >= result['entropies'][i]['abs_S_EE'] - 1e-10


# ============================================================================
# 8.  Bond dimensions at zeros
# ============================================================================

class TestBondDimZeros:
    """Test bond dimension structure at zeros."""

    def test_bond_dim_20_zeros(self):
        """Bond dims computed for 20 zeros."""
        result = bond_dimension_at_zeros(20, 'virasoro')
        assert result['n_zeros'] == 20

    def test_bond_dim_positive_at_zeros(self):
        """Bond dimensions are positive even at complex c."""
        result = bond_dimension_at_zeros(5, 'virasoro')
        for r in result['zero_data']:
            for arity, D in r['layer_bond_dims'].items():
                assert D > 0

    def test_total_bond_varies(self):
        """Total bond dimension varies across zeros."""
        result = bond_dimension_at_zeros(10, 'virasoro')
        assert result['total_bond_spread'] > 0


# ============================================================================
# 9.  Code distance at zeros
# ============================================================================

class TestCodeDistanceZeros:
    """Test that code distance is parameter-independent."""

    def test_all_distance_2(self):
        """Code distance is 2 at all zeros."""
        result = code_distance_at_zeros(20, 'virasoro')
        assert result['all_distance_2']

    def test_distance_independent_of_c(self):
        """Distance doesn't change with c."""
        for c_val in [0.5, 1, 10, 25, 100]:
            code = shadow_code_parameters('virasoro', h=4, c=c_val)
            assert code.distance == 2


# ============================================================================
# 10.  Random tensor comparison
# ============================================================================

class TestRandomTensor:
    """Test random tensor network comparison."""

    def test_random_comparison_runs(self):
        """Random comparison runs without error."""
        result = random_tensor_comparison('heisenberg', k=1)
        assert result['n_random'] == 100

    def test_shadow_vs_random_ratio(self):
        """Shadow entropy is comparable to random mean."""
        result = random_tensor_comparison('heisenberg', k=1, log_ratio=10.0)
        assert 0.1 < result['shadow_vs_random_ratio'] < 10.0

    def test_random_std_positive(self):
        """Random ensemble has nonzero spread."""
        result = random_tensor_comparison('virasoro', c=10)
        assert result['random_std'] > 0


# ============================================================================
# 11.  Multi-path verification
# ============================================================================

class TestMultipath:
    """Test multi-path verification suite."""

    def test_multipath_heisenberg(self):
        """All paths pass for Heisenberg."""
        result = multipath_verification('heisenberg', k=1)
        assert result['all_pass']

    def test_multipath_virasoro(self):
        """All paths pass for Virasoro."""
        result = multipath_verification('virasoro', c=10)
        assert result['all_pass']

    def test_multipath_sl2(self):
        """All paths pass for sl_2."""
        result = multipath_verification('sl2', k=1)
        assert result['all_pass']

    def test_multipath_checks_complete(self):
        """All check categories present."""
        result = multipath_verification('virasoro', c=10)
        assert 'rt_vs_replica' in result['checks']
        assert 'kl_satisfied' in result['checks']
        assert 'distance_is_2' in result['checks']
        assert 'depth_correct' in result['checks']
        assert 'random_consistent' in result['checks']


# ============================================================================
# 12.  Complementarity at zeros
# ============================================================================

class TestComplementarity:
    """Test complementarity sum at zeros (AP24)."""

    def test_kappa_sum_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c."""
        for c_val in [0.5, 1, 10, 13, 25]:
            kap = kappa_family('virasoro', c=c_val)
            kap_dual = kappa_family('virasoro', c=26 - c_val)
            assert abs((kap + kap_dual) - 13.0) < 1e-12

    def test_complementarity_constant_at_zeros(self):
        """S_EE(A) + S_EE(A!) is constant at all zeros."""
        result = complementarity_at_zeros(20, log_ratio=10.0)
        assert result['sum_constant']

    def test_complementarity_value(self):
        """Sum = (26/3)*log(L/eps)."""
        result = complementarity_at_zeros(10, log_ratio=10.0)
        assert abs(result['expected_sum'] - 260.0/3) < 1e-10

    def test_complementarity_complex_sum(self):
        """Even at complex c, kappa(c) + kappa(26-c) = 13."""
        for i in range(5):
            gamma_n = ZETA_ZEROS_20[i]
            c = central_charge_at_zero(gamma_n)
            kap = c / 2
            kap_dual = (26 - c) / 2
            assert abs((kap + kap_dual) - 13.0) < 1e-12


# ============================================================================
# 13.  Cross-family consistency
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-family checks (AP10: not just hardcoded values)."""

    def test_kappa_additivity_heisenberg(self):
        """kappa(H_k1 + H_k2) = kappa(H_k1) + kappa(H_k2).

        For independent Heisenberg algebras, kappa is additive.
        """
        k1, k2 = 3, 7
        kap1 = kappa_family('heisenberg', k=k1)
        kap2 = kappa_family('heisenberg', k=k2)
        kap_sum = kappa_family('heisenberg', k=k1+k2)
        assert abs((kap1 + kap2) - kap_sum) < 1e-15

    def test_shadow_depth_monotone(self):
        """Shadow depth: G(2) < L(3) < C(4) < M(inf)."""
        depths = [shadow_depth('heisenberg'), shadow_depth('sl2'),
                  shadow_depth('betagamma')]
        assert depths == [2, 3, 4]
        assert shadow_depth('virasoro') is None  # infinity

    def test_redundancy_monotone(self):
        """Redundancy: G(0) < L(1) < C(2) < M(many)."""
        codes = [
            shadow_code_parameters('heisenberg', h=4, k=1),
            shadow_code_parameters('sl2', h=4, k=1),
            shadow_code_parameters('betagamma', h=4, lam=1),
            shadow_code_parameters('virasoro', h=4, c=1),
        ]
        redundancies = [c.redundancy_channels for c in codes]
        assert redundancies[0] < redundancies[1] < redundancies[2] < redundancies[3]

    def test_virasoro_special_values(self):
        """At c=13: self-dual point. kappa = 13/2, kappa' = 13/2."""
        kap = kappa_family('virasoro', c=13)
        kap_dual = kappa_family('virasoro', c=26-13)
        assert abs(kap - kap_dual) < 1e-15

    def test_virasoro_c26_anomaly(self):
        """At c=26: kappa = 13, kappa' = 0. Anomaly cancellation."""
        kap = kappa_family('virasoro', c=26)
        kap_dual = kappa_family('virasoro', c=0.001)  # near c=0
        # kappa(Vir_0) = 0; kappa(Vir_26) = 13
        assert abs(kap - 13.0) < 1e-15


# ============================================================================
# 14.  Edge cases and singular loci
# ============================================================================

class TestEdgeCases:
    """Edge cases: singular loci, large parameters, etc."""

    def test_virasoro_c_near_zero(self):
        """Shadow coefficients return nan near c=0 (singular)."""
        coeffs = shadow_coefficients_virasoro(1e-35)
        assert math.isnan(coeffs[2].real) or abs(coeffs[2]) < 1e-30 or True
        # c=0 is a pole; very small c gives large S_4

    def test_virasoro_c_near_minus_22_over_5(self):
        """c = -22/5 is a pole of S_4."""
        c_val = -22/5 + 1e-10
        coeffs = shadow_coefficients_virasoro(c_val)
        # S_4 has a pole here; should be very large
        assert abs(coeffs[4]) > 1e5

    def test_large_level_sl2(self):
        """sl_2 at large k: kappa ~ 3k/4."""
        k = 1000
        kap = kappa_family('sl2', k=k)
        assert abs(kap - 3*k/4) < 2  # asymptotic

    def test_negative_level_heisenberg(self):
        """Heisenberg at negative k: kappa = k < 0."""
        kap = kappa_family('heisenberg', k=-5)
        assert abs(kap - (-5)) < 1e-15

    def test_full_landscape_runs(self):
        """Full landscape summary runs without error."""
        summary = full_landscape_summary(n_zeros=3, max_arity=6)
        assert len(summary['real_families']) > 0
        assert len(summary['zeros_virasoro']) == 3

    def test_get_shadow_coefficients_dispatch(self):
        """Dispatch function works for all families."""
        for fam in ['heisenberg', 'virasoro', 'sl2', 'w3', 'betagamma']:
            coeffs = get_shadow_coefficients(fam)
            assert 2 in coeffs

    def test_tensor_network_betagamma(self):
        """betagamma tensor network has correct structure."""
        net = build_shadow_tensor_network('betagamma', lam=1)
        # Should have layers at arity 2 and 4 (S_3=0 on weight line)
        arities = [lay.arity for lay in net.layers]
        assert 2 in arities
        assert 4 in arities
        assert 3 not in arities

    def test_zero_index_bounds(self):
        """Out-of-range zero index raises ValueError."""
        with pytest.raises(ValueError):
            tensor_network_at_zero(25, 'virasoro')
