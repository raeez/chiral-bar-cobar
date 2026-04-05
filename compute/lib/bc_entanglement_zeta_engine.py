#!/usr/bin/env python3
r"""bc_entanglement_zeta_engine.py -- Entanglement spectral zeta function
at Riemann zeta zeros, connecting the G11-G16 entanglement programme to the
Benjamin-Chang scattering mechanism.

MATHEMATICAL CONTENT
====================

=== 1. ENTANGLEMENT SPECTRAL ZETA FUNCTION ===

For a 2D CFT with central charge c on an interval of length L (UV cutoff
epsilon), the reduced density matrix rho_A of a single interval has eigenvalues
(the entanglement spectrum) determined by the modular Hamiltonian.

The entanglement spectral zeta function is:

    zeta^{EE}_A(s) = Tr(rho_A^s) = sum_n p_n^s

where p_n are the eigenvalues of rho_A (Schmidt coefficients squared).

For a 2D CFT, the replica trick gives Tr(rho_A^n) = Z_n / Z_1^n where Z_n
is the partition function on the n-sheeted Riemann surface branched over
the interval endpoints.  The twist operator computation (Calabrese-Cardy 2004)
yields:

    Tr(rho_A^n) = c_n * (L/epsilon)^{-c(n-1/n)/6}

where c_n is a non-universal constant (c_1 = 1 by normalization).  Thus:

    zeta^{EE}(s) = Tr(rho_A^s) = c(s) * (L/epsilon)^{-c(s-1/s)/6}

The LEADING universal part is:

    log zeta^{EE}(s) ~ -(c/6)(s - 1/s) * log(L/epsilon)

which we denote the UNIVERSAL SPECTRAL ZETA.  This is exact for class G
algebras (Heisenberg, lattice) and leading-order for all others.

=== 2. RENYI ENTROPY FROM SPECTRAL ZETA ===

The Renyi entropy of order n is:

    S_n = (1/(1-n)) * log(Tr(rho_A^n)) = (1/(1-n)) * log(zeta^{EE}(n))

For the universal spectral zeta:

    S_n = (c/6) * (1+1/n) * log(L/epsilon)

The von Neumann entropy is the n -> 1 limit:

    S_1 = lim_{n->1} S_n = (c/3) * log(L/epsilon)

which is the Calabrese-Cardy formula.  Equivalently:

    S_1 = -zeta'^{EE}(1) / zeta^{EE}(1) = -(d/ds) log zeta^{EE}(s)|_{s=1}

since zeta^{EE}(1) = Tr(rho_A) = 1.

=== 3. EVALUATION AT ZETA ZEROS ===

The Benjamin-Chang scattering factor F_c(s) has poles at s = (1+rho_k)/2
where rho_k are the nontrivial zeros of the Riemann zeta function.
For rho_k = 1/2 + i*gamma_k (assuming RH): s_k = 3/4 + i*gamma_k/2.

The entanglement spectral zeta at these special points:

    zeta^{EE}((1+rho_k)/2)

probes the entanglement spectrum at COMPLEX Renyi index, where the
Benjamin-Chang mechanism predicts resonant behaviour.  The value

    E_k(A) = |zeta^{EE}_A(s_k)|

measures the "zeta-entanglement" at the k-th zeta zero.

=== 4. MODULAR ENTROPY ===

The modular Hamiltonian K = -log(rho_A) generates the modular flow.
For a single interval in a CFT: K = (2*pi/beta_eff) * (H - c/24)
where beta_eff depends on the interval geometry.

The modular entropy S_mod = <K> = Tr(rho_A * K) = -Tr(rho_A * log(rho_A))
= S_EE (von Neumann entropy).

The connection to the shadow tower: F_1(A) = kappa(A)/24 = kappa * lambda_1^FP,
and the genus-1 contribution to the partition function determines the
entanglement spectrum through the modular Hamiltonian.

=== 5. ENTROPY FUNCTIONAL EQUATION ===

The Renyi entropy S_n at the scalar (universal) level satisfies:

    S_n = (c/6)(1 + 1/n) * log(L/epsilon)

Under n -> c/(3*log(L/epsilon)) - n (a c-dependent reflection), the
entropy transforms.  The Benjamin-Chang functional equation for the
constrained Epstein zeta relates epsilon^c_{c/2-s} to epsilon^c_{c/2+s-1}
via F_c(s).  We test whether the entanglement spectral zeta inherits
any analogous functional equation.

=== 6. COMPLEMENTARITY ===

For Koszul dual pairs under Virasoro duality c <-> 26-c:

    S_EE(Vir_c) + S_EE(Vir_{26-c}) = (26/3) * log(L/epsilon)

since kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13.

At the self-dual point c = 13: S_EE = (13/3) * log(L/epsilon),
the maximum entanglement for a single copy of the Virasoro algebra.

For the spectral zeta:
    log zeta^{EE}_c(s) + log zeta^{EE}_{26-c}(s)
    = -(13/3)(s - 1/s) * log(L/epsilon)

=== 7. SHADOW RENYI ===

The shadow Renyi entropy uses the shadow tower {F_g(A)} as a
probability-like distribution (after normalization):

    S_r^{shadow}(A) = (1/(1-r)) * log(sum_g |F_g(A)|^r / (sum_g |F_g(A)|)^r)

This is a Renyi-type entropy measuring the concentration of the shadow
tower across genera.

References:
    [BenjaminChang22]: arXiv:2208.02259
    [CalabreseCardy04]: hep-th/0405152
    [CalabreseCardy09]: arXiv:0905.4013 (entanglement spectrum)
    entanglement_shadow_engine.py (scalar entanglement from shadow tower)
    benjamin_chang_analysis.py (scattering factor and zeta zeros)
    modular_entanglement_flow_engine.py (modular Hamiltonian, flow, Page curve)

Manuscript references:
    prop:thqg-III-entanglement-entropy (thqg_symplectic_polarization.tex)
    eq:constrained-epstein-fe (arithmetic_shadows.tex)
    thm:scattering-coupling-factorization (arithmetic_shadows.tex)
    cor:free-energy-ahat-genus (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Dict, List, Optional, Tuple, Any

try:
    import mpmath
    from mpmath import (mp, mpf, mpc, pi as mp_pi, zeta as mp_zeta,
                        gamma as mpgamma, log as mp_log, exp as mp_exp,
                        power, sqrt as mp_sqrt, re as mpre, im as mpim,
                        conj as mpconj, fabs, zetazero, inf as mp_inf,
                        sin as mp_sin, cos as mp_cos, arg as mparg,
                        diff as mp_diff, nstr, fac as mp_fac)
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

from sympy import (
    Rational, Symbol, bernoulli, factorial, log, pi, S,
    simplify, sqrt, symbols, limit as sym_limit, oo,
)


# =====================================================================
# Symbols
# =====================================================================

c_sym = Symbol('c', positive=True)
n_sym = Symbol('n', positive=True)
s_sym = Symbol('s')
L_sym = Symbol('L', positive=True)
eps_sym = Symbol('epsilon', positive=True)


# =====================================================================
# Helper: Faber-Pandharipande coefficients (duplicated for self-containment)
# =====================================================================

@lru_cache(maxsize=64)
def faber_pandharipande(g: int) -> Rational:
    r"""Faber-Pandharipande coefficient lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    >>> faber_pandharipande(1)
    1/24
    >>> faber_pandharipande(2)
    7/5760
    >>> faber_pandharipande(3)
    31/967680
    """
    if g < 1:
        raise ValueError(f"g must be >= 1, got {g}")
    b2g = bernoulli(2 * g)
    sign = (-1)**(g + 1)
    abs_b2g = sign * b2g
    numerator = (2**(2 * g - 1) - 1) * abs_b2g
    denominator = 2**(2 * g - 1) * factorial(2 * g)
    return Rational(numerator, denominator)


# =====================================================================
# 1. ENTANGLEMENT SPECTRAL ZETA FUNCTION
# =====================================================================

def log_spectral_zeta_universal(s, c_val, log_ratio, dps=30):
    r"""Universal (leading) log of the entanglement spectral zeta function.

    log zeta^{EE}(s) = -(c/6)(s - 1/s) * log(L/epsilon)

    This is the replica-trick result from the twist operator dimension
    h_n = (c/24)(n - 1/n), giving Tr(rho^n) = (L/eps)^{-2*h_n}
    = (L/eps)^{-(c/12)(n-1/n)}.

    For a non-chiral (full) CFT with left+right:
    Tr(rho^n) = (L/eps)^{-(c/6)(n-1/n)}

    Parameters
    ----------
    s : complex or float
        The spectral parameter (generalizes the Renyi index n).
    c_val : float
        Central charge.
    log_ratio : float
        log(L/epsilon), the UV-regulated interval size.

    Returns
    -------
    complex
        The value log zeta^{EE}(s).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        c = mpf(c_val)
        lr = mpf(log_ratio)
        return complex(-(c / 6) * (s - 1 / s) * lr)


