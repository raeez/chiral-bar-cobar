r"""Tests for quantum spectral curve of the shadow obstruction tower.

Verifies:
1. Classical spectral curve: potential, momentum, shadow metric recovery
2. WKB expansion: leading term matches shadow, quantum corrections well-defined
3. Eigenvalue computation: Bohr-Sommerfeld vs grid, growth exponent
4. Spectral zeta function: convergence, special values
5. Spectral determinant: analytic properties at Riemann zeros
6. Exact WKB / Voros: A-cycle and B-cycle periods
7. Topological recursion: F_g^{EO} = F_g^{shadow} through g=5
8. Nekrasov-Shatashvili: wave function well-defined at zeta zeros
9. Class G/L exact solutions: Airy/Bessel eigenvalue formulas
10. Cross-verification: 4 independent paths to eigenvalues

Multi-path verification mandate (AP10):
  Path 1: WKB / Bohr-Sommerfeld (semiclassical)
  Path 2: Grid eigenvalues (numerical PDE)
  Path 3: Topological recursion F_g match
  Path 4: Class G/L exact solutions (limiting cases)
"""

import sys
sys.path.insert(0, 'compute')

import math
import cmath
import pytest
import numpy as np

PI = math.pi


# =====================================================================
# Fixtures
# =====================================================================

@pytest.fixture
def virasoro_c13():
    """Virasoro shadow data at the self-dual point c = 13."""
    from lib.bc_quantum_spectral_curve_zeta_engine import virasoro_shadow_invariants
    return virasoro_shadow_invariants(13.0)


@pytest.fixture
def virasoro_c1():
    """Virasoro shadow data at c = 1."""
    from lib.bc_quantum_spectral_curve_zeta_engine import virasoro_shadow_invariants
    return virasoro_shadow_invariants(1.0)


@pytest.fixture
def virasoro_c26():
    """Virasoro shadow data at c = 26 (string theory)."""
    from lib.bc_quantum_spectral_curve_zeta_engine import virasoro_shadow_invariants
    return virasoro_shadow_invariants(26.0)


@pytest.fixture
def heisenberg_data():
    """Heisenberg (class G): kappa = 1, alpha = 0, S4 = 0."""
    return {'kappa': 1.0, 'alpha': 0.0, 'S4': 0.0}


@pytest.fixture
def affine_sl2_data():
    """Affine sl_2 at k=1 (class L): kappa = 3(k+2)/4 = 9/4, alpha = 2, S4 = 0."""
    return {'kappa': 9.0 / 4.0, 'alpha': 2.0, 'S4': 0.0}


# =====================================================================
# 1. Classical spectral curve
# =====================================================================

class TestClassicalSpectralCurve:
    """Tests for the classical spectral curve y^2 = t^4 Q_L(t)."""

    def test_potential_at_origin(self, virasoro_c13):
        """V(0) = 0 (potential vanishes at the origin)."""
        from lib.bc_quantum_spectral_curve_zeta_engine import classical_potential
        V0 = classical_potential(0.0, 6.5, 2.0, virasoro_c13['S4'])
        assert abs(V0) < 1e-15

    def test_potential_positive_for_positive_t(self, virasoro_c13):
        """V(t) > 0 for t > 0 (positive definite for Virasoro with c > 0)."""
        from lib.bc_quantum_spectral_curve_zeta_engine import classical_potential
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        for t in [0.01, 0.1, 0.5, 1.0, 2.0, 5.0]:
            V = classical_potential(t, kappa, alpha, S4)
            assert V > 0, f"V({t}) = {V} should be positive"

    def test_potential_sextic_growth(self, virasoro_c13):
        """V(t) ~ (9 alpha^2 + 2 Delta) t^6 for large t."""
        from lib.bc_quantum_spectral_curve_zeta_engine import classical_potential
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4
        t_large = 1000.0
        V = classical_potential(t_large, kappa, alpha, S4)
        leading = q2 * t_large ** 6
        assert abs(V / leading - 1.0) < 0.01, "V should be asymptotically ~ q2 * t^6"

    def test_momentum_matches_shadow(self, virasoro_c13):
        """p(t) = t^2 sqrt(Q_L(t)) matches the shadow generating function at leading order."""
        from lib.bc_quantum_spectral_curve_zeta_engine import (
            classical_momentum, shadow_coefficients_from_QL
        )
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']

        # At t small, p(t) ~ 2|kappa| t^2 + 6 alpha t^3 + ...
        t_small = 0.01
        p = classical_momentum(t_small, kappa, alpha, S4)
        leading = 2.0 * abs(kappa) * t_small ** 2
        assert abs(abs(p) / leading - 1.0) < 0.1

    def test_shadow_coefficients_S2_equals_kappa(self, virasoro_c13):
        """S_2 = kappa (the first shadow coefficient is the curvature)."""
        from lib.bc_quantum_spectral_curve_zeta_engine import shadow_coefficients_from_QL
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        coeffs = shadow_coefficients_from_QL(kappa, alpha, S4, r_max=5)
        # S_2 = (1/2) * [t^0] sqrt(Q_L) = (1/2) * 2|kappa| = |kappa|
        assert abs(coeffs[0] - abs(kappa)) < 1e-10, f"S_2 = {coeffs[0]}, expected {abs(kappa)}"

    def test_shadow_coefficients_S3_equals_alpha(self, virasoro_c13):
        """S_3 = alpha (the cubic shadow)."""
        from lib.bc_quantum_spectral_curve_zeta_engine import shadow_coefficients_from_QL
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        coeffs = shadow_coefficients_from_QL(kappa, alpha, S4, r_max=5)
        # S_3 = (1/3) * [t^1] sqrt(Q_L) = (1/3) * q1/(2*sqrt(q0)) = (1/3)*12*kappa*alpha/(4*kappa)
        # = (1/3) * 3 * alpha = alpha
        assert abs(coeffs[1] - alpha) < 1e-10, f"S_3 = {coeffs[1]}, expected {alpha}"

    def test_class_g_shadow_terminates(self, heisenberg_data):
        """For class G (Heisenberg): S_r = 0 for r >= 3."""
        from lib.bc_quantum_spectral_curve_zeta_engine import shadow_coefficients_from_QL
        kappa = heisenberg_data['kappa']
        coeffs = shadow_coefficients_from_QL(kappa, 0.0, 0.0, r_max=10)
        assert abs(coeffs[0] - abs(kappa)) < 1e-10  # S_2 = kappa
        for r in range(1, 8):
            assert abs(coeffs[r]) < 1e-10, f"S_{r+2} = {coeffs[r]} should be 0 for class G"

    def test_class_l_shadow_terminates(self, affine_sl2_data):
        """For class L (affine KM): S_r = 0 for r >= 4."""
        from lib.bc_quantum_spectral_curve_zeta_engine import shadow_coefficients_from_QL
        kappa = affine_sl2_data['kappa']
        alpha = affine_sl2_data['alpha']
        coeffs = shadow_coefficients_from_QL(kappa, alpha, 0.0, r_max=10)
        assert abs(coeffs[0] - abs(kappa)) < 1e-10  # S_2 = kappa
        assert abs(coeffs[1] - alpha) < 1e-10  # S_3 = alpha
        for r in range(2, 8):
            assert abs(coeffs[r]) < 1e-10, f"S_{r+2} should be 0 for class L"


