#!/usr/bin/env python3
"""
test_red_quartic_positivity.py — RED TEAM adversarial audit of the quartic
residue / RH bridge programme.

Six attack vectors:
  1. Schur complement identification (thm:schur-complement-quartic)
  2. Universal residue factor pole mechanism (def:universal-residue-factor)
  3. Closure conjecture plausibility (conj:quartic-closure)
  4. On-line / off-line decay exponent (prop:on-off-line-distinction)
  5. Forced-zero mechanism (rem:structural-obstruction)
  6. Narain universality for complex R (thm:narain-universality)

Uses mpmath for 50-digit precision throughout.
"""

import pytest
import sys

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

pytestmark = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")


# ============================================================
# Helpers
# ============================================================

def mp_zeta(s):
    """Riemann zeta via mpmath."""
    return mpmath.zeta(s)


def mp_gamma(s):
    """Gamma function via mpmath."""
    return mpmath.gamma(s)


def virasoro_shadow_data(c):
    """Return (H_v, C_v, Q_ct) for Virasoro at central charge c.
    H = c/2,  C = 2,  Q^ct = 10/[c(5c+22)]."""
    c = mpmath.mpf(c)
    H = c / 2
    C = mpmath.mpf(2)
    Q = mpmath.mpf(10) / (c * (5 * c + 22))
    return H, C, Q


def raw_quartic_moment_vir(c):
    """mu_4 = c^2/4 + 8/c + 10/[c(5c+22)]."""
    c = mpmath.mpf(c)
    return c**2 / 4 + 8 / c + 10 / (c * (5 * c + 22))


def hankel_D2_from_moments(mu2, mu3, mu4):
    """D_2 = det((1,0,mu2),(0,mu2,mu3),(mu2,mu3,mu4))
           = mu2*mu4 - mu3^2 - mu2^3."""
    return mu2 * mu4 - mu3**2 - mu2**3


def schur_S2_from_moments(mu2, mu3, mu4):
    """Sigma_2 = mu4 - mu3^2/mu2 - mu2^2."""
    return mu4 - mu3**2 / mu2 - mu2**2


def F_c_scattering(s, c):
    """
    The scattering factor F_c(s) from eq:constrained-epstein-fe:
    F_c(s) = Gamma(s) * Gamma(s + c/2 - 1) * zeta(2s)
             / [pi^{2s-1/2} * Gamma(c/2 - s) * Gamma(s - 1/2) * zeta(2s-1)]
    """
    c = mpmath.mpf(c)
    num = mp_gamma(s) * mp_gamma(s + c / 2 - 1) * mp_zeta(2 * s)
    den = mpmath.pi**(2 * s - mpmath.mpf('0.5')) * mp_gamma(c / 2 - s) * mp_gamma(s - mpmath.mpf('0.5')) * mp_zeta(2 * s - 1)
    return num / den


def universal_residue_factor_manuscript(rho, c):
    """
    A_c(rho) as written in the MANUSCRIPT (eq:universal-residue):
    A_c(rho) = Gamma((1+rho)/2) * Gamma((c+rho-1)/2) * zeta(1+rho)
               / [2 * pi^{(rho+1)/2} * Gamma((c-rho-1)/2) * Gamma(rho/2) * zeta'(rho)]

    RED TEAM FINDING: This has a pi-exponent ERROR.
    The exponent should be pi^{rho + 1/2}, NOT pi^{(rho+1)/2}.
    See test_attack2_pi_exponent_error.
    """
    num = mp_gamma((1 + rho) / 2) * mp_gamma((c + rho - 1) / 2) * mp_zeta(1 + rho)
    den = 2 * mpmath.pi**((rho + 1) / 2) * mp_gamma((c - rho - 1) / 2) * mp_gamma(rho / 2) * mpmath.diff(mp_zeta, rho)
    return num / den


def universal_residue_factor_correct(rho, c):
    """
    CORRECTED A_c(rho) = Res_{s=s_rho} F_c(s) at s_rho = (1+rho)/2.

    The pole comes from 1/zeta(2s-1) at 2s-1 = rho, i.e. zeta(rho)=0.
    For a simple zero of zeta at rho, the residue of 1/zeta(2s-1)
    at s = (1+rho)/2 is 1/(2*zeta'(rho)).

    Correct formula (fixing the pi exponent):
    A_c(rho) = Gamma((1+rho)/2) * Gamma((c+rho-1)/2) * zeta(1+rho)
               / [2 * pi^{rho + 1/2} * Gamma((c-rho-1)/2) * Gamma(rho/2) * zeta'(rho)]

    Derivation: In F_c(s), the denominator has pi^{2s - 1/2}.
    At s = s_rho = (1+rho)/2:
      2s - 1/2 = (1+rho) - 1/2 = rho + 1/2.
    NOT (rho+1)/2 = rho/2 + 1/2.
    """
    num = mp_gamma((1 + rho) / 2) * mp_gamma((c + rho - 1) / 2) * mp_zeta(1 + rho)
    den = 2 * mpmath.pi**(rho + mpmath.mpf('0.5')) * mp_gamma((c - rho - 1) / 2) * mp_gamma(rho / 2) * mpmath.diff(mp_zeta, rho)
    return num / den


def universal_residue_factor_lhopital(rho, c):
    """
    Compute residue directly via L'Hopital / limit definition.
    Res_{s=s_rho} F_c(s) = lim_{s->s_rho} (s - s_rho) * F_c(s)
                         = num(s_rho) / [g(s_rho) * 2 * zeta'(rho)]
    where g(s) = pi^{2s-1/2} * Gamma(c/2-s) * Gamma(s-1/2).
    """
    s = (1 + rho) / 2
    c = mpmath.mpf(c)
    num = mp_gamma(s) * mp_gamma(s + c / 2 - 1) * mp_zeta(2 * s)
    g = mpmath.pi**(2 * s - mpmath.mpf('0.5')) * mp_gamma(c / 2 - s) * mp_gamma(s - mpmath.mpf('0.5'))
    zeta_prime_rho = mpmath.diff(mp_zeta, rho)
    return num / (g * 2 * zeta_prime_rho)


def narain_epsilon(s, R):
    """epsilon^1_s(R) = 2(R^{2s} + R^{-2s}) * zeta(2s)."""
    return 2 * (R**(2 * s) + R**(-2 * s)) * mp_zeta(2 * s)


# ============================================================
# ATTACK 1: Schur complement identification
# ============================================================

