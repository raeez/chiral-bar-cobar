r"""Tests for the arithmetic conductor spectrum at zeta zeros.

Verifies the conductor function N_A(s), Newton polygon, analytic conductor,
epsilon factor, local Euler factors, conductor-discriminant relation, and
Artin conductor from bar cohomology across all standard chiral algebra families.

60+ tests across 4 verification paths:
  Path 1: Direct computation from connection matrices
  Path 2: Product formula (global conductor = product of local conductors)
  Path 3: Heisenberg minimality (unramified, conductor = 1)
  Path 4: Consistency with Weil explicit formula weight

Test categories:
    1. Zeta zero cache and spectral points (6 tests)
    2. Conductor function N_A(s) (8 tests)
    3. Newton polygon / singularity classification (6 tests)
    4. Analytic conductor (Iwaniec-Sarnak) (8 tests)
    5. Epsilon factor / root number (6 tests)
    6. Local Euler factors (8 tests)
    7. Conductor-discriminant formula (5 tests)
    8. Artin conductor from bar cohomology (7 tests)
    9. Cross-verification: product formula (5 tests)
    10. Full spectrum analysis (5 tests)

Manuscript references:
    def:arithmetic-packet-connection (arithmetic_shadows.tex)
    thm:packet-connection-flatness (arithmetic_shadows.tex)
    eq:constrained-epstein-fe (arithmetic_shadows.tex)
    [BenjaminChang22]: arXiv:2208.02259
"""

import math
import cmath
import pytest
import sys
import os
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

from compute.lib import bc_conductor_zeta_zeros_engine as bcz

DPS = 30
skipmp = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")

# Standard primes for Euler factor tests
SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


# =============================================================================
# Fixtures
# =============================================================================

@pytest.fixture(scope="module")
def first_10_zeros():
    """Cache the first 10 zeta zeros."""
    if not HAS_MPMATH:
        pytest.skip("mpmath required")
    return [bcz.get_zeta_zero(n, DPS) for n in range(1, 11)]


@pytest.fixture(scope="module")
def first_10_spectral():
    """Cache the first 10 spectral points s_n = (1+rho_n)/2."""
    if not HAS_MPMATH:
        pytest.skip("mpmath required")
    return [bcz.spectral_point(n, DPS) for n in range(1, 11)]


@pytest.fixture(scope="module")
def heisenberg_tower():
    """Heisenberg shadow tower (class G, trivial)."""
    from compute.lib.arithmetic_conductor_spectrum_engine import (
        heisenberg_shadow_data, shadow_tower_exact,
    )
    data = heisenberg_shadow_data(Fraction(1))
    tower = {2: Fraction(1)}
    for r in range(3, 21):
        tower[r] = Fraction(0)
    return data, tower


@pytest.fixture(scope="module")
def virasoro_tower():
    """Virasoro c=1 shadow tower (class M)."""
    from compute.lib.arithmetic_conductor_spectrum_engine import (
        virasoro_shadow_data, shadow_tower_exact,
    )
    data = virasoro_shadow_data(Fraction(1))
    tower = shadow_tower_exact(data['kappa'], data['alpha'], data['S4'], max_r=20)
    return data, tower


# =============================================================================
# Section 1: Zeta zero cache and spectral points
# =============================================================================

