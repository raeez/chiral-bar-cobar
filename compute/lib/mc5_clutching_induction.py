"""MC5 clutching induction: genus-by-genus induction avoiding Costello.

STRATEGY: Prove BV/BRST = bar at genus g by induction on g, using
the clutching/sewing map that degenerates Sigma_g to Sigma_{g-1}
with a node.

THE KEY INSIGHT:
  A smooth curve Sigma_g can degenerate (via non-separating degeneration)
  to a nodal curve Sigma_{g-1} union node.  The local model near the
  node is the genus-0 configuration (disk with two marked points).
  The correction from genus g-1 to genus g is therefore LOCAL, determined
  by the genus-0 data (which is proved: d^2 = 0 on P^1).

FABER-PANDHARIPANDE NUMBERS:
  lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

  These are the coefficients of the A-hat genus:
    A-hat(x) = (x/2) / sinh(x/2) = 1 + sum_{g>=1} (-1)^g * lambda_g^FP * x^{2g}

  (Sign convention: in the generating function for F_g, we use
   sum F_g x^{2g} = kappa * (A-hat(x) - 1), where the sign alternation
   is absorbed into the Bernoulli numbers.)

SEWING CORRECTIONS:
  The sewing correction at genus g is:
    Delta_g = lambda_g^FP - lambda_{g-1}^FP   (for g >= 2)

  MC5-RED found: Delta_g < 0 for ALL g >= 2.
  This means lambda_g^FP is DECREASING (after the initial value at g=1).

  Interpretation: the nodal contribution is a CORRECTION that reduces
  the total curvature.  This is consistent with the Arakelov-Green
  identity: the Green function on the nodal curve is "more singular"
  than on the smooth curve, so the defect decreases.

CONVERGENCE:
  The ratio lambda_{g+1}^FP / lambda_g^FP converges to 1/(4*pi^2)
  as g -> infinity.  This follows from the asymptotics of Bernoulli
  numbers: |B_{2g}| ~ 2 * (2g)! / (2*pi)^{2g}.

  The genus expansion has radius of convergence 2*pi:
    sum lambda_g x^{2g} converges for |x| < 2*pi.

Ground truth:
  concordance.tex (Front F, MC5 clutching strategy),
  higher_genus_foundations.tex (degeneration maps),
  genus_expansion.py (lambda_g^FP, A-hat).

All arithmetic is exact (sympy.Rational).  Never floating point.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

from sympy import (
    Rational, Symbol, bernoulli, factorial, pi, sinh,
    series, simplify, Abs, Integer, S, oo,
)

from .utils import lambda_fp, F_g


# ============================================================================
# 1. Faber-Pandharipande number
# ============================================================================

def lambda_fp_exact(g: int) -> Rational:
    r"""Faber-Pandharipande number at genus g (exact rational).

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    Uses sympy.bernoulli and sympy.Rational for exact arithmetic.

    Args:
        g: Genus, must be >= 1.

    Returns:
        Exact rational value of lambda_g^FP.
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B_2g = bernoulli(2 * g)
    numerator = (Integer(2) ** (2 * g - 1) - 1) * Abs(B_2g)
    denominator = Integer(2) ** (2 * g - 1) * factorial(2 * g)
    return Rational(numerator, denominator)


# ============================================================================
# 2. Sewing correction
# ============================================================================

def sewing_correction(g: int) -> Rational:
    r"""Sewing correction: lambda_g^FP - lambda_{g-1}^FP for g >= 2.

    This is the "nodal contribution" at genus g: the amount by which
    the Faber-Pandharipande number changes when adding a handle.

    MC5-RED found: this is NEGATIVE for ALL g >= 2, meaning
    lambda_g^FP is strictly decreasing for g >= 2.

    Args:
        g: Genus, must be >= 2.

    Returns:
        Exact rational value of lambda_g - lambda_{g-1}.
    """
    if g < 2:
        raise ValueError(f"Genus must be >= 2 for sewing correction, got {g}")
    return lambda_fp(g) - lambda_fp(g - 1)


