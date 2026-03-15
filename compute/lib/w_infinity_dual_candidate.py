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


def stage5_visible_pairing_normal_form_report() -> Dict[str, object]:
    """Exact one-parameter normal form for the stage-5 packet on the full visible pairing locus."""
    a5 = Symbol("A_5")
    representative = (3, 5, 4, 4)
    channel_normal_form = {
        (3, 4, 5, 2): {
            "kind": "forced_nonzero",
            "forced_by": representative,
            "ratio_to_A5": Rational(-5, 4),
            "expression": Rational(-5, 4) * a5,
        },
        (3, 5, 5, 3): {
            "kind": "forced_zero",
            "forced_by": representative,
            "ratio_to_A5": Rational(0),
            "expression": 0,
        },
        (4, 5, 5, 4): {
            "kind": "forced_zero",
            "forced_by": representative,
            "ratio_to_A5": Rational(0),
            "expression": 0,
        },
        (5, 5, 4, 6): {
            "kind": "forced_zero",
            "forced_by": representative,
            "ratio_to_A5": Rational(0),
            "expression": 0,
        },
        representative: {
            "kind": "parameter",
            "ratio_to_A5": Rational(1),
            "expression": a5,
        },
        (4, 5, 4, 5): {
            "kind": "forced_zero",
            "forced_by": representative,
            "ratio_to_A5": Rational(0),
            "expression": 0,
        },
        (3, 5, 3, 5): {
            "kind": "forced_zero",
            "forced_by": representative,
            "ratio_to_A5": Rational(0),
            "expression": 0,
        },
        (4, 5, 3, 6): {
            "kind": "forced_nonzero",
            "forced_by": representative,
            "ratio_to_A5": Rational(-3, 4),
            "expression": Rational(-3, 4) * a5,
        },
    }
    return {
        "stage": 5,
        "assumption": "full visible W3/W4/W5 pairing locus",
        "parameter": {
            "name": "A_5",
            "channel": representative,
            "expression": a5,
        },
        "representative_channel": representative,
        "channel_normal_form": channel_normal_form,
        "status": (
            "on the full visible pairing locus, every stage-5 higher-spin "
            "channel is either zero or a fixed rational multiple of A_5 = "
            "C^res_{3,5;4;0,4}(5)"
        ),
    }


def stage5_principal_one_coefficient_normal_form_report() -> Dict[str, object]:
    """Conjectural principal DS one-parameter normal form on the full visible pairing locus."""
    a5_ds = Symbol("A_5_DS")
    representative = (3, 5, 4, 4)
    channel_normal_form = {
        (3, 4, 5, 2): {
            "kind": "forced_nonzero",
            "forced_by": representative,
            "ratio_to_A5_DS": Rational(-5, 4),
            "expression": Rational(-5, 4) * a5_ds,
        },
        (3, 5, 5, 3): {
            "kind": "forced_zero",
            "forced_by": representative,
            "ratio_to_A5_DS": Rational(0),
            "expression": 0,
        },
        (4, 5, 5, 4): {
            "kind": "forced_zero",
            "forced_by": representative,
            "ratio_to_A5_DS": Rational(0),
            "expression": 0,
        },
        (5, 5, 4, 6): {
            "kind": "forced_zero",
            "forced_by": representative,
            "ratio_to_A5_DS": Rational(0),
            "expression": 0,
        },
        representative: {
            "kind": "parameter",
            "ratio_to_A5_DS": Rational(1),
            "expression": a5_ds,
        },
        (4, 5, 4, 5): {
            "kind": "forced_zero",
            "forced_by": representative,
            "ratio_to_A5_DS": Rational(0),
            "expression": 0,
        },
        (3, 5, 3, 5): {
            "kind": "forced_zero",
            "forced_by": representative,
            "ratio_to_A5_DS": Rational(0),
            "expression": 0,
        },
        (4, 5, 3, 6): {
            "kind": "forced_nonzero",
            "forced_by": representative,
            "ratio_to_A5_DS": Rational(-3, 4),
            "expression": Rational(-3, 4) * a5_ds,
        },
    }
    return {
        "stage": 5,
        "assumption": "full visible W3/W4/W5 pairing locus",
        "parameter": {
            "name": "A_5_DS",
            "channel": representative,
            "expression": a5_ds,
        },
        "representative_channel": representative,
        "channel_normal_form": channel_normal_form,
        "status": (
            "conjectural principal stage-5 target normal form: every DS higher-spin "
            "channel is zero or a fixed rational multiple of A_5_DS = "
            "C^DS_{3,5;4;0,4}(5)"
        ),
    }