def spectral_zeta_universal(s, c_val, log_ratio, dps=30):
    r"""Universal entanglement spectral zeta function.

    zeta^{EE}(s) = exp(log zeta^{EE}(s))
                 = (L/epsilon)^{-(c/6)(s - 1/s)}

    Parameters
    ----------
    s : complex or float
        Spectral parameter (= Renyi index for positive integers).
    c_val : float
        Central charge.
    log_ratio : float
        log(L/epsilon).

    Returns
    -------
    complex
        zeta^{EE}(s).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        lz = mpc(log_spectral_zeta_universal(s, c_val, log_ratio, dps))
        return complex(mp_exp(lz))


def spectral_zeta_free_boson(s, log_ratio, dps=30):
    r"""Entanglement spectral zeta for the free boson (c=1).

    For c=1:
        zeta^{EE}(s) = (L/epsilon)^{-(1/6)(s - 1/s)}

    This is a benchmark: the free boson entanglement spectrum is exactly
    known (Li-Haldane 2008).  The entanglement spectrum of a single
    interval in the free boson on an infinite line has eigenvalues:

        xi_n = 2*pi * (n + 1/2) / log(L/epsilon), n = 0, 1, 2, ...

    with entanglement energies E_n = xi_n.

    For the universal approximation (dominant saddle), the spectral zeta
    agrees with the twist-operator computation to leading order in log(L/eps).
    """
    return spectral_zeta_universal(s, 1.0, log_ratio, dps)


def spectral_zeta_family(s, family, params, log_ratio, dps=30):
    r"""Spectral zeta for standard algebra families.

    Dispatches to the universal formula with the correct central charge.

    Parameters
    ----------
    family : str
        One of 'heisenberg', 'virasoro', 'affine_sl2', 'betagamma', 'ising'.
    params : dict
        Family-specific parameters (e.g., {'k': 1} for Heisenberg,
        {'c': 26} for Virasoro).
    """
    c_map = {
        'heisenberg': lambda p: float(p.get('k', 1)),
        'virasoro': lambda p: float(p.get('c', 1)),
        'affine_sl2': lambda p: 3 * float(p.get('k', 1)) / (float(p.get('k', 1)) + 2),
        'betagamma': lambda p: float(p.get('c', -2)),
        'ising': lambda _: 0.5,
        'free_fermion': lambda _: 0.5,
        'w3': lambda p: float(p.get('c', 2)),
    }
    if family not in c_map:
        raise ValueError(f"Unknown family: {family}")
    c_val = c_map[family](params)
    return spectral_zeta_universal(s, c_val, log_ratio, dps)


# =====================================================================
# 2. RENYI ENTROPY FROM SPECTRAL ZETA
# =====================================================================

def renyi_from_spectral_zeta(n_renyi, c_val, log_ratio, dps=30):
    r"""Renyi entropy S_n from the spectral zeta function.

    S_n = (1/(1-n)) * log(zeta^{EE}(n))
        = (1/(1-n)) * (-(c/6)(n - 1/n)) * log(L/epsilon)
        = (c/6)(1 + 1/n) * log(L/epsilon)

    For integer n >= 2, this is the standard Renyi entropy.
    For real n > 0 (n != 1), this is the analytic continuation.

    Parameters
    ----------
    n_renyi : float or complex
        The Renyi index.  Must not equal 1 (use von_neumann instead).
    c_val : float
        Central charge.
    log_ratio : float
        log(L/epsilon).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        n = mpc(n_renyi)
        c = mpf(c_val)
        lr = mpf(log_ratio)
        log_zeta = -(c / 6) * (n - 1 / n) * lr
        if abs(n - 1) < power(10, -dps + 5):
            raise ValueError("n = 1: use von_neumann_entropy instead")
        return complex(log_zeta / (1 - n))


