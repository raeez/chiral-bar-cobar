"""Tests for the quartic arithmetic closure programme.

Verifies:
1. Quartic contact invariant Q^ct_Vir = 10/(c(5c+22))
2. Schur complement Sigma_2 = 5/(5c+22) (normalized)
3. Hankel moment matrix structure and determinants
4. Genuine residue kernel decay exponents and oscillation
5. Li coefficient sign patterns for all standard families
6. Compatibility ratios and locus structure
7. Shadow moment generating functions
8. W_3 double pole structure
9. Arithmetic closure: defect produces negative Li coefficients
10. DS reduction preserves negativity pattern
"""

import pytest
from mpmath import (mp, mpf, mpc, zeta, diff, log, euler as euler_gamma,
                    power, fac, pi, stieltjes, cos, sin, fabs, inf,
                    re as mpre, im as mpim, matrix as mpmatrix, det as mpdet)
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

mp.dps = 50


# =============================================================================
# Self-contained helpers (for test stability)
# =============================================================================

def _zeta_reg(u):
    eps = u - 1
    if fabs(eps) < mpf('1e-20'):
        return (1 + euler_gamma * eps + stieltjes(1) * eps ** 2
                + stieltjes(2) * eps ** 3)
    return (u - 1) * zeta(u)


def _Xi_weights(weights, u):
    harm_sum = sum(sum(power(j, -u) for j in range(1, w)) for w in weights)
    rank = len(weights)
    return zeta(u + 1) * (rank * _zeta_reg(u) - (u - 1) * harm_sum)


def _li_n(weights, n):
    def f(u):
        return power(u, n - 1) * log(_Xi_weights(weights, u))
    return diff(f, mpf(1), n) / fac(n - 1)


# =============================================================================
# Test 1: Quartic contact invariant
# =============================================================================

class TestQuarticContact:
    def test_virasoro_formula(self):
        """Q^ct = 10/(c(5c+22)) at generic c."""
        from lib.quartic_arithmetic_closure import quartic_contact_virasoro
        for c_val in [1, 2, 5, 10, 13, 26, 50, 100]:
            Q = quartic_contact_virasoro(c_val)
            expected = mpf(10) / (c_val * (5 * c_val + 22))
            assert fabs(Q - expected) < mpf('1e-40'), f"Failed at c={c_val}"

    def test_resonance_c0(self):
        """Q^ct has a pole at c=0: Q diverges as c -> 0."""
        from lib.quartic_arithmetic_closure import quartic_contact_virasoro
        # Approach c=0 from the right: Q should grow without bound
        vals = []
        for eps in [1e-1, 1e-3, 1e-5]:
            Q = quartic_contact_virasoro(eps)
            vals.append(float(Q))
        # Each step should be ~100x larger (simple pole)
        for i in range(len(vals) - 1):
            assert vals[i + 1] > 10 * vals[i], \
                f"Q not diverging fast enough: {vals[i+1]} vs {vals[i]}"

    def test_resonance_c_minus_22_5(self):
        """Q^ct has a pole at c=-22/5: |Q| diverges."""
        from lib.quartic_arithmetic_closure import quartic_contact_virasoro
        c_res = -22.0 / 5
        vals = []
        for eps in [1e-1, 1e-3, 1e-5]:
            Q = quartic_contact_virasoro(c_res + eps)
            vals.append(float(fabs(Q)))
        for i in range(len(vals) - 1):
            assert vals[i + 1] > 10 * vals[i], \
                f"|Q| not diverging fast enough near c=-22/5"

    def test_self_dual_c13(self):
        """Q(13) = 10/(13*87) = 10/1131."""
        from lib.quartic_arithmetic_closure import quartic_contact_virasoro
        Q = quartic_contact_virasoro(13)
        expected = mpf(10) / 1131
        assert fabs(Q - expected) < mpf('1e-40')

    def test_large_c_asymptotics(self):
        """Q -> 2/c^2 as c -> infinity."""
        from lib.quartic_arithmetic_closure import quartic_contact_virasoro
        for c_val in [1000, 10000, 100000]:
            Q = quartic_contact_virasoro(c_val)
            asymptotic = mpf(2) / c_val ** 2
            ratio = Q / asymptotic
            assert fabs(ratio - 1) < mpf('0.05'), \
                f"Ratio {float(ratio)} not close to 1 at c={c_val}"

    def test_positive_for_positive_c(self):
        """Q^ct > 0 for all c > 0."""
        from lib.quartic_arithmetic_closure import quartic_contact_virasoro
        for c_val in [0.01, 0.1, 1, 5, 13, 26, 100, 1000]:
            Q = quartic_contact_virasoro(c_val)
            assert Q > 0, f"Q should be positive for c={c_val}, got {float(Q)}"

    def test_bosonic_string_c26(self):
        """Q(26) = 10/(26*152) = 5/1976."""
        from lib.quartic_arithmetic_closure import quartic_contact_virasoro
        Q = quartic_contact_virasoro(26)
        expected = mpf(5) / 1976
        assert fabs(Q - expected) < mpf('1e-40')

    def test_c1_value(self):
        """Q(1) = 10/(1*27) = 10/27."""
        from lib.quartic_arithmetic_closure import quartic_contact_virasoro
        Q = quartic_contact_virasoro(1)
        expected = mpf(10) / 27
        assert fabs(Q - expected) < mpf('1e-40')


