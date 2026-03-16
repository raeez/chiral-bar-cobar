"""BPZ primary projection for W_4 Miura generators.

The raw Miura output W4_raw is NOT a primary field — it contains
T-descendant (d²T) and Λ-composite (:TT: - 3/10 d²T) contamination.

The true W_4 primary is obtained by Gram-Schmidt in the BPZ metric:
  W4_primary = W4_raw - <d²T|W4_raw>/<d²T|d²T> * d²T
                      - <Λ|W4_raw>/<Λ|Λ> * Λ

Then <W4_primary|W4_primary> = c/4 and <W4_primary|Λ> = <W4_primary|d²T> = 0.

Similarly for W3_raw: subtract its d(T) descendant contamination.

This module implements the projection and provides corrected generators
for the W_4 OPE extraction.
"""

from __future__ import annotations
from typing import Tuple

from compute.lib.w4_ope_miura import (
    W4MiuraOPE,
    _bpz_inner_product,
    Field,
    add_fields as field_add,
    scale_field as field_scale,
    derivative_field as field_derivative,
)


def bpz_gram_schmidt_weight4(ope: W4MiuraOPE) -> Tuple[Field, float]:
    """Project W4_raw onto the true primary by subtracting d²T and Λ.

    Returns (W4_primary, norm) where norm = <W4_primary|W4_primary>_BPZ.
    """
    W4_raw = ope.W4

    # Step 1: Subtract d²T component
    d2T = field_derivative(field_derivative(ope.T))
    norm_d2T = _bpz_inner_product(d2T, d2T)
    if abs(norm_d2T) > 1e-15:
        overlap_d2T = _bpz_inner_product(d2T, W4_raw)
        coeff_d2T = overlap_d2T / norm_d2T
        W4_step1 = field_add(W4_raw, field_scale(-coeff_d2T, d2T))
    else:
        W4_step1 = W4_raw
        coeff_d2T = 0.0

    # Step 2: Subtract Λ component
    Lambda = ope.Lambda
    norm_Lambda = _bpz_inner_product(Lambda, Lambda)
    if abs(norm_Lambda) > 1e-15:
        overlap_Lambda = _bpz_inner_product(Lambda, W4_step1)
        coeff_Lambda = overlap_Lambda / norm_Lambda
        W4_primary = field_add(W4_step1, field_scale(-coeff_Lambda, Lambda))
    else:
        W4_primary = W4_step1
        coeff_Lambda = 0.0

    norm_primary = _bpz_inner_product(W4_primary, W4_primary)

    return W4_primary, norm_primary, coeff_d2T, coeff_Lambda


def bpz_gram_schmidt_weight3(ope: W4MiuraOPE) -> Tuple[Field, float]:
    """Project W3_raw onto the true primary by subtracting dT.

    At weight 3, the only Virasoro descendant is dT.
    Returns (W3_primary, norm).
    """
    W3_raw = ope.W3

    dT = field_derivative(ope.T)
    norm_dT = _bpz_inner_product(dT, dT)
    if abs(norm_dT) > 1e-15:
        overlap_dT = _bpz_inner_product(dT, W3_raw)
        coeff_dT = overlap_dT / norm_dT
        W3_primary = field_add(W3_raw, field_scale(-coeff_dT, dT))
    else:
        W3_primary = W3_raw
        coeff_dT = 0.0

    norm_primary = _bpz_inner_product(W3_primary, W3_primary)

    return W3_primary, norm_primary, coeff_dT


def verify_projection(t: float = 1.0) -> dict:
    """Verify the BPZ primary projection at a given parameter value."""
    ope = W4MiuraOPE.from_t(t, verbose=False)
    c = ope.c_actual

    results = {"c": c, "t": t}

    # W3 projection
    W3_prim, norm_W3, coeff_dT_3 = bpz_gram_schmidt_weight3(ope)
    results["W3_raw_norm"] = _bpz_inner_product(ope.W3, ope.W3)
    results["W3_prim_norm"] = norm_W3
    results["W3_expected_norm"] = c / 3
    results["W3_dT_contamination"] = coeff_dT_3

    # W4 projection
    W4_prim, norm_W4, coeff_d2T, coeff_Lambda = bpz_gram_schmidt_weight4(ope)
    results["W4_raw_norm"] = _bpz_inner_product(ope.W4, ope.W4)
    results["W4_prim_norm"] = norm_W4
    results["W4_expected_norm"] = c / 4
    results["W4_d2T_contamination"] = coeff_d2T
    results["W4_Lambda_contamination"] = coeff_Lambda

    # Verify orthogonality after projection
    d2T = field_derivative(field_derivative(ope.T))
    results["<W4_prim|d2T>"] = _bpz_inner_product(W4_prim, d2T)
    results["<W4_prim|Lambda>"] = _bpz_inner_product(W4_prim, ope.Lambda)

    return results


if __name__ == "__main__":
    print("=" * 60)
    print("  BPZ PRIMARY PROJECTION FOR W_4")
    print("=" * 60)

    for t in [0.1, 0.5, 1.0, 2.0, 5.0]:
        r = verify_projection(t)
        c = r["c"]
        print(f"\nt = {t}, c = {c:.2f}:")
        print(f"  W3: raw_norm = {r['W3_raw_norm']:.4f}, "
              f"prim_norm = {r['W3_prim_norm']:.4f}, "
              f"expected = {r['W3_expected_norm']:.4f}, "
              f"ratio = {r['W3_prim_norm'] / r['W3_expected_norm']:.6f}")
        print(f"  W4: raw_norm = {r['W4_raw_norm']:.4f}, "
              f"prim_norm = {r['W4_prim_norm']:.4f}, "
              f"expected = {r['W4_expected_norm']:.4f}, "
              f"ratio = {r['W4_prim_norm'] / r['W4_expected_norm']:.6f}")
        print(f"  W4 contamination: d2T = {r['W4_d2T_contamination']:.6f}, "
              f"Lambda = {r['W4_Lambda_contamination']:.6f}")
        print(f"  Orthogonality: <W4|d2T> = {r['<W4_prim|d2T>']:.2e}, "
              f"<W4|Lambda> = {r['<W4_prim|Lambda>']:.2e}")
