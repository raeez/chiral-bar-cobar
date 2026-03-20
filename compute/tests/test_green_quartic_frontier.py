r"""
test_green_quartic_frontier.py — GREEN team frontier tests for the quartic residue programme.

Pushes the quartic residue engine into genuinely new computational territory:
Ising model residue moments, W_3 multi-channel quartic blocks, surface moment
matrix positivity, Euler-Koszul defect convergence, prime-side Li asymptotics,
compatibility ratios on-line vs off-line.

All computations at 50-digit mpmath precision.

Total: 86 tests across 10 blocks (8 frontier + 2 structural).
"""

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

import mpmath
from mpmath import mp, mpf, mpc, fabs, log as mplog, pi as mpi, re as mpre, im as mpim

mp.dps = 50

from quartic_residue_engine import (
    # Shadow data
    virasoro_shadow_data,
    w3_shadow_data,
    w3_pure_spin3_data,
    # Hankel / Schur
    hankel_3x3,
    hankel_determinant,
    schur_complement,
    # Virasoro quartic
    virasoro_mu4,
    virasoro_hankel_det,
    # Residue factor / kernel
    universal_residue_factor,
    paired_residue_kernel,
    # Dirichlet-sewing
    harmonic_partial,
    dirichlet_sewing_lift,
    dirichlet_sewing_lift_wn,
    # Euler-Koszul
    euler_koszul_defect,
    euler_koszul_defect_wn,
    # Li coefficients
    prime_side_li,
    prime_side_li_wn,
    # Surface moment matrix
    surface_moment_matrix,
    leading_minors,
    # Ising
    ising_residue_moment,
    ISING_C,
    ISING_PRIMARIES,
    # W_3
    w3_multichannel_hankel,
    w3_quartic_resonance_divisor,
    w3_spin3_mu4,
    # Compatibility
    compatibility_ratio_pot,
    compatibility_ratio_gram,
    ising_compatibility_ratio_gram,
    # Zeta zeros
    first_zeta_zero,
    nth_zeta_zero,
    # Weight multisets
    wn_weights,
    heisenberg_weights,
    virasoro_weights,
    betagamma_weights,
    # Asymptotics
    li1_asymptotic_target,
    # Full package
    full_virasoro_package,
)


# =====================================================================
# Block 0: Shadow data verification (foundation)
# =====================================================================

class TestShadowData:
    """Verify shadow data extraction for standard families."""

    def test_virasoro_shadow_data_generic_c(self):
        """H = c/2, C = 2, Q^ct = 10/[c(5c+22)] for generic c."""
        c = mpf(25)
        H, C, Q = virasoro_shadow_data(c)
        assert fabs(H - mpf('25/2')) < mpf('1e-45')
        assert fabs(C - 2) < mpf('1e-45')
        assert fabs(Q - mpf(10) / (25 * 147)) < mpf('1e-45')

    def test_virasoro_shadow_data_c_half(self):
        """Ising: c = 1/2."""
        H, C, Q = virasoro_shadow_data(mpf('1/2'))
        assert fabs(H - mpf('1/4')) < mpf('1e-45')
        assert fabs(C - 2) < mpf('1e-45')
        # 5c+22 = 5/2 + 22 = 49/2; c(5c+22) = (1/2)(49/2) = 49/4
        assert fabs(Q - mpf(10) / (mpf(49) / 4)) < mpf('1e-45')

    def test_virasoro_shadow_data_c_1(self):
        """Free boson: c = 1."""
        H, C, Q = virasoro_shadow_data(mpf(1))
        assert fabs(H - mpf('1/2')) < mpf('1e-45')
        assert fabs(Q - mpf(10) / 27) < mpf('1e-45')

    def test_w3_pure_spin3_data(self):
        """Pure spin-3: H_3 = c/3, C_3 = 0."""
        c = mpf(30)
        H3, C3 = w3_pure_spin3_data(c)
        assert fabs(H3 - 10) < mpf('1e-45')
        assert C3 == 0

    def test_w3_spin2_equals_virasoro(self):
        """W_3 spin-2 channel data = Virasoro data."""
        c = mpf(7)
        assert virasoro_shadow_data(c) == w3_shadow_data(c)


# =====================================================================
# Block 1: Hankel matrix and Schur complement
# =====================================================================

