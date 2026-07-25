"""Guards for strict shadow-channel and cross-channel correction scope."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "chapters/theory/higher_genus_modular_koszul.tex"
ENGINE = ROOT / "compute/lib/shadow_channel_decomposition.py"


def visible_text(path: Path) -> str:
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


class TestShadowChannelCrossChannelScope:
    def test_shadow_channel_theorem_requires_strict_decoupling(self):
        text = visible_text(SOURCE)
        theorem_window = normalized(
            window_after_label(text, "thm:shadow-channel-decomposition", 120)
        )

        required = (
            "Type signature:",
            "H_{\\mathrm{SCD}}",
            "strict orthogonal idempotent channel splitting",
            "mixed transferred higher brackets",
            "no mixed stable-graph weights",
            "\\Theta_{\\cA}^{\\mathrm{mix}}",
            "not a theorem for an arbitrary multi-channel algebra",
            "\\delta F_g^{\\mathrm{cross}}(\\cA)",
        )
        for fragment in required:
            assert fragment in theorem_window

        forbidden = (
            "independent MC element",
            "solving its own MC equation",
            "all degrees and all genera",
            "all cross-terms",
            "since $\\ChirHoch^3 = 0$ for abelian vertex algebras",
            "\\cA^{\\mathrm{sh}} \\cong",
        )
        for fragment in forbidden:
            assert fragment not in theorem_window

    def test_shadow_cauchy_schwarz_is_only_diagonal_diagnostic(self):
        text = visible_text(SOURCE)
        corollary_window = normalized(
            window_after_label(text, "cor:shadow-cauchy-schwarz", 85)
        )

        required = (
            "Type signature:",
            "H_{\\mathrm{SCD}}",
            "scalar diagnostic",
            "at most one",
            "not the full genus-$2$ complementarity statement",
            "\\delta F_2^{\\mathrm{cross}}(\\cA)",
        )
        for fragment in required:
            assert fragment in corollary_window

        forbidden = (
            "all $\\kappa_i$ proportional",
            "by channel independence",
        )
        for fragment in forbidden:
            assert fragment not in corollary_window

    def test_compute_engine_no_longer_treats_abelian_as_sufficient(self):
        engine = normalized(visible_text(ENGINE))

        required = (
            "Abelian primary OPEs alone are not sufficient",
            "strict_channel_decoupled",
            "not killed by abelian primary brackets alone",
            "add δF_g^cross off H_SCD",
        )
        for fragment in required:
            assert fragment in engine

        forbidden = (
            "Abelian OPE → all Gerstenhaber brackets vanish",
            "MC equation decouples. Each channel evolves independently",
            "channels independent",
        )
        for fragment in forbidden:
            assert fragment not in engine
