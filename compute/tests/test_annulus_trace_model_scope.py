"""Scope guards for the annulus-trace Hochschild model.

The review B3/Gelfand gate requires algebraic Hochschild chains,
cyclic/negative-cyclic refinements, THH, and finite table metadata to
remain separate.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
THQG_TEX = ROOT / "chapters" / "connections" / "thqg_open_closed_realization.tex"
ANNULUS_ENGINE = ROOT / "compute" / "lib" / "annulus_trace_verification.py"
ANNULUS_TEST = ROOT / "compute" / "tests" / "test_annulus_trace_verification.py"
AUDIT_SWEEP = ROOT / "compute" / "audit" / "compute_chirhoch_complete_sweep.md"
LEDGER = ROOT / "notes" / "audit_repairs_ledger_20260610.md"
MATRIX = ROOT / "notes" / "external_review_harvest_matrix_20260617.md"


def _flat(path: Path) -> str:
    return " ".join(path.read_text().split())


def test_annulus_theorem_uses_hochschild_chain_model_not_naive_cyclic_quotient():
    source = _flat(THQG_TEX)

    for required in [
        "is the Hochschild cyclic-object model",
        "ordinary Hochschild boundary, including the wrap-around face",
        "not the coinvariant quotient of an ordinary ordered bar complex",
        "Connes' operator belongs to the cyclic/negative-cyclic refinement",
        r"$\operatorname{THH}$ requires an explicit open/closed MC element",
    ]:
        assert required in source

    for forbidden in [
        r"\otimes_{(\mathbb{Z}/n\mathbb{Z})} A_b",
        "same datum as a cyclic word",
        "this differential becomes the standard algebraic Hochschild boundary",
    ]:
        assert forbidden not in source


def test_annulus_compute_helper_is_finite_table_metadata_not_proof_engine():
    engine = _flat(ANNULUS_ENGINE)
    test_source = _flat(ANNULUS_TEST)
    combined = f"{engine} {test_source}"

    for required in [
        "finite annulus-trace table helper",
        "does not build a Hochschild chain complex",
        "does not prove Theorem H",
        "The ordinary Hochschild chain differential is \\(b\\)",
        "not topological Hochschild homology",
        "finite schematic table",
        "These tests preserve the old schematic table row",
    ]:
        assert required in combined

    for forbidden in [
        "H_n(B^cyc_*(A), b + B)",
        "Theorem H + CY duality",
        "TOPOLOGICAL annulus partition function",
        "Z_ann = Tr(Id) = dim HH_0 = 1",
        "Verifies: 1. Hochschild homology dimensions",
    ]:
        assert forbidden not in combined


def test_audit_matrix_records_annulus_scope_repair():
    audit = _flat(AUDIT_SWEEP)
    ledger = _flat(LEDGER)
    matrix = _flat(MATRIX)

    assert "annulus_trace_verification.py AUDITED + FENCED" in audit
    assert "Pass 549: Annulus Hochschild chain-model firewall" in ledger
    assert "Pass 549 fences the annulus trace proof and compute helper" in matrix