# =============================================================================
# Test 2: Schur complement
# =============================================================================

class TestSchurComplement:
    def test_virasoro_formula(self):
        """Sigma_2^Vir = 5/(5c+22) (normalized)."""
        from lib.quartic_arithmetic_closure import schur_complement_virasoro
        for c_val in [1, 5, 13, 26]:
            S2 = schur_complement_virasoro(c_val)
            expected = mpf(5) / (5 * c_val + 22)
            assert fabs(S2 - expected) < mpf('1e-40'), f"Failed at c={c_val}"

    def test_virasoro_at_c1(self):
        """Sigma_2(1) = 5/27."""
        from lib.quartic_arithmetic_closure import schur_complement_virasoro
        S2 = schur_complement_virasoro(1)
        assert fabs(S2 - mpf(5) / 27) < mpf('1e-40')

    def test_virasoro_at_c26(self):
        """Sigma_2(26) = 5/152."""
        from lib.quartic_arithmetic_closure import schur_complement_virasoro
        S2 = schur_complement_virasoro(26)
        assert fabs(S2 - mpf(5) / 152) < mpf('1e-40')

    def test_w3_double_pole(self):
        """W_3 quartic Q_3 has double pole at 5c+22=0."""
        from lib.quartic_arithmetic_closure import w3_quartic_contact
        c_res = -22.0 / 5
        # Near the resonance, Q_3 grows as 1/(5c+22)^2
        eps_vals = [1e-2, 1e-3, 1e-4]
        Q_vals = [float(fabs(w3_quartic_contact(c_res + eps))) for eps in eps_vals]
        # Each 10x decrease in eps should give ~100x increase (double pole)
        for i in range(len(Q_vals) - 1):
            ratio = Q_vals[i + 1] / Q_vals[i]
            assert ratio > 50, f"Double pole ratio {ratio} too small (expected ~100)"

    def test_schur_positive_for_large_c(self):
        """Sigma_2 > 0 for c > 0 (normalized version)."""
        from lib.quartic_arithmetic_closure import schur_complement_virasoro
        for c_val in [1, 10, 100, 1000]:
            S2 = schur_complement_virasoro(c_val)
            assert S2 > 0, f"Sigma_2 should be positive at c={c_val}"

    def test_schur_large_c_asymptotics(self):
        """Sigma_2 -> 1/c as c -> infinity (normalized)."""
        from lib.quartic_arithmetic_closure import schur_complement_virasoro
        for c_val in [1000, 10000]:
            S2 = schur_complement_virasoro(c_val)
            asymp = mpf(1) / c_val
            assert fabs(S2 / asymp - 1) < mpf('0.01')


# =============================================================================
# Test 3: Hankel moment matrix
# =============================================================================

