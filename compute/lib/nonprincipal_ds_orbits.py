"""Non-principal DS orbit scaffold for type-A hook/subregular families.

This module is intentionally separated from the principal finite-type PBW
modules. It records only the orbit-combinatorial data needed to launch the
non-principal W frontier:

  - hook and subregular partitions in type A;
  - Barbasch-Vogan duality as partition transpose (type A);
  - orbit/centralizer dimension identities for sl_n nilpotent orbits;
  - a frontier case catalog with explicit status tags.

No OPE or bar differential is implemented here.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, Tuple

from sympy import Matrix, Symbol, sympify, zeros

Partition = Tuple[int, ...]

TRACK_CORE_PRINCIPAL = "core_principal_finite_type_pbw"
TRACK_FRONTIER_NONPRINCIPAL = "frontier_nonprincipal_ds_orbit"

STATUS_PROVED_SUBREGULAR_SL3 = "proved_subregular_sl3"
STATUS_HOOK_EVIDENCE = "hook_spectrum_evidence"
STATUS_PROGRAMME = "programme"


@dataclass(frozen=True)
class OrbitDualityCase:
    """Small record used by non-principal DS orbit frontier checks."""

    lie_type: str
    rank: int
    partition: Partition
    dual_partition: Partition
    family: str
    level_shift: object
    track: str
    status: str


@dataclass(frozen=True)
class MatrixSl2Triple:
    """Concrete sl_2-triple inside sl_n given by matrices."""

    e: Matrix
    h: Matrix
    f: Matrix


def normalize_partition(parts: Iterable[int]) -> Partition:
    """Normalize an integer partition to nonincreasing order."""
    cleaned = []
    for part in parts:
        value = int(part)
        if value <= 0:
            raise ValueError("partition parts must be positive integers")
        cleaned.append(value)
    if not cleaned:
        raise ValueError("partition must be nonempty")
    return tuple(sorted(cleaned, reverse=True))


def partition_size(partition: Iterable[int]) -> int:
    """Total size n of the partition of n."""
    return sum(normalize_partition(partition))


def transpose_partition(partition: Iterable[int]) -> Partition:
    """Ferrers transpose of a partition."""
    lam = normalize_partition(partition)
    height = lam[0]
    return tuple(sum(1 for part in lam if part >= col) for col in range(1, height + 1))


def is_hook_partition(partition: Iterable[int]) -> bool:
    """Return True iff the partition is of hook type (n-r,1^r)."""
    lam = normalize_partition(partition)
    return sum(1 for part in lam if part > 1) <= 1


def hook_partition(n: int, r: int) -> Partition:
    """Hook partition (n-r, 1^r) of n.

    The endpoints are included:
      r = 0   -> principal partition (n)
      r = n-1 -> trivial partition (1^n)
    """
    if n < 1:
        raise ValueError("n must be positive")
    if not (0 <= r <= n - 1):
        raise ValueError("r must satisfy 0 <= r <= n-1")
    return (n - r,) + (1,) * r


def subregular_partition(n: int) -> Partition:
    """Subregular partition in type A_{n-1}: (n-1, 1)."""
    if n < 3:
        raise ValueError("subregular partition requires n >= 3")
    return (n - 1, 1)


def type_a_bv_dual(partition: Iterable[int]) -> Partition:
    """Barbasch-Vogan dual in type A (partition transpose)."""
    return transpose_partition(partition)


def hook_dual_partition(n: int, r: int) -> Partition:
    """Dual of a hook partition in type A."""
    return type_a_bv_dual(hook_partition(n, r))


def type_a_orbit_class(partition: Iterable[int]) -> str:
    """Classify a type-A nilpotent orbit partition."""
    lam = normalize_partition(partition)
    n = sum(lam)
    if lam == (n,):
        return "principal"
    if lam == (1,) * n:
        return "trivial"
    if n >= 3 and lam == (n - 1, 1):
        return "subregular"
    if is_hook_partition(lam):
        return "hook_nonprincipal"
    return "general_nonprincipal"


def centralizer_dimension_sl_n(partition: Iterable[int]) -> int:
    """Dimension of the nilpotent centralizer in sl_n."""
    dual = transpose_partition(partition)
    # gl_n centralizer dimension is sum_i (dual_i)^2; subtract scalar center for sl_n.
    return sum(part * part for part in dual) - 1


def type_a_nilpotent_matrix(partition: Iterable[int]) -> Matrix:
    """Standard Jordan nilpotent representative for a type-A orbit partition."""
    lam = normalize_partition(partition)
    n = sum(lam)
    matrix = zeros(n, n)
    offset = 0
    for block_size in lam:
        for index in range(block_size - 1):
            matrix[offset + index, offset + index + 1] = 1
        offset += block_size
    return matrix


def _matrix_unit(n: int, i: int, j: int) -> Matrix:
    """Elementary matrix E_{ij} in size n."""
    matrix = zeros(n, n)
    matrix[i - 1, j - 1] = 1
    return matrix


def type_a_hook_nilpotent_matrix(n: int, r: int) -> Matrix:
    """Jordan nilpotent representative for the hook partition (n-r,1^r)."""
    return type_a_nilpotent_matrix(hook_partition(n, r))


def nilpotent_partition_from_matrix(matrix: Matrix) -> Partition:
    """Recover the nilpotent Jordan type from kernel dimensions of powers."""
    if matrix.rows != matrix.cols:
        raise ValueError("matrix must be square")
    n = matrix.rows
    kernel_dims = []
    current = matrix
    for power in range(1, n + 1):
        kernel_dims.append(n - int(current.rank()))
        current *= matrix
    if kernel_dims[-1] != n:
        raise ValueError("matrix is not nilpotent")

    dual = []
    previous = 0
    for kernel_dim in kernel_dims:
        dual_entry = kernel_dim - previous
        if dual_entry < 0:
            raise ValueError("kernel dimensions must be nondecreasing for nilpotent matrices")
        if dual_entry > 0:
            dual.append(dual_entry)
        previous = kernel_dim
    return transpose_partition(tuple(dual))


def matrix_centralizer_dimension_sl_n(matrix: Matrix) -> int:
    """Centralizer dimension in sl_n computed directly from a matrix representative."""
    if matrix.rows != matrix.cols:
        raise ValueError("matrix must be square")
    n = matrix.rows
    columns = []
    for i in range(n):
        for j in range(n):
            basis = zeros(n, n)
            basis[i, j] = 1
            columns.append((matrix * basis - basis * matrix).reshape(n * n, 1))
    ad_matrix = Matrix.hstack(*columns)
    gl_centralizer_dim = n * n - int(ad_matrix.rank())
    return gl_centralizer_dim - 1


def matrix_centralizer_basis_sl_n(matrix: Matrix) -> Tuple[Matrix, ...]:
    """A traceless basis for the centralizer of a matrix representative in sl_n."""
    if matrix.rows != matrix.cols:
        raise ValueError("matrix must be square")
    n = matrix.rows
    matrix_units = []
    columns = []
    for i in range(n):
        for j in range(n):
            basis = zeros(n, n)
            basis[i, j] = 1
            matrix_units.append(basis)
            columns.append((matrix * basis - basis * matrix).reshape(n * n, 1))
    ad_matrix = Matrix.hstack(*columns)
    identity = Matrix.eye(n)
    traceless_candidates = []
    for vector in ad_matrix.nullspace():
        candidate = zeros(n, n)
        for coefficient, basis in zip(vector, matrix_units):
            candidate += coefficient * basis
        candidate -= candidate.trace() * identity / n
        if candidate != zeros(n, n):
            traceless_candidates.append(candidate)

    basis = []
    basis_columns = []
    for candidate in traceless_candidates:
        column = candidate.reshape(n * n, 1)
        if not basis_columns:
            basis_columns.append(column)
            basis.append(candidate)
            continue
        span = Matrix.hstack(*basis_columns, column)
        if span.rank() > len(basis_columns):
            basis_columns.append(column)
            basis.append(candidate)
    return tuple(basis)


def orbit_dimension_sl_n(partition: Iterable[int]) -> int:
    """Dimension of the nilpotent orbit in sl_n."""
    n = partition_size(partition)
    dual = transpose_partition(partition)
    # Dimension agrees with gl_n: n^2 - sum_i (dual_i)^2.
    return n * n - sum(part * part for part in dual)


def principal_ff_level_shift_type_a(n: int, level=Symbol("k")):
    """Principal Feigin-Frenkel involution k -> -k - 2n for sl_n."""
    if n < 2:
        raise ValueError("type A rank requires n >= 2")
    k = sympify(level)
    return -k - 2 * n


def nonprincipal_hook_level_shift_ansatz_type_a(n: int, level=Symbol("k")):
    """Current hook/subregular ansatz for the non-principal level shift.

    This intentionally reuses the principal Feigin-Frenkel involution as a
    starting scaffold, while the full non-principal correction remains open.
    """
    return principal_ff_level_shift_type_a(n, level=level)


def nonprincipal_hook_case(n: int, r: int, level=Symbol("k")) -> OrbitDualityCase:
    """Build a single non-principal hook/subregular frontier case."""
    if not (1 <= r <= n - 2):
        raise ValueError("non-principal hook requires 1 <= r <= n-2")

    partition = hook_partition(n, r)
    dual = hook_dual_partition(n, r)
    family = "subregular" if r == 1 else "hook"

    if n == 3 and r == 1:
        status = STATUS_PROVED_SUBREGULAR_SL3
    elif n <= 6:
        status = STATUS_HOOK_EVIDENCE
    else:
        status = STATUS_PROGRAMME

    return OrbitDualityCase(
        lie_type="A",
        rank=n - 1,
        partition=partition,
        dual_partition=dual,
        family=family,
        level_shift=nonprincipal_hook_level_shift_ansatz_type_a(n, level=level),
        track=TRACK_FRONTIER_NONPRINCIPAL,
        status=status,
    )


def nonprincipal_hook_cases(max_n: int = 6, level=Symbol("k")) -> Tuple[OrbitDualityCase, ...]:
    """Enumerate hook/subregular non-principal seed cases in type A."""
    if max_n < 3:
        return ()
    cases = []
    for n in range(3, max_n + 1):
        for r in range(1, n - 1):
            cases.append(nonprincipal_hook_case(n, r, level=level))
    return tuple(cases)


def first_nonselfdual_hook_pair_nilpotent_matrices() -> Tuple[Matrix, Matrix]:
    """Standard nilpotent representatives for the first non-self-dual hook pair."""
    return (
        type_a_hook_nilpotent_matrix(4, 1),
        type_a_nilpotent_matrix((2, 1, 1)),
    )


def first_nonselfdual_hook_pair_centralizer_bases() -> Tuple[Tuple[Matrix, ...], Tuple[Matrix, ...]]:
    """Traceless centralizer bases for the first non-self-dual hook pair."""
    source, target = first_nonselfdual_hook_pair_nilpotent_matrices()
    return (
        matrix_centralizer_basis_sl_n(source),
        matrix_centralizer_basis_sl_n(target),
    )


def first_nonselfdual_hook_pair_sl2_triples() -> Tuple[MatrixSl2Triple, MatrixSl2Triple]:
    """Standard Jacobson-Morozov triples for the first non-self-dual hook pair."""
    source = MatrixSl2Triple(
        e=_matrix_unit(4, 1, 2) + _matrix_unit(4, 2, 3),
        h=Matrix.diag(2, 0, -2, 0),
        f=2 * _matrix_unit(4, 2, 1) + 2 * _matrix_unit(4, 3, 2),
    )
    target = MatrixSl2Triple(
        e=_matrix_unit(4, 1, 2),
        h=Matrix.diag(1, -1, 0, 0),
        f=_matrix_unit(4, 2, 1),
    )
    return source, target


def ad_h_grade_multiplicities_sl_n(h: Matrix) -> Dict[int, int]:
    """ad(h)-grading multiplicities on the standard traceless basis of sl_n."""
    if h.rows != h.cols:
        raise ValueError("h must be square")
    n = h.rows
    basis = [(_matrix_unit(n, i, j), f"E{i}{j}") for i in range(1, n + 1) for j in range(1, n + 1) if i != j]
    basis += [
        (_matrix_unit(n, i, i) - _matrix_unit(n, i + 1, i + 1), f"H{i}")
        for i in range(1, n)
    ]
    multiplicities: Dict[int, int] = {}
    for element, _ in basis:
        commutator = h * element - element * h
        eigenvalue = None
        for candidate in range(-2 * n, 2 * n + 1):
            if commutator == candidate * element:
                eigenvalue = candidate
                break
        if eigenvalue is None:
            raise ValueError("basis element is not an ad(h)-eigenvector")
        multiplicities[eigenvalue] = multiplicities.get(eigenvalue, 0) + 1
    return multiplicities


def ad_h_graded_basis_labels_sl_n(h: Matrix) -> Dict[int, Tuple[str, ...]]:
    """Standard traceless basis labels grouped by ad(h)-eigenvalue."""
    if h.rows != h.cols:
        raise ValueError("h must be square")
    n = h.rows
    basis = [(_matrix_unit(n, i, j), f"E{i}{j}") for i in range(1, n + 1) for j in range(1, n + 1) if i != j]
    basis += [
        (_matrix_unit(n, i, i) - _matrix_unit(n, i + 1, i + 1), f"H{i}")
        for i in range(1, n)
    ]
    graded: Dict[int, list[str]] = {}
    for element, label in basis:
        commutator = h * element - element * h
        eigenvalue = None
        for candidate in range(-2 * n, 2 * n + 1):
            if commutator == candidate * element:
                eigenvalue = candidate
                break
        if eigenvalue is None:
            raise ValueError("basis element is not an ad(h)-eigenvector")
        graded.setdefault(eigenvalue, []).append(label)
    return {grade: tuple(labels) for grade, labels in graded.items()}


def verify_nonprincipal_ds_orbit_scaffold(max_n: int = 8) -> Dict[str, bool]:
    """Sanity checks for the hook/subregular non-principal DS scaffold."""
    results: Dict[str, bool] = {}

    for n in range(3, max_n + 1):
        sub = subregular_partition(n)
        sub_dual = type_a_bv_dual(sub)
        expected_sub_dual = hook_partition(n, n - 2)
        results[f"A{n-1} subregular classification"] = type_a_orbit_class(sub) == "subregular"
        results[f"A{n-1} subregular dual formula"] = sub_dual == expected_sub_dual

        # sl_n identity: orbit + centralizer = dim(sl_n) = n^2 - 1
        orbit_dim = orbit_dimension_sl_n(sub)
        centralizer_dim = centralizer_dimension_sl_n(sub)
        results[f"A{n-1} subregular dimension identity"] = orbit_dim + centralizer_dim == n * n - 1

        for r in range(1, n - 1):
            hook = hook_partition(n, r)
            dual = hook_dual_partition(n, r)
            expected = hook_partition(n, n - r - 1)
            cls = type_a_orbit_class(hook)
            case = nonprincipal_hook_case(n, r)

            results[f"A{n-1} hook r={r} is hook"] = is_hook_partition(hook)
            results[f"A{n-1} hook r={r} dual formula"] = dual == expected
            results[f"A{n-1} hook r={r} non-principal class"] = cls in {
                "subregular",
                "hook_nonprincipal",
            }
            hook_matrix = type_a_hook_nilpotent_matrix(n, r)
            results[f"A{n-1} hook r={r} matrix partition"] = (
                nilpotent_partition_from_matrix(hook_matrix) == hook
            )
            results[f"A{n-1} hook r={r} matrix centralizer dimension"] = (
                matrix_centralizer_dimension_sl_n(hook_matrix) == centralizer_dimension_sl_n(hook)
            )
            results[f"A{n-1} hook r={r} frontier track"] = (
                case.track == TRACK_FRONTIER_NONPRINCIPAL
            )

    cases = nonprincipal_hook_cases(max_n=max_n)
    results["frontier catalog excludes principal"] = all(
        type_a_orbit_class(case.partition) != "principal" for case in cases
    )
    results["frontier catalog excludes trivial"] = all(
        type_a_orbit_class(case.partition) != "trivial" for case in cases
    )
    first_source, first_target = first_nonselfdual_hook_pair_nilpotent_matrices()
    results["first non-self-dual hook matrices recover partitions"] = (
        nilpotent_partition_from_matrix(first_source) == (3, 1)
        and nilpotent_partition_from_matrix(first_target) == (2, 1, 1)
    )
    first_source_centralizer, first_target_centralizer = first_nonselfdual_hook_pair_centralizer_bases()
    results["first non-self-dual hook centralizer basis sizes"] = (
        len(first_source_centralizer) == centralizer_dimension_sl_n((3, 1))
        and len(first_target_centralizer) == centralizer_dimension_sl_n((2, 1, 1))
    )
    first_source_triple, first_target_triple = first_nonselfdual_hook_pair_sl2_triples()
    results["first non-self-dual hook sl2 relations"] = (
        first_source_triple.h * first_source_triple.e
        - first_source_triple.e * first_source_triple.h
        == 2 * first_source_triple.e
        and first_source_triple.h * first_source_triple.f
        - first_source_triple.f * first_source_triple.h
        == -2 * first_source_triple.f
        and first_source_triple.e * first_source_triple.f
        - first_source_triple.f * first_source_triple.e
        == first_source_triple.h
        and first_target_triple.h * first_target_triple.e
        - first_target_triple.e * first_target_triple.h
        == 2 * first_target_triple.e
        and first_target_triple.h * first_target_triple.f
        - first_target_triple.f * first_target_triple.h
        == -2 * first_target_triple.f
        and first_target_triple.e * first_target_triple.f
        - first_target_triple.f * first_target_triple.e
        == first_target_triple.h
    )
    results["first non-self-dual hook grading multiplicities"] = (
        ad_h_grade_multiplicities_sl_n(first_source_triple.h) == {4: 1, 2: 4, 0: 5, -2: 4, -4: 1}
        and ad_h_grade_multiplicities_sl_n(first_target_triple.h) == {2: 1, 1: 4, 0: 5, -1: 4, -2: 1}
    )
    source_graded_basis = ad_h_graded_basis_labels_sl_n(first_source_triple.h)
    target_graded_basis = ad_h_graded_basis_labels_sl_n(first_target_triple.h)
    results["first non-self-dual hook positive graded basis labels"] = (
        source_graded_basis[4] == ("E13",)
        and source_graded_basis[2] == ("E12", "E14", "E23", "E43")
        and target_graded_basis[2] == ("E12",)
        and target_graded_basis[1] == ("E13", "E14", "E32", "E42")
    )

    return results
