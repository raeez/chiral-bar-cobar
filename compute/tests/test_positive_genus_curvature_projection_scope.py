"""Guardrails for positive-genus curvature projection language."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]

SURFACES = [
    ROOT / "chapters/theory/higher_genus_foundations.tex",
    ROOT / "chapters/theory/bar_cobar_adjunction_curved.tex",
    ROOT / "chapters/frame/preface.tex",
    ROOT / "chapters/theory/introduction.tex",
    ROOT / "chapters/frame/guide_to_main_results.tex",
    ROOT / "chapters/connections/thqg_open_closed_realization.tex",
    ROOT / "appendices/homotopy_transfer.tex",
    ROOT / "chapters/connections/concordance.tex",
    ROOT / "standalone/survey_modular_koszul_duality_v2.tex",
    ROOT / "standalone/programme_summary.tex",
    ROOT / "standalone/programme_summary_section1.tex",
    ROOT / "standalone/survey_track_a_compressed.tex",
    ROOT / "standalone/five_theorems_modular_koszul.tex",
]


def visible(path: Path) -> str:
    lines = []
    for line in path.read_text().splitlines():
        if line.lstrip().startswith("%"):
            continue
        if 'uses the abbreviation "``$\\dfib^{\\,2}=\\kappa\\cdot\\omega_g$' in line:
            continue
        lines.append(line)
    return "\n".join(lines)


def assert_anchor(text: str, anchor: str) -> None:
    normalized_text = re.sub(r"\s+", " ", text)
    normalized_anchor = re.sub(r"\s+", " ", anchor)
    assert anchor in text or normalized_anchor in normalized_text, anchor


def test_raw_scalar_fiber_square_is_not_the_positive_genus_claim_surface():
    combined = "\n".join(visible(path) for path in SURFACES)
    retired = (
        "d_{\\mathrm{fib}}^2 = \\kappa(\\cA) \\cdot \\omega_g",
        "d_{\\mathrm{fib}}^2=\\kappa(\\cA)\\cdot\\omega_g",
        "d_{\\mathrm{fib}}^{2}\\;=\\;\\kappa(\\cA)\\cdot\\omega_g",
        "d_{\\mathrm{fib}}^{\\,2}\\;=\\;\\kappa(\\cA)\\cdot\\omega_g",
        "\\dfib^{\\,2} = \\kappa(\\cA) \\cdot \\omega_g",
        "\\dfib^{\\,2}=\\kappa(\\cA)\\cdot\\omega_g",
        "\\dfib^{\\,2} = k \\cdot \\omega_1",
        "\\dfib^{\\,2}=k\\,\\omega_1",
        "$d^2 = \\kappa \\cdot \\omega_g$",
        "The curvature $d_{\\mathrm{fib}}^2 = \\kappa",
        "the curvature $d_{\\mathrm{fib}}^2=\\kappa",
    )
    for fragment in retired:
        assert fragment not in combined


def test_positive_genus_surfaces_name_chain_scalar_and_total_layers():
    anchors = {
        "chapters/theory/higher_genus_foundations.tex": (
            "m_1^{(g)\\,2}(a)",
            "m_2(m_0^{(g)},a)-m_2(a,m_0^{(g)})",
            "\\operatorname{tr}_{\\mathrm{diag}}\\!\\bigl(m_0^{(g)}\\bigr)",
                "The total corrected differential $\\Dg{g}$ satisfies",
        ),
        "chapters/theory/bar_cobar_adjunction_curved.tex": (
            "The raw fiberwise curved identity is",
            "m_1^{(g)\\,2}(a)=[m_0^{(g)},a]_{m_2}",
            "scalar diagonal projection of $m_0^{(g)}",
        ),
        "chapters/theory/introduction.tex": (
            "the raw chain identity is\n$m_1^2=[m_0^{(g)},-]$",
            "\\operatorname{tr}_{\\mathrm{diag}}(m_0^{(g)})",
            "The period-corrected total bar differential satisfies $D_g^2=0$",
        ),
        "chapters/frame/guide_to_main_results.tex": (
            "The fixed-fibre curved identity is",
            "\\operatorname{tr}_{\\mathrm{diag}}\\!\\bigl(m_0^{(g)}\\bigr)",
            "the raw chain identity is $m_1^2=[m_0,-]$",
            "For $g\\geq2$,\nTheorem~D begins with\n"
            "$\\operatorname{Obs}^{\\mathrm{def}}_g(\\cA)"
            "\\in H^2(\\Def_g(\\cA))$",
        ),
        "appendices/homotopy_transfer.tex": (
            "curved $A_\\infty$/CDG package with $m_1^2=[m_0^{(g)},-]$",
            "scalar diagonal/Hodge projection is\n$\\kappa(\\cA)\\lambda_1$",
        ),
        "standalone/five_theorems_modular_koszul.tex": (
            "the raw identity is $m_1^2=[m_0^{(g)},-]$",
            "after scalar diagonal projection of the matrix-valued ordered\ncurvature residue",
        ),
    }
    for relative_path, required in anchors.items():
        text = visible(ROOT / relative_path)
        for anchor in required:
            assert_anchor(text, anchor)
