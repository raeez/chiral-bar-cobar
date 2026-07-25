"""Tests for the two-point Heisenberg residue-twisted Arnold summand."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

from compute.lib.residue_twisted_heisenberg_engine import (
    heisenberg_evaluate_raw_ungraded_residue_combination,
    heisenberg_mixed_mode_residue_report,
    heisenberg_raw_ungraded_kernel_witness,
    heisenberg_single_mode_polynomial_grid,
    heisenberg_single_mode_polynomial_residue_report,
    heisenberg_single_oscillator_residue_report,
    heisenberg_single_oscillator_window,
    heisenberg_two_point_residue_report,
    heisenberg_weight_one_polynomial_residue_report,
    heisenberg_weight_one_polynomial_window,
)


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/theory/chiral_hochschild_koszul.tex"
ENGINE = ROOT / "compute/lib/residue_twisted_heisenberg_engine.py"
LEDGER = ROOT / "notes/audit_repairs_ledger_20260610.md"
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"


def test_two_point_heisenberg_residue_kills_positive_arnold_line():
    report = heisenberg_two_point_residue_report(Fraction(3, 2))

    assert report.level == Fraction(3, 2)
    assert report.differential_entry == Fraction(3, 2)
    assert report.rank == 1
    assert report.kernel_dim_positive_fibre == 0
    assert report.cokernel_dim_degree_zero == 0
    assert report.positive_fibre_acyclic
    assert report.proves_full_ordered_twisted_tensor_acyclicity is False
    assert report.proves_theorem_h is False
    assert "arity-2 rank-one Heisenberg central-current summand only" in report.logical_scope
    assert "not arbitrary Fock monomials" in report.logical_scope
    assert "not a proof of Theorem H" in report.logical_scope


def test_zero_level_is_rejected_by_positive_fibre_cohomology():
    report = heisenberg_two_point_residue_report(0)

    assert report.rank == 0
    assert report.kernel_dim_positive_fibre == 1
    assert report.cokernel_dim_degree_zero == 1
    assert report.positive_fibre_acyclic is False


def test_weight_one_polynomial_string_has_qk_differential():
    reports = heisenberg_weight_one_polynomial_window(Fraction(5, 3), 5)

    assert [report.power for report in reports] == [1, 2, 3, 4, 5]
    assert [report.differential_entry for report in reports] == [
        Fraction(5, 3),
        Fraction(10, 3),
        Fraction(5, 1),
        Fraction(20, 3),
        Fraction(25, 3),
    ]
    for report in reports:
        assert report.rank == 1
        assert report.kernel_dim_positive_fibre == 0
        assert report.cokernel_dim_degree_zero == 0
        assert report.positive_fibre_acyclic
        assert report.proves_full_ordered_twisted_tensor_acyclicity is False
        assert report.proves_theorem_h is False
        assert "weight-one polynomial summand only" in report.logical_scope
        assert "not higher oscillator Fock monomials" in report.logical_scope


def test_weight_one_polynomial_requires_nonzero_level_and_positive_power():
    report = heisenberg_weight_one_polynomial_residue_report(0, 3)

    assert report.differential_entry == 0
    assert report.kernel_dim_positive_fibre == 1
    assert report.cokernel_dim_degree_zero == 1
    assert report.positive_fibre_acyclic is False

    try:
        heisenberg_weight_one_polynomial_residue_report(1, 0)
    except ValueError as exc:
        assert "power must be at least 1" in str(exc)
    else:  # pragma: no cover - defensive assertion
        raise AssertionError("power=0 must be rejected")


def test_single_oscillator_arbitrary_mode_has_nk_differential():
    reports = heisenberg_single_oscillator_window(Fraction(7, 4), 5)

    assert [report.mode for report in reports] == [1, 2, 3, 4, 5]
    assert [report.differential_entry for report in reports] == [
        Fraction(7, 4),
        Fraction(7, 2),
        Fraction(21, 4),
        Fraction(7, 1),
        Fraction(35, 4),
    ]
    for report in reports:
        assert report.rank == 1
        assert report.kernel_dim_positive_fibre == 0
        assert report.cokernel_dim_degree_zero == 0
        assert report.positive_fibre_acyclic
        assert report.proves_full_ordered_twisted_tensor_acyclicity is False
        assert report.proves_theorem_h is False
        assert "single-oscillator arbitrary-mode summand only" in report.logical_scope
        assert "not products of higher oscillators" in report.logical_scope


def test_single_oscillator_requires_nonzero_level_and_positive_mode():
    report = heisenberg_single_oscillator_residue_report(0, 4)

    assert report.differential_entry == 0
    assert report.kernel_dim_positive_fibre == 1
    assert report.cokernel_dim_degree_zero == 1
    assert report.positive_fibre_acyclic is False

    try:
        heisenberg_single_oscillator_residue_report(1, 0)
    except ValueError as exc:
        assert "mode must be at least 1" in str(exc)
    else:  # pragma: no cover - defensive assertion
        raise AssertionError("mode=0 must be rejected")


def test_single_mode_polynomial_grid_has_qnk_differential():
    reports = heisenberg_single_mode_polynomial_grid(Fraction(2, 5), 3, 4)

    assert [(report.mode, report.power) for report in reports] == [
        (1, 1),
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 1),
        (2, 2),
        (2, 3),
        (2, 4),
        (3, 1),
        (3, 2),
        (3, 3),
        (3, 4),
    ]
    assert [report.differential_entry for report in reports] == [
        Fraction(2, 5),
        Fraction(4, 5),
        Fraction(6, 5),
        Fraction(8, 5),
        Fraction(4, 5),
        Fraction(8, 5),
        Fraction(12, 5),
        Fraction(16, 5),
        Fraction(6, 5),
        Fraction(12, 5),
        Fraction(18, 5),
        Fraction(24, 5),
    ]
    for report in reports:
        assert report.rank == 1
        assert report.kernel_dim_positive_fibre == 0
        assert report.cokernel_dim_degree_zero == 0
        assert report.positive_fibre_acyclic
        assert report.proves_full_ordered_twisted_tensor_acyclicity is False
        assert report.proves_theorem_h is False
        assert "single-mode polynomial arbitrary-mode summand only" in report.logical_scope
        assert "not mixed-mode Fock monomials" in report.logical_scope


def test_single_mode_polynomial_requires_nonzero_level_mode_and_power():
    report = heisenberg_single_mode_polynomial_residue_report(0, 3, 4)

    assert report.differential_entry == 0
    assert report.kernel_dim_positive_fibre == 1
    assert report.cokernel_dim_degree_zero == 1
    assert report.positive_fibre_acyclic is False

    for args, message in (
        ((1, 0, 1), "mode must be at least 1"),
        ((1, 1, 0), "power must be at least 1"),
    ):
        try:
            heisenberg_single_mode_polynomial_residue_report(*args)
        except ValueError as exc:
            assert message in str(exc)
        else:  # pragma: no cover - defensive assertion
            raise AssertionError(f"{args} must be rejected")


def test_mixed_mode_formula_returns_exact_weighted_derivative_terms():
    report = heisenberg_mixed_mode_residue_report(Fraction(3, 2), (2, 1, 0, 3))

    assert report.exponents == (2, 1, 0, 3)
    assert [(term.exponents, term.coefficient) for term in report.image_terms] == [
        ((1, 1, 0, 3), Fraction(3, 1)),
        ((2, 0, 0, 3), Fraction(3, 1)),
        ((2, 1, 0, 2), Fraction(18, 1)),
    ]
    assert report.line_source_dim == 1
    assert report.image_dim_upper_bound == 3
    assert report.kernel_dim_positive_line == 0
    assert report.positive_line_acyclic
    assert report.proves_full_mixed_mode_fock_acyclicity is False
    assert report.proves_theorem_h is False
    assert "mixed-mode formula only" in report.logical_scope
    assert "not full mixed-mode Fock-window acyclicity" in report.logical_scope


def test_mixed_mode_formula_handles_vacuum_zero_level_and_bad_exponents():
    vacuum = heisenberg_mixed_mode_residue_report(Fraction(5, 7), ())
    assert vacuum.image_terms == ()
    assert vacuum.kernel_dim_positive_line == 1
    assert vacuum.positive_line_acyclic is False

    zero_level = heisenberg_mixed_mode_residue_report(0, (1, 2))
    assert [term.coefficient for term in zero_level.image_terms] == [0, 0]
    assert zero_level.kernel_dim_positive_line == 1
    assert zero_level.positive_line_acyclic is False

    try:
        heisenberg_mixed_mode_residue_report(1, (1, -1))
    except ValueError as exc:
        assert "exponents must be nonnegative" in str(exc)
    else:  # pragma: no cover - defensive assertion
        raise AssertionError("negative exponents must be rejected")


def test_raw_ungraded_kernel_witness_is_not_full_fock_acyclicity():
    witness = heisenberg_raw_ungraded_kernel_witness(Fraction(9, 5))
    assert witness == (((0, 1), Fraction(1)), ((1,), Fraction(-2)))
    assert heisenberg_evaluate_raw_ungraded_residue_combination(Fraction(9, 5), witness) == {}

    try:
        heisenberg_raw_ungraded_kernel_witness(0)
    except ValueError as exc:
        assert "level must be nonzero" in str(exc)
    else:  # pragma: no cover - defensive assertion
        raise AssertionError("zero level must not produce a nonzero-level witness")


def test_manuscript_records_exact_two_point_scope():
    text = TARGET.read_text()
    label = r"\label{prop:heisenberg-two-point-residue-twisted-acyclicity}"
    assert label in text
    start = text.rindex(r"\begin{proposition}", 0, text.index(label))
    block = text[start:text.index(r"\end{proof}", start)]
    flat = " ".join(block.split())

    required = (
        "Two-point Heisenberg residue-twisted Arnold contraction",
        r"\ClaimStatusProvedHere",
        r"\operatorname{OS}(A_1)",
        r"d_1\bigl([\alpha|\alpha]\otimes\eta_{12}\bigr)",
        r"\alpha_{(1)}\alpha",
        r"k\,\mathbf1",
        r"H^1(C^\bullet_{2,\alpha})=0",
        "not the full conjecture",
        "arbitrary Fock monomials",
        r"higher collision clusters \(m\ge3\)",
        "ordered-to-symmetric descent",
        "completed curved second-kind endpoint",
        r"\eqref{eq:ordered-residue-arbitrary-mode}",
    )
    for fragment in required:
        assert fragment in flat


def test_manuscript_records_weight_one_polynomial_contraction():
    text = TARGET.read_text()
    label = r"\label{prop:heisenberg-two-point-weight-one-polynomial-residue}"
    assert label in text
    start = text.rindex(r"\begin{proposition}", 0, text.index(label))
    block = text[start:text.index(r"\end{proof}", start)]
    flat = " ".join(block.split())

    required = (
        "Two-point Heisenberg weight-one polynomial residue contraction",
        r"\ClaimStatusProvedHere",
        r"u_q=\alpha_{-1}^{q}\mathbf1",
        r"d_1\bigl([\alpha|u_q]\otimes\eta_{12}\bigr)",
        r"\alpha_{(1)}u_q",
        r"qk\,u_{q-1}",
        r"H^1(C^\bullet_{2,q})=0",
        r"[\alpha_m,\alpha_n]=mk\delta_{m+n,0}\mathbf1",
        r"[\alpha_1,\alpha_{-1}^{q}]",
        "single-mode higher-oscillator polynomial extension",
        "not prove the ordered twisted-tensor acyclicity",
        "mixed-mode oscillator monomials",
        r"clusters \(m\geq3\)",
    )
    for fragment in required:
        assert fragment in flat


def test_manuscript_records_single_oscillator_arbitrary_mode_contraction():
    text = TARGET.read_text()
    label = r"\label{prop:heisenberg-two-point-single-oscillator-residue}"
    assert label in text
    start = text.rindex(r"\begin{proposition}", 0, text.index(label))
    block = text[start:text.index(r"\end{proof}", start)]
    flat = " ".join(block.split())

    required = (
        "Two-point Heisenberg single-oscillator arbitrary-mode residue contraction",
        r"\ClaimStatusProvedHere",
        r"v_n=\alpha_{-n}\mathbf1",
        r"d_1^{(n)}\bigl([\alpha|v_n]\otimes\eta_{12}\bigr)",
        r"\alpha_{(n)}v_n",
        r"nk\,\mathbf1",
        r"H^1(C^\bullet_{2,n})=0",
        r"[\alpha_m,\alpha_n]=mk\delta_{m+n,0}\mathbf1",
        r"[\alpha_n,\alpha_{-n}]",
        r"\eqref{eq:ordered-residue-arbitrary-mode}",
        "single higher-oscillator arbitrary-mode summands",
        "single-mode powers",
        "does not prove the ordered twisted-tensor acyclicity",
        "mixed-mode oscillator monomials",
        r"clusters \(m\geq3\)",
    )
    for fragment in required:
        assert fragment in flat


def test_manuscript_records_single_mode_polynomial_arbitrary_mode_contraction():
    text = TARGET.read_text()
    label = r"\label{prop:heisenberg-two-point-single-mode-polynomial-residue}"
    assert label in text
    start = text.rindex(r"\begin{proposition}", 0, text.index(label))
    block = text[start:text.index(r"\end{proof}", start)]
    flat = " ".join(block.split())

    required = (
        "Two-point Heisenberg single-mode polynomial arbitrary-mode residue contraction",
        r"\ClaimStatusProvedHere",
        r"u_{n,q}=\alpha_{-n}^{q}\mathbf1",
        r"d_1^{(n)}\bigl([\alpha|u_{n,q}]\otimes\eta_{12}\bigr)",
        r"\alpha_{(n)}u_{n,q}",
        r"q\,n\,k\,u_{n,q-1}",
        r"H^1(C^\bullet_{2,n,q})=0",
        r"[\alpha_m,\alpha_n]=mk\delta_{m+n,0}\mathbf1",
        r"[\alpha_n,\alpha_{-n}^{q}]",
        r"\eqref{eq:ordered-residue-arbitrary-mode}",
        "single-mode polynomial strings",
        "does not prove the ordered twisted-tensor acyclicity",
        "mixed-mode oscillator monomials",
        "full Fock-window linear combinations",
        r"clusters \(m\geq3\)",
    )
    for fragment in required:
        assert fragment in flat


def test_manuscript_records_mixed_mode_formula_and_raw_kernel_boundary():
    text = TARGET.read_text()
    label = r"\label{prop:heisenberg-two-point-mixed-mode-residue-formula}"
    assert label in text
    start = text.rindex(r"\begin{proposition}", 0, text.index(label))
    block = text[start:text.index(r"\end{proof}", start)]
    flat = " ".join(block.split())

    required = (
        "Two-point Heisenberg mixed-mode residue formula",
        r"\ClaimStatusProvedHere",
        r"u_{\mathbf q}",
        r"\prod_{r\ge1}\alpha_{-r}^{q_r}\mathbf1",
        r"d_1\bigl([\alpha|u_{\mathbf q}]\otimes\eta_{12}\bigr)",
        r"k\sum_{r:q_r>0} r q_r\,u_{\mathbf q-\mathbf e_r}",
        r"\alpha_{(r)}u_{\mathbf q}",
        r"r k q_r\,u_{\mathbf q-\mathbf e_r}",
        "line-to-image two-term summand",
        "not a proof of full Fock-window acyclicity",
        r"L_k=k\sum_{r\ge1}r\,\partial_{x_r}",
        r"L_k(x_2-2x_1)=0",
        "actual graded residue-twisted/Koszul complex",
    )
    for fragment in required:
        assert fragment in flat


def test_engine_and_harvest_controls_record_scope():
    engine = ENGINE.read_text()
    ledger = LEDGER.read_text()
    matrix = MATRIX.read_text()

    assert "prop:heisenberg-two-point-residue-twisted-acyclicity" in engine
    assert "not higher oscillator Fock monomials" in engine
    assert "prop:heisenberg-two-point-weight-one-polynomial-residue" in engine
    assert "q*k" in engine
    assert "prop:heisenberg-two-point-single-oscillator-residue" in engine
    assert "n*k" in engine
    assert "prop:heisenberg-two-point-single-mode-polynomial-residue" in engine
    assert "q*n*k" in engine
    assert "heisenberg_mixed_mode_residue_report" in engine
    assert "prop:heisenberg-two-point-mixed-mode-residue-formula" in ledger
    assert "mixed-mode residue formula" in ledger.lower()
    assert "Pass 569" in ledger
    assert "two-point heisenberg residue-twisted arnold" in ledger.lower()
    assert "Pass 571" in ledger
    assert "weight-one polynomial string" in ledger.lower()
    assert "Pass 572" in ledger
    assert "single-oscillator arbitrary-mode" in ledger.lower()
    assert "Pass 573" in ledger
    assert "single-mode polynomial" in ledger.lower()
    assert "Pass 574" in ledger
    assert "Pass 569" in matrix
    assert "two-point heisenberg residue-twisted arnold" in matrix.lower()
    assert "Pass 571" in matrix
    assert "weight-one polynomial string" in matrix.lower()
    assert "Pass 572" in matrix
    assert "single-oscillator arbitrary-mode" in matrix.lower()
    assert "Pass 573" in matrix
    assert "single-mode polynomial" in matrix.lower()
    assert "Pass 574" in matrix
    assert "mixed-mode formula" in matrix.lower()
