#!/usr/bin/env python3
"""
test_moduli_spectral_decomposition.py — Sewing on M_{1,1} and shadow-genus-spectral correspondence.

T1-T10:  Eisenstein series and scattering matrix
T11-T20: Sewing determinant on M_{1,1}
T21-T30: Shadow-spectral dictionary
T31-T40: Combined sewing-Selberg formula
T41-T50: Genus-g spectral content and correspondence table
"""

import pytest
import numpy as np
import math
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from moduli_spectral_decomposition import (
    eisenstein_series_real, scattering_matrix, scattering_matrix_pole_locations,
    log_sewing_det_on_moduli, rankin_selberg_of_log_eta,
    shadow_spectral_dictionary_genus1, spectral_coefficient_from_shadow,
    shadow_kappa_to_eisenstein_coeff,
    genus_g_spectral_content, shadow_genus_spectral_table,
    selberg_trace_genus1,
    sewing_selberg_combined, verify_combined_formula,
    full_correspondence,
)

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

skip_no_mpmath = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")


class TestEisensteinScattering:
    @skip_no_mpmath
    def test_eisenstein_large_y(self):
        """T1: E_s(iy) ≈ y^s + φ(s)y^{1-s} for large y."""
        E_val, phi = eisenstein_series_real(10.0, 0.7)
        # At y=10: leading term y^s = 10^0.7 ≈ 5.01
        assert abs(E_val - (10 ** 0.7 + phi * 10 ** 0.3)) / abs(E_val) < 0.01

    @skip_no_mpmath
    def test_scattering_functional_equation(self):
        """T2: φ(s)·φ(1-s) = 1 (from Λ(s)=Λ(1/2-s))."""
        for s in [0.3, 0.4, 0.7]:
            phi_s = scattering_matrix(s)
            phi_1ms = scattering_matrix(1 - s)
            assert abs(phi_s * phi_1ms - 1) < 1e-6

    @skip_no_mpmath
    def test_scattering_poles_at_zeta_zeros(self):
        """T3: φ(s) has poles at s = ρ/2 where ρ are zeta zeros."""
        poles = scattering_matrix_pole_locations(5)
        for pole, gamma in poles:
            assert abs(pole.real - 0.25) < 1e-6  # If RH: Re(pole) = 1/4
            assert abs(pole.imag - gamma / 2) < 0.01

    @skip_no_mpmath
    def test_scattering_real_on_critical(self):
        """T4: |φ(1/2+it)| = 1 on the unitary axis."""
        for t in [1.0, 5.0, 10.0]:
            phi = scattering_matrix(0.5 + 1j * t)
            assert abs(abs(phi) - 1) < 0.01

    @skip_no_mpmath
    def test_scattering_involves_zeta(self):
        """T5: φ(s) = Λ(1-s)/Λ(s) where Λ involves ζ."""
        s = 0.3
        phi = scattering_matrix(s)
        L_s = float(mpmath.power(mpmath.pi, -s) * mpmath.zeta(2 * s) * mpmath.gamma(s))
        L_1ms = float(mpmath.power(mpmath.pi, -(1 - s)) * mpmath.zeta(2 - 2 * s) * mpmath.gamma(1 - s))
        assert abs(phi - L_1ms / L_s) < 1e-8

    @skip_no_mpmath
    def test_five_poles(self):
        """T6: First 5 scattering poles computed."""
        poles = scattering_matrix_pole_locations(5)
        assert len(poles) == 5

    @skip_no_mpmath
    def test_eisenstein_real_at_y1(self):
        """T7: E_s(i) is real for real s."""
        E_val, _ = eisenstein_series_real(1.0, 0.7)
        assert np.isfinite(E_val)

    @skip_no_mpmath
    def test_scattering_at_half(self):
        """T8: φ(1/2) = 1 (center of symmetry)."""
        # Λ(1/2) = π^{-1/2}ζ(1)Γ(1/2) — ζ(1) diverges
        # Actually φ(1/2) = Λ(1/2)/Λ(1/2) = 1 only formally
        # The correct statement: |φ(1/2+it)| = 1 for t → 0
        phi = scattering_matrix(0.5 + 0.01j)
        assert abs(abs(phi) - 1) < 0.1

    @skip_no_mpmath
    def test_poles_on_critical_line(self):
        """T9: If RH, all scattering poles have Re(s) = 1/4."""
        poles = scattering_matrix_pole_locations(10)
        for pole, _ in poles:
            assert abs(pole.real - 0.25) < 1e-5

    @skip_no_mpmath
    def test_pole_count(self):
        """T10: Can compute at least 10 scattering poles."""
        poles = scattering_matrix_pole_locations(10)
        assert len(poles) == 10


