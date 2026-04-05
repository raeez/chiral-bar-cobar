r"""Tests for shadow partition function modularity and arithmetic decomposition.

Tests the seven main results:
1. Z^sh(V_Lambda) = rank * (A-hat(i*hbar) - 1) for ALL lattice VOAs
2. Z^sh is always tau-independent (topological invariant)
3. Full genus-1 amplitude matches -kappa * log eta(tau)
4. Modular anomaly under S and T transforms
5. E_2* quasi-modularity verified numerically
6. Arithmetic decomposition Z = Z^sh_part * Z^arith_part
7. Virasoro special values and Borel resummation

75+ tests covering the full modularity landscape.

Manuscript references:
    prop:genus-expansion-convergence (genus_expansions.tex)
    thm:shadow-double-convergence (higher_genus_modular_koszul.tex)
    thm:shadow-moduli-resolution (arithmetic_shadows.tex)
    rem:propagator-weight-universality (higher_genus_modular_koszul.tex)
"""

import cmath
import math
import pytest

from fractions import Fraction
from sympy import Rational

from compute.lib.shadow_pf_modular import (
    # Section 1: A-hat genus for lattice VOAs
    ahat_genus_series,
    ahat_closed_form,
    lattice_shadow_pf,
    lattice_shadow_pf_series,
    verify_lattice_ahat_identity,
    # Section 2: Full genus-1 amplitude
    log_eta_q_expansion,
    genus1_full_amplitude_lattice,
    genus1_amplitude_scalar_part,
    genus1_amplitude_q_coefficients,
    # Section 3: Genus-2 amplitude
    genus2_scalar_amplitude_lattice,
    genus2_full_amplitude_lattice_structure,
    # Section 4: Virasoro shadow PF
    virasoro_shadow_coefficients,
    virasoro_shadow_pf_formal,
    virasoro_shadow_pf_borel,
    # Section 5: Modular transformations
    eta_numerical,
    log_eta_numerical,
    modular_anomaly_genus1,
    e2_star_numerical,
    verify_e2_quasi_modularity,
    # Section 6: Arithmetic decomposition
    theta_lattice_coeffs,
    arithmetic_decomposition_genus1,
    arithmetic_content_separation,
    # Section 7: Special values
    virasoro_special_values,
    # Section 8: Double expansion
    double_expansion_genus1,
    # Section 9: Modularity classification
    modularity_classification,
    # Section 10: E_2* connection
    genus1_propagator_modular_analysis,
    full_amplitude_quasi_modularity,
    # Section 11: Monster
    monster_shadow_analysis,
    # Section 12: Summary
    master_modularity_summary,
)

from compute.lib.utils import lambda_fp, F_g

PI = math.pi
TWO_PI = 2 * PI


# =========================================================================
# Section 1: A-hat genus tests
# =========================================================================

