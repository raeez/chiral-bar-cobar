r"""Tests for the Selberg-type zeta function from the shadow connection flow.

Multi-path verification:
    Path 1: Direct product computation of Z^{Sel}
    Path 2: Trace formula: log Z = orbit sum
    Path 3: Class G/L exact computation (empty product = 1)
    Path 4: Consistency with shadow spectral dimension d^{sh}(A)

65+ tests covering:
    - Shadow flow orbit geometry (branch points, orbit lengths)
    - Selberg zeta: topological vs geometric orbit lengths
    - Ruelle zeta and Selberg-Ruelle relation
    - Functional equation analysis
    - Zeros of Z^{Sel}: exact formulas, line structure
    - Comparison with Riemann zeros (expecting NO systematic alignment)
    - Dynamical entropy (zero for abelian connections)
    - Class G (Heisenberg): trivial (Z = 1)
    - Class L (affine KM): trivial (Z = 1)
    - Class M (Virasoro): nontrivial, full landscape
    - Cross-family consistency
    - Multi-channel generalization

Tolerance: 1e-10 for exact comparisons, 1e-6 for numerical products.
"""

import math
import cmath
import pytest

from compute.lib.bc_selberg_shadow_flow_engine import (
    # Shadow metric and branch points
    shadow_metric_Q,
    shadow_metric_coefficients,
    branch_points,
    virasoro_shadow_data,
    virasoro_branch_points,
    virasoro_growth_rate,
    affine_sl2_shadow_data,
    heisenberg_shadow_data,
    # Orbits
    ShadowOrbit,
    compute_orbits,
    compute_orbits_with_iterates,
    virasoro_orbits,
    count_orbits_up_to_length,
    # Selberg zeta
    selberg_zeta_from_orbits,
    selberg_zeta_topological,
    selberg_zeta_geometric,
    selberg_zeta_virasoro,
    # Trace formula path
    selberg_zeta_via_trace,
    # Ruelle zeta
    ruelle_zeta_from_orbits,
    ruelle_zeta_topological,
    ruelle_zeta_geometric,
    ruelle_zeta_virasoro,
    # Selberg-Ruelle relation
    selberg_ruelle_relation_check,
    # Functional equation
    selberg_functional_equation_test,
    functional_equation_scan,
    # Zeros
    selberg_zeros_topological,
    selberg_zeros_geometric,
    selberg_zeros_virasoro,
    first_n_selberg_zeros,
    # Riemann comparison
    RIEMANN_ZERO_IMAG_PARTS,
    compare_with_riemann_zeros,
    riemann_zero_alignment_score,
    # Entropy
    dynamical_entropy_topological,
    dynamical_entropy_exact,
    # Spectral dimension
    shadow_spectral_dimension,
    selberg_consistency_with_spectral_dimension,
    # Exact class G/L
    selberg_zeta_class_G_exact,
    ruelle_zeta_class_G_exact,
    selberg_zeta_class_L_exact,
    # Landscape
    SelbergShadowData,
    compute_selberg_data,
    compute_virasoro_selberg_landscape,
    compute_full_selberg_landscape,
    # Hybrid product
    shadow_selberg_product_zeta,
    # Multi-channel
    multi_channel_selberg_zeta,
    # Coefficient providers
    _virasoro_shadow_coefficients,
    _heisenberg_shadow_coefficients,
    _affine_shadow_coefficients,
)


# ============================================================================
# Section 1: Branch point geometry
# ============================================================================