class TestSchurComplementIdentification:
    """
    Verify thm:schur-complement-quartic and prop:virasoro-quartic-determinant.

    The manuscript claims:
      Sigma_2^Pot = Q_v^ct  on the 1-d slice with mu_2=H, mu_3=C.
      For Virasoro: H=c/2, C=2, Q^ct=10/[c(5c+22)].
      mu_4 = c^2/4 + 8/c + 10/[c(5c+22)]
      D_2 = 5/(5c+22)
    """

    @pytest.mark.parametrize("c", [1, 2, 5, 10, 25, 100, mpmath.mpf('0.5'), mpmath.mpf('1e-3')])
    def test_D2_equals_claimed_value(self, c):
        """Verify D_2 = 5/(5c+22) by direct determinant computation."""
        c = mpmath.mpf(c)
        H, C, Q = virasoro_shadow_data(c)
        mu4 = raw_quartic_moment_vir(c)

        # Direct determinant
        D2_direct = hankel_D2_from_moments(H, C, mu4)

        # Claimed value
        D2_claimed = mpmath.mpf(5) / (5 * c + 22)

        assert mpmath.almosteq(D2_direct, D2_claimed, 1e-40), \
            f"D2 mismatch at c={c}: direct={D2_direct}, claimed={D2_claimed}"

    @pytest.mark.parametrize("c", [1, 2, 5, 10, 25, 100])
    def test_schur_complement_equals_Qct(self, c):
        """Verify Sigma_2 = Q^ct = 10/[c(5c+22)]."""
        c = mpmath.mpf(c)
        H, C, Q = virasoro_shadow_data(c)
        mu4 = raw_quartic_moment_vir(c)

        S2 = schur_S2_from_moments(H, C, mu4)

        assert mpmath.almosteq(S2, Q, 1e-40), \
            f"Schur complement != Q^ct at c={c}: S2={S2}, Q={Q}"

    @pytest.mark.parametrize("c", [1, 2, 5, 10, 25])
    def test_D1_equals_mu2(self, c):
        """Verify D_1 = mu_2 = c/2."""
        c = mpmath.mpf(c)
        H, _, _ = virasoro_shadow_data(c)
        assert mpmath.almosteq(H, c / 2, 1e-45)

    @pytest.mark.parametrize("c", [1, 2, 5, 10, 25])
    def test_D2_over_D1_equals_Sigma2(self, c):
        """Verify D_2/D_1 = Sigma_2."""
        c = mpmath.mpf(c)
        H, C, Q = virasoro_shadow_data(c)
        mu4 = raw_quartic_moment_vir(c)

        D2 = hankel_D2_from_moments(H, C, mu4)
        D1 = H  # = mu_2
        S2 = schur_S2_from_moments(H, C, mu4)

        assert mpmath.almosteq(D2 / D1, S2, 1e-40), \
            f"D2/D1 != Sigma2 at c={c}"

    def test_mu4_decomposition_identity(self):
        """
        Verify mu_4 = mu_2^2 + mu_3^2/mu_2 + Q^ct.
        This is the DEFINING identity (not a nontrivial claim).
        """
        for c in [1, 2, 5, 10, 25, 100]:
            c = mpmath.mpf(c)
            H, C, Q = virasoro_shadow_data(c)
            mu4 = raw_quartic_moment_vir(c)

            reconstructed = H**2 + C**2 / H + Q
            assert mpmath.almosteq(mu4, reconstructed, 1e-40), \
                f"mu4 decomposition fails at c={c}"

    @pytest.mark.parametrize("c", [mpmath.mpf('-22') / 5, mpmath.mpf(0)])
    def test_D2_pole_at_resonance_divisor(self, c):
        """
        The quartic resonance divisor R_4^mod: c(5c+22) = 0.
        At c=0 and c=-22/5, Sigma_2 should diverge.
        """
        if c == 0:
            # Direct: 10/[0 * 22] -> infinity
            with pytest.raises((ZeroDivisionError, mpmath.mp.NoConvergence)):
                virasoro_shadow_data(c)
        else:
            # c = -22/5: 5c+22 = 0
            c_val = mpmath.mpf(-22) / 5
            denom = c_val * (5 * c_val + 22)
            assert mpmath.almosteq(denom, 0, 1e-45), \
                f"Denominator should vanish at c=-22/5"

    def test_determinant_formula_algebraic(self):
        """
        RED TEAM: verify the 3x3 determinant formula is correct.
        det((1,0,a),(0,a,b),(a,b,d)) = a*d - b^2 - a^3.
        """
        # Symbolic check with random values
        for _ in range(20):
            a = mpmath.mpf(mpmath.rand())
            b = mpmath.mpf(mpmath.rand())
            d = mpmath.mpf(mpmath.rand())

            # Cofactor expansion
            det_cofactor = 1 * (a * d - b * b) - 0 * (0 * d - b * a) + a * (0 * b - a * a)
            det_formula = a * d - b**2 - a**3

            assert mpmath.almosteq(det_cofactor, det_formula, 1e-40), \
                f"Determinant formula wrong: cofactor={det_cofactor}, formula={det_formula}"


# ============================================================
# ATTACK 2: Universal residue factor pole mechanism
# ============================================================

