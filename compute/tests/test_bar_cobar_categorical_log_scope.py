"""Semantic guards for the repaired categorical-logarithm appendix."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TEX = ROOT / "chapters/theory/bar_cobar_adjunction_inversion.tex"


def _environment(text: str, label: str, kind: str) -> str:
    pos = text.index(label)
    start = text.rfind(rf"\begin{{{kind}}}", 0, pos)
    end = text.index(rf"\end{{{kind}}}", pos)
    return " ".join(text[start:end].split())


def _forward(text: str, label: str, size: int = 3600) -> str:
    pos = text.index(label)
    return " ".join(text[pos : pos + size].split())


def test_pbw_detection_uses_the_quadratic_comparison():
    text = TEX.read_text()
    block = _environment(text, r"\label{prop:log-convergence}", "proposition")
    assert "PBW detection of the quadratic comparison" in block
    assert r"H_{\mathrm{CL}}(A,A^{\mathrm i},\tau_{\mathrm i})" in block
    assert r"q_A\colon A^{\mathrm i}\to B_X(A)" in block
    assert r"\Omega_X(A^{\mathrm i})\to A" in block
    assert "left and right twisted tensor products" in block
    assert "universal counit" not in block


def test_character_growth_claim_is_replaced_by_exact_counterexample():
    text = TEX.read_text()
    block = _environment(
        text, r"\label{prop:subexponential-growth-automatic}", "proposition"
    )
    assert "Tensor-bar counterexample" in block
    assert r"A=k\oplus V" in block
    assert r"\dim_k B(A)_p=d^p" in block
    assert "finite support" in block

    proof_start = text.index(r"\label{prop:subexponential-growth-automatic}")
    proof_end = text.index(r"\end{proof}", proof_start)
    proof = text[proof_start:proof_end]
    assert r"B(A)=T^c(s^{-1}V)" in proof
    assert r"1<c<d" in proof


def test_k3_lane_separates_reconstruction_recognition_and_normalization():
    text = TEX.read_text()
    k3 = _forward(text, r"\label{rem:bcinv-inversion-K3}")
    assert "universal reconstruction map of Theorem~A" in k3
    assert r"q_{A_{\mathrm{K3}}}" in k3
    assert r"K_X(A_{\mathrm{K3}})=\mathbb D_{\Ran}B_X(A_{\mathrm{K3}})" in k3

    branch = _forward(text, r"\label{rem:bcai-deep-1}")
    assert r"\ClaimStatusConditional" in branch
    assert r"\operatorname{Cone}(q_{A_{\mathrm{Hall}}})" in branch
    assert "formal branch" in branch

    normalization = _forward(text, r"\label{rem:bcai-deep-3}", 1800)
    assert "distinct normalizations" in normalization
    assert "conditional choice of branch" in normalization


def test_summary_assigns_theorems_a_and_b_to_distinct_maps():
    text = TEX.read_text()
    summary = _forward(text, r"\label{subsec:monograph-as-log}", 3500)
    assert "Theorem~A: universal reconstruction" in summary
    assert "Theorem~B: quadratic recognition" in summary
    assert r"q_A\colon A^{\mathrm i}\to B_X(A)" in summary

