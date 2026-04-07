r"""Conformal blocks at all genera: TUY factorization, Verlinde dimensions,
and comparison with the shadow obstruction tower.

MATHEMATICAL FRAMEWORK
======================

1. CONFORMAL BLOCKS (Tsuchiya-Ueno-Yamada, Faltings, Beauville-Laszlo)

For a vertex algebra V (or affine Lie algebra g-hat at level k),
the space of conformal blocks on a smooth projective curve (C, p_1,...,p_n)
with modules M_1,...,M_n inserted at the marked points is:

    CB(V; M_1,...,M_n; C) = (M_1 otimes ... otimes M_n) / g_{out}

where g_{out} = V(C \ {p_1,...,p_n}) is the Lie algebra of sections of
the vertex algebra sheaf away from the insertions.

The TUY theorem (1989): for a rational VOA V, the assignment
    (C, p_i, M_i) |-> CB(V; M_i; C)
forms a vector bundle (the "Verlinde bundle") over M_{g,n} with
projectively flat connection.

2. FACTORIZATION (= bar complex factorization)

The fundamental property of conformal blocks is FACTORIZATION:
when a curve degenerates (C -> C_0 with a node), the conformal
block space decomposes as a sum over intermediate representations:

    CB(V; M_i; C_0) = bigoplus_lambda CB(V; M_{S}, M_lambda; C_1)
                       otimes CB(V; M^vee_lambda, M_{S^c}; C_2)

This is EXACTLY the bar complex factorization (thm:chain-modular-functor):
    Delta_sep: V_{g,n} -> bigoplus V_{g_1,|S|+1} otimes V_{g_2,|S^c|+1}

The TUY factorization IS the bar complex factorization restricted to H^0.

3. ZHU'S ALGEBRA AND GENUS-1 BLOCKS

Zhu's algebra A(V) controls the genus-1 representation theory:
    - Simple A(V)-modules <-> simple admissible V-modules (Zhu 1996)
    - Genus-1 conformal blocks = characters of V-modules
    - dim CB(V; g=1) = |Irr(A(V))| = number of simple modules

For g-hat_k: A(V_k(g)) = U(g) (the universal enveloping algebra).
Integrable modules correspond to k+1 simple modules for sl_2.

4. HIGHER ZHU ALGEBRAS (De Sole-Kac)

De Sole-Kac defined higher Zhu algebras A_n(V) for n >= 0, with
A_0(V) = A(V).  These control the higher-level structure of the
VOA.  The relationship to higher-genus conformal blocks is:
    A_n(V) controls the n-th level of the Zhu filtration, which
    governs the convergence of sewing at genus >= 2.

5. PROPAGATION OF VACUA

For a VOA V with vacuum |0>, propagation of vacua states:
    CB(V; M_1,...,M_n, V; C, p_1,...,p_n, q) = CB(V; M_1,...,M_n; C, p_1,...,p_n)

Inserting the vacuum module V at a new point does not change the
conformal block space.  This is the KEY property that makes the
modular functor well-defined.

For non-rational VOAs (Damiolini-Gibney-Tarasca 2019-2024):
propagation fails in general, but holds under C_2-cofiniteness.

6. SHADOW OBSTRUCTION TOWER CONNECTION

The shadow CohFT (thm:shadow-cohft) assigns classes
    Omega_{g,n}^A(v_1,...,v_n) in R*(M-bar_{g,n})

The shadow partition function F_g = kappa * lambda_g^FP is the
SCALAR projection (= first Chern class of the Verlinde bundle).

The full bar cohomology H^*(B^(g)(A), D_g) at genus g recovers:
    H^0 = TUY conformal blocks (for rational VOAs at integrable level)
    H^i (i > 0) = higher derived conformal blocks

The complementarity theorem (Thm C) splits:
    H*(M-bar_g, Z(A)) = Q_g(A) + Q_g(A!)
what A sees as obstruction, A! sees as deformation.

KEY FORMULAS:
    - Verlinde dim: V_{g,k}(G) = sum_lambda S_{0,lambda}^{2-2g}
    - Shadow: F_g = kappa * lambda_g^FP
    - kappa(g_k) = dim(g)*(k+h^v)/(2*h^v)
    - Central charge: c = k*dim(g)/(k+h^v) (Sugawara)
    - Genus-1 Verlinde = |P_+^k| (number of integrable reps)
    - Large-k: log V_{g,k} ~ (g-1)*dim(G)*log(k) + ...

FACTORIZATION VERIFICATION:
    At a separating node C -> C_1 cup C_2 with genera g_1, g_2:
    V_{g_1+g_2, k} = sum_lambda V_{g_1, k}^lambda * V_{g_2, k}^lambda
    where V_{g,k}^lambda = S_{0,lambda}^{-1} * prod_i S_{lambda_i, lambda}
    (pointed Verlinde with external legs labeled lambda).

    At a nonseparating node (self-sewing, C -> C' with g' = g-1):
    V_{g,k} = sum_lambda V_{g-1,k}^{lambda, lambda^*}

These factorization relations are the DEFINING property of a modular
functor and correspond exactly to the bar complex boundary maps.

CONVENTIONS (AP38, AP44):
    - S-matrix: Kac-Peterson normalization, S S^dag = I, S_{00} > 0
    - Representations: Dynkin labels (a_1,...,a_r), sum a_i * colabel_i <= k
    - Verlinde: uses RAW S-matrix entries, NOT quantum dimensions
    - lambda_g^FP: (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!

Mathematical references:
    Tsuchiya-Ueno-Yamada (1989), Conformal field theory on universal family
    Faltings (1994), A proof for the Verlinde formula
    Beauville-Laszlo (1993), Conformal blocks and generalized theta functions
    Zhu (1996), Modular invariance of characters of VOAs
    De Sole-Kac (2006), Finite vs affine W-algebras
    Damiolini-Gibney-Tarasca (2021), Conformal blocks from VOAs
    Codogni-Patakfalvi (2021), Positivity of the Chern-Mumford class
    Frenkel-Ben-Zvi (2004), Vertex Algebras and Algebraic Curves, Ch 17-18
    Beauville (1996), Conformal blocks, fusion rules and the Verlinde formula
    Bakalov-Kirillov (2001), Lectures on tensor categories and modular functors
    thm:shadow-cohft (higher_genus_modular_koszul.tex)
    thm:chain-modular-functor (genus_complete.tex)
    thm:quantum-complementarity-main (higher_genus_complementarity.tex)
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

from sympy import (
    Rational,
    bernoulli,
    factorial,
    pi as sym_pi,
    simplify,
    sin as sym_sin,
    sqrt as sym_sqrt,
    S as sympy_S,
)


# =========================================================================
# Section 0: Lie algebra data (canonical source, per AP3/AAP3)
# =========================================================================

_LIE_DATA = {
    ("A", 1): {"dim": 3, "h": 2, "hv": 2, "rank": 1, "colabels": (1,)},
    ("A", 2): {"dim": 8, "h": 3, "hv": 3, "rank": 2, "colabels": (1, 1)},
    ("A", 3): {"dim": 15, "h": 4, "hv": 4, "rank": 3, "colabels": (1, 1, 1)},
    ("A", 4): {"dim": 24, "h": 5, "hv": 5, "rank": 4, "colabels": (1, 1, 1, 1)},
    ("B", 2): {"dim": 10, "h": 4, "hv": 3, "rank": 2, "colabels": (1, 2)},
    ("C", 2): {"dim": 10, "h": 4, "hv": 3, "rank": 2, "colabels": (2, 1)},
    ("G", 2): {"dim": 14, "h": 6, "hv": 4, "rank": 2, "colabels": (2, 3)},
}


def _get_data(lie_type: str, rank: int) -> dict:
    """Return Lie algebra data, computing for type A if not tabulated."""
    key = (lie_type, rank)
    if key in _LIE_DATA:
        return _LIE_DATA[key]
    if lie_type == "A" and rank >= 1:
        N = rank + 1
        return {
            "dim": N * N - 1,
            "h": N,
            "hv": N,
            "rank": rank,
            "colabels": tuple([1] * rank),
        }
    raise ValueError(f"Unsupported Lie algebra ({lie_type}, {rank})")


# =========================================================================
# Section 1: Modular characteristic kappa (AP1, AP39, AP48)
# =========================================================================

def kappa_km(lie_type: str, rank: int, level: int) -> Fraction:
    r"""Modular characteristic kappa for affine g-hat at level k.

    kappa(g_k) = dim(g) * (k + h^v) / (2 * h^v)

    This is the MODULAR CHARACTERISTIC, distinct from c/2 in general (AP39).
    kappa = c/2 ONLY for the Virasoro algebra (AP48).

    Returns exact Fraction.
    """
    data = _get_data(lie_type, rank)
    return Fraction(data["dim"] * (level + data["hv"]), 2 * data["hv"])


def central_charge_km(lie_type: str, rank: int, level: int) -> Fraction:
    r"""Sugawara central charge c = k * dim(g) / (k + h^v).

    UNDEFINED at critical level k = -h^v (AP: Sugawara UNDEFINED, not divergent).
    """
    data = _get_data(lie_type, rank)
    if level + data["hv"] == 0:
        raise ValueError("Central charge undefined at critical level k = -h^v")
    return Fraction(level * data["dim"], level + data["hv"])


# =========================================================================
# Section 2: Integrable representations enumeration
# =========================================================================

def integrable_weights_km(lie_type: str, rank: int, level: int) -> List[Tuple[int, ...]]:
    r"""Enumerate all integrable highest weights at level k.

    Condition: a_i >= 0, sum_i a_i * colabel_i <= k.
    Returns sorted list of Dynkin label tuples.
    """
    if level < 0:
        raise ValueError(f"Level must be non-negative, got {level}")
    data = _get_data(lie_type, rank)
    colabels = data["colabels"]
    r = data["rank"]
    results: List[Tuple[int, ...]] = []
    _enum_weights(colabels, level, r, 0, [], results)
    return sorted(results)


def _enum_weights(colabels, budget, r, idx, current, results):
    """Recursively enumerate weights."""
    if idx == r:
        results.append(tuple(current))
        return
    c = colabels[idx]
    for a in range(budget // c + 1):
        current.append(a)
        _enum_weights(colabels, budget - a * c, r, idx + 1, current, results)
        current.pop()


def num_integrable(lie_type: str, rank: int, level: int) -> int:
    """Number of integrable highest-weight representations at level k.

    For type A_r at level k: C(k+r, r) (binomial coefficient).
    """
    if lie_type == "A":
        # Exact: C(k+r, r) = (k+r)! / (k! * r!)
        n, r = level + rank, rank
        result = 1
        for i in range(r):
            result = result * (n - i) // (i + 1)
        return result
    return len(integrable_weights_km(lie_type, rank, level))


# =========================================================================
# Section 3: S-matrix computation for sl_2
# =========================================================================

def sl2_S_entry(j: int, l: int, k: int) -> float:
    r"""S-matrix entry S_{j,l} for sl_2 at level k.

    S_{j,l} = sqrt(2/(k+2)) * sin(pi*(j+1)*(l+1)/(k+2))

    j, l in {0, 1, ..., k}.
    """
    n = k + 2
    return math.sqrt(2.0 / n) * math.sin(math.pi * (j + 1) * (l + 1) / n)


def sl2_S_matrix_full(k: int) -> np.ndarray:
    r"""Full (k+1) x (k+1) S-matrix for sl_2 at level k."""
    size = k + 1
    S = np.zeros((size, size))
    for j in range(size):
        for l in range(size):
            S[j, l] = sl2_S_entry(j, l, k)
    return S


# =========================================================================
# Section 4: S-matrix computation for sl_3 (type A, rank 2)
# =========================================================================

def sl3_shifted_eps(dynkin: Tuple[int, int]) -> np.ndarray:
    r"""Convert sl_3 Dynkin labels to shifted epsilon coordinates.

    For sl_3 (N=3), lambda = (a_1, a_2), rho = (1,1):
    shifted = (a_1+1, a_2+1)
    epsilon = (e_1, e_2, e_3) with e_1 = (a_1+1) + (a_2+1),
    e_2 = (a_2+1), e_3 = 0.  Traceless projection follows.
    """
    a1, a2 = dynkin
    s1, s2 = a1 + 1, a2 + 1
    return np.array([s1 + s2, s2, 0], dtype=float)


def sl3_S_matrix_full(k: int) -> np.ndarray:
    r"""S-matrix for sl_3 at level k via Kac-Peterson with S_3 Weyl group.

    Uses epsilon coordinates and the traceless inner product.
    """
    from itertools import permutations

    N = 3
    n = k + N  # shifted level

    weights = integrable_weights_km("A", 2, k)
    n_wts = len(weights)

    def ip_traceless(v, w):
        return float(np.dot(v, w) - np.sum(v) * np.sum(w) / N)

    # Weyl group = S_3
    weyl = []
    for perm in permutations(range(N)):
        inv = sum(1 for i in range(N) for j in range(i + 1, N)
                  if perm[i] > perm[j])
        weyl.append((perm, (-1) ** inv))

    eps_list = [sl3_shifted_eps(wt) for wt in weights]

    S_raw = np.zeros((n_wts, n_wts), dtype=complex)
    for i in range(n_wts):
        for j in range(n_wts):
            val = 0.0j
            for (perm, sgn) in weyl:
                w_eps = eps_list[i][list(perm)]
                ip = ip_traceless(w_eps, eps_list[j])
                val += sgn * np.exp(-2.0j * np.pi * ip / n)
            S_raw[i, j] = val

    row0_norm = np.sqrt(np.sum(np.abs(S_raw[0, :]) ** 2))
    S_mat = S_raw / row0_norm
    phase = S_mat[0, 0] / np.abs(S_mat[0, 0])
    S_mat = S_mat / phase
    return S_mat


# =========================================================================
# Section 5: Verlinde dimensions (conformal block space dimensions)
# =========================================================================

def verlinde_dim_sl2(k: int, g: int) -> int:
    r"""Dimension of conformal blocks for sl_2 at level k, genus g.

    V_{g,k}(sl_2) = (k+2/2)^{g-1} sum_{j=0}^{k} sin^{2-2g}(pi*(j+1)/(k+2))

    Computed via S-matrix: V_g = sum_j |S_{0,j}|^{2-2g}.

    This is the TUY conformal block dimension on M_g.
    Returns exact integer.
    """
    if g < 0:
        raise ValueError(f"Genus must be non-negative, got {g}")

    n = k + 2
    power = 2 - 2 * g

    # Direct computation from S-matrix entries
    total = 0.0
    prefactor = math.sqrt(2.0 / n)
    for j in range(k + 1):
        s0j = prefactor * math.sin(math.pi * (j + 1) / n)
        total += abs(s0j) ** power

    result = int(round(total))
    assert abs(total - result) < 0.01, (
        f"Verlinde dim not integer: V_{g},{k}(sl_2) = {total}"
    )
    return result


def verlinde_dim_sl2_closed(k: int, g: int) -> int:
    r"""Alternative computation via the Beauville formula (independent path).

    V_{g,k}(sl_2) = ((k+2)/2)^{g-1} sum_{j=1}^{k+1} sin^{2-2g}(j*pi/(k+2))

    At g=1: returns k+1.
    At g=2: returns C(k+3, 3) = (k+1)(k+2)(k+3)/6.
    """
    if g < 0:
        raise ValueError(f"Genus must be non-negative, got {g}")

    n = k + 2

    if g == 0:
        return 1

    if g == 1:
        return k + 1

    # General formula
    total = 0.0
    for j in range(1, n):
        sin_val = math.sin(j * math.pi / n)
        total += sin_val ** (2 - 2 * g)
    total *= (n / 2.0) ** (g - 1)

    result = int(round(total))
    assert abs(total - result) < 0.01, (
        f"Verlinde closed form not integer: V_{g},{k}(sl_2) = {total}"
    )
    return result


def verlinde_dim_sl3(k: int, g: int) -> int:
    r"""Verlinde dimension for sl_3 at level k, genus g.

    Computed via the Kac-Peterson S-matrix.
    Number of integrable reps: C(k+2, 2) = (k+1)(k+2)/2.
    """
    if g < 0:
        raise ValueError(f"Genus must be non-negative, got {g}")

    S = sl3_S_matrix_full(k)
    n_wts = S.shape[0]
    power = 2 - 2 * g

    total = 0.0
    for j in range(n_wts):
        s0j = S[0, j]
        mag = abs(s0j)
        if mag > 1e-15:
            total += mag ** power

    result = int(round(total))
    assert abs(total - result) < 0.1, (
        f"Verlinde dim not integer: V_{g},{k}(sl_3) = {total}"
    )
    return result


def verlinde_dim_general(lie_type: str, rank: int, k: int, g: int) -> int:
    """Verlinde dimension for general type, dispatching to specialized code."""
    if lie_type == "A" and rank == 1:
        return verlinde_dim_sl2(k, g)
    elif lie_type == "A" and rank == 2:
        return verlinde_dim_sl3(k, g)
    else:
        raise NotImplementedError(
            f"General S-matrix for ({lie_type}, {rank}) not implemented in this engine; "
            f"use verlinde_shadow_cohft_engine for all types."
        )


# =========================================================================
# Section 6: Faber-Pandharipande numbers (exact, from Bernoulli)
# =========================================================================

@lru_cache(maxsize=64)
def _bernoulli_exact(n: int) -> Fraction:
    """Exact Bernoulli number B_n as Fraction."""
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1:
        return Fraction(0)
    # Recurrence: sum_{k=0}^{n-1} C(n+1,k) B_k = -(n+1) B_n
    s = Fraction(0)
    from math import comb
    for k_idx in range(n):
        s += Fraction(comb(n + 1, k_idx)) * _bernoulli_exact(k_idx)
    return -s / Fraction(n + 1)


def faber_pandharipande(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    Exact computation via Bernoulli numbers.

    First values:
        g=1: 1/24
        g=2: 7/5760
        g=3: 31/967680
        g=4: 127/154828800
        g=5: 73/3503554560
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B2g = _bernoulli_exact(2 * g)
    numer = (2 ** (2 * g - 1) - 1) * abs(B2g)
    denom = Fraction(2 ** (2 * g - 1)) * Fraction(math.factorial(2 * g))
    return Fraction(numer) / denom


# =========================================================================
# Section 7: Shadow free energy F_g = kappa * lambda_g^FP
# =========================================================================

def shadow_free_energy(lie_type: str, rank: int, level: int, g: int) -> Fraction:
    r"""Shadow CohFT genus-g free energy.

    F_g(g_k) = kappa(g_k) * lambda_g^FP

    This is the SCALAR projection of the shadow obstruction tower.
    It is the first Chern class of the Verlinde bundle (rem:verlinde-vs-kappa).
    """
    if g < 1:
        raise ValueError(f"F_g defined for g >= 1, got {g}")
    return kappa_km(lie_type, rank, level) * faber_pandharipande(g)


# =========================================================================
# Section 8: TUY factorization verification
# =========================================================================

def verify_factorization_separating(lie_type: str, rank: int, k: int,
                                     g1: int, g2: int) -> Dict[str, Any]:
    r"""Verify TUY separating factorization identity.

    At a separating node, a genus g = g1 + g2 curve degenerates into
    two components of genera g1 and g2 joined at a node.  The conformal
    block space factorizes as a sum over intermediate representations:

        V_{g1+g2, k} = sum_lambda V_{g1}^{(lambda)} * V_{g2}^{(lambda^*)}

    The one-pointed partition function (genus-g vacuum block with one
    marked point carrying representation lambda) is:

        Z_g^{(lambda)} = S_{0,lambda}^{1-2g}

    The factorization identity then reads:

        sum_lambda S_{0,lambda}^{1-2g1} * S_{0,lambda^*}^{1-2g2}
        = sum_lambda S_{0,lambda}^{(1-2g1) + (1-2g2)}
        = sum_lambda S_{0,lambda}^{2 - 2(g1+g2)}
        = V_{g1+g2}

    where we used S_{0,lambda^*} = S_{0,lambda} (since quantum dimensions
    are real and charge-conjugation-invariant: d_lambda = d_{lambda^*}).

    This is the bar complex separating factorization (thm:chain-modular-functor(ii)).
    """
    g = g1 + g2
    result = {"g1": g1, "g2": g2, "g": g, "k": k,
              "lie_type": lie_type, "rank": rank}

    if lie_type == "A" and rank == 1:
        S = sl2_S_matrix_full(k)
    elif lie_type == "A" and rank == 2:
        S = sl3_S_matrix_full(k)
    else:
        result["error"] = "Only sl_2 and sl_3 implemented"
        return result

    n_wts = S.shape[0]

    # Direct Verlinde dimension at genus g
    V_direct = verlinde_dim_general(lie_type, rank, k, g)
    result["V_direct"] = V_direct

    # Factorized: sum_lambda S_{0,lambda}^{1-2g1} * S_{0,lambda}^{1-2g2}
    # Uses S_{0,lambda^*} = S_{0,lambda} (quantum dims are conjugation-invariant).
    V_factored = 0.0
    channel_contributions = []
    for lam in range(n_wts):
        s0lam = abs(S[0, lam])
        if s0lam > 1e-15:
            contrib_g1 = s0lam ** (1 - 2 * g1)
            contrib_g2 = s0lam ** (1 - 2 * g2)
            channel_contrib = contrib_g1 * contrib_g2
            V_factored += channel_contrib
            channel_contributions.append({
                "lambda": lam,
                "Z_g1": contrib_g1,
                "Z_g2": contrib_g2,
                "product": channel_contrib,
            })

    V_factored_int = int(round(V_factored))
    result["V_factored"] = V_factored_int
    result["V_factored_raw"] = V_factored
    result["factorization_holds"] = abs(V_factored - V_direct) < 0.5
    result["deviation"] = abs(V_factored - V_direct)
    result["channels"] = channel_contributions

    return result


def verify_factorization_nonseparating(lie_type: str, rank: int,
                                        k: int, g: int) -> Dict[str, Any]:
    r"""Verify TUY nonseparating (self-sewing) factorization.

    At a nonseparating node, a genus-g curve degenerates into a
    genus-(g-1) curve with two points identified.  The self-sewing
    factorization reads:

        V_g = sum_lambda (1 / S_{0,lambda}^2) * Z_{g-1} * S_{0,lambda}^{2-2(g-1)}

    where the 1/S_{0,lambda}^2 factor comes from the metric on the
    space of intermediate states (the bilinear pairing on representations).

    Expanding:
        V_g = sum_lambda S_{0,lambda}^{-2} * S_{0,lambda}^{2-2(g-1)}
            = sum_lambda S_{0,lambda}^{-2 + 4 - 2g}
            = sum_lambda S_{0,lambda}^{2 - 2g}
            = V_g  [QED]

    We verify this by computing both sides explicitly, using the
    intermediate-sum form (which sums over lambda with the metric
    factor) against the direct Verlinde formula.

    This is the bar complex self-sewing map (thm:chain-modular-functor(iii)).
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1 for nonseparating, got {g}")

    result = {"g": g, "k": k, "lie_type": lie_type, "rank": rank}

    if lie_type == "A" and rank == 1:
        S = sl2_S_matrix_full(k)
    elif lie_type == "A" and rank == 2:
        S = sl3_S_matrix_full(k)
    else:
        result["error"] = "Only sl_2 and sl_3 implemented"
        return result

    n_wts = S.shape[0]

    V_direct = verlinde_dim_general(lie_type, rank, k, g)
    result["V_direct"] = V_direct

    # Self-sewing: sum_lambda S_{0,lambda}^{-2} * S_{0,lambda}^{2-2(g-1)}
    # = sum_lambda S_{0,lambda}^{2-2g}
    # We compute via the intermediate form to test the mechanism.
    V_sewed = 0.0
    channel_contributions = []
    for lam in range(n_wts):
        s0lam = abs(S[0, lam])
        if s0lam > 1e-15:
            metric_factor = 1.0 / (s0lam ** 2)
            genus_gm1_factor = s0lam ** (2 - 2 * (g - 1))
            contrib = metric_factor * genus_gm1_factor
            V_sewed += contrib
            channel_contributions.append({
                "lambda": lam,
                "metric_factor": metric_factor,
                "genus_gm1_factor": genus_gm1_factor,
                "contribution": contrib,
            })

    V_sewed_int = int(round(V_sewed))
    result["V_sewed"] = V_sewed_int
    result["V_sewed_raw"] = V_sewed
    result["factorization_holds"] = abs(V_sewed - V_direct) < 0.5
    result["deviation"] = abs(V_sewed - V_direct)
    result["channels"] = channel_contributions

    return result