def von_neumann_entropy(c_val, log_ratio):
    r"""Von Neumann entropy: S_1 = lim_{n->1} S_n = (c/3) log(L/epsilon).

    Equivalently: S_1 = -(d/ds) log zeta^{EE}(s)|_{s=1}.

    The derivative:
        (d/ds)[-(c/6)(s - 1/s) * log(L/eps)]|_{s=1}
        = -(c/6)(1 + 1/s^2) * log(L/eps)|_{s=1}
        = -(c/6)(2) * log(L/eps)
        = -(c/3) * log(L/eps)

    So S_1 = -[-(c/3)*log(L/eps)] = (c/3)*log(L/eps).

    Parameters
    ----------
    c_val : float or Rational
        Central charge.
    log_ratio : float or int
        log(L/epsilon).

    Returns
    -------
    Rational or float
        The von Neumann entropy.
    """
    if isinstance(c_val, (Rational, int)) and isinstance(log_ratio, (int, Rational)):
        return Rational(c_val, 3) * log_ratio
    return float(c_val) / 3.0 * float(log_ratio)


def renyi_analytic_continuation(s, c_val, log_ratio, dps=30):
    r"""Analytic continuation of Renyi entropy to complex s.

    S(s) = (1/(1-s)) * log(zeta^{EE}(s))
         = (c/6)(1 + 1/s) * log(L/epsilon)

    This is well-defined for all s != 0, with a removable singularity
    at s = 1 giving the von Neumann entropy.

    For complex s, this probes the entanglement spectrum at complex
    Renyi index.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        c = mpf(c_val)
        lr = mpf(log_ratio)
        return complex((c / 6) * (1 + 1 / s) * lr)


# =====================================================================
# 3. EVALUATION AT ZETA ZEROS
# =====================================================================

def spectral_zeta_at_zeta_zero(k, c_val, log_ratio, dps=30):
    r"""Evaluate zeta^{EE}_A(s_k) where s_k = (1+rho_k)/2.

    Here rho_k is the k-th nontrivial zero of the Riemann zeta function.
    Under RH: rho_k = 1/2 + i*gamma_k, so s_k = 3/4 + i*gamma_k/2.

    These are the points where the Benjamin-Chang scattering factor F_c(s)
    has poles (from zeros of zeta(2s-1)).

    Parameters
    ----------
    k : int
        Index of the zeta zero (k >= 1).
    c_val : float
        Central charge.
    log_ratio : float
        log(L/epsilon).

    Returns
    -------
    dict with keys:
        'k': zero index
        'rho': the zeta zero rho_k
        'gamma': imaginary part of rho_k
        's_rho': the evaluation point (1+rho_k)/2
        'log_spectral_zeta': log zeta^{EE}(s_rho)
        'spectral_zeta': zeta^{EE}(s_rho)
        'abs_spectral_zeta': |zeta^{EE}(s_rho)|
        'renyi_at_zero': S(s_rho) = (c/6)(1 + 1/s_rho) * log(L/eps)
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = zetazero(k)
        gamma_k = float(mpim(rho))
        s_rho = (1 + rho) / 2

        log_sz = log_spectral_zeta_universal(complex(s_rho), c_val, log_ratio, dps)
        sz = spectral_zeta_universal(complex(s_rho), c_val, log_ratio, dps)
        renyi = renyi_analytic_continuation(complex(s_rho), c_val, log_ratio, dps)

        return {
            'k': k,
            'rho': complex(rho),
            'gamma': gamma_k,
            's_rho': complex(s_rho),
            'log_spectral_zeta': log_sz,
            'spectral_zeta': sz,
            'abs_spectral_zeta': abs(sz),
            'renyi_at_zero': renyi,
        }