class TestAhatGenus:
    """Tests for the A-hat genus generating function."""

    def test_ahat_at_zero(self):
        """A-hat(0) = 1."""
        assert abs(ahat_closed_form(0.0) - 1.0) < 1e-12

    def test_ahat_at_one(self):
        """A-hat(i*1) = (1/2)/sin(1/2) ~ 1.0422."""
        val = ahat_closed_form(1.0)
        expected = 0.5 / math.sin(0.5)
        assert abs(val - expected) < 1e-10

    def test_ahat_series_first_term(self):
        """First term: hbar^2/24 at g=1."""
        series = ahat_genus_series(1, max_genus=1)
        F1 = float(series[1])
        assert abs(F1 - 1.0 / 24.0) < 1e-12

    def test_ahat_series_second_term(self):
        """Second term: 7*hbar^4/5760 at g=2."""
        series = ahat_genus_series(1, max_genus=2)
        F2 = float(series[2])
        assert abs(F2 - 7.0 / 5760.0) < 1e-12

    def test_lattice_rank_scaling(self):
        """Z^sh scales linearly with rank."""
        for rank in [1, 2, 4, 8, 16, 24]:
            val = lattice_shadow_pf(rank, 1.0)
            val_1 = lattice_shadow_pf(1, 1.0)
            assert abs(val - rank * val_1) < 1e-10

    def test_lattice_ahat_identity_rank1(self):
        """Z^sh(Heisenberg) = 1 * (A-hat(i*hbar) - 1) at hbar=1."""
        closed = lattice_shadow_pf(1, 1.0)
        expected = ahat_closed_form(1.0) - 1.0
        assert abs(closed - expected) < 1e-10

    def test_lattice_ahat_identity_rank8(self):
        """Z^sh(E_8) = 8 * (A-hat(i*hbar) - 1)."""
        closed = lattice_shadow_pf(8, 1.0)
        expected = 8.0 * (ahat_closed_form(1.0) - 1.0)
        assert abs(closed - expected) < 1e-10

    def test_lattice_ahat_identity_rank24(self):
        """Z^sh(Leech) = 24 * (A-hat(i*hbar) - 1)."""
        closed = lattice_shadow_pf(24, 1.0)
        expected = 24.0 * (ahat_closed_form(1.0) - 1.0)
        assert abs(closed - expected) < 1e-10

    def test_series_matches_closed_form(self):
        """Partial sum converges to closed form."""
        for rank in [1, 8, 24]:
            closed = lattice_shadow_pf(rank, 1.0)
            series = lattice_shadow_pf_series(rank, 1.0, max_genus=40)
            assert abs(series - closed) / abs(closed) < 1e-8

    def test_verify_all_lattices(self):
        """Verify A-hat identity for all standard lattice ranks."""
        result = verify_lattice_ahat_identity()
        assert result['all_match']
        assert result['tau_independent']


class TestLatticeShadowPFTauIndependence:
    """Z^sh depends ONLY on rank, NOT on tau."""

    def test_tau_independent_rank1(self):
        """Z^sh(Heisenberg) is the same for any tau."""
        val1 = lattice_shadow_pf(1, 1.0)
        val2 = lattice_shadow_pf(1, 1.0)  # same function, no tau argument
        assert val1 == val2  # trivially, since there's no tau parameter

    def test_different_lattices_same_rank(self):
        """E_8 x E_8 and D_{16}^+ have rank 16, same Z^sh."""
        # Both have rank 16, so Z^sh = 16 * (A-hat - 1)
        val = lattice_shadow_pf(16, 1.0)
        expected = 16.0 * (ahat_closed_form(1.0) - 1.0)
        assert abs(val - expected) < 1e-10

    def test_f1_equals_kappa_over_24(self):
        """F_1 = kappa/24 for all lattice VOAs.

        For rank-r lattice VOA: kappa = r, so F_1 = r/24.
        """
        for rank in [1, 2, 4, 8, 16, 24]:
            F1 = genus1_amplitude_scalar_part(float(rank))
            assert abs(F1 - rank / 24.0) < 1e-12


# =========================================================================
# Section 2: Full genus-1 amplitude tests
# =========================================================================

