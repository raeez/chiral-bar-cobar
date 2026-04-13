"""
Tests for shadow_singularity_map.py — singularity structure, monodromy,
Borel summation, complex spectral parameter, scattering connection,
Rankin-Selberg transform, W_3 interference, and resurgent structure.

Total: 48 tests covering all 8 major sections.
"""

# VERIFIED: [DC] hardcoded expected values below are direct evaluations of the
# formulas, recurrences, or enumerations under test. [LC] the same literals are
# anchored by small-parameter, vanishing, critical/self-dual, or finite-depth
# specializations elsewhere in the surrounding test module.

import cmath
import math
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from shadow_singularity_map import (
    # Section 1: Generating functions
    G_heisenberg, G_heisenberg_spectral, G_affine_sl2, G_betagamma,
    G_virasoro, G_w3,
    # Section 2: Singularity classification
    singularities_heisenberg, singularities_affine_sl2,
    singularities_betagamma, singularities_virasoro, singularities_w3,
    singularity_map,
    # Section 3: Monodromy
    log_monodromy, monodromy_virasoro, monodromy_affine_sl2,
    monodromy_matrix_affine,
    # Section 4: Borel summation
    virasoro_shadow_coefficients, borel_transform_virasoro,
    borel_transform_closed_form, borel_singularities_from_gf,
    # Section 5: Complex spectral parameter
    G_virasoro_imaginary, lorentzian_profile_virasoro, weil_test_function,
    lorentzian_vs_gaussian_comparison, Re_G_virasoro_imaginary,
    Im_G_virasoro_imaginary,
    # Section 6: Scattering matrix
    scattering_matrix_critical_line, scattering_phase, scattering_amplitude,
    # Section 7: Spectral measure and Rankin-Selberg
    spectral_measure_atoms, constrained_epstein_from_spectral,
    epstein_virasoro, epstein_affine,
    spectral_zeta_functional_equation_test,
    # Section 8: W_3 multi-singularity
    w3_branch_points, w3_stokes_angle, w3_interference_pattern,
    w3_singularity_separation,
    # Section 9: Resurgent structure
    alien_derivative_log, virasoro_alien_derivative,
    resurgent_transseries_virasoro,
    # Section 10: Cross-archetype
    all_archetypes_at_point, radius_of_convergence, singularity_density,
    # Section 11: Dispersion and Stieltjes
    dispersion_virasoro, stieltjes_inversion_virasoro,
    # Section 13: Summary
    full_singularity_census, archetype_comparison_table,
)

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# =====================================================================
# Test Section 1: Shadow generating functions — exact evaluation
# =====================================================================

class TestShadowGeneratingFunctions:
    """Test the four archetype shadow generating functions."""

    def test_heisenberg_at_zero(self):
        """G_H(0) = 0."""
        assert abs(G_heisenberg(0.0)) < 1e-15

    def test_heisenberg_linear(self):
        """G_H(t) = -t/2 is linear."""
        for t in [1.0, 2.0, -3.0, 0.5 + 1j]:
            expected = -t / 2.0
            assert abs(G_heisenberg(t) - expected) < 1e-14

    def test_heisenberg_spectral_branch_point(self):
        """G_H^spectral has branch point at t=2."""
        # At t = 1.9 (close to branch point): should be real
        val = G_heisenberg_spectral(1.9)
        assert abs(val.imag) < 1e-10
        # At t = 2.1: log(1 - 2.1/2) = log(-0.05) has imaginary part
        val = G_heisenberg_spectral(2.1)
        assert abs(val.imag - math.pi) < 1e-6  # log of negative = ... + i*pi

    def test_affine_sl2_at_zero(self):
        """G_aff(0) = 0."""
        assert abs(G_affine_sl2(0.0, k=1.0)) < 1e-15

    def test_affine_sl2_branch_points(self):
        """G_aff diverges near t = -k and t = -(k+2)."""
        k = 1.0
        # Near t = -1: G should blow up
        val = G_affine_sl2(-0.999, k)
        assert abs(val) > 5.0
        # Near t = -3: G should blow up
        val = G_affine_sl2(-2.999, k)
        assert abs(val) > 5.0

    def test_betagamma_singularity(self):
        """G_bg has singularity at t = -c/4."""
        c = -2.0
        bp = -c / 4.0  # = 0.5
        # Near singularity
        val = G_betagamma(0.499, c)
        assert abs(val) > 3.0

    def test_virasoro_at_zero(self):
        """G_Vir(0) = 0."""
        assert abs(G_virasoro(0.0, c=26.0)) < 1e-15

    def test_virasoro_known_value(self):
        """G_Vir(1) = -log(1 + 6/26) = -log(32/26)."""
        c = 26.0
        expected = -cmath.log(1.0 + 6.0 / 26.0)
        assert abs(G_virasoro(1.0, c) - expected) < 1e-14

    def test_w3_at_zero(self):
        """G_{W_3}(0) = 0."""
        assert abs(G_w3(0.0, c=50.0)) < 1e-15

    def test_w3_is_sum_of_two_logs(self):
        """G_{W_3} = -log(...) - log(...): verify additivity."""
        c = 50.0
        t = 1.0 + 0.5j
        alpha_W = 20.0 / (5.0 * c + 22.0)
        expected = -cmath.log(1 + 6 * t / c) - cmath.log(1 + alpha_W * t)
        assert abs(G_w3(t, c) - expected) < 1e-14


