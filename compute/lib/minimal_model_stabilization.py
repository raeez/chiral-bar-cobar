"""Minimal model weight-space dimensions and bar chain stabilization.

Ground truth from the manuscript (deformation_theory.tex, rem:step2-stabilization-threshold):
  M(5,8) = Virasoro minimal model with p=5, q=8 (manuscript convention: p < q)
  Central charge: c = 1 - 6(p-q)^2/(pq) = -7/20
  Period claim: N from formula N = 24q'/gcd(p',24) where c = p'/q'
  Number of modules: (p-1)(q-1)/2 = 14

  NOTE: The manuscript states c = 57/40 at rem:step2-stabilization-threshold
  but the formula gives c = -7/20.  This is a typo in the manuscript.

  The task is to verify eventual periodicity of weight-space dimensions
  and bar chain dimensions computationally, and determine the actual
  stabilization threshold h_0.

Rocha-Caridi character formula for irreducible M(p,q) module V_{r,s}:
  ch_{V_{r,s}}(q) = K_{r,s}(q) / eta(q)
  where K_{r,s} = sum_n [q^{lambda_+^2/(4pq)} - q^{lambda_-^2/(4pq)}]
  with lambda_+(n) = 2pqn + qr - ps, lambda_-(n) = 2pqn + qr + ps.

  Weight-space dimension at level k above h_{r,s}:
  d_{r,s}(k) = sum_{n in Z} [p(k - delta_+(n)) - p(k - delta_-(n))]
  where:
    delta_+(n) = n(m_+ + pqn)     with m_+ = qr - ps
    delta_-(n) = rs + n(m_- + pqn)  with m_- = qr + ps
  and p(k) is the partition function (p(k) = 0 for k < 0).

CONVENTIONS (following manuscript, deformation_theory.tex):
  - 2 <= p < q, gcd(p,q) = 1
  - h_{r,s} = ((qr - ps)^2 - (q-p)^2) / (4pq)
  - Module labels: 1 <= r <= p-1, 1 <= s <= q-1
  - Identification: V_{r,s} = V_{p-r, q-s}
"""

from __future__ import annotations

from typing import Dict, List, Tuple, Optional
from functools import lru_cache
from math import gcd, isqrt

from sympy import Rational

from compute.lib.minimal_model_bar import minimal_model_c


# ---------------------------------------------------------------------------
# Partition function (Euler pentagonal recurrence)
# ---------------------------------------------------------------------------