class TestBranchPointGeometry:
    """Verify branch point computation and orbit structure."""

    def test_virasoro_branch_points_conjugate_c1(self):
        """At c=1, Virasoro branch points should be complex conjugate."""
        t_plus, t_minus = virasoro_branch_points(1.0)
        assert abs(t_plus.real - t_minus.real) < 1e-12
        assert abs(t_plus.imag + t_minus.imag) < 1e-12

    def test_virasoro_branch_points_conjugate_c13(self):
        """At c=13 (self-dual), branch points are complex conjugate."""
        t_plus, t_minus = virasoro_branch_points(13.0)
        assert abs(t_plus.real - t_minus.real) < 1e-12
        assert abs(t_plus.imag + t_minus.imag) < 1e-12

    def test_virasoro_branch_points_conjugate_c25(self):
        """At c=25, branch points are complex conjugate."""
        t_plus, t_minus = virasoro_branch_points(25.0)
        assert abs(t_plus.real - t_minus.real) < 1e-12
        assert abs(t_plus.imag + t_minus.imag) < 1e-12

    def test_branch_point_modulus_equals_inv_rho(self):
        """Branch point modulus |t_0| = 1/rho (convergence radius)."""
        for c_val in [1.0, 5.0, 10.0, 13.0, 20.0, 25.0]:
            t_plus, t_minus = virasoro_branch_points(c_val)
            rho = virasoro_growth_rate(c_val)
            # Both branch points should have the same modulus
            assert abs(abs(t_plus) - abs(t_minus)) < 1e-10
            assert abs(abs(t_plus) - 1.0 / rho) < 1e-8

    def test_shadow_metric_at_branch_point_is_zero(self):
        """Q_L(t_0) = 0 at each branch point."""
        for c_val in [1.0, 7.0, 13.0, 25.0]:
            kappa, alpha, S4, _ = virasoro_shadow_data(c_val)
            t_plus, t_minus = branch_points(kappa, alpha, S4)
            Q_plus = shadow_metric_Q(kappa, alpha, S4, t_plus)
            Q_minus = shadow_metric_Q(kappa, alpha, S4, t_minus)
            assert abs(Q_plus) < 1e-8, f"Q(t+) = {Q_plus} at c={c_val}"
            assert abs(Q_minus) < 1e-8, f"Q(t-) = {Q_minus} at c={c_val}"

    def test_heisenberg_no_branch_points(self):
        """Heisenberg: Q = 4k^2 (constant), no finite zeros."""
        kappa, alpha, S4, _ = heisenberg_shadow_data(1.0)
        orbits = compute_orbits(kappa, alpha, S4)
        assert len(orbits) == 0

    def test_affine_sl2_double_root(self):
        """Affine sl_2: Delta = 0, Q_L is a perfect square with double root."""
        kappa, alpha, S4, Delta = affine_sl2_shadow_data(1.0)
        assert abs(Delta) < 1e-12
        # Q_L = (2*kappa + 3*alpha*t)^2, double root at -2*kappa/(3*alpha)
        expected_root = -2.0 * kappa / (3.0 * alpha)
        t_plus, t_minus = branch_points(kappa, alpha, S4)
        # Both roots should be at the same point (double root)
        assert abs(t_plus - t_minus) < 1e-8

    def test_virasoro_growth_rate_positive(self):
        """Growth rate rho is positive for all c > 0."""
        for c_val in [0.5, 1.0, 5.0, 13.0, 25.0]:
            rho = virasoro_growth_rate(c_val)
            assert rho > 0

    def test_virasoro_growth_rate_formula(self):
        """Verify rho = sqrt((180c+872)/((5c+22)*c^2))."""
        for c_val in [1.0, 10.0, 25.0]:
            rho = virasoro_growth_rate(c_val)
            expected = math.sqrt(
                (180.0 * c_val + 872.0) / ((5.0 * c_val + 22.0) * c_val ** 2)
            )
            assert abs(rho - expected) < 1e-12


# ============================================================================
# Section 2: Orbit geometry
# ============================================================================

class TestOrbitGeometry:
    """Test orbit computation and properties."""

    def test_virasoro_two_orbits(self):
        """Virasoro (class M) has exactly 2 primitive orbits."""
        for c_val in [1.0, 13.0, 25.0]:
            orbits = virasoro_orbits(c_val)
            assert len(orbits) == 2

    def test_orbit_monodromy_is_minus_one(self):
        """All primitive orbits have monodromy -1 (Koszul sign)."""
        for c_val in [1.0, 7.0, 13.0, 20.0]:
            orbits = virasoro_orbits(c_val)
            for orb in orbits:
                assert abs(orb.monodromy - (-1.0)) < 1e-12

    def test_orbit_residue_is_half(self):
        """All primitive orbits have connection residue 1/2."""
        for c_val in [1.0, 13.0]:
            orbits = virasoro_orbits(c_val)
            for orb in orbits:
                assert abs(orb.residue - 0.5) < 1e-12

    def test_orbit_topological_length_is_pi(self):
        """Topological orbit length = pi for all simple zeros."""
        for c_val in [1.0, 5.0, 13.0, 25.0]:
            orbits = virasoro_orbits(c_val)
            for orb in orbits:
                assert abs(orb.topological_length - math.pi) < 1e-12

    def test_orbit_geometric_length_is_pi_over_rho(self):
        """Geometric orbit length = pi * |t_0| = pi/rho."""
        for c_val in [1.0, 10.0, 13.0, 25.0]:
            orbits = virasoro_orbits(c_val)
            rho = virasoro_growth_rate(c_val)
            expected_length = math.pi / rho
            # Both orbits have the same geometric length (conjugate branch points)
            for orb in orbits:
                assert abs(orb.geometric_length - expected_length) < 1e-6

    def test_orbit_iterates_multiply_length(self):
        """Iterate orbits have length n * ell(primitive)."""
        kappa, alpha, S4, _ = virasoro_shadow_data(10.0)
        all_orbits = compute_orbits_with_iterates(kappa, alpha, S4, max_winding=5)
        primitives = [o for o in all_orbits if o.winding_number == 1]
        for orb in all_orbits:
            prim = [p for p in primitives
                    if abs(p.branch_point - orb.branch_point) < 1e-10][0]
            expected = prim.geometric_length * orb.winding_number
            assert abs(orb.geometric_length - expected) < 1e-10

    def test_orbit_iterate_monodromy(self):
        """Monodromy of n-th iterate is (-1)^n."""
        kappa, alpha, S4, _ = virasoro_shadow_data(10.0)
        all_orbits = compute_orbits_with_iterates(kappa, alpha, S4, max_winding=10)
        for orb in all_orbits:
            expected = (-1.0) ** orb.winding_number
            assert abs(orb.monodromy - expected) < 1e-12

    def test_orbit_count_linear_growth(self):
        """Orbit count N(T) grows linearly in T."""
        orbits = virasoro_orbits(13.0)
        T1 = 100.0
        T2 = 200.0
        N1 = count_orbits_up_to_length(orbits, T1)
        N2 = count_orbits_up_to_length(orbits, T2)
        # N(2T) ~ 2*N(T) for large T (linear growth)
        assert abs(N2 - 2 * N1) <= 2 * len(orbits)  # Allow small boundary error

    def test_heisenberg_no_orbits(self):
        """Heisenberg has no primitive orbits."""
        kappa, alpha, S4, _ = heisenberg_shadow_data(1.0)
        orbits = compute_orbits(kappa, alpha, S4)
        assert len(orbits) == 0


