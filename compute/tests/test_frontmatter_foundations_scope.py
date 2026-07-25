"""Semantic guards for the reconstructed abstract and preface."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
MAIN = ROOT / "main.tex"
PREFACE = ROOT / "chapters/frame/preface.tex"


def visible(path: Path) -> str:
    return "\n".join(
        line for line in path.read_text().splitlines()
        if not line.lstrip().startswith("%")
    )


def abstract() -> str:
    source = visible(MAIN)
    start = source.index(r"\begin{abstract}")
    end = source.index(r"\end{abstract}", start)
    return source[start:end]


def block(source: str, label: str, environment: str) -> str:
    label_position = source.index(rf"\label{{{label}}}")
    start = source.rindex(rf"\begin{{{environment}}}", 0, label_position)
    end = source.index(rf"\end{{{environment}}}", label_position)
    return source[start:end]


def assert_anchor(source: str, anchor: str) -> None:
    normalized_source = re.sub(r"\s+", " ", source)
    normalized_anchor = re.sub(r"\s+", " ", anchor)
    assert anchor in source or normalized_anchor in normalized_source


def test_abstract_begins_with_objects_and_maps() -> None:
    source = abstract()
    for required in (
        "complete augmented chiral algebra",
        "complete conilpotent factorization coalgebra",
        "derived chiral centre",
        r"\eta_{12}\wedge\eta_{23}",
        "arity-three bar cancellation is associativity",
        r"\Omega_XB_X(\cA)\xrightarrow{\sim}\cA",
        r"q_\cA\colon \cA^{\mathrm i}",
        "Symmetrisation is treated as homotopy descent",
        "Positive genus begins after a cyclic trace or perfect pairing",
        "Bakalov--De Sole--Kac",
        "quadrant, presentation, Beilinson level, and hypothesis package",
    ):
        assert_anchor(source, required)


def test_abstract_excludes_retired_identifications_and_open_scalars() -> None:
    source = abstract()
    for retired in (
        "Bar(A) is the bulk",
        "primitive open sector",
        "universal curvature identity",
        "98/3",
        "25/3",
        r"K^{\kappa_{\mathrm{ch}}}=8",
    ):
        assert retired not in source


def test_preface_separates_local_geometry_and_associative_bar_algebra() -> None:
    source = visible(PREFACE)
    arnold = block(source, "prop:preface-arnold", "proposition")
    associative = block(
        source, "prop:preface-associative-bar-three", "proposition"
    )
    local = block(source, "prop:preface-local-square-zero", "proposition")

    assert r"\ClaimStatusProvedHere" in arnold
    assert_anchor(arnold, "logarithmic de Rham presentation")
    assert r"\eta_{12}\wedge\eta_{23}" in arnold

    assert r"b_\mu^2[a|b|c]" in associative
    assert r"(ab)c-a(bc)" in associative
    assert_anchor(associative, "dg associativity package")

    assert r"\ClaimStatusConditional" in local
    assert r"H_{\mathrm{loc}}(\cA;U)" in local
    assert r"d_{\bar B}^{\,2}=0" in local


def test_preface_separates_universal_resolution_from_quadratic_recognition() -> None:
    source = visible(PREFACE)
    point = block(source, "thm:preface-point-bar-cobar", "theorem")
    quadratic = block(source, "thm:preface-quadratic-recognition", "theorem")
    ran = block(source, "thm:preface-enhanced-ran-reconstruction", "theorem")
    theorem_a = block(source, "thm:preface-theorem-a", "theorem")

    assert r"\Omega B(A)\xrightarrow{\ \sim\ }A" in point
    assert_anchor(point, "augmentation and conilpotence package")
    assert r"q_A\colon A^{\mathrm i}\longrightarrow B(A)" in quadratic
    assert_anchor(quadratic, "quadratic diagonal")
    assert_anchor(ran, "Francis--Gaitsgory")
    assert_anchor(ran, "enhanced associative Ran presentation")
    assert r"H_{\mathrm{BC}}(X)" in theorem_a
    assert r"\ClaimStatusConditional" in theorem_a


def test_preface_types_levels_three_through_five() -> None:
    source = visible(PREFACE)
    for required in (
        r"\cZ_{\mathrm{ch}}^{\mathrm{der}}(A_b)",
        "module, brane, and line-operator categories",
        "cyclic trace and stable-graph amplitudes",
        r"H_{\mathbb D}(\cA)",
        r"\cA^!_\infty",
        r"H_{\mathrm{mod}}(\cA)",
        r"d_0\Theta_{\cA}",
        r"H_H(\cA;S)",
        r"\operatorname{Supp}",
        r"\operatorname{ChirHoch}^{\bullet}(\cA)\subseteq S",
    ):
        assert required in source


def test_preface_uses_positive_declarative_prose() -> None:
    source = visible(PREFACE)
    prohibited = re.compile(
        r"\b(?:not|does\s+not|do\s+not|cannot|without|never|no|fails?|failure|"
        r"undefined|outside|excluded?)\b",
        flags=re.IGNORECASE,
    )
    assert prohibited.search(source) is None


def test_frontmatter_environment_balance() -> None:
    source = visible(PREFACE)
    for environment in (
        "definition",
        "proposition",
        "theorem",
        "principle",
        "proof",
        "enumerate",
    ):
        assert source.count(rf"\begin{{{environment}}}") == source.count(
            rf"\end{{{environment}}}"
        )