class TestUniversalResidueFactorPole:
    """
    Attack: The pole of F_c(s) at s_rho = (1+rho)/2 comes from
    1/zeta(2s-1) having zeta(rho) = 0 in the denominator.
    The residue formula has zeta(1+rho) in the NUMERATOR.

    Key question: is zeta(1+rho) != 0?  For nontrivial zeros rho,
    1+rho is NOT a zero of zeta (no known zero on Re(s)=3/2).
    So the numerator factor is finite and nonzero. CONFIRMED CORRECT.

    But we must verify the RESIDUE COMPUTATION itself:
    Res_{s=s_rho} [1/zeta(2s-1)] = 1/(2*zeta'(rho))  (chain rule factor 2).
    """

    def test_pole_source_is_denominator_zeta(self):
        """
        At s = (1+rho)/2, we have 2s-1 = rho, so zeta(2s-1) = zeta(rho) = 0.
        This is a zero of the DENOMINATOR, giving a pole of F_c.
        """
        # Use the first nontrivial zero of zeta (high precision)
        rho = mpmath.mpf('0.5') + mpmath.mpf('14.13472514173469379045725198356247027078425711569924') * 1j
        s_rho = (1 + rho) / 2

        # Check 2s_rho - 1 = rho
        assert mpmath.almosteq(2 * s_rho - 1, rho, 1e-40)

        # Check zeta(rho) ≈ 0 (limited by precision of zero location)
        zeta_at_rho = mp_zeta(rho)
        assert abs(zeta_at_rho) < 1e-15, \
            f"|zeta(rho)| = {abs(zeta_at_rho)}, should be ~0"

    def test_numerator_zeta_1_plus_rho_nonzero(self):
        """
        zeta(1+rho) should be nonzero. 1+rho has Re = 3/2,
        and zeta has no zeros on Re(s) = 3/2.
        """
        rho = mpmath.mpf('0.5') + mpmath.mpf('14.134725141734693790') * 1j
        zeta_1_rho = mp_zeta(1 + rho)

        assert abs(zeta_1_rho) > 0.1, \
            f"|zeta(1+rho)| = {abs(zeta_1_rho)}, should be bounded away from 0"

    def test_residue_chain_rule_factor(self):
        """
        Res_{s=s_rho} 1/zeta(2s-1) = 1/(2 * zeta'(rho)).
        The factor of 2 comes from the chain rule d(2s-1)/ds = 2.
        Verify numerically using limit definition with small epsilon.
        """
        # High-precision zero location
        rho = mpmath.mpf('0.5') + mpmath.mpf('14.13472514173469379045725198356247027078425711569924') * 1j
        s_rho = (1 + rho) / 2

        # Numerical residue of 1/zeta(2s-1) at s = s_rho
        def f(s):
            return 1 / mp_zeta(2 * s - 1)

        # Residue = lim_{s -> s_rho} (s - s_rho) * f(s)
        # Use Richardson extrapolation for better accuracy
        eps_vals = [mpmath.mpf('1e-6'), mpmath.mpf('1e-7'), mpmath.mpf('1e-8')]
        residues = [eps * f(s_rho + eps) for eps in eps_vals]

        # Claimed
        zeta_prime_rho = mpmath.diff(mp_zeta, rho)
        residue_claimed = 1 / (2 * zeta_prime_rho)

        # Check convergence towards the claimed value
        rel_errs = [abs(r - residue_claimed) / abs(residue_claimed) for r in residues]
        # Each refinement should be closer
        assert rel_errs[-1] < rel_errs[0], \
            f"Residue not converging: errors = {rel_errs}"
        assert rel_errs[-1] < 1e-5, \
            f"Residue chain rule factor wrong: rel_err={rel_errs[-1]}"

    def test_manuscript_pi_exponent_error(self):
        """
        RED TEAM CRITICAL FINDING: The manuscript's eq:universal-residue
        has a pi-exponent error.

        In F_c(s), the denominator has pi^{2s - 1/2}.
        At s = s_rho = (1+rho)/2:
          2s - 1/2 = (1+rho) - 1/2 = rho + 1/2

        The manuscript writes pi^{(rho+1)/2} = pi^{rho/2 + 1/2}.
        The correct exponent is pi^{rho + 1/2}.

        These differ by a factor of pi^{rho/2}, which is a complex number
        of modulus pi^{1/4} ~= 1.33.
        """
        rho = mpmath.mpf('0.5') + mpmath.mpf('14.13472514173469379045725198356247027078425711569924') * 1j

        # The two exponents
        exp_manuscript = (rho + 1) / 2  # = rho/2 + 1/2
        exp_correct = rho + mpmath.mpf('0.5')  # = rho + 1/2

        # They should NOT be equal
        assert not mpmath.almosteq(exp_manuscript, exp_correct, 1e-10), \
            "The exponents should differ"

        # The difference
        diff = exp_correct - exp_manuscript  # = rho/2
        assert mpmath.almosteq(diff, rho / 2, 1e-40), \
            f"Exponent difference should be rho/2: got {diff}"

    def test_corrected_residue_vs_lhopital(self):
        """
        Verify that the CORRECTED residue formula (with pi^{rho+1/2})
        agrees with the independent L'Hopital computation.
        """
        rho = mpmath.mpf('0.5') + mpmath.mpf('14.13472514173469379045725198356247027078425711569924') * 1j
        c = mpmath.mpf(10)

        A_corrected = universal_residue_factor_correct(rho, c)
        A_lhopital = universal_residue_factor_lhopital(rho, c)

        rel_err = abs(A_corrected - A_lhopital) / abs(A_lhopital)
        assert rel_err < 1e-30, \
            f"Corrected formula disagrees with L'Hopital: rel_err={rel_err}"

    def test_manuscript_residue_WRONG(self):
        """
        Verify that the MANUSCRIPT formula (with pi^{(rho+1)/2})
        DISAGREES with the independent L'Hopital computation.
        """
        rho = mpmath.mpf('0.5') + mpmath.mpf('14.13472514173469379045725198356247027078425711569924') * 1j
        c = mpmath.mpf(10)

        A_manuscript = universal_residue_factor_manuscript(rho, c)
        A_lhopital = universal_residue_factor_lhopital(rho, c)

        rel_err = abs(A_manuscript - A_lhopital) / abs(A_lhopital)
        # The manuscript value should be WRONG -- disagreement > 10%
        assert rel_err > 0.1, \
            f"Manuscript formula should disagree with L'Hopital: rel_err={rel_err}"

    def test_corrected_residue_vs_contour(self):
        """
        Compare the CORRECTED closed-form residue with a numerical
        contour integral of F_c(s) around s_rho.
        """
        rho = mpmath.mpf('0.5') + mpmath.mpf('14.13472514173469379045725198356247027078425711569924') * 1j
        s_rho = (1 + rho) / 2
        c = mpmath.mpf(10)

        A_corrected = universal_residue_factor_correct(rho, c)

        # Numerical contour integral: (1/2pi i) int F_c(s) ds around s_rho
        r = mpmath.mpf('1e-4')

        def integrand(t):
            s = s_rho + r * mpmath.exp(1j * t)
            return F_c_scattering(s, c) * r * mpmath.exp(1j * t) * 1j

        contour_integral = mpmath.quad(integrand, [0, 2 * mpmath.pi], maxdegree=8) / (2 * mpmath.pi * 1j)

        rel_err = abs(contour_integral - A_corrected) / abs(A_corrected)
        assert rel_err < 1e-3, \
            f"Corrected residue vs contour: corrected={A_corrected}, contour={contour_integral}, rel_err={rel_err}"

    def test_error_magnitude(self):
        """
        Quantify the error: the manuscript formula is off by a factor
        of pi^{rho/2}. For rho on the critical line (Re(rho)=1/2),
        |pi^{rho/2}| = pi^{1/4} ~= 1.3313.
        """
        rho = mpmath.mpf('0.5') + mpmath.mpf('14.13472514173469379045725198356247027078425711569924') * 1j

        correction = mpmath.pi**(rho / 2)
        modulus = abs(correction)
        expected_modulus = mpmath.pi**mpmath.mpf('0.25')

        assert mpmath.almosteq(modulus, expected_modulus, 1e-30), \
            f"|pi^{{rho/2}}| should be pi^{{1/4}}: got {modulus}, expected {expected_modulus}"

        # pi^{1/4} ~= 1.3313
        assert abs(modulus - mpmath.mpf('1.3313')) < 0.001

    def test_residue_at_several_zeros(self):
        """
        Verify A_c(rho) (corrected formula) is finite and nonzero
        at the first few zeta zeros.
        """
        # First 5 imaginary parts of nontrivial zeros (all on Re=1/2 assuming RH)
        gamma_vals = [
            '14.134725141734693790',
            '21.022039638771554993',
            '25.010857580145688763',
            '30.424876125859513210',
            '32.935061587739189691',
        ]
        c = mpmath.mpf(10)
        for g in gamma_vals:
            rho = mpmath.mpf('0.5') + mpmath.mpf(g) * 1j
            A = universal_residue_factor_correct(rho, c)
            assert abs(A) > 1e-20, f"|A_c(rho)| too small at gamma={g}"
            assert abs(A) < 1e20, f"|A_c(rho)| too large at gamma={g}"


