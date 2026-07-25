"""Guard the distinction between OPE seeds and shadow asymptotics.

An OPE coefficient such as the ``2T`` term in ``TT`` or ``WW`` supplies
finite local data.  An exponential base for a full shadow series requires a
constructed residue bar complex, a recursion theorem, convergence, and a
scalar projection.  This test keeps that implication open.
"""

import sympy as sp
import pytest

from compute.lib.shadow_tower_extended_families import (
    OpenShadowProjectionError,
    bp_ope_packet,
    bp_t_line_status,
    s3_bp_tline,
    s3_w3_tline,
    s4_w3_tline,
    w3_ope_packet,
    w3_t_line_status,
)


def test_w3_local_ope_seed_is_exact():
    c = sp.Symbol("c")
    assert w3_ope_packet(c)["WW"][3]["T"] == 2
    assert w3_t_line_status(c)["scalar_shadow"].status == "open"


def test_bp_local_ope_packet_is_exact():
    k = sp.Symbol("k")
    packet = bp_ope_packet(k)
    assert packet["G+G-"][0]["T"] == -(k + 3)
    assert bp_t_line_status(k)["scalar_quartic"].status == "open"


@pytest.mark.parametrize("function", [s3_w3_tline, s4_w3_tline, s3_bp_tline])
def test_historical_shadow_seed_names_require_projection_theorem(function):
    with pytest.raises(OpenShadowProjectionError, match="H_bar"):
        function(sp.Symbol("x"))
