#!/usr/bin/env python3
r"""bc_koszul_zeta_complementarity_engine.py -- Koszul duality (Theorem C)
acting on zeta zeros in the Benjamin-Chang framework.

MATHEMATICAL CONTENT
====================

Theorem C (complementarity) states:
    Q_g(A) + Q_g(A!) = H*(M-bar_g, Z(A))

For the Benjamin-Chang constrained Epstein functional equation, this has
a precise arithmetic manifestation: the scattering factors F_c(s) and
F_{26-c}(s) for a Koszul dual pair (Vir_c, Vir_{26-c}) are linked by
partial cancellation of Gamma factors, while the zeta ratio
zeta(2s)/zeta(2s-1) is UNIVERSAL (c-independent).

=== 1. COMPLEMENTARITY OF RESIDUES ===

The universal residue factor at a zeta zero rho is:

    A_c(rho) = Gamma((1+rho)/2) * Gamma((c+rho-1)/2) * zeta(1+rho)
               / (2 * pi^{rho+1/2} * Gamma((c-rho-1)/2) * Gamma(rho/2) * zeta'(rho))

The ratio A_c(rho) / A_{26-c}(rho) simplifies because the factors
    Gamma((1+rho)/2), pi^{rho+1/2}, Gamma(rho/2), zeta'(rho), zeta(1+rho)
are ALL c-independent and cancel.  What remains is:

    A_c(rho) / A_{26-c}(rho) = Gamma((c+rho-1)/2) * Gamma((26-c-rho-1)/2)
                               / (Gamma((c-rho-1)/2) * Gamma((26-c+rho-1)/2))

      = Gamma((c+rho-1)/2) * Gamma((25-c-rho)/2)
        / (Gamma((c-rho-1)/2) * Gamma((25-c+rho)/2))

This is a pure GAMMA RATIO that depends on c and rho but has NO zeta
content.  The zeta zeros enter A_c and A_{26-c} identically.

=== 2. SELF-DUAL RESIDUE (c=13) ===

At c=13 (self-dual Virasoro, kappa=13/2), the residue ratio becomes:

    A_13(rho) / A_13(rho) = 1 (trivially)

But the self-dual structure imposes a REFLECTION SYMMETRY on A_13(rho):
under the substitution rho -> 1-rho (which sends rho = 1/2+it to
rho' = 1/2-it, the conjugate zero), we get:

    A_13(1-rho) = A_13(rho) * g_13(rho)

where g_13 is a computable Gamma ratio (the "self-dual multiplier").

=== 3. DUALITY-TWISTED ZETA ===

Z^Koszul(s) = epsilon^c_s * epsilon^{26-c}_s

is the PRODUCT over the Koszul dual pair.  At each zeta zero rho,
epsilon^c has a singularity from F_c(s) and epsilon^{26-c} has one from
F_{26-c}(s).  Z^Koszul inherits contributions from BOTH, producing
DOUBLE-STRENGTH singularity structure at each zeta zero position.

=== 4. COMPLEMENTARITY L-FUNCTION ===

L^comp_c(s) = epsilon^c_s / epsilon^{26-c}_s

At c=13 this is identically 1 (self-duality).  Near c=13:

    L^comp_c(s) = 1 + (c-13) * delta_L(s) + O((c-13)^2)

where delta_L = (d/dc)|_{c=13} log(F_c(s)/F_{26-c}(s)) is the
"Koszul perturbation".  This is computed from the digamma function.

=== 5. SHADOW COMPLEMENTARITY ===

For the shadow zeta zeta_A(s) = sum_{r>=2} S_r(A) * r^{-s}:
    zeta_A(s) + zeta_{A!}(s) has the sum of shadow coefficients.

At kappa(A) + kappa(A!) = 0 (KM case): S_2(A) + S_2(A!) = 0,
so the leading term cancels.

At kappa(A) + kappa(A!) = 13 (Virasoro): S_2(A) + S_2(A!) = 13,
so the leading term is 13 * 2^{-s} -- nonvanishing.

=== 6. LAGRANGIAN STRUCTURE ===

The shifted-symplectic complementarity maps (Q_g(A), Q_g(A!)) to a
Lagrangian subspace of H*(M-bar_g, Z(A)) x H*(M-bar_g, Z(A!)).
The "zeta zero hyperplane" is the locus where the scattering factor
has a pole.  The Lagrangian intersection with this hyperplane is
computed from the complementarity Gamma ratio.

=== 7. DEFECT FORM ===

Omega_c(s) = (d/dc)(A_c(rho)) measures how the residue changes as
we deform the algebra through the Koszul family.

Manuscript references:
    thm:complementarity (higher_genus_complementarity.tex)
    eq:constrained-epstein-fe (arithmetic_shadows.tex)
    def:universal-residue-factor (arithmetic_shadows.tex)
    rem:koszul-epstein-constraints (arithmetic_shadows.tex)

CAUTION (AP1): kappa formulas are family-specific.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP29): delta_kappa = kappa - kappa' != kappa_eff.
CAUTION (AP39): kappa = c/2 for Virasoro only; NOT general.
CAUTION (AP48): kappa depends on the full algebra, not just c.
"""

from __future__ import annotations

import cmath
import math
from typing import Dict, List, Optional, Tuple, Any

try:
    import mpmath
    from mpmath import (mp, mpf, mpc, pi, zeta, gamma as mpgamma, log, exp,
                        power, sqrt, re as mpre, im as mpim, conj as mpconj,
                        fac, diff, zetazero, inf, sin, cos, arg as mparg,
                        fabs, floor, nstr, psi as mpdigamma)
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ============================================================================
# 0.  Re-export / internal helpers from benjamin_chang_analysis
# ============================================================================