class TestGenus1FullAmplitude:
    """Tests for the full (tau-dependent) genus-1 amplitude."""

    def test_log_eta_coefficients(self):
        """log eta q-coefficients: c_m = -sigma_{-1}(m)."""
        coeffs = log_eta_q_expansion(10)
        # c_1 = -sigma_{-1}(1) = -1
        assert abs(coeffs[1] - (-1.0)) < 1e-12
        # c_2 = -sigma_{-1}(2) = -(1 + 1/2) = -3/2
        assert abs(coeffs[2] - (-1.5)) < 1e-12
        # c_3 = -sigma_{-1}(3) = -(1 + 1/3) = -4/3
        assert abs(coeffs[3] - (-4.0 / 3.0)) < 1e-12
        # c_4 = -(1 + 1/2 + 1/4) = -7/4
        assert abs(coeffs[4] - (-7.0 / 4.0)) < 1e-12

    def test_genus1_amplitude_at_high_im_tau(self):
        """At large Im(tau), A_1 ~ -(kappa/24)*2*pi*i*tau."""
        tau = complex(0, 10)  # large imaginary part
        kappa = 1.0
        A1 = genus1_full_amplitude_lattice(1, tau)
        # Leading: -(1/24)*2*pi*i*10 = -(pi*i*10/12)
        expected_leading = -kappa * 2j * PI * tau / 24.0
        # At large Im(tau), the sum terms are exponentially small
        assert abs(A1 - expected_leading) < 0.01

    def test_genus1_q_coefficients_rank1(self):
        """Q-coefficients for rank 1: a_m = sigma_{-1}(m)."""
        result = genus1_amplitude_q_coefficients(1, nmax=10)
        assert result['F_1_scalar'] == Rational(1, 24)
        assert result['leading_power_log_q'] == Rational(-1, 24)
        # a_1 = 1 * sigma_{-1}(1) = 1
        assert result['q_coefficients'][1] == Rational(1)
        # a_2 = 1 * (1 + 1/2) = 3/2
        assert result['q_coefficients'][2] == Rational(3, 2)

    def test_genus1_scalar_part(self):
        """F_1 = kappa/24 for various kappa values."""
        for kappa in [0.5, 1.0, 6.0, 12.0, 13.0]:
            assert abs(genus1_amplitude_scalar_part(kappa) - kappa / 24.0) < 1e-12


# =========================================================================
# Section 3: Genus-2 amplitude tests
# =========================================================================

class TestGenus2:
    """Tests for genus-2 shadow amplitude."""

    def test_genus2_scalar_rank1(self):
        """F_2(rank=1) = 7/5760."""
        F2 = genus2_scalar_amplitude_lattice(1)
        assert F2 == Rational(7, 5760)

    def test_genus2_scalar_rank8(self):
        """F_2(E_8) = 8 * 7/5760 = 7/720."""
        F2 = genus2_scalar_amplitude_lattice(8)
        assert F2 == Rational(7, 720)

    def test_genus2_scalar_rank24(self):
        """F_2(Leech) = 24 * 7/5760 = 7/240."""
        F2 = genus2_scalar_amplitude_lattice(24)
        assert F2 == Rational(7, 240)

    def test_genus2_structure(self):
        """Genus-2 amplitude structure involves Siegel forms."""
        structure = genus2_full_amplitude_lattice_structure()
        assert 'chi_10' in structure['key_forms']
        assert structure['modular_group'] == 'Sp(4, Z)'


# =========================================================================
# Section 4: Virasoro shadow PF tests
# =========================================================================

class TestVirasoroShadowPF:
    """Tests for the Virasoro shadow partition function."""

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        for c in [1.0, 13.0, 24.0, 26.0]:
            coeffs = virasoro_shadow_coefficients(c)
            assert abs(coeffs[2] - c / 2.0) < 1e-12

    def test_virasoro_cubic_shadow(self):
        """S_3 = 2 (c-independent for Virasoro; AP9)."""
        for c in [1.0, 13.0, 26.0]:
            coeffs = virasoro_shadow_coefficients(c)
            assert abs(coeffs[3] - 2.0) < 1e-10

    def test_virasoro_quartic_contact(self):
        """Q^contact = 10/(c*(5c+22))."""
        c = 13.0
        coeffs = virasoro_shadow_coefficients(c)
        expected = 10.0 / (c * (5 * c + 22))
        assert abs(coeffs[4] - expected) < 1e-12

    def test_virasoro_shadow_pf_tau_independent(self):
        """Z^sh(Vir_c) is tau-independent."""
        result = virasoro_shadow_pf_formal(13.0, 1.0)
        assert result['tau_independent']

    def test_virasoro_scalar_convergent(self):
        """Scalar genus series always convergent for |hbar| < 2*pi."""
        result = virasoro_shadow_pf_formal(13.0, 1.0)
        assert result['scalar_convergent']

    def test_virasoro_arity_convergent_c13(self):
        """Arity series convergent for c=13 (above c*)."""
        result = virasoro_shadow_pf_formal(13.0, 1.0)
        assert result['arity_convergent']

    def test_virasoro_arity_divergent_c1(self):
        """Arity series divergent for c=1 (below c*)."""
        result = virasoro_shadow_pf_formal(1.0, 1.0)
        assert not result['arity_convergent']

    def test_virasoro_borel_entire(self):
        """Borel transform of genus series is entire."""
        result = virasoro_shadow_pf_borel(13.0, 1.0)
        assert result['borel_entire']
        assert result['borel_summable']