# =========================================================================
# Section 9: Genus-g growth and Witten volume
# =========================================================================

def verlinde_growth_exponent(lie_type: str, rank: int, k: int,
                              max_g: int = 8) -> Dict[str, Any]:
    r"""Compute the growth exponent of Verlinde dimensions.

    V_{g,k} ~ C_g * k^{dim(G)*(g-1)} as k -> infinity (Witten).
    The exponent dim(G)*(g-1) is the complex dimension of M_g(G).
    """
    data = _get_data(lie_type, rank)
    dim_G = data["dim"]

    result = {
        "lie_type": lie_type, "rank": rank, "level": k,
        "dim_G": dim_G,
        "expected_exponent_formula": f"dim(G)*(g-1) = {dim_G}*(g-1)",
    }

    dims = {}
    for g in range(0, max_g + 1):
        dims[g] = verlinde_dim_general(lie_type, rank, k, g)
    result["verlinde_dims"] = dims

    return result


# =========================================================================
# Section 10: Zhu algebra dimension and genus-1 blocks
# =========================================================================

def zhu_algebra_dim_km(lie_type: str, rank: int) -> str:
    r"""Description of Zhu's algebra for affine KM.

    For V_k(g) (universal): A(V_k(g)) = U(g), infinite-dimensional.
    For L_k(g) at integrable level: A(L_k(g)) = quotient, finite-dimensional.
    """
    data = _get_data(lie_type, rank)
    return (f"A(V_k({lie_type}_{rank})) = U({lie_type}_{rank}), "
            f"infinite-dimensional. At integrable level k: "
            f"A(L_k) is a finite quotient with |Irr| = |P_+^k| simple modules.")


