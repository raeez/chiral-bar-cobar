"""Exact verification of the scalar formulas in the landscape census.

Each check evaluates a formula from ``chapters/examples/landscape_census.tex``
by exact arithmetic.  The Bershadsky--Polyakov check imports the canonical
normalization from ``bp_koszul_conductor_engine``; this keeps the standard
Fehily--Kawasetsu--Ridout conformal vector, the open genus-one characteristic,
and the secondary shifted formula in separate named lanes.

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
  C10. BP standard conductor 50; all-even diagnostic 17/6; open kappa lane;
       shifted conductor 196

Anti-pattern coverage:
  AP1   family-specific kappa formulas
  AP24  family-dependent complementarity sums
  AP116 boundary checks for summation indices
  AP126/AP141 explicit level prefix in the r-matrix
  AP129 reciprocal swap mistakes in rational formulas
  AP136 distinction between H_N - 1 and H_{N-1}
  AP137 bc / beta-gamma sign complementarity
  AP140 separation of the standard and shifted BP conformal conventions

References:
  - chapters/examples/landscape_census.tex
  - compute/lib/bp_koszul_conductor_engine.py
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from typing import Dict, Iterable, List, Sequence, Tuple, Union

if __package__:
    from . import bp_koszul_conductor_engine as _bp_engine
else:
    import bp_koszul_conductor_engine as _bp_engine


BP_KAPPA_COMPLEMENTARITY_EXACT = _bp_engine.KAPPA_COMPLEMENTARITY_EXACT
BP_GENERATORS = _bp_engine.BP_GENERATORS
BP_KAPPA_STATUS = _bp_engine.BP_KAPPA_STATUS
K_BP_EXACT = _bp_engine.K_BP_EXACT
K_BP_SHIFTED_EXACT = _bp_engine.K_BP_SHIFTED_EXACT
SHIFTED_BP_CONVENTION = _bp_engine.SHIFTED_BP_CONVENTION
STANDARD_BP_CONVENTION = _bp_engine.STANDARD_BP_CONVENTION
VARRHO_BP = _bp_engine.VARRHO_BP
UnverifiedBPInvariantError = _bp_engine.UnverifiedBPInvariantError
_bp_standard_conductor = _bp_engine.K_BP
_bp_shifted_conductor = _bp_engine.K_BP_shifted
_bp_standard_central_charge = _bp_engine.c_BP
_bp_shifted_central_charge = _bp_engine.c_BP_shifted
_bp_reciprocal_weight_diagnostic = _bp_engine.compute_varrho
bp_companion_level = _bp_engine.dual_level
_bp_standard_kappa = _bp_engine.kappa_BP
_bp_standard_kappa_sum = _bp_engine.kappa_complementarity


Scalar = Union[int, Fraction]
StructuredValue = object
ResultDict = Dict[str, object]


THEOREM_C_CERTIFIED_SCALAR_VALUES: Tuple[Fraction, ...] = (
    Fraction(0),
    Fraction(13),
    Fraction(250, 3),
)


TRUE_FORMULA_CENSUS_REFERENCES: Dict[str, str] = {
    "C01": (
        "chapters/examples/landscape_census.tex, Heisenberg census row."
    ),
    "C02": (
        "chapters/examples/landscape_census.tex Virasoro row."
    ),
    "C03": (
        "chapters/examples/landscape_census.tex affine KM rows."
    ),
    "C04": (
        "chapters/examples/landscape_census.tex principal W_N rows."
    ),
    "C05": (
        "chapters/examples/landscape_census.tex bc ghosts row."
    ),
    "C06": (
        "chapters/examples/landscape_census.tex beta-gamma row."
    ),
    "C07": (
        "Weyl dimension computation in this module; "
        "compute/lib/bc_exceptional_categorical_zeta_engine.py."
    ),
    "C08": (
        "Exact definition H_N=sum_{j=1}^N 1/j in landscape_census.tex."
    ),
    "C09": (
        "chapters/examples/landscape_census.tex complementarity rows."
    ),
    "C10": (
        "chapters/examples/landscape_census.tex BP row; "
        "compute/lib/bp_koszul_conductor_engine.py convention records."
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
    """Return the Virasoro census companion parameter ``26-c``."""
    return Fraction(26) - _as_fraction(c)


def kac_moody_dual_level(k: Scalar, h_dual: int) -> Fraction:
    """Return the affine census involution ``-k-2h^vee``."""
    return -_as_fraction(k) - 2 * h_dual


def bp_central_charge(k: Scalar) -> Fraction:
    r"""Return the standard BP charge
    ``-(2k+3)(3k+1)/(k+3)``.

    The implementation is imported from the canonical BP engine.  It has a
    pole at ``k=-3``.
    """

    return _bp_standard_central_charge(_as_fraction(k))


def bp_koszul_conductor(k: Scalar) -> Fraction:
    r"""Return the standard scalar companion sum ``c(k)+c(-k-6)=50``.

    Algebra-level Verdier--Koszul interpretation carries the separate
    subregular DS/bar transport hypothesis; this function computes the scalar
    rational identity.
    """

    return _bp_standard_conductor(_as_fraction(k))


def bp_kappa(k: Scalar) -> Fraction:
    r"""Fail loudly while the BP genus-one characteristic remains open."""

    return _bp_standard_kappa(_as_fraction(k))


def bp_kappa_conductor(k: Scalar) -> Fraction:
    r"""Fail loudly while the BP companion characteristic remains open."""

    return _bp_standard_kappa_sum(_as_fraction(k))


def bp_reciprocal_weight_diagnostic() -> Fraction:
    r"""Return the all-even reciprocal-weight diagnostic ``17/6``.

    This number records the source-correct parity calculation.  Its role is
    diagnostic; the genus-one curvature computation determines ``kappa_BP``.
    """

    return _bp_reciprocal_weight_diagnostic()


def bp_kappa_status_report() -> ResultDict:
    """Return the active BP status and the retracted former proposal."""

    return {
        "kappa_value": None,
        "kappa_complementarity_value": BP_KAPPA_COMPLEMENTARITY_EXACT,
        "status": BP_KAPPA_STATUS.status,
        "resolution_obligation": BP_KAPPA_STATUS.resolution_obligation,
        "reciprocal_weight_diagnostic": bp_reciprocal_weight_diagnostic(),
        "reciprocal_weight_status": "computed-parity-diagnostic-only",
        "former_conditional_proposal": {
            "value": Fraction(25, 3),
            "status": "retracted-derivation",
            "invalidated_derivation": BP_KAPPA_STATUS.invalidated_derivation,
        },
    }


def bp_shifted_central_charge(k: Scalar) -> Fraction:
    r"""Return the secondary shifted formula
    ``2-24(k+1)^2/(k+3)``.
    """

    return _bp_shifted_central_charge(_as_fraction(k))


def bp_shifted_conductor(k: Scalar) -> Fraction:
    r"""Return the explicitly named shifted-formula conductor ``196``."""

    return _bp_shifted_conductor(_as_fraction(k))


def kappa_from_rmatrix(
    level_prefix: Scalar | None,
    averaged_kernel: Scalar = 1,
) -> Fraction:
    """Recover kappa from an r-matrix with an explicit level prefix.

    AP126/AP141 guard:
      The level prefix is part of the input, and the ``k=0`` specialization
      vanishes.
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

    Convention guard:
      AP1: the Heisenberg row has coefficient ``1``.
      AP126/AP141: the Heisenberg r-matrix retains its level prefix.

    Citation:
      ``landscape_census.tex``, Heisenberg census row.
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

    Convention guard:
      AP1: the Virasoro row uses the factor ``1/2``.
      AP24: its displayed scalar companion sum is ``13``.

    Citation:
      ``landscape_census.tex``, Virasoro census row.
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

    Convention guard:
      AP1: the affine row includes the Sugawara shift ``+h^vee``.
      AP126/AP141: the affine r-matrix retains its level prefix.

    Citation:
      ``landscape_census.tex``, affine Kac--Moody census rows.
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

    Convention guard:
      AP136: the coefficient is ``H_N-1``.
      AP116: ``N=2`` recovers the Virasoro boundary value ``c/2``.

    Citation:
      ``landscape_census.tex``, principal ``W_N`` census rows.
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

    Normalization checks:
      The value at ``lambda=2`` is ``c_bc(2)=-26``.

    Citation:
      ``landscape_census.tex``, ``bc`` census row.
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

    Normalization checks:
      The same-weight beta--gamma and ``bc`` values cancel, and
      ``c_bg(3/2)=11``.

    Citation:
      ``landscape_census.tex``, beta--gamma census row.
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

    Verification route:
      Reflection closure produces the 120 positive roots, and the Weyl
      dimension formula computes all eight entries independently.

    Citation:
      Weyl dimension formula evaluated below; local exceptional-data engine.
    """
    expected = E8_FUNDAMENTAL_DIMENSIONS
    computed = compute_e8_fundamental_dimensions()
    result = _make_result("C07", "E_8 fundamental dimensions", expected, computed)
    result["passed"] = result["passed"] and validate_e8_fundamental_dimensions(computed)
    return result


def verify_C08() -> ResultDict:
    """C08. Canonical formula: H_N = sum_{j=1}^N 1 / j exactly.

    Indexing checks:
      The upper index is ``N``; ``H_N-1`` and ``H_{N-1}`` are kept as
      distinct expressions.

    Citation:
      Exact harmonic-number definition in ``landscape_census.tex``.
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

    Family checks:
      The displayed affine and free-field sums are ``0``; the Virasoro sum
      is ``13``.  The ``bc``/beta--gamma pair is evaluated at equal weight.

    Citation:
      ``landscape_census.tex``, family complementarity rows.
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
    r"""C10. Separate exact BP data from the open genus-one lane.

    In the standard FKR census lane,

    ``c_BP(k)=-(2k+3)(3k+1)/(k+3)``,
    ``c_BP(k)+c_BP(-k-6)=50``.

    The generators ``J,G^+,G^-,T`` are even, so the reciprocal-weight
    diagnostic is ``1+2/3+2/3+1/2=17/6``.  This diagnostic has its own
    type.  The BP modular characteristic and its companion sum remain open
    pending the full genus-one curvature computation.

    The secondary shifted lane
    ``c_shifted(k)=2-24(k+1)^2/(k+3)`` has conductor ``196``.
    """
    kappa_status = bp_kappa_status_report()
    expected = {
        "standard:k=0": Fraction(50),
        "standard:k=1": Fraction(50),
        "standard:k=-1/2": Fraction(50),
        "all-generators-even": True,
        "reciprocal-weight-diagnostic": Fraction(17, 6),
        "kappa-value": None,
        "kappa-sum": None,
        "kappa-status": "open-genus-one-computation",
        "shifted-secondary:k=0": Fraction(196),
    }
    computed = {
        "standard:k=0": bp_koszul_conductor(0),
        "standard:k=1": bp_koszul_conductor(1),
        "standard:k=-1/2": bp_koszul_conductor(Fraction(-1, 2)),
        "all-generators-even": all(
            parity == 0 for _weight, parity in BP_GENERATORS.values()
        ),
        "reciprocal-weight-diagnostic": bp_reciprocal_weight_diagnostic(),
        "kappa-value": kappa_status["kappa_value"],
        "kappa-sum": kappa_status["kappa_complementarity_value"],
        "kappa-status": kappa_status["status"],
        "shifted-secondary:k=0": bp_shifted_conductor(0),
    }
    result = _make_result(
        "C10", "Bershadsky-Polyakov convention separation", expected, computed
    )
    result["standard_convention"] = {
        "name": STANDARD_BP_CONVENTION.name,
        "status": STANDARD_BP_CONVENTION.status,
        "conductor": K_BP_EXACT,
        "kappa_sum": BP_KAPPA_COMPLEMENTARITY_EXACT,
        "kappa_status": BP_KAPPA_STATUS.status,
    }
    result["parity_diagnostic"] = {
        "strong_generators": tuple(
            (name, parity) for name, (_weight, parity) in BP_GENERATORS.items()
        ),
        "reciprocal_weight_sum": bp_reciprocal_weight_diagnostic(),
        "status": "computed-parity-diagnostic-only",
    }
    result["shifted_convention"] = {
        "name": SHIFTED_BP_CONVENTION.name,
        "status": SHIFTED_BP_CONVENTION.status,
        "conductor": K_BP_SHIFTED_EXACT,
    }
    result["former_conditional_proposal"] = kappa_status[
        "former_conditional_proposal"
    ]
    result["passed"] = bool(result["passed"]) and (
        STANDARD_BP_CONVENTION.status == "proved-primary-source"
        and SHIFTED_BP_CONVENTION.status == "computed-secondary"
        and all(parity == 0 for _weight, parity in BP_GENERATORS.values())
        and bp_reciprocal_weight_diagnostic() == Fraction(17, 6)
        and VARRHO_BP is None
        and BP_KAPPA_COMPLEMENTARITY_EXACT is None
    )
    return result


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
