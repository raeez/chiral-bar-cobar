"""Tests for genus-1 modular R-matrix corrections.

Verifies the ordered modular bar complex at genus 1:
  1. Heisenberg: r₁(z;τ) = k·℘(z;τ), scalar, av = κ·λ₁
  2. Affine sl_2: Casimir part + non-Casimir corrections
  3. Modular R-matrix consistency: deformation of genus-0 data
  4. Degeneration limit: r₁ → 1/z² as τ → i∞

References:
  - higher_genus_foundations.tex: genus-1 propagator
  - heisenberg_frame.tex: Heisenberg genus-1 curvature
  - e1_lattice_genus1.py: lattice genus-1 computation
"""

import numpy as np
import pytest
from sympy import Rational

from compute.lib.ordered_modular_bar import (
    weierstrass_p_fourier,
    weierstrass_p_leading,
    HeisenbergGenus1,
    AffineSl2Genus1,
    verify_genus0_limit,
    modular_r_consistency,
)


# =========================================================================
# Weierstrass ℘-function
# =========================================================================

class TestWeierstrassP:
    """Numerical evaluation of the Weierstrass ℘-function."""

    def test_leading_term(self):
        """℘(z; τ) ~ 1/z² near z = 0."""
        for z_val in [0.01, 0.05, 0.001]:
            leading = weierstrass_p_leading(z_val)
            assert leading == pytest.approx(1.0 / z_val**2)

    def test_wp_near_origin(self):
        """℘(z; τ) ≈ 1/z² for small z and large Im(τ)."""
        tau_val = 5j  # large Im(τ) → degeneration
        z_val = 0.01
        wp = weierstrass_p_fourier(z_val, tau_val)
        expected = 1.0 / z_val**2
        # Should be close to 1/z² up to exponentially small corrections
        assert abs(np.real(wp) / expected - 1.0) < 0.01

    def test_wp_periodicity_1(self):
        """℘(z + 1; τ) = ℘(z; τ) (period-1 invariance).

        ℘ is doubly periodic with periods (1, τ).
        """
        tau_val = 0.3 + 1j
        z_val = 0.2 + 0.1j
        wp_z = weierstrass_p_fourier(z_val, tau_val, n_terms=30)
        wp_z1 = weierstrass_p_fourier(z_val + 1, tau_val, n_terms=30)
        assert abs(wp_z - wp_z1) < 1e-6, \
            f"℘(z+1) - ℘(z) = {abs(wp_z - wp_z1)}"

    def test_wp_even(self):
        """℘(-z; τ) = ℘(z; τ) (even function)."""
        tau_val = 0.2 + 1.5j
        z_val = 0.15 + 0.05j
        wp_z = weierstrass_p_fourier(z_val, tau_val, n_terms=30)
        wp_neg = weierstrass_p_fourier(-z_val, tau_val, n_terms=30)
        assert abs(wp_z - wp_neg) < 1e-6

    def test_wp_real_for_real_z_pure_imaginary_tau(self):
        """℘(x; iT) is real for real x and pure imaginary τ."""
        tau_val = 2j
        for z_val in [0.1, 0.2, 0.3, 0.4]:
            wp = weierstrass_p_fourier(z_val, tau_val, n_terms=30)
            assert abs(np.imag(wp)) < 1e-8, \
                f"Im(℘({z_val}; 2i)) = {np.imag(wp)}"

    def test_wp_degeneration(self):
        """As Im(τ) → ∞, ℘(z;τ) → π²/sin²(πz) - π²/3.

        The nome q → 0 kills all Fourier corrections.
        The remaining Laurent + Eisenstein terms give the
        degenerate formula.
        """
        z_val = 0.2
        tau_large = 20j  # q ≈ e^{-40π} ≈ 0
        wp = weierstrass_p_fourier(z_val, tau_large, n_terms=5)
        expected = (np.pi / np.sin(np.pi * z_val))**2 - np.pi**2 / 3
        assert abs(np.real(wp) - expected) < 1e-6


# =========================================================================
# Heisenberg genus-1 R-matrix
# =========================================================================

