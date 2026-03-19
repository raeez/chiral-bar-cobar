"""Prefundamental Clebsch-Gordan decomposition for Y(sl_3) (type A_2).

FRONTIER COMPUTATION for MC3 extension beyond type A_1.

For Y(sl_3), there are two prefundamental representations L^-_1, L^-_2
(one per node of the Dynkin diagram). Finite-dimensional irreps are
V_{(a,b)} labeled by dominant weights (a,b) = a*omega_1 + b*omega_2.

The key question: does V_{lambda} tensor L^-_i decompose as a
non-negative integer combination of shifted L^-_j at the character level?

MATHEMATICAL SETUP (Hernandez-Jimbo 2012):

For sl_3, the positive roots are alpha_1, alpha_2, alpha_1+alpha_2.
The prefundamental L^-_i has weight multiplicities controlled by a
restricted Kostant partition function.

ch(L^-_1) has weights in the negative span of {alpha_1, alpha_1+alpha_2},
i.e. the positive roots whose support contains alpha_1.
Weight -(a*alpha_1 + b*(alpha_1+alpha_2)) has multiplicity equal to
the number of 2D partitions: ways to write (a,b) as sum of (n,0) and
(0,m) with n,m >= 1. This equals the bivariate partition function.

More precisely:
  ch(L^-_1) = prod_{n>=1} 1/((1 - e^{-n*alpha_1})(1 - e^{-n*(alpha_1+alpha_2)}))

Similarly:
  ch(L^-_2) = prod_{n>=1} 1/((1 - e^{-n*alpha_2})(1 - e^{-n*(alpha_1+alpha_2)}))

ROOT/WEIGHT CONVENTIONS:
  We work in the fundamental weight basis: weight = (w1, w2) means
  w1*omega_1 + w2*omega_2.

  alpha_1 = 2*omega_1 - omega_2
  alpha_2 = -omega_1 + 2*omega_2
  alpha_1 + alpha_2 = omega_1 + omega_2

  The Weyl dimension formula:
  dim V_{(a,b)} = (a+1)(b+1)(a+b+2)/2

References:
  - Hernandez-Jimbo, Asymptotic representations and Drinfeld rational
    fractions (2012), Section 5 (higher rank)
  - Frenkel-Mukhin, Combinatorics of q-characters (2001)
  - concordance.tex, conj:mc3-arbitrary-type
"""

from __future__ import annotations

from typing import Dict, List, Tuple
from functools import lru_cache

from compute.lib.utils import partition_number


# ---------------------------------------------------------------------------
# Type definitions
# ---------------------------------------------------------------------------

# Weight in fundamental weight basis: (w1, w2) = w1*omega_1 + w2*omega_2
Weight = Tuple[int, int]

# Formal character: weight -> multiplicity
FormalCharSl3 = Dict[Weight, int]


# ---------------------------------------------------------------------------
# Root system data for sl_3
# ---------------------------------------------------------------------------

# Simple roots in omega basis
ALPHA1 = (2, -1)   # alpha_1 = 2*omega_1 - omega_2
ALPHA2 = (-1, 2)   # alpha_2 = -omega_1 + 2*omega_2
ALPHA12 = (1, 1)   # alpha_1 + alpha_2 = omega_1 + omega_2

POSITIVE_ROOTS = [ALPHA1, ALPHA2, ALPHA12]

# Roots whose support contains alpha_1: {alpha_1, alpha_1+alpha_2}
ROOTS_CONTAINING_ALPHA1 = [ALPHA1, ALPHA12]
# Roots whose support contains alpha_2: {alpha_2, alpha_1+alpha_2}
ROOTS_CONTAINING_ALPHA2 = [ALPHA2, ALPHA12]


def add_weights(w1: Weight, w2: Weight) -> Weight:
    return (w1[0] + w2[0], w1[1] + w2[1])


def scale_weight(n: int, w: Weight) -> Weight:
    return (n * w[0], n * w[1])


def neg_weight(w: Weight) -> Weight:
    return (-w[0], -w[1])


