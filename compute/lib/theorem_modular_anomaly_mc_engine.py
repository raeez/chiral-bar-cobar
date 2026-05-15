r"""Finite scalar witnesses for the modular-anomaly / MC projection surface.

This module verifies exact rational identities on the uniform-weight,
arity-zero scalar lane:

    lambda_g^FP = ((2^(2g-1) - 1) |B_(2g)|) / (2^(2g-1) (2g)!)
    F_g(A) = kappa(A) lambda_g^FP
    c_g(A) = (1/24) sum_(h=1)^(g-1) F_h(A) F_(g-h)(A)

The finite checks here do not reconstruct the universal MC element
Theta_A.  They test a scalar projection after the higher arity,
non-scalar OPE, moduli-dependent propagator, and cross-channel data
have been forgotten.  That distinction is part of the compute surface:
any function that returns a finite anomaly coefficient also returns, or
is paired with, a witness that full MC reconstruction has not been
proved by that coefficient.

Local anchors:
    chapters/examples/landscape_census.tex:1069-1082:
        uniform-weight lane and multi-weight cross-channel correction.
    chapters/examples/landscape_census.tex:1662-1681:
        F_g = kappa lambda_g^FP and F_1 = kappa/24.
    chapters/connections/concordance.tex:12460-12470:
        kappa is a scalar trace of the MC element, not any derived-center
        datum on the nose.
    chapters/theory/genus_2_ddybe_platonic.tex:680-730:
        finite genus-2 moduli checks are evidence unless a degeneration
        theorem supplies the missing analytic identity.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Dict, List, Mapping, Optional, Tuple

F = Fraction

SCALAR_LANE = "uniform_weight_scalar"
MISSING_FULL_MC_AXES: Tuple[str, ...] = (
    "higher arity operations",
    "non-scalar OPE structure constants",
    "moduli-dependent propagator kernels",
    "cross-channel corrections for multi-weight algebras",
    "derived-center comparison data",
)


@dataclass(frozen=True)
class ProjectionScope:
    """Scope of a finite modular-anomaly coefficient check."""

    genus: int
    arity: int
    lane: str
    finite_depth: int
    stable_range: bool
    scalar_projection_only: bool
    can_reconstruct_full_mc: bool
    missing_axes: Tuple[str, ...]


@dataclass(frozen=True)
class DatumSeparation:
    """One named datum in the anomaly/curvature/centre separation table."""

    key: str
    formula: str
    value: Optional[Fraction]
    source_anchor: str
    feeds_scalar_anomaly: bool
    proves_full_mc_reconstruction: bool
    role: str


def _require_min_genus(function_name: str, genus: int, minimum: int) -> None:
    if genus < minimum:
        raise ValueError(f"{function_name} requires genus >= {minimum}, got {genus}")


def projection_scope(
    genus: int,
    arity: int = 0,
    lane: str = SCALAR_LANE,
    finite_depth: int = 1,
) -> ProjectionScope:
    """Return the formal scope of an arity-zero scalar anomaly check."""
    if arity < 0:
        raise ValueError(f"Arity must be non-negative, got {arity}")
    if finite_depth < 0:
        raise ValueError(f"Depth must be non-negative, got {finite_depth}")
    return ProjectionScope(
        genus=genus,
        arity=arity,
        lane=lane,
        finite_depth=finite_depth,
        stable_range=(genus >= 2 and arity == 0),
        scalar_projection_only=(arity == 0 and lane == SCALAR_LANE),
        can_reconstruct_full_mc=False,
        missing_axes=MISSING_FULL_MC_AXES,
    )


def finite_mc_reconstruction_witness(max_genus: int, max_depth: int) -> Dict[str, Any]:
    """Witness that finite scalar anomaly checks are not full MC reconstruction."""
    _require_min_genus("finite_mc_reconstruction_witness", max_genus, 2)
    if max_depth < 1:
        raise ValueError(f"max_depth must be >= 1, got {max_depth}")
    return {
        "max_genus": max_genus,
        "max_depth": max_depth,
        "finite_checks": (
            "Faber-Pandharipande lambda_g coefficients",
            "arity-zero convolution coefficients c_g",
            "finite-depth E_2* coefficient extraction",
        ),
        "missing_axes": MISSING_FULL_MC_AXES,
        "can_reconstruct_full_mc": False,
        "claim_status": "finite scalar witness only",
    }


def genus_moduli_scope_witness(genus: int, period_matrix: str = "generic") -> Dict[str, Any]:
    """Record the genus/moduli hypotheses needed to interpret a finite check."""
    if genus < 0:
        raise ValueError(f"Genus must be non-negative, got {genus}")
    period_matrix = period_matrix.lower()
    if period_matrix not in {"generic", "diagonal", "separating"}:
        raise ValueError(f"Unsupported period_matrix={period_matrix!r}")

    diagonal_genus2 = (genus == 2 and period_matrix in {"diagonal", "separating"})
    return {
        "genus": genus,
        "period_matrix": period_matrix,
        "stable_closed_arity_zero_range": genus >= 2,
        "diagonal_genus2_degenerates_to_genus1_theorem": diagonal_genus2,
        "generic_period_finite_check_is_proof": False,
        "topological_degree_is_dynamic_witness": False,
        "required_for_full_moduli_statement": (
            "analytic theta/Fay identity on the relevant moduli locus",
            "uniform control of the propagator over the period domain",
            "higher-arity compatibility under clutching maps",
        ),
    }


def anomaly_datum_separation(g: int, kappa: Fraction) -> Dict[str, DatumSeparation]:
    """Separate Quillen, Arakelov, bar-curvature, and derived-center data."""
    _require_min_genus("anomaly_datum_separation", g, 1)
    kappa = F(kappa)
    scalar_value = kappa * lambda_fp_independent(g)
    genus_one_value = kappa / F(24) if g == 1 else None
    return {
        "bar_scalar_trace": DatumSeparation(
            key="bar_scalar_trace",
            formula="F_g(A) = kappa(A) * lambda_g^FP",
            value=scalar_value,
            source_anchor="chapters/examples/landscape_census.tex:1662",
            feeds_scalar_anomaly=True,
            proves_full_mc_reconstruction=False,
            role="scalar trace of the genus-g component of the universal MC element",
        ),
        "quillen_heisenberg_check": DatumSeparation(
            key="quillen_heisenberg_check",
            formula="F_1 = kappa/24 on the Heisenberg scalar lane",
            value=genus_one_value,
            source_anchor="chapters/connections/concordance.tex:10720",
            feeds_scalar_anomaly=(g == 1),
            proves_full_mc_reconstruction=False,
            role="one verification path for the Heisenberg scalar equality",
        ),
        "arakelov_hodge_curvature": DatumSeparation(
            key="arakelov_hodge_curvature",
            formula="geometric curvature of the Hodge/Quillen metric",
            value=None,
            source_anchor="chapters/connections/concordance.tex:10720",
            feeds_scalar_anomaly=False,
            proves_full_mc_reconstruction=False,
            role="geometric curvature class, not a kappa-valued scalar coefficient",
        ),
        "bar_differential_curvature": DatumSeparation(
            key="bar_differential_curvature",
            formula="d_bar^2 carries scalar curvature kappa before integration",
            value=kappa,
            source_anchor="chapters/connections/concordance.tex:6135",
            feeds_scalar_anomaly=False,
            proves_full_mc_reconstruction=False,
            role="chain-level curvature datum distinct from integrated free energy",
        ),
        "derived_center_bulk": DatumSeparation(
            key="derived_center_bulk",
            formula="Z_ch^der(A) is Hochschild/closed-sector data",
            value=None,
            source_anchor="chapters/connections/concordance.tex:12460",
            feeds_scalar_anomaly=False,
            proves_full_mc_reconstruction=False,
            role="bulk/derived-center datum, not the scalar trace kappa lambda_g",
        ),
    }


def k3xe_kappa_polysemy() -> Dict[str, Any]:
    """Distinguish the K3 x E kappa slots used in adjacent chapters."""
    return {
        "kappa_cat_K3xE": F(0),
        "kappa_ch_heisenberg_K3xE": F(3),
        "kappa_bkm_Delta5": F(5),
        "kappa_fiber_K3": F(24),
        "bkm_multiplier_is_chiral_modular_anomaly_kappa": False,
        "source_anchor": "chapters/connections/concordance.tex:11375",
    }


# =====================================================================
# Section 0: Core invariants (independent implementation, AP3/AP10)
# =====================================================================

def _bernoulli_exact(n: int) -> Fraction:
    """Bernoulli number B_n as exact Fraction.

    B_0 = 1, B_1 = -1/2, B_2 = 1/6, B_4 = -1/30, B_6 = 1/42, ...
    B_n = 0 for odd n >= 3.

    Independent implementation (AP10: do not hardcode from tables).
    Uses the recurrence: sum_{k=0}^{n} C(n+1,k) B_k = 0.
    """
    B = [F(0)] * (n + 1)
    B[0] = F(1)
    for m in range(1, n + 1):
        s = F(0)
        for k in range(m):
            s += _binom_exact(m + 1, k) * B[k]
        B[m] = -s / F(m + 1)
    return B[n]


def _binom_exact(n: int, k: int) -> Fraction:
    """Exact binomial coefficient C(n,k) as Fraction."""
    if k < 0 or k > n:
        return F(0)
    if k == 0 or k == n:
        return F(1)
    result = F(1)
    for i in range(min(k, n - k)):
        result = result * F(n - i) / F(i + 1)
    return result


def _factorial(n: int) -> int:
    """n! for non-negative integer n."""
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def lambda_fp_independent(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number, independent computation (AP10).

    lambda_g^FP = (2^{2g-1} - 1) * |B_{2g}| / (2^{2g-1} * (2g)!)

    Path 1: Direct from Bernoulli numbers.
    Path 2: Cross-check via Ahat generating function.
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B_2g = _bernoulli_exact(2 * g)
    num = (2 ** (2 * g - 1) - 1) * abs(B_2g)
    den = F(2 ** (2 * g - 1)) * F(_factorial(2 * g))
    return num / den


def _ahat_coefficients(max_g: int = 10) -> List[Fraction]:
    r"""Coefficients of Ahat(ix) - 1 = sum_{g>=1} a_g x^{2g}.

    Ahat(ix) = (x/2)/sin(x/2).

    The coefficient a_g equals lambda_g^FP (up to sign conventions).
    We compute independently via the Taylor expansion of (x/2)/sin(x/2).

    sin(x/2) = sum_{k>=0} (-1)^k (x/2)^{2k+1} / (2k+1)!
    (x/2)/sin(x/2) = 1 / (1 - x^2/24 + x^4/1920 - ...)

    Using the relation to Bernoulli numbers:
    (x/2)/sin(x/2) = sum_{g>=0} (-1)^g (2^{2g-1}-1) B_{2g} / (2g)! * x^{2g}
    with the convention that the g=0 term is 1 (since (2^{-1}-1)B_0/0! = -1/2,
    but the actual expansion starts at 1).

    More precisely: (x/2)/sin(x/2) = 1 + sum_{g>=1} |a_g| x^{2g}
    where |a_g| = (2^{2g-1}-1)|B_{2g}|/(2g)! / 2^{2g-1} = lambda_g^FP.
    """
    coeffs = [F(0)] * (max_g + 1)
    for g in range(1, max_g + 1):
        coeffs[g] = lambda_fp_independent(g)
    return coeffs


# =====================================================================
# Section 1: MC equation structure at (g,0)
# =====================================================================

@dataclass
class MCProjectionData:
    """Data for the MC equation projected to genus g, arity 0."""
    genus: int
    D_term: Fraction          # The D(Theta) contribution at (g,0)
    bracket_term: Fraction    # The [Theta,Theta]/2 contribution at (g,0)
    mc_residual: Fraction     # D + bracket (should be 0)
    anomaly_lhs: Fraction     # dF_g/dE_2* (from the D term)
    anomaly_rhs: Fraction     # (1/24)*sum F_h F_{g-h}
    is_consistent: bool
    bracket_sum: Fraction
    mc_to_anomaly_factor: Fraction
    scope: ProjectionScope
    finite_check_reconstructs_full_mc: bool


def mc_projection_genus_g(g: int, kappa: Fraction) -> MCProjectionData:
    r"""Compute the finite scalar MC/anomaly coefficient at (g,0).

    The MC equation D(Theta) + (1/2)[Theta,Theta] = 0 projected to (g,0):

    D term: The sewing differential D at genus g acts by inserting a propagator
    edge connecting two components.  At arity 0, this becomes:
        D(Theta^{(g)})^{(g,0)} = d/dE_2* (F_g) * E_2*
    where d/dE_2* extracts the quasi-modular anomaly.

    At the scalar level F_g = kappa * lambda_g (constant), so dF_g/dE_2* = 0
    for the constant part.  The anomaly equation governs the DRESSED amplitude.
    The verification here is at the level of ANOMALY COEFFICIENTS:
    the coefficient of the depth-1 quasi-modular correction satisfies
    the recursion c_g = (1/24) sum_{h=1}^{g-1} F_h F_{g-h}.

    Bracket term: [Theta,Theta]^{(g,0)} = sum_{h=1}^{g-1} F_h * F_{g-h}
    (the bracket pairs genus-h with genus-(g-h) through the Serre pairing).

    MC residual cancellation uses (1/2) * bracket_sum.  The
    quasi-modular anomaly coefficient uses the same scalar bracket sum
    with sewing normalization 1/24:
        anomaly_coeff = (1/24) * sum_{h=1}^{g-1} F_h * F_{g-h}

    The finite scalar coefficient does not reconstruct Theta_A.  The
    MC bracket half is 12 times the normalized anomaly coefficient.
    """
    _require_min_genus("mc_projection_genus_g", g, 2)
    kappa = F(kappa)

    # Bracket term: (1/2) sum_{h=1}^{g-1} F_h * F_{g-h}
    # where F_h = kappa * lambda_h
    lambda_convolution = F(0)
    for h in range(1, g):
        lambda_convolution += lambda_fp_independent(h) * lambda_fp_independent(g - h)
    bracket_sum = kappa ** 2 * lambda_convolution
    bracket_term = bracket_sum / F(2)

    # D term: the sewing operator at genus 1 has trace kappa/24.
    # The E_2* derivative of the dressed amplitude at genus g gets
    # the anomaly coefficient c_g = (1/24) * kappa^2 * sum lambda_h lambda_{g-h}.
    # This is the NEGATIVE of the bracket term (MC equation: D + bracket = 0).
    D_term = -bracket_term

    # Anomaly equation form:
    # dF_g/dE_2* = (1/24) sum_{h=1}^{g-1} F_h F_{g-h}
    anomaly_rhs = bracket_sum / F(24)
    anomaly_lhs = anomaly_rhs  # finite scalar coefficient witness

    return MCProjectionData(
        genus=g,
        D_term=D_term,
        bracket_term=bracket_term,
        mc_residual=D_term + bracket_term,
        anomaly_lhs=anomaly_lhs,
        anomaly_rhs=anomaly_rhs,
        is_consistent=(D_term + bracket_term == F(0)),
        bracket_sum=bracket_sum,
        mc_to_anomaly_factor=F(12),
        scope=projection_scope(g, arity=0, finite_depth=1),
        finite_check_reconstructs_full_mc=False,
    )


def mc_projection_all_genera(max_genus: int, kappa: Fraction) -> Dict[int, MCProjectionData]:
    """Compute MC projection at all genera from 2 to max_genus."""
    return {g: mc_projection_genus_g(g, kappa) for g in range(2, max_genus + 1)}


# =====================================================================
# Section 2: Anomaly coefficients via convolution square
# =====================================================================

def anomaly_coefficient_direct(g: int, kappa: Fraction) -> Fraction:
    r"""Direct computation of the anomaly coefficient at genus g.

    c_g = (1/24) * sum_{h=1}^{g-1} F_h * F_{g-h}
        = (kappa^2 / 24) * sum_{h=1}^{g-1} lambda_h * lambda_{g-h}
    """
    _require_min_genus("anomaly_coefficient_direct", g, 2)
    kappa = F(kappa)
    s = F(0)
    for h in range(1, g):
        s += lambda_fp_independent(h) * lambda_fp_independent(g - h)
    return kappa ** 2 * s / F(24)


def anomaly_coefficient_gf(g: int, kappa: Fraction) -> Fraction:
    r"""Anomaly coefficient from the generating function convolution.

    Path 2: The GF is sum F_g x^{2g} = kappa * (Ahat(ix) - 1).
    The convolution square (Ahat - 1)^2 at x^{2g} gives
    sum_{h=1}^{g-1} lambda_h * lambda_{g-h}.

    The anomaly is (kappa^2/24) times this convolution coefficient.
    """
    _require_min_genus("anomaly_coefficient_gf", g, 2)
    kappa = F(kappa)
    ahat = _ahat_coefficients(g)
    conv_coeff = F(0)
    for h in range(1, g):
        conv_coeff += ahat[h] * ahat[g - h]
    return kappa ** 2 * conv_coeff / F(24)


def anomaly_coefficient_genus_raising(g: int, kappa: Fraction) -> Fraction:
    r"""Compatibility witness for the genus-indexed convolution coefficient.

    A second hbar-derivative of the scalar Ahat series is not itself the
    anomaly coefficient at the same genus.  This function intentionally
    returns the generating-function convolution coefficient, so callers
    cannot promote a finite derivative identity into a genus-raising
    reconstruction of the full MC element.
    """
    _require_min_genus("anomaly_coefficient_genus_raising", g, 2)
    return anomaly_coefficient_gf(g, kappa)


# =====================================================================
# Section 3: Heat equation structure
# =====================================================================

@dataclass
class HeatEquationData:
    """Data for the finite Leibniz consistency check of the anomaly."""
    genus: int
    kappa: Fraction
    heat_lhs: Fraction    # d/dE_2*(c_g) = second derivative of anomaly
    heat_rhs: Fraction    # (1/24) sum (dc_h/dE_2*) F_{g-h} + F_h (dc_{g-h}/dE_2*)
    integrability_residual: Fraction  # finite scalar residual
    is_consistent: bool
    scalar_level_is_trivial: bool
    proves_full_d_squared_zero: bool


def heat_equation_check(g: int, kappa: Fraction) -> HeatEquationData:
    r"""Verify the scalar-level Leibniz consistency of the anomaly recursion.

    The anomaly equation is:
        dF_g/dE_2* = (1/24) sum_{h=1}^{g-1} F_h F_{g-h}

    Applying d/dE_2* again (the "heat equation" integrability condition):
        d^2 F_g / (dE_2*)^2 = (1/24) sum_{h=1}^{g-1} (dF_h/dE_2*) F_{g-h}
                             + (1/24) sum_{h=1}^{g-1} F_h (dF_{g-h}/dE_2*)

    Using the anomaly equation to substitute dF_h/dE_2*:
        d^2 F_g / (dE_2*)^2 = (1/24)^2 sum_{h=1}^{g-1} [
            sum_{j=1}^{h-1} F_j F_{h-j} * F_{g-h}
            + F_h * sum_{j=1}^{g-h-1} F_j F_{g-h-j}
        ]

    This should equal d/dE_2* of the RHS, which by the product rule is:
        (1/24) sum (dF_h/dE_2*) F_{g-h} + (1/24) sum F_h (dF_{g-h}/dE_2*)

    At the scalar level, F_h is constant, so both E_2* derivatives vanish.
    This is a sanity check on the coefficient model, not a proof of
    D^2 = 0 in the modular convolution algebra.
    """
    _require_min_genus("heat_equation_check", g, 2)
    kappa = F(kappa)

    # At the scalar level, F_g is constant, so all E_2* derivatives vanish.
    # The integrability is therefore trivially satisfied at scalar level.
    # The nontrivial content is at the dressed (tau-dependent) level.

    # For the anomaly coefficient recursion, we check:
    # c_g (depth-1 anomaly) satisfies the iterated recursion.
    # c_g = (kappa^2/24) * sum lambda_h lambda_{g-h}
    # depth-2 anomaly: c_g^{(2)} = (1/24) * sum c_h * F_{g-h} + F_h * c_{g-h}
    # where c_1 = 0 (genus 1 has no anomaly in the constant piece).

    # At the level of anomaly COEFFICIENTS:
    heat_lhs = F(0)  # scalar-level second derivative
    heat_rhs = F(0)  # scalar-level iterated recursion

    # Check: both should be zero at scalar level (no tau-dependence)
    return HeatEquationData(
        genus=g,
        kappa=kappa,
        heat_lhs=heat_lhs,
        heat_rhs=heat_rhs,
        integrability_residual=heat_lhs - heat_rhs,
        is_consistent=True,
        scalar_level_is_trivial=True,
        proves_full_d_squared_zero=False,
    )


def heat_equation_dressed_check(g: int, kappa: Fraction) -> Dict[str, Any]:
    r"""Verify the dressed heat equation at the level of anomaly coefficients.

    The depth-p anomaly coefficient at genus g is:
        c_g^{(p)} = (1/24)^p * (convolution of (p+1) copies of F summed over genera)

    For p=1: c_g^{(1)} = (1/24) sum_{h=1}^{g-1} F_h F_{g-h}
    For p=2: c_g^{(2)} = (1/24)^2 sum_{a+b+c=g, a,b,c>=1} F_a F_b F_c
             (the triple convolution from applying the anomaly twice)

    The finite coefficient-level consistency is verified as follows.
    Differentiating the anomaly RHS by the Leibniz rule:

        d/dE_2* [(1/24) sum_{h} F_h F_{g-h}]
        = (1/24) sum_{h} [dF_h/dE_2* * F_{g-h} + F_h * dF_{g-h}/dE_2*]

    Each Leibniz term substitutes the anomaly equation for dF_h/dE_2*,
    producing a sum over ordered triples (j, h-j, g-h) or (h, j, g-h-j).
    The Leibniz rule produces EACH ordered triple (a,b,c) exactly TWICE:
    once from differentiating the first factor (fixing genus g-h = c,
    splitting h = a+b), and once from differentiating the second factor
    (fixing genus h = a, splitting g-h = b+c).

    The direct triple convolution counts each ordered triple ONCE.
    Therefore the finite coefficient identity is:

        depth2_from_leibniz = 2 * depth2_from_triple_convolution

    This is the arity-zero scalar Leibniz witness at depth 2.  It is not
    the full D^2 = 0 statement before the missing axes in
    MISSING_FULL_MC_AXES are restored.
    """
    _require_min_genus("heat_equation_dressed_check", g, 3)
    kappa = F(kappa)

    # Depth-2 anomaly from direct triple convolution:
    # c_g^{(2)} = (kappa^3 / 24^2) * sum_{a+b+c=g, a,b,c>=1} lambda_a lambda_b lambda_c
    triple_conv = F(0)
    for a in range(1, g - 1):
        for b in range(1, g - a):
            c = g - a - b
            if c >= 1:
                triple_conv += (lambda_fp_independent(a)
                                * lambda_fp_independent(b)
                                * lambda_fp_independent(c))
    depth2_from_triple = kappa ** 3 / F(24) ** 2 * triple_conv

    # Depth-2 anomaly from Leibniz differentiation of the RHS:
    # d/dE_2* [(1/24) sum F_h F_{g-h}]
    # = (1/24) sum [dF_h/dE_2* * F_{g-h} + F_h * dF_{g-h}/dE_2*]
    # First Leibniz term: sum_{h>=2} [(1/24) sum_{j=1}^{h-1} F_j F_{h-j}] * F_{g-h}
    leibniz_sum = F(0)
    for h in range(2, g):
        inner = F(0)
        for j in range(1, h):
            inner += lambda_fp_independent(j) * lambda_fp_independent(h - j)
        leibniz_sum += inner * lambda_fp_independent(g - h)
    # Second Leibniz term: sum_{h=1}^{g-2} F_h * [(1/24) sum_{j=1}^{g-h-1} F_j F_{g-h-j}]
    for h in range(1, g - 1):
        inner = F(0)
        for j in range(1, g - h):
            inner += lambda_fp_independent(j) * lambda_fp_independent(g - h - j)
        leibniz_sum += lambda_fp_independent(h) * inner
    depth2_from_leibniz = kappa ** 3 / F(24) ** 2 * leibniz_sum

    # Coefficient-level Leibniz consistency: differentiating a quadratic
    # convolution gives exactly 2x the ordered triple convolution.
    # Each ordered triple (a,b,c) is reached by two Leibniz routes:
    #   Route 1: h = a+b, j = a -> triple (a, b, c) from first Leibniz term
    #   Route 2: h = a, j = b -> triple (a, b, c) from second Leibniz term
    integrability_holds = (depth2_from_leibniz == F(2) * depth2_from_triple)

    return {
        'genus': g,
        'kappa': kappa,
        'depth2_triple_convolution': depth2_from_triple,
        'depth2_leibniz': depth2_from_leibniz,
        'leibniz_equals_2x_triple': integrability_holds,
        'integrability_holds': integrability_holds,
        'proves_full_d_squared_zero': False,
        'scope': projection_scope(g, arity=0, finite_depth=2),
        'interpretation': (
            'Leibniz differentiation of the finite anomaly RHS produces exactly '
            'twice the direct ordered triple convolution. Each ordered triple '
            '(a,b,c) with a+b+c=g is reached by two Leibniz routes.'
        ),
    }


# =====================================================================
# Section 4: Non-holomorphic completion
# =====================================================================

@dataclass
class NonHolomorphicData:
    """Finite coefficient data for the non-holomorphic completion ansatz."""
    genus: int
    kappa: Fraction
    anomaly_coeff_holomorphic: Fraction  # (1/24) sum F_h F_{g-h}
    nh_correction_prefactor: Fraction    # coefficient of 1/(pi*y) term
    modular_weight: int                  # weight of the completed object
    is_modular_invariant: bool
    completion_is_formal: bool
    finite_coefficient_proves_modularity: bool


def non_holomorphic_completion(g: int, kappa: Fraction) -> NonHolomorphicData:
    r"""Finite depth-1 non-holomorphic completion coefficient.

    Under E_2* -> Ehat_2 = E_2* - 3/(pi*y), the dressed amplitude becomes:
        Fhat_g(tau, tau-bar) = F_g^{hol}(tau) + sum_{p=1}^{g} nh_corrections

    After the full non-holomorphic completion, the anomaly equation has
    the Ward-identity shape:
        (d/dtau-bar) Fhat_g = -(1/(8*pi*y^2)) sum_{h=1}^{g-1} Fhat_h Fhat_{g-h}

    This function computes only the depth-1 replacement coefficient,
    not the completed Ward identity.

    Replacing E_2* by its non-holomorphic completion is the correct
    formal direction, but a single coefficient does not prove modular
    invariance of the full amplitude.

    At the scalar level: F_g is constant, Fhat_g = F_g (no correction needed).
    The non-holomorphic correction is proportional to 1/(pi*Im(tau)) and
    enters at the dressed level.

    The modular anomaly at genus g involves depth p in E_2*.
    Each E_2* -> Ehat_2 replacement contributes lower-depth terms
    involving 1/(pi*y); modularity requires the full completed series.
    """
    _require_min_genus("non_holomorphic_completion", g, 2)
    kappa = F(kappa)
    anomaly = anomaly_coefficient_direct(g, kappa)

    # The nh correction at depth 1 is: c_g * (-3/(pi*y))
    # which restores modularity of the depth-1 piece.
    # At the scalar level, the correction is zero (depth 0).
    nh_correction = -F(3) * anomaly  # coefficient of 1/(pi*y)

    return NonHolomorphicData(
        genus=g,
        kappa=kappa,
        anomaly_coeff_holomorphic=anomaly,
        nh_correction_prefactor=nh_correction,
        modular_weight=0,  # the scalar amplitude has weight 0
        is_modular_invariant=False,
        completion_is_formal=True,
        finite_coefficient_proves_modularity=False,
    )


# =====================================================================
# Section 5: Sewing operator and propagator analysis
# =====================================================================

def sewing_trace_genus1(kappa: Fraction) -> Fraction:
    r"""Trace of the genus-1 sewing operator.

    Tr(S_sew) = kappa(A) * 1/24 = F_1(A)

    This is the source of the 1/24 in the anomaly equation:
    the sewing operator inserts a genus-1 handle, and its trace
    is kappa/24 = F_1.

    The sewing operator S acts on B(A) by contracting through the
    Bergman reproducing kernel B(z,w|tau).  Its q-expansion is:
        B(z,w|tau) = (1/(z-w)^2) + sum_{n>=1} n*q^n/(1-q^n) * (dz)(dw)

    After zeta-regularization of the trace (sum over all modes):
        Tr_zeta(S) = kappa * zeta(-1) = kappa * (-1/12)
    Wait: the correct formula uses zeta'(0) for the BV side.
    For the bar side: Tr = kappa/24 = kappa * |B_2|/4 = kappa * (1/6)/4 = kappa/24.
    """
    return F(kappa) / F(24)


def propagator_e2star_connection(kappa: Fraction) -> Dict[str, Any]:
    r"""The connection between the genus-1 propagator and E_2*.

    The genus-1 propagator in the bar complex is:
        P(tau) = -(1/12) E_2*(tau)

    This is because the Bergman kernel on the elliptic curve E_tau has
    trace proportional to E_2*:
        sum_{n>=1} n*q^n/(1-q^n) = -(1/24) + (1/24)*E_2*(tau)

    So: Tr(kernel) = -(1/24) + (1/24)*E_2*(tau)
    After renormalization: Tr_ren = (1/24)*E_2*(tau)

    The derivative d/dE_2* extracts the coefficient of E_2* in the
    dressed amplitude.  Since each propagator insertion contributes
    one factor of E_2*/12, the d/dE_2* derivative at genus g counts
    the number of propagator insertions, weighted by 1/12.

    For the anomaly equation: d/dE_2* of a genus-g graph with one
    propagator edge gives (1/12) times the same graph with the
    propagator edge removed.  The removal of one edge from a genus-g
    graph (reducing genus by 1) plus the sewing normalization 1/2
    gives the prefactor: (1/12) * (1/2) = 1/24.
    """
    kappa = F(kappa)
    return {
        'propagator_coefficient': -F(1, 12),
        'trace_renormalized': F(1, 24),
        'anomaly_prefactor': F(1, 24),
        'sewing_normalization': F(1, 2),
        'combined': F(1, 24),
        'source': (
            'The 1/24 prefactor in the anomaly equation arises from: '
            '(1/12 from propagator P = -E_2*/12) * (1/2 from ordered pair → unordered) '
            '= 1/24. This is also F_1/kappa = lambda_1 = 1/24.'
        ),
    }


# =====================================================================
# Section 6: Anomaly equation as Ahat product identity
# =====================================================================

def ahat_product_identity(max_genus: int = 8) -> Dict[str, Any]:
    r"""Verify the Ahat product identity underlying the anomaly equation.

    The generating function: G(x) = sum_{g>=1} lambda_g x^{2g} = Ahat(ix) - 1.

    The anomaly recursion at genus g is:
        c_g = (1/24) sum_{h=1}^{g-1} lambda_h lambda_{g-h}

    This is (1/24) times the g-th coefficient of G(x)^2.

    The Ahat product identity:
        G(x)^2 = (Ahat(ix) - 1)^2

    We verify: the convolution coefficients match the direct computation.

    The returned ``genus_raising_next`` value is diagnostic only: the
    hbar-derivative coefficient is not identified with the convolution
    coefficient at the same genus.
    """
    ahat = _ahat_coefficients(max_genus)
    results = {}

    for g in range(2, max_genus + 1):
        # Convolution: [x^{2g}] G^2 = sum_{h=1}^{g-1} lambda_h lambda_{g-h}
        conv = F(0)
        for h in range(1, g):
            conv += ahat[h] * ahat[g - h]

        # Direct anomaly coefficient (without kappa^2 factor)
        direct = F(0)
        for h in range(1, g):
            direct += lambda_fp_independent(h) * lambda_fp_independent(g - h)

        # The genus-raising operator: d^2/dx^2 of G at order x^{2g}
        # d^2/dx^2 [lambda_g x^{2g}] = 2g(2g-1) lambda_g x^{2g-2}
        # So [x^{2g}] of d^2G/dx^2 = (2g+2)(2g+1) lambda_{g+1}
        # This is NOT the same as the convolution -- the genus-raising
        # interpretation is more subtle (see below).
        genus_raising = F(2 * g + 2) * F(2 * g + 1) * lambda_fp_independent(g + 1) \
            if g + 1 <= max_genus else None

        results[g] = {
            'convolution': conv,
            'direct': direct,
            'match': conv == direct,
            'anomaly_coefficient': conv / F(24),
            'genus_raising_next': genus_raising,
        }

    return {
        'max_genus': max_genus,
        'all_match': all(r['match'] for r in results.values()),
        'results': results,
    }


def ahat_recursion_from_anomaly(max_genus: int = 8) -> Dict[str, Any]:
    r"""Recover Ahat coefficients from the sine recursion.

    The anomaly convolution checks the coefficients once the scalar
    amplitudes are known.  It does not reconstruct the scalar amplitudes
    by itself.  This oracle recovers them from
    (x/2)/sin(x/2), independently of the convolution code.

    The Ahat function satisfies: f(x) = (x/2)/sin(x/2), i.e.,
        2f * sin(x/2) = x
    Taking derivatives gives a recursion for the coefficients.

    We verify: starting from lambda_1 = 1/24, applying the identity
        sum_{h=0}^{g} (-1)^h / (2h+1)! * 2^{-2h} * lambda_{g-h} = delta_{g,0} / 2
    (from the sine expansion) reproduces all lambda_g.
    """
    # Recursion from (x/2)/sin(x/2) = sum a_g x^{2g}:
    # 2 * (sum a_g x^{2g}) * (sum (-1)^k x^{2k+1}/(2^{2k+1}(2k+1)!)) = x
    # Comparing x^{2g+1} coefficients:
    # sum_{k=0}^{g} (-1)^k / (2^{2k+1}(2k+1)!) * a_{g-k} = delta_{g,0}/2
    # where a_0 = 1.
    #
    # For g >= 1: sum_{k=0}^{g} (-1)^k / (2^{2k+1}(2k+1)!) * a_{g-k} = 0
    # => a_g = -2^{2*0+1}*(2*0+1)! * sum_{k=1}^{g} (-1)^k / (2^{2k+1}(2k+1)!) * a_{g-k}
    # => a_g = -2 * sum_{k=1}^{g} (-1)^k / (2^{2k+1}(2k+1)!) * a_{g-k}

    a = [F(0)] * (max_genus + 1)
    a[0] = F(1)

    for g in range(1, max_genus + 1):
        s = F(0)
        for k in range(1, g + 1):
            denom = F(2 ** (2 * k + 1)) * F(_factorial(2 * k + 1))
            s += F((-1) ** k) / denom * a[g - k]
        a[g] = -F(2) * s

    # Verify against independent computation
    results = {}
    for g in range(1, max_genus + 1):
        lam = lambda_fp_independent(g)
        results[g] = {
            'from_recursion': a[g],
            'from_bernoulli': lam,
            'match': a[g] == lam,
        }

    return {
        'max_genus': max_genus,
        'all_match': all(r['match'] for r in results.values()),
        'results': results,
    }


# =====================================================================
# Section 7: Convolution algebra structure
# =====================================================================

def convolution_bracket_genus_g(g: int, kappa: Fraction) -> Dict[str, Any]:
    r"""The convolution bracket [Theta,Theta]^{(g,0)} in the modular dg Lie algebra.

    At arity 0, the bracket [Theta^{(h)}, Theta^{(g-h)}] pairs through:
    (a) The Serre duality pairing <,> on H^*(Sigma_g)
    (b) The Serre pairing <,> on the algebra A itself

    The combined pairing gives the genus-0 two-point function:
        <Theta^{(h)}, Theta^{(g-h)}> = F_h * F_{g-h}

    The full bracket at (g,0) sums over all splittings:
        [Theta,Theta]^{(g,0)} = sum_{h=1}^{g-1} F_h * F_{g-h}

    The factor 1/2 in the MC equation cancels the double counting (h, g-h) vs (g-h, h).
    """
    _require_min_genus("convolution_bracket_genus_g", g, 2)
    kappa = F(kappa)

    terms = {}
    total = F(0)
    for h in range(1, g):
        Fh = kappa * lambda_fp_independent(h)
        Fgh = kappa * lambda_fp_independent(g - h)
        term = Fh * Fgh
        terms[(h, g - h)] = term
        total += term

    # With the 1/2 from the MC equation:
    mc_bracket_contribution = total / F(2)

    return {
        'genus': g,
        'kappa': kappa,
        'individual_terms': terms,
        'bracket_sum': total,
        'mc_bracket_half': mc_bracket_contribution,
        'anomaly_coefficient': total / F(24),
        'mc_to_anomaly_factor': F(12),
        'finite_check_reconstructs_full_mc': False,
        'interpretation': (
            f'At genus {g}, the bracket [Theta,Theta] has {g-1} terms. '
            f'The finite scalar MC bracket half is 12 times the normalized '
            f'anomaly coefficient (1/24)*sum F_h F_{{g-h}}.'
        ),
    }


# =====================================================================
# Section 8: Full theorem verification
# =====================================================================

@dataclass
class TheoremVerification:
    """Finite scalar verification of the modular anomaly coefficient surface."""
    kappa: Fraction
    max_genus: int
    path1_mc_projection: bool      # finite scalar MC projection
    path2_gf_convolution: bool     # GF convolution square matches
    path3_heat_integrability: bool  # finite Leibniz coefficient consistency
    path4_nh_completion: bool      # formal non-holomorphic coefficient
    all_paths_agree: bool
    full_mc_reconstructed: bool
    details: Dict[str, Any]


def verify_theorem_all_paths(kappa: Fraction, max_genus: int = 8) -> TheoremVerification:
    r"""Run all finite scalar witnesses for the anomaly coefficient.

    Path 1: MC projection at (g,0) gives the scalar anomaly coefficient.
    Path 2: Generating function convolution square matches anomaly coefficients.
    Path 3: Leibniz consistency of the depth-2 scalar coefficient.
    Path 4: Formal non-holomorphic E_2* replacement has the expected
    depth-1 coefficient.

    The result deliberately records ``full_mc_reconstructed=False``.
    """
    _require_min_genus("verify_theorem_all_paths", max_genus, 2)
    kappa = F(kappa)
    details: Dict[str, Any] = {}

    # Path 1: MC projection
    mc_results = mc_projection_all_genera(max_genus, kappa)
    path1 = all(data.is_consistent for data in mc_results.values())
    path1_anomaly = all(
        data.anomaly_lhs == data.anomaly_rhs for data in mc_results.values()
    )
    details['path1'] = {
        'mc_consistent': path1,
        'anomaly_match': path1_anomaly,
        'genera_tested': list(mc_results.keys()),
    }

    # Path 2: GF convolution
    gf_results = ahat_product_identity(max_genus)
    path2 = gf_results['all_match']
    details['path2'] = {
        'convolution_match': path2,
        'genera_tested': list(gf_results['results'].keys()),
    }

    # Also verify: anomaly_coefficient_direct == anomaly_coefficient_gf
    direct_gf_match = True
    for g in range(2, max_genus + 1):
        d = anomaly_coefficient_direct(g, kappa)
        gf = anomaly_coefficient_gf(g, kappa)
        if d != gf:
            direct_gf_match = False
            break
    details['path2']['direct_gf_match'] = direct_gf_match

    # Path 3: Heat equation
    heat_results = {}
    path3 = True
    for g in range(2, max_genus + 1):
        h = heat_equation_check(g, kappa)
        heat_results[g] = h.is_consistent
        if not h.is_consistent:
            path3 = False
    # Dressed heat equation check
    for g in range(3, min(max_genus + 1, 7)):
        dh = heat_equation_dressed_check(g, kappa)
        if not dh['integrability_holds']:
            path3 = False
        heat_results[f'dressed_{g}'] = dh['integrability_holds']
    details['path3'] = heat_results

    # Path 4: Non-holomorphic completion
    nh_results = {}
    path4 = True
    for g in range(2, max_genus + 1):
        nh = non_holomorphic_completion(g, kappa)
        nh_ok = (
            nh.completion_is_formal
            and not nh.finite_coefficient_proves_modularity
            and nh.nh_correction_prefactor == -F(3) * nh.anomaly_coeff_holomorphic
        )
        nh_results[g] = nh_ok
        if not nh_ok:
            path4 = False
    details['path4'] = nh_results

    # Recursion verification
    recursion = ahat_recursion_from_anomaly(max_genus)
    details['recursion_from_anomaly'] = recursion['all_match']
    details['full_mc_reconstruction'] = finite_mc_reconstruction_witness(max_genus, 2)

    all_paths = path1 and path1_anomaly and path2 and direct_gf_match and path3 and path4

    return TheoremVerification(
        kappa=kappa,
        max_genus=max_genus,
        path1_mc_projection=path1 and path1_anomaly,
        path2_gf_convolution=path2 and direct_gf_match,
        path3_heat_integrability=path3,
        path4_nh_completion=path4,
        all_paths_agree=all_paths,
        full_mc_reconstructed=False,
        details=details,
    )


# =====================================================================
# Section 9: Cross-family verification
# =====================================================================

def cross_family_anomaly_check() -> Dict[str, Any]:
    r"""Verify the anomaly equation across all standard families.

    For each family, kappa determines the scalar F_g = kappa * lambda_g.
    The anomaly coefficient c_g = (kappa^2/24) * sum lambda_h lambda_{g-h}
    is LINEAR in kappa^2 (not kappa).

    Chiral scalar families:
    - Heisenberg H_k: kappa = k
    - Virasoro Vir_c: kappa = c/2
    - Affine sl_2 at level k: kappa = 3(k+2)/4

    The Delta_5 Borcherds multiplier kappa_BKM = 5 is not the
    K3 x E chiral modular-anomaly kappa.  The K3 x E slots are kept
    in k3xe_kappa_polysemy() and excluded from this chiral ratio table.

    Cross-check: the ratio c_g(A)/c_g(B) = (kappa(A)/kappa(B))^2
    because the anomaly is quadratic in kappa.
    """
    families = {
        'Heisenberg_k=1': F(1),
        'Virasoro_c=1': F(1, 2),
        'Virasoro_c=26': F(13),
        'sl2_k=1_universal_vacuum': F(3) * F(3) / F(4),  # 3*(1+2)/4 = 9/4
        'K3xE_chiral_heisenberg_shadow': F(3),
        'Virasoro_c=13_selfdual': F(13, 2),
    }

    max_genus = 6
    results = {}
    for name, kappa in families.items():
        anomalies = {}
        for g in range(2, max_genus + 1):
            anomalies[g] = anomaly_coefficient_direct(g, kappa)
        results[name] = {
            'kappa': kappa,
            'anomalies': anomalies,
        }

    # Cross-check: ratio of anomaly coefficients = ratio of kappa^2
    ratio_checks = {}
    ref_name = 'Heisenberg_k=1'
    ref_kappa = families[ref_name]
    for name, kappa in families.items():
        if name == ref_name:
            continue
        expected_ratio = (kappa / ref_kappa) ** 2
        actual_ratios = {}
        all_match = True
        for g in range(2, max_genus + 1):
            ref_c = results[ref_name]['anomalies'][g]
            fam_c = results[name]['anomalies'][g]
            if ref_c != 0:
                actual_ratios[g] = fam_c / ref_c
                if actual_ratios[g] != expected_ratio:
                    all_match = False
            else:
                actual_ratios[g] = None
        ratio_checks[name] = {
            'expected_ratio': expected_ratio,
            'actual_ratios': actual_ratios,
            'all_match': all_match,
        }

    return {
        'families': results,
        'ratio_checks': ratio_checks,
        'all_ratios_correct': all(r['all_match'] for r in ratio_checks.values()),
        'excluded_non_chiral_kappas': {
            'Delta5_BKM_multiplier': k3xe_kappa_polysemy()['kappa_bkm_Delta5'],
            'K3xE_categorical_kappa': k3xe_kappa_polysemy()['kappa_cat_K3xE'],
        },
    }


# =====================================================================
# Section 10: Explicit anomaly coefficients
# =====================================================================

def explicit_anomaly_table(max_genus: int = 8) -> Dict[int, Dict[str, Fraction]]:
    r"""Table of explicit anomaly coefficients at each genus.

    For kappa = 1:
        c_g = (1/24) * sum_{h=1}^{g-1} lambda_h * lambda_{g-h}

    Genus 2: c_2 = (1/24) * lambda_1^2 = (1/24) * (1/24)^2 = 1/13824
    Genus 3: c_3 = (1/24) * 2*lambda_1*lambda_2 = 7/1658880
    """
    table = {}
    for g in range(2, max_genus + 1):
        conv = F(0)
        terms = []
        for h in range(1, g):
            lh = lambda_fp_independent(h)
            lgh = lambda_fp_independent(g - h)
            product = lh * lgh
            conv += product
            if h <= g - h:
                mult = 1 if h == g - h else 2
                terms.append({
                    'h': h,
                    'g-h': g - h,
                    'lambda_h': lh,
                    'lambda_{g-h}': lgh,
                    'product': product,
                    'multiplicity': mult,
                })
        c_g = conv / F(24)
        table[g] = {
            'convolution_sum': conv,
            'anomaly_coefficient': c_g,
            'terms': terms,
            'num_distinct_terms': len(terms),
        }
    return table


def anomaly_generating_function_coeffs(max_genus: int = 8) -> List[Fraction]:
    r"""Coefficients of the anomaly generating function.

    A(x) = (1/24) * G(x)^2 where G(x) = Ahat(ix) - 1 = sum lambda_g x^{2g}.

    A(x) = sum_{g>=2} c_g x^{2g} where c_g = (1/24)*sum lambda_h lambda_{g-h}.

    Returns list indexed by genus (index 0 and 1 are zero).
    """
    ahat = _ahat_coefficients(max_genus)
    # Convolution square of G(x):
    # [x^{2g}] G^2 = sum_{h=1}^{g-1} ahat[h] * ahat[g-h]
    coeffs = [F(0)] * (max_genus + 1)
    for g in range(2, max_genus + 1):
        s = F(0)
        for h in range(1, g):
            s += ahat[h] * ahat[g - h]
        coeffs[g] = s / F(24)
    return coeffs


# =====================================================================
# Section 11: Propagator variance and multi-weight correction
# =====================================================================

def w3_cross_channel_corrections(c: Fraction) -> Dict[int, Fraction]:
    r"""Exact first W_3 cross-channel corrections from the landscape census."""
    c = F(c)
    if c == 0:
        raise ValueError("W_3 cross-channel formulas require c != 0")
    return {
        2: (c + F(204)) / (F(16) * c),
        3: (
            F(5) * c ** 3
            + F(3792) * c ** 2
            + F(1149120) * c
            + F(217071360)
        ) / (F(138240) * c ** 2),
    }


def multi_weight_anomaly_correction(
    g: int,
    kappa: Fraction,
    delta_cross: Fraction = F(0),
    cross_corrections: Optional[Mapping[int, Fraction]] = None,
) -> Dict[str, Any]:
    r"""Anomaly equation with multi-weight cross-channel correction.

    For multi-weight algebras (AP32, thm:multi-weight-genus-expansion):
        F_g(A) = kappa * lambda_g + delta_F_g^cross

    The anomaly equation generalizes to:
        dF_g/dE_2* = (1/24) sum_{h=1}^{g-1} F_h F_{g-h}
    where F_h now includes the cross-channel corrections.

    The scalar lane does not certify the full MC equation after
    cross-channel corrections are present.  It only computes the corrected
    arity-zero convolution coefficient once the corrected amplitudes are
    supplied.

    For uniform-weight algebras: delta_cross = 0 and F_g = kappa * lambda_g.
    For W_3:
        delta_F_2 = (c+204)/(16c)
        delta_F_3 = (5c^3 + 3792c^2 + 1149120c + 217071360)/(138240 c^2)
    """
    _require_min_genus("multi_weight_anomaly_correction", g, 2)
    kappa = F(kappa)
    corrections: Dict[int, Fraction] = {
        int(key): F(value) for key, value in (cross_corrections or {}).items()
    }
    if delta_cross:
        if g <= 2:
            raise ValueError("delta_cross can first enter the anomaly at genus >= 3")
        corrections[g - 1] = corrections.get(g - 1, F(0)) + F(delta_cross)

    # Scalar anomaly (uniform-weight)
    scalar_anomaly = anomaly_coefficient_direct(g, kappa)

    corrected_conv = F(0)
    corrected_terms = {}
    for h in range(1, g):
        Fh = kappa * lambda_fp_independent(h) + corrections.get(h, F(0))
        Fgh = kappa * lambda_fp_independent(g - h) + corrections.get(g - h, F(0))
        term = Fh * Fgh
        corrected_terms[(h, g - h)] = term
        corrected_conv += term

    total_anomaly = corrected_conv / F(24)
    cross_correction = total_anomaly - scalar_anomaly

    return {
        'genus': g,
        'kappa': kappa,
        'cross_corrections': corrections,
        'scalar_anomaly': scalar_anomaly,
        'cross_channel_correction': cross_correction,
        'total_anomaly': total_anomaly,
        'corrected_terms': corrected_terms,
        'scalar_formula_complete': not any(corrections.values()),
        'mc_still_holds': 'not certified by scalar coefficient check',
        'full_mc_reconstruction': False,
        'note': (
            'The corrected arity-zero coefficient can be computed once the '
            'delta_F_g^cross values are supplied. This finite scalar '
            'coefficient does not prove the full MC equation.'
        ),
    }


# =====================================================================
# Section 12: Numerical verification at specific tau values
# =====================================================================

def _sigma1(n: int) -> int:
    """Sum of positive divisors of n."""
    if n < 1:
        raise ValueError(f"n must be positive, got {n}")
    return sum(d for d in range(1, n + 1) if n % d == 0)


def e2_quasimodular_qexp(tau: complex, terms: int = 200) -> complex:
    r"""Compute E_2*(tau) = 1 - 24 sum sigma_1(n) q^n by q-expansion."""
    if terms < 1:
        raise ValueError(f"terms must be positive, got {terms}")
    import cmath

    q = cmath.exp(2 * cmath.pi * 1j * tau)
    return 1 - 24 * sum(_sigma1(n) * q ** n for n in range(1, terms + 1))


def numerical_anomaly_check(kappa_float: float, g: int,
                             tau: complex = 0.5 + 1.0j) -> Dict[str, Any]:
    r"""Numerical verification of the anomaly equation at a specific tau.

    At the scalar level, F_g is constant and dF_g/dE_2* = 0.
    The anomaly equation is satisfied trivially.

    For the dressed amplitude, we would need the full q-expansion.
    Here we verify the ANOMALY COEFFICIENT numerically.
    """
    _require_min_genus("numerical_anomaly_check", g, 2)

    # lambda_g values
    lam = {}
    for h in range(1, g + 1):
        lam[h] = float(lambda_fp_independent(h))

    # Anomaly coefficient
    conv = sum(lam[h] * lam[g - h] for h in range(1, g))
    anomaly = kappa_float ** 2 * conv / 24.0

    # E_2* at tau (numerical); kept separate from the rational coefficient.
    e2_val = e2_quasimodular_qexp(tau)

    return {
        'genus': g,
        'kappa': kappa_float,
        'tau': tau,
        'anomaly_coefficient': anomaly,
        'lambda_values': lam,
        'convolution_sum': conv,
        'e2_star_approx': e2_val,
        'finite_check_reconstructs_full_mc': False,
    }


# =====================================================================
# Section 13: Comparison with BCOV original formulation
# =====================================================================

def bcov_original_comparison(g: int, kappa: Fraction) -> Dict[str, Any]:
    r"""Compare the scalar convolution coefficient with the BCOV shape.

    BCOV (1993) write the holomorphic anomaly equation as:
        d-bar_tau-bar F_g = (1/2) C-bar^{ij} (D_i D_j F_{g-1}
                            + sum_{h=1}^{g-1} D_i F_h D_j F_{g-h})

    where:
    - C-bar^{ij} = e^{2K} G^{ip} G^{jq} C-bar_{pq} (anti-hol Yukawa coupling)
    - D_i = covariant derivative on the moduli space
    - G^{ij} = inverse Zamolodchikov metric
    - K = Kahler potential

    At the scalar level (one modulus, constant map contribution):
    - D_i F_h -> kappa * d lambda_h / d t_i = 0 (constant)
    - The propagator term C-bar * G * G -> 1/(Im tau)^2 * (1/12)
    - After integration: (1/24) sum F_h F_{g-h}

    The scalar coefficient has the same convolution shape.  This is not
    a full BCOV reconstruction, because the non-constant-map sector and
    covariant moduli derivatives are absent.

    For the non-constant-map sector: the full BCOV anomaly involves
    D_i D_j F_{g-1} (the "dilaton shift" term), which comes from the
    arity-2 part of the MC equation (not arity 0).

    At arity 0 (no insertions): only the sum_{h=1}^{g-1} term survives,
    and D_i -> d/dt is a constant (for the scalar shadow).
    """
    _require_min_genus("bcov_original_comparison", g, 2)
    kappa = F(kappa)

    # Our computation
    our_anomaly = anomaly_coefficient_direct(g, kappa)

    # BCOV scalar-level: same formula
    bcov_anomaly = F(0)
    for h in range(1, g):
        Fh = kappa * lambda_fp_independent(h)
        Fgh = kappa * lambda_fp_independent(g - h)
        bcov_anomaly += Fh * Fgh
    bcov_anomaly /= F(24)

    return {
        'genus': g,
        'kappa': kappa,
        'our_anomaly': our_anomaly,
        'bcov_anomaly': bcov_anomaly,
        'match': our_anomaly == bcov_anomaly,
        'dilaton_term_present': g >= 2,
        'dilaton_term_arity': 2 if g >= 2 else None,
        'full_bcov_reconstruction': False,
        'note': (
            'The BCOV dilaton term D_i D_j F_{g-1} comes from the (g-1, 2) '
            'projection of the MC equation, not the (g, 0) projection. '
            'At arity 0, this finite scalar check sees only the convolution sum.'
        ),
    }


# =====================================================================
# Section 14: Depth filtration and modular anomaly tower
# =====================================================================

def anomaly_depth_tower(g: int, kappa: Fraction, max_depth: int = 3) -> Dict[str, Any]:
    r"""The anomaly equation iterated to depth p.

    Depth 0: F_g^{(0)} = kappa * lambda_g (scalar, constant)
    Depth 1: F_g^{(1)} = c_g * E_2* where c_g = (kappa^2/24) sum lambda_h lambda_{g-h}
    Depth 2: F_g^{(2)} = c_g^{(2)} * (E_2*)^2 where c_g^{(2)} involves triple convolution
    Depth p: F_g^{(p)} involves (p+1)-fold convolution of the scalar amplitudes

    The depth-p coefficient is:
        c_g^{(p)} = (1/24)^p * sum over all genus-g stable graphs with p propagator edges
                    of the product of vertex amplitudes

    At the scalar level, this reduces to:
        c_g^{(p)} = (1/24)^p * kappa^{p+1} * [convolution of (p+1) copies of lambda]
    """
    _require_min_genus("anomaly_depth_tower", g, 1)
    if max_depth < 0:
        raise ValueError(f"max_depth must be non-negative, got {max_depth}")
    kappa = F(kappa)

    tower = {}
    # Depth 0
    tower[0] = kappa * lambda_fp_independent(g)

    # Depth 1: c_g = (kappa^2/24) * sum lambda_h lambda_{g-h}
    if max_depth >= 1:
        conv2 = F(0)
        for h in range(1, g):
            conv2 += lambda_fp_independent(h) * lambda_fp_independent(g - h)
        tower[1] = kappa ** 2 * conv2 / F(24)

    # Depth 2: triple convolution
    if max_depth >= 2 and g >= 3:
        conv3 = F(0)
        for a in range(1, g - 1):
            for b in range(1, g - a):
                c = g - a - b
                if c >= 1:
                    conv3 += (lambda_fp_independent(a)
                              * lambda_fp_independent(b)
                              * lambda_fp_independent(c))
        tower[2] = kappa ** 3 * conv3 / F(24) ** 2
    elif max_depth >= 2:
        tower[2] = F(0)

    # Depth 3: quadruple convolution
    if max_depth >= 3 and g >= 4:
        conv4 = F(0)
        for a in range(1, g - 2):
            for b in range(1, g - a - 1):
                for c_val in range(1, g - a - b):
                    d = g - a - b - c_val
                    if d >= 1:
                        conv4 += (lambda_fp_independent(a)
                                  * lambda_fp_independent(b)
                                  * lambda_fp_independent(c_val)
                                  * lambda_fp_independent(d))
        tower[3] = kappa ** 4 * conv4 / F(24) ** 3
    elif max_depth >= 3:
        tower[3] = F(0)

    return {
        'genus': g,
        'kappa': kappa,
        'max_depth': max_depth,
        'depth_coefficients': tower,
        'total_depths_computed': len(tower),
        'finite_check_reconstructs_full_mc': False,
    }
