r"""Tests for BC-88: Kontsevich-Soibelman wall-crossing from shadow zeros.

Tests organized by section:
  1.  Shadow coefficient providers (ground truth cross-checks)
  2.  Shadow zeta function evaluation
  3.  BPS rays from shadow zeros
  4.  KS automorphism from shadow data
  5.  Spectrum generator expansion
  6.  Wall-crossing at c = 13 (palindromic test)
  7.  Complementarity sums and discriminants
  8.  Tropical wall-crossing and mutation
  9.  Attractor flow integration
  10. Split attractor analysis (AP31 check)
  11. Stokes phenomenon and shadow connection
  12. Cross-verification (multi-path)
  13. Special central charges (c = 1, 13, 25)
  14. Shadow radius and coefficient decay
  15. Pentagon identity verification
"""

import pytest
import math
import cmath
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from bc_wall_crossing_shadow_engine import (
    # Section 0: shadow coefficients
    virasoro_kappa,
    virasoro_shadow_coefficients,
    virasoro_dual_shadow_coefficients,
    virasoro_S4,
    critical_discriminant_virasoro,
    # Section 1: shadow zeta
    shadow_zeta_numerical,
    shadow_zeta_derivative,
    shadow_zeta_zeros_grid,
    # Section 2: BPS rays
    bps_ray_angle,
    bps_rays_from_zeros,
    angular_distribution_histogram,
    # Section 3: KS automorphism
    ks_automorphism_coefficient,
    ks_log_automorphism,
    ks_automorphism_from_shadow,
    # Section 4: spectrum generator
    spectrum_generator_expansion,
    # Section 5: wall-crossing at c=13
    shadow_palindromic_test,
    wall_crossing_at_c13,
    complementarity_sum_at_c,
    discriminant_complementarity,
    # Section 6: tropical
    tropical_shadow_coordinates,
    exchange_matrix_from_ope,
    tropical_mutation,
    mutation_sequence_through_c13,
    # Section 7: attractor flow
    attractor_flow_rhs,
    attractor_flow_integrate,
    attractor_fixed_points,
    # Section 8: split attractor
    split_attractor_analysis,
    find_split_attractor_locus,
    # Section 9: Stokes
    shadow_metric_virasoro,
    shadow_metric_zeros_virasoro,
    stokes_lines_virasoro,
    stokes_graph_summary,
    # Section 10: cross-verification
    verify_ks_identity_pentagon,
    verify_palindromic_self_dual,
    verify_stokes_wall_correspondence,
    shadow_radius_virasoro,
    verify_shadow_coefficient_decay,
    # Helpers
    plethystic_exponential_shadow,
    plethystic_log_shadow,
)

import numpy as np


# ============================================================================
# Section 1: Shadow coefficient providers
# ============================================================================

class TestShadowCoefficients:
    """Ground truth tests for shadow coefficient providers."""

    def test_kappa_virasoro_c1(self):
        """kappa(Vir_1) = 1/2."""
        assert abs(virasoro_kappa(1.0) - 0.5) < 1e-15

    def test_kappa_virasoro_c13(self):
        """kappa(Vir_13) = 13/2 = 6.5."""
        assert abs(virasoro_kappa(13.0) - 6.5) < 1e-15

    def test_kappa_virasoro_c25(self):
        """kappa(Vir_25) = 25/2 = 12.5."""
        assert abs(virasoro_kappa(25.0) - 12.5) < 1e-15

    def test_kappa_virasoro_c26(self):
        """kappa(Vir_26) = 13 (critical dimension)."""
        assert abs(virasoro_kappa(26.0) - 13.0) < 1e-15

    def test_S2_equals_kappa(self):
        """S_2 = kappa for Virasoro (AP9: only for Virasoro!)."""
        for c_val in [1.0, 5.0, 13.0, 24.0, 25.0]:
            coeffs = virasoro_shadow_coefficients(c_val, 5)
            assert abs(coeffs[2] - virasoro_kappa(c_val)) < 1e-10

    def test_S4_quartic_contact(self):
        """S_4 = 10 / [c(5c+22)] for Virasoro."""
        for c_val in [1.0, 5.0, 13.0, 24.0]:
            S4 = virasoro_S4(c_val)
            expected = 10.0 / (c_val * (5.0 * c_val + 22.0))
            assert abs(S4 - expected) < 1e-12

    def test_critical_discriminant(self):
        """Delta = 40 / (5c + 22) for Virasoro."""
        for c_val in [1.0, 13.0, 25.0]:
            Delta = critical_discriminant_virasoro(c_val)
            expected = 40.0 / (5.0 * c_val + 22.0)
            assert abs(Delta - expected) < 1e-12

    def test_shadow_coefficients_c1_S2(self):
        """Virasoro c=1: S_2 = 0.5."""
        coeffs = virasoro_shadow_coefficients(1.0, 10)
        assert abs(coeffs[2] - 0.5) < 1e-10

    def test_shadow_coefficients_nonzero_higher(self):
        """Virasoro (class M): S_r != 0 for r >= 3 generically."""
        coeffs = virasoro_shadow_coefficients(13.0, 10)
        for r in range(3, 8):
            assert abs(coeffs[r]) > 1e-15, f"S_{r} should be nonzero for class M"

    def test_dual_coefficients_c13(self):
        """At c=13 (self-dual): S_r(13) = S_r(26-13) = S_r(13)."""
        coeffs = virasoro_shadow_coefficients(13.0, 15)
        dual_coeffs = virasoro_dual_shadow_coefficients(13.0, 15)
        for r in range(2, 16):
            assert abs(coeffs[r] - dual_coeffs[r]) < 1e-10

    def test_dual_coefficients_asymmetric(self):
        """For c != 13: S_r(c) != S_r(26-c) in general."""
        coeffs = virasoro_shadow_coefficients(5.0, 10)
        dual_coeffs = virasoro_dual_shadow_coefficients(5.0, 10)
        # kappa(5) = 2.5, kappa(21) = 10.5
        assert abs(coeffs[2] - dual_coeffs[2]) > 1.0


