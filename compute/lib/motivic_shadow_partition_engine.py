r"""Finite formal motivic-shadow coefficient windows.

This module deliberately proves less than an analytic tau-function theorem.
It computes the scalar diagonal genus window

    log(tau_shadow) = kappa * sum_{g >= 1} lambda_g^FP q^g,
    q = hbar^2,

inside the finite quotient R[[q]]/(q^(g_max + 1)).  The corresponding
unit series tau_shadow is obtained by the formal exponential recurrence.
No finite window proves analytic convergence, Kontsevich-Witten hierarchy
membership, KdV/Hirota equations, a Beilinson regulator theorem, or a
motivic Galois group.

Exact coefficient facts certified here:

  * lambda_g^FP = (2^(2g-1) - 1)|B_(2g)|/(2^(2g-1)(2g)!).
  * If kappa is rational, every finite tau coefficient lies in Q.
  * If kappa lies in a number field K, every finite tau coefficient lies
    in K.  No root extraction is introduced by nonintegral rational kappa.
  * If kappa is an indeterminate, the q^n coefficient lies in Q[kappa]
    with degree at most n.

Scope firewalls:

  * The scalar formula is the uniform-weight scalar-diagonal lane.  A
    multi-weight algebra has cross-channel terms not certified by this
    engine.
  * kappa = 0 gives the scalar unit series only; it is not Theta_A = 0.
  * The holographic package has seven entries
    (A, A^i, A^!, C, r(z), Theta_A, nabla^hol).
  * The modular Koszul compute package has six projections
    (Fact_X(L), barB_X(L), Theta_L, L_L, (V_br,T_br), R4_mod(L)).
  * A, B(A), A^i, A^!, Omega(B(A)), and Z_ch^der(A) are distinct:
    Omega(B(A)) = A is bar-cobar inversion, A^! is the Verdier /
    continuous-linear dual branch, and Z_ch^der(A) is Hochschild bulk.

Canonical anchors:
    thm:theorem-d, thm:multi-weight-genus-expansion
        (higher_genus_modular_koszul.tex)
    chapters/connections/concordance.tex, construction of Pi_X(L)
    Faber-Pandharipande 2003, Ann. Math. 157
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, FrozenSet, List, Mapping, Optional, Sequence, Tuple

from sympy import (
    Integer,
    Poly,
    QQ,
    Rational,
    Symbol,
    bernoulli,
    cancel,
    diff,
    exp,
    expand,
    factor,
    factorial,
    log,
    minimal_polynomial,
    nsimplify,
    pi as sym_pi,
    series,
    simplify,
    sin,
    sqrt,
    symbols,
    together,
)


# =============================================================================
# Structural firewalls
# =============================================================================

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


def holographic_package_entries() -> Tuple[str, ...]:
    """The seven entries of the holographic package."""

    return HOLOGRAPHIC_PACKAGE_ENTRIES


def modular_koszul_compute_projections() -> Tuple[str, ...]:
    """The six projections of the modular Koszul compute package."""

    return MODULAR_KOSZUL_COMPUTE_PROJECTIONS


def typed_object_firewall() -> Dict[str, str]:
    """Roles that keep bar, dual, inversion, and bulk objects distinct."""

    return dict(TYPED_OBJECT_ROLES)


def structural_firewall_summary() -> Dict[str, Any]:
    """Package cardinalities and object roles used by this compute surface."""

    return {
        "holographic_package_entries": holographic_package_entries(),
        "holographic_package_size": len(HOLOGRAPHIC_PACKAGE_ENTRIES),
        "modular_koszul_compute_projections": modular_koszul_compute_projections(),
        "modular_koszul_compute_projection_size": len(
            MODULAR_KOSZUL_COMPUTE_PROJECTIONS
        ),
        "packages_are_distinct": (
            set(HOLOGRAPHIC_PACKAGE_ENTRIES)
            != set(MODULAR_KOSZUL_COMPUTE_PROJECTIONS)
        ),
        "object_roles": typed_object_firewall(),
    }


# =============================================================================
# 0.  Faber-Pandharipande constants (rational, computed from Bernoulli)
# =============================================================================

@lru_cache(maxsize=64)
def lambda_fp(g: int) -> Rational:
    r"""Faber-Pandharipande intersection number lambda_g^FP.

    lambda_g^FP = int_{M-bar_{g,1}} psi^{2g-2} * lambda_g
                = (2^{2g-1} - 1) * |B_{2g}| / (2^{2g-1} * (2g)!)

    Generating function:
        sum_{g >= 1} lambda_g^FP * x^{2g} = (x/2)/sin(x/2) - 1.

    Equivalently this is A-hat(i*x) - 1, where A-hat is the A-roof genus.
    All coefficients are POSITIVE rational.

    Verified at:  g = 1 -> 1/24
                  g = 2 -> 7/5760
                  g = 3 -> 31/967680
                  g = 4 -> 127/154828800
    """
    if g < 1:
        raise ValueError(f"lambda_fp requires g >= 1; got {g}")
    B = Rational(bernoulli(2 * g))
    num = (2 ** (2 * g - 1) - 1) * abs(B)
    den = (2 ** (2 * g - 1)) * factorial(2 * g)
    return Rational(num, den)


def faber_pandharipande_table(g_max: int = 8) -> Dict[int, Rational]:
    """Tabulate lambda_g^FP from g = 1 through g_max."""
    return {g: lambda_fp(g) for g in range(1, g_max + 1)}


# =============================================================================
# 1.  Q1 — coefficient field of tau_shadow
# =============================================================================

def _validate_g_max(g_max: int) -> None:
    if g_max < 1:
        raise ValueError(f"g_max must be >= 1; got {g_max}")


def _is_rational_scalar(value: Any) -> bool:
    if isinstance(value, (int, Rational, Fraction)):
        return True
    flag = getattr(value, "is_rational", None)
    return flag is True


def _algebraic_extension_degree(value: Any) -> Optional[int]:
    if _is_rational_scalar(value):
        return 1
    if getattr(value, "is_algebraic", None) is not True:
        return None
    try:
        return Poly(minimal_polynomial(value)).degree()
    except Exception:
        return None


def _formal_exponential_coefficients(
    log_coefficients: Mapping[int, Any], g_max: int
) -> Tuple[Any, ...]:
    r"""Return coefficients of exp(L(q)) through q^g_max.

    If E(q) = exp(L(q)), E_0 = 1 and

        n E_n = sum_{i=1}^n i L_i E_{n-i}.

    This is an identity in the finite quotient R[[q]]/(q^(g_max + 1)).
    """

    _validate_g_max(g_max)
    coeffs: List[Any] = [Integer(1)]
    for n in range(1, g_max + 1):
        total = Integer(0)
        for i in range(1, n + 1):
            total += i * log_coefficients.get(i, Integer(0)) * coeffs[n - i]
        coeffs.append(cancel(total / n))
    return tuple(coeffs)


def tau_shadow_genus_coefficient(kappa, g: int) -> Any:
    r"""Coefficient of hbar^{2g} in log(tau_shadow(kappa, hbar)).

    log(tau_shadow) = sum_{g >= 1} F_g(kappa) * hbar^{2g},
        F_g(kappa) = kappa * lambda_g^FP.

    This is a scalar-lane formal coefficient, linear in kappa.
    """
    if g < 1:
        raise ValueError("genus g must be >= 1")
    return kappa * lambda_fp(g)


def formal_shadow_log_coefficients(kappa, g_max: int = 8) -> Dict[int, Any]:
    """Exact coefficients of log(tau_shadow) in q = hbar^2 through q^g_max."""

    _validate_g_max(g_max)
    return {g: tau_shadow_genus_coefficient(kappa, g) for g in range(1, g_max + 1)}


def tau_shadow_exp_coefficients(kappa, g_max: int = 8) -> Tuple[Any, ...]:
    """Exact unit-series coefficients of tau_shadow through q^g_max.

    The return tuple is (a_0, ..., a_g_max) for
    tau_shadow = sum a_n q^n in R[[q]]/(q^(g_max + 1)).
    """

    return _formal_exponential_coefficients(
        formal_shadow_log_coefficients(kappa, g_max), g_max
    )


def coefficient_field_signature(kappa) -> Dict[str, Any]:
    """Identify the coefficient field certified by the finite formal engine.

    F_g(kappa) = kappa * lambda_g^FP has rational lambda_g^FP.  The
    formal exponential recurrence uses only addition, multiplication, and
    division by integers, so tau coefficients stay in the field generated
    by kappa.  For symbolic kappa, each finite q^n coefficient is a
    polynomial in kappa of degree at most n.

    The certified coefficient fields are:
      - Q                 if kappa in Q
      - K                 if kappa in K (a number field) and K contains Q
      - Q(kappa), with finite coefficients in Q[kappa], if kappa is an
        indeterminate or a transcendental constant.
    """
    if _is_rational_scalar(kappa):
        return {
            "kappa": kappa,
            "field": "Q",
            "coefficient_ring": "Q",
            "extension_degree": 1,
            "rational": True,
            "algebraic": True,
            "transcendental": False,
            "finite_polynomial_degree_bound": 0,
            "ring_for_log_tau": "Q[[q]]",
            "ring_for_tau": "Q[[q]]",
            "analytic_convergence_proved": False,
        }
    algebraic_degree = _algebraic_extension_degree(kappa)
    if algebraic_degree is not None:
        return {
            "kappa": kappa,
            "field": "Q(kappa)",
            "coefficient_ring": "Q(kappa)",
            "extension_degree": algebraic_degree,
            "rational": False,
            "algebraic": True,
            "transcendental": False,
            "finite_polynomial_degree_bound": None,
            "ring_for_log_tau": "Q(kappa)[[q]]",
            "ring_for_tau": "Q(kappa)[[q]]",
            "analytic_convergence_proved": False,
        }
    return {
        "kappa": kappa,
        "field": "Q(kappa)",
        "coefficient_ring": "Q[kappa] in each finite window",
        "extension_degree": float("inf"),
        "rational": False,
        "algebraic": False,
        "transcendental": True,
        "finite_polynomial_degree_bound": "degree(q^n coefficient) <= n",
        "ring_for_log_tau": "Q[kappa][[q]] in finite windows",
        "ring_for_tau": "Q[kappa][[q]] in finite windows",
        "analytic_convergence_proved": False,
    }


def verify_no_field_extension(kappa, g_max: int = 8) -> Dict[str, Any]:
    """Q1 answer in a finite formal window.

    For rational kappa, both log and exponential coefficients lie in Q.
    For algebraic or symbolic kappa, the finite window stays in the field
    or polynomial ring generated by kappa.  This is a coefficient theorem,
    not an analytic statement about a power function.

    Returns the explicit verification through genus g_max.
    """
    _validate_g_max(g_max)
    log_coeffs = formal_shadow_log_coefficients(kappa, g_max)
    tau_coeffs = tau_shadow_exp_coefficients(kappa, g_max)
    sig = coefficient_field_signature(kappa)
    sig["log_coefficients"] = log_coeffs
    sig["tau_coefficients"] = tau_coeffs
    sig["coefficients"] = log_coeffs
    sig["all_log_coefficients_in_field"] = all(
        isinstance(c, (Rational, int, Fraction))
        or (hasattr(c, "is_rational") and c.is_rational)
        for c in log_coeffs.values()
    ) if isinstance(kappa, (int, Rational, Fraction)) else None
    sig["all_tau_coefficients_in_field"] = all(
        isinstance(c, (Rational, int, Fraction))
        or (hasattr(c, "is_rational") and c.is_rational)
        for c in tau_coeffs
    ) if _is_rational_scalar(kappa) else None
    sig["all_in_field"] = sig["all_log_coefficients_in_field"]
    return sig


def scalar_lane_certificate(
    family: str,
    generator_weights: Sequence[int],
    scalar_diagonal: bool = True,
) -> Dict[str, Any]:
    """Certify whether the kappa-linear scalar window applies by itself."""

    if not generator_weights:
        raise ValueError("generator_weights must be nonempty")
    weights = tuple(generator_weights)
    uniform_weight = len(set(weights)) == 1
    on_scalar_lane = uniform_weight and bool(scalar_diagonal)
    return {
        "family": family,
        "generator_weights": weights,
        "uniform_weight": uniform_weight,
        "scalar_diagonal": bool(scalar_diagonal),
        "scalar_lane_certified": on_scalar_lane,
        "multi_weight_cross_channels_omitted": not uniform_weight,
        "claim": (
            "F_g = kappa*lambda_g^FP certified on this scalar lane"
            if on_scalar_lane
            else "scalar diagonal only; cross-channel corrections not certified"
        ),
    }


def finite_formal_coefficient_window(
    kappa,
    g_max: int = 8,
    *,
    family: str = "scalar formal input",
    generator_weights: Sequence[int] = (1,),
    scalar_diagonal: bool = True,
) -> Dict[str, Any]:
    """Strongest theorem certified by this module.

    In R[[q]]/(q^(g_max + 1)), q = hbar^2, the scalar-diagonal window is

        tau_shadow = exp(kappa * sum_{g=1}^{g_max} lambda_g^FP q^g)

    with exact coefficients.  The statement is finite and formal.
    """

    _validate_g_max(g_max)
    lane = scalar_lane_certificate(family, generator_weights, scalar_diagonal)
    log_coeffs = formal_shadow_log_coefficients(kappa, g_max)
    tau_coeffs = tau_shadow_exp_coefficients(kappa, g_max)
    return {
        "kappa": kappa,
        "g_max": g_max,
        "variable": "q = hbar^2",
        "modulus": f"q^{g_max + 1}",
        "lambda_fp": faber_pandharipande_table(g_max),
        "log_coefficients": log_coeffs,
        "tau_coefficients": tau_coeffs,
        "coefficient_field": coefficient_field_signature(kappa),
        "lane": lane,
        "finite_formal_identity_certified": lane["scalar_lane_certified"],
        "analytic_tau_identity_proved": False,
        "kw_kdv_theorem_proved": False,
        "motivic_galois_group_proved": False,
        "convergence_proved": False,
    }


# =============================================================================
# 2.  Q2 — motive of F_g(kappa) at fixed genus
# =============================================================================

@dataclass(frozen=True)
class TateMotive:
    """Q(-n) — the Tate twist of weight 2n, Hodge type (n, n).

    Conventions (Deligne):
      Q(0) = trivial motive, weight 0, type (0, 0).
      Q(-1) = Lefschetz motive L, weight 2, type (1, 1).
      Q(-n) = L^n, weight 2n, type (n, n).

    The dual Q(n) has weight -2n.

    Periods:  Q(-n) has period (2*pi*i)^n  (so its complex period is
    transcendental, but its de Rham/Betti realizations are 1-dimensional).
    """
    n: int  # the (negative of the) Tate twist

    @property
    def weight(self) -> int:
        """Motivic weight = 2n for Q(-n)."""
        return 2 * self.n

    @property
    def hodge_type(self) -> Tuple[int, int]:
        """Hodge type (n, n)."""
        return (self.n, self.n)

    @property
    def hodge_dimension(self) -> int:
        """h^{n,n} = 1; all other h^{p,q} = 0."""
        return 1

    @property
    def period(self) -> str:
        """Period (2*pi*i)^n as a symbolic label."""
        if self.n == 0:
            return "1"
        if self.n == 1:
            return "2*pi*i"
        return f"(2*pi*i)^{self.n}"


def motive_of_Fg(g: int) -> TateMotive:
    r"""Formal Tate label of the genus-g free energy coefficient.

    F_g lives in H^0(point, Q) AFTER pairing with the integration cycle
    [M-bar_{g,1}] cap psi^{2g-2}.  The AMBIENT Hodge piece on M-bar_g
    in which lambda_g lives is:

      H^{2g}(M-bar_g, Q) cap F^g = the (g, g) piece, which is Q(-g)^{?}.

    The lambda_g class lives in this (g, g) piece.  After integration
    (which is the canonical isomorphism int: H^{2g}(M-bar_g, Q(-g)) -> Q),
    the class becomes a rational number.

    The finite coefficient engine records:
      Class-level Tate label:              Q(-g)
      Integrated rational period of F_g:   Q  (= Q(0))

    This is not a standalone construction of a global shadow motive.
    """
    return TateMotive(n=g)


def integrated_period_of_Fg(g: int, kappa) -> Any:
    """The integrated period of F_g is rational (= kappa * lambda_g^FP).

    Despite the ambient class living in Q(-g), the integral lands in Q(0) = Q.
    This is the COMPATIBILITY between the period map and the integration
    pairing on M-bar_g.
    """
    return tau_shadow_genus_coefficient(kappa, g)


# =============================================================================
# 3.  Q3 — Hodge structure at genus g and the (g, g) piece
# =============================================================================

@dataclass(frozen=True)
class ShadowHodgeStructure:
    """Formal Hodge label on the genus-g scalar shadow piece.

    The finite scalar window records the expected (g, g) Tate label of
    the lambda_g line.  It does not compute the full Hodge structure of
    H^*(M-bar_g).
    """
    genus: int
    weight: int
    hodge_type: Tuple[int, int]
    rank: int = 1  # rank of the kappa-line in H^{2g}

    @classmethod
    def for_genus(cls, g: int) -> "ShadowHodgeStructure":
        return cls(genus=g, weight=2 * g, hodge_type=(g, g), rank=1)

    @property
    def is_pure(self) -> bool:
        """The formal (g, g) label is pure of weight 2g."""
        return True

    @property
    def is_tate(self) -> bool:
        """The finite-window label is the Tate symbol Q(-g)."""
        return True

    def hodge_polynomial(self) -> str:
        """Hodge polynomial u^g v^g (the (g, g) bidegree)."""
        return f"u^{self.genus} * v^{self.genus}"


def shadow_hodge_filtration(g_max: int = 8) -> Dict[int, ShadowHodgeStructure]:
    """Formal Hodge-type labels on the scalar genus expansion.

    For each genus g, the scalar lambda_g class is recorded with type
    (g, g).  This is a finite-window bookkeeping statement, not a global
    pro-motive theorem.
    """
    return {g: ShadowHodgeStructure.for_genus(g) for g in range(1, g_max + 1)}


# =============================================================================
# 4.  Q4 — periods at each genus: rational vs MZV vs transcendental
# =============================================================================

def is_rational_period(value: Any) -> bool:
    """Detect whether a value is a rational period (Q(0))."""
    if isinstance(value, (int, Fraction)):
        return True
    if isinstance(value, Rational):
        return True
    if hasattr(value, "is_rational"):
        return bool(value.is_rational)
    return False


def period_classification(g: int, kappa) -> Dict[str, Any]:
    """Classify the genus-g free energy period.

    For kappa rational, F_g(kappa) = kappa * lambda_g^FP is rational.
    No positive-weight MZV, no zeta(2g), no transcendental period is
    detected in the integrated coefficient.  Rational numbers are the
    weight-zero part of the usual MZV algebra; this function rules out
    nontrivial MZV content, not membership of Q in that algebra.

    The naive expectation: F_g should involve zeta(2g) (since
    lambda_g^FP comes from Bernoulli numbers, and zeta(2g) ~ B_{2g} * pi^{2g}).
    BUT: lambda_g^FP = B_{2g}/(...) STRIPS the pi^{2g} factor — what
    remains is RATIONAL.

    This is the key insight: the Faber-Pandharipande number is the
    "pi^{2g}-stripped" zeta value, hence rational.
    """
    F = tau_shadow_genus_coefficient(kappa, g)
    sig = coefficient_field_signature(kappa)
    is_rat = is_rational_period(F)
    if is_rat or sig["algebraic"]:
        transcendence_degree = 0
    else:
        transcendence_degree = 1
    return {
        "genus": g,
        "kappa": kappa,
        "F_g": F,
        "lambda_g_FP": lambda_fp(g),
        "is_rational": is_rat,
        "is_mzv": False,            # Legacy key: means no nontrivial MZV here.
        "is_nontrivial_mzv": False,
        "mzv_weight": 0 if is_rat else None,
        "involves_pi": False,       # pi^{2g} stripped via Bernoulli normalization
        "involves_zeta": False,     # zeta(2g) absorbed into lambda_g^FP
        "transcendence_degree": transcendence_degree,
        "motive": motive_of_Fg(g),
        "integrated_to": "Q(0)",
    }


def deligne_critical_value_check(g: int) -> Dict[str, Any]:
    r"""Check the Bernoulli/zeta normalization behind lambda_g^FP.

    This is an exact arithmetic identity:

      lambda_g^FP is a rational multiple of zeta(2g)/(2*pi)^(2g).

    It is a Deligne-compatible normalization check, not a proof of a
    Deligne critical-value theorem for a newly constructed motive.
    """
    lam = lambda_fp(g)
    # Compute the rational multiple of zeta(2g).
    #
    # From  zeta(2g) = (-1)^{g+1} (2pi)^{2g} B_{2g} / (2 (2g)!)
    # we get zeta(2g)/(2pi)^{2g} = (-1)^{g+1} B_{2g} / (2 (2g)!).
    # Meanwhile
    #   lambda_g^FP = (2^{2g-1}-1) |B_{2g}| / (2^{2g-1} (2g)!)
    # and B_{2g} = (-1)^{g+1} |B_{2g}| (sympy convention), so
    #   lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * (-1)^{g+1} * B_{2g}/(2g)!
    #              = [2*(2^{2g-1}-1)/2^{2g-1}] * zeta(2g)/(2pi)^{2g}.
    rational_factor = Rational(2 * (2 ** (2 * g - 1) - 1), 2 ** (2 * g - 1))
    B = Rational(bernoulli(2 * g))  # signed Bernoulli number
    zeta_normalized = Rational(((-1) ** (g + 1)) * B, 2 * factorial(2 * g))
    # Then: rational_factor * zeta_normalized should equal lambda_g^FP
    reconstructed = rational_factor * zeta_normalized
    return {
        "genus": g,
        "lambda_g_FP": lam,
        "rational_factor_times_zeta": rational_factor,
        "zeta_2g_normalized": zeta_normalized,
        "reconstructed": reconstructed,
        "matches": (lam == reconstructed),
        "interpretation": (
            "lambda_g^FP = rational multiple of zeta(2g)/(2pi)^{2g}; "
            "normalization check only"
        ),
        "deligne_theorem_certified": False,
    }


# =============================================================================
# 5.  Q5 — formal Tate labels and motivic Galois boundary
# =============================================================================

@dataclass(frozen=True)
class ShadowProMotive:
    """Formal Tate bookkeeping object for the finite scalar window.

    Each genus-g layer is labelled by the rank-1 Tate symbol Q(-g).
    This records the weight grading visible in the coefficient window.
    It is not a construction of a global pro-motive and does not certify
    a motivic Galois group.
    """
    genera: Tuple[int, ...]

    @classmethod
    def truncate(cls, g_max: int) -> "ShadowProMotive":
        return cls(genera=tuple(range(1, g_max + 1)))

    @property
    def layers(self) -> List[TateMotive]:
        return [TateMotive(n=g) for g in self.genera]

    @property
    def motivic_galois_group(self) -> str:
        """Only the formal Tate weight torus is visible in this engine."""
        return "formal_Tate_weight_torus_not_certified_G_mot"

    @property
    def certified_motivic_galois_group(self) -> bool:
        """This finite coefficient engine does not prove a Galois group."""
        return False

    @property
    def cocharacter_weight(self) -> Dict[int, int]:
        """Cocharacter weight on each genus layer: weight 2g on Q(-g)."""
        return {g: 2 * g for g in self.genera}

    @property
    def is_mixed_tate(self) -> bool:
        """The formal layers are Tate; this is not a global motive theorem."""
        return True

    @property
    def is_pure(self) -> bool:
        """The pro-object is NOT pure (different layers have different weights)."""
        return False


def shadow_pro_motive(g_max: int = 8) -> ShadowProMotive:
    """Construct the truncated formal Tate bookkeeping object."""
    return ShadowProMotive.truncate(g_max)


def motivic_galois_action(g: int, t: Symbol) -> Any:
    """Formal Tate weight action on the genus-g layer by t^{2g}.

    This is the weight cocharacter visible in the finite window, not a
    proof that a motivic Galois group has been constructed.
    """
    return t ** (2 * g)


# =============================================================================
# 6.  Q6 — Beilinson motivic cohomology and the regulator
# =============================================================================

def beilinson_regulator_vanishing(g: int) -> Dict[str, Any]:
    r"""Finite-window regulator boundary.

    This engine verifies only the rational integrated Faber-Pandharipande
    coefficient.  It does not prove a Beilinson regulator vanishing theorem
    for a motivic cohomology class on M-bar_g.

    Returns a non-certification flag plus the exact rational period that
    the coefficient computation does prove.
    """
    return {
        "genus": g,
        "class": f"lambda_{g}",
        "motive": motive_of_Fg(g),
        "regulator_vanishes": None,
        "regulator_vanishing_certified": False,
        "reason": (
            "finite formal coefficients prove rational integrated periods, "
            "not a Beilinson regulator theorem"
        ),
        "period_in_Q": True,
        "period_value": lambda_fp(g),
    }


def deligne_mhs_summary(g_max: int = 8) -> Dict[int, Dict[str, Any]]:
    """Formal Deligne-type labels for each finite genus layer.

    For each g:
      * Weight filtration:  W_{2g} = full piece, W_{2g-1} = 0  (PURE)
      * Hodge filtration:   F^g = full piece, F^{g+1} = 0
      * Hodge type:         (g, g)
      * Bidegree:           h^{g,g} = 1 on the kappa-line

    The labels record the Tate model used by the coefficient window.  They
    are not a proof of the full mixed Hodge structure of M-bar_g.
    """
    out = {}
    for g in range(1, g_max + 1):
        out[g] = {
            "genus": g,
            "weight": 2 * g,
            "filtration_F": {f"F^{g}": "full", f"F^{g+1}": "zero"},
            "filtration_W": {f"W_{2*g}": "full", f"W_{2*g-1}": "zero"},
            "hodge_type": (g, g),
            "h_pq": {(g, g): 1},
            "is_pure": True,
            "tate_twist": -g,  # Q(-g)
            "mhs_theorem_certified": False,
            "formal_tate_label": True,
        }
    return out


# =============================================================================
# 7.  Q7 — negative motivic results
# =============================================================================

def kdv_negative_result(kappa, g_max: int = 8) -> Dict[str, Any]:
    """Record the KdV boundary of the finite coefficient engine.

    The finite formal motivic window does not prove that tau_KW^kappa is
    a KW/KdV tau function.  The only analytic KdV-compatible scalar cases
    named here are kappa = 0 (unit series) and kappa = 1 (the original KW
    normalization, supplied externally).  For other kappa this function
    records the known bilinear obstruction as an external boundary, not as
    a motivic proof.
    """
    in_exception_set = (kappa == 0 or kappa == 1)
    return {
        "kappa": kappa,
        "satisfies_kdv": in_exception_set,
        "satisfies_kdv_certified_by_this_engine": False,
        "analytic_kw_tau_function_certified_by_this_engine": False,
        "reason": (
            "finite q-coefficients do not certify Hirota/KdV equations; "
            "the generic obstruction is bilinear and external to this "
            "motivic coefficient check"
        ),
        "exception": "kappa = 0: tau = 1 (trivially satisfies); "
                     "kappa = 1: tau = tau_KW (Witten's theorem).",
        "negative_result": "tau_shadow is not certified as a KdV tau function.",
    }


def mzv_negative_result(g: int) -> Dict[str, Any]:
    """The integrated coefficient has no positive-weight MZV content.

    The naive guess: F_g should involve MZV(2, 2, ..., 2) (g times) or
    similar.  The finite scalar coefficient is rational up to kappa.
    Since Q is the weight-zero part of the MZV algebra, the precise
    negative statement is absence of nontrivial positive-weight MZV
    content.

    The Bernoulli numbers in lambda_g^FP come from the SAME source as
    zeta(2g), but the (2pi)^{2g} factor is STRIPPED, leaving Q.

    No multi-genus mixing produces an MZV either: the genus expansion
    is a polynomial in kappa with rational coefficients in each hbar^{2g}.
    """
    return {
        "genus": g,
        "F_g_form": "kappa * lambda_g^FP",
        "lambda_g_FP": lambda_fp(g),
        "is_mzv": False,
        "is_nontrivial_mzv": False,
        "mzv_weight": 0,
        "is_rational": True,
        "naive_guess": "MZV(2,...,2) [g times] or polylog(2g)",
        "actual": "rational number",
        "reason": (
            "lambda_g^FP = (rational) * B_{2g} / (2g)! has the (2pi)^{2g} "
            "factor stripped relative to zeta(2g); what remains is rational."
        ),
    }


def injectivity_negative_result() -> Dict[str, Any]:
    """Separate finite scalar injectivity from abstract Tate-shape loss.

    In the finite formal scalar series, kappa is recovered from the q^1
    coefficient because lambda_1^FP = 1/24.  If one forgets all scalar
    coefficients and keeps only the abstract Tate weight shape, kappa is
    lost.  This engine does not prove a motivic Galois-orbit statement.
    """
    return {
        "finite_formal_scalar_injective": True,
        "recovery_formula": "kappa = 24 * [q^1] log(tau_shadow)",
        "abstract_tate_shape_injective": False,
        "galois_orbit_injectivity_certified": False,
        "injective_on_motives": False,
        "injective_on_values": True,
        "explanation": (
            "finite coefficients remember kappa; the bare formal Tate "
            "weight shape does not"
        ),
        "remedy": "Use the full Theta_A (all arities) to recover injectivity.",
    }


# =============================================================================
# 8.  Cross-checks: numerical verification through genus 8
# =============================================================================

def verify_lambda_fp_table(g_max: int = 8) -> Dict[int, Dict[str, Any]]:
    """Verify lambda_g^FP from g = 1 to g = g_max via three independent paths.

    Path 1: direct Bernoulli formula
    Path 2: generating function (x/2)/sin(x/2) - 1 expansion
    Path 3: reverse via Deligne critical value formula
    """
    x = Symbol("x")
    gen = series(x / 2 / sin(x / 2) - 1, x, 0, 2 * g_max + 2).removeO()
    expanded = expand(gen)
    coeffs = Poly(expanded, x).all_coeffs()
    # Polynomial coefficients are in DESCENDING degree.  Reverse and pad.
    deg = Poly(expanded, x).degree()
    coeff_dict = {}
    for i, c in enumerate(coeffs):
        coeff_dict[deg - i] = Rational(c)

    out = {}
    for g in range(1, g_max + 1):
        # Path 1
        p1 = lambda_fp(g)
        # Path 2: from generating function
        p2 = coeff_dict.get(2 * g, Rational(0))
        # Path 3: Deligne reconstruction
        deligne = deligne_critical_value_check(g)
        p3 = deligne["reconstructed"]
        out[g] = {
            "path1_direct": p1,
            "path2_genfun": p2,
            "path3_deligne": p3,
            "all_match": (p1 == p2 == p3),
            "value": p1,
        }
    return out


def tau_shadow_log_expansion(kappa, g_max: int = 6) -> Dict[int, Any]:
    """Coefficient-by-coefficient expansion of log(tau_shadow)."""
    return formal_shadow_log_coefficients(kappa, g_max)


def tau_shadow_exp_expansion(kappa, g_max: int = 4) -> Any:
    """Compute the finite formal tau series in hbar through hbar^{2*g_max}.

    This is the image of the q-window under q = hbar^2.  It is not an
    analytic convergence claim.
    """
    h = Symbol("hbar")
    coeffs = tau_shadow_exp_coefficients(kappa, g_max)
    return sum(coeffs[g] * h ** (2 * g) for g in range(0, g_max + 1))


# =============================================================================
# 9.  Formal Hodge labels on the finite scalar window
# =============================================================================

@dataclass(frozen=True)
class UniversalShadowHodgeStructure:
    """Formal finite-window Hodge labels underlying the scalar coefficients.

    Combining genera through g_max gives the formal direct sum of labels
    Q(-g).  Frobenius and crystalline outputs below are model labels, not
    a constructed etale realization of tau_shadow.
    """
    g_max: int

    @property
    def betti_dimension(self) -> int:
        """Total Betti dimension (one per genus)."""
        return self.g_max

    def hodge_polynomial(self, u: Symbol, v: Symbol) -> Any:
        """Hodge polynomial sum_g u^g v^g."""
        return sum(u ** g * v ** g for g in range(1, self.g_max + 1))

    def weight_polynomial(self, t: Symbol) -> Any:
        """Weight polynomial sum_g t^{2g}."""
        return sum(t ** (2 * g) for g in range(1, self.g_max + 1))

    def frobenius_eigenvalues(self, p: int) -> List[int]:
        """Formal Tate-model Frobenius eigenvalues p^g."""
        return [p ** g for g in range(1, self.g_max + 1)]

    def galois_action_is_abelian(self) -> bool:
        """The formal Tate model is abelian; no Galois theorem is proved."""
        return True

    def is_mixed_tate(self) -> bool:
        return True

    def is_crystalline(self) -> bool:
        """Formal Tate labels are crystalline in the model."""
        return True


def universal_shadow_hodge(g_max: int = 8) -> UniversalShadowHodgeStructure:
    return UniversalShadowHodgeStructure(g_max=g_max)


# =============================================================================
# 10.  Concrete examples: Heisenberg, Virasoro, Lattice
# =============================================================================

def example_heisenberg(level_k: int = 1, g_max: int = 6) -> Dict[str, Any]:
    """Heisenberg H_k example: kappa = k (integer for level k).

    The finite scalar window has rational coefficients.  Class G in the
    shadow taxonomy.
    """
    kappa = Rational(level_k)
    return {
        "family": "Heisenberg H_k",
        "level": level_k,
        "kappa": kappa,
        "kappa_field": "Q (level is integer)",
        "tau_shadow_coeffs": tau_shadow_log_expansion(kappa, g_max),
        "motive": shadow_pro_motive(g_max),
        "hodge_structure": shadow_hodge_filtration(g_max),
        "shadow_class": "G (Gaussian)",
    }


def example_virasoro(c_value, g_max: int = 6) -> Dict[str, Any]:
    """Virasoro Vir_c example: kappa = c/2.

    For rational c, kappa is rational.  For c = 13 (self-dual), kappa = 13/2.
    For c = 26 (critical), kappa = 13.

    Class M in the shadow taxonomy (infinite tower at the FULL level, but
    the SCALAR projection is still kappa * lambda_g^FP at all genera).
    """
    if isinstance(c_value, (int, float, Fraction)):
        kappa = Rational(c_value) / 2
    else:
        kappa = c_value / 2
    return {
        "family": "Virasoro Vir_c",
        "c": c_value,
        "kappa": kappa,
        "kappa_field": "Q (c rational) or Q(c) (c symbolic)",
        "tau_shadow_coeffs": tau_shadow_log_expansion(kappa, g_max),
        "motive": shadow_pro_motive(g_max),
        "hodge_structure": shadow_hodge_filtration(g_max),
        "shadow_class": "M (mixed/infinite tower)",
        "note": "Scalar projection is kappa-linear; full Theta_A has higher arities.",
    }


def example_lattice_voa(rank: int, g_max: int = 6) -> Dict[str, Any]:
    """Lattice VOA V_Lambda example: kappa = rank(Lambda) (NOT c/2 — see AP48).

    For E_8: rank = 8.
    For Leech: rank = 24.
    """
    kappa = Rational(rank)
    return {
        "family": f"Lattice VOA V_Lambda, rank {rank}",
        "rank": rank,
        "kappa": kappa,
        "ap48_check": "kappa = rank, NOT c/2",
        "kappa_field": "Q (rank is integer)",
        "tau_shadow_coeffs": tau_shadow_log_expansion(kappa, g_max),
        "motive": shadow_pro_motive(g_max),
    }


# =============================================================================
# 11.  Top-level summary structure
# =============================================================================

def shadow_motivic_summary(g_max: int = 6) -> Dict[str, Any]:
    """Top-level summary of the finite formal motivic-shadow window."""
    return {
        "Q1_coefficient_field": {
            "rational_kappa": "Q[[q]] in finite windows",
            "number_field_kappa": "K[[q]] in finite windows",
            "transcendental_kappa": "Q[kappa][[q]] coefficientwise",
            "verdict": "formal exponential recurrence introduces no field beyond kappa",
        },
        "Q2_motive_at_genus": {
            f"g={g}": {
                "motive": str(motive_of_Fg(g)),
                "weight": 2 * g,
                "type": (g, g),
                "integrated_period_in": "Q",
            } for g in range(1, g_max + 1)
        },
        "Q3_hodge_structure": {
            "ambient_class": "(g, g) piece of H^{2g}(M-bar_g)",
            "is_pure": True,
            "is_tate": True,
        },
        "Q4_periods": {
            "rational_per_genus": True,
            "involves_mzv": False,
            "involves_pi": False,
            "deligne_critical_value": "compatible (pi^{2g} stripped)",
        },
        "Q5_pro_motive": {
            "object": "formal finite Tate labels Q(-g)",
            "motivic_galois_group": "not certified by this engine",
            "formal_weight_torus": True,
            "is_pure": False,
        },
        "Q6_beilinson": {
            "regulator_vanishes": "not certified",
            "reason": "finite coefficients certify rational periods only",
            "deligne_mhs": "formal (g, g) labels at each genus",
        },
        "Q7_negative_results": {
            "kdv_tau": "not certified by finite motivic coefficients",
            "mzv_at_F_g": "no positive-weight MZV content in rational F_g",
            "scalar_injectivity": "finite scalar coefficients recover kappa; abstract Tate shape does not",
        },
        "table_lambda_fp": faber_pandharipande_table(g_max),
        "universal_hodge": universal_shadow_hodge(g_max),
    }
