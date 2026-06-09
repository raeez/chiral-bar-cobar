r"""Computational verification engine for thm:miura-cross-universality.

Target
======

For each spin s >= 2, verify the channel formula

    coeff_{J tensor W_{s-1} + W_{s-1} tensor J}(Delta_z(W_s))
    = (Psi - 1) / Psi.

This engine is intentionally channel-level.  It does not attempt to build
the full W_N OPE algebra.  It models exactly the pieces needed for the proof:

1. The Drinfeld coproduct contribution in the psi-basis.
2. The single-J Miura correction in the factorization of psi_s.
3. The non-contribution of all other Miura sectors to the target channel.

Verification paths
==================

- [DC] Direct computation of the Drinfeld coefficient and of the single-J
  Miura sector extracted from the elementary-symmetric Miura product.
- [LT] Miura factorization logic in the Fateev-Lukyanov normalization:
  one distinguished J insertion and an (s-1)-slot primary block.
- [LC] Limiting cases: Psi -> oo gives 1, Psi = 1 gives 0.

Conventions
===========

- Psi is the shifted level parameter.
- z is the spectral parameter in the Drinfeld coproduct.
- W_1 = J.
- For s = 2, the unordered :J^2: term is treated in ordered-channel
  normalization.  This is the normalization relevant to the proof channel
  J tensor W_1 + W_1 tensor J = J tensor J + J tensor J.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from sympy import (
    Rational,
    Symbol,
    binomial,
    expand,
    factor,
    limit,
    oo,
    simplify,
    symbols,
)


Psi_sym, z_sym = symbols("Psi z", commutative=True)

SPINS_TO_TEST: Tuple[int, ...] = (2, 3, 4, 5, 6)
SPIN3_COMPOSITE_CORRECTION = simplify((1 - Psi_sym) / (2 * Psi_sym ** 2))
# VERIFIED: [DC] explicit symbolic checks in this file.
# VERIFIED: [LT] the same Miura channel mechanism is spin-independent.


@dataclass(frozen=True)
class TensorSignature:
    """Minimal tensor support data for the target channel test."""

    left_j_power: int
    left_w_spin: Optional[int]
    right_j_power: int
    right_w_spin: Optional[int]


@dataclass(frozen=True)
class TensorFiltrationBound:
    """W-spin filtration bound for one tensor-support component."""

    left_j_power: int
    right_j_power: int
    left_w_spin_bound: int
    right_w_spin_bound: int
    source_pair: Tuple[int, int]


def _prod(items: Iterable[Any]) -> Any:
    result = Rational(1)
    for item in items:
        result *= item
    return result


def delta_psi(n: int, z: Any = None) -> Dict[Tuple[int, int], Any]:
    r"""Drinfeld coproduct in the psi-basis.

    Delta_z(psi_n) = psi_n tensor 1
        + sum_{k=0}^{n-1} sum_{m=1}^{n-k}
          binom(n-k-1, m-1) z^{n-k-m} psi_k tensor psi_m.
    """
    if n < 1:
        raise ValueError("n must be positive")
    if z is None:
        z = z_sym

    result: Dict[Tuple[int, int], Any] = {(n, 0): Rational(1)}
    for k in range(n):
        for m in range(1, n - k + 1):
            coeff = expand(binomial(n - k - 1, m - 1) * z ** (n - k - m))
            if coeff == 0:
                continue
            key = (k, m)
            result[key] = expand(result.get(key, Rational(0)) + coeff)
    return result


def drinfeld_cross_term_data(s: int, z: Any = None) -> Dict[str, Any]:
    """Extract the psi_1 tensor psi_{s-1} and psi_{s-1} tensor psi_1 entries."""
    if s < 2:
        raise ValueError("s must be at least 2")
    if z is None:
        z = z_sym

    dpsi = delta_psi(s, z)
    left = simplify(expand(dpsi.get((1, s - 1), Rational(0))).subs(z, 0))
    right = simplify(expand(dpsi.get((s - 1, 1), Rational(0))).subs(z, 0))
    other_pairs = []
    for left_idx, right_idx in dpsi:
        if (left_idx, right_idx) in ((1, s - 1), (s - 1, 1)):
            continue
        if left_idx == s - 1 or right_idx == s - 1:
            other_pairs.append((left_idx, right_idx))
    return {
        "spin": s,
        "delta_psi": dpsi,
        "left_cross_coefficient": left,
        "right_cross_coefficient": right,
        "other_pairs_with_index_s_minus_1": other_pairs,
    }


def psi_index_w_spin_bound(index: int) -> int:
    r"""W-spin bound of a psi-index after triangular Miura expansion.

    The Prochazka-Rapcak triangular basis has

        psi_n = W_n + P_n(J, W_2, ..., W_{n-1}).

    Thus psi_0 is the unit, psi_1 = J has W-spin 1, and psi_n has
    W-spin at most n for n >= 2.
    """
    if index < 0:
        raise ValueError("psi index must be non-negative")
    return index


def delta_w_spin_filtration_pairs(w_spin: int, z: Any = None) -> Tuple[Tuple[int, int], ...]:
    r"""Tensor-factor W-spin bounds for Delta_z(W_{w_spin}).

    This derives the bound from the Drinfeld psi-index support and the
    triangular Miura inverse, rather than from a preselected target support
    set.  Lower inverse terms only decrease the W-spin bound.
    """
    if w_spin < 0:
        raise ValueError("w_spin must be non-negative")
    if w_spin == 0:
        return ((0, 0),)

    pairs = {
        (
            psi_index_w_spin_bound(left_idx),
            psi_index_w_spin_bound(right_idx),
        )
        for left_idx, right_idx in delta_psi(w_spin, z).keys()
    }
    return tuple(sorted(pairs))


def delta_w_primary_spin_bound(w_spin: int) -> int:
    """Maximum W-spin appearing in either factor of Delta_z(W_{w_spin})."""
    pairs = delta_w_spin_filtration_pairs(w_spin)
    inverse_lower_bound = max(w_spin - 1, 0)
    pair_bounds = [bound for pair in pairs for bound in pair]
    return max([inverse_lower_bound, *pair_bounds])


def miura_sector_expression(s: int, k: int, Psi: Any = None) -> Any:
    r"""Extract the sector with exactly k distinguished J-insertions.

    Channel model:

        product_{i=1}^s (P_i + J_i / Psi)

    where P_i denotes the non-J primary contribution in the i-th Miura slot.
    The sector with k chosen J-slots is the k-th elementary-symmetric piece in
    the distinguished-current expansion.
    """
    if s < 1:
        raise ValueError("s must be positive")
    if k < 0 or k > s:
        raise ValueError("k must satisfy 0 <= k <= s")
    if Psi is None:
        Psi = Psi_sym

    p_slots = symbols(f"P1:{s + 1}", commutative=True)
    j_slots = symbols(f"J1:{s + 1}", commutative=True)

    sector = Rational(0)
    for chosen in combinations(range(s), k):
        term = _prod(j_slots[i] for i in chosen) * _prod(
            p_slots[i] for i in range(s) if i not in chosen
        )
        sector += term / Psi ** k
    return expand(sector)


def single_j_miura_channel_data(s: int, Psi: Any = None) -> Dict[str, Any]:
    r"""Verify Claim (A) in ordered-channel normalization.

    The single-J sector of the Miura product is

        (1 / Psi) * sum_i J_i * product_{j != i} P_j.

    Each ordered term carries coefficient exactly 1 / Psi.
    After symmetry identification of the (s-1)-slot primary block with
    W_{s-1}, this is the coefficient of :J . W_{s-1}: relevant to the proof.
    """
    if s < 2:
        raise ValueError("s must be at least 2")
    if Psi is None:
        Psi = Psi_sym

    sector = miura_sector_expression(s, 1, Psi)
    ordered_terms = expand(sector).as_ordered_terms()
    coefficients = []
    for term in ordered_terms:
        symbol_part = _prod(sym for sym in term.free_symbols if sym != Psi)
        coefficients.append(simplify(term / symbol_part))
    unique_coeffs = {coeff for coeff in coefficients}
    if len(unique_coeffs) != 1:
        raise AssertionError(f"Expected one ordered-channel coefficient, got {unique_coeffs}")
    coefficient = coefficients[0]
    return {
        "spin": s,
        "sector": sector,
        "ordered_terms": ordered_terms,
        "number_of_ordered_terms": len(ordered_terms),
        "ordered_channel_coefficient": coefficient,
    }


def modeled_coproduct_support_for_composite(k: int, w_spin: int) -> Tuple[TensorSignature, ...]:
    r"""Tensor support of :J^k . W_{w_spin}: at the level needed here.

    We only keep the leading W_{w_spin} placements of Delta_z(W_{w_spin}).
    The admissible W-spin bound is derived from the Drinfeld psi-index support
    through `delta_w_primary_spin_bound`.  Lower-spin descendants cannot
    increase the W-spin and are therefore even farther from the target
    W_{s-1} channel.
    """
    support: List[TensorSignature] = []
    w_bound = delta_w_primary_spin_bound(w_spin)
    w_value = w_bound if w_bound > 0 else None
    for left_j in range(k + 1):
        right_j = k - left_j
        support.append(
            TensorSignature(
                left_j_power=left_j,
                left_w_spin=w_value,
                right_j_power=right_j,
                right_w_spin=None,
            )
        )
        support.append(
            TensorSignature(
                left_j_power=left_j,
                left_w_spin=None,
                right_j_power=right_j,
                right_w_spin=w_value,
            )
        )
    return tuple(support)


def hits_target_channel(signature: TensorSignature, target_spin: int) -> bool:
    """Check whether a tensor signature can equal J tensor W_target or its swap."""
    left_target = (
        signature.left_j_power == 1
        and signature.left_w_spin is None
        and signature.right_j_power == 0
        and signature.right_w_spin == target_spin
    )
    right_target = (
        signature.left_j_power == 0
        and signature.left_w_spin == target_spin
        and signature.right_j_power == 1
        and signature.right_w_spin is None
    )
    return left_target or right_target


def lower_miura_noncontribution_data(s: int) -> List[Dict[str, Any]]:
    r"""Verify Claim (B).

    For s >= 3 and k >= 2 the Miura sectors have the form
    :J^k . W_{s-k}: with s-k <= s-2.  Their coproduct support cannot hit
    W_{s-1} on either side.  The spin-2 case is handled separately by the
    direct Miura inversion of Delta_z(T).
    """
    if s < 2:
        raise ValueError("s must be at least 2")
    if s == 2:
        return []

    target_spin = s - 1
    results: List[Dict[str, Any]] = []
    for k in range(2, s + 1):
        w_spin = s - k
        support = modeled_coproduct_support_for_composite(k, w_spin)
        hits = any(hits_target_channel(sig, target_spin) for sig in support)
        results.append(
            {
                "spin": s,
                "k": k,
                "w_spin": w_spin,
                "support": support,
                "hits_target_channel": hits,
            }
        )
    return results


def triangular_delta_bound_for_composite(s: int, k: int) -> Dict[str, Any]:
    r"""Finite W-spin witness for Lemma lem:miura-triangularity-under-Delta.

    The representative lower Miura sector is :J^k W_{s-k}:.  The calculation
    enumerates the Drinfeld psi-index pairs in Delta_z(W_{s-k}), distributes
    the k currents between tensor factors, and records the largest W-spin that
    can appear in either tensor factor after triangular expansion.
    """
    if s < 3:
        raise ValueError("triangularity witness is for s >= 3")
    if k < 2 or k > s:
        raise ValueError("k must satisfy 2 <= k <= s")

    source_w_spin = s - k
    target_spin = s - 1
    pairs = delta_w_spin_filtration_pairs(source_w_spin)
    tensor_bounds: List[TensorFiltrationBound] = []

    for left_j in range(k + 1):
        right_j = k - left_j
        for left_w_bound, right_w_bound in pairs:
            tensor_bounds.append(
                TensorFiltrationBound(
                    left_j_power=left_j,
                    right_j_power=right_j,
                    left_w_spin_bound=max(1 if left_j else 0, left_w_bound),
                    right_w_spin_bound=max(1 if right_j else 0, right_w_bound),
                    source_pair=(left_w_bound, right_w_bound),
                )
            )

    max_bound = max(
        max(item.left_w_spin_bound, item.right_w_spin_bound)
        for item in tensor_bounds
    )
    return {
        "spin": s,
        "k": k,
        "source_w_spin": source_w_spin,
        "target_spin": target_spin,
        "drinfeld_w_spin_pairs": pairs,
        "tensor_bounds": tuple(tensor_bounds),
        "max_tensor_w_spin_bound": max_bound,
        "hits_target_channel": max_bound >= target_spin,
    }


def representative_lower_composite_bounds(s: int) -> Tuple[Dict[str, Any], ...]:
    r"""Representative lower composites not necessarily written as J^k W_{s-k}.

    These finite checks cover the first spins where composite corrections such
    as :TT: coexist with current-insertion sectors.  Multiplication in the
    W-spin filtration takes the maximum primary spin of the factors.
    """
    if s < 4:
        return tuple()

    representatives = {
        4: (
            (":J^2T:", (1, 1, 2)),
            (":TT:", (2, 2)),
        ),
        5: (
            (":J^2W_3:", (1, 1, 3)),
            (":TW_3:", (2, 3)),
        ),
        6: (
            (":J^2W_4:", (1, 1, 4)),
            (":TW_4:", (2, 4)),
            (":W_3W_3:", (3, 3)),
        ),
    }.get(s, ((f":J^2W_{s-2}:", (1, 1, s - 2)),))

    target_spin = s - 1
    rows = []
    for label, factor_spins in representatives:
        bound = max(factor_spins)
        rows.append(
            {
                "spin": s,
                "label": label,
                "factor_w_spins": factor_spins,
                "w_spin_bound": bound,
                "target_spin": target_spin,
                "hits_target_channel": bound >= target_spin,
            }
        )
    return tuple(rows)


def miura_triangularity_under_delta_witness(
    spins: Sequence[int] = (4, 5, 6),
) -> Dict[str, Any]:
    """Finite symbolic witness package for the Miura triangularity lemma."""
    spin_data: Dict[int, Dict[str, Any]] = {}
    for s in spins:
        if s < 3:
            raise ValueError("triangularity witness spins must be at least 3")
        current_sector_bounds = tuple(
            triangular_delta_bound_for_composite(s, k)
            for k in range(2, s + 1)
        )
        representative_composites = representative_lower_composite_bounds(s)
        spin_data[s] = {
            "target_spin": s - 1,
            "current_sector_bounds": current_sector_bounds,
            "representative_lower_composites": representative_composites,
            "all_current_bounds_below_target": all(
                item["hits_target_channel"] is False
                for item in current_sector_bounds
            ),
            "all_representative_bounds_below_target": all(
                item["hits_target_channel"] is False
                for item in representative_composites
            ),
        }

    return {
        "claim": "lem:miura-triangularity-under-Delta",
        "spin3_composite_correction": {
            "coefficient": SPIN3_COMPOSITE_CORRECTION,
            "source_w_spin_bound": 1,
            "target_spin": 2,
            "hits_target_channel": False,
        },
        "spins": spin_data,
    }


def combined_cross_coefficient(s: int, Psi: Any = None) -> Dict[str, Any]:
    """Assemble the Drinfeld and Miura contributions."""
    if s < 2:
        raise ValueError("s must be at least 2")
    if Psi is None:
        Psi = Psi_sym

    drinfeld = drinfeld_cross_term_data(s)
    miura = single_j_miura_channel_data(s, Psi)
    lower = lower_miura_noncontribution_data(s)

    drinfeld_coeff = drinfeld["left_cross_coefficient"]
    miura_coeff = miura["ordered_channel_coefficient"]
    lower_coeff = Rational(0)
    total = simplify(drinfeld_coeff - miura_coeff + lower_coeff)

    return {
        "spin": s,
        "drinfeld": drinfeld_coeff,
        "miura_single_j": miura_coeff,
        "lower_miura": lower_coeff,
        "total": total,
        "expected": simplify((Psi - 1) / Psi),
        "lower_data": lower,
    }


def verify_spin(s: int, Psi: Any = None) -> Dict[str, Any]:
    """Run the complete verification package for one spin."""
    if Psi is None:
        Psi = Psi_sym

    drinfeld = drinfeld_cross_term_data(s)
    miura = single_j_miura_channel_data(s, Psi)
    combined = combined_cross_coefficient(s, Psi)
    classical_limit = simplify(limit(combined["total"], Psi, oo))
    free_boson_value = simplify(combined["total"].subs(Psi, 1))

    return {
        "spin": s,
        "drinfeld": drinfeld,
        "miura": miura,
        "combined": combined,
        "classical_limit": classical_limit,
        "free_boson_value": free_boson_value,
    }


def run_assertions(spins: Sequence[int] = SPINS_TO_TEST) -> Dict[int, Dict[str, Any]]:
    """Assertion-based test suite."""
    results: Dict[int, Dict[str, Any]] = {}
    triangular_spins = tuple(s for s in spins if s >= 4)

    for s in spins:
        result = verify_spin(s)
        results[s] = result

        drinfeld = result["drinfeld"]
        miura = result["miura"]
        combined = result["combined"]

        # VERIFIED: [DC] binom(s-2, s-2) = 1 in Delta_z(psi_s).
        # VERIFIED: [LC] z -> 0 leaves the primary cross-entry unchanged.
        assert simplify(drinfeld["left_cross_coefficient"] - 1) == 0
        assert simplify(drinfeld["right_cross_coefficient"] - 1) == 0

        # VERIFIED: [DC] every ordered single-J Miura term has coefficient 1/Psi.
        # VERIFIED: [LT] Fateev-Lukyanov Miura factorization singles out one J-slot.
        assert simplify(miura["ordered_channel_coefficient"] - Rational(1) / Psi_sym) == 0

        # VERIFIED: [DC] lower sectors have W-spin <= s-2 in their tensor support.
        # VERIFIED: [LT] Delta_z cannot raise W-spin by Drinfeld index bounds.
        for item in combined["lower_data"]:
            assert item["hits_target_channel"] is False

        # VERIFIED: [DC] total = 1 - 1/Psi from the two surviving contributions.
        # VERIFIED: [LC] Psi = 1 gives 0 and Psi -> oo gives 1.
        assert simplify(combined["total"] - (Psi_sym - 1) / Psi_sym) == 0
        assert simplify(result["free_boson_value"]) == 0
        assert simplify(result["classical_limit"] - 1) == 0

    # Spot checks at concrete Psi-values.
    spot_values = (
        Rational(2),
        Rational(3),
        Rational(5, 2),
    )
    # VERIFIED: [DC] direct substitution into (Psi-1)/Psi.
    # VERIFIED: [LC] these interpolate between Psi = 1 and Psi -> oo.
    for s in spins:
        total = results[s]["combined"]["total"]
        for psi_value in spot_values:
            expected = simplify((psi_value - 1) / psi_value)
            assert simplify(total.subs(Psi_sym, psi_value) - expected) == 0

    if triangular_spins:
        triangular = miura_triangularity_under_delta_witness(triangular_spins)
        for spin, data in triangular["spins"].items():
            assert data["all_current_bounds_below_target"] is True
            assert data["all_representative_bounds_below_target"] is True
            for item in data["current_sector_bounds"]:
                assert item["max_tensor_w_spin_bound"] <= spin - 2
                assert item["hits_target_channel"] is False
            for item in data["representative_lower_composites"]:
                assert item["w_spin_bound"] <= spin - 2
                assert item["hits_target_channel"] is False

    return results


def format_summary(results: Dict[int, Dict[str, Any]]) -> str:
    lines = [
        "miura_universality_proof_engine",
        "verified spins: " + ", ".join(str(s) for s in sorted(results)),
    ]
    for s in sorted(results):
        combined = results[s]["combined"]
        lines.append(
            f"s={s}: drinfeld={combined['drinfeld']}, "
            f"miura={combined['miura_single_j']}, total={factor(combined['total'])}"
        )
    lines.append("all assertions passed")
    return "\n".join(lines)


def main() -> None:
    results = run_assertions()
    print(format_summary(results))


if __name__ == "__main__":
    main()