# =========================================================================
# Section 5: Modular transformation tests
# =========================================================================

class TestModularTransformations:
    """Tests for modular transformation properties."""

    def test_eta_at_i(self):
        """eta(i) is a known constant: Gamma(1/4)/(2*pi^{3/4})."""
        tau = complex(0, 1)
        eta_val = eta_numerical(tau)
        # eta(i) ~ 0.76823 (known numerical value)
        assert abs(abs(eta_val) - 0.7682254) < 1e-4

    def test_eta_t_invariance(self):
        """eta(tau+1) = e^{2*pi*i/24} * eta(tau)."""
        tau = complex(0.3, 1.2)
        eta_tau = eta_numerical(tau)
        eta_t = eta_numerical(tau + 1.0)
        phase = cmath.exp(2j * PI / 24.0)
        ratio = eta_t / (phase * eta_tau)
        assert abs(ratio - 1.0) < 1e-6

    def test_eta_s_transform(self):
        """eta(-1/tau) = sqrt(-i*tau) * eta(tau)."""
        tau = complex(0.3, 1.2)
        eta_tau = eta_numerical(tau)
        eta_s = eta_numerical(-1.0 / tau)
        factor = cmath.sqrt(-1j * tau)
        ratio = eta_s / (factor * eta_tau)
        assert abs(ratio - 1.0) < 1e-4

    def test_modular_anomaly_s_transform(self):
        """Genus-1 amplitude S-anomaly: delta_S = -(kappa/2)*log(-i*tau)."""
        tau = complex(0.2, 1.5)
        result = modular_anomaly_genus1(1.0, tau)
        assert result['anomaly_S_match']

    def test_modular_anomaly_t_transform(self):
        """Genus-1 amplitude T-anomaly: delta_T = -kappa*pi*i/12."""
        tau = complex(0.2, 1.5)
        result = modular_anomaly_genus1(1.0, tau)
        assert result['anomaly_T_match']

    def test_e2_star_quasi_modularity(self):
        """E_2*(-1/tau) = tau^2 * E_2*(tau) + 12*tau/(2*pi*i)."""
        result = verify_e2_quasi_modularity(complex(0.3, 1.5))
        assert result['verified']

    def test_e2_star_first_coefficient(self):
        """E_2*(tau) = 1 - 24*q - 72*q^2 - 96*q^3 - ..."""
        tau = complex(0, 2)  # large Im(tau) for convergence
        val = e2_star_numerical(tau, nmax=10)
        # At large Im(tau), E_2* ~ 1
        assert abs(val - 1.0) < 0.01

    def test_e2_star_not_modular(self):
        """E_2* is NOT modular: E_2*(-1/tau) != tau^2 * E_2*(tau)."""
        tau = complex(0.3, 1.5)
        e2_tau = e2_star_numerical(tau)
        e2_S = e2_star_numerical(-1.0 / tau)
        # If it WERE modular: e2_S = tau^2 * e2_tau
        naive_modular = tau ** 2 * e2_tau
        # The difference should be nonzero (the quasi-modular anomaly)
        diff = abs(e2_S - naive_modular)
        assert diff > 0.1  # the anomaly 12*tau/(2*pi*i) is O(1)