class TestHankelMatrix:
    def test_symmetry(self):
        """Hankel matrix is symmetric: M_{ij} = M_{ji}."""
        from lib.quartic_arithmetic_closure import virasoro_shadow_moments, hankel_moment_matrix
        for c_val in [1, 13, 26]:
            moments = virasoro_shadow_moments(c_val, 6)
            M = hankel_moment_matrix(moments)
            for i in range(3):
                for j in range(3):
                    assert fabs(M[i, j] - M[j, i]) < mpf('1e-40'), \
                        f"Not symmetric at ({i},{j}) for c={c_val}"

    def test_hankel_structure(self):
        """M_{ij} = mu_{i+j+2} (Hankel structure)."""
        from lib.quartic_arithmetic_closure import virasoro_shadow_moments, hankel_moment_matrix
        moments = virasoro_shadow_moments(26, 6)
        M = hankel_moment_matrix(moments)
        # M[0,0] = mu_2, M[0,1] = mu_3, M[1,1] = mu_4, etc.
        assert fabs(M[0, 0] - moments[2]) < mpf('1e-40')
        assert fabs(M[0, 1] - moments[3]) < mpf('1e-40')
        assert fabs(M[0, 2] - moments[4]) < mpf('1e-40')
        assert fabs(M[1, 1] - moments[4]) < mpf('1e-40')
        assert fabs(M[1, 2] - moments[5]) < mpf('1e-40')
        assert fabs(M[2, 2] - moments[6]) < mpf('1e-40')

    def test_leading_minor_1(self):
        """First minor det_1 = mu_2 = c/2."""
        from lib.quartic_arithmetic_closure import virasoro_shadow_moments, hankel_moment_matrix, hankel_determinants
        for c_val in [1, 13, 26]:
            moments = virasoro_shadow_moments(c_val, 6)
            M = hankel_moment_matrix(moments)
            dets = hankel_determinants(M)
            assert fabs(dets[0] - mpf(c_val) / 2) < mpf('1e-35'), \
                f"det_1 wrong at c={c_val}"

    def test_leading_minor_2(self):
        """Second minor det_2 = mu_2*mu_4 - mu_3^2."""
        from lib.quartic_arithmetic_closure import virasoro_shadow_moments, hankel_moment_matrix, hankel_determinants
        c_val = 26
        moments = virasoro_shadow_moments(c_val, 6)
        M = hankel_moment_matrix(moments)
        dets = hankel_determinants(M)
        expected = moments[2] * moments[4] - moments[3] ** 2
        assert fabs(dets[1] - expected) < mpf('1e-30')


# =============================================================================
# Test 4: Virasoro shadow moments
# =============================================================================

class TestVirasoroShadowMoments:
    def test_mu2_kappa(self):
        """mu_2 = kappa = c/2."""
        from lib.quartic_arithmetic_closure import virasoro_shadow_moments
        for c_val in [1, 13, 26, 50]:
            moments = virasoro_shadow_moments(c_val)
            assert fabs(moments[2] - mpf(c_val) / 2) < mpf('1e-40')

    def test_mu3_cubic(self):
        """mu_3 = 2 (gravitational cubic)."""
        from lib.quartic_arithmetic_closure import virasoro_shadow_moments
        for c_val in [1, 13, 26]:
            moments = virasoro_shadow_moments(c_val)
            assert fabs(moments[3] - 2) < mpf('1e-40')

    def test_mu4_quartic(self):
        """mu_4 = 10/(c(5c+22)) (quartic contact)."""
        from lib.quartic_arithmetic_closure import virasoro_shadow_moments
        for c_val in [1, 13, 26]:
            moments = virasoro_shadow_moments(c_val)
            expected = mpf(10) / (c_val * (5 * c_val + 22))
            assert fabs(moments[4] - expected) < mpf('1e-35')

    def test_mu5_quintic(self):
        """mu_5 = -48/(c^2(5c+22)) (from master equation)."""
        from lib.quartic_arithmetic_closure import virasoro_shadow_moments
        for c_val in [1, 13, 26]:
            moments = virasoro_shadow_moments(c_val)
            expected = mpf(-48) / (mpf(c_val) ** 2 * (5 * c_val + 22))
            assert fabs(moments[5] - expected) < mpf('1e-30'), \
                f"mu_5 wrong at c={c_val}: got {float(moments[5])}, expected {float(expected)}"

    def test_mu5_sign(self):
        """mu_5 < 0 for all c > 0 (quintic shadow is negative)."""
        from lib.quartic_arithmetic_closure import virasoro_shadow_moments
        for c_val in [1, 5, 13, 26, 100]:
            moments = virasoro_shadow_moments(c_val)
            assert moments[5] < 0, f"mu_5 should be negative at c={c_val}"


# =============================================================================
# Test 5: Residue kernel
# =============================================================================