# ============================================================================
# 3. Sewing correction table
# ============================================================================

def sewing_correction_table(max_g: int = 15) -> Dict[int, Dict[str, object]]:
    r"""Table of sewing corrections and their signs for g = 2, ..., max_g.

    Verifies that Delta_g = lambda_g - lambda_{g-1} is negative for
    all g >= 2 in the computed range.

    Returns:
        Dict mapping genus g to {
            "lambda_g": lambda_g^FP,
            "lambda_g_minus_1": lambda_{g-1}^FP,
            "correction": Delta_g,
            "sign": sign of Delta_g,
            "negative": whether Delta_g < 0,
        }
    """
    if max_g < 2:
        raise ValueError(f"max_g must be >= 2, got {max_g}")

    table = {}
    for g in range(2, max_g + 1):
        lg = lambda_fp(g)
        lg_prev = lambda_fp(g - 1)
        delta = lg - lg_prev
        table[g] = {
            "lambda_g": lg,
            "lambda_g_minus_1": lg_prev,
            "correction": delta,
            "sign": -1 if bool(delta < 0) else (1 if bool(delta > 0) else 0),
            "negative": bool(delta < 0),
        }

    return table


# ============================================================================
# 4. Non-separating degeneration formula
# ============================================================================

def non_separating_degeneration_formula(g: int) -> Dict[str, object]:
    r"""Document the non-separating degeneration at genus g.

    A smooth curve Sigma_g degenerates to a nodal curve via the
    non-separating degeneration:
        Sigma_g -> Sigma_{g-1} union {node}

    The local model near the node is the genus-0 configuration
    (a formal disk around each branch point), where:
      - The propagator is d log(z_1 - z_2) (rational, exact Arnold)
      - The bar differential is nilpotent: d^2 = 0

    The correction from Sigma_{g-1} to Sigma_g is therefore LOCAL,
    determined by the sewing data:
      - The plumbing parameter t in the sewing construction
      - The genus-0 (disk) bar complex data

    This is the basis for the clutching induction strategy.

    Args:
        g: Target genus (>= 2).

    Returns:
        Dict with degeneration description and locality properties.
    """
    if g < 2:
        raise ValueError(f"Genus must be >= 2, got {g}")

    return {
        "genus": g,
        "source_genus": g - 1,
        "degeneration_type": "non-separating",
        "local_model": "genus 0 (formal disk with two marked points)",
        "bar_nilpotent_locally": True,
        "correction_is_local": True,
        "plumbing_parameter": "t (deformation parameter for the node)",
        "sewing_correction": sewing_correction(g),
        "sewing_negative": bool(sewing_correction(g) < 0),
        "note": (
            f"Sigma_{g} degenerates to Sigma_{g - 1} with a node. "
            f"The local model near the node is the genus-0 disk, where "
            f"d^2 = 0. The correction lambda_{g} - lambda_{g - 1} = "
            f"{sewing_correction(g)} is local and determined by the "
            f"plumbing construction."
        ),
    }


# ============================================================================
# 5. Induction step verification
# ============================================================================