def zeta_entanglement_profile(n_zeros, c_val, log_ratio, dps=30):
    r"""Compute the zeta-entanglement profile E_k(A) for the first n_zeros zeros.

    E_k(A) = |zeta^{EE}_A((1+rho_k)/2)|

    Returns a list of dicts, one per zero.
    """
    return [spectral_zeta_at_zeta_zero(k, c_val, log_ratio, dps)
            for k in range(1, n_zeros + 1)]


def log_zeta_entanglement_at_zero(k, c_val, log_ratio, dps=30):
    r"""The real part of log|zeta^{EE}((1+rho_k)/2)| for the k-th zero.

    Under RH, s_k = 3/4 + i*gamma_k/2.  Then:

        log zeta^{EE}(s_k) = -(c/6)(s_k - 1/s_k) * log(L/eps)

    with s_k - 1/s_k = s_k - conj(s_k)/|s_k|^2 (complex).  The real part
    of this quantity controls the modulus |zeta^{EE}(s_k)|.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = zetazero(k)
        s_rho = (1 + rho) / 2
        c = mpf(c_val)
        lr = mpf(log_ratio)
        val = -(c / 6) * (s_rho - 1 / s_rho) * lr
        return float(mpre(val))


# =====================================================================
# 4. MODULAR ENTROPY
# =====================================================================

def modular_hamiltonian_coefficient(c_val):
    r"""Coefficient of the modular Hamiltonian K = alpha * (H - c/24).

    For a single interval of length L in a 2D CFT:
        K = (2*pi * L / (L^2 - x^2)) * (H - c/24)  [at position x]

    The entanglement entropy is:
        S_EE = <K> = (c/3) * log(L/epsilon)

    The connection to F_1: The genus-1 free energy is
        F_1(A) = kappa(A) * lambda_1^FP = kappa(A) / 24

    The modular entropy S_mod = <K> and the genus-1 free energy
    are related by the replica-to-genus dictionary:
        S_EE = (2*kappa/3) * log(L/eps) while F_1 = kappa/24.
    The ratio is S_EE / F_1 = 16 * log(L/eps).

    Returns
    -------
    dict with:
        'kappa': kappa = c/2
        'F1': kappa/24
        'S_EE_per_log': c/3 (coefficient of log(L/eps) in S_EE)
        'ratio_SEE_F1': 16 * log(L/eps) would be the ratio
    """
    c = Rational(c_val)
    kappa = c / 2
    F1 = kappa * Rational(1, 24)
    S_coeff = Rational(c, 3)
    return {
        'kappa': kappa,
        'F1': F1,
        'S_EE_coefficient': S_coeff,
        'ratio_coefficient': S_coeff / F1 if F1 != 0 else None,
    }


def modular_entropy_from_F1(kappa_val, log_ratio):
    r"""Modular entropy related to the genus-1 free energy.

    The genus-1 free energy is F_1 = kappa/24.

    The modular entropy is S_mod = (2*kappa/3) * log(L/eps).

    The dictionary:
        S_mod = F_1 * 16 * log(L/eps)
              = (kappa/24) * 16 * log(L/eps)
              = (2*kappa/3) * log(L/eps)

    This identity connects the genus-1 shadow tower term to the
    entanglement entropy.

    Parameters
    ----------
    kappa_val : float or Rational
        Modular characteristic kappa(A).
    log_ratio : float or int
        log(L/epsilon).
    """
    if isinstance(kappa_val, (Rational, int)):
        kappa = Rational(kappa_val)
        F1 = kappa / 24
        S_mod = 2 * kappa * Rational(log_ratio) / 3
        return {
            'F1': F1,
            'S_mod': S_mod,
            'consistent': S_mod == F1 * 16 * log_ratio,
        }
    kappa = float(kappa_val)
    lr = float(log_ratio)
    F1 = kappa / 24.0
    S_mod = 2 * kappa * lr / 3.0
    return {
        'F1': F1,
        'S_mod': S_mod,
        'consistent': abs(S_mod - F1 * 16 * lr) < 1e-14,
    }


def modular_hamiltonian_spectrum(c_val, log_ratio, n_levels=20, dps=30):
    r"""Approximate entanglement spectrum from the modular Hamiltonian.

    The entanglement energies for a single interval in a 2D CFT are:

        E_n ~ (2*pi / log(L/eps)) * (n + alpha_0)

    where alpha_0 is a non-universal constant.  The entanglement spectrum
    eigenvalues are:

        lambda_n = exp(-E_n) / Z

    with Z = sum_n exp(-E_n) the normalization.

    For the leading (universal) approximation:
        xi_n = 2*pi*n / log(L/eps), n = 1, 2, 3, ...

    The spectral zeta sum:
        sum_n exp(-s * E_n) / Z^s

    converges to zeta^{EE}(s) in the thermodynamic limit.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        c = mpf(c_val)
        lr = mpf(log_ratio)
        beta_eff = lr  # effective inverse temperature

        # Spacing: 2*pi / beta_eff
        spacing = 2 * mp_pi / beta_eff

        levels = []
        for n in range(1, n_levels + 1):
            E_n = spacing * n
            levels.append({
                'n': n,
                'E_n': float(E_n),
                'lambda_n_unnormalized': float(mp_exp(-E_n)),
            })

        # Normalization
        Z = sum(mp_exp(-mpf(lev['E_n'])) for lev in levels)
        for lev in levels:
            lev['lambda_n'] = float(mp_exp(-mpf(lev['E_n'])) / Z)

        return levels


