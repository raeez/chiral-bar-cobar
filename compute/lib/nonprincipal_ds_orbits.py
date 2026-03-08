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

from sympy import Matrix, Symbol, simplify, sympify, zeros

Partition = Tuple[int, ...]
MatrixBasisExpression = Tuple[Tuple[str, object], ...]

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


@dataclass(frozen=True)
class HookOrbitPairProfile:
    """Concrete orbit-side profile for one hook orbit and its transpose dual."""

    lie_type: str
    rank: int
    n: int
    r: int
    source_partition: Partition
    target_partition: Partition
    source_orbit_dimension: int
    target_orbit_dimension: int
    source_centralizer_dimension: int
    target_centralizer_dimension: int
    source_positive_simple_root_count: int
    target_positive_simple_root_count: int
    source_positive_basis_labels: Tuple[str, ...]
    target_positive_basis_labels: Tuple[str, ...]
    source_level_shift: object
    target_level_shift: object
    track: str
    status: str


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


def standard_traceless_basis_sl_n(n: int) -> Tuple[Tuple[str, Matrix], ...]:
    """Ordered standard traceless basis of sl_n."""
    if n < 2:
        raise ValueError("n must be at least 2")
    basis = [(f"E{i}{j}", _matrix_unit(n, i, j)) for i in range(1, n + 1) for j in range(1, n + 1) if i != j]
    basis += [
        (f"H{i}", _matrix_unit(n, i, i) - _matrix_unit(n, i + 1, i + 1))
        for i in range(1, n)
    ]
    return tuple(basis)


def matrix_to_traceless_basis_expression_sl_n(matrix: Matrix) -> MatrixBasisExpression:
    """Re-expand a traceless n x n matrix in the standard sl_n basis."""
    if matrix.rows != matrix.cols:
        raise ValueError("matrix must be square")
    basis = standard_traceless_basis_sl_n(matrix.rows)
    basis_columns = Matrix.hstack(*[element.reshape(matrix.rows * matrix.rows, 1) for _, element in basis])
    coefficients = basis_columns.gauss_jordan_solve(matrix.reshape(matrix.rows * matrix.rows, 1))[0]
    return tuple(
        (label, coefficients[index, 0])
        for index, (label, _) in enumerate(basis)
        if coefficients[index, 0] != 0
    )


def type_a_hook_nilpotent_matrix(n: int, r: int) -> Matrix:
    """Jordan nilpotent representative for the hook partition (n-r,1^r)."""
    return type_a_nilpotent_matrix(hook_partition(n, r))


def type_a_partition_sl2_triple(partition: Iterable[int]) -> MatrixSl2Triple:
    """Canonical block-diagonal sl_2-triple for a type-A Jordan partition."""
    lam = normalize_partition(partition)
    n = sum(lam)
    e = zeros(n, n)
    h = zeros(n, n)
    f = zeros(n, n)

    offset = 0
    for block_size in lam:
        for index in range(block_size):
            h[offset + index, offset + index] = block_size - 1 - 2 * index
        for index in range(block_size - 1):
            e[offset + index, offset + index + 1] = 1
            # sl_2 weight-lowering coefficient in the highest-weight basis.
            f[offset + index + 1, offset + index] = (index + 1) * (block_size - index - 1)
        offset += block_size

    return MatrixSl2Triple(e=e, h=h, f=f)


def type_a_hook_sl2_triple(n: int, r: int) -> MatrixSl2Triple:
    """Canonical sl_2-triple for the type-A hook orbit (n-r,1^r)."""
    return type_a_partition_sl2_triple(hook_partition(n, r))


def type_a_hook_pair_sl2_triples(n: int, r: int) -> Tuple[MatrixSl2Triple, MatrixSl2Triple]:
    """Canonical sl_2-triples for a hook orbit and its transpose-dual hook."""
    if not (1 <= r <= n - 2):
        raise ValueError("non-principal hook requires 1 <= r <= n-2")
    return (
        type_a_hook_sl2_triple(n, r),
        type_a_hook_sl2_triple(n, n - r - 1),
    )


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