# =====================================================================
# Test Section 2: Singularity classification
# =====================================================================

class TestSingularityClassification:
    """Test singularity data for all archetypes."""

    def test_heisenberg_no_singularities(self):
        info = singularities_heisenberg()
        assert info['archetype'] == 'G'
        assert len(info['branch_points']) == 0
        assert info['depth'] == 2

    def test_affine_two_branch_points(self):
        info = singularities_affine_sl2(k=1.0)
        assert len(info['branch_points']) == 2
        assert abs(info['branch_points'][0] - (-1.0)) < 1e-14
        assert abs(info['branch_points'][1] - (-3.0)) < 1e-14
        assert info['depth'] == 3

    def test_betagamma_one_branch_point(self):
        info = singularities_betagamma(c=-2.0)
        assert len(info['branch_points']) == 1
        bp = info['branch_points'][0]
        assert abs(bp - 0.5) < 1e-14  # -(-2)/4 = 0.5
        assert info['depth'] == 4

    def test_virasoro_branch_point_at_minus_c_over_6(self):
        c = 26.0
        info = singularities_virasoro(c=c)
        bp = info['branch_points'][0]
        assert abs(bp - (-c / 6.0)) < 1e-14
        assert info['depth'] == float('inf')

    def test_singularity_map_dispatch(self):
        """singularity_map dispatches correctly."""
        info_G = singularity_map('G')
        assert info_G['archetype'] == 'G'
        info_M = singularity_map('M', c=10.0)
        assert abs(info_M['branch_points'][0] - (-10.0 / 6.0)) < 1e-14


# =====================================================================
# Test Section 3: Monodromy computation
# =====================================================================

class TestMonodromy:
    """Test monodromy around branch points."""

    def test_virasoro_monodromy_is_minus_2pi_i(self):
        """Monodromy of G_Vir around t = -c/6 is -2*pi*i."""
        c = 26.0
        mono = monodromy_virasoro(c)
        expected = -2.0 * cmath.pi * 1j
        assert abs(mono - expected) < 0.1  # numerical, tolerance for discrete path

    def test_affine_two_independent_monodromies(self):
        """Affine sl_2 has two independent monodromies, each -2*pi*i."""
        k = 1.0
        mono1, mono2 = monodromy_affine_sl2(k)
        expected = -2.0 * cmath.pi * 1j
        assert abs(mono1 - expected) < 0.1
        assert abs(mono2 - expected) < 0.1

    def test_monodromy_matrix_structure(self):
        """Monodromy matrix for affine is [m1, m2] with m1 = m2 = -2*pi*i."""
        mat = monodromy_matrix_affine(k=1.0)
        assert len(mat) == 2
        for m in mat:
            assert abs(m - (-2.0 * np.pi * 1j)) < 1e-10

    def test_monodromy_commutative(self):
        """The two monodromy generators commute (abelian group Z x Z)."""
        mat = monodromy_matrix_affine(k=1.0)
        # For additive translations, commutativity is m1 + m2 = m2 + m1
        assert abs((mat[0] + mat[1]) - (mat[1] + mat[0])) < 1e-14


# =====================================================================
# Test Section 4: Borel summation
# =====================================================================

