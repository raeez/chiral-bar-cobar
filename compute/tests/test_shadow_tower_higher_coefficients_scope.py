"""Scope guards for the reconstructed higher-residue chapter."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/theory/shadow_tower_higher_coefficients.tex"


def source() -> str:
    return TARGET.read_text()


def squashed() -> str:
    return re.sub(r"\s+", " ", source())


def window(start: str, end: str) -> str:
    text = source()
    left = text.index(start)
    right = text.index(end, left)
    return text[left:right]


EXTERNAL_LABELS = {
    "ch:shadow-tower-higher-coefficients",
    "chap:shadow-tower-higher-coefficients",
    "cor:virasoro-motivic-purity-r-leq-11",
    "def:shadow-transport-operator",
    "rem:three-filter-composite-scope",
    "rem:w3-wline-doubling-interpretation",
    "thm:kummer-laurent-depth-controlled",
    "thm:phi-n-humbert-heegner-admissibility",
    "thm:phi-n-weight-11-12-13",
    "thm:s-r-kummer-absent-through-r-11",
    "thm:s6-virasoro-closed-form",
    "thm:s7-virasoro-closed-form",
    "thm:s8-virasoro-closed-form",
    "thm:shadow-exponential-base-Virasoro",
    "thm:shadow-series-closed-form-Virasoro",
    "thm:shadow-tower-asymptotic-closed-form",
    "thm:shadow-tower-subleading-closed-form",
    "thm:shadow-tower-tier-4-closed-form",
    "thm:universal-class-M-C-is-6",
    "thm:virasoro-shadow-recurrence",
    "thm:w3-wline-closed-form",
    "thm:w3-wline-exponential-base",
}


class TestCertifiedLocalSurface:
    def test_chapter_is_concise_and_label_surface_is_unique(self):
        text = source()
        labels = re.findall(r"\\label\{([^}]+)\}", text)
        assert len(text.splitlines()) < 900
        assert len(labels) == 250
        assert len(labels) == len(set(labels))
        assert EXTERNAL_LABELS <= set(labels)

    def test_virasoro_ope_is_exact(self):
        text = squashed()
        assert r"\frac{c/2}{(z-w)^4}" in text
        assert r"\frac{2T(w)}{(z-w)^2}" in text
        assert r"\frac{\partial T(w)}{z-w}" in text

    def test_level_four_gram_matrix_and_lambda_norm_are_exact(self):
        text = squashed()
        for fragment in (
            r"5c & 3c",
            r"3c & \dfrac{c(c+8)}{2}",
            r"\det G_4(c)=\frac{c^2(5c+22)}{2}",
            r"N_\Lambda(c):=\langle\lambda,\lambda\rangle =\frac{c(5c+22)}{10}",
        ):
            assert fragment in text

    def test_proved_here_surface_ends_before_the_residue_package(self):
        exact = window(
            r"\section{Exact Virasoro local data}",
            r"\section{The ordered residue package}",
        )
        tail = source()[source().index(r"\section{The ordered residue package}") :]
        assert exact.count(r"\ClaimStatusProvedHere") == 4
        assert r"\ClaimStatusProvedHere" not in tail


class TestResidueConstructionFirewall:
    def test_scalar_definition_requires_the_named_package(self):
        block = window(
            r"\begin{definition}[Ordered residue contraction and scalar coefficient]",
            r"\begin{remark}[The construction obligation]",
        )
        for fragment in (
            r"\mathsf H_{\mathrm{res}}",
            r"\mathfrak g_{\mathrm{res}}^{\mathrm{ord}}",
            r"dh_r+h_rd=\mathrm{id}-\iota_r\pi_r",
            r"collision-compatible chain map",
            r"S_r(\cA;\mathsf H_{\mathrm{res}})",
        ):
            assert fragment in block

    def test_projected_recurrence_is_conditional_and_kernel_typed(self):
        block = window(
            r"\begin{theorem}[Projected Maurer--Cartan identity]",
            r"\begin{remark}[Recurrence and residue]",
        )
        assert r"\ClaimStatusConditional" in block
        assert r"\mathsf H_{\mathrm{quad}}" in block
        assert r"\lambda_r" in block
        assert r"K^r_{a,b}" in block
        assert r"a\star b=r" in block

    def test_higher_and_comparison_claims_are_open(self):
        text = source()
        for title in (
            "Construct and compute the Virasoro residue tower",
            "Asymptotic and arithmetic invariants of a constructed tower",
            r"Construct the \texorpdfstring{$\cW_3$}{W3} scalar lanes",
            "Construct the ordered-residue comparison map",
            "Construct the motivic and modular comparison morphisms",
        ):
            start = text.index(title)
            end = text.index(r"\end{problem}", start)
            assert r"\ClaimStatusOpen" in text[start:end]

    def test_retired_numeric_tower_is_absent(self):
        text = source()
        for fragment in (
            "4144720",
            "45c+193",
            "240c+1031",
            r"H_{\mathrm{Ricc}}",
            r"\sqrt{Q_L",
            r"C_\Vir = 6",
            "2560",
            r"\PadovanDim",
            r"D_{27,9}",
            "691",
            "3617",
            r"c_{\mathrm{K3}}",
        ):
            assert fragment not in text