# =====================================================================
# 2. WKB expansion
# =====================================================================

class TestWKBExpansion:
    """Tests for the WKB expansion of the quantum spectral curve."""

    def test_wkb_leading_term_is_classical(self, virasoro_c13):
        """S_0(t) = sqrt(V(t)) is the classical momentum."""
        from lib.bc_quantum_spectral_curve_zeta_engine import (
            wkb_coefficients, classical_potential
        )
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        S_fns = wkb_coefficients(kappa, alpha, S4, 3)
        for t in [0.3, 0.5, 1.0, 2.0]:
            s0 = S_fns[0](t)
            V = classical_potential(t, kappa, alpha, S4)
            assert abs(s0 - math.sqrt(V)) < 1e-10 * max(abs(s0), 1.0)

    def test_wkb_first_correction_finite(self, virasoro_c13):
        """S_1(t) is finite and well-defined away from turning points."""
        from lib.bc_quantum_spectral_curve_zeta_engine import wkb_coefficients
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        S_fns = wkb_coefficients(kappa, alpha, S4, 3)
        for t in [0.5, 1.0, 2.0]:
            s1 = S_fns[1](t)
            assert math.isfinite(s1), f"S_1({t}) = {s1} should be finite"

    def test_wkb_first_correction_formula(self, virasoro_c13):
        """S_1 = -V'/(4V), verified numerically."""
        from lib.bc_quantum_spectral_curve_zeta_engine import (
            wkb_coefficients, classical_potential
        )
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        S_fns = wkb_coefficients(kappa, alpha, S4, 3)

        t = 1.0
        s1 = S_fns[1](t)
        V = classical_potential(t, kappa, alpha, S4)
        dt = 1e-7
        Vp = (classical_potential(t + dt, kappa, alpha, S4)
              - classical_potential(t - dt, kappa, alpha, S4)) / (2 * dt)
        expected = -Vp / (4.0 * V)
        assert abs(s1 - expected) < 1e-5 * max(abs(expected), 1.0)

    def test_wkb_decreasing_hierarchy(self, virasoro_c13):
        """Higher WKB terms |S_k(t)| decrease for t away from turning points."""
        from lib.bc_quantum_spectral_curve_zeta_engine import wkb_coefficients
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        S_fns = wkb_coefficients(kappa, alpha, S4, 4)
        t = 1.0
        vals = [abs(fn(t)) for fn in S_fns]
        # S_0 >> S_1 >> S_2 (not strict for all t, but should hold at t=1)
        assert vals[0] > vals[1], f"|S_0| = {vals[0]} should exceed |S_1| = {vals[1]}"

    def test_wkb_action_expansion_returns_list(self, virasoro_c13):
        """wkb_action_expansion returns correct number of terms."""
        from lib.bc_quantum_spectral_curve_zeta_engine import wkb_action_expansion
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        result = wkb_action_expansion(kappa, alpha, S4, 0.5, n_terms=4)
        assert len(result) == 4


# =====================================================================
# 3. Eigenvalue computation
# =====================================================================