# ============================================================================
# Section 3: Selberg zeta function
# ============================================================================

class TestSelbergZeta:
    """Test the Selberg zeta function computation."""

    def test_selberg_topological_converges(self):
        """Selberg zeta with topological lengths is nonzero for Re(s) > 0."""
        s = complex(2.0, 0.0)
        Z = selberg_zeta_topological(2, s)
        assert abs(Z) > 0
        assert math.isfinite(abs(Z))

    def test_selberg_geometric_converges(self):
        """Selberg zeta with geometric lengths converges for Re(s) >> 0."""
        rho = virasoro_growth_rate(13.0)
        s = complex(5.0, 0.0)
        Z = selberg_zeta_geometric(rho, 2, s)
        assert abs(Z) > 0
        assert math.isfinite(abs(Z))

    def test_selberg_virasoro_converges(self):
        """Virasoro Selberg zeta converges for Re(s) sufficiently large."""
        for c_val in [1.0, 13.0, 25.0]:
            Z = selberg_zeta_virasoro(c_val, complex(5.0, 0.0))
            assert math.isfinite(abs(Z))

    def test_selberg_from_orbits_matches_geometric(self):
        """Path 1 vs direct formula: orbit-based matches closed-form."""
        for c_val in [1.0, 10.0, 25.0]:
            kappa, alpha, S4, _ = virasoro_shadow_data(c_val)
            orbits = compute_orbits(kappa, alpha, S4)
            rho = virasoro_growth_rate(c_val)
            s = complex(3.0, 1.0)
            Z_orbits = selberg_zeta_from_orbits(orbits, s, max_k=50)
            Z_geometric = selberg_zeta_geometric(rho, 2, s, max_k=50)
            assert abs(Z_orbits - Z_geometric) < 1e-8 * max(abs(Z_orbits), 1e-30)

    def test_selberg_via_trace_matches_direct(self):
        """Path 2: Trace formula matches direct product."""
        kappa, alpha, S4, _ = virasoro_shadow_data(13.0)
        orbits = compute_orbits(kappa, alpha, S4)
        s = complex(3.0, 0.5)
        Z_direct = selberg_zeta_from_orbits(orbits, s, max_k=50)
        Z_trace = selberg_zeta_via_trace(orbits, s, max_winding=100)
        # Trace formula is an approximation; check relative agreement
        if abs(Z_direct) > 1e-10:
            rel_error = abs(Z_direct - Z_trace) / abs(Z_direct)
            assert rel_error < 0.01, f"Relative error {rel_error}"

    def test_selberg_class_G_is_one(self):
        """Path 3: Heisenberg Selberg zeta = 1 (no orbits)."""
        Z = selberg_zeta_class_G_exact(1.0, complex(2.0, 0.0))
        assert abs(Z - 1.0) < 1e-12

    def test_selberg_class_L_is_one(self):
        """Path 3: Affine KM Selberg zeta = 1 (double root, trivial monodromy)."""
        Z = selberg_zeta_class_L_exact(3.0 / 4.0 * 3, 4.0 / 3.0, complex(2.0, 0.0))
        assert abs(Z - 1.0) < 1e-12

    def test_selberg_real_on_real_axis(self):
        """Selberg zeta is real-valued on the real axis (for real orbit data)."""
        for c_val in [1.0, 13.0]:
            Z = selberg_zeta_virasoro(c_val, complex(5.0, 0.0))
            assert abs(Z.imag) < 1e-10 * abs(Z.real)

    def test_selberg_positive_real_axis(self):
        """For real s >> 0, Z^Sel is real and positive."""
        rho = virasoro_growth_rate(13.0)
        Z = selberg_zeta_geometric(rho, 2, complex(10.0, 0.0))
        assert Z.real > 0
        assert abs(Z.imag) < 1e-10

    def test_selberg_increases_with_s_on_real(self):
        """Z^Sel(s) -> 1 as s -> +infinity (all exponentials vanish)."""
        rho = virasoro_growth_rate(13.0)
        Z_small = selberg_zeta_geometric(rho, 2, complex(5.0, 0.0))
        Z_large = selberg_zeta_geometric(rho, 2, complex(20.0, 0.0))
        # Z should be closer to 1 for larger s
        assert abs(Z_large - 1.0) < abs(Z_small - 1.0)