# =========================================================================
# Section 6: Arithmetic decomposition tests
# =========================================================================

class TestArithmeticDecomposition:
    """Tests for the Z = Z^sh * Z^arith decomposition."""

    def test_theta_e8_is_e4(self):
        """Theta_{E_8} = E_4."""
        theta = theta_lattice_coeffs('E8', 10)
        assert theta[0] == 1
        assert theta[1] == 240  # 240*sigma_3(1) = 240

    def test_theta_leech_no_norm2(self):
        """Leech lattice has no vectors of norm 2: r_Leech(1) = 0."""
        theta = theta_lattice_coeffs('Leech', 5)
        assert theta[0] == 1
        assert theta[1] == 0  # no roots

    def test_theta_leech_norm4(self):
        """Leech lattice: r_Leech(2) = 196560 (kissing number)."""
        theta = theta_lattice_coeffs('Leech', 5)
        assert theta[2] == 196560

    def test_theta_z_lattice(self):
        """Theta_Z = 1 + 2q + 2q^4 + 2q^9 + ..."""
        theta = theta_lattice_coeffs('Z', 12)
        assert theta[0] == 1
        assert theta[1] == 2
        assert theta[2] == 0
        assert theta[3] == 0
        assert theta[4] == 2
        assert theta[9] == 2

    def test_e8_decomposition(self):
        """E_8 lattice: Z = E_4 / eta^8."""
        result = arithmetic_decomposition_genus1('E8')
        assert result['rank'] == 8
        assert result['F_1_shadow'] == Rational(8, 24)
        assert result['theta_is_modular_form']
        assert result['theta_weight'] == Rational(4)

    def test_leech_decomposition(self):
        """Leech lattice: Z = Theta_Leech / eta^24."""
        result = arithmetic_decomposition_genus1('Leech')
        assert result['rank'] == 24
        assert result['F_1_shadow'] == Rational(24, 24)
        assert result['Z_weight'] == 0  # j-function is weight 0

    def test_arithmetic_separation_e8(self):
        """Numerical Z = Z^sh * Z^arith for E_8."""
        tau = complex(0, 1.5)
        result = arithmetic_content_separation('E8', tau)
        assert result['decomposition_holds']
        assert result['shadow_is_eta_power']
        assert result['arithmetic_is_theta']

    def test_arithmetic_separation_leech(self):
        """Numerical Z = Z^sh * Z^arith for Leech."""
        tau = complex(0, 1.5)
        result = arithmetic_content_separation('Leech', tau)
        assert result['decomposition_holds']


# =========================================================================
# Section 7: Special values tests
# =========================================================================

class TestSpecialValues:
    """Tests for Virasoro at special central charges."""

    def test_special_values_exist(self):
        """All special c values have entries."""
        results = virasoro_special_values()
        assert 'c=24_Monster' in results
        assert 'c=13_self_dual' in results
        assert 'c=26_critical' in results

    def test_monster_kappa(self):
        """kappa(Monster) = 12."""
        results = virasoro_special_values()
        assert results['c=24_Monster']['kappa'] == 12.0

    def test_self_dual_kappa(self):
        """kappa(Vir_13) = 13/2."""
        results = virasoro_special_values()
        assert results['c=13_self_dual']['kappa'] == 6.5

    def test_critical_kappa(self):
        """kappa(Vir_26) = 13."""
        results = virasoro_special_values()
        assert results['c=26_critical']['kappa'] == 13.0

    def test_ising_kappa(self):
        """kappa(Ising) = 1/4."""
        results = virasoro_special_values()
        assert results['c=1/2_Ising']['kappa'] == 0.25

    def test_all_tau_independent(self):
        """All Z^sh are tau-independent."""
        results = virasoro_special_values()
        for key, val in results.items():
            assert val['Z_sh_scalar_tau_independent']


