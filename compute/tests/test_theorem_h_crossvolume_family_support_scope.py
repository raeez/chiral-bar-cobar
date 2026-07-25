"""Cross-volume guards for the family-indexed Theorem H surface."""

from __future__ import annotations

from pathlib import Path


VOL1 = Path(__file__).resolve().parents[2]
VOL2 = VOL1.parent / "chiral-bar-cobar-vol2"
VOL3 = VOL1.parent / "calabi-yau-quantum-groups"


def compact(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split())


def test_vol1_standalones_use_family_support_and_bounded_benchmarks():
    operadic = compact(VOL1 / "standalone/en_chiral_operadic_circle.tex")
    gravity = compact(
        VOL1 / "standalone/three_dimensional_quantum_gravity.tex"
    )
    survey = compact(VOL1 / "standalone/introduction_full_survey.tex")

    assert r"H_H(\cA;S)" in operadic
    assert r"\operatorname{Supp}\ChirHoch^\bullet(\cA)\subseteq S" in operadic
    assert r"(2,1,0,0,\ldots)" in operadic
    assert r"\{0,2,3\}" in operadic
    assert "Conjecture~7.5" in operadic

    assert r"\{0,2,3\}" in gravity
    assert "1+t^2+t^3" in gravity
    assert r"\Psi_{\mathrm{OCA}}" in gravity
    assert r"\mathbb{C}[\![c]\!]" not in gravity

    assert r"H_H(\cA;S)" in survey
    assert r"H^\bullet(K_{\cA,S})" in survey
    assert r"\ChirHoch^*(\cH_k) = (\C, \C, \C)" not in survey


def test_modular_surveys_keep_family_support_outside_the_equivalence_cycle():
    for relative in (
        "standalone/survey_modular_koszul_duality.tex",
        "standalone/survey_modular_koszul_duality_v2.tex",
    ):
        text = compact(VOL1 / relative)
        assert r"H_H(\cA;S)" in text, relative
        assert "chiral Hochschild family support" in text, relative
        assert r"chiral Hochschild $\{0,1,2\}$" not in text, relative
        assert r"\Leftrightarrow \textup{(viii)}" not in text, relative
        assert r"\Leftrightarrow$(viii)" not in text, relative


def test_vol2_separates_chart_support_from_cy_and_bounded_ambients():
    preface = compact(VOL2 / "chapters/frame/preface.tex")
    axioms = compact(VOL2 / "chapters/theory/axioms.tex")
    introduction = compact(VOL2 / "chapters/theory/introduction.tex")
    concordance = compact(VOL2 / "chapters/connections/concordance.tex")

    for text in (preface, axioms, introduction, concordance):
        assert "H_H(" in text

    for text in (preface, axioms, introduction):
        assert r"q_{\Phi,C}" in text

    assert "rank-one even superboson" in preface
    assert r"\{0,2,3\}" in preface
    assert "CY-$d$-enlarged sparse support" not in preface
    assert r"\chi_3 = 5" not in preface

    assert "transports this support verbatim" not in axioms
    assert r"\{0, 1, 2, d\}" not in introduction
    assert r"family datum $H_H(\cA;S)$" in concordance


def test_vol2_virasoro_surfaces_match_the_bounded_computation():
    for relative in (
        "chapters/examples/w-algebras.tex",
        "chapters/examples/w-algebras-stable.tex",
        "chapters/examples/w-algebras-virasoro.tex",
    ):
        text = compact(VOL2 / relative)
        assert "Bakalov--De Sole--Kac" in text, relative
        assert r"\{0,2,3\}" in text, relative
        assert r"\chi^{\mathrm{bd}}_{\mathrm{Vir}_c}" in text, relative
        assert r"P_{\text{Vir}_c}(t) = 1 + t^2" not in text, relative


def test_vol2_holography_keeps_virasoro_support_and_parameter_maps_typed():
    functor = compact(
        VOL2 / "chapters/connections/universal_holography_functor.tex"
    )
    part_vi = compact(
        VOL2 / "chapters/connections/part_vi_platonic_introduction.tex"
    )

    assert r"\{0,2,3\}" in functor
    assert r"\chi_{\operatorname{Vir}_c}^{\mathrm{bd}}" in functor
    assert r"\pi_c" in functor
    assert r"\Zder^{\mathrm{ch}}(\mathrm{Vir}_c)_{\mathrm{cent}} \simeq \C[\![c]\!]" not in functor

    assert r"H_H(\cA;S)" in part_vi
    assert r"K_{\cA,S}" in part_vi
    assert r"\ChirHoch{\cA}_{|\{0,1,2\}}" not in part_vi


def test_vol3_uses_comparison_maps_between_categorical_and_chiral_objects():
    categories = compact(VOL3 / "chapters/theory/cy_categories.tex")
    bridge = compact(VOL3 / "chapters/connections/bar_cobar_bridge.tex")
    introduction = compact(VOL3 / "chapters/theory/introduction.tex")

    assert r"H_H(A;S_A)" in categories
    assert r"q_{\Phi,C}" in categories
    assert r"H_H(A_\cC;S_{A_\cC})" in bridge
    assert r"H_H(\cA_\cC;S_\cC)" in introduction
    assert "CY-H datum" in introduction
    assert r"\tau_{\le2}\ChirHoch" not in introduction


def test_rank_twenty_four_superboson_uses_exterior_not_symmetric_support():
    text = compact(VOL3 / "chapters/theory/drinfeld_center.tex")
    assert r"\bigl(\Lambda^n\mathfrak h\bigr)^*" in text
    assert r"\binom{24}{n}+\binom{24}{n+1}" in text
    assert r"2^{25}-1" in text
    assert r"\chi^{\mathrm{bd}}_{H_{\mathrm{Muk}}}" in text
    assert r"\HH^2(H_{\mathrm{Muk}}, H_{\mathrm{Muk}}) = \mathrm{Sym}^2" not in text
    assert "total dimension of $325$" not in text


def test_gerbe_class_enters_chiral_cohomology_through_transgression():
    text = compact(
        VOL3
        / "chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex"
    )
    assert r"\operatorname{tg}_\mathcal D" in text
    assert r"q_{\Phi,C}" in text
    assert r"p\,q_{\Phi,C}(\gamma_{\mathrm{ob}})" in text
    assert "categorical chiral Hochschild" not in text
    assert "degree-$3$ gerbe shift" not in text


def test_enveloping_algebra_hochschild_coefficients_are_typed():
    text = compact(VOL3 / "chapters/theory/quantum_chiral_algebras.tex")
    assert r"HH^\bullet(U(\frak g),U(\frak g))" in text
    assert r"H^\bullet(\frak g,U(\frak g)^{\mathrm{ad}})" in text
    assert r"\mathrm{CE}^\bullet(L,L) = \HH^\bullet(A,A)" not in text
