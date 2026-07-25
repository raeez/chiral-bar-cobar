"""Scope guards for affine derived-center finite-window claims."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
CHIRAL_CENTER = ROOT / "chapters/theory/chiral_center_theorem.tex"
BAR_TABLES = ROOT / "chapters/examples/bar_complex_tables.tex"


def visible(path: Path) -> str:
    text = path.read_text()
    return "\n".join(
        line for line in text.splitlines()
        if not line.lstrip().startswith("%")
    )


def window_after(path: Path, label: str, chars: int) -> str:
    text = visible(path)
    start = text.find(label)
    assert start >= 0, f"missing label {label}"
    return text[start:start + chars]


def assert_anchor(window: str, anchor: str) -> None:
    normalized_window = re.sub(r"\s+", " ", window)
    normalized_anchor = re.sub(r"\s+", " ", anchor)
    assert anchor in window or normalized_anchor in normalized_window, anchor


class TestAffineDerivedCenterBarDegreeScope:
    def test_derived_center_checks_are_conditional_and_not_bar_degree_one_resolution(self):
        window = window_after(CHIRAL_CENTER, r"\label{prop:derived-center-explicit}", 6500)
        for anchor in (
            r"\ClaimStatusConditional",
            "finite-window derived-centre statement, not a statement that the\nbar-dual coalgebra has only bar degree~$1$",
            r"$(A^i)_1$ carries the adjoint $\mathfrak{sl}_2$",
            "higher\nbar-degree pieces are present",
            r"\(\dim(A^i)_2=5\) at weight~$3$",
            r"Computation~\ref{comp:sl2-ce-verification}",
            "no three-term diagonal resolution is being used here",
            "localized bar-concentration",
            "zero-mode inner\nquotient",
            "generic scalar centre of the Koszul-dual affine partner",
        ):
            assert_anchor(window, anchor)

    def test_false_bar_degree_one_concentration_phrase_does_not_return(self):
        text = visible(CHIRAL_CENTER)
        for forbidden in (
            "bar cohomology\n$H^*(B(\\widehat{\\mathfrak{sl}}_{2,k}))$ is concentrated in\nbar degree~$1$",
            "bar cohomology is concentrated in bar degree 1 (chiral Koszulness)",
            "three-term diagonal Koszul resolution",
            r"Ext^1_{V_k(\mathfrak{sl}_2)}(\C,\C)",
        ):
            assert forbidden not in text

    def test_sl2_ce_verification_label_is_live_and_records_h2_equals_5(self):
        window = window_after(BAR_TABLES, r"\label{comp:sl2-ce-verification}", 3500)
        for anchor in (
            r"\label{comp:sl2-ce-verification}",
            r"$H^1_{\mathrm{CE}} = 3$",
            r"$H^2_{\mathrm{CE}} = 5$",
            r"$\ker = 9 - 1 = 8$, $\mathrm{im} = 3$, $H^2_3 = 5$",
        ):
            assert_anchor(window, anchor)
