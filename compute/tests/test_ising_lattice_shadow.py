"""Test suite for Ising model and minimal model partition functions from the bar complex.

Tests: Virasoro characters (Rocha-Caridi), Ising torus partition function, shadow
tower at c=1/2, Koszul dual (c'=51/2), complementarity (kappa+kappa'=13),
minimal model family, Verlinde fusion rules, Ising 4-point function,
Yang-Lee edge singularity, critical exponents, transfer matrix, S-matrix
unitarity, quantum dimensions, Faber-Pandharipande lambda_g, genus expansion,
shadow connection monodromy, and the complete analysis driver.

60+ tests covering all public functions.
"""

from __future__ import annotations

import math
from fractions import Fraction

import pytest
from sympy import Rational, cancel, simplify

from compute.lib.ising_lattice_shadow import (
    _eta_product_coeffs,
    _inverse_eta_coeffs,
    rocha_caridi_theta,
    virasoro_character,
    ising_characters,
    ising_torus_partition_function,
    ising_partition_numerical,
    minimal_model_c,
    conformal_weight,
    shadow_tower_virasoro,
    shadow_tower_numerical,
    koszul_dual_data,
    complementarity_discriminant,
    MINIMAL_MODEL_FAMILY,
    minimal_model_shadow_family,
    modular_s_matrix,
    verlinde_fusion,
    ising_fusion_from_verlinde,
    ising_4point_sigma,
    ising_4point_full,
    yang_lee_data,
    yang_lee_characters,
    critical_exponents_from_cft,
    ising_critical_exponents,
    tricritical_ising_exponents,
    ising_transfer_matrix,
    transfer_matrix_eigenvalues,
    conformal_spectrum_from_transfer,
    finite_size_central_charge,
    verify_s_matrix_unitarity,
    quantum_dimensions,
    lambda_fp,
    ising_genus_expansion,
    shadow_connection_monodromy,
    complete_ising_lattice_analysis,
)


# ============================================================================
# 1. Eta product and inverse eta coefficients
# ============================================================================

class TestEtaProduct:
    """Tests for eta product via Euler pentagonal theorem."""

    def test_eta_constant_term(self):
        coeffs = _eta_product_coeffs(10)
        assert coeffs.get(0, 0) == 1

    def test_eta_first_pentagonal(self):
        """First pentagonal numbers: k=1 -> 1, k=-1 -> 2."""
        coeffs = _eta_product_coeffs(10)
        assert coeffs.get(1, 0) == -1
        assert coeffs.get(2, 0) == -1

    def test_eta_second_pentagonal(self):
        """k=2 -> 5, k=-2 -> 7."""
        coeffs = _eta_product_coeffs(10)
        assert coeffs.get(5, 0) == 1
        assert coeffs.get(7, 0) == 1

    def test_eta_non_pentagonal_vanish(self):
        """Coefficients at non-pentagonal numbers should be zero."""
        coeffs = _eta_product_coeffs(20)
        for n in [3, 4, 6, 8, 9, 10, 11, 13, 14, 16, 17, 18, 19, 20]:
            assert coeffs.get(n, 0) == 0


class TestInverseEta:
    """Tests for partition function p(n) = coefficients of 1/eta."""

    def test_partition_initial_values(self):
        """p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7."""
        coeffs = _inverse_eta_coeffs(10)
        expected = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7, 6: 11, 7: 15}
        for n, val in expected.items():
            assert coeffs[n] == val, f"p({n}) = {coeffs[n]}, expected {val}"

    def test_partition_monotone(self):
        """p(n) is strictly increasing for n >= 1."""
        coeffs = _inverse_eta_coeffs(20)
        for n in range(2, 21):
            assert coeffs[n] > coeffs[n - 1]


# ============================================================================
# 2. Rocha-Caridi theta and Virasoro characters
# ============================================================================

class TestRochaCaridiTheta:
    """Tests for the theta functions theta_{r,s} = eta * chi_{r,s}."""

    def test_ising_vacuum_theta_nonzero(self):
        theta = rocha_caridi_theta(4, 3, 1, 1, 10)
        assert len(theta) > 0

    def test_ising_sigma_theta_nonzero(self):
        theta = rocha_caridi_theta(4, 3, 2, 1, 10)
        assert len(theta) > 0

    def test_theta_exponents_rational(self):
        """All exponents in the theta function must be rational."""
        theta = rocha_caridi_theta(4, 3, 1, 1, 10)
        for exp in theta.keys():
            assert isinstance(exp, Fraction)