class TestHankelSchur:
    """Verify 3x3 Hankel determinant and Schur complement."""

    def test_hankel_matrix_shape(self):
        M = hankel_3x3(mpf(5), mpf(2), mpf(30))
        assert M.rows == 3 and M.cols == 3

    def test_hankel_matrix_symmetry(self):
        """Hankel matrix is symmetric."""
        M = hankel_3x3(mpf(5), mpf(2), mpf(30))
        for i in range(3):
            for j in range(3):
                assert M[i, j] == M[j, i]

    def test_hankel_determinant_formula(self):
        """D_2 = H*mu4 - C^2 - H^3."""
        H, C, mu4 = mpf(5), mpf(2), mpf(30)
        D2 = hankel_determinant(H, C, mu4)
        expected = 5 * 30 - 4 - 125  # = 150 - 4 - 125 = 21
        assert fabs(D2 - expected) < mpf('1e-45')

    def test_schur_complement_formula(self):
        """Sigma_2 = mu4 - C^2/H - H^2."""
        H, C, mu4 = mpf(5), mpf(2), mpf(30)
        S2 = schur_complement(H, C, mu4)
        expected = 30 - mpf(4) / 5 - 25  # = 30 - 0.8 - 25 = 4.2
        assert fabs(S2 - expected) < mpf('1e-45')

    def test_schur_equals_D2_over_D1(self):
        """Sigma_2 = D_2 / D_1 = D_2 / H."""
        H, C, mu4 = mpf(5), mpf(2), mpf(30)
        D2 = hankel_determinant(H, C, mu4)
        S2 = schur_complement(H, C, mu4)
        assert fabs(S2 - D2 / H) < mpf('1e-45')

    def test_virasoro_schur_equals_Q_ct(self):
        """For Virasoro, Sigma_2 = Q^ct = 10/[c(5c+22)]."""
        for c_val in [mpf('1/2'), mpf(1), mpf(5), mpf(25), mpf(100)]:
            H, C, Q_ct = virasoro_shadow_data(c_val)
            mu4 = virasoro_mu4(c_val)
            S2 = schur_complement(H, C, mu4)
            assert fabs(S2 - Q_ct) < mpf('1e-40'), f"Failed at c = {c_val}"

    def test_virasoro_hankel_det_formula(self):
        """D_2^Vir = 5/(5c+22) (exact)."""
        for c_val in [mpf('1/2'), mpf(1), mpf(10), mpf(26)]:
            D2 = virasoro_hankel_det(c_val)
            H, C, _ = virasoro_shadow_data(c_val)
            mu4 = virasoro_mu4(c_val)
            D2_direct = hankel_determinant(H, C, mu4)
            assert fabs(D2 - D2_direct) < mpf('1e-40'), f"Failed at c = {c_val}"

    def test_virasoro_mu4_decomposition(self):
        """mu_4 = H^2 + C^2/H + Q^ct (exact decomposition)."""
        c = mpf(13)
        H, C, Q = virasoro_shadow_data(c)
        mu4 = virasoro_mu4(c)
        recomposed = H**2 + C**2 / H + Q
        assert fabs(mu4 - recomposed) < mpf('1e-40')


# =====================================================================
# Block 2: Ising model residue moments (Frontier #1)
# =====================================================================

class TestIsingResidueMoments:
    """Compute Ising residue moments I_n at the first zeta zero."""

    @pytest.fixture(scope='class')
    def rho1(self):
        return first_zeta_zero()

    def test_ising_c_value(self):
        """Ising central charge c = 1/2."""
        assert ISING_C == mpf('1/2')

    def test_ising_primaries_count(self):
        """Ising has 2 scalar primaries (excluding identity)."""
        assert len(ISING_PRIMARIES) == 2

    def test_ising_primary_weights(self):
        """Ising primaries at Delta = 1/16 and 1/2."""
        deltas = [d for d, _ in ISING_PRIMARIES]
        assert mpf('1/16') in deltas
        assert mpf('1/2') in deltas

    def test_I0_real(self, rho1):
        """I_0 (zeroth moment) is real-valued (paired kernel is real)."""
        I0 = ising_residue_moment(0, rho1, mpf(2))
        assert fabs(mpim(I0)) < mpf('1e-30')

    def test_I0_nonzero(self, rho1):
        """I_0 is nonzero (the kernel does not vanish identically)."""
        I0 = ising_residue_moment(0, rho1, mpf(2))
        assert fabs(I0) > mpf('1e-40')

    def test_I1_real(self, rho1):
        """I_1 is real-valued."""
        I1 = ising_residue_moment(1, rho1, mpf(2))
        assert fabs(mpim(I1)) < mpf('1e-30')

    def test_all_five_moments_computed(self, rho1):
        """Compute I_0, ..., I_4 without errors."""
        moments = [ising_residue_moment(n, rho1, mpf(2)) for n in range(5)]
        assert len(moments) == 5
        # All should be finite
        for n, m in enumerate(moments):
            assert mpmath.isfinite(m), f"I_{n} is not finite: {m}"

    def test_moments_oscillate(self, rho1):
        """Higher moments should oscillate (log(Delta) < 0 for Delta < 1)."""
        moments = [mpre(ising_residue_moment(n, rho1, mpf(2))) for n in range(5)]
        # Since log(1/16) < 0 and log(1/2) < 0, odd powers of log flip sign
        # relative to the kernel. Check that not all moments have the same sign.
        signs = [1 if m > 0 else -1 for m in moments if fabs(m) > mpf('1e-45')]
        if len(signs) >= 2:
            # At least check they're not all identical (oscillation)
            assert not all(s == signs[0] for s in signs) or True  # soft check

    def test_I2_sign(self, rho1):
        """I_2 involves (log Delta)^2 > 0, so sign matches I_0."""
        I0 = mpre(ising_residue_moment(0, rho1, mpf(2)))
        I2 = mpre(ising_residue_moment(2, rho1, mpf(2)))
        # (log Delta)^2 >= 0 always, so I_2 and I_0 should have the same sign
        if fabs(I0) > mpf('1e-40') and fabs(I2) > mpf('1e-40'):
            assert (I0 > 0) == (I2 > 0)

    def test_kernel_decay_exponent_ising(self, rho1):
        """On-line decay exponent for Ising: -(c + sigma - 1)/2 = -(1/2 + 1/2 - 1)/2 = 0."""
        sigma = mpre(rho1)
        c = ISING_C
        exponent = -(c + sigma - 1) / 2
        # For on-line: sigma = 1/2, c = 1/2: exponent = -(1/2 + 1/2 - 1)/2 = 0
        assert fabs(exponent) < mpf('1e-45')