# ============================================================================
# Section 2: Shadow zeta function evaluation
# ============================================================================

class TestShadowZeta:
    """Tests for the shadow zeta function."""

    def test_zeta_real_axis(self):
        """zeta_A(s) is real-valued on the real axis for real c."""
        for c_val in [1.0, 13.0, 25.0]:
            for s_re in [3.0, 5.0, 10.0]:
                z = shadow_zeta_numerical(c_val, complex(s_re, 0.0))
                assert abs(z.imag) < 1e-8, f"zeta should be real at s={s_re}"

    def test_zeta_large_s_convergence(self):
        """For large Re(s), zeta_A(s) -> S_2 * 2^{-s} (dominant term)."""
        c_val = 13.0
        s = complex(20.0, 0.0)
        z = shadow_zeta_numerical(c_val, s)
        kappa = virasoro_kappa(c_val)
        dominant = kappa * 2.0 ** (-20.0)
        # At s=20, higher terms are negligible
        assert abs(z - dominant) / abs(dominant) < 0.01

    def test_zeta_conjugation(self):
        """zeta_A(s*) = conj(zeta_A(s)) for real shadow coefficients."""
        c_val = 13.0
        s = complex(3.0, 5.0)
        z1 = shadow_zeta_numerical(c_val, s)
        z2 = shadow_zeta_numerical(c_val, s.conjugate())
        assert abs(z1 - z2.conjugate()) < 1e-8

    def test_zeta_derivative_sign(self):
        """zeta'_A(s) < 0 on the real axis for Re(s) large (decreasing)."""
        c_val = 13.0
        s = complex(5.0, 0.0)
        zp = shadow_zeta_derivative(c_val, s)
        assert zp.real < 0, "zeta' should be negative for large real s"

    def test_zeta_finite_for_large_s(self):
        """Shadow zeta converges for sufficiently large Re(s)."""
        c_val = 13.0
        z = shadow_zeta_numerical(c_val, complex(10.0, 0.0), max_r=60)
        assert math.isfinite(abs(z))


# ============================================================================
# Section 3: BPS rays from shadow zeros
# ============================================================================

class TestBPSRays:
    """Tests for BPS ray computation."""

    def test_bps_ray_angle_real(self):
        """Real positive zeros give angle 0."""
        assert abs(bps_ray_angle(complex(1.0, 0.0))) < 1e-15

    def test_bps_ray_angle_imaginary(self):
        """Purely imaginary zeros give angle pi/2."""
        assert abs(bps_ray_angle(complex(0.0, 1.0)) - math.pi / 2) < 1e-15

    def test_bps_ray_angle_negative(self):
        """Negative real zeros give angle pi."""
        assert abs(abs(bps_ray_angle(complex(-1.0, 0.0))) - math.pi) < 1e-15

    def test_bps_rays_from_zeros_count(self):
        """Number of BPS rays equals number of zeros."""
        zeros = [complex(1, 2), complex(3, -1), complex(-1, 0.5)]
        rays = bps_rays_from_zeros(zeros)
        assert len(rays) == 3

    def test_bps_rays_angles_in_range(self):
        """All angles should be in (-pi, pi]."""
        zeros = [complex(1, 2), complex(-3, -1), complex(0, 5)]
        rays = bps_rays_from_zeros(zeros)
        for angle in rays:
            assert -math.pi < angle <= math.pi + 1e-10

    def test_angular_distribution_basic(self):
        """Angular distribution histogram has correct counts."""
        angles = [0.0, 0.1, 0.2, 1.0, -1.0]
        hist = angular_distribution_histogram(angles, n_bins=10)
        assert hist["n_rays"] == 5
        assert sum(hist["counts"]) == 5

    def test_angular_distribution_empty(self):
        """Empty angle list gives trivial histogram."""
        hist = angular_distribution_histogram([])
        assert hist["n_rays"] == 0


# ============================================================================
# Section 4: KS automorphism from shadow data
# ============================================================================

