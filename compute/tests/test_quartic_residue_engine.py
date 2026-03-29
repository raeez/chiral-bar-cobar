"""Tests for compute/lib/quartic_residue_engine.py — Quartic residue programme.

Verifies:
  - Virasoro shadow data: H = c/2, C = 2, Q^ct = 10/[c(5c+22)]
  - Hankel matrix structure and determinant
  - Schur complement identity: Q^ct = mu_4 - C^2/H - H^2
  - Virasoro mu_4 decomposition: mu_4 = H^2 + C^2/H + Q^ct
  - Hankel determinant formula: D_2 = 5/(5c+22)
  - W_3 pure spin-3 slice: H_3 = c/3, C_3 = 0
  - Dirichlet-sewing lift for standard families
  - Euler-Koszul defect: D = 1 for weight-1 generators
  - Weight multisets for all standard families
  - Surface moment matrix (Hankel structure)
  - Leading minors computation
  - First zeta zero value
  - Full Virasoro package consistency
  - Cross-family consistency checks (AP10 prevention)

References:
  arithmetic_shadows.tex sec:quartic-residue-programme
  genus_complete.tex subsec:dirichlet-sewing-lift
"""

import pytest
from mpmath import mp, mpf, mpc, pi as mpi, zeta as mpzeta, fabs

from compute.lib.quartic_residue_engine import (
    virasoro_shadow_data,
    w3_shadow_data,
    w3_pure_spin3_data,
    hankel_3x3,
    hankel_determinant,
    schur_complement,
    virasoro_mu4,
    dirichlet_sewing_lift,
    dirichlet_sewing_lift_wn,
    euler_koszul_defect,
    euler_koszul_defect_wn,
    harmonic_partial,
    surface_moment_matrix,
    leading_minors,
    virasoro_hankel_det,
    virasoro_resonance_divisor,
    first_zeta_zero,
    nth_zeta_zero,
    wn_weights,
    heisenberg_weights,
    virasoro_weights,
    betagamma_weights,
    affine_weights,
    full_virasoro_package,
    w3_quartic_resonance_divisor,
    w3_spin3_mu4,
    compatibility_ratio_pot,
    compatibility_ratio_gram,
)


# Tolerance for high-precision comparisons
TOL = mpf('1e-30')


def approx_eq(a, b, tol=TOL):
    """Check approximate equality at high precision."""
    return fabs(a - b) < tol


# ═══════════════════════════════════════════════════════════════
# Import test
# ═══════════════════════════════════════════════════════════════

class TestImport:
    def test_module_loads(self):
        """Module imports without error."""
        import compute.lib.quartic_residue_engine
        assert hasattr(compute.lib.quartic_residue_engine, 'virasoro_shadow_data')


# ═══════════════════════════════════════════════════════════════
# Virasoro shadow data
# ═══════════════════════════════════════════════════════════════

class TestVirasiroShadowData:
    """Virasoro shadow data: H = c/2, C = 2, Q^ct = 10/[c(5c+22)]."""

    def test_c_equals_1(self):
        """Shadow data at c = 1."""
        H, C, Q = virasoro_shadow_data(1)
        assert approx_eq(H, mpf('0.5'))
        assert approx_eq(C, mpf(2))
        assert approx_eq(Q, mpf(10) / (1 * 27))  # 10/(1*27) = 10/27

    def test_c_equals_26(self):
        """Shadow data at c = 26 (bosonic string critical dimension)."""
        H, C, Q = virasoro_shadow_data(26)
        assert approx_eq(H, mpf(13))
        assert approx_eq(C, mpf(2))
        # Q^ct = 10 / (26 * (130 + 22)) = 10 / (26 * 152) = 10/3952
        assert approx_eq(Q, mpf(10) / (26 * 152))

    def test_c_equals_half(self):
        """Shadow data at c = 1/2 (Ising model)."""
        H, C, Q = virasoro_shadow_data(0.5)
        assert approx_eq(H, mpf('0.25'))
        assert approx_eq(C, mpf(2))
        # Q^ct = 10 / (0.5 * (2.5 + 22)) = 10 / (0.5 * 24.5) = 10/12.25
        assert approx_eq(Q, mpf(10) / (mpf('0.5') * mpf('24.5')))

    def test_curvature_is_c_over_2(self):
        """H = c/2 for several values of c (independent recomputation)."""
        for c_val in [1, 2, 5, 10, 26, 100]:
            H, _, _ = virasoro_shadow_data(c_val)
            assert approx_eq(H, mpf(c_val) / 2)

    def test_cubic_always_2(self):
        """C_cubic = 2 independent of c."""
        for c_val in [0.5, 1, 2, 10, 26]:
            _, C, _ = virasoro_shadow_data(c_val)
            assert approx_eq(C, mpf(2))

    def test_quartic_contact_formula(self):
        """Q^ct = 10/[c(5c+22)] for several values (independent computation)."""
        for c_val in [1, 2, 5, 10, 26]:
            c = mpf(c_val)
            _, _, Q = virasoro_shadow_data(c_val)
            expected = mpf(10) / (c * (5 * c + 22))
            assert approx_eq(Q, expected)