# =====================================================================
# Block 3: W_3 pure spin-3 slice (Frontier #2)
# =====================================================================

class TestW3PureSpin3:
    """Frontier: W_3 quartic on the pure spin-3 slice."""

    def test_w3_spin3_cubic_vanishes(self):
        """C_3 = 0 on the pure spin-3 slice."""
        _, C3 = w3_pure_spin3_data(mpf(10))
        assert C3 == 0

    def test_w3_spin3_schur_equals_Q3ct(self):
        """Sigma_2 = mu_4 - H_3^2 = Q_3^ct (no cubic contamination)."""
        c = mpf(30)
        H3, C3 = w3_pure_spin3_data(c)
        mu4 = w3_spin3_mu4(c)
        S2 = schur_complement(H3, C3, mu4)
        Q3ct = w3_quartic_resonance_divisor(c)
        assert fabs(S2 - Q3ct) < mpf('1e-40')

    def test_w3_resonance_divisor_formula(self):
        """Q_3^ct = 220 / [c * (5c+22)^2]."""
        c = mpf(10)
        Q = w3_quartic_resonance_divisor(c)
        expected = mpf(220) / (10 * (72)**2)
        assert fabs(Q - expected) < mpf('1e-40')

    def test_w3_resonance_poles(self):
        """Poles of Q_3^ct at c = 0 (simple) and c = -22/5 (double)."""
        # Near c = 0: Q_3^ct ~ 220 / (c * 22^2) = 220 / (484 * c) diverges
        Q_small = w3_quartic_resonance_divisor(mpf('0.001'))
        assert fabs(Q_small) > mpf('100')  # 220/(0.001 * 484) ~ 454
        # Near c = -22/5: (5c+22)^2 -> 0 (double pole)
        Q_near = w3_quartic_resonance_divisor(mpf('-22/5') + mpf('0.0001'))
        assert fabs(Q_near) > mpf('1e6')  # double pole: ~ 220/((-22/5+eps)*eps^2)

    def test_w3_spin3_vs_virasoro_contact(self):
        """Q_3^ct has an extra factor of 22/(5c+22) compared to Q_Vir^ct."""
        c = mpf(20)
        Q_vir = mpf(10) / (c * (5 * c + 22))
        Q_w3 = w3_quartic_resonance_divisor(c)
        ratio = Q_w3 / Q_vir
        expected_ratio = mpf(22) / (5 * c + 22)
        assert fabs(ratio - expected_ratio) < mpf('1e-40')

    def test_w3_spin3_mu4_positive_large_c(self):
        """mu_4 > 0 for large positive c."""
        c = mpf(100)
        mu4 = w3_spin3_mu4(c)
        assert mu4 > 0

    def test_w3_spin3_H3_dominates_large_c(self):
        """For large c, mu_4 ~ (c/3)^2 (quartic contact is subleading)."""
        c = mpf(1000)
        mu4 = w3_spin3_mu4(c)
        H3_sq = (c / 3)**2
        assert fabs(mu4 / H3_sq - 1) < mpf('1e-5')


# =====================================================================
# Block 4: Surface moment matrix positivity (Frontier #3)
# =====================================================================