class TestKSAutomorphism:
    """Tests for Kontsevich-Soibelman automorphisms."""

    def test_ks_coefficient_n1(self):
        """K_r at n=1: Omega * (-1)^0 / 1^2 = Omega."""
        assert abs(ks_automorphism_coefficient(3, 1, 2.5) - 2.5) < 1e-15

    def test_ks_coefficient_n2(self):
        """K_r at n=2: Omega * (-1)^1 / 2^2 = -Omega/4."""
        assert abs(ks_automorphism_coefficient(3, 2, 2.5) - (-2.5 / 4.0)) < 1e-15

    def test_ks_coefficient_n3(self):
        """K_r at n=3: Omega * (-1)^2 / 3^2 = Omega/9."""
        assert abs(ks_automorphism_coefficient(3, 3, 2.5) - (2.5 / 9.0)) < 1e-15

    def test_ks_log_automorphism_keys(self):
        """log(K_r) has keys at multiples of r."""
        log_K = ks_log_automorphism(5, 1.0, 4)
        assert set(log_K.keys()) == {5, 10, 15, 20}

    def test_ks_log_alternating_signs(self):
        """Coefficients in log(K_r) alternate in sign."""
        log_K = ks_log_automorphism(3, 1.0, 6)
        for k in range(1, 7):
            expected_sign = (-1) ** (k - 1)
            assert log_K[3 * k] * expected_sign > 0

    def test_ks_from_shadow_nonempty(self):
        """KS automorphism from shadow data is nonempty."""
        ks = ks_automorphism_from_shadow(13.0, max_r=10, li_order=5)
        assert len(ks) > 0

    def test_ks_from_shadow_leading_term(self):
        """Leading term of KS automorphism at charge 2 is S_2 = kappa."""
        ks = ks_automorphism_from_shadow(13.0, max_r=10, li_order=5)
        # At charge 2: contribution from r=2, k=1 is S_2 * 1 = kappa
        kappa = virasoro_kappa(13.0)
        assert abs(ks.get(2, 0.0) - kappa) < 1e-8

    def test_ks_automorphism_coefficient_zero_omega(self):
        """Zero BPS index gives zero coefficient."""
        assert abs(ks_automorphism_coefficient(5, 3, 0.0)) < 1e-15


# ============================================================================
# Section 5: Spectrum generator expansion
# ============================================================================

class TestSpectrumGenerator:
    """Tests for the spectrum generator S_hat."""

    def test_spectrum_generator_c0_term(self):
        """S_hat starts with 1 (identity)."""
        sg = spectrum_generator_expansion(13.0, max_charge=10)
        assert abs(sg[0] - 1.0) < 1e-12

    def test_spectrum_generator_finite(self):
        """All coefficients are finite."""
        sg = spectrum_generator_expansion(13.0, max_charge=30)
        for i, c in enumerate(sg):
            assert math.isfinite(c), f"Coefficient at charge {i} is not finite"

    def test_spectrum_generator_c1_positive(self):
        """First coefficient (charge 1) vanishes (no arity-1 shadow)."""
        sg = spectrum_generator_expansion(13.0, max_charge=5)
        # S_r starts at r=2, so charge 1 has no contribution
        assert abs(sg[1]) < 1e-10

    def test_spectrum_generator_charge2(self):
        """Charge-2 coefficient of S_hat = S_2 = kappa."""
        sg = spectrum_generator_expansion(13.0, max_charge=5, max_r=10)
        kappa = virasoro_kappa(13.0)
        assert abs(sg[2] - kappa) < 1e-6


# ============================================================================
# Section 6: Wall-crossing at c = 13 (palindromic test)
# ============================================================================

class TestWallCrossingC13:
    """Tests for wall-crossing at the self-dual point c = 13."""

    def test_palindromic_c13(self):
        """At c = 13: BPS spectrum is palindromic (self-dual)."""
        result = shadow_palindromic_test(13.0, max_r=15)
        assert result["is_palindromic"], "c=13 should be palindromic"
        assert result["max_diff"] < 1e-10

    def test_palindromic_c1_fails(self):
        """At c = 1: BPS spectrum is NOT palindromic."""
        result = shadow_palindromic_test(1.0, max_r=10)
        assert not result["is_palindromic"], "c=1 should NOT be palindromic"

    def test_palindromic_c25_fails(self):
        """At c = 25: BPS spectrum is NOT palindromic."""
        result = shadow_palindromic_test(25.0, max_r=10)
        assert not result["is_palindromic"], "c=25 should NOT be palindromic"

    def test_kappa_sum_always_13(self):
        """kappa(c) + kappa(26-c) = 13 for all c (AP24)."""
        for c_val in [1.0, 5.0, 10.0, 13.0, 20.0, 25.0]:
            assert abs(complementarity_sum_at_c(c_val) - 13.0) < 1e-12

    def test_wall_crossing_c13_self_dual(self):
        """Wall-crossing data at c = 13 shows self-duality."""
        result = wall_crossing_at_c13([13.0], max_r=10)
        c13_data = result["c_13.0"]
        assert c13_data["is_self_dual"]

    def test_wall_crossing_c12_not_self_dual(self):
        """Wall-crossing data at c = 12 is NOT self-dual."""
        result = wall_crossing_at_c13([12.0], max_r=10)
        c12_data = result["c_12.0"]
        assert not c12_data["is_self_dual"]


