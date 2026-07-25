"""Guards for local/global scope of the collision logarithmic form."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]

SURFACES = [
    ROOT / "chapters/frame/preface.tex",
    ROOT / "chapters/theory/introduction.tex",
    ROOT / "chapters/theory/configuration_spaces.tex",
    ROOT / "chapters/theory/bar_construction.tex",
    ROOT / "chapters/theory/cobar_construction.tex",
    ROOT / "chapters/theory/quantum_corrections.tex",
    ROOT / "chapters/theory/climax_theorem.tex",
    ROOT / "chapters/theory/chiral_climax_platonic.tex",
    ROOT / "chapters/frame/guide_to_main_results.tex",
    ROOT / "chapters/frame/preface_section1_v2.tex",
    ROOT / "chapters/frame/preface_section1_draft.tex",
    ROOT / "appendices/notation_index.tex",
    ROOT / "appendices/signs_and_shifts.tex",
    ROOT / "standalone/survey_track_a_compressed.tex",
    ROOT / "standalone/survey_modular_koszul_duality.tex",
    ROOT / "standalone/survey_modular_koszul_duality_v2.tex",
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


class TestCollisionFormLocalGlobalScope:
    def test_no_globalized_dlog_coordinate_slogans_on_front_surfaces(self):
        combined = "\n".join(visible(path) for path in SURFACES)
        retired = (
            "configuration spaces and the logarithmic propagator\n$\\eta_{ij}=d\\log(z_i-z_j)$",
            "where $d_{\\mathrm{res}}$ is built from the logarithmic propagator\n$\\eta_{ij}=d\\log(z_i-z_j)$",
            "whose kernel is the logarithmic\npropagator $d\\log(z_i - z_j)$",
            "$\\eta_{12} = d\\log(z_1-z_2)$ is globally defined\non~$\\mathbb P^1$",
            "propagator $\\eta_{ij}=d\\log(z_i-z_j)$ does not extend as a smooth\nform",
            "The logarithmic 1-forms $\\eta_{ij}=d\\log(z_i-z_j)$ are the scalar\ncoefficients",
            "The forms $\\eta_{ij} = d\\log(z_i - z_j)$ that served as propagators",
            "kernel $\\eta_{ij} = d\\log(z_i - z_j)$ on the Fulton--MacPherson",
            "The logarithmic form~$\\eta_{ij} = d\\log(z_i - z_j)$ is not an\nincidental choice",
            "The logarithmic form $\\eta_{ij}=d\\log(z_i-z_j)$ is the integral\nkernel",
            "The categorical logarithm $\\eta_{ij}=d\\log(z_i-z_j)$",
            "logarithmic propagator $d\\log(z_i-z_j)$",
            "governed by the Arnold relation for\n$\\eta_{ij}=d\\log(z_i-z_j)$ on $\\FM_n(X)$",
            "$\\eta_{ij}=d\\log(z_i-z_j)$ on $\\mathrm{Conf}_n(X)$",
            "Standard forms $\\eta_{ij} = d\\log(z_i - z_j)$",
        )
        for fragment in retired:
            assert fragment not in combined

    def test_surfaces_name_local_representative_and_global_replacement_data(self):
        required = {
            "chapters/frame/preface.tex": (
                "affine coordinate chart",
                "formal tangent screen",
                "local\ncoordinate representative",
                "transition cocycle",
                "KZB/theta propagator",
                "prime-form representative",
            ),
            "chapters/theory/introduction.tex": (
                "logarithmic normal form along each\ndiagonal",
                "affine/formal nilpotence check",
                "prime-form/KZB representatives",
                "Virasoro/projective-connection datum",
            ),
            "chapters/theory/configuration_spaces.tex": (
                "affine or\nformal-screen representative of the logarithmic normal form",
                "coordinate-change\ncocycle",
                "FM-residue realization",
                "affine/formal representatives",
                "projective linear relations",
            ),
            "chapters/theory/bar_construction.tex": (
                "logarithmic\nnormal form",
                "represented on an affine/formal genus-zero",
                "screen by \\(d\\log(z_i-z_j)\\)",
                "coordinate-change cocycle",
                "local affine/formal representative",
            ),
            "chapters/theory/cobar_construction.tex": (
                "logarithmic normal form \\(\\eta_{ij}\\) along the collision diagonal",
                "\\(d\\log(z_i-z_j)\\) is its affine/formal representative",
                "projective and positive-genus screens use the projective-linear and\nperiod/KZB replacement data",
            ),
            "chapters/theory/quantum_corrections.tex": (
                "represented by\n\\(d\\log(z_i-z_j)\\) only on affine/formal collision screens",
                "logarithmic normal forms along collision diagonals",
            ),
            "chapters/theory/climax_theorem.tex": (
                r"affine/formal genus-zero screen",
                "not a global function on an\narbitrary curve",
                "coordinate-change cocycle",
            ),
            "chapters/theory/chiral_climax_platonic.tex": (
                "Arnold-local affine/formal representative",
                "coordinate-change cocycle",
                "KZB/theta or prime-form representative",
            ),
            "chapters/frame/guide_to_main_results.tex": (
                "logarithmic normal form\n\\(\\eta_{ij}\\) along a collision diagonal",
                "\\(d\\log(z_i-z_j)\\) only on affine/formal genus-zero screens",
            ),
            "chapters/frame/preface_section1_v2.tex": (
                "logarithmic normal form \\(\\eta_{ij}\\) along the collision diagonal",
                "\\(d\\log(z_i-z_j)\\) is its affine/formal\ngenus-zero representative",
            ),
            "chapters/frame/preface_section1_draft.tex": (
                "logarithmic normal form \\(\\eta_{ij}\\) along the collision diagonal",
                "not a global coordinate difference on an\narbitrary curve",
            ),
            "appendices/notation_index.tex": (
                "FM logarithmic normal form along $D_{ij}$",
                "affine/formal collision screen",
                "coordinate-change cocycle",
                "KZB/prime-form replacement data",
            ),
            "appendices/signs_and_shifts.tex": (
                "local normal coordinate on an affine/formal\ncollision screen",
                "local representative of the logarithmic normal form",
                "coordinate-change or KZB/prime-form\ndata",
            ),
            "standalone/survey_track_a_compressed.tex": (
                "represented by\n\\(d\\log(z_i-z_j)\\) only on affine/formal genus-zero screens",
                "projective\nand positive-genus screens use the corresponding replacement data",
            ),
            "standalone/survey_modular_koszul_duality.tex": (
                "logarithmic normal form \\(\\eta_{ij}\\) along the collision diagonal",
                "not a global coordinate difference on an\narbitrary curve",
            ),
            "standalone/survey_modular_koszul_duality_v2.tex": (
                "represented by\n\\(d\\log(z_i-z_j)\\) only on affine/formal genus-zero screens",
                "projective-linear and period/KZB replacement data",
            ),
        }
        for relative_path, anchors in required.items():
            text = visible(ROOT / relative_path)
            for anchor in anchors:
                assert_anchor(text, anchor)

    def test_bar_construction_proves_coordinate_independence_of_residue_part(self):
        text = visible(ROOT / "chapters/theory/bar_construction.tex")
        required = (
            "Coordinate independence of the collision-residue\nbar differential",
            "\\label{prop:bar-residue-coordinate-independence}",
            "hypothesis\npackage: local affine/formal collision screen",
            "Then \\(v=u\\,g\\), where \\(g\\) is invertible along \\(D_{ij}\\)",
            "d\\log v=d\\log u+d\\log g",
            "The second summand is regular along \\(D_{ij}\\)",
            "\\operatorname{Res}_{D_{ij}}\\!\\bigl(\\alpha\\wedge d\\log(w_i-w_j)\\bigr)",
            "collision-residue summand \\(d_{\\mathrm{res}}\\)",
            "independent of the local affine/formal coordinate",
            "without that stress-tensor\ndatum no Virasoro cocycle is asserted",
        )
        for anchor in required:
            assert_anchor(text, anchor)