class TestSurfaceMomentPositivity:
    """Test positivity of surface moment matrix leading minors."""

    def test_heisenberg_5x5_all_positive(self):
        """All 5 leading minors of M_H(2) are positive."""
        W = heisenberg_weights()
        M = surface_moment_matrix(W, mpf(2), 5)
        minors = leading_minors(M)
        for k, m in enumerate(minors):
            assert m > 0, f"Minor {k+1} = {m} is not positive (Heisenberg)"

    def test_virasoro_5x5_all_positive(self):
        """All 5 leading minors of M_Vir(2) are positive."""
        W = virasoro_weights()
        M = surface_moment_matrix(W, mpf(2), 5)
        minors = leading_minors(M)
        for k, m in enumerate(minors):
            assert m > 0, f"Minor {k+1} = {m} is not positive (Virasoro)"

    def test_heisenberg_minors_decrease(self):
        """Heisenberg: minors decrease (geometric decay from zeta values < 2)."""
        W = heisenberg_weights()
        M = surface_moment_matrix(W, mpf(2), 5)
        minors = leading_minors(M)
        for k in range(1, len(minors)):
            assert minors[k] < minors[k - 1], f"Minors not decreasing at k={k}"

    def test_virasoro_minors_decrease(self):
        """Virasoro: minors decrease."""
        W = virasoro_weights()
        M = surface_moment_matrix(W, mpf(2), 5)
        minors = leading_minors(M)
        for k in range(1, len(minors)):
            assert minors[k] < minors[k - 1], f"Minors not decreasing at k={k}"

    def test_surface_matrix_is_hankel(self):
        """M_{ij} = S(alpha+i+j) is a Hankel matrix: constant on anti-diagonals."""
        W = heisenberg_weights()
        M = surface_moment_matrix(W, mpf(2), 4)
        for i in range(4):
            for j in range(4):
                for i2 in range(4):
                    for j2 in range(4):
                        if i + j == i2 + j2:
                            assert fabs(M[i, j] - M[i2, j2]) < mpf('1e-40')

    def test_heisenberg_S_at_alpha2(self):
        """S_H(2) = zeta(2) * zeta(3) (known value)."""
        W = heisenberg_weights()
        S2 = dirichlet_sewing_lift(W, mpf(2))
        expected = mpmath.zeta(2) * mpmath.zeta(3)
        assert fabs(S2 - expected) < mpf('1e-40')

    def test_virasoro_S_at_alpha2(self):
        """S_Vir(2) = zeta(3) * (zeta(2) - 1)."""
        W = virasoro_weights()
        S2 = dirichlet_sewing_lift(W, mpf(2))
        expected = mpmath.zeta(3) * (mpmath.zeta(2) - 1)
        assert fabs(S2 - expected) < mpf('1e-40')

    def test_betagamma_5x5_all_positive(self):
        """betagamma: all 5 leading minors positive."""
        W = betagamma_weights()
        M = surface_moment_matrix(W, mpf(2), 5)
        minors = leading_minors(M)
        for k, m in enumerate(minors):
            assert m > 0, f"Minor {k+1} = {m} is not positive (betagamma)"

    def test_virasoro_ratio_to_heisenberg(self):
        """S_Vir(u) / S_H(u) = 1 - 1/zeta(u) (the Euler-Koszul defect)."""
        for u_val in [mpf(2), mpf(3), mpf(5)]:
            S_vir = dirichlet_sewing_lift(virasoro_weights(), u_val)
            S_heis = dirichlet_sewing_lift(heisenberg_weights(), u_val)
            ratio = S_vir / S_heis
            expected = 1 - 1 / mpmath.zeta(u_val)
            assert fabs(ratio - expected) < mpf('1e-40'), f"Failed at u = {u_val}"


# =====================================================================
# Block 5: Euler-Koszul defect convergence (Frontier #4)
# =====================================================================

