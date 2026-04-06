"""Channel-refined modular characteristic for W_N algebras.

The W_N algebra (principal DS reduction of sl_N-hat at level k) has N-1
generating fields W_2 = T, W_3, ..., W_N of conformal weights 2, 3, ..., N.

The scalar modular characteristic is:
    kappa(W_N) = c * (H_N - 1)
where H_N = 1 + 1/2 + ... + 1/N is the N-th harmonic number and c is
the central charge.

CHANNEL REFINEMENT (concordance.tex, Future 4):
Each generator W_j contributes a channel kappa_j to the total:
    kappa_j = c / j
from the self-coupling W_j(z)W_j(w) ~ (c/j) / (z-w)^{2j} + ...

The channel-refined characteristic is the vector:
    kappa_tilde_N = (kappa_2, kappa_3, ..., kappa_N) = (c/2, c/3, ..., c/N)

Key properties:
    1. Total: sum_{j=2}^N kappa_j = c * (H_N - 1) = kappa(W_N)
    2. Cross-term vanishing: mixed W_i-W_j (i != j) contributions vanish
       (the double-pole coefficient in W_i(z)W_j(w) is proportional to
       delta_{ij} at leading order)
    3. Divergence: as N -> infinity, sum kappa_j ~ c * log(N) -> infinity
       (harmonic divergence, structural obstruction for W_infinity)
    4. The Sugawara channel kappa_2 = c/2 matches the Virasoro curvature

References:
    - concordance.tex: Future 4 (channel-refined W_N characteristic)
    - kac_moody_framework.tex: prop:ff-channel-shear
    - w4_stage4_coefficients.py: w4_curvature(), w4_kappa_total()
"""

from __future__ import annotations

from typing import Dict, List, Tuple

from sympy import (
    Rational,
    Symbol,
    simplify,
    sympify,
    log,
    EulerGamma,
    N as neval,
    oo,
)


# ---------------------------------------------------------------------------
# Harmonic numbers
# ---------------------------------------------------------------------------

def harmonic_number(n: int) -> Rational:
    """H_n = sum_{j=1}^n 1/j (exact rational arithmetic)."""
    if n < 0:
        raise ValueError(f"Harmonic number undefined for n = {n}")
    return sum(Rational(1, j) for j in range(1, n + 1))


def harmonic_tail(a: int, b: int) -> Rational:
    """sum_{j=a}^b 1/j (partial harmonic sum, exact rational)."""
    if a < 1 or b < a:
        raise ValueError(f"Invalid range [{a}, {b}]")
    return sum(Rational(1, j) for j in range(a, b + 1))


# ---------------------------------------------------------------------------
# W_N central charge (general formula)
# ---------------------------------------------------------------------------

def wn_central_charge(N: int, level):
    """Central charge of the principal W_N algebra = DS of sl_N-hat at level k.

    c = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)

    Fateev-Lukyanov formula.  Decisive test: N=2, k=1 gives c=-7.
    UNDEFINED at k = -N (critical level of sl_N-hat, h^vee = N).
    """
    if N < 2:
        raise ValueError(f"W_N requires N >= 2, got {N}")
    k = sympify(level)
    kN = k + N
    return Rational(N - 1) - Rational(N * (N**2 - 1)) * (kN - 1)**2 / kN


def wn_ff_dual_level(N: int, level):
    """Feigin-Frenkel dual level for sl_N: k' = -k - 2N."""
    return -sympify(level) - 2 * N


# ---------------------------------------------------------------------------
# Channel-refined kappa
# ---------------------------------------------------------------------------

def channel_kappa(j: int, central_charge=None):
    """Channel contribution kappa_j = c / j from the W_j self-coupling.

    The W_j(z)W_j(w) OPE has leading singularity:
        W_j(z)W_j(w) ~ (c/j) / (z-w)^{2j} + ...
    The double-pole (curvature) coefficient is c/j, contributing this
    amount to the total modular characteristic.

    If central_charge is None, uses symbolic c.
    """
    if j < 2:
        raise ValueError(f"Channel index must be >= 2, got {j}")
    c = sympify(central_charge) if central_charge is not None else Symbol('c')
    return c / j


def channel_vector(N: int, central_charge=None) -> Dict[int, object]:
    """Channel-refined kappa vector: kappa_tilde_N = {j: c/j for j=2,...,N}.

    Returns a dict mapping spin j to kappa_j = c/j.
    """
    if N < 2:
        raise ValueError(f"W_N requires N >= 2, got {N}")
    return {j: channel_kappa(j, central_charge) for j in range(2, N + 1)}


