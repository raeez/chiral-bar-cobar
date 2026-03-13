"""Standard W_infinity dual-candidate package for the MC4 frontier.

This module packages the finite-stage data that feed the standard
completed dual candidate

    lim_N barB(W_N)

from the principal finite-type W_N tower. It does not construct the
missing H-level/factorization target. Instead it records the exact
finite packet constraints that, together with a compatible quotient
system, would promote that completed bar object to the candidate dual
object singled out by the manuscript's MC4 reduction.
"""

from __future__ import annotations

from typing import Dict, Tuple

from sympy import Rational, Symbol, simplify

from compute.lib.w4_ds_ope_extraction import (
    c334_squared_formula,
    c343_formula,
    c343_sign_relative_to_c334,
    c344_formula,
    c444_squared_formula,
)
from compute.lib.w4_stage4_coefficients import (
    incremental_higher_spin_channels,
    incremental_higher_spin_nonsingleton_target_decomposition,
    incremental_higher_spin_singleton_blocks,
    seed_set,
    seed_set_size,
    stage3_ds_coefficients,
    stage3_nonzero_count,
    stage3_vanishing_count,
    stage4_exact_identity_packet,
    stage4_residual_higher_spin_channels,
    stage4_virasoro_target_channels,
    stage4_virasoro_target_identities,
)


Channel = Tuple[int, int, int, int]


def completed_bar_candidate_descriptor() -> Dict[str, object]:
    """Standard completed M-level candidate singled out by the MC4 tower."""
    return {
        "kind": "inverse_limit_bar",
        "formula": "varprojlim_N barB(W_N)",
        "tower": "principal finite-type W_N stages",
        "construction_steps": (
            "construct a principal-stage compatible H-level or factorization target",
            "prove the finite packet identities on I_N",
            "apply inverse-limit bar-cobar comparison",
        ),
    }


def stage3_dual_constraint_report() -> Dict[str, object]:
    """Resolved stage-3 packet coming from the explicit W_3 OPE."""
    coefficients = stage3_ds_coefficients()
    nonzero = tuple(channel for channel, value in coefficients.items() if value != 0)
    vanishing = tuple(channel for channel, value in coefficients.items() if value == 0)
    return {
        "stage": 3,
        "seed_packet": tuple(seed_set(3)),
        "coefficients": coefficients,
        "nonzero_channels": nonzero,
        "vanishing_channels": vanishing,
        "status": "resolved_from_explicit_W3_OPE",
    }


def stage4_higher_spin_constraint_map(c=None) -> Dict[Channel, Dict[str, object]]:
    """DS-side higher-spin constraints on the exact stage-4 packet."""
    if c is None:
        c = Symbol("c")
    return {
        (3, 3, 4, 2): {
            "kind": "square_class",
            "expression": c334_squared_formula(c),
            "label": "c_334_squared",
        },
        (4, 4, 4, 4): {
            "kind": "square_class",
            "expression": c444_squared_formula(c),
            "label": "c_444_squared",
        },
        (3, 4, 3, 4): {
            "kind": "dependent_square_class",
            "expression": c343_formula(c),
            "depends_on": (3, 3, 4, 2),
            "sign_ratio_to_c334": c343_sign_relative_to_c334(),
        },
        (3, 4, 4, 3): {
            "kind": "dependent_square_class",
            "expression": c344_formula(c),
            "depends_on": (3, 3, 4, 2),
        },
    }


def stage4_virasoro_constraint_map() -> Dict[Channel, Dict[str, object]]:
    """Exact Virasoro-target identities inside the stage-4 packet."""
    return {
        channel: {
            "kind": "exact_value",
            "expression": value,
        }
        for channel, value in stage4_virasoro_target_identities().items()
    }