def stage5_principal_target5_no_new_independent_data_report() -> Dict[str, object]:
    """Conjectural principal target-5 corridor normal form on the full visible pairing locus."""
    principal = stage5_principal_one_coefficient_normal_form_report()
    representative = principal["representative_channel"]
    corridor = (
        (3, 4, 5, 2),
        (3, 5, 5, 3),
        (4, 5, 5, 4),
    )
    target3 = (4, 5, 3, 6)
    return {
        "stage": 5,
        "assumption": "full visible W3/W4/W5 pairing locus",
        "representative_channel": representative,
        "corridor_channels": corridor,
        "neighboring_target3_channel": target3,
        "tail_ratio_to_representative": principal["channel_normal_form"][(3, 4, 5, 2)][
            "ratio_to_A5_DS"
        ],
        "tail_ratio_to_target3": Rational(5, 3),
        "vanishing_corridor_channels": (
            (3, 5, 5, 3),
            (4, 5, 5, 4),
        ),
        "status": (
            "conjectural principal target-5 corridor normal form: the tail channel "
            "is forced from the target-4 representative and the neighboring "
            "target-3 channel, and the two transport singleton channels vanish"
        ),
    }


def stage5_principal_residual_front_one_coefficient_report() -> Dict[str, object]:
    """Conjectural principal residual-front normal form on the full visible pairing locus."""
    principal = stage5_principal_one_coefficient_normal_form_report()
    representative = principal["representative_channel"]
    target3 = (4, 5, 3, 6)
    return {
        "stage": 5,
        "assumption": "full visible W3/W4/W5 pairing locus",
        "representative_channel": representative,
        "residual_front_channels": (
            (5, 5, 4, 6),
            representative,
            (4, 5, 4, 5),
            (3, 5, 3, 5),
            target3,
        ),
        "vanishing_channels": (
            (5, 5, 4, 6),
            (4, 5, 4, 5),
            (3, 5, 3, 5),
        ),
        "determined_nonzero_channel": {
            "channel": target3,
            "ratio_to_representative": principal["channel_normal_form"][target3][
                "ratio_to_A5_DS"
            ],
        },
        "status": (
            "conjectural principal residual-front normal form: outside the target-5 "
            "corridor, the stage-5 higher-spin packet is controlled by the "
            "target-4 representative, with one target-3 channel determined and "
            "the remaining residual channels vanishing"
        ),
    }


def stage5_principal_one_coefficient_factorization_report() -> Dict[str, object]:
    """Factorization of the principal stage-5 one-coefficient normal form."""
    target5 = stage5_principal_target5_no_new_independent_data_report()
    residual = stage5_principal_residual_front_one_coefficient_report()
    return {
        "stage": 5,
        "assumption": "full visible W3/W4/W5 pairing locus",
        "principal_target5_corridor": target5,
        "principal_residual_front": residual,
        "factorization_inputs": (
            "principal_target5_no_new_independent_data",
            "principal_residual_front_one_coefficient",
        ),
        "equivalent_principal_normal_form": "principal_one_coefficient_normal_form",
        "representative_channel": (3, 5, 4, 4),
        "status": (
            "proved factorization of the principal stage-5 one-coefficient normal "
            "form through the target-5 corridor packet and the residual front"
        ),
    }