def _universal_residue_factor_mp(rho, c, dps=30):
    r"""Internal mpmath version of the universal residue factor.

    A_c(rho) = Gamma((1+rho)/2) * Gamma((c+rho-1)/2) * zeta(1+rho)
               / (2 * pi^{rho+1/2} * Gamma((c-rho-1)/2) * Gamma(rho/2) * zeta'(rho))

    Returns an mpc value (stays inside mpmath context).
    """
    num = (mpgamma((1 + rho) / 2) * mpgamma((c + rho - 1) / 2)
           * zeta(1 + rho))
    zeta_prime_rho = diff(zeta, rho)
    den = (2 * power(pi, rho + mpf('0.5'))
           * mpgamma((c - rho - 1) / 2) * mpgamma(rho / 2)
           * zeta_prime_rho)
    if fabs(den) < power(10, -dps + 5):
        return mpc(inf)
    return num / den


def _scattering_factor_Fc_mp(s, c, dps=30):
    r"""Internal mpmath version of F_c(s).

    F_c(s) = Gamma(s) * Gamma(s + c/2 - 1) * zeta(2s)
             / (pi^{2s-1/2} * Gamma(c/2 - s) * Gamma(s - 1/2) * zeta(2s-1))
    """
    num = mpgamma(s) * mpgamma(s + c / 2 - 1) * zeta(2 * s)
    den = (power(pi, 2 * s - mpf('0.5'))
           * mpgamma(c / 2 - s) * mpgamma(s - mpf('0.5'))
           * zeta(2 * s - 1))
    if fabs(den) < power(10, -dps + 5):
        return mpc(inf)
    return num / den


# ============================================================================
# 1.  Complementarity of residues: A_c(rho) / A_{26-c}(rho)
# ============================================================================

def residue_complementarity_ratio(rho, c, dps=30):
    r"""Compute A_c(rho) / A_{26-c}(rho).

    The c-independent factors (Gamma((1+rho)/2), pi^{rho+1/2},
    Gamma(rho/2), zeta'(rho), zeta(1+rho)) cancel exactly.

    Result:
        Gamma((c+rho-1)/2) * Gamma((25-c-rho)/2)
        / (Gamma((c-rho-1)/2) * Gamma((25-c+rho)/2))

    Parameters
    ----------
    rho : complex
        A nontrivial zero of zeta (or any complex number).
    c : float or complex
        Central charge.  Koszul dual has central charge 26-c.
    dps : int
        Decimal precision.

    Returns
    -------
    dict with 'ratio_direct', 'ratio_gamma', 'relative_error',
    'A_c', 'A_dual'.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = mpc(rho)
        c = mpc(c)
        c_dual = 26 - c

        # Direct computation: A_c / A_{26-c}
        A_c = _universal_residue_factor_mp(rho, c, dps)
        A_dual = _universal_residue_factor_mp(rho, c_dual, dps)
        if fabs(A_dual) < power(10, -dps + 5):
            ratio_direct = mpc(inf)
        else:
            ratio_direct = A_c / A_dual

        # Gamma ratio (the c-dependent part that survives cancellation)
        # A_c / A_{26-c} = Gamma((c+rho-1)/2) * Gamma((c_dual - rho - 1)/2)
        #                  / (Gamma((c-rho-1)/2) * Gamma((c_dual + rho - 1)/2))
        num_gamma = (mpgamma((c + rho - 1) / 2)
                     * mpgamma((c_dual - rho - 1) / 2))
        den_gamma = (mpgamma((c - rho - 1) / 2)
                     * mpgamma((c_dual + rho - 1) / 2))
        if fabs(den_gamma) < power(10, -dps + 5):
            ratio_gamma = mpc(inf)
        else:
            ratio_gamma = num_gamma / den_gamma

        # Relative error between the two methods
        if fabs(ratio_direct) > power(10, -dps + 5):
            rel_err = float(fabs(ratio_direct - ratio_gamma) / fabs(ratio_direct))
        else:
            rel_err = float(fabs(ratio_direct - ratio_gamma))

        return {
            'ratio_direct': complex(ratio_direct),
            'ratio_gamma': complex(ratio_gamma),
            'relative_error': rel_err,
            'A_c': complex(A_c),
            'A_dual': complex(A_dual),
            'c': complex(c),
            'c_dual': complex(c_dual),
        }


def residue_complementarity_table(n_zeros=10, c_values=None, dps=30):
    r"""Table of A_c(rho_k) / A_{26-c}(rho_k) for multiple zeros and c-values.

    Parameters
    ----------
    n_zeros : int
        Number of zeta zeros.
    c_values : list of float, optional
        Central charges to probe.  Default: 1,2,...,25.
    dps : int

    Returns
    -------
    list of dicts, one per (c, k) pair.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    if c_values is None:
        c_values = list(range(1, 26))

    results = []
    with mp.workdps(dps):
        for k in range(1, n_zeros + 1):
            rho = zetazero(k)
            for c_val in c_values:
                entry = residue_complementarity_ratio(complex(rho), c_val, dps)
                entry['k'] = k
                entry['rho'] = complex(rho)
                entry['gamma'] = float(mpim(rho))
                results.append(entry)
    return results


