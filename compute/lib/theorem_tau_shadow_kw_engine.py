r"""Finite-window engine for the tau-shadow / KW scalar lane.

What is computed here:
  * exact Faber-Pandharipande coefficients
      lambda_g^FP = ((2^(2g-1)-1)/2^(2g-1)) * |B_(2g)|/(2g)!;
  * the finite formal log identity
      log tau_shadow^{<=G} = kappa * log tau_KW^{<=G} mod q^(G+1),
      q = hbar^2,
    on the uniform-weight scalar-diagonal lane;
  * the derived finite formal exponential check through the same window;
  * the W_3 cross-channel correction through genus 4.

What is not asserted:
  * no analytic identity of tau functions is proved by a formal
    coefficient window;
  * tau_KW^kappa is not certified as a Kontsevich-Witten tau function
    for kappa != 1;
  * multi-weight algebras are not reduced to the diagonal scalar term.

Canonical anchors:
  * chapters/examples/landscape_census.tex:134-186, 4970-5018;
  * chapters/examples/genus_expansions.tex:1-25, 1438-1607,
    2048-2092, 3178-3237;
  * chapters/connections/concordance.tex:6742-6767.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import factorial
from typing import Any, Dict, Mapping, Tuple


# ---------------------------------------------------------------------------
# Structural firewalls
# ---------------------------------------------------------------------------

HOLOGRAPHIC_PACKAGE_ENTRIES: Tuple[str, ...] = (
    "A",
    "A^i",
    "A^!",
    "C",
    "r(z)",
    "Theta_A",
    "nabla^hol",
)

MODULAR_KOSZUL_COMPUTE_PROJECTIONS: Tuple[str, ...] = (
    "Fact_X(L)",
    "barB_X(L)",
    "Theta_L",
    "L_L",
    "(V_br,T_br)",
    "R4_mod(L)",
)

TYPED_OBJECT_ROLES: Mapping[str, str] = {
    "A": "input chiral algebra",
    "B(A)": "ordered bar coalgebra T^c(s^-1 Abar)",
    "A^i": "bar cohomology coalgebra H^*(B(A))",
    "A^!": "Verdier/continuous-linear dual branch",
    "Omega(B(A))": "bar-cobar inversion recovering A",
    "Z_ch^der(A)": "ChirHoch^*(A,A), the Hochschild bulk",
}

LOCAL_SOURCE_ANCHORS: Mapping[str, str] = {
    "collision_residues": "chapters/examples/landscape_census.tex:173-186",
    "kappa_formulas": "chapters/examples/landscape_census.tex:134-186",
    "fp_coefficients": "chapters/examples/landscape_census.tex:4970-5018",
    "scalar_lane": "chapters/examples/genus_expansions.tex:1-25",
    "multi_weight": "chapters/examples/genus_expansions.tex:1-25, 1438-1580",
    "finite_scalar_tau": "chapters/examples/genus_expansions.tex:2048-2092",
    "free_field_exact": "chapters/examples/genus_expansions.tex:196-240",
    "w3_genus2_cross": (
        "chapters/examples/genus_expansions.tex:1451-1533, 3178-3237"
    ),
    "w3_genus3_cross": "chapters/examples/genus_expansions.tex:1536-1566",
    "w3_genus4_cross": "chapters/examples/genus_expansions.tex:1589-1607",
    "concordance_scalar_free_energy": "chapters/connections/concordance.tex:6742-6767",
    "hierarchy_residual_scope": "chapters/connections/concordance.tex:6759-6767",
}

W3_CROSS_CHANNEL_WITNESSES: Mapping[int, Mapping[str, Any]] = {
    1: {
        "source": LOCAL_SOURCE_ANCHORS["multi_weight"],
        "formula": "0",
        "stable_graph_count": 0,
        "witness": "genus-one scalar universality",
    },
    2: {
        "source": LOCAL_SOURCE_ANCHORS["w3_genus2_cross"],
        "formula": "(c + 204)/(16*c)",
        "stable_graph_count": 7,
        "witness": "graph-by-graph contraction over seven genus-2 stable graphs",
    },
    3: {
        "source": LOCAL_SOURCE_ANCHORS["w3_genus3_cross"],
        "formula": "(5*c^3 + 3792*c^2 + 1149120*c + 217071360)/(138240*c^2)",
        "stable_graph_count": 42,
        "witness": "stable-graph contraction polynomial for genus 3",
    },
    4: {
        "source": LOCAL_SOURCE_ANCHORS["w3_genus4_cross"],
        "formula": (
            "(287*c^4 + 268881*c^3 + 115455816*c^2 + "
            "29725133760*c + 5594347866240)/(17418240*c^3)"
        ),
        "stable_graph_count": None,
        "witness": "overdetermined universal-polynomial computation, N=2..7",
    },
}

KERNEL_NORMALIZATION_FORMULAS: Mapping[str, Mapping[str, str]] = {
    "affine_raw_trace": {
        "formula": "k*Omega_tr/z",
        "scope": "trace-form collision residue",
        "source": LOCAL_SOURCE_ANCHORS["collision_residues"],
    },
    "affine_kz": {
        "formula": "Omega/((k+h^vee)z)",
        "scope": "KZ presentation; not the trace-form collision residue",
        "source": LOCAL_SOURCE_ANCHORS["collision_residues"],
    },
    "heisenberg": {
        "formula": "k/z",
        "scope": "rank-one Heisenberg collision residue",
        "source": LOCAL_SOURCE_ANCHORS["collision_residues"],
    },
    "virasoro": {
        "formula": "(c/2)/z^3 + 2T/z",
        "scope": "Virasoro collision residue",
        "source": LOCAL_SOURCE_ANCHORS["collision_residues"],
    },
}


def holographic_package_entries() -> Tuple[str, ...]:
    """The seven entries of the holographic package H(A)."""

    return HOLOGRAPHIC_PACKAGE_ENTRIES


def modular_koszul_compute_projections() -> Tuple[str, ...]:
    """The six projections of the modular Koszul compute package."""

    return MODULAR_KOSZUL_COMPUTE_PROJECTIONS


def typed_object_firewall() -> Dict[str, str]:
    """Roles that keep A, B(A), A^i, A^!, inversion, and bulk distinct."""

    return dict(TYPED_OBJECT_ROLES)


def kernel_constant_certificate(
    k: Any = Fraction(1), h_vee: Any = Fraction(2), c: Any = Fraction(26)
) -> Dict[str, Any]:
    """Sourced collision and KZ kernel normalizations."""

    k_q = _as_fraction(k)
    h_vee_q = _as_fraction(h_vee)
    c_q = _as_fraction(c)
    if k_q + h_vee_q == 0:
        raise ValueError("affine KZ normalization requires k + h^vee != 0")
    return {
        "source": LOCAL_SOURCE_ANCHORS["collision_residues"],
        "affine_raw_trace": {
            **KERNEL_NORMALIZATION_FORMULAS["affine_raw_trace"],
            "coefficient": k_q,
        },
        "affine_kz": {
            **KERNEL_NORMALIZATION_FORMULAS["affine_kz"],
            "coefficient": Fraction(1, 1) / (k_q + h_vee_q),
        },
        "heisenberg": {
            **KERNEL_NORMALIZATION_FORMULAS["heisenberg"],
            "coefficient": k_q,
        },
        "virasoro": {
            **KERNEL_NORMALIZATION_FORMULAS["virasoro"],
            "central_coefficient": c_q / 2,
            "stress_coefficient": Fraction(2),
        },
    }


def structural_firewall_summary() -> Dict[str, Any]:
    """Package and object separation used by this compute surface."""

    return {
        "holographic_package_entries": holographic_package_entries(),
        "modular_koszul_compute_projections": modular_koszul_compute_projections(),
        "packages_are_distinct": (
            set(HOLOGRAPHIC_PACKAGE_ENTRIES)
            != set(MODULAR_KOSZUL_COMPUTE_PROJECTIONS)
        ),
        "object_roles": typed_object_firewall(),
        "kernel_constants": kernel_constant_certificate(),
        "source_anchors": dict(LOCAL_SOURCE_ANCHORS),
    }


def scalar_projection_firewall() -> Dict[str, Any]:
    """Claims certified, and not certified, by the scalar KW window."""

    return {
        "certifies_fp_coefficients": True,
        "certifies_finite_log_window": True,
        "certifies_formal_exponential_window": True,
        "certifies_tautological_integral": True,
        "tautological_integral": (
            "int_{Mbar_{g,1}} psi_1^{2g-2} lambda_g = lambda_g^FP"
        ),
        "certifies_full_mc_element": False,
        "certifies_bar_cobar_equivalence": False,
        "certifies_derived_center_data": False,
        "certifies_all_class_theorem": False,
        "certifies_full_descendant_hierarchy": False,
        "requires_uniform_weight_or_free_field_exactness": True,
        "source_anchors": {
            "scalar_lane": LOCAL_SOURCE_ANCHORS["scalar_lane"],
            "fp_coefficients": LOCAL_SOURCE_ANCHORS["fp_coefficients"],
            "finite_scalar_tau": LOCAL_SOURCE_ANCHORS["finite_scalar_tau"],
        },
    }


# ---------------------------------------------------------------------------
# Exact Faber-Pandharipande coefficients
# ---------------------------------------------------------------------------


def _as_fraction(value: Any) -> Fraction:
    """Coerce exact numeric input to Fraction."""

    return value if isinstance(value, Fraction) else Fraction(value)


@lru_cache(maxsize=128)
def _bernoulli_number(n: int) -> Fraction:
    """Exact Bernoulli number B_n by the Akiyama-Tanigawa algorithm.

    This gives B_1 = +1/2. Only even Bernoulli numbers enter
    lambda_g^FP, so the convention at B_1 is immaterial here.
    """

    if n < 0:
        raise ValueError(f"Bernoulli index must be nonnegative, got {n}")
    work = [Fraction(0)] * (n + 1)
    for m in range(n + 1):
        work[m] = Fraction(1, m + 1)
        for j in range(m, 0, -1):
            work[j - 1] = j * (work[j - 1] - work[j])
    return work[0]


@lru_cache(maxsize=128)
def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande number lambda_g^FP."""

    if g < 1:
        raise ValueError(f"lambda_fp requires g >= 1, got {g}")
    power = 2 ** (2 * g - 1)
    return Fraction(power - 1, power) * abs(_bernoulli_number(2 * g)) / factorial(
        2 * g
    )