def stage5_effective_independent_frontier_report() -> Dict[str, object]:
    """Effective independent stage-5 frontier on the full visible pairing locus."""
    local = stage5_local_attack_order_report()
    refinement = local["visible_pairing_refinement"]
    normal_form = stage5_visible_pairing_normal_form_report()
    return {
        "stage": 5,
        "assumption": "full visible W3/W4/W5 pairing locus",
        "effective_independent_count": 1,
        "representative_channel": (3, 5, 4, 4),
        "parameter": normal_form["parameter"],
        "channel_normal_form": normal_form["channel_normal_form"],
        "eliminated_target5_corridor": (
            (3, 4, 5, 2),
            (3, 5, 5, 3),
            (4, 5, 5, 4),
        ),
        "independent_entry_channel": refinement["independent_entry_channel"],
        "independent_order": refinement["effective_independent_order"],
        "effective_transport_attack_order": refinement["effective_transport_attack_order"],
        "vanishing_channels": (
            (3, 5, 5, 3),
            (4, 5, 5, 4),
            (5, 5, 4, 6),
            (4, 5, 4, 5),
            (3, 5, 3, 5),
        ),
        "determined_nonzero_channels": {
            (3, 4, 5, 2): {
                "forced_by": (3, 5, 4, 4),
                "ratio": Rational(-5, 4),
            },
            (4, 5, 3, 6): {
                "forced_by": (3, 5, 4, 4),
                "ratio": Rational(-3, 4),
            },
        },
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
            "on the full visible pairing locus, the entire stage-5 higher-spin "
            "packet is controlled by the single target-4 singleton (3,5;4;0,4); "
            "the target-5 corridor contributes no new independent coefficient, "
            "the self-return and upper transport channels vanish, and the "
            "remaining nonzero channels are forced by fixed rational ratios"
        ),
    }


def stage5_one_coefficient_reduction_report() -> Dict[str, object]:
    """Reduction of the full stage-5 comparison to one channel under matching normal forms."""
    residue = stage5_visible_pairing_normal_form_report()
    principal = stage5_principal_one_coefficient_normal_form_report()
    factorization = stage5_principal_one_coefficient_factorization_report()
    representative = residue["representative_channel"]
    shared_ratios = {
        channel: {
            "residue_ratio": data["ratio_to_A5"],
            "principal_ratio": principal["channel_normal_form"][channel]["ratio_to_A5_DS"],
        }
        for channel, data in residue["channel_normal_form"].items()
    }
    return {
        "stage": 5,
        "assumption": (
            "full visible W3/W4/W5 pairing locus plus principal target-5 corridor "
            "and residual-front one-coefficient conjectures"
        ),
        "higher_spin_packet": tuple(incremental_higher_spin_channels(5)),
        "representative_channel": representative,
        "residue_parameter": residue["parameter"],
        "principal_parameter": principal["parameter"],
        "principal_factorization": factorization,
        "shared_channel_ratios": shared_ratios,
        "reduction_goal": {
            "channel": representative,
            "identity": "C^res_{3,5;4;0,4}(5) = C^DS_{3,5;4;0,4}(5)",
        },
        "status": (
            "under the conjectural principal target-5 corridor and residual-front "
            "normal forms, the full stage-5 higher-spin comparison on J_5^hs is "
            "equivalent to the single target-4 singleton identity"
        ),
    }


def stage5_one_defect_family_report() -> Dict[str, object]:
    """Exact one-defect family induced by the residue/DS one-parameter normal forms."""
    residue = stage5_visible_pairing_normal_form_report()
    principal = stage5_principal_one_coefficient_normal_form_report()
    representative = residue["representative_channel"]
    d5 = Symbol("D_5")
    defect_map = {}
    for channel, residue_data in residue["channel_normal_form"].items():
        principal_data = principal["channel_normal_form"][channel]
        residue_ratio = residue_data["ratio_to_A5"]
        principal_ratio = principal_data["ratio_to_A5_DS"]
        defect_map[channel] = {
            "kind": "defect",
            "residue_expression": residue_data["expression"],
            "principal_expression": principal_data["expression"],
            "ratio_to_D5": residue_ratio,
            "defect_expression": simplify(residue_ratio * d5),
        }
    return {
        "stage": 5,
        "assumption": (
            "full visible W3/W4/W5 pairing locus plus principal stage-5 "
            "one-coefficient normal form"
        ),
        "representative_channel": representative,
        "representative_defect": {
            "name": "D_5",
            "channel": representative,
            "expression": d5,
        },
        "channel_defects": defect_map,
        "status": (
            "under the matching one-parameter normal forms, every stage-5 higher-spin "
            "comparison defect is a fixed rational multiple of the single defect "
            "D_5 = C^res_{3,5;4;0,4}(5) - C^DS_{3,5;4;0,4}(5)"
        ),
    }


