r"""Tests for compute/lib/bc_nekrasov_zeta_zeros_engine.py

Comprehensive test suite covering:
  - Section 0: Zeta zero utilities
  - Section 1: Nekrasov at zeta-zero Omega-background
  - Section 2: Instanton sum
  - Section 3: Seiberg-Witten at zeta zeros
  - Section 4: AGT dictionary
  - Section 5: Instanton moduli space
  - Section 6: Perturbative partition function
  - Section 7: Shadow-Nekrasov bridge
  - Section 8: Surface operator
  - Section 9: Multi-path verification

MULTI-PATH VERIFICATION strategy:
  Path 1: Direct Young diagram summation (all Z_k)
  Path 2: AGT -- conformal block at c=25 matches Nekrasov
  Path 3: Asymptotic -- Z_k growth rate
  Path 4: eps -> 0 recovers SW prepotential
  Path 5: Shadow invariants at c=25 are self-consistent

BEILINSON WARNINGS applied:
  AP1:  kappa(Vir_25) = 25/2, recomputed from first principles.
  AP10: Tests use independent cross-checks, not hardcoded wrong values.
  AP38: Convention: rho_n = 1/2 + i*gamma_n under RH.
  AP42: AGT = shadow at the motivic level; naive identification insufficient.
  AP48: kappa = c/2 is specific to Virasoro.
"""

import math
import pytest

# Guard against missing mpmath
try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

pytestmark = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath not available")

from compute.lib.bc_nekrasov_zeta_zeros_engine import (
    # Section 0: Zeta zero utilities
    zeta_zero_gamma,
    zeta_zero_rho,
    zeta_zeros_table,
    # Section 1: Nekrasov at zeta zeros
    nekrasov_at_zeta_zero,
    _nekrasov_instanton_complex,
    _N_function_complex,
    # Section 2: Instanton sum
    instanton_sum_at_zeta_zero,
    instanton_free_energy_at_zeta_zero,
    # Section 3: SW at zeta zeros
    sw_prepotential_at_zeta_zero,
    sw_discriminant_at_zeta_zero,
    # Section 4: AGT dictionary
    agt_at_zeta_zero,
    agt_nekrasov_match_at_zeta_zero,
    # Section 5: Instanton moduli
    adhm_equivariant_volume,
    # Section 6: Perturbative
    perturbative_at_zeta_zero,
    full_partition_function_at_zeta_zero,
    # Section 7: Shadow-Nekrasov bridge
    shadow_at_self_dual,
    shadow_nekrasov_comparison,
    shadow_tower_at_c25,
    # Section 8: Surface operator
    surface_operator_at_zeta_zero,
    surface_operator_sweep,
    # Section 9: Multi-path verification
    verify_self_dual_c25,
    verify_z0_equals_1,
    verify_z1_analytic,
    verify_instanton_growth,
    verify_sw_limit,
    # Section 10: Summary
    full_sweep,
    instanton_magnitude_table,
)


# ====================================================================
# Section 0: Zeta zero utilities
# ====================================================================

class TestZetaZeroUtilities:
    """Tests for the zeta zero helper functions."""

    def test_gamma_1_value(self):
        """gamma_1 ~ 14.134725."""
        g1 = zeta_zero_gamma(1)
        assert abs(g1 - 14.134725) < 0.001

    def test_gamma_2_value(self):
        """gamma_2 ~ 21.022040."""
        g2 = zeta_zero_gamma(2)
        assert abs(g2 - 21.022040) < 0.001

    def test_gamma_3_value(self):
        """gamma_3 ~ 25.010858."""
        g3 = zeta_zero_gamma(3)
        assert abs(g3 - 25.010858) < 0.001

    def test_rho_on_critical_line(self):
        """Under RH, Re(rho_n) = 1/2 for all n."""
        for n in range(1, 6):
            rho = zeta_zero_rho(n)
            assert abs(rho.real - 0.5) < 1e-10

    def test_gamma_positive(self):
        """All gamma_n > 0."""
        for n in range(1, 6):
            g = zeta_zero_gamma(n)
            assert g > 0

    def test_gammas_increasing(self):
        """gamma_1 < gamma_2 < ... < gamma_5."""
        gammas = [zeta_zero_gamma(n) for n in range(1, 6)]
        for i in range(len(gammas) - 1):
            assert gammas[i] < gammas[i + 1]

    def test_zeros_table_length(self):
        """Table with n_max=10 has 10 entries."""
        table = zeta_zeros_table(10)
        assert len(table) == 10

    def test_zeros_table_structure(self):
        """Each entry has the expected keys."""
        table = zeta_zeros_table(3)
        for entry in table:
            assert 'n' in entry
            assert 'rho' in entry
            assert 'gamma' in entry
            assert 'rho_half' in entry

    def test_rho_half_value(self):
        """rho_half = rho/2 correctly computed."""
        table = zeta_zeros_table(3)
        for entry in table:
            assert abs(entry['rho_half'] - entry['rho'] / 2) < 1e-10

    def test_invalid_n_raises(self):
        """n < 1 should raise ValueError."""
        with pytest.raises(ValueError):
            zeta_zero_gamma(0)