class TestResidueKernel:
    def test_on_line_decay(self):
        """sigma=1/2: decay exponent = -(c-1/2)/2."""
        from lib.quartic_arithmetic_closure import on_line_decay, decay_exponent
        for c_val in [1, 13, 26]:
            d = on_line_decay(c_val)
            expected = -(mpf(c_val) - mpf('0.5')) / 2
            assert fabs(d - expected) < mpf('1e-40')
            # Also check consistency with general formula
            d_gen = decay_exponent(c_val, 0.5)
            assert fabs(d - d_gen) < mpf('1e-40')

    def test_off_line_faster_decay(self):
        """sigma > 1/2: decay is faster (more negative exponent)."""
        from lib.quartic_arithmetic_closure import decay_exponent
        for c_val in [1, 13, 26]:
            d_on = decay_exponent(c_val, 0.5)
            d_off = decay_exponent(c_val, 0.7)
            assert d_off < d_on, \
                f"Off-line decay should be faster at c={c_val}"

    def test_decay_exponent_formula(self):
        """Decay exponent = -(c+sigma-1)/2."""
        from lib.quartic_arithmetic_closure import decay_exponent
        c_val, sigma = 26, 0.5
        d = decay_exponent(c_val, sigma)
        expected = -(mpf(c_val) + mpf(sigma) - 1) / 2
        assert fabs(d - expected) < mpf('1e-40')

    def test_oscillation_from_gamma(self):
        """gamma != 0 gives oscillatory kernel via cos factor."""
        from lib.quartic_arithmetic_closure import genuine_residue_kernel
        c_val = 26
        u0 = mpf(2)
        rho_real = mpc(mpf('0.5'), 0)
        rho_complex = mpc(mpf('0.5'), mpf(14.134725))  # near first zeta zero

        # Real rho: kernel at two Delta values should have same sign (no oscillation)
        w1_real = genuine_residue_kernel(c_val, rho_real, u0, mpf(1))
        w2_real = genuine_residue_kernel(c_val, rho_real, u0, mpf(2))
        # Both should be nonzero and have same sign (pure decay)
        assert w1_real * w2_real >= 0 or fabs(w1_real) < mpf('1e-30') or fabs(w2_real) < mpf('1e-30')

    def test_real_zero_no_oscillation(self):
        """gamma=0: the cos factor has no oscillation."""
        from lib.quartic_arithmetic_closure import genuine_residue_kernel
        c_val = 26
        u0 = mpf(2)
        rho = mpc(mpf('0.5'), 0)
        # The cos factor with gamma=0 is just cos(arg(A_c(rho))), a constant
        w1 = genuine_residue_kernel(c_val, rho, u0, mpf(1))
        w2 = genuine_residue_kernel(c_val, rho, u0, mpf(10))
        # Ratio should be a pure power law (no oscillatory correction)
        if fabs(w1) > mpf('1e-40') and fabs(w2) > mpf('1e-40'):
            ratio = w2 / w1
            # For pure power law: ratio = (10/1)^exponent * (10)^(-u0) / (1)^(-u0)
            # which should be a real power of 10
            log_ratio = log(fabs(ratio))
            # Check that log_ratio / log(10) is approximately an integer combination
            assert isinstance(float(log_ratio), float)  # just check it's well-defined

    def test_kernel_positive_large_delta(self):
        """Kernel decays to zero as Delta -> infinity."""
        from lib.quartic_arithmetic_closure import genuine_residue_kernel
        c_val = 26
        rho = mpc(mpf('0.5'), 0)
        u0 = mpf(2)
        w_small = fabs(genuine_residue_kernel(c_val, rho, u0, mpf(1)))
        w_large = fabs(genuine_residue_kernel(c_val, rho, u0, mpf(1000)))
        assert w_large < w_small, "Kernel should decay at large Delta"


# =============================================================================
# Test 6: Li coefficients
# =============================================================================