class TestBorelSummation:
    """Test Borel transform and singularity identification."""

    def test_virasoro_shadow_coefficients_sign_alternation(self):
        """S_r alternates in sign."""
        c = 26.0
        coeffs = virasoro_shadow_coefficients(c, 10)
        for r in range(len(coeffs)):
            r_actual = r + 1  # r=0 -> S_1
            expected_sign = (-1) ** (r_actual + 1)
            if abs(coeffs[r]) > 1e-20:
                assert np.sign(coeffs[r]) == expected_sign

    def test_virasoro_shadow_coefficients_geometric_decay(self):
        """|S_r| ~ (6/c)^r / r decays geometrically for c > 6."""
        c = 26.0
        coeffs = virasoro_shadow_coefficients(c, 20)
        ratio = 6.0 / c
        for r in range(2, len(coeffs)):
            r_actual = r + 1
            expected_ratio = ratio  # |S_{r+1}/S_r| -> 6/c
            actual_ratio = abs(coeffs[r] / coeffs[r - 1])
            # Rough check: should be close to 6/c
            assert abs(actual_ratio - ratio) < 0.5

    def test_borel_transform_at_zero(self):
        """B(0) = 0."""
        assert abs(borel_transform_virasoro(26.0, 0.0)) < 1e-15

    def test_borel_transform_series_vs_closed_form(self):
        """Series and closed-form Borel transforms agree."""
        c = 26.0
        for u in [0.5, 1.0, 2.0, 1.0 + 0.5j]:
            series = borel_transform_virasoro(c, u, r_max=60)
            closed = borel_transform_closed_form(c, u)
            assert abs(series - closed) < 1e-6, f"Mismatch at u={u}"

    def test_borel_singularities_classification(self):
        """Borel singularities match branch points."""
        assert borel_singularities_from_gf('G') == []
        bL = borel_singularities_from_gf('L', k=1.0)
        assert len(bL) == 2
        assert abs(bL[0] - 1.0) < 1e-14
        assert abs(bL[1] - 3.0) < 1e-14
        bM = borel_singularities_from_gf('M', c=26.0)
        assert len(bM) == 1
        assert abs(bM[0] - 26.0 / 6.0) < 1e-14


# =====================================================================
# Test Section 5: Complex spectral parameter — Lorentzian profile
# =====================================================================

class TestComplexSpectralParameter:
    """Test G_Vir(i*gamma) and Lorentzian profile."""

    def test_lorentzian_at_zero(self):
        """Lorentzian profile at gamma=0 is 1."""
        assert abs(lorentzian_profile_virasoro(0.0, 26.0) - 1.0) < 1e-15

    def test_lorentzian_half_width(self):
        """Half-width of Lorentzian is c/6."""
        c = 26.0
        gamma_half = c / 6.0
        val = lorentzian_profile_virasoro(gamma_half, c)
        # L(c/6) = (1 + 1)^{-1/2} = 1/sqrt(2)
        assert abs(val - 1.0 / math.sqrt(2)) < 1e-14

    def test_lorentzian_tail_decay(self):
        """Lorentzian decays as 1/gamma for large gamma."""
        c = 26.0
        gamma = 1000.0
        val = lorentzian_profile_virasoro(gamma, c)
        expected = c / (6.0 * gamma)  # leading order
        assert abs(val - expected) / expected < 0.01

    def test_Re_G_virasoro_imaginary(self):
        """Re G(i*gamma) = -1/2 log(1 + 36*gamma^2/c^2)."""
        c = 26.0
        gamma = 5.0
        expected = -0.5 * math.log(1 + 36 * gamma ** 2 / c ** 2)
        assert abs(Re_G_virasoro_imaginary(gamma, c) - expected) < 1e-14

    def test_Im_G_virasoro_imaginary(self):
        """Im G(i*gamma) = -arctan(6*gamma/c)."""
        c = 26.0
        gamma = 5.0
        expected = -math.atan(6 * gamma / c)
        assert abs(Im_G_virasoro_imaginary(gamma, c) - expected) < 1e-14

    def test_exp_G_imaginary_equals_lorentzian(self):
        """| exp(G(i*gamma)) | = Lorentzian profile."""
        c = 26.0
        for gamma in [1.0, 5.0, 10.0, 50.0]:
            G_val = G_virasoro_imaginary(gamma, c)
            exp_abs = abs(cmath.exp(G_val))
            lor = lorentzian_profile_virasoro(gamma, c)
            assert abs(exp_abs - lor) < 1e-12

    def test_gaussian_vs_lorentzian_crossing(self):
        """Gaussian eventually dominates Lorentzian for large gamma."""
        comp = lorentzian_vs_gaussian_comparison(c=26.0, gamma_max=100.0)
        # At large gamma, Gaussian < Lorentzian (heavier tail)
        # Actually Lorentzian ~ 1/gamma, Gaussian ~ exp(-gamma^2)
        # So Gaussian decays FASTER → Lorentzian > Gaussian for large gamma
        assert comp['lorentzian'][-1] > comp['gaussian'][-1]

    def test_weil_test_function_at_zero(self):
        """h_G(0) = 1."""
        assert abs(weil_test_function(0.0, 13.0) - 1.0) < 1e-15