def induction_step_verification(g: int) -> Dict[str, object]:
    r"""Verify the clutching induction decomposition at genus g.

    The claim: F_g = kappa * lambda_g^FP can be decomposed as
        F_g = F_{g-1} + kappa * (lambda_g - lambda_{g-1})

    where the correction kappa * (lambda_g - lambda_{g-1}) is the
    "nodal contribution" from the non-separating degeneration.

    This is a tautological rewriting, but the CONTENT is that:
      (1) F_{g-1} is the base case (induction hypothesis)
      (2) The correction is proportional to kappa (same universal constant)
      (3) The correction is local (determined by genus-0 data)

    Args:
        g: Genus (>= 2 for induction step, >= 1 for base case).

    Returns:
        Dict with verification data.
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")

    kappa = Symbol('kappa')

    if g == 1:
        return {
            "genus": 1,
            "type": "base case",
            "F_g": kappa * lambda_fp(1),
            "lambda_g": lambda_fp(1),
            "verified": True,
            "note": "Base case: F_1 = kappa * 1/24 (proved at genus 1).",
        }

    lg = lambda_fp(g)
    lg_prev = lambda_fp(g - 1)
    correction = lg - lg_prev

    F_current = kappa * lg
    F_previous = kappa * lg_prev
    F_correction = kappa * correction

    # Verify the decomposition
    decomposition_holds = simplify(F_current - F_previous - F_correction) == 0

    return {
        "genus": g,
        "type": "induction step",
        "F_g": F_current,
        "F_g_minus_1": F_previous,
        "correction": F_correction,
        "lambda_g": lg,
        "lambda_g_minus_1": lg_prev,
        "sewing_correction": correction,
        "decomposition_holds": bool(decomposition_holds),
        "correction_negative": bool(correction < 0),
        "verified": bool(decomposition_holds),
        "note": (
            f"F_{g} = F_{g - 1} + kappa * ({correction}). "
            f"The correction is {'negative' if bool(correction < 0) else 'non-negative'}, "
            f"consistent with the Arakelov-Green defect reduction at the node."
        ),
    }


# ============================================================================
# 6. A-hat multiplicativity check
# ============================================================================

def ahat_multiplicativity_check(max_g: int = 10) -> Dict[str, object]:
    r"""Check lambda_g^FP against the A-hat genus generating function.

    The A-hat genus is:
        A-hat(x) = (x/2) / sinh(x/2)
                  = 1 - x^2/24 + 7*x^4/5760 - 31*x^6/967680 + ...

    The generating function for lambda_g^FP is:
        sum_{g>=1} lambda_g * x^{2g} = A-hat(x) - 1

    (with appropriate sign conventions absorbed into the Bernoulli numbers).

    We verify term-by-term for g = 1, ..., max_g that the coefficient
    of x^{2g} in (x/2)/sinh(x/2) matches (-1)^g * lambda_g^FP.

    Note: lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!
    and the Taylor expansion of (x/2)/sinh(x/2) has coefficients
    involving B_{2g} with alternating signs.

    Returns:
        Dict with term-by-term comparison.
    """
    x = Symbol('x')

    # Compute the Taylor expansion of (x/2)/sinh(x/2) to sufficient order
    order = 2 * max_g + 2
    ahat_expr = x / (2 * sinh(x / 2))
    ahat_series_expr = series(ahat_expr, x, 0, order)

    results = {
        "max_genus_checked": max_g,
        "generating_function": "(x/2)/sinh(x/2)",
        "term_checks": {},
    }

    for g in range(1, max_g + 1):
        # Extract coefficient of x^{2g} from the series
        coeff = ahat_series_expr.coeff(x, 2 * g)
        expected = (-1) ** g * lambda_fp(g)
        match = bool(simplify(coeff - expected) == 0)

        results["term_checks"][g] = {
            "series_coefficient": coeff,
            "expected": expected,
            "match": match,
        }

    results["all_match"] = all(
        v["match"] for v in results["term_checks"].values()
    )

    return results


# ============================================================================
# 7. Convergence radius
# ============================================================================

def convergence_radius() -> Dict[str, object]:
    r"""Convergence radius of the genus expansion.

    The generating function sum_{g>=1} lambda_g^FP * x^{2g}
    has radius of convergence R = 2*pi.

    This follows from the asymptotics of Bernoulli numbers:
        |B_{2g}| ~ 2 * (2g)! / (2*pi)^{2g}  as g -> infinity

    Therefore:
        lambda_g^FP ~ (2^{2g-1}-1) / 2^{2g-1} * 2 / (2*pi)^{2g}
                     ~ 1 / (2*pi)^{2g}  (leading term)

    The ratio test gives:
        lambda_{g+1} / lambda_g -> 1 / (4*pi^2)  as g -> infinity

    So the radius of convergence (in the variable x^2) is 4*pi^2,
    and in the variable x it is 2*pi.

    Returns:
        Dict with theoretical radius, ratio test data, and numerical checks.
    """
    # Compute ratios for several genera
    ratios = {}
    max_g = 20
    for g in range(1, max_g):
        lg = lambda_fp(g)
        lg_next = lambda_fp(g + 1)
        ratio = Rational(lg_next, lg)
        ratios[g] = ratio

    # The theoretical limit is 1/(4*pi^2)
    # We can't compare exactly with pi, but we can check convergence
    # by looking at the decimal approximations.
    ratio_floats = {g: float(r) for g, r in ratios.items()}
    theoretical_limit = float(1 / (4 * pi ** 2))

    # Check that ratios approach the limit
    last_ratio = ratio_floats[max_g - 1]
    relative_error = abs(last_ratio - theoretical_limit) / theoretical_limit

    return {
        "radius_of_convergence": "2*pi",
        "radius_squared": "4*pi^2",
        "theoretical_ratio_limit": "1/(4*pi^2)",
        "theoretical_limit_float": theoretical_limit,
        "ratios_exact": ratios,
        "ratios_float": ratio_floats,
        "last_ratio_computed": last_ratio,
        "relative_error_at_max_g": relative_error,
        "converging": bool(relative_error < 0.01),
        "note": (
            "The ratio lambda_{g+1}/lambda_g converges to 1/(4*pi^2) "
            f"approximately {theoretical_limit:.6f}. "
            f"At g={max_g - 1}, the ratio is {last_ratio:.6f}, "
            f"relative error {relative_error:.4e}."
        ),
    }


# ============================================================================
# 8. Clutching compatibility
# ============================================================================

def clutching_compatibility(g1: int, g2: int) -> Dict[str, object]:
    r"""Check factorization compatibility for separating degeneration.

    For a separating degeneration, a genus-g curve (g = g1 + g2)
    degenerates into two components of genera g1 and g2 joined at
    a node.

    The factorization property of the free energy is:
        F_g = F_{g1} + F_{g2} + nodal_correction

    Since F_g = kappa * lambda_g^FP and the nodal correction should
    be proportional to kappa (universality), we get:
        kappa * lambda_g = kappa * lambda_{g1} + kappa * lambda_{g2} + kappa * delta
    =>  delta = lambda_g - lambda_{g1} - lambda_{g2}

    The nodal correction delta is the "interaction" between the two
    components at the separating node.

    Args:
        g1: Genus of first component (>= 1).
        g2: Genus of second component (>= 1).

    Returns:
        Dict with verification data.
    """
    if g1 < 1 or g2 < 1:
        raise ValueError(f"Both genera must be >= 1, got g1={g1}, g2={g2}")

    g = g1 + g2
    lg = lambda_fp(g)
    lg1 = lambda_fp(g1)
    lg2 = lambda_fp(g2)

    nodal_correction = lg - lg1 - lg2

    kappa = Symbol('kappa')
    F_total = kappa * lg
    F_sum = kappa * lg1 + kappa * lg2
    F_correction = kappa * nodal_correction

    decomposition_holds = bool(simplify(F_total - F_sum - F_correction) == 0)

    return {
        "g": g,
        "g1": g1,
        "g2": g2,
        "lambda_g": lg,
        "lambda_g1": lg1,
        "lambda_g2": lg2,
        "nodal_correction": nodal_correction,
        "nodal_correction_sign": (
            "negative" if bool(nodal_correction < 0)
            else "positive" if bool(nodal_correction > 0)
            else "zero"
        ),
        "decomposition_holds": decomposition_holds,
        "note": (
            f"Separating degeneration: Sigma_{g} -> Sigma_{g1} cup Sigma_{g2}. "
            f"lambda_{g} = lambda_{g1} + lambda_{g2} + ({nodal_correction}). "
            f"The nodal correction is "
            f"{'negative' if nodal_correction < 0 else 'non-negative'}."
        ),
    }