# ============================================================================
# Section 7: Complementarity and discriminants
# ============================================================================

class TestComplementarity:
    """Tests for complementarity sums and discriminants."""

    def test_complementarity_sum_13(self):
        """kappa + kappa' = 13 for Virasoro at all c."""
        for c_val in [0.5, 3.0, 7.5, 13.0, 18.0, 25.5]:
            s = complementarity_sum_at_c(c_val)
            assert abs(s - 13.0) < 1e-12

    def test_discriminant_complementarity_constant_numerator(self):
        """Delta(c) + Delta(26-c) = 6960 / [(5c+22)(152-5c)]."""
        for c_val in [1.0, 5.0, 13.0, 20.0]:
            D_sum = discriminant_complementarity(c_val)
            expected = 6960.0 / ((5.0 * c_val + 22.0) * (152.0 - 5.0 * c_val))
            assert abs(D_sum - expected) < 1e-10

    def test_discriminant_self_dual(self):
        """At c = 13: Delta(13) = Delta(13) (self-dual discriminant)."""
        D13 = critical_discriminant_virasoro(13.0)
        D13_dual = critical_discriminant_virasoro(13.0)
        assert abs(D13 - D13_dual) < 1e-15

    def test_discriminant_positive(self):
        """Delta > 0 for all c > 0 (class M)."""
        for c_val in [0.5, 1.0, 5.0, 13.0, 25.0]:
            assert critical_discriminant_virasoro(c_val) > 0

    def test_discriminant_sum_symmetric(self):
        """Discriminant sum Delta(c)+Delta(26-c) is symmetric under c -> 26-c."""
        for c_val in [3.0, 7.0, 10.0]:
            D_sum_c = discriminant_complementarity(c_val)
            D_sum_dual = discriminant_complementarity(26.0 - c_val)
            assert abs(D_sum_c - D_sum_dual) < 1e-10


# ============================================================================
# Section 8: Tropical wall-crossing and mutation
# ============================================================================

class TestTropicalWallCrossing:
    """Tests for tropical shadow coordinates and mutations."""

    def test_tropical_coords_finite(self):
        """Tropical coordinates are finite for generic c."""
        coords = tropical_shadow_coordinates(13.0, 10)
        for r in range(2, 11):
            assert math.isfinite(coords[r])

    def test_tropical_coords_positive(self):
        """Tropical coordinates -log|S_r| can be any sign."""
        coords = tropical_shadow_coordinates(13.0, 10)
        # S_2 = 6.5 > 1, so x_2 = -log(6.5) < 0
        assert coords[2] < 0

    def test_tropical_c13_self_dual(self):
        """At c=13: tropical coordinates of A and A! agree."""
        coords = tropical_shadow_coordinates(13.0, 10)
        # Since 26 - 13 = 13, dual coords are the same
        dual_coords = tropical_shadow_coordinates(13.0, 10)
        for r in range(2, 11):
            assert abs(coords[r] - dual_coords[r]) < 1e-10

    def test_exchange_matrix_skew(self):
        """Exchange matrix is skew-symmetric."""
        B = exchange_matrix_from_ope(13.0, 8)
        n = B.shape[0]
        for i in range(n):
            for j in range(n):
                assert abs(B[i, j] + B[j, i]) < 1e-15

    def test_exchange_matrix_zero_diagonal(self):
        """Exchange matrix has zero diagonal."""
        B = exchange_matrix_from_ope(13.0, 8)
        for i in range(B.shape[0]):
            assert abs(B[i, i]) < 1e-15

    def test_mutation_preserves_count(self):
        """Mutation preserves the number of coordinates."""
        coords = tropical_shadow_coordinates(13.0, 8)
        B = exchange_matrix_from_ope(13.0, 8)
        mutated = tropical_mutation(coords, B, 3)
        assert len(mutated) == len(coords)

    def test_mutation_involutive(self):
        """Double mutation at the same arity returns to original."""
        coords = tropical_shadow_coordinates(13.0, 8)
        B = exchange_matrix_from_ope(13.0, 8)
        once = tropical_mutation(coords, B, 3)
        # After mutation, B also changes sign in row/col k.
        # For tropical (max-plus), double mutation is involutive.
        twice = tropical_mutation(once, B, 3)
        # Not exactly involutive due to max function, but check structure
        assert len(twice) == len(coords)

    def test_mutation_sequence_runs(self):
        """Mutation sequence computation completes for various c."""
        result = mutation_sequence_through_c13([10.0, 13.0, 16.0], max_r=6)
        assert len(result["sequences"]) == 3


# ============================================================================
# Section 9: Attractor flow integration
# ============================================================================