def residue_ratio_modulus_spectrum(n_zeros=20, c_val=1.0, dps=30):
    r"""Compute |A_c(rho_k) / A_{26-c}(rho_k)| for the first n_zeros zeros.

    Returns a list of (k, gamma_k, |ratio|) triples.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    results = []
    with mp.workdps(dps):
        for k in range(1, n_zeros + 1):
            rho = zetazero(k)
            entry = residue_complementarity_ratio(complex(rho), c_val, dps)
            results.append({
                'k': k,
                'gamma': float(mpim(rho)),
                'ratio_modulus': abs(entry['ratio_gamma']),
                'ratio_arg': cmath.phase(entry['ratio_gamma']),
            })
    return results


# ============================================================================
# 2.  Self-dual residue at c = 13
# ============================================================================

def self_dual_residue(rho, dps=30):
    r"""Compute A_13(rho) at the self-dual point c = 13.

    A_13(rho) = Gamma((1+rho)/2) * Gamma((12+rho)/2) * zeta(1+rho)
                / (2 * pi^{rho+1/2} * Gamma((12-rho)/2) * Gamma(rho/2) * zeta'(rho))

    The self-dual multiplier g_13(rho) relates A_13(rho) to A_13(conj(rho)):

        A_13(conj(rho)) = conj(A_13(rho))  (reality condition)

    since all Gamma arguments become conjugate and zeta(1+conj(rho)) = conj(zeta(1+rho)).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = mpc(rho)
        A = _universal_residue_factor_mp(rho, 13, dps)
        return complex(A)


def self_dual_conjugation_test(rho, dps=30):
    r"""Test the conjugation property A_13(conj(rho)) = conj(A_13(rho)).

    At the self-dual point c=13, since 26-c = 13, the residue factor
    has a reflection symmetry: under rho -> conj(rho), all factors
    conjugate consistently because zeta(conj(s)) = conj(zeta(s)) and
    Gamma(conj(s)) = conj(Gamma(s)).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = mpc(rho)
        A_rho = _universal_residue_factor_mp(rho, 13, dps)
        rho_conj = mpconj(rho)
        A_rho_conj = _universal_residue_factor_mp(rho_conj, 13, dps)
        conj_A_rho = mpconj(A_rho)
        err = fabs(A_rho_conj - conj_A_rho)
        return {
            'A_13(rho)': complex(A_rho),
            'A_13(conj(rho))': complex(A_rho_conj),
            'conj(A_13(rho))': complex(conj_A_rho),
            'error': float(err),
        }


def self_dual_multiplier(rho, dps=30):
    r"""The self-dual multiplier g_13(rho) defined by:

        A_13(1 - rho) = A_13(rho) * g_13(rho)

    Since rho is a zero of zeta and (by functional equation) so is 1-rho,
    both A_13(rho) and A_13(1-rho) are defined.

    The multiplier encodes the FUNCTIONAL EQUATION of the residue:
        g_13(rho) = A_13(1-rho) / A_13(rho)
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = mpc(rho)
        A_rho = _universal_residue_factor_mp(rho, 13, dps)
        A_1mrho = _universal_residue_factor_mp(1 - rho, 13, dps)
        if fabs(A_rho) < power(10, -dps + 5):
            g = mpc(inf)
        else:
            g = A_1mrho / A_rho
        return {
            'g_13(rho)': complex(g),
            'A_13(rho)': complex(A_rho),
            'A_13(1-rho)': complex(A_1mrho),
            '|g_13|': float(fabs(g)),
        }


def self_dual_residue_spectrum(n_zeros=20, dps=30):
    r"""Spectrum of |A_13(rho_k)| and |g_13(rho_k)| for the first n_zeros zeros."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    results = []
    with mp.workdps(dps):
        for k in range(1, n_zeros + 1):
            rho = zetazero(k)
            A_val = _universal_residue_factor_mp(rho, 13, dps)
            g_data = self_dual_multiplier(complex(rho), dps)
            results.append({
                'k': k,
                'gamma': float(mpim(rho)),
                '|A_13|': float(fabs(A_val)),
                'arg_A_13': float(mparg(A_val)),
                '|g_13|': g_data['|g_13|'],
            })
    return results


# ============================================================================
# 3.  Duality-twisted zeta: Z^Koszul(s) = F_c(s) * F_{26-c}(s)
# ============================================================================

def duality_twisted_scattering(s, c, dps=30):
    r"""Compute Z^Koszul(s) = F_c(s) * F_{26-c}(s).

    The product of scattering factors for a Koszul dual pair.
    At zeta zeros rho with s = (1+rho)/2: both F_c and F_{26-c} have
    poles from zeta(2s-1) = 0, producing a DOUBLE pole.

    The zeta ratio factor is [zeta(2s)/zeta(2s-1)]^2 (squared),
    giving double zeros/poles at each zeta zero position.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        c = mpc(c)
        Fc = _scattering_factor_Fc_mp(s, c, dps)
        Fc_dual = _scattering_factor_Fc_mp(s, 26 - c, dps)
        product = Fc * Fc_dual
        return {
            'Z_Koszul': complex(product),
            'F_c': complex(Fc),
            'F_dual': complex(Fc_dual),
            'zeta_ratio_sq': complex(zeta(2 * s) ** 2 / zeta(2 * s - 1) ** 2),
        }


def duality_twisted_double_pole_test(k=1, c=1.0, dps=30):
    r"""Test that Z^Koszul has double-strength singularity at zeta zeros.

    Near s = s_rho = (1+rho)/2, each F has a simple pole from
    zeta(2s-1) ~ zeta'(rho) * (2s-1-rho).  So F_c ~ A_c(rho)/(s-s_rho)
    and F_{26-c} ~ A_{26-c}(rho)/(s-s_rho), giving:

        Z^Koszul ~ A_c(rho) * A_{26-c}(rho) / (s - s_rho)^2

    We verify by checking that |Z^Koszul * (s-s_rho)^2| approaches
    |A_c * A_{26-c}| as s -> s_rho.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = zetazero(k)
        s_rho = (1 + rho) / 2

        # Expected leading coefficient
        A_c = _universal_residue_factor_mp(rho, mpc(c), dps)
        A_dual = _universal_residue_factor_mp(rho, 26 - mpc(c), dps)
        expected_coeff = A_c * A_dual

        # Approach s_rho along a sequence
        results = []
        for n_pow in range(4, 9):
            eps = power(10, -n_pow)
            s_test = s_rho + eps
            Fc = _scattering_factor_Fc_mp(s_test, mpc(c), dps)
            Fc_dual = _scattering_factor_Fc_mp(s_test, 26 - mpc(c), dps)
            Z_approx = Fc * Fc_dual
            # Z ~ coeff / eps^2, so Z * eps^2 ~ coeff
            extracted = Z_approx * eps ** 2
            results.append({
                'eps': float(eps),
                '|Z*eps^2|': float(fabs(extracted)),
                '|expected|': float(fabs(expected_coeff)),
                'rel_err': float(fabs(extracted - expected_coeff)
                                 / max(fabs(expected_coeff), power(10, -dps + 5))),
            })

        return {
            'k': k,
            'c': c,
            'expected_coeff': complex(expected_coeff),
            'approach_data': results,
        }


def duality_twisted_factorization(s, c, dps=30):
    r"""Factor Z^Koszul(s) = [Gamma_product] * [pi_factor] * [zeta(2s)/zeta(2s-1)]^2.

    The squared zeta ratio is the DOUBLE zeta content.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        c = mpc(c)
        c_dual = 26 - c

        # Gamma factor for F_c
        G_c = (mpgamma(s) * mpgamma(s + c / 2 - 1)
               / (mpgamma(c / 2 - s) * mpgamma(s - mpf('0.5'))))
        # Gamma factor for F_{26-c}
        G_dual = (mpgamma(s) * mpgamma(s + c_dual / 2 - 1)
                  / (mpgamma(c_dual / 2 - s) * mpgamma(s - mpf('0.5'))))

        gamma_product = G_c * G_dual
        pi_factor = power(pi, -(4 * s - 1))  # pi^{-(2s-1/2)} squared
        zeta_sq = (zeta(2 * s) / zeta(2 * s - 1)) ** 2

        reconstructed = gamma_product * pi_factor * zeta_sq
        direct = duality_twisted_scattering(s, complex(c), dps)['Z_Koszul']

        return {
            'gamma_product': complex(gamma_product),
            'pi_factor': complex(pi_factor),
            'zeta_ratio_sq': complex(zeta_sq),
            'reconstructed': complex(reconstructed),
            'direct': direct,
            'rel_err': abs(complex(reconstructed) - direct)
                       / max(abs(direct), 1e-100),
        }


# ============================================================================
# 4.  Complementarity L-function: L^comp_c(s) = F_c(s) / F_{26-c}(s)
# ============================================================================

def complementarity_L_function(s, c, dps=30):
    r"""L^comp_c(s) = F_c(s) / F_{26-c}(s).

    At c=13: L^comp_13 = 1 (exactly, by self-duality).
    The zeta ratio cancels completely (it is c-independent).

    What remains is the ratio of Gamma factors:
        L^comp_c(s) = Gamma(s+c/2-1) * Gamma(13-c/2-s)
                      / (Gamma(c/2-s) * Gamma(s+12-c/2))

    This is a MEROMORPHIC function of s with NO zeta content.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        c = mpc(c)
        c_dual = 26 - c

        # Direct computation via F_c / F_{26-c}
        Fc = _scattering_factor_Fc_mp(s, c, dps)
        Fc_dual = _scattering_factor_Fc_mp(s, c_dual, dps)
        if fabs(Fc_dual) < power(10, -dps + 5):
            L_direct = mpc(inf)
        else:
            L_direct = Fc / Fc_dual

        # Gamma-only formula (zeta ratio cancels)
        # F_c / F_{26-c} = [Gamma(s+c/2-1)/Gamma(c/2-s)]
        #                  / [Gamma(s+(26-c)/2-1)/Gamma((26-c)/2-s)]
        # = Gamma(s+c/2-1) * Gamma(13-c/2-s)
        #   / (Gamma(c/2-s) * Gamma(s+12-c/2))
        num_L = mpgamma(s + c / 2 - 1) * mpgamma(13 - c / 2 - s)
        den_L = mpgamma(c / 2 - s) * mpgamma(s + 12 - c / 2)
        if fabs(den_L) < power(10, -dps + 5):
            L_gamma = mpc(inf)
        else:
            L_gamma = num_L / den_L

        rel_err = float(fabs(L_direct - L_gamma)
                        / max(fabs(L_direct), power(10, -dps + 5)))

        return {
            'L_comp': complex(L_direct),
            'L_gamma': complex(L_gamma),
            'relative_error': rel_err,
            'c': complex(c),
        }


def complementarity_L_at_self_dual(s, dps=30):
    r"""Verify L^comp_13(s) = 1 (exactly) at the self-dual point."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    result = complementarity_L_function(s, 13, dps)
    return {
        'L_comp_13': result['L_comp'],
        'L_gamma_13': result['L_gamma'],
        'deviation_from_1': abs(result['L_gamma'] - 1.0),
    }


def koszul_perturbation(s, dps=30):
    r"""The Koszul perturbation delta_L(s) = (d/dc)|_{c=13} log L^comp_c(s).

    Near c=13:
        L^comp_c(s) = 1 + (c-13) * delta_L(s) + O((c-13)^2)

    So: delta_L(s) = (d/dc)|_{c=13} log(F_c/F_{26-c})

    Using log F_c = log Gamma(s+c/2-1) - log Gamma(c/2-s) + [c-independent terms]:

        (d/dc) log F_c = (1/2) [psi(s+c/2-1) + psi(c/2-s)]

    where psi = Gamma'/Gamma is the digamma function.

    So: delta_L(s) = (d/dc)|_{c=13} [log F_c - log F_{26-c}]
                   = (1/2)[psi(s+11/2) + psi(11/2-s)]
                     - (1/2)[(-1)(psi(s+11/2) + psi(11/2-s))]

    Wait -- (d/dc) log F_{26-c} = -(d/dc) log F_c evaluated at c,
    since (d/dc) [log F_{26-c}] = (d/d(26-c)) [log F_{26-c}] * (-1)
                                = -(d/dc') log F_{c'} |_{c'=26-c}.

    At c=13: the full L^comp_c involves four Gamma terms:
        L = Gamma(s+c/2-1)*Gamma(13-c/2-s) / (Gamma(c/2-s)*Gamma(s+12-c/2))

    d/dc log L = (1/2)[psi(s+c/2-1) - psi(13-c/2-s) - psi(c/2-s) + psi(s+12-c/2)]

    At c=13 (where c/2=13/2, 12-c/2=11/2, 13-c/2=13/2):
        = (1/2)[psi(s+11/2) - psi(13/2-s) - psi(13/2-s) + psi(s+11/2)]
        = psi(s+11/2) - psi(13/2-s)

    VERIFICATION: numerical finite-difference check.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)

        # Analytic formula: psi(s + 11/2) - psi(13/2 - s)
        delta_analytic = mpdigamma(0, s + mpf('11') / 2) - mpdigamma(0, mpf('13') / 2 - s)

        # Numerical finite-difference check
        h = mpf('1e-8')
        c_plus = mpf('13') + h
        c_minus = mpf('13') - h
        # log L^comp at c+h and c-h
        L_plus = complementarity_L_function(complex(s), float(c_plus), dps)['L_gamma']
        L_minus = complementarity_L_function(complex(s), float(c_minus), dps)['L_gamma']
        log_L_plus = cmath.log(L_plus)
        log_L_minus = cmath.log(L_minus)
        delta_numerical = (log_L_plus - log_L_minus) / (2 * float(h))

        return {
            'delta_L_analytic': complex(delta_analytic),
            'delta_L_numerical': complex(delta_numerical),
            'relative_error': abs(complex(delta_analytic) - complex(delta_numerical))
                              / max(abs(complex(delta_analytic)), 1e-100),
        }


def koszul_perturbation_at_zeros(n_zeros=10, dps=30):
    r"""Compute delta_L(s_rho) at scattering pole positions for the first n_zeros zeros."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    results = []
    with mp.workdps(dps):
        for k in range(1, n_zeros + 1):
            rho = zetazero(k)
            s_rho = (1 + rho) / 2
            # Evaluate delta_L near s_rho (not exactly at the pole)
            s_near = s_rho + mpf('0.01')
            delta_data = koszul_perturbation(complex(s_near), dps)
            results.append({
                'k': k,
                'gamma': float(mpim(rho)),
                's_rho': complex(s_rho),
                'delta_L': delta_data['delta_L_analytic'],
                '|delta_L|': abs(delta_data['delta_L_analytic']),
            })
    return results


# ============================================================================
# 5.  Shadow complementarity: zeta_A(s) + zeta_{A!}(s)
# ============================================================================

def _virasoro_shadow_coefficients(c_val, max_r=50):
    r"""Shadow coefficients for Vir_c via convolution recursion.

    Standalone implementation to avoid import cycles.
    """
    if c_val == 0.0 or 5.0 * c_val + 22.0 == 0.0:
        raise ValueError(f"Virasoro shadow undefined at c={c_val}")
    q0 = c_val ** 2
    q1 = 12.0 * c_val
    q2 = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
    a0 = abs(c_val)
    a = [a0]
    if max_r >= 3:
        a.append(q1 / (2.0 * a0))
    if max_r >= 4:
        a.append((q2 - a[1] ** 2) / (2.0 * a0))
    for n in range(3, max_r - 2 + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv / (2.0 * a0))
    result = {}
    for n in range(len(a)):
        r = n + 2
        result[r] = a[n] / float(r)
    return result


def _heisenberg_shadow_coefficients(k_val, max_r=50):
    """Shadow coefficients for Heisenberg H_k."""
    result = {2: float(k_val)}
    for r in range(3, max_r + 1):
        result[r] = 0.0
    return result


def _affine_shadow_coefficients(k_val, dim_g, h_dual, max_r=50):
    """Shadow coefficients for affine KM V_k(g)."""
    kappa = dim_g * (k_val + h_dual) / (2.0 * h_dual)
    alpha = 2.0 * h_dual / (k_val + h_dual)
    result = {2: kappa, 3: alpha}
    for r in range(4, max_r + 1):
        result[r] = 0.0
    return result


def shadow_zeta_function(shadow_coeffs, s, max_r=None):
    r"""Compute the shadow zeta function zeta_A(s) = sum_{r>=2} S_r * r^{-s}.

    This is a Dirichlet series over shadow coefficients.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    total = complex(0, 0)
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if Sr == 0.0:
            continue
        total += Sr * r ** (-s)
    return total


def shadow_complementarity_sum(c_val, s, max_r=50):
    r"""Compute zeta_A(s) + zeta_{A!}(s) for Virasoro with A=Vir_c, A!=Vir_{26-c}.

    The leading term S_2(A) + S_2(A!) = kappa(A) + kappa(A!)
      = c/2 + (26-c)/2 = 13  (AP24: this is 13, NOT 0).

    So the sum has leading coefficient 13 * 2^{-s}, regardless of c.
    """
    coeffs_A = _virasoro_shadow_coefficients(c_val, max_r)
    coeffs_dual = _virasoro_shadow_coefficients(26.0 - c_val, max_r)

    zeta_A = shadow_zeta_function(coeffs_A, s, max_r)
    zeta_dual = shadow_zeta_function(coeffs_dual, s, max_r)
    zeta_sum = zeta_A + zeta_dual

    # Leading term coefficient: S_2(A) + S_2(A!) = 13
    leading = 13.0 * 2 ** (-s)

    return {
        'zeta_A': zeta_A,
        'zeta_dual': zeta_dual,
        'zeta_sum': zeta_sum,
        'leading_term': leading,
        'correction': zeta_sum - leading,
        'S2_sum': coeffs_A[2] + coeffs_dual[2],
    }


def shadow_complementarity_difference(c_val, s, max_r=50):
    r"""Compute zeta_A(s) - zeta_{A!}(s) for Virasoro.

    The leading term S_2(A) - S_2(A!) = kappa(A) - kappa(A!)
      = c/2 - (26-c)/2 = c - 13  (= delta_kappa, AP29).

    At c=13 (self-dual): this difference VANISHES at the leading order.
    """
    coeffs_A = _virasoro_shadow_coefficients(c_val, max_r)
    coeffs_dual = _virasoro_shadow_coefficients(26.0 - c_val, max_r)

    zeta_A = shadow_zeta_function(coeffs_A, s, max_r)
    zeta_dual = shadow_zeta_function(coeffs_dual, s, max_r)
    zeta_diff = zeta_A - zeta_dual

    delta_kappa = c_val / 2.0 - (26.0 - c_val) / 2.0  # = c - 13

    return {
        'zeta_A': zeta_A,
        'zeta_dual': zeta_dual,
        'zeta_diff': zeta_diff,
        'delta_kappa': delta_kappa,
        'leading_diff': delta_kappa * 2 ** (-s),
    }


def shadow_complementarity_heisenberg(k_val, s, max_r=50):
    r"""Shadow complementarity for Heisenberg: H_k, H_{-k}.

    kappa(H_k) = k, kappa(H_{-k}) = -k.  So kappa + kappa' = 0.
    Shadow zeta: zeta_{H_k}(s) = k * 2^{-s}, zeta_{H_{-k}}(s) = -k * 2^{-s}.
    Sum = 0 (perfect cancellation).
    """
    coeffs_A = _heisenberg_shadow_coefficients(k_val, max_r)
    coeffs_dual = _heisenberg_shadow_coefficients(-k_val, max_r)

    zeta_A = shadow_zeta_function(coeffs_A, s, max_r)
    zeta_dual = shadow_zeta_function(coeffs_dual, s, max_r)
    zeta_sum = zeta_A + zeta_dual

    return {
        'zeta_A': zeta_A,
        'zeta_dual': zeta_dual,
        'zeta_sum': zeta_sum,
        'kappa_sum': k_val + (-k_val),
    }


def shadow_complementarity_affine_sl2(k_val, s, max_r=50):
    r"""Shadow complementarity for affine sl_2: V_k(sl_2), V_{-k-4}(sl_2).

    Feigin-Frenkel: k -> -k - 2h^v = -k - 4 for sl_2.
    kappa(V_k) = 3(k+2)/4.  kappa(V_{-k-4}) = 3(-k-4+2)/4 = 3(-k-2)/4 = -3(k+2)/4.
    So kappa + kappa' = 0 (as expected for KM families, AP24).
    """
    h_dual = 2.0
    dim_g = 3.0
    k_dual = -k_val - 2 * h_dual

    coeffs_A = _affine_shadow_coefficients(k_val, dim_g, h_dual, max_r)
    coeffs_dual = _affine_shadow_coefficients(k_dual, dim_g, h_dual, max_r)

    zeta_A = shadow_zeta_function(coeffs_A, s, max_r)
    zeta_dual = shadow_zeta_function(coeffs_dual, s, max_r)
    zeta_sum = zeta_A + zeta_dual

    kappa_A = dim_g * (k_val + h_dual) / (2.0 * h_dual)
    kappa_dual = dim_g * (k_dual + h_dual) / (2.0 * h_dual)

    return {
        'zeta_A': zeta_A,
        'zeta_dual': zeta_dual,
        'zeta_sum': zeta_sum,
        'kappa_A': kappa_A,
        'kappa_dual': kappa_dual,
        'kappa_sum': kappa_A + kappa_dual,
    }


# ============================================================================
# 6.  Lagrangian structure: intersection with zeta zero hyperplane
# ============================================================================

def lagrangian_intersection_data(rho, c, dps=30):
    r"""Lagrangian structure of complementarity at a zeta zero.

    The shifted-symplectic complementarity (Theorem C) maps the pair
    (Q_g(A), Q_g(A!)) to a Lagrangian subspace L_c in:

        V = H*(M-bar_g, Z(A)) x H*(M-bar_g, Z(A!))

    At genus 1, the "zeta zero hyperplane" H_rho is the locus where
    F_c has a pole: s = (1+rho)/2.  The Lagrangian intersection
    L_c cap H_rho is measured by:

    1. The residue PAIR (A_c(rho), A_{26-c}(rho))
    2. Their symplectic pairing omega(A_c, A_{26-c})
    3. The Lagrangian angle theta = arg(A_c/A_{26-c})

    The symplectic pairing from the complementarity theorem is:
        omega(v, w) = <v, w> where <.,.> is the Poincare pairing on M-bar_g.

    For the constrained Epstein data at genus 1, this reduces to
    the product A_c * A_{26-c} (the coupling constant).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = mpc(rho)
        c = mpc(c)

        A_c = _universal_residue_factor_mp(rho, c, dps)
        A_dual = _universal_residue_factor_mp(rho, 26 - c, dps)

        # Symplectic coupling: A_c * A_{26-c}
        coupling = A_c * A_dual

        # Lagrangian angle: arg(A_c / A_{26-c})
        if fabs(A_dual) < power(10, -dps + 5):
            lag_angle = float('nan')
            ratio = mpc(inf)
        else:
            ratio = A_c / A_dual
            lag_angle = float(mparg(ratio))

        # Isotropy check: for a Lagrangian, omega restricted to L should vanish.
        # The coupling A_c * A_{26-c} measures the failure of isotropy.
        # At c=13 (self-dual): A_c = A_{26-c}, so coupling = |A_13|^2 (real, positive).

        return {
            'A_c': complex(A_c),
            'A_dual': complex(A_dual),
            'coupling': complex(coupling),
            '|coupling|': float(fabs(coupling)),
            'lagrangian_angle': lag_angle,
            'ratio': complex(ratio),
            '|A_c/A_dual|': float(fabs(ratio)) if fabs(A_dual) > power(10, -dps + 5) else float('inf'),
        }


def lagrangian_angle_spectrum(n_zeros=20, c=1.0, dps=30):
    r"""Compute the Lagrangian angle theta_k = arg(A_c(rho_k)/A_{26-c}(rho_k))
    for the first n_zeros zeros."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    results = []
    with mp.workdps(dps):
        for k in range(1, n_zeros + 1):
            rho = zetazero(k)
            data = lagrangian_intersection_data(complex(rho), c, dps)
            results.append({
                'k': k,
                'gamma': float(mpim(rho)),
                'lagrangian_angle': data['lagrangian_angle'],
                '|coupling|': data['|coupling|'],
                '|ratio|': data['|A_c/A_dual|'],
            })
    return results


# ============================================================================
# 7.  Defect form: Omega_c(s) = (d/dc) A_c(rho)
# ============================================================================

def defect_form(rho, c, dps=30):
    r"""The defect form Omega_c(rho) = (d/dc) A_c(rho).

    Measures how the universal residue factor changes as c varies.
    Computed via the c-dependence in the Gamma factors:

    A_c(rho) = [c-independent] * Gamma((c+rho-1)/2) / Gamma((c-rho-1)/2)

    So: (d/dc) log A_c = (1/2)[psi((c+rho-1)/2) + psi((c-rho-1)/2)]

    and: Omega_c(rho) = A_c(rho) * (1/2)[psi((c+rho-1)/2) + psi((c-rho-1)/2)]

    VERIFICATION: numerical finite difference.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = mpc(rho)
        c = mpc(c)

        A_c = _universal_residue_factor_mp(rho, c, dps)

        # Analytic derivative via digamma
        # d/dc log A_c = (1/2) * [psi((c+rho-1)/2) + psi((c-rho-1)/2)]
        # Note: d/dc Gamma((c+rho-1)/2) = (1/2) Gamma(...) psi(...)
        #       d/dc [-log Gamma((c-rho-1)/2)] = -(1/2) psi((c-rho-1)/2)
        # Wait, d/dc [log Gamma((c+rho-1)/2)] = (1/2) psi((c+rho-1)/2)
        # and d/dc [-log Gamma((c-rho-1)/2)] = -(1/2) psi((c-rho-1)/2)
        # So d/dc log A_c = (1/2)[psi((c+rho-1)/2) - psi((c-rho-1)/2)]
        dlog_A = (mpdigamma(0, (c + rho - 1) / 2)
                  - mpdigamma(0, (c - rho - 1) / 2)) / 2

        omega_analytic = A_c * dlog_A

        # Numerical check
        h = mpf('1e-6')
        A_plus = _universal_residue_factor_mp(rho, c + h, dps)
        A_minus = _universal_residue_factor_mp(rho, c - h, dps)
        omega_numerical = (A_plus - A_minus) / (2 * h)

        rel_err = float(fabs(omega_analytic - omega_numerical)
                        / max(fabs(omega_analytic), power(10, -dps + 5)))

        return {
            'omega_analytic': complex(omega_analytic),
            'omega_numerical': complex(omega_numerical),
            'relative_error': rel_err,
            'A_c': complex(A_c),
            'dlog_A': complex(dlog_A),
        }


def defect_form_at_zeros(n_zeros=10, c_val=13.0, dps=30):
    r"""Compute the defect form at each of the first n_zeros zeros."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    results = []
    with mp.workdps(dps):
        for k in range(1, n_zeros + 1):
            rho = zetazero(k)
            data = defect_form(complex(rho), c_val, dps)
            results.append({
                'k': k,
                'gamma': float(mpim(rho)),
                '|omega|': abs(data['omega_analytic']),
                'omega': data['omega_analytic'],
                'rel_err': data['relative_error'],
            })
    return results


def defect_form_spectrum(n_zeros=20, c_values=None, dps=30):
    r"""Table of |Omega_c(rho_k)| for multiple c-values and zeros."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    if c_values is None:
        c_values = [1.0, 5.0, 10.0, 13.0, 20.0, 25.0]
    results = []
    with mp.workdps(dps):
        for k in range(1, n_zeros + 1):
            rho = zetazero(k)
            row = {'k': k, 'gamma': float(mpim(rho))}
            for c_val in c_values:
                data = defect_form(complex(rho), c_val, dps)
                row[f'|omega_c={c_val}|'] = abs(data['omega_analytic'])
            results.append(row)
    return results


# ============================================================================
# 8.  Boundary cases: c = 0 and c = 26
# ============================================================================

def boundary_case_analysis(rho, dps=30):
    r"""Analyze the boundary cases c=0 and c=26 (and c=epsilon, c=26-epsilon).

    At c=0: kappa = 0, the algebra is "trivial" (zero central charge).
        A_0(rho) involves Gamma((rho-1)/2) / Gamma((-rho-1)/2).

    At c=26: kappa = 13, the critical dimension.
        A_26(rho) involves Gamma((25+rho)/2) / Gamma((25-rho)/2).

    The ratio A_0/A_26 should simplify via the Gamma reflection formula.

    NOTE: c=0 is a boundary of the standard landscape; Vir_0 has kappa=0
    and is depth-zero resonant (AP31: kappa=0 does NOT mean Theta=0).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = mpc(rho)

        # Near c=0 (use c=0.01 to avoid singularity)
        eps = mpf('0.01')
        A_near_0 = _universal_residue_factor_mp(rho, eps, dps)

        # Near c=26 (use c=25.99)
        A_near_26 = _universal_residue_factor_mp(rho, 26 - eps, dps)

        # At exactly c=1 and c=25 (valid and away from boundary)
        A_1 = _universal_residue_factor_mp(rho, 1, dps)
        A_25 = _universal_residue_factor_mp(rho, 25, dps)

        # Ratio A_1 / A_25 via Gamma formula
        ratio_1_25 = residue_complementarity_ratio(complex(rho), 1, dps)

        return {
            'A_near_0': complex(A_near_0),
            'A_near_26': complex(A_near_26),
            'A_1': complex(A_1),
            'A_25': complex(A_25),
            'ratio_1_25': ratio_1_25['ratio_gamma'],
        }


# ============================================================================
# 9.  Consistency checks with kappa values
# ============================================================================

def kappa_consistency_check():
    r"""Verify kappa + kappa' values for standard families.

    From CLAUDE.md / landscape_census.tex:
    - Heisenberg H_k:   kappa = k,    kappa' = -k,   sum = 0
    - Affine sl_2 V_k:  kappa = 3(k+2)/4,  kappa' = -3(k+2)/4, sum = 0
    - Virasoro Vir_c:   kappa = c/2,  kappa' = (26-c)/2, sum = 13

    CAUTION (AP24): The sum is NOT universally zero.
    """
    checks = []

    # Heisenberg
    for k in [1.0, 2.0, 5.0]:
        kappa = k
        kappa_dual = -k
        checks.append({
            'family': f'Heisenberg k={k}',
            'kappa': kappa,
            'kappa_dual': kappa_dual,
            'sum': kappa + kappa_dual,
            'expected_sum': 0.0,
            'ok': abs(kappa + kappa_dual) < 1e-14,
        })

    # Affine sl_2
    for k in [1.0, 2.0, 5.0]:
        h_dual = 2.0
        dim_g = 3.0
        kappa = dim_g * (k + h_dual) / (2.0 * h_dual)
        k_dual = -k - 2 * h_dual
        kappa_dual = dim_g * (k_dual + h_dual) / (2.0 * h_dual)
        checks.append({
            'family': f'Affine sl_2 k={k}',
            'kappa': kappa,
            'kappa_dual': kappa_dual,
            'sum': kappa + kappa_dual,
            'expected_sum': 0.0,
            'ok': abs(kappa + kappa_dual) < 1e-14,
        })

    # Virasoro
    for c_val in [1.0, 13.0, 25.0, 2.0, 24.0]:
        kappa = c_val / 2.0
        kappa_dual = (26.0 - c_val) / 2.0
        checks.append({
            'family': f'Virasoro c={c_val}',
            'kappa': kappa,
            'kappa_dual': kappa_dual,
            'sum': kappa + kappa_dual,
            'expected_sum': 13.0,
            'ok': abs(kappa + kappa_dual - 13.0) < 1e-14,
        })

    return checks


# ============================================================================
# 10.  Scattering factor ratio: F_c / F_{26-c} decomposition
# ============================================================================

def scattering_factor_ratio_decomposition(s, c, dps=30):
    r"""Full decomposition of F_c(s) / F_{26-c}(s).

    Since the zeta ratio zeta(2s)/zeta(2s-1) is c-independent,
    it cancels in the ratio.  The pi factor pi^{-(2s-1/2)} also cancels.

    What remains is the conformal Gamma factor ratio:

        F_c / F_{26-c} = Gamma(s+c/2-1)*Gamma(13-c/2-s)
                         / (Gamma(c/2-s)*Gamma(s+12-c/2))

    This is a product of TWO Gamma ratios:
    R1 = Gamma(s+c/2-1) / Gamma(c/2-s)        [from F_c numerator/denominator]
    R2 = Gamma(13-c/2-s) / Gamma(s+12-c/2)    [from F_{26-c} denominator/numerator]

    At c=13: R1 = Gamma(s+11/2)/Gamma(11/2-s) and R2 = Gamma(11/2-s)/Gamma(s+11/2) = 1/R1.
    So F_13/F_13 = R1/R1 = 1 (consistent).

    VERIFICATION: compare direct ratio with the Gamma-only formula.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        c = mpc(c)
        c_dual = 26 - c

        # Direct computation
        Fc = _scattering_factor_Fc_mp(s, c, dps)
        Fc_dual = _scattering_factor_Fc_mp(s, c_dual, dps)
        direct_ratio = Fc / Fc_dual if fabs(Fc_dual) > power(10, -dps + 5) else mpc(inf)

        # Gamma-only decomposition
        R1 = mpgamma(s + c / 2 - 1) / mpgamma(c / 2 - s)
        R2 = mpgamma(13 - c / 2 - s) / mpgamma(s + 12 - c / 2)
        gamma_ratio = R1 * R2

        rel_err = float(fabs(direct_ratio - gamma_ratio)
                        / max(fabs(direct_ratio), power(10, -dps + 5)))

        return {
            'direct_ratio': complex(direct_ratio),
            'gamma_ratio': complex(gamma_ratio),
            'R1': complex(R1),
            'R2': complex(R2),
            'relative_error': rel_err,
        }


# ============================================================================
# 11.  Summary: full complementarity analysis at a zero
# ============================================================================

def full_complementarity_at_zero(k=1, c=1.0, dps=30):
    r"""Full complementarity analysis at the k-th zeta zero for Virasoro at c.

    Returns: residue ratio, Lagrangian data, defect form, L^comp, all
    cross-checked against kappa values.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = zetazero(k)

        residue_data = residue_complementarity_ratio(complex(rho), c, dps)
        lagrangian_data = lagrangian_intersection_data(complex(rho), c, dps)
        defect_data = defect_form(complex(rho), c, dps)

        s_rho = (1 + rho) / 2
        L_data = complementarity_L_function(complex(s_rho + mpf('0.01')), c, dps)

        kappa_A = c / 2.0
        kappa_dual = (26.0 - c) / 2.0

        return {
            'k': k,
            'c': c,
            'rho': complex(rho),
            'gamma': float(mpim(rho)),
            'kappa_A': kappa_A,
            'kappa_dual': kappa_dual,
            'kappa_sum': kappa_A + kappa_dual,
            'residue_ratio': residue_data['ratio_gamma'],
            '|residue_ratio|': abs(residue_data['ratio_gamma']),
            'lagrangian_angle': lagrangian_data['lagrangian_angle'],
            '|coupling|': lagrangian_data['|coupling|'],
            '|defect|': abs(defect_data['omega_analytic']),
            'L_comp': L_data['L_comp'],
            'complementarity_error': residue_data['relative_error'],
        }