# ═══════════════════════════════════════════════════════════════
# W_3 data
# ═══════════════════════════════════════════════════════════════

class TestW3Data:
    def test_w3_spin2_matches_virasoro(self):
        """W_3 spin-2 channel shadow data equals Virasoro shadow data."""
        for c_val in [1, 10, 26]:
            h_v, c_v, q_v = virasoro_shadow_data(c_val)
            h_w, c_w, q_w = w3_shadow_data(c_val)
            assert approx_eq(h_v, h_w)
            assert approx_eq(c_v, c_w)
            assert approx_eq(q_v, q_w)

    def test_w3_spin3_curvature(self):
        """Pure spin-3 curvature: H_3 = c/3."""
        for c_val in [1, 3, 10]:
            H3, C3 = w3_pure_spin3_data(c_val)
            assert approx_eq(H3, mpf(c_val) / 3)

    def test_w3_spin3_cubic_vanishes(self):
        """Pure spin-3 cubic shadow C_3 = 0."""
        for c_val in [1, 3, 10]:
            _, C3 = w3_pure_spin3_data(c_val)
            assert approx_eq(C3, mpf(0))


# ═══════════════════════════════════════════════════════════════
# Hankel matrix and Schur complement
# ═══════════════════════════════════════════════════════════════

class TestHankel:
    """Test the 3x3 Hankel matrix and its invariants."""

    def test_hankel_structure(self):
        """Hankel matrix has correct shape and diagonal."""
        M = hankel_3x3(mpf(5), mpf(2), mpf(30))
        assert M.rows == 3 and M.cols == 3
        assert approx_eq(M[0, 0], mpf(1))
        assert approx_eq(M[0, 1], mpf(0))
        assert approx_eq(M[1, 1], mpf(5))  # H

    def test_hankel_symmetry(self):
        """Hankel matrix is symmetric."""
        M = hankel_3x3(mpf(5), mpf(2), mpf(30))
        for i in range(3):
            for j in range(3):
                assert approx_eq(M[i, j], M[j, i])

    def test_hankel_determinant_formula(self):
        """D_2 = H*mu4 - C^2 - H^3.

        Independent computation: D_2 = det of 3x3 with known entries.
        """
        H, C, mu4 = mpf(5), mpf(2), mpf(130)
        D = hankel_determinant(H, C, mu4)
        expected = H * mu4 - C**2 - H**3
        assert approx_eq(D, expected)

    def test_hankel_det_virasoro(self):
        """For Virasoro at c=10, D_2 should match 5/(5c+22)."""
        c = mpf(10)
        H, C, Q = virasoro_shadow_data(10)
        mu4 = virasoro_mu4(10)
        D = hankel_determinant(H, C, mu4)
        expected = mpf(5) / (5 * c + 22)
        assert approx_eq(D, expected, tol=mpf('1e-25'))

    def test_schur_complement_formula(self):
        """Sigma_2 = mu_4 - C^2/H - H^2."""
        H, C, mu4 = mpf(5), mpf(2), mpf(30)
        S = schur_complement(H, C, mu4)
        expected = mu4 - C**2 / H - H**2
        assert approx_eq(S, expected)

    def test_schur_complement_equals_qct_virasoro(self):
        """For Virasoro, the Schur complement equals Q^ct.

        This is the key identity: Sigma_2 = Q^ct = 10/[c(5c+22)].
        """
        for c_val in [1, 2, 5, 10, 26]:
            H, C, Q = virasoro_shadow_data(c_val)
            mu4 = virasoro_mu4(c_val)
            S = schur_complement(H, C, mu4)
            assert approx_eq(S, Q, tol=mpf('1e-25'))

    def test_hankel_det_is_h_times_schur(self):
        """D_2 = H * Sigma_2 (relationship between Hankel det and Schur)."""
        H, C, mu4 = mpf(5), mpf(2), mpf(30)
        D = hankel_determinant(H, C, mu4)
        S = schur_complement(H, C, mu4)
        assert approx_eq(D, H * S)