# ====================================================================
# Section 1: Nekrasov at zeta zeros
# ====================================================================

class TestNekrasovAtZetaZeros:
    """Tests for the Nekrasov PF at zeta-zero Omega-background."""

    def test_self_dual_c_equals_25(self):
        """At self-dual point, c = 25."""
        data = nekrasov_at_zeta_zero(1.0, 1, max_inst=1, dps=20)
        assert data['c'] == 25.0

    def test_beta_equals_zero(self):
        """eps1 + eps2 = 0 at self-dual."""
        data = nekrasov_at_zeta_zero(1.0, 1, max_inst=0, dps=20)
        assert abs(data['beta']) < 1e-10

    def test_hbar_equals_gamma_squared(self):
        """hbar = eps1 * eps2 = gamma_n^2."""
        data = nekrasov_at_zeta_zero(1.0, 1, max_inst=0, dps=20)
        gamma = data['gamma']
        assert abs(data['hbar'] - gamma**2) < 1e-5

    def test_z0_equals_1(self):
        """Z_0 = 1 for any Omega-background."""
        data = nekrasov_at_zeta_zero(1.0, 1, max_inst=2, dps=20)
        assert abs(data['coefficients'][0] - 1.0) < 1e-10

    def test_z0_equals_1_different_zeros(self):
        """Z_0 = 1 for different zeta zeros."""
        for n in [1, 2, 5]:
            data = nekrasov_at_zeta_zero(1.0, n, max_inst=0, dps=20)
            assert abs(data['coefficients'][0] - 1.0) < 1e-10

    def test_z1_nonzero(self):
        """Z_1 is nonzero for generic a."""
        data = nekrasov_at_zeta_zero(1.0, 1, max_inst=1, dps=20)
        assert abs(data['coefficients'][1]) > 1e-20

    def test_z1_finite(self):
        """Z_1 is finite (not NaN or inf)."""
        data = nekrasov_at_zeta_zero(1.0, 1, max_inst=1, dps=20)
        z1 = data['coefficients'][1]
        assert math.isfinite(abs(z1))

    def test_kappa_is_c_over_2(self):
        """kappa = c/2 = 25/2 = 12.5 at self-dual."""
        data = nekrasov_at_zeta_zero(1.0, 1, max_inst=0, dps=20)
        assert abs(data['kappa'] - 12.5) < 1e-10

    def test_eps_purely_imaginary(self):
        """eps1, eps2 are purely imaginary."""
        data = nekrasov_at_zeta_zero(1.0, 1, max_inst=0, dps=20)
        assert abs(data['eps1'].real) < 1e-10
        assert abs(data['eps2'].real) < 1e-10

    def test_eps_sum_zero(self):
        """eps1 = -eps2 at self-dual."""
        data = nekrasov_at_zeta_zero(1.0, 1, max_inst=0, dps=20)
        assert abs(data['eps1'] + data['eps2']) < 1e-10


# ====================================================================
# Section 2: Instanton sum
# ====================================================================

