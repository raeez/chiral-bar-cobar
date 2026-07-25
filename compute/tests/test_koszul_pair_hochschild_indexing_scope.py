"""Scope guard for the normalized chiral Hochschild indexing repair."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
KOSZUL_PAIR = ROOT / "chapters/theory/koszul_pair_structure.tex"


def visible(path: Path) -> str:
    return "\n".join(
        line for line in path.read_text(encoding="utf-8").splitlines()
        if not line.lstrip().startswith("%")
    )


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def theorem_block(text: str, label: str) -> str:
    label_pos = text.index(label)
    start = text.rindex(r"\begin{theorem}", 0, label_pos)
    return text[start:text.index(r"\end{proof}", label_pos)]


def test_normalized_chiral_hochschild_complex_has_degree_zero_term():
    source = visible(KOSZUL_PAIR)
    block = theorem_block(source, r"\label{thm:chiral-hochschild-complex}")
    flat = normalized(block)

    for required in (
        r"0 \to M \xrightarrow{\delta_0}",
        r"\operatorname{Hom}_{\mathcal{D}_X}(\overline{\mathcal A},M)",
        r"(\delta_0m)(a)=Y_L(a,m)-(-1)^{|a||m|}Y_R(m,a)",
        r"(\delta_n f)(a_1,\ldots,a_{n+1})",
        r"\sum_{i=1}^{n}(-1)^i",
        r"H^1$ is derivations modulo the inner derivations coming from $\delta_0(M)$",
        "In degree zero the map is precisely the chiral adjoint action",
    ):
        assert normalized(required) in flat, required

    for retired in (
        r"C^0 = \operatorname{Hom}_{\mathcal D_X}(\overline{\mathcal A},M)",
        r"(\delta_n f)(a_0,\ldots,a_{n+1})",
        r"\sum_{i=0}^{n}(-1)^i",
        "H^1$ is derivations before quotienting inner derivations",
    ):
        assert normalized(retired) not in flat, retired


def test_geometric_chiral_hochschild_uses_two_extra_marked_points():
    source = visible(KOSZUL_PAIR)
    block = theorem_block(source, r"\label{thm:geometric-chiral-hochschild}")
    statement = block[:block.index(r"\end{theorem}")]
    flat_statement = normalized(statement)
    flat_block = normalized(block)

    for required in (
        r"\Gamma\left(\overline{C}_{n+2}(X),",
        r"(\overline{\mathcal A}^{\boxtimes n},\mathcal A)",
        "the two additional marked points record the output and the evaluation point",
        r"computes $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$",
        r"it does not produce $\cA^!$",
        "No finite-type dual of the bar coalgebra is used in this extension",
    ):
        assert normalized(required) in flat_block, required

    assert r"\overline{C}_{n+1}(X)" not in statement
    assert r"\overline{C}_{n+3}(X)" not in flat_statement