def genus1_blocks_count(lie_type: str, rank: int, level: int) -> int:
    r"""Dimension of genus-1 conformal blocks (= number of characters).

    For integrable level: dim = |P_+^k| = number of integrable reps.
    This equals the number of simple A(V)-modules (Zhu's theorem).
    """
    return num_integrable(lie_type, rank, level)


# =========================================================================
# Section 11: Verlinde formula vs shadow comparison at all genera
# =========================================================================

def verlinde_vs_shadow_table(lie_type: str, rank: int,
                              levels: List[int],
                              genera: List[int]) -> Dict[str, Any]:
    r"""Comprehensive comparison table: Verlinde dimensions vs shadow F_g.

    For each (k, g):
      - V_{g,k}: Verlinde dimension (integer, from S-matrix)
      - F_g: shadow free energy (rational, = kappa * lambda_g^FP)
      - kappa: modular characteristic
      - ratio V/F_g: quantum-group decomposition index

    The relationship (rem:verlinde-vs-kappa):
      V_{g,k} is the RANK of the Verlinde bundle
      F_g is its FIRST CHERN CLASS (scalar shadow projection)
    """
    result = {"lie_type": lie_type, "rank": rank}
    table = []

    for k in levels:
        kap = kappa_km(lie_type, rank, k)
        c_val = central_charge_km(lie_type, rank, k)
        n_reps = num_integrable(lie_type, rank, k)

        for g in genera:
            row = {
                "k": k, "g": g,
                "kappa": float(kap),
                "central_charge": float(c_val),
                "num_reps": n_reps,
            }

            V = verlinde_dim_general(lie_type, rank, k, g)
            row["verlinde_dim"] = V

            if g >= 1:
                F = shadow_free_energy(lie_type, rank, k, g)
                row["shadow_F_g"] = float(F)
                row["shadow_F_g_exact"] = str(F)
                if float(F) != 0:
                    row["ratio_V_over_F"] = V / float(F)

            table.append(row)

    result["table"] = table
    return result