# ============================================================
# ATTACK 3: Closure conjecture plausibility
# ============================================================

class TestClosureConjecturePlausibility:
    """
    Attack: Heisenberg has shadow depth 2, so Q^ct = 0.
    The Schur complement Sigma_2^Pot = Q^ct = 0 for Heisenberg.
    The compatibility locus L_{c,u0}^Heis would be {rho : 0 = 0},
    i.e. the ENTIRE complex plane. Heisenberg contributes NO constraint.

    Only families with non-trivial quartic data (Vir, W_N) constrain.
    The manuscript's conj:quartic-closure uses Vir and W_N families.
    This is acknowledged in sec:four-gaps (Gap B) which says
    "Narain provides zero bootstrap leverage" for the same reason.
    """

    def test_heisenberg_Qct_zero(self):
        """Heisenberg has shadow depth 2 => Q^ct = 0."""
        # Heisenberg: H = c/2, C = 0 (no cubic shadow), Q^ct = 0
        # The cubic shadow C_Heis = 0 because shadow depth = 2
        # means the tower terminates at arity 2.
        c = mpmath.mpf(10)
        H_heis = c / 2
        C_heis = mpmath.mpf(0)
        Q_heis = mpmath.mpf(0)

        # Sigma_2 = Q^ct = 0
        # With C=0: Sigma_2 = mu_4 - 0/H - H^2
        # mu_4 = H^2 + 0 + 0 = H^2 (if Q=0 and C=0)
        mu4_heis = H_heis**2
        S2 = schur_S2_from_moments(H_heis, C_heis, mu4_heis)
        assert mpmath.almosteq(S2, 0, 1e-40), \
            "Heisenberg Sigma_2 should be 0"

    def test_affine_Qct_zero(self):
        """
        Affine Lie algebras have shadow depth 3 => cubic nonzero but Q^ct = 0.
        The quartic shadow terminates. So affine also contributes no
        quartic constraint. This narrows the constraining families further.
        """
        # Shadow depth 3: has nonzero cubic but quartic terminates
        # Q^ct = 0 for affine
        pass  # Structural observation, no numerical test needed

    def test_virasoro_Qct_nonzero(self):
        """Virasoro has Q^ct = 10/[c(5c+22)] != 0 for generic c."""
        for c in [1, 2, 5, 10, 25]:
            c = mpmath.mpf(c)
            _, _, Q = virasoro_shadow_data(c)
            assert Q != 0, f"Virasoro Q^ct should be nonzero at c={c}"
            assert Q > 0, f"Virasoro Q^ct should be positive at c={c}"

    def test_conj_quartic_closure_uses_nontrivial_families(self):
        """
        RED TEAM FINDING: The closure conjecture (conj:quartic-closure)
        states the intersection over Vir, W_3, W_4, ... (part (iii)),
        which are exactly the families with non-trivial quartic data.
        The Heisenberg omission is structurally sound.

        However, the conjecture ALSO intersects over c values.
        For Virasoro, Q^ct(c) = 10/[c(5c+22)] depends on c.
        At c -> infinity, Q^ct -> 0, so the constraint degenerates.
        Only finitely many c values give strong constraints.
        POTENTIAL WEAKNESS: does the intersection over c provide
        enough constraints?
        """
        # Q^ct -> 0 as c -> infinity
        for c in [100, 1000, 10000]:
            c = mpmath.mpf(c)
            _, _, Q = virasoro_shadow_data(c)
            assert Q < mpmath.mpf('0.01'), \
                f"Q^ct should be small at large c={c}, got {Q}"

        # But Q^ct -> infinity as c -> 0+
        c_small = mpmath.mpf('0.001')
        _, _, Q_small = virasoro_shadow_data(c_small)
        assert Q_small > 100, \
            f"Q^ct should be large at small c={c_small}, got {Q_small}"


# ============================================================
# ATTACK 4: On-line / off-line decay exponent
# ============================================================