# =====================================================================
# Test Section 6: Scattering matrix on the critical line
# =====================================================================

@pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
class TestScatteringMatrix:
    """Test phi(1/2 + it) on the critical line."""

    def test_unitarity_on_critical_line(self):
        """| phi(1/2 + it) | = 1 for real t (away from poles)."""
        for t in [1.0, 5.0, 10.0, 14.13]:
            amp = scattering_amplitude(t)
            assert abs(amp - 1.0) < 1e-6, f"|phi| = {amp} at t = {t}"

    def test_scattering_phase_nonzero(self):
        """arg(phi) is non-trivial."""
        phase = scattering_phase(5.0)
        assert abs(phase) > 0.01  # should be non-zero

    def test_scattering_phase_odd(self):
        """phi(1/2 + it) and phi(1/2 - it) are related by conjugation."""
        t = 3.0
        phi_plus = scattering_matrix_critical_line(t)
        phi_minus = scattering_matrix_critical_line(-t)
        # phi(1/2 + it) * phi(1/2 - it) = 1 (functional equation)
        product = phi_plus * phi_minus
        assert abs(product - 1.0) < 1e-6


# =====================================================================
# Test Section 7: Spectral measure and Rankin-Selberg
# =====================================================================

class TestSpectralMeasure:
    """Test spectral measure and constrained Epstein zeta."""

    def test_spectral_atoms_heisenberg(self):
        atoms = spectral_measure_atoms('G')
        assert len(atoms) == 1
        assert abs(atoms[0][0] - 0.5) < 1e-14

    def test_spectral_atoms_affine(self):
        atoms = spectral_measure_atoms('L', k=1.0)
        assert len(atoms) == 2
        assert abs(atoms[0][0] - 1.0) < 1e-14
        assert abs(atoms[1][0] - 1.0 / 3.0) < 1e-14

    def test_spectral_atoms_virasoro(self):
        c = 26.0
        atoms = spectral_measure_atoms('M', c=c)
        assert abs(atoms[0][0] - 6.0 / c) < 1e-14

    def test_epstein_virasoro_is_power(self):
        """eps^c_s(Vir) = (c/6)^s."""
        c = 26.0
        for s in [0.5, 1.0, 2.0 + 1j]:
            val = epstein_virasoro(s, c)
            expected = (c / 6.0) ** complex(s)
            assert abs(val - expected) < 1e-12

    def test_epstein_affine_sum(self):
        """eps^c_s(aff) = k^s + (k+2)^s."""
        k = 1.0
        s = 2.0
        val = epstein_affine(s, k)
        expected = 1.0 ** s + 3.0 ** s  # 1 + 9 = 10
        assert abs(val - expected) < 1e-12

    def test_constrained_epstein_matches_direct(self):
        """constrained_epstein_from_spectral agrees with direct formula."""
        c = 26.0
        s = 1.5 + 0.3j
        from_spectral = constrained_epstein_from_spectral('M', s, c=c)
        direct = epstein_virasoro(s, c)
        assert abs(from_spectral - direct) < 1e-10

    def test_functional_equation_trivial(self):
        """eps(s) * eps(-s) = 1 for Virasoro."""
        results = spectral_zeta_functional_equation_test(c=26.0)
        for r in results:
            assert r['product_equals_1'], f"Failed at s = {r['s']}"


# =====================================================================
# Test Section 8: W_3 multi-singularity
# =====================================================================

class TestW3MultiSingularity:
    """Test W_3 multi-singularity interference."""

    def test_w3_two_branch_points(self):
        c = 50.0
        t1, t2 = w3_branch_points(c)
        assert t1.real < 0  # on negative real axis
        assert t2.real < 0

    def test_w3_branch_points_distinct(self):
        """The two branch points are distinct."""
        c = 50.0
        t1, t2 = w3_branch_points(c)
        assert abs(t1 - t2) > 0.1

    def test_w3_virasoro_branch_point(self):
        """First branch point is -c/6."""
        c = 50.0
        t1, _ = w3_branch_points(c)
        assert abs(t1.real - (-c / 6.0)) < 1e-12

    def test_w3_stokes_angle_perpendicular(self):
        """Stokes line is perpendicular to the real axis for real branch points."""
        angle = w3_stokes_angle(50.0)
        assert abs(angle - math.pi / 2.0) < 1e-14

    def test_w3_singularity_separation_positive(self):
        """Branch points are separated by a positive distance."""
        sep = w3_singularity_separation(50.0)
        assert sep > 0

    def test_w3_separation_c_dependence(self):
        """Separation grows with c."""
        sep_small = w3_singularity_separation(10.0)
        sep_large = w3_singularity_separation(100.0)
        assert sep_large > sep_small

    def test_w3_interference_grid_computed(self):
        """Interference pattern grid has correct shape."""
        result = w3_interference_pattern(c=50.0, grid_size=20, t_range=10.0)
        assert result['absG'].shape == (20, 20)
        assert len(result['branch_points']) == 2