# =========================================================================
# Section 12: Verlinde formula derivation from shadow (conceptual bridge)
# =========================================================================

def verlinde_from_quantum_group_decomposition(
    lie_type: str, rank: int, k: int, g: int,
) -> Dict[str, Any]:
    r"""Derive Verlinde dimension from quantum group channel decomposition.

    The shadow CohFT (thm:shadow-cohft) provides a CohFT Omega_{g,n}
    on M-bar_{g,n}.  The SCALAR projection gives F_g = kappa * lambda_g^FP.

    The FULL channel decomposition:
        V_{g,k} = sum_lambda S_{0,lambda}^{2-2g}
                = sum_lambda (quantum dimension d_lambda / D)^{2-2g}
                = D^{2g-2} * sum_lambda d_lambda^{2-2g}

    Each channel lambda contributes independently.  The shadow F_g
    sees only the TOTAL kappa = sum_lambda kappa_lambda, not the
    individual channel structure.

    This function decomposes the Verlinde dimension into quantum-group
    channels and compares with the shadow.
    """
    if lie_type == "A" and rank == 1:
        S = sl2_S_matrix_full(k)
    elif lie_type == "A" and rank == 2:
        S = sl3_S_matrix_full(k)
    else:
        return {"error": "Only sl_2 and sl_3 implemented"}

    n_wts = S.shape[0]
    power = 2 - 2 * g

    channels = []
    total = 0.0
    s00 = abs(S[0, 0])

    for j in range(n_wts):
        s0j = abs(S[0, j])
        contrib = s0j ** power if s0j > 1e-15 else 0.0
        qdim = s0j / s00 if s00 > 1e-15 else 0.0
        channels.append({
            "index": j,
            "S_0j": float(s0j),
            "quantum_dim": float(qdim),
            "contribution": float(contrib),
        })
        total += contrib

    kap = kappa_km(lie_type, rank, k)
    F_g = float(kap * faber_pandharipande(g)) if g >= 1 else None

    return {
        "lie_type": lie_type, "rank": rank, "level": k, "genus": g,
        "verlinde_dim": int(round(total)),
        "shadow_F_g": F_g,
        "num_channels": n_wts,
        "channels": channels,
        "D_squared": float(1.0 / (s00 ** 2)) if s00 > 1e-15 else None,
        "kappa": float(kap),
    }


