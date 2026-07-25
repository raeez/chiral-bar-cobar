"""Guards for the Arnold--Borcherds nilpotence proof surface."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]

SURFACES = [
    ROOT / "chapters/frame/preface.tex",
    ROOT / "chapters/frame/preface_section1_v2.tex",
    ROOT / "chapters/frame/preface_section1_draft.tex",
    ROOT / "chapters/theory/introduction.tex",
    ROOT / "chapters/theory/configuration_spaces.tex",
    ROOT / "chapters/theory/chiral_climax_platonic.tex",
    ROOT / "appendices/arnold_relations.tex",
    ROOT / "standalone/programme_summary.tex",
    ROOT / "standalone/programme_summary_section1.tex",
    ROOT / "standalone/five_theorems_modular_koszul.tex",
    ROOT / "standalone/survey_track_a_compressed.tex",
    ROOT / "standalone/survey_modular_koszul_duality.tex",
    ROOT / "standalone/survey_modular_koszul_duality_v2.tex",
    ROOT / "standalone/introduction_full_survey.tex",
]


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


class TestArnoldBorcherdsNilpotenceScope:
    def test_retired_arnold_only_and_degree_slogans_are_absent(self):
        combined = "\n".join(visible(path) for path in SURFACES)
        retired = (
            "same diagonal vanishes for degree reasons",
            "same diagonal is zero for degree reasons",
            "$(\\Res_{D_{ij}})^2 = 0$ by degree",
            "$\\operatorname{Res}_{D_{ij}}^2 = 0$ automatically",
            "The Arnold relation handles all of case~(ii). No algebraic input needed.",
            "Arnold property at disjoint pairs",
            "Arnold-only presentation",
            "additional Arnold-only relation",
            "On an affine genus-$0$ screen, the Arnold relations ensure $d^2 = 0$\nfor the bar differential.",
            "the Arnold relation is the codimension-two compatibility that forces the affine simple-pole component of $d^2$ to vanish on the bar differential",
        )
        for fragment in retired:
            assert fragment not in combined

    def test_surfaces_require_residue_exact_and_borcherds_inputs(self):
        required = {
            "chapters/frame/preface.tex": (
                "nested-set boundary-of-boundary identity cancels",
                "Arnold--Kohno relation",
                "Jacobi--Borcherds identity supplies the coefficient relation",
            ),
            "chapters/theory/introduction.tex": (
                "two independent inputs are present: the Arnold\nrelation cancels the logarithmic two-form coefficients",
                "Borcherds identity cancels the corresponding OPE-mode coefficients",
                "Borcherds identity reduces to\nthe corresponding vacuum-mode identities",
            ),
            "chapters/theory/configuration_spaces.tex": (
                "Higher-genus correction to the affine Arnold scalar presentation",
                "supplies the form half of the affine simple-pole\ncomponent",
                "Borcherds coefficient identity on OPE coefficients",
                "not the whole\noperator-valued bar-square proof",
                "scalar Orlik--Solomon residue differential",
            ),
            "chapters/theory/chiral_climax_platonic.tex": (
                "disjoint-pair infinitesimal\nbraid relation",
                "simple-pole projection of the Borcherds identity",
            ),
            "appendices/arnold_relations.tex": (
                "Arnold forms plus Borcherds coefficients",
                "scalar-form triple-index component",
                "also requires the Borcherds\ncoefficient identity",
            ),
            "standalone/five_theorems_modular_koszul.tex": (
                "first Poincar\\'e residue removes\nthe unique logarithmic normal factor",
            ),
            "standalone/survey_modular_koszul_duality_v2.tex": (
                "desuspension sign records the ordered-bar\norientation",
            ),
            "standalone/introduction_full_survey.tex": (
                "leaving no second normal direction for the same divisor",
            ),
        }
        for relative_path, anchors in required.items():
            text = visible(ROOT / relative_path)
            for anchor in anchors:
                assert_anchor(text, anchor)

    def test_active_nilpotence_surfaces_do_not_use_jacobi_shorthand(self):
        for relative_path in (
            "chapters/theory/configuration_spaces.tex",
            "appendices/arnold_relations.tex",
        ):
            text = visible(ROOT / relative_path)
            assert "Borcherds/Jacobi" not in text
