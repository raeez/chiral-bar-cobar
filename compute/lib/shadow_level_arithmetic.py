r"""
shadow_level_arithmetic.py — Per-channel arithmetic at the shadow level.

The key insight: individual characters eta * chi_{r,s} are theta functions
(Rocha-Caridi), so (eta * chi)^2 is a modular form on a CONGRUENCE SUBGROUP
Gamma(N) where N = 4pq for M(p,q).  On the subgroup, Hecke theory applies
and coefficients should be multiplicative AWAY FROM level primes.

The FULL partition function Z = sum |chi_i|^2 sums forms on different
subgroups, destroying multiplicativity.  This explains WHY Z fails
multiplicativity (prop:rational-cft-multiplicativity-failure) and WHERE
the structure survives (per-channel, shadow-separated).

Three levels of arithmetic:
  Level 0: Full partition function |eta|^2 Z (FAILS multiplicativity)
  Level 1: Per-channel |eta * chi_i|^2 (congruence subgroup structure)
  Level 2: Shadow projection Sh_r (graph sum, inherits from Level 1)

This module tests Level 1 and its interaction with Level 0.

References:
  - arithmetic_shadows.tex: prop:rational-cft-multiplicativity-failure,
    prop:stieltjes-signed-universal, sec:prime-locality-frontier Route D
  - vvmf_hecke.py: character q-series (Rocha-Caridi)

GRADING: Cohomological, |d| = +1.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd
from typing import Any, Dict, List, Optional, Tuple

import mpmath
from mpmath import mp, mpf, mpc, pi, exp, fsum, power, fabs, log as mplog

from compute.lib.vvmf_hecke import (
    MinimalModel,
    character_qseries,
    ising_model,
    tricritical_ising_model,
    three_state_potts_model,
    _eta_coeffs,
)


# ===========================================================================
# Per-channel Rankin-Selberg coefficients
# ===========================================================================

def per_channel_coefficients(
    model: MinimalModel,
    num_terms: int = 100,
    dps: int = 50,
) -> Dict[Tuple[int, int], List[mpf]]:
    """Compute per-channel |eta * chi_{r,s}|^2 coefficients for each primary.

    At imaginary tau, characters and eta are real, so
    |eta * chi|^2 = (eta * chi)^2.

    The Rocha-Caridi formula gives eta * chi = theta_{r,s}, a theta
    function on a 1D lattice.  So (eta * chi)^2 = theta^2 is a modular
    form on a congruence subgroup Gamma(4pq).

    Returns dict {(r,s): [b_0, b_1, ...]} where b_n are coefficients
    of q^n in the expansion of |eta * chi_{r,s}|^2 (after factoring
    out the leading q-power).
    """
    mp.dps = dps
    eta = _eta_coeffs(num_terms)
    labels = model.primary_labels()

    result = {}
    for lab in labels:
        # Character degeneracies
        d = character_qseries(model, lab.r, lab.s, num_terms=num_terms, dps=dps)

        # eta * chi coefficients (convolution)
        eta_chi = [mpf(0)] * num_terms
        for i in range(num_terms):
            if eta[i] == 0:
                continue
            for j in range(num_terms - i):
                if d[j] == 0:
                    continue
                eta_chi[i + j] += mpf(eta[i]) * d[j]

        # |eta * chi|^2 = (eta * chi)^2 at imaginary tau
        b = [mpf(0)] * num_terms
        for i in range(num_terms):
            if eta_chi[i] == 0:
                continue
            for j in range(num_terms - i):
                if eta_chi[j] == 0:
                    continue
                b[i + j] += eta_chi[i] * eta_chi[j]

        result[(lab.r, lab.s)] = b

    return result


def full_partition_coefficients(
    model: MinimalModel,
    num_terms: int = 100,
    dps: int = 50,
) -> List[mpf]:
    """Compute |eta|^2 Z = sum_i |eta chi_i|^2 coefficients.

    This is the Level 0 quantity that FAILS multiplicativity.
    """
    channels = per_channel_coefficients(model, num_terms=num_terms, dps=dps)
    result = [mpf(0)] * num_terms
    for key, b in channels.items():
        for n in range(min(num_terms, len(b))):
            result[n] += b[n]
    return result


# ===========================================================================
# Level-aware multiplicativity test
# ===========================================================================

def _is_coprime_to(n: int, level_primes: List[int]) -> bool:
    """Check if n is coprime to all level primes."""
    for p in level_primes:
        if n % p == 0:
            return False
    return True


def level_aware_multiplicativity(
    coeffs: List[mpf],
    level_primes: List[int],
    max_n: int = 50,
    tol: float = 1e-8,
) -> Dict[str, Any]:
    """Test multiplicativity AWAY FROM level primes.

    For a form on Gamma(N), we expect a_{mn} = a_m a_n when:
    (i)  gcd(m, n) = 1
    (ii) gcd(mn, N) = 1 (both m, n coprime to level)

    Also tests multiplicativity at the level primes (expected to fail).
    """
    N = min(max_n + 1, len(coeffs))

    # Test away from level primes
    away_failures = []
    away_tests = 0
    for m in range(2, N):
        if not _is_coprime_to(m, level_primes):
            continue
        for n in range(m + 1, N):
            if m * n >= N:
                break
            if gcd(m, n) != 1:
                continue
            if not _is_coprime_to(n, level_primes):
                continue
            away_tests += 1
            diff = fabs(coeffs[m * n] - coeffs[m] * coeffs[n])
            if diff > tol:
                away_failures.append((m, n, float(diff)))

    # Test at level primes
    level_failures = []
    level_tests = 0
    for m in range(2, N):
        for n in range(2, N):
            if m * n >= N:
                break
            if gcd(m, n) != 1:
                continue
            if _is_coprime_to(m, level_primes) and _is_coprime_to(n, level_primes):
                continue  # already tested above
            level_tests += 1
            diff = fabs(coeffs[m * n] - coeffs[m] * coeffs[n])
            if diff > tol:
                level_failures.append((m, n, float(diff)))

    return {
        'away_from_level': {
            'tests': away_tests,
            'failures': len(away_failures),
            'is_multiplicative': len(away_failures) == 0,
            'first_failures': away_failures[:5],
        },
        'at_level_primes': {
            'tests': level_tests,
            'failures': len(level_failures),
            'is_multiplicative': len(level_failures) == 0,
            'first_failures': level_failures[:5],
        },
        'level_primes': level_primes,
    }


def congruence_level(model: MinimalModel) -> int:
    """Congruence level N for M(p,q): the theta functions live on Gamma(4pq)."""
    return 4 * model.p * model.q


def level_primes_for_model(model: MinimalModel) -> List[int]:
    """Prime factors of the congruence level 4pq."""
    N = congruence_level(model)
    primes = set()
    for p in range(2, N + 1):
        while N % p == 0:
            primes.add(p)
            N //= p
        if N == 1:
            break
    return sorted(primes)


# ===========================================================================
# Per-channel multiplicativity analysis
# ===========================================================================

def per_channel_multiplicativity(
    model: MinimalModel,
    num_terms: int = 80,
    max_test: int = 30,
    dps: int = 50,
) -> Dict[str, Any]:
    """Test per-channel multiplicativity for each primary field.

    For each character chi_i, computes b_n = (eta * chi_i)^2 coefficients
    and tests:
    (a) Full multiplicativity: b_{mn} = b_m b_n for all coprime (m,n)
    (b) Level-aware multiplicativity: away from level primes

    Returns structured report for each channel.
    """
    mp.dps = dps
    channels = per_channel_coefficients(model, num_terms=num_terms, dps=dps)
    lp = level_primes_for_model(model)
    level = congruence_level(model)

    report: Dict[str, Any] = {
        'model': f"M({model.p},{model.q})",
        'congruence_level': level,
        'level_primes': lp,
        'channels': {},
    }

    for (r, s), coeffs in channels.items():
        # Normalize: divide by b_0 if nonzero
        b0 = coeffs[0] if coeffs[0] != 0 else mpf(1)
        normed = [c / b0 for c in coeffs]

        # Full multiplicativity test
        full_failures = []
        for m in range(2, min(max_test, len(normed))):
            for n in range(m + 1, min(max_test, len(normed))):
                if m * n >= len(normed):
                    break
                if gcd(m, n) != 1:
                    continue
                diff = fabs(normed[m * n] - normed[m] * normed[n])
                if diff > 1e-8:
                    full_failures.append((m, n, float(diff)))

        # Level-aware test
        level_result = level_aware_multiplicativity(
            normed, lp, max_n=max_test
        )

        report['channels'][(r, s)] = {
            'b_0': float(b0),
            'first_coeffs': [float(c) for c in normed[:15]],
            'full_multiplicative': len(full_failures) == 0,
            'full_failures': len(full_failures),
            'full_first_failures': full_failures[:3],
            'level_aware': level_result,
        }

    return report


# ===========================================================================
# Cross-channel diagnostic
# ===========================================================================

def cross_channel_diagnostic(
    model: MinimalModel,
    num_terms: int = 80,
    dps: int = 50,
) -> Dict[str, Any]:
    """Diagnose the partition function multiplicativity failure.

    Decompose a_n = sum_i b_n^{(i)} and identify which cross-terms
    cause the failure.

    For multiplicativity of the sum:
    a_{mn} = sum_i b_{mn}^{(i)} vs a_m a_n = (sum_i b_m^{(i)})(sum_j b_n^{(j)})
    = sum_i b_m^{(i)} b_n^{(i)} + sum_{i!=j} b_m^{(i)} b_n^{(j)}

    If each b is multiplicative: sum_i b_m b_n = sum_i b_{mn}
    So defect = sum_{i!=j} b_m^{(i)} b_n^{(j)} (the cross terms).
    """
    mp.dps = dps
    channels = per_channel_coefficients(model, num_terms=num_terms, dps=dps)
    keys = sorted(channels.keys())

    # Full partition function
    a = [mpf(0)] * num_terms
    for key in keys:
        b = channels[key]
        for n in range(min(num_terms, len(b))):
            a[n] += b[n]

    # Compute cross-term contribution at specific (m,n) pairs
    diagnostics = []
    test_pairs = [(2, 3), (2, 5), (2, 7), (3, 5), (3, 7), (5, 7)]

    for m, n in test_pairs:
        if m * n >= num_terms:
            continue

        # Full defect
        full_defect = float(a[m * n] - a[m] * a[n])

        # Diagonal contribution: sum_i b_m^{(i)} b_n^{(i)}
        diagonal = mpf(0)
        for key in keys:
            b = channels[key]
            if m < len(b) and n < len(b):
                diagonal += b[m] * b[n]

        # Per-channel defect: sum_i (b_{mn}^{(i)} - b_m^{(i)} b_n^{(i)})
        channel_defect = mpf(0)
        for key in keys:
            b = channels[key]
            if m * n < len(b) and m < len(b) and n < len(b):
                channel_defect += b[m * n] - b[m] * b[n]

        # Cross terms: a_m a_n - diagonal = sum_{i!=j} b_m^{(i)} b_n^{(j)}
        cross_terms = float(a[m] * a[n] - diagonal)

        diagnostics.append({
            'pair': (m, n),
            'full_defect': full_defect,
            'channel_defect': float(channel_defect),
            'cross_terms': cross_terms,
            'defect_from_channels': float(channel_defect),
            'defect_from_cross': cross_terms,
        })

    return {
        'model': f"M({model.p},{model.q})",
        'num_channels': len(keys),
        'diagnostics': diagnostics,
    }


# ===========================================================================
# Connected free energy
# ===========================================================================

def connected_free_energy_coefficients(
    model: MinimalModel,
    num_terms: int = 60,
    dps: int = 50,
) -> List[mpf]:
    """Compute connected free energy F^conn = log(Z_normalized) coefficients.

    Z_normalized = Z / Z_leading = 1 + sum_{n>=1} a_n q^n
    F^conn = log(Z_norm) = sum_{n>=1} c_n q^n

    Connected coefficients via cumulant:
    c_1 = a_1
    c_n = a_n - sum_{partitions} products of c_j (Moebius inversion)
    """
    mp.dps = dps
    a = full_partition_coefficients(model, num_terms=num_terms, dps=dps)

    if a[0] == 0:
        return [mpf(0)] * num_terms

    # Normalize so a_0 = 1
    norm = [c / a[0] for c in a]

    # log(1 + sum_{n>=1} a_n q^n) via Newton's formula
    c = [mpf(0)] * num_terms
    for n in range(1, num_terms):
        c[n] = norm[n]
        for k in range(1, n):
            c[n] -= Fraction(k, n) * c[k] * norm[n - k]

    return c


# ===========================================================================
# Comprehensive shadow-level report
# ===========================================================================

def shadow_level_report(
    model: MinimalModel,
    num_terms: int = 60,
    max_test: int = 25,
    dps: int = 50,
) -> Dict[str, Any]:
    """Comprehensive shadow-level arithmetic report.

    Tests three levels:
    Level 0: Full partition function (KNOWN to fail)
    Level 1: Per-channel (eta * chi_i)^2
    Level 2: Connected free energy
    """
    mp.dps = dps

    report: Dict[str, Any] = {
        'model': f"M({model.p},{model.q})",
        'congruence_level': congruence_level(model),
        'level_primes': level_primes_for_model(model),
    }

    # Level 1: per-channel
    report['level_1_per_channel'] = per_channel_multiplicativity(
        model, num_terms=num_terms, max_test=max_test, dps=dps
    )

    # Cross-channel diagnostic
    report['cross_channel'] = cross_channel_diagnostic(
        model, num_terms=num_terms, dps=dps
    )

    # Level 2: connected free energy
    c_coeffs = connected_free_energy_coefficients(
        model, num_terms=num_terms, dps=dps
    )
    # Test multiplicativity of connected coefficients
    lp = level_primes_for_model(model)
    report['level_2_connected'] = level_aware_multiplicativity(
        c_coeffs, lp, max_n=max_test
    )
    report['level_2_connected']['first_coeffs'] = [float(c) for c in c_coeffs[:10]]

    return report
