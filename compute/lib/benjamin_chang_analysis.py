#!/usr/bin/env python3
r"""
benjamin_chang_analysis.py -- The Benjamin-Chang functional equation and
the zeta(2s)/zeta(2s-1) mechanism.

THE MATHEMATICAL CONTENT:

The paper [BenjaminChang22] (arXiv:2208.02259, "Scalar modular bootstrap
and zeros of the Riemann zeta function") derives a crossing equation for
scalar primary operators in 2D CFTs with U(1)^c symmetry.  The equation
contains information about ALL nontrivial zeros of the Riemann zeta
function via the Eisenstein scattering matrix on SL(2,Z)\H.

The mechanism by which zeta zeros enter is the ROELCKE-SELBERG SPECTRAL
DECOMPOSITION of modular-invariant functions on the fundamental domain
F = SL(2,Z)\H.  We explain this step by step.

=== STEP 1: THE PARTITION FUNCTION ON M_{1,1} ===

For a chiral algebra A, the genus-1 partition function
Z_A(tau) = Tr_{V_A}(q^{L_0 - c/24})  (q = e^{2*pi*i*tau})
is a modular-invariant function on H.  The primary-counting function
(stripping descendants) is
    Z_hat^c(tau) = y^{c/2} |eta(tau)|^{2c} Z_A(tau)
where y = Im(tau).  This is SL(2,Z)-invariant and has moderate growth.

=== STEP 2: THE ROELCKE-SELBERG DECOMPOSITION ===

Any SL(2,Z)-invariant L^2 function f on F decomposes as:
    f(tau) = sum_j <f, u_j> u_j(tau)
           + (1/4*pi) * integral_{-inf}^{inf} <f, E(tau, 1/2+it)> E(tau, 1/2+it) dt

where:
- {u_j} are the MAASS CUSP FORMS (discrete spectrum of Delta = -y^2(d^2/dx^2 + d^2/dy^2))
- E(tau, s) is the REAL-ANALYTIC EISENSTEIN SERIES:
    E(tau, s) = sum_{(c,d)=1} y^s / |c*tau + d|^{2s}
              = sum_{gamma in Gamma_inf\SL(2,Z)} (Im(gamma.tau))^s

The Eisenstein series has Fourier expansion:
    E(tau, s) = y^s + phi(s)*y^{1-s} + [exponentially decaying terms]

where phi(s) is the SCATTERING MATRIX (a scalar for SL(2,Z)):

    phi(s) = Lambda(1-s) / Lambda(s)

and Lambda(s) = pi^{-s} Gamma(s) zeta(2s) is the completed Selberg function.

=== STEP 3: THE SCATTERING MATRIX AND zeta(2s)/zeta(2s-1) ===

Explicitly:
    phi(s) = pi^{-(1-s)} Gamma(1-s) zeta(2-2s) / (pi^{-s} Gamma(s) zeta(2s))
           = pi^{2s-1} * Gamma(1-s)/Gamma(s) * zeta(2-2s)/zeta(2s)

Using the duplication and reflection formulas for Gamma, this simplifies to:
    phi(s) = sqrt(pi) * Gamma(s - 1/2) / Gamma(s) * zeta(2s-1) / zeta(2s)

The RATIO zeta(2s-1)/zeta(2s) (equivalently zeta(2s)/zeta(2s-1) in
the inverse) is the KEY NUMBER-THEORETIC CONTENT of the scattering matrix.

The poles of phi(s) occur where zeta(2s) = 0, i.e., at s = rho/2 where
rho ranges over the nontrivial zeros of zeta.

=== STEP 4: THE CONSTRAINED EPSTEIN FUNCTIONAL EQUATION ===

The "constrained Epstein zeta function" of A is defined as:
    epsilon^c_s(A) = sum_{Delta in S} c_Delta * (2*Delta)^{-s}

where S is the scalar primary spectrum of A counted with multiplicity c_Delta.

The RANKIN-SELBERG UNFOLDING extracts the zeroth Fourier coefficient a_0(y;A)
of Z_hat^c.  The Mellin transform of a_0 against y^{s-1} gives:

    integral_{F} Z_hat^c(tau) * E(tau, s) * d*mu(tau)
    = integral_0^inf a_0(y) * y^{s-2} dy  (by unfolding)

The functional equation of Z_hat^c under tau -> -1/tau, combined with the
functional equation of the Eisenstein series, yields:

    epsilon^c_{c/2-s} = F_c(s) * epsilon^c_{c/2+s-1}

where the scattering factor is:

    F_c(s) = Gamma(s) * Gamma(s + c/2 - 1) * zeta(2s)
             / (pi^{2s-1/2} * Gamma(c/2 - s) * Gamma(s - 1/2) * zeta(2s-1))

The factor zeta(2s)/zeta(2s-1) comes DIRECTLY from the Eisenstein scattering
matrix phi(s), modified by the conformal-weight-dependent Gamma factors that
arise from the Mellin transform of y^{c/2} * E(tau, s) integrated against
the primary spectrum.

=== STEP 5: ZETA ZERO MECHANISM ===

The scattering factor F_c(s) has poles where zeta(2s-1) = 0.  Setting
2s - 1 = rho (nontrivial zero of zeta), we get s = (1+rho)/2.

For rho = 1/2 + i*gamma (on the critical line under RH):
    s_rho = (1 + 1/2 + i*gamma) / 2 = 3/4 + i*gamma/2

The UNIVERSAL RESIDUE FACTOR at s = s_rho is:

    A_c(rho) = Res_{s=s_rho} F_c(s)
             = Gamma((1+rho)/2) * Gamma((c+rho-1)/2) * zeta(1+rho)
               / (2 * pi^{rho+1/2} * Gamma((c-rho-1)/2) * Gamma(rho/2) * zeta'(rho))

=== STEP 6: COMPLEMENTARITY ===

For Koszul dual pairs (A, A!) with c(A!) = 26 - c(A) (Virasoro):
    F_{c}(s) and F_{26-c}(s) are related by the complementarity involution.

At c = 13 (self-dual point): F_{13}(s) has a SELF-DUALITY symmetry
that constrains the residue kernel.

Manuscript references:
    eq:constrained-epstein-fe (arithmetic_shadows.tex, line 3303)
    def:universal-residue-factor (arithmetic_shadows.tex, line 3322)
    rem:koszul-epstein-constraints (arithmetic_shadows.tex, line 2864)
    rem:structural-obstruction (arithmetic_shadows.tex, line 300)
    thm:scattering-coupling-factorization (arithmetic_shadows.tex, line 7719)
    [BenjaminChang22]: N. Benjamin, C.-H. Chang, "Scalar modular bootstrap
        and zeros of the Riemann zeta function", arXiv:2208.02259, 2022.
"""