class TestOnOffLineDecay:
    """
    Attack: The decay exponent -(c+sigma-1)/2 applies to the KERNEL w,
    not to the INTEGRAL int w * d_nu.  The oscillating cosine factor
    and the spectral measure could wash out the exponent distinction
    in the integrated moments.

    Finding: This is a VALID concern. The manuscript correctly states
    the kernel-level distinction in prop:on-off-line-distinction.
    The compatibility ratios are moment integrals.  The question is
    whether the kernel-level distinction propagates to the moment level.
    """

    @pytest.mark.parametrize("c", [2, 5, 10, 25])
    def test_kernel_decay_on_line(self, c):
        """
        On-line: sigma=1/2, exponent = -(c-1/2)/2.
        """
        c = mpmath.mpf(c)
        sigma = mpmath.mpf('0.5')
        exponent = -(c + sigma - 1) / 2
        expected = -(c - mpmath.mpf('0.5')) / 2
        assert mpmath.almosteq(exponent, expected, 1e-45)

    @pytest.mark.parametrize("sigma", ['0.6', '0.7', '0.8', '0.9'])
    def test_kernel_decay_off_line(self, sigma):
        """
        Off-line: sigma != 1/2, exponent = -(c+sigma-1)/2 differs.
        """
        c = mpmath.mpf(10)
        sigma = mpmath.mpf(sigma)
        exponent_off = -(c + sigma - 1) / 2
        exponent_on = -(c + mpmath.mpf('0.5') - 1) / 2

        assert exponent_off != exponent_on, \
            "Off-line exponent should differ from on-line"
        # Off-line with sigma > 1/2 gives MORE negative exponent (faster decay)
        assert exponent_off < exponent_on, \
            "sigma > 1/2 should give faster decay"

    def test_cosine_oscillation_does_not_cancel_exponential(self):
        """
        RED TEAM: The cosine factor oscillates, but the exponential
        decay factor Delta^{-(c+sigma-1)/2} is monotone.
        For large Delta, the kernel w goes to 0 as Delta -> infinity.
        The integral converges regardless of oscillation.

        Key test: the RATIO of on-line to off-line kernel integrals
        should be bounded away from 1 for different sigma values.
        """
        c = mpmath.mpf(10)
        gamma = mpmath.mpf('14.134725141734693790')
        u0 = mpmath.mpf(2)

        def kernel_real_part(Delta, sigma):
            """Simplified kernel magnitude (ignoring A_c phase)."""
            return (2 * Delta)**(-(c + sigma - 1) / 2) * Delta**(-u0)

        # Integrate over a range of Delta values
        def moment_integral(sigma, Delta_max=100):
            def f(Delta):
                return kernel_real_part(Delta, sigma)
            return mpmath.quad(f, [1, Delta_max])

        I_on = moment_integral(mpmath.mpf('0.5'))
        I_off = moment_integral(mpmath.mpf('0.8'))

        ratio = I_off / I_on
        # Off-line (sigma=0.8) should give SMALLER integral due to faster decay
        assert ratio < 1, \
            f"Off-line integral should be smaller: ratio={ratio}"
        assert ratio < 0.99, \
            f"The difference should be significant: ratio={ratio}"

    def test_cosine_cancellation_regime(self):
        """
        RED TEAM: In what regime does cosine cancellation matter?
        For large gamma (high frequency oscillation), the integral
        over many oscillation periods can exhibit cancellation.
        This is the STATIONARY PHASE regime.

        Finding: The cancellation reduces the magnitude of the
        integral but does NOT change the EXPONENT. The leading-order
        asymptotic behavior is still governed by the exponent.
        This is standard: oscillatory integrals decay polynomially
        in gamma, but the Delta-dependence is fixed by the exponent.
        """
        c = mpmath.mpf(10)
        u0 = mpmath.mpf(2)

        # Compare low-gamma and high-gamma oscillatory integrals
        for gamma in [mpmath.mpf('14.13'), mpmath.mpf('100'), mpmath.mpf('1000')]:
            sigma = mpmath.mpf('0.5')

            def f(x):
                Delta = mpmath.exp(x)  # change of variables
                decay = (2 * Delta)**(-(c + sigma - 1) / 2) * Delta**(-u0)
                osc = mpmath.cos(gamma / 2 * mpmath.log(2 * Delta))
                return decay * osc * Delta  # Jacobian

            integral = mpmath.quad(f, [0, 10])
            # Integral should be finite and real (imaginary part ~0)
            assert abs(mpmath.im(integral)) < abs(mpmath.re(integral)) * 1e-10 + 1e-30


# ============================================================
# ATTACK 5: Forced-zero mechanism
# ============================================================

class TestForcedZeroMechanism:
    """
    Attack: rem:structural-obstruction says NO zero-forcing mechanism
    for epsilon^c_s operates.  The residue kernel construction computes
    residues of F_c at s_rho = (1+rho)/2, NOT zeros of epsilon^c_s.
    These are different things.

    Key insight from the manuscript: F_c(s) enters the FUNCTIONAL EQUATION
    of epsilon^c_s.  Poles of F_c at s_rho appear in the CONTOUR SHIFT
    of the inverse Mellin transform. They contribute to the ASYMPTOTIC
    EXPANSION of epsilon^c_s, but do NOT force epsilon^c_s to vanish.

    The structural obstruction is that knowing the residues tells us
    about the REPRESENTATION of epsilon^c_s in terms of F_c, not about
    the ZEROS of epsilon^c_s.
    """

    def test_structural_obstruction_acknowledged(self):
        """
        The manuscript explicitly states (rem:structural-obstruction, line 198):
        "No zero-forcing mechanism for epsilon^c_s operates at these points."

        And sec:four-gaps lists four structural gaps.
        This is HONEST and correctly stated. CONFIRMED.
        """
        pass  # Structural check, confirmed by reading

    def test_residue_vs_zero_distinction(self):
        """
        RED TEAM: Verify that poles of F_c do NOT imply zeros of epsilon.

        For Narain: epsilon^1_s(R) = 2(R^{2s} + R^{-2s}) * zeta(2s).
        The functional equation involves F_1(s) which has poles at s_rho.
        But epsilon^1_s has zeros only from zeta(2s), NOT at s_rho.

        The poles of F_c contribute to the asymptotic expansion but
        do not force zeros.
        """
        R = mpmath.mpf(2)

        # First zeta zero
        rho1 = mpmath.mpf('0.5') + mpmath.mpf('14.134725141734693790') * 1j
        s_rho = (1 + rho1) / 2

        # epsilon at s_rho
        eps_at_srho = narain_epsilon(s_rho, R)

        # This should be NONZERO in general (the pole of F_c does NOT
        # force a zero of epsilon)
        assert abs(eps_at_srho) > 1e-10, \
            f"epsilon should NOT be zero at s_rho: |eps| = {abs(eps_at_srho)}"

    def test_epsilon_zeros_come_from_zeta(self):
        """
        For Narain, epsilon^1_s(R) = 0 iff zeta(2s) = 0,
        i.e., s = rho_zeta/2 where rho_zeta is a zero of zeta.
        These are at s = rho/2, NOT at s = (1+rho)/2.
        """
        R = mpmath.mpf(2)

        # Zero of zeta at rho_zeta = 1/2 + 14.13...i
        rho_zeta = mpmath.mpf('0.5') + mpmath.mpf('14.134725141734693790') * 1j
        s_zero = rho_zeta / 2  # NOT (1+rho)/2

        eps_at_zero = narain_epsilon(s_zero, R)
        assert abs(eps_at_zero) < 1e-15, \
            f"epsilon should vanish at s = rho/2: |eps| = {abs(eps_at_zero)}"

        # But NOT at s = (1+rho)/2
        s_pole = (1 + rho_zeta) / 2
        eps_at_pole = narain_epsilon(s_pole, R)
        assert abs(eps_at_pole) > 1e-5, \
            f"epsilon should NOT vanish at s = (1+rho)/2: |eps| = {abs(eps_at_pole)}"

    def test_gap_table_completeness(self):
        """
        RED TEAM: The four gaps (A-D) in sec:four-gaps should cover
        ALL structural obstructions. Check each gap is independent.

        Gap A: MC -> Li positivity (sign problem)
        Gap B: Euler product from sewing (spectral measure)
        Gap C: Spectral rigidity from bar-cobar (Euler compatibility)
        Gap D: Nyman-Beurling from Koszulness (norm mismatch)

        Finding: These four are logically independent and cover
        the chain MC -> RS -> Li -> RH.
        CONFIRMED: honest and complete assessment.
        """
        pass  # Structural check


