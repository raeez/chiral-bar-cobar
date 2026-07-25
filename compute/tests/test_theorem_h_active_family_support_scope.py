"""Source guards for the family-indexed Theorem H surface."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]


def source(relative: str) -> str:
    return " ".join((ROOT / relative).read_text(encoding="utf-8").split())


ACTIVE_SUMMARIES = (
    "appendices/type_system.tex",
    "chapters/frame/open_beilinson_tower_platonic.tex",
    "chapters/frame/guide_to_main_results.tex",
    "chapters/connections/grand_unification_platonic.tex",
    "chapters/theory/introduction.tex",
)

PROPAGATED_SURFACES = (
    "chapters/examples/level1_bridge.tex",
    "chapters/connections/concordance.tex",
    "chapters/frame/heisenberg_frame.tex",
    "chapters/theory/en_koszul_duality.tex",
    "chapters/theory/higher_genus_modular_koszul.tex",
    "chapters/theory/three_invariants.tex",
    "chapters/connections/master_reconstruction.tex",
)

RESIDUAL_SURFACES = (
    "appendices/hochschild_conventions.tex",
    "chapters/connections/frontier_modular_holography_platonic.tex",
    "chapters/connections/holographic_codes_koszul.tex",
    "chapters/connections/outlook.tex",
    "chapters/connections/thqg_introduction_supplement_body.tex",
    "chapters/connections/thqg_open_closed_realization.tex",
    "chapters/examples/bershadsky_polyakov.tex",
    "chapters/examples/beta_gamma.tex",
    "chapters/examples/logarithmic_w_algebras.tex",
    "chapters/examples/symmetric_orbifolds.tex",
    "chapters/examples/w3_holographic_datum.tex",
    "chapters/frame/preface_sections5_9_draft.tex",
    "chapters/theory/chiral_koszul_pairs.tex",
    "chapters/theory/derived_langlands.tex",
    "chapters/theory/e1_modular_koszul.tex",
    "chapters/theory/en_koszul_duality.tex",
    "chapters/theory/existence_criteria.tex",
    "chapters/theory/ftm_seven_fold_tfae_platonic.tex",
    "chapters/theory/higher_genus_complementarity.tex",
    "chapters/theory/higher_genus_modular_koszul.tex",
    "chapters/theory/hochschild_cohomology.tex",
    "chapters/theory/koszul_pair_structure.tex",
    "chapters/theory/motivic_shadow_tower.tex",
    "chapters/theory/shadow_tower_quadrichotomy_platonic.tex",
    "chapters/theory/three_invariants.tex",
    "chapters/theory/universal_conductor_K_platonic.tex",
)

PAIRING_SURFACES = (
    "appendices/hochschild_conventions.tex",
    "chapters/connections/holographic_codes_koszul.tex",
    "chapters/connections/outlook.tex",
    "chapters/connections/thqg_introduction_supplement_body.tex",
    "chapters/connections/thqg_open_closed_realization.tex",
    "chapters/examples/bershadsky_polyakov.tex",
    "chapters/examples/beta_gamma.tex",
    "chapters/examples/symmetric_orbifolds.tex",
    "chapters/examples/w3_holographic_datum.tex",
    "chapters/frame/preface_sections5_9_draft.tex",
    "chapters/theory/chiral_koszul_pairs.tex",
    "chapters/theory/e1_modular_koszul.tex",
    "chapters/theory/ftm_seven_fold_tfae_platonic.tex",
    "chapters/theory/hochschild_cohomology.tex",
    "chapters/theory/motivic_shadow_tower.tex",
    "chapters/theory/universal_conductor_K_platonic.tex",
)


def test_active_summaries_state_family_support_and_benchmarks():
    for relative in ACTIVE_SUMMARIES:
        text = source(relative)
        assert "H_H(" in text, relative
        assert r"\operatorname{Supp}\ChirHoch^\bullet" in text, relative
        assert r"\subset\{0,1,2\}" not in text, relative
        assert r"\subseteq\{0,1,2\}" not in text, relative
        assert "amplitude $[0,2]$" not in text, relative

    for relative in ACTIVE_SUMMARIES[1:]:
        text = source(relative)
        assert r"\{0,2,3\}" in text, relative
        assert "rank-one even superboson" in text, relative


def test_boundary_chapter_uses_variable_cutoff_and_keeps_degree_three():
    text = source("chapters/theory/theorem_h_off_koszul_platonic.tex")
    required = (
        "Fix an integer~$m$",
        r"\mathfrak{o}_{\mathrm H}^{m+1}(\cA)",
        r"n\geq m+2",
        r"S=\{0,2,3\}",
        r"\dim\ChirHoch^3=1",
        r"\operatorname{Supp}\ChirHoch^\bullet(\cA)\subseteq S",
        r"\cA^{i}=C_X(s^{-1}V,s^{-2}R)",
    )
    for fragment in required:
        assert fragment in text, fragment

    assert r"\ChirHoch^n(\cA)=0\qquad(n\notin\{0,1,2\})" not in text
    assert "has amplitude~$[0,2]$" not in text


def test_virasoro_and_superboson_rows_match_bdsk_support():
    pair = source("chapters/theory/koszul_pair_structure.tex")
    crosswalk = source(
        "chapters/theory/three_hochschild_unification_platonic.tex"
    )

    for text in (pair, crosswalk):
        assert r"n\in\{0,2,3\}" in text

    assert "1+t^2+t^3" in pair

    assert r"\dim H^n_{\mathrm{ch},b}=(2,1,0,\ldots)" in crosswalk
    assert r"\cA^{\mathrm i}=C_X(s^{-1}V,s^{-2}R)" in crosswalk
    assert r"\cA^{\mathrm i}=H^\bullet B^{\mathrm{ch}}(\cA)" not in crosswalk
    assert r"\ChirHoch^n(\mathrm{Vir}_c)=0" not in pair


def test_pairing_shift_is_separate_from_support():
    frame = source("chapters/frame/open_beilinson_tower_platonic.tex")
    boundary = source("chapters/theory/theorem_h_off_koszul_platonic.tex")
    assert "A degree-$d$ perfect pairing" in frame
    assert "A perfect degree-$d$ pairing is a separate map" in boundary


def test_remaining_active_surfaces_use_family_support():
    for relative in PROPAGATED_SURFACES:
        text = source(relative)
        assert "H_H(" in text, relative
        stale_phrases = (
            r"concentrated in degrees $\{0,1,2\}$",
            r"concentrated in degrees $\{0, 1, 2\}$",
            "cohomological amplitude $[0,2]$",
            "cohomological amplitude $[0, 2]$",
            "P(t) = 1 + t + t^2",
        )
        for phrase in stale_phrases:
            assert phrase not in text, (relative, phrase)

    heisenberg = source("chapters/frame/heisenberg_frame.tex")
    assert r"$(2,1,0,\ldots)$" in heisenberg
    assert "$P(t)=2+t$" in heisenberg

    master = source("chapters/connections/master_reconstruction.tex")
    assert "hypothesis package $H_H(A_b;S)$" in master
    assert "hypothesis package $H_3(A_b;S)$" not in master


def test_residual_theorem_h_surfaces_are_family_indexed():
    stale_patterns = (
        re.compile(
            r"(?:concentrat\w*|vanish\w*)[^.]{0,180}"
            r"\\\{0,\s*1,\s*2\\\}",
            re.IGNORECASE,
        ),
        re.compile(
            r"(?:Theorem~H|H \(chiral Hochschild\))[^.]{0,260}"
            r"\[0,\s*2\]",
            re.IGNORECASE,
        ),
        re.compile(
            r"\\ChirHoch\^n[^.]{0,180}"
            r"(?:n\\notin\\\{0,\s*1,\s*2\\\}|n\s*>\s*2)",
            re.IGNORECASE,
        ),
        re.compile(r"P\(t\)\s*=\s*1\s*\+\s*t\s*\+\s*t\^2"),
    )

    for relative in RESIDUAL_SURFACES:
        text = source(relative)
        assert "H_H(" in text, relative
        for pattern in stale_patterns:
            assert pattern.search(text) is None, (relative, pattern.pattern)


def test_residual_pairing_statements_are_separate_inputs():
    for relative in PAIRING_SURFACES:
        text = source(relative)
        assert (
            "perfect degree-" in text
            or "degree-$d$ perfect pairing" in text
        ), relative


def test_residual_benchmarks_and_family_examples_have_exact_support():
    bp = source("chapters/examples/bershadsky_polyakov.tex")
    assert r"H_H(\mathcal B^k;S_{\mathrm{BP}})" in bp
    assert r"S_{\mathrm{BP}}\setminus\{0,1,2\}" in bp
    assert "perfect degree-two chain pairing" in bp

    e1 = source("chapters/theory/e1_modular_koszul.tex")
    assert r"=(2,1,0,\ldots)" in e1
    assert r"P_{\cH_k}(t) \;=\; 2+t" in e1

    en = source("chapters/theory/en_koszul_duality.tex")
    assert r"degrees~$\{0,2,3\}$" in en
    assert "$P(t)=1+t^2+t^3$" in en

    portrait = source("chapters/theory/hochschild_cohomology.tex")
    assert r"H_H(\mathcal A_{\mathsf r};S_{\mathsf r})" in portrait
    assert r"\dim H^3" in portrait
    assert "bounded-to-chart quasi-isomorphism" in portrait

    meta = source("chapters/theory/chiral_koszul_pairs.tex")
    assert r"H_H(\cA;S)\Rightarrow" in meta
    assert "one-way consequence on the Koszul locus" not in meta

    orbifold = source("chapters/examples/symmetric_orbifolds.tex")
    assert r"H_H(X_N^{\mathrm{id}};S_N)" in orbifold
    assert r"\subseteq S_N" in orbifold


def test_n1_and_affine_summaries_use_family_support_data():
    n1 = source("standalone/N1_koszul_meta.tex")
    assert r"H_H(\Heis_k;S)" in n1
    assert "bounded rank-one even-superboson model" in n1
    assert "dimensions $(2,1)$ in degrees $(0,1)$" in n1
    assert "single bar degree $\{0,1,2\}$" not in n1
    assert "one-way support theorem for a supplied family datum" in n1

    affine = source("chapters/examples/kac_moody.tex")
    assert r"H_H(\widehat{\fg}_k;S)" in affine
    assert "bounded affine calculation supplies conjectural BDSK upper bounds" in affine
    assert "Proved/generic" not in affine
