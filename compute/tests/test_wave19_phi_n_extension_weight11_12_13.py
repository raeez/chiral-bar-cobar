"""Test harness for wave19_phi_n_extension_weight11_12_13.

Runs all Wave-19 tests and multi-path cross-checks:
  - Padovan MZV basis dimension  d_n
  - Brown-Deligne basis at weights 11, 12, 13
  - KZ iterated-integral word structure
  - Richardson-extrapolated numerical anchors
  - phi^(11), phi^(12), phi^(13) structure
  - reversal-duality symmetry
  - multi-path cross-checks (recurrence self-consistency,
    Richardson-vs-anchor table, depth-4 contribution, KZ-word
    consistency).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "lib"))

from wave19_phi_n_extension_weight11_12_13 import (  # noqa: E402
    run_tests,
    phi_n_mzv,
    padovan_d_n,
    mzv_anchor_float,
    deligne_basis_weight_11,
    deligne_basis_weight_12_depth_le_3,
    deligne_basis_weight_12_depth_4,
    deligne_basis_weight_13_depth_le_3,
)


def test_wave19_phi_n_extension_all():
    """Run the complete Wave-19 test suite."""
    run_tests()


def test_padovan_anchors_claude_md():
    """Confirm Padovan anchors from CLAUDE.md."""
    anchors = {1: 1, 2: 0, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2,
               8: 3, 9: 4, 10: 5, 11: 7, 12: 9}
    for n, d in anchors.items():
        assert padovan_d_n(n) == d


def test_padovan_weight_13():
    """d_13 = d_11 + d_10 = 7 + 5 = 12."""
    assert padovan_d_n(13) == 12
    assert padovan_d_n(13) == padovan_d_n(11) + padovan_d_n(10)


def test_zeta_3333_anchor():
    """V1 anchor for zeta(3,3,3,3) ~ 2.959990 * 10^{-4}."""
    v = mzv_anchor_float((3, 3, 3, 3))
    assert 2.9599e-4 < v < 2.9600e-4


def test_zeta_11_anchor():
    v = mzv_anchor_float((11,))
    assert 1.000494 < v < 1.000495


def test_zeta_13_anchor():
    v = mzv_anchor_float((13,))
    assert 1.000122 < v < 1.000123


def test_phi_11_denominator():
    ph = phi_n_mzv(11)
    assert ph["denominator_factorial"] == 39_916_800


def test_phi_12_denominator():
    ph = phi_n_mzv(12)
    assert ph["denominator_factorial"] == 479_001_600


def test_phi_13_denominator():
    ph = phi_n_mzv(13)
    assert ph["denominator_factorial"] == 6_227_020_800


def test_phi_12_contains_depth_4():
    """phi^(12) basis must contain zeta(3,3,3,3) (depth-4 irreducible)."""
    ph = phi_n_mzv(12)
    found = any(
        e["indices"] == (3, 3, 3, 3) and e["name"] == "zeta(3, 3, 3, 3)"
        for e in ph["basis"]
    )
    assert found


def test_phi_13_no_depth_4():
    """phi^(13) must NOT contain a depth-4 irreducible (Broadhurst-Kreimer)."""
    ph = phi_n_mzv(13)
    for e in ph["basis"]:
        assert len(e["indices"]) <= 3


def test_basis_counts_match_padovan():
    assert len(deligne_basis_weight_11()) == padovan_d_n(11)
    assert (len(deligne_basis_weight_12_depth_le_3()) + 1) == padovan_d_n(12)
    assert len(deligne_basis_weight_13_depth_le_3()) == padovan_d_n(13)


def test_weight_12_depth_4_is_zeta_3333():
    name, s = deligne_basis_weight_12_depth_4()
    assert name == "zeta(3, 3, 3, 3)"
    assert s == (3, 3, 3, 3)


if __name__ == "__main__":
    test_wave19_phi_n_extension_all()
    test_padovan_anchors_claude_md()
    test_padovan_weight_13()
    test_zeta_3333_anchor()
    test_zeta_11_anchor()
    test_zeta_13_anchor()
    test_phi_11_denominator()
    test_phi_12_denominator()
    test_phi_13_denominator()
    test_phi_12_contains_depth_4()
    test_phi_13_no_depth_4()
    test_basis_counts_match_padovan()
    test_weight_12_depth_4_is_zeta_3333()
    print("test_wave19_phi_n_extension_weight11_12_13: all tests passed.")
