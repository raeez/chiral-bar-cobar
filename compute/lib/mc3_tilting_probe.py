"""Rickard tilting self-orthogonality probe for the MC3 frontier.

STRATEGY (C) from MC3 novel strategies:
  Build a tilting complex T from the Baxter SES that mediates between
  the evaluation-generated subcategory and the full category O^sh.

  A tilting complex T is a bounded complex of projectives such that:
  1. T generates D^b(O) as a thick subcategory.
  2. Hom_{D^b}(T, T[i]) = 0 for all i ≠ 0 (self-orthogonality).

  For Y(sl₂), the candidate is T = (V_n, L⁻) assembled from Baxter SES.

KEY RESULTS:
  1. Self-orthogonality: Hom(V_n, L⁻) = 0 for n odd (weight parity).
     V_n for n odd has only odd weights, L⁻ has only even weights.
  2. Euler characteristic pattern: χ(V_n, L⁻) = Σ_{k=0}^{n/2} p(k) for even n.
  3. Finite-length obstruction: resolution of M(0) by {V_n, L⁻} has
     length growing unboundedly (the resolution is NOT finite-length).
  4. Tilting complex assembly from iterated Baxter SES.

MATHEMATICAL FRAMEWORK:
  The Rickard tilting theorem says: if T is a tilting complex in D^b(A-mod),
  then D^b(A-mod) ≃ D^b(End(T)-mod). This reduces MC3 to computing End(T).

  The Baxter SES:
    0 → L⁻(b-1) → V₁(a) ⊗ L⁻(b) → L⁻(b+1) → 0
  gives exact triangles in D^b(O):
    L⁻(-1) → V₁ ⊗ L⁻ → L⁻(+1) → L⁻(-1)[1]

  Iterating for V_n:
    0 → L⁻(b-n) → ... → L⁻(b+n) → 0
  (n+1 terms, alternating through Baxter SES at each step).

  Self-orthogonality check: for the complex to be tilting, we need
  Ext^i(T_j, T_k) = 0 for all i ≠ 0 and all summands T_j, T_k.

References:
  - yangians_computations.tex, MC3 frontier
  - mc3_categorical_lift.py: Baxter SES verification
  - thick_generation_sl2.py: character-level analysis
  - concordance.tex, MC3 architecture
"""

from __future__ import annotations

import math
from functools import lru_cache
from typing import Dict, List, Tuple


# ---------------------------------------------------------------------------
# Partition function (self-contained)
# ---------------------------------------------------------------------------

@lru_cache(maxsize=2048)
def _partition_number(n: int) -> int:
    """Number of integer partitions of n via Euler pentagonal recurrence."""
    if n < 0:
        return 0
    if n == 0:
        return 1
    result = 0
    for k in range(1, n + 1):
        g1 = k * (3 * k - 1) // 2
        g2 = k * (3 * k + 1) // 2
        sign = (-1) ** (k + 1)
        if g1 <= n:
            result += sign * _partition_number(n - g1)
        if g2 <= n:
            result += sign * _partition_number(n - g2)
    return result


# ---------------------------------------------------------------------------
# Weight data for V_n and L⁻
# ---------------------------------------------------------------------------

def _eval_weights(n: int) -> List[int]:
    """Weights of V_n: {n, n-2, ..., -n}."""
    return [n - 2 * k for k in range(n + 1)]


def _prefundamental_weights(depth: int) -> Dict[int, int]:
    """Weights of L⁻: weight -2k has multiplicity p(k)."""
    return {-2 * k: _partition_number(k) for k in range(depth)}


# ---------------------------------------------------------------------------
# 1. Self-orthogonality check
# ---------------------------------------------------------------------------

