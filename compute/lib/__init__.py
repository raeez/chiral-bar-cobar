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
    # Utility
    "partition_number", "lambda_fp", "F_g",
]