# ---------------------------------------------------------------------------
# Weyl dimension formula for sl_3
# ---------------------------------------------------------------------------

def weyl_dim_sl3(a: int, b: int) -> int:
    """Dimension of V_{(a,b)} for sl_3.

    dim V_{(a,b)} = (a+1)(b+1)(a+b+2)/2.
    """
    if a < 0 or b < 0:
        return 0
    return (a + 1) * (b + 1) * (a + b + 2) // 2


# ---------------------------------------------------------------------------
# Weight multiplicities for sl_3 irreps (Freudenthal/Weyl character formula)
# ---------------------------------------------------------------------------

@lru_cache(maxsize=None)
def _kostant_partition_sl3(c1: int, c2: int) -> int:
    """Kostant partition function for sl_3.

    K(c1*alpha_1 + c2*alpha_2) = number of ways to write
    c1*alpha_1 + c2*alpha_2 as a non-negative integer combination
    of positive roots {alpha_1, alpha_2, alpha_1+alpha_2}.

    Equivalently: number of (a, b, c) with a, b, c >= 0 such that
    a + c = c1 and b + c = c2, i.e. c = c1 + c2 - a - b ... no.

    More carefully: a*alpha_1 + b*alpha_2 + c*(alpha_1+alpha_2)
    = (a+c)*alpha_1 + (b+c)*alpha_2. So we need a+c = c1, b+c = c2,
    a,b,c >= 0. This gives c <= min(c1, c2), a = c1-c, b = c2-c.
    So K(c1, c2) = min(c1, c2) + 1 for c1, c2 >= 0.
    """
    if c1 < 0 or c2 < 0:
        return 0
    return min(c1, c2) + 1


def sl3_weight_multiplicity(hw: Weight, mu: Weight) -> int:
    """Weight multiplicity of mu in V_{hw} for sl_3.

    Uses the Weyl character formula / Freudenthal recursion.
    For sl_3, there is a direct formula via the Kostant multiplicity formula:

    mult(mu) = sum_{w in W} (-1)^{l(w)} K(w(hw + rho) - (mu + rho))

    where W = S_3 (Weyl group), rho = omega_1 + omega_2 = (1,1),
    K is the Kostant partition function.

    The Weyl group W = S_3 acts on weights by permuting the coordinates
    in the epsilon basis. In the omega basis:
      e: (a,b) -> (a,b)
      s1: (a,b) -> (-a, a+b)
      s2: (a,b) -> (a+b, -b)
      s1s2: (a,b) -> (-a-b, a)
      s2s1: (a,b) -> (b, -a-b)
      s1s2s1: (a,b) -> (-b, -a)
    """
    a, b = hw
    if a < 0 or b < 0:
        return 0

    rho = (1, 1)
    lam_rho = (a + 1, b + 1)  # hw + rho

    # Weyl group elements with signs and action on omega-basis
    # w(c, d) for each w in S_3:
    weyl_actions = [
        (+1, lambda c, d: (c, d)),           # e
        (-1, lambda c, d: (-c, c + d)),       # s1
        (-1, lambda c, d: (c + d, -d)),       # s2
        (+1, lambda c, d: (-c - d, c)),       # s1 s2
        (+1, lambda c, d: (d, -c - d)),       # s2 s1
        (-1, lambda c, d: (-d, -c)),          # w0 = s1 s2 s1
    ]

    total = 0
    for sign, action in weyl_actions:
        w_lam_rho = action(*lam_rho)
        # Need to express w(lam+rho) - (mu+rho) in the alpha basis
        # If delta = (d1, d2) in omega basis, then in alpha basis:
        # delta = d1*omega_1 + d2*omega_2
        # alpha_1 = 2*omega_1 - omega_2, alpha_2 = -omega_1 + 2*omega_2
        # Inverse: omega_1 = (2*alpha_1 + alpha_2)/3, omega_2 = (alpha_1 + 2*alpha_2)/3
        # So delta in alpha basis: c1 = (2*d1 + d2)/3, c2 = (d1 + 2*d2)/3
        diff = (w_lam_rho[0] - mu[0] - 1, w_lam_rho[1] - mu[1] - 1)
        # Convert to alpha basis
        c1_num = 2 * diff[0] + diff[1]
        c2_num = diff[0] + 2 * diff[1]
        if c1_num % 3 != 0 or c2_num % 3 != 0:
            continue
        c1 = c1_num // 3
        c2 = c2_num // 3
        total += sign * _kostant_partition_sl3(c1, c2)

    return total