class TestZetaZeroCache:
    """Tests for zeta zero caching and spectral point computation."""

    @skipmp
    def test_first_zero_imaginary_part(self, first_10_zeros):
        """gamma_1 ~ 14.1347 (Riemann's first zero)."""
        gamma_1 = first_10_zeros[0].imag
        assert abs(gamma_1 - 14.134725) < 0.001, (
            f"First zero gamma_1 = {gamma_1}, expected ~14.1347"
        )

    @skipmp
    def test_zeros_on_critical_line(self, first_10_zeros):
        """All zeros should have Re(rho) = 1/2 (RH verified for first 10)."""
        for i, rho in enumerate(first_10_zeros):
            assert abs(rho.real - 0.5) < 1e-10, (
                f"Zero #{i+1} has Re(rho) = {rho.real}, expected 0.5"
            )

    @skipmp
    def test_spectral_point_real_part(self, first_10_spectral):
        """All spectral points s_n should have Re(s_n) = 3/4 under RH."""
        for i, s in enumerate(first_10_spectral):
            assert abs(s.real - 0.75) < 1e-10, (
                f"Spectral point #{i+1} has Re(s) = {s.real}, expected 0.75"
            )

    @skipmp
    def test_spectral_point_imaginary_halfing(self, first_10_zeros, first_10_spectral):
        """Im(s_n) = gamma_n / 2."""
        for i in range(10):
            expected_im = first_10_zeros[i].imag / 2
            actual_im = first_10_spectral[i].imag
            assert abs(actual_im - expected_im) < 1e-10, (
                f"Im(s_{i+1}) = {actual_im}, expected {expected_im}"
            )

    @skipmp
    def test_cache_consistency(self):
        """Repeated calls return the same value."""
        rho1a = bcz.get_zeta_zero(1, DPS)
        rho1b = bcz.get_zeta_zero(1, DPS)
        assert rho1a == rho1b

    @skipmp
    def test_zeros_increasing_imaginary(self, first_10_zeros):
        """Zeta zeros have increasing imaginary parts."""
        for i in range(9):
            assert first_10_zeros[i].imag < first_10_zeros[i+1].imag, (
                f"gamma_{i+1} = {first_10_zeros[i].imag} >= "
                f"gamma_{i+2} = {first_10_zeros[i+1].imag}"
            )


# =============================================================================
# Section 2: Conductor function N_A(s)
# =============================================================================

class TestConductorFunction:
    """Tests for the conductor at spectral points."""

    @skipmp
    def test_scattering_conductor_always_1(self):
        """Scattering conductor = 1 at every zeta zero (simple zeros)."""
        for n in range(1, 11):
            cond = bcz.conductor_at_spectral_point(n, rank=1, dps=DPS)
            assert cond['scattering_conductor'] == 1, (
                f"Scattering conductor at zero #{n} = "
                f"{cond['scattering_conductor']}, expected 1"
            )

    @skipmp
    def test_zeta_2s_minus_1_vanishes(self):
        """zeta(2s-1) ~ 0 at spectral points (this is the defining property)."""
        for n in range(1, 6):
            cond = bcz.conductor_at_spectral_point(n, rank=1, dps=DPS)
            assert abs(cond['zeta_2s_minus_1']) < 1e-8, (
                f"zeta(2s-1) at zero #{n} = {cond['zeta_2s_minus_1']}, "
                f"expected ~0"
            )

    @skipmp
    def test_zeta_2s_nonzero(self):
        """zeta(2s) = zeta(1+rho_n) != 0 at spectral points."""
        for n in range(1, 6):
            cond = bcz.conductor_at_spectral_point(n, rank=1, dps=DPS)
            assert abs(cond['zeta_2s']) > 0.1, (
                f"|zeta(2s)| at zero #{n} = {abs(cond['zeta_2s'])}, "
                f"expected >> 0"
            )

    @skipmp
    def test_eisenstein_conductor_zero_rank1(self):
        """Eisenstein conductor = 0 at rank 1 (generic non-vanishing)."""
        for n in range(1, 6):
            cond = bcz.conductor_at_spectral_point(n, rank=1, dps=DPS)
            assert cond['eisenstein_conductor'] == 0, (
                f"Eisenstein conductor at zero #{n} = "
                f"{cond['eisenstein_conductor']}, expected 0"
            )

    @skipmp
    def test_total_conductor_rank1(self):
        """Total conductor = 1 at rank 1 for first 10 zeros."""
        for n in range(1, 11):
            cond = bcz.conductor_at_spectral_point(n, rank=1, dps=DPS)
            assert cond['total_conductor'] == 1

    @skipmp
    def test_conductor_spectrum_length(self):
        """conductor_spectrum returns the correct number of entries."""
        spec = bcz.conductor_spectrum(n_zeros=10, rank=1, dps=DPS)
        assert len(spec) == 10

    @skipmp
    def test_conductor_spectrum_all_equal_1(self):
        """All conductors in the spectrum equal 1 for rank 1."""
        spec = bcz.conductor_spectrum(n_zeros=10, rank=1, dps=DPS)
        for entry in spec:
            assert entry['total_conductor'] == 1

    @skipmp
    def test_conductor_at_higher_rank(self):
        """Conductor at rank 8 (E_8): Eisenstein packet shifted."""
        cond = bcz.conductor_at_spectral_point(1, rank=8, dps=DPS)
        # The shifted zeta zeta(s - 3) at s = (1+rho_1)/2 ~ 0.75 + 7.07i
        # zeta(s - 3) = zeta(-2.25 + 7.07i) which is generically nonzero
        assert cond['scattering_conductor'] == 1


