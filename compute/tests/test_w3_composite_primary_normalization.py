"""Source guards for the Zamolodchikov W_3 normalization."""

from __future__ import annotations

from pathlib import Path
import re

from sympy import Rational, simplify, symbols


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/examples/w3_composite_fields.tex"
HOLOGRAPHIC_TARGET = ROOT / "chapters/examples/w3_holographic_datum.tex"


def source() -> str:
    return TARGET.read_text()


def squashed() -> str:
    return re.sub(r"\s+", " ", source())


def test_complete_ope_uses_32_and_16():
    text = source()
    assert r"\frac{32}{22+5c}\Lambda(w)" in text
    assert r"\frac{16}{22+5c}\partial\Lambda(w)" in text
    assert r"\frac{16}{22+5c}\Lambda(w)" not in text
    assert r"\frac{8}{22+5c}\partial\Lambda(w)" not in text


def test_contour_computation_recovers_mode_coefficient():
    text = squashed()
    assert r"\frac{A}{2}(m-n)\Lambda_{m+n}" in text
    assert "$A=32/(22+5c)$" in text
    assert "$16(m-n)/(22+5c)$" in text
    assert r"\frac{16}{22+5c}(m-n)\Lambda_{m+n}" in text


def test_lambda_modes_use_vacuum_normal_ordering():
    text = source()
    assert r"p\leq-2" in text
    assert r"p\geq-1" in text
    assert r"p < n" not in text


def test_highest_weight_eigenvalue_and_null_curve_are_repaired():
    text = squashed()
    assert r"\left(h^2+\frac h5\right)|h,w\rangle" in text
    assert r"9w^2(22+5c)=2h^2(32h+2-c)" in text
    assert "32h - 62 - c" not in text
    assert r"h^2-\frac{9h}{5}" not in text


def test_rank_one_exchange_ratios_are_normalization_typed():
    text = source()
    for formula in (
        r"\frac{320}{cD^2}",
        r"\frac{10240}{cD^3}",
        r"\frac{160}{cD^2}",
        r"\frac{2560}{cD^3}",
    ):
        assert formula in text
    assert "OPE-normalized" in text
    assert "mode-normalized" in text
    assert "full quartic shadow" in text


def test_weight_six_block_is_not_mocked_up_as_two_dimensional():
    text = squashed()
    assert r"\dim V_5=4" in text
    assert r"\dim V_6=8" in text
    assert "has dimension~$4$" in text
    assert r"c^2(2c-1)(5c+22)" not in text
    assert "two-dimensional weight-$6$" not in text


def test_external_reference_labels_are_retained():
    text = source()
    for label in (
        "def:lambda-complete",
        "thm:lambda-coefficients-derivation",
        "thm:w-w-ope-complete",
    ):
        assert rf"\label{{{label}}}" in text


def test_independent_contour_algebra_gives_the_half_factor():
    A, m, n = symbols("A m n")
    double_pole = A * (m + 2)
    derivative_pole = -A * (m + n + 4) / 2
    assert simplify(double_pole + derivative_pole - A * (m - n) / 2) == 0


def test_independent_highest_weight_normal_ordering():
    h = symbols("h")
    normal_ordered_tt = h**2 + 2 * h
    derivative_correction = Rational(9, 5) * h
    assert simplify(normal_ordered_tt - derivative_correction - (h**2 + h / 5)) == 0


def test_independent_level_one_determinant_reduction():
    c, h, w = symbols("c h w")
    D = 22 + 5 * c
    m22 = -h / 5 + 32 * (h**2 + h / 5) / D
    determinant = 2 * h * m22 - 9 * w**2
    cleared = simplify(D * determinant)
    expected = 2 * h**2 * (32 * h + 2 - c) - 9 * w**2 * D
    assert simplify(cleared - expected) == 0


def test_independent_exchange_ratio_arithmetic():
    c = symbols("c", nonzero=True)
    D = symbols("D", nonzero=True)
    norm = c * D / 10
    ope = 32 / D
    mode = 16 / D
    assert simplify(ope**2 / norm - 10240 / (c * D**3)) == 0
    assert simplify(mode**2 / norm - 2560 / (c * D**3)) == 0


def test_holographic_chapter_uses_the_same_ope_and_highest_weight_conventions():
    text = re.sub(r"\s+", " ", HOLOGRAPHIC_TARGET.read_text())
    assert r"\alpha(c) = 32/(22+5c)" in text
    assert r"\Bigl(h^2 + \tfrac{h}{5}\Bigr)" in text
    assert r"h \in \{0,-1/5\}" in text
    assert "16/(22+5c)" not in text
    assert r"h^2 - \tfrac{9h}{5}" not in text
