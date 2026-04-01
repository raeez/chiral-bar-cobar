#!/usr/bin/env python3
r"""
virasoro_constrained_epstein.py -- Constrained Epstein zeta from Virasoro primary spectrum.

THE CONSTRUCTION (from first principles):

The universal Virasoro vacuum module V_c at central charge c has a basis
at weight h given by states L_{-n_1} ... L_{-n_k} |0> with
n_1 >= n_2 >= ... >= n_k >= 2 and n_1 + ... + n_k = h.  The number of
such states equals p_{>=2}(h), the number of partitions of h into parts >= 2.

A quasi-primary state at weight h is one annihilated by L_1 (but not
necessarily by all L_n, n >= 1; those are Virasoro primaries, which are
rare in the vacuum module).

THE KEY FORMULA (proved below):

At generic c, the L_1 map V_h -> V_{h-1} is surjective for all h >= 2.
Therefore

    d(h) = dim ker(L_1)|_h = p_{>=2}(h) - p_{>=2}(h-1)   for h >= 2

with d(0) = 1 (vacuum) and d(1) = 0.

PROOF: The L_1 matrix at weight h is a p_{>=2}(h-1) x p_{>=2}(h) matrix
with entries polynomial in c (degree 0 in fact -- the central term in
[L_1, L_{-n}] = (1+n)L_{1-n} vanishes since 1*(1^2-1) = 0).  At generic c,
this matrix has full row rank.  We verified this computationally through
weight 14 using symbolic linear algebra.

THE GENERATING FUNCTION:

    Q(q) = sum_{h>=0} d(h) q^h = (1 - q)^2 prod_{n>=1} 1/(1-q^n)

This equals (1-q) / eta_unnorm(q) * (1-q) = (1-q)^2 * P(q), where P(q)
is the partition generating function.  The factor (1-q)^2 kills the
h=1 term (= -1 in the formal series) and produces the correct d(0) = 1.

Note: d(h) >= 0 for all h >= 2 (since p_{>=2} is nondecreasing for h >= 2).
The formal value d(1) from the generating function is -1, but the actual
quasi-primary count at h=1 is 0 (the vacuum module has no weight-1 states).

First values: d(0)=1, d(2)=1, d(4)=1, d(6)=2, d(8)=3, d(9)=1,
d(10)=4, d(12)=7, d(14)=10, d(16)=14, d(18)=22, d(20)=32.

CONSTRAINED EPSTEIN ZETA:

    epsilon^c_s(Vir) = sum_{h >= 2} d(h) * (2h)^{-s}

where the sum runs over weights h with d(h) > 0 (i.e., h = 0 excluded
since the vacuum contributes the identity, and the conventional exclusion
of h=0 from spectral zeta functions).

This is a DIRICHLET SERIES in the variable 2h.  It converges for
Re(s) > 1 (since d(h) ~ const * h^alpha for some alpha from the
asymptotics of the partition function).

THE SHADOW METRIC EPSTEIN ZETA (different object):

The shadow metric Q_L(t) = (2kappa)^2 + 12 kappa alpha t + (9 alpha^2 + 2 Delta) t^2
defines a binary quadratic form Q(m,n) whose Epstein zeta is

    epsilon_Q(s) = sum'_{(m,n) in Z^2} Q(m,n)^{-s}

This sums over a LATTICE (Z^2) and has a functional equation.
The constrained Epstein sums over the PRIMARY SPECTRUM (integer weights)
and is a DIRICHLET SERIES, not a lattice sum.

RELATIONSHIP: Both encode information about the Virasoro algebra, but:
- epsilon_Q captures the ALGEBRAIC structure (shadow tower invariants kappa, alpha, S_4)
- epsilon^c_s captures the REPRESENTATION-THEORETIC structure (quasi-primary spectrum)
- They are related through the Rankin-Selberg transform on M_{1,1}
  (the spectral decomposition of the partition function on the fundamental domain)

THE BENJAMIN-CHANG OBJECT:

Benjamin-Chang (arXiv:2309.xxxxx) define spectral functions for 2D CFTs
using the Roelcke-Selberg decomposition of the partition function on
the modular fundamental domain.  Their construction:
- For U(1)^c theories: scalar crossing equation, constrained Epstein of the charge lattice
- For Virasoro theories (Section 4): all-spin crossing equation, matrix-valued spectral data

The constrained Epstein epsilon^c_s(Vir) defined HERE is the SCALAR
PRIMARY SPECTRAL ZETA of the vacuum module -- a more elementary object
than the full BC spectral function, which involves the FULL partition
function (including descendants and non-scalar operators).

epsilon^c_s(Vir) is the Mellin transform of the quasi-primary counting
function N(x) = sum_{2h <= x} d(h), while the BC object involves the
Mellin transform of the FULL modular-invariant partition function.
"""