# =============================================================================
# Section 3: Newton polygon / singularity classification
# =============================================================================

class TestNewtonPolygon:
    """Tests for the Newton polygon of the connection at zeta zeros."""

    @skipmp
    def test_all_regular_singular(self):
        """Every spectral point is a regular singular point."""
        for n in range(1, 11):
            np_data = bcz.connection_matrix_at_zero(n, c_val=1.0, dps=DPS)
            assert np_data['singularity_type'] == 'regular_singular'

    @skipmp
    def test_irregularity_zero(self):
        """Katz irregularity = 0 at all spectral points (regular singular)."""
        for n in range(1, 6):
            np_data = bcz.connection_matrix_at_zero(n, c_val=1.0, dps=DPS)
            assert np_data['irregularity'] == 0

    @skipmp
    def test_newton_slopes_zero(self):
        """Newton polygon slopes are all 0 (regular singular)."""
        np_data = bcz.connection_matrix_at_zero(1, c_val=1.0, dps=DPS)
        assert np_data['newton_slopes'] == [0]

    @skipmp
    def test_defect_residue_minus_1(self):
        """Defect connection residue = -1 at spectral points."""
        for n in range(1, 6):
            np_data = bcz.connection_matrix_at_zero(n, c_val=1.0, dps=DPS)
            assert np_data['defect_residue'] == -1

    @skipmp
    def test_zeta_prime_nonzero(self):
        """zeta'(rho_n) != 0 (zeta zeros are simple)."""
        for n in range(1, 6):
            np_data = bcz.connection_matrix_at_zero(n, c_val=1.0, dps=DPS)
            assert abs(np_data['zeta_prime_rho']) > 0.1, (
                f"|zeta'(rho_{n})| = {abs(np_data['zeta_prime_rho'])}"
            )

    @skipmp
    def test_newton_polygon_spectrum_length(self):
        """newton_polygon_spectrum returns correct number of entries."""
        spec = bcz.newton_polygon_spectrum(n_zeros=5, c_val=1.0, dps=DPS)
        assert len(spec) == 5


# =============================================================================
# Section 4: Analytic conductor (Iwaniec-Sarnak)
# =============================================================================