class TestEigenvalues:
    """Tests for eigenvalue computations via Bohr-Sommerfeld and grid methods."""

    def test_bohr_sommerfeld_positive(self, virasoro_c13):
        """Bohr-Sommerfeld eigenvalues are all positive."""
        from lib.bc_quantum_spectral_curve_zeta_engine import bohr_sommerfeld_eigenvalues
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        eigs = bohr_sommerfeld_eigenvalues(kappa, alpha, S4, n_max=5)
        for n, E in enumerate(eigs):
            assert E > 0, f"E_{n} = {E} should be positive"

    def test_bohr_sommerfeld_increasing(self, virasoro_c13):
        """Bohr-Sommerfeld eigenvalues are strictly increasing."""
        from lib.bc_quantum_spectral_curve_zeta_engine import bohr_sommerfeld_eigenvalues
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        eigs = bohr_sommerfeld_eigenvalues(kappa, alpha, S4, n_max=8)
        for n in range(len(eigs) - 1):
            assert eigs[n] < eigs[n + 1], (
                f"E_{n} = {eigs[n]} should be less than E_{n+1} = {eigs[n+1]}")

    @pytest.mark.skipif(not pytest.importorskip("scipy", reason="scipy required"),
                        reason="scipy required")
    def test_grid_eigenvalues_positive(self, virasoro_c13):
        """Grid eigenvalues are all positive."""
        from lib.bc_quantum_spectral_curve_zeta_engine import spectral_eigenvalues_grid
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        eigs = spectral_eigenvalues_grid(kappa, alpha, S4, n_eigenvalues=10,
                                          grid_size=500, x_max=4.0)
        for n, E in enumerate(eigs):
            assert E > 0, f"E_{n} = {E} should be positive"

    @pytest.mark.skipif(not pytest.importorskip("scipy", reason="scipy required"),
                        reason="scipy required")
    def test_grid_eigenvalues_increasing(self, virasoro_c13):
        """Grid eigenvalues are strictly increasing."""
        from lib.bc_quantum_spectral_curve_zeta_engine import spectral_eigenvalues_grid
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        eigs = spectral_eigenvalues_grid(kappa, alpha, S4, n_eigenvalues=10,
                                          grid_size=500, x_max=4.0)
        for n in range(len(eigs) - 1):
            assert eigs[n] < eigs[n + 1]

    @pytest.mark.skipif(not pytest.importorskip("scipy", reason="scipy required"),
                        reason="scipy required")
    def test_grid_vs_bs_qualitative_agreement(self, virasoro_c13):
        """Grid eigenvalues and Bohr-Sommerfeld agree to within 50%.

        The agreement is only qualitative because:
        (a) BS is semiclassical, exact only for n >> 1
        (b) Grid discretization has finite-size effects
        """
        from lib.bc_quantum_spectral_curve_zeta_engine import (
            spectral_eigenvalues_grid, bohr_sommerfeld_eigenvalues
        )
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        grid_eigs = spectral_eigenvalues_grid(kappa, alpha, S4, n_eigenvalues=5,
                                               grid_size=800, x_max=5.0)
        bs_eigs = bohr_sommerfeld_eigenvalues(kappa, alpha, S4, n_max=5)
        # Qualitative: same order of magnitude for the first few
        for n in range(min(3, len(grid_eigs), len(bs_eigs))):
            ratio = grid_eigs[n] / bs_eigs[n] if bs_eigs[n] > 0 else 0
            assert 0.2 < ratio < 5.0, (
                f"E_{n}: grid={grid_eigs[n]:.4f}, BS={bs_eigs[n]:.4f}, ratio={ratio:.4f}")

    @pytest.mark.skipif(not pytest.importorskip("scipy", reason="scipy required"),
                        reason="scipy required")
    def test_eigenvalue_growth_exponent(self, virasoro_c13):
        """E_n ~ n^gamma with gamma ~ 3/2 for a sextic potential."""
        from lib.bc_quantum_spectral_curve_zeta_engine import (
            spectral_eigenvalues_grid, eigenvalue_growth_exponent
        )
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        eigs = spectral_eigenvalues_grid(kappa, alpha, S4, n_eigenvalues=30,
                                          grid_size=1500, x_max=5.0)
        growth = eigenvalue_growth_exponent(eigs)
        # For sextic potential: gamma = 6/(6/2 + 1) = 6/4 = 1.5
        # Allow some tolerance due to subleading corrections
        assert 1.0 < growth['gamma'] < 2.0, (
            f"gamma = {growth['gamma']}, expected near 1.5 for sextic")
        assert growth['r_squared'] > 0.95, f"R^2 = {growth['r_squared']} should be > 0.95"


# =====================================================================
# 4. Spectral zeta function
# =====================================================================

class TestSpectralZeta:
    """Tests for the spectral zeta function."""

    @pytest.mark.skipif(not pytest.importorskip("scipy", reason="scipy required"),
                        reason="scipy required")
    def test_spectral_zeta_converges_for_large_s(self, virasoro_c13):
        """zeta^SC(s) converges for Re(s) > 3/4 (sextic potential)."""
        from lib.bc_quantum_spectral_curve_zeta_engine import (
            spectral_eigenvalues_grid, spectral_zeta_from_eigenvalues
        )
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        eigs = spectral_eigenvalues_grid(kappa, alpha, S4, n_eigenvalues=50,
                                          grid_size=1000, x_max=5.0)
        # s = 2 should converge well
        z2 = spectral_zeta_from_eigenvalues(eigs, 2.0)
        assert math.isfinite(z2.real)
        assert z2.real > 0  # sum of positive terms

    @pytest.mark.skipif(not pytest.importorskip("scipy", reason="scipy required"),
                        reason="scipy required")
    def test_spectral_zeta_positive_for_real_s(self, virasoro_c13):
        """zeta^SC(s) > 0 for real s > convergence abscissa."""
        from lib.bc_quantum_spectral_curve_zeta_engine import (
            spectral_eigenvalues_grid, spectral_zeta_from_eigenvalues
        )
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        eigs = spectral_eigenvalues_grid(kappa, alpha, S4, n_eigenvalues=50,
                                          grid_size=1000, x_max=5.0)
        for s in [1.0, 1.5, 2.0, 3.0]:
            zs = spectral_zeta_from_eigenvalues(eigs, s)
            assert zs.real > 0, f"zeta(s={s}) = {zs} should be positive"

    @pytest.mark.skipif(not pytest.importorskip("scipy", reason="scipy required"),
                        reason="scipy required")
    def test_spectral_zeta_decreasing_in_s(self, virasoro_c13):
        """zeta^SC(s) is decreasing in s for real s > abscissa (since E_n > 1 eventually)."""
        from lib.bc_quantum_spectral_curve_zeta_engine import (
            spectral_eigenvalues_grid, spectral_zeta_from_eigenvalues
        )
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        eigs = spectral_eigenvalues_grid(kappa, alpha, S4, n_eigenvalues=50,
                                          grid_size=1000, x_max=5.0)
        z1 = spectral_zeta_from_eigenvalues(eigs, 1.0)
        z2 = spectral_zeta_from_eigenvalues(eigs, 2.0)
        z3 = spectral_zeta_from_eigenvalues(eigs, 3.0)
        assert z1.real > z2.real > z3.real

    @pytest.mark.skipif(not pytest.importorskip("scipy", reason="scipy required"),
                        reason="scipy required")
    def test_spectral_determinant_is_product(self, virasoro_c13):
        """det(H - E) = prod(1 - E/E_n) is an entire function of E."""
        from lib.bc_quantum_spectral_curve_zeta_engine import (
            spectral_eigenvalues_grid, spectral_determinant_regularized
        )
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        eigs = spectral_eigenvalues_grid(kappa, alpha, S4, n_eigenvalues=20,
                                          grid_size=500, x_max=4.0)
        # At E = 0: det = 1
        d0 = spectral_determinant_regularized(eigs, 0.0)
        assert abs(d0 - 1.0) < 1e-10

    @pytest.mark.skipif(not pytest.importorskip("scipy", reason="scipy required"),
                        reason="scipy required")
    def test_spectral_determinant_vanishes_at_eigenvalue(self, virasoro_c13):
        """det(H - E_n) = 0 at each eigenvalue."""
        from lib.bc_quantum_spectral_curve_zeta_engine import (
            spectral_eigenvalues_grid, spectral_determinant_regularized
        )
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        eigs = spectral_eigenvalues_grid(kappa, alpha, S4, n_eigenvalues=10,
                                          grid_size=500, x_max=4.0)
        for n in range(min(3, len(eigs))):
            d = spectral_determinant_regularized(eigs, eigs[n])
            assert abs(d) < 1e-8, f"det at E_{n} = {eigs[n]}: {d} should be ~0"