@lru_cache(maxsize=128)
def _sin_over_x_half_coeff(n: int) -> Fraction:
    """Coefficient of q^n in sin(sqrt(q)/2)/(sqrt(q)/2)."""

    return Fraction((-1) ** n, (2 ** (2 * n)) * factorial(2 * n + 1))


def ahat_log_coefficients(g_max: int) -> Tuple[Fraction, ...]:
    r"""Coefficients of (x/2)/sin(x/2)-1 through x^(2*g_max).

    The computation inverts the sine series recursively, independent of
    the Bernoulli-number implementation used by lambda_fp.
    """

    if g_max < 1:
        raise ValueError(f"g_max requires g_max >= 1, got {g_max}")

    reciprocal = [Fraction(0)] * (g_max + 1)
    reciprocal[0] = Fraction(1)
    for n in range(1, g_max + 1):
        reciprocal[n] = -sum(
            _sin_over_x_half_coeff(j) * reciprocal[n - j] for j in range(1, n + 1)
        )
    return tuple(reciprocal[1:])


def ahat_log_coefficient(g: int) -> Fraction:
    """Coefficient of x^(2g) in (x/2)/sin(x/2)-1."""

    if g < 1:
        raise ValueError(f"ahat_log_coefficient requires g >= 1, got {g}")
    return ahat_log_coefficients(g)[g - 1]