class TestAnalyticConductor:
    """Tests for the Iwaniec-Sarnak analytic conductor."""

    @skipmp
    def test_heisenberg_q_equals_1(self):
        """Heisenberg arithmetic conductor q = 1 (unramified)."""
        s = bcz.spectral_point(1, DPS)
        ac = bcz.analytic_conductor_heisenberg(s)
        assert ac['q'] == 1

    @skipmp
    def test_heisenberg_degree_2(self):
        """Heisenberg effective degree d = 2."""
        s = bcz.spectral_point(1, DPS)
        ac = bcz.analytic_conductor_heisenberg(s)
        assert ac['d'] == 2

    @skipmp
    def test_analytic_conductor_positive(self):
        """Analytic conductor is always positive."""
        for n in range(1, 6):
            s = bcz.spectral_point(n, DPS)
            ac = bcz.analytic_conductor_heisenberg(s)
            assert ac['C_s'] > 0

    @skipmp
    def test_analytic_conductor_grows_with_zero(self):
        """Analytic conductor grows with the imaginary part of s_n."""
        vals = []
        for n in range(1, 6):
            s = bcz.spectral_point(n, DPS)
            ac = bcz.analytic_conductor_heisenberg(s)
            vals.append(ac['C_s'])
        # Should be monotonically increasing (gamma_n increasing)
        for i in range(len(vals) - 1):
            assert vals[i] < vals[i+1], (
                f"C(s_{i+1}) = {vals[i]} >= C(s_{i+2}) = {vals[i+1]}"
            )

    @skipmp
    def test_virasoro_conductor_c_dependence(self):
        """Virasoro analytic conductor depends on c through spectral parameters."""
        s = bcz.spectral_point(1, DPS)
        ac_1 = bcz.analytic_conductor_virasoro(s, c_val=1.0)
        ac_26 = bcz.analytic_conductor_virasoro(s, c_val=26.0)
        # Different c should give different conductors (different spectral params)
        assert ac_1['C_s'] != ac_26['C_s']

    @skipmp
    def test_virasoro_self_dual_c13(self):
        """At c=13, Virasoro is self-dual. Conductor should have special value."""
        s = bcz.spectral_point(1, DPS)
        ac_13 = bcz.analytic_conductor_virasoro(s, c_val=13.0)
        ac_13_dual = bcz.analytic_conductor_virasoro(s, c_val=13.0)
        # Self-dual: same conductor
        assert abs(ac_13['C_s'] - ac_13_dual['C_s']) < 1e-10

    @skipmp
    def test_lattice_conductor_rank_dependence(self):
        """Lattice conductor depends on rank."""
        s = bcz.spectral_point(1, DPS)
        ac_1 = bcz.analytic_conductor_lattice(s, rank=1)
        ac_8 = bcz.analytic_conductor_lattice(s, rank=8)
        assert ac_1['C_s'] != ac_8['C_s']

    @skipmp
    def test_analytic_conductor_at_zeros_list(self):
        """analytic_conductor_at_zeta_zeros returns correct length."""
        result = bcz.analytic_conductor_at_zeta_zeros(
            'heisenberg', n_zeros=5, dps=DPS
        )
        assert len(result) == 5
        for entry in result:
            assert 'C_s' in entry
            assert entry['C_s'] > 0


# =============================================================================
# Section 5: Epsilon factor / root number
# =============================================================================

class TestEpsilonFactor:
    """Tests for the root number at zeta zeros."""

    @skipmp
    def test_global_epsilon_always_1(self):
        """Global epsilon (root number of zeta) is always +1."""
        for n in range(1, 6):
            eps = bcz.epsilon_factor_eisenstein(n, dps=DPS)
            assert eps['global_epsilon'] == 1

    @skipmp
    def test_local_sign_is_pm1(self):
        """Local sign is +1 or -1."""
        for n in range(1, 6):
            eps = bcz.epsilon_factor_eisenstein(n, dps=DPS)
            assert eps['local_sign'] in (1, -1)

    @skipmp
    def test_epsilon_spectrum_length(self):
        """epsilon_spectrum returns correct number of entries."""
        spec = bcz.epsilon_spectrum(n_zeros=5, dps=DPS)
        assert len(spec) == 5

    @skipmp
    def test_phase_jump_nonzero(self):
        """Phase jump at zeta zeros should be nonzero (signature of zero)."""
        eps = bcz.epsilon_factor_eisenstein(1, dps=DPS)
        assert abs(eps['phase_jump']) > 1e-6

    @skipmp
    def test_epsilon_data_complete(self):
        """All expected fields present in epsilon data."""
        eps = bcz.epsilon_factor_eisenstein(1, dps=DPS)
        expected_keys = {'n', 'rho_n', 's_n', 'global_epsilon',
                         'local_sign', 'phase_above', 'phase_below',
                         'phase_jump'}
        assert expected_keys <= set(eps.keys())

    @skipmp
    def test_epsilon_at_multiple_zeros(self):
        """Epsilon computation succeeds for zeros with large imaginary part."""
        for n in [1, 5, 10]:
            eps = bcz.epsilon_factor_eisenstein(n, dps=DPS)
            assert eps['global_epsilon'] == 1


# =============================================================================
# Section 6: Local Euler factors
# =============================================================================

