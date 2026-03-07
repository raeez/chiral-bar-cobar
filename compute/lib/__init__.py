"""Chiral bar-cobar compute engine.

Core types and algebra constructors for the monograph's computational kernel.

Usage:
    from compute.lib import OPEAlgebra, Generator
    from compute.lib import heisenberg_algebra, sl2_algebra, virasoro_algebra
    from compute.lib import GradedVectorSpace, ChainComplex
"""

# Core types
from compute.lib.utils import GradedVectorSpace, ChainComplex, partition_number, lambda_fp, F_g
from compute.lib.bar_complex import OPEAlgebra, Generator

# Standard algebra constructors
from compute.lib.bar_complex import (
    heisenberg_algebra,
    sl2_algebra,
    virasoro_algebra,
    free_fermion_algebra,
)

# Lie algebra data
from compute.lib.lie_algebra import cartan_data, sugawara_c, ff_dual_level, kappa_km

# Cross-algebra registry
from compute.lib.cross_algebra import ALGEBRA_REGISTRY

# Bar cohomology dimensions (known values)
from compute.lib.bar_complex import KNOWN_BAR_DIMS, verify_bar_dim

# Koszul dual Hilbert series
from compute.lib.koszul_hilbert import quadratic_dual_dims, verify_koszul, riordan, motzkin

# Orlik-Solomon algebra
from compute.lib.os_algebra import os_dimension, os_basis, residue_map

# Pronilpotent weight-filtered completion (MC4 scaffold)
from compute.lib.pronilpotent_bar import (
    max_bar_degree,
    effective_generator_weights,
    w_infinity_generator_weights,
    ordered_weight_monomials,
    weight_sector_profile,
    degree_sector_dimension_formula,
    total_sector_dimension_formula,
    w_infinity_weight_sector,
    verify_w_infinity_completion,
)

# Truncated W_infinity structural OPE scaffold (MC4 / Tool 8.2)
from compute.lib.w_infinity_ope import (
    TruncatedWinfinityOPE,
    verify_truncated_w_infinity_ope,
)
from compute.lib.w_infinity_support_complex import (
    TruncatedWinfinitySupportComplex,
    verify_w_infinity_support_complex,
)

# Non-principal DS orbit scaffold (hook/subregular frontier)
from compute.lib.nonprincipal_ds_orbits import (
    TRACK_CORE_PRINCIPAL,
    TRACK_FRONTIER_NONPRINCIPAL,
    STATUS_PROVED_SUBREGULAR_SL3,
    STATUS_HOOK_EVIDENCE,
    STATUS_PROGRAMME,
    OrbitDualityCase,
    normalize_partition,
    partition_size,
    transpose_partition,
    is_hook_partition,
    hook_partition,
    subregular_partition,
    type_a_bv_dual,
    hook_dual_partition,
    type_a_orbit_class,
    centralizer_dimension_sl_n,
    orbit_dimension_sl_n,
    principal_ff_level_shift_type_a,
    nonprincipal_hook_level_shift_ansatz_type_a,
    nonprincipal_hook_case,
    nonprincipal_hook_cases,
    verify_nonprincipal_ds_orbit_scaffold,
)

# BV duality + non-principal DS seed reductions
from compute.lib.bv_duality import (
    BVDualOrbit,
    STATUS_EXACT_TYPE_A,
    STATUS_HOOK_FRONTIER,
    type_a_bv_dual,
    is_type_a_self_dual_orbit,
    type_a_bv_pair,
    type_a_hook_bv_pair,
    first_nonselfdual_type_a_hook_pair,
    verify_bv_duality_scaffold,
)
from compute.lib.nonprincipal_ds_reduction import (
    NonprincipalDSSeed,
    bp_dual_level,
    bp_residual_sl2_level,
    bp_residual_sl2_dual_relation,
    bp_central_charge,
    bp_complementarity_sum,
    bp_complementarity_constant,
    bp_curvature_proxy,
    bp_curvature_dual_relation,
    sl3_subregular_good_grading_multiplicities,
    bp_current_presentation,
    bp_strong_presentation,
    sl3_subregular_bp_seed,
    first_nonselfdual_hook_seed,
    verify_nonprincipal_ds_reduction_seed,
)
from compute.lib.nonprincipal_ds_normalization import (
    CentralChargeConvention,
    RAW_BP_CONVENTION,
    CHAPTER_BP_SUM_CONVENTION,
    bp_dual_sum_under_convention,
    shift_to_target_dual_sum,
    bp_shift_to_target_sum,
    bp_shifted_convention_for_target,
    verify_nonprincipal_ds_normalization,
)
from compute.lib.ds_reduction import (
    Sl2TripleSeed,
    DSGhostWeight,
    DSReductionSeed,
    TruncatedBRSTComplex,
    HookPairDSComplexSeed,
    DSBasisElement,
    DSConstraint,
    DSBRSTBlueprint,
    STATUS_DS_SEED,
    brst_ghost_weights,
    exterior_basis_indices,
    character_wedge_differential,
    build_character_wedge_complex,
    differential_square_blocks,
    complex_has_nilpotent_differential,
    sl3_subregular_sl2_triple,
    sl3_subregular_basis_grades,
    sl3_subregular_basis_profile,
    sl3_subregular_positive_grades,
    sl3_subregular_ghost_profile,
    sl3_subregular_constraint_character,
    sl3_subregular_constraints,
    sl3_subregular_positive_nilpotent_brackets,
    sl3_subregular_ds_seed,
    sl3_subregular_truncated_brst_complex,
    first_nonselfdual_hook_pair_ds_seed,
    sl3_subregular_brst_blueprint,
    verify_ds_reduction_seed,
)

