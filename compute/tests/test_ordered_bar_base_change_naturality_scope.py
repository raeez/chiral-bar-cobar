"""Guards for ordered-bar differential naturality under base change."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
BAR = ROOT / "chapters/theory/bar_construction.tex"
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"
LEDGER = ROOT / "notes/audit_repairs_ledger_20260610.md"


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


class TestOrderedBarBaseChangeNaturalityScope:
    def test_etale_pullback_commutes_with_all_bar_differential_pieces(self):
        text = visible(BAR)
        required = (
            "\\'{E}tale and holonomic base-change naturality of\nthe ordered bar differential",
            r"\label{cor:ordered-bar-differential-base-change}",
            r"\ClaimStatusProvedHere",
            "Let \\(u\\colon Y\\to X\\) be an \\'{e}tale map of smooth curves",
            r"\Phi_{u,n}\colon",
            r"u_n^*\mathbb B^{\ord}_{X,n}(\cA)",
            r"\mathbb B^{\ord}_{Y,n}(u^*\cA)",
            r"\Phi_{u,n}\,u_n^*d_\cA=d_{u^*\cA}\,\Phi_{u,n}",
            r"\Phi_{u,n}\,u_n^*d_{\mathrm{dR}}",
            r"\Phi_{u,n}\,u_n^*d_{\mathrm{res}}^X",
            r"=d_{\mathrm{res}}^Y\,\Phi_{u,n}",
            r"\Phi_{u,n}\,u_n^*d_B^X=d_B^Y\,\Phi_{u,n}",
        )
        for anchor in required:
            assert_anchor(text, anchor)

    def test_residue_pullback_identity_and_chiral_product_pullback_are_proved(self):
        text = visible(BAR)
        required = (
            r"u_n^{-1}(D^X_{ij})=D^Y_{ij}",
            r"u_n^*\Res_{D^X_{ij}}=\Res_{D^Y_{ij}}\,u_n^*",
            r"Proposition~\ref{prop:bar-residue-coordinate-independence}",
            r"\mu_{\cA}\colon j_*j^*(\cA\boxtimes\cA)\to\Delta_!\cA",
            r"\mu_{u^*\cA}",
            "OPE-mode projections\nand the residue operation commute with pullback",
        )
        for anchor in required:
            assert_anchor(text, anchor)

    def test_smooth_base_change_is_holonomic_and_proper_support_gated(self):
        text = visible(BAR)
        required = (
            "cartesian smooth base change of smooth proper curve families",
            "holonomic\n\\(\\cD\\)-complexes on \\(\\FM_n(\\mathcal X/S)\\)",
            "proper support\nover \\(S\\)",
            r"h^*\,R(\pi_n)_+",
            r"R(\pi'_n)_+",
            "Hotta--Takeuchi--Tanisaki~\\cite[\\S1.7]{HTT08}",
            "Without the holonomic\nfinite-window and proper-support hypotheses",
            "only\nthe aritywise pullback identity before relative de~Rham pushforward",
        )
        for anchor in required:
            assert_anchor(text, anchor)

    def test_review_harvest_records_base_change_pass(self):
        matrix = MATRIX.read_text()
        ledger = LEDGER.read_text()
        for text in (matrix, ledger):
            normalized = re.sub(r"\s+", " ", text)
            assert "Pass 546" in text
            assert "base-change naturality" in normalized
            assert "ordered-bar" in normalized or "ordered bar" in normalized
