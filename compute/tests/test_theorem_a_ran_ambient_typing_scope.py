"""Structural guards for Theorem A's ambient and transition packages."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
THEOREM_A = ROOT / "chapters/theory/theorem_A_infinity_2.tex"
MASTER = ROOT / "chapters/connections/master_reconstruction.tex"
INVERSION = ROOT / "chapters/theory/bar_cobar_adjunction_inversion.tex"
THEOREM_B = ROOT / "chapters/theory/theorem_B_scope_platonic.tex"


def flat(path: Path) -> str:
    return " ".join(path.read_text().split())


def environment(path: Path, label: str, kind: str) -> str:
    source = path.read_text()
    anchor = source.index(rf"\label{{{label}}}")
    begin = rf"\begin{{{kind}}}"
    end = rf"\end{{{kind}}}"
    start = source.rfind(begin, 0, anchor)
    assert start >= 0
    stop = source.index(end, anchor) + len(end)
    return " ".join(source[start:stop].split())


def test_active_tex_uses_the_ran_category_as_ambient_data() -> None:
    active = tuple((ROOT / "chapters").rglob("*.tex")) + tuple(
        (ROOT / "standalone").rglob("*.tex")
    )
    token = r"H_{\mathrm{Ran}}"
    occurrences = [str(path.relative_to(ROOT)) for path in active if token in path.read_text()]
    assert occurrences == []


def test_theorem_a_separates_ambient_from_transition_packages() -> None:
    source = flat(THEOREM_A)
    for anchor in (
        "Ran ambient and four Theorem~A packages",
        r"\mathcal C_X=\bigl(D(\Ran X),\otimes^{\ch}\bigr)",
        "These are the published ambient data",
        r"\tau_{\mathrm i}\colon A^{\mathrm i}\longrightarrow A",
        r"$H_{\mathrm{fact}}$",
        r"$H_{\mathrm{conv}}$",
        r"$H_{\mathrm{CL}}(A,A^{\mathrm i},\tau_{\mathrm i})$",
        r"$H_{\mathrm{VD}}$",
        r"$H_{\mathrm{prop}}$",
    ):
        assert anchor in source
    assert r"\kappa_A" not in source

    theorem = environment(THEOREM_A, "thm:koszul-reflection", "theorem")
    for anchor in (
        "pro-nilpotent Francis--Gaitsgory ambient",
        r"$H_{\mathrm{fact}}$",
        r"$H_{\mathrm{conv}}$",
        r"$H_{\mathrm{CL}}(A,A^{\mathrm i},\tau_{\mathrm i})$",
        r"$H_{\mathrm{VD}}$",
        r"\label{KR-i}",
        r"\label{KR-v}",
    ):
        assert anchor in theorem


def test_completed_chain_realizations_use_h_conv() -> None:
    master = environment(MASTER, "thm:mr-A", "theorem")
    inversion = environment(INVERSION, "thm:bar-cobar-platonic", "theorem")
    coalgebra_unit = environment(
        THEOREM_B,
        "thm:thm-B-coalgebra-side-unit-qi",
        "theorem",
    )

    assert r"H_1=H_{\mathrm{fact}}\cup H_{\mathrm{conv}}" in master
    assert r"\(H_{\mathrm{conv}}\)" in inversion
    assert r"\(H_{\mathrm{conv}}\)" in coalgebra_unit