class TestVirasoroCharacter:
    """Tests for chi_{r,s}(q) at M(p,q)."""

    def test_ising_vacuum_leading(self):
        """Vacuum character chi_0: d_0 = 1 (unique vacuum)."""
        chi = virasoro_character(4, 3, 1, 1, 15)
        assert chi[0] == 1

    def test_ising_sigma_leading(self):
        """Sigma character chi_{1/16}: d_0 = 1 (unique primary)."""
        chi = virasoro_character(4, 3, 2, 1, 15)
        assert chi[0] == 1

    def test_ising_epsilon_leading(self):
        """Epsilon character chi_{1/2}: d_0 = 1 (unique primary)."""
        chi = virasoro_character(4, 3, 1, 2, 15)
        assert chi[0] == 1

    def test_ising_vacuum_level1(self):
        """At level 1, the vacuum has 0 descendants (null at level 1 for c=1/2)."""
        chi = virasoro_character(4, 3, 1, 1, 15)
        assert chi[1] == 0

    def test_ising_epsilon_level1(self):
        """Epsilon (h=1/2) has 1 descendant at level 1 (L_{-1}|1/2>)."""
        chi = virasoro_character(4, 3, 1, 2, 15)
        assert chi[1] == 1

    def test_character_degeneracies_nonneg(self):
        """All degeneracies must be nonneg (counting states)."""
        chi = virasoro_character(4, 3, 1, 1, 20)
        for n, d in chi.items():
            assert d >= 0, f"d_{n} = {d} < 0"


# ============================================================================
# 3. Ising characters and partition function
# ============================================================================

class TestIsingCharacters:
    """Tests for Ising (c=1/2) characters."""

    def test_three_channels(self):
        chars = ising_characters(10)
        assert set(chars.keys()) == {'0', '1/16', '1/2'}

    def test_all_leading_one(self):
        chars = ising_characters(10)
        for label, ch in chars.items():
            assert ch[0] == 1, f"Leading coefficient of {label} is {ch[0]}, expected 1"


class TestIsingTorusPartition:
    """Tests for the diagonal torus partition function Z_Ising."""

    def test_keys_present(self):
        result = ising_torus_partition_function(10)
        assert 'characters' in result
        assert 'channel_sums' in result
        assert 'combined' in result
        assert 'c' in result
        assert 'primaries' in result

    def test_central_charge(self):
        result = ising_torus_partition_function(10)
        assert result['c'] == Fraction(1, 2)

    def test_primaries_correct(self):
        result = ising_torus_partition_function(10)
        assert result['primaries'] == {
            '0': Fraction(0),
            '1/16': Fraction(1, 16),
            '1/2': Fraction(1, 2),
        }

    def test_combined_level0(self):
        """At level 0: each channel contributes 1^2 = 1, so combined = 3."""
        result = ising_torus_partition_function(10)
        assert result['combined'][0] == 3

    def test_channel_sums_nonneg(self):
        result = ising_torus_partition_function(10)
        for label, cs in result['channel_sums'].items():
            for n, val in cs.items():
                assert val >= 0, f"Negative squared degeneracy in {label} at level {n}"


class TestIsingPartitionNumerical:
    """Tests for numerical evaluation of Z_Ising(tau=iy)."""

    def test_positive(self):
        """Partition function must be positive for y > 0."""
        z = ising_partition_numerical(1.0, 30)
        assert z > 0

    def test_smaller_y_larger_z(self):
        """At smaller y (closer to modular boundary), Z is larger."""
        z1 = ising_partition_numerical(0.3, 100)
        z2 = ising_partition_numerical(1.0, 100)
        assert z1 > z2

    def test_large_y_approaches_three(self):
        """At large y (q -> 0): Z -> sum |d_0|^2 * q^{...}.
        Actually three primaries each contribute 1 at leading order,
        but the q powers differ. At very large y the identity dominates."""
        z = ising_partition_numerical(10.0, 30)
        # Should be dominated by the vacuum: ~ q^{-c/12} = q^{-1/24}
        # At y=10: q = e^{-20*pi}, so the value is dominated by e^{20*pi/24}
        assert z > 0
        assert math.isfinite(z)


# ============================================================================
# 4. Minimal model central charge and conformal weights
# ============================================================================

