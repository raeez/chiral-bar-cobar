"""Coefficient-free support skeleton for the truncated W_infinity bar differential.

The actual completed bar differential for W_infinity depends on higher-spin
structure constants that are not yet implemented. This module records the
support combinatorics forced by the structural OPE scaffold:

  - source basis: truncated generator-weight words in fixed total weight;
  - target basis: lower-weight truncated words together with the vacuum word;
  - matrix entries: 1 when a target word can appear from some adjacent singular
    merge, 0 otherwise.

This is enough to verify continuity and finite support of the completed
differential on each finite-weight truncation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

from sympy import Matrix, zeros

from compute.lib.w_infinity_ope import TruncatedWinfinityOPE, WeightWord
from compute.lib.pronilpotent_bar import w_infinity_weight_sector


@dataclass(frozen=True)
class TruncatedWinfinitySupportComplex:
    """Support-level completed bar skeleton for truncated W_infinity."""

    max_spin: int

    def __post_init__(self):
        object.__setattr__(self, "ope", TruncatedWinfinityOPE(self.max_spin))

    def weight_sector_basis(self, total_weight: int) -> Tuple[WeightWord, ...]:
        """All truncated weight words of total conformal weight `total_weight`."""
        basis: List[WeightWord] = []
        for degree in sorted(w_infinity_weight_sector(total_weight)):
            for word in w_infinity_weight_sector(total_weight)[degree]:
                if all(spin <= self.max_spin for spin in word):
                    basis.append(word)
        return tuple(basis)

    def lower_weight_target_basis(self, total_weight: int) -> Tuple[WeightWord, ...]:
        """Vacuum plus all truncated words of smaller total weight."""
        basis: List[WeightWord] = [()]
        for lower in range(2, total_weight):
            basis.extend(self.weight_sector_basis(lower))
        return tuple(basis)

    def support_targets(self, word: WeightWord) -> Tuple[WeightWord, ...]:
        """All distinct support targets reachable by one adjacent singular merge."""
        targets = []
        seen = set()
        for position in range(len(word) - 1):
            for out in self.ope.adjacent_truncated_singular_outputs(word, position):
                if out not in seen:
                    seen.add(out)
                    targets.append(out)
        return tuple(targets)

    def support_matrix_at_weight(
        self,
        total_weight: int,
    ) -> Tuple[Tuple[WeightWord, ...], Tuple[WeightWord, ...], Matrix]:
        """Support matrix from weight `total_weight` sources to all lower-weight targets."""
        source_basis = self.weight_sector_basis(total_weight)
        target_basis = self.lower_weight_target_basis(total_weight)
        target_index = {word: idx for idx, word in enumerate(target_basis)}
        matrix = zeros(len(target_basis), len(source_basis))

        for col, source in enumerate(source_basis):
            for target in self.support_targets(source):
                row = target_index[target]
                matrix[row, col] = 1

        return source_basis, target_basis, matrix

    def support_profile(self, total_weight: int) -> Dict[str, int]:
        """Size data for the finite-weight support skeleton."""
        source_basis, target_basis, matrix = self.support_matrix_at_weight(total_weight)
        edge_count = sum(1 for entry in matrix if entry != 0)
        return {
            "source_size": len(source_basis),
            "target_size": len(target_basis),
            "edge_count": edge_count,
        }


def verify_w_infinity_support_complex(
    max_spin: int = 6,
    max_total_weight: int = 8,
) -> Dict[str, bool]:
    """Verification bundle for the support-level completed-bar skeleton."""
    complex_ = TruncatedWinfinitySupportComplex(max_spin=max_spin)
    results: Dict[str, bool] = {}

    for total_weight in range(4, max_total_weight + 1):
        source_basis, target_basis, matrix = complex_.support_matrix_at_weight(total_weight)
        results[f"weight {total_weight} source basis finite"] = len(source_basis) < 10 ** 6
        results[f"weight {total_weight} target basis finite"] = len(target_basis) < 10 ** 6
        results[f"weight {total_weight} support matrix shape"] = (
            matrix.rows == len(target_basis) and matrix.cols == len(source_basis)
        )
        for col, source in enumerate(source_basis):
            targets = [
                target_basis[row]
                for row in range(matrix.rows)
                if matrix[row, col] != 0
            ]
            results[f"weight {total_weight} source {source} drops weight"] = all(
                sum(target) <= total_weight - 1 for target in targets
            )

    source_basis, target_basis, matrix = complex_.support_matrix_at_weight(4)
    source_index = {word: idx for idx, word in enumerate(source_basis)}
    target_index = {word: idx for idx, word in enumerate(target_basis)}
    expected = {(), (2,), (3,)}
    actual = {
        target_basis[row]
        for row in range(matrix.rows)
        if matrix[row, source_index[(2, 2)]] != 0
    }
    results["weight 4 pair (2,2) support"] = actual == expected

    return results
