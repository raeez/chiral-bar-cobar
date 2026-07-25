"""Semantic guards for Theorem A/B typing in deformation quantization."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/examples/deformation_quantization.tex"


def visible() -> str:
    return "\n".join(
        line
        for line in TARGET.read_text().splitlines()
        if not line.lstrip().startswith("%")
    )


def between(text: str, start: str, end: str) -> str:
    start_pos = text.index(start)
    end_pos = text.index(end, start_pos)
    return text[start_pos:end_pos]


def environment(text: str, label: str, kind: str) -> str:
    label_pos = text.index(label)
    start = text.rfind(rf"\begin{{{kind}}}", 0, label_pos)
    end = text.index(rf"\end{{{kind}}}", label_pos)
    return text[start:end]


def test_quadratic_duality_section_separates_three_comparison_lanes():
    text = visible()
    block = between(
        text,
        r"\subsection{Relation to quadratic duality}",
        r"\subsection{Connection to Ayala--Francis}",
    )
    flat = " ".join(block.split())

    for token in (
        "augmentation-preserving descended Maurer--Cartan lift",
        r"Theorem~\ref{thm:mr-A}",
        r"Theorem~\ref{thm:mr-B}",
        r"Proposition~\ref{prop:mr-fixed-C-second-kind}",
        r"\mathsf{Pos}^{\mathrm{ch}}_{\mathrm{co-ctr}}(C)",
        r"\mathsf{Tw}^{\mathrm{ch}}_{\mathrm{acyc}}(C,A,\tau)",
        "Positselski fixed-coalgebra lane",
    ):
        assert token in flat, token

    for token in (
        r"H_1=H_{\mathrm{fact}}\cup H_{\mathrm{conv}}",
        r"\Omegach_X B_X(\mathcal A_\hbar) \xrightarrow{\;\sim\;}\mathcal A_\hbar",
        r"\mathcal A_\hbar^{\mathrm i}=C_X(s^{-1}V,s^{-2}R)",
        r"q_{\mathcal A_\hbar}\colon \mathcal A_\hbar^{\mathrm i}"
        r"\longrightarrow B_X(\mathcal A_\hbar)",
        r"H_{\mathrm{CL}}(\mathcal A_\hbar, \mathcal A_\hbar^{\mathrm i},\tau_{\mathrm i})",
    ):
        assert token in flat, token

    assert r"\mathcal A_{\mathrm{cl}}" not in block


def test_main_remark_assigns_reconstruction_recognition_and_second_kind():
    text = visible()
    block = environment(text, r"\label{rem:deformation-three-theorems}", "remark")
    flat = " ".join(block.split())

    for token in (
        r"\ClaimStatusConditional",
        r"Theorem~\ref{thm:mr-A}",
        r"Theorem~\ref{thm:mr-B}",
        r"Theorem~\ref{thm:higher-genus-inversion}",
        r"Theorem~\ref{thm:quantum-complementarity-main}",
        r"Proposition~\ref{prop:mr-fixed-C-second-kind}",
        "reconstruction counit of Theorem~A",
        r"\mathrm{MK1--MK3}",
        r"\mathrm C_1",
        "independent second-kind co--contra equivalence",
    ):
        assert token in flat, token

    for token in (
        r"\Omegach_X B_X(\mathcal A_\hbar) \xrightarrow{\;\sim\;}\mathcal A_\hbar",
        r"q_{\mathcal A_\hbar}\colon \mathcal A_\hbar^{\mathrm i}"
        r"\longrightarrow B_X(\mathcal A_\hbar)",
        r"H_1=H_{\mathrm{fact}}\cup H_{\mathrm{conv}}",
    ):
        assert token in flat, token

    for stale in (
        "Theorems~B and~C",
        "Theorem~B's completed bar-cobar inversion",
        r"Theorem~\ref{thm:bar-cobar-isomorphism-main}",
    ):
        assert stale not in block


def test_higher_genus_obligation_preserves_all_five_typed_clauses():
    text = visible()
    block = between(
        text,
        r"\section{Higher-genus formality obstruction}",
        r"\section{Synthesis}",
    )
    flat = " ".join(block.split())

    for token in (
        "compatibility package has five independent clauses",
        r"Theorem~\ref{thm:mr-A}",
        r"Theorem~\ref{thm:mr-B}",
        r"Theorem~\ref{thm:quantum-complementarity-main}",
        r"\mathsf{Pos}^{\mathrm{ch}}_{\mathrm{co-ctr}}(C)",
        r"\mathsf{Tw}^{\mathrm{ch}}_{\mathrm{acyc}}(C,A,\tau)",
        r"H_1=H_{\mathrm{fact}}\cup H_{\mathrm{conv}}",
        r"\mathrm C_1",
        "all five clauses above",
    ):
        assert token in flat, token

    assert r"q_A\colon A^{\mathrm i}\longrightarrow B_X(A)" in flat
    assert "completed bar-cobar inversion of Theorem~B" not in flat
