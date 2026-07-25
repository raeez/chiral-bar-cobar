"""Scope guards for the high-risk higher-shadow consumers."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]

VMP_ALL = ROOT / "chapters/theory/virasoro_motivic_purity_all_r_platonic.tex"
SUBSUB = ROOT / "chapters/theory/shadow_tower_sub_subleading_platonic.tex"
ZG = ROOT / "chapters/theory/z_g_kummer_bernoulli_platonic.tex"
NILPOTENT = ROOT / "chapters/theory/nilpotent_completion.tex"
CLASS_M = ROOT / "chapters/theory/shadow_tower_other_class_M_platonic.tex"
SHADOW_L = ROOT / "chapters/theory/shadow_L_function_platonic.tex"
ARITHMETIC = ROOT / "chapters/connections/arithmetic_shadows.tex"


def source(path: Path) -> str:
    return path.read_text()


def labels(path: Path) -> list[str]:
    return re.findall(r"\\label\{([^}]+)\}", source(path))


def window(path: Path, start: str, end: str) -> str:
    text = source(path)
    left = text.index(start)
    right = text.index(end, left)
    return text[left:right]


class TestLabelSurface:
    def test_all_labels_are_retained_and_unique(self):
        expected = {
            VMP_ALL: 23,
            SUBSUB: 18,
            ZG: 34,
            NILPOTENT: 90,
            CLASS_M: 49,
            SHADOW_L: 24,
            ARITHMETIC: 641,
        }
        for path, count in expected.items():
            found = labels(path)
            assert len(found) == count, path
            assert len(found) == len(set(found)), path


class TestMotivicAndAsymptoticSeparation:
    def test_all_arity_motivic_claim_requires_the_full_package(self):
        block = window(
            VMP_ALL,
            r"\begin{theorem}[Tate factorization of the Virasoro residue tower]",
            r"\begin{remark}[Logical relation with a formal recurrence]",
        )
        assert r"\ClaimStatusConditional" in block
        for package in (
            r"\mathsf H_{\mathrm{res}}",
            r"\mathsf H_{\mathrm{mot}}",
            r"\mathsf H_{\mathrm{Tate}}",
        ):
            assert package in block
        closing = window(
            VMP_ALL,
            r"\begin{corollary}[All-arity Virasoro motivic status]",
            r"\section*{Epilogue}",
        )
        assert r"\ClaimStatusOpen" in closing

    def test_subsubleading_formula_is_formal_and_geometric_use_is_typed(self):
        formal = window(
            SUBSUB,
            r"\begin{theorem}[Formal sub-subleading coefficient]",
            r"\begin{remark}[Initial value]",
        )
        assert r"\ClaimStatusProvedHere" in formal
        geometric = window(
            SUBSUB,
            r"\begin{remark}[Residue-tower interpretation]",
            r"\section{Congruence data of the formal quartic}",
        )
        assert r"\ClaimStatusConditional" in geometric
        assert r"\mathsf H_{\mathrm{res}}+\mathsf H_{\mathrm{asymp}}" in geometric

    def test_shadow_l_analytic_and_genus_lanes_are_conditional(self):
        text = source(SHADOW_L)
        for package in (
            r"\mathsf H_{\mathrm{res}}",
            r"\mathsf H_{\mathrm{asymp}}",
            r"\mathsf H_{\mathrm{mot}}",
            r"\mathsf H_{\mathrm{Kum}}",
            r"\mathsf H_{\mathrm{gen}}",
        ):
            assert package in text
        analytic = window(
            SHADOW_L,
            r"\begin{theorem}[Meromorphic continuation from",
            r"\begin{remark}[The weight-one motivic line]",
        )
        genus = window(
            SHADOW_L,
            r"\begin{theorem}[Genus-slot comparison]",
            r"\begin{remark}[Bernoulli values and genus slots]",
        )
        assert r"\ClaimStatusConditional" in analytic
        assert r"\ClaimStatusConditional" in genus


class TestArithmeticAndFamilyComparisons:
    def test_zg_preserves_exact_bernoulli_values_and_types_comparison(self):
        text = source(ZG)
        for fragment in (
            r"B_{12}=-691/2730",
            r"B_{16}=-3617/510",
            r"\mathsf H_{\mathrm{res}}",
            r"\mathsf H_{\mathrm{Kum}}",
        ):
            assert fragment in text
        comparison = window(
            ZG,
            r"\begin{theorem}[Bernoulli witnesses and the residue comparison problem]",
            r"\begin{remark}[Geometric provenance]",
        )
        assert r"\ClaimStatusConditional" in comparison
        assert r"\ref{thm:s-r-kummer-absent-through-r-11}" not in comparison

    def test_class_m_keeps_local_data_and_opens_geometric_towers(self):
        text = source(CLASS_M)
        for fragment in (
            r"\mathsf H_{\mathrm{form}}",
            r"\mathsf H_{\mathrm{res}}",
            r"\mathsf H_{\mathrm{asymp}}",
            r"\frac{3W(w)}{(z-w)^2}",
            r"\(32/(22+5c)\)",
            r"c_{\mathrm{BP}}(k)=-\frac{(2k+3)(3k+1)}{k+3}",
        ):
            assert fragment in text
        assert r"\label{prop:wp-cartan-shadow-through-r6}" in text
        wp = window(
            CLASS_M,
            r"\begin{proposition}[Cartan-line computation through arity six]",
            r"\begin{remark}[Small parameters]",
        )
        assert r"\ClaimStatusOpen" in wp

    def test_nilpotent_phi_and_delta_surfaces_are_chain_level_problems(self):
        text = source(NILPOTENT)
        phi = window(
            NILPOTENT,
            r"\begin{proposition}[Motivic comparison problem for \(\phi^{(n)}\)]",
            r"\begin{remark}[The weight-\(25\) test]",
        )
        delta = window(
            NILPOTENT,
            r"\begin{proposition}[Construction problem for higher correction cochains]",
            r"\begin{remark}[Planar counts and residue corrections]",
        )
        assert r"\ClaimStatusOpen" in phi
        assert r"\mathsf H_{\mathrm{mot}}" in phi
        assert r"\ClaimStatusOpen" in delta
        assert r"\mathsf H_{\mathrm{res}}+\mathsf H_{\mathrm{mot}}" in delta
        assert r"\langle\Lambda,\Lambda\rangle=\frac{c(5c+22)}{10}" in delta
        for retired in (
            r"S_3^{E_8, \mathrm{skew}} = 2",
            r"2\,\zeta(3)\,k^3",
            r"Q_7(c) = c^2 + 42c",
            r"(\Phi_{10}^{\mathrm{un}})^{25/2}",
        ):
            assert retired not in text

    def test_humbert_filter_is_a_typed_comparison_diagram(self):
        coordinates = window(
            ARITHMETIC,
            r"\section{Formal coordinates for a Yetter--Drinfeld correction}",
            r"\begin{remark}[Yetter--Drinfeld and pentagon complexes]",
        )
        assert r"\ClaimStatusProvedHere" in coordinates
        assert "formal tree--period coordinates" in coordinates
        assert "rank of a represented yetter--drinfeld cochain" in " ".join(
            coordinates.lower().split()
        )
        assert r"\mathrm{wt}(\delta" not in coordinates

        block = window(
            ARITHMETIC,
            r"\begin{remark}[Yetter--Drinfeld and pentagon complexes]",
            r"\section{$\mu_{32}$ obstruction near the quadruple wall",
        )
        for package in (
            r"\mathsf H_{\mathrm{res}}",
            r"\mathsf H_{\mathrm{mot}}",
            r"\mathsf H_{\mathrm{Kum}}",
        ):
            assert package in block
        assert r"\ClaimStatusConditional" in block
        assert "open comparison problems" in block
        for retired in (
            r"n\equiv 3, 5\pmod 8",
            r"C_{n-1}\cdot d_n > 0",
            r"k_{\mathrm{HH}}^{\mathrm{win}}(g)=2g-1",
        ):
            assert retired not in block
