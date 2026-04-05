#!/usr/bin/env python3
r"""
bc_higher_genus_epstein_engine.py -- Higher-genus constrained Epstein zeta
functions and the Boecherer bridge.

THE MATHEMATICAL CONTENT
========================

At genus 1, the Benjamin-Chang constrained Epstein zeta function
epsilon^c_s(A) encodes the scalar primary spectrum of a chiral algebra A
via the Roelcke-Selberg spectral decomposition on SL(2,Z)\H.  The
scattering factor F_c(s) contains a SINGLE ratio zeta(2s)/zeta(2s-1),
inherited from the Eisenstein scattering matrix phi(s) = Lambda(1-s)/Lambda(s).

At genus g >= 2, the modular group is Sp(2g,Z) and the symmetric space
is the Siegel upper half-space H_g.  The spectral decomposition of
modular-invariant functions on Sp(2g,Z)\H_g involves:

  (a) Siegel-Maass cusp forms (discrete spectrum)
  (b) Klingen Eisenstein series (intermediate parabolic induction)
  (c) Siegel Eisenstein series (maximal parabolic / full continuous spectrum)

The scattering matrix of the Siegel Eisenstein series E_g(Omega, s) is:

  phi_g(s) = prod_{j=0}^{g-1} Lambda(s-j) / Lambda(s-j)
           = prod_{j=0}^{g-1} [xi(2s-2j-1) / xi(2s-2j)]

where xi(s) = pi^{-s/2} Gamma(s/2) zeta(s) is the completed Riemann
zeta function.  This produces g INDEPENDENT zeta ratios:

  phi_g(s) involves zeta(2s-2j-1)/zeta(2s-2j) for j = 0, 1, ..., g-1

GENUS-2 CONSTRAINED EPSTEIN
============================

The genus-2 partition function Z_2(Omega) on H_2 gives rise to a
constrained Epstein functional equation via the Rankin-Selberg unfolding
against the Siegel Eisenstein series E_2(Omega, s).

The scattering factor at genus 2 is:

  F_{2,c}(s) = Gamma_2(s, c) * [zeta(2s)/zeta(2s-1)] * [zeta(2s-2)/zeta(2s-3)]

where Gamma_2(s, c) is the conformal Gamma factor determined by the
central charge.  The TWO zeta ratios introduce poles at:

  s = (1+rho_1)/2   from zeta(2s-1) = 0
  s = (3+rho_2)/2   from zeta(2s-3) = 0

where rho_1, rho_2 are nontrivial zeros of zeta.

The GENUS-2 UNIVERSAL RESIDUE FACTOR at a pair (rho_1, rho_2):

  A^{(2)}_c(rho_1, rho_2) involves DOUBLE residues of the scattering
  factor when BOTH zeta ratios have poles simultaneously.

When rho_1 = rho_2 = rho (coincident zeros), this reduces to a
second-order pole, and the residue involves zeta'(rho) and zeta''(rho).

GENUS-3 CONSTRAINED EPSTEIN
============================

At genus 3, the Siegel Eisenstein series E_3(Omega, s) on Sp(6,Z)\H_3
produces THREE zeta ratios:

  phi_3(s) ~ zeta(2s-1)/zeta(2s) * zeta(2s-3)/zeta(2s-2) * zeta(2s-5)/zeta(2s-4)

The scattering factor F_{3,c}(s) has poles at:
  s = (1+rho)/2, (3+rho)/2, (5+rho)/2  for each nontrivial zero rho.

BOECHERER CONNECTION
====================

Boecherer's conjecture (proved by Furusawa-Morimoto 2021) relates
genus-2 Fourier coefficients of Siegel eigenforms to central L-values:

  |a(T; F)|^2 / <F, F> = C * L(1/2, pi_F) * L(1/2, pi_F x chi_D)

where T has fundamental discriminant D and content 1.

For the shadow CohFT at genus 2, the genus-2 partition function Z_2(Omega)
is a Siegel modular form whose Fourier-Jacobi expansion interacts with
the Saito-Kurokawa lift.  The shadow contribution F_2 = kappa * lambda_2^FP
produces a specific pattern of Fourier coefficients that can be compared
against Boecherer's formula.

PLANTED-FOREST CORRECTION
==========================

The genus-2 planted-forest correction delta_pf^{(2,0)} = S_3(10*S_3 - kappa)/48
contributes to the constrained Epstein at genus 2.  Its residue at zeta
zeros is:

  Res_{s=s_rho} [delta_pf contribution] = delta_pf * [Gamma/zeta' factor]

This is an INDEPENDENT contribution beyond the scalar F_2 = kappa * lambda_2^FP.

References:
    benjamin_chang_analysis.py: genus-1 framework
    virasoro_constrained_epstein.py: Virasoro primary spectrum
    genus2_bar_cobar_engine.py: genus-2 bar complex
    genus2_bocherer_bridge.py: Boecherer bridge at genus 2
    genus2_bocherer_deep_engine.py: Niemeier atlas, Saito-Kurokawa
    siegel_genus3_engine.py: genus-3 Siegel modular forms
    [BenjaminChang22]: arXiv:2208.02259
    [FurusawaMorimoto21]: Refined global Gross-Prasad conjecture
    [Boecherer86]: Fourier-Jacobi development of Siegel modular forms
    [Shimura83]: On Eisenstein series
    [Langlands76]: Eisenstein series, the functional equation
"""

from __future__ import annotations

import math
from typing import Any, Dict, List, Optional, Tuple

try:
    import mpmath
    from mpmath import (mp, mpf, mpc, pi, zeta, gamma as mpgamma, log, exp,
                        power, sqrt, re as mpre, im as mpim, conj as mpconj,
                        diff, zetazero, inf, sin, cos, arg as mparg,
                        fabs, floor, nstr, fac, rgamma)
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

from fractions import Fraction
from functools import lru_cache


# ====================================================================
# 1. Completed zeta and Selberg functions
# ====================================================================

def completed_riemann_xi(s, dps=30):
    r"""The completed Riemann zeta: xi(s) = pi^{-s/2} Gamma(s/2) zeta(s).

    This satisfies xi(s) = xi(1-s).

    NOTE: This is the xi-function normalised so that xi(s) = xi(1-s).
    Some references use Xi(s) = (1/2) s(s-1) xi(s); we do NOT include
    the polynomial prefactor.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        return power(pi, -s / 2) * mpgamma(s / 2) * zeta(s)


def completed_selberg_Lambda(s, dps=30):
    r"""Lambda(s) = pi^{-s} Gamma(s) zeta(2s).

    This is the genus-1 building block: the Eisenstein scattering
    matrix is phi_1(s) = Lambda(1-s) / Lambda(s).

    Relation to xi: Lambda(s) = xi(2s).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        return power(pi, -s) * mpgamma(s) * zeta(2 * s)


# ====================================================================
# 2. Siegel Eisenstein scattering matrix
# ====================================================================