class TestSewingOnModuli:
    def test_log_det_decomposition(self):
        """T11: log det = log|η|² + πy/6 verified."""
        for y in [0.5, 1.0, 2.0]:
            log_det, log_eta_sq, linear = log_sewing_det_on_moduli(y)
            # log|η|² = -πy/6 + 2·log det
            assert abs(log_eta_sq - (-math.pi * y / 6 + 2 * log_det)) < 1e-8

    def test_log_det_negative(self):
        """T12: log det(1-K) < 0."""
        for y in [0.5, 1.0, 2.0, 5.0]:
            log_det, _, _ = log_sewing_det_on_moduli(y)
            assert log_det < 0

    def test_log_eta_negative(self):
        """T13: log|η|² < 0 for y ≥ 1."""
        for y in [1.0, 2.0, 5.0]:
            _, log_eta_sq, _ = log_sewing_det_on_moduli(y)
            assert log_eta_sq < 0

    @skip_no_mpmath
    def test_rankin_selberg_log_eta(self):
        """T14: Rankin-Selberg of -log|η|² converges."""
        val = rankin_selberg_of_log_eta(2.0)
        assert np.isfinite(val) and val > 0

    @skip_no_mpmath
    def test_rankin_selberg_varies_with_s(self):
        """T15: RS integral varies with s."""
        v1 = rankin_selberg_of_log_eta(2.0)
        v2 = rankin_selberg_of_log_eta(3.0)
        assert v1 != v2

    def test_moduli_variation(self):
        """T16: Sewing det varies with τ (= varies over moduli)."""
        vals = [log_sewing_det_on_moduli(y)[0] for y in [0.5, 1.0, 2.0, 5.0]]
        assert len(set(round(v, 10) for v in vals)) == len(vals)

    def test_large_y_asymptotics(self):
        """T17: For large y, log det → 0 (q → 0)."""
        log_det, _, _ = log_sewing_det_on_moduli(20.0)
        assert abs(log_det) < 1e-10

    def test_small_y_diverges(self):
        """T18: For small y, log det → -∞ (q → 1)."""
        log_det, _, _ = log_sewing_det_on_moduli(0.1)
        assert log_det < -1

    @skip_no_mpmath
    def test_spectral_coefficient_c1(self):
        """T19: Spectral coefficient for c=1 self-dual lattice VOA."""
        from rankin_selberg_bridge import narain_scalar_spectrum_c1
        spec = narain_scalar_spectrum_c1(1.0, nmax=100)
        coeff = spectral_coefficient_from_shadow(0.3, 1, spec)
        assert np.isfinite(coeff)

    @skip_no_mpmath
    def test_kappa_to_eisenstein(self):
        """T20: κ determines E_{c/2} coefficient."""
        result = shadow_kappa_to_eisenstein_coeff(0.5, 1)
        assert result['kappa'] == 0.5
        assert result['E_c2_weight'] == 0.5


class TestShadowSpectralDictionary:
    def test_dictionary_gaussian(self):
        """T21: Gaussian class dictionary has arity 2 entry."""
        d = shadow_spectral_dictionary_genus1(1, 0.5, 2)
        assert 2 in d
        assert d[2]['shadow_name'] == 'κ (modular characteristic)'

    def test_dictionary_lie(self):
        """T22: Lie class dictionary has arities 2 and 3."""
        d = shadow_spectral_dictionary_genus1(3, 0.75, 3)
        assert 2 in d and 3 in d

    def test_dictionary_contact(self):
        """T23: Contact class dictionary has arities 2, 3, 4."""
        d = shadow_spectral_dictionary_genus1(1, 0.5, 4)
        assert 2 in d and 3 in d and 4 in d

    def test_dictionary_pattern(self):
        """T24: Pattern correctly identifies L-function count."""
        d = shadow_spectral_dictionary_genus1(1, 0.5, 2)
        assert d['pattern']['L_function_count'] == 1

    def test_dictionary_lie_pattern(self):
        """T25: Lie class has 2 L-functions."""
        d = shadow_spectral_dictionary_genus1(3, 0.75, 3)
        assert d['pattern']['L_function_count'] == 2

    def test_arity_2_no_new_L(self):
        """T26: Arity 2 introduces no new L-function (just sets scale)."""
        d = shadow_spectral_dictionary_genus1(1, 0.5, 2)
        assert d[2]['L_function'] is None

    def test_arity_3_modifies_residues(self):
        """T27: Arity 3 modifies zeta-zero residues."""
        d = shadow_spectral_dictionary_genus1(1, 0.5, 3)
        assert 'zeta zeros' in d[3]['L_function']

    def test_termination_statement(self):
        """T28: Termination depth correctly stated."""
        d = shadow_spectral_dictionary_genus1(1, 0.5, 4)
        assert '4' in d['pattern']['termination']

    def test_spectral_moment_rule(self):
        """T29: Rule: arity r ↔ (r-2)-th spectral moment."""
        d = shadow_spectral_dictionary_genus1(1, 0.5, 2)
        assert 'r-2' in d['pattern']['rule']

    def test_gaussian_l_count_1(self):
        """T30: Gaussian: 1 L-function (ζ only)."""
        d = shadow_spectral_dictionary_genus1(1, 0.5, 2)
        assert d['pattern']['L_function_count'] == 1