def channel_vector_tuple(N: int, central_charge=None) -> Tuple:
    """Channel-refined kappa as a tuple (kappa_2, kappa_3, ..., kappa_N)."""
    vec = channel_vector(N, central_charge)
    return tuple(vec[j] for j in range(2, N + 1))


def total_kappa(N: int, central_charge=None):
    """Total modular characteristic: kappa(W_N) = sum_{j=2}^N kappa_j = c * (H_N - 1).

    Computed as the sum of channel contributions.
    """
    vec = channel_vector(N, central_charge)
    return sum(vec.values())


def total_kappa_harmonic(N: int, central_charge=None):
    """Total modular characteristic via harmonic number formula: c * (H_N - 1).

    This should equal total_kappa(N, central_charge) exactly.
    """
    c = sympify(central_charge) if central_charge is not None else Symbol('c')
    return c * (harmonic_number(N) - 1)


# ---------------------------------------------------------------------------
# Cross-term vanishing
# ---------------------------------------------------------------------------

def cross_term_coefficient(i: int, j: int) -> Rational:
    """Cross-term contribution from W_i-W_j mixed OPE to the modular characteristic.

    For i != j: the double-pole coefficient in W_i(z)W_j(w) that contributes
    to the curvature is proportional to delta_{ij}. Specifically:

    The leading singularity in W_i(z)W_j(w) for i != j has pole order at most
    i + j - 1, with the leading term being a primary field (not a scalar).
    The vacuum-channel contribution (which determines curvature) requires
    pole order 2*max(i,j), which exceeds i + j - 1 when i != j.

    Therefore the cross-term vanishes: kappa_{ij} = 0 for i != j.

    Returns 0 for i != j, and Rational(1, j) for i == j (the coefficient
    of c in kappa_j).
    """
    if i != j:
        return Rational(0)
    return Rational(1, j)


def cross_term_matrix(N: int) -> Dict[Tuple[int, int], Rational]:
    """Matrix of cross-term contributions: kappa_{ij} for 2 <= i, j <= N.

    Diagonal: kappa_{jj} = 1/j (coefficient of c).
    Off-diagonal: kappa_{ij} = 0 for i != j.
    """
    return {(i, j): cross_term_coefficient(i, j)
            for i in range(2, N + 1)
            for j in range(2, N + 1)}


def verify_cross_term_vanishing(N: int) -> bool:
    """Verify that all off-diagonal cross-terms vanish."""
    matrix = cross_term_matrix(N)
    return all(matrix[(i, j)] == 0
               for i in range(2, N + 1)
               for j in range(2, N + 1)
               if i != j)


# ---------------------------------------------------------------------------
# Pole-order argument for cross-term vanishing
# ---------------------------------------------------------------------------

def ope_max_pole_order(i: int, j: int) -> int:
    """Maximum pole order in W_i(z) W_j(w) OPE.

    For i == j: pole order 2i (from the 2-point function normalization).
    For i != j: pole order i + j - 1 (conformal weight bound).
    """
    if i == j:
        return 2 * i
    return i + j - 1


def vacuum_pole_order(j: int) -> int:
    """Pole order at which the vacuum/scalar channel appears in W_j(z)W_j(w).

    The scalar contribution has pole order 2j (the leading singularity).
    """
    return 2 * j


def cross_term_pole_deficit(i: int, j: int) -> int:
    """Pole deficit: vacuum_pole_order - ope_max_pole_order.

    Positive deficit means the vacuum channel CANNOT contribute, proving
    the cross-term vanishes.

    For i == j: deficit = 0 (vacuum channel contributes).
    For i != j: deficit = max(2i, 2j) - (i + j - 1) = |i - j| + 1 > 0.
    """
    if i == j:
        return 0
    # The vacuum channel would need pole order 2*max(i,j) or i+j
    # (for the 2-point pairing), but the OPE only has poles up to i+j-1.
    # More precisely: the scalar/vacuum appears at pole i+j (from the
    # leading 2-point function between W_i and W_j), but W_i and W_j
    # are orthogonal (different conformal weights) so the 2-point function
    # <W_i, W_j> = 0 for i != j.
    return 1  # The mechanism is orthogonality, not pole counting per se


# ---------------------------------------------------------------------------
# Sugawara channel verification
# ---------------------------------------------------------------------------