def sl3_irrep_character(hw: Weight, depth: int = 10) -> FormalCharSl3:
    """Character of the irreducible sl_3 representation V_{hw}.

    Computes weight multiplicities for all weights mu = hw - sum of positive roots
    up to the given depth (sum of root coefficients).

    Args:
        hw: highest weight (a, b) in omega basis.
        depth: maximum depth (sum of alpha coefficients subtracted).

    Returns:
        Character as dict: weight -> multiplicity.
    """
    a, b = hw
    if a < 0 or b < 0:
        return {}

    char: FormalCharSl3 = {}
    # Enumerate weights: mu = hw - c1*alpha_1 - c2*alpha_2 for c1, c2 >= 0
    for c1 in range(depth + 1):
        for c2 in range(depth + 1 - c1):
            mu = (a - 2 * c1 + c2, b + c1 - 2 * c2)
            mult = sl3_weight_multiplicity(hw, mu)
            if mult > 0:
                char[mu] = mult
    return char


# ---------------------------------------------------------------------------
# Prefundamental characters for Y(sl_3)
# ---------------------------------------------------------------------------

@lru_cache(maxsize=None)
def _bipartition_count(a: int, b: int) -> int:
    """Number of ways to write (a, b) as a sum of pairs from
    {(n, 0) : n >= 1} union {(0, m) : m >= 1}.

    This is the 2D partition function: number of ways to write
    a as a sum of positive integers AND b as a sum of positive integers,
    independently. So this equals p(a) * p(b).

    Wait -- that's for INDEPENDENT partitions. But here we have a single
    multiset of pairs. Let me reconsider.

    For L^-_1, the generating function is:
    prod_{n>=1} 1/((1 - x^n)(1 - y^n))

    where x = e^{-alpha_1} and y = e^{-(alpha_1+alpha_2)}.

    The coefficient of x^a * y^b in this product is p(a) * p(b)
    because the product factors into two independent Euler products.

    So mult of weight -(a*alpha_1 + b*(alpha_1+alpha_2)) = p(a) * p(b).
    """
    if a < 0 or b < 0:
        return 0
    return partition_number(a) * partition_number(b)


def prefundamental_character_sl3_1(depth: int = 15) -> FormalCharSl3:
    """Character of L^-_1 for Y(sl_3).

    L^-_1 has weights -(a*alpha_1 + b*(alpha_1+alpha_2)) for a, b >= 0.
    Multiplicity = p(a) * p(b).

    In omega basis: -(a*alpha_1 + b*(alpha_1+alpha_2))
    = -(2a+b)*omega_1 + (a-b)*omega_2
    = (-2a-b, a-b)

    Args:
        depth: maximum value of a+b to compute.
    """
    char: FormalCharSl3 = {}
    for a in range(depth + 1):
        for b in range(depth + 1 - a):
            mult = partition_number(a) * partition_number(b)
            if mult > 0:
                w = (-2 * a - b, a - b)
                char[w] = char.get(w, 0) + mult
    return char


def prefundamental_character_sl3_2(depth: int = 15) -> FormalCharSl3:
    """Character of L^-_2 for Y(sl_3).

    L^-_2 has weights -(a*alpha_2 + b*(alpha_1+alpha_2)) for a, b >= 0.
    Multiplicity = p(a) * p(b).

    In omega basis: -(a*alpha_2 + b*(alpha_1+alpha_2))
    = (a-b)*omega_1 + (-2a-b)*omega_2
    = (a-b, -2a-b)
    """
    char: FormalCharSl3 = {}
    for a in range(depth + 1):
        for b in range(depth + 1 - a):
            mult = partition_number(a) * partition_number(b)
            if mult > 0:
                w = (a - b, -2 * a - b)
                char[w] = char.get(w, 0) + mult
    return char