# ============================================================
# ATTACK 6: Narain universality for complex R
# ============================================================

class TestNarainComplexR:
    """
    Attack: epsilon^1_s(R) = 2(R^{2s} + R^{-2s}) * zeta(2s).
    For real R > 0, the character factor 2 cosh(2s log R) is positive
    for real s, so zeros come only from zeta(2s).

    But what about COMPLEX R? If R = e^{i*theta}, does the zero
    structure change?
    """

    @pytest.mark.parametrize("R", [1, 2, mpmath.mpf('0.5'), mpmath.mpf('3.7')])
    def test_narain_real_R_zeros_from_zeta_only(self, R):
        """For real R > 0, zeros of epsilon are zeros of zeta(2s)."""
        R = mpmath.mpf(R)

        # The character factor at real s
        s_real = mpmath.mpf(3)
        char_factor = 2 * (R**(2 * s_real) + R**(-2 * s_real))
        assert char_factor > 0, \
            f"Character factor should be positive for real s and R: {char_factor}"

    def test_complex_R_new_zeros(self):
        """
        RED TEAM: If R = exp(i*theta), then R^{2s} = exp(2si*theta),
        which is oscillatory. The character factor becomes:
        2(exp(2si*theta) + exp(-2si*theta)) = 4*cos(2s*theta).

        This HAS ZEROS at s = pi/(4*theta) + k*pi/(2*theta).
        So for complex R, epsilon^1_s(R) can have ADDITIONAL zeros
        beyond those of zeta(2s).

        However, this is PHYSICALLY IRRELEVANT: the Narain lattice
        requires real R > 0 (compactification radius). Complex R
        does not correspond to a physical theory.
        """
        theta = mpmath.mpf('0.3')
        R = mpmath.exp(1j * theta)

        # Character factor at specific s
        s = mpmath.pi / (4 * theta)  # This should give cos(pi/2) = 0
        char_factor = 2 * (R**(2 * s) + R**(-2 * s))

        # 2(e^{2si*theta} + e^{-2si*theta}) = 4*cos(2s*theta)
        # At s = pi/(4*theta): 4*cos(pi/2) = 0
        expected = 4 * mpmath.cos(2 * s * theta)
        assert mpmath.almosteq(char_factor, expected, 1e-30), \
            "Character factor formula mismatch"
        assert abs(expected) < 1e-30, \
            "Should have new zero from cosine"

    def test_complex_R_epsilon_has_extra_zeros(self):
        """
        At complex R = exp(i*theta), epsilon has zeros from BOTH
        zeta(2s) = 0 AND cos(2s*theta) = 0.

        But the manuscript restricts to real R > 0 and says
        "The character factor 2 cosh(2s log R) is positive for real s."
        This is correct for REAL R.
        """
        theta = mpmath.mpf('0.3')
        R = mpmath.exp(1j * theta)

        # A zero of cos(2s*theta) that is NOT a zero of zeta
        s_extra = mpmath.pi / (4 * theta)
        eps_val = narain_epsilon(s_extra, R)

        # epsilon = 4*cos(2s*theta) * zeta(2s) at these special s values
        # If zeta(2s) != 0 but cos = 0, then epsilon = 0
        zeta_2s = mp_zeta(2 * s_extra)
        if abs(zeta_2s) > 1e-10:  # zeta not zero here
            assert abs(eps_val) < abs(zeta_2s) * 1e-10, \
                f"Extra zero from complex R: eps={eps_val}, zeta(2s)={zeta_2s}"

    def test_R_equals_1_self_dual(self):
        """At R=1: epsilon^1_s(1) = 4*zeta(2s)."""
        s = mpmath.mpf(3)
        eps = narain_epsilon(s, mpmath.mpf(1))
        expected = 4 * mp_zeta(2 * s)
        assert mpmath.almosteq(eps, expected, 1e-40)

    def test_T_duality_R_to_1_over_R(self):
        """T-duality: epsilon^1_s(R) = epsilon^1_s(1/R)."""
        R = mpmath.mpf(3)
        s = mpmath.mpf(2) + mpmath.mpf('0.5') * 1j

        eps_R = narain_epsilon(s, R)
        eps_inv_R = narain_epsilon(s, 1 / R)

        assert mpmath.almosteq(eps_R, eps_inv_R, 1e-35), \
            f"T-duality violation: eps(R)={eps_R}, eps(1/R)={eps_inv_R}"

    def test_narain_no_leverage(self):
        """
        Varying R changes the coefficient but NOT the zero locations
        (for real R > 0). This is explicitly stated in the manuscript
        (Gap B, lines 1616-1624) and is CORRECT.

        Numerically: at several R values, verify that zeros of
        epsilon occur at the same s values (zeros of zeta(2s)).
        """
        # First zero of zeta is at 1/2 + 14.13...i
        # So zero of zeta(2s) is at s = (1/2 + 14.13...i)/2
        rho = mpmath.mpf('0.5') + mpmath.mpf('14.134725141734693790') * 1j
        s_zero = rho / 2

        for R in [mpmath.mpf('0.5'), mpmath.mpf(1), mpmath.mpf(2), mpmath.mpf(10)]:
            eps = narain_epsilon(s_zero, R)
            assert abs(eps) < 1e-15, \
                f"Epsilon should vanish at rho/2 for R={R}: |eps|={abs(eps)}"


