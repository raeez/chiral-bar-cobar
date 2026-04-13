r"""Canonical triple verification for sl_2 degree-2 chiral bar cohomology.

This module is the stable entrypoint for the corrected claim

    dim H^2(B(V_k(sl_2))) = 5.

It assembles three independent routes that are already present in the live
repository state:

1. Direct bar-differential matrices at degree 2, weight 3
   via ``bar_differential_sl2_matrices_engine``.
2. The Chevalley-Eilenberg comparison
   ``H^*(B(V_k(sl_2))) = H^*_{CE}(sl_2 \otimes t^{-1}C[t^{-1}], C)``
   via the PBW ``E_2 = E_infinity`` collapse, using the independent
   sympy-based CE implementation in ``bar_cohomology_verification``.
3. The lightweight compute engine entry ``bar_complex.bar_dim_sl2(2)``.

The theorem surface this matches is:

- ``comp:sl2-ce-verification`` in ``chapters/examples/bar_complex_tables.tex``
- ``lem:bar-deg2-symmetric-square`` in ``chapters/examples/landscape_census.tex``
- ``cor:bar-cohomology-koszul-dual`` in ``chapters/theory/chiral_koszul_pairs.tex``

Literature cross-check:

- Garland--Lepowsky, *Lie algebra homology and the Macdonald--Kac formulas*,
  Invent. Math. 34 (1976), 37--76. The repo's current restatement specializes
  their semisimple concentration theorem to
  ``dim H^p(g_-, C)_w = 2p+1`` at ``w = p(p+1)/2`` for ``g = sl_2``.
  Convention conversion: our ``g_-`` is the negative loop algebra
  ``sl_2 \otimes t^{-1}C[t^{-1}]`` with cohomological grading and mode weight
  ``w = sum n_i``. Under that convention, ``p = 2`` lands at ``w = 3`` and
  gives ``dim = 5``.
"""

from __future__ import annotations

from typing import Dict

if __package__ in {None, ""}:
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parents[2]))

from compute.lib.bar_cohomology_sl2_explicit_engine import (
    BarCohomologySl2Engine,
    h2_at_weight_3,
)
from compute.lib.bar_cohomology_verification import strategy_a_detail
from compute.lib.bar_complex import bar_dim_sl2
from compute.lib.bar_differential_sl2_matrices_engine import (
    BarDifferentialSl2Engine,
    h2_cocycle_representatives_weight3,
)


def direct_bar_degree2_verification(max_weight: int = 6) -> Dict:
    """Direct degree-2 bar verification from explicit differential matrices.

    The critical computation is at weight 3:

    - ``dim Lambda^1_3 = 3``
    - ``dim Lambda^2_3 = 9``
    - ``dim Lambda^3_3 = 1``
    - ``rank d_1 = 3``
    - ``rank d_2 = 1``

    hence ``dim H^2_3 = (9 - 1) - 3 = 5``.
    """
    engine = BarDifferentialSl2Engine(max_weight=max_weight)
    weight_decomposition = {
        weight: engine.cohomology_dim(2, weight)
        for weight in range(2, max_weight + 1)
    }
    critical_weight = h2_cocycle_representatives_weight3()
    return {
        "method": "direct_bar",
        "max_weight_checked": max_weight,
        "weight_decomposition": weight_decomposition,
        "support": [w for w, dim in weight_decomposition.items() if dim],
        "critical_weight": critical_weight,
        "H2_total_checked_range": sum(weight_decomposition.values()),
        "verified": critical_weight["H2_dim"] == 5,
    }


def ce_chiral_comparison_verification(max_weight: int = 6) -> Dict:
    """CE comparison using the independent sympy-based loop-algebra engine."""
    weight_detail = strategy_a_detail(max_degree=2, max_weight=max_weight)[2]
    weight_decomposition = {
        weight: weight_detail.get(weight, 0)
        for weight in range(2, max_weight + 1)
    }
    return {
        "method": "ce_comparison",
        "max_weight_checked": max_weight,
        "weight_decomposition": weight_decomposition,
        "support": [w for w, dim in weight_decomposition.items() if dim],
        "H2_total_checked_range": sum(weight_decomposition.values()),
        "verified": sum(weight_decomposition.values()) == 5,
    }


def compute_engine_verification(max_weight: int = 6) -> Dict:
    """Canonical compute-engine value plus explicit engine cross-check."""
    explicit_engine = BarCohomologySl2Engine(max_weight=max_weight)
    explicit_weight3 = h2_at_weight_3()
    explicit_total = sum(
        explicit_engine.cohomology_dim(2, weight)
        for weight in range(2, max_weight + 1)
    )
    table_value = bar_dim_sl2(2)
    return {
        "method": "compute_engine",
        "bar_complex_table_value": table_value,
        "explicit_engine_weight3": explicit_weight3,
        "explicit_engine_total_checked_range": explicit_total,
        "verified": table_value == 5 and explicit_weight3["H2_dim"] == 5,
    }


def triple_verification(max_weight: int = 6) -> Dict:
    """Run the three required checks and assert they agree on 5."""
    direct = direct_bar_degree2_verification(max_weight=max_weight)
    ce = ce_chiral_comparison_verification(max_weight=max_weight)
    engine = compute_engine_verification(max_weight=max_weight)

    values = {
        "direct_bar": direct["critical_weight"]["H2_dim"],
        "ce_comparison": ce["H2_total_checked_range"],
        "compute_engine": engine["bar_complex_table_value"],
    }
    all_five = all(value == 5 for value in values.values())
    return {
        "claim": "dim H^2(B(V_k(sl_2))) = 5",
        "checked_weight_range": [2, max_weight],
        "values": values,
        "direct_bar": direct,
        "ce_comparison": ce,
        "compute_engine": engine,
        "all_five": all_five,
    }


def _print_report(report: Dict) -> None:
    print("sl_2 degree-2 chiral bar cohomology")
    print(f"claim: {report['claim']}")
    print(f"checked weights: {report['checked_weight_range'][0]}..{report['checked_weight_range'][1]}")
    print()

    direct = report["direct_bar"]
    critical = direct["critical_weight"]
    print("1. Direct bar differential")
    print(f"   H^2 weight support on checked range: {direct['weight_decomposition']}")
    print(
        "   weight 3 ranks: "
        f"dim L^2={critical['chain_dims']['L^2']}, "
        f"rank d_1={critical['rank_d1']}, "
        f"rank d_2={critical['rank_d2']}, "
        f"H^2_3={critical['H2_dim']}"
    )
    print()

    ce = report["ce_comparison"]
    print("2. CE comparison")
    print(f"   H^2 weight support on checked range: {ce['weight_decomposition']}")
    print(f"   total H^2 on checked range: {ce['H2_total_checked_range']}")
    print()

    engine = report["compute_engine"]
    print("3. Compute engine")
    print(f"   bar_complex.bar_dim_sl2(2) = {engine['bar_complex_table_value']}")
    print(
        "   explicit engine weight 3: "
        f"H^2_3={engine['explicit_engine_weight3']['H2_dim']}"
    )
    print()

    verdict = "PASS" if report["all_five"] else "FAIL"
    print(f"verdict: {verdict}")


if __name__ == "__main__":
    _print_report(triple_verification())
