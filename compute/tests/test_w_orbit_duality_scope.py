"""Guards for W-orbit duality evidence versus theorem status."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
W_TEX = ROOT / "chapters/examples/w_algebras.tex"
LIB = ROOT / "compute/lib/w_orbit_duality.py"
TESTS = ROOT / "compute/tests/test_w_orbit_duality.py"
BP_LIB = ROOT / "compute/lib/bp_koszul_conductor_engine.py"
BP_TESTS = ROOT / "compute/tests/test_bp_koszul_conductor_engine.py"
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


class TestWOrbitDualityScope:
    def test_principal_w_theorem_remains_conditional_and_principal(self):
        text = visible_text(W_TEX)
        theorem = normalized(environment_window(text, "thm:w-algebra-koszul-main", 70))
        scope = normalized(environment_window(text, "rem:w-principal-theorem-scope", 25))
        conjecture = normalized(environment_window(text, "conj:w-orbit-duality", 25))

        assert "\\ClaimStatusConditional" in theorem
        assert "principal W-algebra" in theorem
        assert "DS/bar transport package" in theorem
        assert "Theorem~\\ref{thm:w-algebra-koszul-main} proves only the principal" in scope
        assert "belongs to Conjecture~\\ref{conj:w-orbit-duality}" in scope
        assert "is not used in the proof of the principal result" in scope
        assert "\\ClaimStatusConjectured" in conjecture

    def test_compute_layer_is_evidence_not_conjecture_proof(self):
        lib = normalized(LIB.read_text())
        tests = normalized(TESTS.read_text())
        combined = lib + " " + tests

        required = (
            "W-orbit duality: finite evidence and consistency checks",
            "This module does not prove conj:w-orbit-duality",
            "conditional principal characteristic transport",
            "conj:bp-duality (BP self-duality conjecture; conductor evidence only)",
            "Finite evidence for W-orbit duality",
            "They do not prove conj:w-orbit-duality",
            "Finite type-A consistency packet",
            "Computed complementarity table",
        )
        for fragment in required:
            assert fragment in combined

        forbidden = (
            "computational verification of conj:w-orbit-duality",
            "conj:w-orbit-duality verification",
            "prop:bp-duality (BP self-duality " + "proved)",
            "Full type-A verification",
            "Verified complementarity table",
        )
        for fragment in forbidden:
            assert fragment not in combined

    def test_bp_conductor_compute_layer_is_scalar_diagnostic_not_duality_proof(self):
        lib = normalized(BP_LIB.read_text())
        tests = normalized(BP_TESTS.read_text())
        combined = lib + " " + tests

        required = (
            "scalar-conductor diagnostics",
            "These identities are scalar companion checks",
            "do not prove BP same-family Koszul duality",
            "non-principal DS/bar transport",
            "bar-cobar inversion",
            "Theorem H",
            "subregular DS/bar transport hypothesis",
            "SCALAR-DIAGNOSTIC TESTS",
            "exact scalar identities",
            "scalar polynomial identity",
        )
        for fragment in required:
            assert fragment in combined

        forbidden = (
            "THEOREM-LEVEL " + "TESTS",
            "THEOREM-LEVEL " + "ENGINE",
            "proves BP same-family Koszul duality",
            "proof of BP same-family Koszul " + "duality",
            "BP same-family Koszul duality is " + "proved",
            "prop:bp-duality (BP self-duality " + "proved)",
            "proof of Theorem " + "H",
        )
        for fragment in forbidden:
            assert fragment not in combined

    def test_harvest_matrix_and_ledger_record_w_orbit_scope_pass(self):
        ledger = LEDGER.read_text()
        matrix = MATRIX.read_text()

        assert "Pass 531: W-orbit compute evidence scoped" in ledger
        assert "Pass 554: BP scalar-conductor compute scope" in ledger
        assert "Pass 531" in matrix
        assert "Pass 554" in matrix
        assert "W-orbit compute layer" in matrix
