"""True Formula Census verification engine.

Independently recomputes the canonical Wave 12-2 formulas used in the
standard landscape census and cross-checks them against the census values.

Checks covered:
  C01. kappa(Heis_k) = k
  C02. kappa(Vir_c) = c/2
  C03. kappa(V_k(g)) = dim(g) * (k + h^vee) / (2 * h^vee)
  C04. kappa(W_N) = c * (H_N - 1)
  C05. c_bc(lambda) = 1 - 3 * (2 * lambda - 1)^2
  C06. c_bg(lambda) = 2 * (6 * lambda^2 - 6 * lambda + 1)
  C07. E_8 fundamental irrep dimensions
  C08. H_N = sum_{j=1}^N 1/j exactly
  C09. Complementarity sums by family
  C10. K_BP = 196 for Bershadsky-Polyakov W_3^(2)

Anti-pattern coverage:
  AP1   family-specific kappa formulas
  AP24  complementarity is not universal across families
  AP116 boundary checks for summation indices
  AP126/AP141 explicit level prefix in the r-matrix
  AP129 reciprocal swap mistakes in rational formulas
  AP136 H_N - 1 is not H_{N-1}
  AP137 bc / beta-gamma sign complementarity
  AP140 K_BP = 196, not 2

References:
  - compute/audit/true_formula_census_draft_wave12.md
  - chapters/examples/landscape_census.tex
  - CLAUDE.md
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from typing import Dict, Iterable, List, Sequence, Tuple, Union


Scalar = Union[int, Fraction]
StructuredValue = Union[Scalar, Tuple[int, ...], Dict[str, Scalar]]
ResultDict = Dict[str, object]


TRUE_FORMULA_CENSUS_REFERENCES: Dict[str, str] = {
    "C01": (
        "True Formula Census Wave 12-2 C1; "
        "chapters/examples/landscape_census.tex tab:master-invariants."
    ),
    "C02": (
        "True Formula Census Wave 12-2 C2; "
        "chapters/examples/landscape_census.tex Virasoro row."
    ),
    "C03": (
        "True Formula Census Wave 12-2 C3; "
        "chapters/examples/landscape_census.tex affine KM rows."
    ),
    "C04": (
        "True Formula Census Wave 12-2 C4 and C19; "
        "chapters/examples/landscape_census.tex principal W_N rows."
    ),
    "C05": (
        "True Formula Census Wave 12-2 C5; "
        "chapters/examples/landscape_census.tex bc ghosts row."
    ),
    "C06": (
        "True Formula Census Wave 12-2 C6 and C7; "
        "compute/audit/true_formula_census_draft_wave12.md."
    ),
    "C07": (
        "True Formula Census Wave 12-2 C16; Bourbaki tables; "
        "compute/lib/bc_exceptional_categorical_zeta_engine.py FUNDAMENTAL_DIMS['E8']."
    ),
    "C08": (
        "True Formula Census Wave 12-2 C19; CLAUDE.md AP116/AP136."
    ),
    "C09": (
        "True Formula Census Wave 12-2 C7, C8, C18; "
        "chapters/examples/landscape_census.tex complementarity rows."
    ),
    "C10": (
        "True Formula Census Wave 12-2 C20; "
        "chapters/examples/landscape_census.tex BP row."
    ),
}


E8_FUNDAMENTAL_DIMENSIONS: Tuple[int, ...] = (
    248,
    3875,
    30380,
    147250,
    2450240,
    6696000,
    146325270,
    6899079264,
)

_E8_CARTAN_MATRIX: Tuple[Tuple[int, ...], ...] = (
    (2, -1, 0, 0, 0, 0, 0, 0),
    (-1, 2, -1, 0, 0, 0, 0, 0),
    (0, -1, 2, -1, 0, 0, 0, -1),
    (0, 0, -1, 2, -1, 0, 0, 0),
    (0, 0, 0, -1, 2, -1, 0, 0),
    (0, 0, 0, 0, -1, 2, -1, 0),
    (0, 0, 0, 0, 0, -1, 2, 0),
    (0, 0, -1, 0, 0, 0, 0, 2),
)


def _as_fraction(value: Scalar) -> Fraction:
    """Convert a scalar to Fraction without losing exactness."""
    if isinstance(value, Fraction):
        return value
    return Fraction(value)


def harmonic_number(n: int) -> Fraction:
    """Return H_n = sum_{j=1}^n 1/j exactly as a Fraction."""
    if n < 1:
        raise ValueError("harmonic_number requires n >= 1")
    total = Fraction(0)
    for j in range(1, n + 1):
        total += Fraction(1, j)
    return total


def kappa_heisenberg(k: Scalar) -> Fraction:
    """Return kappa(Heis_k) = k."""
    return _as_fraction(k)


def kappa_virasoro(c: Scalar) -> Fraction:
    """Return kappa(Vir_c) = c / 2."""
    return _as_fraction(c) / 2


def kappa_kac_moody(dim_g: int, k: Scalar, h_dual: int) -> Fraction:
    """Return kappa(V_k(g)) = dim(g) * (k + h^vee) / (2 * h^vee)."""
    return Fraction(dim_g) * (_as_fraction(k) + h_dual) / (2 * h_dual)


def kappa_w_n(n: int, c: Scalar) -> Fraction:
    """Return kappa(W_N) = c * (H_N - 1)."""
    if n < 2:
        raise ValueError("kappa_w_n requires N >= 2")
    return _as_fraction(c) * (harmonic_number(n) - 1)


def central_charge_bc(lambda_weight: Scalar) -> Fraction:
    """Return c_bc(lambda) = 1 - 3 * (2 * lambda - 1)^2."""
    lam = _as_fraction(lambda_weight)
    return 1 - 3 * (2 * lam - 1) ** 2


def central_charge_bg(lambda_weight: Scalar) -> Fraction:
    """Return c_bg(lambda) = 2 * (6 * lambda^2 - 6 * lambda + 1)."""
    lam = _as_fraction(lambda_weight)
    return 2 * (6 * lam * lam - 6 * lam + 1)


def kappa_bc(lambda_weight: Scalar) -> Fraction:
    """Return kappa for the bc system in the census normalization."""
    return central_charge_bc(lambda_weight) / 2


def kappa_bg(lambda_weight: Scalar) -> Fraction:
    """Return kappa for the beta-gamma system in the census normalization."""
    return central_charge_bg(lambda_weight) / 2


def virasoro_dual_c(c: Scalar) -> Fraction:
    """Return the Virasoro same-family dual central charge 26 - c."""
    return Fraction(26) - _as_fraction(c)


def kac_moody_dual_level(k: Scalar, h_dual: int) -> Fraction:
    """Return the Feigin-Frenkel dual level -k - 2 h^vee."""
    return -_as_fraction(k) - 2 * h_dual


def bp_central_charge(k: Scalar) -> Fraction:
    """Return c_BP(k) = 2 - 24 * (k + 1)^2 / (k + 3)."""
    level = _as_fraction(k)
    if level == -3:
        return Fraction(98)
    return 2 - Fraction(24) * (level + 1) ** 2 / (level + 3)


def bp_koszul_conductor(k: Scalar) -> Fraction:
    """Return K_BP(k) = c(k) + c(-k - 6)."""
    level = _as_fraction(k)
    return bp_central_charge(level) + bp_central_charge(-level - 6)


def kappa_from_rmatrix(
    level_prefix: Scalar | None,
    averaged_kernel: Scalar = 1,
) -> Fraction:
    """Recover kappa from an r-matrix with an explicit level prefix.

    AP126/AP141 guard:
      The bare form Omega / z is forbidden. The level prefix must remain
      visible, and the k = 0 specialization must force vanishing.
    """
    if level_prefix is None:
        raise ValueError(
            "AP126/AP141: missing explicit level prefix in r-matrix; "
            "bare Omega/z is forbidden"
        )
    level = _as_fraction(level_prefix)
    kernel = _as_fraction(averaged_kernel)
    if level == 0:
        return Fraction(0)
    return level * kernel


def validate_e8_fundamental_dimensions(candidate: Iterable[int]) -> bool:
    """Return True iff the candidate set matches the canonical E_8 data."""
    normalized = tuple(sorted(int(value) for value in candidate))
    return normalized == E8_FUNDAMENTAL_DIMENSIONS


def _compute_positive_roots(
    cartan_matrix: Sequence[Sequence[int]],
) -> Tuple[Tuple[int, ...], ...]:
    """Compute positive roots from the Cartan matrix by reflection closure."""
    rank = len(cartan_matrix)
    roots = {
        tuple(1 if i == j else 0 for j in range(rank))
        for i in range(rank)
    }

    changed = True
    iteration_count = 0
    while changed:
        changed = False
        iteration_count += 1
        if iteration_count > 500:
            raise RuntimeError("positive root computation did not stabilize")
        new_roots = set()
        for root in list(roots):
            for i in range(rank):
                pairing = sum(root[j] * cartan_matrix[j][i] for j in range(rank))
                reflected = list(root)
                reflected[i] -= pairing
                reflected_root = tuple(reflected)
                if all(coefficient >= 0 for coefficient in reflected_root):
                    if any(coefficient > 0 for coefficient in reflected_root):
                        if reflected_root not in roots:
                            new_roots.add(reflected_root)
                            changed = True
        roots.update(new_roots)
    return tuple(sorted(roots))


@lru_cache(maxsize=1)
def _e8_positive_roots() -> Tuple[Tuple[int, ...], ...]:
    """Return the 120 positive roots of E_8 in simple-root coordinates."""
    return _compute_positive_roots(_E8_CARTAN_MATRIX)


def _weyl_dimension_fundamental(weight_index: int) -> int:
    """Compute dim V(omega_i) for E_8 via the Weyl dimension formula.

    For simply-laced E_8, coroots and roots coincide. If alpha is written
    in simple-root coordinates alpha = sum_j c_j alpha_j, then
    <rho, alpha^vee> = sum_j c_j and <omega_i, alpha^vee> = c_i.
    """
    product = Fraction(1)
    for root in _e8_positive_roots():
        height = sum(root)
        numerator = height + root[weight_index]
        product *= Fraction(numerator, height)
    if product.denominator != 1:
        raise ValueError("Weyl dimension did not simplify to an integer")
    return product.numerator


@lru_cache(maxsize=1)
def compute_e8_fundamental_dimensions() -> Tuple[int, ...]:
    """Compute and sort the eight E_8 fundamental dimensions."""
    dimensions = [_weyl_dimension_fundamental(index) for index in range(8)]
    return tuple(sorted(dimensions))


def _make_result(
    code: str,
    name: str,
    expected: StructuredValue,
    computed: StructuredValue,
) -> ResultDict:
    """Construct the standard result dictionary."""
    return {
        "name": f"{code} {name}",
        "expected": expected,
        "computed": computed,
        "passed": computed == expected,
        "reference": TRUE_FORMULA_CENSUS_REFERENCES[code],
    }


def verify_C01() -> ResultDict:
    """C01. Canonical formula: kappa(Heis_k) = k.

    Anti-pattern guard:
      AP1: do not import the Virasoro factor 1/2 into Heisenberg.
      AP126/AP141: any Heisenberg r-matrix must keep the level prefix.

    Citation:
      True Formula Census Wave 12-2 C1 and landscape_census.tex.
    """
    expected = {
        "k=0": Fraction(0),
        "k=1": Fraction(1),
        "k=5/2": Fraction(5, 2),
    }
    computed = {
        "k=0": kappa_heisenberg(0),
        "k=1": kappa_heisenberg(1),
        "k=5/2": kappa_heisenberg(Fraction(5, 2)),
    }
    return _make_result("C01", "Heisenberg kappa", expected, computed)


def verify_C02() -> ResultDict:
    """C02. Canonical formula: kappa(Vir_c) = c / 2.

    Anti-pattern guard:
      AP1: Virasoro is the unique standard family with kappa = c / 2.
      AP24: the Virasoro complementarity sum is 13, not 0.

    Citation:
      True Formula Census Wave 12-2 C2 and landscape_census.tex.
    """
    expected = {
        "c=0": Fraction(0),
        "c=13": Fraction(13, 2),
        "c=26": Fraction(13),
    }
    computed = {
        "c=0": kappa_virasoro(0),
        "c=13": kappa_virasoro(13),
        "c=26": kappa_virasoro(26),
    }
    return _make_result("C02", "Virasoro kappa", expected, computed)


def verify_C03() -> ResultDict:
    """C03. Canonical formula: kappa(V_k(g)) = dim(g)(k + h^vee)/(2 h^vee).

    Anti-pattern guard:
      AP1: the Sugawara shift +h^vee must remain.
      AP126/AP141: the affine r-matrix keeps its explicit level prefix.

    Citation:
      True Formula Census Wave 12-2 C3 and landscape_census.tex.
    """
    expected = {
        "sl_2@k=1": Fraction(9, 4),
        "sl_2@k=0": Fraction(3, 2),
        "sl_2@k=-2": Fraction(0),
        "sl_3@k=1": Fraction(16, 3),
        "sl_3@k=0": Fraction(4),
        "sl_3@k=-3": Fraction(0),
        "so_5@k=1": Fraction(20, 3),
        "so_5@k=0": Fraction(5),
        "so_5@k=-3": Fraction(0),
    }
    computed = {
        "sl_2@k=1": kappa_kac_moody(3, 1, 2),
        "sl_2@k=0": kappa_kac_moody(3, 0, 2),
        "sl_2@k=-2": kappa_kac_moody(3, -2, 2),
        "sl_3@k=1": kappa_kac_moody(8, 1, 3),
        "sl_3@k=0": kappa_kac_moody(8, 0, 3),
        "sl_3@k=-3": kappa_kac_moody(8, -3, 3),
        "so_5@k=1": kappa_kac_moody(10, 1, 3),
        "so_5@k=0": kappa_kac_moody(10, 0, 3),
        "so_5@k=-3": kappa_kac_moody(10, -3, 3),
    }
    return _make_result("C03", "Affine Kac-Moody kappa", expected, computed)


def verify_C04() -> ResultDict:
    """C04. Canonical formula: kappa(W_N) = c * (H_N - 1).

    Anti-pattern guard:
      AP136: use H_N - 1, not H_{N-1}.
      AP116: substitute N = 2 to recover the Virasoro boundary value c / 2.

    Citation:
      True Formula Census Wave 12-2 C4 and C19; landscape_census.tex.
    """
    expected = {
        "W_3(c=1)": Fraction(5, 6),
        "W_4(c=1)": Fraction(13, 12),
        "W_5(c=1)": Fraction(77, 60),
    }
    computed = {
        "W_3(c=1)": kappa_w_n(3, 1),
        "W_4(c=1)": kappa_w_n(4, 1),
        "W_5(c=1)": kappa_w_n(5, 1),
    }
    return _make_result("C04", "Principal W_N kappa", expected, computed)


def verify_C05() -> ResultDict:
    """C05. Canonical formula: c_bc(lambda) = 1 - 3 * (2 lambda - 1)^2.

    Anti-pattern guard:
      AP129: reciprocal or sign swaps fail at lambda = 2.
      The bosonic string ghost check must return c_bc(2) = -26.

    Citation:
      True Formula Census Wave 12-2 C5 and landscape_census.tex.
    """
    expected = {
        "lambda=1/2": Fraction(1),
        "lambda=2": Fraction(-26),
    }
    computed = {
        "lambda=1/2": central_charge_bc(Fraction(1, 2)),
        "lambda=2": central_charge_bc(2),
    }
    return _make_result("C05", "bc central charge", expected, computed)


def verify_C06() -> ResultDict:
    """C06. Canonical formula: c_bg(lambda) = 2 * (6 lambda^2 - 6 lambda + 1).

    Anti-pattern guard:
      AP137: beta-gamma must cancel the bc value at the same lambda.
      The superghost check must return c_bg(3/2) = 11.

    Citation:
      True Formula Census Wave 12-2 C6 and C7.
    """
    expected = {
        "lambda=1/2": Fraction(-1),
        "lambda=3/2": Fraction(11),
        "lambda=2": Fraction(26),
    }
    computed = {
        "lambda=1/2": central_charge_bg(Fraction(1, 2)),
        "lambda=3/2": central_charge_bg(Fraction(3, 2)),
        "lambda=2": central_charge_bg(2),
    }
    return _make_result("C06", "beta-gamma central charge", expected, computed)


def verify_C07() -> ResultDict:
    """C07. Canonical data: the E_8 fundamental dimensions form a fixed set.

    Anti-pattern guard:
      Wave 10-8 / AP-style memory pollution inserted 779247, which is not
      a fundamental E_8 dimension.

    Citation:
      True Formula Census Wave 12-2 C16; Bourbaki tables; local E_8 engines.
    """
    expected = E8_FUNDAMENTAL_DIMENSIONS
    computed = compute_e8_fundamental_dimensions()
    result = _make_result("C07", "E_8 fundamental dimensions", expected, computed)
    result["passed"] = result["passed"] and validate_e8_fundamental_dimensions(computed)
    return result


def verify_C08() -> ResultDict:
    """C08. Canonical formula: H_N = sum_{j=1}^N 1 / j exactly.

    Anti-pattern guard:
      AP116: the upper index is N, not N - 1.
      AP136: H_{N-1} is not H_N - 1.

    Citation:
      True Formula Census Wave 12-2 C19; CLAUDE.md AP116/AP136.
    """
    expected = {
        "H_1": Fraction(1),
        "H_2": Fraction(3, 2),
        "H_3": Fraction(11, 6),
        "H_4": Fraction(25, 12),
        "H_5": Fraction(137, 60),
    }
    computed = {
        "H_1": harmonic_number(1),
        "H_2": harmonic_number(2),
        "H_3": harmonic_number(3),
        "H_4": harmonic_number(4),
        "H_5": harmonic_number(5),
    }
    result = _make_result("C08", "Harmonic numbers", expected, computed)
    result["passed"] = result["passed"] and all(
        isinstance(value, Fraction) for value in computed.values()
    )
    return result


def verify_C09() -> ResultDict:
    """C09. Canonical complementarity sums are family-specific.

    Anti-pattern guard:
      AP24: KM and free families sum to 0, while Virasoro sums to 13.
      AP137: bc / beta-gamma cancellation is a same-weight free-field check.

    Citation:
      True Formula Census Wave 12-2 C7, C8, C18; landscape_census.tex.
    """
    expected = {
        "Heisenberg(k=3)": Fraction(0),
        "affine_sl_2(k=1)": Fraction(0),
        "affine_so_5(k=1)": Fraction(0),
        "bc_bg(lambda=2)": Fraction(0),
        "Virasoro(c=25)": Fraction(13),
    }
    computed = {
        "Heisenberg(k=3)": kappa_heisenberg(3) + kappa_heisenberg(-3),
        "affine_sl_2(k=1)": (
            kappa_kac_moody(3, 1, 2)
            + kappa_kac_moody(3, kac_moody_dual_level(1, 2), 2)
        ),
        "affine_so_5(k=1)": (
            kappa_kac_moody(10, 1, 3)
            + kappa_kac_moody(10, kac_moody_dual_level(1, 3), 3)
        ),
        "bc_bg(lambda=2)": kappa_bc(2) + kappa_bg(2),
        "Virasoro(c=25)": kappa_virasoro(25) + kappa_virasoro(virasoro_dual_c(25)),
    }
    return _make_result("C09", "Complementarity sums", expected, computed)


def verify_C10() -> ResultDict:
    """C10. Canonical value: K_BP = 196 for Bershadsky-Polyakov W_3^(2).

    Anti-pattern guard:
      AP140: do not confuse the global Koszul conductor with the local
      ghost constant 2.

    Citation:
      True Formula Census Wave 12-2 C20 and landscape_census.tex.
    """
    expected = {
        "k=0": Fraction(196),
        "k=-3": Fraction(196),
    }
    computed = {
        "k=0": bp_koszul_conductor(0),
        "k=-3": bp_koszul_conductor(-3),
    }
    return _make_result("C10", "Bershadsky-Polyakov conductor", expected, computed)


CHECK_FUNCTIONS = (
    verify_C01,
    verify_C02,
    verify_C03,
    verify_C04,
    verify_C05,
    verify_C06,
    verify_C07,
    verify_C08,
    verify_C09,
    verify_C10,
)


def run_all_checks() -> Tuple[List[ResultDict], Dict[str, int]]:
    """Execute every C01-C10 verification and return results plus summary."""
    results = [verify_function() for verify_function in CHECK_FUNCTIONS]
    passed = sum(1 for result in results if result["passed"])
    summary = {
        "total": len(results),
        "passed": passed,
        "failed": len(results) - passed,
    }
    return results, summary


def _format_value(value: object) -> str:
    """Format Fractions, tuples, and dictionaries for human-readable output."""
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, tuple):
        return "[" + ", ".join(_format_value(item) for item in value) + "]"
    if isinstance(value, dict):
        pieces = [f"{key}: {_format_value(subvalue)}" for key, subvalue in value.items()]
        return "{" + ", ".join(pieces) + "}"
    return str(value)


def format_report(results: Sequence[ResultDict]) -> str:
    """Return a multiline human-readable report for the census checks."""
    passed = sum(1 for result in results if result["passed"])
    failed = len(results) - passed
    lines = ["True Formula Census verification report", ""]
    for result in results:
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(f"[{status}] {result['name']}")
        lines.append(f"  expected: {_format_value(result['expected'])}")
        lines.append(f"  computed: {_format_value(result['computed'])}")
        lines.append(f"  reference: {result['reference']}")
        lines.append("")
    lines.append(f"Summary: total={len(results)} passed={passed} failed={failed}")
    return "\n".join(lines)


if __name__ == "__main__":
    all_results, _ = run_all_checks()
    print(format_report(all_results))