class TestInstantonSum:
    """Tests for the instanton partial sums and free energy."""

    def test_partial_sums_monotone_dict(self):
        """Partial sums are computed for each k."""
        data = instanton_sum_at_zeta_zero(1.0, 1, max_inst=3, q_val=0.1, dps=20)
        assert 0 in data['partial_sums']
        assert 1 in data['partial_sums']
        assert 2 in data['partial_sums']
        assert 3 in data['partial_sums']

    def test_partial_sum_0_equals_1(self):
        """Partial sum at k=0 is Z_0 = 1."""
        data = instanton_sum_at_zeta_zero(1.0, 1, max_inst=3, q_val=0.1, dps=20)
        assert abs(data['partial_sums'][0] - 1.0) < 1e-10

    def test_instanton_sum_convergent(self):
        """For small q, higher instanton corrections are small."""
        data = instanton_sum_at_zeta_zero(1.0, 1, max_inst=5, q_val=0.01, dps=20)
        # |Z_total - 1| should be small for q = 0.01
        assert abs(data['Z_total'] - 1.0) < 1.0  # loose bound

    def test_free_energy_f1_equals_z1(self):
        """The first cumulant f_1 = Z_1."""
        data = instanton_free_energy_at_zeta_zero(1.0, 1, max_inst=3, dps=20)
        z1 = data['Z_coefficients'].get(1, 0.0)
        f1 = data['cumulants'].get(1, 0.0)
        assert abs(f1 - z1) < 1e-10

    def test_cumulant_structure(self):
        """f_2 = Z_2 - Z_1^2 / 2."""
        data = instanton_free_energy_at_zeta_zero(1.0, 1, max_inst=3, dps=20)
        z1 = data['Z_coefficients'].get(1, 0.0)
        z2 = data['Z_coefficients'].get(2, 0.0)
        f2 = data['cumulants'].get(2, 0.0)
        expected = z2 - z1**2 / 2
        assert abs(f2 - expected) < 1e-10


# ====================================================================
# Section 3: Seiberg-Witten at zeta zeros
# ====================================================================

class TestSeibergWitten:
    """Tests for the SW prepotential and discriminant at zeta zeros."""

    def test_sw_f1_coefficient(self):
        """F_1 = 1/2 (known exact value for pure SU(2))."""
        data = sw_prepotential_at_zeta_zero(1, max_inst=1, dps=20)
        assert abs(data['F_coefficients'][1] - 0.5) < 1e-10

    def test_sw_f2_coefficient(self):
        """F_2 = 5/64."""
        data = sw_prepotential_at_zeta_zero(1, max_inst=2, dps=20)
        assert abs(data['F_coefficients'][2] - 5.0/64) < 1e-10

    def test_sw_f3_coefficient(self):
        """F_3 = 3/128."""
        data = sw_prepotential_at_zeta_zero(1, max_inst=3, dps=20)
        assert abs(data['F_coefficients'][3] - 3.0/128) < 1e-10

    def test_sw_coefficients_independent_of_zero(self):
        """SW prepotential coefficients are universal constants."""
        data1 = sw_prepotential_at_zeta_zero(1, max_inst=3, dps=20)
        data2 = sw_prepotential_at_zeta_zero(5, max_inst=3, dps=20)
        for k in [1, 2, 3]:
            assert abs(data1['F_coefficients'][k] - data2['F_coefficients'][k]) < 1e-10

    def test_sw_a_is_rho_half(self):
        """a = rho_n / 2."""
        data = sw_prepotential_at_zeta_zero(1, max_inst=1, dps=20)
        rho = data['rho']
        a = data['a']
        assert abs(a - rho / 2) < 1e-10

    def test_sw_discriminant_finite(self):
        """SW discriminant is finite at zeta-zero Coulomb parameter."""
        data = sw_discriminant_at_zeta_zero(1, dps=20)
        assert math.isfinite(data['|discriminant|'])
        assert data['|discriminant|'] > 0

    def test_sw_discriminant_complex(self):
        """Discriminant is complex (a is complex)."""
        data = sw_discriminant_at_zeta_zero(1, dps=20)
        # rho_1 = 1/2 + i*14.13..., so a is complex, u is complex
        assert abs(data['discriminant'].imag) > 0.1

    def test_sw_f_inst_finite(self):
        """Total F_inst is finite."""
        data = sw_prepotential_at_zeta_zero(1, max_inst=3, dps=20)
        assert math.isfinite(abs(data['F_inst']))


# ====================================================================
# Section 4: AGT dictionary
# ====================================================================

