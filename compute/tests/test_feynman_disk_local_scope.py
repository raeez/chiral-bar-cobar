"""Guards for the disk-local ternary/Feynman comparison scope."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
FEYNMAN = ROOT / "chapters/connections/feynman_diagrams.tex"
EDITORIAL = ROOT / "chapters/connections/editorial_constitution.tex"
LIB = ROOT / "compute/lib/mc5_disk_local.py"
TESTS = ROOT / "compute/tests/test_mc5_disk_local.py"
LEDGER = ROOT / "notes/audit_repairs_ledger_20260610.md"
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"


def visible_text(path: Path) -> str:
    return "\n".join(
        line for line in path.read_text().splitlines() if not line.lstrip().startswith("%")
    )


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def environment_window(text: str, label: str, lines: int) -> str:
    anchor = rf"\label{{{label}}}"
    assert anchor in text, label
    prefix, suffix = text.split(anchor, 1)
    begin = prefix.rfind(r"\begin{")
    assert begin != -1, label
    return "\n".join((prefix[begin:] + anchor + suffix).splitlines()[:lines])


def window_after_phrase(text: str, phrase: str, lines: int) -> str:
    assert phrase in text, phrase
    return "\n".join(text.split(phrase, 1)[1].splitlines()[:lines])


class TestFeynmanDiskLocalScope:
    def test_compactified_ternary_proposition_is_pure_logarithmic_reduction(self):
        text = visible_text(FEYNMAN)
        window = normalized(
            environment_window(text, "prop:compactified-ternary-two-channel", 75)
        )

        required = (
            "Two-channel reduction for a compactified logarithmic ternary packet",
            "\\ClaimStatusProvedHere",
            "geometric/logarithmic comparison lemma",
            "two already constructed logarithmic $1$-forms",
            "same boundary-channel labelling and orientation convention",
            "residue theorem on~$\\bP^1$",
            "$H^0(\\bP^1,\\Omega^1_{\\bP^1})=0$",
            "purely logarithmic $\\bP^1$ residue reduction",
            "does not construct the perturbative ternary form",
            "does not compare it with the bar form",
            "does not prove Conjecture~\\ref{conj:v1-disk-local-perturbative-fm}",
        )
        for fragment in required:
            assert fragment in window

        forbidden = (
            "Two-channel reduction after compactifying the ternary packet",
            "Once the local ternary forms are constructed on $\\overline{M}_{0,4}$",
        )
        for fragment in forbidden:
            assert fragment not in window

    def test_application_remark_is_conditional_not_conjecture_promotion(self):
        text = visible_text(FEYNMAN)
        window = normalized(
            window_after_phrase(
                text, r"\begin{remark}[Conditional application to the disk-local", 18
            )
        )

        required = (
            "only after the compactified perturbative and bar logarithmic forms",
            "have been constructed on $\\overline{M}_{0,4}$",
            "reduces the ternary comparison from three residue equalities to two",
            "does not supply the compactification/Stokes upgrade",
            "or the perturbative/FM identification",
        )
        for fragment in required:
            assert fragment in window

    def test_editorial_route_uses_reduction_language_only_after_forms_exist(self):
        text = normalized(visible_text(EDITORIAL))

        required = (
            "supplies only the logarithmic $\\bP^1$ residue reduction",
            "once the compactified perturbative and bar logarithmic ternary forms",
            "have been constructed with the stated pole and orientation conventions",
            "does not construct the compactified perturbative form or prove the",
            "disk-local perturbative/FM comparison",
        )
        for fragment in required:
            assert fragment in text

    def test_compute_headers_are_finite_evidence_not_conjecture_verification(self):
        lib = normalized(LIB.read_text())
        tests = normalized(TESTS.read_text())
        combined = lib + " " + tests

        required = (
            "finite symbolic evidence for the disk-local perturbative/FM comparison",
            "It does not prove conj:disk-local-perturbative-fm",
            "Finite C2/C3 evidence for the MC5 disk-local packet",
            "They do not prove conj:disk-local-perturbative-fm",
        )
        for fragment in required:
            assert fragment in combined

        forbidden = (
            "This module verifies conj:disk-local-perturbative-fm",
            "Verifies conj:disk-local-perturbative-fm",
        )
        for fragment in forbidden:
            assert fragment not in combined

    def test_harvest_matrix_and_ledger_record_disk_local_pass(self):
        ledger = LEDGER.read_text()
        matrix = MATRIX.read_text()

        assert "Pass 529: Disk-local ternary comparison scoped" in ledger
        assert "Pass 529" in matrix
        assert "pure logarithmic two-channel residue lemma" in matrix