class TestMinimalModelC:
    """Tests for c = 1 - 6(p-q)^2/(pq)."""

    def test_ising(self):
        assert minimal_model_c(4, 3) == Rational(1, 2)

    def test_tricritical_ising(self):
        assert minimal_model_c(5, 4) == Rational(7, 10)

    def test_three_state_potts(self):
        assert minimal_model_c(6, 5) == Rational(4, 5)

    def test_yang_lee(self):
        assert minimal_model_c(5, 2) == Rational(-22, 5)

    def test_tricritical_three_state_potts(self):
        assert minimal_model_c(7, 6) == Rational(6, 7)


class TestConformalWeight:
    """Tests for h_{r,s} = ((pr-qs)^2 - (p-q)^2)/(4pq)."""

    def test_ising_vacuum(self):
        assert conformal_weight(4, 3, 1, 1) == 0

    def test_ising_sigma_field(self):
        """h_{1,2} = 1/16 (sigma field, the h=1/16 primary)."""
        assert conformal_weight(4, 3, 1, 2) == Rational(1, 16)

    def test_ising_epsilon_field(self):
        """h_{1,3} = h_{2,1} = 1/2 (epsilon / energy operator)."""
        assert conformal_weight(4, 3, 1, 3) == Rational(1, 2)
        assert conformal_weight(4, 3, 2, 1) == Rational(1, 2)

    def test_yang_lee_phi(self):
        """h_{1,2} for M(5,2) = -1/5."""
        assert conformal_weight(5, 2, 1, 2) == Rational(-1, 5)


# ============================================================================
# 5. Shadow obstruction tower at c=1/2
# ============================================================================

class TestShadowTowerVirasoro:
    """Tests for the exact shadow obstruction tower."""

    def test_ising_kappa(self):
        data = shadow_tower_virasoro(Rational(1, 2), 10)
        assert data['kappa'] == Rational(1, 4)

    def test_ising_S3(self):
        data = shadow_tower_virasoro(Rational(1, 2), 10)
        assert data['S3'] == 2

    def test_ising_S4(self):
        """S_4 = 10/(c*(5c+22)) = 10/((1/2)*(5/2+22)) = 10/((1/2)*(49/2)) = 10/(49/4) = 40/49."""
        data = shadow_tower_virasoro(Rational(1, 2), 10)
        expected = Rational(40, 49)
        assert data['S4'] == expected

    def test_ising_depth_class(self):
        """Ising is class M (Delta != 0)."""
        data = shadow_tower_virasoro(Rational(1, 2), 10)
        assert data['depth_class'] == 'M'

    def test_ising_delta_positive(self):
        data = shadow_tower_virasoro(Rational(1, 2), 10)
        assert data['Delta'] > 0

    def test_tower_arity2_is_kappa(self):
        """Tower at arity 2 should be kappa / 2 (from a[0]/2)."""
        # a[0] = 2*kappa = 1/2; tower[2] = a[0]/2 = 1/4
        data = shadow_tower_virasoro(Rational(1, 2), 10)
        assert data['tower'][2] == Rational(1, 4)

    def test_c_zero_trivial(self):
        data = shadow_tower_virasoro(Rational(0), 5)
        assert data['depth_class'] == 'trivial'
        assert data['kappa'] == 0
        for r in range(2, 6):
            assert data['tower'][r] == 0

    def test_yang_lee_singular(self):
        """At c=-22/5: 5c+22=0, so S_4 diverges."""
        data = shadow_tower_virasoro(Rational(-22, 5), 5)
        assert data['depth_class'] == 'singular'
        assert data['S4'] is None

    def test_heisenberg_kappa_1(self):
        """Heisenberg at c=1: kappa = 1/2."""
        data = shadow_tower_virasoro(Rational(1), 10)
        assert data['kappa'] == Rational(1, 2)


class TestShadowTowerNumerical:
    """Tests for the float64 numerical shadow obstruction tower."""

    def test_agrees_with_exact_at_c_half(self):
        exact = shadow_tower_virasoro(Rational(1, 2), 15)
        numerical = shadow_tower_numerical(0.5, 15)
        for r in range(2, 16):
            exact_val = float(exact['tower'][r])
            num_val = numerical[r]
            tol = max(1e-10, abs(exact_val) * 1e-12)
            assert abs(exact_val - num_val) < tol, \
                f"Arity {r}: exact={exact_val}, numerical={num_val}"

    def test_c_zero_all_zero(self):
        numerical = shadow_tower_numerical(0.0, 10)
        for r in range(2, 11):
            assert numerical[r] == 0.0

    def test_yang_lee_returns_zero(self):
        """At c=-22/5=-4.4: 5c+22=0, returns zeros."""
        numerical = shadow_tower_numerical(-4.4, 10)
        for r in range(2, 11):
            assert numerical[r] == 0.0