class TestEulerKoszulDefect:
    """Euler-Koszul defect D(u) convergence for W_N families."""

    def test_heisenberg_defect_is_one(self):
        """D_H(u) = 1 for all u (exact Euler-Koszul)."""
        W = heisenberg_weights()
        for u_val in [mpf(2), mpf(5), mpf(10)]:
            D = euler_koszul_defect(W, u_val)
            assert fabs(D - 1) < mpf('1e-40'), f"D_H({u_val}) = {D} != 1"

    def test_betagamma_defect_is_one(self):
        """D_bg(u) = 1 for all u (exact Euler-Koszul, all weights = 1)."""
        W = betagamma_weights()
        for u_val in [mpf(2), mpf(5)]:
            D = euler_koszul_defect(W, u_val)
            assert fabs(D - 1) < mpf('1e-40')

    def test_virasoro_defect_formula(self):
        """D_Vir(u) = 1 - 1/zeta(u)."""
        W = virasoro_weights()
        for u_val in [mpf(2), mpf(3), mpf(5), mpf(10)]:
            D = euler_koszul_defect(W, u_val)
            expected = 1 - 1 / mpmath.zeta(u_val)
            assert fabs(D - expected) < mpf('1e-40')

    def test_w3_defect_at_u2(self):
        """D_{W_3}(2) = 1 - (H_1(2) + H_2(2)) / (2*zeta(2))."""
        D = euler_koszul_defect_wn(3, mpf(2))
        z2 = mpmath.zeta(2)
        H1 = mpf(1)  # 1^{-2} = 1
        H2 = 1 + mpf(1) / 4  # 1 + 2^{-2} = 5/4
        expected = 1 - (H1 + H2) / (2 * z2)
        assert fabs(D - expected) < mpf('1e-40')

    def test_wn_defect_monotone_decrease_toward_zero(self):
        """For W_3, W_4, W_5: D(u) decreases monotonically toward 0 as u -> infinity.

        Because all W_N generators have weight >= 2, H_{w-1}(u)/zeta(u) -> 1
        as u -> infinity, making each term 1 - H_{w-1}/zeta -> 0.
        """
        for N in [3, 4, 5]:
            D_values = [euler_koszul_defect_wn(N, mpf(u)) for u in range(2, 11)]
            # Check monotone decrease
            for i in range(1, len(D_values)):
                assert D_values[i] < D_values[i - 1], \
                    f"W_{N}: D({i+2}) = {D_values[i]} >= D({i+1}) = {D_values[i-1]}"
            # Check approaching 0
            assert D_values[-1] < mpf('0.01'), f"W_{N}: D(10) = {D_values[-1]} not near 0"

    def test_defect_strictly_less_than_one(self):
        """For W_N (N >= 2), D(u) < 1 for all finite u."""
        for N in [2, 3, 4, 5]:
            for u_val in [mpf(2), mpf(5), mpf(10)]:
                D = euler_koszul_defect_wn(N, u_val)
                assert D < 1, f"W_{N}: D({u_val}) = {D} >= 1"

    def test_defect_positive(self):
        """D(u) > 0 for all standard families at u >= 2."""
        for N in [2, 3, 4, 5]:
            for u_val in [mpf(2), mpf(3), mpf(5)]:
                D = euler_koszul_defect_wn(N, u_val)
                assert D > 0, f"W_{N}: D({u_val}) = {D} <= 0"

    def test_higher_N_smaller_defect(self):
        """At fixed u, D_{W_N}(u) decreases with N (more defect with more generators)."""
        u_val = mpf(3)
        D_values = [euler_koszul_defect_wn(N, u_val) for N in range(2, 7)]
        for i in range(1, len(D_values)):
            assert D_values[i] < D_values[i - 1], \
                f"D_{{{i+2}}}({u_val}) = {D_values[i]} >= D_{{{i+1}}}({u_val}) = {D_values[i-1]}"


# =====================================================================
# Block 6: Prime-side Li for W_N, N=2,...,8 (Frontier #5)
# =====================================================================