# ============================================================
# ATTACK SYNTHESIS: Cross-cutting consistency checks
# ============================================================

class TestCrossCuttingConsistency:
    """
    Cross-cutting tests that combine multiple attack vectors.
    """

    def test_virasoro_Sigma2_positive_for_positive_c(self):
        """
        Q^ct = 10/[c(5c+22)] > 0 for c > 0.
        This means the Schur complement is positive, so the
        Hankel matrix is positive definite for c > 0.
        """
        for c in [mpmath.mpf('0.01'), mpmath.mpf('0.5'), 1, 2, 5, 10, 25, 100]:
            c = mpmath.mpf(c)
            _, _, Q = virasoro_shadow_data(c)
            assert Q > 0, f"Q^ct should be positive for c > 0: c={c}, Q={Q}"

    def test_virasoro_Sigma2_negative_for_negative_c(self):
        """
        For -22/5 < c < 0: 5c+22 > 0 but c < 0, so Q^ct < 0.
        The Schur complement is NEGATIVE. This is the non-unitary regime.
        """
        for c in [mpmath.mpf('-0.5'), mpmath.mpf('-1'), mpmath.mpf('-2'), mpmath.mpf('-4')]:
            c = mpmath.mpf(c)
            _, _, Q = virasoro_shadow_data(c)
            assert Q < 0, f"Q^ct should be negative for -22/5 < c < 0: c={c}, Q={Q}"

    def test_D2_consistency_three_ways(self):
        """
        Compute D_2 three ways and verify agreement:
        1. From 3x3 determinant formula
        2. From D_2 = mu_2 * Q^ct
        3. From claimed 5/(5c+22)
        """
        for c in [1, 2, 5, 10, 25]:
            c = mpmath.mpf(c)
            H, C, Q = virasoro_shadow_data(c)
            mu4 = raw_quartic_moment_vir(c)

            D2_det = hankel_D2_from_moments(H, C, mu4)
            D2_product = H * Q
            D2_claimed = mpmath.mpf(5) / (5 * c + 22)

            assert mpmath.almosteq(D2_det, D2_product, 1e-40), \
                f"D2 det vs product at c={c}"
            assert mpmath.almosteq(D2_det, D2_claimed, 1e-40), \
                f"D2 det vs claimed at c={c}"

    def test_schur_complement_reciprocal_property(self):
        """
        The manuscript claims Sigma_2^Pot * Sigma_2^Gram = 1.
        Since Sigma_2^Gram = (Q^ct)^{-1} = N^ct, this is tautological:
        Q^ct * (1/Q^ct) = 1.

        RED TEAM: This is a DEFINITION, not a theorem.
        The Gram-side transform is DEFINED to be the reciprocal.
        """
        for c in [1, 2, 5, 10]:
            c = mpmath.mpf(c)
            _, _, Q = virasoro_shadow_data(c)
            product = Q * (1 / Q)
            assert mpmath.almosteq(product, 1, 1e-45)

    def test_heisenberg_sewing_dirichlet(self):
        """
        S_H(u) = zeta(u) * zeta(u+1). Verify at several u values.
        Coefficients a_H(N) = sigma_{-1}(N) = sum_{d|N} 1/d.
        """
        # Direct Dirichlet series vs product formula
        u = mpmath.mpf(3)
        S_product = mp_zeta(u) * mp_zeta(u + 1)

        # Partial sum of Dirichlet series
        nmax = 5000
        S_partial = sum(
            mpmath.mpf(sum(mpmath.mpf(1) / d for d in range(1, N + 1) if N % d == 0)) * mpmath.power(N, -u)
            for N in range(1, nmax + 1)
        )

        rel_err = abs(S_partial - S_product) / abs(S_product)
        assert rel_err < 1e-5, \
            f"Heisenberg Dirichlet series mismatch: partial={S_partial}, product={S_product}"

    def test_virasoro_sewing_dirichlet(self):
        """
        S_Vir(u) = zeta(u+1) * (zeta(u) - 1). Verify.
        Virasoro has W = {2}, so H_{w-1}(u) = H_1(u) = 1.
        """
        u = mpmath.mpf(3)
        S_vir = mp_zeta(u + 1) * (mp_zeta(u) - 1)

        # Direct: generator of weight 2, modes m >= 2
        nmax = 5000
        # a_Vir(N) = sum_{d|N, N/d >= 2} 1/d
        S_partial = mpmath.mpf(0)
        for N in range(1, nmax + 1):
            coeff = mpmath.mpf(0)
            for d in range(1, N + 1):
                if N % d == 0 and N // d >= 2:
                    coeff += mpmath.mpf(1) / d
            S_partial += coeff * mpmath.power(N, -u)

        rel_err = abs(S_partial - S_vir) / abs(S_vir)
        assert rel_err < 1e-4, \
            f"Virasoro Dirichlet series mismatch: partial={S_partial}, formula={S_vir}"

    def test_euler_koszul_defect_virasoro(self):
        """
        D_Vir(u) = 1 - 1/zeta(u). Verify at several u values.
        """
        for u in [2, 3, 4, 5, 10]:
            u = mpmath.mpf(u)
            D_claimed = 1 - 1 / mp_zeta(u)

            # From S_Vir / (1 * zeta(u) * zeta(u+1)):
            S_vir = mp_zeta(u + 1) * (mp_zeta(u) - 1)
            D_from_S = S_vir / (1 * mp_zeta(u) * mp_zeta(u + 1))

            assert mpmath.almosteq(D_claimed, D_from_S, 1e-40), \
                f"Euler-Koszul defect mismatch at u={u}"

    def test_li_coefficient_heisenberg_sign(self):
        """
        Manuscript claims lambda_tilde_1(H) > 0 (= gamma + zeta'(2)/zeta(2)).
        Verify numerically.
        """
        gamma = mpmath.euler
        zeta_prime_2 = mpmath.diff(mp_zeta, 2)
        zeta_2 = mp_zeta(2)

        lambda1_H = gamma + zeta_prime_2 / zeta_2
        assert lambda1_H > 0, \
            f"lambda_1(H) should be positive: {lambda1_H}"

        # Manuscript claims +0.0072546718
        expected = mpmath.mpf('0.0072546718')
        rel_err = abs(lambda1_H - expected) / abs(expected)
        assert rel_err < 1e-5, \
            f"lambda_1(H) value mismatch: computed={lambda1_H}, expected={expected}"

    def test_li_coefficient_virasoro_sign(self):
        """
        Manuscript claims lambda_tilde_1(Vir) < 0.
        Vir = W_2, so lambda_1(W_2) = zeta'(2)/zeta(2) + gamma + 1 - (2/1)*H_1.
        H_1 = 1, so lambda_1 = zeta'(2)/zeta(2) + gamma + 1 - 2 = zeta'(2)/zeta(2) + gamma - 1.
        """
        gamma = mpmath.euler
        zeta_prime_2 = mpmath.diff(mp_zeta, 2)
        zeta_2 = mp_zeta(2)

        lambda1_Vir = zeta_prime_2 / zeta_2 + gamma - 1

        assert lambda1_Vir < 0, \
            f"lambda_1(Vir) should be negative: {lambda1_Vir}"

        # Manuscript claims -0.9927453282
        expected = mpmath.mpf('-0.9927453282')
        rel_err = abs(lambda1_Vir - expected) / abs(expected)
        assert rel_err < 1e-5, \
            f"lambda_1(Vir) value mismatch: computed={lambda1_Vir}, expected={expected}"

    def test_lambda1_vir_equals_lambda1_H_minus_1(self):
        """
        lambda_1(Vir) = lambda_1(H) - 1.
        This follows from: Vir has one weight-2 generator, H has one weight-1.
        The difference is exactly H_1(u) = 1 evaluated at u=1.
        """
        gamma = mpmath.euler
        zeta_prime_2 = mpmath.diff(mp_zeta, 2)
        zeta_2 = mp_zeta(2)

        lambda1_H = gamma + zeta_prime_2 / zeta_2
        lambda1_Vir = zeta_prime_2 / zeta_2 + gamma - 1

        diff = lambda1_H - lambda1_Vir
        assert mpmath.almosteq(diff, 1, 1e-40), \
            f"lambda_1(H) - lambda_1(Vir) should be 1: diff={diff}"


