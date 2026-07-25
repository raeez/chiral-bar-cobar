"""Guardrails for Feigin--Frenkel terminology.

The level map k -> -k - 2h^vee is a critical-level reflection on the
affine scalar/current-presentation lane.  The Feigin--Frenkel centre
theorem occupies the fixed critical level, while the chiral Koszul
dual is constructed through the Verdier bar and pair map.
"""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]

SURFACES = [
    ROOT / "chapters/connections/concordance.tex",
    ROOT / "chapters/frame/preface.tex",
    ROOT / "chapters/frame/preface_sections2_4_draft.tex",
    ROOT / "chapters/theory/introduction.tex",
    ROOT / "chapters/theory/poincare_duality_quantum.tex",
    ROOT / "chapters/examples/kac_moody.tex",
    ROOT / "standalone/five_theorems_modular_koszul.tex",
    ROOT / "standalone/introduction_full_survey.tex",
    ROOT / "standalone/survey_modular_koszul_duality_v2.tex",
    ROOT / "standalone/survey_track_a_compressed.tex",
    ROOT / "chapters/examples/landscape_census.tex",
    ROOT / "chapters/theory/infinite_fingerprint_classification.tex",
]


def visible(path: Path) -> str:
    return "\n".join(
        line
        for line in path.read_text().splitlines()
        if not line.lstrip().startswith("%")
    )


def compact(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def assert_anchor(text: str, anchor: str) -> None:
    assert compact(anchor) in compact(text), anchor


def test_level_map_is_not_called_the_feigin_frenkel_involution_on_guarded_surfaces():
    combined = "\n".join(visible(path) for path in SURFACES)
    retired = (
        "The Feigin--Frenkel involution",
        "Feigin--Frenkel involution $k",
        "Feigin--Frenkel involution $k\\mapsto",
        "Feigin--Frenkel involution $k\\leftrightarrow",
        "Feigin--Frenkel reflection",
        "Feigin--Frenkel = Koszul duality",
        "Feigin--Frenkel Koszul dual sends",
        "on the Koszul dual side this is Feigin--Frenkel duality",
        "is Koszul duality on configuration spaces",
        "Feigin--Frenkel involution on $r$-matrices",
        "$c \\mapsto 26 - c$ (Feigin--Frenkel involution)",
    )
    for fragment in retired:
        assert fragment not in combined


def test_canonical_surfaces_name_the_three_distinct_objects():
    concordance = visible(ROOT / "chapters/connections/concordance.tex")
    for anchor in (
        "\\iota_{\\mathrm{crit}}(k)=-k-2h^\\vee",
        "Feigin--Frenkel centre theorem concerns the fixed critical level",
        "chiral Koszul dual object passes through the Verdier dual bar and\nthe chiral CE construction",
        "Feigin--Frenkel enters at the fixed\ncritical level",
    ):
        assert_anchor(concordance, anchor)

    intro = visible(ROOT / "chapters/theory/introduction.tex")
    assert_anchor(intro, "k'=\\iota_{\\mathrm{crit}}(k):=-k-2h^\\vee")
    assert_anchor(intro, "be the critical-level reflection")


def test_kac_moody_chapter_keeps_reflection_separate_from_verdier_duality():
    text = visible(ROOT / "chapters/examples/kac_moody.tex")
    for anchor in (
        "critical-level reflection \\(k \\mapsto -k - 2h^\\vee\\) records the\n"
        "level parameter of the affine scalar companion",
        "Verdier duality acts\non the bar coalgebra and then passes through the chiral CE dual",
        "not the bare level relabelling",
        "Kappa anti-symmetry under the critical-level reflection",
    ):
        assert_anchor(text, anchor)


def test_copy_forward_surfaces_keep_level_reflection_outside_koszul_dual_object():
    intro = visible(ROOT / "standalone/introduction_full_survey.tex")
    assert_anchor(
        intro,
        "critical-level reflection distinct from the chiral Koszul dual",
    )

    census = visible(ROOT / "chapters/examples/landscape_census.tex")
    assert_anchor(census, "The critical-level reflected companion level is")
    assert_anchor(census, "not the chiral\nKoszul dual object itself")

    fingerprint = visible(ROOT / "chapters/theory/infinite_fingerprint_classification.tex")
    assert_anchor(fingerprint, "critical-level reflected comparison side")
    assert_anchor(fingerprint, "not an identification\nof either \\(W\\)-algebra with the chiral Koszul dual object")
