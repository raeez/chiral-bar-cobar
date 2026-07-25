"""Structural guards for the two stable-base lanes of Theorem D."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]


def _active_tex_files() -> tuple[Path, ...]:
    return (
        ROOT / "main.tex",
        *sorted((ROOT / "chapters").rglob("*.tex")),
        *sorted((ROOT / "appendices").rglob("*.tex")),
        *sorted((ROOT / "standalone").rglob("*.tex")),
    )


def _visible(path: Path) -> str:
    return "\n".join(
        line
        for line in path.read_text().splitlines()
        if not line.lstrip().startswith("%")
    )


UNPOINTED_GENUS_ONE = re.compile(
    r"\\operatorname\{Obs\}\^\{\\mathrm\{def\}\}_"
    r"(?:1(?![0-9,{])|\{1\})"
)
UNPOINTED_GENUS_ONE_COMPLEX = re.compile(
    r"(?:\\Def|\\operatorname\{Def\}|\\mathrm\{Def\})_"
    r"(?:1(?![0-9,{])|\{1\})"
)
NATIVE_ASSERTION = re.compile(
    r"\\operatorname\{Obs\}\^\{\\mathrm\{def\}\}_g"
    r"(?:\([^)]*\))?"
    r".{0,80}?(?:\\in|lies\s+in)"
    r".{0,80}?H\^2",
    re.DOTALL,
)
STABLE_RANGE = re.compile(r"g\s*\\geq?\s*2")
COLLAPSED_PRONOUN = re.compile(
    r"\\operatorname\{Obs\}\^\{\\mathrm\{def\}\}_g"
    r".{0,220}?H_D\^1.{0,100}?its\s+(?:normalized\s+)?"
    r"(?:pointed\s+)?genus-one\s+trace",
    re.DOTALL,
)


def test_genus_one_deformation_class_is_pointed_on_every_active_surface():
    offenders: list[tuple[Path, int, str]] = []
    for path in _active_tex_files():
        for line_number, line in enumerate(_visible(path).splitlines(), start=1):
            if UNPOINTED_GENUS_ONE.search(line):
                offenders.append((path.relative_to(ROOT), line_number, line))
            if UNPOINTED_GENUS_ONE_COMPLEX.search(line):
                offenders.append((path.relative_to(ROOT), line_number, line))
    assert offenders == []


def test_every_native_unpointed_assertion_carries_the_stable_range():
    offenders: list[tuple[Path, str]] = []
    for path in _active_tex_files():
        text = _visible(path)
        for match in NATIVE_ASSERTION.finditer(text):
            start = max(0, match.start() - 400)
            stop = min(len(text), match.end() + 400)
            if STABLE_RANGE.search(text[start:stop]) is None:
                excerpt = " ".join(text[match.start() : match.end()].split())
                offenders.append((path.relative_to(ROOT), excerpt))
    assert offenders == []


def test_pointed_trace_is_not_a_pronoun_shadow_of_the_stable_class():
    offenders: list[tuple[Path, str]] = []
    for path in _active_tex_files():
        text = _visible(path)
        for match in COLLAPSED_PRONOUN.finditer(text):
            offenders.append(
                (
                    path.relative_to(ROOT),
                    " ".join(text[match.start() : match.end()].split()),
                )
            )
    assert offenders == []


def test_principal_theorem_d_surfaces_name_both_stable_bases():
    principal = (
        "chapters/theory/higher_genus_foundations.tex",
        "chapters/theory/chiral_climax_platonic.tex",
        "chapters/connections/master_concordance.tex",
        "chapters/connections/master_reconstruction.tex",
        "standalone/five_theorems_modular_koszul.tex",
        "appendices/type_system.tex",
    )
    for relative_path in principal:
        text = _visible(ROOT / relative_path)
        assert STABLE_RANGE.search(text), relative_path
        assert r"\operatorname{Obs}^{\mathrm{def}}_g" in text, relative_path
        assert (
            r"\operatorname{Obs}^{\mathrm{def}}_{1,1}" in text
        ), relative_path

    foundations = _visible(
        ROOT / "chapters/theory/higher_genus_foundations.tex"
    )
    standalone = _visible(
        ROOT / "standalone/five_theorems_modular_koszul.tex"
    )
    assert r"H^2(\Def_{1,1}(\cA))" in foundations
    assert r"H^2(\mathrm{Def}_{1,1}(\cA))" in standalone