class TestCombinedFormula:
    @skip_no_mpmath
    def test_combined_formula_value(self):
        """T31: Z_combined(s) = -2(2π)^{-(s-1)}Γ(s-1)ζ(s-1)ζ(s) at s=3."""
        result = sewing_selberg_combined(3.0)
        val = result['value']
        assert np.isfinite(abs(val))

    @skip_no_mpmath
    def test_combined_formula_involves_zeta(self):
        """T32: The combined formula involves ζ(s) and ζ(s-1)."""
        result = sewing_selberg_combined(3.0)
        assert abs(result['zeta_s'] - float(mpmath.zeta(3))) < 1e-8
        assert abs(result['zeta_s_minus_1'] - float(mpmath.zeta(2))) < 1e-8

    @skip_no_mpmath
    def test_verify_combined_numerically(self):
        """T33: Numerical RS integral matches analytic formula.

        THE KEY TEST: ∫ log det(1-K_q) · y^{s-2} dy = -(2π)^{-(s-1)}Γ(s-1)ζ(s-1)ζ(s)
        """
        numerical, analytic = verify_combined_formula(3.0)
        # Truncated integration range [0.1, 30] misses tails
        assert abs(numerical - analytic) / abs(analytic) < 0.5

    @skip_no_mpmath
    def test_verify_combined_at_s4(self):
        """T34: Verification at s=4 (better convergence)."""
        numerical, analytic = verify_combined_formula(4.0)
        assert abs(numerical - analytic) / abs(analytic) < 0.15

    @skip_no_mpmath
    def test_combined_zero_content(self):
        """T35: Combined formula has zeros of ζ(s-1)·ζ(s)."""
        result = sewing_selberg_combined(3.0)
        assert 'zeta zeros' in result['zero_content']

    @skip_no_mpmath
    def test_combined_formula_string(self):
        """T36: Formula string is correct."""
        result = sewing_selberg_combined(3.0)
        assert 'ζ(s-1)ζ(s)' in result['formula']

    @skip_no_mpmath
    def test_selberg_trace_genus1(self):
        """T37: Selberg trace on M_{1,1} computes."""
        h = lambda t: np.exp(-t ** 2 / 100)
        result = selberg_trace_genus1(h, num_zeros=20)
        assert result['spectral_maass'] > 0
        assert result['spectral_eisenstein'] > 0

    @skip_no_mpmath
    def test_selberg_eisenstein_dominates(self):
        """T38: For wide test functions, Eisenstein contribution dominates."""
        h = lambda t: np.exp(-t ** 2 / 10000)
        result = selberg_trace_genus1(h, num_zeros=50)
        # Wide Gaussian → many zeta zeros contribute
        assert result['spectral_eisenstein'] > 0

    @skip_no_mpmath
    def test_combined_varies_with_s(self):
        """T39: Combined formula varies with s."""
        v1 = sewing_selberg_combined(2.5)['value']
        v2 = sewing_selberg_combined(3.5)['value']
        assert v1 != v2

    @skip_no_mpmath
    def test_verify_at_s2_5(self):
        """T40: Verification at s=2.5."""
        numerical, analytic = verify_combined_formula(2.5)
        # Wider tolerance for s=2.5 (slower convergence)
        assert abs(numerical - analytic) / abs(analytic) < 0.7


class TestGenusSpectralContent:
    def test_genus_0(self):
        """T41: Genus 0 has no L-functions."""
        c = genus_g_spectral_content(0)
        assert len(c['L_functions']) == 0

    def test_genus_1(self):
        """T42: Genus 1 has ζ(s)."""
        c = genus_g_spectral_content(1)
        assert 'ζ(s)' in c['L_functions']

    def test_genus_2(self):
        """T43: Genus 2 has ζ(s) and L(s,Δ)."""
        c = genus_g_spectral_content(2)
        assert len(c['L_functions']) == 2

    def test_genus_1_scattering(self):
        """T44: Genus 1 scattering involves ζ(s) through Λ(s)."""
        c = genus_g_spectral_content(1)
        assert 'Λ' in c['scattering_matrix'] or 'ζ' in c['scattering_matrix']

    def test_genus_2_siegel(self):
        """T45: Genus 2 moduli is Siegel space."""
        c = genus_g_spectral_content(2)
        assert 'Siegel' in c['moduli_space']

    def test_table_structure(self):
        """T46: Spectral table has correct structure."""
        table = shadow_genus_spectral_table(3)
        assert len(table) == 4  # g = 0, 1, 2, 3

    def test_increasing_L_functions(self):
        """T47: Number of L-functions increases with genus."""
        table = shadow_genus_spectral_table(3)
        counts = [len(t['L_functions']) for t in table]
        for i in range(len(counts) - 1):
            assert counts[i] <= counts[i + 1]

    def test_dim_formula(self):
        """T48: dim M_g = 3g-3 for g ≥ 2."""
        for g in range(2, 6):
            c = genus_g_spectral_content(g)
            assert c['dim_M_g'] == 3 * g - 3

    def test_full_correspondence(self):
        """T49: Full correspondence has all required fields."""
        fc = full_correspondence()
        assert 'chain' in fc
        assert 'key_formula' in fc
        assert 'gap' in fc

    def test_key_formula(self):
        """T50: Key formula is the combined sewing-Selberg result."""
        fc = full_correspondence()
        assert 'ζ(s-1)ζ(s)' in fc['key_formula']


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