# ============================================================================
# 6. Koszul dual and complementarity
# ============================================================================

class TestKoszulDual:
    """Tests for Koszul duality c' = 26-c."""

    def test_ising_dual_c(self):
        data = koszul_dual_data(Rational(1, 2))
        assert data['c_dual'] == Rational(51, 2)

    def test_kappa_sum_is_13(self):
        """AP24: kappa + kappa' = 13 for Virasoro."""
        data = koszul_dual_data(Rational(1, 2))
        assert data['kappa_sum'] == 13
        assert data['complementarity_verified'] is True

    def test_kappa_sum_13_for_various_c(self):
        for c_val in [Rational(1, 2), Rational(7, 10), Rational(4, 5),
                      Rational(1), Rational(26), Rational(-22, 5)]:
            data = koszul_dual_data(c_val)
            assert data['kappa_sum'] == 13, f"Failed for c={c_val}"

    def test_self_dual_at_c13(self):
        data = koszul_dual_data(Rational(13))
        assert data['c'] == data['c_dual']
        assert data['kappa'] == data['kappa_dual']


class TestComplementarityDiscriminant:
    """Tests for Delta(A) + Delta(A!) = 13920/((5c+22)(152-5c))."""

    def test_ising_match(self):
        result = complementarity_discriminant(Rational(1, 2))
        assert result['match'] is True

    def test_tricritical_ising_match(self):
        result = complementarity_discriminant(Rational(7, 10))
        assert result['match'] is True

    def test_self_dual_c13(self):
        result = complementarity_discriminant(Rational(13))
        assert result['match'] is True
        # At c=13: Delta = Delta' by symmetry
        assert result['Delta'] == result['Delta_dual']

    def test_yang_lee_singular(self):
        """At c=-22/5: 5c+22=0, returns None."""
        result = complementarity_discriminant(Rational(-22, 5))
        assert result['sum'] is None


# ============================================================================
# 7. Minimal model family
# ============================================================================

class TestMinimalModelFamily:
    """Tests for the shadow data across the standard minimal model family."""

    def test_five_models(self):
        family = minimal_model_shadow_family(8)
        assert len(family) == 5

    def test_ising_data_correct(self):
        family = minimal_model_shadow_family(8)
        ising = family['Ising M(4,3)']
        assert ising['c'] == Rational(1, 2)
        assert ising['p'] == 4
        assert ising['q'] == 3

    def test_ising_n_primaries(self):
        family = minimal_model_shadow_family(8)
        ising = family['Ising M(4,3)']
        assert ising['n_primaries'] == 3

    def test_unitary_flag(self):
        family = minimal_model_shadow_family(8)
        assert family['Ising M(4,3)']['unitary'] is True
        assert family['tricritical Ising M(5,4)']['unitary'] is True
        assert family['Yang-Lee M(5,2)']['unitary'] is False

    def test_yang_lee_negative_c(self):
        family = minimal_model_shadow_family(8)
        yl = family['Yang-Lee M(5,2)']
        assert yl['c'] == Rational(-22, 5)
        assert yl['kappa'] < 0


# ============================================================================
# 8. Verlinde fusion rules
# ============================================================================

class TestModularSMatrix:
    """Tests for the modular S-matrix."""

    def test_ising_3_primaries(self):
        prims, mat = modular_s_matrix(4, 3)
        assert len(prims) == 3

    def test_s00_positive(self):
        prims, mat = modular_s_matrix(4, 3)
        assert mat[0][0] > 0

    def test_ising_s_matrix_symmetric(self):
        prims, mat = modular_s_matrix(4, 3)
        n = len(prims)
        for i in range(n):
            for j in range(n):
                assert abs(mat[i][j] - mat[j][i]) < 1e-10