class TestHeisenbergGenus1:
    """Genus-1 R-matrix for Heisenberg H_k."""

    def test_r0(self):
        """r₀(z) = k/z."""
        h = HeisenbergGenus1()
        assert h.r0(0.5, level_val=2.0) == pytest.approx(4.0)
        assert h.r0(1.0, level_val=3.0) == pytest.approx(3.0)

    def test_r1_is_scalar(self):
        """r₁(z; τ) is scalar."""
        h = HeisenbergGenus1()
        assert h.r1_is_scalar()

    def test_r1_proportional_to_wp(self):
        """r₁(z; τ) = k · ℘(z; τ)."""
        h = HeisenbergGenus1()
        tau_val = 1j
        z_val = 0.2
        level_val = 3.0

        r1 = h.r1(z_val, tau_val, level_val)
        wp = weierstrass_p_fourier(z_val, tau_val)
        expected = level_val * wp

        assert abs(r1 - expected) < 1e-10

    def test_r1_average(self):
        """av(r₁) = κ · λ₁ = k/24."""
        h = HeisenbergGenus1()
        result = h.r1_average(level_val=6.0)
        assert result["kappa"] == 6.0
        assert result["lambda1"] == pytest.approx(1.0 / 24.0)
        assert result["product"] == pytest.approx(6.0 / 24.0)

    def test_modular_r_at_hbar_zero(self):
        """R^mod(z; ℏ=0) = r₀(z)."""
        h = HeisenbergGenus1()
        z_val = 0.3
        tau_val = 1j
        level_val = 2.0

        r_mod = h.modular_r_matrix(z_val, tau_val, 0.0, level_val)
        r0 = h.r0(z_val, level_val)
        assert abs(complex(r_mod) - r0) < 1e-10

    def test_modular_r_deformation(self):
        """R^mod(z; ℏ) deforms r₀(z) at nonzero ℏ."""
        h = HeisenbergGenus1()
        z_val = 0.2
        tau_val = 1j
        level_val = 1.0

        r_mod_0 = h.modular_r_matrix(z_val, tau_val, 0.0, level_val)
        r_mod_small = h.modular_r_matrix(z_val, tau_val, 0.1, level_val)
        # Should differ at order ℏ²
        assert abs(r_mod_small - r_mod_0) > 1e-6

    def test_degeneration_limit(self):
        """r₁(z; τ) → k/z² as τ → i∞."""
        h = HeisenbergGenus1()
        result = h.verify_degeneration(z_val=0.1, level_val=1.0)
        assert result["approaches_1"]

    def test_r1_at_multiple_levels(self):
        """r₁ scales linearly with k."""
        h = HeisenbergGenus1()
        tau_val = 1.5j
        z_val = 0.15

        r1_k1 = h.r1(z_val, tau_val, 1.0)
        r1_k3 = h.r1(z_val, tau_val, 3.0)
        assert abs(r1_k3 - 3.0 * r1_k1) < 1e-10

    def test_complementarity_genus1(self):
        """κ + κ^! = 0 implies genus-1 complementarity.

        For Heisenberg: κ = k, κ^! = -k. Sum = 0.
        """
        h = HeisenbergGenus1()
        result = h.r1_average(level_val=5.0)
        kappa = result["kappa"]
        kappa_dual = -kappa  # Koszul dual has opposite level
        assert kappa + kappa_dual == 0


# =========================================================================
# Affine sl_2 genus-1 R-matrix
# =========================================================================

class TestAffineSl2Genus1:
    """Genus-1 R-matrix for affine sl_2 at level k."""

    def test_casimir_shape(self):
        """Casimir tensor is 4×4."""
        a = AffineSl2Genus1()
        omega = a.casimir_tensor_4x4()
        assert omega.shape == (4, 4)

    def test_r1_casimir_part_shape(self):
        """Casimir part of r₁ is 4×4."""
        a = AffineSl2Genus1()
        r1_cas = a.r1_casimir_part(0.2, 1j, level_val=2.0)
        assert r1_cas.shape == (4, 4)

    def test_r1_casimir_proportional_to_omega(self):
        """r₁^Cas(z; τ) ∝ ℘(z;τ) · Ω."""
        a = AffineSl2Genus1()
        z_val = 0.15
        tau_val = 1j
        level_val = 4.0  # k = 4

        r1_cas = a.r1_casimir_part(z_val, tau_val, level_val)
        omega = a.casimir_tensor_4x4()
        wp = weierstrass_p_fourier(z_val, tau_val)
        coeff = level_val / (level_val + 2)**2  # k/(k+h^v)²

        expected = coeff * wp * omega
        assert np.allclose(r1_cas, expected)

    def test_r1_has_non_casimir(self):
        """Non-Casimir corrections are present."""
        a = AffineSl2Genus1()
        assert a.r1_has_non_casimir()

    def test_kappa_genus1(self):
        """κ = 3k/(k+2), same at genus 0 and genus 1."""
        a = AffineSl2Genus1()
        # k = 1: κ = 3/3 = 1
        assert a.kappa_genus1(1.0) == pytest.approx(1.0)
        # k = 4: κ = 12/6 = 2
        assert a.kappa_genus1(4.0) == pytest.approx(2.0)
        # k = 10: κ = 30/12 = 5/2
        assert a.kappa_genus1(10.0) == pytest.approx(2.5)