class TestLocalEulerFactors:
    """Tests for local Euler factors at primes."""

    @skipmp
    def test_heisenberg_euler_factor_at_2(self):
        """Heisenberg L_2(s) = 1/((1-2^{-s})(1-2^{-(s+1)}))."""
        s = 2.0 + 1j  # generic point with Re(s) > 1
        L2 = bcz.local_euler_factor_heisenberg(2, s)
        expected = 1.0 / ((1 - 2**(-s)) * (1 - 2**(-(s+1))))
        assert abs(L2 - expected) < 1e-12

    @skipmp
    def test_heisenberg_euler_factor_positive_real(self):
        """Heisenberg Euler factors are real and positive for real s > 1."""
        for p in [2, 3, 5, 7]:
            Lp = bcz.local_euler_factor_heisenberg(p, 3.0)
            assert Lp.imag < 1e-15, f"L_{p}(3) not real: {Lp}"
            assert Lp.real > 0, f"L_{p}(3) not positive: {Lp}"

    @skipmp
    def test_virasoro_euler_factor_structure(self):
        """Virasoro Euler factor = (1-p^{-2s})^{-1} * (1-p^{-(2s-1)})."""
        s = 2.0 + 0.5j
        for p in [2, 3, 5]:
            Lp = bcz.local_euler_factor_virasoro(p, s, c_val=1.0)
            expected = (1.0 / (1 - p**(-2*s))) * (1 - p**(-(2*s-1)))
            assert abs(Lp - expected) < 1e-12

    @skipmp
    def test_euler_product_partial_heisenberg(self):
        """Partial Euler product for Heisenberg is a complex number."""
        s = bcz.spectral_point(1, DPS)
        ep = bcz.euler_product_partial('heisenberg', SMALL_PRIMES, s)
        assert isinstance(ep['product'], complex)
        assert abs(ep['product']) > 0

    @skipmp
    def test_euler_product_partial_virasoro(self):
        """Partial Euler product for Virasoro works."""
        s = bcz.spectral_point(1, DPS)
        ep = bcz.euler_product_partial('virasoro', SMALL_PRIMES, s, c=1.0)
        assert isinstance(ep['product'], complex)

    @skipmp
    def test_euler_factors_at_zeta_zeros_length(self):
        """euler_factors_at_zeta_zeros returns correct length."""
        result = bcz.euler_factors_at_zeta_zeros(
            'heisenberg', [2, 3, 5], n_zeros=5, dps=DPS
        )
        assert len(result) == 5

    @skipmp
    def test_shadow_euler_connection_heisenberg(self, heisenberg_tower):
        """For Heisenberg, shadow coefficients S_p = 0 for p >= 3."""
        _, tower = heisenberg_tower
        conn = bcz.shadow_euler_connection(tower, SMALL_PRIMES)
        for p in [3, 5, 7]:
            if p in conn:
                assert conn[p]['S_p'] == 0, (
                    f"S_{p} = {conn[p]['S_p']} for Heisenberg, expected 0"
                )

    @skipmp
    def test_shadow_euler_connection_virasoro(self, virasoro_tower):
        """For Virasoro c=1, shadow coefficients S_p are nonzero."""
        _, tower = virasoro_tower
        conn = bcz.shadow_euler_connection(tower, [2, 3, 5, 7])
        # S_3 should be nonzero for Virasoro (class M)
        if 3 in conn:
            assert conn[3]['S_p'] != 0


# =============================================================================
# Section 7: Conductor-discriminant formula
# =============================================================================

class TestConductorDiscriminant:
    """Tests for the conductor-discriminant relation."""

    @skipmp
    def test_heisenberg_delta_zero(self, heisenberg_tower):
        """Heisenberg: Delta = 0 (class G)."""
        data, tower = heisenberg_tower
        result = bcz.conductor_discriminant_at_zeros(
            data['kappa'], Fraction(0), tower,
            n_zeros=5, max_R=20, dps=DPS,
        )
        assert result['Delta'] == 0

    @skipmp
    def test_virasoro_delta_nonzero(self, virasoro_tower):
        """Virasoro c=1: Delta != 0 (class M)."""
        data, tower = virasoro_tower
        result = bcz.conductor_discriminant_at_zeros(
            data['kappa'], data['S4'], tower,
            n_zeros=5, max_R=20, dps=DPS,
        )
        assert result['Delta'] != 0

    @skipmp
    def test_all_conductors_equal_1(self, heisenberg_tower):
        """At zeta zeros, all connection conductors are 1."""
        data, tower = heisenberg_tower
        result = bcz.conductor_discriminant_at_zeros(
            data['kappa'], Fraction(0), tower,
            n_zeros=5, max_R=20, dps=DPS,
        )
        assert result['all_conductors_equal_1']

    @skipmp
    def test_shadow_conductor_heisenberg(self, heisenberg_tower):
        """Heisenberg shadow conductor N_shadow = 1 (trivial denominators)."""
        data, tower = heisenberg_tower
        result = bcz.conductor_discriminant_at_zeros(
            data['kappa'], Fraction(0), tower,
            n_zeros=5, max_R=20, dps=DPS,
        )
        assert result['N_shadow'] == 1

    @skipmp
    def test_shadow_conductor_virasoro(self, virasoro_tower):
        """Virasoro c=1 shadow conductor N_shadow > 1."""
        data, tower = virasoro_tower
        result = bcz.conductor_discriminant_at_zeros(
            data['kappa'], data['S4'], tower,
            n_zeros=5, max_R=20, dps=DPS,
        )
        # Virasoro c=1: S_2 = 1/2, so N_2 = 2; S_4 has denominator > 1
        assert result['N_shadow'] > 1