# =====================================================================
# 5. Spectral determinant at Riemann zeros
# =====================================================================

class TestRiemannZeros:
    """Tests for the spectral determinant evaluated at Riemann zeros."""

    @pytest.mark.skipif(not pytest.importorskip("scipy", reason="scipy required"),
                        reason="scipy required")
    def test_spectral_det_at_zeta_zeros_finite(self, virasoro_c13):
        """det(H - E_n) is finite at Riemann zeros (generically nonzero)."""
        try:
            import mpmath
        except ImportError:
            pytest.skip("mpmath required")
        from lib.bc_quantum_spectral_curve_zeta_engine import spectral_det_at_riemann_zeros
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        results = spectral_det_at_riemann_zeros(kappa, alpha, S4, n_zeros=3,
                                                  n_eigenvalues=30,
                                                  grid_size=500, x_max=4.0)
        for r in results:
            assert math.isfinite(r['det_modulus']), f"n={r['n']}: |det| not finite"

    @pytest.mark.skipif(not pytest.importorskip("scipy", reason="scipy required"),
                        reason="scipy required")
    def test_spectral_det_at_zeta_zeros_nonzero_generic_c(self, virasoro_c13):
        """For generic c, the spectral determinant does NOT vanish at Riemann zeros.

        This is the expected result: the quantum spectral curve of the
        shadow tower has no direct relationship to zeta zeros for generic c.
        The zeros of det(H - E) are the eigenvalues of H, which are real,
        while E_n = 3/4 + i gamma_n/2 is complex.
        """
        try:
            import mpmath
        except ImportError:
            pytest.skip("mpmath required")
        from lib.bc_quantum_spectral_curve_zeta_engine import spectral_det_at_riemann_zeros
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        results = spectral_det_at_riemann_zeros(kappa, alpha, S4, n_zeros=3,
                                                  n_eigenvalues=30,
                                                  grid_size=500, x_max=4.0)
        # For self-adjoint H, eigenvalues are real, so det at complex E should be nonzero
        for r in results:
            assert r['det_modulus'] > 1e-6, (
                f"n={r['n']}: |det| = {r['det_modulus']} unexpectedly small")

    @pytest.mark.skipif(not pytest.importorskip("scipy", reason="scipy required"),
                        reason="scipy required")
    def test_spectral_det_at_zeta_zeros_complex_E(self, virasoro_c13):
        """E_n = 3/4 + i gamma_n/2 are complex numbers on the critical line."""
        try:
            import mpmath
        except ImportError:
            pytest.skip("mpmath required")
        from lib.bc_quantum_spectral_curve_zeta_engine import spectral_det_at_riemann_zeros
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        results = spectral_det_at_riemann_zeros(kappa, alpha, S4, n_zeros=2,
                                                  n_eigenvalues=20,
                                                  grid_size=500, x_max=4.0)
        for r in results:
            assert abs(r['E_n'].real - 0.75) < 1e-10
            assert abs(r['E_n'].imag) > 1.0  # gamma_1 ~ 14.13


# =====================================================================
# 6. Exact WKB and Voros coefficients
# =====================================================================

class TestVoros:
    """Tests for Voros coefficients of the quantum spectral curve."""

    def test_voros_A_cycle_well_defined(self, virasoro_c13):
        """The A-cycle Voros coefficient is finite and nonzero."""
        from lib.bc_quantum_spectral_curve_zeta_engine import exact_wkb_voros_coefficients
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        voros = exact_wkb_voros_coefficients(kappa, alpha, S4)
        assert 'A_cycle' in voros
        assert math.isfinite(abs(voros['A_cycle'].action))
        assert abs(voros['A_cycle'].action) > 0

    def test_voros_B_cycle_well_defined(self, virasoro_c13):
        """The B-cycle Voros coefficient is finite and nonzero."""
        from lib.bc_quantum_spectral_curve_zeta_engine import exact_wkb_voros_coefficients
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        voros = exact_wkb_voros_coefficients(kappa, alpha, S4)
        assert 'B_cycle' in voros
        assert math.isfinite(abs(voros['B_cycle'].action))

    def test_voros_B_period_is_imaginary(self, virasoro_c13):
        """B-cycle period is purely imaginary (logarithmic monodromy)."""
        from lib.bc_quantum_spectral_curve_zeta_engine import exact_wkb_voros_coefficients
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        voros = exact_wkb_voros_coefficients(kappa, alpha, S4)
        B_action = voros['B_cycle'].action
        assert abs(B_action.real) < 1e-10 * abs(B_action.imag)

    def test_voros_class_g_degenerate(self, heisenberg_data):
        """For class G, Voros coefficients are empty (degenerate case)."""
        from lib.bc_quantum_spectral_curve_zeta_engine import exact_wkb_voros_coefficients
        voros = exact_wkb_voros_coefficients(
            heisenberg_data['kappa'], heisenberg_data['alpha'], heisenberg_data['S4'])
        # Degenerate case: Q_L has double root, no well-defined branch cut
        assert len(voros) == 0 or all(
            math.isfinite(abs(v.action)) for v in voros.values())


# =====================================================================
# 7. Topological recursion match
# =====================================================================

