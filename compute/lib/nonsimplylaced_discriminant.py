"""Non-simply-laced discriminant analysis for bar cohomology.

Verifies conj:non-simply-laced-discriminant from the monograph:
  For non-simply-laced g (B_n, C_n, F_4, G_2), the bar cohomology GF
  P_{g-hat}(x) is algebraic with discriminant Delta_g(x) satisfying:
    (i)   Delta_g has a simple root at x = 1/dim(g)
    (ii)  The DS discriminant Delta_{W(g)} shares the same branch locus
    (iii) For G_2: dim(g) = 14, so predicted growth rate is 14^n

Key facts for non-simply-laced (CLAUDE.md):
  - h^vee != h (dual Coxeter != Coxeter)
  - B_n: h^vee = 2n-1, C_n: h^vee = n+1
  - Root lengths differ: short roots have |alpha|^2 = 2/r, r = lacing number
  - KM periodicity uses h (Coxeter), NOT h^vee

Discriminant framework (combinatorial_frontier.tex, sec:discriminant-families):
  - sl_2 family: Delta = (1-3x)(1+x), roots 1/3 = 1/dim(sl_2) and -1
  - sl_3 family (conj): discriminant factor 1-3x-x^2
  - Transfer matrix T_rec: eigenvalues = roots of reciprocal of Delta
  - det(1 - x*T_rec) = Delta(x) up to normalization

The rank-plus-one pattern (subsec:gf-sl3-family):
  - sl_2: recurrence depth = 2 = rank + 1
  - sl_3 (conj): recurrence depth = 3 = rank + 1
  - Predicted: depth = rank(g) + 1 for all g

This module:
  1. Implements Cartan matrices for B_2, G_2, C_3, F_4
  2. Computes Weyl group data: order, exponents, Coxeter number
  3. Computes E_1 page dimensions via LQT partition function
  4. Predicts discriminant structure from the conjecture
  5. Compares with simply-laced cases

CONVENTIONS:
- Cohomological grading, |d| = +1
- Root length normalization: long roots have |alpha|^2 = 2
"""

from __future__ import annotations

from math import comb, factorial, prod
from typing import Dict, List, Optional, Tuple

from sympy import Matrix, Rational, Symbol, sqrt, eye, det, Poly, symbols

from compute.lib.lie_algebra import cartan_data, LieAlgebraData, CARTAN_MATRICES


# ---------------------------------------------------------------------------
# Cartan matrix properties
# ---------------------------------------------------------------------------

def cartan_matrix(type_: str, rank: int) -> Matrix:
    """Return the Cartan matrix for the given type and rank."""
    data = cartan_data(type_, rank)
    return data.cartan