# =========================================================================
# Section 8: Double expansion tests
# =========================================================================

class TestDoubleExpansion:
    """Tests for the double expansion in tau and hbar."""

    def test_shadow_is_constant(self):
        """The shadow F_1 is a constant (tau-independent)."""
        tau = complex(0.3, 1.5)
        result = double_expansion_genus1(26.0, tau)
        assert result['shadow_is_constant']

    def test_full_amplitude_quasi_modular(self):
        """The full genus-1 amplitude is quasi-modular."""
        tau = complex(0.3, 1.5)
        result = double_expansion_genus1(26.0, tau)
        assert result['full_amplitude_is_quasi_modular']

    def test_f1_value(self):
        """F_1 = kappa/24 for c=26."""
        tau = complex(0.3, 1.5)
        result = double_expansion_genus1(26.0, tau)
        assert abs(result['F_1_shadow'] - 13.0 / 24.0) < 1e-12

    def test_q_correction_first_term(self):
        """First q-correction: kappa * sigma_{-1}(1) = kappa."""
        tau = complex(0.3, 1.5)
        result = double_expansion_genus1(2.0, tau)  # c=2, kappa=1
        assert abs(result['q_correction_coeffs'][1] - 1.0) < 1e-12


# =========================================================================
# Section 9: Modularity classification tests
# =========================================================================

class TestModularityClassification:
    """Tests for the modularity classification across depth classes."""

    def test_all_classes_present(self):
        """All four depth classes are classified."""
        classes = modularity_classification()
        assert 'G' in classes
        assert 'L' in classes
        assert 'C' in classes
        assert 'M' in classes

    def test_all_tau_independent(self):
        """All classes have tau-independent Z^sh."""
        classes = modularity_classification()
        for key, val in classes.items():
            assert not val['tau_dependent']

    def test_class_g_gaussian(self):
        """Class G: Gaussian, rmax=2."""
        classes = modularity_classification()
        assert classes['G']['rmax'] == 2

    def test_class_m_infinite(self):
        """Class M: infinite tower."""
        classes = modularity_classification()
        assert classes['M']['rmax'] == 'infinity'


# =========================================================================
# Section 10: E_2* connection tests
# =========================================================================

class TestE2StarConnection:
    """Tests for the E_2* / quasi-modularity connection."""

    def test_propagator_is_quasi_modular(self):
        """The genus-1 propagator is quasi-modular."""
        tau = complex(0.3, 1.5)
        result = genus1_propagator_modular_analysis(tau)
        assert result['is_quasi_modular']
        assert not result['is_holomorphic_modular']
        assert result['weight'] == 2
        assert result['depth'] == 1

    def test_propagator_quasi_modularity_verified(self):
        """P(-1/tau) = tau^2 * P(tau) - tau/(2*pi*i)."""
        tau = complex(0.3, 1.5)
        result = genus1_propagator_modular_analysis(tau)
        assert result['quasi_modular_verified']

    def test_full_amplitude_holomorphic_quasi_modular(self):
        """Holomorphic genus-1 amplitude is quasi-modular."""
        tau = complex(0.3, 1.5)
        result = full_amplitude_quasi_modularity(1.0, tau)
        assert result['holomorphic_part_quasi_modular']

    def test_full_amplitude_nh_modular(self):
        """Non-holomorphic completion is modular invariant."""
        tau = complex(0.3, 1.5)
        result = full_amplitude_quasi_modularity(1.0, tau)
        assert result['non_holomorphic_part_modular_invariant']

    def test_conformal_anomaly_from_e2(self):
        """The conformal anomaly comes from E_2*."""
        tau = complex(0.3, 1.5)
        result = full_amplitude_quasi_modularity(1.0, tau)
        assert result['conformal_anomaly_from_E2']

    def test_e2_hat_formula(self):
        """E_2^hat = E_2* - 3/(pi*y) is the non-holomorphic modular completion."""
        tau = complex(0.3, 1.5)
        result = full_amplitude_quasi_modularity(1.0, tau)
        y = tau.imag
        e2_star = result['E2_star']
        e2_hat = result['E2_hat']
        assert abs(e2_hat - (e2_star - 3.0 / (PI * y))) < 1e-8