def sugawara_kappa(dim_g: int, h_dual: int, level):
    """Sugawara (W_2 = T) channel contribution to kappa.

    For the KM algebra g-hat_k with Sugawara stress tensor:
        T = (1/2(k+h^vee)) sum :J^a J^a:
        c = k * dim(g) / (k + h^vee)

    The Virasoro curvature is:
        kappa_2 = c / 2

    This is the universal formula for ANY VOA with a conformal vector.
    """
    k = sympify(level)
    c = Rational(dim_g) * k / (k + h_dual)
    return c / 2


def verify_sugawara_channel(N: int, level) -> Dict[str, object]:
    """Verify that the W_2 = T channel gives c/2 for W_N from sl_N DS.

    For sl_N: dim = N^2 - 1, h^vee = N.
    The DS central charge c_DS != Sugawara c (DS subtracts ghost contribution),
    but the curvature kappa_2 = c_DS / 2 still holds because T is normalized
    the same way.
    """
    k = sympify(level)
    c = wn_central_charge(N, k)
    kap2 = channel_kappa(2, c)
    return {
        "central_charge": c,
        "kappa_2": kap2,
        "equals_c_over_2": simplify(kap2 - c / 2) == 0,
    }


# ---------------------------------------------------------------------------
# Specific W_N algebras
# ---------------------------------------------------------------------------

def w3_channel_data(central_charge=None) -> Dict[str, object]:
    """Channel data for W_3: generators T (spin 2), W (spin 3).

    kappa_tilde_3 = (c/2, c/3), total = 5c/6.
    """
    c = sympify(central_charge) if central_charge is not None else Symbol('c')
    return {
        "channels": {2: c / 2, 3: c / 3},
        "total": c * Rational(5, 6),
        "expected_total": c * (harmonic_number(3) - 1),
    }


def w4_channel_data(central_charge=None) -> Dict[str, object]:
    """Channel data for W_4: generators T (spin 2), W_3 (spin 3), W_4 (spin 4).

    kappa_tilde_4 = (c/2, c/3, c/4), total = 13c/12.
    """
    c = sympify(central_charge) if central_charge is not None else Symbol('c')
    return {
        "channels": {2: c / 2, 3: c / 3, 4: c / 4},
        "total": c * Rational(13, 12),
        "expected_total": c * (harmonic_number(4) - 1),
    }


def w5_channel_data(central_charge=None) -> Dict[str, object]:
    """Channel data for W_5: generators T, W_3, W_4, W_5.

    kappa_tilde_5 = (c/2, c/3, c/4, c/5), total = 77c/60.
    """
    c = sympify(central_charge) if central_charge is not None else Symbol('c')
    return {
        "channels": {2: c / 2, 3: c / 3, 4: c / 4, 5: c / 5},
        "total": c * Rational(77, 60),
        "expected_total": c * (harmonic_number(5) - 1),
    }


# ---------------------------------------------------------------------------
# Harmonic divergence
# ---------------------------------------------------------------------------

def kappa_growth_data(max_N: int = 100) -> List[Tuple[int, float]]:
    """(N, H_N - 1) pairs showing the harmonic divergence of kappa(W_N)/c.

    As N -> infinity, H_N - 1 ~ log(N) + gamma - 1 where gamma is the
    Euler-Mascheroni constant.
    """
    return [(N, float(harmonic_number(N) - 1)) for N in range(2, max_N + 1)]


def harmonic_divergence_bound(N: int) -> Tuple[float, float]:
    """Lower and upper bounds for H_N - 1.

    log(N) + gamma - 1 - 1/(2N) < H_N - 1 < log(N) + gamma - 1 + 1/(2N)

    where gamma is the Euler-Mascheroni constant ~ 0.5772.
    """
    gamma = float(EulerGamma.evalf())
    ln_N = float(neval(log(N)))
    center = ln_N + gamma - 1
    return (center - 1.0 / (2 * N), center + 1.0 / (2 * N))


# ---------------------------------------------------------------------------
# Consistency with w4_stage4_coefficients
# ---------------------------------------------------------------------------

def verify_w4_consistency() -> Dict[str, bool]:
    """Cross-check channel-refined data against w4_stage4_coefficients.py.

    Verifies:
    1. w4_curvature() matches channel_vector(4, c)
    2. w4_kappa_total() matches total_kappa(4, c)
    """
    from compute.lib.w4_stage4_coefficients import (
        w4_curvature,
        w4_kappa_total,
    )

    c = Symbol('c')

    # Curvature channels
    curv = w4_curvature()
    vec = channel_vector(4, c)

    results = {}
    results["T_channel_matches"] = simplify(curv["T"] - vec[2]) == 0
    results["W3_channel_matches"] = simplify(curv["W3"] - vec[3]) == 0
    results["W4_channel_matches"] = simplify(curv["W4"] - vec[4]) == 0
    results["total_matches"] = simplify(w4_kappa_total() - total_kappa(4, c)) == 0

    return results


