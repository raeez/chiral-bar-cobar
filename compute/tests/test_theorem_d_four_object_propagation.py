"""Structural guards for the four ambient stages of Theorem D."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

FOUR_STAGE_SUMMARIES = (
    "main.tex",
    "chapters/theory/introduction.tex",
    "chapters/frame/guide_to_main_results.tex",
    "chapters/frame/part_iv_platonic_introduction.tex",
    "standalone/programme_summary.tex",
    "standalone/programme_summary_sections2_4.tex",
    "standalone/survey_track_a_compressed.tex",
    "standalone/survey_modular_koszul_duality_v2.tex",
    "standalone/chiral_chern_weil.tex",
)

EXPLICIT_HODGE_SUMMARIES = tuple(
    path
    for path in FOUR_STAGE_SUMMARIES
    if path != "chapters/frame/part_iv_platonic_introduction.tex"
)


def _compact(relative_path: str) -> str:
    return "".join((ROOT / relative_path).read_text().split())


def _active_tex_files() -> tuple[Path, ...]:
    return (
        ROOT / "main.tex",
        *sorted((ROOT / "chapters").rglob("*.tex")),
        *sorted((ROOT / "standalone").glob("*.tex")),
    )


def test_theorem_d_summary_surfaces_name_every_ambient_stage():
    structural_tokens = (
        r"\operatorname{Obs}^{\mathrm{def}}_g",
        r"H_D^1",
        r"H_D^K",
        r"\lambda_{-1}(\mathbbE_g)",
        r"H_D^{\mathrm{tr}}",
        r"H_D^{\mathrm{graph}}",
        r"\lambda_g^{\mathrm{FP}}",
        r"\deltaF_g^{\mathrm{cross}}",
    )
    for relative_path in FOUR_STAGE_SUMMARIES:
        compact = _compact(relative_path)
        for token in structural_tokens:
            assert token in compact, (relative_path, token)


def test_hodge_character_is_the_signed_character_of_the_perfect_object():
    for relative_path in EXPLICIT_HODGE_SUMMARIES:
        compact = _compact(relative_path)
        assert r"\operatorname{ch}_g" in compact, relative_path
        assert r"(-1)^g\kappa" in compact, relative_path
        assert r"\lambda_g" in compact, relative_path


def test_native_deformation_class_is_never_declared_equal_to_top_hodge_class():
    for path in _active_tex_files():
        for line_number, line in enumerate(path.read_text().splitlines(), start=1):
            if r"\operatorname{Obs}^{\mathrm{def}}_g" not in line:
                continue
            assert not (
                "=" in line
                and r"\kappa" in line
                and r"\lambda_g" in line
            ), (path.relative_to(ROOT), line_number, line)


def test_cross_channel_term_occurs_only_in_the_numerical_graph_lane():
    for path in _active_tex_files():
        for line_number, line in enumerate(path.read_text().splitlines(), start=1):
            if r"\delta F" not in line and r"\deltaF" not in line:
                continue
            assert not (
                (r"\mathrm{obs}_g" in line or r"\operatorname{obs}_g" in line)
                and "=" in line
            ), (path.relative_to(ROOT), line_number, line)


def test_short_obs_notation_is_confined_to_its_explicit_hodge_definition():
    allowed = Path("chapters/theory/clutching_uniqueness_platonic.tex")
    offenders: list[tuple[Path, int, str]] = []
    for path in _active_tex_files():
        relative = path.relative_to(ROOT)
        for line_number, line in enumerate(path.read_text().splitlines(), start=1):
            has_short_obs = (
                r"\mathrm{obs}_g" in line or r"\operatorname{obs}_g" in line
            )
            has_hodge_formula = r"\lambda_g" in line and "=" in line
            if has_short_obs and has_hodge_formula and relative != allowed:
                offenders.append((relative, line_number, line))
    assert offenders == []

    compact = _compact(str(allowed))
    assert (
        r"\mathrm{obs}_g(\cA):=(-1)^g"
        r"\operatorname{obs}^{\mathrm{Hdg}}_g(\cA):=(-1)^g"
        r"\operatorname{ch}_g(\mathfrakO_g^K(\cA))"
    ) in compact
