"""Semantic guards for the repaired W-algebra chapter."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/examples/w_algebras.tex"


def source() -> str:
    return TARGET.read_text()


def squashed() -> str:
    return re.sub(r"\s+", " ", source())


def between(start: str, end: str) -> str:
    text = source()
    left = text.index(start)
    right = text.index(end, left)
    return text[left:right]


def test_principal_central_charge_and_conductor_are_exact():
    text = squashed()
    assert (
        r"c_N(k) =(N-1)-\frac{N(N^2-1)(k+N-1)^2}{k+N}"
        in text
    )
    assert r"k^\vee=-k-2N" in text
    assert r"K_N^c:=c_N(k)+c_N(k^\vee)=4N^3-2N-2" in text
    assert r"\sum_{s=2}^N2(6s^2-6s+1)=4N^3-2N-2" in text


def test_principal_modular_formula_is_hypothesis_typed():
    block = between(
        r"\begin{theorem}[Principal modular trace formula;",
        r"\begin{corollary}[Principal $W(\mathfrak g)$ trace formula;",
    )
    assert r"\ClaimStatusConditional" in block
    assert r"H_{\mathrm{diag}}^{g=1}" in block
    assert r"c_N(k)(H_N-1)\lambda_1" in block


def test_bp_standard_shifted_and_modular_lanes_are_separate():
    text = source()
    flat = squashed()
    assert (
        r"c_{\mathrm{BP}}(k) =-\frac{(2k+3)(3k+1)}{k+3}"
        in flat
    )
    assert (
        r"c_{\mathrm{BP}}(k)+c_{\mathrm{BP}}(-k-6)=50"
        in flat
    )
    assert r"c_{\mathrm{BP}}^{\mathrm{shift}}" in text
    assert (
        r"1+\frac{1}{3/2}+\frac{1}{3/2}+\frac12=\frac{17}{6}"
        in flat
    )
    assert "all even" in text
    assert "status \\ClaimStatusOpen" in text

    for match in re.finditer(r"(?<!\d)196(?!\d)", text):
        context = text[max(0, match.start() - 180) : match.end() + 180]
        assert "shift" in context.lower()

    for stale in (
        "98/3",
        r"\frac{98}{3}",
        r"\kappa(\BP_k)=\frac{c_{\BP}(k)}{6}",
        r"\varrho_{\mathrm{BP}}=1/6",
    ):
        assert stale not in text


def test_w3_ope_and_mode_coefficients_are_distinguished():
    block = between(
        r"\begin{definition}[Zamolodchikov $\mathcal W_3$ algebra]",
        r"\begin{proposition}[Principal $W_3/W_N$ standard-family ledger;",
    )
    assert r"\frac{32}{22+5c}\Lambda(w)" in block
    assert r"\frac{16}{22+5c}\partial\Lambda(w)" in block
    assert r"\frac{16}{22+5c}\Lambda(w)" not in block
    assert r"\frac{8}{22+5c}\partial\Lambda(w)" not in block


def test_quartic_audit_keeps_ope_and_mode_ratios_separate():
    block = between(
        r"\begin{theorem}[$\mathcal W_3$ rank-one exchange audit;",
        r"\begin{proposition}[Denominator filtration for the $\Lambda$ line;",
    )
    assert r"\ClaimStatusComputed" in block
    assert r"\frac{10240}{cD^3}" in block
    assert r"\frac{2560}{cD^3}" in block
    assert "OPE normalization" in block
    assert "mode-normalized" in block
    assert "full quartic tensor" in block


def test_bar_and_companion_claims_have_named_hypotheses():
    bar = between(
        r"\begin{theorem}[Bar differential and transferred curvature;",
        r"\begin{definition}[DS reduction of modules]",
    )
    assert r"d_{\bar B}^{2}=0" in bar
    assert "three typed objects" in bar

    duality = between(
        r"\begin{theorem}[Principal characteristic transport;",
        r"\begin{proposition}[Virasoro companion;",
    )
    assert r"\ClaimStatusConditional" in duality
    for item in ("DS/bar", "Verdier", "genus-one"):
        assert item in duality


def test_unverified_legacy_surfaces_are_absent():
    text = source()
    retired = (
        "Completion entropy ladder",
        "MacMahon plane-partition",
        r"\dim \sim 20",
        r"\dim \sim 200",
        "two-dimensional space of genus-$1$ deformations",
        r"c^2(2c-1)(5c+22)",
        r"\delta F_2(\mathcal{W}_3)=\frac{c + 204}{16c}",
        "genus-$2$ free energy of $\\mathcal{W}_3$",
        "bar cohomology of $\\mathcal W_\\infty$ grows",
    )
    for fragment in retired:
        assert fragment not in text


def test_cross_file_labels_remain_available():
    text = source()
    required = (
        "chap:w-algebra-koszul",
        "def:w3-algebra",
        "prop:principal-WN-standard-family-ledger",
        "thm:w-algebra-koszul-main",
        "thm:w3-koszul-dual",
        "thm:wn-obstruction",
        "thm:w3-quartic-channel-decomposition",
        "thm:w-virasoro-quartic-explicit",
        "comp:w3-genus2-multichannel",
        "conj:bp-duality",
        "thm:w-bp-strict",
        "thm:w-subregular-appell",
    )
    for label in required:
        assert rf"\label{{{label}}}" in text
