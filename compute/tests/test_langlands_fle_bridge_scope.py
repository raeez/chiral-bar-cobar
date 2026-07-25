"""Scope guard for the legacy Langlands/FLE bridge helper.

The helper is a finite critical-level consistency suite for the
cohomological shadow of the FLE.  It must not present the critical
reflection fixed point as strict Koszul self-duality or as a proof of the
categorical FLE.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

ENGINE = ROOT / "compute/lib/theorem_langlands_fle_bridge_engine.py"
TESTS = ROOT / "compute/tests/test_theorem_langlands_fle_bridge_engine.py"
LEDGER = ROOT / "notes/audit_repairs_ledger_20260610.md"
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"


def text(path: Path) -> str:
    return path.read_text()


def compact(source: str) -> str:
    return " ".join(source.split())


def test_bridge_helper_declares_finite_cohomological_shadow_scope():
    combined = text(ENGINE) + "\n" + text(TESTS)
    compacted = compact(combined)
    required = (
        "finite critical-level consistency checks",
        "not a proof of the categorical FLE",
        "cohomological shadow",
        "does not identify critical centers, chiral Koszul duals",
        "level-reflection fixed point only",
        "not strict Koszul self-duality",
        "not membership in KSDual",
        "Generic-level Koszulness is a separate",
        "outside the generic Koszul locus",
    )
    for fragment in required:
        assert compact(fragment) in compacted


def test_bridge_helper_retired_false_proof_and_self_duality_phrases():
    combined = text(ENGINE) + "\n" + text(TESTS)
    retired = (
        "THEOREM (Langlands FLE bridge",
        "verifies the bridge by SIX INDEPENDENT METHODS",
        "Proved by SIX INDEPENDENT METHODS",
        "Full six-method verification",
        "Full FLE bridge verification",
        "At the fixed point: the Koszul dual is the algebra itself",
        "complementarity becomes self-complementarity",
        "holds at ALL generic",
        "bar cohomology = Koszul dual algebra",
        "At critical level, the algebra is self-dual",
        "dual algebra is V_{k'}",
        "Verify the FLE bridge for all standard simple Lie algebras",
    )
    for fragment in retired:
        assert fragment not in combined


def test_bridge_result_runtime_metadata_exposes_scope():
    from compute.lib.theorem_langlands_fle_bridge_engine import (
        ff_involution_analysis,
        lie_data,
        verify_fle_bridge,
    )

    result = verify_fle_bridge("A", 1, max_weight=6)
    assert result.all_methods_pass
    assert "finite critical-level consistency checks" in result.verification_scope
    assert "not a proof of the categorical FLE" in result.verification_scope
    assert "not strict Koszul self-duality" in result.ff_fixed_point_scope
    assert result.not_koszul_self_dual is True
    assert result.critical_not_koszul is True

    reflection = ff_involution_analysis(lie_data("A", 1), -2)
    assert reflection["is_ff_fixed_point"] is True
    assert reflection["not_koszul_self_dual"] is True
    assert "not strict Koszul self-duality" in reflection["ff_fixed_point_scope"]


def test_pass_551_is_recorded_in_ledger_and_matrix():
    ledger = text(LEDGER)
    matrix = text(MATRIX)
    assert "Pass 551: FLE critical-level reflection scope" in ledger
    assert "Pass 551 fences the legacy Langlands/FLE bridge helper" in matrix
    assert "finite critical-level consistency checks" in matrix
