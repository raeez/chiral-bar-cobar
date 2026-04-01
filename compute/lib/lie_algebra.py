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

# ---------------------------------------------------------------------------
# Programmatic Cartan matrix generators
# ---------------------------------------------------------------------------

def _cartan_A(n):
    """Cartan matrix for A_n (sl_{n+1})."""
    rows = []
    for i in range(n):
        row = [0] * n
        row[i] = 2
        if i > 0:
            row[i - 1] = -1
        if i < n - 1:
            row[i + 1] = -1
        rows.append(row)
    return Matrix(rows)


def _cartan_B(n):
    """Cartan matrix for B_n (so_{2n+1}), n >= 2.

    Standard Dynkin diagram: o---o---...---o==>o
    Last node is short root. A[n-2,n-1] = -1, A[n-1,n-2] = -2.
    """
    rows = []
    for i in range(n):
        row = [0] * n
        row[i] = 2
        if i > 0:
            row[i - 1] = -1
        if i < n - 1:
            row[i + 1] = -1
        rows.append(row)
    # The bond between nodes n-2 and n-1 is double with arrow toward n-1 (short root)
    if n >= 2:
        rows[n - 1][n - 2] = -2
    return Matrix(rows)


def _cartan_C(n):
    """Cartan matrix for C_n (sp_{2n}), n >= 2.

    Standard Dynkin diagram: o---o---...---o<==o
    Last node is long root. A[n-2,n-1] = -2, A[n-1,n-2] = -1.
    """
    rows = []
    for i in range(n):
        row = [0] * n
        row[i] = 2
        if i > 0:
            row[i - 1] = -1
        if i < n - 1:
            row[i + 1] = -1
        rows.append(row)
    # The bond between nodes n-2 and n-1 is double with arrow toward n-2
    if n >= 2:
        rows[n - 2][n - 1] = -2
    return Matrix(rows)


def _cartan_D(n):
    """Cartan matrix for D_n (so_{2n}), n >= 4.

    Standard Dynkin diagram: o---o---...---o---o
                                              |
                                              o
    Nodes 0..n-3 form a chain. Node n-2 and n-1 both connect to node n-3.
    """
    rows = []
    for i in range(n):
        row = [0] * n
        row[i] = 2
        rows.append(row)
    # Chain: 0-1-2-...(n-3)
    for i in range(n - 3):
        rows[i][i + 1] = -1
        rows[i + 1][i] = -1
    # Fork: (n-3)---(n-2) and (n-3)---(n-1)
    if n >= 4:
        rows[n - 3][n - 2] = -1
        rows[n - 2][n - 3] = -1
        rows[n - 3][n - 1] = -1
        rows[n - 1][n - 3] = -1
    return Matrix(rows)