# ═══════════════════════════════════════════════════════════════
# Virasoro mu_4 and Hankel determinant
# ═══════════════════════════════════════════════════════════════

class TestVirasiroMu4:
    def test_mu4_decomposition(self):
        """mu_4 = H^2 + C^2/H + Q^ct for Virasoro.

        This is the defining decomposition that the module implements.
        Verify independently.
        """
        for c_val in [1, 2, 5, 10, 26]:
            c = mpf(c_val)
            H = c / 2
            C = mpf(2)
            Q = mpf(10) / (c * (5 * c + 22))
            expected = H**2 + C**2 / H + Q
            actual = virasoro_mu4(c_val)
            assert approx_eq(actual, expected, tol=mpf('1e-25'))

    def test_mu4_explicit_formula(self):
        """mu_4 = c^2/4 + 8/c + 10/[c(5c+22)].

        Verify: H^2 = c^2/4, C^2/H = 4/(c/2) = 8/c.
        """
        for c_val in [1, 2, 5, 10]:
            c = mpf(c_val)
            actual = virasoro_mu4(c_val)
            expected = c**2 / 4 + mpf(8) / c + mpf(10) / (c * (5 * c + 22))
            assert approx_eq(actual, expected)


class TestVirasiroHankelDet:
    def test_formula_5_over_5c_plus_22(self):
        """D_2^Vir = 5/(5c+22)."""
        for c_val in [1, 2, 5, 10, 26]:
            c = mpf(c_val)
            D = virasoro_hankel_det(c_val)
            expected = mpf(5) / (5 * c + 22)
            assert approx_eq(D, expected)

    def test_positive_for_positive_c(self):
        """D_2 > 0 for c > 0 (positive curvature => positive determinant)."""
        for c_val in [0.5, 1, 2, 10, 26, 100]:
            D = virasoro_hankel_det(c_val)
            assert D > 0

    def test_approaches_zero_as_c_grows(self):
        """D_2 -> 0 as c -> infinity (large-c limit)."""
        D_100 = virasoro_hankel_det(100)
        D_1000 = virasoro_hankel_det(1000)
        assert D_1000 < D_100
        assert D_1000 < mpf('0.001')

    def test_consistency_with_hankel_determinant_function(self):
        """D_2 from formula matches the generic hankel_determinant computation."""
        for c_val in [1, 5, 26]:
            formula_val = virasoro_hankel_det(c_val)
            H, C, Q = virasoro_shadow_data(c_val)
            mu4 = virasoro_mu4(c_val)
            generic_val = hankel_determinant(H, C, mu4)
            assert approx_eq(formula_val, generic_val, tol=mpf('1e-25'))


# ═══════════════════════════════════════════════════════════════
# Weight multisets
# ═══════════════════════════════════════════════════════════════

class TestWeightMultisets:
    def test_heisenberg(self):
        """Heisenberg: W = {1}."""
        assert heisenberg_weights() == [1]

    def test_virasoro(self):
        """Virasoro = W_2: W = {2}."""
        assert virasoro_weights() == [2]

    def test_betagamma(self):
        """betagamma: W = {1, 1}."""
        assert betagamma_weights() == [1, 1]

    def test_wn(self):
        """W_N: W = {2, 3, ..., N}."""
        assert wn_weights(2) == [2]
        assert wn_weights(3) == [2, 3]
        assert wn_weights(4) == [2, 3, 4]
        assert wn_weights(5) == [2, 3, 4, 5]

    def test_wn_length(self):
        """W_N weight multiset has N-1 elements."""
        for N in range(2, 10):
            assert len(wn_weights(N)) == N - 1

    def test_affine(self):
        """V_k(g): W = {1^dim(g)}."""
        assert affine_weights(3) == [1, 1, 1]
        assert affine_weights(8) == [1] * 8

    def test_virasoro_equals_w2(self):
        """Virasoro weights = W_2 weights."""
        assert virasoro_weights() == wn_weights(2)