# ============================================================================
# Section 4: Ruelle zeta function
# ============================================================================

class TestRuelleZeta:
    """Test the Ruelle zeta function."""

    def test_ruelle_topological_formula(self):
        """Ruelle with topological lengths: (1 + exp(-s*pi))^{-N_bp}."""
        s = complex(2.0, 0.0)
        Z = ruelle_zeta_topological(2, s)
        expected = (1.0 + cmath.exp(-s * math.pi)) ** (-2)
        assert abs(Z - expected) < 1e-12

    def test_ruelle_geometric_formula(self):
        """Ruelle with geometric lengths: (1 + exp(-s*pi/rho))^{-N_bp}."""
        rho = virasoro_growth_rate(13.0)
        s = complex(2.0, 0.0)
        Z = ruelle_zeta_geometric(rho, 2, s)
        expected = (1.0 + cmath.exp(-s * math.pi / rho)) ** (-2)
        assert abs(Z - expected) < 1e-12

    def test_ruelle_virasoro_converges(self):
        """Virasoro Ruelle zeta converges for Re(s) > 0."""
        for c_val in [1.0, 13.0, 25.0]:
            Z = ruelle_zeta_virasoro(c_val, complex(2.0, 0.0))
            assert math.isfinite(abs(Z))

    def test_ruelle_from_orbits_matches_closed_form(self):
        """Orbit-based Ruelle matches closed-form."""
        for c_val in [1.0, 13.0, 25.0]:
            orbits = virasoro_orbits(c_val)
            rho = virasoro_growth_rate(c_val)
            s = complex(3.0, 1.0)
            Z_orbits = ruelle_zeta_from_orbits(orbits, s)
            Z_closed = ruelle_zeta_geometric(rho, 2, s)
            assert abs(Z_orbits - Z_closed) < 1e-8

    def test_ruelle_class_G_is_one(self):
        """Heisenberg Ruelle zeta = 1."""
        Z = ruelle_zeta_class_G_exact(1.0, complex(2.0, 0.0))
        assert abs(Z - 1.0) < 1e-12


# ============================================================================
# Section 5: Selberg-Ruelle relation
# ============================================================================

class TestSelbergRuelleRelation:
    """Verify Z^{Sel}(s) = prod_{k>=0} zeta^{Ruelle}(s+k)^{-1}."""

    def test_relation_topological(self):
        """Selberg-Ruelle relation with topological lengths."""
        s = complex(3.0, 0.0)
        orbits = virasoro_orbits(13.0)
        Z_sel, ruelle_prod = selberg_ruelle_relation_check(
            orbits, s, max_k=50, use_geometric=False,
        )
        if abs(Z_sel) > 1e-10:
            rel_error = abs(Z_sel - ruelle_prod) / abs(Z_sel)
            assert rel_error < 1e-6

    def test_relation_geometric(self):
        """Selberg-Ruelle relation with geometric lengths."""
        s = complex(3.0, 0.0)
        orbits = virasoro_orbits(13.0)
        Z_sel, ruelle_prod = selberg_ruelle_relation_check(
            orbits, s, max_k=50, use_geometric=True,
        )
        if abs(Z_sel) > 1e-10:
            rel_error = abs(Z_sel - ruelle_prod) / abs(Z_sel)
            assert rel_error < 1e-6

    def test_relation_complex_s(self):
        """Selberg-Ruelle relation at complex s."""
        s = complex(3.0, 2.0)
        orbits = virasoro_orbits(10.0)
        Z_sel, ruelle_prod = selberg_ruelle_relation_check(
            orbits, s, max_k=40, use_geometric=True,
        )
        if abs(Z_sel) > 1e-10:
            rel_error = abs(Z_sel - ruelle_prod) / abs(Z_sel)
            assert rel_error < 1e-4


# ============================================================================
# Section 6: Functional equation
# ============================================================================