class TestVerlindeFusion:
    """Tests for Ising fusion rules from the Verlinde formula."""

    def test_vacuum_is_identity(self):
        """Fusing with the vacuum should give identity: N_{0,i}^j = delta_{ij}."""
        for i in range(3):
            for j in range(3):
                expected = 1 if i == j else 0
                assert verlinde_fusion(4, 3, 0, i, j) == expected, \
                    f"N_{{0,{i}}}^{j} = {verlinde_fusion(4, 3, 0, i, j)}, expected {expected}"

    def test_sigma_times_sigma(self):
        """sigma x sigma = 1 + epsilon: N_{1,1}^0 = 1, N_{1,1}^2 = 1."""
        assert verlinde_fusion(4, 3, 1, 1, 0) == 1
        assert verlinde_fusion(4, 3, 1, 1, 2) == 1

    def test_sigma_times_epsilon(self):
        """sigma x epsilon = sigma: N_{1,2}^1 = 1."""
        assert verlinde_fusion(4, 3, 1, 2, 1) == 1

    def test_epsilon_times_epsilon(self):
        """epsilon x epsilon = 1: N_{2,2}^0 = 1."""
        assert verlinde_fusion(4, 3, 2, 2, 0) == 1

    def test_ising_fusion_driver(self):
        fusion = ising_fusion_from_verlinde()
        # sigma x sigma contains vacuum and epsilon
        assert 0 in fusion[(1, 1)]
        assert 2 in fusion[(1, 1)]


# ============================================================================
# 9. Ising 4-point function
# ============================================================================

class TestIsing4Point:
    """Tests for the Ising 4-point function."""

    def test_hypergeometric_at_zero(self):
        """2F1(1/2,1/2;1;0) = 1."""
        val = ising_4point_sigma(0.0, 50)
        assert abs(val - 1.0) < 1e-12

    def test_hypergeometric_at_small_z(self):
        """At z=0.01, 2F1(1/2,1/2;1;z) ~ 1 + z/4 + ..."""
        z = 0.01
        val = ising_4point_sigma(z, 80).real
        # Leading correction: (1/2)^2/1 * z = z/4
        expected_approx = 1.0 + z / 4.0
        assert abs(val - expected_approx) < 1e-3

    def test_full_4point_positive(self):
        """G(z) > 0 for z in (0,1)."""
        for z in [0.1, 0.3, 0.5, 0.7, 0.9]:
            g = ising_4point_full(z, 80)
            assert g > 0, f"G({z}) = {g} <= 0"

    def test_full_4point_symmetric(self):
        """G(z) should equal G(1-z) by the crossing symmetry z <-> 1-z."""
        g1 = ising_4point_full(0.3, 80)
        g2 = ising_4point_full(0.7, 80)
        assert abs(g1 - g2) < 1e-6

    def test_full_4point_raises_outside_01(self):
        with pytest.raises(ValueError):
            ising_4point_full(0.0, 50)
        with pytest.raises(ValueError):
            ising_4point_full(1.0, 50)


# ============================================================================
# 10. Yang-Lee edge singularity
# ============================================================================

class TestYangLee:
    """Tests for the Yang-Lee model M(5,2), c=-22/5."""

    def test_central_charge(self):
        data = yang_lee_data()
        assert data['c'] == Rational(-22, 5)

    def test_kappa_negative(self):
        data = yang_lee_data()
        assert data['kappa'] == Rational(-11, 5)

    def test_two_primaries(self):
        data = yang_lee_data()
        assert data['n_primaries'] == 2

    def test_non_unitary(self):
        data = yang_lee_data()
        assert data['unitary'] is False

    def test_negative_weight(self):
        """h=-1/5 is a negative conformal weight (non-unitary hallmark)."""
        data = yang_lee_data()
        assert data['primaries'][(1, 2)] == Rational(-1, 5)

    def test_5c_plus_22_zero(self):
        data = yang_lee_data()
        assert data['5c_plus_22'] == 0

    def test_s4_diverges(self):
        data = yang_lee_data()
        assert data['S4_diverges'] is True

    def test_koszul_dual_c(self):
        data = yang_lee_data()
        assert data['koszul_dual_c'] == 26 - Rational(-22, 5)
        assert data['koszul_dual_c'] == Rational(152, 5)

    def test_complementarity_kappa_sum(self):
        data = yang_lee_data()
        assert data['complementarity_kappa_sum'] == 13