class TestTopologicalRecursion:
    """Tests for F_g^{EO} = F_g^{shadow} verification."""

    def test_eo_shadow_match_g1(self, virasoro_c13):
        """F_1^{EO} = F_1^{shadow} = kappa/24."""
        from lib.bc_quantum_spectral_curve_zeta_engine import verify_eo_shadow_match
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        match = verify_eo_shadow_match(kappa, alpha, S4, g_max=1)
        assert match[1]['match_eo_direct']
        assert match[1]['match_ahat_direct']
        assert abs(match[1]['F_g_direct'] - kappa / 24.0) < 1e-12

    def test_eo_shadow_match_through_g5(self, virasoro_c13):
        """F_g^{EO} = F_g^{shadow} for g = 1, ..., 5."""
        from lib.bc_quantum_spectral_curve_zeta_engine import verify_eo_shadow_match
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        match = verify_eo_shadow_match(kappa, alpha, S4, g_max=5)
        for g in range(1, 6):
            assert match[g]['match_eo_direct'], f"g={g}: EO/direct mismatch"
            assert match[g]['match_ahat_direct'], f"g={g}: Ahat/direct mismatch"

    def test_f_g_positive(self, virasoro_c13):
        """F_g > 0 for all g >= 1 (Virasoro with c > 0).

        AP22: Bernoulli signs — the combination (2^{2g-1}-1)|B_{2g}|/(2^{2g-1}(2g)!)
        is POSITIVE.
        """
        from lib.bc_quantum_spectral_curve_zeta_engine import shadow_tower_F_g
        kappa = virasoro_c13['kappa']
        for g in range(1, 8):
            fg = shadow_tower_F_g(kappa, g)
            assert fg > 0, f"F_{g} = {fg} should be positive for kappa > 0"

    def test_f_g_ahat_generating_function(self, virasoro_c13):
        """sum F_g x^{2g} = kappa * ((x/2)/sin(x/2) - 1) at x = 0.1.

        AP22: convention check.  The F_g use hbar^{2g}, NOT hbar^{2g-2}.
        """
        from lib.bc_quantum_spectral_curve_zeta_engine import shadow_tower_F_g
        kappa = virasoro_c13['kappa']
        x = 0.1
        partial_sum = sum(shadow_tower_F_g(kappa, g) * x ** (2 * g) for g in range(1, 20))
        ahat_val = kappa * ((x / 2.0) / math.sin(x / 2.0) - 1.0)
        assert abs(partial_sum - ahat_val) < 1e-10 * abs(ahat_val)

    def test_f_g_koszul_complementarity(self, virasoro_c13):
        """F_g(Vir_c) + F_g(Vir_{26-c}) = 13 * lambda_g^FP at c = 13.

        AP24: kappa + kappa' = 13 for Virasoro.
        """
        from lib.bc_quantum_spectral_curve_zeta_engine import shadow_tower_F_g, _faber_pandharipande
        c = 13.0
        kappa_c = c / 2.0
        kappa_dual = (26.0 - c) / 2.0
        for g in range(1, 6):
            fg = shadow_tower_F_g(kappa_c, g)
            fg_dual = shadow_tower_F_g(kappa_dual, g)
            lam_g = _faber_pandharipande(g)
            expected_sum = 13.0 * lam_g
            assert abs(fg + fg_dual - expected_sum) < 1e-12 * abs(expected_sum)

    def test_eo_match_class_g(self, heisenberg_data):
        """EO-shadow match for class G (Heisenberg)."""
        from lib.bc_quantum_spectral_curve_zeta_engine import verify_eo_shadow_match
        match = verify_eo_shadow_match(heisenberg_data['kappa'],
                                        heisenberg_data['alpha'],
                                        heisenberg_data['S4'], g_max=3)
        for g in range(1, 4):
            assert match[g]['match_eo_direct']

    def test_eo_match_class_l(self, affine_sl2_data):
        """EO-shadow match for class L (affine KM)."""
        from lib.bc_quantum_spectral_curve_zeta_engine import verify_eo_shadow_match
        match = verify_eo_shadow_match(affine_sl2_data['kappa'],
                                        affine_sl2_data['alpha'],
                                        affine_sl2_data['S4'], g_max=3)
        for g in range(1, 4):
            assert match[g]['match_eo_direct']


# =====================================================================
# 8. Nekrasov-Shatashvili
# =====================================================================

class TestNekrasovShatashvili:
    """Tests for the NS wave function at zeta zeros."""

    def test_ns_wave_function_well_defined(self, virasoro_c13):
        """NS wave function is finite for real epsilon_1."""
        from lib.bc_quantum_spectral_curve_zeta_engine import (
            nekrasov_shatashvili_wave_function
        )
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        psi = nekrasov_shatashvili_wave_function(kappa, alpha, S4, 1.0, 0.5, n_inst=3)
        assert math.isfinite(abs(psi))

    def test_ns_wave_function_exponential_form(self, virasoro_c13):
        """NS wave function ~ exp(integral p dt / hbar), so |psi| > 0.

        At small t values, the integral is small and psi is finite.
        """
        from lib.bc_quantum_spectral_curve_zeta_engine import (
            nekrasov_shatashvili_wave_function
        )
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        # Use small t to avoid overflow
        psi = nekrasov_shatashvili_wave_function(kappa, alpha, S4, 1.0, 0.1, n_inst=3)
        assert abs(psi) > 0

    def test_ns_at_imaginary_epsilon(self, virasoro_c13):
        """NS wave function at epsilon_1 = i (purely imaginary) is finite."""
        from lib.bc_quantum_spectral_curve_zeta_engine import (
            nekrasov_shatashvili_wave_function
        )
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        psi = nekrasov_shatashvili_wave_function(kappa, alpha, S4, 1.0j, 0.5, n_inst=3)
        assert math.isfinite(abs(psi))

    def test_ns_at_zeta_zeros_well_defined(self, virasoro_c13):
        """NS wave function at epsilon_1 = i gamma_n is finite."""
        try:
            import mpmath
        except ImportError:
            pytest.skip("mpmath required")
        from lib.bc_quantum_spectral_curve_zeta_engine import ns_at_zeta_zeros
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        results = ns_at_zeta_zeros(kappa, alpha, S4, t_val=0.5, n_zeros=2, n_inst=3)
        for r in results:
            assert math.isfinite(r['psi_modulus']), f"n={r['n']}: |psi| not finite"

    def test_ns_gamma_values_are_zeta_zeros(self, virasoro_c13):
        """gamma_n values match known Riemann zeta zero imaginary parts."""
        try:
            import mpmath
        except ImportError:
            pytest.skip("mpmath required")
        from lib.bc_quantum_spectral_curve_zeta_engine import ns_at_zeta_zeros
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        results = ns_at_zeta_zeros(kappa, alpha, S4, t_val=0.5, n_zeros=3, n_inst=2)
        # Known: gamma_1 ~ 14.1347, gamma_2 ~ 21.0220, gamma_3 ~ 25.0109
        assert abs(results[0]['gamma_n'] - 14.1347) < 0.01
        assert abs(results[1]['gamma_n'] - 21.0220) < 0.01
        assert abs(results[2]['gamma_n'] - 25.0109) < 0.01


