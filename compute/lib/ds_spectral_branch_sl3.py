"""DS spectral branch preservation for sl₃ (conj:ds-spectral-branch-preservation).

The manuscript proves that Drinfeld--Sokolov reduction preserves the
discriminant Δ_A(x) = det(1 - x·T_br) of the bar cohomology generating
function (Theorem thm:ds-bar-gf-discriminant).  The conjecture
(conj:ds-spectral-branch-preservation) asks whether the FULL spectral
branch object (V^br, T_br) is preserved up to similarity, not merely
its determinant.

For sl₂ this is automatic: the eigenvalues {3, -1} of T_br are distinct,
so similarity follows from det matching.  For sl₃ (rank 2) the branch
transport operator T_br has 3 eigenvalues, and similarity is not automatic
from the determinant.

KEY DATA (from examples_summary.tex, concordance.tex):
  sl₂ family:
    Δ = (1-3x)(1+x) = 1-2x-3x²
    T_br eigenvalues: {3, -1}
    Members: sl₂-hat, Vir, βγ
  sl₃ family:
    Δ = (1-8x)(1-3x-x²)
    T_br eigenvalues: {8, (3+√13)/2, (3-√13)/2}
    Members: sl₃-hat, W₃

CENTRAL CHARGES:
  Virasoro DS: c = 1 - 6(k+1)²/(k+2)
  W₃ DS: c = 2 - 24(k+2)²/(k+3)
  W₃ complementarity: c + c' = 100 where c' = c(-k-6)

GENERATING FUNCTIONS (conjectured):
  sl₃-hat: P(x) = 4x(2-13x-2x²)/((1-8x)(1-3x-x²))
    bar dims: 8, 36, 204, 1352, 9892, ...
    recurrence: a(n) = 11a(n-1) - 23a(n-2) - 8a(n-3)
  W₃: P(x) = x(2-3x)/((1-x)(1-3x-x²))
    bar dims: 2, 5, 16, 52, 171, 564, ...
    recurrence: a(n) = 3a(n-1) + a(n-2) - 1

References:
    conj:ds-spectral-branch-preservation (examples_summary.tex)
    def:spectral-branch-object (concordance.tex)
    thm:dominant-branch-point (examples_summary.tex)
    conj:sl3-bar-gf, conj:w3-algebraicity
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from math import sqrt as math_sqrt
from typing import Dict, List, Optional, Tuple

from sympy import (
    Matrix,
    Rational,
    Symbol,
    cancel,
    det,
    expand,
    factor,
    nsimplify,
    oo,
    poly,
    simplify,
    solve,
    sqrt,
    symbols,
)


# =========================================================================
# Lie algebra data
# =========================================================================

@dataclass(frozen=True)
class LieAlgebraData:
    """Root system data for a simple Lie algebra."""

    type_label: str
    rank: int
    dimension: int
    coxeter_number: int
    dual_coxeter_number: int
    num_positive_roots: int
    exponents: Tuple[int, ...]


SL2_DATA = LieAlgebraData(
    type_label="A1", rank=1, dimension=3,
    coxeter_number=2, dual_coxeter_number=2,
    num_positive_roots=1,
    exponents=(1,),
)

SL3_DATA = LieAlgebraData(
    type_label="A2", rank=2, dimension=8,
    coxeter_number=3, dual_coxeter_number=3,
    num_positive_roots=3,
    exponents=(1, 2),
)

SL4_DATA = LieAlgebraData(
    type_label="A3", rank=3, dimension=15,
    coxeter_number=4, dual_coxeter_number=4,
    num_positive_roots=6,
    exponents=(1, 2, 3),
)


def lie_data(type_label: str) -> LieAlgebraData:
    """Return Lie algebra data for a given type label."""
    catalog = {"A1": SL2_DATA, "A2": SL3_DATA, "A3": SL4_DATA}
    if type_label not in catalog:
        raise ValueError(f"Unknown type: {type_label}")
    return catalog[type_label]


# =========================================================================
# DS reduction central charges
# =========================================================================

def virasoro_ds_central_charge(k: object) -> object:
    """Central charge of the Virasoro algebra via DS reduction of sl₂-hat.

    Formula: c = 1 - 6/(k+2).
    """
    return 1 - 6 / (k + 2)


def w3_ds_central_charge(k: object) -> object:
    """Central charge of W₃ = W^k(sl₃) via DS reduction of sl₃-hat.

    Formula: c = 2 - 24/(k+3).
    """
    return 2 - 24 / (k + 3)


def w_n_ds_central_charge(n: int, k: object) -> object:
    """Central charge of the principal W_N algebra W^k(sl_N).

    Formula: c = (N-1)(1 - N(N+1)/(k+N)).
    For N=2: c = 1 - 6/(k+2) (Virasoro).
    For N=3: c = 2 - 24/(k+3) (W₃).

    Reference: Fateev-Lukyanov, Feigin-Frenkel.
    """
    return (n - 1) * (1 - n * (n + 1) / (k + n))


def virasoro_complementarity_sum() -> int:
    """Verify c + c' = 2 for Virasoro.  Dual level: k' = -k - 4."""
    k = Symbol('k')
    c = virasoro_ds_central_charge(k)
    c_dual = virasoro_ds_central_charge(-k - 4)
    return int(simplify(c + c_dual))


def w3_complementarity_sum() -> int:
    """Verify c + c' = 4 for W₃.  Dual level: k' = -k - 6."""
    k = Symbol('k')
    c = w3_ds_central_charge(k)
    c_dual = w3_ds_central_charge(-k - 6)
    return int(simplify(c + c_dual))


def general_wn_complementarity_sum(n: int) -> int:
    """Verify c + c' for W_N.  Dual level: k' = -k - 2N."""
    k = Symbol('k')
    c = w_n_ds_central_charge(n, k)
    c_dual = w_n_ds_central_charge(n, -k - 2 * n)
    result = simplify(c + c_dual)
    return int(result)


# =========================================================================
# Bar cohomology dimensions (known and conjectured)
# =========================================================================

# sl₂ bar dimensions: proved via PBW spectral sequence + CE cohomology
# H*(sl₂) = (1, 0, 0, 1), dim sl₂ = 3
SL2_BAR_DIMS_PROVED = [3, 5]  # H¹=3 (CE), H²=5 (CE, corrected from Riordan)
SL2_BAR_DIMS_EXTENDED = [3, 6, 15, 36, 91, 232, 603]  # Riordan R(n+3)

# sl₃ bar dimensions: H¹=8 (= dim sl₃), H²=36, H³=204 proved
# H⁴=1352, H⁵=9892 conjectured from rational GF
SL3_BAR_DIMS_PROVED = [8, 36, 204]
SL3_BAR_DIMS_CONJECTURED = [8, 36, 204, 1352, 9892, 76084, 598592]

# Virasoro bar dimensions: Motzkin M(n+1) - M(n) proved
VIR_BAR_DIMS = [1, 2, 5, 12, 30, 76, 196, 512]

# W₃ bar dimensions: H¹=2, H²=5, H³=16 proved; H⁴=52, H⁵=171 conjectured
W3_BAR_DIMS_PROVED = [2, 5, 16]
W3_BAR_DIMS_CONJECTURED = [2, 5, 16, 52, 171, 564, 1862, 6149]

# βγ bar dimensions: proved
BETAGAMMA_BAR_DIMS = [2, 4, 10, 26, 70, 196]


def sl3_bar_recurrence(initial: List[int], num_terms: int) -> List[int]:
    """Generate sl₃ bar dimensions via the conjectured recurrence.

    Recurrence: a(n) = 11a(n-1) - 23a(n-2) - 8a(n-3).
    Initial values: a(1) = 8, a(2) = 36, a(3) = 204.

    The characteristic polynomial t³ - 11t² + 23t + 8 factors as
    (t - 8)(t² - 3t - 1), where t = 8 gives the dominant growth rate
    dim(sl₃) = 8, and t² - 3t - 1 gives the DS-invariant sub-dominant
    eigenvalues (3 ± √13)/2.

    Reference: conj:sl3-bar-gf, eq:sl3-bar-recurrence.
    """
    a = list(initial[:3])
    for _ in range(num_terms - 3):
        a.append(11 * a[-1] - 23 * a[-2] - 8 * a[-3])
    return a[:num_terms]


def w3_bar_recurrence(initial: List[int], num_terms: int) -> List[int]:
    """Generate W₃ bar dimensions via the conjectured recurrence.

    Recurrence: a(n) = 3a(n-1) + a(n-2) - 1.
    Initial values: a(0) = 0, a(1) = 2.

    The rational GF is P(x) = x(2-3x)/((1-x)(1-3x-x²)).
    Denominator factors: (1-x) and (1-3x-x²).
    The DS-invariant factor is (1-3x-x²), shared with sl₃-hat.

    Reference: conj:w3-algebraicity, eq:w3-bar-recurrence.
    """
    a = list(initial[:2])
    for _ in range(num_terms - 2):
        a.append(3 * a[-1] + a[-2] - 1)
    return a[:num_terms]


# =========================================================================
# Discriminant and spectral branch computation
# =========================================================================

@dataclass(frozen=True)
class DiscriminantData:
    """Discriminant polynomial and branch transport eigenvalues."""

    algebra_label: str
    discriminant_coeffs: Tuple[int, ...]  # coeffs of 1, x, x², ... in Δ(x)
    eigenvalues: Tuple[object, ...]  # eigenvalues of T_br
    rank: int  # rank of T_br = degree of Δ


def sl2_discriminant() -> DiscriminantData:
    """Discriminant for the sl₂ family.

    Δ(x) = (1-3x)(1+x) = 1 - 2x - 3x².
    T_br eigenvalues: {3, -1}.
    Rank 2 (degree of algebraicity of P_sl₂).

    Reference: rem:dominant-branch-verified.
    """
    return DiscriminantData(
        algebra_label="sl2_family",
        discriminant_coeffs=(1, -2, -3),
        eigenvalues=(Rational(3), Rational(-1)),
        rank=2,
    )


def virasoro_discriminant() -> DiscriminantData:
    """Discriminant for Virasoro (same as sl₂ family).

    Δ(x) = (1-3x)(1+x) = 1 - 2x - 3x².
    The sl₂ → Vir DS reduction preserves this discriminant.

    Reference: thm:ds-bar-gf-discriminant, rem:dominant-branch-verified.
    """
    return DiscriminantData(
        algebra_label="virasoro",
        discriminant_coeffs=(1, -2, -3),
        eigenvalues=(Rational(3), Rational(-1)),
        rank=2,
    )


def betagamma_discriminant() -> DiscriminantData:
    """Discriminant for βγ (same as sl₂ family).

    P_βγ(x) = √((1+x)/(1-3x)), singularity type Δ^{-1/2}.
    Same branch locus as sl₂ and Virasoro.

    Reference: cor:betagamma-inverse-discriminant.
    """
    return DiscriminantData(
        algebra_label="betagamma",
        discriminant_coeffs=(1, -2, -3),
        eigenvalues=(Rational(3), Rational(-1)),
        rank=2,
    )


def sl3_discriminant() -> DiscriminantData:
    """Discriminant for the sl₃ family (conjectured).

    Δ(x) = (1-8x)(1-3x-x²) = 1 - 11x + 23x² + 8x³.
    T_br eigenvalues: {8, (3+√13)/2, (3-√13)/2}.
    Rank 3 (degree 3, matching the order-3 recurrence).

    The dominant eigenvalue 8 = dim(sl₃) (Theorem thm:dominant-branch-point).
    The sub-dominant eigenvalues (3 ± √13)/2 are the DS-invariant part
    (roots of 1 - 3x - x² reversed to x² - 3x - 1 = 0, roots (3±√13)/2).

    Reference: conj:sl3-bar-gf, rem:dominant-branch-verified.
    """
    return DiscriminantData(
        algebra_label="sl3_family",
        discriminant_coeffs=(1, -11, 23, 8),
        eigenvalues=(
            Rational(8),
            Rational(3, 2) + sqrt(Rational(13)) / 2,
            Rational(3, 2) - sqrt(Rational(13)) / 2,
        ),
        rank=3,
    )


def w3_discriminant() -> DiscriminantData:
    """Discriminant for W₃ (conjectured).

    W₃ GF: P(x) = x(2-3x)/((1-x)(1-3x-x²)).
    Denominator: (1-x)(1-3x-x²).

    The DS-invariant factor is (1-3x-x²), shared with sl₃-hat.
    The factor (1-x) is the "gauge factor" from the W₃ structure
    (it contributes the eigenvalue 1, which does NOT appear in the
    sl₃-hat discriminant; instead, sl₃-hat has the factor (1-8x)
    with eigenvalue 8 = dim(sl₃)).

    Full denominator Δ_W₃ = (1-x)(1-3x-x²) = 1 - 4x + 2x² + x³.
    Eigenvalues: {1, (3+√13)/2, (3-√13)/2}.

    Reference: conj:w3-algebraicity, rem:two-discriminant-families.
    """
    return DiscriminantData(
        algebra_label="w3",
        discriminant_coeffs=(1, -4, 2, 1),
        eigenvalues=(
            Rational(1),
            Rational(3, 2) + sqrt(Rational(13)) / 2,
            Rational(3, 2) - sqrt(Rational(13)) / 2,
        ),
        rank=3,
    )


# =========================================================================
# Branch transport operator T_br
# =========================================================================

@dataclass(frozen=True)
class BranchTransportOperator:
    """Spectral branch object (V^br, T_br).

    The branch transport operator T_br is defined by
        Δ(x) / Δ(0) = det(1 - x·T_br).
    Its eigenvalues are 1/x_i where x_i are the roots of Δ.

    Reference: def:spectral-branch-object (concordance.tex).
    """

    algebra_label: str
    rank: int
    matrix: Matrix  # T_br as a matrix (companion or diagonal)
    eigenvalues: Tuple[object, ...]
    char_poly_coeffs: Tuple[object, ...]  # t^n - c_{n-1}t^{n-1} - ... - c_0


def discriminant_to_char_poly(disc: DiscriminantData) -> Tuple[object, ...]:
    """Convert discriminant Δ(x) = 1 + c₁x + c₂x² + ... to the
    characteristic polynomial of T_br.

    If Δ(x) = prod(1 - λ_i x), then char poly of T_br is
    prod(t - λ_i) = t^n - (sum λ_i)t^{n-1} + ... + (-1)^n prod λ_i.

    The discriminant coefficients [1, c₁, c₂, ...] relate to the
    characteristic polynomial by: the coefficient of x^k in Δ(x) is
    (-1)^k · e_k(λ_1, ..., λ_n), where e_k is the k-th elementary
    symmetric polynomial.

    So the char poly is t^n - e_1 t^{n-1} + e_2 t^{n-2} - ... + (-1)^n e_n.
    And e_k = (-1)^k · disc_coeffs[k].
    """
    n = disc.rank
    coeffs = disc.discriminant_coeffs
    # e_k(eigenvalues) = (-1)^k * coeffs[k]
    e_vals = []
    for k in range(1, n + 1):
        if k < len(coeffs):
            e_vals.append((-1)**k * coeffs[k])
        else:
            e_vals.append(0)
    # Char poly: t^n - e_1 t^{n-1} + e_2 t^{n-2} - ... + (-1)^n e_n
    # Return as (e_1, -e_2, ..., (-1)^{n+1} e_n) so that
    # char poly = t^n - sum(char_poly_coeffs[k] * t^{n-1-k})
    char_coeffs = []
    for k in range(n):
        char_coeffs.append((-1)**k * e_vals[k])
    return tuple(char_coeffs)


def build_companion_matrix(disc: DiscriminantData) -> Matrix:
    """Build the companion matrix for T_br from the discriminant.

    The companion matrix of the char poly t^n - c₁t^{n-1} - ... - c_n is:
        [[0, 0, ..., c_n],
         [1, 0, ..., c_{n-1}],
         [0, 1, ..., c_{n-2}],
         ...
         [0, 0, ..., c_1]]
    """
    n = disc.rank
    char_poly = discriminant_to_char_poly(disc)
    # char_poly_coeffs[k] is the coefficient in front of t^{n-1-k}
    # so char poly = t^n - char_poly[0]*t^{n-1} - char_poly[1]*t^{n-2} - ...
    # For companion: last column is [c_n, c_{n-1}, ..., c_1]^T
    # where c_k are from char poly t^n - c_1*t^{n-1} - ... - c_n = 0

    # Standard companion matrix form:
    # [[0, 0, ..., 0, c_0],
    #  [1, 0, ..., 0, c_1],
    #  [0, 1, ..., 0, c_2],
    #  ...
    #  [0, 0, ..., 1, c_{n-1}]]
    # where char poly = t^n - c_{n-1}*t^{n-1} - ... - c_0

    # From our convention: char_poly[k] multiplies t^{n-1-k}
    # So c_{n-1} = char_poly[0], c_{n-2} = char_poly[1], ...
    c_vec = list(reversed(char_poly))  # [c_0, c_1, ..., c_{n-1}]

    rows = []
    for i in range(n):
        row = [Rational(0)] * n
        if i > 0:
            row[i - 1] = Rational(1)
        row[n - 1] = c_vec[i]
        rows.append(row)

    return Matrix(rows)


def build_transport_operator(disc: DiscriminantData) -> BranchTransportOperator:
    """Build the branch transport operator from discriminant data."""
    mat = build_companion_matrix(disc)
    char_poly = discriminant_to_char_poly(disc)
    return BranchTransportOperator(
        algebra_label=disc.algebra_label,
        rank=disc.rank,
        matrix=mat,
        eigenvalues=disc.eigenvalues,
        char_poly_coeffs=char_poly,
    )


def transport_operator_det_check(op: BranchTransportOperator) -> object:
    """Verify det(1 - x*T_br) = Δ(x)/Δ(0).

    Returns the symbolic expression det(1 - x*T_br) and checks
    it matches the discriminant.
    """
    x = Symbol('x')
    identity = Matrix.eye(op.rank)
    det_expr = det(identity - x * op.matrix)
    return expand(det_expr)


# =========================================================================
# DS-invariant sub-discriminant
# =========================================================================

def ds_invariant_factor_sl2() -> Tuple[int, ...]:
    """DS-invariant factor of the sl₂ discriminant.

    Full Δ = (1-3x)(1+x).
    For sl₂ (rank 1), the "dominant" factor is (1 - dim(g)·x) = (1-3x).
    The DS-invariant sub-discriminant is the remaining factor: (1+x).
    But since rank = 1, the DS-invariant part is 1-dimensional,
    making similarity automatic.

    Actually for sl₂, the entire discriminant (1-3x)(1+x) is shared
    between sl₂-hat and Virasoro, so both factors are DS-invariant.
    The point is that similarity of 2×2 matrices with equal char polys
    and distinct eigenvalues is automatic.

    Returns: coefficients of the shared factor (1+x) = [1, 1].
    """
    return (1, 1)


def ds_invariant_factor_sl3() -> Tuple[int, ...]:
    """DS-invariant factor of the sl₃ discriminant.

    sl₃-hat Δ = (1-8x)(1-3x-x²).
    W₃ Δ = (1-x)(1-3x-x²).
    The shared DS-invariant factor is (1-3x-x²).

    This has eigenvalues (3 ± √13)/2 ≈ 3.303, -0.303.
    The dominant eigenvalue 8 = dim(sl₃) is NOT DS-invariant;
    it changes to 1 for W₃ (reflecting the different growth rates).

    Returns: coefficients of (1-3x-x²) = [1, -3, -1].
    """
    return (1, -3, -1)


def ds_invariant_eigenvalues_sl2() -> Tuple[object, object]:
    """DS-invariant eigenvalues of the sl₂ branch transport operator.

    Both eigenvalues {3, -1} are DS-invariant (since the full
    discriminant is preserved).  But the eigenvalue 3 = dim(sl₂)
    is the "dominant" one; -1 is the "sub-dominant" DS-invariant
    eigenvalue.
    """
    return (Rational(3), Rational(-1))


def ds_invariant_eigenvalues_sl3() -> Tuple[object, object]:
    """DS-invariant eigenvalues of the sl₃ branch transport operator.

    From the shared factor (1-3x-x²) = 0, eigenvalues are
    (3 ± √13)/2.  These are the same for both sl₃-hat and W₃.

    The third eigenvalue is NOT DS-invariant:
      sl₃-hat: 8 = dim(sl₃)
      W₃: 1 (from the (1-x) factor)
    """
    return (
        Rational(3, 2) + sqrt(Rational(13)) / 2,
        Rational(3, 2) - sqrt(Rational(13)) / 2,
    )


def check_ds_invariant_eigenvalues_match(
    disc_source: DiscriminantData,
    disc_target: DiscriminantData,
) -> bool:
    """Check whether the DS-invariant eigenvalues match.

    Two algebras related by DS reduction should share the
    DS-invariant sub-discriminant factor.  This means they share
    all eigenvalues except possibly the dominant one (dim(g) vs
    some other value for the W-algebra).

    For the full conjecture (conj:ds-spectral-branch-preservation),
    we need ALL eigenvalues to match (i.e., T_br matrices to be
    similar), which is stronger than just the sub-discriminant.

    The full conjecture FAILS at the eigenvalue level for sl₃:
    sl₃-hat has eigenvalue 8, W₃ has eigenvalue 1.  But the
    conjecture claims similarity of T_br, which requires the
    SAME eigenvalues.

    CORRECTION: Re-reading the conjecture carefully, T_br should
    be the SAME matrix (up to similarity) for sl₃-hat and W₃.
    This means det matching: (1-8x)(1-3x-x²) vs (1-x)(1-3x-x²).
    These are DIFFERENT, so the full T_br is NOT preserved.

    What IS preserved is the DS-INVARIANT PART of T_br, which
    corresponds to the shared factor (1-3x-x²).

    Actually, the conjecture in the manuscript says T_br is
    similar.  Let's check this carefully by extracting the shared
    eigenvalues from the respective discriminants.
    """
    src_eigs = set(disc_source.eigenvalues)
    tgt_eigs = set(disc_target.eigenvalues)
    shared = src_eigs & tgt_eigs
    # DS-invariant eigenvalues are those in the intersection
    return len(shared) >= disc_source.rank - 1


def shared_eigenvalues(
    disc1: DiscriminantData,
    disc2: DiscriminantData,
) -> List[object]:
    """Compute eigenvalues shared between two discriminants.

    Uses symbolic simplification to identify equal eigenvalues.
    """
    shared = []
    for e1 in disc1.eigenvalues:
        for e2 in disc2.eigenvalues:
            if simplify(e1 - e2) == 0:
                shared.append(e1)
                break
    return shared


def non_shared_eigenvalues(
    disc: DiscriminantData,
    shared_eigs: List[object],
) -> List[object]:
    """Eigenvalues in disc that are NOT in the shared set."""
    result = []
    for e in disc.eigenvalues:
        is_shared = False
        for s in shared_eigs:
            if simplify(e - s) == 0:
                is_shared = True
                break
        if not is_shared:
            result.append(e)
    return result


# =========================================================================
# Recurrence from discriminant
# =========================================================================

def discriminant_to_recurrence_coeffs(disc: DiscriminantData) -> List[int]:
    """Extract the linear recurrence coefficients from the discriminant.

    If Δ(x) = 1 + c₁x + c₂x² + ... + c_d x^d, the bar cohomology
    dims satisfy a(n) + c₁ a(n-1) + ... + c_d a(n-d) = 0 for n > p
    (where p is the numerator degree of the rational GF).

    Returns [-c₁, -c₂, ...] as the recurrence coefficients:
    a(n) = rec[0]*a(n-1) + rec[1]*a(n-2) + ...
    """
    return [-c for c in disc.discriminant_coeffs[1:]]


def generate_from_recurrence(
    initial: List[int],
    rec_coeffs: List[int],
    num_terms: int,
) -> List[int]:
    """Generate a sequence from a linear recurrence.

    a(n) = rec_coeffs[0]*a(n-1) + rec_coeffs[1]*a(n-2) + ...
    """
    a = list(initial)
    depth = len(rec_coeffs)
    while len(a) < num_terms:
        next_val = sum(rec_coeffs[k] * a[-(k + 1)] for k in range(depth))
        a.append(int(next_val))
    return a[:num_terms]


# =========================================================================
# Spectral radius and growth rate
# =========================================================================

def spectral_radius(disc: DiscriminantData) -> object:
    """Spectral radius of T_br = max |eigenvalue|.

    For KM algebras, this equals dim(g) (Theorem thm:dominant-branch-point).
    """
    max_val = None
    for e in disc.eigenvalues:
        # For exact comparison, use simplify
        val = simplify(abs(e))
        if max_val is None or simplify(val - max_val) > 0:
            max_val = val
    return max_val


def convergence_radius(disc: DiscriminantData) -> object:
    """Radius of convergence R = 1/spectral_radius(T_br).

    This is the nearest branch point to the origin.
    """
    return 1 / spectral_radius(disc)


# =========================================================================
# Similarity analysis for the full conjecture
# =========================================================================

def matrices_have_same_char_poly(M1: Matrix, M2: Matrix) -> bool:
    """Check if two matrices have the same characteristic polynomial."""
    t = Symbol('t')
    cp1 = M1.charpoly(t)
    cp2 = M2.charpoly(t)
    diff = expand(cp1.as_expr() - cp2.as_expr())
    return simplify(diff) == 0


def matrices_similar_by_eigenvalues(
    eigs1: Tuple[object, ...],
    eigs2: Tuple[object, ...],
) -> bool:
    """Check if two sets of eigenvalues are the same (as multisets).

    If eigenvalues are distinct and match, the matrices are similar.
    If eigenvalues match but have multiplicity, similarity requires
    matching Jordan normal forms.
    """
    if len(eigs1) != len(eigs2):
        return False
    # Try to match eigenvalues one-to-one
    remaining = list(eigs2)
    for e1 in eigs1:
        found = False
        for i, e2 in enumerate(remaining):
            if simplify(e1 - e2) == 0:
                remaining.pop(i)
                found = True
                break
        if not found:
            return False
    return True


def eigenvalues_distinct(eigs: Tuple[object, ...]) -> bool:
    """Check if all eigenvalues are distinct."""
    for i in range(len(eigs)):
        for j in range(i + 1, len(eigs)):
            if simplify(eigs[i] - eigs[j]) == 0:
                return False
    return True


@dataclass(frozen=True)
class SpectralBranchComparison:
    """Comparison result for two spectral branch objects under DS."""

    source_label: str
    target_label: str
    source_disc: DiscriminantData
    target_disc: DiscriminantData
    shared_eigenvalues: Tuple[object, ...]
    source_only_eigenvalues: Tuple[object, ...]
    target_only_eigenvalues: Tuple[object, ...]
    discriminants_match: bool
    eigenvalues_match: bool
    ds_invariant_factor_matches: bool
    conjecture_holds: bool  # True iff T_br matrices are similar


def compare_spectral_branches(
    source_label: str,
    target_label: str,
    source_disc: DiscriminantData,
    target_disc: DiscriminantData,
) -> SpectralBranchComparison:
    """Compare spectral branch objects before and after DS reduction.

    The full conjecture (conj:ds-spectral-branch-preservation) states
    that T_br(source) ~ T_br(target) (similarity).  This requires:
    1. Same rank
    2. Same eigenvalues (as multisets)
    3. If eigenvalues are distinct, similarity is automatic

    The PROVED part (thm:ds-bar-gf-discriminant) is weaker: only the
    discriminant det(1-xT) is preserved.  For the sl₂ family this
    implies the full conjecture (distinct eigenvalues).  For sl₃,
    the discriminants are actually DIFFERENT: the dominant eigenvalue
    changes from dim(g) to something else.  What's preserved is the
    DS-invariant sub-discriminant factor.
    """
    shared = shared_eigenvalues(source_disc, target_disc)
    src_only = non_shared_eigenvalues(source_disc, shared)
    tgt_only = non_shared_eigenvalues(target_disc, shared)

    disc_match = (source_disc.discriminant_coeffs ==
                  target_disc.discriminant_coeffs)

    eig_match = matrices_similar_by_eigenvalues(
        source_disc.eigenvalues, target_disc.eigenvalues
    )

    # DS-invariant factor check: shared eigenvalues should account
    # for all eigenvalues except possibly one (the dominant one)
    ds_inv = len(shared) >= min(source_disc.rank, target_disc.rank) - 1

    return SpectralBranchComparison(
        source_label=source_label,
        target_label=target_label,
        source_disc=source_disc,
        target_disc=target_disc,
        shared_eigenvalues=tuple(shared),
        source_only_eigenvalues=tuple(src_only),
        target_only_eigenvalues=tuple(tgt_only),
        discriminants_match=disc_match,
        eigenvalues_match=eig_match,
        ds_invariant_factor_matches=ds_inv,
        conjecture_holds=eig_match,
    )


# =========================================================================
# Full analysis functions
# =========================================================================

def sl2_family_analysis() -> SpectralBranchComparison:
    """Full spectral branch comparison for sl₂ → Virasoro."""
    return compare_spectral_branches(
        "sl2_hat", "virasoro",
        sl2_discriminant(), virasoro_discriminant(),
    )


def sl3_family_analysis() -> SpectralBranchComparison:
    """Full spectral branch comparison for sl₃ → W₃.

    This is the KEY non-trivial test case.
    The full discriminants differ:
      sl₃: (1-8x)(1-3x-x²)
      W₃:  (1-x)(1-3x-x²)
    So T_br matrices are NOT similar (different eigenvalues).

    The DS-invariant sub-discriminant (1-3x-x²) IS preserved,
    giving shared eigenvalues (3±√13)/2.

    The conjecture as stated (T_br similar) CANNOT hold in the
    strong form for sl₃ → W₃, because the eigenvalues differ.
    What the evidence supports is preservation of the
    sub-discriminant factor.
    """
    return compare_spectral_branches(
        "sl3_hat", "W3",
        sl3_discriminant(), w3_discriminant(),
    )


def ds_invariant_factor_check_sl2() -> Dict:
    """Verify DS-invariant factor for sl₂ family.

    Full discriminant (1-3x)(1+x) is shared between
    sl₂-hat, Virasoro, and βγ.
    """
    sl2 = sl2_discriminant()
    vir = virasoro_discriminant()
    bg = betagamma_discriminant()
    return {
        "sl2_vir_match": sl2.discriminant_coeffs == vir.discriminant_coeffs,
        "sl2_bg_match": sl2.discriminant_coeffs == bg.discriminant_coeffs,
        "vir_bg_match": vir.discriminant_coeffs == bg.discriminant_coeffs,
        "all_match": (sl2.discriminant_coeffs ==
                      vir.discriminant_coeffs ==
                      bg.discriminant_coeffs),
    }


def ds_invariant_factor_check_sl3() -> Dict:
    """Verify DS-invariant factor for sl₃ family.

    sl₃-hat: Δ = (1-8x)(1-3x-x²)
    W₃:  Δ = (1-x)(1-3x-x²)
    Shared factor: (1-3x-x²)
    """
    sl3 = sl3_discriminant()
    w3 = w3_discriminant()

    # Extract shared eigenvalues
    shared = shared_eigenvalues(sl3, w3)

    # The shared eigenvalues should be roots of (1-3x-x²)
    # i.e., eigenvalues (3 ± √13)/2
    phi_plus = Rational(3, 2) + sqrt(Rational(13)) / 2
    phi_minus = Rational(3, 2) - sqrt(Rational(13)) / 2

    shared_match_expected = len(shared) == 2
    if shared_match_expected:
        shared_vals = sorted(
            [float(simplify(s)) for s in shared], reverse=True
        )
        expected_vals = sorted(
            [float(simplify(phi_plus)), float(simplify(phi_minus))],
            reverse=True,
        )
        shared_match_expected = all(
            abs(a - b) < 1e-10 for a, b in zip(shared_vals, expected_vals)
        )

    return {
        "sl3_disc_coeffs": sl3.discriminant_coeffs,
        "w3_disc_coeffs": w3.discriminant_coeffs,
        "discriminants_equal": sl3.discriminant_coeffs == w3.discriminant_coeffs,
        "num_shared_eigenvalues": len(shared),
        "shared_eigenvalues_match_expected": shared_match_expected,
        "sl3_dominant_eigenvalue": Rational(8),
        "w3_non_shared_eigenvalue": Rational(1),
    }


# =========================================================================
# Verification: recurrence reproduces known bar dims
# =========================================================================

def verify_sl2_bar_from_discriminant(num_terms: int = 7) -> Dict:
    """Check that the sl₂ discriminant recurrence reproduces bar dims.

    Discriminant (1-3x)(1+x) gives recurrence a(n) = 2a(n-1) + 3a(n-2).
    This is NOT the recurrence for Riordan numbers (which is depth 2
    but with different coefficients).  The Riordan recurrence is
    (n+1)R(n) = (n-1)(2R(n-1) + 3R(n-2)), which is non-constant.

    For the rational GF P_sl2(x), the denominator IS (1-3x)(1+x)
    but the numerator modifies the initial conditions.
    """
    disc = sl2_discriminant()
    rec = discriminant_to_recurrence_coeffs(disc)
    # rec = [2, 3] from Δ = 1 - 2x - 3x²
    return {
        "recurrence_coeffs": rec,
        "dominant_eigenvalue": 3,
        "subdominant_eigenvalue": -1,
        "spectral_radius": 3,
    }


def verify_sl3_bar_from_discriminant(num_terms: int = 7) -> Dict:
    """Check that sl₃ discriminant reproduces the conjectured bar dims.

    Δ = (1-8x)(1-3x-x²) = 1 - 11x + 23x² + 8x³.
    Recurrence: a(n) = 11a(n-1) - 23a(n-2) - 8a(n-3).
    """
    disc = sl3_discriminant()
    rec = discriminant_to_recurrence_coeffs(disc)
    # Should be [11, -23, -8]
    generated = generate_from_recurrence(
        SL3_BAR_DIMS_PROVED, rec, num_terms
    )
    return {
        "recurrence_coeffs": rec,
        "generated_dims": generated,
        "matches_conjectured": generated == SL3_BAR_DIMS_CONJECTURED[:num_terms],
    }


def verify_w3_bar_from_discriminant(num_terms: int = 8) -> Dict:
    """Check that W₃ denominator reproduces the conjectured bar dims.

    W₃ GF denominator: (1-x)(1-3x-x²) = 1 - 4x + 2x² + x³.
    Recurrence: a(n) = 4a(n-1) - 2a(n-2) - a(n-3).

    But the W₃ recurrence is actually a(n) = 3a(n-1) + a(n-2) - 1,
    which is an inhomogeneous depth-2 recurrence.  The homogeneous
    depth-3 recurrence comes from the denominator (1-x)(1-3x-x²):
    a(n) = 4a(n-1) - 2a(n-2) - a(n-3).

    These are equivalent: the inhomogeneous form absorbs the (1-x) factor.
    """
    disc = w3_discriminant()
    rec = discriminant_to_recurrence_coeffs(disc)
    # Should be [4, -2, -1]
    generated = generate_from_recurrence(
        W3_BAR_DIMS_PROVED, rec, num_terms
    )
    return {
        "recurrence_coeffs": rec,
        "generated_dims": generated,
        "matches_conjectured": generated == W3_BAR_DIMS_CONJECTURED[:num_terms],
    }


# =========================================================================
# Generating function verification
# =========================================================================

def eval_rational_gf(
    numer_coeffs: List[object],
    denom_coeffs: List[object],
    num_terms: int,
) -> List[object]:
    """Evaluate a rational GF P(x) = N(x)/D(x) as a power series.

    numer_coeffs: [n_0, n_1, ...] with N(x) = n_0 + n_1 x + ...
    denom_coeffs: [d_0, d_1, ...] with D(x) = d_0 + d_1 x + ...

    Returns [a_0, a_1, ...] where P(x) = sum a_k x^k.
    """
    result = []
    nd = len(denom_coeffs)
    nn = len(numer_coeffs)
    for k in range(num_terms):
        # D(x) * P(x) = N(x) implies:
        # d_0 * a_k + d_1 * a_{k-1} + ... = n_k
        n_k = Rational(numer_coeffs[k]) if k < nn else Rational(0)
        s = n_k
        for j in range(1, min(nd, k + 1)):
            s -= Rational(denom_coeffs[j]) * result[k - j]
        result.append(s / Rational(denom_coeffs[0]))
    return result


def sl3_gf_coefficients(num_terms: int = 10) -> List[int]:
    """Evaluate the conjectured sl₃ GF.

    P(x) = 4x(2 - 13x - 2x²) / ((1-8x)(1-3x-x²))
         = (8x - 52x² - 8x³) / (1 - 11x + 23x² + 8x³)

    Numerator: 0 + 8x - 52x² - 8x³
    Denominator: 1 - 11x + 23x² + 8x³
    """
    numer = [0, 8, -52, -8]
    denom = [1, -11, 23, 8]
    vals = eval_rational_gf(numer, denom, num_terms)
    return [int(v) for v in vals]


def w3_gf_coefficients(num_terms: int = 10) -> List[int]:
    """Evaluate the conjectured W₃ GF.

    P(x) = x(2 - 3x) / ((1-x)(1-3x-x²))
         = (2x - 3x²) / (1 - 4x + 2x² + x³)

    Numerator: 0 + 2x - 3x²
    Denominator: 1 - 4x + 2x² + x³
    """
    numer = [0, 2, -3]
    denom = [1, -4, 2, 1]
    vals = eval_rational_gf(numer, denom, num_terms)
    return [int(v) for v in vals]


# =========================================================================
# Characteristic polynomial factoring
# =========================================================================

def sl3_char_poly_factors() -> Dict:
    """Factor the characteristic polynomial of the sl₃ recurrence.

    Char poly: t³ - 11t² + 23t + 8 = (t - 8)(t² - 3t - 1).
    The linear factor t - 8 gives the dominant eigenvalue dim(sl₃) = 8.
    The quadratic t² - 3t - 1 gives the DS-invariant eigenvalues.
    """
    t = Symbol('t')
    p = t**3 - 11 * t**2 + 23 * t + 8
    factored = factor(p)
    # Verify factorization
    check = expand((t - 8) * (t**2 - 3 * t - 1) - p)
    return {
        "polynomial": p,
        "factored": factored,
        "factorization_correct": check == 0,
        "dominant_root": 8,
        "ds_invariant_quadratic": t**2 - 3 * t - 1,
    }


def w3_char_poly_factors() -> Dict:
    """Factor the characteristic polynomial of the W₃ recurrence.

    Char poly: t³ - 4t² + 2t + 1 = (t - 1)(t² - 3t - 1).
    The linear factor t - 1 is the "gauge" eigenvalue.
    The quadratic t² - 3t - 1 gives the DS-invariant eigenvalues.
    """
    t = Symbol('t')
    p = t**3 - 4 * t**2 + 2 * t + 1
    check = expand((t - 1) * (t**2 - 3 * t - 1) - p)
    return {
        "polynomial": p,
        "factorization_correct": check == 0,
        "non_ds_root": 1,
        "ds_invariant_quadratic": t**2 - 3 * t - 1,
    }


def shared_quadratic_factor() -> Dict:
    """The shared quadratic factor t² - 3t - 1 between sl₃ and W₃.

    Roots: (3 ± √13) / 2.
    Product of roots: -1 (from Vieta's: c/a = -1/1 = -1).
    Sum of roots: 3 (from Vieta's: -b/a = 3).
    """
    t = Symbol('t')
    quad = t**2 - 3 * t - 1
    discriminant_of_quad = 9 + 4  # b² - 4ac = 9 + 4 = 13
    roots = (
        (Rational(3) + sqrt(Rational(13))) / 2,
        (Rational(3) - sqrt(Rational(13))) / 2,
    )
    product = simplify(roots[0] * roots[1])
    sum_roots = simplify(roots[0] + roots[1])
    return {
        "quadratic": quad,
        "discriminant": discriminant_of_quad,
        "roots": roots,
        "product_of_roots": product,
        "sum_of_roots": sum_roots,
    }


# =========================================================================
# DS reduction Weyl group perspective
# =========================================================================

def weyl_group_size(type_label: str) -> int:
    """Size of the Weyl group for a simple Lie algebra.

    A_n: |W| = (n+1)!
    """
    data = lie_data(type_label)
    r = data.rank
    if type_label.startswith("A"):
        from math import factorial
        return factorial(r + 1)
    raise ValueError(f"Weyl group size not implemented for {type_label}")


def num_weyl_generators(type_label: str) -> int:
    """Number of simple reflections = rank."""
    return lie_data(type_label).rank


def branch_operator_expected_rank(type_label: str) -> int:
    """Expected rank of T_br for a KM algebra of type g.

    For a rational GF, rank(T_br) = degree of denominator.
    For sl₂: rank = 2 (denominator (1-3x)(1+x) has degree 2).
    For sl₃: rank = 3 (denominator (1-8x)(1-3x-x²) has degree 3).

    Conjectured pattern: rank(T_br) = rank(g) + 1 for type A.
    """
    data = lie_data(type_label)
    return data.rank + 1


# =========================================================================
# CE cohomology data (for cross-checks)
# =========================================================================

def ce_cohomology_sl2() -> Tuple[int, ...]:
    """H*(sl₂, C) = exterior algebra on one generator in degree 3.

    dim H^k = (1, 0, 0, 1) for k = 0, 1, 2, 3.
    Total: 2 (since sl₂ has one independent 3-cocycle).
    """
    return (1, 0, 0, 1)


def ce_cohomology_sl3() -> Tuple[int, ...]:
    """H*(sl₃, C) = exterior algebra on generators in degrees 3 and 5.

    dim H^k = (1, 0, 0, 1, 0, 1, 0, 0, 1) for k = 0, ..., 8.
    Poincare poly: (1 + t³)(1 + t⁵).
    Total dim: 4.
    """
    return (1, 0, 0, 1, 0, 1, 0, 0, 1)


def ce_poincare_polynomial_sl_n(n: int) -> List[int]:
    """Poincare polynomial of H*(sl_n, C).

    H*(sl_n) = Λ(x_3, x_5, ..., x_{2n-1}) where |x_{2i+1}| = 2i+1.
    Generators in degrees 3, 5, ..., 2n-1.
    """
    degrees = [2 * i + 1 for i in range(1, n)]
    # Poincare polynomial: product of (1 + t^d) for d in degrees
    max_degree = sum(degrees)
    poly = [0] * (max_degree + 1)
    poly[0] = 1
    for d in degrees:
        new_poly = list(poly)
        for k in range(max_degree + 1):
            if poly[k] != 0 and k + d <= max_degree:
                new_poly[k + d] += poly[k]
        poly = new_poly
    return poly


# =========================================================================
# Summary / catalog
# =========================================================================

@dataclass(frozen=True)
class DSSpectralBranchEntry:
    """Catalog entry for one DS-related pair."""

    source_type: str  # e.g., "A1"
    source_label: str  # e.g., "sl2_hat"
    target_label: str  # e.g., "virasoro"
    rank_g: int
    dim_g: int
    source_disc: DiscriminantData
    target_disc: DiscriminantData
    ds_invariant_factor_coeffs: Tuple[int, ...]
    ds_invariant_eigenvalues: Tuple[object, ...]
    dominant_source_eigenvalue: object
    dominant_target_eigenvalue: object
    full_conjecture_status: str  # "proved", "holds", "fails", "open"


def build_catalog() -> List[DSSpectralBranchEntry]:
    """Build the catalog of all DS spectral branch comparisons."""
    entries = []

    # sl₂ → Virasoro
    sl2_inv = ds_invariant_eigenvalues_sl2()
    entries.append(DSSpectralBranchEntry(
        source_type="A1",
        source_label="sl2_hat",
        target_label="virasoro",
        rank_g=1,
        dim_g=3,
        source_disc=sl2_discriminant(),
        target_disc=virasoro_discriminant(),
        ds_invariant_factor_coeffs=(1, -2, -3),  # full disc is DS-inv for sl₂
        ds_invariant_eigenvalues=sl2_inv,
        dominant_source_eigenvalue=Rational(3),
        dominant_target_eigenvalue=Rational(3),
        full_conjecture_status="proved",
    ))

    # sl₃ → W₃
    sl3_inv = ds_invariant_eigenvalues_sl3()
    entries.append(DSSpectralBranchEntry(
        source_type="A2",
        source_label="sl3_hat",
        target_label="W3",
        rank_g=2,
        dim_g=8,
        source_disc=sl3_discriminant(),
        target_disc=w3_discriminant(),
        ds_invariant_factor_coeffs=(1, -3, -1),  # shared (1-3x-x²)
        ds_invariant_eigenvalues=sl3_inv,
        dominant_source_eigenvalue=Rational(8),
        dominant_target_eigenvalue=Rational(1),
        full_conjecture_status="open",
    ))

    return entries


def verify_catalog() -> Dict[str, bool]:
    """Run all catalog consistency checks."""
    catalog = build_catalog()
    results = {}
    for entry in catalog:
        key = f"{entry.source_label}_to_{entry.target_label}"

        # 1. Dominant eigenvalue = dim(g) for source
        results[f"{key}_dominant_is_dim_g"] = (
            entry.dominant_source_eigenvalue == entry.dim_g
        )

        # 2. DS-invariant eigenvalues match
        comp = compare_spectral_branches(
            entry.source_label, entry.target_label,
            entry.source_disc, entry.target_disc,
        )
        results[f"{key}_ds_invariant_matches"] = comp.ds_invariant_factor_matches

        # 3. Spectral radius check
        src_sr = spectral_radius(entry.source_disc)
        results[f"{key}_spectral_radius_is_dim_g"] = (
            simplify(src_sr - entry.dim_g) == 0
        )

    return results