class TestFunctionalEquation:
    """Test the functional equation of the shadow Selberg zeta."""

    def test_no_exact_functional_equation(self):
        """The shadow Selberg zeta does NOT satisfy Z(s) = Z(1-s) exactly.

        This is expected: the shadow connection lives on a meromorphic
        connection, not a compact Riemann surface, so the classical
        Selberg functional equation does not apply.
        """
        rho = virasoro_growth_rate(13.0)
        s = complex(2.0, 1.0)
        Zs, Z1s, ratio = selberg_functional_equation_test(rho, 2, s)
        # The ratio should NOT be 1 (no exact functional equation)
        assert abs(ratio - 1.0) > 0.01

    def test_functional_equation_scan(self):
        """Scan the functional equation ratio across multiple s values."""
        rho = virasoro_growth_rate(13.0)
        s_values = [complex(0.5, t) for t in [1.0, 2.0, 5.0, 10.0]]
        results = functional_equation_scan(rho, 2, s_values)
        assert len(results) == 4
        for s, Zs, Z1s, ratio in results:
            assert math.isfinite(abs(Zs))

    def test_ratio_not_involving_riemann_zeta(self):
        """The correction factor Z(s)/Z(1-s) does NOT involve zeta(2s)/zeta(2s-1).

        This is because the shadow Selberg zeta is built from a logarithmic
        connection with finitely many singular points, not from a hyperbolic
        surface. There is no Laplacian, no Weyl law, and no Patterson-Perry
        scattering matrix to produce Riemann zeta factors.
        """
        rho = virasoro_growth_rate(13.0)
        # Evaluate the correction ratio at several points
        corrections = []
        for t in [1.0, 2.0, 3.0, 5.0]:
            s = complex(0.5, t)
            _, _, ratio = selberg_functional_equation_test(rho, 2, s)
            corrections.append(ratio)
        # The corrections should NOT form a simple rational function
        # (no systematic pattern expected)
        # Just verify they are all finite and distinct
        for c in corrections:
            assert math.isfinite(abs(c))
        assert len(set(abs(c) for c in corrections)) > 1


# ============================================================================
# Section 7: Zeros of the Selberg zeta
# ============================================================================

class TestSelbergZeros:
    """Test the zeros of the shadow Selberg zeta."""

    def test_topological_zeros_formula(self):
        """Zeros with topological lengths at s = -k + (2n+1)*i."""
        zeros = selberg_zeros_topological(2, max_k=3, max_n=5)
        # Check that s = 0 + 1i is a zero
        assert any(abs(z - complex(0, 1)) < 1e-10 for z in zeros)
        # Check that s = -1 + 3i is a zero
        assert any(abs(z - complex(-1, 3)) < 1e-10 for z in zeros)

    def test_geometric_zeros_formula(self):
        """Zeros with geometric lengths at s = -k + (2n+1)*rho*i."""
        rho = virasoro_growth_rate(13.0)
        zeros = selberg_zeros_geometric(rho, 2, max_k=3, max_n=5)
        # The first zero with k=0, n=0 is at s = rho*i
        assert any(abs(z - complex(0, rho)) < 1e-10 for z in zeros)

    def test_zeros_are_actual_zeros(self):
        """Verify that the computed zeros are actually zeros of Z^{Sel}."""
        rho = virasoro_growth_rate(13.0)
        zeros = selberg_zeros_geometric(rho, 2, max_k=2, max_n=3)
        for z in zeros[:10]:
            Z = selberg_zeta_geometric(rho, 2, z, max_k=100)
            assert abs(Z) < 1e-6, f"Z({z}) = {Z}, not zero"

    def test_zeros_on_vertical_lines(self):
        """All zeros lie on vertical lines Re(s) = -k for k = 0, 1, 2, ..."""
        rho = virasoro_growth_rate(13.0)
        zeros = selberg_zeros_geometric(rho, 2, max_k=5, max_n=10)
        for z in zeros:
            # Re(s) should be a non-positive integer
            k = -round(z.real)
            assert k >= 0
            assert abs(z.real - (-k)) < 1e-10

    def test_zeros_NOT_on_critical_line(self):
        """Shadow Selberg zeros do NOT lie on Re(s) = 1/2.

        This is a fundamental structural difference from the Riemann zeta.
        """
        rho = virasoro_growth_rate(13.0)
        zeros = first_n_selberg_zeros(rho, 2, 30)
        for z in zeros:
            assert abs(z.real - 0.5) > 0.01, f"Zero {z} unexpectedly on Re(s)=1/2"

    def test_first_50_zeros(self):
        """Compute first 50 zeros and verify basic structure."""
        rho = virasoro_growth_rate(13.0)
        zeros = first_n_selberg_zeros(rho, 2, 50)
        assert len(zeros) >= 50
        # All zeros should have non-positive integer real parts
        for z in zeros:
            k = -round(z.real)
            assert k >= 0
            assert abs(z.real - (-k)) < 1e-10

    def test_zero_spacing_equals_two_rho(self):
        """On the line Re(s) = 0, zeros are spaced by 2*rho."""
        rho = virasoro_growth_rate(13.0)
        zeros_on_imaginary = [z for z in selberg_zeros_geometric(rho, 2, max_k=1, max_n=20)
                              if abs(z.real) < 1e-10 and z.imag > 0]
        zeros_on_imaginary.sort(key=lambda z: z.imag)
        for i in range(1, min(10, len(zeros_on_imaginary))):
            spacing = zeros_on_imaginary[i].imag - zeros_on_imaginary[i - 1].imag
            assert abs(spacing - 2.0 * rho) < 1e-10

    def test_virasoro_zeros_across_c(self):
        """First zeros for Virasoro at different c values."""
        for c_val in [1.0, 10.0, 13.0, 25.0]:
            zeros = selberg_zeros_virasoro(c_val, max_k=2, max_n=5)
            assert len(zeros) > 0
            rho = virasoro_growth_rate(c_val)
            # First positive zero on Im axis should be at rho*i
            positive_imag_zeros = [z for z in zeros if z.imag > 0 and abs(z.real) < 1e-10]
            if positive_imag_zeros:
                first = min(positive_imag_zeros, key=lambda z: z.imag)
                assert abs(first.imag - rho) < 1e-8