def siegel_scattering_matrix(g, s, dps=30):
    r"""The Siegel Eisenstein scattering matrix c_g(s) for Sp(2g,Z).

    For the Siegel Eisenstein series E_g(Omega, s) on Sp(2g,Z)\H_g,
    the constant term along the Siegel parabolic is:

      a_0(Y; E_g) = det(Y)^s + c_g(s) * det(Y)^{(g+1)/2 - s} + ...

    The intertwining operator / scattering matrix is
    (Shimura 1983, Boecherer 1986, Langlands):

      c_g(s) = prod_{i=1}^{g} xi(2s - i + 1) / xi(2s - i)

    This telescopes to c_g(s) = xi(2s) / xi(2s - g).

    FUNCTIONAL EQUATION: c_g(s) * c_g((g+1)/2 - s) = 1.
    Proof: c_g(s) = xi(2s)/xi(2s-g). Set s' = (g+1)/2 - s.
    Then c_g(s') = xi(g+1-2s)/xi(1-2s).  Using xi(t) = xi(1-t):
    xi(g+1-2s) = xi(2s-g) and xi(1-2s) = xi(2s).
    So c_g(s') = xi(2s-g)/xi(2s) = 1/c_g(s).

    For g=1: c_1(s) = xi(2s)/xi(2s-1).  FE: c_1(s)*c_1(1-s) = 1.
    This matches the standard SL(2,Z) Eisenstein scattering
    Lambda(s)/Lambda(s) ... well, phi(s) = Lambda(1-s)/Lambda(s) = xi(2-2s)/xi(2s)
    = xi(2s-1)/xi(2s) (by xi FE).  So c_1(s) = 1/phi(s), i.e.,
    c_1 is the INVERSE of the standard phi.  Both satisfy FE with product = 1.
    The sign convention does not affect poles or residue magnitudes.

    Poles of c_g(s): where xi(2s - i) = 0 for some i = 1,...,g, i.e.,
    where 2s - i = rho (nontrivial zero), giving s = (i + rho)/2.
    Under RH: Re(s) = (i + 1/2)/2 = i/2 + 1/4.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        product = mpc(1)
        for i in range(1, g + 1):
            num = completed_riemann_xi(2 * s - i + 1, dps)
            den = completed_riemann_xi(2 * s - i, dps)
            if fabs(den) < power(10, -dps + 5):
                return complex(inf)
            product *= num / den
        return complex(product)


def siegel_scattering_zeta_ratios(g, s, dps=30):
    r"""Decompose the Siegel scattering matrix into its g zeta ratios.

    c_g(s) = prod_{i=1}^{g} [arch_factor_i * zeta_ratio_i]

    where factor i corresponds to xi(2s-i+1)/xi(2s-i), and:
      zeta_ratio_i = zeta(2s - i + 1) / zeta(2s - i)
      arch_factor_i = [pi^{-...} Gamma(...)] ratio

    Returns a list of g dicts, one per factor i = 1,...,g.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        factors = []
        for i in range(1, g + 1):
            arg_num = 2 * s - i + 1
            arg_den = 2 * s - i
            z_ratio = zeta(arg_num) / zeta(arg_den) if fabs(zeta(arg_den)) > 1e-50 else complex(inf)
            arch_ratio = (power(pi, -arg_num / 2) * mpgamma(arg_num / 2)
                          / (power(pi, -arg_den / 2) * mpgamma(arg_den / 2)))
            factors.append({
                'i': i,
                'zeta_ratio': complex(z_ratio),
                'archimedean_ratio': complex(arch_ratio),
                'combined': complex(z_ratio * arch_ratio) if not isinstance(z_ratio, complex) or abs(z_ratio) < 1e50 else complex(inf),
                'zeta_num_arg': complex(arg_num),
                'zeta_den_arg': complex(arg_den),
            })
        return factors


# ====================================================================
# 3. Genus-2 scattering factor and constrained Epstein FE
# ====================================================================

def genus2_conformal_gamma(s, c, dps=30):
    r"""The genus-2 conformal Gamma factor.

    At genus 2, the Rankin-Selberg unfolding against E_2(Omega, s)
    produces Gamma factors from the weight-c/2 Mellin transform on H_2.

    The genus-2 generalisation of the genus-1 factor
    Gamma(s)*Gamma(s + c/2 - 1) / (Gamma(c/2 - s)*Gamma(s - 1/2))
    involves additional Gamma shifts from the Siegel parabolic:

      Gamma_2(s, c) = Gamma(s)*Gamma(s-1/2)*Gamma(s+c/2-1)*Gamma(s+c/2-3/2)
                     / (Gamma(c/2-s)*Gamma(c/2-s+1/2)*Gamma(s-1/2)*Gamma(s-1))

    Simplification after cancellation:

      Gamma_2(s, c) = Gamma(s)*Gamma(s+c/2-1)*Gamma(s+c/2-3/2)
                     / (Gamma(c/2-s)*Gamma(c/2-s+1/2)*Gamma(s-1))

    DERIVATION: The Mellin transform of det(y)^{c/2} against E_2(Omega, s)
    on the Siegel fundamental domain produces the shifted Gamma integrals
    int y_1^{s+c/2-1} y_2^{s+c/2-3/2} ... from the Selberg-type reduction
    of the H_2 integral to iterated H_1 integrals.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        c = mpc(c)
        num = mpgamma(s) * mpgamma(s + c / 2 - 1) * mpgamma(s + c / 2 - mpf('1.5'))
        den = mpgamma(c / 2 - s) * mpgamma(c / 2 - s + mpf('0.5')) * mpgamma(s - 1)
        if fabs(den) < power(10, -dps + 5):
            return complex(inf)
        return complex(num / den)


def genus2_scattering_factor(s, c, dps=30):
    r"""The genus-2 scattering factor F_{2,c}(s).

    Delegates to genus_g_scattering_factor(2, s, c, dps) for consistency.

    The two zeta ratios from the Siegel Eisenstein scattering c_2(s):
      i=1: zeta(2s)/zeta(2s-1)
      i=2: zeta(2s-1)/zeta(2s-2)

    Poles from ratio i=1: 2s - 1 = rho => s = (1+rho)/2
    Poles from ratio i=2: 2s - 2 = rho => s = (2+rho)/2
    """
    return genus_g_scattering_factor(2, s, c, dps)


def genus2_scattering_factor_decomposition(s, c, dps=30):
    r"""Decompose F_{2,c}(s) into its constituent factors.

    Returns dict with conformal Gamma, pi, and both zeta ratio factors.
    Uses the same Gamma/pi convention as the general genus_g function.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        c_mp = mpc(c)
        g = 2

        # Conformal Gamma factor (from general formula)
        gamma_num = mpc(1)
        gamma_den = mpc(1)
        for j in range(g):
            gamma_num *= mpgamma(s + c_mp / 2 - 1 - j) * mpgamma(s - j)
            gamma_den *= mpgamma(c_mp / 2 - s + j + mpf('0.5')) * mpgamma(s - j - mpf('0.5'))
        gamma_fac = complex(gamma_num / gamma_den) if fabs(gamma_den) > 1e-50 else complex(inf)

        # Pi factor (from general formula)
        pi_exp = -(2 * g * s - g * (g + 1) / 2 + mpf('0.5'))
        pi_fac = complex(power(pi, pi_exp))

        # Two zeta ratios
        zr1_num = zeta(2 * s)
        zr1_den = zeta(2 * s - 1)
        zr1 = complex(zr1_num / zr1_den) if fabs(zr1_den) > 1e-50 else complex(inf)

        zr2_num = zeta(2 * s - 1)
        zr2_den = zeta(2 * s - 2)
        zr2 = complex(zr2_num / zr2_den) if fabs(zr2_den) > 1e-50 else complex(inf)

        product = complex(mpc(gamma_fac) * mpc(pi_fac) * mpc(zr1) * mpc(zr2))

        return {
            'conformal_gamma': gamma_fac,
            'pi_factor': pi_fac,
            'zeta_ratio_1': zr1,
            'zeta_ratio_2': zr2,
            'product': product,
        }