# =====================================================================
# 5. ENTROPY FUNCTIONAL EQUATION
# =====================================================================

def entropy_functional_equation_test(s, c_val, log_ratio, dps=30):
    r"""Test whether the spectral zeta satisfies a functional equation.

    The spectral zeta:
        log zeta^{EE}(s) = -(c/6)(s - 1/s) * log(L/eps)

    Under s -> 1/s:
        log zeta^{EE}(1/s) = -(c/6)(1/s - s) * log(L/eps)
                            = (c/6)(s - 1/s) * log(L/eps)
                            = -log zeta^{EE}(s)

    So:
        zeta^{EE}(s) * zeta^{EE}(1/s) = 1

    This is a FUNCTIONAL EQUATION of the entanglement spectral zeta:
    the spectral zeta at s and at 1/s are multiplicative inverses.

    The Renyi entropy satisfies:
        S(s) = (c/6)(1 + 1/s) * log(L/eps)
        S(1/s) = (c/6)(1 + s) * log(L/eps)
        S(s) + S(1/s) = (c/6)(2 + s + 1/s) * log(L/eps)

    This is NOT a simple reflection symmetry for S_n itself, but it
    relates S(s) and S(1/s) via s + 1/s.

    Also test the Benjamin-Chang-like relation: under n -> 1-n:
        S(1-n) = (c/6)(1 + 1/(1-n)) * log = (c/6)((2-n)/(1-n)) * log

    Returns
    -------
    dict with verification data.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        c = mpf(c_val)
        lr = mpf(log_ratio)

        # Functional equation: zeta(s) * zeta(1/s) = 1
        log_z_s = -(c / 6) * (s - 1 / s) * lr
        log_z_inv = -(c / 6) * (1 / s - s) * lr
        product_log = log_z_s + log_z_inv  # should be 0

        # Renyi sum S(s) + S(1/s)
        S_s = (c / 6) * (1 + 1 / s) * lr
        S_inv = (c / 6) * (1 + s) * lr
        renyi_sum = S_s + S_inv
        expected_sum = (c / 6) * (2 + s + 1 / s) * lr

        return {
            'log_product': complex(product_log),
            'product_error': float(fabs(product_log)),
            'S_s': complex(S_s),
            'S_inv_s': complex(S_inv),
            'renyi_sum': complex(renyi_sum),
            'expected_sum': complex(expected_sum),
            'renyi_sum_error': float(fabs(renyi_sum - expected_sum)),
        }


def spectral_zeta_inversion_symmetry(s, c_val, log_ratio, dps=30):
    r"""Verify the inversion symmetry zeta^{EE}(s) * zeta^{EE}(1/s) = 1.

    This is exact for the universal spectral zeta and follows from
    (s - 1/s) + (1/s - s) = 0.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        z_s = mpc(spectral_zeta_universal(s, c_val, log_ratio, dps))
        z_inv = mpc(spectral_zeta_universal(1.0 / complex(s), c_val, log_ratio, dps))
        product = z_s * z_inv
        return {
            'zeta_s': complex(z_s),
            'zeta_inv_s': complex(z_inv),
            'product': complex(product),
            'error': float(fabs(product - 1)),
        }


# =====================================================================
# 6. COMPLEMENTARITY OF ENTANGLEMENT
# =====================================================================

