"""Scope guards for the repaired deep W-algebra chapter."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/examples/w_algebras_deep.tex"


def source() -> str:
    return TARGET.read_text()


def squashed() -> str:
    return re.sub(r"\s+", " ", source())


def window(start: str, end: str) -> str:
    text = source()
    left = text.index(start)
    right = text.index(end, left)
    return text[left:right]


class TestPrincipalWN:
    def test_fateev_lukyanov_formula_and_reflection_are_exact(self):
        text = squashed()
        assert (
            r"c_N(k) =(N-1)-N(N^2-1)\frac{(k+N-1)^2}{k+N}"
            in text
        )
        assert r"k^\vee=-k-2N" in text
        assert r"c_N(k)+c_N(k^\vee) =4N^3-2N-2" in text
        assert r"t^\vee=k^\vee+N=-t" in text

    def test_modular_formula_is_hypothesis_typed(self):
        block = window(
            r"\begin{proposition}[Principal genus-one scalar package]",
            r"\begin{computation}[The \(\mathfrak{sl}_3\) DS hierarchy]",
        )
        assert r"\ClaimStatusConditional" in block
        assert r"H_{\mathrm{genus1}}^{W_N}" in block
        assert r"\kappa(\mathcal W_N^k)" in block
        assert r"c_N(k)(H_N-1)" in block
        assert r"K_N^\kappa" in block
        for value in ("13", "250/3", "533/2", "9394/15"):
            assert value in block

    def test_w3_ope_uses_the_zamolodchikov_normalization(self):
        block = window(
            r"\begin{computation}[Universal \(W_3\) OPE packet]",
            r"\begin{proposition}[Weight-four Virasoro Gram matrix]",
        )
        assert r"\frac{c/3}{(z-w)^6}" in block
        assert r"\frac{32}{5c+22}\Lambda" in block
        assert r"\frac{16}{5c+22}\partial\Lambda" in block
        assert r"\frac{A}{2}(m-n)\Lambda_{m+n}" in block


class TestBershadskyPolyakov:
    def test_fkr_lane_is_bosonic_and_all_even(self):
        text = source()
        assert "ordinary\nbosonic vertex algebra" in text
        for generator in (
            r"J_{1}^{\mathrm{even}}",
            r"G^+_{3/2}^{\mathrm{even}}",
            r"G^-_{3/2}^{\mathrm{even}}",
            r"T_{2}^{\mathrm{even}}",
        ):
            assert generator in text
        assert "fermionic" not in text

    def test_standard_central_charge_and_conductor_are_canonical(self):
        text = squashed()
        assert (
            r"c_{\mathrm{BP}}(k) =-\frac{(2k+3)(3k+1)}{k+3}"
            in text
        )
        assert r"k^\vee=-k-6" in text
        assert (
            r"c_{\mathrm{BP}}(k)+c_{\mathrm{BP}}(k^\vee)=50"
            in text
        )
        assert r"c_{\mathrm{BP}}(k)=25-6t-\frac{24}{t}" in text

    def test_196_is_confined_to_the_shifted_secondary_lane(self):
        block = window(
            r"\begin{proposition}[Secondary shifted BP scalar]",
            r"\begin{proposition}[BP reciprocal-weight diagnostic]",
        )
        assert r"\ClaimStatusComputed" in block
        assert r"c_{\mathrm{BP}}^{\mathrm{shift}}" in block
        assert "196" in block
        for match in re.finditer(r"(?<!\d)196(?!\d)", source()):
            context = source()[max(0, match.start() - 180) : match.end() + 180]
            assert "shift" in context.lower()

    def test_reciprocal_weight_value_is_diagnostic_only(self):
        block = window(
            r"\begin{proposition}[BP reciprocal-weight diagnostic]",
            r"\begin{computation}[BP bar and modular ledger]",
        )
        assert r"\frac{17}{6}" in block
        assert "reciprocal-weight diagnostic" in block
        assert "genus-one" in block

    def test_bp_modular_and_duality_entries_are_open(self):
        block = window(
            r"\begin{computation}[BP bar and modular ledger]",
            r"\begin{remark}[Orbit label and duality datum]",
        )
        assert r"\ClaimStatusOpen" in block
        for item in (
            r"\kappa_{\mathrm{BP}}(k)",
            r"\rho_{\mathrm{BP}}(k)",
            r"K^\kappa_{\mathrm{BP}}",
            r"(\mathcal B^k)^!",
            r"\mathbf R\mathrm{DS}_{(2,1)}\bar B_X",
        ):
            assert item in block

    def test_retired_bp_values_and_parity_are_absent(self):
        text = source()
        for stale in (
            "98/3",
            r"\frac{98}{3}",
            r"\kappa_{\mathrm{BP}}(k)=\frac{c_{\mathrm{BP}}(k)}6",
            r"(\mathcal B^k)^!\simeq\mathcal B^{-k-6}",
        ):
            assert stale not in text


class TestDerivedComparisons:
    def test_ds_bar_theorem_is_a_filtered_criterion(self):
        block = window(
            r"\begin{proposition}[Filtered criterion for DS--bar exchange]",
            r"\begin{remark}[Visible comparison obligations]",
        )
        assert r"\ClaimStatusConditional" in block
        for hypothesis in (
            r"\eta_{A,f}",
            r"\operatorname{gr}\eta_{A,f}",
            "complete, separated",
            "converge strongly",
        ):
            assert hypothesis in block

    def test_bp_and_arbitrary_nilpotent_comparisons_remain_open(self):
        text = source()
        bp = window(
            r"\begin{computation}[The \(\mathfrak{sl}_3\to W_3\) comparison window]",
            r"\begin{conjecture}[DS--Verdier intertwining for arbitrary nilpotent]",
        )
        assert r"\ClaimStatusOpen" in bp
        conjecture_start = text.index(
            r"\begin{conjecture}[DS--Verdier intertwining for arbitrary nilpotent]"
        )
        conjecture_end = text.index(r"\end{conjecture}", conjecture_start)
        conjecture = text[conjecture_start:conjecture_end]
        assert r"\ClaimStatusConjectured" in conjecture

    def test_fabricated_geometric_identifications_are_absent(self):
        text = source()
        retired = (
            r"J^\infty(G/B)\cong",
            "chains on",
            r"\operatorname{Maps}(X,G/P",
            "partition transpose gives",
            "bar homology is the exterior",
            "ghost Fock module is acyclic",
        )
        for fragment in retired:
            assert fragment not in text


class TestCharacterVsBar:
    def test_generic_character_and_macmahon_factorization_are_exact(self):
        text = squashed()
        assert (
            r"\chi_N(q) =\prod_{s=2}^{N}\prod_{m\ge0}(1-q^{s+m})^{-1}"
            in text
        )
        assert r"\chi_{\mathrm{st}}(q)=M(q)\varphi(q)" in text
        assert r"\frac{\varphi(q)}{1-q}\,M(q)" not in text

    def test_character_is_not_promoted_to_bar_cohomology(self):
        text = source()
        assert "This is a state-counting theorem." in text
        assert "These series are determined by the bar differential." in text
        bar_block = window(
            r"\begin{remark}[Bar-growth quantities]",
            r"\begin{remark}[Principal shadow data]",
        )
        assert r"\ClaimStatusOpen" in bar_block
        assert "Koszul entropy" not in text

    def test_large_rank_koszul_and_scalar_claims_are_open(self):
        text = source()
        for label in (
            r"\label{thm:winfty-factorization-kd}",
            r"\label{thm:winfty-scalar}",
        ):
            start = text.index(label)
            assert r"\ClaimStatusOpen" in text[start : start + 400]


class TestArithmeticRecognition:
    def test_borcherds_weight_is_conditional_on_explicit_input(self):
        block = window(
            r"\begin{theorem}[Weight implied by a recognition package]",
            r"\begin{remark}[The \(N=3,4\) coefficient obligation]",
        )
        assert r"\ClaimStatusConditional" in block
        assert r"f^{(N)}(0,0)=2(N+3)" in block
        assert (
            r"\operatorname{wt}\operatorname{Borch}(\phi^{(N)})=N+3"
            in block
        )

    def test_extended_ladder_is_open(self):
        text = source()
        start = text.index(r"\label{thm:walgdeep-N13-N24-ladder}")
        assert r"\ClaimStatusOpen" in text[start : start + 500]


def test_cross_file_reference_labels_are_retained():
    text = source()
    labels = (
        "comp:sl3-ds-hierarchy",
        "comp:miura-w3",
        "thm:master-commutative-square",
        "comp:ds-bar-sl3-w3",
        "comp:w3-deg3-cohom",
        "comp:bp-bar",
        "conj:ds-kd-arbitrary-nilpotent",
        "def:filtered-derived-ds-functor",
        "prop:ds-bar-formality",
        "prop:ds-transferred-koszul-dual",
        "def:modular-koszul-triple",
        "thm:winfty-scalar",
        "prop:gram-wt4",
        "thm:c334",
        "thm:y-algebra-koszulness",
        "conj:pixton-from-shadows",
        "thm:walgdeep-gaiotto-siegel-weight",
        "thm:walgdeep-N24-conway",
    )
    for label in labels:
        assert rf"\label{{{label}}}" in text
