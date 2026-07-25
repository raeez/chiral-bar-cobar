r"""Exact finite-window comparison engine for Theorem-H KDH retracts.

This module verifies the finite-dimensional algebra in
``prop:theorem-h-finite-window-kdh-retracts``.  Over ``Fraction``
arithmetic, a finite KDH window carries:

* a cochain differential ``d`` with ``d^2 = 0``;
* the composite projector ``P = i p`` with ``P^2 = P`` and ``dP = Pd``;
* a degree ``-1`` homotopy ``h`` satisfying ``dh + hd = id - P``;
* ``P`` vanishing in degrees >= 3;
* rank-nullity cohomology dimensions in the high tail;
* optional tower transition maps that are cochain maps, surjective, and
  projector- and homotopy-compatible.

It also gives an exact combinatorial realization of the rank-one
Heisenberg finite-window Fock spaces: partition counts, cumulative
window dimensions, and the normalized bar-length bound.

Scope:
    The engine checks supplied finite windows and supplied transition
    maps.  A family realization additionally supplies
    ``KD_H(A) ~= lim_N K_N``, compatible retract data throughout the
    strict Mittag--Leffler tower, the ordered residue contraction, and
    curved second-kind convergence.  The Heisenberg helper establishes
    finite-window combinatorics and degreewise Mittag--Leffler finiteness.

The stored projector is the endomorphism ``P_N=i_N p_N``.  Over the
finite-dimensional rational windows, ``L_N=im(P_N)``, inclusion, and
corestriction recover the explicit retract maps used in the manuscript.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Mapping, Sequence


def _f(value: object) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)  # type: ignore[arg-type]


@dataclass(frozen=True)
class RationalMatrix:
    """Small exact rational matrix with rows acting on column vectors."""

    nrows: int
    ncols: int
    entries: tuple[tuple[Fraction, ...], ...]

    @classmethod
    def from_rows(
        cls, rows: Sequence[Sequence[object]], ncols: int | None = None
    ) -> "RationalMatrix":
        converted = tuple(tuple(_f(x) for x in row) for row in rows)
        if converted:
            width = len(converted[0])
            if any(len(row) != width for row in converted):
                raise ValueError("matrix rows must have constant length")
            if ncols is not None and ncols != width:
                raise ValueError("declared ncols does not match row width")
            return cls(len(converted), width, converted)
        if ncols is None:
            ncols = 0
        return cls(0, ncols, tuple())

    @classmethod
    def zero(cls, nrows: int, ncols: int) -> "RationalMatrix":
        return cls(nrows, ncols, tuple(tuple(Fraction(0) for _ in range(ncols)) for _ in range(nrows)))

    @classmethod
    def identity(cls, n: int) -> "RationalMatrix":
        return cls(
            n,
            n,
            tuple(
                tuple(Fraction(1 if i == j else 0) for j in range(n))
                for i in range(n)
            ),
        )

    def __matmul__(self, other: "RationalMatrix") -> "RationalMatrix":
        if self.ncols != other.nrows:
            raise ValueError(
                f"matrix shape mismatch: {self.shape} cannot multiply {other.shape}"
            )
        rows: list[list[Fraction]] = []
        for i in range(self.nrows):
            row: list[Fraction] = []
            for j in range(other.ncols):
                row.append(
                    sum(
                        self.entries[i][k] * other.entries[k][j]
                        for k in range(self.ncols)
                    )
                )
            rows.append(row)
        return RationalMatrix.from_rows(rows, ncols=other.ncols)

    def __add__(self, other: "RationalMatrix") -> "RationalMatrix":
        self._same_shape(other)
        return RationalMatrix.from_rows(
            [
                [self.entries[i][j] + other.entries[i][j] for j in range(self.ncols)]
                for i in range(self.nrows)
            ],
            ncols=self.ncols,
        )

    def __sub__(self, other: "RationalMatrix") -> "RationalMatrix":
        self._same_shape(other)
        return RationalMatrix.from_rows(
            [
                [self.entries[i][j] - other.entries[i][j] for j in range(self.ncols)]
                for i in range(self.nrows)
            ],
            ncols=self.ncols,
        )

    @property
    def shape(self) -> tuple[int, int]:
        return (self.nrows, self.ncols)

    def is_zero(self) -> bool:
        return all(x == 0 for row in self.entries for x in row)

    def rank(self) -> int:
        """Exact row-reduction rank over Q."""
        rows = [list(row) for row in self.entries]
        rank = 0
        pivot_col = 0
        while rank < self.nrows and pivot_col < self.ncols:
            pivot = None
            for i in range(rank, self.nrows):
                if rows[i][pivot_col] != 0:
                    pivot = i
                    break
            if pivot is None:
                pivot_col += 1
                continue
            rows[rank], rows[pivot] = rows[pivot], rows[rank]
            pivot_value = rows[rank][pivot_col]
            rows[rank] = [x / pivot_value for x in rows[rank]]
            for i in range(self.nrows):
                if i == rank:
                    continue
                factor = rows[i][pivot_col]
                if factor != 0:
                    rows[i] = [
                        rows[i][j] - factor * rows[rank][j]
                        for j in range(self.ncols)
                    ]
            rank += 1
            pivot_col += 1
        return rank

    def _same_shape(self, other: "RationalMatrix") -> None:
        if self.shape != other.shape:
            raise ValueError(f"matrix shape mismatch: {self.shape} != {other.shape}")


@dataclass(frozen=True)
class FiniteKDHWindow:
    """One finite KDH window with composite projector P=i p."""

    dimensions: Mapping[int, int]
    differentials: Mapping[int, RationalMatrix]
    projectors: Mapping[int, RationalMatrix]
    homotopies: Mapping[int, RationalMatrix]
    name: str = "K"

    def dim(self, degree: int) -> int:
        return int(self.dimensions.get(degree, 0))

    def degrees(self) -> tuple[int, ...]:
        keys = set(self.dimensions)
        keys.update(self.differentials)
        keys.update(n + 1 for n in self.differentials)
        keys.update(self.projectors)
        keys.update(self.homotopies)
        keys.update(n - 1 for n in self.homotopies)
        return tuple(sorted(keys))

    def d(self, degree: int) -> RationalMatrix:
        return self.differentials.get(
            degree, RationalMatrix.zero(self.dim(degree + 1), self.dim(degree))
        )

    def P(self, degree: int) -> RationalMatrix:
        return self.projectors.get(
            degree, RationalMatrix.zero(self.dim(degree), self.dim(degree))
        )

    def h(self, degree: int) -> RationalMatrix:
        return self.homotopies.get(
            degree, RationalMatrix.zero(self.dim(degree - 1), self.dim(degree))
        )


@dataclass(frozen=True)
class TransitionMap:
    """A finite-window transition pi: source -> target."""

    source: FiniteKDHWindow
    target: FiniteKDHWindow
    maps: Mapping[int, RationalMatrix]
    name: str = "pi"

    def at(self, degree: int) -> RationalMatrix:
        return self.maps.get(
            degree,
            RationalMatrix.zero(self.target.dim(degree), self.source.dim(degree)),
        )


@dataclass(frozen=True)
class KDHComparisonReport:
    """Result of checking a supplied system of finite-window KDH retracts."""

    valid: bool
    errors: tuple[str, ...]
    windows_checked: int
    transitions_checked: int = 0
    high_tail_starts_at: int = 3
    high_tail_cohomology: tuple[tuple[str, int, int], ...] = ()
    rank_nullity_checked: bool = False
    logical_scope: str = (
        "finite-window exact algebra for supplied KDH windows and transitions"
    )
    theorem_h_status: str = (
        "requires a family KDH realization, low-column comparison, and "
        "completed collision hypotheses"
    )
    inverse_limit_status: str = (
        "requires the supplied comparison KD_H(A) ~= lim_N K_N"
    )


@dataclass(frozen=True)
class HeisenbergWindowReport:
    """Exact rank-one Heisenberg Fock-window count."""

    max_weight: int
    partition_numbers: tuple[int, ...]
    cumulative_dimension: int
    max_normalized_bar_length: int
    finite_dimensional: bool = True
    mittag_leffler_reason: str = (
        "degreewise finite-dimensional inverse systems have stabilized "
        "image chains"
    )
    logical_scope: str = (
        "rank-one Heisenberg finite-window Fock combinatorics and "
        "degreewise Mittag--Leffler finiteness"
    )
    theorem_h_status: str = (
        "requires the KDH realization and low-column comparison"
    )
    ordered_residue_status: str = (
        "requires the ordered collision contraction"
    )
    curved_completion_status: str = (
        "requires curved second-kind convergence"
    )


def cohomology_dimension(window: FiniteKDHWindow, degree: int) -> int:
    """Return dim H^degree(window) by exact rank-nullity over Q."""

    for n in (degree - 1, degree, degree + 1):
        if window.dim(n) < 0:
            raise ValueError(f"negative dimension in degree {n}")

    d_prev = window.d(degree - 1)
    d_now = window.d(degree)
    if d_prev.shape != (window.dim(degree), window.dim(degree - 1)):
        raise ValueError(f"d^{degree - 1} has shape {d_prev.shape}")
    if d_now.shape != (window.dim(degree + 1), window.dim(degree)):
        raise ValueError(f"d^{degree} has shape {d_now.shape}")
    if not (d_now @ d_prev).is_zero():
        raise ValueError(f"d^{degree} d^{degree - 1} != 0")

    kernel_dim = window.dim(degree) - d_now.rank()
    image_dim = d_prev.rank()
    cohomology_dim = kernel_dim - image_dim
    if cohomology_dim < 0:
        raise ValueError(
            f"rank-nullity produced negative H^{degree} dimension "
            f"{cohomology_dim}"
        )
    return cohomology_dim


def high_tail_cohomology_dimensions(
    window: FiniteKDHWindow, high_tail_starts_at: int = 3
) -> dict[int, int]:
    """Return exact cohomology dimensions in degrees >= high_tail_starts_at."""

    return {
        degree: cohomology_dimension(window, degree)
        for degree in window.degrees()
        if degree >= high_tail_starts_at
    }


def verify_window_retract(
    window: FiniteKDHWindow, high_tail_starts_at: int = 3
) -> tuple[str, ...]:
    """Return the equation defects of one finite-window deformation retract."""

    errors: list[str] = []
    degrees = window.degrees()
    for degree, dim in window.dimensions.items():
        if dim < 0:
            errors.append(f"{window.name}: negative dimension in degree {degree}")

    for n in degrees:
        d_n = window.d(n)
        if d_n.shape != (window.dim(n + 1), window.dim(n)):
            errors.append(f"{window.name}: d^{n} has shape {d_n.shape}")
        P_n = window.P(n)
        if P_n.shape != (window.dim(n), window.dim(n)):
            errors.append(f"{window.name}: P^{n} has shape {P_n.shape}")
        h_n = window.h(n)
        if h_n.shape != (window.dim(n - 1), window.dim(n)):
            errors.append(f"{window.name}: h^{n} has shape {h_n.shape}")

    if errors:
        return tuple(errors)

    for n in degrees:
        if not (window.d(n + 1) @ window.d(n)).is_zero():
            errors.append(f"{window.name}: d^{n+1} d^{n} != 0")

        P_n = window.P(n)
        if P_n @ P_n != P_n:
            errors.append(f"{window.name}: P^{n}P^{n}-P^{n} is nonzero")
        if n >= high_tail_starts_at and not P_n.is_zero():
            errors.append(f"{window.name}: P^{n} is nonzero in the high tail")

        if window.dim(n) or window.dim(n + 1):
            if window.d(n) @ P_n != window.P(n + 1) @ window.d(n):
                errors.append(f"{window.name}: [d,P] is nonzero at degree {n}")

        lhs = (window.d(n - 1) @ window.h(n)) + (window.h(n + 1) @ window.d(n))
        rhs = RationalMatrix.identity(window.dim(n)) - P_n
        if lhs != rhs:
            errors.append(
                f"{window.name}: dh+hd-id+P is nonzero at degree {n}"
            )

    return tuple(errors)


def verify_transition_compatibility(transition: TransitionMap) -> tuple[str, ...]:
    """Return the cochain, projector, and homotopy defects of a transition."""

    errors: list[str] = []
    degrees = sorted(set(transition.source.degrees()) | set(transition.target.degrees()))
    for n in degrees:
        pi_n = transition.at(n)
        expected_shape = (transition.target.dim(n), transition.source.dim(n))
        if pi_n.shape != expected_shape:
            errors.append(f"{transition.name}: pi^{n} has shape {pi_n.shape}")
            continue
        if pi_n.rank() != transition.target.dim(n):
            errors.append(
                f"{transition.name}: rank(pi^{n})={pi_n.rank()} "
                f"is below target dimension {transition.target.dim(n)}"
            )

    if errors:
        return tuple(errors)

    for n in degrees:
        pi_n = transition.at(n)
        pi_next = transition.at(n + 1)
        if transition.target.d(n) @ pi_n != pi_next @ transition.source.d(n):
            errors.append(
                f"{transition.name}: d pi-pi d is nonzero at degree {n}"
            )
        if pi_n @ transition.source.P(n) != transition.target.P(n) @ pi_n:
            errors.append(
                f"{transition.name}: pi P-P pi is nonzero at degree {n}"
            )
        if (
            transition.target.h(n) @ pi_n
            != transition.at(n - 1) @ transition.source.h(n)
        ):
            errors.append(
                f"{transition.name}: h pi-pi h is nonzero at degree {n}"
            )

    return tuple(errors)


def verify_kdh_retract_system(
    windows: Sequence[FiniteKDHWindow],
    transitions: Sequence[TransitionMap] = (),
    high_tail_starts_at: int = 3,
) -> KDHComparisonReport:
    """Check a supplied inverse system of finite-window KDH retract data."""

    errors: list[str] = []
    high_tail_cohomology: list[tuple[str, int, int]] = []
    if not windows:
        errors.append("the supplied KDH window sequence is empty")
    for window in windows:
        errors.extend(
            verify_window_retract(
                window, high_tail_starts_at=high_tail_starts_at
            )
        )
        try:
            cohomology = high_tail_cohomology_dimensions(
                window, high_tail_starts_at=high_tail_starts_at
            )
        except ValueError as exc:
            errors.append(f"{window.name}: rank-nullity cross-check failed: {exc}")
            continue
        for degree, dimension in sorted(cohomology.items()):
            high_tail_cohomology.append((window.name, degree, dimension))
            if dimension != 0:
                errors.append(
                    f"{window.name}: rank-nullity high-tail H^{degree} "
                    f"has dimension {dimension}"
                )
    for transition in transitions:
        errors.extend(verify_transition_compatibility(transition))
    return KDHComparisonReport(
        valid=not errors,
        errors=tuple(errors),
        windows_checked=len(windows),
        transitions_checked=len(transitions),
        high_tail_starts_at=high_tail_starts_at,
        high_tail_cohomology=tuple(high_tail_cohomology),
        rank_nullity_checked=True,
    )


def partition_numbers_up_to(max_weight: int) -> tuple[int, ...]:
    """Return p(0), ..., p(max_weight) by the exact Euler product DP."""

    if max_weight < 0:
        raise ValueError("max_weight must be nonnegative")
    counts = [0] * (max_weight + 1)
    counts[0] = 1
    for part in range(1, max_weight + 1):
        for total in range(part, max_weight + 1):
            counts[total] += counts[total - part]
    return tuple(counts)


def heisenberg_fock_window_dimension(max_weight: int) -> int:
    """Return dim F_{<= max_weight} H_k for rank-one Heisenberg."""

    return sum(partition_numbers_up_to(max_weight))


def heisenberg_finite_window_report(max_weight: int) -> HeisenbergWindowReport:
    """Construct the exact finite-window combinatorial realization.

    The normalized augmentation ideal has no conformal-weight-zero
    vector, so a normalized bar word with p inputs has weight at least p.
    Hence no bar word of length p > max_weight contributes to the
    window.  This gives the finite-window counting and
    Mittag--Leffler finiteness part of the Heisenberg Theorem-H package.
    """

    partitions = partition_numbers_up_to(max_weight)
    return HeisenbergWindowReport(
        max_weight=max_weight,
        partition_numbers=partitions,
        cumulative_dimension=sum(partitions),
        max_normalized_bar_length=max_weight,
    )


def model_contractible_tail_window(name: str = "model") -> FiniteKDHWindow:
    """A minimal exact model: one harmonic degree-2 line and a 3--4 pair."""

    one = RationalMatrix.identity(1)
    zero11 = RationalMatrix.zero(1, 1)
    return FiniteKDHWindow(
        dimensions={2: 1, 3: 1, 4: 1},
        differentials={2: zero11, 3: one, 4: RationalMatrix.zero(0, 1)},
        projectors={2: one, 3: zero11, 4: zero11},
        homotopies={2: RationalMatrix.zero(0, 1), 3: zero11, 4: one},
        name=name,
    )


def identity_transition(
    source: FiniteKDHWindow, target: FiniteKDHWindow, name: str = "id"
) -> TransitionMap:
    """Identity transition between windows with matching dimensions."""

    degrees = sorted(set(source.degrees()) | set(target.degrees()))
    maps = {}
    for degree in degrees:
        if source.dim(degree) != target.dim(degree):
            raise ValueError("identity_transition requires matching dimensions")
        maps[degree] = RationalMatrix.identity(source.dim(degree))
    return TransitionMap(source=source, target=target, maps=maps, name=name)
