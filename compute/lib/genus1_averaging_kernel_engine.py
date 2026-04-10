r"""Genus-1 averaging-kernel toy engine for the F08 evidence surface.

This module gives a finite-dimensional matrix model for the conjectural claim
that the genus-1 averaging kernel at arity 2 for sl_2 is strictly larger than
its genus-0 counterpart once quasi-modular sectors are present.

Model summary
-------------
Genus 0:
  Domain = g \otimes g with g = sl_2, dim g = 3, so dim = 9.
  Averaging = Sigma_2 symmetrization on the ordered arity-2 bar sector:
      av_0 = (I + P) / 2
  where P swaps tensor factors.  Its kernel is the antisymmetric subspace.

Genus 1:
  Domain = (g \otimes g) \otimes span{1, E_2*, E_4, E_6}, dim = 36.
  The sectors 1, E_4, E_6 use the same averaging operator av_0.
  The E_2* sector is modified by a toy anomaly operator supported on the
  diagonal symmetric tensors ee, ff, hh:
      av_{E_2*} = av_0 - D_diag
  where D_diag projects onto span{e⊗e, f⊗f, h⊗h}.  This forces three extra
  null directions in the quasi-modular sector while leaving a concrete matrix
  computation.  The resulting genus-1 kernel dimension is 15 in this model.

This is computational evidence for an enlarged kernel, not a proof of F08.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

import numpy as np


SL2_BASIS: Tuple[str, str, str] = ("e", "f", "h")
QUASI_MODULAR_SECTORS: Tuple[str, str, str, str] = ("1", "E2*", "E4", "E6")


@dataclass(frozen=True)
class Genus1AveragingKernelResult:
    genus0_domain_dim: int
    genus0_kernel_dim: int
    genus0_image_dim: int
    genus1_domain_dim: int
    genus1_kernel_dim: int
    genus1_image_dim: int
    kernel_enlargement: int
    quasi_modular_sectors: Tuple[str, ...]


def _ordered_tensor_basis() -> Tuple[Tuple[str, str], ...]:
    return tuple((a, b) for a in SL2_BASIS for b in SL2_BASIS)


def _transposition_matrix() -> np.ndarray:
    """Permutation matrix for a⊗b -> b⊗a on g⊗g."""
    basis = _ordered_tensor_basis()
    index = {pair: i for i, pair in enumerate(basis)}
    matrix = np.zeros((len(basis), len(basis)), dtype=float)
    for col, pair in enumerate(basis):
        row = index[(pair[1], pair[0])]
        matrix[row, col] = 1.0
    return matrix


def _diagonal_anomaly_projector() -> np.ndarray:
    """Projector onto span{e⊗e, f⊗f, h⊗h} inside g⊗g."""
    basis = _ordered_tensor_basis()
    matrix = np.zeros((len(basis), len(basis)), dtype=float)
    for i, pair in enumerate(basis):
        if pair[0] == pair[1]:
            matrix[i, i] = 1.0
    return matrix


def genus0_averaging_matrix() -> np.ndarray:
    """Genus-0 averaging matrix on g⊗g."""
    swap = _transposition_matrix()
    identity = np.eye(swap.shape[0], dtype=float)
    return 0.5 * (identity + swap)


def genus1_averaging_matrix() -> np.ndarray:
    """Genus-1 averaging matrix on (g⊗g)⊗span{1,E2*,E4,E6}."""
    genus0 = genus0_averaging_matrix()
    anomaly_block = genus0 - _diagonal_anomaly_projector()
    zero = np.zeros_like(genus0)
    return np.block(
        [
            [genus0, zero, zero, zero],
            [zero, anomaly_block, zero, zero],
            [zero, zero, genus0, zero],
            [zero, zero, zero, genus0],
        ]
    )


def _matrix_rank(matrix: np.ndarray, tol: float = 1e-9) -> int:
    return int(np.linalg.matrix_rank(matrix, tol=tol))


def compute_genus1_averaging_kernel() -> Genus1AveragingKernelResult:
    """Compute domain, image, and kernel dimensions for the toy model."""
    genus0_matrix = genus0_averaging_matrix()
    genus1_matrix = genus1_averaging_matrix()

    genus0_domain_dim = int(genus0_matrix.shape[1])
    genus0_image_dim = _matrix_rank(genus0_matrix)
    genus0_kernel_dim = genus0_domain_dim - genus0_image_dim

    genus1_domain_dim = int(genus1_matrix.shape[1])
    genus1_image_dim = _matrix_rank(genus1_matrix)
    genus1_kernel_dim = genus1_domain_dim - genus1_image_dim

    return Genus1AveragingKernelResult(
        genus0_domain_dim=genus0_domain_dim,
        genus0_kernel_dim=genus0_kernel_dim,
        genus0_image_dim=genus0_image_dim,
        genus1_domain_dim=genus1_domain_dim,
        genus1_kernel_dim=genus1_kernel_dim,
        genus1_image_dim=genus1_image_dim,
        kernel_enlargement=genus1_kernel_dim - genus0_kernel_dim,
        quasi_modular_sectors=QUASI_MODULAR_SECTORS,
    )


if __name__ == "__main__":
    print(compute_genus1_averaging_kernel())