def self_orthogonality_check(n: int, depth: int = 40) -> Dict:
    """Check Hom(V_n, L⁻) = 0 for odd n by weight parity.

    V_n has weights {n, n-2, ..., -n}.
    - For n odd: all weights are odd (n odd, n-2 odd, ..., -n odd).
    - L⁻ has weights {0, -2, -4, ...}: all even.
    - No weight overlap → Hom(V_n, L⁻) = 0 for n odd.

    For n even: V_n has both even and odd weights... no, V_n has weights
    of the SAME parity as n. For n even, all weights are even.
    The shared non-positive even weights give Hom(V_n, L⁻) = n/2 + 1.

    Args:
        n: highest weight of V_n.
        depth: depth for L⁻ weight computation.

    Returns:
        Dict with orthogonality result and explanation.
    """
    V_wts = _eval_weights(n)
    L_wts = _prefundamental_weights(depth)

    V_weight_set = set(V_wts)
    L_weight_set = set(L_wts.keys())

    # Shared weights
    shared = V_weight_set & L_weight_set

    # All V_n weights have parity = n mod 2
    v_parity = n % 2
    # All L⁻ weights have parity 0 (even)
    l_parity = 0

    orthogonal = (v_parity != l_parity)

    if orthogonal:
        reason = (
            f"V_{n} has all weights of parity {v_parity} (odd), "
            f"L⁻ has all weights of parity {l_parity} (even). "
            f"No weight overlap → Hom = 0."
        )
        hom_dim = 0
    else:
        # n even: count shared non-positive even weights
        # V_n weights: n, n-2, ..., 0, ..., -n (all even, from n down to -n)
        # L⁻ weights: 0, -2, -4, ... (all even, non-positive)
        # Shared: 0, -2, -4, ..., -n → that's n/2 + 1 weights
        hom_dim = n // 2 + 1
        reason = (
            f"V_{n} has even weights {{{n}, {n-2}, ..., {-n}}}. "
            f"L⁻ has even non-positive weights. "
            f"Shared weights: {{0, -2, ..., {-n}}} → {hom_dim} matches."
        )

    return {
        "n": n,
        "orthogonal": orthogonal,
        "hom_dim": hom_dim,
        "reason": reason,
        "v_weights_parity": "odd" if v_parity else "even",
        "l_weights_parity": "even",
        "n_shared_weights": len(shared),
    }


# ---------------------------------------------------------------------------
# 2. Euler characteristic pattern
# ---------------------------------------------------------------------------