def stage4_dual_constraint_report(c=None) -> Dict[str, object]:
    """Exact stage-4 packet with higher-spin formulas and Virasoro values."""
    higher_spin = stage4_higher_spin_constraint_map(c)
    virasoro = stage4_virasoro_constraint_map()
    constraints = dict(higher_spin)
    constraints.update(virasoro)
    return {
        "stage": 4,
        "exact_identity_packet": tuple(stage4_exact_identity_packet()),
        "higher_spin_channels": tuple(stage4_residual_higher_spin_channels()),
        "virasoro_target_channels": tuple(stage4_virasoro_target_channels()),
        "higher_spin_constraints": higher_spin,
        "virasoro_constraints": virasoro,
        "constraints": constraints,
        "status": "DS-side explicit; bar-side residue identities remain to be matched",
    }


def stage4_residue_symbol_map() -> Dict[Channel, Dict[str, object]]:
    """Symbolic residue-side variables for the exact stage-4 packet.

    The higher-spin channels are recorded as square-class variables, since
    the DS-side target is presently packaged in that signless form.
    The Virasoro-target channels are exact value variables.
    """
    return {
        (3, 3, 4, 2): {
            "kind": "residue_square_variable",
            "expression": Symbol("R_334_sq"),
        },
        (4, 4, 4, 4): {
            "kind": "residue_square_variable",
            "expression": Symbol("R_444_sq"),
        },
        (3, 4, 3, 4): {
            "kind": "residue_square_variable",
            "expression": Symbol("R_343_sq"),
        },
        (3, 4, 4, 3): {
            "kind": "residue_square_variable",
            "expression": Symbol("R_344_sq"),
        },
        (4, 4, 2, 6): {
            "kind": "residue_value_variable",
            "expression": Symbol("R_442"),
        },
        (3, 4, 2, 5): {
            "kind": "residue_value_variable",
            "expression": Symbol("R_342"),
        },
    }


def stage4_dual_defect_map(c=None) -> Dict[Channel, Dict[str, object]]:
    """Defect family for the exact stage-4 packet.

    Vanishing of these six defects is the first fully explicit stage-4
    residue-vs-DS goal package on the standard W_infinity side.
    """
    residue = stage4_residue_symbol_map()
    target = stage4_dual_constraint_report(c)["constraints"]
    defects = {}
    for channel in stage4_exact_identity_packet():
        defects[channel] = {
            "kind": "defect",
            "residue_expression": residue[channel]["expression"],
            "target_expression": target[channel]["expression"],
            "defect_expression": residue[channel]["expression"] - target[channel]["expression"],
        }
    return defects


def stage4_dual_goal_report(c=None) -> Dict[str, object]:
    """Exact stage-4 vanishing goal for the standard W_infinity packet."""
    return {
        "stage": 4,
        "exact_identity_packet": tuple(stage4_exact_identity_packet()),
        "residue_symbols": stage4_residue_symbol_map(),
        "target_constraints": stage4_dual_constraint_report(c)["constraints"],
        "defects": stage4_dual_defect_map(c),
        "goal": "vanish all six stage-4 defects",
    }


def stage4_primitive_square_class_report(c=None) -> Dict[str, object]:
    """Principal stage-4 higher-spin packet reduced to primitive square classes."""
    if c is None:
        c = Symbol("c")
    higher_spin = stage4_higher_spin_constraint_map(c)
    primitive = {
        (3, 3, 4, 2): higher_spin[(3, 3, 4, 2)],
        (4, 4, 4, 4): higher_spin[(4, 4, 4, 4)],
    }
    forced = {
        (3, 4, 3, 4): {
            **higher_spin[(3, 4, 3, 4)],
            "forced_by": (3, 3, 4, 2),
            "ratio_to_primitive": Rational(9, 16),
        },
        (3, 4, 4, 3): {
            **higher_spin[(3, 4, 4, 3)],
            "forced_by": (3, 3, 4, 2),
            "ratio_to_primitive": Rational(5, 7),
        },
    }
    return {
        "stage": 4,
        "primitive_square_channels": primitive,
        "forced_mixed_square_channels": forced,
        "primitive_count": len(primitive),
        "forced_count": len(forced),
        "status": "principal DS higher-spin packet determined at square-class level by two primitive channels",
    }