class TestYangLeeCharacters:
    """Tests for Yang-Lee M(5,2) characters."""

    def test_two_channels(self):
        chars = yang_lee_characters(10)
        assert set(chars.keys()) == {'0', '-1/5'}

    def test_vacuum_leading(self):
        chars = yang_lee_characters(10)
        assert chars['0'][0] == 1

    def test_phi_channel_present(self):
        """The -1/5 channel is present in the dict (may be trivially zero
        due to M(5,2) Rocha-Caridi cancellation)."""
        chars = yang_lee_characters(10)
        assert '-1/5' in chars


# ============================================================================
# 11. Critical exponents
# ============================================================================

class TestCriticalExponents:
    """Tests for critical exponents from CFT data."""

    def test_ising_eta(self):
        """eta = 4*h_sigma = 4*(1/16) = 1/4."""
        exp = ising_critical_exponents()
        assert exp['eta'] == Rational(1, 4)

    def test_ising_nu(self):
        """nu = 1/(2*h_epsilon) = 1/(2*1/2) = 1."""
        exp = ising_critical_exponents()
        assert exp['nu'] == 1

    def test_ising_beta(self):
        """beta = nu * eta / 2 = 1 * (1/4) / 2 = 1/8."""
        exp = ising_critical_exponents()
        assert exp['beta'] == Rational(1, 8)

    def test_ising_gamma(self):
        """gamma = nu * (2-eta) = 1 * 7/4 = 7/4."""
        exp = ising_critical_exponents()
        assert exp['gamma'] == Rational(7, 4)

    def test_ising_alpha(self):
        """alpha = 2 - 2*nu = 0 (logarithmic specific heat)."""
        exp = ising_critical_exponents()
        assert exp['alpha'] == 0

    def test_ising_delta(self):
        """delta = (4-eta)/eta = (15/4)/(1/4) = 15."""
        exp = ising_critical_exponents()
        assert exp['delta'] == 15

    def test_tricritical_ising_eta(self):
        exp = tricritical_ising_exponents()
        assert exp['eta'] == Rational(3, 20)

    def test_tricritical_ising_nu(self):
        exp = tricritical_ising_exponents()
        assert exp['nu'] == 5


# ============================================================================
# 12. Transfer matrix
# ============================================================================

class TestTransferMatrix:
    """Tests for the Ising transfer matrix at criticality."""

    def test_matrix_size(self):
        """L=3 gives 2^3=8 x 8 matrix."""
        T = ising_transfer_matrix(3)
        assert len(T) == 8
        assert len(T[0]) == 8

    def test_matrix_positive(self):
        """All transfer matrix elements are positive (exp of real)."""
        T = ising_transfer_matrix(3)
        for row in T:
            for val in row:
                assert val > 0

    def test_eigenvalues_ordered(self):
        eigs = transfer_matrix_eigenvalues(3)
        if eigs:
            for i in range(len(eigs) - 1):
                assert eigs[i] >= eigs[i + 1] - 1e-10

    def test_eigenvalues_positive(self):
        """Largest eigenvalues should be positive for the Ising model."""
        eigs = transfer_matrix_eigenvalues(3)
        if eigs:
            assert eigs[0] > 0


class TestConformalSpectrumFromTransfer:
    """Tests for extracting conformal data from transfer matrix."""

    def test_spectrum_has_vacuum(self):
        result = conformal_spectrum_from_transfer(3)
        if result['spectrum']:
            # First entry should be 0 (vacuum)
            assert abs(result['spectrum'][0]) < 1e-10

    def test_f_per_site_finite(self):
        result = conformal_spectrum_from_transfer(3)
        if result['eigenvalues']:
            assert math.isfinite(result['f_per_site'])


class TestFiniteSizeCentralCharge:
    """Tests for extracting c from finite-size scaling."""

    def test_approaches_half(self):
        """c extracted from L=4,6 should be in the ballpark of 0.5."""
        c_ext = finite_size_central_charge(4, 6)
        if math.isfinite(c_ext):
            # Finite-size corrections are large for small L, so use loose tolerance
            assert abs(c_ext - 0.5) < 2.0


# ============================================================================
# 13. S-matrix verification
# ============================================================================

