"""Independent arithmetic guards for the affine type-A H1 audit."""

from __future__ import annotations

import pytest

from compute.lib.chirhoch_sl_n_outer_derivations_engine import (
    CHART_H1_OBLIGATION,
    affine_sl_n_outer_derivation_audit,
    compute_chirhoch1_affine_sl_n,
    verify_fr4_conjecture,
)


@pytest.mark.parametrize("N", range(2, 9))
def test_exact_adjoint_zero_mode_dimension(N):
    audit = affine_sl_n_outer_derivation_audit(N)
    expected = N * N - 1
    assert audit.lie_dimension == expected
    assert audit.adjoint_zero_mode_dimension == expected
    assert audit.known_inner_zero_mode_dimension == expected


@pytest.mark.parametrize("N", range(2, 9))
def test_full_chart_quotient_is_withheld(N):
    audit = affine_sl_n_outer_derivation_audit(N)
    assert audit.chart_chirhoch1_dimension is None
    assert compute_chirhoch1_affine_sl_n(N) is None
    assert audit.status == "open-complete-chiral-derivation-quotient"
    assert audit.resolution_obligation == CHART_H1_OBLIGATION


def test_family_report_contains_exact_arithmetic_and_open_status():
    report = verify_fr4_conjecture()
    assert set(report) == set(range(2, 9))
    for N, audit in report.items():
        assert audit.lie_dimension == N * N - 1
        assert audit.chart_chirhoch1_dimension is None


def test_critical_level_has_separate_scope():
    with pytest.raises(ValueError, match="critical"):
        affine_sl_n_outer_derivation_audit(5, -5)


@pytest.mark.parametrize("value", [1, 0, -2, 2.5, "sl2"])
def test_invalid_rank(value):
    with pytest.raises(ValueError):
        affine_sl_n_outer_derivation_audit(value)