# ═══════════════════════════════════════════════════════════════
# Harmonic partial sums
# ═══════════════════════════════════════════════════════════════

class TestHarmonicPartial:
    def test_h0(self):
        """H_0(u) = 0."""
        assert approx_eq(harmonic_partial(0, 2), mpf(0))

    def test_h1(self):
        """H_1(u) = 1^{-u} = 1."""
        assert approx_eq(harmonic_partial(1, 2), mpf(1))

    def test_h2_at_u1(self):
        """H_2(1) = 1 + 1/2 = 3/2."""
        assert approx_eq(harmonic_partial(2, 1), mpf(3) / 2)

    def test_h3_at_u2(self):
        """H_3(2) = 1 + 1/4 + 1/9 = 49/36."""
        assert approx_eq(harmonic_partial(3, 2), mpf(49) / 36)

    def test_negative_n(self):
        """H_n(u) = 0 for n <= 0."""
        assert approx_eq(harmonic_partial(-1, 2), mpf(0))

    def test_monotone_in_n(self):
        """H_n(u) is strictly increasing in n for u > 0."""
        for u in [1, 2, 3]:
            prev = harmonic_partial(0, u)
            for n in range(1, 10):
                curr = harmonic_partial(n, u)
                assert curr > prev
                prev = curr


# ═══════════════════════════════════════════════════════════════
# Dirichlet-sewing lift
# ═══════════════════════════════════════════════════════════════

class TestDirichletSewingLift:
    """Test the Dirichlet-sewing lift S_A(u)."""

    def test_heisenberg_formula(self):
        """Heisenberg: S = zeta(u) * zeta(u+1).

        For W = {1}: H_0(u) = 0, so S = zeta(u+1) * zeta(u).
        """
        mp.dps = 50
        for u_val in [2, 3, 5]:
            u = mpf(u_val)
            S = dirichlet_sewing_lift([1], u)
            expected = mpzeta(u) * mpzeta(u + 1)
            assert approx_eq(S, expected, tol=mpf('1e-25'))

    def test_betagamma_formula(self):
        """betagamma: S = 2 * zeta(u) * zeta(u+1).

        For W = {1, 1}: both w_i = 1, H_0(u) = 0.
        S = zeta(u+1) * 2 * zeta(u).
        """
        mp.dps = 50
        u = mpf(3)
        S = dirichlet_sewing_lift([1, 1], u)
        expected = 2 * mpzeta(u) * mpzeta(u + 1)
        assert approx_eq(S, expected, tol=mpf('1e-25'))

    def test_virasoro_formula(self):
        """Virasoro: S = zeta(u+1) * (zeta(u) - 1).

        For W = {2}: H_1(u) = 1, so S = zeta(u+1) * (zeta(u) - 1).
        """
        mp.dps = 50
        for u_val in [2, 3, 5]:
            u = mpf(u_val)
            S = dirichlet_sewing_lift([2], u)
            expected = mpzeta(u + 1) * (mpzeta(u) - 1)
            assert approx_eq(S, expected, tol=mpf('1e-25'))

    def test_wn_shortcut(self):
        """W_N shortcut should match general function with weights {2,...,N}."""
        mp.dps = 50
        u = mpf(3)
        for N in [2, 3, 4, 5]:
            S_general = dirichlet_sewing_lift(list(range(2, N + 1)), u)
            S_shortcut = dirichlet_sewing_lift_wn(N, u)
            assert approx_eq(S_general, S_shortcut, tol=mpf('1e-30'))

    def test_affine_formula(self):
        """Affine V_k(g): S = dim(g) * zeta(u) * zeta(u+1).

        All weights are 1, so each term contributes zeta(u).
        """
        mp.dps = 50
        u = mpf(3)
        for dim_g in [3, 8]:
            S = dirichlet_sewing_lift([1] * dim_g, u)
            expected = dim_g * mpzeta(u) * mpzeta(u + 1)
            assert approx_eq(S, expected, tol=mpf('1e-25'))

    def test_positive_for_large_u(self):
        """S_A(u) > 0 for u >> 1 (all terms positive for large real u)."""
        mp.dps = 50
        for weights in [[1], [2], [1, 1], [2, 3]]:
            S = dirichlet_sewing_lift(weights, mpf(10))
            assert S > 0