def fp_window(g_max: int) -> Dict[int, Fraction]:
    """Faber-Pandharipande coefficients in the finite genus window."""

    if g_max < 1:
        raise ValueError(f"g_max requires g_max >= 1, got {g_max}")
    return {g: lambda_fp(g) for g in range(1, g_max + 1)}


# ---------------------------------------------------------------------------
# Formal finite-window tau algebra
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ScalarWindowRow:
    genus: int
    lambda_fp: Fraction
    ahat_coefficient: Fraction
    scalar_free_energy: Fraction
    coefficient_match: bool


@dataclass(frozen=True)
class ScalarWindowCertificate:
    kappa: Fraction
    g_max: int
    variable: str
    ring: str
    lane: str
    log_identity: str
    log_identity_modulus: str
    tautological_ring_input: str
    analytic_tau_identity_proved: bool
    kw_kdv_tau_membership_certified: bool
    full_descendant_hierarchy_certified: bool
    full_mc_element_certified: bool
    bar_cobar_theorem_certified: bool
    derived_center_data_certified: bool
    stable_graph_cross_channels_checked: bool
    multi_weight_theorem: bool
    source: str
    rows: Tuple[ScalarWindowRow, ...]

    @property
    def all_coefficients_match(self) -> bool:
        return all(row.coefficient_match for row in self.rows)


def shadow_free_energy(kappa: Any, g: int) -> Fraction:
    r"""Diagonal scalar free energy kappa * lambda_g^FP."""

    return _as_fraction(kappa) * lambda_fp(g)