def stage5_visible_conjecture_network_collapse_report() -> Dict[str, object]:
    """Visible stage-5 local conjecture network under the principal one-coefficient normal form."""
    representative = (3, 5, 4, 4)
    return {
        "stage": 5,
        "assumption": (
            "full visible W3/W4/W5 pairing locus plus principal stage-5 "
            "one-coefficient normal form"
        ),
        "comparison_goal": {
            "channel": representative,
            "identity": "C^res_{3,5;4;0,4}(5) = C^DS_{3,5;4;0,4}(5)",
        },
        "equivalent_surfaces": {
            "conj:winfty-stage5-higher-spin-identities": {
                "kind": "full_packet",
                "channels": tuple(incremental_higher_spin_channels(5)),
                "nontrivial_channel": representative,
            },
            "conj:winfty-stage5-entry-identities": {
                "kind": "entry_packet",
                "channels": ((3, 4, 5, 2), (5, 5, 4, 6)),
                "nontrivial_channel": (3, 4, 5, 2),
                "ratio_to_representative": Rational(-5, 4),
            },
            "conj:winfty-stage5-transport-identities": {
                "kind": "transport_packet",
                "channels": (
                    (3, 5, 5, 3),
                    (4, 5, 5, 4),
                    (3, 5, 4, 4),
                    (4, 5, 4, 5),
                    (3, 5, 3, 5),
                    (4, 5, 3, 6),
                ),
                "nontrivial_channel": representative,
            },
            "conj:winfty-stage5-transport-target-3": {
                "kind": "target3_ladder",
                "channels": ((3, 5, 3, 5), (4, 5, 3, 6)),
                "nontrivial_channel": (4, 5, 3, 6),
                "ratio_to_representative": Rational(-3, 4),
            },
            "conj:winfty-stage5-transport-target-4": {
                "kind": "target4_ladder",
                "channels": ((3, 5, 4, 4), (4, 5, 4, 5)),
                "nontrivial_channel": representative,
                "ratio_to_representative": Rational(1),
            },
            "conj:winfty-stage5-block-34": {
                "kind": "block",
                "channels": ((3, 4, 5, 2),),
                "nontrivial_channel": (3, 4, 5, 2),
                "ratio_to_representative": Rational(-5, 4),
            },
            "conj:winfty-stage5-block-35": {
                "kind": "block",
                "channels": ((3, 5, 5, 3), (3, 5, 4, 4), (3, 5, 3, 5)),
                "nontrivial_channel": representative,
                "ratio_to_representative": Rational(1),
            },
            "conj:winfty-stage5-block-45": {
                "kind": "block",
                "channels": ((4, 5, 5, 4), (4, 5, 4, 5), (4, 5, 3, 6)),
                "nontrivial_channel": (4, 5, 3, 6),
                "ratio_to_representative": Rational(-3, 4),
            },
        },
        "automatic_surfaces": {
            "conj:winfty-stage5-transport-target-5": {
                "kind": "target5_ladder",
                "channels": ((3, 5, 5, 3), (4, 5, 5, 4)),
            },
            "conj:winfty-stage5-transport-target5-35": {
                "kind": "singleton",
                "channel": (3, 5, 5, 3),
            },
            "conj:winfty-stage5-transport-target5-45": {
                "kind": "singleton",
                "channel": (4, 5, 5, 4),
            },
            "conj:winfty-stage5-block-55": {
                "kind": "self_block",
                "channel": (5, 5, 4, 6),
            },
        },
        "status": (
            "under the conjectural principal one-coefficient normal form, every "
            "local stage-5 conjectural surface is either automatic or equivalent "
            "to the single target-4 singleton identity"
        ),
    }


def stage5_conjecture_defect_dictionary_report() -> Dict[str, object]:
    """Labeled stage-5 conjecture surfaces as exact multiples of the representative defect."""
    defect_family = stage5_one_defect_family_report()
    network = stage5_visible_conjecture_network_collapse_report()
    d5 = defect_family["representative_defect"]["expression"]
    representative = defect_family["representative_channel"]

    equivalent = {}
    for label, surface in network["equivalent_surfaces"].items():
        nontrivial_channel = surface["nontrivial_channel"]
        defect_ratio = surface.get("ratio_to_representative", Rational(1))
        equivalent[label] = {
            **surface,
            "defect_channel": nontrivial_channel,
            "ratio_to_D5": defect_ratio,
            "defect_expression": simplify(defect_ratio * d5),
        }

    automatic = {}
    for label, surface in network["automatic_surfaces"].items():
        automatic[label] = {
            **surface,
            "ratio_to_D5": Rational(0),
            "defect_expression": Rational(0),
        }

    return {
        "stage": 5,
        "assumption": defect_family["assumption"],
        "representative_channel": representative,
        "representative_defect": defect_family["representative_defect"],
        "equivalent_surfaces": equivalent,
        "automatic_surfaces": automatic,
        "status": (
            "under the principal stage-5 one-coefficient normal form, every labeled "
            "local stage-5 conjecture surface has defect either 0 or a fixed rational "
            "multiple of D_5"
        ),
    }


