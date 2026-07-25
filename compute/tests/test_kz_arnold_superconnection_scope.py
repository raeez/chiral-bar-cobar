"""Guards for the typed KZ--Arnold bar-superconnection surface."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]

SURFACES = [
    ROOT / "chapters/frame/preface.tex",
    ROOT / "chapters/theory/introduction.tex",
    ROOT / "chapters/theory/bar_construction.tex",
    ROOT / "chapters/theory/climax_theorem.tex",
    ROOT / "chapters/theory/chiral_climax_platonic.tex",
    ROOT / "chapters/theory/e1_modular_koszul.tex",
    ROOT / "chapters/theory/theorem_B_scope_platonic.tex",
    ROOT / "chapters/theory/chiral_koszul_pairs.tex",
    ROOT / "chapters/theory/mc5_class_m_chain_level_platonic.tex",
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


class TestKZArnoldSuperconnectionScope:
    def test_front_surfaces_do_not_state_untyped_chain_connection_equality(self):
        combined = "\n".join(visible(path) for path in SURFACES)
        retired = (
            r"\chapter{The Climax Theorem: $d_{\mathrm{bar}} = \mathrm{KZ}^*(\nabla_{\mathrm{Arnold}})$}",
            r"\boxed{\;d_{\barB}\;=\;\mathrm{KZ}^{\ast}\!\bigl(\nabla_{\mathrm{Arnold}}\bigr).\;}",
            r"d_{\barB}\;=\;\mathrm{KZ}^{\ast}\!\bigl(\nabla_{\mathrm{Arnold}}\bigr)",
            r"\dbar \;=\; \KZ^{*}(\nabla_{\Arn}),",
            "bar differential = pulled-back KZ--Arnold connection",
            "bar differential is the pullback of one universal flat connection",
            "identifies the\nbar differential as $\\mathrm{KZ}^*(\\nabla^{\\mathrm{Arnold}})$",
            "The chiral bar differential $d_{\\mathrm{bar}} = \\mathrm{KZ}^{*}(\\nabla_{\\mathrm{Arnold}})$",
            r"$\dbar = \KZ^*(\nabla_{\Arn})$",
            "identifies the genus-$0$\naffine/tangent KZ-window chiral bar differential with the pullback",
            "The bar differential $d_{\\mathrm{bar}}$ of\n $\\mathrm{Bar}^{\\mathrm{ord}}(A)$ is the pullback of Arnold's\n universal KZ connection",
            r"$d_{\mathrm{bar}}^{(1)} = \mathrm{KZ}^*(\nabla_{\mathrm{KZB}})$",
            r"$d_{\mathrm{bar}}^{(g)} = \mathrm{KZ}^*(\nabla_{\mathrm{BD}}^{(g)})$",
        )
        for fragment in retired:
            assert fragment not in combined

    def test_each_surface_names_superconnection_and_residue_realization(self):
        required = {
            "chapters/frame/preface.tex": (
                "comparison map from the affine Arnold--Kohno screen to the",
                "nested residue complex",
                "signed residue maps along every collision divisor",
                "criterion for a chain model",
            ),
            "chapters/theory/introduction.tex": (
                "KZ--Arnold superconnection realizes the bar differential",
                "finite-window\nsuperconnection identity",
                "Fulton--MacPherson\nresidue-realization functor",
                "superconnection and the\nchain differential have distinct types",
            ),
            "chapters/theory/bar_construction.tex": (
                "Bar differential from the KZ--Arnold superconnection",
                r"\nabla^{B,0}_{\cA,V,n}",
                "residue-realized superconnection identity",
                "not a literal equality between a chain differential and a connection",
            ),
            "chapters/theory/climax_theorem.tex": (
                "The Climax Theorem: the KZ--Arnold bar superconnection",
                "genus-zero finite-window form",
                r"\ClaimStatusConditional",
                "Fulton--MacPherson boundary/residue realization",
                "old shorthand",
            ),
            "chapters/theory/chiral_climax_platonic.tex": (
                "two typed\nstatements",
                r"\nabla^{B,0}_{A,V,n}",
                "Fulton--MacPherson residue\nrealization",
                "FM-boundary residue realization",
            ),
            "chapters/theory/e1_modular_koszul.tex": (
                "genus-$0$ affine/tangent finite-window collision part",
                "Fulton--MacPherson residue realisation",
                "KZ--Arnold bar superconnection",
            ),
            "chapters/theory/theorem_B_scope_platonic.tex": (
                "On each genus-\\(0\\) affine/tangent finite KZ window",
                "Fulton--MacPherson boundary-residue realisation",
                "relates objects of distinct types through the Fulton--MacPherson\nresidue-realization functor",
                "finite-window flat-connection statement",
            ),
            "chapters/theory/chiral_koszul_pairs.tex": (
                "finite-window\nKZ--Arnold bar-superconnection identity",
                "Fulton--MacPherson residue realisation",
            ),
            "chapters/theory/mc5_class_m_chain_level_platonic.tex": (
                "genus-$0$\naffine/tangent KZ-window collision part",
                "Fulton--MacPherson residue realisation",
                "residue-realised\nsuperconnection",
            ),
        }
        for relative_path, anchors in required.items():
            text = visible(ROOT / relative_path)
            for anchor in anchors:
                assert_anchor(text, anchor)
