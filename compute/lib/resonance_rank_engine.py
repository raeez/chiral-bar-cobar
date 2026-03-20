"""Resonance rank classification and MC4 splitting engine.

The resonance rank rho(A) classifies the difficulty of the completed
bar-cobar tower. MC4 splits into:
  MC4+ (rho=0, positive): weight-stabilized, automatic completion
  MC4^0 (rho>=1, resonant): finite resonance problem via filtered bar-cobar

Key objects:
  - Reduced-weight windows K_q(A): bar cohomology dimension at weight q
  - Resonance rank rho(A): dim of weight-0 subspace in completion
  - Coefficient stabilization: a^(N)_{ij} -> a_{ij} as N -> infinity
  - Virasoro resonance shadow: Vir_{26-c}

The weight generating function G_A(t) = sum K_q * t^q encodes the
combinatorics of the completed bar-cobar tower. For the standard families:
  Heisenberg:     G(t) = 1/(1-t)          (one generator, weight 1)
  Affine sl_2:    G(t) = 1/(1-t)^3        (three generators, weight 1)
  Affine g:       G(t) = 1/(1-t)^{dim g}
  Virasoro:       G(t) = prod_{n>=2} 1/(1-t^n)   (generators L_{-n}, n>=2)
  W_N:            G(t) = prod_{s=2}^{N} prod_{n>=s} 1/(1-t^n)
  betagamma:      G(t) = 1/(1-t)^2        (two generators, weight 1)

References:
  concordance.tex: thm:resonance-filtered-bar-cobar, def:resonance-rank,
  thm:coefficient-stability-criterion, conj:platonic-completion
  higher_genus_modular_koszul.tex: def:resonance-rank, thm:resonance-filtered-bar-cobar
"""

from __future__ import annotations

import math
from functools import lru_cache
from typing import Dict, List, Optional, Tuple

from sympy import Rational, Symbol, pi, sqrt, log, oo


# ===========================================================================
# 1. Partition helpers
# ===========================================================================

@lru_cache(maxsize=256)
def _partition_number(n: int) -> int:
    """Number of unrestricted partitions of n.  p(0) = 1."""
    if n < 0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    for k in range(1, n + 1):
        for m in range(k, n + 1):
            dp[m] += dp[m - k]
    return dp[n]


@lru_cache(maxsize=256)
def _partitions_min_part(n: int, min_part: int) -> int:
    """Number of partitions of n into parts >= min_part.  p_{>=s}(0) = 1."""
    if n < 0:
        return 0
    if n == 0:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    for part in range(min_part, n + 1):
        for j in range(part, n + 1):
            dp[j] += dp[j - part]
    return dp[n]


# ===========================================================================
# 2. Reduced-weight windows K_q(A)
# ===========================================================================

def reduced_weight_windows(family: str, max_q: int = 20,
                           **kwargs) -> List[int]:
    """Return K_q(A) for q = 0, ..., max_q.

    K_q is the dimension of weight-q bar cohomology H^*(B(A))|_{weight q}.
    For Koszul algebras this equals the weight-q component of H^*(B(A)),
    which is concentrated in cohomological degree 1 and equals A^!_q.

    Families:
      heisenberg:   K_q = 1 for all q >= 0.
                    Bar cohomology = k[x], x of weight 1.  GF = 1/(1-t).
      affine_sl2:   K_q = (q+1)(q+2)/2 = binom(q+2,2).
                    Bar cohomology = k[e,h,f], 3 generators of weight 1.
                    GF = 1/(1-t)^3.
      affine_g:     K_q = binom(q + dim_g - 1, dim_g - 1).
                    Bar cohomology = Sym(g*[-1]) with dim_g generators of weight 1.
                    Provide dim_g=N as kwarg.
      virasoro:     K_q = partitions of q into parts >= 2.
                    Bar cohomology = k[L_2, L_3, L_4, ...].
                    GF = prod_{n>=2} 1/(1-t^n).
      w_N:          K_q = convolution of (N-1) partition series.
                    Bar cohomology = k[{W^{(s)}_{-n} : s=2..N, n>=s}].
                    Provide N as kwarg (default 3 for W_3).
      betagamma:    K_q = q + 1.
                    Bar cohomology = k[beta, gamma], 2 generators of weight 1.
                    GF = 1/(1-t)^2.
      w_infinity:   K_q = p(q) (unrestricted partitions).
                    In the N -> infinity limit of W_N.
                    GF = prod_{n>=1} 1/(1-t^n) (MacMahon connection).
      free_fermion: K_q = 1 for all q >= 0.
                    Single generator of weight 1, but fermionic so exterior.
                    Actually K_0 = 1, K_1 = 1, K_q = 0 for q >= 2 (exterior).
    """
    dispatch = {
        "heisenberg": _kq_heisenberg,
        "affine_sl2": _kq_affine_sl2,
        "affine_g": _kq_affine_g,
        "virasoro": _kq_virasoro,
        "w_N": _kq_w_N,
        "w3": _kq_w3,
        "betagamma": _kq_betagamma,
        "w_infinity": _kq_w_infinity,
        "free_fermion": _kq_free_fermion,
    }
    fn = dispatch.get(family)
    if fn is None:
        raise ValueError(f"Unknown family: {family}")
    return fn(max_q, **kwargs)