def stage4_pairing_reduction_report() -> Dict[str, object]:
    """Residue-side stage-4 reduction under a visible invariant pairing package."""
    return {
        "assumption": "stage-4 Ward-normalized visible invariant pairing",
        "forced_channel": (3, 4, 3, 4),
        "forced_by": (3, 3, 4, 2),
        "sign_ratio": Rational(-3, 4),
        "square_ratio": Rational(9, 16),
        "independent_higher_spin_channels": (
            (3, 3, 4, 2),
            (4, 4, 4, 4),
            (3, 4, 4, 3),
        ),
        "status": "four-channel Ward-normalized residue packet contracts to three higher-spin channels under visible pairing invariance",
    }


def stage4_target_packet_at_level(k) -> Dict[Channel, object]:
    """Exact DS-side stage-4 target packet evaluated at a specific level."""
    from compute.lib.w4_stage4_coefficients import w4_central_charge

    c_k = w4_central_charge(k)
    constraints = stage4_dual_constraint_report(c_k)["constraints"]
    return {
        channel: simplify(data["expression"])
        for channel, data in constraints.items()
    }


def evaluate_stage4_dual_defects_at_level(
    k,
    residue_data: Dict[Channel, object] | None = None,
) -> Dict[Channel, object]:
    """Evaluate the stage-4 defect family at a specific level.

    If ``residue_data`` is omitted, the returned expressions remain symbolic in
    the residue-side variables.  If residue data is supplied, it must assign a
    value to every channel in the exact stage-4 packet.
    """
    target_packet = stage4_target_packet_at_level(k)
    if residue_data is None:
        residue_data = {
            channel: data["expression"]
            for channel, data in stage4_residue_symbol_map().items()
        }

    return {
        channel: simplify(residue_data[channel] - target_packet[channel])
        for channel in stage4_exact_identity_packet()
    }


def stage4_defect_vanishing_report(
    k,
    residue_data: Dict[Channel, object],
) -> Dict[str, object]:
    """Channelwise vanishing report for the exact stage-4 defect family."""
    defects = evaluate_stage4_dual_defects_at_level(k, residue_data)
    return {
        "level": k,
        "defects": defects,
        "channel_vanishing": {
            channel: simplify(value) == 0 for channel, value in defects.items()
        },
        "all_vanish": all(simplify(value) == 0 for value in defects.values()),
    }


def stage5_dual_frontier_report() -> Dict[str, object]:
    """First higher-spin frontier beyond the exact stage-4 packet."""
    entry_singletons = incremental_higher_spin_singleton_blocks(5)
    transport_targets = incremental_higher_spin_nonsingleton_target_decomposition(5)
    attack_order = tuple(
        target
        for target, _ in sorted(
            transport_targets.items(),
            key=lambda item: min(channel[3] for channel in item[1]),
        )
    )
    return {
        "stage": 5,
        "higher_spin_channels": tuple(incremental_higher_spin_channels(5)),
        "entry_singletons": entry_singletons,
        "transport_target_blocks": transport_targets,
        "transport_attack_order": attack_order,
    }


def standard_winfinity_dual_candidate_report(c=None) -> Dict[str, object]:
    """Machine-readable summary of the standard W_infinity dual candidate."""
    return {
        "completed_bar_candidate": completed_bar_candidate_descriptor(),
        "stage3": stage3_dual_constraint_report(),
        "stage4": stage4_dual_constraint_report(c),
        "stage4_goal": stage4_dual_goal_report(c),
        "stage4_square_class": stage4_primitive_square_class_report(c),
        "stage4_pairing_reduction": stage4_pairing_reduction_report(),
        "stage4_level_contract": "use stage4_target_packet_at_level / evaluate_stage4_dual_defects_at_level",
        "stage5_frontier": stage5_dual_frontier_report(),
    }