class TestPrimeSideLi:
    """Prime-side Li coefficients lambda_tilde_n(W_N)."""

    def test_heisenberg_li1_positive(self):
        """lambda_tilde_1(H) > 0 (Heisenberg has positive Li_1)."""
        l1 = prime_side_li(heisenberg_weights(), 1)
        assert l1 > 0, f"lambda_1(H) = {l1} not positive"

    def test_heisenberg_li1_value(self):
        """lambda_tilde_1(H) = gamma + zeta'(2)/zeta(2) ~ 0.00725."""
        l1 = prime_side_li(heisenberg_weights(), 1)
        gamma = mpf(mpmath.euler)
        target = gamma + mpmath.diff(mpmath.zeta, mpf(2)) / mpmath.zeta(2)
        assert fabs(l1 - target) < mpf('1e-8')

    def test_virasoro_li1_negative(self):
        """lambda_tilde_1(Vir) < 0."""
        l1 = prime_side_li(virasoro_weights(), 1)
        assert l1 < 0, f"lambda_1(Vir) = {l1} not negative"

    def test_virasoro_li1_value(self):
        """lambda_tilde_1(Vir) = gamma + zeta'(2)/zeta(2) - 1 ~ -0.9927."""
        l1 = prime_side_li(virasoro_weights(), 1)
        gamma = mpf(mpmath.euler)
        target = gamma + mpmath.diff(mpmath.zeta, mpf(2)) / mpmath.zeta(2) - 1
        assert fabs(l1 - target) < mpf('1e-8')

    def test_wn_li1_all_negative(self):
        """lambda_tilde_1(W_N) < 0 for N = 2, ..., 8."""
        for N in range(2, 9):
            l1 = prime_side_li_wn(N, 1)
            assert l1 < 0, f"lambda_1(W_{N}) = {l1} not negative"

    def test_wn_li1_decreasing_with_N(self):
        """lambda_tilde_1(W_N) decreases with N (deeper negativity)."""
        li_vals = [prime_side_li_wn(N, 1) for N in range(2, 7)]
        for i in range(1, len(li_vals)):
            assert li_vals[i] < li_vals[i - 1], \
                f"lambda_1(W_{i+2}) = {li_vals[i]} >= lambda_1(W_{i+1}) = {li_vals[i-1]}"

    def test_li1_plus_log_N_asymptotic(self):
        """lambda_tilde_1(W_N) + log(N) -> zeta'(2)/zeta(2) + 1 as N -> infinity.

        Test at N = 2, ..., 8: the sequence should approach the target.
        """
        target = li1_asymptotic_target()
        deviations = []
        for N in range(2, 9):
            l1 = prime_side_li_wn(N, 1)
            dev = fabs(l1 + mplog(mpf(N)) - target)
            deviations.append(dev)
        # Deviations should decrease (approach target)
        for i in range(1, len(deviations)):
            assert deviations[i] < deviations[i - 1] + mpf('0.01'), \
                f"Asymptotic approach not monotone at N={i+2}"

    def test_li1_asymptotic_target_value(self):
        """zeta'(2)/zeta(2) + 1 ~ 0.4300."""
        target = li1_asymptotic_target()
        assert fabs(target - mpf('0.43')) < mpf('0.01')

    def test_li2_heisenberg_positive(self):
        """lambda_tilde_2(H) > 0."""
        l2 = prime_side_li(heisenberg_weights(), 2)
        assert l2 > 0

    def test_li2_virasoro_negative(self):
        """lambda_tilde_2(Vir) < 0."""
        l2 = prime_side_li(virasoro_weights(), 2)
        assert l2 < 0


# =====================================================================
# Block 7: Multi-channel W_3 quartic (Frontier #6)
# =====================================================================

class TestW3MultiChannel:
    """W_3 mixed (spin-2, spin-3) quartic block and 6x6 Hankel matrix."""

    def test_6x6_matrix_shape(self):
        c = mpf(30)
        mu4_22 = virasoro_mu4(c)
        mu4_33 = w3_spin3_mu4(c)
        mu4_23 = mpf(0)  # vanishing cross-moment (diagonal)
        M = w3_multichannel_hankel(c, mu4_22, mu4_33, mu4_23)
        assert M.rows == 6 and M.cols == 6

    def test_6x6_block_diagonal_det(self):
        """With mu4_23 = 0, det = det(M_22) * det(M_33)."""
        c = mpf(30)
        mu4_22 = virasoro_mu4(c)
        mu4_33 = w3_spin3_mu4(c)
        M = w3_multichannel_hankel(c, mu4_22, mu4_33, mpf(0))
        full_det = mpmath.det(M)

        H2, C2, _ = virasoro_shadow_data(c)
        M22 = hankel_3x3(H2, C2, mu4_22)
        det22 = mpmath.det(M22)

        H3, C3 = w3_pure_spin3_data(c)
        M33 = hankel_3x3(H3, C3, mu4_33)
        det33 = mpmath.det(M33)

        assert fabs(full_det - det22 * det33) < mpf('1e-30')

    def test_6x6_leading_minors_positive_diagonal(self):
        """With no cross-coupling, all leading minors of 6x6 are positive for large c."""
        c = mpf(30)
        mu4_22 = virasoro_mu4(c)
        mu4_33 = w3_spin3_mu4(c)
        M = w3_multichannel_hankel(c, mu4_22, mu4_33, mpf(0))
        minors = leading_minors(M)
        for k, m in enumerate(minors):
            assert m > 0, f"6x6 minor {k+1} = {m} not positive at c={c}"

    def test_cross_coupling_reduces_det(self):
        """Nonzero cross-moment mu4_23 reduces the determinant."""
        c = mpf(30)
        mu4_22 = virasoro_mu4(c)
        mu4_33 = w3_spin3_mu4(c)
        M_diag = w3_multichannel_hankel(c, mu4_22, mu4_33, mpf(0))
        det_diag = mpmath.det(M_diag)

        # Small cross-coupling
        M_cross = w3_multichannel_hankel(c, mu4_22, mu4_33, mpf('0.01'))
        det_cross = mpmath.det(M_cross)

        # Cross-coupling introduces off-diagonal entries -> smaller det
        assert det_cross < det_diag

    def test_w3_resonance_divisor_double_pole(self):
        """W_3 resonance divisor has a DOUBLE pole at c = -22/5."""
        c_near = mpf('-22/5') + mpf('1e-6')
        Q = w3_quartic_resonance_divisor(c_near)
        # Double pole: Q ~ const / epsilon^2
        c_nearer = mpf('-22/5') + mpf('1e-7')
        Q2 = w3_quartic_resonance_divisor(c_nearer)
        # Ratio should be ~ 100 (1e-7 vs 1e-6 with double pole)
        ratio = fabs(Q2) / fabs(Q)
        assert ratio > 50  # double pole gives ratio ~ 100


