"""Guards for general twisting morphisms versus quadratic compression."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "chapters/theory/chiral_koszul_pairs.tex"


def visible(path: Path) -> str:
    return "\n".join(
        line
        for line in path.read_text().splitlines()
        if not line.lstrip().startswith("%")
    )


def environment_block(label: str, environment: str) -> str:
    text = visible(SOURCE)
    marker = rf"\label{{{label}}}"
    anchor = text.index(marker)
    begin = rf"\begin{{{environment}}}"
    end = rf"\end{{{environment}}}"
    start = text.rfind(begin, 0, anchor)
    assert start >= 0, (label, environment)
    stop = text.index(end, anchor) + len(end)
    return text[start:stop]


def theorem_and_proof(label: str) -> str:
    text = visible(SOURCE)
    theorem = environment_block(label, "theorem")
    theorem_start = text.index(theorem)
    proof_start = text.index(r"\begin{proof}", theorem_start + len(theorem))
    proof_end_marker = r"\end{proof}"
    proof_end = text.index(proof_end_marker, proof_start) + len(proof_end_marker)
    return text[theorem_start:proof_end]


def assert_anchor(block: str, anchor: str) -> None:
    normalized_block = re.sub(r"\s+", " ", block)
    normalized_anchor = re.sub(r"\s+", " ", anchor)
    assert anchor in block or normalized_anchor in normalized_block, anchor


def test_general_koszul_morphism_definition_precedes_quadratic_specialization():
    block = environment_block("def:chiral-koszul-morphism", "definition")
    required = (
        r"\ClaimStatusDefinitional",
        "general chiral twisting presentation",
        r"K_\tau^L(\cA,\cC)",
        r"K_\tau^R(\cC,\cA)",
        "are acyclic",
        r"\cite[Theorem~2.3.2]{LV12}",
        "Quadratic compression is an additional specialization",
        r"\cA^{\mathrm i}=C(s^{-1}V,s^{-2}R)",
        r"q_\cA\colon\cA^{\mathrm i}\longrightarrow\bar B_X(\cA)",
        r"\cite[Theorem~3.4.6]{LV12}",
    )
    for anchor in required:
        assert_anchor(block, anchor)
    assert "the associated graded" not in block


def test_fundamental_theorem_has_general_and_two_specialized_lanes():
    block = environment_block("thm:fundamental-twisting-morphisms", "theorem")
    required = (
        r"H_{\mathrm{CL}}(\cA,\cC,\tau)",
        r"p_\tau:=\varepsilon_\tau\colon\Omega_X(\cC)\to\cA",
        r"q_\tau:=\eta_\tau\colon\cC\to\bar B_X(\cA)",
        r"\cite[Theorem~2.3.2]{LV12}",
        r"\cC=\cA^{\mathrm i}",
        r"q_\cA\colon\cA^{\mathrm i}\longrightarrow\bar B_X(\cA)",
        r"\cite[Theorem~3.4.6]{LV12}",
        r"\cC=\bar B_X(\cA)",
        "the induced coalgebra map is the identity",
        r"\cite[Corollary~2.3.4]{LV12}",
    )
    for anchor in required:
        assert_anchor(block, anchor)


def test_theorem_a_decomposition_names_comparison_compression_reconstruction():
    block = environment_block("rem:theorem-A-decomposition", "remark")
    required = (
        "General twisting comparison",
        "Quadratic compression",
        "Universal reconstruction and Verdier duality",
        r"q_\tau\colon\cC\to\bar B_X(\cA)",
        r"q_\cA\colon\cA^{\mathrm i}\to\bar B_X(\cA)",
        r"\Omega_X\bar B_X(\cA)\to\cA",
        r"\cite[Theorem~2.3.2]{LV12}",
        r"\cite[Theorem~3.4.6]{LV12}",
        r"\cite[Corollary~2.3.4]{LV12}",
    )
    for anchor in required:
        assert_anchor(block, anchor)


def test_admissible_sl3_cartan_class_obstructs_quadratic_compression():
    block = theorem_and_proof("thm:admissible-sl3-non-koszul-qge3")
    required = (
        "Cartan cone for quadratic compression",
        r"\ClaimStatusConditional",
        r"with $q=3$",
        r"H_{\mathrm{CL}}(A,A^{\mathrm i},\tau_{\mathrm i})",
        r"q_A\colon A^{\mathrm i}\longrightarrow\bar B^{\mathrm{ch}}(A)",
        r"\operatorname{Cone}(q_A)",
        "quadratic Koszul defect",
        "exact rational matrix",
        r"\cite[Theorem~2.3.2 and Theorem~3.4.6]{LV12}",
        "universal full-bar counit",
        "independent reconstruction status",
        r"\cite[Corollary~2.3.4]{LV12}",
        r"For denominators~$q>3$",
        "explicit extension problem",
    )
    for anchor in required:
        assert_anchor(block, anchor)
    assert "Falsification of the bar--cobar counit" not in block
    assert "is \\emph{not} a chain quasi-isomorphism" not in block


def test_meta_theorem_condition_v_is_quadratic_comparison():
    block = environment_block("thm:koszul-equivalences-meta", "theorem")
    required = (
        r"\cA^{\mathrm i}=C(s^{-1}V,s^{-2}R)",
        r"\tau_{\mathrm i}\colon\cA^{\mathrm i}\longrightarrow\cA",
        r"H_{\mathrm{CL}}(\cA,\cA^{\mathrm i},\tau_{\mathrm i})",
        r"q_\cA\colon\cA^{\mathrm i}\longrightarrow\bar B_X(\cA)",
        r"p_\cA\colon\Omega_X(\cA^{\mathrm i})\longrightarrow\cA",
        "The quadratic comparison maps are equivalences",
        r"\cite[Theorem~3.4.6]{LV12}",
        "canonical full-bar twisting morphism",
        r"\mathrm{id}_{\bar B_X(\cA)}",
        r"\cite[Corollary~2.3.4]{LV12}",
        "measures the additional compression",
    )
    for anchor in required:
        assert_anchor(block, anchor)
    assert r"\Omega(\barBgeom(\cA)) \to \cA" not in block