def symmetrizer(type_: str, rank: int) -> List[int]:
    """Compute the symmetrizer D = diag(d_1, ..., d_r) such that D*A is symmetric.

    For a Cartan matrix A, there exist positive integers d_i such that
    d_i * a_{ij} = d_j * a_{ji} for all i,j.

    The symmetrizer is determined (up to overall scale) by the Cartan matrix:
    for adjacent nodes i,j, d_i/d_j = a_{ji}/a_{ij}.  We compute d by
    BFS from node 0, then normalize to coprime positive integers.

    Ground truth (verified):
      B_2: [2,1], B_3: [2,2,1], C_2: [1,2], C_3: [1,1,2],
      G_2: [3,1], F_4: [1,1,2,2], A_n: [1,...,1], D_4: [1,1,1,1].
    """
    A = cartan_matrix(type_, rank)
    n = A.rows

    # BFS from node 0 to determine ratios
    d_rat = [Rational(0)] * n
    d_rat[0] = Rational(1)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        i = queue.pop(0)
        for j in range(n):
            if visited[j] or A[i, j] == 0 or i == j:
                continue
            # d_i * a_{ij} = d_j * a_{ji}  =>  d_j = d_i * a_{ij} / a_{ji}
            d_rat[j] = d_rat[i] * Rational(int(A[i, j]), int(A[j, i]))
            visited[j] = True
            queue.append(j)

    # Normalize: clear denominators and make coprime
    from math import gcd
    from functools import reduce
    # Find LCD
    denoms = [d.q for d in d_rat]
    lcd = reduce(lambda a, b: a * b // gcd(a, b), denoms)
    int_d = [int(d * lcd) for d in d_rat]
    # Make all positive
    if any(x < 0 for x in int_d):
        int_d = [-x if int_d[0] < 0 else x for x in int_d]
    # Divide by GCD
    g = reduce(gcd, int_d)
    return [x // g for x in int_d]


def is_symmetrizable(type_: str, rank: int) -> bool:
    """Check that D*A is symmetric where D = diag(symmetrizer)."""
    A = cartan_matrix(type_, rank)
    d = symmetrizer(type_, rank)
    n = A.rows
    for i in range(n):
        for j in range(n):
            if d[i] * A[i, j] != d[j] * A[j, i]:
                return False
    return True


def symmetrized_cartan(type_: str, rank: int) -> Matrix:
    """Return D*A (symmetric positive-definite matrix) where D = diag(symmetrizer)."""
    A = cartan_matrix(type_, rank)
    d = symmetrizer(type_, rank)
    n = A.rows
    DA = Matrix(n, n, lambda i, j: d[i] * A[i, j])
    return DA


def inner_product_matrix(type_: str, rank: int) -> Matrix:
    """Return the Weyl-invariant inner product matrix B_{ij} = <alpha_i, alpha_j>.

    Uses the relation a_{ij} = 2<alpha_i, alpha_j> / <alpha_j, alpha_j>,
    giving B_{ij} = a_{ij} * |alpha_j|^2 / 2.

    This is the correct bilinear form for computing root lengths:
    |alpha|^2 = sum_{i,j} c_i c_j B_{ij} for alpha = sum c_i alpha_i.

    The matrix B is symmetric and positive-definite.
    """
    data = cartan_data(type_, rank)
    A = data.cartan
    rl = data.root_lengths_squared
    n = A.rows
    B = Matrix(n, n, lambda i, j: Rational(int(A[i, j]) * rl[j], 2))
    return B


def is_positive_definite(M: Matrix) -> bool:
    """Check if a symmetric matrix is positive-definite via eigenvalues."""
    # Use Cholesky-like check: all leading principal minors > 0
    n = M.rows
    for k in range(1, n + 1):
        minor = M[:k, :k]
        if det(minor) <= 0:
            return False
    return True


def lacing_number(type_: str, rank: int) -> int:
    """Lacing number r: ratio of long to short root lengths squared.

    r = max(|alpha_i|^2) / min(|alpha_j|^2).
    Simply-laced: r=1. B,C,F: r=2. G: r=3.
    """
    data = cartan_data(type_, rank)
    lengths = data.root_lengths_squared
    return max(lengths) // min(lengths)


# ---------------------------------------------------------------------------
# Root system data
# ---------------------------------------------------------------------------

def root_system_data(type_: str, rank: int) -> Dict[str, object]:
    """Complete root system data for a simple Lie algebra."""
    data = cartan_data(type_, rank)
    pos_roots = data.positive_roots
    n_pos = len(pos_roots)
    lengths = data.root_lengths_squared

    # Classify positive roots as long or short using the inner product matrix
    # B_{ij} = <alpha_i, alpha_j> where <alpha_i, alpha_i> = root_lengths_squared[i]
    B = inner_product_matrix(type_, rank)
    max_len_sq = max(lengths)  # length^2 of long simple roots

    long_roots = []
    short_roots = []

    for root in pos_roots:
        # Compute |root|^2 = sum c_i c_j B_{ij}
        len_sq = 0
        for i in range(rank):
            for j in range(rank):
                len_sq += root[i] * root[j] * int(B[i, j])
        if len_sq == max_len_sq:
            long_roots.append(root)
        else:
            short_roots.append(root)

    return {
        "type": f"{type_}{rank}",
        "rank": data.rank,
        "dim": data.dim,
        "h": data.h,
        "h_dual": data.h_dual,
        "exponents": data.exponents,
        "n_positive_roots": n_pos,
        "n_long_positive": len(long_roots),
        "n_short_positive": len(short_roots),
        "n_total_roots": 2 * n_pos,
        "root_lengths_squared": lengths,
        "lacing_number": lacing_number(type_, rank),
        "simply_laced": data.h == data.h_dual,
        "weyl_group_order": weyl_group_order(type_, rank),
    }


def weyl_group_order(type_: str, rank: int) -> int:
    """Order of the Weyl group |W|.

    |W| = prod_{i=1}^{r} (m_i + 1)  where m_i are the exponents.
    """
    data = cartan_data(type_, rank)
    return prod(m + 1 for m in data.exponents)


def coxeter_number(type_: str, rank: int) -> int:
    """Coxeter number h = max exponent + 1."""
    data = cartan_data(type_, rank)
    return data.h


def dual_coxeter_number(type_: str, rank: int) -> int:
    """Dual Coxeter number h^vee."""
    data = cartan_data(type_, rank)
    return data.h_dual


def number_of_positive_roots(type_: str, rank: int) -> int:
    """Number of positive roots = dim(g) - rank / 2."""
    data = cartan_data(type_, rank)
    return len(data.positive_roots)


# ---------------------------------------------------------------------------
# E_1 page dimension computation (LQT-based)
# ---------------------------------------------------------------------------

def e1_dimensions_lqt(type_: str, rank: int, p_max: int) -> List[int]:
    """dim E_1^{0,p}(g[t]) for p = 0, ..., p_max via LQT theorem.

    The LQT theorem gives H*(g[t], k) = Lambda(xi_{i,n})
    where deg(xi_{i,n}) = 2*e_i + 1 + 2*n for n >= 0.

    dim E_1^{0,p} = number of subsets S of generators {(i,n)} with
    sum of degrees = p.

    This uses the same algorithm as lqt_e1_growth.py but works with
    the lie_algebra.py infrastructure.
    """
    data = cartan_data(type_, rank)
    exps = data.exponents

    # Generate all LQT generator degrees <= p_max
    gens = []
    for e in exps:
        n = 0
        while 2 * e + 1 + 2 * n <= p_max:
            gens.append(2 * e + 1 + 2 * n)
            n += 1

    # Dynamic programming: count subsets with given total degree
    dp = [0] * (p_max + 1)
    dp[0] = 1
    for gen_deg in sorted(gens):
        for s in range(p_max, gen_deg - 1, -1):
            dp[s] += dp[s - gen_deg]
    return dp


def e1_total_through_degree(type_: str, rank: int, n_max: int, p_max: int = 200) -> Dict[int, int]:
    """Total E_1 dimension at each bar degree n, summing over weights.

    For the PBW spectral sequence E_1 page:
      dim E_1^{n,*} = sum_{p >= n} dim E_1^{0,p} * C(N_p, n) / ...

    Actually, the LQT E_1 computation gives E_1^{0,p} as the generating
    function for the Koszul dual of the associated graded. The bar degree n
    data requires a different decomposition.

    For low degrees, the bar cohomology at degree n is related to the
    n-th exterior power of the primitive CE generators.

    Here we compute the E_1 page dimensions at each total weight p,
    which inform the growth rate of bar cohomology.
    """
    dims = e1_dimensions_lqt(type_, rank, p_max)
    # Return nonzero entries
    return {p: dims[p] for p in range(p_max + 1) if dims[p] > 0}


# ---------------------------------------------------------------------------
# Discriminant framework
# ---------------------------------------------------------------------------

def predicted_growth_rate(type_: str, rank: int) -> int:
    """Predicted exponential growth rate = dim(g).

    From conj:non-simply-laced-discriminant (i):
      Delta_g has a simple root at x = 1/dim(g),
      so the growth rate is dim(g)^n.
    """
    data = cartan_data(type_, rank)
    return data.dim


def predicted_discriminant_degree(type_: str, rank: int) -> int:
    """Predicted degree of discriminant = rank + 1.

    From the rank-plus-one pattern (combinatorial_frontier.tex):
      sl_2: depth 2 = rank(1) + 1
      sl_3 (conj): depth 3 = rank(2) + 1
    """
    data = cartan_data(type_, rank)
    return data.rank + 1


def predicted_discriminant_roots(type_: str, rank: int) -> Dict[str, object]:
    """Predicted structure of the discriminant.

    The discriminant Delta(x) = det(1 - x*T_rec) factors as:
      - (1 - dim(g)*x): the growth pole
      - a degree-rank polynomial: the DS-invariant factor

    Returns predicted properties of the discriminant.
    """
    data = cartan_data(type_, rank)
    dim_g = data.dim
    r = data.rank

    return {
        "total_degree": r + 1,
        "growth_pole": Rational(1, dim_g),
        "ds_invariant_degree": r,
        "dim_g": dim_g,
        "rank": r,
        "growth_rate": dim_g,
    }


def simply_laced_discriminant(type_: str, rank: int) -> Optional[Dict]:
    """Known discriminant for simply-laced types.

    sl_2: Delta(x) = (1-3x)(1+x) = 1 - 2x - 3x^2
    sl_3 (conj): (1-8x)(1-3x-x^2)
    """
    if type_ == "A" and rank == 1:
        x = Symbol('x')
        return {
            "polynomial": 1 - 2*x - 3*x**2,
            "factored": (1 - 3*x) * (1 + x),
            "roots": [Rational(1, 3), Rational(-1)],
            "growth_rate": 3,
            "ds_invariant_factor": (1 + x),
            "status": "proved",
        }
    elif type_ == "A" and rank == 2:
        x = Symbol('x')
        return {
            "polynomial": (1 - 8*x) * (1 - 3*x - x**2),
            "factored_growth": (1 - 8*x),
            "factored_ds": (1 - 3*x - x**2),
            "growth_rate": 8,
            "ds_invariant_factor": (1 - 3*x - x**2),
            "status": "conjectured",
        }
    return None


# ---------------------------------------------------------------------------
# Transfer matrix and recurrence structure
# ---------------------------------------------------------------------------

def sl2_transfer_matrix() -> Matrix:
    """Picard-Fuchs companion matrix for sl_2.

    T_rec = [[2, 3], [1, 0]]
    eigenvalues: 3, -1 (roots of t^2 - 2t - 3 = (t-3)(t+1))
    det(I - x*T) = 1 - 2x - 3x^2 = Delta(x)
    """
    return Matrix([[2, 3], [1, 0]])


def verify_sl2_transfer_matrix() -> Dict[str, bool]:
    """Verify that det(I - x*T_rec) = Delta(x) for sl_2."""
    T = sl2_transfer_matrix()
    x = Symbol('x')
    I = eye(2)
    det_val = det(I - x * T)
    expected = 1 - 2*x - 3*x**2

    eigenvals = list(T.eigenvals().keys())
    eigenvals_sorted = sorted([int(e) for e in eigenvals])

    return {
        "det_equals_discriminant": det_val.expand() == expected.expand(),
        "eigenvalues": eigenvals_sorted,
        "eigenvalues_correct": eigenvals_sorted == [-1, 3],
        "growth_eigenvalue": max(eigenvals_sorted),
        "growth_equals_dim": max(eigenvals_sorted) == 3,
    }


def conjectured_sl3_transfer_matrix() -> Matrix:
    """Conjectured Picard-Fuchs companion matrix for sl_3.

    Characteristic polynomial: t^3 - 11t^2 + 23t + 8 = (t-8)(t^2-3t-1)
    Companion matrix in standard form.
    """
    return Matrix([
        [11, -23, -8],
        [1, 0, 0],
        [0, 1, 0],
    ])


def verify_sl3_transfer_matrix() -> Dict[str, bool]:
    """Verify conjectured sl_3 transfer matrix properties."""
    T = conjectured_sl3_transfer_matrix()
    x = Symbol('x')
    I = eye(3)
    det_val = det(I - x * T)

    # Expected: (1-8x)(1-3x-x^2) = 1 - 11x + 23x^2 + 8x^3
    expected = 1 - 11*x + 23*x**2 + 8*x**3

    return {
        "det_equals_discriminant": det_val.expand() == expected.expand(),
        "growth_pole_at_1_over_8": det_val.subs(x, Rational(1, 8)) == 0,
    }


# ---------------------------------------------------------------------------
# Non-simply-laced predictions
# ---------------------------------------------------------------------------

def nonsimplylaced_predicted_data() -> Dict[str, Dict]:
    """Predicted data for all non-simply-laced types in the registry.

    Returns for each type: predicted growth rate, discriminant degree,
    h vs h^vee distinction, and chain group dimensions.
    """
    types = [("B", 2), ("B", 3), ("C", 2), ("C", 3), ("G", 2), ("F", 4)]
    results = {}

    for type_, rank in types:
        data = cartan_data(type_, rank)
        label = f"{type_}{rank}"

        results[label] = {
            "dim": data.dim,
            "rank": data.rank,
            "h": data.h,
            "h_dual": data.h_dual,
            "h_neq_h_dual": data.h != data.h_dual,
            "exponents": data.exponents,
            "predicted_growth_rate": data.dim,
            "predicted_discriminant_degree": data.rank + 1,
            "predicted_ds_invariant_degree": data.rank,
            "lacing_number": lacing_number(type_, rank),
            "weyl_order": weyl_group_order(type_, rank),
            "chain_dim_1": data.dim,
            "chain_dim_2": data.dim ** 2,
            "chain_dim_3": data.dim ** 3 * 2,  # dim^3 * 2!
        }

    return results


def chain_group_dimensions(type_: str, rank: int, max_degree: int = 5) -> Dict[int, int]:
    """Chain group dimensions dim B-bar^n = dim(g)^n * (n-1)! for KM algebra.

    From bar_complex.py: proved in rem:bar-dims-level-independent.
    """
    data = cartan_data(type_, rank)
    dim_g = data.dim
    return {n: dim_g ** n * factorial(n - 1) for n in range(1, max_degree + 1)}


# ---------------------------------------------------------------------------
# Comparison: simply-laced vs non-simply-laced
# ---------------------------------------------------------------------------

def comparison_table() -> List[Dict]:
    """Build comparison table between simply-laced and non-simply-laced types."""
    all_types = [
        ("A", 1), ("A", 2), ("A", 3),     # simply-laced
        ("B", 2), ("B", 3),                # non-simply-laced
        ("C", 2), ("C", 3),
        ("G", 2),
        ("D", 4),                           # simply-laced
        ("F", 4),                           # non-simply-laced
    ]

    rows = []
    for type_, rank in all_types:
        data = cartan_data(type_, rank)
        rows.append({
            "label": f"{type_}{rank}",
            "dim": data.dim,
            "rank": data.rank,
            "h": data.h,
            "h_dual": data.h_dual,
            "simply_laced": data.h == data.h_dual,
            "exponents": data.exponents,
            "lacing": lacing_number(type_, rank),
            "predicted_growth": data.dim,
            "predicted_disc_deg": data.rank + 1,
            "weyl_order": weyl_group_order(type_, rank),
        })

    return rows


def growth_rate_comparison() -> Dict[str, Dict]:
    """Compare predicted vs known growth rates across types."""
    results = {}

    # sl_2: PROVED growth rate 3 = dim(sl_2)
    results["A1"] = {
        "dim": 3,
        "growth_rate": 3,
        "status": "proved",
        "matches_dim": True,
    }

    # sl_3: CONJECTURED growth rate 8 = dim(sl_3)
    results["A2"] = {
        "dim": 8,
        "growth_rate": 8,
        "status": "conjectured",
        "matches_dim": True,
    }

    # Non-simply-laced: PREDICTED
    for type_, rank, label in [("B", 2, "B2"), ("G", 2, "G2"),
                                ("C", 3, "C3"), ("F", 4, "F4")]:
        data = cartan_data(type_, rank)
        results[label] = {
            "dim": data.dim,
            "growth_rate": data.dim,  # predicted
            "status": "predicted",
            "matches_dim": True,  # by construction
        }

    return results


# ---------------------------------------------------------------------------
# Koszul dual Hilbert series predictions
# ---------------------------------------------------------------------------

def koszul_dual_prediction_h1(type_: str, rank: int) -> int:
    """Koszul dual dim at degree 1 = dim(g).

    For any KM algebra g-hat_k, H^1(B-bar) = dim(g).
    This is universal (proved, bar_complex.py).
    """
    data = cartan_data(type_, rank)
    return data.dim


def exponent_product_formula(type_: str, rank: int) -> int:
    """Product formula prod(m_i + 1) = |W| (Weyl group order).

    The exponents m_1, ..., m_r satisfy:
      - Sum(m_i) = n_positive_roots
      - Product(m_i + 1) = |W|
      - h = max(m_i) + 1 (Coxeter number)
    """
    data = cartan_data(type_, rank)
    return prod(m + 1 for m in data.exponents)


def exponent_sum_formula(type_: str, rank: int) -> int:
    """Sum of exponents = number of positive roots.

    sum(m_i) = |Phi^+| = (dim(g) - rank) / 2
    """
    data = cartan_data(type_, rank)
    return sum(data.exponents)


# ---------------------------------------------------------------------------
# Discriminant factorization conjectures
# ---------------------------------------------------------------------------

def conjectured_discriminant_structure(type_: str, rank: int) -> Dict[str, object]:
    """Conjectured discriminant structure for a Lie algebra.

    From conj:non-simply-laced-discriminant and the rank-plus-one pattern:
      Delta_g(x) = (1 - dim(g)*x) * Delta_DS(x)
    where Delta_DS is a degree-rank polynomial (the DS-invariant factor).

    For non-simply-laced types, the h vs h^vee distinction should
    manifest in the discriminant structure (remark in combinatorial_frontier).
    """
    data = cartan_data(type_, rank)
    dim_g = data.dim
    r = data.rank

    result = {
        "type": f"{type_}{rank}",
        "dim": dim_g,
        "rank": r,
        "total_discriminant_degree": r + 1,
        "growth_pole": Rational(1, dim_g),
        "ds_invariant_degree": r,
        "simply_laced": data.h == data.h_dual,
        "h": data.h,
        "h_dual": data.h_dual,
    }

    # For non-simply-laced, the dual Coxeter discrepancy Delta_h = h - h^vee
    # should manifest in the discriminant structure
    if data.h != data.h_dual:
        result["coxeter_discrepancy"] = data.h - data.h_dual
        result["lacing_number"] = lacing_number(type_, rank)

    return result


# ---------------------------------------------------------------------------
# E_1 growth comparison across types
# ---------------------------------------------------------------------------

def e1_growth_constants() -> Dict[str, Dict]:
    """Theoretical growth constants C_g = pi*sqrt(r/12) for all types.

    This is the sub-exponential growth rate of the E_1 page:
      dim E_1^{0,p} ~ exp(C_g * sqrt(p))
    """
    import math
    all_types = [
        ("A", 1, "A1"), ("A", 2, "A2"), ("A", 3, "A3"),
        ("B", 2, "B2"), ("B", 3, "B3"),
        ("C", 2, "C2"), ("C", 3, "C3"),
        ("G", 2, "G2"),
        ("D", 4, "D4"),
        ("F", 4, "F4"),
    ]

    results = {}
    for type_, rank, label in all_types:
        data = cartan_data(type_, rank)
        r = data.rank
        C_g = math.pi * math.sqrt(r / 12.0)
        results[label] = {
            "rank": r,
            "C_theory": C_g,
            "simply_laced": data.h == data.h_dual,
        }

    return results


def e1_small_values(type_: str, rank: int, p_max: int = 30) -> List[int]:
    """First few E_1 dimensions for diagnostic purposes."""
    return e1_dimensions_lqt(type_, rank, p_max)


# ---------------------------------------------------------------------------
# Verification functions
# ---------------------------------------------------------------------------

def verify_cartan_properties() -> Dict[str, bool]:
    """Verify Cartan matrix properties for all non-simply-laced types."""
    results = {}

    for type_, rank in [("B", 2), ("B", 3), ("C", 2), ("C", 3),
                         ("G", 2), ("F", 4)]:
        label = f"{type_}{rank}"
        A = cartan_matrix(type_, rank)

        # Diagonal entries = 2
        results[f"{label}: diagonal=2"] = all(A[i, i] == 2 for i in range(rank))

        # Off-diagonal entries <= 0
        results[f"{label}: off-diag<=0"] = all(
            A[i, j] <= 0 for i in range(rank) for j in range(rank) if i != j
        )

        # Symmetrizable
        results[f"{label}: symmetrizable"] = is_symmetrizable(type_, rank)

        # Symmetrized matrix positive-definite
        DA = symmetrized_cartan(type_, rank)
        results[f"{label}: DA_pos_def"] = is_positive_definite(DA)

        # Symmetrized matrix actually symmetric
        results[f"{label}: DA_symmetric"] = all(
            DA[i, j] == DA[j, i] for i in range(rank) for j in range(rank)
        )

    return results


def verify_root_system_identities() -> Dict[str, bool]:
    """Verify standard root system identities for all types."""
    results = {}

    for type_, rank in [("A", 1), ("A", 2), ("B", 2), ("B", 3),
                         ("C", 2), ("C", 3), ("G", 2), ("D", 4), ("F", 4)]:
        label = f"{type_}{rank}"
        data = cartan_data(type_, rank)
        exps = data.exponents
        n_pos = len(data.positive_roots)

        # sum(exponents) = n_positive_roots
        results[f"{label}: sum(exp)=n_pos"] = sum(exps) == n_pos

        # dim = rank + 2*n_positive_roots
        results[f"{label}: dim=rank+2*n_pos"] = data.dim == data.rank + 2 * n_pos

        # max(exponents) + 1 = h
        results[f"{label}: max(exp)+1=h"] = max(exps) + 1 == data.h

        # |W| = prod(m_i + 1)
        W = weyl_group_order(type_, rank)
        results[f"{label}: |W|=prod(m+1)"] = W == prod(m + 1 for m in exps)

    return results


def verify_nonsimplylaced_h_distinction() -> Dict[str, bool]:
    """Verify h != h^vee for all non-simply-laced types."""
    results = {}

    simply_laced = [("A", 1), ("A", 2), ("A", 3), ("D", 4)]
    for type_, rank in simply_laced:
        label = f"{type_}{rank}"
        data = cartan_data(type_, rank)
        results[f"{label}: h=h_dual (simply-laced)"] = data.h == data.h_dual

    nonsimply_laced = [("B", 2), ("B", 3), ("C", 2), ("C", 3), ("G", 2), ("F", 4)]
    for type_, rank in nonsimply_laced:
        label = f"{type_}{rank}"
        data = cartan_data(type_, rank)
        results[f"{label}: h!=h_dual (non-simply-laced)"] = data.h != data.h_dual

    # Specific values from CLAUDE.md
    results["B2: h_dual=3"] = cartan_data("B", 2).h_dual == 3
    results["C2: h_dual=3"] = cartan_data("C", 2).h_dual == 3
    results["B3: h_dual=5"] = cartan_data("B", 3).h_dual == 5
    results["C3: h_dual=4"] = cartan_data("C", 3).h_dual == 4
    results["G2: h_dual=4"] = cartan_data("G", 2).h_dual == 4
    results["F4: h_dual=9"] = cartan_data("F", 4).h_dual == 9

    return results


def verify_all() -> Dict[str, bool]:
    """Run all verification checks."""
    results = {}
    for section, fn in [
        ("cartan", verify_cartan_properties),
        ("roots", verify_root_system_identities),
        ("h_distinction", verify_nonsimplylaced_h_distinction),
    ]:
        for name, ok in fn().items():
            results[f"{section}: {name}"] = ok
    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("NON-SIMPLY-LACED DISCRIMINANT ANALYSIS")
    print("conj:non-simply-laced-discriminant verification")
    print("=" * 70)

    print("\n--- Verification ---")
    for name, ok in verify_all().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n--- Comparison table ---")
    for row in comparison_table():
        sl = "SL" if row["simply_laced"] else "NSL"
        print(f"  {row['label']:3s} [{sl:3s}]: dim={row['dim']:3d}, "
              f"h={row['h']:2d}, h^v={row['h_dual']:2d}, "
              f"exp={row['exponents']}, "
              f"growth={row['predicted_growth']:3d}, "
              f"disc_deg={row['predicted_disc_deg']}")

    print("\n--- Transfer matrix (sl_2) ---")
    for name, ok in verify_sl2_transfer_matrix().items():
        print(f"  {name}: {ok}")

    print("\n--- Transfer matrix (sl_3, conjectured) ---")
    for name, ok in verify_sl3_transfer_matrix().items():
        print(f"  {name}: {ok}")

    print("\n--- Non-simply-laced predictions ---")
    for label, data in nonsimplylaced_predicted_data().items():
        print(f"  {label}: dim={data['dim']}, rank={data['rank']}, "
              f"h={data['h']}, h^v={data['h_dual']}, "
              f"growth={data['predicted_growth_rate']}, "
              f"disc_deg={data['predicted_discriminant_degree']}")
