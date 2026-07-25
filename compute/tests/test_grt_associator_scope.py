"""Guards for GRT/associator scope discipline."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ORDERED_QG = ROOT / "chapters/theory/ordered_associative_chiral_kd.tex"
ARITHMETIC = ROOT / "chapters/connections/arithmetic_shadows.tex"
E1_STANDALONE = ROOT / "standalone/e1_primacy_ordered_bar.tex"
EN_STANDALONE = ROOT / "standalone/en_chiral_operadic_circle.tex"
ORDERED_STANDALONE = ROOT / "standalone/ordered_chiral_homology.tex"
SEVEN_FACES = ROOT / "standalone/seven_faces.tex"
ANTIPATTERNS = ROOT / "notes/antipatterns_catalogue.md"


def _text(path: Path) -> str:
    return " ".join(path.read_text().split())


def test_chiral_qg_torsor_remark_is_h0_shadow_only():
    text = _text(ORDERED_QG)
    required = [
        "The invariant actually used below is narrower",
        r"verified $\mathfrak{sl}_2$ and affine Kac--Moody checks",
        r"bar-side $\mathrm{H}^0$ shadow",
        "associator-independence is a comparison hypothesis",
        "not a formal consequence of the $\\mathrm{GRT}_1$ action",
        "It does not prove $\\mathrm{GRT}_1$-triviality of categorical modular data",
        "any root-of-unity BKM $S$-matrix",
        "a stronger chain-level claim requires fixing a specific associator class",
    ]
    for fragment in required:
        assert fragment in text


def test_arithmetic_s_matrix_firewall_names_categorical_modular_data():
    text = _text(ARITHMETIC)
    required = [
        r"Conditional GRT$_1$-invariance of the $130\times 130$ $S$-matrix",
        r"the GRT$_1$ action on categorical modular data is trivial",
        r"no proof even for this finite scalar $S$-matrix without the displayed factorisation",
        "it does not prove GRT$_1$-triviality of categorical modular data",
    ]
    for fragment in required:
        assert fragment in text


def test_standalone_surfaces_do_not_extrapolate_grt_triviality():
    e1 = _text(E1_STANDALONE)
    en = _text(EN_STANDALONE)
    ordered = _text(ORDERED_STANDALONE)
    seven = _text(SEVEN_FACES)

    assert "For general $\\fg$ this is a comparison hypothesis" in e1
    assert "No categorical modular datum or Drinfeld-centre object is claimed" in e1
    assert "For general simple $\\fg$ this independence is an additional comparison hypothesis" in en
    assert "it says nothing by itself about categorical modular data" in en
    assert "After fixing an associator gauge" in ordered
    assert "does not upgrade this scalar shadow into an associator-independent chain-level object" in ordered
    assert r"\ClaimStatusConditional" in seven
    assert "not a theorem that categorical modular data, the Drinfeld centre" in seven


def test_antipattern_catalogue_records_conditional_chiral_qg_scope():
    text = _text(ANTIPATTERNS)
    required = [
        "ORDERED (base): CONDITIONAL on the ordered Koszul locus",
        r"`\ClaimStatusConditional`",
        r"general simple-$\fg$ independence is a comparison hypothesis",
        "no categorical modular datum follows from the torsor alone",
    ]
    for fragment in required:
        assert fragment in text


def test_retired_grt_overclaims_are_absent_from_current_surfaces():
    forbidden = [
        "extended structurally to all simple",
        r"the $\GRT_1$ action on the $\Pthree$ bracket is trivial for simple",
        r"are $\mathrm{GRT}_1(\bQ)$-trivial on $H^0$: any two associators",
        r"is the unique (up to $\GRT_1$-action) non-trivial element",
        "the GRT$_1$ action on modular data is trivial.",
    ]
    for path in (
        ORDERED_QG,
        ARITHMETIC,
        E1_STANDALONE,
        EN_STANDALONE,
        ORDERED_STANDALONE,
        SEVEN_FACES,
        ANTIPATTERNS,
    ):
        text = _text(path)
        for fragment in forbidden:
            assert fragment not in text, f"{fragment!r} remains in {path}"