# ---------------------------------------------------------------------------
# Character operations
# ---------------------------------------------------------------------------

def tensor_product_sl3(chi1: FormalCharSl3, chi2: FormalCharSl3) -> FormalCharSl3:
    """Tensor product of two sl_3 characters."""
    result: FormalCharSl3 = {}
    for w1, m1 in chi1.items():
        for w2, m2 in chi2.items():
            w = add_weights(w1, w2)
            result[w] = result.get(w, 0) + m1 * m2
    return result


def sum_characters_sl3(*chars: FormalCharSl3) -> FormalCharSl3:
    """Direct sum of sl_3 characters."""
    result: FormalCharSl3 = {}
    for chi in chars:
        for w, m in chi.items():
            result[w] = result.get(w, 0) + m
    return result


def subtract_characters_sl3(chi1: FormalCharSl3, chi2: FormalCharSl3) -> FormalCharSl3:
    """Subtract chi2 from chi1."""
    result = dict(chi1)
    for w, m in chi2.items():
        result[w] = result.get(w, 0) - m
    return {w: m for w, m in result.items() if m != 0}


def shift_character_sl3(chi: FormalCharSl3, shift: Weight) -> FormalCharSl3:
    """Shift all weights by the given vector."""
    return {add_weights(w, shift): m for w, m in chi.items()}


# ---------------------------------------------------------------------------
# CG decomposition tests
# ---------------------------------------------------------------------------