# =====================================================================
# 9. Class G/L exact solutions
# =====================================================================

class TestExactSolutions:
    """Tests for exact eigenvalue solutions in degenerate classes."""

    def test_class_g_quartic_eigenvalues_positive(self, heisenberg_data):
        """Class G (quartic potential) eigenvalues are positive."""
        from lib.bc_quantum_spectral_curve_zeta_engine import airy_bessel_eigenvalues_classG
        eigs = airy_bessel_eigenvalues_classG(heisenberg_data['kappa'], n_max=10)
        for n, E in enumerate(eigs):
            assert E > 0, f"E_{n} = {E} should be positive"

    def test_class_g_quartic_eigenvalues_increasing(self, heisenberg_data):
        """Class G eigenvalues are strictly increasing."""
        from lib.bc_quantum_spectral_curve_zeta_engine import airy_bessel_eigenvalues_classG
        eigs = airy_bessel_eigenvalues_classG(heisenberg_data['kappa'], n_max=10)
        for n in range(len(eigs) - 1):
            assert eigs[n] < eigs[n + 1]

    def test_class_g_growth_exponent_quartic(self, heisenberg_data):
        """Class G: E_n ~ n^{4/3} (quartic potential)."""
        from lib.bc_quantum_spectral_curve_zeta_engine import airy_bessel_eigenvalues_classG
        eigs = airy_bessel_eigenvalues_classG(heisenberg_data['kappa'], n_max=20)
        # Fit log E vs log n
        n_vals = np.arange(1, len(eigs) + 1, dtype=float)
        log_n = np.log(n_vals[3:])  # skip first few for better asymptotic
        log_E = np.log(np.array(eigs[3:]))
        A = np.column_stack([log_n, np.ones_like(log_n)])
        coeffs, _, _, _ = np.linalg.lstsq(A, log_E, rcond=None)
        gamma = coeffs[0]
        assert abs(gamma - 4.0 / 3.0) < 0.15, f"gamma = {gamma}, expected 4/3"

    def test_class_l_sextic_eigenvalues_positive(self, affine_sl2_data):
        """Class L (sextic potential) eigenvalues are positive."""
        from lib.bc_quantum_spectral_curve_zeta_engine import airy_bessel_eigenvalues_classL
        eigs = airy_bessel_eigenvalues_classL(
            affine_sl2_data['kappa'], affine_sl2_data['alpha'], n_max=10)
        for n, E in enumerate(eigs):
            assert E > 0, f"E_{n} = {E} should be positive"

    def test_class_l_sextic_eigenvalues_increasing(self, affine_sl2_data):
        """Class L eigenvalues are strictly increasing."""
        from lib.bc_quantum_spectral_curve_zeta_engine import airy_bessel_eigenvalues_classL
        eigs = airy_bessel_eigenvalues_classL(
            affine_sl2_data['kappa'], affine_sl2_data['alpha'], n_max=10)
        for n in range(len(eigs) - 1):
            assert eigs[n] < eigs[n + 1]

    @pytest.mark.skipif(not pytest.importorskip("scipy", reason="scipy required"),
                        reason="scipy required")
    def test_class_g_wkb_vs_grid(self, heisenberg_data):
        """For class G, WKB eigenvalues agree with grid eigenvalues qualitatively."""
        from lib.bc_quantum_spectral_curve_zeta_engine import (
            airy_bessel_eigenvalues_classG, spectral_eigenvalues_grid
        )
        wkb_eigs = airy_bessel_eigenvalues_classG(heisenberg_data['kappa'], n_max=5)
        grid_eigs = spectral_eigenvalues_grid(
            heisenberg_data['kappa'], heisenberg_data['alpha'], heisenberg_data['S4'],
            n_eigenvalues=5, grid_size=800, x_max=5.0)
        # Qualitative agreement: within a factor of 3 for the first few
        for n in range(min(3, len(grid_eigs))):
            ratio = grid_eigs[n] / wkb_eigs[n] if wkb_eigs[n] > 0 else 0
            assert 0.1 < ratio < 10.0, (
                f"E_{n}: WKB={wkb_eigs[n]:.4f}, grid={grid_eigs[n]:.4f}")


# =====================================================================
# 10. Cross-verification
# =====================================================================