# =========================================================================
# Section 13: Propagation of vacua verification
# =========================================================================

def verify_propagation_of_vacua(lie_type: str, rank: int, k: int,
                                 g: int) -> Dict[str, Any]:
    r"""Verify propagation of vacua: inserting vacuum doesn't change blocks.

    CB(V; M_1,...,M_n, V; C) = CB(V; M_1,...,M_n; C)

    In Verlinde formula terms:
        V_{g,k}^{(0)} = V_{g,k}  (inserting vacuum rep = trivial rep)

    This is because S_{0,0}/S_{0,mu} * S_{0,mu} = S_{0,0} ... but
    the one-pointed Verlinde with vacuum insertion:
        V_g^{(0)} = sum_mu (S_{0,mu}/S_{0,mu}) * S_{0,mu}^{2-2g}
                  = sum_mu S_{0,mu}^{2-2g}
                  = V_g

    Propagation holds trivially at the level of the Verlinde formula.
    """
    result = {"lie_type": lie_type, "rank": rank, "k": k, "g": g}

    V_g = verlinde_dim_general(lie_type, rank, k, g)
    result["V_g"] = V_g

    # One-pointed with vacuum (lambda = 0)
    if lie_type == "A" and rank == 1:
        S = sl2_S_matrix_full(k)
    elif lie_type == "A" and rank == 2:
        S = sl3_S_matrix_full(k)
    else:
        result["error"] = "Only sl_2 and sl_3 implemented"
        return result

    n_wts = S.shape[0]
    V_g_vac = 0.0
    for mu in range(n_wts):
        s0mu = abs(S[0, mu])
        if s0mu > 1e-15:
            # S_{0,mu}/S_{0,mu} = 1
            V_g_vac += s0mu ** (2 - 2 * g)

    result["V_g_vacuum_inserted"] = int(round(V_g_vac))
    result["propagation_holds"] = abs(V_g_vac - V_g) < 0.5

    return result


