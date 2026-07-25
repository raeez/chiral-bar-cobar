r"""Cross-agreement between two independent bar/CE homology implementations.

Two harnesses in this repository compute Chevalley-Eilenberg homology by
unrelated routes:

  compute/lib/witt_pentagonal_rigidity.py
      exact Fraction arithmetic, sparse dict-of-dict elimination, cochain
      basis = increasing tuples, differential defined as a graded derivation
      with the Koszul sign (-1)^p and d^2 = 0 asserted per space.

  compute/lib/reconstruction_bar_models.py
      sympy Rational dense matrices, structure constants supplied directly,
      ranks via sympy; also computes normalized-bar windows for the quantum
      and Jordan planes.

They share exactly one claim: the CE homology of sl_2.  Agreement is a genuine
cross-validation because neither implementation shares code, basis convention,
sign convention, or linear-algebra backend with the other.

The remaining tests pin the reconstruction harness's own published outputs so
that a regression in it is caught here rather than in the manuscript.
"""

from __future__ import annotations

import pytest

from compute.lib.witt_pentagonal_rigidity import sl2 as witt_sl2
from compute.lib.reconstruction_bar_models import (
    hall_a2,
    homology_window,
    jordan_product,
    qplane_product,
    sl2_ce,
    stable_trace_jacobi_sample,
)


def test_sl2_ce_homology_agrees_across_both_harnesses():
    """The one shared claim: H^*(sl_2) = 1,0,0,1."""
    g = witt_sl2()
    mine = [g.cohomology(n, 0)[0] for n in range(4)]

    theirs_raw = sl2_ce()
    dims = theirs_raw["homology_dimensions"]
    theirs = [int(dims[f"H{n}"]) for n in range(4)]

    assert mine == [1, 0, 0, 1], "Whitehead: H^*(sl_2) = Lambda(c_3)"
    assert theirs == mine, (
        "independent implementations disagree on H^*(sl_2): "
        f"witt_pentagonal_rigidity={mine} reconstruction_bar_models={theirs}"
    )


@pytest.mark.parametrize(
    "product,label",
    [(qplane_product, "quantum plane q=2"), (jordan_product, "Jordan plane")],
)
def test_plane_bar_windows_have_koszul_shape(product, label):
    """Both planes are Koszul: homology 2 in (w=1,deg=1), 1 in (w=2,deg=2), else 0.

    This is the Poincare polynomial 1 + 2t + t^2 restricted to the computed
    window, and it is the finite-window evidence behind the quantum-plane and
    Jordan-plane resolutions.
    """
    records = homology_window(5, product)["records"]
    got = {(r["weight"], r["homological_degree"]): r["homology_dim"] for r in records}

    assert got[(1, 1)] == 2, f"{label}: two generators in weight 1"
    assert got[(2, 2)] == 1, f"{label}: one quadratic relation class"
    for (w, d), h in got.items():
        if (w, d) not in {(1, 1), (2, 2)}:
            assert h == 0, f"{label}: unexpected class at weight {w} degree {d}"


def test_plane_chain_dims_are_not_homology_dims():
    """The audit's point, made numerically: chain counts differ from homology."""
    records = homology_window(5, qplane_product)["records"]
    chain = sum(r["chain_dim"] for r in records)
    homology = sum(r["homology_dim"] for r in records)
    assert chain > homology
    assert (chain, homology) == (sum(r["chain_dim"] for r in records), 3)


def test_a2_hall_serre_relations_hold():
    result = hall_a2(q=2)
    assert all(bool(v) for k, v in result.items() if isinstance(v, bool)), result


def test_stable_trace_bracket_satisfies_jacobi():
    result = stable_trace_jacobi_sample()
    assert all(bool(v) for k, v in result.items() if isinstance(v, bool)), result
