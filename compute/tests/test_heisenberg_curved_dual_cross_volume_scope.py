"""Cross-volume guard for the Heisenberg curved-dual convention."""

from __future__ import annotations

from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
VOL2 = ROOT.parent / "chiral-bar-cobar-vol2"
VOL3 = ROOT.parent / "calabi-yau-quantum-groups"


SURFACES = [
    ROOT / "compute/lib/koszul_pairs.py",
    ROOT / "compute/lib/modular_koszul_engine.py",
    ROOT / "compute/lib/theorem_twisted_holography_deep_engine.py",
    ROOT / "compute/lib/theorem_gui_li_zeng_bridge_engine.py",
    ROOT / "compute/tests/test_literature_cross_check.py",
    ROOT / "compute/tests/test_kappa_stratification_G.py",
    VOL2 / "compute/lib/holographic_ht_engine.py",
    VOL2 / "compute/lib/bulk_boundary_duality_engine.py",
    VOL2 / "compute/lib/modular_obstruction_engine.py",
    VOL2 / "compute/lib/ym_synthesis_engine.py",
    VOL3 / "compute/lib/e1_koszul_three_families.py",
    VOL3 / "compute/lib/e2_koszul_heisenberg.py",
    VOL3 / "compute/lib/drinfeld_center_heisenberg_bulk.py",
    VOL3 / "compute/lib/swiss_cheese_cy3_e1.py",
    VOL3 / "compute/lib/three_d_n2_cy3_engine.py",
    VOL3 / "compute/lib/mirror_e1_koszul_engine.py",
    VOL3 / "compute/lib/string_field_theory_e1_cy3.py",
    VOL3 / "compute/tests/test_string_field_theory_e1_cy3.py",
    VOL3 / "compute/tests/test_hyperkahler_anchored_fixed_point.py",
]


FORBIDDEN = [
    "H_k^! = Sym^ch(V*)",
    "H_k^! = Sym^ch(V^*)",
    "H_1^! = Sym^ch(V*)",
    "H_1^! = Sym^ch(V^*)",
    "H_1^! = H_1",
    "H_1^! = H_{-1}",
    "H_k^! = H_{-k}",
    "rank-1 Heisenberg is its own Koszul dual",
    "K_H1 = 2",
]


def existing_surfaces() -> list[Path]:
    paths = [path for path in SURFACES if path.exists()]
    if not paths:
        pytest.skip("No Heisenberg curved-dual surfaces are present.")
    return paths


@pytest.mark.parametrize("path", existing_surfaces(), ids=lambda path: path.name)
def test_heisenberg_dual_surfaces_do_not_reintroduce_uncurved_object(path: Path):
    text = path.read_text()
    for phrase in FORBIDDEN:
        assert phrase not in text


def test_cross_volume_surfaces_name_curved_branch_where_present():
    text = "\n".join(path.read_text() for path in existing_surfaces())
    assert "curved Sym^ch(V*[1])" in text
    assert "curved second-kind Sym^ch(V*[1])" in text

    string_field = VOL3 / "compute/lib/string_field_theory_e1_cy3.py"
    if string_field.exists():
        sf_text = string_field.read_text()
        assert "is_self_dual=False" in sf_text
        assert "H_1 is not E_1 Koszul self-dual" in sf_text

    hyper = VOL3 / "compute/tests/test_hyperkahler_anchored_fixed_point.py"
    if hyper.exists():
        hyper_text = hyper.read_text()
        assert "K_H1 = 0" in hyper_text
        assert "kappa_H1_dual = -1" in hyper_text