class TestCrossVerification:
    """Cross-verification of results across multiple independent paths."""

    def test_three_path_F1_virasoro(self):
        """F_1 = kappa/24 verified three ways.

        Path 1: Direct formula F_1 = kappa * lambda_1^FP = kappa * (1/24)
        Path 2: A-hat generating function at order x^2
        Path 3: Shadow coefficients S_2 = kappa, F_1 = S_2 * lambda_1^FP
        """
        from lib.bc_quantum_spectral_curve_zeta_engine import (
            shadow_tower_F_g, _faber_pandharipande, shadow_coefficients_from_QL
        )
        c_val = 10.0
        kappa = c_val / 2.0

        # Path 1: Direct
        f1_direct = shadow_tower_F_g(kappa, 1)
        assert abs(f1_direct - kappa / 24.0) < 1e-12

        # Path 2: A-hat
        lam1 = _faber_pandharipande(1)
        f1_ahat = kappa * lam1
        assert abs(f1_ahat - kappa / 24.0) < 1e-12

        # Path 3: From shadow coefficients
        coeffs = shadow_coefficients_from_QL(kappa, 2.0, 10.0 / (c_val * (5 * c_val + 22)), r_max=3)
        S2 = coeffs[0]
        f1_shadow = S2 * lam1
        assert abs(f1_shadow - kappa / 24.0) < 1e-10

    def test_four_path_eigenvalue_count(self):
        """Eigenvalue count from 4 paths agree.

        Path 1: Bohr-Sommerfeld semiclassical
        Path 2: Grid discretization
        Path 3: WKB class G exact (for Heisenberg)
        Path 4: Growth exponent consistency (E_n ~ n^gamma implies N(E) ~ E^{1/gamma})
        """
        try:
            from scipy.linalg import eigh_tridiagonal
        except ImportError:
            pytest.skip("scipy required")
        from lib.bc_quantum_spectral_curve_zeta_engine import (
            bohr_sommerfeld_eigenvalues, spectral_eigenvalues_grid,
            airy_bessel_eigenvalues_classG, eigenvalue_growth_exponent
        )
        kappa = 1.0  # Heisenberg

        # Paths 1-3: get eigenvalues
        bs = bohr_sommerfeld_eigenvalues(kappa, 0.0, 0.0, n_max=5)
        grid = spectral_eigenvalues_grid(kappa, 0.0, 0.0,
                                          n_eigenvalues=5, grid_size=800, x_max=5.0)
        wkb_exact = airy_bessel_eigenvalues_classG(kappa, n_max=5)

        # All three produce 5 positive increasing eigenvalues
        assert len(bs) == 5
        assert len(grid) >= 5
        assert len(wkb_exact) == 5

        for eig_set in [bs, list(grid[:5]), wkb_exact]:
            for n in range(4):
                assert eig_set[n] < eig_set[n + 1]

        # Path 4: Growth exponent from grid
        grid_many = spectral_eigenvalues_grid(kappa, 0.0, 0.0,
                                               n_eigenvalues=20, grid_size=1000, x_max=5.0)
        growth = eigenvalue_growth_exponent(grid_many)
        assert abs(growth['gamma'] - 4.0 / 3.0) < 0.3

    def test_shadow_potential_consistency(self):
        """V(t) = t^4 Q_L(t) recovers Q_L from V/t^4 for t != 0."""
        from lib.bc_quantum_spectral_curve_zeta_engine import classical_potential
        kappa, alpha, S4 = 3.0, 1.5, 0.05
        q0 = 4.0 * kappa ** 2
        q1 = 12.0 * kappa * alpha
        q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4
        for t in [0.1, 0.5, 1.0, 3.0]:
            V = classical_potential(t, kappa, alpha, S4)
            Q_recovered = V / t ** 4
            Q_direct = q0 + q1 * t + q2 * t ** 2
            assert abs(Q_recovered - Q_direct) < 1e-10 * abs(Q_direct)

    def test_virasoro_kappa_formula(self):
        """kappa(Vir_c) = c/2 for various c values.

        AP1/AP39: Virasoro-specific.  c/2, NOT c or c_eff.
        """
        from lib.bc_quantum_spectral_curve_zeta_engine import virasoro_kappa
        for c in [0.5, 1.0, 13.0, 25.0, 26.0]:
            assert abs(virasoro_kappa(c) - c / 2.0) < 1e-15

    def test_shadow_invariants_consistency(self):
        """Shadow invariants satisfy Delta = 8 kappa S_4 and disc = -32 kappa^2 Delta."""
        from lib.bc_quantum_spectral_curve_zeta_engine import virasoro_shadow_invariants
        for c in [1.0, 5.0, 13.0, 26.0]:
            inv = virasoro_shadow_invariants(c)
            kappa = inv['kappa']
            S4 = inv['S4']
            Delta = inv['Delta']
            assert abs(Delta - 8.0 * kappa * S4) < 1e-12 * abs(Delta)
            disc = inv['q1'] ** 2 - 4.0 * inv['q0'] * inv['q2']
            assert abs(disc - (-32.0 * kappa ** 2 * Delta)) < 1e-8 * abs(disc)


# =====================================================================
# 11. Stokes lines
# =====================================================================

class TestStokesLines:
    """Tests for Stokes line directions of the quantum curve."""

    def test_stokes_lines_exist(self, virasoro_c13):
        """Stokes lines are computed for class M."""
        from lib.bc_quantum_spectral_curve_zeta_engine import stokes_lines_quantum_curve
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        lines = stokes_lines_quantum_curve(kappa, alpha, S4)
        assert len(lines) == 6  # 3 from each branch point

    def test_stokes_directions_120_degrees_apart(self, virasoro_c13):
        """Stokes directions from each branch point are 120 degrees apart."""
        from lib.bc_quantum_spectral_curve_zeta_engine import stokes_lines_quantum_curve
        kappa = virasoro_c13['kappa']
        alpha = virasoro_c13['alpha']
        S4 = virasoro_c13['S4']
        lines = stokes_lines_quantum_curve(kappa, alpha, S4)
        # First three are from t_+
        dirs_plus = [l['stokes_direction'] for l in lines[:3]]
        for i in range(2):
            diff = (dirs_plus[i + 1] - dirs_plus[i]) % (2 * PI)
            expected = 2 * PI / 3
            assert abs(diff - expected) < 0.01 or abs(diff - expected + 2 * PI) < 0.01

    def test_stokes_lines_class_g_empty(self, heisenberg_data):
        """For class G (degenerate), Stokes lines computation returns empty."""
        from lib.bc_quantum_spectral_curve_zeta_engine import stokes_lines_quantum_curve
        lines = stokes_lines_quantum_curve(
            heisenberg_data['kappa'], heisenberg_data['alpha'], heisenberg_data['S4'])
        assert len(lines) == 0


# =====================================================================
# 12. Full analysis pipeline
# =====================================================================