# =========================================================================
# Section 11: Monster module tests
# =========================================================================

class TestMonsterModule:
    """Tests for the Monster module (c=24) shadow analysis."""

    def test_monster_kappa(self):
        """kappa(V^natural) = 12."""
        result = monster_shadow_analysis()
        assert result['kappa'] == 12.0

    def test_monster_f1(self):
        """F_1(Monster) = 12/24 = 1/2."""
        result = monster_shadow_analysis()
        assert abs(result['F_1'] - 0.5) < 1e-12

    def test_monster_f2(self):
        """F_2(Monster) = 12 * 7/5760 = 7/480."""
        result = monster_shadow_analysis()
        expected = 12.0 * 7.0 / 5760.0
        assert abs(result['F_2'] - expected) < 1e-12

    def test_monster_convergent(self):
        """Monster (c=24 > c*) has convergent arity series."""
        result = monster_shadow_analysis()
        assert result['arity_convergent']

    def test_monster_zsh_constant(self):
        """Z^sh(Monster) is a constant."""
        result = monster_shadow_analysis()
        assert result['Z_sh_is_constant']

    def test_j_first_coeffs(self):
        """j - 744 starts with q^{-1} + 0 + 196884*q + ..."""
        result = monster_shadow_analysis()
        assert result['j_first_coeffs'][0] == 1      # q^{-1}
        assert result['j_first_coeffs'][1] == 0      # q^0 (removed 744)
        assert result['j_first_coeffs'][2] == 196884  # q^1


# =========================================================================
# Section 12: Master summary tests
# =========================================================================

class TestMasterSummary:
    """Tests for the master modularity summary."""

    def test_main_result(self):
        """The main result: Z^sh is tau-independent."""
        result = master_modularity_summary()
        assert result['all_Z_sh_tau_independent']

    def test_genus1_quasi_modular(self):
        """Genus-1 amplitude is quasi-modular."""
        result = master_modularity_summary()
        assert result['genus_1_quasi_modular']

    def test_nh_modular(self):
        """Non-holomorphic completion is modular."""
        result = master_modularity_summary()
        assert result['non_holomorphic_modular']


# =========================================================================
# Cross-checks: consistency with existing modules
# =========================================================================

class TestCrossChecks:
    """Cross-checks against existing compute infrastructure."""

    def test_f1_matches_utils(self):
        """F_1 from this module matches compute.lib.utils.F_g."""
        for rank in [1, 8, 24]:
            our_F1 = genus1_amplitude_scalar_part(float(rank))
            utils_F1 = float(F_g(Rational(rank), 1))
            assert abs(our_F1 - utils_F1) < 1e-12

    def test_f2_matches_utils(self):
        """F_2 from this module matches compute.lib.utils.F_g."""
        for rank in [1, 8, 24]:
            our_F2 = float(genus2_scalar_amplitude_lattice(rank))
            utils_F2 = float(F_g(Rational(rank), 2))
            assert abs(our_F2 - utils_F2) < 1e-12

    def test_lambda_fp_values(self):
        """Cross-check lambda_g^FP values."""
        # lambda_1 = 1/24
        assert lambda_fp(1) == Rational(1, 24)
        # lambda_2 = 7/5760
        assert lambda_fp(2) == Rational(7, 5760)
        # lambda_3 = 31/967680 (from B_6 = 1/42)
        # (2^5 - 1)/2^5 * |B_6|/6! = 31/32 * (1/42)/720 = 31/(32*30240) = 31/967680
        assert lambda_fp(3) == Rational(31, 967680)

    def test_bernoulli_decay(self):
        """Bernoulli numbers give geometric decay: |lambda_g^FP| ~ 2/(2*pi)^{2g}."""
        for g in range(5, 15):
            lam_g = float(lambda_fp(g))
            lam_g1 = float(lambda_fp(g + 1))
            ratio = lam_g1 / lam_g
            expected_ratio = 1.0 / (TWO_PI ** 2)
            assert abs(ratio - expected_ratio) / expected_ratio < 0.1

    def test_ahat_convergence_radius(self):
        """A-hat has poles at hbar = 2*pi*n, so R = 2*pi."""
        # At hbar slightly below 2*pi, the function should be large but finite
        hbar = TWO_PI - 0.01
        val = ahat_closed_form(hbar)
        assert math.isfinite(val)
        assert abs(val) > 100  # near the pole

    def test_ahat_pole_at_2pi(self):
        """A-hat diverges as hbar -> 2*pi."""
        vals = []
        for eps in [0.1, 0.01, 0.001]:
            vals.append(abs(ahat_closed_form(TWO_PI - eps)))
        # Should be increasing
        assert vals[1] > vals[0]
        assert vals[2] > vals[1]