def homogeneous_f_centralizer_basis_sl_n(
    f: Matrix,
    h: Matrix,
) -> Dict[int, Tuple[MatrixBasisExpression, ...]]:
    """Homogeneous basis of g^f grouped by ad(h)-grade."""
    if f.rows != f.cols or h.rows != h.cols or f.rows != h.rows:
        raise ValueError("f and h must be square matrices of the same size")
    n = f.rows
    graded_basis = ad_h_graded_basis_labels_sl_n(h)
    basis_dict = dict(standard_traceless_basis_sl_n(n))
    homogeneous: Dict[int, Tuple[MatrixBasisExpression, ...]] = {}
    for grade in sorted(graded_basis, reverse=True):
        labels = graded_basis[grade]
        columns = [((f * basis_dict[label] - basis_dict[label] * f).reshape(n * n, 1), label) for label in labels]
        if not columns:
            continue
        nullspace = Matrix.hstack(*[column for column, _ in columns]).nullspace()
        if not nullspace:
            continue
        homogeneous[grade] = tuple(
            tuple((label, vector[index, 0]) for index, (_, label) in enumerate(columns) if vector[index, 0] != 0)
            for vector in nullspace
        )
    return homogeneous


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
    return type_a_hook_pair_sl2_triples(4, 1)


def first_nonselfdual_hook_pair_f_centralizer_bases(
) -> Tuple[Dict[int, Tuple[MatrixBasisExpression, ...]], Dict[int, Tuple[MatrixBasisExpression, ...]]]:
    """Homogeneous g^f bases for the first non-self-dual hook pair."""
    source, target = first_nonselfdual_hook_pair_sl2_triples()
    return (
        homogeneous_f_centralizer_basis_sl_n(source.f, source.h),
        homogeneous_f_centralizer_basis_sl_n(target.f, target.h),
    )


def ad_h_grade_multiplicities_sl_n(h: Matrix) -> Dict[int, int]:
    """ad(h)-grading multiplicities on the standard traceless basis of sl_n."""
    if h.rows != h.cols:
        raise ValueError("h must be square")
    n = h.rows
    basis = [(element, label) for label, element in standard_traceless_basis_sl_n(n)]
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
    basis = [(element, label) for label, element in standard_traceless_basis_sl_n(n)]
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


def _positive_simple_root_grade_count(h: Matrix) -> int:
    """Count positive ad(h)-grades on simple roots alpha_i (i=1,...,n-1)."""
    if h.rows != h.cols:
        raise ValueError("h must be square")
    positive = 0
    for index in range(h.rows - 1):
        grade = h[index, index] - h[index + 1, index + 1]
        if grade > 0:
            positive += 1
    return positive


def _positive_basis_labels_from_h(h: Matrix) -> Tuple[str, ...]:
    """Flatten positive-graded standard-basis labels in descending grade order."""
    graded = ad_h_graded_basis_labels_sl_n(h)
    labels = []
    for grade in sorted((entry for entry in graded if entry > 0), reverse=True):
        labels.extend(graded[grade])
    return tuple(labels)


def hook_orbit_pair_profile(n: int, r: int, level=Symbol("k")) -> HookOrbitPairProfile:
    """Orbit-side profile for one hook pair, including dual orbit and grading sizes."""
    case = nonprincipal_hook_case(n, r, level=level)
    source_triple, target_triple = type_a_hook_pair_sl2_triples(n, r)
    source_partition = case.partition
    target_partition = case.dual_partition
    return HookOrbitPairProfile(
        lie_type=case.lie_type,
        rank=case.rank,
        n=n,
        r=r,
        source_partition=source_partition,
        target_partition=target_partition,
        source_orbit_dimension=orbit_dimension_sl_n(source_partition),
        target_orbit_dimension=orbit_dimension_sl_n(target_partition),
        source_centralizer_dimension=centralizer_dimension_sl_n(source_partition),
        target_centralizer_dimension=centralizer_dimension_sl_n(target_partition),
        source_positive_simple_root_count=_positive_simple_root_grade_count(source_triple.h),
        target_positive_simple_root_count=_positive_simple_root_grade_count(target_triple.h),
        source_positive_basis_labels=_positive_basis_labels_from_h(source_triple.h),
        target_positive_basis_labels=_positive_basis_labels_from_h(target_triple.h),
        source_level_shift=sympify(level),
        target_level_shift=case.level_shift,
        track=case.track,
        status=case.status,
    )


def hook_orbit_pair_profile_catalog(
    max_n: int = 6,
    level=Symbol("k"),
) -> Tuple[HookOrbitPairProfile, ...]:
    """Enumerate hook/subregular orbit profiles in type A."""
    if max_n < 3:
        return ()
    return tuple(
        hook_orbit_pair_profile(n, r, level=level)
        for n in range(3, max_n + 1)
        for r in range(1, n - 1)
    )