# ═══════════════════════════════════════════════════════════════
# Euler-Koszul defect
# ═══════════════════════════════════════════════════════════════

class TestEulerKoszulDefect:
    """Test the Euler-Koszul defect D_A(u)."""

    def test_heisenberg_exact(self):
        """Heisenberg: all weights = 1, so D = 1 (exact Euler-Koszul).

        D = (1/1) * (1 - H_0/zeta(u)) = 1 - 0 = 1.
        """
        mp.dps = 50
        for u_val in [2, 3, 5]:
            D = euler_koszul_defect([1], mpf(u_val))
            assert approx_eq(D, mpf(1), tol=mpf('1e-25'))

    def test_betagamma_exact(self):
        """betagamma: D = 1 (all weights = 1)."""
        mp.dps = 50
        D = euler_koszul_defect([1, 1], mpf(3))
        assert approx_eq(D, mpf(1), tol=mpf('1e-25'))

    def test_affine_exact(self):
        """Affine: D = 1 for any dim(g) (all weights = 1)."""
        mp.dps = 50
        for dim_g in [3, 8, 24]:
            D = euler_koszul_defect([1] * dim_g, mpf(3))
            assert approx_eq(D, mpf(1), tol=mpf('1e-25'))

    def test_virasoro_defect_less_than_1(self):
        """Virasoro: D < 1 (weight 2 introduces defect).

        D = 1 - H_1(u)/zeta(u) = 1 - 1/zeta(u) < 1 for u > 1.
        """
        mp.dps = 50
        for u_val in [2, 3, 5]:
            D = euler_koszul_defect([2], mpf(u_val))
            assert D < 1
            assert D > 0  # still positive

    def test_virasoro_defect_formula(self):
        """Virasoro defect: D = 1 - 1/zeta(u)."""
        mp.dps = 50
        for u_val in [2, 3, 5]:
            u = mpf(u_val)
            D = euler_koszul_defect([2], u)
            expected = 1 - 1 / mpzeta(u)
            assert approx_eq(D, expected, tol=mpf('1e-25'))

    def test_wn_shortcut(self):
        """W_N shortcut should match general function."""
        mp.dps = 50
        u = mpf(3)
        for N in [2, 3, 4]:
            D_gen = euler_koszul_defect(list(range(2, N + 1)), u)
            D_short = euler_koszul_defect_wn(N, u)
            assert approx_eq(D_gen, D_short, tol=mpf('1e-30'))

    def test_defect_decreases_with_higher_weights(self):
        """Higher weights increase the defect (D further from 1)."""
        mp.dps = 50
        u = mpf(3)
        D_w2 = euler_koszul_defect([2], u)
        D_w3 = euler_koszul_defect([3], u)
        # Both < 1, but D_w3 should be further from 1
        assert D_w3 < D_w2


# ═══════════════════════════════════════════════════════════════
# Surface moment matrix
# ═══════════════════════════════════════════════════════════════

class TestSurfaceMomentMatrix:
    def test_shape(self):
        """Surface moment matrix has correct shape."""
        mp.dps = 50
        M = surface_moment_matrix([1], mpf(3), 3)
        assert M.rows == 3 and M.cols == 3

    def test_hankel_structure(self):
        """Surface moment matrix is Hankel: M[i,j] depends on i+j only."""
        mp.dps = 50
        M = surface_moment_matrix([1], mpf(3), 4)
        for i in range(4):
            for j in range(4):
                for i2 in range(4):
                    for j2 in range(4):
                        if i + j == i2 + j2:
                            assert approx_eq(M[i, j], M[i2, j2], tol=mpf('1e-25'))

    def test_symmetry(self):
        """Surface moment matrix is symmetric."""
        mp.dps = 50
        M = surface_moment_matrix([2], mpf(3), 3)
        for i in range(3):
            for j in range(3):
                assert approx_eq(M[i, j], M[j, i])


