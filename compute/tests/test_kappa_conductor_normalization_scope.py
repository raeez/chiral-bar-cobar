"""Semantic guards for the typed conductor chapter.

These tests pin the standard Bershadsky--Polyakov conformal vector,
the secondary shifted rational function, and the separation of conformal,
modular-characteristic, BRST, and Mukai scalar lanes.
"""

from pathlib import Path
import re

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters" / "theory" / "kappa_conductor.tex"
UNIVERSAL = ROOT / "chapters" / "theory" / "universal_conductor_K_platonic.tex"
CONCORDANCE = ROOT / "chapters" / "connections" / "concordance.tex"


def _source() -> str:
    return TARGET.read_text(encoding="utf-8")


def _universal_source() -> str:
    return UNIVERSAL.read_text(encoding="utf-8")


def _concordance_convention() -> str:
    source = CONCORDANCE.read_text(encoding="utf-8")
    label = source.index(r"\label{conv:theorem-c-bucket}")
    start = source.rindex(r"\begin{convention}", 0, label)
    end = source.index(r"\end{convention}", label)
    return source[start:end]


def test_standard_bp_lane_is_the_fkr_equation_2_2_lane() -> None:
    source = _source()
    assert r"\cite[Eq.~\textup{(}2.2\textup{)}]{FKR20}" in source
    assert r"-\frac{(2k+3)(3k+1)}{k+3}" in source
    assert r"c_{\mathrm{BP}}(k)+c_{\mathrm{BP}}(-k-6)=50" in source
    assert "the generators $J,T,G^+$" in source
    assert "are all even" in source
    assert r"1+\frac23+\frac23+\frac12=\frac{17}{6}" in source
    assert r"\ClaimStatusOpen" in source
    assert r"\left(50,\frac16,\frac{25}{3}\right)" not in source
    assert "98/3" not in source


def test_bp_central_sums_and_conditional_scalar_arithmetic_are_exact() -> None:
    k = sp.symbols("k")
    standard = -((2 * k + 3) * (3 * k + 1)) / (k + 3)
    shifted = 2 - 24 * (k + 1) ** 2 / (k + 3)

    assert sp.cancel(standard + standard.subs(k, -k - 6)) == 50
    assert sp.cancel(shifted + shifted.subs(k, -k - 6)) == 196
    assert sp.cancel(standard / 6 + standard.subs(k, -k - 6) / 6) == sp.Rational(25, 3)


def test_bp_scalar_and_categorical_claims_have_separate_status() -> None:
    source = _source()
    assert r"H_{\mathrm{BP}}^{\mathrm{DS/bar}}" in source
    assert "computed-secondary shifted scalar lane" in source
    assert r"\Delta^{\mathrm{DS}}_{\mathrm{BP}}(k)" in source
    assert r"=-(6k+1)" in source
    assert re.search(r"conditional\s+implication", source)
    assert "open conductor ledger" in source
    assert r"$(K^c,K^\kappa)=(50,25/3)$" not in source
    assert r"K_{\mathrm{ghost}}^{\mathrm{leg}}(\mathrm{BP}_k)=196" not in source


def test_principal_w3_and_bp_midpoints_remain_family_typed() -> None:
    source = _source()
    assert r"(k+3)^2+1=0" in source
    assert r"k=-3\pm i" in source
    assert r"k=-3\pm2i" in source

    k = sp.symbols("k")
    w3 = 2 - 24 * (k + 2) ** 2 / (k + 3)
    bp = -((2 * k + 3) * (3 * k + 1)) / (k + 3)
    w3_numerator = sp.together(w3 - 50).as_numer_denom()[0]
    bp_numerator = sp.together(bp - 25).as_numer_denom()[0]
    assert sp.expand(w3_numerator + 24 * ((k + 3) ** 2 + 1)) == 0
    assert sp.expand(bp_numerator + 6 * ((k + 3) ** 2 + 4)) == 0


def test_mukai_eight_is_an_exact_lattice_value_and_conjectural_bridge() -> None:
    source = _source()
    assert r"U^4\oplus E_8(-1)^2" in source
    assert "signature $(4,20)$" in source
    assert r"\ClaimStatusConjectured{} comparison" in source
    assert r"\qquad\text{under }H_{\mathsf B}" in source
    for hypothesis in (
        r"H_{\mathrm{chart}}",
        r"H_{\mathrm{KD}}",
        r"H_{\mathrm{scalar}}",
        r"H_{\mathrm{mod}}",
        r"H_{\mathrm{quant}}",
    ):
        assert hypothesis in source