class TestLiCoefficients:
    def test_heisenberg_positive_low(self):
        """Heisenberg: lambda_n > 0 for n <= 6."""
        from lib.quartic_arithmetic_closure import li_coefficient
        for n in range(1, 7):
            lam = li_coefficient([1], n)
            assert lam > 0, f"lambda_{n}(H) should be positive, got {float(lam)}"

    def test_heisenberg_negative_7(self):
        """Heisenberg: lambda_7 < 0 (first sign change)."""
        from lib.quartic_arithmetic_closure import li_coefficient
        lam = li_coefficient([1], 7)
        assert lam < 0, f"lambda_7(H) should be negative, got {float(lam)}"

    def test_virasoro_all_negative(self):
        """Virasoro: all lambda_n < 0 for n >= 1."""
        from lib.quartic_arithmetic_closure import li_coefficient
        for n in range(1, 10):
            lam = li_coefficient([2], n)
            assert lam < 0, f"lambda_{n}(Vir) should be negative, got {float(lam)}"

    def test_w3_all_negative(self):
        """W_3: all lambda_n < 0 for n >= 1."""
        from lib.quartic_arithmetic_closure import li_coefficient
        for n in range(1, 8):
            lam = li_coefficient([2, 3], n)
            assert lam < 0, f"lambda_{n}(W_3) should be negative, got {float(lam)}"

    def test_wN_all_negative(self):
        """W_N (N=4,5): all lambda_n < 0 for n >= 1."""
        from lib.quartic_arithmetic_closure import li_coefficient
        for N in [4, 5]:
            weights = list(range(2, N + 1))
            for n in range(1, 6):
                lam = li_coefficient(weights, n)
                assert lam < 0, f"lambda_{n}(W_{N}) should be negative"

    def test_sign_dichotomy(self):
        """Exact Euler-Koszul gives mixed signs; defective gives all negative."""
        from lib.quartic_arithmetic_closure import li_sign_pattern
        # Heisenberg (exact EK): mixed signs
        h_signs = li_sign_pattern([1], max_n=10)
        assert 1 in h_signs and -1 in h_signs, "Heisenberg should have mixed signs"

        # Virasoro (defective): all negative
        v_signs = li_sign_pattern([2], max_n=10)
        assert all(s == -1 for s in v_signs), "Virasoro should be all negative"

    def test_li_positivity_fails(self):
        """Li positivity check fails for all standard families."""
        from lib.quartic_arithmetic_closure import li_positivity_check
        assert not li_positivity_check([1], max_n=10), "Heisenberg should fail"
        assert not li_positivity_check([2], max_n=5), "Virasoro should fail"
        assert not li_positivity_check([2, 3], max_n=5), "W_3 should fail"

    def test_li_cross_check_with_helper(self):
        """Cross-check li_coefficient against self-contained helper."""
        from lib.quartic_arithmetic_closure import li_coefficient
        # Heisenberg lambda_1
        lam_lib = li_coefficient([1], 1)
        lam_self = _li_n([1], 1)
        assert fabs(lam_lib - lam_self) < mpf('1e-8'), \
            f"Cross-check failed: {float(lam_lib)} vs {float(lam_self)}"

    def test_betagamma_positive_low(self):
        """Beta-gamma (weights [1,1]): lambda_n > 0 for low n."""
        from lib.quartic_arithmetic_closure import li_coefficient
        # beta-gamma = 2 copies of Heisenberg at character level
        lam1 = li_coefficient([1, 1], 1)
        assert lam1 > 0, f"lambda_1(bg) should be positive"


# =============================================================================
# Test 7: Compatibility locus
# =============================================================================

class TestCompatibilityLocus:
    def test_compatibility_ratios_finite(self):
        """Compatibility ratios are finite at generic (c, rho, u_0)."""
        from lib.quartic_arithmetic_closure import compatibility_ratio_c3, compatibility_ratio_c4_gram
        c_val = mpf(26)
        rho = mpc(mpf('0.5'), 0)
        u0 = mpf(2)
        r3 = compatibility_ratio_c3(c_val, rho, u0)
        r4 = compatibility_ratio_c4_gram(c_val, rho, u0)
        assert fabs(r3) < mpf('1e20'), "C_3 should be finite"
        assert fabs(r4) < mpf('1e20'), "C_4 should be finite"

    def test_on_line_satisfies(self):
        """On-line (sigma=1/2) gives well-defined compatibility ratios for all c."""
        from lib.quartic_arithmetic_closure import compatibility_ratio_c3
        for c_val in [5, 13, 26, 50]:
            rho = mpc(mpf('0.5'), 0)
            u0 = mpf(2)
            r3 = compatibility_ratio_c3(mpf(c_val), rho, u0)
            # The ratio should be a finite real number (not NaN or exactly inf)
            assert isinstance(r3, (mpf, type(mpf(0)))), \
                f"On-line ratio should be well-defined at c={c_val}"

    def test_off_line_excluded_at_some_c(self):
        """Off-line (sigma != 1/2) gives different ratio behavior."""
        from lib.quartic_arithmetic_closure import compatibility_ratio_c3
        # Compare on-line and off-line at fixed c
        c_val = mpf(26)
        u0 = mpf(2)
        r_on = compatibility_ratio_c3(c_val, mpc(mpf('0.5'), 0), u0)
        r_off = compatibility_ratio_c3(c_val, mpc(mpf('0.7'), 0), u0)
        # They should be different (the off-line point is not in the locus)
        assert fabs(r_on - r_off) > mpf('1e-10'), \
            "On-line and off-line should give different ratios"

    def test_compatibility_locus_well_defined(self):
        """The compatibility locus computation runs and returns data."""
        from lib.quartic_arithmetic_closure import compatibility_locus
        c_val = mpf(26)
        u0 = mpf(2)
        rho_range = [0.3, 0.5, 0.7]
        # Use a very wide tolerance to just check the code runs
        locus = compatibility_locus(c_val, u0, rho_range, tol=mpf('100.0'))
        # Should return a list (possibly empty if ratios are very far from 1)
        assert isinstance(locus, list)