def verify_standard_winfinity_dual_candidate(c=None) -> Dict[str, bool]:
    """Internal consistency checks for the standard dual-candidate package."""
    if c is None:
        c = Symbol("c")

    report = standard_winfinity_dual_candidate_report(c)
    stage3 = report["stage3"]
    stage4 = report["stage4"]
    stage4_goal = report["stage4_goal"]
    stage4_square = report["stage4_square_class"]
    stage4_pairing = report["stage4_pairing_reduction"]
    stage5 = report["stage5_frontier"]
    descriptor = report["completed_bar_candidate"]

    higher_spin = stage4["higher_spin_constraints"]
    virasoro = stage4["virasoro_constraints"]
    constraints = stage4["constraints"]
    defects = stage4_goal["defects"]

    return {
        "descriptor has three construction steps": len(descriptor["construction_steps"]) == 3,
        "stage-3 seed packet size": len(stage3["seed_packet"]) == seed_set_size(3),
        "stage-3 nonzero count": len(stage3["nonzero_channels"]) == stage3_nonzero_count(),
        "stage-3 vanishing count": len(stage3["vanishing_channels"]) == stage3_vanishing_count(),
        "stage-4 constraints cover exact packet": set(constraints) == set(stage4["exact_identity_packet"]),
        "stage-4 defects cover exact packet": set(defects) == set(stage4_goal["exact_identity_packet"]),
        "stage-4 higher-spin coverage": set(higher_spin) == set(stage4["higher_spin_channels"]),
        "stage-4 Virasoro coverage": set(virasoro) == set(stage4["virasoro_target_channels"]),
        "stage-4 primitive square-class count": stage4_square["primitive_count"] == 2,
        "stage-4 forced square-class count": stage4_square["forced_count"] == 2,
        "stage-4 pairing-reduced independent channel count": (
            len(stage4_pairing["independent_higher_spin_channels"]) == 3
        ),
        "stage-4 higher-spin defects are signless": all(
            stage4_goal["residue_symbols"][channel]["kind"] == "residue_square_variable"
            for channel in stage4["higher_spin_channels"]
        ),
        "stage-4 Virasoro defects are exact-value variables": all(
            stage4_goal["residue_symbols"][channel]["kind"] == "residue_value_variable"
            for channel in stage4["virasoro_target_channels"]
        ),
        "stage-4 mixed W3 forced by c334": (
            stage4_square["forced_mixed_square_channels"][(3, 4, 3, 4)]["forced_by"]
            == (3, 3, 4, 2)
        ),
        "stage-4 mixed W4 forced by c334": (
            stage4_square["forced_mixed_square_channels"][(3, 4, 4, 3)]["forced_by"]
            == (3, 3, 4, 2)
        ),
        "stage-4 pairing reduction sign ratio": (
            stage4_pairing["sign_ratio"] == Rational(-3, 4)
        ),
        "stage-4 pairing reduction square ratio": (
            stage4_pairing["square_ratio"] == Rational(9, 16)
        ),
        "stage-4 mixed W3 square relation": simplify(
            higher_spin[(3, 4, 3, 4)]["expression"]
            / higher_spin[(3, 3, 4, 2)]["expression"]
        ) == Rational(9, 16),
        "stage-4 mixed W4 square relation": simplify(
            higher_spin[(3, 4, 4, 3)]["expression"]
            / higher_spin[(3, 3, 4, 2)]["expression"]
        ) == Rational(5, 7),
        "stage-4 mixed sign relation": higher_spin[(3, 4, 3, 4)]["sign_ratio_to_c334"]
        == c343_sign_relative_to_c334(),
        "stage-4 self-consistency at level 1": stage4_defect_vanishing_report(
            1, stage4_target_packet_at_level(1)
        )["all_vanish"],
        "stage-5 first higher-spin frontier exists": len(stage5["higher_spin_channels"]) > 0,
        "stage-5 transport attack order": stage5["transport_attack_order"] == (5, 4, 3),
    }