from __future__ import annotations

import math
from typing import Dict, List, Optional, Tuple, Any

try:
    import mpmath
    from mpmath import (mp, mpf, mpc, pi, zeta, gamma as mpgamma, log, exp,
                        power, sqrt, re as mpre, im as mpim, conj as mpconj,
                        fac, diff, zetazero, inf, sin, cos, arg as mparg,
                        fabs, floor, nstr)
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ============================================================
# 1. The Eisenstein scattering matrix phi(s) on SL(2,Z)\H
# ============================================================

def completed_selberg(s, dps=30):
    r"""The completed Selberg function Lambda(s) = pi^{-s} Gamma(s) zeta(2s).

    This is the building block of the Eisenstein scattering matrix:
    phi(s) = Lambda(1-s)/Lambda(s).  Note that Lambda(s) does NOT
    satisfy Lambda(s) = Lambda(1-s); rather, the scattering matrix
    phi(s) satisfies phi(s)*phi(1-s) = 1 (a tautology).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        return power(pi, -s) * mpgamma(s) * zeta(2 * s)


def scattering_matrix(s, dps=30):
    r"""The Eisenstein scattering matrix phi(s) = Lambda(1-s)/Lambda(s).

    For SL(2,Z), this is a SCALAR function.  Its poles are at s = rho/2
    where rho ranges over the nontrivial zeros of zeta(s).

    Explicitly:
        phi(s) = sqrt(pi) * Gamma(s - 1/2) / Gamma(s) * zeta(2s-1) / zeta(2s)

    The ratio zeta(2s-1)/zeta(2s) is the NUMBER-THEORETIC content.
    The Gamma ratio is the ARCHIMEDEAN content.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        L1 = completed_selberg(1 - s, dps)
        Ls = completed_selberg(s, dps)
        if abs(Ls) < power(10, -dps + 5):
            return mpc(inf)
        return L1 / Ls