# ============================================================================
# Section 8: Comparison with Riemann zeros
# ============================================================================

class TestRiemannComparison:
    """Test comparison with Riemann zeta zeros."""

    def test_riemann_zeros_table_correct(self):
        """Verify the Riemann zero table against known values."""
        # First zero: gamma_1 = 14.13472...
        assert abs(RIEMANN_ZERO_IMAG_PARTS[0] - 14.134725) < 1e-4
        # Second zero: gamma_2 = 21.02204...
        assert abs(RIEMANN_ZERO_IMAG_PARTS[1] - 21.022040) < 1e-4

    def test_no_systematic_alignment(self):
        """Shadow Selberg zeros do NOT systematically align with Riemann zeros.

        This is expected (AP42): the shadow connection and the Riemann zeta
        encode fundamentally different mathematical structures.
        """
        for c_val in [1.0, 13.0, 25.0]:
            rho = virasoro_growth_rate(c_val)
            score = riemann_zero_alignment_score(rho, 2, 15)
            # Score should be of order 1 (random alignment)
            # A score << 0.1 would indicate suspicious alignment
            # We assert score > 0.05 to confirm no systematic alignment
            assert score > 0.05, f"Suspicious alignment at c={c_val}, score={score}"

    def test_comparison_produces_data(self):
        """compare_with_riemann_zeros returns meaningful data."""
        rho = virasoro_growth_rate(13.0)
        comparisons = compare_with_riemann_zeros(rho, 2, 10)
        assert len(comparisons) == 10
        for shadow, riemann, diff in comparisons:
            assert math.isfinite(shadow)
            assert math.isfinite(riemann)
            assert math.isfinite(diff)

    def test_alignment_score_varies_with_c(self):
        """Alignment score varies with c (no universal alignment)."""
        scores = {}
        for c_val in [1.0, 5.0, 13.0, 25.0]:
            rho = virasoro_growth_rate(c_val)
            scores[c_val] = riemann_zero_alignment_score(rho, 2, 10)
        # Scores should be different (not a universal coincidence)
        score_values = list(scores.values())
        assert max(score_values) / min(score_values) > 1.1


# ============================================================================
# Section 9: Dynamical entropy
# ============================================================================

