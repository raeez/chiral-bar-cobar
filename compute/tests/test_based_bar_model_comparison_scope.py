"""Guards for based comparison of bar models and the unbased torsor."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
BAR = ROOT / "chapters/theory/bar_construction.tex"
INTRO = ROOT / "chapters/theory/introduction.tex"
HIGHER = ROOT / "chapters/theory/higher_genus_modular_koszul.tex"
SURVEY = ROOT / "standalone/introduction_full_survey.tex"


def _flat(path: Path) -> str:
    return re.sub(r"\s+", " ", path.read_text())


def _environment(path: Path, label: str, environment: str) -> str:
    source = path.read_text()
    label_at = source.index(rf"\label{{{label}}}")
    start = source.rindex(rf"\begin{{{environment}}}", 0, label_at)
    end = source.index(rf"\end{{{environment}}}", label_at)
    return re.sub(r"\s+", " ", source[start:end])


def test_canonical_proposition_is_a_based_slice_comparison():
    proposition = _environment(BAR, "prop:model-independence", "proposition")
    required = (
        "Based comparison of bar models",
        r"u_i\colon B_i\xrightarrow{\;\sim\;}\mathcal B_X(\cA)",
        r"\mathsf{dgCoalg}_{X,/\mathcal B_X(\cA)}",
        "is contractible",
        r"\operatorname{Aut}(\mathcal B_X(\cA))",
        "automorphism torsor",
    )
    for fragment in required:
        assert fragment in proposition


def test_introduction_states_based_and_unbased_comparison_types():
    text = _flat(INTRO)
    required = (
        r"$u_i\colon B_i\xrightarrow{\sim}\mathcal B_X(\cA)$",
        "In the slice over the fixed bar object",
        r"$(B_1,u_1)$ and~$(B_2,u_2)$ is contractible",
        r"$\operatorname{Aut}(\mathcal B_X(\cA))$",
        "A chosen based quasi-isomorphism transports cohomology",
        "unbased self-equivalences form the homotopy automorphism space",
    )
    for fragment in required:
        assert fragment in text


def test_higher_genus_definition_transports_along_a_based_map():
    text = _flat(HIGHER)
    required = (
        "Based comparison of models",
        r"$u_i\colon B_i\xrightarrow{\sim}B$",
        "in the slice over~$B$ is contractible",
        r"$\operatorname{Aut}(B)$",
        "Transport along a chosen based quasi-isomorphism",
        "factorization algebra together with its fixed comparison datum",
    )
    for fragment in required:
        assert fragment in text


def test_standalone_survey_uses_chosen_comparisons():
    text = _flat(SURVEY)
    required = (
        "faithful chosen chart on the formal moduli problem",
        r"$u_i\colon B_i\xrightarrow{\sim}\mathcal B_X(\cA)$",
        "contractible based comparison space in the slice",
        r"$\operatorname{Aut}(\mathcal B_X(\cA))$-torsor",
        r"A chosen quasi-isomorphism of $L_\infty$ algebras",
        "induces an equivalence of their Maurer--Cartan infinity-groupoids",
        "changing that comparison acts through the corresponding gauge",
    )
    for fragment in required:
        assert fragment in text


def test_raw_contractibility_advertisements_are_absent():
    retired = (
        "The space of models is contractible",
        "contractibility of the space of models",
        "Any two admissible dg presentations are connected by a contractible",
        "Defined up to contractible ambiguity",
        r"every MC element of~$\Convstr$ lifts canonically",
    )
    for path in (INTRO, HIGHER, SURVEY):
        text = _flat(path)
        for phrase in retired:
            assert phrase not in text, f"{phrase!r} occurs in {path}"
