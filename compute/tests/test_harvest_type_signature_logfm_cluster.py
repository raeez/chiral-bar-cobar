"""Regression guards for harvested type signatures in the log-FM cluster."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "chapters/theory/higher_genus_modular_koszul.tex"

THEOREM_LABELS = [
    "thm:perturbative-exactness",
    "thm:universal-modular-deformation",
    "thm:modular-propagator-existence",
    "thm:logfm-modular-cocomposition",
    "thm:logfm-obstruction-criterion",
    "thm:empty-boundary-logfm-obstructions-vanish",
    "thm:finite-rank-spectral-reduction",
    "thm:primitive-to-global-reconstruction",
]


def visible_text() -> str:
    return "\n".join(
        line
        for line in SOURCE.read_text().splitlines()
        if not line.lstrip().startswith("%")
    )


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def window_after_label(text: str, label: str, lines: int = 14) -> str:
    anchor = rf"\label{{{label}}}"
    assert anchor in text, label
    suffix = text.split(anchor, 1)[1]
    return "\n".join(suffix.splitlines()[:lines])


class TestHarvestTypeSignatureLogFMCluster:
    def test_conditional_logfm_cluster_theorems_have_type_signatures(self):
        text = visible_text()
        for label in THEOREM_LABELS:
            window = window_after_label(text, label)
            assert "Type signature:" in window, label
            assert "hypothesis package:" in window, label

    def test_logfm_cocomposition_names_global_signed_package(self):
        text = visible_text()
        window = normalized(window_after_label(text, "thm:logfm-modular-cocomposition", lines=22))
        required = (
            "logarithmic FM chain-coefficient/homotopy modular cooperad presentation",
            "Mok logarithmic FM geometry",
            "local Gysin residue signs",
            "finite groupoid/Reynolds normalisation",
            "global signed log-FM residue-pushforward package",
            "LF1--LF6",
        )
        for fragment in required:
            assert fragment in window

    def test_logfm_global_coherence_obstruction_complex_is_explicit(self):
        text = normalized(visible_text())
        required = (
            "Global log-FM coherence obstruction complex",
            "def:global-logfm-coherence-obstruction-complex",
            "mathfrak E_{\\log\\mathrm{FM}}^\\bullet(\\mathcal W)",
            "Boardman--Vogt resolution of the stable-graph category restricted to the same window",
            "mathfrak o_q^{\\log\\mathrm{FM}}(\\mathcal W)",
            "First log-FM coherence obstructions",
            "codimension-two target-identification defect",
            "pentagon defect for four iterated contractions",
            "Obstruction criterion for the signed log-FM package",
            "exist if and only if the obstruction classes",
            "strict Mittag--Leffler tower",
            "Theorem~\\ref{thm:logfm-obstruction-criterion}",
        )
        for fragment in required:
            assert fragment in text

    def test_empty_boundary_fm_core_has_positive_obstruction_vanishing(self):
        text = normalized(visible_text())
        required = (
            "Empty-boundary FM obstruction vanishing",
            "thm:empty-boundary-logfm-obstructions-vanish",
            "hypothesis package: $D=\\emptyset$, fixed smooth curve",
            "d_{\\mathrm{sew}}=d_{\\mathrm{pf}}=\\hbar\\Delta=0",
            "mathcal W_{\\mathrm{sm}}",
            "ordinary Fulton--MacPherson tree-cooperad obstruction complex",
            "C_\\bullet(W\\mathsf{Tree}_{\\mathcal W_{\\mathrm{sm}}})",
            "ordinary FM collision cocomposition",
            "[\\mathfrak o_q^{\\log\\mathrm{FM}}(\\mathcal W_{\\mathrm{sm}})] =0",
            "obstruction-free classical FM core",
            "does not assert vanishing for stable-node",
        )
        for fragment in required:
            assert fragment in text
