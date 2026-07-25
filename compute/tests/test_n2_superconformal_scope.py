"""Semantic guards for the reconstructed N=2 superconformal chapter."""

from pathlib import Path
import re

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/examples/n2_superconformal.tex"
LANDSCAPE = ROOT / "chapters/examples/landscape_census.tex"
CONCORDANCE = ROOT / "chapters/connections/concordance.tex"


def source() -> str:
    return TARGET.read_text()


def block(label: str, environment: str) -> str:
    text = source()
    label_position = text.index(rf"\label{{{label}}}")
    start = text.rindex(rf"\begin{{{environment}}}", 0, label_position)
    end = text.index(rf"\end{{{environment}}}", label_position)
    return text[start:end]


def assert_anchor(text: str, anchor: str) -> None:
    assert re.sub(r"\s+", " ", anchor) in re.sub(r"\s+", " ", text)


def test_ope_packet_has_the_standard_parities_and_coefficients() -> None:
    text = source()
    for required in (
        r"T\quad(h=2,\ \bar0)",
        r"J\quad(h=1,\ \bar0)",
        r"G^\pm\quad(h=\tfrac32,\ \bar1)",
        r"\frac{c/3}{(z-w)^2}",
        r"\frac{2c/3}{(z-w)^3}",
        r"\frac{2J(w)}{(z-w)^2}",
        r"\frac{2T(w)+\partial J(w)}{z-w}",
    ):
        assert required in text


def test_kazama_suzuki_scope_and_parameter_arithmetic() -> None:
    text = source()
    coset = block("rem:n2-kazama-suzuki", "remark")
    assert r"k\in\mathbb Z_{\ge0}" in coset
    assert r"L_k(\mathfrak{sl}_2)\otimes F" in coset
    assert r"c_{\mathcal N=2}(k)=\frac{3k}{k+2}" in coset
    assert r"H_{\mathrm{KS}}" in coset

    k = sp.symbols("k")
    c = 3 * k / (k + 2)
    reflected = c.subs(k, -k - 4)
    assert sp.cancel(c + reflected) == 6
    assert sp.cancel(2 * c / (3 - c) - k) == 0
    assert "k=-2" in text and "c=3" in text


def test_modular_formula_is_a_conditional_implication() -> None:
    proposition = block("prop:n2-kappa", "proposition")
    assert r"\ClaimStatusConditional" in proposition
    assert r"H_{\mathrm{KS}}" in proposition
    assert r"H_{\mathcal N=2}^{\mathrm{mod}}" in proposition
    assert r"\frac{3(k+2)}4" in proposition
    assert r"\frac{k}{2}+1" in proposition
    assert r"\frac{k+4}{4}" in proposition
    assert r"\frac{6-c}{2(3-c)}" in proposition

    chapter_opening = source().split(r"\section{OPE data", 1)[0]
    assert r"\left(\frac{3k}{k+2},\,\text{open},\,\text{open}\right)" in chapter_opening


def test_reflection_and_object_level_duality_are_separate() -> None:
    proposition = block("prop:n2-complementarity", "proposition")
    assert r"\ClaimStatusConditional" in proposition
    assert r"H_{\mathcal N=2}^{\mathrm{KD}}" in proposition
    assert r"\mathbb D_{\operatorname{Ran}}B" in proposition
    assert r"V_{c(-k-4)}^{\mathcal N=2}" in proposition
    assert r"=1" in proposition
    text = source()
    assert "identity of rational functions" in text
    assert "requires a Verdier--bar comparison" in text


def test_pbw_page_stops_before_bar_collapse() -> None:
    proposition = block("prop:n2-koszulness", "proposition")
    assert r"\ClaimStatusConditional" in proposition
    assert_anchor(proposition, "Li-associated graded")
    assert_anchor(proposition, "first page of the bar spectral sequence")
    assert r"H_{\mathcal N=2}^{\mathrm{bar}}" in proposition
    assert r"q_{\mathcal N=2}" in proposition


def test_spectral_flow_and_shadow_are_typed() -> None:
    text = source()
    for required in (
        r"\sigma^\ell(L_n)&=L_n+\ell J_n+\frac{c}{6}\ell^2\delta_{n,0}",
        r"\sigma^\ell(J_n)&=J_n+\frac{c}{3}\ell\delta_{n,0}",
        r"\sigma^\ell(G_r^\pm)&=G_{r\pm\ell}^\pm",
        "full multi-generator Maurer--Cartan tensor",
        "full shadow tower is",
        "open computation",
    ):
        assert_anchor(text, required)


def test_stale_scalar_promotions_are_absent() -> None:
    text = source()
    for stale in (
        "98/3",
        r"K(\mathrm{BP}) = 196",
        r"\varrho_{\mathcal{N}=2} = 1",
        "13, \\; 41/4, \\; 1, \\; {-}8",
        "Feigin--Frenkel involution",
        "PBW collapse at~$E_2$",
    ):
        assert stale not in text


def test_census_and_concordance_propagate_the_open_modular_lane() -> None:
    landscape = LANDSCAPE.read_text()
    n2_row_start = landscape.index(r"\(\mathcal N=2\) SCA")
    n2_row_end = landscape.index(r"Lattice \(V_\Lambda", n2_row_start)
    n2_row = landscape[n2_row_start:n2_row_end]
    for required in (
        r"H_{\mathcal N=2}^{\mathrm{mod}}",
        r"H_{\mathcal N=2}^{\mathrm{bar}}",
        "modular/bar comparisons conditional",
    ):
        assert required in n2_row

    ph_start = landscape.index(r"\item PH$^{\mathrm{N2}}$")
    ph_end = landscape.index(r"\item CJ$^{\mathrm{log}}$", ph_start)
    ph = landscape[ph_start:ph_end]
    for required in (
        r"c(k)+c(-k-4)=6",
        r"H_{\mathcal N=2}^{\mathrm{mod}}",
        r"H_{\mathcal N=2}^{\mathrm{KD}}",
        "open comparison ledger",
    ):
        assert required in ph
    assert r"\varrho_{\mathcal{N}=2} = 1" not in ph

    concordance = CONCORDANCE.read_text()
    ledger_start = concordance.index(r"\textbf{Superconformal comparison ledger}")
    ledger_end = concordance.index(r"\textbf{Moonshine module", ledger_start)
    ledger = concordance[ledger_start:ledger_end]
    for required in (
        r"c=3k/(k+2)",
        r"c(k)+c(-k-4)=6",
        r"H_{\mathcal N=2}^{\mathrm{mod}}+H_{\mathcal N=2}^{\mathrm{KD}}",
        r"H_{\mathcal N=2}^{\mathrm{bar}}",
        "Li filtration computes the PBW page",
    ):
        assert required in ledger
    assert r"$1$ & $c = 3$" not in ledger


def test_chapter_uses_positive_declarative_prose() -> None:
    prohibited = re.compile(
        r"\b(?:not|does\s+not|do\s+not|cannot|without|never|no|fails?|failure|"
        r"undefined|outside|excluded?)\b",
        flags=re.IGNORECASE,
    )
    assert prohibited.search(source()) is None


def test_environments_balance() -> None:
    text = source()
    for environment in (
        "table",
        "tabular",
        "equation",
        "align",
        "proposition",
        "proof",
        "definition",
        "remark",
        "conjecture",
        "enumerate",
    ):
        assert text.count(rf"\begin{{{environment}}}") == text.count(
            rf"\end{{{environment}}}"
        )
