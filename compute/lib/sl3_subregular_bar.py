r"""Typed bar audit for the minimal/subregular ``sl_3`` W-algebra.

For ``sl_3`` the minimal and subregular nilpotent orbit is the partition
``(2,1)``.  Its quantum Drinfeld--Sokolov reduction is the
Bershadsky--Polyakov algebra.  This module exposes the exact FKR OPE data
and keeps four further assertions as separate proof obligations:

* collapse of the completed chiral bar spectral sequence;
* identification of the bar dual with ``BP_{-k-6}``;
* commutation of Drinfeld--Sokolov reduction with the chosen bar model;
* the genus-one modular characteristic.

Free strong generation and a quadratic OPE normal form supply PBW evidence.
They do not by themselves prove any of the four assertions above.
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Tuple

from sympy import Rational, Symbol, simplify, solve, sympify

from compute.lib.bershadsky_polyakov_bar import (
    GENERATORS,
    GENERATOR_NAMES,
    bp_central_charge as _bp_central_charge,
    bp_dual_level,
    bp_is_chirally_koszul as _canonical_koszul_status,
    bp_koszul_conductor,
    bp_nth_products,
    bp_primary_ope_normal_form,
    bp_shifted_central_charge,
)
from compute.lib.bp_koszul_conductor_engine import (
    BP_KAPPA_STATUS,
    UnverifiedBPInvariantError,
    compute_varrho as _reciprocal_weight_diagnostic,
)


k = Symbol("k")
c = Symbol("c")

PARTITION: Tuple[int, int] = (2, 1)
N_SL3 = 3
H_DUAL_SL3 = 3
DIM_SL3 = 8

BP_BAR_HYPOTHESES: Tuple[str, ...] = (
    "completed_BP_bar_complex_constructed",
    "PBW_bar_filtration_exhaustive_complete_and_Hausdorff",
    "bar_spectral_sequence_strongly_convergent",
    "comparison_q_BP_quasi_isomorphism",
    "DS_bar_intertwiner_constructed_and_filtered",
)

BP_BAR_RESOLUTION_OBLIGATION = (
    "construct the completed BP bar differential, identify its associated "
    "graded comparison with the quadratic coalgebra, and prove strong "
    "convergence with vanishing off-diagonal homology"
)


def bp_central_charge(level: Any = None) -> Any:
    """Return the standard FKR central charge and enforce its pole."""

    lev = k if level is None else sympify(level)
    if simplify(lev + 3) == 0:
        raise ZeroDivisionError("the standard BP conformal vector has a pole at k=-3")
    return simplify(_bp_central_charge(lev))


def bp_reciprocal_weight_diagnostic() -> Rational:
    """Return the source-correct all-even reciprocal-weight sum ``17/6``."""

    value = _reciprocal_weight_diagnostic()
    return Rational(value.numerator, value.denominator)


def bp_anomaly_ratio() -> Rational:
    """Signal the open BP genus-one modular calculation."""

    raise UnverifiedBPInvariantError(BP_KAPPA_STATUS.resolution_obligation)


def kappa_path1_anomaly_ratio(level: Any = None) -> Any:
    """Signal the open BP modular characteristic."""

    if level is not None:
        sympify(level)
    raise UnverifiedBPInvariantError(BP_KAPPA_STATUS.resolution_obligation)


def kappa_path2_ds_from_affine(level: Any = None) -> Any:
    """Signal the missing genus-one DS comparison."""

    if level is not None:
        sympify(level)
    raise UnverifiedBPInvariantError(BP_KAPPA_STATUS.resolution_obligation)


def kappa_path3_complementarity(level: Any = None) -> Any:
    """Signal the open modular companion sum."""

    if level is not None:
        sympify(level)
    raise UnverifiedBPInvariantError(BP_KAPPA_STATUS.resolution_obligation)


def kappa_all_paths_agree(level: Any = None) -> Dict[str, Any]:
    """Return a status packet in place of three copies of one assumption."""

    lev = k if level is None else sympify(level)
    return {
        "level": lev,
        "path1": None,
        "path2": None,
        "path3": None,
        "all_agree": None,
        "status": BP_KAPPA_STATUS.status,
        "resolution_obligation": BP_KAPPA_STATUS.resolution_obligation,
    }


def max_ope_generator_degree() -> int:
    """Return the maximum generator degree in the displayed singular OPEs."""

    return 2


def bp_is_chirally_koszul() -> Dict[str, Any]:
    """Return PBW evidence and the open bar-collapse criterion."""

    packet = dict(_canonical_koszul_status())
    packet.update(
        {
            "is_koszul": None,
            "canonical_arity": None,
            "bar_collapse_status": "open-strong-convergence-and-diagonal-homology",
            "hypothesis_package": BP_BAR_HYPOTHESES,
            "resolution_obligation": BP_BAR_RESOLUTION_OBLIGATION,
        }
    )
    return packet


def bp_koszul_dual() -> Dict[str, Any]:
    """Separate the parameter involution from the bar-duality theorem."""

    dual = bp_dual_level(k)
    return {
        "partition": PARTITION,
        "transpose": PARTITION,
        "partition_self_transpose": True,
        "dual_level": simplify(dual),
        "dual_central_charge": simplify(bp_central_charge(dual)),
        "central_conductor": simplify(bp_koszul_conductor()),
        "central_conductor_status": "proved-rational-identity",
        "same_family_duality_claim": "BP_k^! ~= BP_{-k-6}",
        "same_family_duality_status": "conditional-H_BP_DS_bar",
        "dual_kappa": None,
        "kappa_sum": None,
        "resolution_obligation": BP_BAR_RESOLUTION_OBLIGATION,
    }


def ds_bar_intertwining() -> Dict[str, Any]:
    """Return exact conformal data and the open DS--bar comparison."""

    c_affine = simplify(8 * k / (k + 3))
    c_bp = simplify(bp_central_charge(k))
    total_shift = simplify(c_bp - c_affine)
    return {
        "c_affine": c_affine,
        "c_bp": c_bp,
        "total_DS_conformal_shift": total_shift,
        "total_shift_check": simplify(total_shift + 6 * k + 1) == 0,
        "charged_neutral_improvement_decomposition": None,
        "ds_preserves_koszulness": None,
        "ds_preserves_swiss_cheese_formality": None,
        "intertwiner_status": "open-filtered-DS-bar-comparison",
        "hypothesis_package": BP_BAR_HYPOTHESES,
        "resolution_obligation": BP_BAR_RESOLUTION_OBLIGATION,
    }


def bar_spectral_sequence_e1() -> Dict[str, Any]:
    """Record the PBW candidate page and withhold the collapse verdict."""

    return {
        "pbw_input": "free strong generation by J,G+,G-,T",
        "associated_graded_candidate": "differential polynomial algebra on four generators",
        "dim_V": 4,
        "e1_page": None,
        "collapses_at": None,
        "bar_cohomology": None,
        "status": "open-filtered-bar-computation",
        "hypothesis_package": BP_BAR_HYPOTHESES,
        "resolution_obligation": BP_BAR_RESOLUTION_OBLIGATION,
    }


def bar_cohomology_generators() -> Dict[str, Any]:
    """Return the open bar-cohomology generator packet."""

    return {
        "n_generators": None,
        "generators": None,
        "dual_level": simplify(bp_dual_level(k)),
        "dual_central_charge": simplify(bp_central_charge(bp_dual_level(k))),
        "status": "open-bar-cohomology-computation",
        "resolution_obligation": BP_BAR_RESOLUTION_OBLIGATION,
    }


def shadow_tower_on_T_line(max_arity: int = 8) -> Dict[str, Any]:
    """Return the exact Virasoro leading-pole datum and an open tower status."""

    if max_arity < 2:
        raise ValueError("the T-line diagnostic begins at arity two")
    return {
        "max_arity_requested": max_arity,
        "S2_T": simplify(bp_central_charge(k) / 2),
        "higher_coefficients": None,
        "status": "open-Maurer-Cartan-recursion-and-full-BP-comparison",
    }


def shadow_depth_classification() -> Dict[str, Any]:
    """Return exact T-line singular loci and withhold the BP class verdict."""

    cc = simplify(bp_central_charge(k))
    return {
        "generic_class": None,
        "generic_depth": None,
        "T_line_c_zero_levels": solve(cc, k),
        "T_line_5c_plus_22_zero_levels": solve(5 * cc + 22, k),
        "critical_level": Rational(-3),
        "status": "open-full-shadow-tower-computation",
        "reason": "a Virasoro T-line restriction does not classify the mixed J,G+,G-,T tower",
    }


def kappa_deficit_analysis() -> Dict[str, Any]:
    """Return exact affine data while withholding the open BP kappa deficit."""

    kappa_affine = simplify(Rational(DIM_SL3, 2 * H_DUAL_SL3) * (k + H_DUAL_SL3))
    return {
        "kappa_affine": kappa_affine,
        "kappa_bp": None,
        "deficit": None,
        "total_DS_conformal_shift": simplify(bp_central_charge(k) - 8 * k / (k + 3)),
        "status": BP_KAPPA_STATUS.status,
        "resolution_obligation": BP_KAPPA_STATUS.resolution_obligation,
    }


def n2_sca_structure() -> Dict[str, Any]:
    """Compatibility wrapper for the source-correct BP OPE packet."""

    fs = bp_primary_ope_normal_form(k)
    return {
        "is_n2_sca": False,
        "is_feigin_semikhatov_bp": True,
        "all_generators_even": True,
        "j_level": simplify(fs["J_level"]),
        "g_pairing": simplify(fs["G_pairing"]),
        "g_j_coefficient": simplify(fs["GJ_coefficient"]),
        "jj_coefficient": fs["JJ_coefficient"],
        "dJ_coefficient": simplify(fs["dJ_coefficient"]),
        "T_coefficient": simplify(fs["T_coefficient"]),
        "charge_conservation": True,
        "central_charge": simplify(fs["central_charge"]),
        "convention": fs["convention"],
    }


def verify_sl3_subregular_bar() -> Dict[str, bool]:
    """Verify every certified input and every open-status firewall."""

    dual = bp_koszul_dual()
    ds = ds_bar_intertwining()
    bar = bar_spectral_sequence_e1()
    shadow = shadow_depth_classification()
    return {
        "standard_central_charge": simplify(
            bp_central_charge(k)
            + ((2 * k + 3) * (3 * k + 1)) / (k + 3)
        ) == 0,
        "standard_central_conductor_50": simplify(bp_koszul_conductor() - 50) == 0,
        "shifted_conductor_196_is_separate": simplify(
            bp_shifted_central_charge(k)
            + bp_shifted_central_charge(bp_dual_level(k))
            - 196
        ) == 0,
        "four_generators_all_even": len(GENERATORS) == 4 and all(
            datum["parity"] == 0 for datum in GENERATORS.values()
        ),
        "reciprocal_weight_diagnostic_17_6": (
            bp_reciprocal_weight_diagnostic() == Rational(17, 6)
        ),
        "parameter_involution": simplify(bp_dual_level(bp_dual_level(k)) - k) == 0,
        "same_family_duality_conditional": (
            dual["same_family_duality_status"] == "conditional-H_BP_DS_bar"
        ),
        "DS_total_shift": ds["total_shift_check"],
        "bar_collapse_withheld": bar["collapses_at"] is None,
        "shadow_class_withheld": shadow["generic_class"] is None,
        "kappa_withheld": kappa_all_paths_agree()["all_agree"] is None,
    }


def main() -> None:
    """Print exact certificates and the remaining bar obligation."""

    print("sl_3 minimal/subregular BP bar audit")
    for name, passed in verify_sl3_subregular_bar().items():
        print(f"  {name}: {passed}")
    print(f"  obligation: {BP_BAR_RESOLUTION_OBLIGATION}")


if __name__ == "__main__":
    main()