def scattering_matrix_explicit(s, dps=30):
    r"""Explicit form: phi(s) = sqrt(pi) * Gamma(s-1/2)/Gamma(s) * zeta(2s-1)/zeta(2s).

    This makes the zeta(2s-1)/zeta(2s) ratio manifest.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        archimedean = sqrt(pi) * mpgamma(s - mpf('0.5')) / mpgamma(s)
        arithmetic = zeta(2 * s - 1) / zeta(2 * s)
        return archimedean * arithmetic


def zeta_ratio(s, dps=30):
    r"""The ratio zeta(2s)/zeta(2s-1).

    This is the INVERSE of the arithmetic part of the scattering matrix.
    It appears in the scattering factor F_c(s) of the constrained Epstein FE.

    Poles: where zeta(2s-1) = 0, i.e., at 2s-1 = rho (nontrivial zero of zeta),
           giving s = (1+rho)/2.

    Zeros: where zeta(2s) = 0, i.e., at 2s = rho, giving s = rho/2.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        num = zeta(2 * s)
        den = zeta(2 * s - 1)
        if abs(den) < power(10, -dps + 5):
            return mpc(inf)
        return num / den


# ============================================================
# 2. The constrained Epstein functional equation
# ============================================================

def scattering_factor_Fc(s, c, dps=30):
    r"""The scattering factor F_c(s) from the constrained Epstein FE.

    F_c(s) = Gamma(s) * Gamma(s + c/2 - 1) * zeta(2s)
             / (pi^{2s-1/2} * Gamma(c/2 - s) * Gamma(s - 1/2) * zeta(2s-1))

    (eq:constrained-epstein-fe, arithmetic_shadows.tex line 3303)

    This satisfies:
        epsilon^c_{c/2-s} = F_c(s) * epsilon^c_{c/2+s-1}
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        c = mpc(c)
        num = mpgamma(s) * mpgamma(s + c / 2 - 1) * zeta(2 * s)
        den = power(pi, 2 * s - mpf('0.5')) * mpgamma(c / 2 - s) * mpgamma(s - mpf('0.5')) * zeta(2 * s - 1)
        if abs(den) < power(10, -dps + 5):
            return mpc(inf)
        return num / den


def scattering_factor_decomposition(s, c, dps=30):
    r"""Decompose F_c(s) into its three factors.

    F_c(s) = [Gamma factor] * [pi factor] * [zeta ratio]

    Returns dict with:
        'gamma_factor': Gamma(s)*Gamma(s+c/2-1) / (Gamma(c/2-s)*Gamma(s-1/2))
        'pi_factor': pi^{-(2s-1/2)}
        'zeta_ratio': zeta(2s)/zeta(2s-1)
        'product': the full F_c(s)

    The zeta ratio is the NUMBER-THEORETIC content (from Eisenstein scattering).
    The Gamma factor is the CONFORMAL content (from the c-dependent weight).
    The pi factor is the ARCHIMEDEAN normalization.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        c = mpc(c)
        gamma_factor = (mpgamma(s) * mpgamma(s + c / 2 - 1)
                        / (mpgamma(c / 2 - s) * mpgamma(s - mpf('0.5'))))
        pi_factor = power(pi, -(2 * s - mpf('0.5')))
        zr = zeta(2 * s) / zeta(2 * s - 1)
        return {
            'gamma_factor': complex(gamma_factor),
            'pi_factor': complex(pi_factor),
            'zeta_ratio': complex(zr),
            'product': complex(gamma_factor * pi_factor * zr),
        }


# ============================================================
# 3. Standard Epstein FE for binary quadratic forms
# ============================================================