def scalar_shadow_window(kappa: Any, g_max: int) -> ScalarWindowCertificate:
    r"""Finite formal log identity on the scalar-diagonal lane.

    The result certifies
    log tau_shadow^{<=G} = kappa log tau_KW^{<=G} in Q[kappa][[q]]/(q^(G+1)),
    q = hbar^2. It does not certify analytic tau membership.
    """

    if g_max < 1:
        raise ValueError(f"g_max requires g_max >= 1, got {g_max}")
    kappa_q = _as_fraction(kappa)
    ahat_coeffs = ahat_log_coefficients(g_max)
    rows = []
    for g, ahat_coeff in enumerate(ahat_coeffs, start=1):
        lam = lambda_fp(g)
        rows.append(
            ScalarWindowRow(
                genus=g,
                lambda_fp=lam,
                ahat_coefficient=ahat_coeff,
                scalar_free_energy=kappa_q * lam,
                coefficient_match=(ahat_coeff == lam),
            )
        )
    return ScalarWindowCertificate(
        kappa=kappa_q,
        g_max=g_max,
        variable="q = hbar^2",
        ring=f"Q[kappa][[q]]/(q^{g_max + 1})",
        lane="uniform-weight scalar-diagonal",
        log_identity=(
            "log_tau_shadow_scal^{<=G} = "
            "kappa*log_tau_KW^{<=G} mod q^{G+1}"
        ),
        log_identity_modulus=f"q^{g_max + 1}",
        tautological_ring_input=(
            "int_{Mbar_{g,1}} psi_1^{2g-2} lambda_g = lambda_g^FP"
        ),
        analytic_tau_identity_proved=False,
        kw_kdv_tau_membership_certified=False,
        full_descendant_hierarchy_certified=False,
        full_mc_element_certified=False,
        bar_cobar_theorem_certified=False,
        derived_center_data_certified=False,
        stable_graph_cross_channels_checked=False,
        multi_weight_theorem=False,
        source=LOCAL_SOURCE_ANCHORS["finite_scalar_tau"],
        rows=tuple(rows),
    )


def _normalize_log_coeffs(log_coeffs: Mapping[int, Any], g_max: int) -> Dict[int, Fraction]:
    return {g: _as_fraction(log_coeffs.get(g, 0)) for g in range(1, g_max + 1)}


def formal_exponential_coefficients(
    log_coeffs: Mapping[int, Any], g_max: int
) -> Tuple[Fraction, ...]:
    r"""Coefficients of exp(sum a_g q^g) through q^g_max.

    Returned tuple is (t_0, ..., t_gmax). The recurrence follows from
    T' = L' T and is exact over Q.
    """

    if g_max < 0:
        raise ValueError(f"g_max must be nonnegative, got {g_max}")
    coeffs = _normalize_log_coeffs(log_coeffs, g_max)
    tau = [Fraction(0)] * (g_max + 1)
    tau[0] = Fraction(1)
    for n in range(1, g_max + 1):
        tau[n] = (
            sum(
                (j * coeffs[j] * tau[n - j] for j in range(1, n + 1)),
                Fraction(0),
            )
            / n
        )
    return tuple(tau)


def formal_log_from_unit_series(series_coeffs: Tuple[Any, ...]) -> Tuple[Fraction, ...]:
    r"""Recover log coefficients from a unit series T(q) = 1 + ... ."""

    if not series_coeffs or _as_fraction(series_coeffs[0]) != 1:
        raise ValueError("formal_log_from_unit_series requires a unit series")
    g_max = len(series_coeffs) - 1
    tau = [_as_fraction(v) for v in series_coeffs]
    log_coeffs = [Fraction(0)] * (g_max + 1)
    for n in range(1, g_max + 1):
        lower = sum(
            (j * log_coeffs[j] * tau[n - j] for j in range(1, n)),
            Fraction(0),
        )
        log_coeffs[n] = tau[n] - lower / n
    return tuple(log_coeffs)


def tau_kw_coefficients(g_max: int) -> Tuple[Fraction, ...]:
    """Formal coefficients of exp(sum lambda_g^FP q^g) through q^g_max."""

    return formal_exponential_coefficients(fp_window(g_max), g_max)


def tau_shadow_coefficients(kappa: Any, g_max: int) -> Tuple[Fraction, ...]:
    """Formal scalar-lane coefficients of exp(sum kappa*lambda_g^FP q^g)."""

    kappa_q = _as_fraction(kappa)
    return formal_exponential_coefficients(
        {g: kappa_q * lambda_fp(g) for g in range(1, g_max + 1)}, g_max
    )


