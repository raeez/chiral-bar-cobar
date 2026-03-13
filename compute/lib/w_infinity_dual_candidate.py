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
    incremental_reduced_packet,
    incremental_virasoro_target_channels,
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


def stage4_primitive_transport_report(c=None) -> Dict[str, object]:
    """Stage-4 higher-spin matching reduced to a primitive-plus-transport square triple."""
    if c is None:
        c = Symbol("c")

    higher_spin = stage4_higher_spin_constraint_map(c)
    residue = stage4_residue_symbol_map()
    primitive = {
        (3, 3, 4, 2): higher_spin[(3, 3, 4, 2)],
        (4, 4, 4, 4): higher_spin[(4, 4, 4, 4)],
    }
    transport_channel = (3, 4, 4, 3)
    automatic_channel = (3, 4, 3, 4)

    return {
        "assumption": "stage-4 Ward-normalized visible invariant pairing",
        "independent_square_identity_channels": (
            (3, 3, 4, 2),
            (4, 4, 4, 4),
            transport_channel,
        ),
        "primitive_self_square_channels": primitive,
        "transport_square_channel": {
            "channel": transport_channel,
            **higher_spin[transport_channel],
            "kind": "transport_square_class",
            "ratio_to_c334": Rational(5, 7),
        },
        "automatic_square_channel": {
            "channel": automatic_channel,
            "forced_by_residue_channel": (3, 3, 4, 2),
            "residue_square_ratio": Rational(9, 16),
            "target_square_ratio": Rational(9, 16),
        },
        "square_identity_targets": {
            (3, 3, 4, 2): higher_spin[(3, 3, 4, 2)]["expression"],
            (4, 4, 4, 4): higher_spin[(4, 4, 4, 4)]["expression"],
            transport_channel: higher_spin[transport_channel]["expression"],
        },
        "next_transport_gap": {
            "channel": transport_channel,
            "relation_expression": simplify(
                residue[transport_channel]["expression"]
                - Rational(5, 7) * residue[(3, 3, 4, 2)]["expression"]
            ),
            "status": "not forced by the visible Ward plus pairing package alone",
        },
        "status": (
            "on the visible pairing locus, stage-4 higher-spin matching reduces "
            "at signless square-class level to two primitive self-couplings plus "
            "one mixed transport square"
        ),
    }


def stage4_borcherds_transport_report(c=None) -> Dict[str, object]:
    """Exact remaining stage-4 transport input on the visible pairing locus."""
    if c is None:
        c = Symbol("c")

    residue = stage4_residue_symbol_map()
    higher_spin = stage4_higher_spin_constraint_map(c)
    transport_channel = (3, 4, 4, 3)
    primitive_channel = (3, 3, 4, 2)

    return {
        "assumption": "stage-4 Ward-normalized visible invariant pairing",
        "relation_channel": transport_channel,
        "forced_by_residue_channel": primitive_channel,
        "relation_expression": simplify(
            residue[transport_channel]["expression"]
            - Rational(5, 7) * residue[primitive_channel]["expression"]
        ),
        "target_square_ratio": Rational(5, 7),
        "principal_transport_target": higher_spin[transport_channel]["expression"],
        "equivalent_closure_channels": (
            (3, 3, 4, 2),
            (4, 4, 4, 4),
        ),
        "status": (
            "this single relation is exactly the remaining stage-4 higher-spin "
            "input on the visible pairing locus; imposing it collapses the "
            "primitive-plus-transport triple to the principal two-primitive profile"
        ),
    }


def stage4_two_primitive_square_closure_report(c=None) -> Dict[str, object]:
    """Stage-4 two-primitive closure equivalent to visible Borcherds transport."""
    if c is None:
        c = Symbol("c")

    higher_spin = stage4_higher_spin_constraint_map(c)
    return {
        "assumption": (
            "stage-4 Ward-normalized visible invariant pairing plus visible "
            "top-pole Borcherds transport"
        ),
        "independent_square_identity_channels": (
            (3, 3, 4, 2),
            (4, 4, 4, 4),
        ),
        "equivalent_transport_relation_channel": (3, 4, 4, 3),
        "primitive_square_targets": {
            (3, 3, 4, 2): higher_spin[(3, 3, 4, 2)]["expression"],
            (4, 4, 4, 4): higher_spin[(4, 4, 4, 4)]["expression"],
        },
        "forced_transport_channel": {
            "channel": (3, 4, 4, 3),
            "forced_by_residue_channel": (3, 3, 4, 2),
            "square_ratio": Rational(5, 7),
        },
        "automatic_square_channel": {
            "channel": (3, 4, 3, 4),
            "forced_by_residue_channel": (3, 3, 4, 2),
            "square_ratio": Rational(9, 16),
        },
        "status": (
            "equivalently to the visible top-pole Borcherds transport relation, "
            "the visible pairing stage-4 higher-spin square frontier closes to the "
            "same two primitive self-coupling squares as the principal DS packet"
        ),
    }