# ═══════════════════════════════════════════════════════════════
# Leading minors
# ═══════════════════════════════════════════════════════════════

class TestLeadingMinors:
    def test_1x1(self):
        """Leading 1x1 minor is the (0,0) entry."""
        from mpmath import matrix as mpmatrix
        M = mpmatrix([[mpf(5), mpf(2)], [mpf(2), mpf(3)]])
        minors = leading_minors(M)
        assert approx_eq(minors[0], mpf(5))

    def test_2x2(self):
        """Leading 2x2 minor is the determinant."""
        from mpmath import matrix as mpmatrix
        M = mpmatrix([[mpf(5), mpf(2)], [mpf(2), mpf(3)]])
        minors = leading_minors(M)
        assert approx_eq(minors[1], mpf(5 * 3 - 2 * 2))  # 11

    def test_positive_definite_all_positive(self):
        """A positive definite matrix should have all positive leading minors."""
        from mpmath import matrix as mpmatrix
        # Identity matrix is positive definite
        I = mpmatrix([[mpf(1), mpf(0)], [mpf(0), mpf(1)]])
        minors = leading_minors(I)
        for m in minors:
            assert m > 0


# ═══════════════════════════════════════════════════════════════
# First zeta zero
# ═══════════════════════════════════════════════════════════════

class TestZetaZero:
    def test_first_zero_real_part(self):
        """Re(rho_1) = 1/2 (on the critical line)."""
        mp.dps = 50
        rho1 = first_zeta_zero()
        from mpmath import re as mpre
        assert approx_eq(mpre(rho1), mpf('0.5'), tol=mpf('1e-30'))

    def test_first_zero_imaginary_part(self):
        """Im(rho_1) ~ 14.134725..."""
        mp.dps = 50
        rho1 = first_zeta_zero()
        from mpmath import im as mpim
        assert fabs(mpim(rho1) - mpf('14.134725')) < mpf('0.001')

    def test_nth_zeros_increasing(self):
        """Successive zeta zeros have increasing imaginary part."""
        mp.dps = 30
        for n in range(1, 5):
            rho_n = nth_zeta_zero(n)
            rho_n1 = nth_zeta_zero(n + 1)
            from mpmath import im as mpim
            assert mpim(rho_n1) > mpim(rho_n)


# ═══════════════════════════════════════════════════════════════
# W_3 quartic resonance
# ═══════════════════════════════════════════════════════════════

class TestW3QuarticResonance:
    def test_w3_resonance_divisor_formula(self):
        """Q_3^ct = 220/[c*(5c+22)^2]."""
        for c_val in [1, 2, 5, 10]:
            c = mpf(c_val)
            Q3 = w3_quartic_resonance_divisor(c_val)
            expected = mpf(220) / (c * (5 * c + 22)**2)
            assert approx_eq(Q3, expected)

    def test_w3_spin3_mu4_decomposition(self):
        """mu_4 = H_3^2 + Q_3^ct on spin-3 slice."""
        for c_val in [1, 2, 5, 10]:
            c = mpf(c_val)
            mu4 = w3_spin3_mu4(c_val)
            H3 = c / 3
            Q3 = w3_quartic_resonance_divisor(c_val)
            assert approx_eq(mu4, H3**2 + Q3, tol=mpf('1e-25'))


# ═══════════════════════════════════════════════════════════════
# Compatibility ratios
# ═══════════════════════════════════════════════════════════════

class TestCompatibilityRatios:
    def test_pot_gram_reciprocal(self):
        """C_4^pot and C_4^Gram are reciprocals (when m3_sharp factor is absorbed).

        C_4^pot = c(5c+22)/10 * S_4^res
        C_4^Gram = 10/[c(5c+22)] / S_4^res
        So C_4^pot * C_4^Gram = S_4^res / S_4^res = 1.
        """
        mp.dps = 50
        for c_val, s4 in [(10, 0.5), (26, 0.1), (1, 2.0)]:
            pot = compatibility_ratio_pot(c_val, 0, s4)
            gram = compatibility_ratio_gram(c_val, s4)
            assert approx_eq(pot * gram, mpf(1), tol=mpf('1e-25'))