def cg_test_sl3(hw_V: Weight, i: int, depth: int = 12) -> Dict:
    """Test the CG decomposition V_{hw_V} tensor L^-_i for Y(sl_3).

    Computes the tensor product character and checks whether it can be
    decomposed as a non-negative integer combination of shifted
    prefundamental characters L^-_j(shift).

    The sl_2 pattern (V_n tensor L^- = sum of shifted L^-) suggests
    that for sl_3:
      V_{(a,b)} tensor L^-_i = sum_{j, shifts} c_j(shift) * L^-_j(shift)

    where c_j >= 0 are non-negative integer multiplicities.

    We check this by computing the tensor product and attempting to
    subtract off shifted prefundamentals.

    Args:
        hw_V: highest weight of the finite-dim rep.
        i: which prefundamental (1 or 2).
        depth: truncation depth.

    Returns:
        dict with decomposition data.
    """
    V_char = sl3_irrep_character(hw_V, depth=depth + sum(hw_V))
    if i == 1:
        L_char = prefundamental_character_sl3_1(depth=depth)
    else:
        L_char = prefundamental_character_sl3_2(depth=depth)

    tensor = tensor_product_sl3(V_char, L_char)

    # The tensor product has highest weight hw_V + 0 = hw_V with
    # mult = mult_V(hw_V) * mult_L(0) = 1.
    # This top weight should come from a single shifted L^-_?.

    # Strategy: greedy decomposition. Find the highest weight in the
    # tensor product, identify which L^-_j it belongs to, subtract,
    # repeat.
    remainder = dict(tensor)
    summands = []
    max_iterations = 200

    for _ in range(max_iterations):
        if not remainder or all(m == 0 for m in remainder.values()):
            break
        # Clean zeros
        remainder = {w: m for w, m in remainder.items() if m != 0}
        if not remainder:
            break

        # Find "highest" weight (lexicographically largest)
        top = max(remainder.keys(), key=lambda w: (w[0] + w[1], w[0]))
        top_mult = remainder[top]

        if top_mult <= 0:
            break  # Cannot decompose further with positive coefficients

        # Determine which L^-_j(shift) has this as its highest weight.
        # L^-_j has highest weight (0,0). So L^-_j(shift=s) has
        # highest weight s. The shift is s = top.
        # But which j? Both L^-_1 and L^-_2 have hw (0,0).
        # The weight structure differs: L^-_1 has weights going in the
        # -alpha_1, -(alpha_1+alpha_2) directions, while L^-_2 goes in
        # -alpha_2, -(alpha_1+alpha_2) directions.

        # Try both j=1 and j=2. Accept whichever produces non-negative remainder.
        best_j = None
        best_shifted = None

        for j in [1, 2]:
            if j == 1:
                L_j = prefundamental_character_sl3_1(depth=depth)
            else:
                L_j = prefundamental_character_sl3_2(depth=depth)
            shifted = shift_character_sl3(L_j, top)

            # Check if subtracting top_mult copies leaves non-negative remainder
            # (at least at the weights we can check)
            test_rem = dict(remainder)
            ok = True
            for w, m in shifted.items():
                test_rem[w] = test_rem.get(w, 0) - top_mult * m
                if test_rem[w] < 0:
                    # Check if this weight is in the reliable range
                    # (not too deep where truncation artifacts occur)
                    dist = abs(w[0] - top[0]) + abs(w[1] - top[1])
                    if dist < 2 * (depth - 3):
                        ok = False
                        break
            if ok:
                best_j = j
                best_shifted = shifted
                break

        if best_j is None:
            # Neither j works -- decomposition fails or needs mixed type
            summands.append({
                "type": "RESIDUAL",
                "top_weight": top,
                "multiplicity": top_mult,
                "note": "Cannot subtract any shifted L^-_j",
            })
            break

        # Subtract
        for w, m in best_shifted.items():
            remainder[w] = remainder.get(w, 0) - top_mult * m

        summands.append({
            "type": f"L^-_{best_j}",
            "shift": top,
            "multiplicity": top_mult,
        })

    # Check if remainder is zero (within truncation range)
    remainder_clean = {w: m for w, m in remainder.items() if m != 0}
    # Only check weights not too deep
    in_range_nonzero = {}
    for w, m in remainder_clean.items():
        dist_from_hw = abs(hw_V[0] - w[0]) + abs(hw_V[1] - w[1])
        if dist_from_hw < 2 * (depth - 5) and m != 0:
            in_range_nonzero[w] = m

    decomposition_exact = len(in_range_nonzero) == 0
    all_positive_remainder = all(m >= 0 for m in in_range_nonzero.values())
    any_negative = any(m < 0 for m in in_range_nonzero.values())

    return {
        "hw_V": hw_V,
        "prefundamental_index": i,
        "n_summands": len(summands),
        "summands": summands,
        "decomposition_exact": decomposition_exact,
        "all_positive_remainder": all_positive_remainder,
        "any_negative_remainder": any_negative,
        "in_range_nonzero_remainder": in_range_nonzero,
        "total_tensor_weights": len(tensor),
    }


# ---------------------------------------------------------------------------
# Fundamental CG computations
# ---------------------------------------------------------------------------

def cg_fundamental_V10_L1(depth: int = 12) -> Dict:
    """V_{(1,0)} tensor L^-_1."""
    return cg_test_sl3((1, 0), 1, depth=depth)


def cg_fundamental_V01_L1(depth: int = 12) -> Dict:
    """V_{(0,1)} tensor L^-_1."""
    return cg_test_sl3((0, 1), 1, depth=depth)


def cg_fundamental_V10_L2(depth: int = 12) -> Dict:
    """V_{(1,0)} tensor L^-_2."""
    return cg_test_sl3((1, 0), 2, depth=depth)


def cg_fundamental_V01_L2(depth: int = 12) -> Dict:
    """V_{(0,1)} tensor L^-_2."""
    return cg_test_sl3((0, 1), 2, depth=depth)


def cg_adjoint_V11_L1(depth: int = 12) -> Dict:
    """V_{(1,1)} tensor L^-_1 (adjoint rep)."""
    return cg_test_sl3((1, 1), 1, depth=depth)


def cg_adjoint_V11_L2(depth: int = 12) -> Dict:
    """V_{(1,1)} tensor L^-_2 (adjoint rep)."""
    return cg_test_sl3((1, 1), 2, depth=depth)