def stage4_local_attack_order_report(c=None) -> Dict[str, object]:
    """Exact local stage-4 attack order on the standard W_infinity side."""
    if c is None:
        c = Symbol("c")

    return {
        "stage": 4,
        "step_1": {
            "kind": "virasoro_target_normalization",
            "report": {
                "channel": (4, 4, 2, 6),
                "equivalent_scalar_identity": "C^res_{4,4;2;0,6}(4)=2",
                "effect": "contracts the six-entry packet to the four higher-spin channels",
            },
        },
        "step_2": {
            "kind": "higher_spin_transport",
            "report": stage4_borcherds_transport_report(c),
            "effect": "collapses the primitive-plus-transport triple to the principal two-primitive square profile",
        },
        "status": (
            "after the exact six-entry stage-4 packet, the local frontier is first "
            "a one-scalar Ward-normalization problem and then, on the visible "
            "pairing locus, a one-relation higher-spin transport problem"
        ),
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
    """First reduced stage strictly downstream of the exact stage-4 packet."""
    entry_singletons = incremental_higher_spin_singleton_blocks(5)
    transport_targets = incremental_higher_spin_nonsingleton_target_decomposition(5)
    reduced_packet = tuple(incremental_reduced_packet(5))
    higher_spin_channels = tuple(incremental_higher_spin_channels(5))
    virasoro_target_channels = tuple(incremental_virasoro_target_channels(5))
    attack_order = tuple(
        target
        for target, _ in sorted(
            transport_targets.items(),
            key=lambda item: min(channel[3] for channel in item[1]),
        )
    )
    return {
        "stage": 5,
        "prerequisite_stage": 4,
        "prerequisite_goal": "vanish all six stage-4 defects",
        "prerequisite_exact_packet": tuple(stage4_exact_identity_packet()),
        "reduced_packet": reduced_packet,
        "reduced_packet_size": len(reduced_packet),
        "higher_spin_channels": higher_spin_channels,
        "higher_spin_count": len(higher_spin_channels),
        "virasoro_target_channels": virasoro_target_channels,
        "virasoro_target_count": len(virasoro_target_channels),
        "entry_singletons": entry_singletons,
        "transport_target_blocks": transport_targets,
        "transport_attack_order": attack_order,
        "status": (
            "first reduced stage downstream of the exact stage-4 defect-vanishing "
            "packet: eleven reduced channels split into an eight-channel higher-spin "
            "core and three Virasoro-target channels"
        ),
    }


def stage5_local_attack_order_report() -> Dict[str, object]:
    """Exact local attack order for the first stage-5 higher-spin packet."""
    return {
        "stage": 5,
        "step_1": {
            "kind": "entry_packet",
            "packet": (
                (3, 4, 5, 2),
                (5, 5, 4, 6),
            ),
            "singleton_order": (
                (3, 4, 5, 2),
                (5, 5, 4, 6),
            ),
        },
        "step_2": {
            "kind": "target5_corridor",
            "corridor": (
                (3, 4, 5, 2),
                (3, 5, 5, 3),
                (4, 5, 5, 4),
            ),
            "tail_singleton": (3, 4, 5, 2),
            "residual_singleton_order": (
                (3, 5, 5, 3),
                (4, 5, 5, 4),
            ),
        },
        "step_3": {
            "kind": "remaining_transport_ladders",
            "target_order": (5, 4, 3),
        },
        "visible_pairing_refinement": {
            "target5_corridor_no_new_independent_data": True,
            "independent_entry_channel": (5, 5, 4, 6),
            "dependent_target5_corridor": {
                "tail_channel": (3, 4, 5, 2),
                "determined_by_target4_channel": {
                    "channel": (3, 5, 4, 4),
                    "ratio": Rational(-5, 4),
                },
                "determined_by_target3_channel": {
                    "channel": (4, 5, 3, 6),
                    "ratio": Rational(5, 3),
                },
                "vanishing_transport_channels": (
                    (3, 5, 5, 3),
                    (4, 5, 5, 4),
                ),
            },
            "effective_independent_order": (
                (5, 5, 4, 6),
                "target4_ladder",
                "target3_ladder",
            ),
            "effective_transport_attack_order": (4, 3),
        },
        "status": (
            "the first local stage-5 frontier is entry packet first, then the "
            "target-5 corridor, then the remaining transport ladders ordered by "
            "targets 5, 4, 3"
        ),
    }


def stage5_effective_independent_frontier_report() -> Dict[str, object]:
    """Effective independent stage-5 frontier on the full visible pairing locus."""
    local = stage5_local_attack_order_report()
    refinement = local["visible_pairing_refinement"]
    return {
        "stage": 5,
        "assumption": "full visible W3/W4/W5 pairing locus",
        "eliminated_target5_corridor": (
            (3, 4, 5, 2),
            (3, 5, 5, 3),
            (4, 5, 5, 4),
        ),
        "independent_entry_channel": refinement["independent_entry_channel"],
        "independent_order": refinement["effective_independent_order"],
        "effective_transport_attack_order": refinement["effective_transport_attack_order"],
        "remaining_transport_ladders": {
            "target4": (
                (3, 5, 4, 4),
                (4, 5, 4, 5),
            ),
            "target3": (
                (3, 5, 3, 5),
                (4, 5, 3, 6),
            ),
        },
        "status": (
            "on the full visible pairing locus, the target-5 corridor contributes "
            "no new independent coefficient; the effective independent frontier is "
            "the self-return singleton followed by the target-4 and target-3 ladders"
        ),
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
        "stage4_primitive_transport": stage4_primitive_transport_report(c),
        "stage4_borcherds_transport": stage4_borcherds_transport_report(c),
        "stage4_two_primitive_closure": stage4_two_primitive_square_closure_report(c),
        "stage4_local_attack_order": stage4_local_attack_order_report(c),
        "stage4_level_contract": "use stage4_target_packet_at_level / evaluate_stage4_dual_defects_at_level",
        "stage5_frontier": stage5_dual_frontier_report(),
        "stage5_local_attack_order": stage5_local_attack_order_report(),
        "stage5_effective_independent_frontier": stage5_effective_independent_frontier_report(),
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
    stage4_transport = report["stage4_primitive_transport"]
    stage4_borcherds = report["stage4_borcherds_transport"]
    stage4_closure = report["stage4_two_primitive_closure"]
    stage4_attack_order = report["stage4_local_attack_order"]
    stage5 = report["stage5_frontier"]
    stage5_attack_order = report["stage5_local_attack_order"]
    stage5_effective = report["stage5_effective_independent_frontier"]
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
        "stage-4 primitive-plus-transport count": (
            len(stage4_transport["independent_square_identity_channels"]) == 3
        ),
        "stage-4 Borcherds transport ratio": (
            stage4_borcherds["target_square_ratio"] == Rational(5, 7)
        ),
        "stage-4 two-primitive closure count": (
            len(stage4_closure["independent_square_identity_channels"]) == 2
        ),
        "stage-4 local attack order has two steps": (
            set(stage4_attack_order) >= {"stage", "step_1", "step_2", "status"}
        ),
        "stage-5 prerequisite is stage-4 vanishing": (
            stage5["prerequisite_goal"] == "vanish all six stage-4 defects"
        ),
        "stage-5 reduced packet size": stage5["reduced_packet_size"] == 11,
        "stage-5 higher-spin count": stage5["higher_spin_count"] == 8,
        "stage-5 virasoro-target count": stage5["virasoro_target_count"] == 3,
        "stage-5 local attack order has three steps": (
            set(stage5_attack_order) >= {"stage", "step_1", "step_2", "step_3", "status"}
        ),
        "stage-5 effective frontier order": (
            stage5_effective["independent_order"]
            == ((5, 5, 4, 6), "target4_ladder", "target3_ladder")
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
        "stage-4 transport square ratio": (
            stage4_transport["transport_square_channel"]["ratio_to_c334"] == Rational(5, 7)
        ),
        "stage-4 automatic square ratio": (
            stage4_transport["automatic_square_channel"]["residue_square_ratio"]
            == Rational(9, 16)
        ),
        "stage-4 forced transport closure ratio": (
            stage4_closure["forced_transport_channel"]["square_ratio"] == Rational(5, 7)
        ),
        "stage-4 local step 1 channel": (
            stage4_attack_order["step_1"]["report"]["channel"] == (4, 4, 2, 6)
        ),
        "stage-4 local step 2 channel": (
            stage4_attack_order["step_2"]["report"]["relation_channel"] == (3, 4, 4, 3)
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
        "stage-5 local step 1 mixed-entry singleton": (
            stage5_attack_order["step_1"]["singleton_order"][0] == (3, 4, 5, 2)
        ),
        "stage-5 local step 2 residual order": (
            stage5_attack_order["step_2"]["residual_singleton_order"]
            == ((3, 5, 5, 3), (4, 5, 5, 4))
        ),
        "stage-5 visible pairing self-return singleton": (
            stage5_attack_order["visible_pairing_refinement"]["independent_entry_channel"]
            == (5, 5, 4, 6)
        ),
        "stage-5 visible pairing effective transport order": (
            stage5_attack_order["visible_pairing_refinement"]["effective_transport_attack_order"]
            == (4, 3)
        ),
        "stage-5 effective frontier removes target-5 corridor": (
            stage5_effective["eliminated_target5_corridor"]
            == ((3, 4, 5, 2), (3, 5, 5, 3), (4, 5, 5, 4))
        ),
    }
