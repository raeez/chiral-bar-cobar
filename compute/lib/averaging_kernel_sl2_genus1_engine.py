"""SymPy engine for the genus-1 sl2 averaging kernel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Mapping, Tuple

import sympy as sp

SL2_BASIS: Tuple[str, str, str] = ("e", "f", "h")
TENSOR_BASIS: Tuple[Tuple[str, str], ...] = tuple(
    (left, right) for left in SL2_BASIS for right in SL2_BASIS
)
TENSOR_DIM = len(TENSOR_BASIS)
SL2_DIM = len(SL2_BASIS)
SL2_DUAL_COXETER = sp.Integer(2)
SL2_SYMMETRIC_DIM = SL2_DIM * (SL2_DIM + 1) // 2
SL2_ANTISYMMETRIC_DIM = SL2_DIM * (SL2_DIM - 1) // 2
SL2_CASIMIR_AVERAGE_WEIGHT = sp.Rational(SL2_DIM, 2 * SL2_DUAL_COXETER)
SL2_SUGAWARA_SHIFT = sp.Rational(SL2_DIM, 2)

Z = sp.Symbol("z")
K = sp.Symbol("k")
ZETA = sp.Function("zeta")

_BASIS_INDEX: Dict[Tuple[str, str], int] = {
    basis_element: position for position, basis_element in enumerate(TENSOR_BASIS)
}


@dataclass(frozen=True)
class AveragingKernelSL2Genus1Result:
    tensor_dim: int
    symmetric_dim: int
    antisymmetric_dim: int
    projector_rank: int
    kernel_dim: int
    casimir_average_weight: sp.Expr
    sugawara_shift: sp.Expr


def zero_tensor() -> sp.Matrix:
    return sp.zeros(TENSOR_DIM, 1)


def tensor_vector(coefficients: Mapping[Tuple[str, str], sp.Expr]) -> sp.Matrix:
    vector = zero_tensor()
    for basis_element, coefficient in coefficients.items():
        if basis_element not in _BASIS_INDEX:
            raise KeyError(f"Unknown tensor basis element: {basis_element}")
        vector[_BASIS_INDEX[basis_element], 0] = sp.sympify(coefficient)
    return vector


def swap_matrix() -> sp.Matrix:
    matrix = sp.zeros(TENSOR_DIM, TENSOR_DIM)
    for basis_element, column in _BASIS_INDEX.items():
        row = _BASIS_INDEX[(basis_element[1], basis_element[0])]
        matrix[row, column] = 1
    return matrix


def symmetrization_projector() -> sp.Matrix:
    identity = sp.eye(TENSOR_DIM)
    return sp.Rational(1, 2) * (identity + swap_matrix())


def antisymmetrization_projector() -> sp.Matrix:
    identity = sp.eye(TENSOR_DIM)
    return sp.Rational(1, 2) * (identity - swap_matrix())


def project_symmetric(vector: sp.Matrix) -> sp.Matrix:
    return symmetrization_projector() * vector


def project_antisymmetric(vector: sp.Matrix) -> sp.Matrix:
    return antisymmetrization_projector() * vector


def exterior_square_basis() -> Tuple[sp.Matrix, ...]:
    return (
        tensor_vector({("e", "f"): 1, ("f", "e"): -1}),
        tensor_vector({("e", "h"): 1, ("h", "e"): -1}),
        tensor_vector({("f", "h"): 1, ("h", "f"): -1}),
    )


def casimir_tensor() -> sp.Matrix:
    return tensor_vector(
        {
            ("h", "h"): sp.Rational(1, 2),
            ("e", "f"): 1,
            ("f", "e"): 1,
        }
    )


def generic_antisymmetric_part(
    a12: sp.Expr | None = None,
    a13: sp.Expr | None = None,
    a23: sp.Expr | None = None,
) -> sp.Matrix:
    a12 = sp.Symbol("a12") if a12 is None else sp.sympify(a12)
    a13 = sp.Symbol("a13") if a13 is None else sp.sympify(a13)
    a23 = sp.Symbol("a23") if a23 is None else sp.sympify(a23)
    basis_vectors = exterior_square_basis()
    return a12 * basis_vectors[0] + a13 * basis_vectors[1] + a23 * basis_vectors[2]


def elliptic_r_matrix(
    level: sp.Expr,
    z: sp.Expr = Z,
    antisymmetric_part: sp.Matrix | None = None,
) -> sp.Matrix:
    level = sp.sympify(level)
    antisymmetric_part = zero_tensor() if antisymmetric_part is None else antisymmetric_part
    return level * (ZETA(z) * casimir_tensor() + antisymmetric_part)


def symmetric_sector_of_r(
    level: sp.Expr,
    z: sp.Expr = Z,
    antisymmetric_part: sp.Matrix | None = None,
) -> sp.Matrix:
    return project_symmetric(elliptic_r_matrix(level=level, z=z, antisymmetric_part=antisymmetric_part))


def antisymmetric_sector_of_r(
    level: sp.Expr,
    z: sp.Expr = Z,
    antisymmetric_part: sp.Matrix | None = None,
) -> sp.Matrix:
    return project_antisymmetric(
        elliptic_r_matrix(level=level, z=z, antisymmetric_part=antisymmetric_part)
    )


def kappa_sl2(level: sp.Expr) -> sp.Expr:
    level = sp.sympify(level)
    return sp.Rational(3) * (level + SL2_DUAL_COXETER) / 4


def classical_average_from_symmetric_casimir(level: sp.Expr) -> sp.Expr:
    level = sp.sympify(level)
    return sp.simplify(SL2_CASIMIR_AVERAGE_WEIGHT * level)


def affine_genus1_average(level: sp.Expr) -> sp.Expr:
    level = sp.sympify(level)
    return sp.simplify(classical_average_from_symmetric_casimir(level) + SL2_SUGAWARA_SHIFT)


def averaging_map_of_elliptic_r_matrix(
    level: sp.Expr,
    z: sp.Expr = Z,
    antisymmetric_part: sp.Matrix | None = None,
) -> sp.Expr:
    symmetric_sector = symmetric_sector_of_r(level=level, z=z, antisymmetric_part=antisymmetric_part)
    expected_sector = sp.sympify(level) * ZETA(z) * casimir_tensor()
    if not is_zero_tensor(symmetric_sector - expected_sector):
        raise ValueError("The symmetric sector is not the Casimir sector of the elliptic sl2 r-matrix.")
    return affine_genus1_average(level)


def summarize_averaging_kernel() -> AveragingKernelSL2Genus1Result:
    projector = symmetrization_projector()
    return AveragingKernelSL2Genus1Result(
        tensor_dim=TENSOR_DIM,
        symmetric_dim=SL2_SYMMETRIC_DIM,
        antisymmetric_dim=SL2_ANTISYMMETRIC_DIM,
        projector_rank=int(projector.rank()),
        kernel_dim=TENSOR_DIM - int(projector.rank()),
        casimir_average_weight=SL2_CASIMIR_AVERAGE_WEIGHT,
        sugawara_shift=SL2_SUGAWARA_SHIFT,
    )


def is_zero_tensor(vector: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in vector)


def supports_level_prefix(vector: sp.Matrix, level: sp.Expr = K) -> bool:
    level = sp.sympify(level)
    return all(sp.simplify(entry) == 0 or sp.factor(entry).has(level) for entry in vector)


__all__ = [
    "AveragingKernelSL2Genus1Result",
    "K",
    "SL2_ANTISYMMETRIC_DIM",
    "SL2_BASIS",
    "SL2_CASIMIR_AVERAGE_WEIGHT",
    "SL2_DIM",
    "SL2_DUAL_COXETER",
    "SL2_SUGAWARA_SHIFT",
    "SL2_SYMMETRIC_DIM",
    "TENSOR_BASIS",
    "TENSOR_DIM",
    "Z",
    "ZETA",
    "affine_genus1_average",
    "averaging_map_of_elliptic_r_matrix",
    "antisymmetric_sector_of_r",
    "antisymmetrization_projector",
    "casimir_tensor",
    "classical_average_from_symmetric_casimir",
    "elliptic_r_matrix",
    "exterior_square_basis",
    "generic_antisymmetric_part",
    "is_zero_tensor",
    "kappa_sl2",
    "project_antisymmetric",
    "project_symmetric",
    "summarize_averaging_kernel",
    "supports_level_prefix",
    "swap_matrix",
    "symmetric_sector_of_r",
    "symmetrization_projector",
    "tensor_vector",
    "zero_tensor",
]
