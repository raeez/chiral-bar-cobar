"""Guards for determinant-line anomaly and conformal-block comparison scope."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "chapters/theory/higher_genus_modular_koszul.tex"
ORDERED_STANDALONE = ROOT / "standalone" / "ordered_chiral_homology.tex"
E1_STANDALONE = ROOT / "standalone" / "e1_primacy_ordered_bar.tex"
EN_STANDALONE = ROOT / "standalone" / "en_chiral_operadic_circle.tex"
PREFACE = ROOT / "chapters" / "frame" / "preface.tex"
SURVEY_V2 = ROOT / "standalone" / "survey_modular_koszul_duality_v2.tex"
VERLINDE_ENGINE = ROOT / "compute" / "lib" / "verlinde_ordered_engine.py"


def visible_text(path: Path = SOURCE) -> str:
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


class TestDeterminantAnomalyConformalBlockScope:
    def test_determinant_line_is_not_declared_flat_with_nonzero_c1(self):
        text = visible_text()
        theorem_window = normalized(
            window_after_label(text, "thm:conformal-block-reconstruction", 110)
        )
        forbidden = (
            "is a flat connection on $L_\\cA$",
            "flat connection on $L_\\cA$",
        )
        for fragment in forbidden:
            assert fragment not in theorem_window

        required = (
            "Chern--Weil curvature class",
            "kappa(\\cA)\\lambda",
            "anomaly line connection",
            "not an ordinary flat line connection",
            "projectivised or anomaly-cancelled transport",
            "determinant-line anomaly matching",
        )
        for fragment in required:
            assert fragment in theorem_window

    def test_verlinde_recovery_is_ordered_tuy_comparison_not_raw_homology(self):
        windows = {
            "canonical": normalized(
                window_after_label(
                    visible_text(SOURCE), "prop:verlinde-from-ordered", 175
                )
            ),
            "ordered_standalone": normalized(
                window_after_label(
                    visible_text(ORDERED_STANDALONE),
                    "prop:verlinde-from-ordered",
                    175,
                )
            ),
            "e1_standalone": normalized(
                window_after_label(
                    visible_text(E1_STANDALONE), "prop:verlinde-standalone", 125
                )
            ),
            "en_standalone": normalized(
                window_after_label(
                    visible_text(EN_STANDALONE), "prop:e-verlinde", 95
                )
            ),
        }

        for name, window in windows.items():
            for fragment in (
                "\\ClaimStatusConditional",
                "Type signature:",
                "TUY/Hitchin finite-rank",
                "ordered-chain-to-TUY comparison",
                "determinant-anomaly",
            ):
                assert fragment in window, name

        assert "Through the ordered-chain-to-TUY comparison" in windows["canonical"]
        assert "Through the ordered-chain-to-TUY comparison" in windows[
            "ordered_standalone"
        ]
        assert "TUY non-separating factorization" in windows["canonical"]
        assert "TUY non-separating factorization" in windows["ordered_standalone"]
        assert "TUY non-separating factorisation" in windows["e1_standalone"]
        assert "TUY identities" in windows["en_standalone"]

        summary_text = normalized(visible_text(PREFACE) + "\n" + visible_text(SURVEY_V2))
        for fragment in (
            "ordered/TUY comparison lane recovers the Verlinde formula",
            "TUY/Hitchin conformal-block sheaf",
            "determinant-anomaly matching",
            "ordered chiral chain complex entering through the comparison morphism",
        ):
            assert fragment in summary_text

        engine_text = normalized(VERLINDE_ENGINE.read_text())
        for fragment in (
            "ordered-chain-to-TUY comparison package is supplied",
            "not by itself identified with H^0",
            "RECOVERY THROUGH ORDERED/TUY COMPARISON",
            "identified with conformal blocks only through the "
            "ordered-chain-to-TUY comparison morphism",
        ):
            assert fragment in engine_text

        searched_text = "\n".join(
            [
                visible_text(SOURCE),
                visible_text(ORDERED_STANDALONE),
                visible_text(E1_STANDALONE),
                visible_text(EN_STANDALONE),
                visible_text(PREFACE),
                visible_text(SURVEY_V2),
                VERLINDE_ENGINE.read_text(),
            ]
        )
        for fragment in (
            "symmetric coinvariants recover the space of conformal",
            "From the ordered chiral homology",
            "ordered chiral homology recovers the Verlinde",
            "ordered chiral homology at level~$k$",
            "dimension of ordered chiral homology",
            "computes H^0 = conformal blocks",
        ):
            assert fragment not in searched_text

    def test_formal_disk_ope_only_determines_bar_side_expansion(self):
        text = visible_text()
        theorem_window = normalized(
            window_after_label(text, "thm:deformation-quantization-ope", 115)
        )
        assert (
            "Conformal blocks on all Riemann surfaces are determined by "
            "the OPE on the formal disk"
        ) not in theorem_window

        required = (
            "bar-side perturbative log-FM genus expansion",
            "completed modular convolution algebra",
            "does not by itself determine analytic conformal blocks",
            "comparison theorem",
            "TUY/Hitchin finite-rank sheaf",
            "determinant-anomaly matching package",
        )
        for fragment in required:
            assert fragment in theorem_window
