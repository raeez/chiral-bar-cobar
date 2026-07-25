"""Guards for CME/QME and physical BV quantization scope."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
KOSZUL_PAIR = ROOT / "chapters/theory/koszul_pair_structure.tex"
BV_BRST = ROOT / "chapters/connections/bv_brst.tex"
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"


def _text(path: Path) -> str:
    return " ".join(path.read_text().split())


def test_koszul_pair_qme_is_algebraic_shell_not_all_loop_physics():
    text = _text(KOSZUL_PAIR)
    required = [
        "algebraic modular QME shell",
        "finite-window identity in the completed modular convolution algebra",
        "not an all-loop analytic QME for a physical factorization algebra",
        "It becomes a physical all-loop QME only after a local-observables model",
        "propagator, renormalization scale, counterterms, analytic SDR",
        "anomaly-cancellation package",
    ]
    for fragment in required:
        assert fragment in text


def test_bv_brst_keeps_classical_pva_separate_from_all_loop_qme():
    text = _text(BV_BRST)
    required = [
        "Finite-type PVA BV/QME gate",
        "classical master equation is equivalent to the PVA Hamiltonian condition",
        "The all-loop quantum master equation is not a consequence",
        "analytic strong deformation retract",
        "counterterms",
    ]
    for fragment in required:
        assert fragment in text


def test_old_unqualified_qme_equals_mc_phrase_does_not_return():
    text = _text(KOSZUL_PAIR)
    assert "The QME is the Maurer--Cartan equation in the modular convolution algebra" not in text


def test_harvest_matrix_records_physics_local_pass():
    text = _text(MATRIX)
    assert "K Physics and open/closed bridges" in text
    assert "Pass 509" in text
    assert "applied for local physics-surface harvest" in text