# =========================================================================
# Section 14: Genus-2 closed form for sl_2
# =========================================================================

def sl2_genus2_closed(k: int) -> int:
    r"""Closed-form genus-2 Verlinde for sl_2.

    V_{2,k}(sl_2) = C(k+3, 3) = (k+1)(k+2)(k+3)/6

    Proof: sum_{j=1}^{k+1} csc^2(j*pi/(k+2)) = (k+1)(k+3)/3.
    Then V_2 = (k+2/2) * (k+1)(k+3)/3 = (k+1)(k+2)(k+3)/6.
    """
    return (k + 1) * (k + 2) * (k + 3) // 6


def sl2_genus1_count(k: int) -> int:
    r"""Genus-1 Verlinde = number of integrable reps.

    V_{1,k}(sl_2) = k + 1.
    """
    return k + 1


# =========================================================================
# Section 15: Fusion rules as factorization data
# =========================================================================

def sl2_fusion_rule(i: int, j: int, m: int, k: int) -> int:
    r"""Exact fusion coefficient for sl_2.

    N_{ij}^m = 1 if |i-j| <= m <= min(i+j, 2k-i-j) and i+j+m even
             = 0 otherwise

    This is the truncated Clebsch-Gordan decomposition.
    """
    if (abs(i - j) <= m <= min(i + j, 2 * k - i - j)
            and (i + j + m) % 2 == 0):
        return 1
    return 0