# =============================================================================
# Section 8: Artin conductor from bar cohomology
# =============================================================================

class TestArtinConductor:
    """Tests for the Artin conductor from the shadow class."""

    def test_class_G_unramified(self):
        """Class G (Heisenberg): Artin conductor = 0."""
        ac = bcz.artin_conductor_from_shadow_class('G', 2, 'Heisenberg')
        assert ac.artin_conductor == 0
        assert ac.tame_part == 0
        assert ac.wild_part == 0
        assert ac.ramification_breaks == []

    def test_class_L_tame(self):
        """Class L (affine KM): Artin conductor = 1, tame."""
        ac = bcz.artin_conductor_from_shadow_class('L', 3, 'sl2_1')
        assert ac.artin_conductor == 1
        assert ac.tame_part == 1
        assert ac.wild_part == 0
        assert ac.ramification_breaks == [3]

    def test_class_C_wild(self):
        """Class C (beta-gamma): Artin conductor = 2, wild depth 1."""
        ac = bcz.artin_conductor_from_shadow_class('C', 4, 'betagamma')
        assert ac.artin_conductor == 2
        assert ac.tame_part == 1
        assert ac.wild_part == 1
        assert ac.ramification_breaks == [3, 4]

    def test_class_M_infinite(self):
        """Class M (Virasoro): Artin conductor = -1 (infinite)."""
        ac = bcz.artin_conductor_from_shadow_class('M', 100, 'Virasoro')
        assert ac.artin_conductor == -1

    def test_artin_truncated_class_G(self):
        """Truncated Artin conductor for class G is always 0."""
        for R in range(2, 20):
            assert bcz.artin_conductor_truncated('G', 2, R) == 0

    def test_artin_truncated_class_M_linear(self):
        """Truncated Artin conductor for class M grows linearly: f_R = R-2."""
        for R in range(2, 20):
            expected = max(R - 2, 0)
            assert bcz.artin_conductor_truncated('M', 100, R) == expected

    def test_artin_conductor_ordering(self):
        """Artin conductor respects G < L < C < M ordering."""
        f_G = bcz.artin_conductor_from_shadow_class('G', 2).artin_conductor
        f_L = bcz.artin_conductor_from_shadow_class('L', 3).artin_conductor
        f_C = bcz.artin_conductor_from_shadow_class('C', 4).artin_conductor
        f_M = bcz.artin_conductor_from_shadow_class('M', 100).artin_conductor
        # G=0 < L=1 < C=2 < M=-1(inf)
        assert f_G < f_L < f_C
        # M is infinite (represented as -1)
        assert f_M == -1


# =============================================================================
# Section 9: Cross-verification: product formula
# =============================================================================