# ═══════════════════════════════════════════════════════════════
# Full Virasoro package
# ═══════════════════════════════════════════════════════════════

class TestFullVirasiroPackage:
    def test_package_keys(self):
        """Package should contain all expected keys."""
        pkg = full_virasoro_package(10)
        expected_keys = {'c', 'kappa', 'H', 'C_cubic', 'Q_ct', 'mu4', 'D2', 'Sigma2',
                         'resonance_divisor'}
        assert expected_keys.issubset(set(pkg.keys()))

    def test_kappa_equals_h(self):
        """kappa = H = c/2."""
        pkg = full_virasoro_package(10)
        assert approx_eq(pkg['kappa'], pkg['H'])
        assert approx_eq(pkg['kappa'], mpf(5))

    def test_sigma2_equals_qct(self):
        """Sigma_2 = Q^ct (the key identity for Virasoro)."""
        for c_val in [1, 2, 5, 10, 26]:
            pkg = full_virasoro_package(c_val)
            assert approx_eq(pkg['Sigma2'], pkg['Q_ct'], tol=mpf('1e-25'))

    def test_internal_consistency(self):
        """All package entries should be internally consistent.

        H = c/2, C = 2, mu_4 = H^2 + C^2/H + Q^ct, D2 = 5/(5c+22).
        """
        for c_val in [1, 5, 10, 26]:
            pkg = full_virasoro_package(c_val)
            c = mpf(c_val)
            assert approx_eq(pkg['H'], c / 2)
            assert approx_eq(pkg['C_cubic'], mpf(2))
            assert approx_eq(pkg['Q_ct'], mpf(10) / (c * (5 * c + 22)))
            assert approx_eq(pkg['D2'], mpf(5) / (5 * c + 22))
            assert approx_eq(pkg['mu4'],
                             pkg['H']**2 + pkg['C_cubic']**2 / pkg['H'] + pkg['Q_ct'],
                             tol=mpf('1e-25'))


# ═══════════════════════════════════════════════════════════════
# Cross-family consistency checks (AP10 prevention)
# ═══════════════════════════════════════════════════════════════

class TestCrossFamilyConsistency:
    """Cross-family checks using structural relations, not hardcoded values."""

    def test_dirichlet_sewing_additivity(self):
        """S_A is additive in weight multisets (by linearity).

        S_{A1 cup A2}(u) = S_{A1}(u) + S_{A2}(u)
        since the sum over weights decomposes.
        """
        mp.dps = 50
        u = mpf(3)
        S_12 = dirichlet_sewing_lift([1, 2], u)
        S_1 = dirichlet_sewing_lift([1], u)
        S_2 = dirichlet_sewing_lift([2], u)
        assert approx_eq(S_12, S_1 + S_2, tol=mpf('1e-25'))

    def test_euler_koszul_defect_weight_average(self):
        """D_A is a weighted average of single-weight defects.

        D_A(u) = (1/r) * sum D_{w_i}(u) where D_{w_i}(u) = 1 - H_{w_i-1}(u)/zeta(u).
        """
        mp.dps = 50
        u = mpf(3)
        # W_3 weights {2, 3}
        D_w3 = euler_koszul_defect([2, 3], u)
        D_2_single = euler_koszul_defect([2], u)
        D_3_single = euler_koszul_defect([3], u)
        expected = (D_2_single + D_3_single) / 2
        assert approx_eq(D_w3, expected, tol=mpf('1e-25'))

    def test_virasoro_w2_equivalence(self):
        """Virasoro = W_2: all computations should agree."""
        mp.dps = 50
        u = mpf(3)
        S_vir = dirichlet_sewing_lift(virasoro_weights(), u)
        S_w2 = dirichlet_sewing_lift_wn(2, u)
        assert approx_eq(S_vir, S_w2, tol=mpf('1e-30'))

    def test_shadow_data_w3_vs_virasoro(self):
        """W_3 spin-2 channel = Virasoro shadow data (same T channel)."""
        for c_val in [1, 5, 26]:
            v = virasoro_shadow_data(c_val)
            w = w3_shadow_data(c_val)
            for i in range(3):
                assert approx_eq(v[i], w[i])