# ---------------------------------------------------------------------------
# Direct analytical CG for V_{(1,0)} tensor L^-_1
# ---------------------------------------------------------------------------

def analytical_cg_V10_L1(depth: int = 15) -> Dict:
    """Analytical computation of V_{(1,0)} tensor L^-_1.

    V_{(1,0)} is the standard 3-dim rep with weights:
      (1, 0), (-1, 1), (0, -1)  [in omega basis]

    These correspond to epsilon_1, epsilon_2, epsilon_3 respectively.

    L^-_1 has highest weight (0,0) and weights
    -(a*alpha_1 + b*(alpha_1+alpha_2)) = (-2a-b, a-b) with mult p(a)*p(b).

    The tensor product V_{(1,0)} tensor L^-_1 shifts the L^-_1 character
    by each weight of V_{(1,0)}:

    Shift by (1,0): weights become (1-2a-b, a-b) with mult p(a)*p(b)
    Shift by (-1,1): weights become (-1-2a-b, 1+a-b) with mult p(a)*p(b)
    Shift by (0,-1): weights become (-2a-b, -1+a-b) with mult p(a)*p(b)

    PREDICTION (sl_2 analogy): If the CG decomposition holds, then
    V_{(1,0)} tensor L^-_1 = L^-_1(shift=(1,0)) + L^-_?(shift=(-1,1)) + L^-_?(shift=(0,-1))

    corresponding to the three weights of V_{(1,0)}.

    The top shift (1,0) should produce L^-_1 (since V_{(1,0)} is the
    first fundamental and we're tensoring with L^-_1).
    The second shift (-1,1) = hw_V - alpha_1... this is subtler.
    The third shift (0,-1) = hw_V - alpha_1 - alpha_2.

    By the Hernandez-Jimbo theory, the expected decomposition is:
    [V_{(1,0)}] * [L^-_1] = [L^-_1(shift_1)] + [L^-_2(shift_2)] + [L^-_1(shift_3)]
    or some similar combination of L^-_1 and L^-_2 with appropriate shifts.

    We compute numerically and determine the pattern.
    """
    V10 = sl3_irrep_character((1, 0), depth=depth + 2)
    L1 = prefundamental_character_sl3_1(depth=depth)
    tensor = tensor_product_sl3(V10, L1)

    # Now try to decompose. The highest weight in tensor is (1,0) with mult 1.
    # This must come from L^-_j(shift=(1,0)).
    # Since L^-_j has hw (0,0), shifting by (1,0) gives hw (1,0).

    # Try L^-_1(shift=(1,0)):
    L1_shifted_10 = shift_character_sl3(L1, (1, 0))
    remainder1 = subtract_characters_sl3(tensor, L1_shifted_10)

    # Try L^-_2(shift=(1,0)):
    L2 = prefundamental_character_sl3_2(depth=depth)
    L2_shifted_10 = shift_character_sl3(L2, (1, 0))
    remainder2 = subtract_characters_sl3(tensor, L2_shifted_10)

    # Check which remainder is non-negative
    r1_nonneg = all(m >= 0 for w, m in remainder1.items()
                    if abs(w[0]) + abs(w[1]) < 2 * (depth - 3))
    r2_nonneg = all(m >= 0 for w, m in remainder2.items()
                    if abs(w[0]) + abs(w[1]) < 2 * (depth - 3))

    # Report the top few weights of each remainder
    def top_weights(r, n=10):
        items = sorted(r.items(), key=lambda x: (-x[0][0] - x[0][1], -x[0][0]))
        return items[:n]

    return {
        "tensor_hw": (1, 0),
        "tensor_hw_mult": tensor.get((1, 0), 0),
        "remainder_L1_shift_10_nonneg": r1_nonneg,
        "remainder_L2_shift_10_nonneg": r2_nonneg,
        "remainder_L1_top": top_weights(remainder1),
        "remainder_L2_top": top_weights(remainder2),
        "total_weights_in_tensor": len(tensor),
    }


# ---------------------------------------------------------------------------
# Systematic decomposition verification
# ---------------------------------------------------------------------------

