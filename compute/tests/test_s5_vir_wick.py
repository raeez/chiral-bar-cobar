r"""Scope checks for the historical ``s5_vir_wick`` entry point."""

from __future__ import annotations

import pytest
import sympy as sp

from compute.lib.s5_vir_wick import (
    ResidueProjectionRequired,
    g5_connected_ward_correlator,
    s5_virasoro_wick,
)
from compute.lib.virasoro_ward_correlators import standard_points


def test_g5_entry_point_returns_the_connected_ward_correlator():
    points = standard_points(5)
    expression = g5_connected_ward_correlator(1)
    value = sp.cancel(expression.subs(dict(zip(points, range(5)))))
    assert value == sp.Rational(775, 5184)


def test_g5_retains_configuration_space_dependence():
    points = standard_points(5)
    expression = g5_connected_ward_correlator(1)
    first = sp.cancel(expression.subs(dict(zip(points, (0, 1, 2, 3, 4)))))
    second = sp.cancel(expression.subs(dict(zip(points, (0, 1, 3, 6, 10)))))
    assert first != second


def test_scalar_entry_point_requests_residue_data():
    with pytest.raises(ResidueProjectionRequired) as error:
        s5_virasoro_wick(1)
    assert "H_res(Vir_c; X)" in str(error.value)