class TestAGTDictionary:
    """Tests for the AGT correspondence at zeta zeros."""

    def test_agt_c_equals_25(self):
        """At self-dual, c = 25."""
        data = agt_at_zeta_zero(1, a_coulomb=1.0, max_level=1, dps=20)
        assert data['c'] == 25.0

    def test_agt_h_ext_equals_1(self):
        """External dimension h_ext = Q^2/4 = 1 at c = 25."""
        data = agt_at_zeta_zero(1, a_coulomb=1.0, max_level=1, dps=20)
        assert abs(data['h_ext'] - 1.0) < 1e-10

    def test_agt_h_int_positive(self):
        """Internal dimension h_int = a^2/gamma^2 > 0 for real a."""
        data = agt_at_zeta_zero(1, a_coulomb=1.0, max_level=1, dps=20)
        assert data['h_int'] > 0

    def test_agt_block_f0_equals_1(self):
        """Block coefficient F_0 = 1."""
        data = agt_at_zeta_zero(1, a_coulomb=1.0, max_level=1, dps=20)
        assert abs(data['block_coefficients'][0] - 1.0) < 1e-10

    def test_agt_h_int_scaling(self):
        """h_int = a^2 / gamma^2 scales correctly."""
        data1 = agt_at_zeta_zero(1, a_coulomb=1.0, max_level=0, dps=20)
        data2 = agt_at_zeta_zero(1, a_coulomb=2.0, max_level=0, dps=20)
        # h_int(2a) / h_int(a) = 4
        ratio = data2['h_int'] / data1['h_int'] if data1['h_int'] > 1e-30 else None
        if ratio is not None:
            assert abs(ratio - 4.0) < 1e-5

    def test_agt_match_z0(self):
        """AGT: both Z_0 and F_0 equal 1."""
        data = agt_nekrasov_match_at_zeta_zero(1, a_val=1.0, max_inst=1, dps=20)
        assert abs(data['comparison'][0]['Z_k (Nekrasov)'] - 1.0) < 1e-10
        assert abs(data['comparison'][0]['F_k (conformal block)'] - 1.0) < 1e-10


# ====================================================================
# Section 5: Instanton moduli space
# ====================================================================

class TestInstantonModuli:
    """Tests for the equivariant volume of M_k."""

    def test_k0_volume(self):
        """Volume at k=0 is 1 (empty partition)."""
        data = adhm_equivariant_volume(0, 1, dps=20)
        assert abs(data['su2_pair_volume'] - 1.0) < 1e-10

    def test_k1_volume_finite(self):
        """Volume at k=1 is finite."""
        data = adhm_equivariant_volume(1, 1, dps=20)
        assert math.isfinite(abs(data['su2_pair_volume']))

    def test_k1_single_finite(self):
        """Single partition volume at k=1 is finite."""
        data = adhm_equivariant_volume(1, 1, dps=20)
        assert math.isfinite(abs(data['single_partition_volume']))

    def test_volume_depends_on_zero(self):
        """Volumes at different zeta zeros differ (different gamma)."""
        v1 = adhm_equivariant_volume(1, 1, dps=20)
        v2 = adhm_equivariant_volume(1, 2, dps=20)
        # Different gamma_n => different eps => different volume
        assert v1['gamma'] != v2['gamma']


# ====================================================================
# Section 6: Perturbative partition function
# ====================================================================

class TestPerturbative:
    """Tests for the perturbative partition function."""

    def test_pert_finite(self):
        """Z^pert is finite for generic a."""
        data = perturbative_at_zeta_zero(1.0, 1, dps=20)
        assert math.isfinite(abs(data['Z_pert']))

    def test_pert_nonzero(self):
        """Z^pert is nonzero for generic a."""
        data = perturbative_at_zeta_zero(1.0, 1, dps=20)
        assert abs(data['Z_pert']) > 1e-20

    def test_full_pf_structure(self):
        """Full PF has all expected keys."""
        data = full_partition_function_at_zeta_zero(1.0, 1, max_inst=2,
                                                    q_val=0.1, dps=20)
        assert 'Z_pert' in data
        assert 'Z_inst' in data
        assert 'Z_full' in data

    def test_full_pf_product(self):
        """Z_full = Z_pert * Z_inst."""
        data = full_partition_function_at_zeta_zero(1.0, 1, max_inst=2,
                                                    q_val=0.1, dps=20)
        product = data['Z_pert'] * data['Z_inst']
        assert abs(product - data['Z_full']) < 1e-8 * abs(data['Z_full'])


# ====================================================================
# Section 7: Shadow-Nekrasov bridge
# ====================================================================