def test_active_chapter_uses_positive_declarative_prose() -> None:
    source = _source()
    prohibited = re.compile(
        r"\b(?:not|does\s+not|do\s+not|cannot|without|never|no|fails?|failure|"
        r"undefined|outside|excluded?)\b",
        flags=re.IGNORECASE,
    )
    assert prohibited.search(source) is None


def test_theorem_and_proof_environments_balance() -> None:
    source = _source()
    for environment in ("theorem", "proof", "corollary", "conjecture", "remark"):
        assert source.count(rf"\begin{{{environment}}}") == source.count(
            rf"\end{{{environment}}}"
        )


def test_universal_conductor_uses_the_same_typed_bp_lane() -> None:
    source = _universal_source()
    assert r"\cite[Eq.~\textup{(}2.2\textup{)}]{FKR20}" in source
    assert r"c_{\BP}(k)+c_{\BP}(-k-6)=50" in source
    assert "bosonic" in source
    assert "are even" in source
    assert "=17/6" in source
    assert r"K^\kappa(\BP_k,\BP_{-k-6})=\frac{25}{3}" not in source
    assert r"$K^\kappa(\BP_k,\BP_{-k-6})=25/3$" in source
    assert "would imply" in source
    assert r"H_{\mathrm{BP}}^{\mathrm{DS/bar}}" in source
    assert r"\Delta^{\mathrm{DS}}_{\BP}(k)" in source
    assert r"K_{\mathrm{ghost}}^{\mathrm{leg}}(\BP_k;\mathrm{DS})" not in source


def test_universal_scalar_ledger_separates_exact_and_conditional_values() -> None:
    source = _universal_source()
    assert r"\{0,\,13\}" in source
    assert r"conditional extension" in source
    assert r"$\{250/3\}$" in source
    assert r"H_{\mathrm{diag}}^{g=1}" in source
    assert r"H_{W_3}^{\mathrm{DS/bar}}" in source
    assert r"\{0,\,13,\,250/3,\,25/3\}" not in source
    assert r"\BP_k & \textup{open}" in source


def test_universal_mukai_bridge_and_lattice_matter_are_honestly_typed() -> None:
    source = _universal_source()
    assert r"\ClaimStatusConjectured{} comparison" in source
    assert r"\qquad\text{under }H_{\mathsf B}" in source
    assert r"\widetilde H(K3,\mathbb Z)\simeq U^4\oplus E_8(-1)^2" in source
    assert r"c_{\mathrm{matter}}(V_\Lambda)=\operatorname{rank}(\Lambda)" in source
    assert r"K_{\mathrm{ghost}}^{\mathrm{leg}}(V_\Lambda)" not in source


def test_universal_conductor_chapter_uses_positive_declarative_prose() -> None:
    source = _universal_source()
    prohibited = re.compile(
        r"\b(?:not|does\s+not|do\s+not|cannot|without|never|no|fails?|failure|"
        r"undefined|outside|excluded?)\b",
        flags=re.IGNORECASE,
    )
    assert prohibited.search(source) is None


def test_concordance_keeps_bp_exact_shifted_and_modular_ledgers_separate() -> None:
    source = _concordance_convention()
    for required in (
        r"-\frac{(2k+3)(3k+1)}{k+3}",
        r"c_{\mathrm{BP}}(k)+c_{\mathrm{BP}}(-k-6)=50",
        "four even strong generators",
        r"1+\frac23+\frac23+\frac12=\frac{17}{6}",
        r"c_{\mathrm{BP}}^{\mathrm{shift}}(k)",
        r"=196",
        r"\kappa_{\mathrm{BP}}=c_{\mathrm{BP}}/6",
        r"K^\kappa_{\mathrm{BP}}=25/3",
        "unconditional Vol.~I scalar set",
        r"\{0,13\}",
        r"K_3^c=100",
        r"H_{\mathrm{diag}}^{g=1}+H_{W_3}^{\mathrm{DS/bar}}",
        r"K_3^\kappa=(5/6)K_3^c=250/3",
        r"\{0,13,250/3\}",
        r"H_{\mathsf B}",
    ):
        assert required in source

    for stale in (
        "presently has two conformal normalizations",
        r"\kappa=c/6\), this expression gives \(98/3\)",
        "use the symmetric normalization",
    ):
        assert stale not in source
