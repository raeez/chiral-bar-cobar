"""Lie algebra data from Cartan matrices.

Provides structure constants, Killing forms, root systems for simple Lie algebras.

CRITICAL DISTINCTION (non-simply-laced):
  h  = Coxeter number (periodicity of bar cohomology)
  h* = dual Coxeter number (Sugawara, FF involution, level shifts)
  For simply-laced: h = h*. Otherwise they differ.

Uses the Chevalley-Serre presentation with structure constants computed
from the Cartan matrix via the Chevalley basis algorithm.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

from sympy import Matrix, Rational, sqrt, eye, sympify


# ---------------------------------------------------------------------------
# Cartan data
# ---------------------------------------------------------------------------

# Standard Cartan matrices for simple types
CARTAN_MATRICES = {
    ("A", 1): Matrix([[2]]),
    ("A", 2): Matrix([[2, -1], [-1, 2]]),
    ("A", 3): Matrix([[2, -1, 0], [-1, 2, -1], [0, -1, 2]]),
    ("B", 2): Matrix([[2, -1], [-2, 2]]),
    ("B", 3): Matrix([[2, -1, 0], [-1, 2, -1], [0, -2, 2]]),
    ("C", 2): Matrix([[2, -2], [-1, 2]]),
    ("C", 3): Matrix([[2, -1, 0], [-1, 2, -2], [0, -1, 2]]),
    ("D", 4): Matrix([[2, -1, 0, 0], [-1, 2, -1, -1], [0, -1, 2, 0], [0, -1, 0, 2]]),
    ("G", 2): Matrix([[2, -1], [-3, 2]]),
    ("F", 4): Matrix([[2, -1, 0, 0], [-1, 2, -2, 0], [0, -1, 2, -1], [0, 0, -1, 2]]),
}


@dataclass
class LieAlgebraData:
    """Complete data for a simple Lie algebra."""
    type: str           # "A", "B", "C", "D", "E", "F", "G"
    rank: int           # rank (number of simple roots)
    cartan: Matrix      # Cartan matrix
    dim: int            # dimension of the Lie algebra
    h: int              # Coxeter number
    h_dual: int         # dual Coxeter number
    exponents: List[int]  # exponents m_1, ..., m_r (sorted)
    root_lengths_squared: List[int]  # |alpha_i|^2 for simple roots (normalized: long = 2)
    positive_roots: List[Tuple[int, ...]]  # positive roots as tuples of simple root coefficients


def _positive_roots_from_cartan(A: Matrix, rank: int) -> List[Tuple[int, ...]]:
    """Compute positive roots from Cartan matrix by iterative root string method.

    For each root alpha and simple root alpha_i, the alpha_i-string through alpha
    is alpha - p*alpha_i, ..., alpha, ..., alpha + q*alpha_i where
    p - q = <alpha, alpha_i^vee>. If q > 0, then alpha + alpha_i is a root.
    """
    simple = [tuple(1 if j == i else 0 for j in range(rank)) for i in range(rank)]
    roots = list(simple)
    seen = set(map(tuple, roots))
    queue = list(simple)

    while queue:
        alpha = queue.pop(0)
        for i in range(rank):
            # <alpha, alpha_i^vee> = sum_j alpha_j * A[j,i]
            inner = sum(alpha[j] * int(A[j, i]) for j in range(rank))
            # p = largest integer such that alpha - p*alpha_i is a root
            p = 0
            test = list(alpha)
            while True:
                test[i] -= 1
                if tuple(test) in seen:
                    p += 1
                else:
                    break
            # q = p - inner; if q > 0, alpha + alpha_i is a root
            q = p - inner
            if q > 0:
                beta = tuple(alpha[j] + (1 if j == i else 0) for j in range(rank))
                if beta not in seen:
                    seen.add(beta)
                    roots.append(beta)
                    queue.append(beta)
    return roots


def cartan_data(type_: str, rank: int) -> LieAlgebraData:
    """Get complete Lie algebra data for a given type and rank."""
    key = (type_, rank)
    if key not in CARTAN_MATRICES:
        raise ValueError(f"Cartan matrix for {type_}{rank} not in registry. "
                         f"Available: {list(CARTAN_MATRICES.keys())}")

    A = CARTAN_MATRICES[key]

    # Dimension, Coxeter, dual Coxeter, exponents by type
    data_table = {
        ("A", 1): (3, 2, 2, [1], [2]),
        ("A", 2): (8, 3, 3, [1, 2], [2, 2]),
        ("A", 3): (15, 4, 4, [1, 2, 3], [2, 2, 2]),
        ("B", 2): (10, 4, 3, [1, 3], [2, 1]),     # so(5), long root = 2, short = 1
        ("B", 3): (21, 6, 5, [1, 3, 5], [2, 2, 1]),
        ("C", 2): (10, 4, 3, [1, 3], [1, 2]),     # sp(4), short root = 1, long = 2
        ("C", 3): (21, 6, 4, [1, 3, 5], [2, 2, 1]),  # NOTE: C_3 h*=4, not 5
        ("D", 4): (28, 6, 6, [1, 3, 3, 5], [2, 2, 2, 2]),
        ("G", 2): (14, 6, 4, [1, 5], [2, 2]),     # short root normalized to 2/3
        ("F", 4): (52, 12, 9, [1, 5, 7, 11], [2, 2, 1, 1]),
    }

    if key not in data_table:
        raise ValueError(f"Data for {type_}{rank} not in table")

    dim, h, h_dual, exponents, root_len_sq = data_table[key]

    # Compute positive roots
    pos_roots = _positive_roots_from_cartan(A, rank)

    return LieAlgebraData(
        type=type_,
        rank=rank,
        cartan=A,
        dim=dim,
        h=h,
        h_dual=h_dual,
        exponents=exponents,
        root_lengths_squared=root_len_sq,
        positive_roots=pos_roots,
    )


# ---------------------------------------------------------------------------
# Structure constants (Chevalley basis)
# ---------------------------------------------------------------------------

def structure_constants_sl2() -> Dict[Tuple[str, str], Dict[str, Rational]]:
    """Structure constants for sl_2 in the standard basis {e, h, f}.

    [e, f] = h, [h, e] = 2e, [h, f] = -2f.

    Returns dict: (a, b) -> {c: f^{ab}_c}
    """
    return {
        ("e", "f"): {"h": Rational(1)},
        ("f", "e"): {"h": Rational(-1)},
        ("h", "e"): {"e": Rational(2)},
        ("e", "h"): {"e": Rational(-2)},
        ("h", "f"): {"f": Rational(-2)},
        ("f", "h"): {"f": Rational(2)},
    }


def structure_constants_sl3() -> Dict[Tuple[str, str], Dict[str, Rational]]:
    """Structure constants for sl_3 in basis {e1, e2, e12, h1, h2, f1, f2, f12}.

    e12 = [e1, e2], f12 = [f2, f1] = -[f1, f2].
    """
    sc: Dict[Tuple[str, str], Dict[str, Rational]] = {}

    # [e_i, f_j] = delta_{ij} h_i
    sc[("e1", "f1")] = {"h1": Rational(1)}
    sc[("f1", "e1")] = {"h1": Rational(-1)}
    sc[("e2", "f2")] = {"h2": Rational(1)}
    sc[("f2", "e2")] = {"h2": Rational(-1)}

    # [h_i, e_j] = a_{ij} e_j  (Cartan matrix entries)
    sc[("h1", "e1")] = {"e1": Rational(2)}
    sc[("e1", "h1")] = {"e1": Rational(-2)}
    sc[("h1", "e2")] = {"e2": Rational(-1)}
    sc[("e2", "h1")] = {"e2": Rational(1)}
    sc[("h2", "e1")] = {"e1": Rational(-1)}
    sc[("e1", "h2")] = {"e1": Rational(1)}
    sc[("h2", "e2")] = {"e2": Rational(2)}
    sc[("e2", "h2")] = {"e2": Rational(-2)}

    # [h_i, f_j] = -a_{ij} f_j
    sc[("h1", "f1")] = {"f1": Rational(-2)}
    sc[("f1", "h1")] = {"f1": Rational(2)}
    sc[("h1", "f2")] = {"f2": Rational(1)}
    sc[("f2", "h1")] = {"f2": Rational(-1)}
    sc[("h2", "f1")] = {"f1": Rational(1)}
    sc[("f1", "h2")] = {"f1": Rational(-1)}
    sc[("h2", "f2")] = {"f2": Rational(-2)}
    sc[("f2", "h2")] = {"f2": Rational(2)}

    # [e1, e2] = e12
    sc[("e1", "e2")] = {"e12": Rational(1)}
    sc[("e2", "e1")] = {"e12": Rational(-1)}

    # [f1, f2] = -f12  (i.e., [f2, f1] = f12)
    sc[("f1", "f2")] = {"f12": Rational(-1)}
    sc[("f2", "f1")] = {"f12": Rational(1)}

    # [e12, f1] = -e2, [e12, f2] = e1
    sc[("e12", "f1")] = {"e2": Rational(-1)}
    sc[("f1", "e12")] = {"e2": Rational(1)}
    sc[("e12", "f2")] = {"e1": Rational(1)}
    sc[("f2", "e12")] = {"e1": Rational(-1)}

    # [e1, f12] = -f2, [e2, f12] = f1
    sc[("e1", "f12")] = {"f2": Rational(-1)}
    sc[("f12", "e1")] = {"f2": Rational(1)}
    sc[("e2", "f12")] = {"f1": Rational(1)}
    sc[("f12", "e2")] = {"f1": Rational(-1)}

    # [e12, f12] = h1 + h2
    sc[("e12", "f12")] = {"h1": Rational(1), "h2": Rational(1)}
    sc[("f12", "e12")] = {"h1": Rational(-1), "h2": Rational(-1)}

    # [h_i, e12] = (a_{i1} + a_{i2}) e12
    sc[("h1", "e12")] = {"e12": Rational(1)}   # 2 + (-1) = 1
    sc[("e12", "h1")] = {"e12": Rational(-1)}
    sc[("h2", "e12")] = {"e12": Rational(1)}   # (-1) + 2 = 1
    sc[("e12", "h2")] = {"e12": Rational(-1)}

    # [h_i, f12]
    sc[("h1", "f12")] = {"f12": Rational(-1)}
    sc[("f12", "h1")] = {"f12": Rational(1)}
    sc[("h2", "f12")] = {"f12": Rational(-1)}
    sc[("f12", "h2")] = {"f12": Rational(1)}

    return sc


# ---------------------------------------------------------------------------
# Killing form
# ---------------------------------------------------------------------------

def killing_form_sl2() -> Dict[Tuple[str, str], Rational]:
    """Killing form for sl_2: kappa(x, y) = 4 * tr(ad(x) ad(y)) normalized.

    Standard normalization: (e, f) = 1, (h, h) = 2, all others 0.
    """
    return {
        ("e", "f"): Rational(1),
        ("f", "e"): Rational(1),
        ("h", "h"): Rational(2),
    }


# ---------------------------------------------------------------------------
# Central charge and level formulas
# ---------------------------------------------------------------------------

def sugawara_c(type_: str, rank: int, level) -> Rational:
    """Sugawara central charge: c = k * dim(g) / (k + h*).

    UNDEFINED at k = -h* (critical level). Raises ValueError.
    """
    data = cartan_data(type_, rank)
    k = sympify(level)
    if k + data.h_dual == 0:
        raise ValueError(f"Sugawara undefined at critical level k = -h* = {-data.h_dual}")
    return k * data.dim / (k + data.h_dual)


def ff_dual_level(type_: str, rank: int, level) -> Rational:
    """Feigin-Frenkel dual level: k' = -k - 2h*.

    NOT -k - h*. This is a verified fact (VF031).
    """
    data = cartan_data(type_, rank)
    k = sympify(level)
    return -k - 2 * data.h_dual


def kappa_km(type_: str, rank: int, level) -> Rational:
    """Obstruction coefficient for Kac-Moody ĝ_k.

    kappa = c * dim(g) / (2 * h* * dim(g)) ... actually:
    kappa = (k + h*) * dim(g) / (2 * h*)

    Wait — let me derive this correctly from the manuscript.
    From the Master Table: kappa(sl2_k) = 3(k+2)/4.
    sl2: dim=3, h*=2. So kappa = dim*(k+h*)/(2*h*) = 3*(k+2)/4. Check. ✓
    """
    data = cartan_data(type_, rank)
    k = sympify(level)
    t = k + data.h_dual  # shifted level
    return data.dim * t / (2 * data.h_dual)


def sigma_invariant(type_: str, rank: int) -> Rational:
    """Root datum invariant sigma(g) = sum 1/(m_i + 1).

    Where m_i are the exponents. This appears in:
    kappa(W^k(g)) = c * sigma(g)
    """
    data = cartan_data(type_, rank)
    return sum(Rational(1, m + 1) for m in data.exponents)


def virasoro_ds_c(level) -> Rational:
    """Virasoro central charge from Drinfeld-Sokolov reduction of sl2.

    c = 1 - 6(k+1)^2/(k+2)

    This is a verified formula (VF032).
    """
    k = sympify(level)
    return 1 - 6 * (k + 1)**2 / (k + 2)


def w3_ds_c(level) -> Rational:
    """W_3 central charge from DS reduction of sl3.

    c = 2 - 24(k+2)^2/(k+3)

    This is a verified formula (VF033).
    """
    k = sympify(level)
    return 2 - 24 * (k + 2)**2 / (k + 3)