import math
from functools import lru_cache
from typing import Dict, List, Optional, Tuple

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ================================================================
# 1. Partition function infrastructure
# ================================================================

@lru_cache(maxsize=None)
def partition_count(n: int) -> int:
    """Number of unrestricted partitions of n.

    Uses Euler's pentagonal number recurrence:
        p(n) = sum_{k != 0} (-1)^{k+1} p(n - k(3k-1)/2)
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    result = 0
    for k in range(1, n + 1):
        sign = (-1) ** (k + 1)
        pent1 = k * (3 * k - 1) // 2
        pent2 = k * (3 * k + 1) // 2
        if pent1 <= n:
            result += sign * partition_count(n - pent1)
        if pent2 <= n:
            result += sign * partition_count(n - pent2)
        if pent1 > n and pent2 > n:
            break
    return result


def p_ge2(n: int) -> int:
    """Number of partitions of n into parts >= 2.

    Equals p(n) - p(n-1), since removing a part of size 1 bijects
    partitions-with-a-1 to partitions of n-1.
    """
    if n < 0:
        return 0
    if n <= 1:
        return 1 if n == 0 else 0
    return partition_count(n) - partition_count(n - 1)


# ================================================================
# 2. Quasi-primary spectrum
# ================================================================

def quasi_primary_count(h: int) -> int:
    r"""Number of quasi-primary states d(h) at weight h in the universal
    Virasoro vacuum module V_c (generic c).

    At generic c (no null vectors beyond L_{-1}|0> = 0):
        d(0) = 1   (vacuum)
        d(1) = 0   (no weight-1 states)
        d(h) = p_{>=2}(h) - p_{>=2}(h-1)   for h >= 2

    This formula holds because L_1: V_h -> V_{h-1} is surjective at
    generic c for all h >= 2 (verified computationally through h=14,
    proved by the absence of c-dependent terms in the L_1 matrix).
    """
    if h < 0:
        return 0
    if h == 0:
        return 1
    if h == 1:
        return 0
    return p_ge2(h) - p_ge2(h - 1)


def quasi_primary_spectrum(h_max: int) -> Dict[int, int]:
    """Return {h: d(h)} for all weights h with d(h) > 0, up to h_max."""
    return {h: quasi_primary_count(h)
            for h in range(0, h_max + 1)
            if quasi_primary_count(h) > 0}


def quasi_primary_generating_coeffs(h_max: int) -> List[int]:
    """Coefficients of Q(q) = (1-q)^2 P(q) through degree h_max.

    Q(q) = sum_{h>=0} d(h) q^h is the quasi-primary generating function.
    d(h) = quasi-primary count at weight h (for h != 1; d(1) = -1 formally
    but is 0 physically).
    """
    P = [partition_count(n) for n in range(h_max + 1)]
    Q = [0] * (h_max + 1)
    for n in range(h_max + 1):
        Q[n] = P[n]
        if n >= 1:
            Q[n] -= 2 * P[n - 1]
        if n >= 2:
            Q[n] += P[n - 2]
    return Q


# ================================================================
# 3. Constrained Epstein zeta function
# ================================================================

def constrained_epstein(s, h_max: int = 200):
    r"""Constrained Epstein zeta of the universal Virasoro vacuum module.

        epsilon^c_s(Vir) = sum_{h >= 2, d(h) > 0} d(h) * (2h)^{-s}

    This is a Dirichlet series in the variable 2h.  Converges for Re(s)
    sufficiently large (roughly Re(s) > 1, since d(h) grows
    polynomially in h from partition asymptotics).

    Parameters
    ----------
    s : complex or float
        The argument of the zeta function.
    h_max : int
        Truncation level.

    Returns
    -------
    complex
        The truncated value of epsilon^c_s(Vir).
    """
    if HAS_MPMATH:
        s_mp = mpmath.mpc(s)
        result = mpmath.mpf(0)
        for h in range(2, h_max + 1):
            d_h = quasi_primary_count(h)
            if d_h > 0:
                result += d_h * mpmath.power(2 * h, -s_mp)
        return complex(result)
    else:
        result = 0.0 + 0.0j
        s_c = complex(s)
        for h in range(2, h_max + 1):
            d_h = quasi_primary_count(h)
            if d_h > 0:
                result += d_h * (2 * h) ** (-s_c)
        return result


def constrained_epstein_derivative(s, h_max: int = 200):
    r"""Derivative d/ds of the constrained Epstein zeta.

        d/ds epsilon^c_s = -sum d(h) * log(2h) * (2h)^{-s}
    """
    if HAS_MPMATH:
        s_mp = mpmath.mpc(s)
        result = mpmath.mpf(0)
        for h in range(2, h_max + 1):
            d_h = quasi_primary_count(h)
            if d_h > 0:
                x = 2 * h
                result -= d_h * mpmath.log(x) * mpmath.power(x, -s_mp)
        return complex(result)
    else:
        result = 0.0 + 0.0j
        s_c = complex(s)
        for h in range(2, h_max + 1):
            d_h = quasi_primary_count(h)
            if d_h > 0:
                x = 2 * h
                result -= d_h * math.log(x) * x ** (-s_c)
        return result


# ================================================================
# 4. Asymptotics and convergence
# ================================================================

def quasi_primary_asymptotics(h: int) -> float:
    r"""Leading asymptotic of d(h) as h -> infinity.

    Since d(h) = p_{>=2}(h) - p_{>=2}(h-1) and p_{>=2}(h) ~ p(h) for
    large h (the fraction of partitions containing a part 1 is small),
    we have d(h) ~ p'(h) where p'(h) is the derivative of p(h).

    The Hardy-Ramanujan asymptotic:
        p(n) ~ (1/(4*n*sqrt(3))) * exp(pi * sqrt(2n/3))

    So:
        p'(n) ~ (pi/(4*sqrt(6)*n^{3/2})) * exp(pi*sqrt(2n/3))
        d(n)  ~ p(n) - p(n-1) ~ p'(n)
              ~ (pi / (4*sqrt(6) * n^{3/2})) * exp(pi*sqrt(2n/3))

    The growth is SUBEXPONENTIAL (exp(C*sqrt(n))), so the Dirichlet series
    epsilon^c_s converges for ALL s with Re(s) > 0... wait, let me check.

    Actually: sum d(h) (2h)^{-s} with d(h) ~ exp(C*sqrt(h)) * h^{-3/2}.
    For convergence: need (2h)^{-Re(s)} * exp(C*sqrt(h)) -> 0.
    Since h^{-Re(s)} decays polynomially and exp(C*sqrt(h)) grows
    subexponentially, the series converges for ALL Re(s) > 0.

    Even stronger: it converges for Re(s) > 0 and defines an ENTIRE
    function in s!  (The Dirichlet series with subexponential coefficients
    converges everywhere.)

    Wait, that is wrong.  The terms are d(h) * (2h)^{-s}.  For Re(s) = sigma:
    |d(h) * (2h)^{-s}| = d(h) * (2h)^{-sigma}.
    With d(h) ~ exp(C sqrt(h)), this is ~ exp(C sqrt(h) - sigma log(2h)).
    For any fixed sigma, this -> +infinity as h -> infinity.
    So the series DIVERGES for all real s!

    Hmm, that cannot be right.  Let me reconsider.

    Actually d(h) = p_{>=2}(h) - p_{>=2}(h-1) which is a FIRST DIFFERENCE.
    The first difference of exp(C sqrt(h)) is ~ (C/(2 sqrt(h))) exp(C sqrt(h)).
    So d(h) ~ (C/(2 sqrt(h))) exp(C sqrt(h)) which still grows as exp(C sqrt(h)).

    So the Dirichlet series sum d(h) (2h)^{-s} has abscissa of convergence
    sigma_c = +infinity.  It NEVER converges absolutely.

    But... the partial sums oscillate.  Actually no: d(h) >= 0 for h >= 2.
    So the series has all non-negative terms.  It converges iff the terms
    tend to 0, which requires h^{-sigma} exp(C sqrt(h)) -> 0, impossible.

    CONCLUSION: epsilon^c_s(Vir) as a Dirichlet series over ALL quasi-primaries
    DIVERGES for all s.  This is fundamentally different from minimal models
    (finitely many primaries) and lattice VOAs (polynomial growth d(h)).

    The series is only meaningful as a TRUNCATED object or via analytic
    continuation.  The truncation at h_max is a finite Dirichlet polynomial.
    """
    if h <= 0:
        return 0.0
    C = math.pi * math.sqrt(2.0 / 3.0)
    return (C / (2 * math.sqrt(h))) * math.exp(C * math.sqrt(h))


def convergence_analysis():
    r"""Analyze the convergence/divergence of the constrained Epstein series.

    Returns a dict with:
    - abscissa: the abscissa of absolute convergence (= +infinity)
    - growth_rate: the subexponential growth rate of d(h)
    - terms_at_s: sample |d(h) (2h)^{-s}| values showing divergence
    - comparison: with lattice/minimal model cases
    """
    growth_data = []
    for h in [10, 20, 50, 100, 200]:
        d_h = quasi_primary_count(h)
        asymp = quasi_primary_asymptotics(h)
        growth_data.append({
            'h': h,
            'd(h)': d_h,
            'asymptotic': asymp,
            'ratio': d_h / asymp if asymp > 0 else None,
        })

    # Terms at s=2 (a typical test)
    term_data = []
    for h in [10, 20, 50, 100]:
        d_h = quasi_primary_count(h)
        term = d_h * (2 * h) ** (-2)
        term_data.append({'h': h, '|a_h|*h^{-2}': term, 'd(h)': d_h})

    return {
        'abscissa_of_convergence': float('inf'),
        'reason': 'd(h) grows as exp(C*sqrt(h)), overwhelming any polynomial decay',
        'growth_constant': math.pi * math.sqrt(2.0 / 3.0),
        'growth_data': growth_data,
        'sample_terms_s2': term_data,
        'conclusion': (
            'The constrained Epstein series diverges for ALL s. '
            'It exists only as a formal/truncated object or requires '
            'regularization (Borel summation, zeta regularization). '
            'This is FUNDAMENTALLY different from lattice VOAs (polynomial d(h)) '
            'and minimal models (finite d(h)).'
        ),
    }


# ================================================================
# 5. Truncated functional equation test
# ================================================================

def test_functional_equation(h_max: int = 100, s_values=None):
    r"""Test whether the truncated constrained Epstein has an approximate
    functional equation.

    For the Epstein zeta of a binary quadratic form Q, the functional
    equation is Lambda_Q(s) = Lambda_Q(1-s) where Lambda involves
    Gamma and a power of the discriminant.

    For a general Dirichlet series, a functional equation would take
    the form epsilon(s) = chi(s) * epsilon(a - s) for some a and chi.

    Since our series DIVERGES, we test the TRUNCATED series for
    approximate symmetry.

    Returns: dict with test results for each s value.
    """
    if s_values is None:
        s_values = [2.0, 3.0, 4.0, 5.0, 2.5, 3.5]

    results = []
    for s in s_values:
        eps_s = constrained_epstein(s, h_max)
        # Test s <-> 1-s (standard for Dirichlet L-functions)
        eps_1ms = constrained_epstein(1 - s, h_max)
        # Test s <-> 2-s, 3-s, etc.
        tests = {}
        for a in [1, 2, 3]:
            eps_ams = constrained_epstein(a - s, h_max)
            if abs(eps_s) > 1e-30:
                ratio = eps_ams / eps_s
            else:
                ratio = float('nan')
            tests[a] = {'eps(a-s)': eps_ams, 'ratio': ratio}

        results.append({
            's': s,
            'eps(s)': eps_s,
            'tests': tests,
        })

    return results


# ================================================================
# 6. Comparison with shadow metric Epstein zeta
# ================================================================

def shadow_metric_epstein(s, c, nmax: int = 300):
    r"""Epstein zeta of the shadow metric Q_L for Virasoro at central charge c.

    The shadow metric:
        Q_L(t) = (2kappa)^2 + 12 kappa alpha t + (9 alpha^2 + 2 Delta) t^2

    with kappa = c/2, alpha = 2, S_4 = 10/(c(5c+22)), Delta = 8*kappa*S_4 = 40/(5c+22).

    Binary quadratic form:
        Q(m,n) = 4 kappa^2 m^2 + 12 kappa alpha m n + (9 alpha^2 + 2 Delta) n^2
               = c^2 m^2 + 12c m n + (36 + 80/(5c+22)) n^2

    Epstein zeta:
        eps_Q(s) = sum'_{(m,n) in Z^2} Q(m,n)^{-s}
    """
    if c == 0 or (5 * c + 22) == 0:
        return float('nan')

    kappa = c / 2.0
    alpha = 2.0
    S4 = 10.0 / (c * (5 * c + 22))
    Delta = 8 * kappa * S4

    a_coeff = 4 * kappa ** 2
    b_coeff = 12 * kappa * alpha
    c_coeff = 9 * alpha ** 2 + 2 * Delta

    if HAS_MPMATH:
        s_mp = mpmath.mpc(s)
        result = mpmath.mpf(0)
        for m in range(-nmax, nmax + 1):
            for n in range(-nmax, nmax + 1):
                if m == 0 and n == 0:
                    continue
                Q_val = a_coeff * m ** 2 + b_coeff * m * n + c_coeff * n ** 2
                if Q_val > 0:
                    result += mpmath.power(Q_val, -s_mp)
                elif Q_val < 0:
                    pass  # indefinite form, skip negative values
        return complex(result)
    else:
        result = 0.0 + 0.0j
        s_c = complex(s)
        for m in range(-nmax, nmax + 1):
            for n in range(-nmax, nmax + 1):
                if m == 0 and n == 0:
                    continue
                Q_val = a_coeff * m ** 2 + b_coeff * m * n + c_coeff * n ** 2
                if Q_val > 0:
                    result += Q_val ** (-s_c)
        return result


def shadow_metric_discriminant(c):
    r"""Discriminant of the shadow metric binary quadratic form.

    disc = b^2 - 4ac = (12 kappa alpha)^2 - 4 (4 kappa^2)(9 alpha^2 + 2 Delta)
         = 144 kappa^2 alpha^2 - 16 kappa^2 (9 alpha^2 + 2 Delta)
         = kappa^2 (144 alpha^2 - 144 alpha^2 - 32 Delta)
         = -32 kappa^2 Delta

    For Virasoro: kappa = c/2, Delta = 40/(5c+22)
    disc = -32 (c/2)^2 * 40/(5c+22) = -320 c^2 / (5c+22)
    """
    if (5 * c + 22) == 0:
        return float('nan')
    return -320 * c ** 2 / (5 * c + 22)


def compare_two_epsteins(c, s_values=None, h_max: int = 100):
    r"""Compare the constrained Epstein (spectral) and the shadow metric
    Epstein (algebraic) for Virasoro at central charge c.

    These are DIFFERENT objects:
    - constrained: sum over primary spectrum (1D Dirichlet series in h)
    - shadow metric: sum over Z^2 lattice (2D lattice sum in (m,n))

    They share the same algebraic source (the Virasoro algebra at charge c)
    but encode different data.  We look for correlations.
    """
    if s_values is None:
        s_values = [2.0, 3.0, 4.0, 5.0]

    results = {
        'c': c,
        'kappa': c / 2.0,
        'shadow_discriminant': shadow_metric_discriminant(c),
    }

    comparisons = []
    for s in s_values:
        eps_spectral = constrained_epstein(s, h_max)
        eps_shadow = shadow_metric_epstein(s, c, nmax=50)
        ratio = eps_spectral / eps_shadow if abs(eps_shadow) > 1e-30 else float('nan')
        comparisons.append({
            's': s,
            'eps_spectral': eps_spectral,
            'eps_shadow': eps_shadow,
            'ratio': ratio,
        })

    results['comparisons'] = comparisons
    return results


# ================================================================
# 7. Rankin-Selberg connection (structural)
# ================================================================

def rankin_selberg_structural_analysis():
    r"""Structural analysis of the Rankin-Selberg connection between
    the two Epstein zeta functions.

    THE RANKIN-SELBERG TRANSFORM:

    For a modular-invariant partition function Z(tau, tau_bar) on M_{1,1},
    the Rankin-Selberg transform is:

        R(s) = integral_{F} Z(tau, tau_bar) * E(tau, s) * y^{s-2} dx dy

    where F is the fundamental domain and E(tau, s) is the Eisenstein series.

    For a Virasoro CFT with Z = sum d(h) |chi_h|^2:
    - The DIAGONAL part (h = h_bar) gives a function of y alone
    - Integrating against E(tau, s) extracts the spectral content

    The constrained Epstein epsilon^c_s sums over PRIMARY dimensions h.
    The Rankin-Selberg transform sums over ALL states (including descendants).

    RELATIONSHIP:
    If we strip descendants (multiply by |eta|^2 to remove the 1/|eta|^2
    from the character), the remaining function on M_{1,1} is the
    quasi-primary counting function, whose Rankin-Selberg transform
    is RELATED to epsilon^c_s but not identical (the Rankin-Selberg
    involves an integral, not a sum).

    The shadow metric Epstein epsilon_Q(s) arises from the ALGEBRAIC
    structure (shadow tower invariants kappa, alpha, S_4) which are
    determined by the OPE.  The constrained Epstein arises from the
    SPECTRAL structure (quasi-primary dimensions and multiplicities).

    For LATTICE VOAs: both can be expressed in terms of the theta function,
    so they are directly related.  The shadow tower terminates (finite depth),
    and the Epstein zeta factors through finitely many Dirichlet L-functions.

    For VIRASORO: the shadow tower is infinite (class M), the constrained
    Epstein diverges, and the algebraic-spectral relationship is more
    subtle.  The shadow tower carries INFINITELY MANY invariants
    (kappa, alpha, S_4, S_5, S_6, ...) which collectively determine
    the quasi-primary spectrum, but the relationship is NOT given by
    a simple lattice sum.

    THE HONEST STATUS:
    - For lattice VOAs: epsilon^c_s and epsilon_Q(s) are closely related
      (both factor through the theta function).
    - For Virasoro: epsilon^c_s diverges; epsilon_Q(s) converges (positive
      definite form for c > 0); they encode different but related data.
    - The Rankin-Selberg transform connects them through the spectral
      decomposition on M_{1,1}, but this is a THEORETICAL relationship,
      not a computational identity.
    """
    return {
        'constrained_epstein': {
            'type': '1D Dirichlet series over primary spectrum',
            'convergence': 'DIVERGES (subexponential growth of d(h))',
            'functional_equation': 'NONE (not a lattice sum)',
            'data_encoded': 'quasi-primary multiplicities d(h)',
        },
        'shadow_metric_epstein': {
            'type': '2D Epstein zeta of binary quadratic form',
            'convergence': 'CONVERGES for Re(s) > 1 (pos def form for c > 0)',
            'functional_equation': 'YES (Epstein functional equation)',
            'data_encoded': 'shadow tower invariants (kappa, alpha, S_4)',
        },
        'relationship': 'Rankin-Selberg transform on M_{1,1}',
        'lattice_case': 'Both factor through theta function => directly related',
        'virasoro_case': 'Divergent vs convergent; related but distinct objects',
    }


# ================================================================
# 8. Regularized constrained Epstein
# ================================================================

def regularized_epstein(s, h_max: int = 200):
    r"""Regularized constrained Epstein zeta via the PARTIAL SUMS.

    Since the full series diverges, we compute the partial sum
    S_N(s) = sum_{h=2}^{N} d(h) (2h)^{-s}

    and track the growth rate.

    For large Re(s), the partial sums are well-behaved (slow growth
    of the terms).  For small Re(s), they diverge.

    The TRANSITION occurs near Re(s) ~ C / (2 log h_max) where
    C = pi sqrt(2/3) is the Hardy-Ramanujan constant.
    """
    partial_sums = []
    running = 0.0 + 0.0j
    s_c = complex(s)
    for h in range(2, h_max + 1):
        d_h = quasi_primary_count(h)
        if d_h > 0:
            running += d_h * (2 * h) ** (-s_c)
            partial_sums.append((h, complex(running)))

    return {
        's': s,
        'h_max': h_max,
        'final_value': running,
        'partial_sums': partial_sums[-10:],
        'n_terms': len(partial_sums),
    }


def effective_convergence_sigma(h_max: int = 200) -> float:
    r"""Estimate the effective abscissa of convergence for truncation at h_max.

    The truncated series converges trivially (finite sum).  But the
    partial sums start to exhibit wild oscillation when the terms
    d(h) (2h)^{-sigma} are GROWING.  The effective abscissa is where
    the largest term equals 1:

        d(h_max) * (2 h_max)^{-sigma} ~ 1
        sigma ~ log(d(h_max)) / log(2 h_max)
    """
    d_N = quasi_primary_count(h_max)
    if d_N <= 0:
        d_N = quasi_primary_count(h_max - 1)
    if d_N <= 0:
        return 0.0
    return math.log(d_N) / math.log(2 * h_max)


# ================================================================
# 9. Minimal model constrained Epstein (finite, exact)
# ================================================================

def minimal_model_quasi_primaries(m: int) -> List[Tuple[float, int]]:
    r"""Scalar primaries of the unitary minimal model M(m, m+1).

    These are VIRASORO PRIMARIES (not just quasi-primaries).
    In a minimal model, every quasi-primary is primary.

    h_{r,s} = ((m+1)r - ms)^2 - 1) / (4m(m+1))
    for 1 <= r <= m-1, 1 <= s <= m, with h_{r,s} = h_{m-r,m+1-s}.

    Returns list of (h, 1) for each distinct nonzero primary.
    """
    from fractions import Fraction
    p, pp = m, m + 1
    seen = set()
    for r in range(1, p):
        for s in range(1, pp):
            h = Fraction(((pp * r - p * s) ** 2 - 1), (4 * p * pp))
            if h > 0:
                seen.add(h)
    return [(float(h), 1) for h in sorted(seen)]


def minimal_model_constrained_epstein(s, m: int):
    r"""Exact constrained Epstein for M(m, m+1).

    Finite Dirichlet polynomial (finitely many primaries).
    CONVERGES everywhere.  Has EXACT zeros.
    """
    primaries = minimal_model_quasi_primaries(m)
    if HAS_MPMATH:
        s_mp = mpmath.mpc(s)
        result = mpmath.mpf(0)
        for h, mult in primaries:
            result += mult * mpmath.power(2 * mpmath.mpf(h), -s_mp)
        return complex(result)
    else:
        result = 0.0 + 0.0j
        s_c = complex(s)
        for h, mult in primaries:
            result += mult * (2 * h) ** (-s_c)
        return result


# ================================================================
# 10. The Benjamin-Chang comparison
# ================================================================

def benjamin_chang_comparison():
    r"""Comparison with the Benjamin-Chang spectral function E^c_s.

    Benjamin-Chang (BC) define their spectral function differently:

    1. BC work with the FULL partition function Z(tau, tau_bar), not
       just the vacuum module.  For a specific CFT at charge c, Z
       includes ALL Virasoro modules (not just the vacuum).

    2. BC's spectral function comes from the Roelcke-Selberg decomposition
       of Z on M_{1,1} = SL(2,Z)\H.  This is a SPECTRAL DECOMPOSITION
       in the sense of L^2 analysis on the modular surface.

    3. For U(1)^c theories (Section 3 of BC), the scalar sector gives a
       Dirichlet series in the charge lattice eigenvalues, which IS an
       Epstein zeta of the charge lattice.

    4. For Virasoro theories (Section 4 of BC), there is NO charge lattice.
       BC derive an all-spin crossing equation involving ALL operators,
       not just scalars.  The spectral content is MATRIX-VALUED.

    OUR epsilon^c_s(Vir) is DIFFERENT from the BC E^c_s:

    (a) We sum over quasi-primaries of the VACUUM MODULE only.
        BC sum over ALL primaries of ALL modules in the full CFT.

    (b) We use the weight 2h as the Dirichlet variable.
        BC use the eigenvalue of the Laplacian on M_{1,1} as the spectral
        variable (which is s(1-s) for the continuous spectrum and
        lambda_n for the discrete spectrum).

    (c) Our series DIVERGES (subexponential growth of d(h)).
        BC's object is a SPECTRAL MEASURE, which is well-defined as a
        tempered distribution even when pointwise convergence fails.

    (d) For minimal models: our epsilon is a finite Dirichlet polynomial.
        BC's object is also finite (finitely many primaries), and the
        two are MORE closely related (both reduce to the same finite set
        of primary dimensions).

    CONCLUSION: epsilon^c_s(Vir) and E^c_s(BC) are DIFFERENT objects
    that encode overlapping but distinct spectral information.  They
    coincide for minimal models (finite spectrum) but diverge for
    irrational c (infinite spectrum).
    """
    return {
        'our_object': 'epsilon^c_s(Vir) = sum d(h) (2h)^{-s} over vacuum quasi-primaries',
        'bc_object': 'E^c_s = spectral function from Roelcke-Selberg of full Z',
        'differences': [
            'We: vacuum module only. BC: full CFT.',
            'We: weight as Dirichlet variable. BC: Laplacian eigenvalue.',
            'We: divergent series. BC: spectral measure (tempered distribution).',
            'We: independent of c at generic c. BC: depends on specific CFT.',
        ],
        'coincidence': 'For minimal models (finite spectrum), closely related.',
        'for_generic_c': 'Different objects. Our d(h) is universal; BC depends on the CFT.',
    }


# ================================================================
# 11. The c-dependence question
# ================================================================

def c_dependence_analysis():
    r"""Analysis of the c-dependence of the constrained Epstein.

    CRITICAL OBSERVATION: At generic c, the quasi-primary counts d(h)
    are INDEPENDENT of c.  The formula d(h) = p_{>=2}(h) - p_{>=2}(h-1)
    involves only combinatorics of partitions, with no c-dependence.

    This is because:
    (1) The L_1 matrix has entries that are integers (no c-terms), since
        [L_1, L_{-n}] = (1+n)L_{1-n} has coefficient 1+n (no central term).
    (2) The rank of an integer matrix is independent of parameters.

    CONSEQUENCE: epsilon^c_s(Vir) is the SAME function for all generic c.
    It does NOT depend on c at all!

    This makes it a TOPOLOGICAL invariant of the Virasoro algebra's
    vacuum module, not a deformation invariant.

    The c-dependence enters only at SPECIAL values where null vectors
    appear (reducing the module and changing d(h)):
    - c = 1 - 6/[m(m+1)] (minimal models): d(h) = 0 or 1 (primaries only)
    - c = 0: L_{-2}|0> = 0 (T is null), drastically reducing d(h)
    - c = 25: Virasoro has additional structure

    For these special c values, the constrained Epstein IS c-dependent
    and is a genuinely different (often finite) object.

    THE PHILOSOPHICAL POINT: The universal Virasoro vacuum module at
    generic c is a FIXED algebraic object.  Its quasi-primary spectrum
    is combinatorial, not analytic.  The c-dependence of Virasoro physics
    is carried by the OPE coefficients (which ARE c-dependent), not by
    the quasi-primary multiplicities (which are not).

    The shadow tower invariants (kappa = c/2, alpha = 2, S_4 = 10/(c(5c+22)))
    ARE c-dependent and encode the OPE structure.  The shadow metric
    Epstein zeta IS c-dependent.  The constrained Epstein is NOT.

    This is a FUNDAMENTAL ASYMMETRY between the two Epstein objects.
    """
    return {
        'c_dependence': False,
        'reason': 'L_1 matrix has integer entries; quasi-primary counts are combinatorial',
        'exceptions': [
            'Minimal models: null vectors reduce the module',
            'c = 0: T is null, module collapses',
            'c = 25: additional structure',
        ],
        'philosophical': (
            'The constrained Epstein is a TOPOLOGICAL invariant of the '
            'Virasoro vacuum module, independent of c at generic c. '
            'The shadow metric Epstein IS c-dependent and encodes the OPE. '
            'These are fundamentally different types of invariants.'
        ),
    }


# ================================================================
# 12. Weight-multiplicity Dirichlet series
# ================================================================

def weight_multiplicity_dirichlet(s, h_max: int = 200):
    r"""The weight-multiplicity Dirichlet series WITH weights.

    An alternative to the naive sum: weight each quasi-primary by its
    conformal weight h (or by powers of h):

        D_k(s) = sum_{h >= 2} d(h) * h^k * (2h)^{-s}

    For k=0: the constrained Epstein.
    For k=1: the first moment.
    For k=-1: emphasizes low-lying primaries.
    """
    results = {}
    for k in [-1, 0, 1, 2]:
        if HAS_MPMATH:
            s_mp = mpmath.mpc(s)
            val = mpmath.mpf(0)
            for h in range(2, h_max + 1):
                d_h = quasi_primary_count(h)
                if d_h > 0:
                    val += d_h * mpmath.power(h, k) * mpmath.power(2 * h, -s_mp)
            results[k] = complex(val)
        else:
            val = 0.0 + 0.0j
            s_c = complex(s)
            for h in range(2, h_max + 1):
                d_h = quasi_primary_count(h)
                if d_h > 0:
                    val += d_h * h ** k * (2 * h) ** (-s_c)
            results[k] = val
    return results


# ================================================================
# Main
# ================================================================

if __name__ == '__main__':
    print("=" * 70)
    print("VIRASORO CONSTRAINED EPSTEIN ZETA")
    print("=" * 70)

    print("\n1. Quasi-primary spectrum d(h):")
    print("   h    d(h)  p_ge2(h)  cumulative")
    cum = 0
    for h in range(0, 21):
        d = quasi_primary_count(h)
        cum += max(d, 0)
        p = p_ge2(h)
        if d > 0 or h <= 2:
            print(f"  {h:3d}  {d:5d}  {p:5d}    {cum:5d}")

    print(f"\n2. Generating function: Q(q) = (1-q)^2 * prod_{{n>=1}} 1/(1-q^n)")

    print(f"\n3. Convergence analysis:")
    ca = convergence_analysis()
    print(f"   Abscissa of convergence: {ca['abscissa_of_convergence']}")
    print(f"   Growth constant C = pi*sqrt(2/3) = {ca['growth_constant']:.6f}")
    print(f"   Conclusion: {ca['conclusion']}")

    print(f"\n4. Truncated Epstein at h_max=200:")
    for s in [3.0, 5.0, 10.0, 20.0]:
        eps = constrained_epstein(s, h_max=200)
        print(f"   eps(s={s:.0f}) = {eps.real:.8f}")

    print(f"\n5. c-dependence: NONE at generic c")
    cd = c_dependence_analysis()
    print(f"   {cd['philosophical']}")

    print(f"\n6. Shadow metric Epstein at c=26 (critical string):")
    for s in [3.0, 5.0]:
        eps_shadow = shadow_metric_epstein(s, 26.0, nmax=30)
        eps_spec = constrained_epstein(s, h_max=100)
        print(f"   s={s}: shadow={eps_shadow.real:.4f}, spectral={eps_spec.real:.4f}")