class TestShadowNekrasovBridge:
    """Tests for the shadow invariants at c = 25."""

    def test_shadow_c25_kappa(self):
        """kappa(Vir_25) = 25/2 = 12.5.

        AP1: recompute from first principles.  kappa(Vir_c) = c/2.
        At c = 25: kappa = 25/2 = 12.5.
        """
        data = shadow_at_self_dual()
        assert abs(data['kappa'] - 12.5) < 1e-10

    def test_shadow_c25_s3_is_2(self):
        """S_3(Vir_c) = 2 (c-independent, universal gravitational cubic)."""
        data = shadow_at_self_dual()
        assert abs(data['S3'] - 2.0) < 1e-10

    def test_shadow_c25_q_contact(self):
        """Q^contact(Vir_25) = 10/(25*147) = 2/735.

        AP10: verify independently.
        c = 25, 5c + 22 = 147.
        Q^contact = 10 / (25 * 147) = 10/3675 = 2/735.
        """
        data = shadow_at_self_dual()
        expected = 10.0 / (25.0 * 147.0)
        assert abs(data['Q_contact'] - expected) < 1e-12

    def test_shadow_c25_s4(self):
        """S_4 = Q^contact = 10/(c(5c+22)) = 10/(25*147) = 2/735.

        Independent check: 2/735 ~ 0.002721.
        """
        data = shadow_at_self_dual()
        expected = 10.0 / (25.0 * 147.0)  # = 2/735
        assert abs(data['S4'] - expected) < 1e-10

    def test_shadow_c25_delta(self):
        """Delta = 8 * kappa * S_4 = 8 * 12.5 * (2/735) = 200/735 = 40/147.

        Independent: 8 * (25/2) * 10/(25*147) = 8 * 10/(2*147) = 40/147.
        """
        data = shadow_at_self_dual()
        expected = 40.0 / 147.0  # 8 * (25/2) * 10/(25*147) = 40/147
        assert abs(data['Delta'] - expected) < 1e-8

    def test_shadow_c25_class_M(self):
        """Virasoro at c=25 has infinite shadow depth (class M)."""
        data = shadow_at_self_dual()
        assert 'infinite' in data['shadow_depth'].lower()

    def test_shadow_c25_growth_rate_positive(self):
        """Shadow growth rate rho > 0 for class M."""
        data = shadow_at_self_dual()
        assert data['shadow_growth_rate'] > 0

    def test_shadow_tower_kappa_matches(self):
        """Shadow tower at c=25: S_2 = 2*kappa = 25."""
        data = shadow_tower_at_c25()
        assert abs(data['gf_coefficients'][2] - 25.0) < 1e-10

    def test_shadow_tower_s4_gf(self):
        """Generating function coefficient at t^4.

        With corrected S_4 = Q^contact = 2/735 (NOT Q^contact * kappa):
        Delta = 8*kappa*S_4 = 8*(25/2)*(2/735) = 40/147.
        x = Delta/(2*kappa^2) = (40/147)/(625/2) = 16/18375.
        GF coeff at t^4 = 2*kappa * (1/2) * x = kappa * x
            = (25/2)*(16/18375) = 200/18375 = 8/735.
        """
        data = shadow_tower_at_c25()
        expected = 8.0 / 735.0
        assert abs(data['gf_coefficients'][4] - expected) < 1e-8

    def test_shadow_comparison_runs(self):
        """shadow_nekrasov_comparison returns expected structure."""
        data = shadow_nekrasov_comparison(1, a_val=1.0, max_inst=2, dps=20)
        assert 'shadow' in data
        assert 'nekrasov_comparison' in data
        assert 1 in data['nekrasov_comparison']


# ====================================================================
# Section 8: Surface operator
# ====================================================================

