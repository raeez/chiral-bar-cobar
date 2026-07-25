"""Guards for the Siegel--Borcherds target-cocycle scope."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HOCHSCHILD = ROOT / "chapters/theory/hochschild_cohomology.tex"
NILPOTENT = ROOT / "chapters/theory/nilpotent_completion.tex"
THEOREM_B_SCOPE = ROOT / "chapters/theory/theorem_B_scope_platonic.tex"
E1_MODULAR = ROOT / "chapters/theory/e1_modular_koszul.tex"
YANGIAN_DK = ROOT / "chapters/examples/yangians_drinfeld_kohno.tex"
FINGERPRINT = ROOT / "chapters/theory/infinite_fingerprint_classification.tex"
MOTIVIC = ROOT / "chapters/theory/motivic_shadow_tower.tex"
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"


CURRENT_SURFACES = (
    HOCHSCHILD,
    NILPOTENT,
    THEOREM_B_SCOPE,
    E1_MODULAR,
    YANGIAN_DK,
    FINGERPRINT,
    MOTIVIC,
)


def _text(path: Path) -> str:
    return " ".join(path.read_text().split())


def test_hochschild_types_filtered_transport_and_associator_input():
    text = _text(HOCHSCHILD)
    required = [
        "Filtered Siegel--Borcherds deformation transport",
        r"\mathcal U_{\mathrm{Bor}\to\mathrm{ch},*}",
        "Its linear term sends the automorphic first-order direction",
        "its quadratic obstruction map lands in",
        r"\mathsf O_{\mathrm{Bor}\to\mathrm{ch}}",
        "An all-order compact Hall associator consists of a compact Hall source",
        "completed pentagon identity",
    ]
    for fragment in required:
        assert fragment in text


def test_companion_lanes_name_target_cocycle_and_order_scope():
    expectations = {
        NILPOTENT: [
            "Pentagon target cocycle at $\\hbar^3, \\hbar^4, \\hbar^5$",
            "candidate Siegel--Borcherds scalar cocycle",
            "An all-order associator on the compact Hall realisation additionally requires",
        ],
        THEOREM_B_SCOPE: [
            "candidate Siegel--Borcherds target cocycle",
            "order-\\(\\hbar^3\\) target-cocycle calculation",
            "all-order Hall associator additionally requires",
        ],
        E1_MODULAR: [
            "Siegel-modular $E_1$ target cocycle",
            "The package D1--D5 together with an all-order pentagon proof",
            "present proved content is the order-$\\hbar^{\\le3}$ target-cocycle calculation",
        ],
        YANGIAN_DK: [
            "Conditional Siegel--Borcherds target cocycle",
            "candidate target cocycle",
            "compact Hall realisation and all-order pentagon proof promote this display",
        ],
        FINGERPRINT: [
            "Pentagon target cocycle and umbral cohomology class",
            "candidate Siegel--Borcherds target cocycle",
        ],
        MOTIVIC: [
            "candidate K3 Siegel--Borcherds target cocycle",
            "order-$\\hbar^3$ target-cocycle statement",
            "all-order Hall-realised associator additionally requires",
        ],
    }
    for path, fragments in expectations.items():
        text = _text(path)
        for fragment in fragments:
            assert fragment in text, f"{fragment!r} missing from {path}"


def test_retired_sieg_borcherds_associator_language_absent_from_current_tree():
    forbidden = [
        "Siegel--Borcherds associator",
        "twisted Siegel--Borcherds associator",
        r"candidate \(E_1\) associator",
        "With D1--D5 it is the",
    ]
    search_roots = [
        ROOT / "chapters",
        ROOT / "standalone",
        ROOT / "appendices",
        ROOT / "notes",
        ROOT / "metadata",
    ]
    for root in search_roots:
        for path in root.rglob("*"):
            if path.suffix not in {".tex", ".md", ".jsonl"} or not path.is_file():
                continue
            text = _text(path)
            for fragment in forbidden:
                assert fragment not in text, f"{fragment!r} remains in {path}"


def test_harvest_matrix_records_sieg_borcherds_pass():
    text = _text(MATRIX)
    assert "J \\(H_{\\Delta}\\), K3, Hall, BKM, CY comparison" in text
    assert "Pass 516" in text