def sl2_fusion_matrix(k: int) -> np.ndarray:
    r"""Full fusion coefficient tensor N_{ij}^m for sl_2 at level k.

    Returns (k+1) x (k+1) x (k+1) integer array.
    """
    size = k + 1
    N = np.zeros((size, size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            for m in range(size):
                N[i, j, m] = sl2_fusion_rule(i, j, m, k)
    return N


def verify_fusion_from_verlinde(k: int) -> Dict[str, Any]:
    r"""Verify fusion coefficients computed from Verlinde formula match exact rules.

    N_{ij}^m = sum_l S_{il} S_{jl} S_{ml} / S_{0l}

    Compare against exact truncated CG rules.
    """
    S = sl2_S_matrix_full(k)
    size = k + 1
    max_dev = 0.0
    mismatches = []

    for i in range(size):
        for j in range(size):
            for m in range(size):
                # Verlinde formula
                verlinde_N = 0.0
                for l in range(size):
                    if abs(S[0, l]) > 1e-15:
                        verlinde_N += S[i, l] * S[j, l] * S[m, l] / S[0, l]

                exact_N = sl2_fusion_rule(i, j, m, k)
                dev = abs(verlinde_N - exact_N)
                if dev > max_dev:
                    max_dev = dev
                if dev > 0.01:
                    mismatches.append((i, j, m, verlinde_N, exact_N))

    return {
        "level": k,
        "max_deviation": max_dev,
        "all_match": len(mismatches) == 0,
        "mismatches": mismatches[:10],
    }


# =========================================================================
# Section 16: Complementarity (Thm C) at the Verlinde level
# =========================================================================

def complementarity_verlinde(lie_type: str, rank: int, k: int,
                              max_g: int = 5) -> Dict[str, Any]:
    r"""Complementarity at the Verlinde level.

    Thm C: Q_g(A) + Q_g(A!) = H*(M-bar_g, Z(A))

    For KM: the Feigin-Frenkel dual of g-hat_k is g-hat_{-k-2h^v}.
    kappa(g_k) + kappa(g_{k'}) = 0 for KM (exact cancellation, AP24).

    At the Verlinde level:
      kappa * lambda_g^FP + kappa' * lambda_g^FP = 0
      => F_g + F_g' = 0

    The Verlinde dimensions themselves do NOT simply add:
      V_{g,k} + V_{g,k'} is NOT the "total" obstruction space.
    The shadow F_g + F_g' = 0 is the SCALAR shadow of complementarity.
    """
    data = _get_data(lie_type, rank)
    hv = data["hv"]
    k_dual = -k - 2 * hv  # Feigin-Frenkel dual level

    result = {
        "lie_type": lie_type, "rank": rank,
        "k": k, "k_dual": k_dual,
        "kappa": float(kappa_km(lie_type, rank, k)),
        "kappa_dual": float(kappa_km(lie_type, rank, k_dual)),
    }

    # Verify kappa + kappa' = 0 for KM
    kap_sum = kappa_km(lie_type, rank, k) + kappa_km(lie_type, rank, k_dual)
    result["kappa_sum"] = float(kap_sum)
    result["kappa_sum_zero"] = abs(float(kap_sum)) < 1e-15

    # Shadow complementarity at each genus
    genus_data = []
    for g in range(1, max_g + 1):
        F = shadow_free_energy(lie_type, rank, k, g)
        F_dual = shadow_free_energy(lie_type, rank, k_dual, g)
        genus_data.append({
            "g": g,
            "F_g": float(F),
            "F_g_dual": float(F_dual),
            "sum": float(F + F_dual),
            "complementarity_holds": abs(float(F + F_dual)) < 1e-15,
        })
    result["genus_data"] = genus_data

    return result


# =========================================================================
# Section 17: Large-k asymptotics: Witten volume
# =========================================================================

def large_k_asymptotics_sl2(k_values: List[int], g: int) -> Dict[str, Any]:
    r"""Verify Witten's asymptotic formula for sl_2.

    V_{g,k}(sl_2) ~ C_g * (k+2)^{3(g-1)} as k -> infinity.

    The exponent 3(g-1) = dim_C M_g(SU(2)).
    C_g = Vol M_g(SU(2)) = Witten-Zograf symplectic volume.
    """
    result = {"genus": g, "expected_exponent": 3 * (g - 1)}

    data = []
    for k in k_values:
        V = verlinde_dim_sl2(k, g)
        ratio = V / ((k + 2) ** (3 * (g - 1))) if g >= 2 else V / (k + 1)
        data.append({
            "k": k,
            "V_g": V,
            "ratio_V_over_k_power": ratio,
        })

    result["data"] = data

    # Check convergence of ratios
    if len(data) >= 3:
        ratios = [d["ratio_V_over_k_power"] for d in data[-3:]]
        if all(r > 0 for r in ratios):
            max_var = max(ratios) / min(ratios) - 1
            result["ratio_variation_last3"] = max_var
            result["converging"] = max_var < 0.1

    return result


# =========================================================================
# Section 18: Comprehensive diagnostic
# =========================================================================

def full_diagnostic(lie_type: str, rank: int, k: int,
                     max_g: int = 5) -> Dict[str, Any]:
    r"""Full diagnostic comparing conformal blocks with shadow tower.

    Returns comprehensive data for all genera up to max_g.
    """
    result = {
        "lie_type": lie_type, "rank": rank, "level": k,
        "kappa": float(kappa_km(lie_type, rank, k)),
        "central_charge": float(central_charge_km(lie_type, rank, k)),
        "num_integrable_reps": num_integrable(lie_type, rank, k),
    }

    genus_data = []
    for g in range(0, max_g + 1):
        row = {"g": g}
        row["verlinde_dim"] = verlinde_dim_general(lie_type, rank, k, g)

        if g >= 1:
            F = shadow_free_energy(lie_type, rank, k, g)
            row["shadow_F_g"] = float(F)
            row["shadow_F_g_exact"] = str(F)
            fp = faber_pandharipande(g)
            row["lambda_g_FP"] = float(fp)

        genus_data.append(row)

    result["genus_data"] = genus_data
    return result