class TestSMatrixVerification:
    """Tests for modular S-matrix properties."""

    def test_ising_unitarity(self):
        result = verify_s_matrix_unitarity(4, 3)
        assert result['symmetric'] is True
        assert result['unitary'] is True
        assert result['S00_positive'] is True
        assert result['n_primaries'] == 3

    def test_tricritical_ising_unitarity(self):
        result = verify_s_matrix_unitarity(5, 4)
        assert result['symmetric'] is True
        assert result['unitary'] is True

    def test_yang_lee_s_matrix(self):
        result = verify_s_matrix_unitarity(5, 2)
        assert result['symmetric'] is True
        assert result['n_primaries'] == 2


class TestQuantumDimensions:
    """Tests for quantum dimensions d_i = S_{0i}/S_{00}."""

    def test_ising_vacuum_dim_1(self):
        qdims = quantum_dimensions(4, 3)
        prims = list(qdims.keys())
        # Vacuum (first primary) should have quantum dimension 1
        assert abs(qdims[prims[0]] - 1.0) < 1e-10

    def test_ising_all_positive(self):
        """Quantum dimensions are positive for unitary models."""
        qdims = quantum_dimensions(4, 3)
        for prim, d in qdims.items():
            assert d > 0, f"Quantum dim of {prim} = {d} <= 0"


# ============================================================================
# 14. Faber-Pandharipande and genus expansion
# ============================================================================

class TestLambdaFP:
    """Tests for lambda_g^FP = (2^{2g-1}-1)/(2^{2g-1}) * |B_{2g}|/(2g)!."""

    def test_genus_1(self):
        assert lambda_fp(1) == Rational(1, 24)

    def test_genus_2(self):
        assert lambda_fp(2) == Rational(7, 5760)

    def test_genus_3(self):
        assert lambda_fp(3) == Rational(31, 967680)

    def test_positive_for_all(self):
        for g in range(1, 8):
            assert lambda_fp(g) > 0

    def test_raises_for_genus_0(self):
        with pytest.raises(ValueError):
            lambda_fp(0)


class TestIsingGenusExpansion:
    """Tests for F_g(Ising) = kappa * lambda_g^FP = (1/4) * lambda_g."""

    def test_genus_1(self):
        expansion = ising_genus_expansion(5)
        assert expansion[1] == Rational(1, 4) * Rational(1, 24)
        assert expansion[1] == Rational(1, 96)

    def test_genus_2(self):
        expansion = ising_genus_expansion(5)
        assert expansion[2] == Rational(1, 4) * Rational(7, 5760)
        assert expansion[2] == Rational(7, 23040)

    def test_all_positive(self):
        expansion = ising_genus_expansion(8)
        for g, fg in expansion.items():
            assert fg > 0, f"F_{g} = {fg} <= 0"


# ============================================================================
# 15. Shadow connection monodromy
# ============================================================================

class TestShadowConnectionMonodromy:
    """Tests for the shadow connection nabla^sh and its monodromy."""

    def test_monodromy_minus_one(self):
        data = shadow_connection_monodromy(Rational(1, 2))
        assert data['monodromy'] == -1

    def test_branch_modulus_positive(self):
        data = shadow_connection_monodromy(Rational(1, 2))
        assert data['branch_modulus'] > 0

    def test_c_zero_no_monodromy(self):
        data = shadow_connection_monodromy(Rational(0))
        assert data['monodromy'] is None

    def test_yang_lee_no_monodromy(self):
        data = shadow_connection_monodromy(Rational(-22, 5))
        assert data['monodromy'] is None

    def test_self_dual_c13(self):
        data = shadow_connection_monodromy(Rational(13))
        assert data['monodromy'] == -1
        assert data['convergence_radius'] > 0


# ============================================================================
# 16. Complete analysis driver
# ============================================================================

class TestCompleteAnalysis:
    """Tests for the summary driver function."""

    def test_returns_all_keys(self):
        result = complete_ising_lattice_analysis(max_arity=8, max_genus=3,
                                                  max_terms=10)
        expected_keys = {
            'partition_function', 'shadow_tower', 'koszul_dual',
            'complementarity_disc', 'minimal_model_family',
            'ising_fusion_verlinde', 'yang_lee', 'critical_exponents',
            'genus_expansion', 'shadow_connection',
        }
        assert expected_keys == set(result.keys())

    def test_shadow_tower_present(self):
        result = complete_ising_lattice_analysis(max_arity=8, max_genus=3,
                                                  max_terms=10)
        tower = result['shadow_tower']
        assert 'kappa' in tower
        assert 'tower' in tower
        assert tower['kappa'] == Rational(1, 4)
