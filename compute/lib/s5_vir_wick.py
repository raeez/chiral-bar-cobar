r"""Compatibility surface for the proposed Virasoro ``S_5`` extraction.

The exact computation now lives in :mod:`virasoro_ward_correlators`.  It
constructs the coordinate-dependent connected five-point function from the
full Virasoro Ward identity.  A scalar ``S_5`` additionally uses
``H_res(Vir_c; X)`` and a normalized ordered Arnold/residue projection.
"""

from __future__ import annotations

from compute.lib.virasoro_ward_correlators import (
    CENTRAL_CHARGE,
    ResidueProjectionRequired,
    require_residue_projection,
    standard_points,
    virasoro_connected_correlator,
)


def g5_connected_ward_correlator(central_charge=CENTRAL_CHARGE):
    """Return ``G_5^conn(z_1,...,z_5)`` as an exact rational function."""

    points = standard_points(5)
    return virasoro_connected_correlator(points, central_charge)


def s5_virasoro_wick(_central_charge):
    """Request the residue datum that turns ``G_5^conn`` into a scalar."""

    require_residue_projection(5)


__all__ = [
    "ResidueProjectionRequired",
    "g5_connected_ward_correlator",
    "s5_virasoro_wick",
]