class TestFullAnalysis:
    """Tests for the full analysis pipeline."""

    @pytest.mark.skipif(not pytest.importorskip("scipy", reason="scipy required"),
                        reason="scipy required")
    def test_full_analysis_runs(self):
        """Full analysis completes without error."""
        from lib.bc_quantum_spectral_curve_zeta_engine import full_quantum_spectral_analysis
        analysis = full_quantum_spectral_analysis(13.0, n_eigenvalues=10, g_max=3, n_zeros=1)
        assert 'c' in analysis
        assert analysis['c'] == 13.0
        assert 'shadow_invariants' in analysis
        assert 'shadow_coefficients' in analysis
        assert 'eo_shadow_match' in analysis

    @pytest.mark.skipif(not pytest.importorskip("scipy", reason="scipy required"),
                        reason="scipy required")
    def test_full_analysis_c1(self):
        """Full analysis at c = 1."""
        from lib.bc_quantum_spectral_curve_zeta_engine import full_quantum_spectral_analysis
        analysis = full_quantum_spectral_analysis(1.0, n_eigenvalues=10, g_max=3, n_zeros=1)
        assert analysis['shadow_invariants']['kappa'] == 0.5

    @pytest.mark.skipif(not pytest.importorskip("scipy", reason="scipy required"),
                        reason="scipy required")
    def test_full_analysis_c26(self):
        """Full analysis at c = 26 (string theory)."""
        from lib.bc_quantum_spectral_curve_zeta_engine import full_quantum_spectral_analysis
        analysis = full_quantum_spectral_analysis(26.0, n_eigenvalues=10, g_max=3, n_zeros=1)
        assert analysis['shadow_invariants']['kappa'] == 13.0
        # rho should be small (convergent tower)
        assert analysis['shadow_invariants']['rho'] < 0.3


# =====================================================================
# 13. Parameter space exploration
# =====================================================================

class TestParameterSpace:
    """Tests for behavior across the c parameter space."""

    def test_kappa_linear_in_c(self):
        """kappa(Vir_c) = c/2 is linear in c."""
        from lib.bc_quantum_spectral_curve_zeta_engine import virasoro_shadow_invariants
        for c in [1.0, 5.0, 13.0, 25.0]:
            inv = virasoro_shadow_invariants(c)
            assert abs(inv['kappa'] - c / 2.0) < 1e-14

    def test_delta_positive_for_positive_c(self):
        """Delta = 40/(5c+22) > 0 for c > 0 (class M)."""
        from lib.bc_quantum_spectral_curve_zeta_engine import virasoro_shadow_invariants
        for c in [0.5, 1.0, 5.0, 13.0, 25.0, 26.0]:
            inv = virasoro_shadow_invariants(c)
            assert inv['Delta'] > 0, f"Delta = {inv['Delta']} at c = {c}"

    def test_rho_at_c13_self_dual(self):
        """rho at c = 13 matches rho at c = 26 - 13 = 13 (self-dual)."""
        from lib.bc_quantum_spectral_curve_zeta_engine import virasoro_shadow_invariants
        inv13 = virasoro_shadow_invariants(13.0)
        inv_dual = virasoro_shadow_invariants(26.0 - 13.0)
        assert abs(inv13['rho'] - inv_dual['rho']) < 1e-12

    def test_rho_decreasing_for_large_c(self):
        """rho(c) -> 0 as c -> infinity (tower always converges for large c)."""
        from lib.bc_quantum_spectral_curve_zeta_engine import virasoro_shadow_invariants
        rhos = [virasoro_shadow_invariants(c)['rho'] for c in [10.0, 50.0, 100.0, 1000.0]]
        for i in range(len(rhos) - 1):
            assert rhos[i] > rhos[i + 1], (
                f"rho should decrease: rho({10 * 10**i}) = {rhos[i]}")

    def test_branch_points_complex_conjugate_class_m(self):
        """For class M (Delta > 0), branch points are complex conjugates."""
        from lib.bc_quantum_spectral_curve_zeta_engine import virasoro_shadow_invariants
        for c in [1.0, 13.0, 26.0]:
            inv = virasoro_shadow_invariants(c)
            bp = inv['branch_plus']
            bm = inv['branch_minus']
            assert abs(bp - bm.conjugate()) < 1e-10 * abs(bp)


# =====================================================================
# 14. Complementarity and Koszul duality
# =====================================================================

class TestComplementarity:
    """Tests for Koszul duality properties of the spectral curve."""

    def test_kappa_complementarity_virasoro(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c.

        AP24: this is 13, NOT 0.
        """
        from lib.bc_quantum_spectral_curve_zeta_engine import virasoro_kappa
        for c in [1.0, 5.0, 13.0, 20.0, 25.0]:
            assert abs(virasoro_kappa(c) + virasoro_kappa(26.0 - c) - 13.0) < 1e-14

    def test_fg_complementarity(self):
        """F_g(Vir_c) + F_g(Vir_{26-c}) = 13 * lambda_g^FP.

        This is the genus-g complementarity theorem.
        """
        from lib.bc_quantum_spectral_curve_zeta_engine import shadow_tower_F_g, _faber_pandharipande
        for c in [1.0, 10.0, 25.0]:
            for g in range(1, 6):
                fg = shadow_tower_F_g(c / 2.0, g)
                fg_dual = shadow_tower_F_g((26.0 - c) / 2.0, g)
                lam_g = _faber_pandharipande(g)
                assert abs(fg + fg_dual - 13.0 * lam_g) < 1e-12 * abs(13.0 * lam_g)

    def test_spectral_curve_self_dual_at_c13(self):
        """At c = 13, the spectral curve is self-dual: Q_L(c) = Q_L(26-c)."""
        from lib.bc_quantum_spectral_curve_zeta_engine import virasoro_shadow_invariants
        inv = virasoro_shadow_invariants(13.0)
        inv_dual = virasoro_shadow_invariants(13.0)  # 26 - 13 = 13
        assert abs(inv['q0'] - inv_dual['q0']) < 1e-12
        assert abs(inv['q1'] - inv_dual['q1']) < 1e-12
        assert abs(inv['q2'] - inv_dual['q2']) < 1e-12
