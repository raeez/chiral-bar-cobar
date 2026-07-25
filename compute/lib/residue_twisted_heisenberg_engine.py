"""Exact two-point Heisenberg residue-twisted Arnold check.

This module checks the arity-2 central-current summand inscribed as
``prop:heisenberg-two-point-residue-twisted-acyclicity``.  The complex is

    C^1 = Q * ([alpha|alpha] tensor eta_12) --k--> C^0 = Q * 1.

For k != 0 the positive Arnold fibre line has zero cohomology.  This is
extended by ``prop:heisenberg-two-point-weight-one-polynomial-residue``
to the weight-one polynomial string

    [alpha | alpha_{-1}^q 1] tensor eta_12  --q*k--> alpha_{-1}^{q-1} 1.

It is also extended by
``prop:heisenberg-two-point-single-oscillator-residue`` to the
single-oscillator arbitrary-mode string

    [alpha | alpha_{-n} 1] tensor eta_12  --n*k--> 1.

Finally, ``prop:heisenberg-two-point-single-mode-polynomial-residue``
combines these two directions:

    [alpha | alpha_{-n}^q 1] tensor eta_12  --q*n*k--> alpha_{-n}^{q-1} 1.

For a finite-support mixed-mode monomial
``u_q = prod_n alpha_{-n}^{q_n} 1`` the total two-point residue is

    [alpha | u_q] tensor eta_12  --k * sum_n n*q_n*u_{q-e_n}--> image.

These are still only two-point rank-one Heisenberg summands of the
ordered residue-twisted mechanism; they do not prove mixed-mode Fock
monomials, full Fock-window linear combinations, higher collision
clusters, ordered-to-symmetric descent, curved second-kind convergence,
or Theorem H.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


def _trim_exponents(exponents: tuple[int, ...]) -> tuple[int, ...]:
    """Remove trailing zero exponents while keeping internal mode gaps."""

    end = len(exponents)
    while end > 0 and exponents[end - 1] == 0:
        end -= 1
    return exponents[:end]


def _validate_exponents(exponents: tuple[int, ...]) -> tuple[int, ...]:
    if any(exponent < 0 for exponent in exponents):
        raise ValueError("exponents must be nonnegative")
    return _trim_exponents(exponents)


@dataclass(frozen=True)
class HeisenbergTwoPointResidueReport:
    """Result of the exact two-point residue-twisted Arnold check."""

    level: Fraction
    differential_entry: Fraction
    rank: int
    kernel_dim_positive_fibre: int
    cokernel_dim_degree_zero: int
    positive_fibre_acyclic: bool
    logical_scope: str = (
        "arity-2 rank-one Heisenberg central-current summand only; "
        "not arbitrary Fock monomials, not higher collision clusters, "
        "not ordered-to-symmetric descent, not curved second-kind "
        "convergence, and not a proof of Theorem H"
    )
    proves_full_ordered_twisted_tensor_acyclicity: bool = False
    proves_theorem_h: bool = False


def heisenberg_two_point_residue_report(
    level: int | Fraction,
) -> HeisenbergTwoPointResidueReport:
    """Return the exact report for d([alpha|alpha] eta_12) = k * 1."""

    k = level if isinstance(level, Fraction) else Fraction(level)
    rank = 0 if k == 0 else 1
    kernel_dim = 1 - rank
    cokernel_dim = 1 - rank
    return HeisenbergTwoPointResidueReport(
        level=k,
        differential_entry=k,
        rank=rank,
        kernel_dim_positive_fibre=kernel_dim,
        cokernel_dim_degree_zero=cokernel_dim,
        positive_fibre_acyclic=(kernel_dim == 0),
    )


@dataclass(frozen=True)
class HeisenbergWeightOnePolynomialResidueReport:
    """Exact report for d([alpha|alpha_{-1}^q] eta_12) = q*k alpha_{-1}^{q-1}."""

    level: Fraction
    power: int
    differential_entry: Fraction
    rank: int
    kernel_dim_positive_fibre: int
    cokernel_dim_degree_zero: int
    positive_fibre_acyclic: bool
    logical_scope: str = (
        "arity-2 rank-one Heisenberg weight-one polynomial summand only; "
        "not higher oscillator Fock monomials, not higher collision "
        "clusters, not ordered-to-symmetric descent, and not a proof of "
        "Theorem H"
    )
    proves_full_ordered_twisted_tensor_acyclicity: bool = False
    proves_theorem_h: bool = False


def heisenberg_weight_one_polynomial_residue_report(
    level: int | Fraction,
    power: int,
) -> HeisenbergWeightOnePolynomialResidueReport:
    """Return the exact report for the q-th weight-one polynomial summand."""

    if power < 1:
        raise ValueError("power must be at least 1")
    k = level if isinstance(level, Fraction) else Fraction(level)
    entry = k * power
    rank = 0 if entry == 0 else 1
    kernel_dim = 1 - rank
    cokernel_dim = 1 - rank
    return HeisenbergWeightOnePolynomialResidueReport(
        level=k,
        power=power,
        differential_entry=entry,
        rank=rank,
        kernel_dim_positive_fibre=kernel_dim,
        cokernel_dim_degree_zero=cokernel_dim,
        positive_fibre_acyclic=(kernel_dim == 0),
    )


def heisenberg_weight_one_polynomial_window(
    level: int | Fraction,
    max_power: int,
) -> tuple[HeisenbergWeightOnePolynomialResidueReport, ...]:
    """Return reports for powers 1 through ``max_power``."""

    if max_power < 1:
        raise ValueError("max_power must be at least 1")
    return tuple(
        heisenberg_weight_one_polynomial_residue_report(level, power)
        for power in range(1, max_power + 1)
    )


@dataclass(frozen=True)
class HeisenbergSingleOscillatorResidueReport:
    """Exact report for d([alpha|alpha_{-n}] eta_12) = n*k * 1."""

    level: Fraction
    mode: int
    differential_entry: Fraction
    rank: int
    kernel_dim_positive_fibre: int
    cokernel_dim_degree_zero: int
    positive_fibre_acyclic: bool
    logical_scope: str = (
        "arity-2 rank-one Heisenberg single-oscillator arbitrary-mode "
        "summand only; not products of higher oscillators, not mixed Fock "
        "monomials, not higher collision clusters, not ordered-to-symmetric "
        "descent, and not a proof of Theorem H"
    )
    proves_full_ordered_twisted_tensor_acyclicity: bool = False
    proves_theorem_h: bool = False


def heisenberg_single_oscillator_residue_report(
    level: int | Fraction,
    mode: int,
) -> HeisenbergSingleOscillatorResidueReport:
    """Return the exact report for the n-th single-oscillator summand."""

    if mode < 1:
        raise ValueError("mode must be at least 1")
    k = level if isinstance(level, Fraction) else Fraction(level)
    entry = k * mode
    rank = 0 if entry == 0 else 1
    kernel_dim = 1 - rank
    cokernel_dim = 1 - rank
    return HeisenbergSingleOscillatorResidueReport(
        level=k,
        mode=mode,
        differential_entry=entry,
        rank=rank,
        kernel_dim_positive_fibre=kernel_dim,
        cokernel_dim_degree_zero=cokernel_dim,
        positive_fibre_acyclic=(kernel_dim == 0),
    )


def heisenberg_single_oscillator_window(
    level: int | Fraction,
    max_mode: int,
) -> tuple[HeisenbergSingleOscillatorResidueReport, ...]:
    """Return reports for single oscillator modes 1 through ``max_mode``."""

    if max_mode < 1:
        raise ValueError("max_mode must be at least 1")
    return tuple(
        heisenberg_single_oscillator_residue_report(level, mode)
        for mode in range(1, max_mode + 1)
    )


@dataclass(frozen=True)
class HeisenbergSingleModePolynomialResidueReport:
    """Exact report for d([alpha|alpha_{-n}^q] eta_12) = q*n*k alpha_{-n}^{q-1}."""

    level: Fraction
    mode: int
    power: int
    differential_entry: Fraction
    rank: int
    kernel_dim_positive_fibre: int
    cokernel_dim_degree_zero: int
    positive_fibre_acyclic: bool
    logical_scope: str = (
        "arity-2 rank-one Heisenberg single-mode polynomial "
        "arbitrary-mode summand only; not mixed-mode Fock monomials, "
        "not full Fock-window linear combinations, not higher collision "
        "clusters, not ordered-to-symmetric descent, and not a proof of "
        "Theorem H"
    )
    proves_full_ordered_twisted_tensor_acyclicity: bool = False
    proves_theorem_h: bool = False


def heisenberg_single_mode_polynomial_residue_report(
    level: int | Fraction,
    mode: int,
    power: int,
) -> HeisenbergSingleModePolynomialResidueReport:
    """Return the exact report for the (n, q) single-mode polynomial summand."""

    if mode < 1:
        raise ValueError("mode must be at least 1")
    if power < 1:
        raise ValueError("power must be at least 1")
    k = level if isinstance(level, Fraction) else Fraction(level)
    entry = k * mode * power
    rank = 0 if entry == 0 else 1
    kernel_dim = 1 - rank
    cokernel_dim = 1 - rank
    return HeisenbergSingleModePolynomialResidueReport(
        level=k,
        mode=mode,
        power=power,
        differential_entry=entry,
        rank=rank,
        kernel_dim_positive_fibre=kernel_dim,
        cokernel_dim_degree_zero=cokernel_dim,
        positive_fibre_acyclic=(kernel_dim == 0),
    )


def heisenberg_single_mode_polynomial_grid(
    level: int | Fraction,
    max_mode: int,
    max_power: int,
) -> tuple[HeisenbergSingleModePolynomialResidueReport, ...]:
    """Return reports for all 1 <= mode <= max_mode and 1 <= power <= max_power."""

    if max_mode < 1:
        raise ValueError("max_mode must be at least 1")
    if max_power < 1:
        raise ValueError("max_power must be at least 1")
    return tuple(
        heisenberg_single_mode_polynomial_residue_report(level, mode, power)
        for mode in range(1, max_mode + 1)
        for power in range(1, max_power + 1)
    )


@dataclass(frozen=True)
class HeisenbergMixedModeResidueTerm:
    """One term c * u_exponents in the mixed-mode two-point residue."""

    exponents: tuple[int, ...]
    coefficient: Fraction


@dataclass(frozen=True)
class HeisenbergMixedModeResidueReport:
    """Exact report for d([alpha|prod alpha_-n^q_n] eta_12)."""

    level: Fraction
    exponents: tuple[int, ...]
    image_terms: tuple[HeisenbergMixedModeResidueTerm, ...]
    line_source_dim: int
    image_dim_upper_bound: int
    kernel_dim_positive_line: int
    positive_line_acyclic: bool
    raw_ungraded_operator: str = "L_k = k * sum_{n>=1} n * d/dx_n"
    logical_scope: str = (
        "arity-2 rank-one Heisenberg mixed-mode formula only; the "
        "one-dimensional monomial line contracts onto its image when the "
        "image is nonzero, but this is not full mixed-mode Fock-window "
        "acyclicity and not a proof of Theorem H"
    )
    proves_full_mixed_mode_fock_acyclicity: bool = False
    proves_theorem_h: bool = False


def heisenberg_mixed_mode_residue_report(
    level: int | Fraction,
    exponents: tuple[int, ...],
) -> HeisenbergMixedModeResidueReport:
    """Return the exact mixed-mode image of a finite-support Fock monomial."""

    q = _validate_exponents(tuple(exponents))
    k = level if isinstance(level, Fraction) else Fraction(level)
    terms: list[HeisenbergMixedModeResidueTerm] = []
    for index, exponent in enumerate(q):
        if exponent == 0:
            continue
        mode = index + 1
        image = list(q)
        image[index] -= 1
        terms.append(
            HeisenbergMixedModeResidueTerm(
                exponents=_trim_exponents(tuple(image)),
                coefficient=k * mode * exponent,
            )
        )

    nonzero_image = k != 0 and bool(terms)
    return HeisenbergMixedModeResidueReport(
        level=k,
        exponents=q,
        image_terms=tuple(terms),
        line_source_dim=1,
        image_dim_upper_bound=len(terms),
        kernel_dim_positive_line=0 if nonzero_image else 1,
        positive_line_acyclic=nonzero_image,
    )


def heisenberg_raw_ungraded_kernel_witness(
    level: int | Fraction,
) -> tuple[tuple[tuple[int, ...], Fraction], ...]:
    """Return the raw ungraded witness x_2 - 2*x_1 killed by L_k."""

    k = level if isinstance(level, Fraction) else Fraction(level)
    if k == 0:
        raise ValueError("level must be nonzero for the kernel witness")
    return (((0, 1), Fraction(1)), ((1,), Fraction(-2)))


def heisenberg_evaluate_raw_ungraded_residue_combination(
    level: int | Fraction,
    combination: tuple[tuple[tuple[int, ...], int | Fraction], ...],
) -> dict[tuple[int, ...], Fraction]:
    """Evaluate the mixed-mode residue on a finite raw polynomial combination."""

    totals: dict[tuple[int, ...], Fraction] = {}
    for exponents, scalar in combination:
        scale = scalar if isinstance(scalar, Fraction) else Fraction(scalar)
        report = heisenberg_mixed_mode_residue_report(level, exponents)
        for term in report.image_terms:
            totals[term.exponents] = totals.get(term.exponents, Fraction(0)) + (
                scale * term.coefficient
            )
    return {
        exponents: coefficient
        for exponents, coefficient in sorted(totals.items())
        if coefficient != 0
    }