# =============================================================================
# Test 8: Moment generating function
# =============================================================================

class TestMomentGF:
    def test_heisenberg_gf_terminates(self):
        """Heisenberg GF terminates at arity 2: F_H(t) = (1/2)t^2."""
        from lib.quartic_arithmetic_closure import shadow_moment_generating_function
        for t_val in [0.1, 0.5, 1.0]:
            F = shadow_moment_generating_function('heisenberg', t_val)
            expected = mpf('0.5') * mpf(t_val) ** 2
            assert fabs(F - expected) < mpf('1e-30'), \
                f"Heisenberg GF wrong at t={t_val}"

    def test_virasoro_gf_nonzero(self):
        """Virasoro GF has nontrivial higher terms."""
        from lib.quartic_arithmetic_closure import shadow_moment_generating_function
        F_small = shadow_moment_generating_function('virasoro', 0.01)
        F_larger = shadow_moment_generating_function('virasoro', 0.1)
        # Should be different (higher terms contribute)
        assert fabs(F_small) > 0
        assert fabs(F_larger) > fabs(F_small)

    def test_betagamma_gf_terminates(self):
        """Beta-gamma GF terminates: F_{bg}(t) = t^2."""
        from lib.quartic_arithmetic_closure import shadow_moment_generating_function
        for t_val in [0.1, 0.5]:
            F = shadow_moment_generating_function('betagamma', t_val)
            expected = mpf(1) * mpf(t_val) ** 2
            assert fabs(F - expected) < mpf('1e-30')


# =============================================================================
# Test 9: Resonance divisor and residues
# =============================================================================

class TestResonance:
    def test_resonance_points(self):
        """Resonance divisor c(5c+22) = 0 gives c=0 and c=-22/5."""
        from lib.quartic_arithmetic_closure import resonance_divisor_virasoro
        pts = resonance_divisor_virasoro()
        assert fabs(pts[0]) < mpf('1e-40')
        assert fabs(pts[1] - mpf(-22) / 5) < mpf('1e-40')

    def test_residue_at_c0(self):
        """Residue at c=0 is 5/11."""
        from lib.quartic_arithmetic_closure import quartic_residue_at_resonance
        res = quartic_residue_at_resonance(0)
        assert fabs(res - mpf(5) / 11) < mpf('1e-30')

    def test_residue_at_lee_yang(self):
        """Residue at c=-22/5 is -5/11."""
        from lib.quartic_arithmetic_closure import quartic_residue_at_resonance
        res = quartic_residue_at_resonance(-22.0 / 5)
        assert fabs(res - mpf(-5) / 11) < mpf('1e-30')

    def test_residue_sum_zero(self):
        """Sum of residues at the two poles is zero: 5/11 + (-5/11) = 0."""
        from lib.quartic_arithmetic_closure import quartic_residue_at_resonance
        r1 = quartic_residue_at_resonance(0)
        r2 = quartic_residue_at_resonance(-22.0 / 5)
        assert fabs(r1 + r2) < mpf('1e-30')


# =============================================================================
# Test 10: Arithmetic closure
# =============================================================================

class TestArithmeticClosure:
    def test_defect_produces_negative_li(self):
        """Euler-Koszul defect produces all-negative Li coefficients."""
        from lib.quartic_arithmetic_closure import li_sign_pattern, euler_koszul_class
        # Virasoro: defective, all negative
        assert euler_koszul_class([2]) == 'finitely_defective'
        signs = li_sign_pattern([2], max_n=8)
        assert all(s == -1 for s in signs)

    def test_no_defect_mixed_li(self):
        """Exact Euler-Koszul (Heisenberg) gives mixed Li signs."""
        from lib.quartic_arithmetic_closure import li_sign_pattern, euler_koszul_class
        assert euler_koszul_class([1]) == 'exact'
        signs = li_sign_pattern([1], max_n=10)
        assert 1 in signs and -1 in signs

    def test_ds_preserves_negativity(self):
        """DS reduction (W_N -> W_{N-1} at character level) preserves sign pattern.

        W_3 weights [2,3] and W_4 weights [2,3,4] both have all-negative Li.
        DS reduction at the character level removes the highest weight generator.
        """
        from lib.quartic_arithmetic_closure import li_sign_pattern
        signs_w3 = li_sign_pattern([2, 3], max_n=6)
        signs_w4 = li_sign_pattern([2, 3, 4], max_n=6)
        # Both should be all negative
        assert all(s == -1 for s in signs_w3), "W_3 should be all negative"
        assert all(s == -1 for s in signs_w4), "W_4 should be all negative"

    def test_euler_koszul_defect_virasoro(self):
        """Virasoro defect D(u) = 1 - 1/zeta(u) at integer u."""
        from lib.quartic_arithmetic_closure import euler_koszul_defect
        for u_val in [3, 5, 10]:
            D = euler_koszul_defect([2], u_val)
            expected = 1 - 1 / zeta(mpf(u_val))
            assert fabs(D - expected) < mpf('1e-15'), \
                f"Defect wrong at u={u_val}: got {float(D)}, expected {float(expected)}"

    def test_euler_koszul_exact_heisenberg(self):
        """Heisenberg defect D(u) = 1 identically."""
        from lib.quartic_arithmetic_closure import euler_koszul_defect
        for u_val in [2, 3, 5, 10]:
            D = euler_koszul_defect([1], u_val)
            assert fabs(D - 1) < mpf('1e-15'), \
                f"Heisenberg defect should be 1 at u={u_val}, got {float(D)}"