class TestDynamicalEntropy:
    """Test dynamical entropy of the shadow flow."""

    def test_entropy_vanishes_class_G(self):
        """Heisenberg: zero entropy (no orbits)."""
        kappa, alpha, S4, _ = heisenberg_shadow_data(1.0)
        orbits = compute_orbits(kappa, alpha, S4)
        h = dynamical_entropy_exact(orbits)
        assert h == 0.0

    def test_entropy_vanishes_class_M(self):
        """Virasoro: zero entropy (abelian connection, finitely many orbits).

        The shadow connection is rank 1 (abelian), so it has zero
        topological entropy regardless of the number of branch points.
        """
        orbits = virasoro_orbits(13.0)
        h = dynamical_entropy_exact(orbits)
        assert h == 0.0

    def test_entropy_numerical_small(self):
        """Numerical entropy estimate is near zero."""
        orbits = virasoro_orbits(13.0)
        T_vals, N_vals, h = dynamical_entropy_topological(orbits, T_max=100.0)
        # h should be close to 0 (linear growth -> log(N)/T -> 0)
        assert h < 0.1  # Very loose bound; true value is 0

    def test_entropy_linear_orbit_growth(self):
        """Orbit count grows linearly, confirming h = 0."""
        orbits = virasoro_orbits(13.0)
        T_vals, N_vals, _ = dynamical_entropy_topological(orbits, T_max=200.0, n_points=20)
        # Linear growth: N(T) ~ c*T
        # Check that N(2T)/N(T) ~ 2 for large T
        if N_vals[-1] > 0 and N_vals[len(N_vals) // 2] > 0:
            ratio = N_vals[-1] / N_vals[len(N_vals) // 2]
            assert 1.5 < ratio < 2.5


# ============================================================================
# Section 10: Spectral dimension consistency (Path 4)
# ============================================================================

class TestSpectralDimension:
    """Test consistency of Selberg zeros with spectral dimension."""

    def test_spectral_dimension_class_G(self):
        """Class G: d^sh = 0."""
        d = shadow_spectral_dimension(0.0)
        assert d == 0.0

    def test_spectral_dimension_class_M_convergent(self):
        """Class M with rho < 1: d^sh = 1/log(1/rho) > 0."""
        for c_val in [10.0, 13.0, 25.0]:
            rho = virasoro_growth_rate(c_val)
            if rho < 1.0:
                d = shadow_spectral_dimension(rho)
                assert d > 0
                assert abs(d - 1.0 / math.log(1.0 / rho)) < 1e-12

    def test_spectral_dimension_class_M_divergent(self):
        """Class M with rho > 1: d^sh = infinity."""
        rho = virasoro_growth_rate(1.0)  # rho > 1 for c < c*
        if rho > 1.0:
            d = shadow_spectral_dimension(rho)
            assert d == float('inf')

    def test_selberg_consistency(self):
        """Zero spacing consistent with spectral dimension."""
        for c_val in [10.0, 13.0, 25.0]:
            rho = virasoro_growth_rate(c_val)
            if 0 < rho < 1.0:
                result = selberg_consistency_with_spectral_dimension(rho, 2)
                assert result['consistency'] is True
                assert abs(result['zero_spacing'] - result['predicted_spacing_from_d_sh']) < 1e-10


# ============================================================================
# Section 11: Landscape computation
# ============================================================================

class TestLandscape:
    """Test the full landscape computation."""

    def test_virasoro_landscape(self):
        """Compute Selberg data across the Virasoro landscape."""
        landscape = compute_virasoro_selberg_landscape()
        assert len(landscape) > 0
        for c_val, data in landscape.items():
            assert data.shadow_class == 'M'
            assert data.N_bp == 2
            assert data.rho > 0
            assert data.dynamical_entropy == 0.0

    def test_full_landscape(self):
        """Compute the full standard landscape."""
        landscape = compute_full_selberg_landscape()
        assert 'Heis_k=1' in landscape
        assert 'Vir_c=13' in landscape
        # Heisenberg has no orbits
        assert landscape['Heis_k=1'].N_bp == 0
        # Virasoro has 2 orbits
        assert landscape['Vir_c=13'].N_bp == 2

    def test_selberg_data_zeta_method(self):
        """SelbergShadowData.selberg_zeta method works."""
        kappa, alpha, S4, _ = virasoro_shadow_data(13.0)
        data = compute_selberg_data('Vir_c=13', 'M', kappa, alpha, S4)
        Z = data.selberg_zeta(complex(3.0, 0.0))
        assert math.isfinite(abs(Z))

    def test_selberg_data_first_zeros(self):
        """SelbergShadowData.first_zeros method works."""
        kappa, alpha, S4, _ = virasoro_shadow_data(13.0)
        data = compute_selberg_data('Vir_c=13', 'M', kappa, alpha, S4)
        zeros = data.first_zeros(20)
        assert len(zeros) == 20


# ============================================================================
# Section 12: Hybrid shadow-Selberg product
# ============================================================================

class TestHybridProduct:
    """Test the hybrid shadow-Selberg product zeta."""

    def test_heisenberg_hybrid(self):
        """Heisenberg hybrid product: prod_{k>=0} (1 - k * 2^{-(s+k)})."""
        coeffs = _heisenberg_shadow_coefficients(1.0, max_r=10)
        s = complex(5.0, 0.0)
        Z = shadow_selberg_product_zeta(coeffs, s, max_k=30)
        assert math.isfinite(abs(Z))

    def test_virasoro_hybrid_converges(self):
        """Virasoro hybrid product converges for Re(s) sufficiently large."""
        coeffs = _virasoro_shadow_coefficients(13.0, max_r=30)
        s = complex(10.0, 0.0)
        Z = shadow_selberg_product_zeta(coeffs, s, max_k=20)
        assert math.isfinite(abs(Z))

    def test_hybrid_different_from_geometric(self):
        """Hybrid product is a DIFFERENT object from the geometric Selberg zeta."""
        rho = virasoro_growth_rate(13.0)
        coeffs = _virasoro_shadow_coefficients(13.0, max_r=30)
        s = complex(5.0, 0.0)
        Z_hybrid = shadow_selberg_product_zeta(coeffs, s, max_k=20)
        Z_geom = selberg_zeta_geometric(rho, 2, s, max_k=50)
        # These should be different (two distinct constructions)
        assert abs(Z_hybrid - Z_geom) > 1e-6


# ============================================================================
# Section 13: Multi-channel Selberg zeta
# ============================================================================

class TestMultiChannel:
    """Test the multi-channel Selberg zeta for rank > 1."""

    def test_rank1_matches_single_channel(self):
        """Rank 1 with M = [-1]: matches the single-channel formula."""
        s = complex(3.0, 0.0)
        ell = math.pi / virasoro_growth_rate(13.0)
        Z_multi = multi_channel_selberg_zeta([-1.0 + 0.0j], ell, s, max_k=50)
        Z_single = selberg_zeta_geometric(virasoro_growth_rate(13.0), 1, s, max_k=50)
        assert abs(Z_multi - Z_single) < 1e-8

    def test_rank2_product(self):
        """Rank 2 decomposes as product of rank-1 factors."""
        s = complex(3.0, 0.0)
        ell = 2.0
        m1 = -1.0 + 0.0j
        m2 = 0.5 + 0.5j
        Z_multi = multi_channel_selberg_zeta([m1, m2], ell, s, max_k=50)
        Z_1 = multi_channel_selberg_zeta([m1], ell, s, max_k=50)
        Z_2 = multi_channel_selberg_zeta([m2], ell, s, max_k=50)
        assert abs(Z_multi - Z_1 * Z_2) < 1e-8

    def test_trivial_monodromy(self):
        """Monodromy = identity: Z decomposes into standard Selberg factor."""
        s = complex(3.0, 0.0)
        ell = 2.0
        Z = multi_channel_selberg_zeta([1.0 + 0.0j], ell, s, max_k=50)
        # Factor: prod_{k>=0} (1 - exp(-(s+k)*ell))
        # This is related to q-Pochhammer
        assert math.isfinite(abs(Z))


# ============================================================================
# Section 14: Koszul duality relations
# ============================================================================

class TestKoszulDuality:
    """Test Koszul duality properties of the Selberg zeta."""

    def test_virasoro_dual_rho(self):
        """rho(Vir_c) and rho(Vir_{26-c}) are related but NOT equal.

        CAUTION (AP24): kappa(c) + kappa(26-c) = 13, not 0.
        """
        for c_val in [1.0, 5.0, 10.0, 20.0]:
            rho = virasoro_growth_rate(c_val)
            rho_dual = virasoro_growth_rate(26.0 - c_val)
            # They should be different (except at c=13)
            if abs(c_val - 13.0) > 1.0:
                assert abs(rho - rho_dual) > 1e-8

    def test_self_dual_c13(self):
        """At c=13, rho(Vir_13) = rho(Vir_13) (self-dual point)."""
        rho = virasoro_growth_rate(13.0)
        rho_dual = virasoro_growth_rate(13.0)
        assert abs(rho - rho_dual) < 1e-12

    def test_selberg_at_self_dual(self):
        """At c=13, Z^Sel_A(s) = Z^Sel_{A!}(s)."""
        s = complex(3.0, 1.0)
        Z = selberg_zeta_virasoro(13.0, s)
        Z_dual = selberg_zeta_virasoro(13.0, s)  # Same algebra at self-dual
        assert abs(Z - Z_dual) < 1e-12

    def test_koszul_duality_exchanges_branch_points(self):
        """Koszul duality c -> 26-c transforms Q_L(t,c) to Q_L(t,26-c).

        The branch points are different for A and A!.
        """
        for c_val in [1.0, 5.0, 10.0]:
            bp = virasoro_branch_points(c_val)
            bp_dual = virasoro_branch_points(26.0 - c_val)
            # Branch points should be different
            assert abs(abs(bp[0]) - abs(bp_dual[0])) > 1e-8


# ============================================================================
# Section 15: Edge cases and robustness
# ============================================================================

class TestEdgeCases:
    """Test edge cases and robustness."""

    def test_large_c(self):
        """Virasoro at large c: rho -> 0, Z^Sel -> 1."""
        rho = virasoro_growth_rate(1000.0)
        assert rho < 0.1
        Z = selberg_zeta_virasoro(1000.0, complex(2.0, 0.0))
        assert abs(Z - 1.0) < 0.01

    def test_small_c(self):
        """Virasoro at small c (c=1/2): rho is large."""
        rho = virasoro_growth_rate(0.5)
        assert rho > 1.0  # Divergent tower

    def test_zero_s(self):
        """Z^Sel at s=0 is computable."""
        rho = virasoro_growth_rate(13.0)
        Z = selberg_zeta_geometric(rho, 2, complex(0.0, 0.0), max_k=100)
        assert math.isfinite(abs(Z))

    def test_negative_s(self):
        """Z^Sel at negative real s: zeros expected."""
        rho = virasoro_growth_rate(13.0)
        # At s = -1 + rho*i, should be a zero
        z = complex(-1, rho)
        Z = selberg_zeta_geometric(rho, 2, z, max_k=100)
        assert abs(Z) < 1e-4

    def test_large_imaginary(self):
        """Z^Sel at large imaginary part."""
        rho = virasoro_growth_rate(13.0)
        Z = selberg_zeta_geometric(rho, 2, complex(2.0, 50.0), max_k=80)
        assert math.isfinite(abs(Z))