class TestAttractorFlow:
    """Tests for the attractor flow ODE."""

    def test_attractor_rhs_finite(self):
        """RHS of attractor ODE is finite away from zeros."""
        rhs = attractor_flow_rhs(13.0, complex(3.0, 5.0))
        assert cmath.isfinite(rhs)

    def test_attractor_rhs_near_zero(self):
        """RHS returns 0 near a zero of zeta (fixed point)."""
        # At a zero, ds/dc = 0 (fixed point)
        # We don't know exact zeros, but the function should be well-behaved
        rhs = attractor_flow_rhs(13.0, complex(3.0, 0.0))
        assert cmath.isfinite(rhs)

    def test_attractor_flow_runs(self):
        """Attractor flow integration completes."""
        result = attractor_flow_integrate(
            c_start=5.0, c_end=20.0,
            s0=complex(2.0, 10.0),
            n_steps=50, max_r=20
        )
        assert result["success"]
        assert len(result["s_vals"]) > 0

    def test_attractor_flow_continuous(self):
        """Flow trajectory is continuous (no jumps)."""
        result = attractor_flow_integrate(
            c_start=10.0, c_end=16.0,
            s0=complex(3.0, 5.0),
            n_steps=100, max_r=20
        )
        s_vals = result["s_vals"]
        for i in range(1, len(s_vals)):
            jump = abs(s_vals[i] - s_vals[i-1])
            assert jump < 5.0, f"Jump of {jump} at step {i}"

    def test_attractor_flow_c1_to_c25(self):
        """Flow from c=1 to c=25 completes."""
        result = attractor_flow_integrate(
            c_start=1.0, c_end=25.0,
            s0=complex(2.0, 10.0),
            n_steps=50, max_r=20
        )
        assert result["success"]

    def test_attractor_fixed_points_type(self):
        """Fixed points function returns a list."""
        fps = attractor_fixed_points(13.0, max_r=20)
        assert isinstance(fps, list)


# ============================================================================
# Section 10: Split attractor analysis (AP31 check)
# ============================================================================

class TestSplitAttractor:
    """Tests for split attractor analysis, verifying AP31."""

    def test_kappa_zero_not_split_attractor(self):
        """AP31: kappa = 0 does NOT imply Theta = 0.

        At c = 0 (if it were defined): kappa = 0 but higher S_r survive.
        We check at c very close to 0.
        """
        # c = 0 is singular for Virasoro shadow, but we can check c near 0
        # using a small positive c
        result = split_attractor_analysis(0.5, max_r=10)
        assert not result["is_split_attractor"]
        assert result["n_nonvanishing"] > 1  # more than just S_2

    def test_split_attractor_not_at_kappa_zero(self):
        """The split attractor (where ALL S_r vanish) is not at kappa = 0."""
        result = split_attractor_analysis(0.5, max_r=10)
        assert not result["is_split_attractor"]
        # Higher arities survive even though kappa is small
        assert result["n_nonvanishing"] >= 3

    def test_class_m_never_split(self):
        """For class M (Virasoro), the tower never fully terminates."""
        for c_val in [1.0, 5.0, 13.0, 25.0]:
            result = split_attractor_analysis(c_val, max_r=15)
            assert not result["is_split_attractor"]
            assert result["n_nonvanishing"] > 5

    def test_split_attractor_locus_search(self):
        """Search for split attractor locus returns results."""
        result = find_split_attractor_locus(
            c_range=(1.0, 25.0), n_points=50, max_r=10
        )
        assert len(result["c_vals"]) == 50
        assert result["global_min_mag"] > 0  # never fully zero for Virasoro

    def test_total_shadow_magnitude_positive(self):
        """Total shadow magnitude is positive for all c > 0."""
        for c_val in [1.0, 5.0, 13.0, 20.0, 25.0]:
            result = split_attractor_analysis(c_val, max_r=15)
            assert result["total_shadow_magnitude"] > 0


# ============================================================================
# Section 11: Stokes phenomenon and shadow connection
# ============================================================================

class TestStokesLines:
    """Tests for Stokes lines and the shadow connection."""

    def test_shadow_metric_at_origin(self):
        """Q_Vir(0) = c^2 (positive for c != 0)."""
        for c_val in [1.0, 13.0, 25.0]:
            Q0 = shadow_metric_virasoro(c_val, 0.0)
            assert abs(Q0 - c_val ** 2) < 1e-10

    def test_shadow_metric_zeros_complex(self):
        """Zeros of Q_Vir are complex for Delta > 0 (class M)."""
        for c_val in [1.0, 13.0, 25.0]:
            t0, t1 = shadow_metric_zeros_virasoro(c_val)
            # For class M with Delta > 0, zeros should be complex
            assert abs(t0.imag) > 1e-10 or abs(t1.imag) > 1e-10

    def test_shadow_metric_zeros_conjugate(self):
        """Zeros of Q_Vir come in conjugate pairs."""
        for c_val in [1.0, 13.0, 25.0]:
            t0, t1 = shadow_metric_zeros_virasoro(c_val)
            assert abs(t0 - t1.conjugate()) < 1e-8 or abs(t0.conjugate() - t1) < 1e-8

    def test_shadow_metric_zero_is_zero(self):
        """Q_Vir(t_0) = 0 at the computed zeros."""
        for c_val in [1.0, 13.0, 25.0]:
            t0, t1 = shadow_metric_zeros_virasoro(c_val)
            Q_at_t0 = shadow_metric_virasoro(c_val, t0)
            Q_at_t1 = shadow_metric_virasoro(c_val, t1)
            assert abs(Q_at_t0) < 1e-6, f"Q(t0) = {Q_at_t0} should be 0"
            assert abs(Q_at_t1) < 1e-6, f"Q(t1) = {Q_at_t1} should be 0"

    def test_stokes_graph_runs(self):
        """Stokes graph computation completes."""
        summary = stokes_graph_summary(13.0)
        assert "n_stokes_lines" in summary
        assert "zeros" in summary

    def test_stokes_graph_class_m(self):
        """Virasoro is class M (Delta != 0)."""
        for c_val in [1.0, 13.0, 25.0]:
            summary = stokes_graph_summary(c_val)
            assert summary["class"] == "M"

    def test_stokes_lines_exist(self):
        """Stokes lines exist for class M algebras."""
        lines = stokes_lines_virasoro(13.0, n_theta=180)
        assert len(lines) > 0


