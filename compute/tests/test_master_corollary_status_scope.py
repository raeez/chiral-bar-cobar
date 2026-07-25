"""Status guards for the Master Reconstruction corollary layer."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
MASTER_RECONSTRUCTION = ROOT / "chapters/connections/master_reconstruction.tex"
INTRODUCTION = ROOT / "chapters/theory/introduction.tex"
FRONTIER = ROOT / "FRONTIER.md"


def visible(path: Path) -> str:
    text = path.read_text()
    return "\n".join(
        line for line in text.splitlines()
        if not line.lstrip().startswith("%")
    )


def window_around(path: Path, label: str, before: int, after: int) -> str:
    text = visible(path)
    start = text.find(label)
    assert start >= 0, f"missing label {label}"
    return text[max(0, start - before):start + after]


def environment_block(path: Path, label: str, environment: str) -> str:
    text = visible(path)
    label_pos = text.find(label)
    assert label_pos >= 0, f"missing label {label}"
    start = text.rfind(rf"\begin{{{environment}}}", 0, label_pos)
    assert start >= 0, f"missing {environment} before {label}"
    end_marker = rf"\end{{{environment}}}"
    end = text.find(end_marker, label_pos)
    assert end >= 0, f"missing {end_marker} after {label}"
    return text[start:end + len(end_marker)]


def assert_anchor(window: str, anchor: str) -> None:
    normalized_window = re.sub(r"\s+", " ", window)
    normalized_anchor = re.sub(r"\s+", " ", anchor)
    assert anchor in window or normalized_anchor in normalized_window, anchor


class TestMasterCorollaryStatusScope:
    def test_corollary_layer_preserves_individual_statuses_and_packages(self):
        section = window_around(
            MASTER_RECONSTRUCTION,
            r"\label{sec:mr-corollaries}",
            500,
            9000,
        )
        for anchor in (
            "Each retains its own claim status, mathematical\ncarrier, and hypothesis package",
            r"\label{cor:mr-A}",
            r"\ClaimStatusConditional",
            r"\label{cor:mr-B}",
            "Theorem~B is the quadratic comparison",
            r"\label{rem:mr-fixed-C-placement}",
            r"\label{cor:mr-C}",
            r"\ClaimStatusConjectured",
            r"\mathsf G,\mathsf L,\mathsf C,\mathsf M,\mathsf B",
            r"\kappa_{\mathrm{cat}},\kappa_{\ch}^{\mathrm{Hodge}}",
            r"(0,0,3,5,24)",
            r"\label{cor:mr-D}",
            r"H_D=(H_D^1,H_D^K,H_D^{\mathrm{tr}}, H_D^{\mathrm{graph}})",
            r"\operatorname{Obs}^{\mathrm{def}}_g(A_b)",
            r"\operatorname{Obs}^{\mathrm{def}}_{1,1}(A_b)",
            r"\mathfrak O^K_g(A_b)=\kappa(A_b)\lambda_{-1}(\mathbb E_g)",
            r"F_g(A_b)=\kappa(A_b)\lambda_g^{\mathrm{FP}}",
            r"\label{cor:mr-H}",
            r"hypothesis package $H_H(A_b;S)$",
            r"dh+hd=\mathrm{id}-\iota p",
            r"\{0,1\}",
            r"\{0,2,3\}",
        ):
            assert_anchor(section, anchor)

    def test_a_b_and_fixed_c_have_distinct_carriers(self):
        theorem_a = environment_block(
            MASTER_RECONSTRUCTION, r"\label{thm:mr-A}", "theorem"
        )
        theorem_b = environment_block(
            MASTER_RECONSTRUCTION, r"\label{thm:mr-B}", "theorem"
        )
        fixed_c = environment_block(
            MASTER_RECONSTRUCTION,
            r"\label{prop:mr-fixed-C-second-kind}",
            "proposition",
        )
        corollary_a = environment_block(
            MASTER_RECONSTRUCTION, r"\label{cor:mr-A}", "corollary"
        )
        corollary_b = environment_block(
            MASTER_RECONSTRUCTION, r"\label{cor:mr-B}", "corollary"
        )
        placement = environment_block(
            MASTER_RECONSTRUCTION,
            r"\label{rem:mr-fixed-C-placement}",
            "remark",
        )

        for required in (
            r"\Omegach_X\Bbarch_X(A)\xrightarrow{\ \sim\ }A",
            r"C\xrightarrow{\ \sim\ }\Bbarch_X\Omegach_X(C)",
            "pro-nilpotent Francis--Gaitsgory Ran ambient",
            r"H_1=H_{\mathrm{fact}}\cup H_{\mathrm{conv}}",
        ):
            assert_anchor(theorem_a, required)
        assert "q_A" not in theorem_a
        assert r"H_{\mathrm{quad}}" not in theorem_a

        for required in (
            r"q_A\colon A^i\longrightarrow B_X(A)",
            r"\Omega_X(A^i)\to A",
            "left and right twisted tensor products",
            r"H_{\mathrm{CL}}(A,A^i,\tau_i)",
        ):
            assert_anchor(theorem_b, required)

        for required in (
            r"\mathsf{Pos}^{\mathrm{ch}}_{\mathrm{co-ctr}}(C)",
            r"D^{\mathrm{co}}(C\text{-}\mathrm{CoFact})",
            r"D^{\mathrm{ctr}}(C\text{-}\mathrm{ContraFact})",
            r"\mathsf{Tw}^{\mathrm{ch}}_{\mathrm{acyc}}(C,A,\tau)",
        ):
            assert_anchor(fixed_c, required)

        for required in (
            r"\epsilon_{A_b}\colon\Omegach_XB_X(A_b)\xrightarrow{\sim}A_b",
            r"\eta_C\colon C\xrightarrow{\sim}B_X\Omegach_X(C)",
        ):
            assert_anchor(corollary_a, required)
        assert "q_{A_b}" not in corollary_a

        for required in (
            r"q_{A_b}\colon A_b^i\longrightarrow B_X(A_b)",
            r"\Omega_X(A_b^i)\to A_b",
            "quadratic twisted tensor products",
        ):
            assert_anchor(corollary_b, required)
        assert "Positselski" not in corollary_b

        assert_anchor(placement, r"Proposition~\ref{prop:mr-fixed-C-second-kind}")
        assert_anchor(placement, "independent\nsecond-kind equivalence")

        source = visible(MASTER_RECONSTRUCTION)
        for stale in (
            "Theorem~B as ambient-qualified bar--cobar inversion",
            "The coalgebra-side statement of Theorem~B is the unit",
        ):
            assert stale not in source

    def test_corollary_h_is_conditional_not_provedhere(self):
        block = environment_block(
            MASTER_RECONSTRUCTION, r"\label{cor:mr-H}", "corollary"
        )
        assert r"\ClaimStatusConditional" in block
        assert r"\ClaimStatusProvedHere" not in block
        for anchor in (
            r"hypothesis package $H_H(A_b;S)$",
            r"K_{A_b,S}",
            r"dh+hd=\mathrm{id}-\iota p",
            r"\{0,1\}",
            r"\{0,2,3\}",
        ):
            assert_anchor(block, anchor)

    def test_corollary_d_has_correct_hodge_degree_and_lane_scope(self):
        block = environment_block(
            MASTER_RECONSTRUCTION, r"\label{cor:mr-D}", "corollary"
        )
        assert r"\ClaimStatusConditional" in block
        assert r"\ClaimStatusProvedHere" not in block
        for anchor in (
            r"$4\text{--}5$ on $\Mbar_{g,n}$",
            r"H_D=(H_D^1,H_D^K,H_D^{\mathrm{tr}}, H_D^{\mathrm{graph}})",
            r"For $g\geq2$",
            r"\operatorname{Obs}^{\mathrm{def}}_g(A_b)",
            r"\operatorname{Obs}^{\mathrm{def}}_{1,1}(A_b)",
            r"\mathfrak O^K_g(A_b)=\kappa(A_b)\lambda_{-1}(\mathbb E_g)",
            r"(-1)^g\kappa(A_b)\lambda_g",
            r"\delta F_g^{\mathrm{cross}}(A_b)",
        ):
            assert_anchor(block, anchor)

    def test_summary_surfaces_keep_hypothesis_packages_visible(self):
        for path in (INTRODUCTION, FRONTIER):
            text = visible(path)
            for anchor in (
                "Theorems",
                "corollaries restratified by Beilinson-tower\nlevel, each scoped by its named hypothesis package",
                "computed in the finite-type curved\nVerdier--Koszul ambient",
                "chart-side bar--cobar lane is\nself-dual",
                "higher projections retain their own hypotheses",
            ):
                assert_anchor(text, anchor)
            assert "every\nforgetful step degenerates from adjunction to strict equivalence" not in text
            assert "Theorems A--H as corollaries restratified by level" not in text

    def test_false_status_and_degree_phrases_do_not_return(self):
        source = "\n".join(
            visible(path)
            for path in (MASTER_RECONSTRUCTION, INTRODUCTION, FRONTIER)
        )
        for forbidden in (
            r"\begin{corollary}[Theorem~H as $F_2$-concentration;"
            "\n\\ClaimStatusProvedHere]",
            r"with $\lambda_g\in H^2(\Mbar_{g,n})$",
            "Theorems A through H as corollaries restratified by Beilinson-tower\nlevel; KSDual",
            "Theorems A--H as corollaries restratified by level",
            "every forgetful step degenerates from adjunction to strict equivalence",
        ):
            assert forbidden not in source
