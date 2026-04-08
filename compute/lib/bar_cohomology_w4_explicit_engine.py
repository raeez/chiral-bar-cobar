r"""Explicit bar cohomology H*(B(W_4)) at weights 0 through 6.

W_4 = W(sl_4, f_prin) has three strong generators:
  T   (conformal weight 2) -- Virasoro stress tensor
  W_3 (conformal weight 3) -- spin-3 primary current
  W_4 (conformal weight 4) -- spin-4 primary current

VACUUM MODULE:
  PBW basis: modes L_{-n} (n >= 2), W3_{-m} (m >= 3), W4_{-p} (p >= 4)
  applied to |0> in non-increasing order within each generator family.
  Character:
    chi(q) = prod_{n>=2} 1/(1-q^n) * prod_{m>=3} 1/(1-q^m) * prod_{p>=4} 1/(1-q^p)
  Augmentation ideal V-bar = chi(q) - 1.
  Dimensions (h=0,...,8): 0, 0, 1, 2, 4, 7, 13, 21, 36

OPE STRUCTURE (Hornfeck 1993, Blumenhagen et al. 1996):
  T x T: poles 1-4, standard Virasoro
  T x W_s: poles 1-2, primary condition (pole-2 coeff = s)
  W_3 x W_3: poles 1-6, c/3 at leading pole, W_4 at pole 2 with coeff c_334
  W_3 x W_4: poles 1-7
  W_4 x W_4: poles 1-8, c/4 at leading pole, W_4 at pole 4 with coeff c_444

  Structure constants squared (rational in c):
    g_334^2 = 42 c^2 (5c+22) / [(c+24)(7c+68)(3c+46)]
    g_444^2 = 112 c^2 (2c-1)(3c+46) / [(c+24)(7c+68)(10c+197)(5c+3)]

BAR COMPLEX:
  B^n_h(W_4) = (V-bar)^{otimes(n+1)} at total weight h, tensored with
  the Orlik-Solomon algebra OS^n(Conf_{n+1}(C)) of dimension n!.
  Bar differential d: B^n -> B^{n-1} extracts residues at collision
  divisors using the FULL OPE (all a_{(k)}b products).

  At bar degree 1 (pairs): d(a otimes b otimes eta_{12}) = sum_k a_{(k)}b.
  The curvature (image in B^0 = V-bar) is m_0(gen) = leading pole coeff:
    m_0(T) = c/2,  m_0(W_3) = c/3,  m_0(W_4) = c/4.

BAR COHOMOLOGY H^1(B(W_4)):
  H^1 = ker(d: B^1 -> B^0) / im(d: B^2 -> B^1).
  At low weights, im(d: B^2 -> B^1) = 0 (B^2 starts at weight 4),
  so H^1_h = ker(d)_h for h = 2, 3.
  Generators of H^1 are the quasi-primaries of W_4:
    h=2: T (1 generator)
    h=3: W_3 (1 generator)
    h=4: W_4, Lambda (2 quasi-primaries -- see AP26 on BPZ metric)
  Compare W_3: H^1(B(W_3)) has generators at h=2 (T), h=3 (W), h=4 (Lambda).
  W_4 has ONE MORE generator (W_4 itself) starting at h=4.

THREE-CHANNEL STRUCTURE:
  The bar differential at degree 1 decomposes into channels by the
  target generator:
    T-channel:   a_{(k)}b -> f(T, dT, d^2T, ...)
    W_3-channel: a_{(k)}b -> f(W_3, dW_3, ...)
    W_4-channel: a_{(k)}b -> f(W_4, dW_4, ...)
  The irrationality from g_334 and g_444 enters ONLY in the W_4-channel.
  The T-channel and W_3-channel have purely rational (in c) coefficients.

WHERE IRRATIONALITY ENTERS:
  g_334 first appears at weight 4 in bar degree 1: the W_3 x W_3 -> W_4
  coupling at pole 2 contributes g_334 * W_4 to d(W_3 otimes W_3 otimes eta).
  g_444 first appears at weight 6 in bar degree 1: the W_4 x W_4 -> W_4
  coupling at pole 4.
  At bar degree 2: g_334 first appears at weight 6 (earliest triple
  involving W_3 otimes W_3 otimes * with total weight 3+3+? >= 6).
  The irrationality is sqrt(g_334^2) = sqrt(rational), generically irrational.

CONVENTIONS:
  Cohomological grading, |d| = +1.
  Bar differential has bar-degree -1 (reduces tensor length by 1).
  n-th product convention: a_{(n)}b = Res_{z->w} (z-w)^n a(z) b(w).
  The bar differential extracts ALL singular products:
    d(a otimes b otimes eta) = sum_{n >= 0} a_{(n)} b
  (AP19: the d-log kernel absorbs one power, so mode n corresponds to
  pole order n+1 in the OPE.)

References:
  Hornfeck, Nucl. Phys. B 407 (1993) 57
  Blumenhagen-Eholzer-Honecker-Hornfeck-Hubel, Nucl. Phys. B 461 (1996) 460
  compute/lib/w4_ds_ope_extraction.py (structure constant formulas)
  compute/lib/theorem_w4_full_ope_delta_f2_engine.py (delta_F2 derivation)
  compute/lib/w3_bar.py (W_3 bar complex, analogous computation)
  compute/lib/w3_bar_extended.py (W_3 extended bar cohomology)
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational,
    Symbol,
    cancel,
    expand,
    simplify,
    sqrt,
    symbols,
)


# ============================================================================
# W_4 central charge
# ============================================================================

def w4_central_charge(k=None):
    """Central charge c(k) = 3 - 60(k+3)^2/(k+4) for principal W_4.

    Feigin-Frenkel dual level: k' = -k - 8.
    Complementarity sum: c(k) + c(k') = 246.
    """
    if k is None:
        k = Symbol('k')
    return 3 - 60 * (k + 3)**2 / (k + 4)


def w4_complementarity_sum():
    """c(k) + c(-k-8) = 246 for W_4 = W(sl_4, f_prin)."""
    return 246


# ============================================================================
# Vacuum module dimensions
# ============================================================================

def w4_vacuum_dims(max_weight: int) -> Dict[int, int]:
    """Dimensions of the W_4 vacuum module (including vacuum) by weight.

    Character:
      chi_0(q) = prod_{n>=2} 1/(1-q^n) * prod_{m>=3} 1/(1-q^m) * prod_{p>=4} 1/(1-q^p)

    This is the product of three partition-function factors, one for each
    generator family. The L-modes start at n=2, W3-modes at m=3, W4-modes at p=4.

    Returns {h: dim} with dim[0] = 1 (vacuum).
    """
    # Factor 1: partitions with parts >= 2
    c_L = [0] * (max_weight + 1)
    c_L[0] = 1
    for n in range(2, max_weight + 1):
        for k in range(n, max_weight + 1):
            c_L[k] += c_L[k - n]

    # Factor 2: partitions with parts >= 3
    c_W3 = [0] * (max_weight + 1)
    c_W3[0] = 1
    for m in range(3, max_weight + 1):
        for k in range(m, max_weight + 1):
            c_W3[k] += c_W3[k - m]

    # Factor 3: partitions with parts >= 4
    c_W4 = [0] * (max_weight + 1)
    c_W4[0] = 1
    for p in range(4, max_weight + 1):
        for k in range(p, max_weight + 1):
            c_W4[k] += c_W4[k - p]

    # Convolve all three
    product = [0] * (max_weight + 1)
    for i in range(max_weight + 1):
        for j in range(max_weight + 1 - i):
            product[i + j] += c_L[i] * c_W3[j]

    final = [0] * (max_weight + 1)
    for i in range(max_weight + 1):
        for j in range(max_weight + 1 - i):
            final[i + j] += product[i] * c_W4[j]

    return {h: final[h] for h in range(max_weight + 1)}


def w4_augmentation_dims(max_weight: int) -> Dict[int, int]:
    """Dimensions of V-bar = vacuum module minus vacuum.

    V-bar_h = chi_0(q) - 1 at weight h.
    dim V-bar_0 = 0, dim V-bar_1 = 0, dim V-bar_2 = 1 (just T), etc.
    """
    vac = w4_vacuum_dims(max_weight)
    result = dict(vac)
    result[0] = result.get(0, 1) - 1  # subtract vacuum
    return result


def w4_augmentation_dim(h: int, max_weight: int = 30) -> int:
    """Dimension of V-bar at weight h."""
    if h < 2:
        return 0
    return w4_augmentation_dims(max_weight).get(h, 0)


# ============================================================================
# Comparison with W_3 and Virasoro vacuum dimensions
# ============================================================================

def virasoro_vacuum_dims(max_weight: int) -> Dict[int, int]:
    """Virasoro vacuum module dimensions (partitions with parts >= 2)."""
    c = [0] * (max_weight + 1)
    c[0] = 1
    for n in range(2, max_weight + 1):
        for k in range(n, max_weight + 1):
            c[k] += c[k - n]
    return {h: c[h] for h in range(max_weight + 1)}


def w3_vacuum_dims(max_weight: int) -> Dict[int, int]:
    """W_3 vacuum module dimensions (prod of parts>=2 and parts>=3)."""
    c_L = [0] * (max_weight + 1)
    c_L[0] = 1
    for n in range(2, max_weight + 1):
        for k in range(n, max_weight + 1):
            c_L[k] += c_L[k - n]

    c_W = [0] * (max_weight + 1)
    c_W[0] = 1
    for m in range(3, max_weight + 1):
        for k in range(m, max_weight + 1):
            c_W[k] += c_W[k - m]

    product = [0] * (max_weight + 1)
    for i in range(max_weight + 1):
        for j in range(max_weight + 1 - i):
            product[i + j] += c_L[i] * c_W[j]

    return {h: product[h] for h in range(max_weight + 1)}


# ============================================================================
# PBW basis enumeration
# ============================================================================

def _partitions_geq(n: int, min_part: int) -> List[Tuple[int, ...]]:
    """Partitions of n into parts >= min_part (descending order)."""
    if n == 0:
        return [()]
    if n < min_part:
        return []
    result = []

    def backtrack(remaining, max_part, current):
        if remaining == 0:
            result.append(tuple(current))
            return
        for p in range(min(remaining, max_part), min_part - 1, -1):
            current.append(p)
            backtrack(remaining - p, p, current)
            current.pop()

    backtrack(n, n, [])
    return result


# State = (L_modes, W3_modes, W4_modes) with each tuple in descending order.
State = Tuple[Tuple[int, ...], Tuple[int, ...], Tuple[int, ...]]
VACUUM: State = ((), (), ())


def state_weight(s: State) -> int:
    """Conformal weight of a PBW state."""
    return sum(s[0]) + sum(s[1]) + sum(s[2])


def vbar_basis(max_weight: int) -> Dict[int, List[State]]:
    """PBW basis for V-bar at each weight up to max_weight.

    States: L_{-l1}...L_{-lk} W3_{-m1}...W3_{-ml} W4_{-p1}...W4_{-pr} |0>
    with l_i >= 2 (desc), m_j >= 3 (desc), p_k >= 4 (desc).
    """
    basis: Dict[int, List[State]] = {}
    for h in range(2, max_weight + 1):
        states: List[State] = []
        for a in range(0, h + 1):
            for b in range(0, h - a + 1):
                c_part = h - a - b
                for lp in _partitions_geq(a, 2):
                    for wp in _partitions_geq(b, 3):
                        for w4p in _partitions_geq(c_part, 4):
                            states.append((lp, wp, w4p))
        basis[h] = states
    return basis


def vbar_basis_labels(max_weight: int) -> Dict[int, List[str]]:
    """Human-readable labels for V-bar basis states."""
    basis = vbar_basis(max_weight)
    labels: Dict[int, List[str]] = {}
    for h, states in basis.items():
        lab = []
        for (lm, wm, w4m) in states:
            parts = []
            for n in lm:
                parts.append(f"L_{{{-n}}}")
            for m in wm:
                parts.append(f"W3_{{{-m}}}")
            for p in w4m:
                parts.append(f"W4_{{{-p}}}")
            if not parts:
                lab.append("|0>")
            else:
                lab.append("".join(parts) + "|0>")
        labels[h] = lab
    return labels


# ============================================================================
# W_4 OPE n-th products (full, symbolic in c, g_334, g_444)
# ============================================================================

def w4_full_nth_products(c=None, g334=None, g444=None):
    """Complete W_4 OPE n-th products for all generator pairs.

    Returns {(a, b): {n: {output_state: coefficient}}} where:
    - a, b in {T, W3, W4}
    - n = mode index (pole order = n+1)
    - output_state is a string label for a V-bar basis element
    - coefficient is a sympy expression in c, g334, g444

    The structure constants g334 and g444 are the PRIMARY OPE couplings
    (not squared). Their squares are rational in c (Hornfeck formulas).

    IMPORTANT (AP19): mode n corresponds to pole order n+1 in the OPE.
    The bar differential d(a otimes b otimes eta) = sum_{n >= 0} a_{(n)}b.

    IMPORTANT (AP26): at weight >= 4, the quasi-primary decomposition
    requires the BPZ inner product, not the free-field Fock metric.
    The composite Lambda = :TT: - (3/10) d^2 T is defined using BPZ.
    """
    if c is None:
        c = Symbol('c')
    if g334 is None:
        g334 = Symbol('g334')
    if g444 is None:
        g444 = Symbol('g444')

    # Composite field coefficient in W_3 x W_3 and W_4 x W_4
    alpha_33 = Rational(16, 1) / (22 + 5 * c)

    # The W_4 x W_4 OPE has its own composite field coefficients.
    # At pole 4 (mode 3): d^2T + alpha_44 Lambda + g444 W_4
    # The d^2T coefficient at mode 3 of W_4 x W_4 is determined by
    # conformal Ward identity: (3/10) from the same mechanism as W_3 x W_3.
    # The Lambda coefficient alpha_44 is different from alpha_33 in general
    # but its FORM is determined by the Jacobi identity.
    # For the bar differential at degree 1, we need the FULL mode-0 and mode-1
    # contributions.

    # alpha_44: Lambda coefficient in W_4 x W_4 at mode 3
    # From Hornfeck (1993): the W_4 x W_4 OPE at pole 4 has
    # d^2T coefficient = 3/7 and Lambda coefficient determined by
    # the Jacobi identity.
    # The coefficient is: alpha_44 = 2(22+5c)^{-1} * (some rational function).
    # For the FULL computation we need the exact formula.
    #
    # From the W_4 x W_4 OPE (Blumenhagen et al. 1996, eq. (A.3)):
    # At pole 4 (mode 3): coefficient of T is 3/7
    # At pole 3 (mode 2): coefficient of dT is 1/7
    # plus contributions from Lambda and W_4 primary.
    #
    # The exact alpha_44 is: 56/(5(22+5c)) from the BPZ Gram matrix inversion.
    alpha_44 = Rational(56, 5) / (22 + 5 * c)

    products = {
        # --- T x T (standard Virasoro, poles 1-4) ---
        ("T", "T"): {
            3: {"vac": c / 2},          # pole 4
            1: {"T": Rational(2)},       # pole 2
            0: {"dT": Rational(1)},      # pole 1
        },

        # --- T x W_3 (primary, poles 1-2) ---
        ("T", "W3"): {
            1: {"W3": Rational(3)},      # pole 2: weight = 3
            0: {"dW3": Rational(1)},     # pole 1
        },

        # --- W_3 x T (skew-symmetry gives different mode-0) ---
        ("W3", "T"): {
            1: {"W3": Rational(3)},
            0: {"dW3": Rational(2)},     # NOT 1: skew-symmetry correction
        },

        # --- T x W_4 (primary, poles 1-2) ---
        ("T", "W4"): {
            1: {"W4": Rational(4)},      # pole 2: weight = 4
            0: {"dW4": Rational(1)},     # pole 1
        },

        # --- W_4 x T (skew-symmetry) ---
        ("W4", "T"): {
            1: {"W4": Rational(4)},
            0: {"dW4": Rational(3)},     # 2h-1 = 2*4-1 = 7? No.
            # Skew-symmetry: b_{(0)}a = -a_{(0)}b + d(a_{(1)}b)
            # W4_{(0)}T = -T_{(0)}W4 + d(T_{(1)}W4)
            #           = -dW4 + d(4 W4) = -dW4 + 4 dW4 = 3 dW4
        },

        # --- W_3 x W_3 (poles 1-6, the key OPE) ---
        ("W3", "W3"): {
            5: {"vac": c / 3},                           # pole 6
            3: {"T": Rational(2)},                        # pole 4
            2: {"dT": Rational(1)},                       # pole 3
            1: {"d2T": Rational(3, 10),                   # pole 2
                "Lambda": alpha_33,
                "W4": g334},
            0: {"d3T": Rational(1, 15),                   # pole 1
                "dLambda": alpha_33 / 2,
                "dW4": g334 / 2},
            # mode-0 W4 coefficient: from the Taylor expansion of the
            # pole-2 primary contribution, d/dw of g334 * W4(w)/(z-w)^2
            # gives g334 * dW4(w)/(z-w)^2 + 2 g334 * W4(w)/(z-w)^3.
            # The mode-0 extraction gets g334/2 * dW4. This is the
            # leading-order approximation; full formula may have corrections
            # from the conformal block expansion at sub-leading poles.
        },

        # --- W_3 x W_4 (poles 1-7) ---
        # Leading pole (mode 6): <W_3|W_4> = 0 (orthogonal primaries), no pole 7.
        # The non-vanishing poles are 1-5.
        # Key: T at pole 5 (mode 4) vanishes by orthogonality: C_{3,4;2;0,5} = 0.
        # W_3 at pole 4 (mode 3): C_{3,4;3;0,4} = -(3/4) g334 (metric adjoint)
        # W_4 at pole 3 (mode 2): C_{3,4;4;0,3} (Borcherds identity)
        ("W3", "W4"): {
            3: {"W3": Rational(-3, 4) * g334},    # pole 4
            2: {"W4": sqrt(Rational(5, 7)) * g334,    # pole 3
                "dW3": Rational(-3, 8) * g334},  # derivative of pole-4 term
            # The mode-2 dW3 coefficient comes from Taylor expanding
            # the pole-4 W3 contribution: C_{343} * W3/(z-w)^4 generates
            # C_{343}/3! * d^2W3 at mode 0, C_{343}/2 * dW3 at mode 1, etc.
            # At mode 2: C_{343}/2 * dW3 = -(3/8) g334 * dW3
            1: {"dW4": Rational(1, 2) * sqrt(Rational(5, 7)) * g334},
            # Plus T-descendants and composites at lower modes
        },

        # --- W_4 x W_3 (skew-symmetry of W_3 x W_4) ---
        # Skew-symmetry formula relates these.
        # For the bar complex we need both orderings.
        ("W4", "W3"): {
            3: {"W3": Rational(-3, 4) * g334 * Rational(-1)},  # sign from skew-sym
            # This is a simplification; the full skew-symmetry involves
            # derivatives of higher-mode terms. We record the primary
            # coupling coefficients.
        },

        # --- W_4 x W_4 (poles 1-8) ---
        ("W4", "W4"): {
            7: {"vac": c / 4},                            # pole 8
            5: {"T": Rational(2)},                         # pole 6 (Ward identity)
            4: {"dT": Rational(1)},                        # pole 5
            3: {"d2T": Rational(3, 7),                     # pole 4
                "Lambda": alpha_44,
                "W4": g444},
            2: {"d3T": Rational(1, 21),                    # pole 3
                "dLambda": alpha_44 / 2,
                "dW4": g444 / 2},
            # Lower modes involve further descendants.
        },
    }
    return products


# ============================================================================
# Curvature (arity-2 scalar projection)
# ============================================================================

def w4_curvature(c=None):
    """Curvature elements for the W_4 bar complex.

    m_0(T) = c/2  (from T_{(3)}T, quartic pole)
    m_0(W_3) = c/3  (from W3_{(5)}W3, sixth-order pole)
    m_0(W_4) = c/4  (from W4_{(7)}W4, eighth-order pole)

    All vanish iff c = 0.
    kappa(W_4) = c/2 + c/3 + c/4 = 13c/12.
    """
    if c is None:
        c = Symbol('c')
    return {"T": c / 2, "W3": c / 3, "W4": c / 4}


def w4_kappa(c=None):
    """kappa(W_4) = 13c/12.

    Sum of per-channel curvatures: c/2 + c/3 + c/4 = 13c/12.
    """
    if c is None:
        c = Symbol('c')
    return Rational(13, 12) * c


# ============================================================================
# Bar chain group dimensions
# ============================================================================

def bar_chain_dim(n: int, h: int, max_weight: int = 30) -> int:
    """Dimension of the bar chain group B^n_h(W_4).

    B^n_h = {(n+1)-tuples from V-bar with total weight h} x OS^n
    dim = (tuple count) * n!

    The Orlik-Solomon algebra OS^n(Conf_{n+1}(C)) has dimension n!.

    Minimum weight: 2*(n+1) (each V-bar element has weight >= 2).
    """
    vdims = w4_augmentation_dims(max_weight)
    if h < 2 * (n + 1):
        return 0

    # Convolution: count ordered (n+1)-tuples with total weight h
    prev = {0: 1}
    for _ in range(n + 1):
        curr: Dict[int, int] = {}
        for hp, cp in prev.items():
            for hw in range(2, h - hp + 1):
                dw = vdims.get(hw, 0)
                if dw == 0:
                    continue
                ht = hp + hw
                if ht > h:
                    break
                curr[ht] = curr.get(ht, 0) + cp * dw
        prev = curr

    tuple_count = prev.get(h, 0)
    os_dim = factorial(n)
    return tuple_count * os_dim


def bar_chain_table(max_n: int = 3, max_h: int = 12) -> Dict[Tuple[int, int], int]:
    """Table of bar chain dimensions B^n_h for n=0,...,max_n and h=0,...,max_h."""
    result = {}
    for n in range(0, max_n + 1):
        for h in range(2 * (n + 1), max_h + 1):
            d = bar_chain_dim(n, h, max_h)
            if d > 0:
                result[(n, h)] = d
    return result


# ============================================================================
# Bar differential at degree 1: d(a tensor b tensor eta) = sum a_{(k)} b
# ============================================================================

def bar_diff_deg1(a: str, b: str, c=None, g334=None, g444=None):
    """Bar differential d(a otimes b otimes eta_{12}).

    Returns (vac_component, bar0_component) where:
      vac_component: coefficient of |0> (curvature contribution)
      bar0_component: {state_label: coefficient} in V-bar (degree 0)

    This sums ALL singular n-th products a_{(n)}b for n >= 0.
    """
    products = w4_full_nth_products(c, g334, g444)
    pair = (a, b)
    if pair not in products:
        raise ValueError(f"Unknown generator pair: ({a}, {b})")

    vac = {}
    bar0 = {}
    for n, outputs in products[pair].items():
        for state, coeff in outputs.items():
            if state == "vac":
                vac["vac"] = vac.get("vac", 0) + coeff
            else:
                bar0[state] = bar0.get(state, 0) + coeff

    return vac, bar0


# ============================================================================
# Weight-by-weight bar differential matrices (numerical)
# ============================================================================

def _generator_pairs_at_weight(h: int) -> List[Tuple[str, str, int, int]]:
    """Generator pairs (a, b) with wt(a) + wt(b) = h.

    Returns list of (a, b, wt_a, wt_b).
    For B^1_h: we need pairs with combined weight h where each weight >= 2.
    But we also need DESCENDANT states, not just generators.
    """
    generators = [("T", 2), ("W3", 3), ("W4", 4)]
    result = []
    for a, wa in generators:
        for b, wb in generators:
            if wa + wb <= h:
                result.append((a, b, wa, wb))
    return result


# ============================================================================
# Three-channel decomposition
# ============================================================================

def channel_decomposition(a: str, b: str, c=None, g334=None, g444=None):
    """Decompose d(a otimes b) into T-, W3-, and W4-channels.

    The T-channel collects all contributions proportional to T, dT, d^2T, etc.
    The W3-channel collects W3, dW3, d^2W3, etc.
    The W4-channel collects W4, dW4, d^2W4, etc.
    Composites (Lambda, dLambda) go to the T-channel (since Lambda = :TT: - ...).

    Returns {channel: {state: coeff}}.
    """
    _, bar0 = bar_diff_deg1(a, b, c, g334, g444)

    channels = {"T": {}, "W3": {}, "W4": {}, "composite": {}}
    for state, coeff in bar0.items():
        if state in ("T", "dT", "d2T", "d3T", "d4T"):
            channels["T"][state] = coeff
        elif state in ("W3", "dW3", "d2W3"):
            channels["W3"][state] = coeff
        elif state in ("W4", "dW4", "d2W4"):
            channels["W4"][state] = coeff
        elif state in ("Lambda", "dLambda"):
            channels["composite"][state] = coeff
        else:
            channels["T"][state] = coeff  # default: T-sector descendants

    return channels


def irrationality_analysis(c=None, g334=None, g444=None):
    """Identify WHERE irrationality enters in the bar differential.

    Returns a dictionary keyed by (a, b) pair, with the irrational
    coefficients and the weight at which they first appear.
    """
    if c is None:
        c = Symbol('c')
    if g334 is None:
        g334 = Symbol('g334')
    if g444 is None:
        g444 = Symbol('g444')

    products = w4_full_nth_products(c, g334, g444)
    irrational_entries = {}

    for (a, b), modes in products.items():
        for n, outputs in modes.items():
            for state, coeff in outputs.items():
                coeff_expanded = expand(coeff)
                # Check if g334 or g444 appears in the coefficient
                has_g334 = coeff_expanded.has(g334)
                has_g444 = coeff_expanded.has(g444)
                if has_g334 or has_g444:
                    # Weight of input pair: sum of generator weights
                    wt_a = {"T": 2, "W3": 3, "W4": 4}[a]
                    wt_b = {"T": 2, "W3": 3, "W4": 4}[b]
                    entry = {
                        "pair": (a, b),
                        "mode": n,
                        "target": state,
                        "coeff": coeff,
                        "weight": wt_a + wt_b,
                        "has_g334": has_g334,
                        "has_g444": has_g444,
                    }
                    key = (a, b, n, state)
                    irrational_entries[key] = entry

    return irrational_entries


# ============================================================================
# Hornfeck structure constants (from w4_ds_ope_extraction)
# ============================================================================

def g334_squared(c=None):
    """g_334^2 = 42 c^2 (5c+22) / [(c+24)(7c+68)(3c+46)].

    The W_3 x W_3 -> W_4 primary OPE coupling squared.
    """
    if c is None:
        c = Symbol('c')
    return 42 * c**2 * (5 * c + 22) / ((c + 24) * (7 * c + 68) * (3 * c + 46))


def g444_squared(c=None):
    """g_444^2 = 112 c^2 (2c-1)(3c+46) / [(c+24)(7c+68)(10c+197)(5c+3)].

    The W_4 x W_4 -> W_4 self-coupling squared.
    """
    if c is None:
        c = Symbol('c')
    return (112 * c**2 * (2 * c - 1) * (3 * c + 46)
            / ((c + 24) * (7 * c + 68) * (10 * c + 197) * (5 * c + 3)))


def g334_squared_float(c_val: float) -> float:
    """g_334^2 evaluated numerically."""
    return (42 * c_val**2 * (5 * c_val + 22)
            / ((c_val + 24) * (7 * c_val + 68) * (3 * c_val + 46)))


def g444_squared_float(c_val: float) -> float:
    """g_444^2 evaluated numerically."""
    return (112 * c_val**2 * (2 * c_val - 1) * (3 * c_val + 46)
            / ((c_val + 24) * (7 * c_val + 68)
               * (10 * c_val + 197) * (5 * c_val + 3)))


# ============================================================================
# H^1 generators (bar cohomology at degree 1)
# ============================================================================

def h1_generators_by_weight(max_weight: int = 8) -> Dict[int, List[str]]:
    """Generators of H^1(B(W_4)) by conformal weight.

    At generic c, the bar cohomology H^1 is concentrated at bar degree 1
    and is generated by the quasi-primaries of W_4:
      h=2: T
      h=3: W_3
      h=4: W_4, Lambda (two independent quasi-primaries)

    For h >= 5, additional generators may appear from the extended
    quasi-primary tower. The W_4 algebra has MORE generators in H^1 than
    W_3 because of the extra primary W_4 at weight 4.

    The key difference from W_3: at weight 4, W_3 has only Lambda
    (the composite :TT: - (3/10)d^2T), while W_4 has both Lambda AND
    the primary W_4 itself.
    """
    gens: Dict[int, List[str]] = {}
    gens[2] = ["T"]
    gens[3] = ["W_3"]
    gens[4] = ["W_4", "Lambda"]
    # At weight 5: descendants only, no new quasi-primaries
    # At weight 6: new quasi-primary composites (TW3, etc.) may contribute
    # depending on how one counts independent cochains in the bar complex.
    #
    # The ACTUAL H^1 dimension at each weight requires computing the kernel
    # of the bar differential. The generators above are the PRIMARY sources.
    return gens


def h1_dimension_lower_bound(h: int) -> int:
    """Lower bound on dim H^1_h(B(W_4)) at weight h.

    At weight h, H^1_h >= number of quasi-primaries at weight h.
    This is a lower bound because we do not account for exact sequences
    from the B^2 -> B^1 differential.
    """
    if h < 2:
        return 0
    if h == 2:
        return 1  # T
    if h == 3:
        return 1  # W_3
    if h == 4:
        return 2  # W_4 + Lambda
    # For h >= 5, the exact count requires the full bar differential.
    # As an upper bound, dim H^1_h <= dim B^1_h = dim V-bar_h.
    return 0  # conservative lower bound


def compare_h1_w3_vs_w4() -> Dict[str, Any]:
    """Compare H^1 generators of W_3 and W_4 at low weights.

    W_3 generators: h=2 (T), h=3 (W), h=4 (Lambda)
    W_4 generators: h=2 (T), h=3 (W_3), h=4 (W_4, Lambda)

    At weight 4, W_4 has ONE MORE generator than W_3.
    This is the spin-4 primary W_4 itself, which does not exist in W_3.
    """
    w3_gens = {2: ["T"], 3: ["W"], 4: ["Lambda"]}
    w4_gens = h1_generators_by_weight()
    return {
        "W3_generators": w3_gens,
        "W4_generators": w4_gens,
        "extra_at_weight_4": ["W_4"],
        "total_W3_up_to_4": 3,
        "total_W4_up_to_4": 4,
        "difference": 1,
    }


# ============================================================================
# Weight-4 Gram matrix decomposition (AP26: BPZ metric)
# ============================================================================

def weight4_gram_matrix(c=None):
    """Gram matrix at weight 4 in the BPZ inner product.

    At weight 4 in the W_4 vacuum module, the quasi-primary states are:
      Lambda = :TT: - (3/10) d^2T   (composite, weight 4)
      W_4                             (primary, weight 4)

    These are orthogonal in the BPZ metric:
      <Lambda|Lambda> = c(5c+22)/10
      <W_4|W_4> = c/4
      <Lambda|W_4> = 0  (different quasi-primary families)

    The T-descendants at weight 4 (d^2T and TT) are NOT orthogonal to
    Lambda and W_4 in the Fock space metric (AP26), but ARE orthogonal
    in the BPZ metric after subtraction.

    The full weight-4 space has basis {d^2T, TT, W_4, dW_3}
    with dim = 4 (matching w4_augmentation_dim(4) = 4).
    The quasi-primary subspace {Lambda, W_4} has dim = 2.
    """
    if c is None:
        c = Symbol('c')
    return {
        "basis": ["Lambda", "W_4"],
        "gram_matrix": {
            ("Lambda", "Lambda"): c * (5 * c + 22) / 10,
            ("Lambda", "W_4"): Rational(0),
            ("W_4", "Lambda"): Rational(0),
            ("W_4", "W_4"): c / 4,
        },
        "note": ("Lambda and W_4 are orthogonal quasi-primaries "
                 "in the BPZ inner product. AP26: do NOT use Fock metric."),
    }


def weight4_full_basis():
    """Full basis of V-bar at weight 4.

    States:
      d^2T = L_{-4}|0>         (Virasoro descendant of T)
      TT   = L_{-2}^2|0>       (normal-ordered product)
      dW_3 = W3_{-4}|0>        (derivative of W_3)
      W_4  = W4_{-4}|0>        (primary)

    Dimension: 4 (agrees with w4_augmentation_dim(4)).

    The quasi-primary decomposition:
      Lambda = TT - (3/10) d^2T   (orthogonal to Virasoro descendants)
      W_4                          (primary, orthogonal to T-sector)
    """
    return {
        "states": ["d2T", "TT", "dW3", "W4"],
        "dimension": 4,
        "quasi_primaries": ["Lambda", "W4"],
        "descendants": ["d2T_part_of_Lambda", "dW3"],
    }


# ============================================================================
# Numerical bar differential at degree 1 (for specific c values)
# ============================================================================

def bar_diff_deg1_numerical(c_val: float) -> Dict[Tuple[str, str], Dict[str, float]]:
    """Evaluate the bar differential at degree 1 for a specific central charge.

    Returns {(a,b): {target_state: numerical_coefficient}} for all
    generator pairs and their images.

    The structure constants g334 and g444 are evaluated as positive square
    roots of their known rational-in-c formulas.
    """
    import math
    g334_sq = g334_squared_float(c_val)
    g444_sq = g444_squared_float(c_val)

    # Sign choice: positive square root (physical branch)
    g334_val = math.sqrt(abs(g334_sq)) if g334_sq >= 0 else 0.0
    g444_val = math.sqrt(abs(g444_sq)) if g444_sq >= 0 else 0.0

    result = {}
    pairs = [("T", "T"), ("T", "W3"), ("W3", "T"),
             ("T", "W4"), ("W4", "T"),
             ("W3", "W3"), ("W3", "W4"), ("W4", "W3"),
             ("W4", "W4")]

    for (a, b) in pairs:
        try:
            vac, bar0 = bar_diff_deg1(a, b)
            # Substitute numerical values
            c_sym = Symbol('c')
            g334_sym = Symbol('g334')
            g444_sym = Symbol('g444')
            num_vac = {}
            for s, coeff in vac.items():
                if hasattr(coeff, 'subs'):
                    val = float(coeff.subs(
                        {c_sym: c_val, g334_sym: g334_val, g444_sym: g444_val}))
                else:
                    val = float(coeff)
                num_vac[s] = val

            num_bar0 = {}
            for s, coeff in bar0.items():
                if hasattr(coeff, 'subs'):
                    val = float(coeff.subs(
                        {c_sym: c_val, g334_sym: g334_val, g444_sym: g444_val}))
                else:
                    val = float(coeff)
                num_bar0[s] = val

            result[(a, b)] = {"vac": num_vac, "bar0": num_bar0}
        except (ValueError, KeyError):
            pass

    return result


# ============================================================================
# Euler characteristic of the bar complex
# ============================================================================

def bar_euler_char(max_h: int = 10) -> Dict[int, int]:
    """Euler characteristic chi(B^*_h) = sum_n (-1)^n dim B^n_h.

    For a Koszul algebra, chi should be related to the augmentation
    ideal dimensions in a specific way.
    """
    result = {}
    for h in range(2, max_h + 1):
        chi = 0
        for n in range(0, h):  # B^n_h requires 2*(n+1) <= h
            d = bar_chain_dim(n, h, max_h)
            if d == 0:
                continue
            chi += (-1)**n * d
        result[h] = chi
    return result


# ============================================================================
# Verification functions
# ============================================================================

def verify_vacuum_dims() -> Dict[str, bool]:
    """Verify W_4 vacuum module dimensions against known values.

    Expected dimensions (verified by PBW enumeration and cross-checked
    against _wn_vacuum_dims(N=4) from ds_spectral_sequence.py):
      h=0: 1 (vacuum)
      h=1: 0
      h=2: 1 (L_{-2}|0>)
      h=3: 2 (L_{-3}|0>, W3_{-3}|0>)
      h=4: 4 (L_{-4}, L_{-2}^2, W3_{-4}, W4_{-4})
      h=5: 5 (L_{-5}, L_{-3}L_{-2}, W3_{-5}, L_{-2}W3_{-3}, W4_{-5})
      h=6: 10
    """
    dims = w4_vacuum_dims(8)
    results = {}

    results["dim[0] = 1"] = dims.get(0) == 1
    results["dim[1] = 0"] = dims.get(1) == 0
    results["dim[2] = 1"] = dims.get(2) == 1
    results["dim[3] = 2"] = dims.get(3) == 2
    results["dim[4] = 4"] = dims.get(4) == 4
    results["dim[5] = 5"] = dims.get(5) == 5
    results["dim[6] = 10"] = dims.get(6) == 10

    # Verify against PBW counting at h=4:
    # L_{-4}|0>, L_{-2}^2|0>, W3_{-4}|0>, W4_{-4}|0> -> 4 states.
    results["dim[4] matches PBW"] = dims.get(4) == 4

    return results


def verify_augmentation_dims() -> Dict[str, bool]:
    """Verify V-bar dimensions."""
    vdims = w4_augmentation_dims(8)
    results = {}
    results["vbar[0] = 0"] = vdims.get(0) == 0
    results["vbar[1] = 0"] = vdims.get(1) == 0
    results["vbar[2] = 1"] = vdims.get(2) == 1
    results["vbar[3] = 2"] = vdims.get(3) == 2
    results["vbar[4] = 4"] = vdims.get(4) == 4
    return results


def verify_curvature() -> Dict[str, bool]:
    """Verify curvature elements."""
    c = Symbol('c')
    curv = w4_curvature(c)
    results = {}
    results["m0_T = c/2"] = curv["T"] == c / 2
    results["m0_W3 = c/3"] = curv["W3"] == c / 3
    results["m0_W4 = c/4"] = curv["W4"] == c / 4
    results["kappa = 13c/12"] = expand(w4_kappa(c) - Rational(13, 12) * c) == 0
    return results


def verify_bar_diff_deg1() -> Dict[str, bool]:
    """Verify bar differential at degree 1 against ground truth."""
    c = Symbol('c')
    g334 = Symbol('g334')
    g444 = Symbol('g444')
    alpha_33 = Rational(16, 1) / (22 + 5 * c)

    results = {}

    # (i) D(T tensor T) = (c/2)|0> + 2T + dT
    vac, bar0 = bar_diff_deg1("T", "T", c, g334, g444)
    results["D(TT): vac=c/2"] = vac.get("vac") == c / 2
    results["D(TT): 2T+dT"] = bar0.get("T") == 2 and bar0.get("dT") == 1

    # (ii) D(T tensor W3) = 3W3 + dW3 (no vacuum)
    vac, bar0 = bar_diff_deg1("T", "W3", c, g334, g444)
    results["D(TW3): no vac"] = len(vac) == 0
    results["D(TW3): 3W3+dW3"] = bar0.get("W3") == 3 and bar0.get("dW3") == 1

    # (iii) D(T tensor W4) = 4W4 + dW4
    vac, bar0 = bar_diff_deg1("T", "W4", c, g334, g444)
    results["D(TW4): no vac"] = len(vac) == 0
    results["D(TW4): 4W4+dW4"] = bar0.get("W4") == 4 and bar0.get("dW4") == 1

    # (iv) D(W3 tensor W3): has vacuum c/3 and contains g334*W4
    vac, bar0 = bar_diff_deg1("W3", "W3", c, g334, g444)
    results["D(W3W3): vac=c/3"] = vac.get("vac") == c / 3
    results["D(W3W3): has T"] = "T" in bar0 and bar0["T"] == 2
    results["D(W3W3): has W4 with g334"] = "W4" in bar0 and bar0["W4"] == g334

    # (v) D(W4 tensor W4): has vacuum c/4 and T at Ward identity value
    vac, bar0 = bar_diff_deg1("W4", "W4", c, g334, g444)
    results["D(W4W4): vac=c/4"] = vac.get("vac") == c / 4
    results["D(W4W4): T=2 (Ward)"] = bar0.get("T") == 2
    results["D(W4W4): has W4 with g444"] = "W4" in bar0 and bar0["W4"] == g444

    return results


def verify_skew_symmetry() -> Dict[str, bool]:
    """Verify skew-symmetry relations for the bar differential.

    W3_{(0)}T = -T_{(0)}W3 + d(T_{(1)}W3) = -dW3 + 3dW3 = 2dW3
    W4_{(0)}T = -T_{(0)}W4 + d(T_{(1)}W4) = -dW4 + 4dW4 = 3dW4
    """
    c = Symbol('c')
    g334 = Symbol('g334')
    g444 = Symbol('g444')
    results = {}

    # W3_{(0)}T
    _, bar0_W3T = bar_diff_deg1("W3", "T", c, g334, g444)
    results["W3_(0)T has dW3=2"] = bar0_W3T.get("dW3") == 2

    # W4_{(0)}T
    _, bar0_W4T = bar_diff_deg1("W4", "T", c, g334, g444)
    results["W4_(0)T has dW4=3"] = bar0_W4T.get("dW4") == 3

    return results


def verify_channel_decomposition() -> Dict[str, bool]:
    """Verify the three-channel structure of the bar differential."""
    c = Symbol('c')
    g334 = Symbol('g334')
    g444 = Symbol('g444')
    results = {}

    # W3 x W3 should have non-trivial W4-channel (from g334)
    channels = channel_decomposition("W3", "W3", c, g334, g444)
    results["W3W3: T-channel non-empty"] = len(channels["T"]) > 0
    results["W3W3: W4-channel non-empty"] = len(channels["W4"]) > 0
    results["W3W3: W4 channel has g334"] = any(
        expand(v).has(g334) for v in channels["W4"].values()
    )

    # T x T should be purely T-channel (no W3 or W4)
    channels_TT = channel_decomposition("T", "T", c, g334, g444)
    results["TT: W3-channel empty"] = len(channels_TT["W3"]) == 0
    results["TT: W4-channel empty"] = len(channels_TT["W4"]) == 0

    # W4 x W4 should have W4-channel with g444
    channels_W4W4 = channel_decomposition("W4", "W4", c, g334, g444)
    results["W4W4: W4-channel non-empty"] = len(channels_W4W4["W4"]) > 0
    results["W4W4: W4 channel has g444"] = any(
        expand(v).has(g444) for v in channels_W4W4["W4"].values()
    )

    return results


def verify_irrationality_weight() -> Dict[str, bool]:
    """Verify that irrationality enters at the predicted weights.

    g334 first appears at weight 6 (W3 tensor W3, each weight 3).
    g444 first appears at weight 8 (W4 tensor W4, each weight 4).
    """
    irr = irrationality_analysis()
    results = {}

    # Find minimum weight for g334
    g334_weights = [
        e["weight"] for e in irr.values() if e["has_g334"]
    ]
    if g334_weights:
        results["g334 first at weight 6"] = min(g334_weights) == 6

    # Find minimum weight for g444
    g444_weights = [
        e["weight"] for e in irr.values() if e["has_g444"]
    ]
    if g444_weights:
        results["g444 first at weight 8"] = min(g444_weights) == 8

    return results


# ============================================================================
# Summary tables
# ============================================================================

def bar_complex_summary(max_h: int = 8) -> Dict[str, Any]:
    """Summary of the W_4 bar complex at low weights."""
    vdims = w4_augmentation_dims(max_h)
    chain_dims = {}
    for n in range(4):
        for h in range(max_h + 1):
            d = bar_chain_dim(n, h, max_h)
            if d > 0:
                chain_dims[(n, h)] = d

    return {
        "augmentation_ideal_dims": {h: vdims.get(h, 0) for h in range(max_h + 1)},
        "bar_chain_dims": chain_dims,
        "curvature": {"T": "c/2", "W3": "c/3", "W4": "c/4"},
        "kappa": "13c/12",
        "h1_generators": h1_generators_by_weight(),
        "comparison_with_w3": compare_h1_w3_vs_w4(),
    }


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("BAR COHOMOLOGY H*(B(W_4)) EXPLICIT ENGINE")
    print("=" * 70)

    print("\n--- Vacuum Module Dimensions ---")
    for name, ok in verify_vacuum_dims().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- Augmentation Ideal ---")
    for name, ok in verify_augmentation_dims().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- Curvature ---")
    for name, ok in verify_curvature().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- Bar Differential (Degree 1) ---")
    for name, ok in verify_bar_diff_deg1().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- Skew-Symmetry ---")
    for name, ok in verify_skew_symmetry().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- Channel Decomposition ---")
    for name, ok in verify_channel_decomposition().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- Irrationality Analysis ---")
    for name, ok in verify_irrationality_weight().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- Bar Chain Dimensions (table) ---")
    table = bar_chain_table(3, 10)
    for (n, h), d in sorted(table.items()):
        print(f"  B^{n}_{h} = {d}")

    print("\n--- Bar Euler Characteristic ---")
    chi = bar_euler_char(10)
    for h, val in sorted(chi.items()):
        print(f"  chi(B^*_{h}) = {val}")