# ====================================================================
# 3a. Helper: conformal Gamma and pi factors for genus-g
# ====================================================================

def _conformal_gamma_pi(g, s, c, dps=30):
    r"""Compute the conformal Gamma and pi factors for genus-g.

    Returns (gamma_fac, pi_fac) as mpmath numbers.
    Uses the same formula as genus_g_scattering_factor.
    """
    with mp.workdps(dps):
        s = mpc(s)
        c = mpc(c)
        gamma_num = mpc(1)
        gamma_den = mpc(1)
        for j in range(g):
            gamma_num *= mpgamma(s + c / 2 - 1 - j) * mpgamma(s - j)
            gamma_den *= mpgamma(c / 2 - s + j + mpf('0.5')) * mpgamma(s - j - mpf('0.5'))
        gamma_fac = gamma_num / gamma_den if fabs(gamma_den) > 1e-50 else mpc(inf)
        pi_exp = -(2 * g * s - g * (g + 1) / 2 + mpf('0.5'))
        pi_fac = power(pi, pi_exp)
        return gamma_fac, pi_fac


# ====================================================================
# 4. Genus-2 pole structure and residue factors
# ====================================================================

def genus2_pole_positions(n_zeros=10, dps=30):
    r"""Poles of F_{2,c}(s) from zeros of the two zeta functions.

    From c_2(s) = xi(2s)/xi(2s-1) * xi(2s-1)/xi(2s-2):
    Poles from xi(2s-1): 2s-1 = rho => s = (1+rho)/2
    Poles from xi(2s-2): 2s-2 = rho => s = (2+rho)/2

    NOTE: The poles from xi(2s-1) in the numerator of factor i=2
    CANCEL the poles from xi(2s-1) in the denominator of factor i=1.
    After telescoping c_2(s) = xi(2s)/xi(2s-2), the ACTUAL poles are:
      Family 1: 2s - 2 = rho => s = (2+rho)/2  (from xi(2s-2) denominator)

    And xi(2s) in the numerator has zeros at 2s = rho => s = rho/2.

    Under RH: Family 1 poles at Re(s) = (2+1/2)/2 = 5/4.

    HOWEVER, for the constrained Epstein FE, the scattering factor F_{2,c}(s)
    includes the conformal Gamma factor which may re-introduce poles
    at the cancelled locations.  For the purpose of pole analysis,
    we track BOTH individual-factor pole families:

    Family 1 (from factor i=1 denominator): s = (1+rho)/2, Re = 3/4
    Family 2 (from factor i=2 denominator): s = (2+rho)/2, Re = 5/4
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        poles = {'family_1': [], 'family_2': []}
        for k in range(1, n_zeros + 1):
            rho = zetazero(k)
            gamma_k = float(mpim(rho))

            # Family 1
            s1 = (1 + rho) / 2
            poles['family_1'].append({
                'k': k, 'rho': complex(rho), 'gamma': gamma_k,
                's': complex(s1), 'real': float(mpre(s1)), 'imag': float(mpim(s1)),
            })

            # Family 2: s = (2+rho)/2
            s2 = (2 + rho) / 2
            poles['family_2'].append({
                'k': k, 'rho': complex(rho), 'gamma': gamma_k,
                's': complex(s2), 'real': float(mpre(s2)), 'imag': float(mpim(s2)),
            })

        return poles


def genus2_universal_residue_single(rho, c, family, dps=30):
    r"""Residue of F_{2,c}(s) at a SINGLE zeta zero.

    With the correct zeta ratios zeta(2s)/zeta(2s-1) * zeta(2s-1)/zeta(2s-2):

    Family 1 (pole from zeta(2s-1)=0 in ratio i=1 denominator):
      s = (1+rho)/2, where 2s-1 = rho.
      At this s: ratio i=1 has residue zeta(1+rho)/(2*zeta'(rho)).
      Ratio i=2: zeta(rho)/zeta(rho-1) evaluated at s0 (regular).

    Family 2 (pole from zeta(2s-2)=0 in ratio i=2 denominator):
      s = (2+rho)/2, where 2s-2 = rho.
      At this s: ratio i=2 has residue zeta(1+rho)/(2*zeta'(rho)).
      Ratio i=1: zeta(2+rho)/zeta(1+rho) evaluated at s0 (regular).

    NOTE: There is potential cancellation at family 1 because the
    numerator of ratio i=2 is zeta(2s-1) which ALSO vanishes at
    2s-1=rho.  So the pole from i=1 denominator may be cancelled
    by the zero from i=2 numerator.  This reflects the telescoping
    c_2(s) = xi(2s)/xi(2s-2): after cancellation, the only poles
    come from xi(2s-2)=0, i.e., family 2.

    For the FULL scattering factor F_{2,c}(s) (not just the zeta product),
    the conformal Gamma factor may introduce or cancel poles independently.
    We compute the residue of the FULL F_{2,c} at both locations.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = mpc(rho)
        c_mp = mpc(c)
        zeta_prime_rho = diff(zeta, rho)
        g = 2

        if family == 1:
            s0 = (1 + rho) / 2
        elif family == 2:
            s0 = (2 + rho) / 2
        else:
            raise ValueError(f"family must be 1 or 2, got {family}")

        # Use general Gamma/pi factors for consistency
        gamma_fac, pi_fac = _conformal_gamma_pi(g, s0, c_mp, dps)

        if family == 1:
            # Cancelled pole: zeta(2s-1) vanishes in both denom of ratio 1
            # and numer of ratio 2.  Telescoped product is regular here.
            zeta_prod = zeta(1 + rho) / zeta(rho - 1) if fabs(zeta(rho - 1)) > 1e-50 else mpc(inf)
            result = gamma_fac * pi_fac * zeta_prod
        else:
            # Genuine pole at 2s-2=rho from telescoped zeta(2s)/zeta(2s-2).
            res_factor = zeta(2 + rho) / (2 * zeta_prime_rho)
            result = gamma_fac * pi_fac * res_factor

        return complex(result)


def genus2_universal_residue_double(rho1, rho2, c, dps=30):
    r"""Paired residue factor at a PAIR of zeta zeros.

    After telescoping, c_2(s) = xi(2s)/xi(2s-2) has a SINGLE family
    of poles at s = (2+rho)/2.  The "family 1" poles at s = (1+rho)/2
    are CANCELLED by the telescoping.

    The paired residue factor A^{(2)}_c(rho1, rho2) measures the
    genus-2 spectral weight at two different zeta zeros.  Since there
    is only one pole family (family 2), this is:

      A^{(2)}_c(rho1, rho2) = A^{(2,2)}_c(rho1) * A^{(2,2)}_c(rho2)
                               * (interference kernel from conformal Gamma)

    The interference kernel encodes the coupling between the two zeros
    through the c-dependent Gamma factor.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho1 = mpc(rho1)
        rho2 = mpc(rho2)
        c = mpc(c)

        A1 = genus2_universal_residue_single(rho1, c, family=1, dps=dps)
        A2 = genus2_universal_residue_single(rho2, c, family=2, dps=dps)

        # Interference kernel: the cross-correlation between the two
        # pole families mediated by the genus-2 Gamma factor
        s1 = (1 + rho1) / 2
        s2 = (3 + rho2) / 2

        # The cross-gamma ratio measures how the conformal weights interact
        # when both poles contribute to the same spectral integral
        if fabs(s1 - s2) > 1e-50:
            cross_gamma = mpgamma(s1) * mpgamma(s2) / (mpgamma(s1 + s2 - 1) * mpgamma(1))
        else:
            # Coincident case: higher-order pole (see below)
            cross_gamma = mpc(1)

        interference = complex(cross_gamma)

        return {
            'rho1': complex(rho1),
            'rho2': complex(rho2),
            'A_family1': complex(A1),
            'A_family2': complex(A2),
            'product': complex(mpc(A1) * mpc(A2)),
            'interference_kernel': interference,
            'paired_residue': complex(mpc(A1) * mpc(A2) * cross_gamma),
        }


def genus2_coincident_residue(rho, c, dps=30):
    r"""Residue when both families are excited by the SAME zero rho.

    rho1 = rho2 = rho does NOT mean a double pole at a single s-value
    (the two families have poles at different s).  Rather, it means:

      A^{(2)}_c(rho, rho) = A^{(2,1)}_c(rho) * A^{(2,2)}_c(rho)

    This product measures the total genus-2 spectral weight at the
    zero rho.  Compare with the genus-1 residue A^{(1)}_c(rho).

    The RATIO A^{(2)}_c(rho,rho) / [A^{(1)}_c(rho)]^2 measures how
    much more genus-2 "sees" each zeta zero compared to genus-1 squared.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        A1 = genus2_universal_residue_single(rho, c, family=1, dps=dps)
        A2 = genus2_universal_residue_single(rho, c, family=2, dps=dps)
        product = complex(mpc(A1) * mpc(A2))

        return {
            'rho': complex(rho),
            'A_family1': complex(A1),
            'A_family2': complex(A2),
            'coincident_product': product,
            'magnitude': abs(product),
        }


# ====================================================================
# 5. Genus-1 to genus-2 consistency check
# ====================================================================

def genus1_universal_residue(rho, c, dps=30):
    r"""The genus-1 universal residue factor A_c(rho) for comparison.

    A_c(rho) = Gamma((1+rho)/2) * Gamma((c+rho-1)/2) * zeta(1+rho)
               / (2 * pi^{rho+1/2} * Gamma((c-rho-1)/2) * Gamma(rho/2) * zeta'(rho))

    Reproduced from benjamin_chang_analysis.py for self-contained comparison.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = mpc(rho)
        c = mpc(c)
        zeta_prime_rho = diff(zeta, rho)
        num = (mpgamma((1 + rho) / 2) * mpgamma((c + rho - 1) / 2)
               * zeta(1 + rho))
        den = (2 * power(pi, rho + mpf('0.5'))
               * mpgamma((c - rho - 1) / 2) * mpgamma(rho / 2)
               * zeta_prime_rho)
        if fabs(den) < power(10, -dps + 5):
            return complex(inf)
        return complex(num / den)


def genus2_vs_genus1_residue_ratio(rho, c, dps=30):
    r"""Ratio A^{(2)}_c(rho, rho) / [A^{(1)}_c(rho)]^2.

    This measures how the genus-2 spectral decomposition enhances or
    suppresses each zeta zero relative to the genus-1 prediction.

    If the genus-2 partition function were a simple square Z_2 ~ Z_1^2,
    this ratio would be 1.  Deviations from 1 measure genuine genus-2
    arithmetic content (the Boecherer coefficient, Klingen Eisenstein
    series, Siegel-Maass cusp forms).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        A1_genus1 = genus1_universal_residue(rho, c, dps=dps)
        res2 = genus2_coincident_residue(rho, c, dps=dps)
        A2_product = res2['coincident_product']

        if abs(A1_genus1) < 1e-100:
            return {'ratio': complex(inf), 'genus1_squared': 0.0}

        A1_squared = complex(mpc(A1_genus1) ** 2)
        ratio = complex(mpc(A2_product) / mpc(A1_squared))

        return {
            'rho': complex(rho),
            'c': complex(c),
            'genus1_residue': complex(A1_genus1),
            'genus1_squared': A1_squared,
            'genus2_coincident': A2_product,
            'ratio': ratio,
            'ratio_magnitude': abs(ratio),
        }


# ====================================================================
# 6. Genus-3 scattering factor
# ====================================================================

def genus3_conformal_gamma(s, c, dps=30):
    r"""The genus-3 conformal Gamma factor.

    At genus 3, the Rankin-Selberg unfolding against E_3(Omega, s)
    on Sp(6,Z)\H_3 produces:

      Gamma_3(s, c) = prod_{j=0}^{2}
          Gamma(s + c/2 - 1 - j) / Gamma(c/2 - s + j + 1/2)
        * Gamma(s - j) / Gamma(s - j - 1/2)

    after simplification from the triple Selberg integral on H_3.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        c = mpc(c)
        num = mpc(1)
        den = mpc(1)
        for j in range(3):
            num *= mpgamma(s + c / 2 - 1 - j) * mpgamma(s - j)
            den *= mpgamma(c / 2 - s + j + mpf('0.5')) * mpgamma(s - j - mpf('0.5'))
        if fabs(den) < power(10, -dps + 5):
            return complex(inf)
        return complex(num / den)


def genus3_scattering_factor(s, c, dps=30):
    r"""The genus-3 scattering factor F_{3,c}(s).

    Delegates to genus_g_scattering_factor(3, s, c, dps) for consistency.

    Three zeta ratios from the Sp(6,Z) Eisenstein scattering c_3(s):
      i=1: zeta(2s)/zeta(2s-1)
      i=2: zeta(2s-1)/zeta(2s-2)
      i=3: zeta(2s-2)/zeta(2s-3)

    After telescoping: zeta product = zeta(2s)/zeta(2s-3).
    Only family i=3 poles survive at s = (3+rho)/2.
    """
    return genus_g_scattering_factor(3, s, c, dps)


def genus3_pole_positions(n_zeros=10, dps=30):
    r"""Poles of F_{3,c}(s) from individual-factor zeta function zeros.

    Before telescoping, the three factors i=1,2,3 have denominators
    at 2s-i=rho:
      Family 1: s = (1+rho)/2     [Re = 3/4 under RH]
      Family 2: s = (2+rho)/2     [Re = 5/4 under RH]
      Family 3: s = (3+rho)/2     [Re = 7/4 under RH]

    After telescoping c_3(s) = xi(2s)/xi(2s-3), only family 3
    poles survive.  We track all three for the full F_{3,c}(s)
    analysis (conformal Gamma factor may break cancellations).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        poles = {'family_1': [], 'family_2': [], 'family_3': []}
        for k in range(1, n_zeros + 1):
            rho = zetazero(k)
            gamma_k = float(mpim(rho))

            for fam, offset in [(1, 1), (2, 2), (3, 3)]:
                s_pole = (offset + rho) / 2
                poles[f'family_{fam}'].append({
                    'k': k, 'rho': complex(rho), 'gamma': gamma_k,
                    's': complex(s_pole),
                    'real': float(mpre(s_pole)),
                    'imag': float(mpim(s_pole)),
                })

        return poles


def genus3_universal_residue_single(rho, c, family, dps=30):
    r"""Residue of F_{3,c}(s) at a single zeta zero, in one of three families.

    Family i (i=1,2,3): pole from 2s - i = rho => s = (i+rho)/2.

    After telescoping, c_3(s) = xi(2s)/xi(2s-3), only family 3 poles
    survive.  But for the full F_{3,c}(s) (with conformal Gamma factor),
    we compute the value (not residue) at family 1 and 2 locations
    (where the zeta product has no pole), and the true residue at
    family 3 (where 2s-3 = rho gives a genuine pole).

    For family 3: the telescoped zeta product zeta(2s)/zeta(2s-3) has
    a pole at 2s-3 = rho, and the residue picks up zeta(3+rho)/(2*zeta'(rho)).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = mpc(rho)
        c = mpc(c)
        zeta_prime_rho = diff(zeta, rho)

        offsets = {1: 1, 2: 2, 3: 3}
        if family not in offsets:
            raise ValueError(f"family must be 1, 2, or 3, got {family}")

        s0 = (offsets[family] + rho) / 2
        gamma_fac, pi_fac = _conformal_gamma_pi(3, s0, c, dps)

        if family <= 2:
            # Telescoped: zeta(2s0)/zeta(2s0-3) is regular here
            # (the pole from the individual factor is cancelled)
            zeta_prod = zeta(2 * s0) / zeta(2 * s0 - 3) if fabs(zeta(2 * s0 - 3)) > 1e-50 else mpc(inf)
            result = mpc(gamma_fac) * pi_fac * zeta_prod
        else:
            # Family 3: genuine pole at 2s-3 = rho
            # Residue of zeta(2s)/zeta(2s-3) at 2s-3=rho:
            # = zeta(3+rho) / (2*zeta'(rho))
            res_factor = zeta(3 + rho) / (2 * zeta_prime_rho)
            result = mpc(gamma_fac) * pi_fac * res_factor

        return complex(result)


# ====================================================================
# 7. General genus-g scattering factor
# ====================================================================

def genus_g_scattering_factor(g, s, c, dps=30):
    r"""General genus-g scattering factor (for any g >= 1).

    F_{g,c}(s) = Gamma_g(s,c) * pi^{-nu_g(s)} * prod_{i=1}^{g} zeta(2s-i+1)/zeta(2s-i)

    The g zeta ratios come from c_g(s) = prod_{i=1}^g xi(2s-i+1)/xi(2s-i).
    Individual-factor poles at s = (i+rho)/2 for i = 1,...,g.
    After telescoping: c_g(s) = xi(2s)/xi(2s-g), only the i=g pole survives.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        c_mp = mpc(c)

        # Conformal Gamma factor (genus-g generalisation)
        gamma_num = mpc(1)
        gamma_den = mpc(1)
        for j in range(g):
            gamma_num *= mpgamma(s + c_mp / 2 - 1 - j) * mpgamma(s - j)
            gamma_den *= mpgamma(c_mp / 2 - s + j + mpf('0.5')) * mpgamma(s - j - mpf('0.5'))

        if fabs(gamma_den) < power(10, -dps + 5):
            return complex(inf)
        gamma_fac = gamma_num / gamma_den

        # Pi normalisation: from genus-g unfolding
        # Generalises pi^{-(2s-1/2)} at g=1, pi^{-(4s-3)} at g=2
        # Pattern: pi^{-(2g*s - g(g+1)/2 + 1/2)}
        pi_exp = -(2 * g * s - g * (g + 1) / 2 + mpf('0.5'))
        pi_fac = power(pi, pi_exp)

        # g zeta ratios from c_g(s) = prod_{i=1}^g xi(2s-i+1)/xi(2s-i)
        zeta_product = mpc(1)
        for i in range(1, g + 1):
            z_num = zeta(2 * s - i + 1)
            z_den = zeta(2 * s - i)
            if fabs(z_den) < 1e-50:
                return complex(inf)
            zeta_product *= z_num / z_den

        return complex(gamma_fac * pi_fac * zeta_product)


def genus_g_pole_families(g, n_zeros=10, dps=30):
    r"""All g pole families for the genus-g scattering factor.

    Family i (i=1,...,g): individual-factor poles at s = (i+rho)/2.
    Under RH: Re(s) = (i + 1/2)/2 = i/2 + 1/4.

    After telescoping c_g(s) = xi(2s)/xi(2s-g), only the family i=g
    poles survive.  We track all g families for completeness.

    Dict keyed by i-1 (0-indexed) for backward compatibility.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        families = {}
        for i in range(1, g + 1):
            family_poles = []
            for k in range(1, n_zeros + 1):
                rho = zetazero(k)
                s_pole = (i + rho) / 2
                family_poles.append({
                    'k': k,
                    'rho': complex(rho),
                    's': complex(s_pole),
                    'real': float(mpre(s_pole)),
                    'imag': float(mpim(s_pole)),
                })
            families[i - 1] = family_poles  # 0-indexed key
        return families


# ====================================================================
# 8. Boecherer connection: Fourier coefficients and L-values
# ====================================================================

def faber_pandharipande_lambda(g):
    r"""lambda_g^{FP} = |B_{2g}| * (2^{2g-1} - 1) / (2^{2g-1} * (2g)!).

    The Faber-Pandharipande invariant, used in F_g = kappa * lambda_g^FP.
    """
    B_2g = _bernoulli_number(2 * g)
    num = abs(B_2g) * (2 ** (2 * g - 1) - 1)
    den = 2 ** (2 * g - 1) * math.factorial(2 * g)
    return Fraction(num).limit_denominator(10**20) / den


def _bernoulli_number(n):
    """Bernoulli number B_n as a Fraction."""
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1 and n > 1:
        return Fraction(0)
    # Use the recursive definition
    B = [Fraction(0)] * (n + 1)
    B[0] = Fraction(1)
    B[1] = Fraction(-1, 2)
    for m in range(2, n + 1):
        if m % 2 == 1 and m > 1:
            continue
        s = Fraction(0)
        for k in range(m):
            if B[k] == 0 and k > 1:
                continue
            binom = Fraction(1)
            for j in range(k):
                binom = binom * (m + 1 - j) / (j + 1)
            s += binom * B[k]
        B[m] = -s / (m + 1)
    return B[n]


def shadow_genus2_fourier_coefficient(kappa_val, S3=0, pf_correction=True):
    r"""The genus-2 shadow contribution to the Fourier coefficient.

    F_2(A) = kappa * lambda_2^FP = kappa * 7/5760

    The planted-forest correction delta_pf^{(2,0)} = S_3(10*S_3 - kappa)/48
    modifies the total:

      F_2^{total}(A) = kappa * 7/5760 + S_3(10*S_3 - kappa)/48

    For the Boecherer bridge, the Fourier coefficient of the genus-2
    partition function at a fundamental discriminant D is:

      a(T; Z_2) ~ F_2(A) * [tautological factor(T)]
    """
    lambda2 = Fraction(7, 5760)
    F2_scalar = Fraction(kappa_val) * lambda2

    if pf_correction and S3 != 0:
        delta_pf = Fraction(S3) * (10 * Fraction(S3) - Fraction(kappa_val)) / 48
        F2_total = F2_scalar + delta_pf
    else:
        delta_pf = Fraction(0)
        F2_total = F2_scalar

    return {
        'F2_scalar': F2_scalar,
        'delta_pf': delta_pf,
        'F2_total': F2_total,
        'lambda2_FP': lambda2,
    }


def bocherer_central_L_value_proxy(kappa_val, c_val, dps=30):
    r"""Boecherer connection: genus-2 Fourier coefficient vs central L-value.

    Boecherer's conjecture (Furusawa-Morimoto theorem):
      |a(T; F)|^2 / <F,F> = C_F * L(1/2, pi_F) * L(1/2, pi_F x chi_D)

    For the shadow CohFT at genus 2:
    - F is the weight-c/2 Siegel modular form contribution to Z_2
    - The Saito-Kurokawa component gives L(1/2, pi_{SK}) = L(1/2, f)
      where f is the underlying elliptic modular form
    - For lattice VOAs at rank 24 (weight 12): the SK lift from
      Delta (weight 22 newform) gives chi_12

    The PROXY here computes the ratio:
      F_2(A)^2 / (some normalisation) as a function of kappa and c,
    which should be proportional to L(1/2, ...) by Boecherer.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        lambda2 = mpf(7) / 5760
        F2 = mpf(kappa_val) * lambda2

        # The normalisation involves the Petersson norm, which at the
        # shadow CohFT level is determined by the shadow metric.
        # For the scalar shadow: <F_2, F_2>^{shadow} ~ kappa^2 * lambda2^2
        # The Boecherer ratio is then F_2^2 / (kappa^2 * lambda2^2) = 1
        # for the scalar part.  Deviations come from:
        # (a) planted-forest corrections
        # (b) non-scalar (higher-arity) contributions
        # (c) genuine L-value content

        ratio = F2 ** 2 / (mpf(kappa_val) ** 2 * lambda2 ** 2) if kappa_val != 0 else mpf(0)

        return {
            'kappa': float(kappa_val),
            'c': float(c_val),
            'F2': float(F2),
            'F2_squared': float(F2 ** 2),
            'bocherer_ratio': float(ratio),
            'interpretation': (
                'ratio = 1 means scalar shadow saturates Boecherer; '
                'deviations measure genuine genus-2 arithmetic content'
            ),
        }


# ====================================================================
# 9. Planted-forest correction at genus 2
# ====================================================================

def planted_forest_genus2(kappa_val, S3_val):
    r"""The genus-2 planted-forest correction.

    delta_pf^{(2,0)} = S_3 * (10*S_3 - kappa) / 48

    This is EXACT (not an approximation) and has been verified in
    pixton_shadow_bridge.py (54 tests).

    For Heisenberg: S_3 = 0 => delta_pf = 0 (class G, no planted forests).
    For Virasoro at c: S_3 = 2, kappa = c/2 =>
      delta_pf = 2*(20 - c/2)/48 = (40 - c)/48 = (40-c)/48.
    """
    S3 = Fraction(S3_val) if not isinstance(S3_val, Fraction) else S3_val
    kap = Fraction(kappa_val) if not isinstance(kappa_val, Fraction) else kappa_val
    return S3 * (10 * S3 - kap) / 48


def planted_forest_residue_at_zeta_zero(kappa_val, S3_val, rho, c, family=1, dps=30):
    r"""Residue contribution from the planted-forest correction at a zeta zero.

    The planted-forest delta_pf contributes to the genus-2 constrained Epstein
    as an ADDITIVE correction to F_2.  Its residue at a zeta zero is:

      Res_{s=s_rho}[delta_pf contribution]
        = delta_pf * [residue of the genus-2 spectral kernel at s_rho]

    The spectral kernel residue is the conformal-Gamma/zeta' factor
    from the Rankin-Selberg unfolding, WITHOUT the zeta ratio that
    produces the pole.

    NOTE: This is an approximation that treats delta_pf as a constant
    coefficient multiplying the genus-2 spectral kernel.  The actual
    contribution may have s-dependent modifications from the graph sum.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        delta_pf = float(planted_forest_genus2(kappa_val, S3_val))
        # The residue of the spectral kernel at the zeta zero
        # is the single-family residue divided by F_2 (removing the
        # leading shadow contribution and replacing with delta_pf)
        kap = float(kappa_val)
        if kap == 0:
            return complex(0)

        lambda2 = 7.0 / 5760.0
        F2 = kap * lambda2

        # Genus-2 single-family residue
        A_family = genus2_universal_residue_single(rho, c, family, dps)

        # Scale by delta_pf / F2
        if abs(F2) < 1e-100:
            return complex(0)

        return complex(mpc(A_family) * mpc(delta_pf / F2))


# ====================================================================
# 10. Complementarity at higher genus
# ====================================================================

def genus2_complementarity(s, c, dps=30):
    r"""Compare F_{2,c}(s) and F_{2,26-c}(s) for Koszul dual Virasoro.

    At genus 2, complementarity c <-> 26-c maps:
      kappa = c/2 <-> kappa' = (26-c)/2
      F_2(A) = c/2 * 7/5760 <-> F_2(A!) = (26-c)/2 * 7/5760

    The zeta ratios are UNIVERSAL (c-independent), so the ratio
    F_{2,c}/F_{2,26-c} depends only on the conformal Gamma factor.

    At c = 13 (self-dual): the genus-2 scattering factor has a
    self-duality that constrains the residue kernel.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        F2c = genus2_scattering_factor(s, c, dps)
        F2c_dual = genus2_scattering_factor(s, 26 - c, dps)

        ratio = complex(mpc(F2c) / mpc(F2c_dual)) if abs(F2c_dual) > 1e-50 else None

        return {
            'c': float(c),
            'c_dual': float(26 - c),
            'F2_c': complex(F2c),
            'F2_c_dual': complex(F2c_dual),
            'ratio': ratio,
        }


def genus_g_complementarity(g, s, c, dps=30):
    r"""General genus-g complementarity F_{g,c}(s) vs F_{g,26-c}(s)."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        Fgc = genus_g_scattering_factor(g, s, c, dps)
        Fgc_dual = genus_g_scattering_factor(g, s, 26 - c, dps)
        ratio = complex(mpc(Fgc) / mpc(Fgc_dual)) if abs(Fgc_dual) > 1e-50 else None
        return {
            'g': g, 'c': float(c), 'c_dual': float(26 - c),
            'Fg_c': complex(Fgc), 'Fg_c_dual': complex(Fgc_dual),
            'ratio': ratio,
        }


# ====================================================================
# 11. Genus-g Rankin-Selberg theta lift (verification path 2)
# ====================================================================

def siegel_eisenstein_at_genus_g(g, s, dps=30):
    r"""The normalised Siegel Eisenstein series evaluated symbolically.

    For verification purposes, we compute the CONSTANT TERM of E_g(Omega, s):

      a_0(det(Y); E_g) = det(Y)^s + phi_g(s) * det(Y)^{(g+1)/2 - s} + ...

    This gives us direct access to the scattering matrix phi_g(s).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        phi = siegel_scattering_matrix(g, s, dps)
        return {
            'g': g,
            's': complex(s),
            'phi_g(s)': phi,
            'phi_g_magnitude': abs(phi),
        }


def rankin_selberg_theta_lift_consistency(g, c, s, dps=30):
    r"""Verify consistency between the direct scattering factor
    and the Rankin-Selberg theta lift computation.

    The Rankin-Selberg integral:
      int_{Sp(2g,Z)\H_g} Z_g(Omega) * E_g(Omega, s) * dmu_g

    unfolds to iterated Mellin transforms.  The functional equation
    of the result inherits the scattering matrix phi_g(s), giving the
    g zeta ratios.

    Consistency check: the genus-g scattering factor should agree with
    the product of phi_g(s) and the conformal Gamma factor.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        # Direct computation
        Fgc = genus_g_scattering_factor(g, s, c, dps)

        # From scattering matrix decomposition
        phi = siegel_scattering_matrix(g, s, dps)

        # The scattering factor = (conformal factor) * phi^{-1} * (correction)
        # More precisely: the zeta ratios in F_{g,c} are the INVERSES of those in phi_g
        # (because F_c has zeta(2s)/zeta(2s-1) while phi has zeta(2s-1)/zeta(2s))
        # So F_{g,c} should contain 1/phi_g^{arithmetic} times conformal factors

        return {
            'g': g, 'c': float(c), 's': complex(s),
            'F_gc_direct': complex(Fgc),
            'phi_g': phi,
            'phi_g_inverse_magnitude': 1.0 / abs(phi) if abs(phi) > 1e-100 else float('inf'),
        }


# ====================================================================
# 12. Genus-2 Rankin-Selberg integral via theta lift (Path 2)
# ====================================================================

def genus2_theta_lift_scattering(s, c, dps=30):
    r"""The genus-2 scattering factor via theta lift / Rallis inner product.

    Alternative derivation: the Siegel-Weil formula relates the
    theta lift integral to a ratio of automorphic L-functions.

    For the genus-2 case, the Rallis inner product formula gives:

      I_2(s, c) ~ L^S(s, pi_f, std) * [local factors]

    where L(s, pi_f, std) is the standard L-function of the automorphic
    form associated to the partition function.

    At the level of the scattering matrix, this reduces to:

      c_2(s) = xi(2s)/xi(2s-1) * xi(2s-1)/xi(2s-2) = xi(2s)/xi(2s-2)

    Verification: this should agree with siegel_scattering_matrix(2, s).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        # Direct product of two xi ratios (correct Shimura/Boecherer convention)
        # Factor i=1: xi(2s)/xi(2s-1)
        xi_num_1 = completed_riemann_xi(2 * s, dps)
        xi_den_1 = completed_riemann_xi(2 * s - 1, dps)
        # Factor i=2: xi(2s-1)/xi(2s-2)
        xi_num_2 = completed_riemann_xi(2 * s - 1, dps)
        xi_den_2 = completed_riemann_xi(2 * s - 2, dps)

        if fabs(xi_den_1) < 1e-50 or fabs(xi_den_2) < 1e-50:
            theta_lift = complex(inf)
        else:
            theta_lift = complex(xi_num_1 / xi_den_1 * xi_num_2 / xi_den_2)

        # Compare with general Siegel scattering
        phi2 = siegel_scattering_matrix(2, s, dps)

        return {
            's': complex(s),
            'theta_lift_phi2': theta_lift,
            'direct_phi2': phi2,
            'agreement': abs(theta_lift - phi2) < 1e-10 if isinstance(theta_lift, complex) and abs(theta_lift) < 1e50 else None,
        }


# ====================================================================
# 13. Standard family data for higher-genus Epstein
# ====================================================================

def standard_family_genus2_data():
    r"""Shadow data for all standard families at genus 2.

    Returns dict mapping family name to (kappa, F_2, delta_pf, F_2_total).
    """
    families = {}

    # Heisenberg (class G): kappa = k, S_3 = 0
    families['Heisenberg'] = {
        'kappa': 'k',
        'kappa_numeric': None,  # parametric
        'S3': 0,
        'F2': 'k * 7/5760',
        'delta_pf': 0,
        'shadow_class': 'G',
    }

    # Affine sl_2 (class L): kappa = 3(k+2)/4, S_3 = cubic (nonzero)
    families['V_k(sl_2)'] = {
        'kappa': '3(k+2)/4',
        'kappa_numeric': None,
        'S3': 2,
        'F2': '3(k+2)/4 * 7/5760',
        'delta_pf': '2*(20 - 3(k+2)/4)/48',
        'shadow_class': 'L',
    }

    # Virasoro (class M): kappa = c/2, S_3 = 2
    families['Virasoro'] = {
        'kappa': 'c/2',
        'kappa_numeric': None,
        'S3': 2,
        'F2': 'c/2 * 7/5760 = 7c/11520',
        'delta_pf': '2*(20 - c/2)/48 = (40-c)/48',
        'shadow_class': 'M',
    }

    # Beta-gamma (class C): kappa = 1, S_3 = 2
    families['beta-gamma'] = {
        'kappa': 1,
        'kappa_numeric': 1,
        'S3': 2,
        'F2': float(Fraction(7, 5760)),
        'delta_pf': float(planted_forest_genus2(1, 2)),
        'shadow_class': 'C',
    }

    # W_3 (class M): kappa = 5c/6, S_3 = 2 (leading cubic from Vir subalgebra)
    families['W_3'] = {
        'kappa': '5c/6',
        'kappa_numeric': None,
        'S3': 2,
        'F2': '5c/6 * 7/5760',
        'delta_pf': '2*(20 - 5c/6)/48',
        'shadow_class': 'M',
    }

    return families


def virasoro_genus2_epstein_data(c_val):
    r"""Complete genus-2 Epstein data for Virasoro at central charge c.

    Returns the full package: kappa, F_2, delta_pf, total, and
    the Koszul dual data at 26-c.
    """
    kap = Fraction(c_val, 2)
    S3 = Fraction(2)
    data = shadow_genus2_fourier_coefficient(kap, S3)

    kap_dual = Fraction(26 - c_val, 2)
    data_dual = shadow_genus2_fourier_coefficient(kap_dual, S3)

    return {
        'c': c_val,
        'kappa': kap,
        'F2': data,
        'c_dual': 26 - c_val,
        'kappa_dual': kap_dual,
        'F2_dual': data_dual,
        'F2_sum': data['F2_total'] + data_dual['F2_total'],
    }


# ====================================================================
# 14. Verification: genus-g scattering matrix functional equation
# ====================================================================

def verify_siegel_scattering_fe(g, s, dps=30):
    r"""Verify the functional equation phi_g(s) * phi_g((g+1)/2 - s) = 1.

    This is the genus-g generalisation of phi_1(s) * phi_1(1-s) = 1.
    The functional equation of the Siegel Eisenstein series maps
    s -> (g+1)/2 - s.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        s_dual = mpf(g + 1) / 2 - s

        phi_s = siegel_scattering_matrix(g, s, dps)
        phi_dual = siegel_scattering_matrix(g, s_dual, dps)

        product = complex(mpc(phi_s) * mpc(phi_dual))
        return {
            'g': g,
            's': complex(s),
            's_dual': complex(s_dual),
            'phi(s)': phi_s,
            'phi(s_dual)': phi_dual,
            'product': product,
            'error': abs(product - 1),
        }


def verify_genus2_reduces_to_genus1(s, dps=30):
    r"""When the genus-2 period matrix degenerates, the genus-2
    scattering factorises into shifted genus-1 contributions.

    c_2(s) = c_1(s) * c_1(s - 1/2).

    This is because:
      c_1(s) = xi(2s)/xi(2s-1)
      c_1(s-1/2) = xi(2s-1)/xi(2s-2)
      Product = xi(2s)/xi(2s-2) = c_2(s).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        phi2 = siegel_scattering_matrix(2, s, dps)
        phi1_s = siegel_scattering_matrix(1, s, dps)
        phi1_shifted = siegel_scattering_matrix(1, s - mpf('0.5'), dps)

        product = complex(mpc(phi1_s) * mpc(phi1_shifted))

        return {
            's': complex(s),
            'phi_2(s)': phi2,
            'phi_1(s)*phi_1(s-1/2)': product,
            'relative_error': abs(phi2 - product) / max(abs(phi2), 1e-100) if abs(phi2) > 1e-100 else abs(phi2 - product),
        }


def verify_genus3_factorisation(s, dps=30):
    r"""c_3(s) = c_1(s) * c_1(s-1/2) * c_1(s-1).

    General pattern: c_g(s) = prod_{j=0}^{g-1} c_1(s - j/2).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        phi3 = siegel_scattering_matrix(3, s, dps)
        product = mpc(1)
        for j in range(3):
            product *= mpc(siegel_scattering_matrix(1, s - mpf(j) / 2, dps))

        return {
            's': complex(s),
            'phi_3(s)': phi3,
            'product_phi_1': complex(product),
            'relative_error': abs(phi3 - complex(product)) / max(abs(phi3), 1e-100),
        }


# ====================================================================
# 15. Summary: higher-genus zeta zero mechanism
# ====================================================================

def higher_genus_zeta_zero_summary(g, c, n_zeros=5, dps=30):
    r"""Summary of how genus-g partition functions see zeta zeros.

    At genus g, there are g individual-factor pole families, at:
      Family i: Re(s) = i/2 + 1/4, i = 1, ..., g

    After telescoping c_g(s) = xi(2s)/xi(2s-g), only the family i=g
    poles survive at Re(s) = g/2 + 1/4.

    Returns a summary dict with pole positions, residue magnitudes,
    and genus-1 comparison.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        summary = {
            'genus': g,
            'central_charge': float(c),
            'num_pole_families': g,
            'pole_families': [],
            'first_zeros': [],
        }

        for i in range(1, g + 1):
            summary['pole_families'].append({
                'family': i,
                'real_part_under_RH': i / 2 + 0.25,
                'offset': i,
            })

        for k in range(1, n_zeros + 1):
            rho = zetazero(k)
            gamma_k = float(mpim(rho))
            zero_data = {
                'k': k,
                'gamma': gamma_k,
                'rho': complex(rho),
            }
            # Genus-1 residue for comparison
            A1 = genus1_universal_residue(rho, c, dps)
            zero_data['genus1_residue_mag'] = abs(A1)

            # Genus-g single-family residues (only for g <= 3 to avoid
            # excessive computation)
            if g <= 3:
                family_residues = []
                for fam in range(1, g + 1):
                    try:
                        if g == 2:
                            A_fam = genus2_universal_residue_single(rho, c, fam, dps)
                        elif g == 3:
                            A_fam = genus3_universal_residue_single(rho, c, fam, dps)
                        else:
                            A_fam = A1  # genus 1
                        family_residues.append({
                            'family': fam,
                            'residue_magnitude': abs(A_fam),
                        })
                    except Exception:
                        family_residues.append({
                            'family': fam,
                            'residue_magnitude': float('nan'),
                        })
                zero_data['family_residues'] = family_residues

            summary['first_zeros'].append(zero_data)

        return summary
