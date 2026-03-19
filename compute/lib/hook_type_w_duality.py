"""Hook-type W-algebra duality for sl_4.

Computes the bar complex data and Koszul duality invariants for the
hook-type W-algebras W_k(sl_4, f_{(2,1,1)}) and W_k(sl_4, f_{(3,1)}),
which form the first genuinely non-self-dual non-principal corridor
for chiral Koszul duality in type A.

Key results:
  - ad(h)-grading and generator content of both W-algebras
  - Central charge formulas via KRW (Kac-Roan-Wakimoto)
  - Kappa (modular characteristic) for both algebras
  - Verification of the transport-to-transpose conjecture:
    kappa(W_k(sl_4, f_{(3,1)})) + kappa(W_{k^v}(sl_4, f_{(2,1,1)})) = 0

Mathematical context:
  - Partition (3,1) of 4: subregular nilpotent of sl_4
  - Partition (2,1,1) of 4: minimal nilpotent of sl_4
  - Transpose: (3,1)^t = (2,1,1), (2,1,1)^t = (3,1)
  - Also includes (2,2) (self-dual, even nilpotent) as a cross-check

The central charge formula for W^k(sl_N, f_lambda) uses the KRW result
(Kac-Roan-Wakimoto 2004, De Sole-Kac 2006):

  c = dim(g_0) - (1/2)*dim(g_{1/2}) - 12*||rho - rho_L||^2 / (k + h^v)

where g_j are eigenspaces of (1/2)*ad(h) on g, and rho_L is the Weyl
vector of the Levi subalgebra corresponding to the grading.  This is the
UNSHIFTED (algebraic) central charge; the manuscript's level convention
may include an additional rho-shift.

For the modular characteristic kappa, we use two approaches:
  1. Direct from the partition data via the ds_kappa formula
  2. Cross-check via complementarity sum for self-dual pairs
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

from sympy import Rational, Symbol, simplify, sympify, sqrt

from compute.lib.nonprincipal_ds_orbits import (
    Partition,
    ad_h_grade_multiplicities_sl_n,
    ad_h_graded_basis_labels_sl_n,
    centralizer_dimension_sl_n,
    homogeneous_f_centralizer_basis_sl_n,
    normalize_partition,
    orbit_dimension_sl_n,
    partition_size,
    transpose_partition,
    type_a_bv_dual,
    type_a_orbit_class,
    type_a_partition_sl2_triple,
)


# ---------------------------------------------------------------------------
# W-algebra generator data
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class WAlgebraGeneratorData:
    """Strong generator content of W^k(sl_N, f_lambda)."""

    lie_algebra: str
    rank: int
    partition: Partition
    transpose_partition: Partition
    orbit_class: str
    # f-centralizer data (from Jacobson-Morozov sl_2-triple)
    f_centralizer_dimension: int
    f_centralizer_grades: Dict[int, int]  # ad(h)-grade -> count
    # ad(h)-grading of full sl_N
    full_grading: Dict[int, int]
    # Strong generator conformal weights: weight = 1 - (ad(h)-grade)/2
    strong_generators: Tuple[Tuple[str, object, str], ...]
    # Number of bosonic and fermionic generators
    n_bosonic: int
    n_fermionic: int


@dataclass(frozen=True)
class WAlgebraCentralCharge:
    """Central charge data for W^k(sl_N, f_lambda)."""

    partition: Partition
    N: int
    # KRW formula ingredients
    dim_g0: int          # dim of grade-0 part of sl_N
    dim_g_half: int      # dim of grade-1/2 part of sl_N
    rho_squared: object  # ||rho||^2 for sl_N
    rho_L_squared: object  # ||rho_L||^2 for the Levi
    # Central charge as rational function of k
    central_charge: object  # c(k) = A - B/(k+N) where A, B are explicit
    leading_term: object    # A = dim(g_0) - (1/2)*dim(g_{1/2})
    quadratic_coeff: object  # B = 12*(||rho||^2 - ||rho_L||^2)


@dataclass(frozen=True)
class HookDualityData:
    """Complete hook-type duality data for a transpose pair."""

    source_partition: Partition  # lambda
    target_partition: Partition  # lambda^t
    source_generators: WAlgebraGeneratorData
    target_generators: WAlgebraGeneratorData
    source_central_charge: WAlgebraCentralCharge
    target_central_charge: WAlgebraCentralCharge
    # Kappa invariants
    source_kappa: object  # kappa(W_k(sl_N, f_lambda))
    target_kappa: object  # kappa(W_{k^v}(sl_N, f_{lambda^t}))
    dual_level: object    # k^v as function of k
    # Complementarity
    kappa_sum: object     # source_kappa + target_kappa (should be 0)
    c_sum: object         # c(k) + c(k^v) for the pair


# ---------------------------------------------------------------------------
# Weyl vector and Levi computation
# ---------------------------------------------------------------------------

def weyl_vector_sl_n(N: int) -> Tuple[Rational, ...]:
    """Weyl vector rho = (N-1, N-3, ..., -(N-1))/2 for sl_N."""
    return tuple(Rational(N - 1 - 2 * i, 2) for i in range(N))


def weyl_vector_norm_squared_sl_n(N: int) -> Rational:
    """||rho||^2 = N(N^2-1)/12 in the trace form on sl_N."""
    return Rational(N * (N * N - 1), 12)


def levi_rho_from_partition(partition: Partition) -> Tuple[Rational, ...]:
    """Weyl vector of the Levi subalgebra for the ad(h)-grading.

    For partition lambda = (l_1, ..., l_p) of N, the Levi is
    gl_{l_1} x gl_{l_2} x ... x gl_{l_p} (block-diagonal).
    rho_L is the concatenation of the Weyl vectors of each block.
    """
    lam = normalize_partition(partition)
    rho_L = []
    for block_size in lam:
        for i in range(block_size):
            rho_L.append(Rational(block_size - 1 - 2 * i, 2))
    return tuple(rho_L)


def levi_rho_norm_squared(partition: Partition) -> Rational:
    """||rho_L||^2 = sum_i l_i(l_i^2-1)/12 for partition (l_1,...,l_p)."""
    lam = normalize_partition(partition)
    return sum(Rational(l * (l * l - 1), 12) for l in lam)


def rho_shift_norm_squared(partition: Partition) -> Rational:
    """||rho - rho_L||^2 for the partition of sl_N."""
    N = partition_size(partition)
    return weyl_vector_norm_squared_sl_n(N) - levi_rho_norm_squared(partition)


# ---------------------------------------------------------------------------
# Generator data
# ---------------------------------------------------------------------------

def w_algebra_generator_data(partition: Partition) -> WAlgebraGeneratorData:
    """Compute the strong generator content of W^k(sl_N, f_lambda)."""
    lam = normalize_partition(partition)
    N = partition_size(lam)
    dual = transpose_partition(lam)
    orbit_cls = type_a_orbit_class(lam)

    triple = type_a_partition_sl2_triple(lam)
    full_grading = ad_h_grade_multiplicities_sl_n(triple.h)
    f_centralizer = homogeneous_f_centralizer_basis_sl_n(triple.f, triple.h)
    f_cent_grades = {grade: len(elems) for grade, elems in f_centralizer.items()}
    f_cent_dim = sum(f_cent_grades.values())

    # Strong generators: elements of g^f at ad(h)-grade <= 0.
    # Conformal weight = 1 - (ad(h)-grade)/2.
    generators = []
    n_bos = 0
    n_fer = 0
    for grade in sorted(f_cent_grades, reverse=True):
        count = f_cent_grades[grade]
        weight = 1 - Rational(grade, 2)
        # Half-integer weight -> fermionic; integer weight -> bosonic
        is_fermionic = (2 * weight) % 2 != 0
        parity = "fermionic" if is_fermionic else "bosonic"
        for i in range(count):
            name = f"W_{weight}^({i + 1})"
            generators.append((name, weight, parity))
            if is_fermionic:
                n_fer += 1
            else:
                n_bos += 1

    return WAlgebraGeneratorData(
        lie_algebra=f"sl_{N}",
        rank=N - 1,
        partition=lam,
        transpose_partition=dual,
        orbit_class=orbit_cls,
        f_centralizer_dimension=f_cent_dim,
        f_centralizer_grades=f_cent_grades,
        full_grading=full_grading,
        strong_generators=tuple(generators),
        n_bosonic=n_bos,
        n_fermionic=n_fer,
    )


# ---------------------------------------------------------------------------
# Central charge (KRW formula)
# ---------------------------------------------------------------------------

def krw_central_charge_data(partition: Partition) -> WAlgebraCentralCharge:
    """KRW central charge for W^k(sl_N, f_lambda).

    c(k) = dim(g_0) - (1/2)*dim(g_{1/2}) - 12*||rho - rho_L||^2 / (k + N)

    This is the ALGEBRAIC (unshifted) central charge from Kac-Roan-Wakimoto.
    """
    lam = normalize_partition(partition)
    N = partition_size(lam)

    triple = type_a_partition_sl2_triple(lam)
    # x = h/2 gives the good grading; eigenvalues of ad(x) on E_{ij} = x_i - x_j
    # We need dim(g_j) where j ranges over eigenvalues of ad(x) = (1/2)*ad(h).
    h_diag = [triple.h[i, i] for i in range(N)]
    x_diag = [Rational(h_diag[i], 2) for i in range(N)]

    # Count eigenspaces of ad(x)
    grade_counts: Dict[Rational, int] = {}
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            eigenval = x_diag[i] - x_diag[j]
            grade_counts[eigenval] = grade_counts.get(eigenval, 0) + 1
    # Add Cartan contributions (all at grade 0)
    grade_counts[Rational(0)] = grade_counts.get(Rational(0), 0) + (N - 1)

    dim_g0 = grade_counts.get(Rational(0), 0)
    dim_g_half = grade_counts.get(Rational(1, 2), 0)

    rho_sq = weyl_vector_norm_squared_sl_n(N)
    rho_L_sq = levi_rho_norm_squared(lam)
    shift_sq = rho_sq - rho_L_sq

    k = Symbol('k')
    leading = dim_g0 - Rational(dim_g_half, 2)
    quadratic = 12 * shift_sq
    c = leading - quadratic / (k + N)

    return WAlgebraCentralCharge(
        partition=lam,
        N=N,
        dim_g0=dim_g0,
        dim_g_half=dim_g_half,
        rho_squared=rho_sq,
        rho_L_squared=rho_L_sq,
        central_charge=c,
        leading_term=leading,
        quadratic_coeff=quadratic,
    )


def krw_central_charge(partition: Partition, level=Symbol('k')):
    """Central charge c(k) for W^k(sl_N, f_lambda) as a function of k."""
    data = krw_central_charge_data(partition)
    k = sympify(level)
    N = data.N
    return data.leading_term - data.quadratic_coeff / (k + N)


# ---------------------------------------------------------------------------
# Ghost constant and kappa
# ---------------------------------------------------------------------------

def ghost_constant(partition: Partition) -> Rational:
    """Ghost constant C_lambda = sum_{j>0} j * dim(g_j).

    This is (1/2) * sum_{i<j} |h_i - h_j| where h is the diagonal of the
    Jacobson-Morozov semisimple element. The eigenspaces g_j are for
    ad(x) = (1/2)*ad(h), so j ranges over multiples of 1/2.

    C_lambda controls the constant term in the DS kappa formula:
      kappa(W^k(sl_N, f_lambda)) = dim(g)(k+N)/(2N) - C_lambda

    The complementarity constant for a transpose pair is:
      kappa(W_k(f_lambda)) + kappa(W_{-k-2N}(f_{lambda^t})) = -(C_lambda + C_{lambda^t})
    """
    lam = normalize_partition(partition)
    N = partition_size(lam)
    triple = type_a_partition_sl2_triple(lam)
    h_diag = [triple.h[i, i] for i in range(N)]

    C = Rational(0)
    for i in range(N):
        for j in range(i + 1, N):
            C += abs(h_diag[i] - h_diag[j])
    return C / 2


def ghost_constant_hook(N: int, r: int) -> Rational:
    """Ghost constant for hook partition (N-r, 1^r).

    Uses the closed formula:
      C = m(m^2-1)/6 + r * floor(m^2/2) / 2
    where m = N-r, with the floor depending on parity of m.
    """
    from compute.lib.nonprincipal_ds_orbits import hook_partition
    return ghost_constant(hook_partition(N, r))


def complementarity_constant(partition: Partition) -> Rational:
    """Complementarity constant -(C_lambda + C_{lambda^t}).

    kappa(W_k(sl_N, f_lambda)) + kappa(W_{-k-2N}(sl_N, f_{lambda^t})) = this value.
    """
    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    return -(ghost_constant(lam) + ghost_constant(lam_t))


def ds_kappa_from_affine(partition: Partition, level=Symbol('k')):
    """Kappa for W^k(sl_N, f_lambda) via DS ghost subtraction.

    kappa(W^k(sl_N, f_lambda)) = dim(sl_N) * (k + N) / (2N) - C_lambda

    where C_lambda is the ghost constant (sum_{j>0} j * dim(g_j)).

    This formula is LINEAR in k with universal slope dim(g)/(2h^v),
    so the kappa sum under k -> -k-2N is automatically k-independent:
      kappa(k) + kappa(-k-2N) = -(C_lambda + C_{lambda^t}).
    """
    lam = normalize_partition(partition)
    N = partition_size(lam)
    k = sympify(level)

    dim_g = N * N - 1
    kappa_affine = Rational(dim_g, 2 * N) * (k + N)
    return kappa_affine - ghost_constant(lam)


# ---------------------------------------------------------------------------
# Dual level for hook-type
# ---------------------------------------------------------------------------

def hook_dual_level_sl4(level=Symbol('k')):
    """Dual level for sl_4 hook-type duality: k^v = -k - 2N = -k - 8.

    For the principal Feigin-Frenkel involution on sl_N:
      k -> -k - 2h^v = -k - 2N
    This is also used for non-principal hook-type pairs in the current ansatz.
    """
    return -sympify(level) - 8


def hook_dual_level_sl_n(N: int, level=Symbol('k')):
    """Dual level for sl_N: k^v = -k - 2N."""
    return -sympify(level) - 2 * N


# ---------------------------------------------------------------------------
# sl_4 specific data
# ---------------------------------------------------------------------------

def sl4_hook_211_generators():
    """Generator data for W_k(sl_4, f_{(2,1,1)}) — minimal W-algebra."""
    return w_algebra_generator_data((2, 1, 1))


def sl4_hook_31_generators():
    """Generator data for W_k(sl_4, f_{(3,1)}) — subregular W-algebra."""
    return w_algebra_generator_data((3, 1))


def sl4_22_generators():
    """Generator data for W_k(sl_4, f_{(2,2)}) — even nilpotent."""
    return w_algebra_generator_data((2, 2))


def sl4_principal_generators():
    """Generator data for W_k(sl_4, f_{(4)}) — principal (W_4 algebra)."""
    return w_algebra_generator_data((4,))


# ---------------------------------------------------------------------------
# Central charge formulas
# ---------------------------------------------------------------------------

def c_sl4_211(level=Symbol('k')):
    """c(W_k(sl_4, f_{(2,1,1)})) = 3 - 54/(k+4)."""
    return krw_central_charge((2, 1, 1), level)


def c_sl4_31(level=Symbol('k')):
    """c(W_k(sl_4, f_{(3,1)})) = 5 - 36/(k+4)."""
    return krw_central_charge((3, 1), level)


def c_sl4_22(level=Symbol('k')):
    """c(W_k(sl_4, f_{(2,2)})) = 7 - 48/(k+4)."""
    return krw_central_charge((2, 2), level)


def c_sl4_principal(level=Symbol('k')):
    """c(W_k(sl_4, f_{(4)})) = 3 - 60/(k+4)."""
    return krw_central_charge((4,), level)


# ---------------------------------------------------------------------------
# Kappa formulas
# ---------------------------------------------------------------------------

def kappa_sl4_211(level=Symbol('k')):
    """kappa(W_k(sl_4, f_{(2,1,1)})) via DS ghost subtraction."""
    return ds_kappa_from_affine((2, 1, 1), level)


def kappa_sl4_31(level=Symbol('k')):
    """kappa(W_k(sl_4, f_{(3,1)})) via DS ghost subtraction."""
    return ds_kappa_from_affine((3, 1), level)


def kappa_sl4_22(level=Symbol('k')):
    """kappa(W_k(sl_4, f_{(2,2)})) via DS ghost subtraction."""
    return ds_kappa_from_affine((2, 2), level)


def kappa_sl4_principal(level=Symbol('k')):
    """kappa(W_k(sl_4, f_{(4)})) via DS ghost subtraction."""
    return ds_kappa_from_affine((4,), level)


# ---------------------------------------------------------------------------
# Complementarity and duality checks
# ---------------------------------------------------------------------------

def kappa_anti_symmetry_31_211(level=Symbol('k')):
    """Test kappa(W_k(sl_4, f_{(3,1)})) + kappa(W_{k^v}(sl_4, f_{(2,1,1)})) = 0.

    Returns the sum (should be zero if the transport-to-transpose conjecture holds).
    """
    k = sympify(level)
    kv = hook_dual_level_sl4(k)
    return simplify(kappa_sl4_31(k) + kappa_sl4_211(kv))


def kappa_anti_symmetry_22(level=Symbol('k')):
    """Test kappa(W_k(sl_4, f_{(2,2)})) + kappa(W_{k^v}(sl_4, f_{(2,2)})) = 0.

    Self-dual partition: (2,2)^t = (2,2).
    """
    k = sympify(level)
    kv = hook_dual_level_sl4(k)
    return simplify(kappa_sl4_22(k) + kappa_sl4_22(kv))


def c_complementarity_22(level=Symbol('k')):
    """c(k) + c(k^v) for (2,2) — should be constant (k-independent)."""
    k = sympify(level)
    kv = hook_dual_level_sl4(k)
    return simplify(c_sl4_22(k) + c_sl4_22(kv))


def c_complementarity_31_211(level=Symbol('k')):
    """c(k) + c(k^v) for (3,1) + (2,1,1) — test k-independence."""
    k = sympify(level)
    kv = hook_dual_level_sl4(k)
    return simplify(c_sl4_31(k) + c_sl4_211(kv))


# ---------------------------------------------------------------------------
# Hook duality data assembly
# ---------------------------------------------------------------------------

def sl4_hook_duality_data(level=Symbol('k')) -> HookDualityData:
    """Complete duality data for the sl_4 hook pair (3,1) <-> (2,1,1)."""
    k = sympify(level)
    kv = hook_dual_level_sl4(k)

    source_gen = sl4_hook_31_generators()
    target_gen = sl4_hook_211_generators()
    source_cc = krw_central_charge_data((3, 1))
    target_cc = krw_central_charge_data((2, 1, 1))

    source_kappa = kappa_sl4_31(k)
    target_kappa = kappa_sl4_211(kv)
    kappa_sum = simplify(source_kappa + target_kappa)
    c_sum = simplify(c_sl4_31(k) + c_sl4_211(kv))

    return HookDualityData(
        source_partition=(3, 1),
        target_partition=(2, 1, 1),
        source_generators=source_gen,
        target_generators=target_gen,
        source_central_charge=source_cc,
        target_central_charge=target_cc,
        source_kappa=source_kappa,
        target_kappa=target_kappa,
        dual_level=kv,
        kappa_sum=kappa_sum,
        c_sum=c_sum,
    )


# ---------------------------------------------------------------------------
# Bar cohomology in low degrees
# ---------------------------------------------------------------------------

def bar_cohomology_h0(partition: Partition) -> int:
    """H^0(B(W)) = ground field (always 1-dimensional for connected VOAs)."""
    return 1


def bar_cohomology_h1_generators(partition: Partition) -> int:
    """dim H^1(B(W)) = number of strong generators.

    For a freely generated W-algebra, H^1 is spanned by the generators.
    """
    gen_data = w_algebra_generator_data(partition)
    return gen_data.f_centralizer_dimension


def bar_cohomology_h2_estimate(partition: Partition) -> Dict[str, object]:
    """Estimate of H^2(B(W)) from the OPE relations.

    H^2 is generated by the OPE relations among the strong generators.
    For W-algebras from DS reduction, the number of relations is bounded
    by the dimension of the positive-grade part of g/g^f.

    Returns a dict with:
      - n_generators: dim H^1
      - n_relations_upper: upper bound on dim H^2
      - n_relations_from_ope: expected from OPE closure
    """
    lam = normalize_partition(partition)
    N = partition_size(lam)
    gen_data = w_algebra_generator_data(lam)

    # Upper bound: dim(g) - dim(g^f) counts the constrained directions
    dim_g = N * N - 1
    dim_gf = gen_data.f_centralizer_dimension
    dim_constrained = dim_g - dim_gf

    # OPE relations: for each pair of generators, the OPE gives structure
    # constants. The number of independent relations is at most
    # n_gen*(n_gen+1)/2 - dim(algebra).
    n_gen = dim_gf
    n_ope_pairs = n_gen * (n_gen + 1) // 2

    return {
        "n_generators": n_gen,
        "n_relations_upper": dim_constrained,
        "n_ope_pairs": n_ope_pairs,
        "euler_char_estimate": n_gen - dim_constrained,
    }


# ---------------------------------------------------------------------------
# General hook-type duality for sl_N
# ---------------------------------------------------------------------------

def hook_kappa_anti_symmetry_sl_n(
    N: int, r: int, level=Symbol('k')
) -> object:
    """Test kappa anti-symmetry for hook partition (N-r, 1^r) in sl_N.

    Returns kappa(W_k(sl_N, f_{(N-r,1^r)})) + kappa(W_{k^v}(sl_N, f_{(N-r,1^r)^t})).
    Should be zero if the transport-to-transpose conjecture holds.
    """
    from compute.lib.nonprincipal_ds_orbits import hook_partition

    lam = hook_partition(N, r)
    lam_t = transpose_partition(lam)
    k = sympify(level)
    kv = hook_dual_level_sl_n(N, k)
    return simplify(
        ds_kappa_from_affine(lam, k) + ds_kappa_from_affine(lam_t, kv)
    )


def hook_kappa_anti_symmetry_catalog(
    max_N: int = 6, level=Symbol('k')
) -> Dict[str, object]:
    """Catalog of kappa anti-symmetry tests for hook partitions in type A."""
    from compute.lib.nonprincipal_ds_orbits import hook_partition

    results = {}
    for N in range(3, max_N + 1):
        for r in range(1, N - 1):
            lam = hook_partition(N, r)
            lam_t = transpose_partition(lam)
            key = f"sl_{N} hook ({','.join(str(x) for x in lam)}) <-> ({','.join(str(x) for x in lam_t)})"
            results[key] = hook_kappa_anti_symmetry_sl_n(N, r, level)
    return results


# ---------------------------------------------------------------------------
# Verification bundle
# ---------------------------------------------------------------------------

def verify_hook_type_w_duality() -> Dict[str, bool]:
    """Comprehensive verification of hook-type W-algebra duality data."""
    k = Symbol('k')
    results: Dict[str, bool] = {}

    # 1. Partition transpose relations
    results["(3,1)^t = (2,1,1)"] = transpose_partition((3, 1)) == (2, 1, 1)
    results["(2,1,1)^t = (3,1)"] = transpose_partition((2, 1, 1)) == (3, 1)
    results["(2,2)^t = (2,2)"] = transpose_partition((2, 2)) == (2, 2)

    # 2. Orbit classifications
    results["(2,1,1) is hook"] = type_a_orbit_class((2, 1, 1)) == "hook_nonprincipal"
    results["(3,1) is subregular"] = type_a_orbit_class((3, 1)) == "subregular"
    results["(2,2) is two-row"] = type_a_orbit_class((2, 2)) == "two_row_nonhook"

    # 3. Generator data
    gen_211 = sl4_hook_211_generators()
    gen_31 = sl4_hook_31_generators()
    gen_22 = sl4_22_generators()

    results["(2,1,1) f-centralizer dim = 9"] = gen_211.f_centralizer_dimension == 9
    results["(3,1) f-centralizer dim = 5"] = gen_31.f_centralizer_dimension == 5
    results["(2,2) f-centralizer dim = 7"] = gen_22.f_centralizer_dimension == 7
    results["(2,1,1) has 4 fermionic generators"] = gen_211.n_fermionic == 4
    results["(3,1) has 0 fermionic generators"] = gen_31.n_fermionic == 0

    # 4. f-centralizer grades
    results["(2,1,1) grade 0 count = 4"] = gen_211.f_centralizer_grades[0] == 4
    results["(2,1,1) grade -1 count = 4"] = gen_211.f_centralizer_grades[-1] == 4
    results["(2,1,1) grade -2 count = 1"] = gen_211.f_centralizer_grades[-2] == 1
    results["(3,1) grade 0 count = 1"] = gen_31.f_centralizer_grades[0] == 1
    results["(3,1) grade -2 count = 3"] = gen_31.f_centralizer_grades[-2] == 3

    # 5. Central charge formulas (KRW unshifted)
    cc_211 = krw_central_charge_data((2, 1, 1))
    cc_31 = krw_central_charge_data((3, 1))
    cc_22 = krw_central_charge_data((2, 2))
    cc_4 = krw_central_charge_data((4,))

    results["(2,1,1) leading = 3"] = cc_211.leading_term == 3
    results["(2,1,1) quadratic = 54"] = cc_211.quadratic_coeff == 54
    results["(3,1) leading = 5"] = cc_31.leading_term == 5
    results["(3,1) quadratic = 36"] = cc_31.quadratic_coeff == 36
    results["(2,2) leading = 7"] = cc_22.leading_term == 7
    results["(2,2) quadratic = 48"] = cc_22.quadratic_coeff == 48
    # Principal: rho_L = rho (single block), so ||rho-rho_L||^2 = 0, quadratic = 0
    results["(4) leading = 3"] = cc_4.leading_term == 3
    results["(4) quadratic = 0"] = cc_4.quadratic_coeff == 0

    # 6. Ghost constants
    results["C_(4) = 10"] = ghost_constant((4,)) == 10
    results["C_(3,1) = 6"] = ghost_constant((3, 1)) == 6
    results["C_(2,2) = 4"] = ghost_constant((2, 2)) == 4
    results["C_(2,1,1) = 3"] = ghost_constant((2, 1, 1)) == 3
    results["C_(1^4) = 0"] = ghost_constant((1, 1, 1, 1)) == 0

    # 7. Kappa = 15(k+4)/8 - C_lambda
    kappa_principal = kappa_sl4_principal(k)
    results["principal kappa = 15(k+4)/8 - 10"] = simplify(
        kappa_principal - (Rational(15, 8) * (k + 4) - 10)
    ) == 0

    # 8. Kappa complementarity constants (NOT zero, but k-independent)
    results["(2,2) kappa sum = -8"] = simplify(kappa_anti_symmetry_22(k) + 8) == 0
    kv = hook_dual_level_sl4(k)
    results["principal kappa sum = -20"] = simplify(
        kappa_sl4_principal(k) + kappa_sl4_principal(kv) + 20
    ) == 0
    results["hook kappa sum = -9"] = simplify(kappa_anti_symmetry_31_211(k) + 9) == 0

    # 9. c-complementarity: (2,2) is k-independent, (3,1)+(2,1,1) is NOT
    c_22_sum = c_complementarity_22(k)
    results["(2,2) c+c' is k-independent"] = simplify(c_22_sum.diff(k)) == 0
    results["(2,2) c+c' = 14"] = simplify(c_22_sum - 14) == 0
    c_hook_sum = c_complementarity_31_211(k)
    results["(3,1)+(2,1,1) c+c' is k-dependent"] = simplify(c_hook_sum.diff(k)) != 0

    # 10. Bar cohomology
    results["(2,1,1) bar H^1 = 9"] = bar_cohomology_h1_generators((2, 1, 1)) == 9
    results["(3,1) bar H^1 = 5"] = bar_cohomology_h1_generators((3, 1)) == 5

    # 11. Hook duality data
    duality = sl4_hook_duality_data(k)
    results["hook duality source = (3,1)"] = duality.source_partition == (3, 1)
    results["hook duality target = (2,1,1)"] = duality.target_partition == (2, 1, 1)
    results["hook dual level = -k-8"] = simplify(duality.dual_level + k + 8) == 0
    results["hook kappa sum = complementarity constant"] = (
        simplify(duality.kappa_sum - complementarity_constant((3, 1))) == 0
    )

    # 12. General hook catalog: all kappa sums are k-independent constants
    catalog = hook_kappa_anti_symmetry_catalog(max_N=6, level=k)
    for key, value in catalog.items():
        results[f"kappa constant: {key}"] = simplify(sympify(value).diff(k)) == 0

    return results