def stage5_exact_remaining_input_report() -> Dict[str, object]:
    """Exact remaining stage-5 visible-pairing input package."""
    target5 = stage5_principal_target5_no_new_independent_data_report()
    residual = stage5_principal_residual_front_one_coefficient_report()
    factorization = stage5_principal_one_coefficient_factorization_report()
    reduction = stage5_one_coefficient_reduction_report()
    singleton = reduction["reduction_goal"]
    return {
        "stage": 5,
        "assumption": "full visible W3/W4/W5 pairing locus",
        "higher_spin_packet": reduction["higher_spin_packet"],
        "principal_target5_corridor": target5,
        "principal_residual_front": residual,
        "principal_factorization": factorization,
        "singleton_identity": singleton,
        "remaining_input_package": (
            "principal_target5_no_new_independent_data",
            "principal_residual_front_one_coefficient",
            "singleton_identity",
        ),
        "closure_equivalence": (
            "full stage-5 higher-spin comparison on J_5^hs closes iff the "
            "principal target-5 corridor carries no new independent data, the "
            "principal residual front carries one effective coefficient, and the "
            "singleton identity "
            "C^res_{3,5;4;0,4}(5) = C^DS_{3,5;4;0,4}(5) holds"
        ),
        "status": (
            "proved packaging of the exact remaining local stage-5 "
            "visible-pairing input: principal target-5 corridor packet, "
            "principal residual-front packet, and the target-4 singleton identity"
        ),
    }