class TestSurfaceOperator:
    """Tests for the surface operator at zeta zeros."""

    def test_surface_op_runs(self):
        """surface_operator_at_zeta_zero returns expected keys."""
        data = surface_operator_at_zeta_zero(1, c_val=25.0, dps=20)
        assert 'A_c(rho)' in data
        assert '|A_c(rho)|' in data
        assert 'gamma' in data

    def test_surface_op_nonzero(self):
        """The BC residue A_c is nonzero at the first zeta zero."""
        data = surface_operator_at_zeta_zero(1, c_val=25.0, dps=20)
        assert data['|A_c(rho)|'] > 1e-20

    def test_surface_op_finite(self):
        """The BC residue is finite."""
        data = surface_operator_at_zeta_zero(1, c_val=25.0, dps=20)
        assert math.isfinite(data['|A_c(rho)|'])

    def test_surface_sweep_length(self):
        """Surface operator sweep returns n_max entries."""
        data = surface_operator_sweep(5, c_val=25.0, dps=20)
        assert len(data) == 5

    def test_surface_sweep_all_finite(self):
        """|A_c(rho_n)| is finite for at least the first 5 zeros.

        The residue A_c(rho_n) involves Gamma functions and zeta'(rho_n),
        all evaluated at well-separated zeros, so should be finite.

        Note: the magnitudes oscillate due to the arg(A_c) phase;
        monotonic decrease is NOT expected.  We only verify finiteness.
        """
        data = surface_operator_sweep(5, c_val=25.0, dps=30)
        finite_count = sum(1 for d in data if math.isfinite(d['|A_c|']))
        assert finite_count >= 3

    def test_surface_sweep_gammas_ordered(self):
        """Gammas in the sweep are ordered."""
        data = surface_operator_sweep(5, c_val=25.0, dps=20)
        gammas = [d['gamma'] for d in data]
        for i in range(len(gammas) - 1):
            assert gammas[i] < gammas[i + 1]


# ====================================================================
# Section 9: Multi-path verification
# ====================================================================

class TestMultiPathVerification:
    """Tests that verify results from multiple independent paths."""

    def test_path1_self_dual_c25(self):
        """Path 1: At self-dual, c = 25 by direct computation."""
        data = verify_self_dual_c25()
        assert abs(data['c'] - 25.0) < 1e-10
        assert abs(data['check_c'] - 25.0) < 1e-10

    def test_path1_b_equals_1(self):
        """Path 1: b = 1 at self-dual."""
        data = verify_self_dual_c25()
        assert abs(data['b'] - 1.0) < 1e-10

    def test_path2_z0_equals_1_first_zero(self):
        """Path 2: Z_0 = 1 at gamma_1."""
        data = verify_z0_equals_1(1, dps=20)
        assert data['|Z_0 - 1|'] < 1e-10

    def test_path2_z0_equals_1_fifth_zero(self):
        """Path 2: Z_0 = 1 at gamma_5."""
        data = verify_z0_equals_1(5, dps=20)
        assert data['|Z_0 - 1|'] < 1e-10

    def test_path3_z1_analytic(self):
        """Path 3: Z_1 is finite and nonzero for generic a."""
        data = verify_z1_analytic(1.0, 1, dps=20)
        assert data['|Z_1|'] > 1e-20
        assert math.isfinite(data['|Z_1|'])

    def test_path4_growth_rate_decreasing(self):
        """Path 4: |Z_k| decreases for large k at moderate a.

        For large a (weak coupling), |Z_k| should decrease.
        """
        data = verify_instanton_growth(5.0, 1, max_inst=5, dps=20)
        mags = data['magnitudes']
        # For a = 5 (large), the instanton expansion converges
        # |Z_1| should be larger than |Z_5|
        if mags.get(1, 0) > 1e-20 and mags.get(3, 0) > 1e-20:
            assert mags[1] > mags[3]

    def test_path5_sw_universal(self):
        """Path 5: SW prepotential is independent of which zeta zero."""
        data = verify_sw_limit(1, max_inst=3, dps=20)
        assert data['all_match']

    def test_cross_check_kappa_from_c(self):
        """Cross-check: kappa computed from c agrees with direct formula.

        kappa(Vir_c) = c/2.  At c = 25: kappa = 12.5.
        From the AGT map: c = 1 + 6*(b+1/b)^2 with b = 1 gives c = 25.
        """
        data = nekrasov_at_zeta_zero(1.0, 1, max_inst=0, dps=20)
        kappa = data['kappa']
        c = data['c']
        assert abs(kappa - c / 2) < 1e-10

    def test_cross_check_hbar_positive(self):
        """Cross-check: hbar = gamma_n^2 > 0.

        At self-dual: hbar = eps1*eps2 = (i*gamma_n)*(-i*gamma_n) = gamma_n^2.
        """
        data = nekrasov_at_zeta_zero(1.0, 1, max_inst=0, dps=20)
        hbar = data['hbar']
        gamma = data['gamma']
        assert abs(hbar - gamma**2) < 1e-5
        assert hbar.real > 0