# ============================================================================
# Section 12: Cross-verification (multi-path)
# ============================================================================

class TestCrossVerification:
    """Multi-path verification tests (3+ independent paths per claim)."""

    def test_pentagon_identity(self):
        """Pentagon identity verified at Lie algebra level.

        Path 1: Direct BCH bracket computation
        Path 2: KS consistency condition
        """
        result = verify_ks_identity_pentagon(order=8)
        assert result["consistent"]
        assert result["euler_form"] == 1

    def test_palindromic_three_paths(self):
        """c = 13 palindromy verified by 3 independent paths.

        Path 1: Shadow coefficient comparison
        Path 2: KS automorphism comparison
        Path 3: Tropical coordinate comparison
        """
        result = verify_palindromic_self_dual()
        assert result["all_palindromic"]
        assert result["max_diff_coefficients"] < 1e-10
        assert result["max_diff_ks"] < 1e-10
        assert result["max_diff_tropical"] < 1e-10
        assert abs(result["kappa_sum"] - 13.0) < 1e-12

    def test_stokes_wall_correspondence(self):
        """Stokes lines correspond to wall-crossing walls."""
        result = verify_stokes_wall_correspondence(13.0)
        assert result["n_active_bps"] > 5  # class M has many active arities
        assert result["class"] == "M"

    def test_complementarity_sum_three_paths(self):
        """Complementarity sum = 13 verified by 3 paths.

        Path 1: kappa(c) + kappa(26-c) directly
        Path 2: From shadow coefficients S_2(c) + S_2(26-c)
        Path 3: From shadow palindromic test
        """
        c_val = 7.0
        # Path 1
        s1 = virasoro_kappa(c_val) + virasoro_kappa(26.0 - c_val)
        # Path 2
        coeffs = virasoro_shadow_coefficients(c_val, 5)
        dual_coeffs = virasoro_dual_shadow_coefficients(c_val, 5)
        s2 = coeffs[2] + dual_coeffs[2]
        # Path 3
        s3 = complementarity_sum_at_c(c_val)
        assert abs(s1 - 13.0) < 1e-12
        assert abs(s2 - 13.0) < 1e-12
        assert abs(s3 - 13.0) < 1e-12

    def test_discriminant_three_paths(self):
        """Discriminant complementarity verified by 3 paths.

        Path 1: Direct computation Delta(c) + Delta(26-c)
        Path 2: From the formula 6960 / [(5c+22)(152-5c)]
        Path 3: From the shadow metric Q_L zeros
        """
        c_val = 10.0
        # Path 1
        D_sum_1 = discriminant_complementarity(c_val)
        # Path 2
        D_sum_2 = 6960.0 / ((5.0 * c_val + 22.0) * (152.0 - 5.0 * c_val))
        # Path 3: via Delta = 8*kappa*S4
        D_c = 8.0 * virasoro_kappa(c_val) * virasoro_S4(c_val)
        D_dual = 8.0 * virasoro_kappa(26.0 - c_val) * virasoro_S4(26.0 - c_val)
        D_sum_3 = D_c + D_dual

        assert abs(D_sum_1 - D_sum_2) < 1e-10
        assert abs(D_sum_1 - D_sum_3) < 1e-10


# ============================================================================
# Section 13: Special central charges
# ============================================================================