def verify_cg_closes(max_hw_sum: int = 2, depth: int = 12) -> Dict:
    """Check whether the CG decomposition closes for all V_{(a,b)}
    with a + b <= max_hw_sum, tensored with both L^-_1 and L^-_2.

    "Closes" means: the tensor product decomposes as a non-negative
    integer combination of shifted L^-_j characters.
    """
    results = {}
    for a in range(max_hw_sum + 1):
        for b in range(max_hw_sum + 1 - a):
            if a == 0 and b == 0:
                continue  # trivial
            for i in [1, 2]:
                key = f"V_({a},{b}) x L^-_{i}"
                cg = cg_test_sl3((a, b), i, depth=depth)
                results[key] = {
                    "exact": cg["decomposition_exact"],
                    "n_summands": cg["n_summands"],
                    "summands": [(s["type"], s.get("shift"), s.get("multiplicity"))
                                 for s in cg["summands"]],
                    "any_negative": cg["any_negative_remainder"],
                }
    return results


# ---------------------------------------------------------------------------
# Weight multiplicity verification
# ---------------------------------------------------------------------------

def verify_sl3_weight_formula() -> Dict[str, bool]:
    """Verify the weight multiplicity formula against known results."""
    results = {}

    # V_{(1,0)} = standard 3-dim: weights (1,0), (-1,1), (0,-1) each mult 1
    char_10 = sl3_irrep_character((1, 0), depth=5)
    results["V(1,0) dim=3"] = (sum(char_10.values()) == 3)
    results["V(1,0) hw mult=1"] = (char_10.get((1, 0), 0) == 1)
    results["V(1,0) has (-1,1)"] = (char_10.get((-1, 1), 0) == 1)
    results["V(1,0) has (0,-1)"] = (char_10.get((0, -1), 0) == 1)

    # V_{(0,1)} = dual 3-dim: weights (0,1), (1,-1), (-1,0) each mult 1
    char_01 = sl3_irrep_character((0, 1), depth=5)
    results["V(0,1) dim=3"] = (sum(char_01.values()) == 3)
    results["V(0,1) hw mult=1"] = (char_01.get((0, 1), 0) == 1)
    results["V(0,1) has (1,-1)"] = (char_01.get((1, -1), 0) == 1)
    results["V(0,1) has (-1,0)"] = (char_01.get((-1, 0), 0) == 1)

    # V_{(1,1)} = adjoint 8-dim: hw (1,1), dimension 8
    char_11 = sl3_irrep_character((1, 1), depth=5)
    results["V(1,1) dim=8"] = (sum(char_11.values()) == 8)
    results["V(1,1) (0,0) mult=2"] = (char_11.get((0, 0), 0) == 2)

    # V_{(2,0)} = symmetric square of standard, dim 6
    char_20 = sl3_irrep_character((2, 0), depth=5)
    results["V(2,0) dim=6"] = (sum(char_20.values()) == 6)

    # V_{(0,2)} = symmetric square of dual, dim 6
    char_02 = sl3_irrep_character((0, 2), depth=5)
    results["V(0,2) dim=6"] = (sum(char_02.values()) == 6)

    return results


