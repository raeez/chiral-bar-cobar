"""Guards for the Virasoro c=13 scalar/object self-duality firewall."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "chapters/theory/higher_genus_modular_koszul.tex"
CONCORDANCE = ROOT / "chapters/connections/concordance.tex"
THEOREM_INDEX = ROOT / "standalone/theorem_index.tex"


def visible_text() -> str:
    return visible(SOURCE)


def visible(path: Path) -> str:
    return "\n".join(
        line
        for line in path.read_text().splitlines()
        if not line.lstrip().startswith("%")
    )


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def window_after_label(text: str, label: str, lines: int) -> str:
    anchor = rf"\label{{{label}}}"
    assert anchor in text, label
    return "\n".join(text.split(anchor, 1)[1].splitlines()[:lines])


class TestC13SelfDualityScope:
    def test_c13_proposition_has_scalar_shadow_type_signature_and_firewall(self):
        text = visible_text()
        window = normalized(window_after_label(text, "prop:c13-full-self-duality", 95))

        required = (
            "Type signature:",
            "\\iota_{\\mathrm{Vir}}(c)=26-c",
            "No isomorphism of ordered bar complexes",
            "additional Virasoro Koszul-equivalence package",
            "Bar-complex firewall",
            "does not by itself construct an isomorphism",
            "weaker than an all-degree bar-complex self-equivalence",
        )
        for fragment in required:
            assert fragment in window

        forbidden = (
            "Feigin--Frenkel Koszul",
            "Feigin--Frenkel isomorphism",
            "is isomorphic to its Koszul dual",
            "the modular Koszul package is self-dual at every level",
            "Full tower self-duality",
        )
        for fragment in forbidden:
            assert fragment not in window

    def test_c13_holographic_remark_keeps_rtf_checked_not_all_degree(self):
        text = visible_text()
        window = normalized(
            window_after_label(text, "rem:c13-holographic-significance", 105)
        )

        required = (
            "unique scalar self-dual point",
            "not, without an additional Virasoro Koszul-equivalence package",
            "through the checked degree range",
            "Conjecture~\\ref{conj:c13-full-rtf-vanishing}",
            "not an all-degree bar-complex self-equivalence theorem",
            "critical-level reflection",
            "scalar fixed point",
        )
        for fragment in required:
            assert fragment in window

        forbidden = (
            "boundary theory and its dual are identical",
            "vanishes for all test functions. This is strictly stronger",
            "hence vanish identically at $c = 13$",
            "Feigin--Frenkel involution",
        )
        for fragment in forbidden:
            assert fragment not in window

    def test_c13_drinfeld_scope_marks_all_degree_rtf_as_conjectural(self):
        text = visible_text()
        window = normalized(window_after_label(text, "rem:c13-drinfeld-double-scope", 55))

        required = (
            "possible all-degree self-duality",
            "separate Virasoro Koszul-equivalence package",
            "rather than as a formal consequence of the scalar equality",
            "all-degree extension",
            "\\emph{conjecture}",
            "open beyond the checked degree range",
        )
        for fragment in required:
            assert fragment in window

    def test_concordance_and_index_use_scoped_c13_language(self):
        concordance = normalized(visible(CONCORDANCE))
        local = concordance.split("\\index{Virasoro algebra!self-duality at $c=13$!concordance}", 1)[1]
        local = local.split("\\IfFileExists{chapters/connections/thqg_concordance_supplement.tex}", 1)[0]

        required = (
            "unique scalar fixed point",
            "does not, by itself, construct an isomorphism",
            "Rational-shadow and checked trace self-duality",
            "through the checked degree range",
            "all-degree vanishing for every test function is Conjecture",
            "matching scalar and rational-shadow components",
            "stronger Drinfeld-double/Koszul-equivalence target",
        )
        for fragment in required:
            assert fragment in local

        forbidden = (
            "boundary theory and its Koszul dual coincide",
            "Full tower self-duality",
            "vanishes for all test functions",
            "vanish identically",
            "self-dual in all six components simultaneously",
        )
        for fragment in forbidden:
            assert fragment not in local

        theorem_index = visible(THEOREM_INDEX)
        assert "Scalar and rational shadow fixed point at \\$c = 13\\$" in theorem_index
        assert "Full tower self-duality at \\$c = 13\\$" not in theorem_index