def formal_tau_power_window(kappa: Any, g_max: int) -> Dict[str, Any]:
    r"""Derived finite formal exponential check.

    The theorem-level statement is the logarithmic coefficient identity
    in Q[[q]]/(q^(g_max+1)), q = hbar^2. Exponentiating inside this
    nilpotent ring is a formal algebra check, not analytic tau membership.
    """

    if g_max < 1:
        raise ValueError(f"g_max requires g_max >= 1, got {g_max}")
    kappa_q = _as_fraction(kappa)
    kw_tau = tau_kw_coefficients(g_max)
    recovered_kw_log = formal_log_from_unit_series(kw_tau)
    power_from_kw = formal_exponential_coefficients(
        {g: kappa_q * recovered_kw_log[g] for g in range(1, g_max + 1)},
        g_max,
    )
    shadow_tau = tau_shadow_coefficients(kappa_q, g_max)
    return {
        "kappa": kappa_q,
        "g_max": g_max,
        "variable": "q = hbar^2",
        "modulus": f"q^{g_max + 1}",
        "kw_tau_coefficients": kw_tau,
        "recovered_kw_log": recovered_kw_log,
        "shadow_tau_coefficients": shadow_tau,
        "tau_kw_power_coefficients": power_from_kw,
        "finite_formal_match": shadow_tau == power_from_kw,
        "certified_identity": (
            "log_tau_shadow_scal^{<=G} = "
            "kappa*log_tau_KW^{<=G} mod q^{G+1}"
        ),
        "firewall": scalar_projection_firewall(),
        "theorem_proves_log_coefficients_only": True,
        "derived_formal_exponential_check": True,
        "analytic_tau_identity_proved": False,
        "constructs_analytic_tau_function": False,
        "kw_kdv_tau_membership_certified": False,
        "full_descendant_hierarchy_certified": False,
        "source": LOCAL_SOURCE_ANCHORS["finite_scalar_tau"],
    }


# ---------------------------------------------------------------------------
# Lane and family certificates
# ---------------------------------------------------------------------------


def scalar_lane_certificate(
    family: str,
    generator_weights: Tuple[int, ...],
    scalar_diagonal: bool = True,
    free_field_exception: bool = False,
) -> Dict[str, Any]:
    """Decide the local scalar-lane hypothesis used by this engine."""

    if not generator_weights:
        raise ValueError("generator_weights must be nonempty")
    uniform_weight = len(set(generator_weights)) == 1
    on_scalar_lane = uniform_weight and scalar_diagonal
    scalar_formula_exact = on_scalar_lane or bool(free_field_exception)
    stable_graphs_required = not scalar_formula_exact
    return {
        "family": family,
        "generator_weights": tuple(generator_weights),
        "uniform_weight": uniform_weight,
        "scalar_diagonal": bool(scalar_diagonal),
        "free_field_exception": bool(free_field_exception),
        "on_scalar_lane": on_scalar_lane,
        "scalar_formula_exact": scalar_formula_exact,
        "cross_channel_correction_required": not scalar_formula_exact,
        "stable_graph_cross_channels_required": stable_graphs_required,
        "certifies_full_mc_element": False,
        "certifies_derived_center_data": False,
        "tautological_ring_input": (
            "scalar term uses the Hodge class lambda_g; interacting "
            "multi-weight full amplitudes require boundary stable graphs"
        ),
        "exception_source": (
            LOCAL_SOURCE_ANCHORS["free_field_exact"]
            if free_field_exception
            else None
        ),
        "source": LOCAL_SOURCE_ANCHORS["scalar_lane"],
    }


def standard_family_verification_table(g_max: int = 5) -> Dict[str, Dict[str, Any]]:
    """Finite scalar-window checks for standard scalar-lane families."""

    families = {
        "Heisenberg_k=1": (Fraction(1), (1,)),
        "Heisenberg_k=7": (Fraction(7), (1,)),
        "Virasoro_c=10": (Fraction(5), (2,)),
        "Virasoro_c=26": (Fraction(13), (2,)),
        "Affine_sl2_k=1": (Fraction(9, 4), (1,)),
        "Affine_sl2_k=2": (Fraction(3), (1,)),
    }
    table: Dict[str, Dict[str, Any]] = {}
    for name, (kappa_q, weights) in families.items():
        lane = scalar_lane_certificate(name, weights)
        window = scalar_shadow_window(kappa_q, g_max)
        tau = formal_tau_power_window(kappa_q, g_max)
        table[name] = {
            "kappa": kappa_q,
            "on_scalar_lane": lane["on_scalar_lane"],
            "scalar_formula_exact": lane["scalar_formula_exact"],
            "log_coefficients_match": window.all_coefficients_match,
            "finite_formal_tau_match": tau["finite_formal_match"],
            "analytic_tau_identity_proved": False,
            "kw_kdv_tau_membership_certified": False,
        }
    return table


# ---------------------------------------------------------------------------
# Multi-weight W_3 corrections
# ---------------------------------------------------------------------------


def kappa_w3(c: Any) -> Fraction:
    """kappa(W_3) = c * (1/2 + 1/3) = 5c/6."""

    return Fraction(5, 6) * _as_fraction(c)