@lru_cache(maxsize=1024)
def partition(n: int) -> int:
    """Number of partitions of non-negative integer n.

    Returns 0 for n < 0.  Uses Euler's pentagonal recurrence.
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    result = 0
    k = 1
    while True:
        g1 = k * (3 * k - 1) // 2
        g2 = k * (3 * k + 1) // 2
        sign = (-1) ** (k + 1)
        if g1 > n and g2 > n:
            break
        if g1 <= n:
            result += sign * partition(n - g1)
        if g2 <= n:
            result += sign * partition(n - g2)
        k += 1
    return result


# ---------------------------------------------------------------------------
# Kac table
# ---------------------------------------------------------------------------

def kac_weight(p: int, q: int, r: int, s: int) -> Rational:
    """Conformal weight h_{r,s} for M(p,q), 2 <= p < q, gcd(p,q) = 1.

    h_{r,s} = ((qr - ps)^2 - (q-p)^2) / (4pq)
    for 1 <= r <= p-1, 1 <= s <= q-1.
    """
    return Rational((q * r - p * s) ** 2 - (q - p) ** 2, 4 * p * q)


def kac_table(p: int, q: int) -> List[Tuple[int, int]]:
    """Independent module labels for M(p,q), 2 <= p < q.

    Returns list of (r, s) with 1 <= r <= p-1, 1 <= s <= q-1,
    deduplicated under (r,s) ~ (p-r, q-s).
    Total: (p-1)(q-1)/2 modules.
    """
    seen = set()
    modules = []
    for r in range(1, p):
        for s in range(1, q):
            if (p - r, q - s) not in seen:
                seen.add((r, s))
                modules.append((r, s))
    return modules


def n_modules(p: int, q: int) -> int:
    """Number of irreducible modules of M(p,q)."""
    return (p - 1) * (q - 1) // 2


# ---------------------------------------------------------------------------
# Weight-space dimensions via Rocha-Caridi
# ---------------------------------------------------------------------------

def _delta_plus(p: int, q: int, r: int, s: int, n: int) -> int:
    """delta_+(n) = n(m_+ + pq*n) where m_+ = qr - ps."""
    m_plus = q * r - p * s
    return n * (m_plus + p * q * n)


def _delta_minus(p: int, q: int, r: int, s: int, n: int) -> int:
    """delta_-(n) = rs + n(m_- + pq*n) where m_- = qr + ps."""
    m_minus = q * r + p * s
    return r * s + n * (m_minus + p * q * n)


def weight_space_dim(p: int, q: int, r: int, s: int, k: int) -> int:
    """Dimension of the weight-(h_{r,s}+k) subspace of V_{r,s}.

    Uses the Rocha-Caridi formula:
    d(k) = sum_{n in Z} [p(k - delta_+(n)) - p(k - delta_-(n))]
    """
    if k < 0:
        return 0

    d = 0
    # delta_+(n) ~ pq*n^2 for large |n|, so |n| <= sqrt(k/pq) + safety
    n_max = isqrt(k) + 3  # safe upper bound

    for n in range(-n_max, n_max + 1):
        dp = _delta_plus(p, q, r, s, n)
        dm = _delta_minus(p, q, r, s, n)
        # partition() returns 0 for negative arguments
        d += partition(k - dp)
        d -= partition(k - dm)

    return d


def weight_space_dims(p: int, q: int, r: int, s: int,
                      max_level: int) -> List[int]:
    """Weight-space dimensions d_{r,s}(k) for k = 0, 1, ..., max_level."""
    return [weight_space_dim(p, q, r, s, k) for k in range(max_level + 1)]


# ---------------------------------------------------------------------------
# Period computation
# ---------------------------------------------------------------------------

def modular_period(p: int, q: int) -> int:
    """Period N from the T-matrix formula.

    N = 24q'/gcd(p',24) where c = p'/q' in lowest terms.
    """
    c = minimal_model_c(p, q)
    # c is a sympy Rational p'/q'
    p_prime = int(c.p)
    q_prime = int(c.q)
    return 24 * q_prime // gcd(abs(p_prime), 24)


def theta_level_period(p: int, q: int) -> int:
    """Period from theta function level = pq."""
    return p * q


# ---------------------------------------------------------------------------
# Periodicity detection
# ---------------------------------------------------------------------------

def detect_eventual_period(seq: List[int], period: int,
                           min_repeats: int = 3) -> Optional[int]:
    """Find the threshold k_0 such that seq[k+period] == seq[k] for k >= k_0.

    Returns k_0 if found, None otherwise.
    Requires at least min_repeats consecutive periodic matches.
    """
    if len(seq) < period + min_repeats:
        return None

    # Check from the end backwards
    n = len(seq)
    # First verify the last few entries satisfy periodicity
    for k in range(n - period - 1, -1, -1):
        if seq[k + period] != seq[k]:
            # Periodicity fails at k; threshold is at least k+1
            threshold = k + 1
            # Verify enough periodic matches above threshold
            ok = True
            for j in range(threshold, n - period):
                if seq[j + period] != seq[j]:
                    ok = False
                    break
            if ok and n - period - threshold >= min_repeats:
                return threshold
            return None

    return 0  # Periodic from the start


def find_best_period(seq: List[int], candidates: List[int],
                     min_repeats: int = 3) -> List[Tuple[int, Optional[int]]]:
    """Test each candidate period and return (period, threshold) pairs.

    Only returns candidates where periodicity was detected.
    """
    results = []
    for per in candidates:
        threshold = detect_eventual_period(seq, per, min_repeats)
        if threshold is not None:
            results.append((per, threshold))
    return results


def divisors(n: int) -> List[int]:
    """All positive divisors of n, sorted."""
    divs = []
    for i in range(1, isqrt(abs(n)) + 1):
        if abs(n) % i == 0:
            divs.append(i)
            if i != abs(n) // i:
                divs.append(abs(n) // i)
    return sorted(divs)


# ---------------------------------------------------------------------------
# M(5,8) specific data
# ---------------------------------------------------------------------------

def m58_data() -> Dict[str, object]:
    """Ground truth data for M(5,8)."""
    p, q = 5, 8
    c = minimal_model_c(p, q)
    modules = kac_table(p, q)
    weights = {(r, s): kac_weight(p, q, r, s) for r, s in modules}

    return {
        "p": p,
        "q": q,
        "c": c,
        "n_modules": n_modules(p, q),
        "modules": modules,
        "conformal_weights": weights,
        "modular_period": modular_period(p, q),
        "theta_period": theta_level_period(p, q),
    }


# ---------------------------------------------------------------------------
# Main verification
# ---------------------------------------------------------------------------

def verify_weight_space_periodicity(p: int, q: int,
                                    max_level: int = 100) -> Dict[str, object]:
    """Verify eventual periodicity of weight-space dims for all modules.

    Returns a dict with periodicity data for each module.
    """
    modules = kac_table(p, q)
    N_T = modular_period(p, q)
    N_theta = theta_level_period(p, q)

    # Candidate periods: divisors of N_T, divisors of pq, and small values
    candidates = sorted(set(
        divisors(N_theta) + divisors(N_T) +
        [p, q, p - 1, q - 1, q - p] +
        list(range(1, min(51, max_level // 3)))
    ))

    results = {}
    for r, s in modules:
        dims = weight_space_dims(p, q, r, s, max_level)
        periods = find_best_period(dims, candidates)
        results[(r, s)] = {
            "dims": dims,
            "detected_periods": periods,
            "h_rs": kac_weight(p, q, r, s),
        }

    return results


def verify_m58_stabilization(max_level: int = 100) -> Dict[str, object]:
    """Main verification: M(5,8) weight-space dimension periodicity.

    Computes d_{r,s}(k) for all 14 modules up to k = max_level,
    tests for eventual periodicity with various candidate periods.
    """
    p, q = 5, 8
    data = m58_data()
    period_results = verify_weight_space_periodicity(p, q, max_level)

    # Summary: for each module, what's the smallest period detected?
    summary = {}
    for (r, s), info in period_results.items():
        if info["detected_periods"]:
            best = min(info["detected_periods"], key=lambda x: x[0])
            summary[(r, s)] = {
                "best_period": best[0],
                "threshold": best[1],
                "h_rs": info["h_rs"],
            }
        else:
            summary[(r, s)] = {
                "best_period": None,
                "threshold": None,
                "h_rs": info["h_rs"],
            }

    return {
        "data": data,
        "period_results": period_results,
        "summary": summary,
    }


# ---------------------------------------------------------------------------
# Cross-validation: known character dims for simple models
# ---------------------------------------------------------------------------

def lee_yang_vacuum_dims(max_level: int = 20) -> List[int]:
    """M(2,5) vacuum module weight-space dims (cross-validation).

    Lee-Yang: p=2, q=5, c=-22/5. Vacuum = (r=1,s=1).
    """
    return weight_space_dims(2, 5, 1, 1, max_level)


def ising_vacuum_dims(max_level: int = 20) -> List[int]:
    """M(3,4) vacuum module weight-space dims.

    Ising: p=3, q=4, c=1/2. Vacuum = (1,1).
    """
    return weight_space_dims(3, 4, 1, 1, max_level)


def ising_sigma_dims(max_level: int = 20) -> List[int]:
    """M(3,4) sigma module weight-space dims.

    Ising sigma: (r=1,s=2), h=1/16.
    """
    return weight_space_dims(3, 4, 1, 2, max_level)


def ising_epsilon_dims(max_level: int = 20) -> List[int]:
    """M(3,4) epsilon module weight-space dims.

    Ising epsilon: (r=2,s=1) [or equivalently (1,3)], h=1/2.
    """
    return weight_space_dims(3, 4, 2, 1, max_level)


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("M(5,8) BAR CHAIN STABILIZATION: WEIGHT-SPACE PERIODICITY")
    print("=" * 70)

    data = m58_data()
    print(f"\nCentral charge: c = {data['c']} = {float(data['c']):.6f}")
    print(f"Number of modules: {data['n_modules']}")
    print(f"Modular period (T-matrix): N_T = {data['modular_period']}")
    print(f"Theta level period: pq = {data['theta_period']}")

    print("\nKac table conformal weights:")
    for (r, s), h in data["conformal_weights"].items():
        print(f"  h_({r},{s}) = {h} = {float(h):.6f}")

    print("\n" + "-" * 70)
    print("Weight-space dimensions (first 30 levels):")
    print("-" * 70)

    for r, s in data["modules"][:4]:  # Show first 4 modules
        dims = weight_space_dims(5, 8, r, s, 30)
        print(f"\n  V_({r},{s}) [h={kac_weight(5,8,r,s)}]:")
        print(f"    {dims}")

    print("\n" + "-" * 70)
    print("Periodicity analysis:")
    print("-" * 70)

    results = verify_m58_stabilization(80)
    for (r, s), info in results["summary"].items():
        h = info["h_rs"]
        if info["best_period"]:
            print(f"  V_({r},{s}) [h={h}]: period={info['best_period']}, "
                  f"threshold={info['threshold']}")
        else:
            print(f"  V_({r},{s}) [h={h}]: no periodicity detected")