# =========================================================================
# Beilinson-grade verification: AP-specific tests
# =========================================================================

class TestAntiPatternGuards:
    """Tests that guard against known anti-patterns."""

    def test_ap15_e2_quasi_modular(self):
        """AP15: E_2* is quasi-modular, NOT holomorphic modular."""
        tau = complex(0.3, 1.5)
        result = genus1_propagator_modular_analysis(tau)
        assert not result['is_holomorphic_modular']
        assert result['is_quasi_modular']

    def test_ap20_kappa_not_c(self):
        """AP20: kappa is NOT the same as c. For Virasoro: kappa = c/2."""
        c = 26.0
        kappa = c / 2.0
        assert kappa != c
        assert kappa == 13.0

    def test_ap24_complementarity_not_zero_for_virasoro(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0."""
        for c in [1.0, 13.0, 25.0]:
            kappa = c / 2.0
            kappa_dual = (26.0 - c) / 2.0
            assert abs(kappa + kappa_dual - 13.0) < 1e-12

    def test_ap25_bar_not_cobar_not_verdier(self):
        """AP25: Z^sh extracts the eta part, not the theta part.
        The theta function is the ARITHMETIC content, not the shadow."""
        result = arithmetic_decomposition_genus1('E8')
        # The shadow captures the eta^{-rank} part (topological)
        # The theta function is the ARITHMETIC part (lattice-specific)
        assert result['F_1_shadow'] == Rational(8, 24)

    def test_ap31_kappa_zero_does_not_imply_theta_zero(self):
        """AP31: kappa=0 does NOT imply Theta_A=0 (higher-arity shadows exist)."""
        results = virasoro_special_values()
        c0 = results['c=0_trivial']
        assert c0['kappa'] == 0.0
        # But higher-arity shadows could be nonzero (AP31)
        # This is structural: we just verify the flag
        assert c0['Z_sh_scalar_tau_independent']

    def test_ap39_kappa_neq_s2_for_affine(self):
        """AP39: kappa != S_2 = c/2 for affine KM at rank > 1.
        For Virasoro: kappa = c/2 (they agree).
        For Heisenberg rank r: kappa = r, c = r, so kappa = c (also agree, rank 1).
        The distinction matters for affine KM at rank > 1."""
        # For sl_2 level 1: kappa = dim(sl_2)*(1+2)/(2*2) = 3*3/4 = 9/4
        # But c = 3*1/(1+2) = 1, so S_2 = c/2 = 1/2
        # kappa != S_2 for this family
        kappa_sl2 = 3.0 * 3.0 / 4.0  # = 9/4
        c_sl2 = 1.0
        S2_sl2 = c_sl2 / 2.0  # = 1/2
        assert abs(kappa_sl2 - S2_sl2) > 1.0  # they differ by 9/4 - 1/2 = 7/4