__all__ = [
    # Types
    "GradedVectorSpace", "ChainComplex", "OPEAlgebra", "Generator",
    # Algebra constructors
    "heisenberg_algebra", "sl2_algebra", "virasoro_algebra", "free_fermion_algebra",
    # Lie algebra
    "cartan_data", "sugawara_c", "ff_dual_level", "kappa_km",
    # Registry
    "ALGEBRA_REGISTRY", "KNOWN_BAR_DIMS", "verify_bar_dim",
    # Koszul dual
    "quadratic_dual_dims", "verify_koszul", "riordan", "motzkin",
    # Orlik-Solomon
    "os_dimension", "os_basis", "residue_map",
    # Pronilpotent completion
    "max_bar_degree", "effective_generator_weights",
    "w_infinity_generator_weights", "ordered_weight_monomials",
    "weight_sector_profile", "degree_sector_dimension_formula",
    "total_sector_dimension_formula", "w_infinity_weight_sector",
    "verify_w_infinity_completion",
    # Truncated W_infinity OPE
    "TruncatedWinfinityOPE", "verify_truncated_w_infinity_ope",
    # Truncated W_infinity support complex
    "TruncatedWinfinitySupportComplex", "verify_w_infinity_support_complex",
    # Non-principal DS orbit scaffold
    "TRACK_CORE_PRINCIPAL", "TRACK_FRONTIER_NONPRINCIPAL",
    "STATUS_PROVED_SUBREGULAR_SL3", "STATUS_HOOK_EVIDENCE", "STATUS_PROGRAMME",
    "OrbitDualityCase", "normalize_partition", "partition_size",
    "transpose_partition", "is_hook_partition", "hook_partition",
    "subregular_partition", "type_a_bv_dual", "hook_dual_partition",
    "type_a_orbit_class", "centralizer_dimension_sl_n", "orbit_dimension_sl_n",
    "principal_ff_level_shift_type_a", "nonprincipal_hook_level_shift_ansatz_type_a",
    "nonprincipal_hook_case", "nonprincipal_hook_cases",
    "verify_nonprincipal_ds_orbit_scaffold",
    # BV duality scaffold
    "BVDualOrbit", "STATUS_EXACT_TYPE_A", "STATUS_HOOK_FRONTIER",
    "type_a_bv_dual", "is_type_a_self_dual_orbit", "type_a_bv_pair",
    "type_a_hook_bv_pair", "first_nonselfdual_type_a_hook_pair",
    "verify_bv_duality_scaffold",
    # Non-principal DS seed reductions
    "NonprincipalDSSeed", "bp_dual_level", "bp_central_charge",
    "bp_residual_sl2_level", "bp_residual_sl2_dual_relation",
    "bp_complementarity_sum", "bp_complementarity_constant",
    "bp_curvature_proxy", "bp_curvature_dual_relation",
    "sl3_subregular_good_grading_multiplicities",
    "bp_current_presentation", "bp_strong_presentation",
    "sl3_subregular_bp_seed", "first_nonselfdual_hook_seed",
    "verify_nonprincipal_ds_reduction_seed",
    # Non-principal DS normalization bridge
    "CentralChargeConvention", "RAW_BP_CONVENTION", "CHAPTER_BP_SUM_CONVENTION",
    "bp_dual_sum_under_convention", "shift_to_target_dual_sum",
    "bp_shift_to_target_sum", "bp_shifted_convention_for_target",
    "verify_nonprincipal_ds_normalization",
    # DS reduction seed scaffold
    "Sl2TripleSeed", "DSGhostWeight", "DSReductionSeed",
    "TruncatedBRSTComplex", "HookPairDSComplexSeed",
    "DSBasisElement", "DSConstraint", "DSBRSTBlueprint", "STATUS_DS_SEED",
    "brst_ghost_weights", "exterior_basis_indices", "character_wedge_differential",
    "build_character_wedge_complex", "differential_square_blocks",
    "complex_has_nilpotent_differential", "sl3_subregular_sl2_triple",
    "sl3_subregular_basis_grades", "sl3_subregular_basis_profile",
    "sl3_subregular_positive_grades", "sl3_subregular_ghost_profile",
    "sl3_subregular_constraint_character", "sl3_subregular_constraints",
    "sl3_subregular_positive_nilpotent_brackets",
    "sl3_subregular_ds_seed", "sl3_subregular_truncated_brst_complex",
    "first_nonselfdual_hook_pair_ds_seed", "sl3_subregular_brst_blueprint",
    "verify_ds_reduction_seed",
    # Utility
    "partition_number", "lambda_fp", "F_g",
]
