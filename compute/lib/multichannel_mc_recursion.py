r"""Rectified audit harness for naive multichannel MC recursions on W_3.

This file preserves only the exact channel data that survive local checks and
records two failed exploratory ansaetze:

1. a direct shadow-tensor lift of the genus-(1,2) recursion;
2. a naive genus-2 boundary graph sum built from that lift.

Both fail benchmark tests:

- both exploratory genus-(1,2) multichannel lifts fail the known Virasoro
  formula `ell_2^{(1)} = c/24 - 4` once the full channel sum is kept;
- the naive genus-2 graph sum fails the proved single-channel identity
  `F_2 = kappa * lambda_2^{FP}` and therefore cannot be used as evidence for
  multi-generator universality.

What remains trustworthy here:

- exact per-channel curvatures `kappa_T = c/2`, `kappa_W = c/3`;
- exact cubic/quartic W_3 channel tensors used in the bookkeeping lane;
- exact sphere three-point data `C_{TTT} = C_{TWW} = c`;
- explicit benchmark diagnostics against the single-channel formulas.

This module is an audit surface, not a proof surface for
`op:multi-generator-universality`.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product as cartprod
from typing import Dict, Iterable, Tuple

from compute.lib.stable_graph_enumeration import (
    _lambda_fp_exact,
    genus1_stable_graphs_n2,
)


# ============================================================================
# Universal graph-level constants
# ============================================================================

CHANNELS: Tuple[str, str] = ("T", "W")

HODGE = {
    "B_lollipop": Fraction(1, 24),
    "C_sunset": Fraction(0),
    "D_dumbbell": Fraction(-1, 576),
    "E_bridge_loop": Fraction(-1, 24),
    "F_theta": Fraction(1),
    "G_fig8_bridge": Fraction(1),
}

AUT = {
    "B_lollipop": 2,
    "C_sunset": 8,
    "D_dumbbell": 2,
    "E_bridge_loop": 2,
    "F_theta": 12,
    "G_fig8_bridge": 8,
}


# ============================================================================
# Exact verified bookkeeping data
# ============================================================================

def lambda_fp(g: int) -> Fraction:
    """Exact Faber-Pandharipande number lambda_g^FP."""
    if g < 1:
        raise ValueError(f"lambda_fp requires g >= 1, got {g}")
    return _lambda_fp_exact(g)


def kappa(channel: str, c: Fraction) -> Fraction:
    """Per-channel modular characteristic for W_3."""
    if channel == "T":
        return c / 2
    if channel == "W":
        return c / 3
    raise ValueError(f"Unknown channel: {channel}")


def S3(s1: str, s2: str, s3: str, c: Fraction) -> Fraction:
    """Exact cubic W_3 shadow tensor used in the bookkeeping lane."""
    del c  # The normalized cubic tensor is c-independent in this convention.
    labels = sorted((s1, s2, s3))
    w_count = labels.count("W")
    if w_count % 2 == 1:
        return Fraction(0)
    if labels == ["T", "T", "T"]:
        return Fraction(2)
    if labels == ["T", "W", "W"]:
        return Fraction(1)
    return Fraction(0)


def S4(s1: str, s2: str, s3: str, s4: str, c: Fraction) -> Fraction:
    """Exact quartic W_3 shadow tensor from the corrected bookkeeping lane."""
    labels = sorted((s1, s2, s3, s4))
    w_count = labels.count("W")
    if w_count % 2 == 1:
        return Fraction(0)

    denom = c * (5 * c + 22)
    if w_count == 0:
        return Fraction(10, 1) / denom
    if w_count == 2:
        return Fraction(160, 1) / (denom * (5 * c + 22))
    if w_count == 4:
        return Fraction(2560, 1) / (denom * (5 * c + 22) ** 2)
    return Fraction(0)


def C3_func(i: str, j: str, k: str, c: Fraction) -> Fraction:
    """Exact sphere three-point constants for the W_3 bookkeeping model."""
    w_count = sum(1 for x in (i, j, k) if x == "W")
    if w_count % 2 == 1:
        return Fraction(0)
    labels = sorted((i, j, k))
    if labels == ["T", "T", "T"]:
        return c
    if labels == ["T", "W", "W"]:
        return c
    return Fraction(0)


def virasoro_ell2_reference(c: Fraction) -> Fraction:
    """Known single-channel benchmark: ell_2^{(1)} = S_3*kappa/24 - S_3^2."""
    return c / 24 - 4


# ============================================================================
# Genus-(1,2) audit: two exploratory lifts and the benchmark
# ============================================================================

def ell2_genus1_multichannel(channel: str, c: Fraction) -> Fraction:
    r"""Rejected shadow-tensor lift of the `(g,n)=(1,2)` recursion.

    This is kept only as an audit witness.  It was the first direct attempt to
    lift the single-channel relation by inserting the normalized shadow tensor
    `S_3` together with explicit channel propagators.  It does not recover the
    Virasoro benchmark and should not be used downstream.
    """
    sep = sum(-S3(channel, channel, sp, c) / 24 for sp in CHANNELS)

    pf = Fraction(0)
    for s1, s2 in cartprod(CHANNELS, repeat=2):
        S3_val = S3(channel, s1, s2, c)
        if S3_val != 0:
            pf += S3_val**2 / (2 * kappa(s1, c) * kappa(s2, c))

    return -(sep + pf)


def ell2_genus1_v2(channel: str, c: Fraction) -> Fraction:
    r"""Alternative three-point lift of the `(g,n)=(1,2)` recursion.

    This lift uses the exact sphere three-point constants `C_{ijk}` rather than
    the normalized shadow tensor.  Its pure `TTT` restriction reproduces the
    single-channel Virasoro value, but the honest multichannel sum keeps the
    `TWW` term and therefore still fails the benchmark.
    """
    sep = sum(C3_func(channel, channel, sp, c) / 24 for sp in CHANNELS)

    pf = Fraction(0)
    for s1, s2 in cartprod(CHANNELS, repeat=2):
        C_val = C3_func(channel, s1, s2, c)
        if C_val != 0:
            pf += C_val**2 / (kappa(s1, c) * kappa(s2, c))

    return sep - pf


def verify_ell2_single_channel(c: Fraction) -> Dict[str, Fraction | bool]:
    """Benchmark both exploratory multichannel lifts against Virasoro."""
    reference = virasoro_ell2_reference(c)
    shadow_tensor = ell2_genus1_multichannel("T", c)
    cohft_three_point = ell2_genus1_v2("T", c)
    return {
        "reference": reference,
        "shadow_tensor_ansatz": shadow_tensor,
        "cohft_three_point_ansatz": cohft_three_point,
        "shadow_tensor_match": shadow_tensor == reference,
        "cohft_match": cohft_three_point == reference,
    }


def genus1_boundary_graph_audit() -> Dict[str, object]:
    """Audit the stable graph surface for `(g,n) = (1,2)`.

    The authoritative enumeration in `stable_graph_enumeration.py` shows five
    stable graphs.  In particular, both codimension-2 planted-forest types are
    present:

    - the double bridge;
    - the self-loop-plus-bridge graph.

    The latter was omitted during the initial scratch derivation and is the
    first topological failure mode we want the module to remember explicitly.
    """
    graph_types = []
    has_self_loop_plus_bridge = False
    has_double_bridge = False

    for graph in genus1_stable_graphs_n2():
        loops = sum(1 for a, b in graph.edges if a == b)
        bridges = sum(1 for a, b in graph.edges if a != b)

        if graph.vertex_genera == (1,) and not graph.edges:
            graph_type = "smooth"
        elif graph.num_vertices == 1 and loops == 1:
            graph_type = "self_node"
        elif sorted(graph.vertex_genera) == [0, 1] and bridges == 1:
            graph_type = "separating"
        elif loops == 1 and bridges == 1:
            graph_type = "self_loop_plus_bridge"
            has_self_loop_plus_bridge = True
        elif loops == 0 and bridges == 2:
            graph_type = "double_bridge"
            has_double_bridge = True
        else:
            graph_type = "other"

        graph_types.append(
            {
                "type": graph_type,
                "genera": graph.vertex_genera,
                "edges": graph.edges,
                "legs": graph.legs,
                "aut": graph.automorphism_order(),
            }
        )

    return {
        "graph_count": len(graph_types),
        "has_self_loop_plus_bridge": has_self_loop_plus_bridge,
        "has_double_bridge": has_double_bridge,
        "graph_types": graph_types,
    }


# ============================================================================
# Genus-2 audit: explicit failure of the naive graph-sum convention
# ============================================================================

def naive_genus2_single_channel(c: Fraction) -> Dict[str, Fraction | bool]:
    """Audit the naive genus-2 graph-sum convention on the Virasoro lane."""
    kap = c / 2
    alpha = Fraction(2)
    ell2 = virasoro_ell2_reference(c)

    B = ell2 * HODGE["B_lollipop"] / AUT["B_lollipop"]
    D = kap**2 * HODGE["D_dumbbell"] / AUT["D_dumbbell"]
    pf = alpha * (10 * alpha - kap) / 48
    boundary = B + D + pf
    F2_naive = -boundary
    expected = kap * lambda_fp(2)

    return {
        "kappa": kap,
        "ell2": ell2,
        "B": B,
        "D": D,
        "pf": pf,
        "boundary": boundary,
        "F2_naive": F2_naive,
        "expected": expected,
        "matches": F2_naive == expected,
    }


def genus2_multichannel(c: Fraction) -> Dict[str, Fraction | bool]:
    r"""Rejected naive genus-2 W_3 graph sum.

    The returned value is intentionally diagnostic: it records what the naive
    multichannel boundary formula produces and whether it matches the known
    genus-2 scalar benchmark.  The answer is expected to be `False`.
    """
    single_channel_audit = naive_genus2_single_channel(c)

    B_multi = sum(
        ell2_genus1_v2(channel, c) * HODGE["B_lollipop"] / AUT["B_lollipop"]
        for channel in CHANNELS
    )

    D_multi = sum(
        kappa(channel, c) ** 2 * HODGE["D_dumbbell"] / AUT["D_dumbbell"]
        for channel in CHANNELS
    )

    E_multi = Fraction(0)
    for bridge_channel, loop_channel in cartprod(CHANNELS, repeat=2):
        vertex_weight = S3(loop_channel, loop_channel, bridge_channel, c)
        vertex_weight *= kappa(bridge_channel, c)
        E_multi += vertex_weight * HODGE["E_bridge_loop"] / AUT["E_bridge_loop"]

    F_multi = Fraction(0)
    for channels in cartprod(CHANNELS, repeat=3):
        F_multi += S3(*channels, c) ** 2 * HODGE["F_theta"] / AUT["F_theta"]

    G_multi = Fraction(0)
    for s1, s2, s3 in cartprod(CHANNELS, repeat=3):
        vertex_weight = S3(s1, s1, s3, c) * S3(s2, s2, s3, c)
        G_multi += vertex_weight * HODGE["G_fig8_bridge"] / AUT["G_fig8_bridge"]

    pf_multi = E_multi + F_multi + G_multi
    boundary_multi = B_multi + D_multi + pf_multi
    F2_multi = -boundary_multi
    expected = sum(kappa(channel, c) for channel in CHANNELS) * lambda_fp(2)

    return {
        "c": c,
        "kappa_T": kappa("T", c),
        "kappa_W": kappa("W", c),
        "kappa_total": sum(kappa(channel, c) for channel in CHANNELS),
        "ell2_T": ell2_genus1_v2("T", c),
        "ell2_W": ell2_genus1_v2("W", c),
        "B_multi": B_multi,
        "D_multi": D_multi,
        "E_multi": E_multi,
        "F_multi": F_multi,
        "G_multi": G_multi,
        "pf_multi": pf_multi,
        "boundary_multi": boundary_multi,
        "F2_multi": F2_multi,
        "F2_expected": expected,
        "single_channel_match": bool(single_channel_audit["matches"]),
        "universality_holds": F2_multi == expected,
    }


# ============================================================================
# CLI helper
# ============================================================================

def run_rectification_audit(
    c_values: Iterable[Fraction] = (
        Fraction(6),
        Fraction(10),
        Fraction(26),
        Fraction(50),
    ),
) -> None:
    """Print the benchmark failures that justify the rectification."""
    print("=" * 72)
    print("RECTIFICATION AUDIT: naive multichannel MC recursion on W_3")
    print("=" * 72)

    graph_audit = genus1_boundary_graph_audit()
    print(
        f"(g,n)=(1,2) stable-graph audit: {graph_audit['graph_count']} graphs; "
        f"double-bridge={graph_audit['has_double_bridge']}; "
        f"self-loop+bridge={graph_audit['has_self_loop_plus_bridge']}"
    )

    for c in c_values:
        ell2_audit = verify_ell2_single_channel(c)
        genus2_audit = genus2_multichannel(c)
        single_channel = naive_genus2_single_channel(c)

        print(f"\nc = {c}")
        print(
            "  ell_2 benchmark:"
            f" reference={ell2_audit['reference']},"
            f" shadow-tensor={ell2_audit['shadow_tensor_ansatz']}"
            f" (match={ell2_audit['shadow_tensor_match']}),"
            f" CohFT={ell2_audit['cohft_three_point_ansatz']}"
            f" (match={ell2_audit['cohft_match']})"
        )
        print(
            "  naive genus-2 single-channel:"
            f" F2={single_channel['F2_naive']},"
            f" expected={single_channel['expected']},"
            f" match={single_channel['matches']}"
        )
        print(
            "  naive genus-2 multichannel:"
            f" F2={genus2_audit['F2_multi']},"
            f" expected={genus2_audit['F2_expected']},"
            f" universality={genus2_audit['universality_holds']}"
        )

    print("\nConclusion: preserve the exact channel data, reject the naive lifts.")


def run_decisive_test() -> None:
    """Backward-compatible alias for the rectified audit printer."""
    run_rectification_audit()


if __name__ == "__main__":
    run_rectification_audit()
