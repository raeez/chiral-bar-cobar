r"""Kodaira-Spencer operator on reduced bar cohomology (conj:discriminant-ks-operator).

CONJECTURE (landscape_census.tex, label conj:discriminant-ks-operator):
  For simple Lie algebra g, the genus-1 component Theta_A^{(1)} induces a
  finite-rank Kodaira-Spencer transport operator KS_g on reduced bar cohomology
  H^red_1(A), of dimension rank(g) + 1, such that:

    Delta_g(x) = det(1 - x * KS_g | H^red_1(A))

  and the largest eigenvalue of KS_g is dim(g).

KEY DATA (landscape_census.tex, ds_spectral_branch_sl3.py):
  sl_2:  Delta = (1-3x)(1+x),         eigenvalues {3, -1}
  sl_3:  Delta = (1-8x)(1-3x-x^2),    eigenvalues {8, (3+sqrt13)/2, (3-sqrt13)/2}

RANK-PLUS-ONE PATTERN (rem:rank-plus-one):
  dim H^red_1 = rank(g) + 1.
  sl_2: rank 1 + 1 = 2 (degree 2)
  sl_3: rank 2 + 1 = 3 (degree 3)

CONSTRUCTION (prop:hred-sl2):
  The reduced bar cohomology H^red_1 is the fiber at x=0 of the Picard-Fuchs
  D-module of the bar cohomology generating function.  The KS operator is the
  asymptotic companion matrix T_rec of the holonomic recurrence satisfied by
  the dimension sequence.

For sl_2:
  T_rec = [[2, 3], [1, 0]], eigenvalues {3, -1}
  det(1 - x*T_rec) = (1-3x)(1+x)

For sl_3 (conjectural, from conj:sl3-bar-gf):
  Recurrence a(n) = 11*a(n-1) - 23*a(n-2) - 8*a(n-3)
  Char poly: t^3 - 11*t^2 + 23*t + 8 = (t-8)(t^2-3t-1)
  T_rec companion matrix with eigenvalues {8, (3+sqrt13)/2, (3-sqrt13)/2}

DS INVARIANCE:
  Under Drinfeld-Sokolov reduction sl_N -> W_N, the dominant eigenvalue
  dim(sl_N) is replaced but the sub-discriminant (DS-invariant factor)
  is preserved:
    sl_2: (1-3x)(1+x) -> same (Virasoro has same discriminant)
    sl_3: (1-8x)(1-3x-x^2) -> (1-x)(1-3x-x^2) for W_3

KAPPA FORMULA:
  kappa(V_k(g)) = dim(g) * (k + h^v) / (2 * h^v)
  At k -> infinity: kappa -> infinity.
  The "dim(g)" appearing in the KS dominant eigenvalue is the growth rate
  of bar cohomology: dim H^n(B(g)) ~ C * dim(g)^n * n^{-3/2}.

This module implements the KS operator, verifies the determinant formula,
and tests the conjecture predictions for sl_2, sl_3, and higher-rank cases.

References:
  conj:discriminant-ks-operator (landscape_census.tex)
  prop:hred-sl2 (landscape_census.tex)
  thm:dominant-branch-point (landscape_census.tex)
  rem:rank-plus-one (landscape_census.tex)
  conj:sl3-bar-gf (landscape_census.tex)
  thm:ds-bar-gf-discriminant (landscape_census.tex)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from sympy import (
    Matrix,
    Poly,
    Rational,
    Symbol,
    det,
    expand,
    eye,
    factor,
    nsimplify,
    simplify,
    solve,
    sqrt,
    symbols,
)


# =========================================================================
# Lie algebra data (self-contained; mirrors lie_algebra.py to avoid circular deps)
# =========================================================================

@dataclass(frozen=True)
class SimpleLieData:
    """Minimal data for a simple Lie algebra relevant to the KS conjecture."""

    label: str           # e.g. "sl_2", "sl_3", "so_5"
    cartan_type: str     # e.g. "A", "B", "C", "D", "G", "F"
    rank: int
    dimension: int
    dual_coxeter: int    # h^vee
    exponents: Tuple[int, ...]


# Registry of simple Lie algebras
_LIE_DATA: Dict[str, SimpleLieData] = {
    "sl_2": SimpleLieData("sl_2", "A", 1, 3, 2, (1,)),
    "sl_3": SimpleLieData("sl_3", "A", 2, 8, 3, (1, 2)),
    "sl_4": SimpleLieData("sl_4", "A", 3, 15, 4, (1, 2, 3)),
    "sl_5": SimpleLieData("sl_5", "A", 4, 24, 5, (1, 2, 3, 4)),
    "so_5": SimpleLieData("so_5", "B", 2, 10, 3, (1, 3)),
    "sp_4": SimpleLieData("sp_4", "C", 2, 10, 3, (1, 3)),
    "G_2":  SimpleLieData("G_2", "G", 2, 14, 4, (1, 5)),
    "so_8": SimpleLieData("so_8", "D", 4, 28, 6, (1, 3, 3, 5)),
    "F_4":  SimpleLieData("F_4", "F", 4, 52, 9, (1, 5, 7, 11)),
}


def get_lie_data(label: str) -> SimpleLieData:
    """Retrieve Lie algebra data by label."""
    if label not in _LIE_DATA:
        raise ValueError(f"Unknown Lie algebra: {label}. "
                         f"Known: {list(_LIE_DATA.keys())}")
    return _LIE_DATA[label]


# =========================================================================
# Kappa formula
# =========================================================================

def kappa_affine(label: str, level) -> object:
    r"""Obstruction coefficient kappa(V_k(g)).

    Formula: kappa = dim(g) * (k + h^v) / (2 * h^v)

    This is the genus-1 shadow: F_1(A) = kappa * lambda_1^FP.
    """
    data = get_lie_data(label)
    k = Rational(level) if isinstance(level, (int, float)) else level
    return Rational(data.dimension) * (k + data.dual_coxeter) / (2 * data.dual_coxeter)


# =========================================================================
# Known discriminant polynomials
# =========================================================================

def discriminant_sl2() -> Poly:
    r"""Delta_{sl_2}(x) = (1 - 3x)(1 + x) = 1 - 2x - 3x^2.

    PROVED (Riordan generating function algebraicity).
    """
    x = Symbol('x')
    return Poly(expand((1 - 3*x) * (1 + x)), x)


def discriminant_sl3() -> Poly:
    r"""Delta_{sl_3}(x) = (1 - 8x)(1 - 3x - x^2).

    CONJECTURAL (from conj:sl3-bar-gf).
    Expanded: 1 - 11x + 23x^2 + 8x^3.
    """
    x = Symbol('x')
    return Poly(expand((1 - 8*x) * (1 - 3*x - x**2)), x)


def discriminant_virasoro() -> Poly:
    r"""Delta_{Vir}(x) = (1 - 3x)(1 + x).

    Same as sl_2 family (DS-preserved).
    PROVED.
    """
    return discriminant_sl2()


def discriminant_w3() -> Poly:
    r"""Delta_{W_3}(x) = (1 - x)(1 - 3x - x^2).

    CONJECTURAL (from conj:w3-algebraicity).
    The DS-invariant factor (1-3x-x^2) is shared with sl_3.
    """
    x = Symbol('x')
    return Poly(expand((1 - x) * (1 - 3*x - x**2)), x)


def discriminant_betagamma() -> Poly:
    r"""Delta_{betagamma}(x) = (1 - 3x)(1 + x).

    Same branch locus as sl_2 and Virasoro.
    PROVED.
    """
    return discriminant_sl2()


# =========================================================================
# Kodaira-Spencer operator construction
# =========================================================================

@dataclass(frozen=True)
class KSOperator:
    """Kodaira-Spencer transport operator on H^red_1(A).

    Attributes:
        label: algebra label
        rank_plus_one: dimension of H^red_1 = rank(g) + 1
        matrix: the KS operator as a matrix (companion form)
        eigenvalues: eigenvalues of KS_g
        discriminant: Delta_g(x) = det(1 - x * KS_g)
        dominant_eigenvalue: largest eigenvalue (should equal dim(g))
    """

    label: str
    rank_plus_one: int
    matrix: Matrix
    eigenvalues: Tuple[object, ...]
    discriminant: Poly
    dominant_eigenvalue: object


def _companion_matrix_from_char_poly(coeffs: List) -> Matrix:
    r"""Build companion matrix from monic characteristic polynomial.

    Given char poly t^n - c_{n-1} t^{n-1} - ... - c_1 t - c_0 = 0,
    coeffs = [c_{n-1}, c_{n-2}, ..., c_1, c_0] (highest to lowest).

    The companion matrix has eigenvalues equal to the roots of the char poly.
    Convention: last column contains the coefficients [c_0, c_1, ..., c_{n-1}]^T.
    """
    n = len(coeffs)
    # coeffs[i] = coefficient of t^{n-1-i} in the non-leading part
    # So the char poly is t^n - coeffs[0]*t^{n-1} - coeffs[1]*t^{n-2} - ... - coeffs[n-1]
    # Standard companion: last column is [coeffs[n-1], coeffs[n-2], ..., coeffs[0]]
    rows = []
    for i in range(n):
        row = [Rational(0)] * n
        if i > 0:
            row[i - 1] = Rational(1)
        row[n - 1] = coeffs[n - 1 - i]
        rows.append(row)
    return Matrix(rows)


def _discriminant_to_char_poly_coeffs(disc_poly: Poly) -> List:
    r"""Convert discriminant Delta(x) to characteristic polynomial coefficients.

    If Delta(x) = det(1 - x*KS) = prod(1 - lambda_i * x), then the
    characteristic polynomial of KS is det(t*I - KS) = prod(t - lambda_i).

    The discriminant Delta(x) has x^0 coefficient = 1 (normalization).
    The coefficient of x^k in Delta(x) is (-1)^k * e_k(lambda_1, ..., lambda_n)
    where e_k is the k-th elementary symmetric polynomial.

    The char poly is t^n - e_1 * t^{n-1} + e_2 * t^{n-2} - ... + (-1)^n * e_n.

    We return [c_{n-1}, c_{n-2}, ..., c_0] where
    char poly = t^n - c_{n-1}*t^{n-1} - c_{n-2}*t^{n-2} - ... - c_0.
    So c_{n-1-k} = (-1)^{k+1} * e_{k+1} for the monic form.
    """
    x = Symbol('x')
    all_coeffs = disc_poly.all_coeffs()  # highest degree first

    # Reverse to get x^0, x^1, x^2, ...
    # Poly.all_coeffs() returns [leading, ..., constant]
    degree = disc_poly.degree()
    # Get coefficient of x^k for k = 0, 1, ..., degree
    coeffs_by_power = [Rational(0)] * (degree + 1)
    for i, c in enumerate(all_coeffs):
        coeffs_by_power[degree - i] = c

    n = degree
    # e_k = (-1)^k * coeffs_by_power[k]
    e = [(-1)**k * coeffs_by_power[k] for k in range(1, n + 1)]

    # char poly = t^n - e[0]*t^{n-1} + e[1]*t^{n-2} - ... + (-1)^n * e[n-1]
    # In the form t^n - c_{n-1}*t^{n-1} - c_{n-2}*t^{n-2} - ... - c_0:
    # c_{n-1-k} = (-1)^k * e[k]... actually:
    # Standard form: t^n + a_{n-1}*t^{n-1} + ... + a_0
    # where a_{n-1-k} = (-1)^{k+1} * e[k]
    # We want t^n - c_{n-1}*t^{n-1} - ... - c_0,
    # so c_{n-1} = e[0], c_{n-2} = -e[1], c_{n-3} = e[2], ...
    # i.e., c_{n-1-k} = (-1)^k * e[k]

    char_coeffs = []  # [c_{n-1}, c_{n-2}, ..., c_0]
    for k in range(n):
        char_coeffs.append((-1)**k * e[k])

    return char_coeffs


def build_ks_operator(label: str, disc_poly: Poly, eigenvalues: Tuple) -> KSOperator:
    """Build the KS operator from a discriminant polynomial and known eigenvalues."""
    degree = disc_poly.degree()
    char_coeffs = _discriminant_to_char_poly_coeffs(disc_poly)
    mat = _companion_matrix_from_char_poly(char_coeffs)

    # Dominant eigenvalue = max by absolute value among real eigenvalues
    # For our cases, the dominant eigenvalue is always real and positive
    dom = max(eigenvalues, key=lambda e: float(simplify(e)))

    return KSOperator(
        label=label,
        rank_plus_one=degree,
        matrix=mat,
        eigenvalues=eigenvalues,
        discriminant=disc_poly,
        dominant_eigenvalue=dom,
    )


def ks_sl2() -> KSOperator:
    r"""KS operator for sl_2.

    From prop:hred-sl2:
      T_rec = [[2, 3], [1, 0]]
      eigenvalues {3, -1}
      det(1 - x*T_rec) = (1-3x)(1+x)

    This is the PROVED case.
    """
    disc = discriminant_sl2()
    eigs = (Rational(3), Rational(-1))
    return build_ks_operator("sl_2", disc, eigs)


def ks_sl3() -> KSOperator:
    r"""KS operator for sl_3 (conjectural).

    Char poly: t^3 - 11t^2 + 23t + 8 = (t-8)(t^2-3t-1)
    Eigenvalues: {8, (3+sqrt(13))/2, (3-sqrt(13))/2}
    """
    disc = discriminant_sl3()
    eigs = (
        Rational(8),
        Rational(3, 2) + sqrt(Rational(13)) / 2,
        Rational(3, 2) - sqrt(Rational(13)) / 2,
    )
    return build_ks_operator("sl_3", disc, eigs)


def ks_virasoro() -> KSOperator:
    r"""KS operator for Virasoro (same discriminant as sl_2)."""
    disc = discriminant_virasoro()
    eigs = (Rational(3), Rational(-1))
    return build_ks_operator("virasoro", disc, eigs)


def ks_w3() -> KSOperator:
    r"""KS operator for W_3 (conjectural).

    Discriminant: (1-x)(1-3x-x^2)
    Eigenvalues: {1, (3+sqrt(13))/2, (3-sqrt(13))/2}
    """
    disc = discriminant_w3()
    eigs = (
        Rational(1),
        Rational(3, 2) + sqrt(Rational(13)) / 2,
        Rational(3, 2) - sqrt(Rational(13)) / 2,
    )
    return build_ks_operator("w3", disc, eigs)


# =========================================================================
# Verification functions
# =========================================================================

def verify_det_formula(ks: KSOperator) -> bool:
    r"""Verify det(I - x * KS_g) = Delta_g(x).

    This is the core identity of conj:discriminant-ks-operator.
    """
    x = Symbol('x')
    n = ks.rank_plus_one
    identity = eye(n)
    det_expr = det(identity - x * ks.matrix)
    det_poly = Poly(expand(det_expr), x)

    # Compare coefficient by coefficient
    disc_coeffs = ks.discriminant.all_coeffs()
    det_coeffs = det_poly.all_coeffs()

    if len(disc_coeffs) != len(det_coeffs):
        return False

    return all(simplify(a - b) == 0 for a, b in zip(disc_coeffs, det_coeffs))


def verify_rank_plus_one(label: str, ks: KSOperator) -> bool:
    r"""Verify dim H^red_1(A) = rank(g) + 1."""
    data = get_lie_data(label)
    return ks.rank_plus_one == data.rank + 1


def verify_dominant_eigenvalue(label: str, ks: KSOperator) -> bool:
    r"""Verify largest eigenvalue of KS_g = dim(g)."""
    data = get_lie_data(label)
    return simplify(ks.dominant_eigenvalue - data.dimension) == 0


def verify_eigenvalue_product(ks: KSOperator) -> bool:
    r"""Verify product of eigenvalues = (-1)^n * Delta(0)... actually the
    product of eigenvalues = det(KS_g) = (-1)^n * constant term of char poly.

    From Delta(x) = det(1 - x*KS): Delta(0) = det(I) = 1.
    Product of eigenvalues = det(KS) = product of (reciprocals of roots of Delta).
    """
    prod_eigs = Rational(1)
    for e in ks.eigenvalues:
        prod_eigs *= e

    # det(KS) from matrix
    det_ks = det(ks.matrix)

    return simplify(prod_eigs - det_ks) == 0


def verify_eigenvalue_sum(ks: KSOperator) -> bool:
    r"""Verify trace(KS_g) = sum of eigenvalues = -coefficient of x in Delta / 1.

    From Delta(x) = prod(1 - lambda_i * x):
      coefficient of x = -sum(lambda_i) = -trace(KS_g).
    """
    sum_eigs = sum(ks.eigenvalues)
    trace_ks = ks.matrix.trace()

    return simplify(sum_eigs - trace_ks) == 0


# =========================================================================
# DS-invariance analysis
# =========================================================================

def ds_invariant_factor(disc_source: Poly, disc_target: Poly) -> Optional[Poly]:
    r"""Extract the DS-invariant factor shared between source and target discriminants.

    Under DS reduction g-hat -> W(g), the discriminant changes:
      Delta_{g-hat}(x) = (1 - dim(g)*x) * Delta_inv(x)
      Delta_{W(g)}(x)  = (1 - c_W*x) * Delta_inv(x)
    where Delta_inv is the shared DS-invariant part.

    We extract this by polynomial GCD.
    """
    x = Symbol('x')
    from sympy import gcd as sym_gcd

    p1 = disc_source.as_expr()
    p2 = disc_target.as_expr()

    g = sym_gcd(Poly(p1, x), Poly(p2, x))
    if g.degree() > 0:
        return g
    return None


def ds_pair_analysis(label_source: str, label_target: str,
                     ks_source: KSOperator, ks_target: KSOperator) -> Dict:
    r"""Analyze a DS pair (g-hat, W(g)) for discriminant preservation.

    Returns a dictionary with:
      - shared_factor: the GCD polynomial
      - source_specific: the non-shared factor of the source
      - target_specific: the non-shared factor of the target
      - shared_eigenvalues: eigenvalues from the shared factor
      - ds_invariant: whether the shared factor matches expectation
    """
    x = Symbol('x')
    shared = ds_invariant_factor(ks_source.discriminant, ks_target.discriminant)

    # Factor out the shared part
    src_expr = ks_source.discriminant.as_expr()
    tgt_expr = ks_target.discriminant.as_expr()

    if shared is not None and shared.degree() > 0:
        shared_expr = shared.as_expr()
        src_specific = Poly(simplify(src_expr / shared_expr), x)
        tgt_specific = Poly(simplify(tgt_expr / shared_expr), x)

        # Shared eigenvalues = reciprocals of roots of shared factor
        shared_roots = solve(shared_expr, x)
        shared_eigs = [Rational(1) / r for r in shared_roots if r != 0]
    else:
        src_specific = ks_source.discriminant
        tgt_specific = ks_target.discriminant
        shared_eigs = []

    return {
        "shared_factor": shared,
        "source_specific": src_specific,
        "target_specific": tgt_specific,
        "shared_eigenvalues": shared_eigs,
        "n_shared": len(shared_eigs),
    }


# =========================================================================
# Recurrence generation from KS operator
# =========================================================================

def generate_dims_from_ks(ks: KSOperator, initial: List[int], n_terms: int) -> List[int]:
    r"""Generate bar cohomology dimension sequence from the KS recurrence.

    The KS operator encodes a linear recurrence via its characteristic polynomial.
    Given initial values a_1, ..., a_d (where d = rank+1 = degree of discriminant),
    generate subsequent terms.

    For sl_2: a(n) = 2*a(n-1) + 3*a(n-2)  (from char poly t^2 - 2t - 3)
    For sl_3: a(n) = 11*a(n-1) - 23*a(n-2) - 8*a(n-3)
    """
    d = ks.rank_plus_one
    # The char poly of KS is t^d - c_{d-1}*t^{d-1} - ... - c_0
    # The recurrence is: a(n) = c_{d-1}*a(n-1) + c_{d-2}*a(n-2) + ... + c_0*a(n-d)
    char_coeffs = _discriminant_to_char_poly_coeffs(ks.discriminant)
    # char_coeffs = [c_{d-1}, c_{d-2}, ..., c_0]

    a = list(initial[:d])
    for _ in range(n_terms - d):
        next_val = sum(int(char_coeffs[k]) * a[-(k+1)] for k in range(d))
        a.append(next_val)
    return a[:n_terms]


def verify_recurrence_against_known(ks: KSOperator, known_dims: List[int]) -> bool:
    r"""Check that the KS recurrence reproduces known bar cohomology dimensions."""
    d = ks.rank_plus_one
    if len(known_dims) <= d:
        return True  # not enough data to check

    generated = generate_dims_from_ks(ks, known_dims[:d], len(known_dims))
    return generated == known_dims


# =========================================================================
# sl_N family predictions
# =========================================================================

def predicted_ks_degree(label: str) -> int:
    r"""Predicted degree of the discriminant = rank(g) + 1."""
    data = get_lie_data(label)
    return data.rank + 1


def predicted_dominant_eigenvalue(label: str) -> int:
    r"""Predicted dominant eigenvalue of KS_g = dim(g)."""
    data = get_lie_data(label)
    return data.dimension


def sl_n_dim(n: int) -> int:
    """Dimension of sl_n = n^2 - 1."""
    return n**2 - 1


def sl_n_rank(n: int) -> int:
    """Rank of sl_n = n - 1."""
    return n - 1


def sl_n_ks_prediction(n: int) -> Dict:
    r"""Predictions from conj:discriminant-ks-operator for sl_n.

    Returns:
      - discriminant_degree: n - 1 + 1 = n (rank + 1)
      - dominant_eigenvalue: n^2 - 1 (dim sl_n)
      - ks_dimension: n (rank + 1)
    """
    dim = sl_n_dim(n)
    rank = sl_n_rank(n)
    return {
        "n": n,
        "rank": rank,
        "dimension": dim,
        "discriminant_degree": rank + 1,
        "dominant_eigenvalue": dim,
        "ks_dimension": rank + 1,
    }


# =========================================================================
# Kappa-eigenvalue relationship
# =========================================================================

def kappa_at_special_level(label: str) -> Dict:
    r"""Compute kappa at levels where it equals dim(g) (the dominant eigenvalue).

    kappa(V_k(g)) = dim(g) * (k + h^v) / (2 * h^v)
    Setting kappa = dim(g): dim(g) = dim(g) * (k + h^v) / (2*h^v)
    => 1 = (k + h^v)/(2*h^v)
    => k + h^v = 2*h^v
    => k = h^v

    So kappa = dim(g) exactly at k = h^v (the "self-dual" level).
    """
    data = get_lie_data(label)

    # Level where kappa = dim(g)
    k_self_dual = data.dual_coxeter

    # Verify
    kappa_val = kappa_affine(label, k_self_dual)

    return {
        "label": label,
        "k_self_dual": k_self_dual,
        "kappa_at_k_self_dual": kappa_val,
        "dim_g": data.dimension,
        "match": simplify(kappa_val - data.dimension) == 0,
    }


def kappa_eigenvalue_table(label: str, levels: List[int]) -> List[Dict]:
    r"""Compute kappa at various levels and compare with dominant eigenvalue.

    The dominant eigenvalue dim(g) is level-INDEPENDENT (it is a property
    of the growth rate of bar cohomology, which is determined by the
    algebraic structure of g, not the level k).

    kappa varies with k; the dominant eigenvalue does not.
    """
    data = get_lie_data(label)
    results = []
    for k in levels:
        kappa_val = kappa_affine(label, k)
        results.append({
            "k": k,
            "kappa": kappa_val,
            "dominant_eig": data.dimension,
            "ratio": simplify(kappa_val / data.dimension),
        })
    return results


# =========================================================================
# Growth rate analysis
# =========================================================================

def asymptotic_growth_rate(ks: KSOperator) -> object:
    r"""Dominant growth rate of bar cohomology dimensions.

    dim H^n(B(A)) ~ C * lambda_max^n * n^{-3/2}
    where lambda_max = max eigenvalue of KS_g = dim(g).

    Returns the dominant eigenvalue.
    """
    return ks.dominant_eigenvalue


def growth_rate_check(label: str, known_dims: List[int], n_check: int = 5) -> List[float]:
    r"""Check convergence of ratio a(n)/a(n-1) to the dominant eigenvalue.

    For n large: a(n)/a(n-1) -> lambda_max = dim(g).
    """
    data = get_lie_data(label)
    ratios = []
    for i in range(1, min(n_check + 1, len(known_dims))):
        if known_dims[i-1] != 0:
            ratios.append(float(known_dims[i]) / float(known_dims[i-1]))
    return ratios


# =========================================================================
# Higher-rank predictions (sl_4, so_5, G_2)
# =========================================================================

def sl4_ks_prediction() -> Dict:
    r"""Prediction for sl_4 from conj:discriminant-ks-operator.

    sl_4: rank 3, dim 15
    Predicted:
      - H^red_1 dimension: 4
      - Dominant eigenvalue: 15
      - Discriminant degree: 4
      - Char poly: t^4 - (15 + subdominant sum) * t^3 + ...
    """
    return sl_n_ks_prediction(4)


def so5_ks_prediction() -> Dict:
    r"""Prediction for so_5 (= B_2 = sp_4) from conj:discriminant-ks-operator.

    so_5: rank 2, dim 10
    Predicted:
      - H^red_1 dimension: 3
      - Dominant eigenvalue: 10
      - Discriminant degree: 3
    """
    data = get_lie_data("so_5")
    return {
        "label": "so_5",
        "rank": data.rank,
        "dimension": data.dimension,
        "discriminant_degree": data.rank + 1,
        "dominant_eigenvalue": data.dimension,
        "ks_dimension": data.rank + 1,
    }


def g2_ks_prediction() -> Dict:
    r"""Prediction for G_2 from conj:discriminant-ks-operator.

    G_2: rank 2, dim 14
    Predicted:
      - H^red_1 dimension: 3
      - Dominant eigenvalue: 14
      - Discriminant degree: 3
    """
    data = get_lie_data("G_2")
    return {
        "label": "G_2",
        "rank": data.rank,
        "dimension": data.dimension,
        "discriminant_degree": data.rank + 1,
        "dominant_eigenvalue": data.dimension,
        "ks_dimension": data.rank + 1,
    }


# =========================================================================
# Picard-Fuchs D-module connection (prop:hred-sl2)
# =========================================================================

def picard_fuchs_sl2() -> Dict:
    r"""Picard-Fuchs operator for the sl_2 bar GF (prop:hred-sl2).

    The Riordan GF R(x) satisfies x(1+x)R^2 - (1+x)R + 1 = 0.
    Differentiating and eliminating R gives the order-2 ODE:
      L = (1 - 2x - 3x^2)*D_x^2 + (-1 + 3x)*D_x + 1
    where D_x = d/dx.

    Regular singular points: x = 1/3, x = -1, x = infinity.
    Local exponents at each singular point determine monodromy.

    The fiber at x=0 is H^red_1 = Q^2.
    """
    x = Symbol('x')
    # Singular points = roots of leading coefficient (1-2x-3x^2) = (1-3x)(1+x)
    leading = (1 - 3*x) * (1 + x)
    singular_pts = solve(leading, x)

    return {
        "order": 2,
        "leading_coeff": leading,
        "singular_points": singular_pts,
        "fiber_dim": 2,
        "companion_matrix": Matrix([[2, 3], [1, 0]]),
        "eigenvalues": (Rational(3), Rational(-1)),
    }


# =========================================================================
# Complete conjecture verification suite
# =========================================================================

def full_verification(label: str, ks: KSOperator, known_dims: Optional[List[int]] = None) -> Dict:
    r"""Run all verification checks for a given KS operator.

    Returns a dictionary of check results.
    """
    results = {
        "label": label,
        "det_formula": verify_det_formula(ks),
        "rank_plus_one": verify_rank_plus_one(label, ks),
        "dominant_eigenvalue": verify_dominant_eigenvalue(label, ks),
        "eigenvalue_product": verify_eigenvalue_product(ks),
        "eigenvalue_sum": verify_eigenvalue_sum(ks),
    }

    if known_dims is not None:
        results["recurrence_match"] = verify_recurrence_against_known(ks, known_dims)

    return results