def stage5_one_coefficient_comparison_report() -> Dict[str, object]:
    """Exact next local stage-5 comparison frontier on the full visible pairing locus."""
    frontier = stage5_effective_independent_frontier_report()
    normal_form = stage5_visible_pairing_normal_form_report()
    principal_normal_form = stage5_principal_one_coefficient_normal_form_report()
    principal_target5 = stage5_principal_target5_no_new_independent_data_report()
    principal_residual = stage5_principal_residual_front_one_coefficient_report()
    principal_factorization = stage5_principal_one_coefficient_factorization_report()
    reduction = stage5_one_coefficient_reduction_report()
    defect_family = stage5_one_defect_family_report()
    defect_dictionary = stage5_conjecture_defect_dictionary_report()
    remaining_input = stage5_exact_remaining_input_report()
    network_collapse = stage5_visible_conjecture_network_collapse_report()
    return {
        "stage": 5,
        "assumption": "full visible W3/W4/W5 pairing locus",
        "representative_channel": frontier["representative_channel"],
        "comparison_goal": {
            "channel": frontier["representative_channel"],
            "identity": "C^res_{3,5;4;0,4}(5) = C^DS_{3,5;4;0,4}(5)",
        },
        "residue_normal_form": normal_form,
        "principal_normal_form": principal_normal_form,
        "principal_target5_corridor": principal_target5,
        "principal_residual_front": principal_residual,
        "principal_factorization": principal_factorization,
        "comparison_reduction": reduction,
        "defect_family": defect_family,
        "conjecture_defect_dictionary": defect_dictionary,
        "exact_remaining_input": remaining_input,
        "conjecture_network_collapse": network_collapse,
        "effective_residue_frontier": frontier,
        "status": (
            "conjectural single-coefficient closure of the stage-5 higher-spin "
            "comparison on the full visible pairing locus"
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
        "stage5_visible_pairing_normal_form": stage5_visible_pairing_normal_form_report(),
        "stage5_principal_one_coefficient_normal_form": (
            stage5_principal_one_coefficient_normal_form_report()
        ),
        "stage5_principal_target5_no_new_independent_data": (
            stage5_principal_target5_no_new_independent_data_report()
        ),
        "stage5_principal_residual_front_one_coefficient": (
            stage5_principal_residual_front_one_coefficient_report()
        ),
        "stage5_principal_one_coefficient_factorization": (
            stage5_principal_one_coefficient_factorization_report()
        ),
        "stage5_effective_independent_frontier": stage5_effective_independent_frontier_report(),
        "stage5_one_coefficient_reduction": stage5_one_coefficient_reduction_report(),
        "stage5_one_defect_family": stage5_one_defect_family_report(),
        "stage5_conjecture_defect_dictionary": stage5_conjecture_defect_dictionary_report(),
        "stage5_exact_remaining_input": stage5_exact_remaining_input_report(),
        "stage5_visible_conjecture_network_collapse": (
            stage5_visible_conjecture_network_collapse_report()
        ),
        "stage5_one_coefficient_comparison": stage5_one_coefficient_comparison_report(),
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
    stage5_normal_form = report["stage5_visible_pairing_normal_form"]
    stage5_principal_normal_form = report["stage5_principal_one_coefficient_normal_form"]
    stage5_principal_target5 = report["stage5_principal_target5_no_new_independent_data"]
    stage5_principal_residual = report["stage5_principal_residual_front_one_coefficient"]
    stage5_principal_factorization = report["stage5_principal_one_coefficient_factorization"]
    stage5_effective = report["stage5_effective_independent_frontier"]
    stage5_reduction = report["stage5_one_coefficient_reduction"]
    stage5_defect_family = report["stage5_one_defect_family"]
    stage5_defect_dictionary = report["stage5_conjecture_defect_dictionary"]
    stage5_exact = report["stage5_exact_remaining_input"]
    stage5_network_collapse = report["stage5_visible_conjecture_network_collapse"]
    stage5_one = report["stage5_one_coefficient_comparison"]
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
        "stage-5 visible normal form covers higher-spin packet": (
            set(stage5_normal_form["channel_normal_form"]) == set(stage5["higher_spin_channels"])
        ),
        "stage-5 visible normal form parameter channel": (
            stage5_normal_form["parameter"]["channel"] == (3, 5, 4, 4)
        ),
        "stage-5 visible normal form mixed-entry ratio": (
            stage5_normal_form["channel_normal_form"][(3, 4, 5, 2)]["ratio_to_A5"]
            == Rational(-5, 4)
        ),
        "stage-5 visible normal form target-3 ratio": (
            stage5_normal_form["channel_normal_form"][(4, 5, 3, 6)]["ratio_to_A5"]
            == Rational(-3, 4)
        ),
        "stage-5 principal normal form representative": (
            stage5_principal_normal_form["representative_channel"] == (3, 5, 4, 4)
        ),
        "stage-5 principal normal form target-3 ratio": (
            stage5_principal_normal_form["channel_normal_form"][(4, 5, 3, 6)]["ratio_to_A5_DS"]
            == Rational(-3, 4)
        ),
        "stage-5 principal target5 representative": (
            stage5_principal_target5["representative_channel"] == (3, 5, 4, 4)
        ),
        "stage-5 principal target5 tail ratio": (
            stage5_principal_target5["tail_ratio_to_target3"] == Rational(5, 3)
        ),
        "stage-5 principal residual representative": (
            stage5_principal_residual["representative_channel"] == (3, 5, 4, 4)
        ),
        "stage-5 principal residual target3 ratio": (
            stage5_principal_residual["determined_nonzero_channel"]["ratio_to_representative"]
            == Rational(-3, 4)
        ),
        "stage-5 principal factorization has two packets": (
            stage5_principal_factorization["factorization_inputs"]
            == (
                "principal_target5_no_new_independent_data",
                "principal_residual_front_one_coefficient",
            )
        ),
        "stage-5 effective frontier order": (
            stage5_effective["independent_order"]
            == ((5, 5, 4, 6), "target4_ladder", "target3_ladder")
        ),
        "stage-5 effective frontier count": (
            stage5_effective["effective_independent_count"] == 1
        ),
        "stage-5 effective frontier representative": (
            stage5_effective["representative_channel"] == (3, 5, 4, 4)
        ),
        "stage-5 effective frontier matches visible normal form": (
            stage5_effective["channel_normal_form"] == stage5_normal_form["channel_normal_form"]
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
        "stage-5 one-coefficient comparison representative": (
            stage5_one["comparison_goal"]["channel"] == (3, 5, 4, 4)
        ),
        "stage-5 reduction representative": (
            stage5_reduction["reduction_goal"]["channel"] == (3, 5, 4, 4)
        ),
        "stage-5 reduction covers higher-spin packet": (
            set(stage5_reduction["higher_spin_packet"]) == set(stage5["higher_spin_channels"])
        ),
        "stage-5 exact remaining input representative": (
            stage5_exact["singleton_identity"]["channel"] == (3, 5, 4, 4)
        ),
        "stage-5 exact remaining input has three factors": (
            stage5_exact["remaining_input_package"]
            == (
                "principal_target5_no_new_independent_data",
                "principal_residual_front_one_coefficient",
                "singleton_identity",
            )
        ),
        "stage-5 reduction matches shared target5 vanishing": (
            stage5_reduction["shared_channel_ratios"][(3, 5, 5, 3)]
            == {"residue_ratio": Rational(0), "principal_ratio": Rational(0)}
        ),
        "stage-5 defect family representative": (
            stage5_defect_family["representative_defect"]["channel"] == (3, 5, 4, 4)
        ),
        "stage-5 defect family covers higher-spin packet": (
            set(stage5_defect_family["channel_defects"]) == set(stage5["higher_spin_channels"])
        ),
        "stage-5 defect family mixed-entry ratio": (
            stage5_defect_family["channel_defects"][(3, 4, 5, 2)]["ratio_to_D5"]
            == Rational(-5, 4)
        ),
        "stage-5 defect family target-3 ratio": (
            stage5_defect_family["channel_defects"][(4, 5, 3, 6)]["ratio_to_D5"]
            == Rational(-3, 4)
        ),
        "stage-5 defect dictionary full packet representative": (
            stage5_defect_dictionary["equivalent_surfaces"][
                "conj:winfty-stage5-higher-spin-identities"
            ]["defect_channel"]
            == (3, 5, 4, 4)
        ),
        "stage-5 defect dictionary entry ratio": (
            stage5_defect_dictionary["equivalent_surfaces"][
                "conj:winfty-stage5-entry-identities"
            ]["ratio_to_D5"]
            == Rational(-5, 4)
        ),
        "stage-5 defect dictionary target-5 is automatic": (
            stage5_defect_dictionary["automatic_surfaces"][
                "conj:winfty-stage5-transport-target-5"
            ]["defect_expression"]
            == 0
        ),
        "stage-5 network collapse representative": (
            stage5_network_collapse["comparison_goal"]["channel"] == (3, 5, 4, 4)
        ),
        "stage-5 network collapse block-45 ratio": (
            stage5_network_collapse["equivalent_surfaces"]["conj:winfty-stage5-block-45"][
                "ratio_to_representative"
            ]
            == Rational(-3, 4)
        ),
        "stage-5 network collapse target5 singleton automatic": (
            stage5_network_collapse["automatic_surfaces"][
                "conj:winfty-stage5-transport-target5-35"
            ]["channel"]
            == (3, 5, 5, 3)
        ),
        "stage-5 one-coefficient comparison uses visible normal form": (
            stage5_one["residue_normal_form"]["parameter"]["channel"] == (3, 5, 4, 4)
        ),
        "stage-5 one-coefficient comparison includes principal normal form": (
            stage5_one["principal_normal_form"]["parameter"]["channel"] == (3, 5, 4, 4)
        ),
        "stage-5 one-coefficient comparison includes defect family": (
            stage5_one["defect_family"]["representative_defect"]["channel"] == (3, 5, 4, 4)
        ),
        "stage-5 one-coefficient comparison includes defect dictionary": (
            stage5_one["conjecture_defect_dictionary"]["representative_defect"]["channel"]
            == (3, 5, 4, 4)
        ),
        "stage-5 one-coefficient comparison includes exact remaining input": (
            stage5_one["exact_remaining_input"]["singleton_identity"]["channel"] == (3, 5, 4, 4)
        ),
        "stage-5 one-coefficient comparison includes network collapse": (
            stage5_one["conjecture_network_collapse"]["comparison_goal"]["channel"]
            == (3, 5, 4, 4)
        ),
    }