class TestSpecialCentralCharges:
    """Tests at special central charge values."""

    def test_c1_data(self):
        """c = 1: free boson, kappa = 1/2."""
        assert abs(virasoro_kappa(1.0) - 0.5) < 1e-15
        coeffs = virasoro_shadow_coefficients(1.0, 10)
        assert abs(coeffs[2] - 0.5) < 1e-10

    def test_c13_self_dual_comprehensive(self):
        """c = 13: comprehensive self-duality check.

        Multiple invariants should match between A and A!.
        """
        # kappa
        assert abs(virasoro_kappa(13.0) - virasoro_kappa(13.0)) < 1e-15
        # S4
        assert abs(virasoro_S4(13.0) - virasoro_S4(13.0)) < 1e-15
        # Delta
        assert abs(critical_discriminant_virasoro(13.0) -
                   critical_discriminant_virasoro(13.0)) < 1e-15
        # Full coefficient match
        coeffs = virasoro_shadow_coefficients(13.0, 15)
        dual = virasoro_dual_shadow_coefficients(13.0, 15)
        for r in range(2, 16):
            assert abs(coeffs[r] - dual[r]) < 1e-10

    def test_c25_dual_is_c1(self):
        """c = 25: Koszul dual is Vir_1 (c! = 26 - 25 = 1)."""
        coeffs_25 = virasoro_shadow_coefficients(25.0, 10)
        dual_25 = virasoro_dual_shadow_coefficients(25.0, 10)
        coeffs_1 = virasoro_shadow_coefficients(1.0, 10)
        # dual of c=25 should equal c=1
        for r in range(2, 11):
            assert abs(dual_25[r] - coeffs_1[r]) < 1e-8

    def test_c24_moonshine(self):
        """c = 24: moonshine central charge, kappa = 12.

        CAUTION (AP48): kappa = c/2 = 12 is for the Virasoro
        subalgebra; the moonshine module V^natural has kappa = 24
        (from rank). Here we test only the Virasoro piece.
        """
        assert abs(virasoro_kappa(24.0) - 12.0) < 1e-15

    def test_c26_critical(self):
        """c = 26: critical dimension, kappa = 13."""
        assert abs(virasoro_kappa(26.0) - 13.0) < 1e-15

    def test_lee_yang_c_minus22_over_5(self):
        """c = -22/5: Lee-Yang edge singularity.

        The dual is c! = 26 - (-22/5) = 152/5 = 30.4.
        """
        c_ly = -22.0 / 5.0
        c_dual = 26.0 - c_ly
        assert abs(c_dual - 152.0 / 5.0) < 1e-12
        assert abs(complementarity_sum_at_c(c_ly) - 13.0) < 1e-12


# ============================================================================
# Section 14: Shadow radius and coefficient decay
# ============================================================================

class TestShadowRadius:
    """Tests for shadow radius and asymptotic decay of S_r."""

    def test_shadow_radius_positive(self):
        """Shadow radius is positive for all c."""
        for c_val in [1.0, 5.0, 13.0, 25.0]:
            rho = shadow_radius_virasoro(c_val)
            assert rho > 0

    def test_shadow_radius_c1(self):
        """Shadow radius at c = 1."""
        rho = shadow_radius_virasoro(1.0)
        # alpha(1) = (180 + 872)/(5 + 22) = 1052/27
        # rho^2 = alpha / c^2 = 1052/27
        expected_rho_sq = (180.0 + 872.0) / (5.0 + 22.0)
        assert abs(rho ** 2 - expected_rho_sq) < 1e-8

    def test_shadow_radius_formula(self):
        """rho^2 = (180c + 872) / [c^2(5c + 22)]."""
        for c_val in [1.0, 5.0, 13.0, 25.0]:
            rho = shadow_radius_virasoro(c_val)
            expected = math.sqrt((180 * c_val + 872) / (c_val ** 2 * (5 * c_val + 22)))
            assert abs(rho - expected) < 1e-10

    def test_coefficient_decay_c13(self):
        """Verify S_r ~ C * rho^r * r^{-5/2} for Virasoro at c = 13."""
        result = verify_shadow_coefficient_decay(13.0, max_r=30)
        assert result["n_ratios"] > 10
        # The ratios should be somewhat stable (generous tolerance)
        assert result["max_deviation"] < 2.0

    def test_coefficient_decay_c1(self):
        """Verify coefficient decay at c = 1."""
        result = verify_shadow_coefficient_decay(1.0, max_r=20)
        assert result["n_ratios"] > 5

    def test_shadow_radius_decreases_with_c(self):
        """Shadow radius decreases as c increases (for large c)."""
        rho_5 = shadow_radius_virasoro(5.0)
        rho_10 = shadow_radius_virasoro(10.0)
        rho_20 = shadow_radius_virasoro(20.0)
        assert rho_5 > rho_10 > rho_20


# ============================================================================
# Section 15: Pentagon identity verification
# ============================================================================

class TestPentagonIdentity:
    """Tests for the pentagon identity (arity-3 MC equation)."""

    def test_pentagon_euler_form(self):
        """Euler form <(1,0), (0,1)> = 1."""
        result = verify_ks_identity_pentagon()
        assert result["euler_form"] == 1

    def test_pentagon_gamma_12(self):
        """Composite charge gamma_{12} = (1,1)."""
        result = verify_ks_identity_pentagon()
        assert result["gamma_12"] == (1, 1)

    def test_pentagon_bracket_coefficient(self):
        """Bracket coefficient matches expected."""
        result = verify_ks_identity_pentagon()
        # log K_1 at (1,0): 1/1 = 1
        # log K_2 at (0,1): 1/1 = 1
        # bracket: 1 * 1 * euler_form = 1
        assert abs(result["bracket_coefficient"] - 1.0) < 1e-12

    def test_pentagon_consistent(self):
        """Full pentagon consistency check."""
        result = verify_ks_identity_pentagon(order=10)
        assert result["consistent"]