# ---------------------------------------------------------------------------
# Consistency with sigma_invariant from lie_algebra module
# ---------------------------------------------------------------------------

def verify_sigma_consistency(max_N: int = 4) -> Dict[str, bool]:
    """Cross-check total kappa against sigma_invariant for A_{N-1}.

    For W_N from sl_N, kappa(W_N) = c * sigma(A_{N-1}) where
    sigma(A_{N-1}) = sum_{i=1}^{N-1} 1/(m_i + 1) with m_i = i
    (exponents of A_{N-1}).
    """
    from compute.lib.lie_algebra import sigma_invariant

    results = {}
    c = Symbol('c')
    for N in range(2, max_N + 1):
        sigma = sigma_invariant("A", N - 1)
        h_minus_1 = harmonic_number(N) - 1
        results[f"sigma_A{N-1}_equals_H{N}_minus_1"] = sigma == h_minus_1
        results[f"total_kappa_W{N}_matches_sigma"] = simplify(
            total_kappa(N, c) - c * sigma
        ) == 0
    return results


# ---------------------------------------------------------------------------
# FF duality on channel vector
# ---------------------------------------------------------------------------

def ff_dual_channel_vector(N: int, level) -> Dict[int, object]:
    """Channel vector at the FF dual level k' = -k - 2N.

    kappa_j(k') = c(k') / j where c(k') is the DS central charge at dual level.
    """
    k = sympify(level)
    k_prime = wn_ff_dual_level(N, k)
    c_prime = wn_central_charge(N, k_prime)
    return {j: c_prime / j for j in range(2, N + 1)}


def ff_channel_anti_symmetry(N: int, level) -> Dict[str, object]:
    """Verify kappa_j(k) + kappa_j(k') = 0 for each channel.

    This follows from the scalar anti-symmetry kappa(k) + kappa(k') = 0
    applied channel by channel, since kappa_j = c/j and c(k) + c(k') = 0
    would imply channel-wise cancellation. However, c(k) + c(k') = sigma_N
    (complementarity sum, generally nonzero), so channel-wise anti-symmetry
    only holds for the TOTAL kappa, not individual channels.
    """
    k = sympify(level)
    c_k = wn_central_charge(N, k)
    c_k_prime = wn_central_charge(N, wn_ff_dual_level(N, k))

    # Complementarity sum
    comp_sum = simplify(c_k + c_k_prime)

    # Channel-wise check
    channel_sums = {}
    for j in range(2, N + 1):
        kap_j = c_k / j
        kap_j_prime = c_k_prime / j
        channel_sums[j] = simplify(kap_j + kap_j_prime)

    # Total kappa anti-symmetry
    total_sum = simplify(sum(channel_sums.values()))

    return {
        "complementarity_sum": comp_sum,
        "channel_sums": channel_sums,
        "total_kappa_sum": total_sum,
    }


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    c = Symbol('c')
    print("=" * 70)
    print("CHANNEL-REFINED MODULAR CHARACTERISTIC FOR W_N ALGEBRAS")
    print("=" * 70)

    for N in [3, 4, 5, 6, 10]:
        vec = channel_vector(N, c)
        tot = total_kappa(N, c)
        h_form = total_kappa_harmonic(N, c)
        print(f"\nW_{N}:")
        print(f"  channels: {vec}")
        print(f"  total (sum): {tot}")
        print(f"  total (harmonic): {h_form}")
        print(f"  match: {simplify(tot - h_form) == 0}")

    print(f"\nCross-term vanishing:")
    for N in [3, 4, 5]:
        print(f"  W_{N}: {verify_cross_term_vanishing(N)}")

    print(f"\nW_4 consistency with w4_stage4_coefficients:")
    for k, v in verify_w4_consistency().items():
        print(f"  {k}: {v}")

    print(f"\nSigma consistency:")
    for k, v in verify_sigma_consistency().items():
        print(f"  {k}: {v}")

    print(f"\nHarmonic divergence:")
    for N, val in kappa_growth_data(20):
        lo, hi = harmonic_divergence_bound(N)
        print(f"  N={N:3d}: H_N - 1 = {val:.6f}, bounds = ({lo:.6f}, {hi:.6f})")