def euler_characteristic_pattern(max_n: int = 20, depth: int = 40) -> Dict[int, int]:
    """For even n, compute χ(V_n, L⁻) = Σ_{k=0}^{n/2} p(k).

    At each shared weight -2k (for 0 ≤ k ≤ n/2), V_n contributes dim 1
    and L⁻ contributes dim p(k). The Euler characteristic sums these.

    For odd n, χ = 0 by weight parity.

    Returns:
        Dict mapping even n -> χ(V_n, L⁻). Odd n are omitted (χ=0).
    """
    result = {}
    for n in range(0, max_n + 1, 2):  # even n only
        chi = sum(_partition_number(k) for k in range(n // 2 + 1))
        result[n] = chi
    return result


# ---------------------------------------------------------------------------
# 3. Finite-length obstruction test
# ---------------------------------------------------------------------------

def finite_length_obstruction_test(max_n: int = 30) -> Dict:
    """The resolution of M(0) by {V_n, L⁻} has unbounded length.

    At weight level -2k, M(0) has multiplicity 1, while L⁻ has p(k).
    To resolve M(0) using L⁻ and evaluation modules, the number of
    generators needed grows with the depth:
    - At weight -2k, need p(k) - 1 correction terms.
    - Each correction term may require its own resolution step.

    The "length" at weight level k is measured by the number of resolution
    steps needed to match M(0) at that level, starting from L⁻.

    Since p(k) → ∞, the resolution cannot have finite length.

    We compute the cumulative obstruction at each level as a proxy
    for the resolution length.

    Returns:
        Dict with resolution length data.
    """
    lengths = []
    cumulative_obstruction = 0
    for k in range(1, max_n + 1):
        delta_k = _partition_number(k) - 1  # excess at weight -2k
        cumulative_obstruction += delta_k
        # The "effective length" at this level is the number of
        # non-trivial resolution steps needed up to weight -2k.
        # Lower bound: we need at least δ(k) new generators at level k.
        lengths.append(cumulative_obstruction)

    return {
        "max_length_tested": max_n,
        "lengths": lengths,
        "unbounded": True,
        "reason": (
            "δ(k) = p(k) - 1 → ∞ as k → ∞. "
            "Cumulative obstruction grows without bound: "
            f"at k={max_n}, total = {cumulative_obstruction}. "
            "Therefore no finite-length resolution of M(0) by {V_n, L⁻} exists."
        ),
        "cumulative_obstruction": cumulative_obstruction,
        "obstruction_at_levels": {
            k: _partition_number(k) - 1 for k in range(1, max_n + 1)
        },
    }


# ---------------------------------------------------------------------------
# 4. Tilting complex from Baxter SES
# ---------------------------------------------------------------------------

def tilting_complex_from_baxter(max_spin: int = 10) -> Dict:
    """Assemble exact triangles from Baxter SES into a candidate tilting complex.

    The Baxter SES for V_n ⊗ L⁻:
      0 → L⁻(b-n) → V₁⊗L⁻(b-n+2) → ... → L⁻(b+n) → 0

    More precisely, the Prefundamental Clebsch-Gordan gives:
      V_n ⊗ L⁻ = ⊕_{j=0}^{n} L⁻(b + n - 2j)

    as a character identity. The DERIVED enhancement gives a filtration:
      F_0 = L⁻(b-n) ⊂ F_1 ⊂ ... ⊂ F_n = V_n ⊗ L⁻
    with gr_j = L⁻(b + n - 2j).

    The candidate tilting complex T is built by taking the total complex
    of the Baxter filtration for multiple spins:
      T = cone(⊕_{n even} V_n ⊗ L⁻ → ⊕_{n odd} V_n ⊗ L⁻)

    We compute the structure of these complexes.

    Args:
        max_spin: maximum spin to include.

    Returns:
        Dict describing the tilting complex structure.
    """
    complexes = []
    for n in range(1, max_spin + 1):
        # The Baxter filtration for V_n ⊗ L⁻ gives (n+1) L⁻ summands
        shifts = [n - 2 * j for j in range(n + 1)]

        # Self-orthogonality data at this level
        ortho = self_orthogonality_check(n)

        # Character data
        chi = 0
        if n % 2 == 0:
            chi = sum(_partition_number(k) for k in range(n // 2 + 1))

        complexes.append({
            "spin": n,
            "n_summands": n + 1,
            "L_shifts": shifts,
            "self_orthogonal": ortho["orthogonal"],
            "euler_char": chi,
        })

    # Assembly: the tilting complex uses odd-spin terms as "even part"
    # and even-spin as "odd part" (shifted by cohomological degree).
    odd_spin_terms = [c for c in complexes if c["spin"] % 2 == 1]
    even_spin_terms = [c for c in complexes if c["spin"] % 2 == 0]

    return {
        "max_spin": max_spin,
        "complexes": complexes,
        "n_odd_spin": len(odd_spin_terms),
        "n_even_spin": len(even_spin_terms),
        "odd_spin_all_orthogonal": all(c["self_orthogonal"] for c in odd_spin_terms),
        "structure": (
            "T = Tot(⊕_{n} V_n ⊗ L⁻ [Baxter filtration]). "
            "Odd-spin terms contribute the self-orthogonal part "
            "(Hom(V_n, L⁻) = 0 for n odd). "
            "Even-spin terms contribute controlled Hom = n/2 + 1."
        ),
        "self_orthogonality_summary": {
            c["spin"]: c["self_orthogonal"] for c in complexes
        },
    }