def w3_cross_correction_decomposition_genus2(c: Any) -> Dict[str, Fraction]:
    """Four-term rational witness for delta F_2^cross(W_3).

    This is a computable witness for the total cross-channel constant.
    The tautological-ring proof still requires the seven stable-graph
    contributions.
    """

    c_q = _as_fraction(c)
    if c_q == 0:
        raise ValueError("W_3 cross-channel formulas require c != 0")
    pieces = {
        "sunset": Fraction(3, 1) / c_q,
        "theta": Fraction(9, 2) / c_q,
        "bridge_loop": Fraction(1, 16),
        "barbell": Fraction(21, 4) / c_q,
    }
    pieces["total"] = sum(pieces.values(), Fraction(0))
    return pieces


def w3_cross_channel_witness(g: int, c: Any) -> Dict[str, Any]:
    """Stable-graph and tautological-ring witness for W_3 cross terms."""

    if g not in W3_CROSS_CHANNEL_WITNESSES:
        raise ValueError("W_3 cross-channel witness is implemented only for g = 1..4")
    c_q = _as_fraction(c)
    datum = W3_CROSS_CHANNEL_WITNESSES[g]
    return {
        "genus": g,
        "c": c_q,
        "delta_cross": w3_delta_cross(g, c_q),
        "formula": datum["formula"],
        "stable_graph_count": datum["stable_graph_count"],
        "witness": datum["witness"],
        "source": datum["source"],
        "tautological_ring_input_required": g >= 2,
        "scalar_diagonal_sufficient": g == 1,
        "certifies_full_mc_element": False,
        "certifies_derived_center_data": False,
    }


def w3_delta_cross(g: int, c: Any) -> Fraction:
    """Known exact W_3 cross-channel correction for g = 1, 2, 3, 4."""

    c_q = _as_fraction(c)
    if c_q == 0:
        raise ValueError("W_3 cross-channel formulas require c != 0")
    if g == 1:
        return Fraction(0)
    if g == 2:
        return (c_q + 204) / (16 * c_q)
    if g == 3:
        return (
            5 * c_q**3
            + 3792 * c_q**2
            + 1_149_120 * c_q
            + 217_071_360
        ) / (138_240 * c_q**2)
    if g == 4:
        return (
            287 * c_q**4
            + 268_881 * c_q**3
            + 115_455_816 * c_q**2
            + 29_725_133_760 * c_q
            + 5_594_347_866_240
        ) / (17_418_240 * c_q**3)
    raise ValueError("W_3 cross-channel window is implemented only for g = 1..4")


def w3_free_energy_window(c: Any, g_max: int = 4) -> Dict[str, Any]:
    """Full W_3 free energy through the known cross-channel window."""

    if not 1 <= g_max <= 4:
        raise ValueError("W_3 free-energy window is implemented for 1 <= g_max <= 4")
    c_q = _as_fraction(c)
    kappa_q = kappa_w3(c_q)
    rows: Dict[int, Dict[str, Fraction | bool]] = {}
    for g in range(1, g_max + 1):
        scalar = kappa_q * lambda_fp(g)
        delta = w3_delta_cross(g, c_q)
        rows[g] = {
            "scalar_diagonal": scalar,
            "delta_cross": delta,
            "full": scalar + delta,
            "scalar_equals_full": delta == 0,
        }
    return {
        "family": "W_3",
        "c": c_q,
        "kappa": kappa_q,
        "lane": scalar_lane_certificate("W_3", (2, 3)),
        "cross_channel_witnesses": {
            g: w3_cross_channel_witness(g, c_q) for g in range(1, g_max + 1)
        },
        "full_mc_element_certified": False,
        "derived_center_data_certified": False,
        "rows": rows,
    }


def multi_weight_failure_genus2_w3(c: Any) -> Dict[str, Any]:
    """Sharp genus-2 negative test for the diagonal scalar shortcut."""

    window = w3_free_energy_window(c, g_max=2)
    row = window["rows"][2]
    return {
        "c": window["c"],
        "kappa_W3": window["kappa"],
        "F2_scalar": row["scalar_diagonal"],
        "delta_F2_cross": row["delta_cross"],
        "F2_full": row["full"],
        "scalar_equals_full": row["scalar_equals_full"],
        "correction_positive": row["delta_cross"] > 0,
        "tau_power_fails_for_full_free_energy": row["delta_cross"] != 0,
    }


def w3_large_c_cross_to_scalar_ratio(g: int) -> Fraction:
    """Large-c ratio delta F_g^cross / (kappa(W_3) lambda_g^FP)."""

    if g == 2:
        return Fraction(0)
    if g == 3:
        return Fraction(42, 31)
    if g == 4:
        return Fraction(9184, 381)
    raise ValueError("large-c ratio implemented only for W_3 genus 2, 3, 4")


# ---------------------------------------------------------------------------
# KdV / Virasoro / analytic-scope certificates
# ---------------------------------------------------------------------------