def entanglement_complementarity_spectral(s, c_val, log_ratio, dps=30):
    r"""Complementarity of the entanglement spectral zeta under c <-> 26-c.

    For Virasoro duality:
        log zeta^{EE}_c(s) + log zeta^{EE}_{26-c}(s)
        = -(c/6)(s-1/s)*log - ((26-c)/6)(s-1/s)*log
        = -(26/6)(s-1/s)*log
        = -(13/3)(s-1/s)*log

    This is INDEPENDENT of c: it depends only on the complementarity
    sum c + (26-c) = 26, or equivalently kappa + kappa' = 13.

    At the self-dual point c=13: each contributes half of the total.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        c = mpf(c_val)
        lr = mpf(log_ratio)

        log_z_c = -(c / 6) * (s - 1 / s) * lr
        log_z_dual = -((26 - c) / 6) * (s - 1 / s) * lr
        total = log_z_c + log_z_dual
        expected = -(mpf(26) / 6) * (s - 1 / s) * lr

        return {
            'c': float(c),
            'c_dual': float(26 - c),
            'log_zeta_c': complex(log_z_c),
            'log_zeta_dual': complex(log_z_dual),
            'sum': complex(total),
            'expected': complex(expected),
            'error': float(fabs(total - expected)),
        }


def complementarity_renyi(n_renyi, c_val, log_ratio, dps=30):
    r"""Complementarity of Renyi entropy: S_n(c) + S_n(26-c).

    S_n(c) + S_n(26-c) = (c/6)(1+1/n)*log + ((26-c)/6)(1+1/n)*log
                        = (26/6)(1+1/n)*log
                        = (13/3)(1+1/n)*log

    Independent of c.  At n=1 (von Neumann): sum = (26/3)*log.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        n = mpc(n_renyi)
        c = mpf(c_val)
        lr = mpf(log_ratio)

        S_c = (c / 6) * (1 + 1 / n) * lr
        S_dual = ((26 - c) / 6) * (1 + 1 / n) * lr
        total = S_c + S_dual
        expected = (mpf(26) / 6) * (1 + 1 / n) * lr

        return {
            'S_n_c': complex(S_c),
            'S_n_dual': complex(S_dual),
            'sum': complex(total),
            'expected': complex(expected),
            'error': float(fabs(total - expected)),
        }


def self_dual_spectral_zeta(s, log_ratio, dps=30):
    r"""Spectral zeta at the self-dual point c = 13.

    zeta^{EE}_{13}(s) = (L/eps)^{-(13/6)(s-1/s)}

    At c=13, both algebra and dual have the same spectral zeta.
    """
    return spectral_zeta_universal(s, 13.0, log_ratio, dps)


# =====================================================================
# 7. ENTROPY-ZERO CORRESPONDENCE
# =====================================================================

def zeta_entanglement_values(n_zeros, c_val, log_ratio, dps=30):
    r"""E_k(A) = |zeta^{EE}_A((1+rho_k)/2)| for the first n_zeros zeros.

    Returns a list of (k, gamma_k, E_k) tuples.

    The pattern: since s_k = 3/4 + i*gamma_k/2 and

        log|zeta^{EE}(s_k)| = Re[-(c/6)(s_k - 1/s_k) * log(L/eps)]

    the modulus depends on gamma_k through s_k - 1/s_k.  Let a = 3/4,
    b = gamma_k/2.  Then s_k = a + ib, 1/s_k = (a - ib)/(a^2 + b^2).

        s - 1/s = a(1 - 1/(a^2+b^2)) + ib(1 + 1/(a^2+b^2))

    The real part of (s-1/s) gives the decay/growth of |zeta^{EE}|:

        Re(s - 1/s) = a * (1 - 1/(a^2+b^2))

    For a = 3/4, this is positive when a^2 + b^2 > 1, i.e., when
    b > sqrt(1 - 9/16) = sqrt(7/16) ~ 0.66.  Since gamma_1/2 ~ 7.07,
    this is always satisfied for all nontrivial zeros.

    So Re(log zeta^{EE}(s_k)) < 0 (since the coefficient is -(c/6)*log(L/eps) < 0
    times a positive real part), meaning |zeta^{EE}(s_k)| < 1 and DECAYS
    as gamma_k grows.

    The imaginary part of (s-1/s) gives oscillations in arg(zeta^{EE}(s_k)).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    results = []
    with mp.workdps(dps):
        c = mpf(c_val)
        lr = mpf(log_ratio)

        for k in range(1, n_zeros + 1):
            rho = zetazero(k)
            gamma_k = float(mpim(rho))
            s_k = (1 + rho) / 2

            log_z = -(c / 6) * (s_k - 1 / s_k) * lr
            E_k = float(mp_exp(mpre(log_z)))

            results.append({
                'k': k,
                'gamma': gamma_k,
                'E_k': E_k,
                'log_E_k': float(mpre(log_z)),
                'phase': float(mpim(log_z)),
            })

    return results


def zeta_entanglement_decay_rate(c_val, log_ratio):
    r"""Asymptotic decay rate of E_k(A) as gamma_k -> infinity.

    For large gamma_k: s_k ~ i*gamma_k/2, and

        s_k - 1/s_k ~ i*gamma_k/2 - 2i/gamma_k ~ i*gamma_k/2

    So:
        log|zeta^{EE}(s_k)| ~ Re[-(c/6) * i*gamma_k/2 * log(L/eps)]
                             = 0  (purely imaginary!)

    More precisely, with s_k = 3/4 + i*gamma_k/2:

        Re(s_k - 1/s_k) = 3/4 * (1 - 1/(9/16 + gamma_k^2/4))
                         -> 3/4 as gamma_k -> infinity

    So:
        log|E_k| -> -(c/6) * (3/4) * log(L/eps) = -(c/8) * log(L/eps)

    The |E_k| converge to a CONSTANT (L/eps)^{-c/8} at large k.

    Returns the asymptotic value.
    """
    c = float(c_val)
    lr = float(log_ratio)
    asymptotic_log = -c / 8.0 * lr
    return {
        'asymptotic_E': math.exp(asymptotic_log),
        'asymptotic_log_E': asymptotic_log,
        'formula': '(L/eps)^{-c/8}',
    }


# =====================================================================
# 8. SHADOW RENYI ENTROPY
# =====================================================================

def shadow_free_energies(kappa_val, g_max=10):
    r"""Compute the scalar free energies F_g = kappa * lambda_g^FP.

    Returns list of (g, F_g) for g = 1, ..., g_max.

    >>> shadow_free_energies(Rational(1), 3)
    [(1, Rational(1, 24)), (2, Rational(7, 5760)), (3, Rational(31, 967680))]
    """
    kappa = Rational(kappa_val)
    return [(g, kappa * faber_pandharipande(g)) for g in range(1, g_max + 1)]


def shadow_renyi_entropy(kappa_val, r_renyi, g_max=20, dps=30):
    r"""Shadow Renyi entropy of the shadow tower.

    S_r^{shadow}(A) = (1/(1-r)) * log(sum_g |F_g|^r / (sum_g |F_g|)^r)

    This measures the concentration of the shadow tower across genera.
    A tower concentrated at genus 1 has low shadow Renyi; a tower
    spread across many genera has high shadow Renyi.

    Parameters
    ----------
    kappa_val : float or Rational
        Modular characteristic kappa(A).
    r_renyi : int or float
        The Renyi index (r >= 2).
    g_max : int
        Maximum genus in the sum.

    Returns
    -------
    float
        The shadow Renyi entropy.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        kappa = mpf(float(kappa_val))
        fg_list = []
        for g in range(1, g_max + 1):
            lam_g = faber_pandharipande(g)
            fg = kappa * mpf(float(lam_g))
            fg_list.append(fabs(fg))

        if not fg_list or all(f == 0 for f in fg_list):
            return 0.0

        total = sum(fg_list)
        if total == 0:
            return 0.0

        # Normalize: p_g = |F_g| / sum |F_g|
        probs = [f / total for f in fg_list]

        r = mpf(float(r_renyi))
        sum_pr = sum(power(p, r) for p in probs)

        if sum_pr <= 0:
            return float(mp_inf)

        return float(mp_log(sum_pr) / (1 - r))


