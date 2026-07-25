"""Guards for the Theorem A reconstruction-versus-duality firewall."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
THEOREM_A = ROOT / "chapters/theory/theorem_A_infinity_2.tex"
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


def environment_block(path: Path, label: str, environment: str) -> str:
    text = visible(path)
    marker = rf"\label{{{label}}}"
    anchor = text.index(marker)
    begin = rf"\begin{{{environment}}}"
    end = rf"\end{{{environment}}}"
    start = text.rfind(begin, 0, anchor)
    assert start >= 0, (path, label, environment)
    stop = text.index(end, anchor) + len(end)
    return text[start:stop]


class TestTheoremAReconstructionDualityFirewallScope:
    def test_typed_reconstruction_verdier_comparison_is_proved_here(self):
        block = environment_block(
            THEOREM_A,
            "cor:no-dual-from-barcobar-counit",
            "corollary",
        )
        required = (
            "Typed comparison of reconstruction and Verdier duality",
            r"\label{cor:no-dual-from-barcobar-counit}",
            r"\ClaimStatusProvedHere",
            "pro-nilpotent chiral Ran ambient",
            r"$H_{\mathrm{fact}}\cup H_{\mathrm{VD}}$",
            r"\varepsilon_A\colon R_X(A)=\Omegach_X\Bbarch_X(A)\xrightarrow{\sim}A",
            r"K_X(A)=\mathbb D_{\Ran}\Bbarch_X(A)",
            r"\operatorname{Map}(A,K_X(A))",
            r"\operatorname{Map}(R_X(A),K_X(A))",
            r"\sigma_A\colon A\xrightarrow{\sim}K_X(A)",
        )
        for anchor in required:
            assert_anchor(block, anchor)

    def test_strict_dual_is_the_specified_formality_realization(self):
        block = environment_block(
            THEOREM_A,
            "cor:no-dual-from-barcobar-counit",
            "corollary",
        )
        required = (
            r"Under $H_{\mathrm{CL}}(A,A^{\mathrm i},\tau_{\mathrm i})$ and local finite duality",
            r"$K_X(A)$ identifies with the continuous realization of $A^!$",
            "A strict model is obtained from a specified formality equivalence",
            r"K_X(A)\simeq A^!",
        )
        for anchor in required:
            assert_anchor(block, anchor)

    def test_reconstruction_and_verdier_duality_have_typed_lanes(self):
        remark = environment_block(
            THEOREM_A,
            "rem:reconstruction-duality-separation",
            "remark",
        )
        theorem = environment_block(
            THEOREM_A,
            "thm:koszul-reflection",
            "theorem",
        )
        remark_anchors = (
            "Reconstruction and duality are separate operations",
            r"\label{rem:reconstruction-duality-separation}",
            "Two functors leave the bar object in different directions",
            r"\Omegach_X\Bbarch_X(A)\to A",
            r"K_X(A)=\mathbb D_{\Ran}\Bbarch_X(A)",
            "Their codomains and hypothesis packages determine their respective type signatures",
        )
        theorem_anchors = (
            r"\ClaimStatusConditional",
            r"\label{KR-i} \emph{Enhanced Ran equivalence; $\ClaimStatusProvedElsewhere$.",
            r"\label{KR-ii} \emph{Universal reconstruction; $\ClaimStatusProvedElsewhere$.",
            r"\label{KR-iii} \emph{Factorization closure; $\ClaimStatusConjectured$.",
            r"\label{KR-iv} \emph{Quadratic compression; $\ClaimStatusConditional$.",
            r"\label{KR-v} \emph{Verdier refinement; $\ClaimStatusConditional$.",
        )
        for anchor in remark_anchors:
            assert_anchor(remark, anchor)
        for anchor in theorem_anchors:
            assert_anchor(theorem, anchor)

    def test_review_harvest_records_typed_comparison_pass(self):
        matrix = MATRIX.read_text()
        ledger = LEDGER.read_text()
        for text in (matrix, ledger):
            normalized = re.sub(r"\s+", " ", text)
            assert "Pass 547" in text
            assert "reconstruction counit" in normalized
            assert "self-duality equivalence" in normalized
            assert "formality/minimal-model" in normalized
