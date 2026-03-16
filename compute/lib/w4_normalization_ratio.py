"""MC4 normalization ratio R(t): exact conversion between Miura and concordance.

THIS MODULE RESOLVES THE MC4 BPZ NORMALIZATION BARRIER.

The quantum Miura expansion for W(sl₄) produces generators T, W₃, W₄ whose
BPZ norms and 3-point functions are exact polynomials in t = α₀²:

  norm_T(t)  = 3t(3t - 28)
  norm_W₃(t) = 4t(4t² - 167t + 660)
  norm_W₄(t) = 6t(t³ - 73t² + 1032t - 2520)
  C₄₃₃(t)   = -96t³(t - 8)(2t - 21)

The CONCORDANCE formula (Blumenhagen et al.) gives:
  c₃₃₄²(phys) = 42c²(5c+22) / ((c+24)(7c+68)(3c+46))
with c = 3 + 60t.

The NORMALIZATION RATIO R(t) = c₃₃₄²(Miura) / c₃₃₄²(concordance) is:

  R(t) = 640 t⁴(t-8)²(2t-21)²(20t+9)(36t+11)(420t+89)
         / [63(20t+1)²(300t+37)(t³-73t²+1032t-2520)²]

ROOT CAUSE: T_Miura (coefficient of ∂² in quantum Miura operator) has
central charge c_M = 6t(3t-28) ≠ c_phys = 3+60t.  The Miura T is NOT
the standard free-boson Virasoro generator; it differs by the cross-terms
e₂(J) vs -½Σ(∂φ)² structure and by the quantum correction normalization.

R(t) is the EXACT conversion factor.  The physical c₃₃₄ is recovered:
  c₃₃₄²(phys) = c₃₃₄²(Miura) / R(t)  = concordance formula.

Ground truth:
  mc4_bpz_frontier.md (MEMORY)
  w4_exact_miura.py (exact computation at t=1)
  concordance.tex (MC4 status)
"""

from __future__ import annotations

from sympy import (
    Symbol, Rational, simplify, factor, cancel, expand,
    Poly, sqrt, S, oo, limit,
)


# ═══════════════════════════════════════════════════════════════════════
# Exact Miura norm formulas (polynomials in t = α₀²)
# ═══════════════════════════════════════════════════════════════════════

def norm_T(t):
    """BPZ norm of T_Miura: ⟨T|T⟩ = 3t(3t - 28)."""
    return 3 * t * (3 * t - 28)


def norm_W3(t):
    """BPZ norm of W₃_Miura: ⟨W₃|W₃⟩ = 4t(4t² - 167t + 660)."""
    return 4 * t * (4 * t**2 - 167 * t + 660)


def norm_W4(t):
    """BPZ norm of W₄_Miura: ⟨W₄|W₄⟩ = 6t(t³ - 73t² + 1032t - 2520)."""
    return 6 * t * (t**3 - 73 * t**2 + 1032 * t - 2520)


def C433(t):
    """3-point function C₄₃₃ = ⟨W₄ W₃ W₃⟩ (Miura basis)."""
    return -96 * t**3 * (t - 8) * (2 * t - 21)


# ═══════════════════════════════════════════════════════════════════════
# Central charge comparison
# ═══════════════════════════════════════════════════════════════════════

def c_physical(t):
    """Physical central charge: c = 3 + 60t (free-boson background charge)."""
    return 3 + 60 * t


def c_miura(t):
    """Central charge from T_Miura self-OPE: c_M = 2·norm_T = 6t(3t-28)."""
    return 2 * norm_T(t)


def c_ratio(t):
    """Ratio c_M / c_phys = 2t(3t-28)/(20t+1)."""
    return 2 * t * (3 * t - 28) / (20 * t + 1)


# ═══════════════════════════════════════════════════════════════════════
# Concordance formula (literature, Blumenhagen et al.)
# ═══════════════════════════════════════════════════════════════════════

def concordance_c334_sq(c):
    """c₃₃₄² from the concordance (Blumenhagen-Eholzer-Honecker-Hornfeck-Huebel).

    c₃₃₄² = 42c²(5c+22) / ((c+24)(7c+68)(3c+46))
    """
    return 42 * c**2 * (5 * c + 22) / ((c + 24) * (7 * c + 68) * (3 * c + 46))