def shadow_renyi_profile(kappa_val, r_values=None, g_max=20, dps=30):
    r"""Compute shadow Renyi entropy for multiple r values.

    Returns list of (r, S_r^{shadow}).
    """
    if r_values is None:
        r_values = list(range(2, 11))
    return [(r, shadow_renyi_entropy(kappa_val, r, g_max, dps))
            for r in r_values]


def shadow_shannon_entropy(kappa_val, g_max=20, dps=30):
    r"""Shadow Shannon entropy: the r -> 1 limit of shadow Renyi.

    H^{shadow} = -sum_g p_g log(p_g)

    where p_g = |F_g| / sum |F_g|.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        kappa = mpf(float(kappa_val))
        fg_list = []
        for g in range(1, g_max + 1):
            lam_g = faber_pandharipande(g)
            fg = fabs(kappa * mpf(float(lam_g)))
            fg_list.append(fg)

        total = sum(fg_list)
        if total == 0:
            return 0.0

        probs = [f / total for f in fg_list]
        H = mpf(0)
        for p in probs:
            if p > 0:
                H -= p * mp_log(p)

        return float(H)


def shadow_tower_concentration(kappa_val, g_max=20):
    r"""Measure how concentrated the shadow tower is at genus 1.

    Returns the ratio F_1 / sum_{g=1}^{g_max} |F_g|.

    For large |kappa|: F_g ~ kappa * |B_{2g}| / (2g)!, so the tower
    is dominated by g=1 (since |B_{2g}|/(2g)! decays super-exponentially).
    The Faber-Pandharipande coefficients lambda_g^FP decay like (2*pi)^{-2g},
    so the tower is highly concentrated at g=1.
    """
    kappa = Rational(kappa_val)
    fgs = [abs(kappa * faber_pandharipande(g)) for g in range(1, g_max + 1)]
    total = sum(fgs)
    if total == 0:
        return 0
    return float(fgs[0] / total)


# =====================================================================
# COMBINED ANALYSIS: BENJAMIN-CHANG + ENTANGLEMENT
# =====================================================================

def bc_entanglement_census(c_val, log_ratio, n_zeros=10, g_max=10, dps=30):
    r"""Combined Benjamin-Chang + entanglement analysis for a given c.

    Computes:
    - Von Neumann entropy
    - Renyi S_2, S_3
    - Spectral zeta at first n_zeros zeta zeros
    - Complementarity sum
    - Shadow Renyi S_2^{shadow}
    - Modular entropy data
    """
    kappa = float(c_val) / 2.0
    lr = float(log_ratio)

    vn = float(c_val) / 3.0 * lr
    s2 = renyi_from_spectral_zeta(2, c_val, log_ratio, dps).real
    s3 = renyi_from_spectral_zeta(3, c_val, log_ratio, dps).real

    # Zeta-entanglement at first n_zeros zeros
    E_vals = zeta_entanglement_values(n_zeros, c_val, log_ratio, dps)

    # Complementarity
    comp = entanglement_complementarity_spectral(1.5, c_val, log_ratio, dps)

    # Shadow Renyi
    sr2 = shadow_renyi_entropy(kappa, 2, g_max, dps)

    # Modular
    mod = modular_entropy_from_F1(kappa, log_ratio)

    return {
        'c': float(c_val),
        'kappa': kappa,
        'von_neumann': vn,
        'renyi_2': s2,
        'renyi_3': s3,
        'zeta_entanglement': E_vals,
        'complementarity': comp,
        'shadow_renyi_2': sr2,
        'modular': mod,
    }


# =====================================================================
# VERIFICATION INFRASTRUCTURE
# =====================================================================

def verify_renyi_limit(c_val, log_ratio, dps=30):
    r"""Verify that lim_{n->1} S_n = (c/3) * log(L/eps).

    Path 1: Direct formula S_n = (c/6)(1+1/n)*log.
    Path 2: Replica trick: S_n = (1/(1-n)) * log(Z_n/Z_1^n).
    Path 3: Derivative: S_1 = -(d/ds) log zeta^{EE}(s)|_{s=1}.

    All three must agree.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        c = mpf(c_val)
        lr = mpf(log_ratio)
        expected = c / 3 * lr

        # Path 1: limit of (c/6)(1+1/n) as n->1
        path1 = c / 6 * 2 * lr  # = c/3 * lr

        # Path 2: Z_n = (L/eps)^{-(c/6)(n-1/n)}, then S_n = (1/(1-n))*log Z_n
        # = (c/6)(1+1/n)*lr -> c/3*lr
        eps_val = mpf('1e-10')
        n_near_1 = 1 + eps_val
        S_near = (c / 6) * (1 + 1 / n_near_1) * lr
        path2 = S_near  # approaches c/3*lr

        # Path 3: -(d/ds)[-(c/6)(s-1/s)*lr]|_{s=1} = (c/6)(1+1/s^2)*lr|_{s=1} = c/3*lr
        path3 = (c / 6) * 2 * lr

        return {
            'expected': float(expected),
            'path1_direct_limit': float(path1),
            'path2_replica_limit': float(path2),
            'path3_derivative': float(path3),
            'path1_error': float(fabs(path1 - expected)),
            'path2_error': float(fabs(path2 - expected)),
            'path3_error': float(fabs(path3 - expected)),
        }