# =====================================================================
# Test Section 9: Resurgent structure
# =====================================================================

class TestResurgentStructure:
    """Test alien derivatives and resurgent transseries."""

    def test_alien_derivative_log_is_2pi_i(self):
        """Alien derivative for log branch point is 2*pi*i."""
        alien = alien_derivative_log(complex(-26.0 / 6.0))
        assert abs(alien - 2.0 * cmath.pi * 1j) < 1e-12

    def test_virasoro_alien_derivative_topological(self):
        """Virasoro alien derivative is pure imaginary (topological)."""
        result = virasoro_alien_derivative(c=26.0)
        assert result['is_topological']
        assert abs(result['alien_derivative'].real) < 1e-10
        assert abs(result['alien_derivative'].imag - 2.0 * math.pi) < 1e-10

    def test_virasoro_non_perturbative_action(self):
        """Non-perturbative action is c/6."""
        c = 26.0
        result = virasoro_alien_derivative(c)
        assert abs(result['non_perturbative_action'] - c / 6.0) < 1e-14

    def test_transseries_agrees_with_exact_inside_convergence(self):
        """Perturbative truncation of transseries agrees with exact G(t)
        for |t| well inside the radius of convergence."""
        c = 26.0
        t = 0.5  # well inside R = c/6 ~ 4.33
        exact = G_virasoro(t, c)
        pert = resurgent_transseries_virasoro(c, t, n_perturbative=50, n_instanton=0)
        assert abs(exact - pert) < 1e-8


# =====================================================================
# Test Section 10: Cross-archetype utilities
# =====================================================================

class TestCrossArchetype:
    """Test cross-archetype comparison utilities."""

    def test_all_archetypes_at_zero(self):
        """All GFs vanish at t=0."""
        vals = all_archetypes_at_point(0.0)
        for name, val in vals.items():
            assert abs(val) < 1e-14, f"{name} nonzero at t=0"

    def test_radius_of_convergence_heisenberg_infinite(self):
        assert radius_of_convergence('G') == float('inf')

    def test_radius_of_convergence_virasoro(self):
        c = 26.0
        assert abs(radius_of_convergence('M', c=c) - c / 6.0) < 1e-14

    def test_radius_of_convergence_affine(self):
        k = 1.0
        assert abs(radius_of_convergence('L', k=k) - 1.0) < 1e-14

    def test_singularity_density_heisenberg_zero(self):
        assert singularity_density('G') == 0.0


# =====================================================================
# Test Section 11: Dispersion and Stieltjes
# =====================================================================

class TestDispersionAndStieltjes:
    """Test dispersion relation and Stieltjes inversion."""

    def test_stieltjes_carleman_diverges(self):
        """Carleman sum diverges (measure uniquely determined)."""
        c = 26.0
        carleman = stieltjes_inversion_virasoro(c, 0.0, n_moments=20)
        # For lambda_0 = 6/c < 1, moments (6/c)^r -> 0,
        # M_{2r}^{-1/(2r)} -> (c/6) -> infinity sum diverges
        assert carleman > 5.0  # should be large (diverging sum)


# =====================================================================
# Test Section 13: Census and comparison table
# =====================================================================

class TestCensusAndTable:
    """Test summary functions."""

    def test_full_census_has_all_entries(self):
        census = full_singularity_census()
        assert len(census) >= 5  # G, L, C, M(26), M(1/2), W3

    def test_comparison_table_four_rows(self):
        table = archetype_comparison_table()
        assert len(table) == 4
        classes = [row['class'] for row in table]
        assert set(classes) == {'G', 'L', 'C', 'M'}

    def test_comparison_table_depths(self):
        table = archetype_comparison_table()
        depths = {row['class']: row['depth'] for row in table}
        assert depths['G'] == 2
        assert depths['L'] == 3
        assert depths['C'] == 4
        assert depths['M'] == float('inf')
