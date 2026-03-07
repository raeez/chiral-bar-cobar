"""Structural OPE scaffold for truncated W_infinity.

This module does not attempt to encode the full Prochazka-Rapcak structure
constants. It packages the part that is already rigid from conformal data and
that is needed for the completed-bar programme:

  - generators W_s of spins s = 2, ..., N in a finite truncation;
  - the exact stress-tensor OPE with primary generators;
  - coarse singular-support bounds for higher-spin/higher-spin products;
  - adjacent-merge maps on generator-weight words, compatible with the
    pronilpotent weight filtration.

The key continuity fact is that every singular adjacent merge lowers total
conformal weight by at least one. For the Virasoro generator W_2 = T this is
exact; for higher-spin pairs it is a structural upper bound.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

from sympy import Rational, Symbol, sympify

from compute.lib.bar_complex import Generator
from compute.lib.pronilpotent_bar import w_infinity_weight_sector


WeightWord = Tuple[int, ...]


@dataclass(frozen=True)
class TruncatedWinfinityOPE:
    """Finite-spin structural model for W_infinity."""

    max_spin: int
    central_charge: object = Symbol("c")

    def __post_init__(self):
        if self.max_spin < 2:
            raise ValueError("max_spin must be at least 2")
        object.__setattr__(self, "central_charge", sympify(self.central_charge))

    @property
    def generator_spins(self) -> Tuple[int, ...]:
        return tuple(range(2, self.max_spin + 1))

    @property
    def generators(self) -> List[Generator]:
        return [
            Generator(f"W_{spin}", weight=spin, index=spin - 2)
            for spin in self.generator_spins
        ]

    def has_generator(self, spin: int) -> bool:
        return 2 <= spin <= self.max_spin

    def stress_tensor_ope(self, spin: int) -> Dict[int, Dict[str, object]]:
        """Exact T(z)W_s(w) singular terms for primary W_s."""
        if not self.has_generator(spin):
            raise ValueError(f"spin {spin} outside truncation")

        if spin == 2:
            return {
                4: {"1": self.central_charge / 2},
                2: {"W_2": Rational(2)},
                1: {"dW_2": Rational(1)},
            }

        return {
            2: {f"W_{spin}": Rational(spin)},
            1: {f"dW_{spin}": Rational(1)},
        }

    @staticmethod
    def nth_product_weight(left_spin: int, right_spin: int, product_index: int) -> int:
        """Conformal weight of the product a_(n)b."""
        return left_spin + right_spin - product_index - 1

    def exact_stress_tensor_output_weights(self, spin: int) -> Tuple[int, ...]:
        """Conformal weights appearing in the exact singular T*W_s OPE."""
        if spin == 2:
            return (0, 2, 3)
        return (spin, spin + 1)

    def truncated_singular_output_weights(
        self,
        left_spin: int,
        right_spin: int,
    ) -> Tuple[int, ...]:
        """Conservative weight support for the singular OPE.

        Exact when one input is the stress tensor. For higher-spin pairs this
        returns the generator-weight window compatible with conformal weight and
        the finite-spin truncation.
        """
        if not self.has_generator(left_spin) or not self.has_generator(right_spin):
            raise ValueError("input spin outside truncation")

        if left_spin == 2:
            return tuple(
                weight
                for weight in self.exact_stress_tensor_output_weights(right_spin)
                if weight == 0 or weight <= self.max_spin
            )
        if right_spin == 2:
            return tuple(
                weight
                for weight in self.exact_stress_tensor_output_weights(left_spin)
                if weight == 0 or weight <= self.max_spin
            )

        upper = min(self.max_spin, left_spin + right_spin - 1)
        return tuple(range(2, upper + 1))

    def adjacent_truncated_singular_outputs(
        self,
        word: WeightWord,
        position: int,
    ) -> Tuple[WeightWord, ...]:
        """All truncated singular outputs from merging a chosen adjacent pair.

        A vacuum output is represented by removing the pair entirely. Positive
        weights are represented by a single merged entry.
        """
        if position < 0 or position >= len(word) - 1:
            raise IndexError("position must choose an adjacent pair")

        left_spin = word[position]
        right_spin = word[position + 1]
        prefix = word[:position]
        suffix = word[position + 2 :]

        outputs = []
        for weight in self.truncated_singular_output_weights(left_spin, right_spin):
            if weight == 0:
                outputs.append(prefix + suffix)
            else:
                outputs.append(prefix + (weight,) + suffix)

        return tuple(outputs)

    def degree_two_inputs_at_weight(self, total_weight: int) -> Tuple[WeightWord, ...]:
        """Degree-two generator inputs in fixed total weight."""
        sector = w_infinity_weight_sector(total_weight)
        return sector.get(2, ())

    def degree_two_output_profile(self, total_weight: int) -> Dict[WeightWord, Tuple[WeightWord, ...]]:
        """Truncated singular outputs for all degree-two inputs of weight `total_weight`."""
        return {
            pair: self.adjacent_truncated_singular_outputs(pair, 0)
            for pair in self.degree_two_inputs_at_weight(total_weight)
            if all(self.has_generator(spin) for spin in pair)
        }


def verify_truncated_w_infinity_ope(
    max_spin: int = 6,
    max_total_weight: int = 8,
) -> Dict[str, bool]:
    """Verification bundle for the truncated W_infinity structural scaffold."""
    model = TruncatedWinfinityOPE(max_spin=max_spin)
    results: Dict[str, bool] = {}

    for spin in model.generator_spins:
        ope = model.stress_tensor_ope(spin)
        if spin == 2:
            results["T*T quartic pole"] = ope[4]["1"] == model.central_charge / 2
            results["T*T double pole coefficient"] = ope[2]["W_2"] == 2
            results["T*T simple pole derivative"] = ope[1]["dW_2"] == 1
        else:
            results[f"T*W_{spin} double pole coefficient"] = ope[2][f"W_{spin}"] == spin
            results[f"T*W_{spin} simple pole derivative"] = ope[1][f"dW_{spin}"] == 1

    for total_weight in range(4, max_total_weight + 1):
        for degree, words in w_infinity_weight_sector(total_weight).items():
            for word in words:
                if not all(model.has_generator(spin) for spin in word):
                    continue
                for position in range(len(word) - 1):
                    outputs = model.adjacent_truncated_singular_outputs(word, position)
                    results[
                        f"weight {total_weight} word {word} pos {position} has finite outputs"
                    ] = len(outputs) > 0
                    results[
                        f"weight {total_weight} word {word} pos {position} lowers total weight"
                    ] = all(sum(out) <= total_weight - 1 for out in outputs)
                    results[
                        f"weight {total_weight} word {word} pos {position} stays in truncation"
                    ] = all(all(spin <= max_spin for spin in out) for out in outputs)

    return results