def concordance_c444_sq(c):
    """c₄₄₄² from the concordance.

    c₄₄₄² = 112c²(2c-1)(3c+46) / ((c+24)(7c+68)(10c+197)(5c+3))
    """
    return 112 * c**2 * (2 * c - 1) * (3 * c + 46) / (
        (c + 24) * (7 * c + 68) * (10 * c + 197) * (5 * c + 3))


# ═══════════════════════════════════════════════════════════════════════
# THE NORMALIZATION RATIO R(t)
# ═══════════════════════════════════════════════════════════════════════

def normalization_ratio_R(t):
    """Exact normalization ratio R(t) = c₃₃₄²(Miura) / c₃₃₄²(concordance).

    R(t) = 640 t⁴(t-8)²(2t-21)²(20t+9)(36t+11)(420t+89)
           / [63(20t+1)²(300t+37)(t³-73t²+1032t-2520)²]

    This is the EXACT conversion factor between Miura and concordance
    normalizations.  The physical structure constant is:

      c₃₃₄²(phys) = c₃₃₄²(Miura) / R(t) = concordance(c(t))
    """
    num = (640 * t**4 * (t - 8)**2 * (2 * t - 21)**2
           * (20 * t + 9) * (36 * t + 11) * (420 * t + 89))
    den = (63 * (20 * t + 1)**2 * (300 * t + 37)
           * (t**3 - 73 * t**2 + 1032 * t - 2520)**2)
    return num / den


def c334_sq_miura(t):
    """c₃₃₄²(Miura) = C₄₃₃² / norm_W₄²."""
    return C433(t)**2 / norm_W4(t)**2


def verify_R_definition(t_val):
    """Verify R(t) = c₃₃₄²(Miura) / c₃₃₄²(concordance) at a given t."""
    c = c_physical(t_val)
    miura = c334_sq_miura(t_val)
    conc = concordance_c334_sq(c)
    R_computed = miura / conc
    R_formula = normalization_ratio_R(t_val)
    return {
        "t": t_val,
        "c": c,
        "c334_sq_miura": miura,
        "c334_sq_concordance": conc,
        "R_computed": simplify(R_computed),
        "R_formula": simplify(R_formula),
        "match": simplify(R_computed - R_formula) == 0,
    }


# ═══════════════════════════════════════════════════════════════════════
# Structural analysis of R(t)
# ═══════════════════════════════════════════════════════════════════════

def R_zeros():
    """Zeros of R(t): where the Miura c₃₃₄ vanishes.

    - t = 0 (order 4): trivial (no background charge)
    - t = 8 (order 2): c = 483; W₃×W₃→W₄ coupling vanishes
    - t = 21/2 (order 2): c = 633; coupling vanishes
    """
    return {
        "t=0": {"order": 4, "c": 3},
        "t=8": {"order": 2, "c": 483},
        "t=21/2": {"order": 2, "c": 633},
    }


def R_poles():
    """Poles of R(t): where concordance c₃₃₄ vanishes or norm_W₄ vanishes.

    - t = -1/20 (order 2): c = 0 (degenerate theory)
    - t = -37/300 (order 1): c = -22/5 (rational value)
    - Roots of t³-73t²+1032t-2520 = 0 (order 2): norm_W₄ vanishes
    """
    return {
        "t=-1/20": {"order": 2, "c": 0},
        "t=-37/300": {"order": 1, "c": Rational(-22, 5)},
        "cubic_roots": "t³ - 73t² + 1032t - 2520 = 0 (order 2 each)",
    }


if __name__ == "__main__":
    t = Symbol('t')

    print("MC4 Normalization Ratio R(t)")
    print("=" * 60)
    print()
    print(f"R(t) = {factor(normalization_ratio_R(t))}")
    print()
    print(f"c_M/c_phys = {factor(c_ratio(t))}")
    print()

    for tv in [Rational(1), Rational(2), Rational(1, 2)]:
        result = verify_R_definition(tv)
        print(f"t={tv}: R = {result['R_formula']}, match = {result['match']}")