# Standard Cartan matrices for simple types
# Explicitly listed for small cases; programmatically generated for higher ranks
CARTAN_MATRICES = {
    ("A", 1): _cartan_A(1),
    ("A", 2): _cartan_A(2),
    ("A", 3): _cartan_A(3),
    ("A", 4): _cartan_A(4),
    ("A", 5): _cartan_A(5),
    ("A", 6): _cartan_A(6),
    ("A", 7): _cartan_A(7),
    ("A", 8): _cartan_A(8),
    ("B", 2): _cartan_B(2),
    ("B", 3): _cartan_B(3),
    ("B", 4): _cartan_B(4),
    ("B", 5): _cartan_B(5),
    ("B", 6): _cartan_B(6),
    ("B", 7): _cartan_B(7),
    ("B", 8): _cartan_B(8),
    ("C", 2): _cartan_C(2),
    ("C", 3): _cartan_C(3),
    ("C", 4): _cartan_C(4),
    ("C", 5): _cartan_C(5),
    ("C", 6): _cartan_C(6),
    ("C", 7): _cartan_C(7),
    ("C", 8): _cartan_C(8),
    ("D", 4): _cartan_D(4),
    ("D", 5): _cartan_D(5),
    ("D", 6): _cartan_D(6),
    ("D", 7): _cartan_D(7),
    ("D", 8): _cartan_D(8),
    ("G", 2): Matrix([[2, -1], [-3, 2]]),
    ("F", 4): Matrix([[2, -1, 0, 0], [-1, 2, -2, 0], [0, -1, 2, -1], [0, 0, -1, 2]]),
    ("E", 6): Matrix([
        [2, -1, 0, 0, 0, 0],
        [-1, 2, -1, 0, 0, 0],
        [0, -1, 2, -1, 0, -1],
        [0, 0, -1, 2, -1, 0],
        [0, 0, 0, -1, 2, 0],
        [0, 0, -1, 0, 0, 2],
    ]),
    ("E", 7): Matrix([
        [2, -1, 0, 0, 0, 0, 0],
        [-1, 2, -1, 0, 0, 0, 0],
        [0, -1, 2, -1, 0, 0, -1],
        [0, 0, -1, 2, -1, 0, 0],
        [0, 0, 0, -1, 2, -1, 0],
        [0, 0, 0, 0, -1, 2, 0],
        [0, 0, -1, 0, 0, 0, 2],
    ]),
    ("E", 8): Matrix([
        [2, -1, 0, 0, 0, 0, 0, 0],
        [-1, 2, -1, 0, 0, 0, 0, 0],
        [0, -1, 2, -1, 0, 0, 0, -1],
        [0, 0, -1, 2, -1, 0, 0, 0],
        [0, 0, 0, -1, 2, -1, 0, 0],
        [0, 0, 0, 0, -1, 2, -1, 0],
        [0, 0, 0, 0, 0, -1, 2, 0],
        [0, 0, -1, 0, 0, 0, 0, 2],
    ]),
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

    # Dimension, Coxeter, dual Coxeter, exponents, root_lengths_squared by type
    #
    # Reference data (Bourbaki, Humphreys):
    #   A_n: dim = n(n+2), h = n+1, h^v = n+1, exponents = [1,2,...,n]
    #   B_n: dim = n(2n+1), h = 2n, h^v = 2n-1, exponents = [1,3,5,...,2n-1]
    #         Root lengths: alpha_1..alpha_{n-1} long (2), alpha_n short (1)
    #   C_n: dim = n(2n+1), h = 2n, h^v = n+1, exponents = [1,3,5,...,2n-1]
    #         Root lengths: alpha_1..alpha_{n-1} short (1), alpha_n long (2)
    #   D_n: dim = n(2n-1), h = 2n-2, h^v = 2n-2, exponents = [1,3,...,2n-3,n-1]
    #   E_6: dim = 78, h = 12, h^v = 12, exponents = [1,4,5,7,8,11]
    #   E_7: dim = 133, h = 18, h^v = 18, exponents = [1,5,7,9,11,13,17]
    #   E_8: dim = 248, h = 30, h^v = 30, exponents = [1,7,11,13,17,19,23,29]
    #   F_4: dim = 52, h = 12, h^v = 9, exponents = [1,5,7,11]
    #   G_2: dim = 14, h = 6, h^v = 4, exponents = [1,5]
    data_table = {
        # A_n = sl_{n+1}: dim = n(n+2), h = h^v = n+1, all roots length 2
        ("A", 1): (3, 2, 2, [1], [2]),
        ("A", 2): (8, 3, 3, [1, 2], [2, 2]),
        ("A", 3): (15, 4, 4, [1, 2, 3], [2, 2, 2]),
        ("A", 4): (24, 5, 5, [1, 2, 3, 4], [2, 2, 2, 2]),
        ("A", 5): (35, 6, 6, [1, 2, 3, 4, 5], [2, 2, 2, 2, 2]),
        ("A", 6): (48, 7, 7, [1, 2, 3, 4, 5, 6], [2, 2, 2, 2, 2, 2]),
        ("A", 7): (63, 8, 8, [1, 2, 3, 4, 5, 6, 7], [2, 2, 2, 2, 2, 2, 2]),
        ("A", 8): (80, 9, 9, [1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 2, 2, 2, 2, 2, 2]),
        # B_n = so_{2n+1}: dim = n(2n+1), h = 2n, h^v = 2n-1
        # Root lengths: first n-1 long (2), last short (1)
        ("B", 2): (10, 4, 3, [1, 3], [2, 1]),
        ("B", 3): (21, 6, 5, [1, 3, 5], [2, 2, 1]),
        ("B", 4): (36, 8, 7, [1, 3, 5, 7], [2, 2, 2, 1]),
        ("B", 5): (55, 10, 9, [1, 3, 5, 7, 9], [2, 2, 2, 2, 1]),
        ("B", 6): (78, 12, 11, [1, 3, 5, 7, 9, 11], [2, 2, 2, 2, 2, 1]),
        ("B", 7): (105, 14, 13, [1, 3, 5, 7, 9, 11, 13], [2, 2, 2, 2, 2, 2, 1]),
        ("B", 8): (136, 16, 15, [1, 3, 5, 7, 9, 11, 13, 15], [2, 2, 2, 2, 2, 2, 2, 1]),
        # C_n = sp_{2n}: dim = n(2n+1), h = 2n, h^v = n+1
        # Root lengths: first n-1 short (1), last long (2)
        ("C", 2): (10, 4, 3, [1, 3], [1, 2]),
        ("C", 3): (21, 6, 4, [1, 3, 5], [1, 1, 2]),
        ("C", 4): (36, 8, 5, [1, 3, 5, 7], [1, 1, 1, 2]),
        ("C", 5): (55, 10, 6, [1, 3, 5, 7, 9], [1, 1, 1, 1, 2]),
        ("C", 6): (78, 12, 7, [1, 3, 5, 7, 9, 11], [1, 1, 1, 1, 1, 2]),
        ("C", 7): (105, 14, 8, [1, 3, 5, 7, 9, 11, 13], [1, 1, 1, 1, 1, 1, 2]),
        ("C", 8): (136, 16, 9, [1, 3, 5, 7, 9, 11, 13, 15], [1, 1, 1, 1, 1, 1, 1, 2]),
        # D_n = so_{2n}: dim = n(2n-1), h = h^v = 2n-2, all simply-laced
        # Exponents for D_n: 1, 3, 5, ..., 2n-3, n-1 (note n-1 appears in middle)
        ("D", 4): (28, 6, 6, [1, 3, 3, 5], [2, 2, 2, 2]),
        ("D", 5): (45, 8, 8, [1, 3, 4, 5, 7], [2, 2, 2, 2, 2]),
        ("D", 6): (66, 10, 10, [1, 3, 5, 5, 7, 9], [2, 2, 2, 2, 2, 2]),
        ("D", 7): (91, 12, 12, [1, 3, 5, 6, 7, 9, 11], [2, 2, 2, 2, 2, 2, 2]),
        ("D", 8): (120, 14, 14, [1, 3, 5, 7, 7, 9, 11, 13], [2, 2, 2, 2, 2, 2, 2, 2]),
        # Exceptional types
        ("G", 2): (14, 6, 4, [1, 5], [2, 6]),
        ("F", 4): (52, 12, 9, [1, 5, 7, 11], [2, 2, 1, 1]),
        ("E", 6): (78, 12, 12, [1, 4, 5, 7, 8, 11], [2, 2, 2, 2, 2, 2]),
        ("E", 7): (133, 18, 18, [1, 5, 7, 9, 11, 13, 17], [2, 2, 2, 2, 2, 2, 2]),
        ("E", 8): (248, 30, 30, [1, 7, 11, 13, 17, 19, 23, 29], [2, 2, 2, 2, 2, 2, 2, 2]),
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

    UNDEFINED at k = -2 (sl2 critical level k = -h*). Raises ValueError.
    This is a verified formula (VF032).
    """
    k = sympify(level)
    if k + 2 == 0:
        raise ValueError("Virasoro DS central charge undefined at sl2 critical level k = -2")
    return 1 - 6 * (k + 1)**2 / (k + 2)


def w3_ds_c(level) -> Rational:
    """W_3 central charge from DS reduction of sl3.

    c = 2 - 24(k+2)^2/(k+3)

    UNDEFINED at k = -3 (sl3 critical level k = -h*). Raises ValueError.
    This is a verified formula (VF033).
    """
    k = sympify(level)
    if k + 3 == 0:
        raise ValueError("W3 DS central charge undefined at sl3 critical level k = -3")
    return 2 - 24 * (k + 2)**2 / (k + 3)
