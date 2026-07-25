"""Tests for the rank-one Heisenberg curved second-kind endpoint."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

from compute.lib.curved_second_kind_heisenberg_engine import (
    curved_second_kind_heisenberg_report,
)


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/theory/chiral_hochschild_koszul.tex"
ENGINE = ROOT / "compute/lib/curved_second_kind_heisenberg_engine.py"
LEDGER = ROOT / "notes/audit_repairs_ledger_20260610.md"
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"


def test_nonzero_level_curved_second_kind_window_is_scalar():
    report = curved_second_kind_heisenberg_report(Fraction(2, 3), 5)

    assert report.coefficients == tuple(Fraction(-2 * n, 3) for n in range(1, 6))
    assert report.vacuum_cohomology_dim == 1
    assert report.positive_weight_cohomology == tuple((n, 0) for n in range(1, 6))
    assert report.strict_mittag_leffler
    assert report.proves_curved_second_kind_endpoint
    assert report.proves_theorem_h is False
    assert "curved second-kind endpoint only" in report.logical_scope
    assert "not ordered residue-twisted acyclicity" in report.logical_scope
    assert "not a proof of Theorem H" in report.logical_scope


def test_zero_level_curvature_does_not_contract_positive_weights():
    report = curved_second_kind_heisenberg_report(0, 3)

    assert report.coefficients == (0, 0, 0)
    assert report.positive_weight_cohomology == ((1, 1), (2, 1), (3, 1))
    assert report.strict_mittag_leffler is False
    assert report.proves_curved_second_kind_endpoint is False


def test_manuscript_curved_dual_lemma_is_proved_with_finite_window_contraction():
    text = TARGET.read_text()
    label = r"\label{lem:curved-dual-centre-heisenberg}"
    assert label in text
    start = text.rindex(r"\begin{lemma}", 0, text.index(label))
    block = text[start:text.index(r"\end{proof}", start)]
    flat = " ".join(block.split())

    required = (
        "Curved-dual centre of the Heisenberg algebra",
        r"\ClaimStatusProvedHere",
        "finite tensor product of oscillator Koszul--Clifford pairs",
        "nonzero coefficients \\(kn\\)",
        r"0\longrightarrow \C\cdot e_n",
        r"\xrightarrow{\ -kn\ }",
        r"h_n(f_n)=(-kn)^{-1}e_n",
        "strict Mittag--Leffler",
        r"R^1\!\varprojlim",
        "completed second-kind convergence",
        "scalar centre",
    )
    for fragment in required:
        assert fragment in flat


def test_heisenberg_residual_text_no_longer_lists_curved_convergence_as_open():
    text = TARGET.read_text()
    label = r"\label{prop:heisenberg-theorem-h-window-certificate}"
    start = text.rindex(r"\begin{proposition}", 0, text.index(label))
    block = text[start:text.index(r"\end{proposition}", start)]
    flat = " ".join(block.split())

    assert "completed second-kind convergence obligation" not in flat
    assert "curved second-kind degree-\\(2\\) endpoint is supplied separately" in flat
    assert "ordered residue-twisted acyclicity input" in flat
    assert "PBW/averaging descent package" in flat


def test_engine_and_harvest_controls_record_pass_570():
    engine = ENGINE.read_text()
    ledger = LEDGER.read_text()
    matrix = MATRIX.read_text()

    assert "lem:curved-dual-centre-heisenberg" in engine
    assert "does not prove ordered" in engine
    assert "Pass 570" in ledger
    assert "curved second-kind heisenberg endpoint" in ledger.lower()
    assert "Pass 570" in matrix
    assert "curved second-kind heisenberg endpoint" in matrix.lower()