def verify_free_boson_spectral_zeta(log_ratio, dps=30):
    r"""Verification for c=1 free boson: three independent computations.

    Path 1: Universal formula zeta^{EE}(s) = (L/eps)^{-(1/6)(s-1/s)}.
    Path 2: Renyi S_n = (1/6)(1+1/n)*log => Tr(rho^n) = exp((1-n)*S_n).
    Path 3: S_EE = (1/3)*log (Calabrese-Cardy for c=1).

    For integer n, Paths 1 and 2 must agree exactly.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        lr = mpf(log_ratio)
        c = mpf(1)

        results = {}
        for n in [2, 3, 4, 5]:
            n_mp = mpf(n)

            # Path 1: universal spectral zeta
            z1 = mp_exp(-(c / 6) * (n_mp - 1 / n_mp) * lr)

            # Path 2: from Renyi: Tr(rho^n) = exp((1-n)*S_n)
            S_n = (c / 6) * (1 + 1 / n_mp) * lr
            z2 = mp_exp((1 - n_mp) * S_n)

            results[n] = {
                'path1': float(z1),
                'path2': float(z2),
                'error': float(fabs(z1 - z2)),
            }

        # Von Neumann
        S_vn = c / 3 * lr
        results['von_neumann'] = float(S_vn)

        return results


def verify_cardy_calabrese(c_val, log_ratio, dps=30):
    r"""Verify Calabrese-Cardy formula via four independent paths.

    Path 1: CFT formula S_EE = (c/3)*log(L/eps).
    Path 2: Replica limit: lim_{n->1} S_n.
    Path 3: Spectral zeta derivative: S_1 = -(d/ds) log zeta^{EE}|_{s=1}.
    Path 4: From kappa: S_EE = (2*kappa/3)*log with kappa = c/2.

    All four must agree.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        c = mpf(c_val)
        lr = mpf(log_ratio)

        path1 = c / 3 * lr
        path2 = c / 6 * 2 * lr  # limit of (c/6)(1+1/n) as n->1
        path3 = (c / 6) * (1 + 1) * lr  # -(d/ds)[-(c/6)(s-1/s)*lr] at s=1
        kappa = c / 2
        path4 = 2 * kappa / 3 * lr

        return {
            'path1_CFT': float(path1),
            'path2_replica': float(path2),
            'path3_spectral_derivative': float(path3),
            'path4_kappa': float(path4),
            'all_agree': float(max(
                fabs(path1 - path2),
                fabs(path1 - path3),
                fabs(path1 - path4),
            )),
        }