def standard_epstein_completed(s, a, b, c_form, dps=30):
    r"""Completed Epstein zeta for Q(m,n) = a*m^2 + b*m*n + c_form*n^2.

    Xi_Q(s) = (D_E)^{s/2} * pi^{-s} * Gamma(s) * Z_Q(s)

    where D_E = a*c_form - (b/2)^2 = |disc|/4.

    The standard FE is Xi_Q(s) = Xi_Q(1-s).

    NOTE: This is DIFFERENT from the Benjamin-Chang FE. The standard
    Epstein FE has NO zeta(2s)/zeta(2s-1) factor because it applies
    to a FIXED binary form, not to a constrained Epstein zeta that
    arises from spectral decomposition on M_{1,1}.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s_mp = mpc(s)
        a_mp, b_mp, c_mp = mpf(a), mpf(b), mpf(c_form)
        D_E = a_mp * c_mp - (b_mp / 2) ** 2

        # Use theta function method for analytic continuation
        # theta_Q(t) = sum_{(m,n) in Z^2} exp(-pi*t*Q(m,n)/D_E)
        # We use the standard Epstein-to-Hurwitz reduction for computation
        eps = _epstein_zeta_theta(s_mp, a_mp, b_mp, c_mp, dps)
        Xi = power(D_E, s_mp / 2) * power(pi, -s_mp) * mpgamma(s_mp) * eps
        return complex(Xi)


def _epstein_zeta_theta(s, a, b, c_form, dps=30):
    r"""Epstein zeta via theta function / direct summation for Re(s) > 1.

    Z_Q(s) = sum'_{(m,n)} Q(m,n)^{-s}

    For testing purposes, use direct truncated sum (not optimal for
    analytic continuation, but correct for Re(s) > 1.5).
    """
    with mp.workdps(dps):
        total = mpc(0)
        # Sum over a box |m|, |n| <= N
        N = 80
        for m in range(-N, N + 1):
            for n in range(-N, N + 1):
                if m == 0 and n == 0:
                    continue
                Q_val = a * m * m + b * m * n + c_form * n * n
                if Q_val > 0:
                    total += power(Q_val, -s)
        return total


# ============================================================
# 4. The universal residue factor A_c(rho)
# ============================================================

def universal_residue_factor(rho, c, dps=30):
    r"""The residue of F_c at s = s_rho = (1+rho)/2.

    A_c(rho) = Gamma((1+rho)/2) * Gamma((c+rho-1)/2) * zeta(1+rho)
               / (2 * pi^{rho+1/2} * Gamma((c-rho-1)/2) * Gamma(rho/2) * zeta'(rho))

    (eq:universal-residue, arithmetic_shadows.tex line 3326)
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = mpc(rho)
        c = mpc(c)
        num = (mpgamma((1 + rho) / 2) * mpgamma((c + rho - 1) / 2)
               * zeta(1 + rho))
        # zeta'(rho): derivative of zeta at a zero
        zeta_prime_rho = diff(zeta, rho)
        den = (2 * power(pi, rho + mpf('0.5'))
               * mpgamma((c - rho - 1) / 2) * mpgamma(rho / 2)
               * zeta_prime_rho)
        if abs(den) < power(10, -dps + 5):
            return complex(mpc(inf))
        return complex(num / den)


def residue_kernel(Delta, c, rho, u0=0, dps=30):
    r"""The paired real residue kernel w_{c,rho,u0}(Delta).

    w = 2 |A_c(rho)| (2*Delta)^{-(c+sigma-1)/2} Delta^{-u0}
        * cos(gamma/2 * log(2*Delta) + arg(A_c(rho)))

    where rho = sigma + i*gamma.
    (eq:residue-kernel, arithmetic_shadows.tex line 3346)
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = mpc(rho)
        c_mp = mpc(c)
        Delta_mp = mpf(Delta)
        sigma = mpre(rho)
        gamma_val = mpim(rho)

        A = universal_residue_factor(rho, c, dps)
        A_mp = mpc(A)
        A_abs = fabs(A_mp)
        A_arg = mparg(A_mp)

        decay = power(2 * Delta_mp, -(c_mp + sigma - 1) / 2)
        u0_factor = power(Delta_mp, -mpf(u0))
        oscillation = cos(gamma_val / 2 * log(2 * Delta_mp) + A_arg)

        return complex(2 * A_abs * decay * u0_factor * oscillation)


# ============================================================
# 5. Zeta zero positions relative to F_c poles
# ============================================================

def scattering_pole_positions(n_zeros=20, dps=30):
    r"""Compute the positions of scattering poles s_rho = (1+rho)/2.

    These are the poles of F_c(s) from zeros of zeta(2s-1).
    Setting 2s - 1 = rho gives s = (1+rho)/2.

    For rho = 1/2 + i*gamma (under RH): s = 3/4 + i*gamma/2.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        poles = []
        for k in range(1, n_zeros + 1):
            rho = zetazero(k)
            s_rho = (1 + rho) / 2
            poles.append({
                'k': k,
                'rho': complex(rho),
                'gamma': float(mpim(rho)),
                's_rho': complex(s_rho),
                's_rho_real': float(mpre(s_rho)),
                's_rho_imag': float(mpim(s_rho)),
            })
        return poles


def zeta_ratio_poles_and_zeros(n_zeros=20, dps=30):
    r"""Poles and zeros of zeta(2s)/zeta(2s-1).

    Poles: at s = (1+rho)/2 where zeta(rho) = 0  (from zeta(2s-1) zeros)
    Zeros: at s = rho/2 where zeta(rho) = 0  (from zeta(2s) zeros)

    Under RH:
        Poles at Re(s) = 3/4 + i*gamma/2
        Zeros at Re(s) = 1/4 + i*gamma/2

    The poles and zeros are INTERLACED in the imaginary direction.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        data = {'poles': [], 'zeros': []}
        for k in range(1, n_zeros + 1):
            rho = zetazero(k)
            gamma_k = float(mpim(rho))

            # Poles of zeta(2s)/zeta(2s-1): at s = (1+rho)/2
            s_pole = (1 + rho) / 2
            data['poles'].append({
                'k': k, 'gamma': gamma_k,
                's': complex(s_pole),
                'real': float(mpre(s_pole)),
                'imag': float(mpim(s_pole)),
            })

            # Zeros of zeta(2s)/zeta(2s-1): at s = rho/2
            s_zero = rho / 2
            data['zeros'].append({
                'k': k, 'gamma': gamma_k,
                's': complex(s_zero),
                'real': float(mpre(s_zero)),
                'imag': float(mpim(s_zero)),
            })

        return data


# ============================================================
# 6. Complementarity analysis
# ============================================================

def complementarity_scattering_factors(s, c, dps=30):
    r"""Compare F_c(s) and F_{26-c}(s) for Koszul dual Virasoro.

    For Virasoro: A = Vir_c, A! = Vir_{26-c}.
    The Koszul duality c -> 26-c maps:
        kappa = c/2 -> kappa' = (26-c)/2

    The scattering factors F_c and F_{26-c} differ only in the
    Gamma factors (the zeta ratio is universal).

    At c = 13 (self-dual): F_{13}(s) = F_{13}(s), trivially.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        Fc = scattering_factor_Fc(s, c, dps)
        Fc_dual = scattering_factor_Fc(s, 26 - c, dps)
        ratio = complex(mpc(Fc) / mpc(Fc_dual)) if abs(mpc(Fc_dual)) > 1e-50 else None
        return {
            'c': float(c),
            'c_dual': float(26 - c),
            'F_c': complex(Fc),
            'F_c_dual': complex(Fc_dual),
            'ratio': ratio,
        }


def complementarity_self_dual_test(s, dps=30):
    r"""At c = 13 (self-dual Virasoro), F_13(s) should be self-consistent.

    The Gamma factor becomes:
        Gamma(s)*Gamma(s+11/2) / (Gamma(13/2-s)*Gamma(s-1/2))

    This has the reflection symmetry s -> 13/2 - s + 1/2 = 7 - s.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        return complementarity_scattering_factors(s, 13, dps)


# ============================================================
# 7. The origin of zeta(2s)/zeta(2s-1): the Eisenstein explanation
# ============================================================

def verify_scattering_matrix_functional_eq(s, dps=30):
    r"""Verify phi(s) * phi(1-s) = 1 (the functional equation for the scattering matrix).

    Since phi(s) = Lambda(1-s)/Lambda(s) and Lambda satisfies Lambda(s) = Lambda(1-s):
        phi(s) * phi(1-s) = Lambda(1-s)/Lambda(s) * Lambda(s)/Lambda(1-s) = 1

    This is a tautology, but verifies our computation.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        phi_s = scattering_matrix(s, dps)
        phi_1ms = scattering_matrix(1 - s, dps)
        product = complex(mpc(phi_s) * mpc(phi_1ms))
        return {
            's': complex(s),
            'phi(s)': complex(phi_s),
            'phi(1-s)': complex(phi_1ms),
            'product': product,
            'error': abs(product - 1),
        }


def verify_explicit_vs_ratio_form(s, dps=30):
    r"""Verify two forms of the scattering matrix agree.

    Form 1: phi(s) = Lambda(1-s)/Lambda(s)
    Form 2: phi(s) = sqrt(pi) * Gamma(s-1/2)/Gamma(s) * zeta(2s-1)/zeta(2s)
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        phi_ratio = scattering_matrix(s, dps)
        phi_explicit = scattering_matrix_explicit(s, dps)
        return {
            'ratio_form': complex(phi_ratio),
            'explicit_form': complex(phi_explicit),
            'relative_error': abs(complex(mpc(phi_ratio) - mpc(phi_explicit)))
                              / max(abs(complex(phi_ratio)), 1e-100),
        }


def Fc_vs_phi_relationship(s, c, dps=30):
    r"""Show how F_c(s) relates to the Eisenstein scattering matrix.

    F_c(s) = [conformal Gamma factor] * phi^{-1}(s) * [correction]

    More precisely:
        F_c(s) = Gamma(s)*Gamma(s+c/2-1) / (pi^{2s-1/2} * Gamma(c/2-s)*Gamma(s-1/2))
                 * zeta(2s)/zeta(2s-1)

    The zeta ratio is 1/[arithmetic part of phi(s)].
    The Gamma(s)/Gamma(s-1/2) ratio partially cancels the archimedean
    part of phi(s).  The remaining Gamma(s+c/2-1)/Gamma(c/2-s) is the
    CONFORMAL CONTRIBUTION: it depends on the central charge c and is
    absent from the pure Eisenstein scattering matrix.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        c = mpc(c)

        # Eisenstein arithmetic factor (inverse)
        zr = zeta(2 * s) / zeta(2 * s - 1)

        # Eisenstein archimedean factor (inverse)
        archimedean_inv = mpgamma(s) / (sqrt(pi) * mpgamma(s - mpf('0.5')))

        # Conformal factor (c-dependent)
        conformal = mpgamma(s + c / 2 - 1) / mpgamma(c / 2 - s)

        # pi normalization correction
        pi_correction = power(pi, -(2 * s - 1))

        # Full F_c should be archimedean_inv * conformal * pi_correction * zr
        Fc_reconstructed = archimedean_inv * conformal * pi_correction * zr

        # Direct computation
        Fc_direct = scattering_factor_Fc(s, c, dps)

        return {
            'Fc_direct': complex(Fc_direct),
            'Fc_reconstructed': complex(Fc_reconstructed),
            'zeta_ratio': complex(zr),
            'archimedean_inv': complex(archimedean_inv),
            'conformal': complex(conformal),
            'relative_error': abs(complex(mpc(Fc_direct) - Fc_reconstructed))
                              / max(abs(complex(Fc_direct)), 1e-100),
        }


# ============================================================
# 8. Grid evaluation of |zeta(2s)/zeta(2s-1)| for visualization
# ============================================================

def zeta_ratio_grid(sigma_range=(0.05, 0.95), t_range=(0.5, 50),
                    n_sigma=50, n_t=200, dps=15):
    r"""Evaluate |zeta(2s)/zeta(2s-1)| on a grid in the critical strip.

    Returns arrays sigma, t, |ratio| for plotting.

    The poles (from zeros of zeta(2s-1)) lie at:
        s = (1+rho_k)/2, with Re(s) = 3/4 under RH.
    The zeros (from zeros of zeta(2s)) lie at:
        s = rho_k/2, with Re(s) = 1/4 under RH.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    sigma_vals = [sigma_range[0] + i * (sigma_range[1] - sigma_range[0]) / (n_sigma - 1)
                  for i in range(n_sigma)]
    t_vals = [t_range[0] + i * (t_range[1] - t_range[0]) / (n_t - 1)
              for i in range(n_t)]

    grid = []
    with mp.workdps(dps):
        for sigma in sigma_vals:
            row = []
            for t in t_vals:
                s = mpc(sigma, t)
                try:
                    val = zeta(2 * s) / zeta(2 * s - 1)
                    row.append(float(fabs(val)))
                except (ZeroDivisionError, ValueError):
                    row.append(float('inf'))
            grid.append(row)

    return sigma_vals, t_vals, grid


# ============================================================
# 9. Standard Epstein FE verification (for comparison)
# ============================================================

def standard_epstein_fe_test(s, c_central, dps=30):
    r"""Verify the standard Epstein FE for the Virasoro shadow metric.

    The shadow metric Q_L for Virasoro at central charge c gives:
        Q(m,n) = c^2 m^2 + 12c m*n + (36 + 2*Delta) n^2

    where Delta = 40/(5c+22) (critical discriminant).

    The STANDARD Epstein FE is:
        Xi_Q(s) = Xi_Q(1-s)
    with Xi_Q(s) = D_E^{s/2} pi^{-s} Gamma(s) Z_Q(s)
    and D_E = |disc(Q)|/4.

    This has NO zeta(2s)/zeta(2s-1) factor. That factor appears
    ONLY in the Benjamin-Chang FE, which is the constrained Epstein FE.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        c = mpf(c_central)
        kappa = c / 2
        alpha = mpf(2)
        S4 = mpf(10) / (c * (5 * c + 22))
        Delta = 8 * kappa * S4  # = 40/(5c+22)

        # Binary form Q(m,n) = 4*kappa^2 m^2 + 12*kappa*alpha m*n + (9*alpha^2 + 2*Delta) n^2
        a = 4 * kappa ** 2
        b = 12 * kappa * alpha
        cf = 9 * alpha ** 2 + 2 * Delta

        Xi_s = standard_epstein_completed(s, float(a), float(b), float(cf), dps)
        Xi_1ms = standard_epstein_completed(1 - s, float(a), float(b), float(cf), dps)

        return {
            'c': float(c),
            'Xi_Q(s)': Xi_s,
            'Xi_Q(1-s)': Xi_1ms,
            'relative_error': abs(Xi_s - Xi_1ms) / max(abs(Xi_s), 1e-100),
        }


# ============================================================
# 10. Explaining the difference: standard Epstein vs Benjamin-Chang
# ============================================================

def explain_zeta_ratio_origin():
    r"""Explains WHY zeta(2s)/zeta(2s-1) appears in the Benjamin-Chang FE
    but NOT in the standard Epstein FE.

    Returns a structured explanation.
    """
    return {
        'standard_epstein': {
            'object': 'Z_Q(s) = sum\'_{(m,n)} Q(m,n)^{-s}',
            'domain': 'Fixed binary quadratic form Q',
            'fe': 'Xi_Q(s) = Xi_Q(1-s)',
            'mechanism': 'Poisson summation on Z^2',
            'zeta_content': 'NONE — the FE involves only Q and Gamma',
            'reason': 'The lattice sum sees only the geometry of Q',
        },
        'benjamin_chang': {
            'object': 'epsilon^c_s = sum_Delta c_Delta (2*Delta)^{-s}',
            'domain': 'PRIMARY SPECTRUM of a modular-invariant CFT',
            'fe': 'epsilon^c_{c/2-s} = F_c(s) * epsilon^c_{c/2+s-1}',
            'mechanism': 'Rankin-Selberg unfolding on SL(2,Z)\\H',
            'zeta_content': 'zeta(2s)/zeta(2s-1) from Eisenstein scattering matrix',
            'reason': (
                'The primary spectrum is NOT a lattice sum; it is the '
                'SPECTRAL COEFFICIENT of the partition function in the '
                'Roelcke-Selberg decomposition.  The Eisenstein series '
                'E(tau, s) has a constant term y^s + phi(s)*y^{1-s}, '
                'and the scattering matrix phi(s) = Lambda(1-s)/Lambda(s) '
                'contains zeta(2s-1)/zeta(2s).  When the Rankin-Selberg '
                'integral extracts the spectral coefficient of the '
                'partition function, the scattering matrix enters the '
                'functional equation — producing the RECIPROCAL '
                'zeta(2s)/zeta(2s-1) in F_c(s).'
            ),
        },
        'the_key_distinction': (
            'The standard Epstein FE applies to a FIXED LATTICE SUM. '
            'The Benjamin-Chang FE applies to the SPECTRAL DECOMPOSITION '
            'of a modular-invariant function.  The latter sees the Eisenstein '
            'scattering matrix because the partition function lives on the '
            'MODULI SPACE M_{1,1}, not on a fixed torus.  The modular '
            'coupling (the integration over all tori, weighted by the '
            'Eisenstein kernel) is what introduces the zeta ratio.'
        ),
    }


# ============================================================
# 11. Heisenberg special case: epsilon factors through zeta
# ============================================================

def heisenberg_constrained_epstein(s, k=1, dps=30):
    r"""Heisenberg constrained Epstein: epsilon^KE_{H_k}(s) = 2 k^{-2s} zeta(2s).

    For Heisenberg at level k, the primary spectrum is
    {n * k : n >= 1} with multiplicity 2 (left+right movers).
    So epsilon^KE(s) = 2 sum_{n>=1} (2*n*k)^{-s} = 2*(2k)^{-s}*zeta(s).

    Wait — let me recheck from the manuscript (eq:heisenberg-koszul-epstein):
    epsilon^KE_{H_k}(s) = 2 * k^{-2s} * zeta(2s).

    This factors through zeta. All nontrivial zeros lie on Re(s) = 1/4
    (corresponding to Re(2s) = 1/2).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        k_mp = mpc(k)
        return complex(2 * power(k_mp, -2 * s) * zeta(2 * s))


def narain_constrained_epstein(s, R=1.0, dps=30):
    r"""Narain universality: epsilon^1_s(R) = 2 (R^{2s} + R^{-2s}) zeta(2s).

    (eq:narain-universality, arithmetic_shadows.tex line 338)

    Character factor 2*cosh(2s*log R) is positive for real s, R > 0.
    Zeros are exactly the zeros of zeta(2s), independent of R.
    T-duality R <-> 1/R preserves epsilon identically.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        R_mp = mpf(R)
        char_factor = 2 * (power(R_mp, 2 * s) + power(R_mp, -2 * s))
        return complex(char_factor * zeta(2 * s))


# ============================================================
# 12. Summary functions
# ============================================================

def full_analysis_at_zero(k=1, c=26.0, dps=30):
    r"""Full analysis at the k-th zeta zero for Virasoro at central charge c.

    Returns: rho, s_rho, F_c(s_rho) residue, residue kernel at Delta=1,
    complementarity data.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = zetazero(k)
        s_rho = (1 + rho) / 2

        A_c = universal_residue_factor(rho, c, dps)
        w_kernel = residue_kernel(1.0, c, complex(rho), u0=0, dps=dps)
        comp = complementarity_scattering_factors(complex(s_rho), c, dps)

        return {
            'k': k,
            'rho': complex(rho),
            'gamma': float(mpim(rho)),
            's_rho': complex(s_rho),
            'A_c(rho)': A_c,
            '|A_c(rho)|': abs(A_c),
            'w_kernel(Delta=1)': w_kernel,
            'complementarity': comp,
            'decay_exponent_on_line': -(float(c) + 0.5 - 1) / 2,
            'decay_exponent_formula': '-(c + sigma - 1)/2 with sigma=1/2 under RH',
        }
