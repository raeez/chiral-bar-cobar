"""Regression guards for the typed chiral-centre theorem surface."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/theory/chiral_center_theorem.tex"
MAIN = ROOT / "main.tex"
PREFACE = ROOT / "chapters/frame/preface.tex"


def source() -> str:
    return TARGET.read_text()


def compact() -> str:
    return re.sub(r"\s+", " ", source())


def block(label: str, environment: str) -> str:
    text = source()
    label_position = text.index(rf"\label{{{label}}}")
    start = text.rindex(rf"\begin{{{environment}}}", 0, label_position)
    end = text.index(rf"\end{{{environment}}}", label_position)
    return re.sub(r"\s+", " ", text[start:end])


class TestTypedDerivedCentre:
    def test_object_precedes_its_charts(self):
        text = compact()
        assert r"Z^{\mathrm{der}}_{\mathrm{ch}}(A) := R\operatorname{End}_{A^e}(A)" in text
        assert "definition fixes the object before a bar resolution" in text

    def test_operadic_package_carries_actual_comparison_data(self):
        datum = block("def:cct-operadic-chart-package", "definition")
        for required in (
            r"H_{\mathrm{op}}(A)",
            "complete one-coloured dg nonsymmetric operad",
            "fixed common expansion domain",
            r"m\in\mathfrak g_A^1",
            r"d_{\mathcal P}m+\frac12[m,m]=0",
            r"\gamma_A\colon C^\bullet_{\mathcal P}(A,A)",
            r"\varprojlim\nolimits_N^1 H^{q-1}",
        ):
            assert required in datum

    def test_mauer_cartan_degree_and_curvature_identity_are_pinned(self):
        theorem = block("thm:brace-dg-algebra", "theorem")
        text = compact()
        assert r"H_{\mathrm{op}}(A)" in theorem
        assert r"\ClaimStatusConditional" in theorem
        assert "Type signature: Open quadrant" in theorem
        assert "completed minimal-operad action" in theorem
        assert "complete dg Lie algebra" in theorem
        assert r"d_m^2f = \left[d_{\mathcal P}m+\frac12[m,m],f\right] =0" in text
        assert r"\cite[identity~\textup{(}6\textup{)} and Theorem~3]{GV95}" in source()
        assert "adjacent cup-boundary terms" in text
        assert "complete brace dg algebra" not in text


class TestComparisonFirewalls:
    def test_geometric_to_algebraic_map_has_finite_window_and_limit_gates(self):
        datum = block("def:cct-geometric-algebraic-package", "definition")
        theorem = block("prop:geometric-algebraic-hochschild", "proposition")
        for required in (
            r"H_{\mathrm{geom/alg}}(A)",
            "restriction-and-expansion chain map",
            "finite-window quasi-isomorphism proof",
            r"\varprojlim_N^1 H^{q-1}",
        ):
            assert required in datum
        assert r"\ClaimStatusConditional" in theorem
        assert "preserves the ordered brace operations" in theorem

    def test_swiss_cheese_surface_is_an_evaluation_criterion(self):
        datum = block("def:local-swiss-cheese-pair", "definition")
        theorem = block("thm:chiral-deligne-tamarkin", "theorem")
        text = compact()
        assert r"H_{\mathrm{SC}}(B,A)" in datum
        assert r"\Phi_\mu\colon B\to C^\bullet_{\mathcal P}(A,A)" in datum
        assert r"\ClaimStatusConditional" in theorem
        assert "Type signature: Open quadrant" in theorem
        assert "evaluation criterion" in text
        assert "mapping-space equivalence" in text
        assert "open comparison problem" in text

    def test_e3_upgrade_names_its_extra_topologization_data(self):
        datum = block(
            "def:e3-topologization-datum-derived-centre", "definition"
        )
        theorem = block(
            "prop:e2-center-not-e3-topologization", "proposition"
        )
        assert r"[Q,G]=L_{-1}" in datum
        assert "framed-discs or Dunn-additivity comparison" in datum
        assert r"\ClaimStatusConditional" in theorem


class TestBoundedComputationLedger:
    def test_bounded_benchmarks_and_promotion_package_are_separated(self):
        datum = block("def:cct-finite-window-promotion", "definition")
        theorem = block("prop:derived-center-explicit", "proposition")
        assert r"H_{\mathrm{fw}}(V)" in datum
        assert "each finite conformal-weight window" in datum
        assert r"vanishing \(\varprojlim^1\)" in datum
        assert r"\cite[Theorem~7.4]{BDSK21}" in theorem
        assert r"(2,1,0,0,\ldots)" in theorem
        assert r"\cite[Theorem~7.2]{BDSK21}" in theorem
        assert r"n\in\{0,2,3\}" in theorem
        assert r"\cite[Conjecture~7.5]{BDSK21}" in theorem

    def test_affine_claim_is_restricted_to_inner_directions(self):
        first = block("prop:chirhoch1-affine-km", "proposition")
        bracket = block("prop:gerstenhaber-sl2-bracket", "proposition")
        assert "inner chiral derivation" in first
        assert "exhaustion theorem for all continuous outer derivations" in first
        assert "prequotient zero-mode derivations" in bracket
        assert "Additional outer classes form a separate cohomological sector" in bracket
        assert re.search(r"\\ChirHoch\^1\([^)]*\)\s*(?:=|\\cong)\s*0", source()) is None

    def test_cyclic_and_hkr_structures_retain_comparison_status(self):
        cyclic = block("prop:heisenberg-bv-structure", "conjecture")
        hkr = block("prop:chirhoch-cdr", "conjecture")
        attribution = block("rem:chirhoch-cdr-attribution", "remark")
        assert r"\ClaimStatusConjectured" in cyclic
        assert "quasi-isomorphism to the chart cyclic complex" in cyclic
        assert r"\ClaimStatusConjectured" in hkr
        assert r"\Omega_X^{\mathrm{ch}}" in hkr
        assert r"\cite{MSV99}" in attribution
        assert "supplies the proposed target" in attribution
        assert "additional comparison problem" in attribution


class TestScalarLedger:
    def test_exact_and_conditional_vol_i_sets_are_separated(self):
        theorem = block(
            "thm:derived-centre-complementarity-strengthened", "theorem"
        )
        assert r"\mathcal S^{\mathrm{VolI,exact}}_\kappa=\{0,\;13\}" in theorem
        assert r"\left\{0,\;13,\;\frac{250}{3}\right\}" in theorem
        assert r"H_{\mathrm{diag}}^{g=1}+H_{W_3}^{\mathrm{DS/bar}}" in theorem
        assert "free/affine cancellation" in theorem
        assert r"\operatorname{Vir}_c & 26 & 13" in theorem
        assert r"\mathcal W_3^{\mathrm{prin}} & 100 & 250/3" in theorem

    def test_bp_central_conductor_is_exact_and_modular_lane_is_open(self):
        theorem = block(
            "thm:derived-centre-complementarity-strengthened", "theorem"
        )
        assert r"k\in\mathbb C\setminus\{-3\}" in theorem
        assert r"c_{\mathrm{BP}}(k)+c_{\mathrm{BP}}(-k-6)=50" in theorem
        assert r"K^c_{\mathrm{BP}}=50" in theorem
        assert r"J,G^+,G^-,T\) are even" in theorem
        assert r"\frac{17}{6}" in theorem
        assert r"\ClaimStatusOpen" in theorem
        assert "genus-one computation is the open obligation" in theorem
        assert "consequence of that conditional genus-one equation" in theorem
        assert r"K^\kappa_{\mathrm{BP}}=25/3" in theorem
        assert r"\mathcal S^{\mathrm{VolI,exact}}_\kappa" in theorem

    def test_mukai_eight_is_lattice_exact_and_chiral_conditional(self):
        theorem = block(
            "thm:derived-centre-complementarity-strengthened", "theorem"
        )
        for required in (
            r"U^4\oplus E_8(-1)^2",
            r"\mathrm{II}_{4,20}",
            r"rank \(24\), signature \((4,20)\)",
            r"2c_+(\mathrm{II}_{4,20})=8",
            r"K^\kappa_{\mathsf B}=8",
            r"H_{\mathrm{chart}}",
            r"H_{\mathrm{KD}}",
            r"H_{\mathrm{scalar}}",
            r"H_{\mathrm{mod}}",
            r"H_{\mathrm{quantum}}",
        ):
            assert required in theorem
        assert "is conjectural under" in theorem

    def test_comparison_display_retains_status_tags(self):
        text = compact()
        assert r"\left\{\frac{250}{3}\right\}_{H_{\mathrm{diag}}^{g=1}+H_{W_3}^{\mathrm{DS/bar}}}" in text
        assert r"\left\{\frac{25}{3}\right\}_{\kappa_{\mathrm{BP}}=c_{\mathrm{BP}}/6}" in text
        assert r"\{8\}_{H_B\text{-candidate}}" in text
        assert "status tags in this display are part of the notation" in text


class TestIndependentArithmeticOracles:
    @staticmethod
    def bp_central_charge(k: Fraction) -> Fraction:
        return -((2 * k + 3) * (3 * k + 1)) / (k + 3)

    def test_bp_reflection_and_even_weight_diagnostic(self):
        for k in map(Fraction, (-8, -5, -2, -1, 0, 1, 4, 9)):
            assert k != -3
            assert self.bp_central_charge(k) + self.bp_central_charge(-k - 6) == 50
        assert Fraction(1) + Fraction(2, 3) + Fraction(2, 3) + Fraction(1, 2) == Fraction(17, 6)

    def test_mukai_rank_signature_and_status_separated_vol_i_values(self):
        rank_u, signature_u = 2, (1, 1)
        rank_e8_negative, signature_e8_negative = 8, (0, 8)
        rank = 4 * rank_u + 2 * rank_e8_negative
        signature = (
            4 * signature_u[0] + 2 * signature_e8_negative[0],
            4 * signature_u[1] + 2 * signature_e8_negative[1],
        )
        assert rank == 24
        assert signature == (4, 20)
        assert 2 * signature[0] == 8
        exact_values = {Fraction(0), Fraction(13)}
        conditional_w3_extension = exact_values | {Fraction(250, 3)}
        assert exact_values == {Fraction(0), Fraction(13)}
        assert conditional_w3_extension == {
            Fraction(0), Fraction(13), Fraction(250, 3)
        }


class TestAutomorphicFrontier:
    def test_baily_borel_realization_is_an_open_comparison_datum(self):
        remark = block("rem:cct-baily-borel", "remark")
        assert r"\ClaimStatusConjectured" in remark
        assert "a functor from each specified chiral family" in remark
        assert "a theorem identifying the chiral genus-one trace" in remark
        assert r"\cite{BailyBorel66}" in remark
        assert "compatibility with a specified Humbert-divisor inclusion" in remark
        assert "normalization checks distinguishing" in remark
        assert "open comparison problem" in remark

    def test_fabricated_realization_language_is_retired(self):
        text = source().lower()
        for retired in (
            "realised geometrically",
            "realized geometrically",
            "is the baily--borel stratum",
            "is the humbert surface",
            "humbert realization theorem",
        ):
            assert retired not in text


class TestFrontmatterCorrections:
    def test_arnold_identity_stays_on_the_coordinate_chart(self):
        text = MAIN.read_text()
        abstract = text[text.index(r"\begin{abstract}") : text.index(r"\end{abstract}")]
        assert r"On a coordinate disc \(U\subset X\)" in abstract
        assert r"\operatorname{Conf}_3(U)" in abstract
        assert r"\operatorname{Conf}_3(X)" not in abstract

    def test_boundedness_is_repeated_for_both_bdsk_benchmarks(self):
        text = MAIN.read_text()
        abstract = text[text.index(r"\begin{abstract}") : text.index(r"\end{abstract}")]
        normalized = re.sub(r"\s+", " ", abstract)
        assert normalized.count("bounded vertex cohomology") == 2
        assert "rank-one even free superboson" in normalized
        assert "universal Virasoro algebra" in normalized

    def test_preface_koszul_sentence_is_unique_and_clean(self):
        text = PREFACE.read_text()
        assert text.count("the classical Koszul calculation") == 1
        assert r"\xrightarrow{\ \sim\ }A ." not in text