def genus1_universality(kappa: Any) -> Dict[str, Any]:
    """The genus-1 scalar coefficient is kappa/24 for every family."""

    kappa_q = _as_fraction(kappa)
    value = kappa_q * lambda_fp(1)
    return {
        "kappa": kappa_q,
        "F_1": value,
        "expected": kappa_q / 24,
        "match": value == kappa_q / 24,
        "cross_channel_delta": Fraction(0),
    }


def kdv_residual_certificate(kappa: Any) -> Dict[str, Any]:
    r"""Residual for substituting F_shadow = kappa F_KW into scalar KdV.

    The nonlinear KdV term gives residual coefficient kappa(1-kappa).
    Vanishing at kappa = 0 is the trivial solution, not the normalized
    Kontsevich-Witten descendant potential.
    """

    kappa_q = _as_fraction(kappa)
    residual = kappa_q * (1 - kappa_q)
    return {
        "kappa": kappa_q,
        "residual_coefficient": residual,
        "scalar_kdv_equation_satisfied": residual == 0,
        "kw_reference_case": kappa_q == 1,
        "kw_tau_normalization_certified": False,
        "kw_tau_normalization_certified_by_this_engine": False,
        "trivial_solution": kappa_q == 0,
        "coefficient_identity_used": False,
        "source": LOCAL_SOURCE_ANCHORS["hierarchy_residual_scope"],
    }


def kdv_hirota_residual_certificate(kappa: Any) -> Dict[str, Any]:
    r"""Standard nonlinear hierarchy residuals, separate from coefficients."""

    cert = kdv_residual_certificate(kappa)
    residual = cert["residual_coefficient"]
    return {
        "kappa": cert["kappa"],
        "kdv_residual_factor": residual,
        "hirota_residual_factor": residual,
        "standard_kdv_hierarchy": residual == 0,
        "standard_hirota_equations": residual == 0,
        "kw_reference_case": cert["kw_reference_case"],
        "full_kw_descendant_hierarchy": False,
        "full_descendant_hierarchy_certified_by_this_engine": False,
        "kw_tau_normalization_certified": cert["kw_tau_normalization_certified"],
        "trivial_zero_solution_exception": cert["trivial_solution"],
        "coefficient_identity_used": False,
        "source": LOCAL_SOURCE_ANCHORS["hierarchy_residual_scope"],
    }


def kdv_compatibility_check(kappa: Any) -> Dict[str, Any]:
    """KdV residual certificate with the historical result keys."""

    cert = kdv_residual_certificate(kappa)
    return {
        "kappa": cert["kappa"],
        "discrepancy_coefficient": cert["residual_coefficient"],
        "satisfies_kdv": cert["scalar_kdv_equation_satisfied"],
        "kw_reference_case": cert["kw_reference_case"],
        "kw_tau_normalization_certified": cert["kw_tau_normalization_certified"],
        "kw_tau_normalization_certified_by_this_engine": cert[
            "kw_tau_normalization_certified_by_this_engine"
        ],
        "trivial_solution": cert["trivial_solution"],
        "coefficient_identity_used": cert["coefficient_identity_used"],
    }


def virasoro_constraint_scope(kappa: Any) -> Dict[str, Any]:
    """Scope of Virasoro claims visible from this zero-time engine."""

    kappa_q = _as_fraction(kappa)
    return {
        "kappa": kappa_q,
        "zero_time_coefficients_only": True,
        "full_descendant_constraints_checked": False,
        "full_descendant_hierarchy_certified": False,
        "full_descendant_hierarchy_certified_by_this_engine": False,
        "analytic_tau_membership_certified_by_coefficients": False,
        "kw_reference_case": kappa_q == 1,
        "kw_virasoro_normalization_preserved": False,
        "reason": (
            "finite zero-time scalar coefficients do not certify full "
            "descendant Virasoro constraints; kappa rescaling changes the "
            "normalization outside the KW reference case kappa = 1"
        ),
    }


def free_energy_virasoro_constraints(kappa: Any, g_max: int = 5) -> Dict[str, Any]:
    """Coefficient-window report; it does not check Virasoro constraints."""

    scope = virasoro_constraint_scope(kappa)
    scope["coefficient_window"] = {
        g: shadow_free_energy(kappa, g) for g in range(1, g_max + 1)
    }
    scope["coefficient_identity_only"] = True
    return scope