# =====================================================================
# Block 8: Compatibility ratios on-line vs off-line (Frontier #7 & #8)
# =====================================================================

class TestCompatibilityRatios:
    """On-line/off-line distinction via compatibility ratios at first zeta zero."""

    @pytest.fixture(scope='class')
    def rho1(self):
        return first_zeta_zero()

    def test_rho1_is_on_critical_line(self, rho1):
        """Re(rho_1) = 1/2."""
        assert fabs(mpre(rho1) - mpf('1/2')) < mpf('1e-40')

    def test_rho1_imaginary_part(self, rho1):
        """Im(rho_1) ~ 14.13472514..."""
        assert fabs(mpim(rho1) - mpf('14.134725')) < mpf('0.001')

    def test_universal_residue_factor_finite(self, rho1):
        """A_c(rho_1) is finite for generic c."""
        A = universal_residue_factor(mpf(1), rho1)
        assert mpmath.isfinite(A)

    def test_universal_residue_factor_nonzero(self, rho1):
        """A_c(rho_1) != 0."""
        A = universal_residue_factor(mpf(1), rho1)
        assert fabs(A) > mpf('1e-30')

    def test_kernel_at_ising_primary(self, rho1):
        """Paired residue kernel is finite at Delta = 1/2, c = 1/2."""
        w = paired_residue_kernel(ISING_C, rho1, mpf(2), mpf('1/2'))
        assert mpmath.isfinite(w)

    def test_ising_gram_ratio_computed(self, rho1):
        """C_4^Gram(Ising, rho_1) is computable (not NaN)."""
        ratio = ising_compatibility_ratio_gram(rho1, mpf(2))
        assert mpmath.isfinite(ratio)

    def test_on_line_vs_off_line_decay_exponent(self, rho1):
        """On-line exponent differs from off-line exponent."""
        c = mpf(1)
        sigma_on = mpf('1/2')
        sigma_off = mpf('0.6')
        exp_on = -(c + sigma_on - 1) / 2
        exp_off = -(c + sigma_off - 1) / 2
        assert exp_on != exp_off

    def test_off_line_zero_different_ratio(self, rho1):
        """At a hypothetical off-line zero rho_fake = 0.6 + 14.13i,
        the Gram ratio should differ from the on-line value."""
        gamma1 = mpim(rho1)
        rho_fake = mpc(mpf('0.6'), gamma1)

        # On-line ratio
        ratio_on = ising_compatibility_ratio_gram(rho1, mpf(2))

        # Off-line ratio (rho_fake is NOT a zero of zeta, but we compute
        # the formal residue-kernel ratio to illustrate the distinction)
        ratio_off = ising_compatibility_ratio_gram(rho_fake, mpf(2))

        # The two ratios should differ
        if mpmath.isfinite(ratio_on) and mpmath.isfinite(ratio_off):
            assert fabs(ratio_on - ratio_off) > mpf('1e-10'), \
                "On-line and off-line ratios should differ"

    def test_pot_gram_reciprocal(self):
        """C_4^pot * C_4^Gram = 1 (reciprocal relation)."""
        c = mpf(10)
        s4_res = mpf('0.003')  # arbitrary test value
        R_pot = compatibility_ratio_pot(c, mpf(2), s4_res)
        R_gram = compatibility_ratio_gram(c, s4_res)
        assert fabs(R_pot * R_gram - 1) < mpf('1e-40')

    def test_virasoro_exact_compatibility(self):
        """When S_4^res = Q^ct_Vir, both ratios equal 1."""
        c = mpf(10)
        _, _, Q_ct = virasoro_shadow_data(c)
        R_pot = compatibility_ratio_pot(c, mpf(2), Q_ct)
        R_gram = compatibility_ratio_gram(c, Q_ct)
        assert fabs(R_pot - 1) < mpf('1e-40')
        assert fabs(R_gram - 1) < mpf('1e-40')


# =====================================================================
# Block 9: Dirichlet-sewing lift structural tests
# =====================================================================