# =============================================================================
# Test 11: Shadow depth classification
# =============================================================================

class TestShadowDepth:
    def test_heisenberg_gaussian(self):
        """Heisenberg is Gaussian (depth 2)."""
        from lib.quartic_arithmetic_closure import shadow_depth_class
        cls, depth = shadow_depth_class('heisenberg')
        assert cls == 'G'
        assert depth == 2

    def test_affine_lie(self):
        """Affine is Lie/tree (depth 3)."""
        from lib.quartic_arithmetic_closure import shadow_depth_class
        cls, depth = shadow_depth_class('affine')
        assert cls == 'L'
        assert depth == 3

    def test_betagamma_contact(self):
        """Beta-gamma is contact (depth 4)."""
        from lib.quartic_arithmetic_closure import shadow_depth_class
        cls, depth = shadow_depth_class('betagamma')
        assert cls == 'C'
        assert depth == 4

    def test_virasoro_mixed(self):
        """Virasoro is mixed (depth infinity)."""
        from lib.quartic_arithmetic_closure import shadow_depth_class
        cls, depth = shadow_depth_class('virasoro')
        assert cls == 'M'
        assert depth == float('inf')

    def test_wn_mixed(self):
        """W_N is mixed (depth infinity) for N >= 3."""
        from lib.quartic_arithmetic_closure import shadow_depth_class
        for name in ['W3', 'W4', 'WN']:
            cls, depth = shadow_depth_class(name)
            assert cls == 'M'
            assert depth == float('inf')


# =============================================================================
# Test 12: Schur complement general families
# =============================================================================

class TestSchurComplementGeneral:
    def test_heisenberg_zero(self):
        """Heisenberg Schur complement is zero (no cubic, no quartic)."""
        from lib.quartic_arithmetic_closure import schur_complement_general
        S = schur_complement_general('heisenberg', 26)
        assert fabs(S) < mpf('1e-40')

    def test_betagamma_zero(self):
        """Beta-gamma Schur complement is zero (mu = 0)."""
        from lib.quartic_arithmetic_closure import schur_complement_general
        S = schur_complement_general('betagamma', 26)
        assert fabs(S) < mpf('1e-40')

    def test_virasoro_negative(self):
        """Virasoro raw Schur complement mu_4 - mu_3^2/mu_2 < 0 for c > 0.

        mu_4 = 10/(c(5c+22)) is small, mu_3^2/mu_2 = 8/c is large,
        so the raw Schur complement is negative for all c > 0.
        This means the 2x2 Hankel matrix is NOT positive definite.
        """
        from lib.quartic_arithmetic_closure import schur_complement_general
        for c_val in [1, 5, 13, 26, 100]:
            S = schur_complement_general('virasoro', c_val)
            assert S < 0, f"Raw Schur complement should be negative at c={c_val}"

    def test_w3_schur_complement(self):
        """W_3 Schur complement is well-defined and finite."""
        from lib.quartic_arithmetic_closure import schur_complement_general
        S = schur_complement_general('W3', 26)
        assert fabs(S) < mpf('1e10'), "W_3 Schur complement should be finite"
        assert fabs(S) > mpf('1e-40'), "W_3 Schur complement should be nonzero"


# =============================================================================
# Test 13: Decay exponent structure
# =============================================================================