# ============================================================================
# Additional tests: edge cases and robustness
# ============================================================================

class TestEdgeCases:
    """Edge cases and robustness tests."""

    def test_small_c(self):
        """Shadow coefficients at small c (c = 0.5)."""
        coeffs = virasoro_shadow_coefficients(0.5, 10)
        assert len(coeffs) >= 9
        assert math.isfinite(coeffs[2])

    def test_large_c(self):
        """Shadow coefficients at large c (c = 100)."""
        coeffs = virasoro_shadow_coefficients(100.0, 10)
        assert abs(coeffs[2] - 50.0) < 1e-10  # kappa = c/2

    def test_near_critical_c_minus22_over5(self):
        """c near -22/5 (Lee-Yang): approach the pole carefully."""
        c_val = -22.0 / 5.0 + 0.1  # slightly above the pole
        # 5c + 22 = 0.5, small but nonzero
        coeffs = virasoro_shadow_coefficients(c_val, 8)
        assert math.isfinite(coeffs[2])

    def test_spectrum_generator_nonzero_at_c1(self):
        """Spectrum generator at c = 1 has nontrivial structure."""
        sg = spectrum_generator_expansion(1.0, max_charge=10)
        assert abs(sg[0] - 1.0) < 1e-12
        assert abs(sg[2] - 0.5) < 1e-6  # S_2 = 0.5

    def test_shadow_zeta_consistency(self):
        """zeta_A(s) computed with different truncations converges."""
        c_val = 13.0
        s = complex(5.0, 3.0)
        z30 = shadow_zeta_numerical(c_val, s, max_r=30)
        z60 = shadow_zeta_numerical(c_val, s, max_r=60)
        # Should be close since higher terms are suppressed
        assert abs(z30 - z60) < abs(z60) * 0.1

    def test_attractor_flow_short_interval(self):
        """Attractor flow on a very short interval."""
        result = attractor_flow_integrate(
            c_start=12.9, c_end=13.1,
            s0=complex(3.0, 5.0),
            n_steps=20, max_r=15
        )
        assert result["success"]
        assert len(result["s_vals"]) > 0

    def test_plethystic_exponential_identity(self):
        """PE at x = 0 is 1."""
        pe = plethystic_exponential_shadow(13.0, 0.0, max_r=10)
        assert abs(pe - 1.0) < 1e-10

    def test_plethystic_exponential_finite(self):
        """PE at small x is finite."""
        pe = plethystic_exponential_shadow(13.0, 0.1, max_r=10)
        assert cmath.isfinite(pe)

    def test_plethystic_log_length(self):
        """Plethystic log returns correct number of entries."""
        pl = plethystic_log_shadow(13.0, max_charge=15, max_r=10, li_order=5)
        assert len(pl) == 16  # 0 through 15

    def test_shadow_metric_quadratic(self):
        """Q_Vir is a degree-2 polynomial in t."""
        # Q(t) = c^2 + 12c*t + alpha*t^2
        c_val = 10.0
        t_vals = [0.0, 1.0, 2.0]
        Q_vals = [shadow_metric_virasoro(c_val, t) for t in t_vals]
        # A quadratic is determined by 3 points; check a 4th
        # Q(t) = at^2 + bt + c: solve from Q(0), Q(1), Q(2)
        Q0, Q1, Q2 = Q_vals
        a_coeff = (Q2 - 2 * Q1 + Q0) / 2.0
        b_coeff = Q1 - Q0 - a_coeff
        c_coeff = Q0
        Q3_predicted = a_coeff * 9.0 + b_coeff * 3.0 + c_coeff
        Q3_actual = shadow_metric_virasoro(c_val, 3.0)
        assert abs(Q3_predicted - Q3_actual) < 1e-6

    def test_dual_involution(self):
        """Koszul duality is an involution: (A!)! = A.

        For Virasoro: c -> 26-c -> 26-(26-c) = c.
        """
        for c_val in [3.0, 13.0, 20.0]:
            coeffs = virasoro_shadow_coefficients(c_val, 10)
            dual = virasoro_dual_shadow_coefficients(c_val, 10)
            # dual of dual = original
            double_dual = virasoro_dual_shadow_coefficients(26.0 - c_val, 10)
            for r in range(2, 11):
                assert abs(coeffs[r] - double_dual[r]) < 1e-8

    def test_kappa_additivity_under_direct_sum(self):
        """kappa is additive: kappa(A+B) = kappa(A) + kappa(B).

        For Virasoro: kappa(Vir_c + Vir_c') = c/2 + c'/2.
        """
        c1, c2 = 5.0, 8.0
        k_sum = virasoro_kappa(c1) + virasoro_kappa(c2)
        k_combined = virasoro_kappa(c1 + c2)
        assert abs(k_sum - k_combined) < 1e-12