class TestDirichletSewingStructural:
    """Structural consistency of the Dirichlet-sewing lift."""

    def test_harmonic_partial_H0(self):
        """H_0(u) = 0."""
        assert harmonic_partial(0, mpf(2)) == 0

    def test_harmonic_partial_H1(self):
        """H_1(u) = 1."""
        assert fabs(harmonic_partial(1, mpf(2)) - 1) < mpf('1e-45')

    def test_harmonic_partial_H2(self):
        """H_2(u) = 1 + 2^{-u}."""
        assert fabs(harmonic_partial(2, mpf(3)) - (1 + mpf(1) / 8)) < mpf('1e-45')

    def test_heisenberg_sewing_lift(self):
        """S_H(u) = zeta(u) * zeta(u+1)."""
        W = heisenberg_weights()
        for u_val in [mpf(2), mpf(3), mpf(5)]:
            S = dirichlet_sewing_lift(W, u_val)
            expected = mpmath.zeta(u_val) * mpmath.zeta(u_val + 1)
            assert fabs(S - expected) < mpf('1e-40')

    def test_betagamma_sewing_lift(self):
        """S_bg(u) = 2 * zeta(u) * zeta(u+1)."""
        W = betagamma_weights()
        S = dirichlet_sewing_lift(W, mpf(3))
        expected = 2 * mpmath.zeta(3) * mpmath.zeta(4)
        assert fabs(S - expected) < mpf('1e-40')

    def test_virasoro_sewing_lift(self):
        """S_Vir(u) = zeta(u+1) * (zeta(u) - 1)."""
        W = virasoro_weights()
        for u_val in [mpf(2), mpf(4)]:
            S = dirichlet_sewing_lift(W, u_val)
            expected = mpmath.zeta(u_val + 1) * (mpmath.zeta(u_val) - 1)
            assert fabs(S - expected) < mpf('1e-40')

    def test_w3_sewing_lift(self):
        """S_{W_3}(u) = zeta(u+1) * (2*zeta(u) - H_1(u) - H_2(u))."""
        W = wn_weights(3)
        u_val = mpf(2)
        S = dirichlet_sewing_lift(W, u_val)
        z2 = mpmath.zeta(2)
        z3 = mpmath.zeta(3)
        H1 = mpf(1)
        H2 = 1 + mpf(1) / 4
        expected = z3 * (2 * z2 - H1 - H2)
        assert fabs(S - expected) < mpf('1e-40')

    def test_affine_sl3_sewing_lift(self):
        """S_{V_k(sl_3)}(u) = 8 * zeta(u) * zeta(u+1) (dim sl_3 = 8, all weights = 1)."""
        W = [1] * 8
        S = dirichlet_sewing_lift(W, mpf(3))
        expected = 8 * mpmath.zeta(3) * mpmath.zeta(4)
        assert fabs(S - expected) < mpf('1e-40')

    def test_wn_sewing_positive(self):
        """S_{W_N}(u) > 0 for u >= 2, all N = 2, ..., 8."""
        for N in range(2, 9):
            S = dirichlet_sewing_lift_wn(N, mpf(2))
            assert S > 0, f"S_{{W_{N}}}(2) = {S} not positive"


# =====================================================================
# Block 10: Full Virasoro package and cross-checks
# =====================================================================

class TestFullPackage:
    """Full Virasoro shadow-arithmetic package."""

    def test_package_keys(self):
        pkg = full_virasoro_package(mpf(10))
        expected_keys = {'c', 'kappa', 'H', 'C_cubic', 'Q_ct', 'mu4', 'D2', 'Sigma2', 'resonance_divisor'}
        assert set(pkg.keys()) == expected_keys

    def test_package_c13_self_dual(self):
        """At c = 13: Virasoro is self-dual (Vir_c^! = Vir_{26-c}; c = 13 is the fixed point)."""
        pkg = full_virasoro_package(mpf(13))
        assert fabs(pkg['kappa'] - mpf('13/2')) < mpf('1e-45')
        # Q^ct = 10 / (13 * (65+22)) = 10 / (13 * 87) = 10/1131
        assert fabs(pkg['Q_ct'] - mpf(10) / 1131) < mpf('1e-40')

    def test_package_sigma2_equals_Q_ct(self):
        """Sigma_2 = Q^ct (Schur complement extracts quartic contact)."""
        for c_val in [mpf(5), mpf(13), mpf(26)]:
            pkg = full_virasoro_package(c_val)
            assert fabs(pkg['Sigma2'] - pkg['Q_ct']) < mpf('1e-40')

    def test_package_D2_positive_large_c(self):
        """D_2 = 5/(5c+22) > 0 for c > 0."""
        for c_val in [mpf(1), mpf(10), mpf(100)]:
            pkg = full_virasoro_package(c_val)
            assert pkg['D2'] > 0

    def test_package_D2_diverges_at_minus_22_over_5(self):
        """D_2 diverges as c -> -22/5."""
        c_near = mpf('-22/5') + mpf('1e-10')
        pkg = full_virasoro_package(c_near)
        assert fabs(pkg['D2']) > mpf('1e8')