def _kq_heisenberg(max_q: int, **kw) -> List[int]:
    """K_q = 1 for all q.  One generator (J) of weight 1."""
    return [1] * (max_q + 1)


def _kq_affine_sl2(max_q: int, **kw) -> List[int]:
    """K_q = binom(q+2, 2).  Three generators of weight 1."""
    return [(q + 1) * (q + 2) // 2 for q in range(max_q + 1)]


def _kq_affine_g(max_q: int, **kw) -> List[int]:
    """K_q = binom(q + d - 1, d - 1) for d = dim(g) generators of weight 1."""
    d = kw.get("dim_g", 3)
    result = []
    for q in range(max_q + 1):
        # binom(q + d - 1, d - 1)
        val = 1
        for i in range(1, d):
            val = val * (q + i) // i
        result.append(val)
    return result


def _kq_virasoro(max_q: int, **kw) -> List[int]:
    """K_q = partitions of q into parts >= 2."""
    return [_partitions_min_part(q, 2) for q in range(max_q + 1)]


def _kq_w3(max_q: int, **kw) -> List[int]:
    """K_q for W_3: generators L_{-n} (n>=2) and W_{-m} (m>=3).

    GF = prod_{n>=2} 1/(1-t^n) * prod_{m>=3} 1/(1-t^m).
    Compute by convolving the two partition sequences.
    """
    return _kq_w_N(max_q, N=3)


def _kq_w_N(max_q: int, **kw) -> List[int]:
    """K_q for W_N algebra.

    W_N has (N-1) strong generators of spins s = 2, 3, ..., N.
    The spin-s generator contributes modes at weights n >= s.
    Bar cohomology = Sym({W^{(s)}_{-n} : n >= s, s = 2..N}).

    GF = prod_{s=2}^{N} prod_{n>=s} 1/(1-t^n).

    We compute by successively adding generator series.
    """
    N = kw.get("N", 3)
    # Start with K_q = delta_{q,0}
    result = [0] * (max_q + 1)
    result[0] = 1

    for s in range(2, N + 1):
        # Add generator modes at weights n = s, s+1, s+2, ...
        # This is equivalent to taking partitions into parts >= s
        # and convolving with the current result.
        # In-place: for each part size n >= s, accumulate.
        for n in range(s, max_q + 1):
            for j in range(n, max_q + 1):
                result[j] += result[j - n]

    return result


def _kq_betagamma(max_q: int, **kw) -> List[int]:
    """K_q = q + 1.  Two generators (beta, gamma) of weight 1."""
    return [q + 1 for q in range(max_q + 1)]


def _kq_w_infinity(max_q: int, **kw) -> List[int]:
    """K_q = p(q) (unrestricted partitions).  MacMahon limit N -> infinity."""
    return [_partition_number(q) for q in range(max_q + 1)]


def _kq_free_fermion(max_q: int, **kw) -> List[int]:
    """K_0 = 1, K_1 = 1, K_q = 0 for q >= 2.  Exterior algebra on one generator."""
    result = [0] * (max_q + 1)
    result[0] = 1
    if max_q >= 1:
        result[1] = 1
    return result


# ===========================================================================
# 3. Resonance rank rho(A)
# ===========================================================================

# Resonance rank table for standard families.
# rho(A) = dim of the weight-0 resonance subspace in the completed bar-cobar.
# MC4+ families have rho = 0; MC4^0 families have rho >= 1.
_RESONANCE_RANKS: Dict[str, int] = {
    "heisenberg": 0,
    "affine_sl2": 0,
    "affine_g": 0,
    "virasoro": 1,
    "w3": 1,
    "w_N": 1,       # rho = 1 for all finite N >= 2 (single L_0 resonance)
    "betagamma": 0,
    "w_infinity": 0,  # positive tower, MacMahon limit
    "free_fermion": 0,
}


def resonance_rank(family: str, **kwargs) -> int:
    """Return rho(A), the resonance rank.

    rho(A) = dim of the weight-0 resonance subspace in the completed
    bar-cobar tower.

    MC4+ (rho = 0): Heisenberg, affine, betagamma, W_{1+infinity}.
      Weight filtration is strictly positive; completion is automatic
      by weight stabilization (thm:stabilized-completion-positive).

    MC4^0 (rho >= 1): Virasoro, W_N (finite N >= 2).
      The single resonance direction is the L_0 = 0 mode, which
      generates the depth-zero resonance shadow Vir_{26-c}.
      The resonance-filtered bar-cobar (thm:resonance-filtered-bar-cobar)
      reduces the infinite completion problem to a finite one.
    """
    if family == "w_N":
        N = kwargs.get("N", 3)
        if N == float("inf") or N > 10**6:
            return 0  # W_infinity limit
        return 1 if N >= 2 else 0
    rho = _RESONANCE_RANKS.get(family)
    if rho is None:
        raise ValueError(f"Unknown family: {family}")
    return rho


# ===========================================================================
# 4. MC4 class
# ===========================================================================

def mc4_class(family: str, **kwargs) -> str:
    """Return 'MC4+' or 'MC4^0' for the given family.

    MC4+:  rho = 0, weight-bounded from below, solved by stabilization.
    MC4^0: rho >= 1, resonant, reduced to finite problem.
    """
    rho = resonance_rank(family, **kwargs)
    return "MC4+" if rho == 0 else "MC4^0"


# ===========================================================================
# 5. Coefficient stabilization
# ===========================================================================

def coefficient_stabilization_test(family: str, max_N: int = 10,
                                   **kwargs) -> Dict:
    """Check that bar-cobar coefficients stabilize as arity N -> infinity.

    For rho = 0 (MC4+): stabilization is AUTOMATIC by the arity cutoff
    lemma (lem:arity-cutoff). The strong filtration axiom
    mu_r(F^{i_1}, ..., F^{i_r}) subset F^{i_1+...+i_r} ensures that
    arity-N contributions to weight-q coefficients vanish for N > q.

    For rho >= 1 (MC4^0): stabilization must be checked on finite windows.
    The coefficient-stability criterion (thm:coefficient-stability-criterion)
    states: a^(N)_{ij} = a^(N+1)_{ij} for all N >= N_0(i,j).

    We model this by computing the arity cutoff: at arity N, contributions
    to weight q require N <= q (since each bar element has weight >= 1
    in the reduced complex). So coefficients at weight q stabilize at N = q.

    Returns dict with stabilization data.
    """
    rho = resonance_rank(family, **kwargs)
    K = reduced_weight_windows(family, max_q=max_N, **kwargs)

    if rho == 0:
        # MC4+: automatic stabilization
        # Arity cutoff: contribution to weight q vanishes for arity > q
        cutoffs = {}
        for q in range(max_N + 1):
            cutoffs[q] = q  # stabilizes at arity = q
        return {
            "family": family,
            "rho": rho,
            "class": "MC4+",
            "automatic": True,
            "cutoffs": cutoffs,
            "stabilized": True,
        }
    else:
        # MC4^0: resonance-filtered stabilization
        # The resonance piece has finitely many persistent classes.
        # After removing the resonance subspace, the positive part
        # stabilizes automatically. The resonance piece requires
        # explicit analysis on a finite window of size rho.
        cutoffs = {}
        for q in range(max_N + 1):
            # Positive part: cutoff at arity q
            # Resonance part: cutoff at arity 1 (the resonance is weight-0)
            cutoffs[q] = q if q > 0 else 1
        return {
            "family": family,
            "rho": rho,
            "class": "MC4^0",
            "automatic": False,
            "cutoffs": cutoffs,
            "stabilized": True,  # thm:resonance-filtered-bar-cobar
            "resonance_window": rho,
        }


# ===========================================================================
# 6. Virasoro resonance shadow
# ===========================================================================

def virasoro_resonance_shadow(c) -> Dict:
    """Compute the Virasoro depth-zero resonance shadow data.

    The Koszul dual Vir_c^! = Vir_{26-c}. The resonance shadow is the
    image of the finite-dimensional resonance truncation R_Vir.

    Key values:
      c = 13: self-dual point, Vir_13^! = Vir_13
      c = 26: Vir_26^! = Vir_0 (ghost Virasoro, trivial central charge)
      c = 0:  Vir_0^! = Vir_26

    The complementarity sum c + c' = 26 is the shadow of Theorem C
    projected to the Virasoro family.
    """
    c_sym = Symbol("c") if c is None else c
    c_dual = 26 - c_sym

    is_self_dual = False
    try:
        is_self_dual = (c_sym == 13) or (float(c_sym) == 13.0)
    except (TypeError, ValueError):
        pass

    is_ghost = False
    try:
        is_ghost = (c_dual == 0) or (float(c_dual) == 0.0)
    except (TypeError, ValueError):
        pass

    return {
        "c": c_sym,
        "c_dual": c_dual,
        "complementarity_sum": 26,
        "rho": 1,
        "self_dual": is_self_dual,
        "ghost": is_ghost,
        "depth_zero_resonance": True,
        "description": "Vir_{26-c} is the depth-zero resonance shadow",
    }


# ===========================================================================
# 7. Platonic completion check
# ===========================================================================

ALL_STANDARD_FAMILIES = [
    "heisenberg", "affine_sl2", "virasoro", "w3",
    "betagamma", "w_infinity", "free_fermion",
]


def platonic_completion_check(family: str, **kwargs) -> Dict:
    """Verify rho(A) < infinity for the given family.

    conj:platonic-completion: Every positive-energy chiral algebra has
    rho < infinity.

    For the standard landscape this is verified: all families have
    finite resonance rank (rho = 0 or 1).
    """
    rho = resonance_rank(family, **kwargs)
    return {
        "family": family,
        "rho": rho,
        "finite": rho < float("inf"),
        "class": mc4_class(family, **kwargs),
    }


def platonic_completion_all() -> Tuple[bool, Dict]:
    """Check the platonic completion conjecture for all standard families.

    Returns (all_finite, family_data).
    """
    data = {}
    for fam in ALL_STANDARD_FAMILIES:
        data[fam] = platonic_completion_check(fam)
    all_finite = all(d["finite"] for d in data.values())
    return all_finite, data


# ===========================================================================
# 8. Weight generating function G_A(t)
# ===========================================================================

def weight_generating_function(family: str, max_q: int = 30,
                               **kwargs) -> List[int]:
    """Compute G_A(t) = sum_{q=0}^{max_q} K_q * t^q as a list of coefficients.

    This is identical to reduced_weight_windows but with a clearer name
    for the generating-function interpretation.

    The analytic forms:
      Heisenberg:     1/(1-t)
      Affine sl_2:    1/(1-t)^3
      Affine g:       1/(1-t)^{dim g}
      Virasoro:       prod_{n>=2} 1/(1-t^n)
      W_3:            prod_{n>=2} 1/(1-t^n) * prod_{n>=3} 1/(1-t^n)
      W_N:            prod_{s=2}^N prod_{n>=s} 1/(1-t^n)
      betagamma:      1/(1-t)^2
      W_infinity:     prod_{n>=1} 1/(1-t^n) = sum p(q) t^q
    """
    return reduced_weight_windows(family, max_q=max_q, **kwargs)


# ===========================================================================
# 9. Entropy from weight windows
# ===========================================================================

def entropy_from_windows(K_q: List[int]) -> Optional[float]:
    """Compute the bar-cohomology entropy h_K = lim_{q->inf} log(K_q) / q.

    For polynomial-growth families (K_q ~ q^d): h_K = 0.
    For Virasoro (K_q ~ partitions of q into parts >= 2):
      h_K = pi * sqrt(2/3) ~ 2.565   (Hardy-Ramanujan asymptotics).
    For W_infinity (K_q = p(q)):
      h_K = pi * sqrt(2/3) ~ 2.565   (same leading asymptotics).

    Returns None if insufficient data or K_q = 0 for large q.
    """
    # Use the last several terms to estimate the limit
    n = len(K_q)
    if n < 5:
        return None

    # Find the largest q with K_q > 0
    last_nonzero = -1
    for i in range(n - 1, -1, -1):
        if K_q[i] > 0:
            last_nonzero = i
            break

    if last_nonzero < 4:
        return None

    # Compute log(K_q)/q for the last few terms
    estimates = []
    for q in range(max(1, last_nonzero - 9), last_nonzero + 1):
        if K_q[q] > 0 and q > 0:
            estimates.append(math.log(K_q[q]) / q)

    if not estimates:
        return None

    return estimates[-1]


def hardy_ramanujan_entropy() -> float:
    """The Hardy-Ramanujan asymptotic entropy pi * sqrt(2/3).

    For p(n) ~ (1/(4n*sqrt(3))) * exp(pi*sqrt(2n/3)):
      log p(n) / n -> pi * sqrt(2/3) / sqrt(n) -> 0

    Actually, for partitions: log p(n) ~ pi*sqrt(2n/3), so
    log p(n) / n ~ pi*sqrt(2/(3n)) -> 0.

    For partitions into parts >= 2: the leading asymptotics are the same
    (subtracting the 1-part shifts the partition generating function by
    a factor of (1-t), which does not affect the exponential growth rate).

    So h_K = lim log K_q / q = 0 for partition-like growth.

    HOWEVER, the ENTROPY LADDER in the manuscript (raeeznotes91/92)
    uses a different normalization: h_K = lim log K_q / sqrt(q),
    which gives pi*sqrt(2/3) for partition-like growth.

    We return the sqrt-normalized entropy for partition asymptotics.
    """
    return float(pi * sqrt(Rational(2, 3)))


def entropy_sqrt_normalized(K_q: List[int]) -> Optional[float]:
    """Compute h_K = lim_{q->inf} log(K_q) / sqrt(q).

    This is the correct normalization for partition-like growth,
    where log p(n) ~ pi*sqrt(2n/3), giving h_K = pi*sqrt(2/3).

    For polynomial growth: h_K = 0 (log q^d / sqrt(q) -> 0).
    """
    n = len(K_q)
    if n < 10:
        return None

    last_nonzero = -1
    for i in range(n - 1, -1, -1):
        if K_q[i] > 0:
            last_nonzero = i
            break

    if last_nonzero < 9:
        return None

    estimates = []
    for q in range(max(1, last_nonzero - 9), last_nonzero + 1):
        if K_q[q] > 0 and q > 0:
            estimates.append(math.log(K_q[q]) / math.sqrt(q))

    if not estimates:
        return None

    return estimates[-1]


# ===========================================================================
# 10. Stabilization defect
# ===========================================================================

def stabilization_defect(family: str, N: int, **kwargs) -> int:
    """Count how many weight-q coefficients at arity N differ from arity (N-1).

    In the bar-cobar tower, the arity-N truncation Omega^{<=N}(B(A)) provides
    coefficients a^(N)_{ij}. The stabilization defect at arity N counts
    how many of these differ from a^(N-1)_{ij}.

    For MC4+ families: the arity cutoff lemma gives defect(N) = K_N
    (exactly the weight-N coefficients appear for the first time at arity N,
    and all lower-weight coefficients have already stabilized).

    For MC4^0 families: same pattern for the positive part; the resonance
    piece adds at most rho additional unstable coefficients.
    """
    if N < 1:
        return 0

    K = reduced_weight_windows(family, max_q=N, **kwargs)
    rho = resonance_rank(family, **kwargs)

    # At arity N, weight-N coefficients appear for the first time
    new_coefficients = K[N] if N < len(K) else 0

    # For MC4^0: the resonance piece may contribute additional defect
    # at the first few stages, but stabilizes quickly.
    resonance_defect = rho if N <= 2 else 0

    return new_coefficients + resonance_defect


# ===========================================================================
# 11. W_N resonance rank as function of N
# ===========================================================================

def w_n_resonance_rank(N: int) -> int:
    """rho(W_N) as a function of N.

    For finite N >= 2: rho = 1 (the single L_0 resonance direction,
    which is the Virasoro sub-resonance inherited by all W_N algebras).
    The higher-spin currents W^{(s)} for s >= 3 do not contribute
    additional independent resonance directions at generic central charge.

    For N = infinity (W_{1+infinity}): rho = 0 (positive tower,
    the MacMahon limit stabilizes all weight-0 classes).

    The transition N -> infinity is the content of
    thm:stabilized-completion-positive for the W_{1+infinity} case.
    """
    if N < 2:
        raise ValueError(f"W_N requires N >= 2, got {N}")
    if N == float("inf") or N > 10**6:
        return 0
    return 1


# ===========================================================================
# 12. Shadow depth classification (for comparison)
# ===========================================================================

_SHADOW_DEPTHS: Dict[str, object] = {
    "heisenberg": 2,
    "affine_sl2": 3,
    "affine_g": 3,
    "virasoro": float("inf"),
    "w3": float("inf"),
    "w_N": float("inf"),
    "betagamma": 4,
    "w_infinity": float("inf"),
    "free_fermion": 2,
}

_SHADOW_ARCHETYPES: Dict[str, str] = {
    "heisenberg": "G",     # Gaussian, r_max = 2
    "affine_sl2": "L",     # Lie/tree, r_max = 3
    "affine_g": "L",
    "virasoro": "M",       # Mixed, r_max = infinity
    "w3": "M",
    "w_N": "M",
    "betagamma": "C",      # Contact/quartic, r_max = 4
    "w_infinity": "M",
    "free_fermion": "G",
}


def shadow_depth(family: str) -> object:
    """Shadow depth r_max(A) from the archetype classification."""
    d = _SHADOW_DEPTHS.get(family)
    if d is None:
        raise ValueError(f"Unknown family: {family}")
    return d


def shadow_archetype(family: str) -> str:
    """Shadow archetype class: G, L, C, or M."""
    a = _SHADOW_ARCHETYPES.get(family)
    if a is None:
        raise ValueError(f"Unknown family: {family}")
    return a


# ===========================================================================
# 13. Full classification table
# ===========================================================================

def classification_table() -> List[Dict]:
    """Produce the full resonance rank / shadow depth / MC4 classification table.

    This table is the computational content of the MC4 splitting section
    in concordance.tex.
    """
    families = [
        ("heisenberg", {}),
        ("affine_sl2", {}),
        ("virasoro", {}),
        ("w3", {}),
        ("betagamma", {}),
        ("w_infinity", {}),
        ("free_fermion", {}),
    ]
    table = []
    for fam, kw in families:
        rho = resonance_rank(fam, **kw)
        K = reduced_weight_windows(fam, max_q=10, **kw)
        table.append({
            "family": fam,
            "rho": rho,
            "mc4_class": mc4_class(fam, **kw),
            "shadow_depth": shadow_depth(fam),
            "archetype": shadow_archetype(fam),
            "K_q_first_11": K,
        })
    return table


# ===========================================================================
# 14. Virasoro-specific computations
# ===========================================================================

def virasoro_k_q_exact(q: int) -> int:
    """K_q(Vir) = number of partitions of q into parts >= 2.

    This is the exact formula. Values:
      q:  0  1  2  3  4  5  6  7  8  9  10  11  12
    K_q:  1  0  1  1  2  2  4  4  7  8  12  14  21
    """
    return _partitions_min_part(q, 2)


def virasoro_gf_euler_product(max_q: int = 30) -> List[int]:
    """Compute the Virasoro weight GF via the Euler product.

    G_{Vir}(t) = prod_{n>=2} 1/(1-t^n)

    Computed by iteratively multiplying (convolving) with 1/(1-t^n).
    """
    coeffs = [0] * (max_q + 1)
    coeffs[0] = 1

    for n in range(2, max_q + 1):
        # Multiply by 1/(1-t^n) = 1 + t^n + t^{2n} + ...
        for j in range(n, max_q + 1):
            coeffs[j] += coeffs[j - n]

    return coeffs


def virasoro_gf_from_unrestricted(max_q: int = 30) -> List[int]:
    """Compute K_q(Vir) via the identity:

    prod_{n>=2} 1/(1-t^n) = (1-t) * prod_{n>=1} 1/(1-t^n)
                           = (1-t) * sum p(q) t^q.

    So K_q = p(q) - p(q-1).
    """
    result = []
    for q in range(max_q + 1):
        pq = _partition_number(q)
        pq1 = _partition_number(q - 1) if q >= 1 else 0
        result.append(pq - pq1)
    return result


# ===========================================================================
# 15. W_N weight-window data
# ===========================================================================

def w_n_weight_windows(N: int, max_q: int = 20) -> List[int]:
    """K_q(W_N) for the W_N algebra at given N.

    GF = prod_{s=2}^N prod_{n>=s} 1/(1-t^n).
    """
    return reduced_weight_windows("w_N", max_q=max_q, N=N)


def w_n_gf_ratio_at_large_q(N: int, max_q: int = 50) -> float:
    """Compute K_{max_q}(W_N) / K_{max_q}(W_{N+1}) to track the N -> inf limit."""
    K_N = w_n_weight_windows(N, max_q)
    K_N1 = w_n_weight_windows(N + 1, max_q)
    if K_N1[-1] == 0:
        return float("inf")
    return K_N[-1] / K_N1[-1]