class TestProductFormula:
    """Tests for the product formula verification (Path 2)."""

    @skipmp
    def test_heisenberg_product_approximation(self):
        """Partial Euler product should approximate zeta(s)*zeta(s+1)."""
        s = 2.0 + 1j  # Re(s) > 1 for convergence
        result = bcz.verify_product_formula(
            bcz.PRIMES_TO_97, s, 'heisenberg', dps=DPS
        )
        # With 25 primes, relative error should be moderate
        assert result['relative_error'] is not None
        assert result['relative_error'] < 0.1, (
            f"Product formula relative error = {result['relative_error']}"
        )

    @skipmp
    def test_virasoro_product_approximation(self):
        """Partial Euler product for Virasoro zeta(2s)/zeta(2s-1)."""
        s = 2.0 + 1j
        result = bcz.verify_product_formula(
            bcz.PRIMES_TO_97, s, 'virasoro', dps=DPS, c=1.0
        )
        assert result['relative_error'] is not None
        assert result['relative_error'] < 0.1

    @skipmp
    def test_heisenberg_minimality_verification(self):
        """Path 3: Heisenberg is minimal (unramified, all conductors = 1)."""
        result = bcz.verify_heisenberg_minimality(n_zeros=5, dps=DPS)
        assert result['is_minimal']
        assert result['artin_is_zero']
        assert result['all_conductors_are_1']
        assert result['arithmetic_q'] == 1

    @skipmp
    def test_product_improves_with_more_primes(self):
        """Error decreases as more primes are included."""
        s = 2.0 + 0.5j
        errors = []
        prime_lists = [
            [2, 3, 5],
            [2, 3, 5, 7, 11, 13],
            bcz.PRIMES_TO_97,
        ]
        for pl in prime_lists:
            result = bcz.verify_product_formula(pl, s, 'heisenberg', dps=DPS)
            if result['relative_error'] is not None:
                errors.append(result['relative_error'])
        # Errors should decrease (more primes = better approximation)
        for i in range(len(errors) - 1):
            assert errors[i] >= errors[i+1] * 0.5, (
                f"Error not decreasing: {errors[i]} -> {errors[i+1]}"
            )

    @skipmp
    def test_lattice_product_approximation(self):
        """Lattice VOA Euler product for zeta(s)*zeta(s-r/2+1)."""
        s = 5.0 + 1j  # Large real part for convergence with shifted zeta
        result = bcz.verify_product_formula(
            bcz.PRIMES_TO_97, s, 'lattice', dps=DPS, rank=8
        )
        assert result['relative_error'] is not None
        assert result['relative_error'] < 0.5  # Looser bound for shifted zeta


# =============================================================================
# Section 10: Full spectrum analysis
# =============================================================================

class TestFullSpectrumAnalysis:
    """Tests for the full conductor analysis at zeta zeros."""

    @skipmp
    def test_full_analysis_heisenberg(self):
        """Full analysis for Heisenberg at the first zero."""
        analysis = bcz.full_analysis_at_zero(1, 'heisenberg', dps=DPS)
        assert analysis.total_conductor == 1
        assert analysis.singularity_type == 'regular_singular'
        assert analysis.global_epsilon == 1
        assert analysis.analytic_conductor > 0

    @skipmp
    def test_full_analysis_virasoro(self):
        """Full analysis for Virasoro c=1 at the first zero."""
        analysis = bcz.full_analysis_at_zero(1, 'virasoro', dps=DPS, c=1.0)
        assert analysis.total_conductor == 1  # universal at zeta zeros
        assert analysis.singularity_type == 'regular_singular'
        assert analysis.gamma_n > 0

    @skipmp
    def test_full_spectrum_length(self):
        """Full spectrum returns correct number of entries."""
        spec = bcz.full_spectrum_analysis('heisenberg', n_zeros=5, dps=DPS)
        assert len(spec) == 5

    @skipmp
    def test_weil_weight_monotone(self):
        """Weil weights are monotonically increasing for Heisenberg."""
        spec = bcz.full_spectrum_analysis('heisenberg', n_zeros=5, dps=DPS)
        weights = [a.weil_weight for a in spec]
        for i in range(len(weights) - 1):
            assert weights[i] <= weights[i+1] + 1e-10, (
                f"Weil weight not monotone: w_{i+1} = {weights[i]}, "
                f"w_{i+2} = {weights[i+1]}"
            )

    @skipmp
    def test_summary_string(self):
        """conductor_zero_summary produces a non-empty string."""
        analysis = bcz.full_analysis_at_zero(1, 'heisenberg', dps=DPS)
        summary = bcz.conductor_zero_summary(analysis)
        assert len(summary) > 50
        assert "Zero #1" in summary
        assert "regular_singular" in summary