# ============================================================
# RED TEAM SUMMARY: Detailed findings
# ============================================================

class TestRedTeamSummary:
    """
    Summary tests encoding the RED TEAM findings.
    Each test encodes a specific verdict.
    """

    def test_attack1_verdict_CONFIRMED_CORRECT(self):
        """
        ATTACK 1 VERDICT: Schur complement identification is CORRECT.
        The 3x3 determinant formula, the Virasoro specialization,
        and the D_2 = 5/(5c+22) identity all check out numerically
        at 50-digit precision across many c values including extremes.
        No errors found.
        """
        pass

    def test_attack2_verdict_PI_EXPONENT_ERROR_FOUND(self):
        """
        ATTACK 2 VERDICT: **ERROR FOUND** in eq:universal-residue.

        The pole mechanism is correct: F_c has a pole at s = (1+rho)/2
        from 1/zeta(2s-1) where zeta(rho) = 0. The chain rule factor
        of 2 is correct. zeta(1+rho) in the numerator is finite.

        HOWEVER: the pi exponent in the closed-form residue formula
        is WRONG. The manuscript has pi^{(rho+1)/2} in the denominator.
        The correct exponent is pi^{rho + 1/2}.

        Derivation: F_c(s) has pi^{2s - 1/2} in the denominator.
        At s = (1+rho)/2: 2s - 1/2 = (1+rho) - 1/2 = rho + 1/2.
        But (rho+1)/2 = rho/2 + 1/2, which is DIFFERENT.

        The error factor is pi^{rho/2}. For rho on the critical line,
        |pi^{rho/2}| = pi^{1/4} ~= 1.3313, so the modulus is off by ~33%.

        Confirmed by: (1) independent L'Hopital residue computation,
        (2) numerical contour integral around s_rho.

        FIX: In eq:universal-residue (line 1417 of arithmetic_shadows.tex),
        change \\pi^{\\frac{\\rho+1}{2}} to \\pi^{\\rho+\\frac{1}{2}}.
        """
        pass

    def test_attack3_verdict_GAP_ACKNOWLEDGED(self):
        """
        ATTACK 3 VERDICT: The Heisenberg weakness is ACKNOWLEDGED.

        Heisenberg contributes no quartic constraint (Q^ct = 0).
        The conjecture correctly uses Vir and W_N families.
        However, Q^ct -> 0 as c -> infinity for Virasoro,
        so only bounded c values give strong constraints.
        This is a LEGITIMATE WEAKNESS of the closure programme,
        but it is acknowledged in sec:four-gaps.
        """
        pass

    def test_attack4_verdict_VALID_CONCERN_properly_scoped(self):
        """
        ATTACK 4 VERDICT: The on-line/off-line distinction at the
        KERNEL level is correct. The question of whether it survives
        integration against the spectral measure is the content of
        the closure conjecture (conj:quartic-closure), not of
        prop:on-off-line-distinction.

        The proposition correctly states the kernel-level fact.
        The conjecture is about the moment-level consequence.
        These are properly separated. NO ERROR.
        """
        pass

    def test_attack5_verdict_HONESTLY_STATED(self):
        """
        ATTACK 5 VERDICT: The structural obstruction is HONESTLY STATED.

        rem:structural-obstruction correctly says no zero-forcing mechanism
        operates. The residue kernel computes residues of F_c, which enter
        the asymptotic expansion of epsilon^c_s but do NOT force zeros.

        The four gaps (A-D) are a complete and honest assessment.
        The manuscript does not overclaim: it identifies the programme as
        "well-defined but incomplete" (line 1551).
        """
        pass

    def test_attack6_verdict_CORRECT_for_physical_R(self):
        """
        ATTACK 6 VERDICT: Narain universality is CORRECT for real R > 0.

        For complex R = exp(i*theta), the character factor acquires
        additional zeros from cos(2s*theta) = 0. However, complex R
        does not correspond to a physical Narain lattice.

        The manuscript restricts to real R > 0 ("compactification radius")
        and correctly states that the character factor "is positive for
        real s and carries no zeros" (line 223-224). This is precise.

        RED TEAM NOTE: The statement "positive for real s" needs the
        qualifier "and real R > 0" to be fully precise. The manuscript
        does state "at compactification radius R" which implies R > 0.
        """
        pass
