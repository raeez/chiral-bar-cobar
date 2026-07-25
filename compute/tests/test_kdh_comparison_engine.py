"""Exact tests for finite-window KDH retract comparisons."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from compute.lib.kdh_comparison_engine import (
    FiniteKDHWindow,
    RationalMatrix,
    TransitionMap,
    cohomology_dimension,
    heisenberg_finite_window_report,
    heisenberg_fock_window_dimension,
    high_tail_cohomology_dimensions,
    identity_transition,
    model_contractible_tail_window,
    partition_numbers_up_to,
    verify_kdh_retract_system,
)


ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "compute/lib/kdh_comparison_engine.py"


def test_model_contractible_tail_window_realizes_finite_retract():
    window = model_contractible_tail_window("K_0")
    report = verify_kdh_retract_system([window])

    assert report.valid
    assert report.errors == ()
    assert report.windows_checked == 1
    assert report.high_tail_starts_at == 3
    assert report.rank_nullity_checked
    assert ("K_0", 3, 0) in report.high_tail_cohomology
    assert ("K_0", 4, 0) in report.high_tail_cohomology
    assert "finite-window exact algebra" in report.logical_scope
    assert "requires a family KDH realization" in report.theorem_h_status
    assert "KD_H(A) ~= lim_N K_N" in report.inverse_limit_status


def test_exact_rank_nullity_agrees_with_explicit_contractible_pair():
    window = model_contractible_tail_window("K_0")

    assert cohomology_dimension(window, 2) == 1
    assert cohomology_dimension(window, 3) == 0
    assert cohomology_dimension(window, 4) == 0

    high_tail = high_tail_cohomology_dimensions(window)
    assert high_tail == {3: 0, 4: 0, 5: 0}


def test_two_window_identity_tower_preserves_retract_data():
    target = model_contractible_tail_window("K_N")
    source = model_contractible_tail_window("K_Nplus1")
    transition = identity_transition(source, target, name="pi_Nplus1_N")
    report = verify_kdh_retract_system([target, source], [transition])

    assert report.valid
    assert report.transitions_checked == 1


def test_homotopy_equation_defect_is_detected():
    one = RationalMatrix.identity(1)
    zero11 = RationalMatrix.zero(1, 1)
    broken = FiniteKDHWindow(
        dimensions={2: 1, 3: 1, 4: 1},
        differentials={2: zero11, 3: one, 4: RationalMatrix.zero(0, 1)},
        projectors={2: one, 3: zero11, 4: zero11},
        homotopies={
            2: RationalMatrix.zero(0, 1),
            3: zero11,
            4: zero11,
        },
        name="broken_h",
    )
    report = verify_kdh_retract_system([broken])

    assert report.valid is False
    assert any("dh+hd-id+P is nonzero" in error for error in report.errors)


def test_high_tail_projector_support_is_detected():
    one = RationalMatrix.identity(1)
    zero11 = RationalMatrix.zero(1, 1)
    tail_projector = FiniteKDHWindow(
        dimensions={2: 1, 3: 1, 4: 1},
        differentials={2: zero11, 3: one, 4: RationalMatrix.zero(0, 1)},
        projectors={2: one, 3: one, 4: zero11},
        homotopies={2: RationalMatrix.zero(0, 1), 3: zero11, 4: one},
        name="tail_projector",
    )
    report = verify_kdh_retract_system([tail_projector])

    assert report.valid is False
    assert any("P^3 is nonzero in the high tail" in error for error in report.errors)


def test_rank_nullity_records_high_tail_cohomology():
    high_tail_line = FiniteKDHWindow(
        dimensions={3: 1},
        differentials={3: RationalMatrix.zero(0, 1)},
        projectors={3: RationalMatrix.zero(1, 1)},
        homotopies={3: RationalMatrix.zero(0, 1)},
        name="high_tail_line",
    )

    assert cohomology_dimension(high_tail_line, 3) == 1

    report = verify_kdh_retract_system([high_tail_line])
    assert report.valid is False
    assert ("high_tail_line", 3, 1) in report.high_tail_cohomology
    assert any(
        "rank-nullity high-tail H^3 has dimension 1" in error
        for error in report.errors
    )


def test_transition_rank_defect_is_detected():
    target = model_contractible_tail_window("target")
    source = model_contractible_tail_window("source")
    maps = {
        2: RationalMatrix.identity(1),
        3: RationalMatrix.zero(1, 1),
        4: RationalMatrix.identity(1),
        5: RationalMatrix.zero(0, 0),
    }
    transition = TransitionMap(source, target, maps, name="rank_defect")
    report = verify_kdh_retract_system([target, source], [transition])

    assert report.valid is False
    assert any(
        "rank(pi^3)=0 is below target dimension 1" in error
        for error in report.errors
    )


def _three_term_contraction(name: str, parameter: int) -> FiniteKDHWindow:
    """Acyclic Q -> Q^2 -> Q with a one-parameter contracting homotopy."""

    a = parameter
    return FiniteKDHWindow(
        dimensions={3: 1, 4: 2, 5: 1},
        differentials={
            3: RationalMatrix.from_rows([[1], [0]]),
            4: RationalMatrix.from_rows([[0, 1]]),
            5: RationalMatrix.zero(0, 1),
        },
        projectors={
            3: RationalMatrix.zero(1, 1),
            4: RationalMatrix.zero(2, 2),
            5: RationalMatrix.zero(1, 1),
        },
        homotopies={
            3: RationalMatrix.zero(0, 1),
            4: RationalMatrix.from_rows([[1, a]]),
            5: RationalMatrix.from_rows([[-a], [1]]),
        },
        name=name,
    )


def test_transition_checks_homotopy_compatibility_independently():
    source = _three_term_contraction("source_a0", parameter=0)
    target = _three_term_contraction("target_a1", parameter=1)

    assert verify_kdh_retract_system([source]).valid
    assert verify_kdh_retract_system([target]).valid

    identity = identity_transition(source, target, name="identity_on_complex")
    report = verify_kdh_retract_system([target, source], [identity])

    assert report.valid is False
    assert any("h pi-pi h is nonzero" in error for error in report.errors)
    assert all("d pi-pi d" not in error for error in report.errors)
    assert all("pi P-P pi" not in error for error in report.errors)


def test_matrix_rank_is_exact_over_fractions():
    rank_two = RationalMatrix.from_rows(
        [[1, 2, 3], [2, 4, 6], [0, 1, 1]]
    )
    determinant_one = RationalMatrix.from_rows(
        [[1, 0, 1], [0, 1, 1], [1, 1, 3]]
    )

    assert rank_two.rank() == 2
    assert determinant_one.rank() == 3


@lru_cache(maxsize=None)
def _partition_count_by_largest_part(total: int, largest_part: int) -> int:
    """Independent recursion: partitions using parts at most largest_part."""

    if total == 0:
        return 1
    if total < 0 or largest_part == 0:
        return 0
    return _partition_count_by_largest_part(
        total, largest_part - 1
    ) + _partition_count_by_largest_part(total - largest_part, largest_part)


def test_heisenberg_window_counts_match_independent_partition_recursion():
    max_weight = 8
    expected = tuple(
        _partition_count_by_largest_part(weight, weight)
        for weight in range(max_weight + 1)
    )
    report = heisenberg_finite_window_report(max_weight)

    assert expected == (1, 1, 2, 3, 5, 7, 11, 15, 22)
    assert report.partition_numbers == expected
    assert report.cumulative_dimension == sum(expected) == 67
    assert report.max_normalized_bar_length == max_weight
    assert report.finite_dimensional
    assert "requires the KDH realization" in report.theorem_h_status
    assert "ordered collision contraction" in report.ordered_residue_status
    assert "second-kind convergence" in report.curved_completion_status
    assert "stabilized image chains" in report.mittag_leffler_reason


def test_heisenberg_dimension_matches_partition_sum_and_vacuum_limit():
    assert partition_numbers_up_to(0) == (1,)
    assert heisenberg_fock_window_dimension(0) == 1
    assert heisenberg_fock_window_dimension(1) == 2
    assert heisenberg_fock_window_dimension(4) == 12

    try:
        partition_numbers_up_to(-1)
    except ValueError as exc:
        assert "nonnegative" in str(exc)
    else:  # pragma: no cover
        raise AssertionError("negative weights lie outside the Fock window domain")


def test_engine_names_the_exact_retract_and_family_realization_data():
    text = " ".join(ENGINE.read_text().split())
    for fragment in (
        "finite-window comparison engine",
        "prop:theorem-h-finite-window-kdh-retracts",
        "dh + hd = id - P",
        "projector- and homotopy-compatible",
        "KD_H(A) ~= lim_N K_N",
        "strict Mittag--Leffler tower",
        "ordered residue contraction",
        "curved second-kind convergence",
        "rank-nullity cohomology dimensions",
        "partition counts",
    ):
        assert fragment in text