def verify_prefundamental_basic() -> Dict[str, bool]:
    """Basic checks on the prefundamental characters."""
    results = {}

    L1 = prefundamental_character_sl3_1(depth=10)
    L2 = prefundamental_character_sl3_2(depth=10)

    # Both have hw (0,0) with mult 1
    results["L1 hw (0,0) mult=1"] = (L1.get((0, 0), 0) == 1)
    results["L2 hw (0,0) mult=1"] = (L2.get((0, 0), 0) == 1)

    # L1 weight -(alpha_1) = (-2, 1) with mult p(1)*p(0) = 1
    results["L1 at -alpha1 mult=1"] = (L1.get((-2, 1), 0) == 1)

    # L1 weight -(alpha_1+alpha_2) = (-1, -1) with mult p(0)*p(1) = 1
    results["L1 at -(alpha1+alpha2) mult=1"] = (L1.get((-1, -1), 0) == 1)

    # L2 weight -(alpha_2) = (1, -2) with mult p(1)*p(0) = 1
    results["L2 at -alpha2 mult=1"] = (L2.get((1, -2), 0) == 1)

    # L2 weight -(alpha_1+alpha_2) = (-1, -1) with mult p(0)*p(1) = 1
    results["L2 at -(alpha1+alpha2) mult=1"] = (L2.get((-1, -1), 0) == 1)

    # L1 weight -(2*alpha_1 + alpha_1+alpha_2) = -(3*alpha_1+alpha_2+alpha_2)
    # actually: a=2, b=1: weight = (-2*2-1, 2-1) = (-5, 1), mult = p(2)*p(1) = 2
    results["L1 at a=2,b=1 mult=2"] = (L1.get((-5, 1), 0) == 2)

    # L1 total dim at depth 5
    total_L1 = sum(L1.values())
    expected_total = sum(
        partition_number(a) * partition_number(b)
        for a in range(11) for b in range(11 - a)
    )
    results["L1 total consistent"] = (total_L1 == expected_total)

    # Symmetry: L^-_2 is obtained from L^-_1 by swapping omega_1 <-> omega_2
    # i.e., (w1, w2) in L1 <-> (w2, w1) in L2
    l1_swapped = {(w2, w1): m for (w1, w2), m in L1.items()}
    l2_dict = dict(L2)
    swap_match = True
    for w in set(l1_swapped.keys()) | set(l2_dict.keys()):
        if l1_swapped.get(w, 0) != l2_dict.get(w, 0):
            swap_match = False
            break
    results["L1 swap = L2"] = swap_match

    return results


# ---------------------------------------------------------------------------
# Master verification
# ---------------------------------------------------------------------------

def verify_all() -> Dict[str, bool]:
    """Run all verification checks."""
    results = {}
    results.update(verify_sl3_weight_formula())
    results.update(verify_prefundamental_basic())
    return results


if __name__ == "__main__":
    print("=" * 70)
    print("PREFUNDAMENTAL CG FOR Y(sl_3) — MC3 TYPE A_2 FRONTIER")
    print("=" * 70)

    # Basic checks
    print("\n--- Weight formula and prefundamental checks ---")
    basic = verify_all()
    for name, ok in basic.items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    # Analytical CG for V_{(1,0)} tensor L^-_1
    print("\n--- Analytical CG: V_{(1,0)} tensor L^-_1 ---")
    ana = analytical_cg_V10_L1(depth=12)
    print(f"  tensor hw: {ana['tensor_hw']}, mult: {ana['tensor_hw_mult']}")
    print(f"  remainder after L^-_1(1,0) nonneg: {ana['remainder_L1_shift_10_nonneg']}")
    print(f"  remainder after L^-_2(1,0) nonneg: {ana['remainder_L2_shift_10_nonneg']}")
    print(f"  top weights of L1-remainder:")
    for w, m in ana["remainder_L1_top"][:5]:
        print(f"    {w}: {m}")
    print(f"  top weights of L2-remainder:")
    for w, m in ana["remainder_L2_top"][:5]:
        print(f"    {w}: {m}")

    # Systematic CG
    print("\n--- Systematic CG decomposition ---")
    sys_results = verify_cg_closes(max_hw_sum=2, depth=10)
    for key, data in sys_results.items():
        status = "EXACT" if data["exact"] else ("NEG" if data["any_negative"] else "INEXACT")
        summand_str = ", ".join(f"{s[0]}({s[1]})*{s[2]}" for s in data["summands"][:5])
        print(f"  [{status}] {key}: {data['n_summands']} summands: {summand_str}")

    # Summary
    n_pass = sum(1 for v in basic.values() if v)
    n_fail = sum(1 for v in basic.values() if not v)
    print(f"\n{n_pass} basic checks passed, {n_fail} failed.")

    n_exact = sum(1 for d in sys_results.values() if d["exact"])
    n_total = len(sys_results)
    print(f"{n_exact}/{n_total} CG decompositions are exact.")
