"""Guards for Etingof--Kazhdan quantization signature discipline."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFORMATION = ROOT / "chapters/examples/deformation_quantization.tex"
ORDERED_QG = ROOT / "chapters/theory/ordered_associative_chiral_kd.tex"
E1_MODULAR = ROOT / "chapters/theory/e1_modular_koszul.tex"
DERIVED_LANGLANDS = ROOT / "chapters/theory/derived_langlands.tex"
BAR_CONSTRUCTION = ROOT / "chapters/theory/bar_construction.tex"
VIRASORO_PUR = ROOT / "chapters/theory/virasoro_motivic_purity_all_r_platonic.tex"
MOTIVIC_CLASS_M = ROOT / "chapters/theory/motivic_shadow_full_class_m_platonic.tex"
E1_STANDALONE = ROOT / "standalone/e1_primacy_ordered_bar.tex"
N3_STANDALONE = ROOT / "standalone/N3_e1_primacy.tex"
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"


def _text(path: Path) -> str:
    return " ".join(path.read_text().split())


def test_deformation_quantization_firewall_names_full_ek_signature():
    text = _text(DEFORMATION)
    required = [
        "source Lie bialgebra \\((\\mathfrak g,\\delta)\\)",
        "completed/pro-nilpotent topology",
        "Drinfeld associator \\(\\Phi\\)",
        "target QUE/quasi-Hopf category",
        "specified completed Lie bialgebra, associator, topology, and quasi-Hopf target",
        "source, completion topology, associator, and target categories have been fixed",
    ]
    for fragment in required:
        assert fragment in text


def test_live_ek_surfaces_carry_source_topology_associator_target():
    expectations = {
        ORDERED_QG: [
            "source Lie bialgebra",
            "\\(\\hbar\\)-adic/pro-nilpotent topology",
            "associator",
            "QUE/quasi-Hopf target",
        ],
        E1_MODULAR: [
            "Lie bialgebra \\((\\mathfrak g,\\delta)\\)",
            "\\(\\hbar\\)-adic/pro-nilpotent topology",
            "QUE/quasi-Hopf target category",
        ],
        DERIVED_LANGLANDS: [
            "specified completed Lie bialgebra",
            "\\((\\frakg_{\\Delta_5},\\delta_{\\mathrm{GN}})\\)",
            "\\(\\hbar\\)-adic super-quasi-Hopf target",
        ],
        BAR_CONSTRUCTION: [
            "completed Lie bialgebra",
            "$(\\mathfrak{g}_{\\Delta_5},\\delta_{\\mathrm{GN}})$",
            "chosen associator and pro-\\(\\hbar\\)-adic topology",
            "Etingof--Kazhdan super-quasi-Hopf target",
        ],
        VIRASORO_PUR: [
            "ordered residue package",
            "motivic realization",
            "Tate factorization",
        ],
        MOTIVIC_CLASS_M: [
            "source Lie bialgebra",
            "\\(\\hbar\\)-adic topology",
            "chiral QUE/quasi-Hopf target",
        ],
    }
    for path, fragments in expectations.items():
        text = _text(path)
        for fragment in fragments:
            assert fragment in text, f"{fragment!r} missing from {path}"


def test_standalone_ek_surfaces_are_not_bare_invocations():
    for path in (E1_STANDALONE, N3_STANDALONE):
        text = _text(path)
        assert "source Lie bialgebra" in text
        assert "\\(\\hbar\\)-adic topology" in text
        assert "associator" in text
        assert "QUE/quasi-Hopf target" in text

    retired = [
        r"Etingof--Kazhdan quantisation theorem~\cite{EK96}.",
        "gives the same torsor for quantisation choices of a fixed Lie bialgebra",
        "Etingof--Kazhdan quantization datum has been supplied. The pentagon",
    ]
    for path in (E1_STANDALONE, N3_STANDALONE, E1_MODULAR, ORDERED_QG):
        text = _text(path)
        for fragment in retired:
            assert fragment not in text, f"{fragment!r} remains in {path}"


def test_harvest_matrix_records_ek_signature_pass():
    text = _text(MATRIX)
    assert "B1 / review q-\\(\\hbar\\) gate" in text
    assert "Pass 517" in text