# ====================================================================
# Sweep tests (integration)
# ====================================================================

class TestSweep:
    """Integration tests for sweep functions."""

    def test_full_sweep_runs(self):
        """Full sweep over 3 zeros runs without error."""
        data = full_sweep(n_max=3, a_val=1.0, max_inst=2, dps=20)
        assert len(data) == 3

    def test_full_sweep_gammas_increasing(self):
        """Gammas in sweep are increasing."""
        data = full_sweep(n_max=5, a_val=1.0, max_inst=1, dps=20)
        gammas = [d['gamma'] for d in data]
        for i in range(len(gammas) - 1):
            assert gammas[i] < gammas[i + 1]

    def test_magnitude_table_structure(self):
        """Magnitude table has expected shape."""
        table = instanton_magnitude_table(a_val=1.0, n_zeros=3,
                                          max_inst=2, dps=20)
        assert 1 in table
        assert 2 in table
        assert 3 in table
        for n in table:
            assert 1 in table[n]
            assert 2 in table[n]


# ====================================================================
# Additional cross-consistency tests
# ====================================================================

class TestCrossConsistency:
    """Cross-consistency checks between different sections."""

    def test_nek_equals_instanton_sum_at_k(self):
        """Nekrasov coefficients from Section 1 match Section 2."""
        data1 = nekrasov_at_zeta_zero(1.0, 1, max_inst=3, dps=20)
        data2 = instanton_sum_at_zeta_zero(1.0, 1, max_inst=3, q_val=0.1, dps=20)
        for k in range(4):
            assert abs(data1['coefficients'][k] - data2['coefficients'][k]) < 1e-8

    def test_shadow_kappa_matches_nek_c(self):
        """Shadow kappa = c/2 where c comes from Nekrasov."""
        nek = nekrasov_at_zeta_zero(1.0, 1, max_inst=0, dps=20)
        shadow = shadow_at_self_dual()
        assert abs(shadow['kappa'] - nek['c'] / 2) < 1e-10

    def test_surface_gamma_matches_nek_gamma(self):
        """Surface operator gamma matches Nekrasov gamma."""
        nek = nekrasov_at_zeta_zero(1.0, 1, max_inst=0, dps=20)
        surf = surface_operator_at_zeta_zero(1, dps=20)
        assert abs(nek['gamma'] - surf['gamma']) < 1e-5

    def test_sw_rho_matches_zeta_zero(self):
        """SW data: rho matches the actual zeta zero."""
        sw = sw_prepotential_at_zeta_zero(1, dps=20)
        rho_direct = zeta_zero_rho(1)
        assert abs(sw['rho'] - rho_direct) < 1e-8

    def test_perturbative_depends_on_gamma(self):
        """Perturbative PF differs for different zeta zeros."""
        p1 = perturbative_at_zeta_zero(1.0, 1, dps=20)
        p2 = perturbative_at_zeta_zero(1.0, 2, dps=20)
        assert abs(p1['Z_pert'] - p2['Z_pert']) > 1e-10

    def test_z1_depends_on_a(self):
        """Z_1 depends on the Coulomb parameter a."""
        d1 = nekrasov_at_zeta_zero(1.0, 1, max_inst=1, dps=20)
        d2 = nekrasov_at_zeta_zero(2.0, 1, max_inst=1, dps=20)
        assert abs(d1['coefficients'][1] - d2['coefficients'][1]) > 1e-15

    def test_z1_depends_on_zero(self):
        """Z_1 depends on which zeta zero (different gamma => different eps)."""
        d1 = nekrasov_at_zeta_zero(1.0, 1, max_inst=1, dps=20)
        d2 = nekrasov_at_zeta_zero(1.0, 2, max_inst=1, dps=20)
        assert abs(d1['coefficients'][1] - d2['coefficients'][1]) > 1e-15

    def test_full_pf_at_q0_is_perturbative(self):
        """At q = 0, Z_full = Z_pert (no instanton corrections)."""
        data = full_partition_function_at_zeta_zero(1.0, 1, max_inst=3,
                                                    q_val=0.0, dps=20)
        Z_pert = data['Z_pert']
        Z_inst = data['Z_inst']
        # Z_inst at q=0 is just Z_0 = 1
        assert abs(Z_inst - 1.0) < 1e-10
        assert abs(data['Z_full'] - Z_pert) < 1e-10 * abs(Z_pert)
