"""Guardrails for higher-genus curved versus square-zero surfaces."""

from __future__ import annotations

from pathlib import Path

from compute.lib.independent_verification import independent_verification


ROOT = Path(__file__).resolve().parents[2]
FOUNDATIONS = ROOT / "chapters/theory/higher_genus_foundations.tex"
MODULAR_KOSZUL = ROOT / "chapters/theory/higher_genus_modular_koszul.tex"


def _window(text: str, needle: str, radius: int = 1400) -> str:
    idx = text.index(needle)
    return text[max(0, idx - radius) : idx + radius]


@independent_verification(
    claim="higher-genus curved fiber complexes are compared in the coderived CDG category",
    derived_from=[
        "fiberwise d_fib^2 = kappa omega_g is curved",
        "period-corrected D_g is the square-zero comparison model",
    ],
    verified_against=[
        "localized source window around chain-level structure not recoverable from cohomology",
        "proof window for the gauge change between Arakelov representatives",
    ],
    disjoint_rationale=(
        "The theorem surface may still use ordinary quasi-isomorphism after "
        "passing to square-zero A-infinity models, but not for the genuinely "
        "curved fiber CDG complexes themselves."
    ),
)
def test_fiberwise_curved_representatives_use_coderived_language():
    tex = FOUNDATIONS.read_text()
    statement = _window(tex, "Chain-level structure not recoverable from cohomology")
    proof = _window(tex, "Two chain representatives")

    assert "coderived-equivalent" in statement
    assert "ordinary quasi-isomorphism is\n not the invariant" in statement
    assert "filtered curved gauge\nequivalence" in proof
    assert "cone is coacyclic" in proof
    assert "period-corrected square-zero model" in proof
    assert "produce quasi-isomorphic but\n not isomorphic curved bar complexes" not in statement
    assert "provides a quasi-isomorphism\nbut not an isomorphism of curved coalgebras" not in proof


@independent_verification(
    claim="strict Mittag-Leffler completion is required for higher-genus coderived recovery",
    derived_from=[
        "CP1--CP3 completed chiral Positselski theorem",
        "positive-energy finite windows alone do not identify the completed category",
    ],
    verified_against=[
        "genus extension hierarchy statement",
        "level-(ii) proof paragraph",
    ],
    disjoint_rationale=(
        "The finite-dimensional window hypothesis and the inverse-limit "
        "homotopy theory fail independently; both must be visible in the "
        "higher-genus hierarchy."
    ),
)
def test_higher_genus_hierarchy_requires_strict_ml_completion():
    tex = FOUNDATIONS.read_text()
    hierarchy = _window(tex, "\\label{thm:genus-extension-hierarchy}", 3600)
    proof = _window(tex, "Level~(ii):", 1800)

    assert "finite-window\n bar tower is a strict Mittag--Leffler" in hierarchy
    assert "Mittag--Leffler control supplies the derived inverse-limit recovery" in hierarchy
    assert "strict finite-window tower hypothesis" in tex
    assert "Every positive-energy chiral algebra satisfies\n\\textup{(i)}--\\textup{(ii)}" not in hierarchy
    assert "The strict Mittag--Leffler hypothesis" in proof
    assert "$R\\!\\varprojlim$ recovery" in proof


@independent_verification(
    claim="higher-genus modular Koszul separates total square-zero from fiberwise curvature",
    derived_from=[
        "total D_A^2=0 on the modular bar construction",
        "fiberwise d_fib^2=kappa omega_g on a fixed curve",
    ],
    verified_against=[
        "opening deficiency paragraph",
        "ambient square-zero theorem status comment",
    ],
    disjoint_rationale=(
        "The opening paragraph and theorem label comment are independent "
        "places where conflating the total and fiberwise differentials would "
        "reintroduce the old genus >= 1 error."
    ),
)
def test_higher_genus_modular_koszul_keeps_total_and_fiberwise_apart():
    tex = MODULAR_KOSZUL.read_text()
    opening = _window(tex, "At genus~$g \\geq 1$, this fact fails fiberwise.", 1800)
    square_zero = _window(tex, "\\label{thm:differential-square-zero}", 400)

    assert "d_{\\mathrm{fib}}^2 = \\kappa(\\cA) \\cdot \\omega_g" in opening
    assert "total} bar differential" in opening
    assert "$D_\\cA^2 = 0$" in opening
    assert "claim is ProvedHere" not in square_zero
    assert "ambient status is conditional on the relative log-FM package" in square_zero