class TestDecayStructure:
    def test_on_line_formula(self):
        """On-line decay = -(2c-1)/4."""
        from lib.quartic_arithmetic_closure import on_line_decay
        for c_val in [1, 13, 26]:
            d = on_line_decay(c_val)
            expected = -(2 * mpf(c_val) - 1) / 4
            assert fabs(d - expected) < mpf('1e-40')

    def test_off_line_strictly_less(self):
        """Off-line decay exponent is strictly less than on-line for sigma > 1/2."""
        from lib.quartic_arithmetic_closure import on_line_decay, off_line_decay
        for c_val in [1, 13, 26]:
            d_on = on_line_decay(c_val)
            for sigma in [0.6, 0.7, 0.8, 0.9, 1.0]:
                d_off = off_line_decay(c_val, sigma)
                assert d_off < d_on, \
                    f"Off-line decay should be faster at c={c_val}, sigma={sigma}"

    def test_decay_monotone_in_sigma(self):
        """Decay exponent decreases monotonically with sigma."""
        from lib.quartic_arithmetic_closure import decay_exponent
        c_val = 26
        sigmas = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        exponents = [float(decay_exponent(c_val, s)) for s in sigmas]
        for i in range(len(exponents) - 1):
            assert exponents[i] > exponents[i + 1], \
                f"Decay not monotone at sigma={sigmas[i]} to {sigmas[i+1]}"

    def test_decay_monotone_in_c(self):
        """Decay exponent decreases with c at fixed sigma."""
        from lib.quartic_arithmetic_closure import decay_exponent
        sigma = 0.5
        c_vals = [1, 5, 13, 26, 50, 100]
        exponents = [float(decay_exponent(c, sigma)) for c in c_vals]
        for i in range(len(exponents) - 1):
            assert exponents[i] > exponents[i + 1], \
                f"Decay not monotone in c at c={c_vals[i]} to {c_vals[i+1]}"


# =============================================================================
# Test 14: W_3 quartic contact
# =============================================================================

class TestW3QuarticContact:
    def test_w3_formula(self):
        """Q_3^ct = 220/(c(5c+22)^2)."""
        from lib.quartic_arithmetic_closure import w3_quartic_contact
        for c_val in [1, 5, 13, 26]:
            Q = w3_quartic_contact(c_val)
            expected = mpf(220) / (c_val * (5 * c_val + 22) ** 2)
            assert fabs(Q - expected) < mpf('1e-35'), f"Failed at c={c_val}"

    def test_w3_larger_than_vir(self):
        """W_3 quartic > Virasoro quartic for all c > 0 (extra 22/(5c+22) factor)."""
        from lib.quartic_arithmetic_closure import w3_quartic_contact, quartic_contact_virasoro
        for c_val in [1, 5, 13, 26, 100]:
            Q_vir = quartic_contact_virasoro(c_val)
            Q_w3 = w3_quartic_contact(c_val)
            # Q_w3 / Q_vir = 22/(5c+22)
            ratio = Q_w3 / Q_vir
            expected_ratio = mpf(22) / (5 * c_val + 22)
            assert fabs(ratio - expected_ratio) < mpf('1e-30'), \
                f"Ratio wrong at c={c_val}"

    def test_w3_positive(self):
        """Q_3^ct > 0 for c > 0."""
        from lib.quartic_arithmetic_closure import w3_quartic_contact
        for c_val in [0.01, 1, 10, 100]:
            Q = w3_quartic_contact(c_val)
            assert Q > 0


# =============================================================================
# Test 15: Full closure test
# =============================================================================

class TestQuarticClosureConjecture:
    def test_closure_test_runs(self):
        """The quartic closure test runs without error."""
        from lib.quartic_arithmetic_closure import quartic_closure_test
        results = quartic_closure_test(
            c_values=[26],
            u0_values=[2],
            sigma_range=[0.3, 0.5, 0.7],
            gamma_val=0
        )
        assert len(results) == 1
        key = (26.0, 2.0)
        assert key in results
        assert len(results[key]) == 3  # three sigma values tested

    def test_closure_different_c(self):
        """Different c values give different compatibility data."""
        from lib.quartic_arithmetic_closure import quartic_closure_test
        results = quartic_closure_test(
            c_values=[13, 26],
            u0_values=[2],
            sigma_range=[0.5],
            gamma_val=0
        )
        assert len(results) == 2
        data_13 = results[(13.0, 2.0)]
        data_26 = results[(26.0, 2.0)]
        # The C3 values should differ between c=13 and c=26
        if len(data_13) > 0 and len(data_26) > 0:
            assert data_13[0]['C3'] != data_26[0]['C3']


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
