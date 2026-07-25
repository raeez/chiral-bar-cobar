"""Guards for the ordered OPE-mode/BD chiral-operation comparison."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
BAR = ROOT / "chapters/theory/bar_construction.tex"
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"
LEDGER = ROOT / "notes/audit_repairs_ledger_20260610.md"


def visible(path: Path) -> str:
    return "\n".join(
        line
        for line in path.read_text().splitlines()
        if not line.lstrip().startswith("%")
    )


def assert_anchor(window: str, anchor: str) -> None:
    normalized_window = re.sub(r"\s+", " ", window)
    normalized_anchor = re.sub(r"\s+", " ", anchor)
    assert anchor in window or normalized_anchor in normalized_window, anchor


class TestBarOpeModeBDComparisonScope:
    def test_arbitrary_mode_residue_formula_keeps_every_ope_pole(self):
        text = visible(BAR)
        required = (
            "Arbitrary-mode ordered residue formula",
            r"\label{thm:residue-formula}",
            r"\label{eq:ordered-residue-arbitrary-mode}",
            r"d_{(m),I}\bigl([a_1|\cdots|a_N]\otimes\omega\bigr)",
            r"\epsilon_B(I;a_\bullet,\omega)",
            r"Theorem~\ref{thm:bar-sign-coherence}",
            r"\operatorname{pr}_m\mu_{\mathrm{BD}}(a_i,a_j)",
            r"=a_i{}_{(m)}a_j",
            "The Poincar\\'e residue removes only the logarithmic form factor",
            "it never imposes \\(m=0\\)",
            "no higher pole can be lost by the form-residue operation",
        )
        for anchor in required:
            assert_anchor(text, anchor)

    def test_bd_chiral_operation_comparison_is_typed_and_not_a_polar_kernel(self):
        text = visible(BAR)
        required = (
            "BD chiral operation and full OPE residue",
            r"\label{thm:bd-ope-residue-full-poles}",
            r"\ClaimStatusProvedHere",
            "Beilinson--Drinfeld/Ran presentation compared with the ordered",
            "ordered-to-symmetric\ncomparison only after a separate descent datum",
            r"\mu_{\mathrm{BD}}\colon",
            r"\operatorname{pr}_m\mu_{\mathrm{BD}}(a,b)=a_{(m)}b",
            "No singular OPE\nmode is discarded",
            r"\eqref{eq:ordered-residue-arbitrary-mode}",
            "Higher poles are therefore part of\n$d_{\\mathrm{res}}$",
            "not the polar connection\nkernel",
            "does\nnot multiply the OPE pole by a second propagator pole",
            r"\cite[\S\S3.3--3.4]{BD04}",
            r"Proposition~\ref{prop:pole-decomposition}",
            r"Theorem~\ref{thm:bar-sign-coherence}",
        )
        for anchor in required:
            assert_anchor(text, anchor)

    def test_symmetric_bd_residue_remains_conditional_on_descent(self):
        text = visible(BAR)
        required = (
            "Symmetric BD residue after descent",
            r"\label{cor:bd-ope-symmetric-ran-differential}",
            r"\ClaimStatusConditional",
            "ordered-to-symmetric\ndescent datum",
            r"Proposition~\ref{prop:symmetric-bar-descent-criterion}",
            "Without that descent datum this quotient is only a graded",
            "not asserted to be a dg factorisation\ncoalgebra",
        )
        for anchor in required:
            assert_anchor(text, anchor)

    def test_review_harvest_records_bd_ope_mode_pass(self):
        matrix = MATRIX.read_text()
        ledger = LEDGER.read_text()
        for text in (matrix, ledger):
            normalized = re.sub(r"\s+", " ", text)
            assert "Pass 545" in text
            assert "BD chiral operation and full OPE residue" in normalized