def verify_hook_orbit_pair_profile_catalog(
    max_n: int = 8,
    level=Symbol("k"),
) -> Dict[str, bool]:
    """Sanity checks for the hook-orbit profile catalog."""
    results: Dict[str, bool] = {}
    profiles = hook_orbit_pair_profile_catalog(max_n=max_n, level=level)

    results["hook orbit pair profile catalog is nonempty"] = bool(profiles)
    for profile in profiles:
        n = profile.n
        r = profile.r
        dual_r = n - r - 1
        key = f"A{n-1} hook r={r}"
        results[f"{key} source partition is hook/subregular"] = (
            type_a_orbit_class(profile.source_partition) in {"subregular", "hook_nonprincipal"}
        )
        results[f"{key} target partition is hook/subregular"] = (
            type_a_orbit_class(profile.target_partition) in {"subregular", "hook_nonprincipal"}
        )
        results[f"{key} source dimension identity"] = (
            profile.source_orbit_dimension + profile.source_centralizer_dimension == n * n - 1
        )
        results[f"{key} target dimension identity"] = (
            profile.target_orbit_dimension + profile.target_centralizer_dimension == n * n - 1
        )
        results[f"{key} source positive simple-root count bounded"] = (
            1 <= profile.source_positive_simple_root_count <= n - 1
        )
        results[f"{key} target positive simple-root count bounded"] = (
            1 <= profile.target_positive_simple_root_count <= n - 1
        )
        results[f"{key} source positive basis labels nonempty"] = bool(
            profile.source_positive_basis_labels
        )
        results[f"{key} target positive basis labels nonempty"] = bool(
            profile.target_positive_basis_labels
        )
        results[f"{key} target level-shift propagation"] = (
            simplify(
                profile.target_level_shift
                - nonprincipal_hook_level_shift_ansatz_type_a(n, profile.source_level_shift)
            )
            == 0
        )
        dual_profile = hook_orbit_pair_profile(n, dual_r, level=profile.source_level_shift)
        results[f"{key} dual swap partition symmetry"] = (
            profile.source_partition == dual_profile.target_partition
            and profile.target_partition == dual_profile.source_partition
        )
        results[f"{key} dual swap simple-root symmetry"] = (
            profile.source_positive_simple_root_count == dual_profile.target_positive_simple_root_count
            and profile.target_positive_simple_root_count == dual_profile.source_positive_simple_root_count
        )
        results[f"{key} dual swap positive-label symmetry"] = (
            profile.source_positive_basis_labels == dual_profile.target_positive_basis_labels
            and profile.target_positive_basis_labels == dual_profile.source_positive_basis_labels
        )

    return results


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
            hook_triple, dual_triple = type_a_hook_pair_sl2_triples(n, r)

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
            results[f"A{n-1} hook r={r} triple e partition"] = (
                nilpotent_partition_from_matrix(hook_triple.e) == hook
            )
            results[f"A{n-1} hook r={r} dual triple e partition"] = (
                nilpotent_partition_from_matrix(dual_triple.e) == dual
            )
            results[f"A{n-1} hook r={r} source triple sl2 relations"] = (
                hook_triple.h * hook_triple.e - hook_triple.e * hook_triple.h == 2 * hook_triple.e
                and hook_triple.h * hook_triple.f - hook_triple.f * hook_triple.h == -2 * hook_triple.f
                and hook_triple.e * hook_triple.f - hook_triple.f * hook_triple.e == hook_triple.h
            )
            results[f"A{n-1} hook r={r} dual triple sl2 relations"] = (
                dual_triple.h * dual_triple.e - dual_triple.e * dual_triple.h == 2 * dual_triple.e
                and dual_triple.h * dual_triple.f - dual_triple.f * dual_triple.h == -2 * dual_triple.f
                and dual_triple.e * dual_triple.f - dual_triple.f * dual_triple.e == dual_triple.h
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
    first_source_f_centralizer, first_target_f_centralizer = first_nonselfdual_hook_pair_f_centralizer_bases()
    results["first non-self-dual hook homogeneous f-centralizer sizes"] = (
        sum(len(items) for items in first_source_f_centralizer.values()) == 5
        and sum(len(items) for items in first_target_f_centralizer.values()) == 9
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
    results["first non-self-dual hook f-centralizer grades"] = (
        tuple(sorted(first_source_f_centralizer, reverse=True)) == (0, -2, -4)
        and tuple(sorted(first_target_f_centralizer, reverse=True)) == (0, -1, -2)
    )
    results["hook orbit pair profile catalog checks"] = all(
        verify_hook_orbit_pair_profile_catalog(max_n=max_n).values()
    )

    return results
