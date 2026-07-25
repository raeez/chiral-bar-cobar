"""Guards for the Yetter--Drinfeld Schauenburg Padovan seed."""

from __future__ import annotations

from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ARITHMETIC = ROOT / "chapters/connections/arithmetic_shadows.tex"
PREFACE = ROOT / "chapters/frame/preface.tex"
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"


def _text(path: Path) -> str:
    return " ".join(path.read_text().split())


def _padovan_brown_dimensions(limit: int) -> dict[int, int]:
    dims = {0: 1, 1: 0, 2: 1}
    for n in range(3, limit + 1):
        dims[n] = dims[n - 2] + dims[n - 3]
    return dims


def test_formal_motivic_coordinate_counts_use_browns_hilbert_series():
    text = _text(ARITHMETIC)
    assert r"\frac{1}{1-t^2-t^3}" in text
    assert "formal tree--period coordinates" in text
    assert "$(d_3, d_4, d_5) = (1, 1, 1)$" not in text


def test_preface_keeps_the_formal_brown_seed_out_of_the_theorem_spine():
    text = _text(PREFACE)
    assert "$(d_0,d_1,d_2)=(1,0,1)$" not in text
    assert "$(d_1,d_2,d_3)=(1,0,1)$" not in text


def test_yetter_drinfeld_high_weight_products_match_padovan_brown_values():
    dims = _padovan_brown_dimensions(16)
    expected = {
        13: (comb(24, 12) // 13, 16, 3_328_192, 7),
        14: (comb(26, 13) // 14, 21, 15_600_900, 8),
        15: (comb(28, 14) // 15, 28, 74_884_320, 8),
        16: (comb(30, 15) // 16, 37, 358_709_265, 9),
    }
    for n, (catalan, dimension, product, weight) in expected.items():
        assert dims[n] == dimension
        assert catalan * dimension == product
        assert n // 2 + 1 == weight


def test_harvest_matrix_records_yetter_drinfeld_seed_pass():
    text = _text(MATRIX)
    assert "Yetter--Drinfeld/Schauenburg item" in text
    assert "Pass 518" in text