def convergence_radius_shadow(kappa: Any) -> Dict[str, Any]:
    """A-hat model radius datum, separated from the finite tau theorem."""

    return {
        "kappa": _as_fraction(kappa),
        "formal_coefficient_window_only": True,
        "coefficient_identity_implies_radius": False,
        "finite_window_has_radius": False,
        "ahat_meromorphic_model_radius_hbar": "2*pi",
        "ahat_model_radius_independent_of_kappa": True,
        "radius_theorem_for_tau_shadow": False,
        "analytic_tau_identity_proved": False,
        "scope_note": (
            "the pole of (hbar/2)/sin(hbar/2) belongs to the A-hat "
            "meromorphic model, not to the finite KW coefficient theorem"
        ),
        "source": LOCAL_SOURCE_ANCHORS["concordance_scalar_free_energy"],
    }


def kappa_zero_degenerate_case(g_max: int = 8) -> Dict[str, Any]:
    """At kappa = 0 the scalar free energies vanish in every finite window."""

    coeffs = tau_shadow_coefficients(Fraction(0), g_max)
    return {
        "kappa": Fraction(0),
        "all_Fg_zero": all(shadow_free_energy(0, g) == 0 for g in range(1, g_max + 1)),
        "tau_coefficients": coeffs,
        "trivial_solution_not_theta_vanishing": True,
    }


def kappa_one_recovers_kw(g_max: int = 8) -> Dict[str, Any]:
    """At kappa = 1 the finite scalar window is the KW finite window."""

    return {
        "kappa": Fraction(1),
        "recovers_kw": tau_shadow_coefficients(1, g_max) == tau_kw_coefficients(g_max),
        "kw_finite_window_normalization_certified": True,
        "kw_tau_normalization_certified": False,
        "full_descendant_hierarchy_certified_by_this_engine": False,
        "tau_coefficients": tau_kw_coefficients(g_max),
    }


def complementarity_tau_functions(
    kappa: Any, kappa_dual: Any, g_max: int = 5
) -> Dict[str, Any]:
    """Finite formal scalar product for paired kappa values."""

    kappa_q = _as_fraction(kappa)
    kappa_dual_q = _as_fraction(kappa_dual)
    total = kappa_q + kappa_dual_q
    return {
        "kappa": kappa_q,
        "kappa_dual": kappa_dual_q,
        "kappa_sum": total,
        "product_log_coefficients": {
            g: total * lambda_fp(g) for g in range(1, g_max + 1)
        },
        "product_tau_coefficients": tau_shadow_coefficients(total, g_max),
        "finite_formal_product": (
            f"exp(({total})*log_tau_KW^<=G) mod q^{g_max + 1}"
        ),
        "analytic_tau_identity_proved": False,
        "kw_kdv_tau_membership_certified": False,
        "object_firewall": {
            "A^!": TYPED_OBJECT_ROLES["A^!"],
            "Omega(B(A))": TYPED_OBJECT_ROLES["Omega(B(A))"],
            "Z_ch^der(A)": TYPED_OBJECT_ROLES["Z_ch^der(A)"],
        },
        "source": LOCAL_SOURCE_ANCHORS["finite_scalar_tau"],
    }


__all__ = [
    "HOLOGRAPHIC_PACKAGE_ENTRIES",
    "KERNEL_NORMALIZATION_FORMULAS",
    "LOCAL_SOURCE_ANCHORS",
    "MODULAR_KOSZUL_COMPUTE_PROJECTIONS",
    "TYPED_OBJECT_ROLES",
    "W3_CROSS_CHANNEL_WITNESSES",
    "ScalarWindowCertificate",
    "ScalarWindowRow",
    "_bernoulli_number",
    "ahat_log_coefficient",
    "ahat_log_coefficients",
    "complementarity_tau_functions",
    "convergence_radius_shadow",
    "formal_exponential_coefficients",
    "formal_log_from_unit_series",
    "formal_tau_power_window",
    "fp_window",
    "free_energy_virasoro_constraints",
    "genus1_universality",
    "holographic_package_entries",
    "kappa_one_recovers_kw",
    "kappa_w3",
    "kappa_zero_degenerate_case",
    "kdv_compatibility_check",
    "kdv_hirota_residual_certificate",
    "kdv_residual_certificate",
    "kernel_constant_certificate",
    "lambda_fp",
    "modular_koszul_compute_projections",
    "multi_weight_failure_genus2_w3",
    "scalar_lane_certificate",
    "scalar_projection_firewall",
    "scalar_shadow_window",
    "shadow_free_energy",
    "standard_family_verification_table",
    "structural_firewall_summary",
    "tau_kw_coefficients",
    "tau_shadow_coefficients",
    "typed_object_firewall",
    "virasoro_constraint_scope",
    "w3_cross_channel_witness",
    "w3_cross_correction_decomposition_genus2",
    "w3_delta_cross",
    "w3_free_energy_window",
    "w3_large_c_cross_to_scalar_ratio",
]