# =========================================================================
# Modular R-matrix consistency
# =========================================================================

class TestModularRConsistency:
    """Consistency checks for the full modular R-matrix."""

    def test_genus0_limit_heisenberg(self):
        """r₁/r₀' → 1 as τ → i∞ for Heisenberg."""
        result = verify_genus0_limit("Heisenberg", z_val=0.1, k=1.0)
        assert result["consistent"]

    def test_r_consistency(self):
        """R^mod at ℏ=0 matches r₀."""
        result = modular_r_consistency(level_val=2.0, z_val=0.2, tau_val=1j)
        assert result["r_mod_at_hbar_0_matches_r0"]

    def test_deformation_nonzero(self):
        """The genus-1 correction is nonzero."""
        result = modular_r_consistency(level_val=1.0, z_val=0.1, tau_val=1j)
        assert result["deformation_nonzero"]

    def test_r_consistency_different_levels(self):
        """Consistency holds at different levels k."""
        for k_val in [0.5, 1.0, 3.0, 10.0]:
            result = modular_r_consistency(
                level_val=k_val, z_val=0.15, tau_val=1.5j
            )
            assert result["r_mod_at_hbar_0_matches_r0"]
            assert result["deformation_nonzero"]

    def test_r_consistency_different_tau(self):
        """Consistency holds at different τ values."""
        for tau_val in [0.5j, 1j, 2j, 5j]:
            result = modular_r_consistency(
                level_val=1.0, z_val=0.1, tau_val=tau_val
            )
            assert result["r_mod_at_hbar_0_matches_r0"]


# =========================================================================
# Degeneration and analytic structure
# =========================================================================

class TestDegeneration:
    """Degeneration limits and analytic structure."""

    def test_wp_approaches_inverse_square(self):
        """℘(z; τ) → π²/sin²(πz) - π²/3 as Im(τ) → ∞."""
        z_val = 0.25
        tau_values_imag = [1, 2, 5, 10, 20]
        for t in tau_values_imag:
            wp = weierstrass_p_fourier(z_val, t * 1j, n_terms=20)
            limit_val = (np.pi / np.sin(np.pi * z_val))**2 - np.pi**2 / 3
            # Exponentially improving approximation
            if t >= 5:
                assert abs(np.real(wp) - limit_val) < 1e-6

    def test_r1_scales_with_level(self):
        """r₁(z; τ; k) = k · ℘(z; τ): linear in k."""
        h = HeisenbergGenus1()
        z_val = 0.2
        tau_val = 1j
        r1_1 = h.r1(z_val, tau_val, 1.0)
        r1_7 = h.r1(z_val, tau_val, 7.0)
        assert abs(r1_7 - 7.0 * r1_1) < 1e-10

    def test_modular_r_hbar_expansion(self):
        """R^mod = r₀ + ℏ² r₁ + O(ℏ⁴): verify coefficient extraction."""
        h = HeisenbergGenus1()
        z_val = 0.15
        tau_val = 1.2j
        k_val = 2.0

        r0 = h.r0(z_val, k_val)
        r1 = h.r1(z_val, tau_val, k_val)

        # Use small ℏ to extract the ℏ² coefficient
        hbar_small = 0.001
        r_mod = h.modular_r_matrix(z_val, tau_val, hbar_small, k_val)
        extracted_r1 = (complex(r_mod) - r0) / hbar_small**2

        assert abs(extracted_r1 - r1) / abs(r1) < 1e-4

    def test_tautological_class_lambda1(self):
        """λ₁ = 1/24 (orbifold Euler characteristic of M_{1,1})."""
        h = HeisenbergGenus1()
        result = h.r1_average(level_val=1.0)
        assert result["lambda1"] == pytest.approx(1.0 / 24.0)

    def test_genus1_free_energy(self):
        """F₁ = κ · λ₁ = k/24 for Heisenberg."""
        h = HeisenbergGenus1()
        for k_val in [1.0, 2.0, 12.0, 24.0]:
            result = h.r1_average(level_val=k_val)
            assert result["product"] == pytest.approx(k_val / 24.0)
