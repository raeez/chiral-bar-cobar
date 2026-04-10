r"""Shadow zeta engine: Z_A(s) = sum_{g=1}^{infty} F_g * g^{-s}.

The shadow zeta function encodes the genus tower of a chiral algebra A
into a single Dirichlet-type series.  At uniform weight with parameter
kappa = kappa(A), the genus-g free energy is

    F_g(kappa) = kappa^g * b_g

where b_g are universal rational coefficients determined by the formula

    b_g = (2^{2g-1} - 1) * |B_{2g}| / (2^{2g-1} * (2g)!)

with B_{2g} the Bernoulli numbers.  Equivalently,

    b_g = (1 - 2^{1-2g}) * |B_{2g}| / (2g)!

SANITY CHECKS:
  b_1 = 1/24         =>  F_1 = kappa/24
  b_2 = 7/5760       =>  F_2 = 7*kappa^2/5760
  # VERIFIED [DC] direct computation from Bernoulli  [LT] Faber-Pandharipande (1999)
  # VERIFIED b_1: F_1 = kappa/24 matches CLAUDE.md C24
  # VERIFIED b_2: F_2 = 7/5760 matches CLAUDE.md B37

CONVERGENCE:
  The ratios |b_{g+1}/b_g| converge to 1/(2*pi)^2, so b_g ~ C*(2*pi)^{-2g}.
  This is Gevrey-0 (geometric decay), NOT Gevrey-1 (factorial).
  The series F_g(kappa) converges absolutely when |kappa| < (2*pi)^2 ~ 39.478.
  All standard Virasoro test cases (c=1,13,25,26) lie within this radius.

  The shadow zeta Z_A(s) = sum F_g * g^{-s} inherits this convergence:
  for |kappa| < (2*pi)^2 the series converges absolutely for all Re(s) > 0,
  and in fact for all s in C (since |F_g| decays geometrically in g).

CONVENTIONS:
  - kappa(Vir_c) = c/2 (CLAUDE.md C2)
  - Cohomological grading, |d| = +1
  - B_{2g} with standard sign convention: B_2 = 1/6, B_4 = -1/30, ...
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Bernoulli numbers (exact, via the tangent-number recurrence)
# ---------------------------------------------------------------------------

def _bernoulli_exact(n: int) -> Fraction:
    """Compute B_n as an exact Fraction.

    Uses the standard recurrence: sum_{k=0}^{n} C(n+1,k) B_k = 0.
    Only even indices >= 2 are nonzero (besides B_0=1, B_1=-1/2).
    """
    if n < 0:
        raise ValueError(f"Bernoulli number index must be >= 0, got {n}")
    B: List[Fraction] = [Fraction(0)] * (n + 1)
    B[0] = Fraction(1)
    for m in range(1, n + 1):
        B[m] = Fraction(0)
        for k in range(m):
            B[m] -= Fraction(math.comb(m + 1, k), m + 1) * B[k]
        # B[m] is now correct
    return B[n]


# Cache the first 20 even Bernoulli numbers (B_2 through B_40)
_BERNOULLI_CACHE: Dict[int, Fraction] = {}


def bernoulli_even(g: int) -> Fraction:
    """Return B_{2g} as exact Fraction, cached."""
    if g not in _BERNOULLI_CACHE:
        _BERNOULLI_CACHE[g] = _bernoulli_exact(2 * g)
    return _BERNOULLI_CACHE[g]


# ---------------------------------------------------------------------------
# Shadow free energy coefficients b_g
# ---------------------------------------------------------------------------

def shadow_b_g(g: int) -> Fraction:
    r"""Universal coefficient b_g in F_g = kappa^g * b_g.

    Formula: b_g = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    # VERIFIED [DC] direct computation  [LT] Faber-Pandharipande (1999)
    # VERIFIED [CF] cross-check: b_1=1/24 matches C24; b_2=7/5760 matches B37
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B2g = bernoulli_even(g)
    abs_B2g = abs(B2g)
    power = 2 ** (2 * g - 1)
    numerator_factor = Fraction(power - 1, power)
    factorial_2g = Fraction(math.factorial(2 * g))
    return numerator_factor * abs_B2g / factorial_2g


def shadow_F_g(g: int, kappa: Fraction) -> Fraction:
    r"""Genus-g shadow free energy at uniform weight kappa.

    F_g(kappa) = kappa^g * b_g

    For Virasoro at central charge c: kappa = c/2 (CLAUDE.md C2).
    """
    return kappa ** g * shadow_b_g(g)


# ---------------------------------------------------------------------------
# Shadow zeta function
# ---------------------------------------------------------------------------

def shadow_zeta_terms(kappa: Fraction, G_max: int = 10) -> List[Fraction]:
    """Return [F_1, F_2, ..., F_{G_max}] at given kappa."""
    return [shadow_F_g(g, kappa) for g in range(1, G_max + 1)]


def shadow_zeta(s: float, kappa: Fraction, G_max: int = 10) -> float:
    r"""Evaluate Z_A(s) = sum_{g=1}^{G_max} F_g * g^{-s}.

    Parameters
    ----------
    s : float or complex
        The zeta argument.
    kappa : Fraction
        Uniform-weight parameter (= c/2 for Virasoro).
    G_max : int
        Truncation genus.

    Returns
    -------
    float
        The partial sum of Z_A(s).
    """
    total = 0.0
    for g in range(1, G_max + 1):
        Fg = float(shadow_F_g(g, kappa))
        total += Fg * g ** (-s)
    return total


def shadow_zeta_exact(s: int, kappa: Fraction, G_max: int = 10) -> Fraction:
    r"""Evaluate Z_A(s) exactly for integer s >= 0.

    At integer s, g^{-s} is rational, so the sum is exact.
    """
    total = Fraction(0)
    for g in range(1, G_max + 1):
        Fg = shadow_F_g(g, kappa)
        total += Fg * Fraction(1, g ** s)
    return total


# ---------------------------------------------------------------------------
# Convergence analysis
# ---------------------------------------------------------------------------

@dataclass
class ConvergenceAnalysis:
    """Result of convergence analysis for the shadow zeta series."""
    kappa: Fraction
    G_max: int
    terms: List[Fraction]
    ratios: List[float]
    gevrey_class: int
    convergence_radius_kappa: float
    is_convergent: bool
    asymptotic_ratio: float


def analyze_convergence(
    kappa: Fraction, G_max: int = 10
) -> ConvergenceAnalysis:
    r"""Analyze convergence of the shadow zeta series at given kappa.

    Computes:
    - The first G_max terms F_g
    - Successive ratios |F_{g+1}/F_g|
    - Gevrey classification (0 = geometric, 1 = factorial)
    - Convergence radius in kappa
    - Whether the series converges at this kappa

    The b_g satisfy |b_{g+1}/b_g| -> 1/(2*pi)^2, giving geometric decay
    (Gevrey-0).  The radius of convergence in kappa is (2*pi)^2.
    """
    terms = shadow_zeta_terms(kappa, G_max)

    # Ratios |F_{g+1}/F_g|
    ratios: List[float] = []
    for g in range(len(terms) - 1):
        if terms[g] != 0:
            ratios.append(abs(float(terms[g + 1]) / float(terms[g])))
        else:
            ratios.append(float('inf'))

    # Asymptotic ratio of |b_{g+1}/b_g| -> 1/(2*pi)^2
    # For F_g = kappa^g * b_g, |F_{g+1}/F_g| -> |kappa|/(2*pi)^2
    asymptotic_b_ratio = 1.0 / (2.0 * math.pi) ** 2
    convergence_radius = (2.0 * math.pi) ** 2  # ~ 39.478

    # Check: ratios should approach |kappa| * asymptotic_b_ratio
    kappa_float = abs(float(kappa))
    is_convergent = kappa_float < convergence_radius

    # Gevrey class: 0 (geometric/convergent), NOT 1 (factorial/asymptotic)
    # Evidence: |b_{g+1}/b_g| -> constant (not growing), so Gevrey-0.
    gevrey_class = 0

    return ConvergenceAnalysis(
        kappa=kappa,
        G_max=G_max,
        terms=terms,
        ratios=ratios,
        gevrey_class=gevrey_class,
        convergence_radius_kappa=convergence_radius,
        is_convergent=is_convergent,
        asymptotic_ratio=asymptotic_b_ratio,
    )


# ---------------------------------------------------------------------------
# Virasoro specialization
# ---------------------------------------------------------------------------

def virasoro_kappa(c: Fraction) -> Fraction:
    r"""kappa(Vir_c) = c/2.

    # VERIFIED [DC] CLAUDE.md C2  [LT] landscape_census.tex
    """
    return c / 2


def virasoro_shadow_zeta(
    s: float, c: Fraction, G_max: int = 10
) -> float:
    """Z_{Vir_c}(s) at central charge c."""
    return shadow_zeta(s, virasoro_kappa(c), G_max)


# ---------------------------------------------------------------------------
# Display / main
# ---------------------------------------------------------------------------

def _format_fraction(f: Fraction, max_digits: int = 40) -> str:
    """Format a fraction for display."""
    s = str(f)
    if len(s) <= max_digits:
        return s
    return f"{float(f):.15e}"


def print_shadow_zeta_report(c: Fraction, G_max: int = 10) -> None:
    """Print a full shadow zeta report for Virasoro at central charge c."""
    kappa = virasoro_kappa(c)
    print(f"\n{'='*70}")
    print(f"Shadow Zeta Function: Virasoro c = {c}, kappa = {kappa}")
    print(f"{'='*70}")

    # Terms
    terms = shadow_zeta_terms(kappa, G_max)
    print(f"\nGenus-g free energies F_g (uniform weight, kappa = {kappa}):")
    for g, Fg in enumerate(terms, 1):
        print(f"  g={g:2d}:  F_g = {_format_fraction(Fg):>45s}  ({float(Fg):+.10e})")

    # Zeta values
    print(f"\nShadow zeta Z_A(s) = sum_{{g=1}}^{{{G_max}}} F_g * g^{{-s}}:")
    for s_val in [0, 1, 2, 3, 4]:
        z_exact = shadow_zeta_exact(s_val, kappa, G_max)
        z_float = float(z_exact)
        print(f"  Z_A({s_val}) = {z_float:+.15e}  (exact: {_format_fraction(z_exact)})")

    # Convergence
    analysis = analyze_convergence(kappa, G_max)
    print(f"\nConvergence analysis:")
    print(f"  Gevrey class:              {analysis.gevrey_class} (geometric decay)")
    print(f"  Convergence radius:        (2*pi)^2 = {analysis.convergence_radius_kappa:.6f}")
    print(f"  |kappa| = {abs(float(kappa)):.6f} < {analysis.convergence_radius_kappa:.6f}: "
          f"{'CONVERGENT' if analysis.is_convergent else 'DIVERGENT'}")
    print(f"  Asymptotic |b_{{g+1}}/b_g|: 1/(2*pi)^2 = {analysis.asymptotic_ratio:.10f}")
    print(f"\n  Successive ratios |F_{{g+1}}/F_g|:")
    for g, r in enumerate(analysis.ratios, 1):
        print(f"    g={g:2d} -> {g+1:2d}:  {r:.10e}")


if __name__ == "__main__":
    # Virasoro at c = 1, 13, 25, 26
    # kappa(Vir_c) = c/2 (CLAUDE.md C2)
    # c=13: self-dual point (CLAUDE.md C8)
    # c=26: kappa=13, string theory critical dimension

    for c_val in [1, 13, 25, 26]:
        c = Fraction(c_val)
        print_shadow_zeta_report(c, G_max=10)

    # Summary comparison
    print(f"\n{'='*70}")
    print("Summary: Z_A(0) across central charges")
    print(f"{'='*70}")
    print(f"  Z_A(0) = sum F_g = total shadow amplitude\n")
    for c_val in [1, 13, 25, 26]:
        c = Fraction(c_val)
        kappa = virasoro_kappa(c)
        z0 = shadow_zeta_exact(0, kappa, 10)
        print(f"  c={c_val:2d} (kappa={str(kappa):>5s}):  Z_A(0) = {float(z0):+.15e}")

    print(f"\n{'='*70}")
    print("Summary: Z_A(1) across central charges")
    print(f"{'='*70}")
    print(f"  Z_A(1) = sum F_g/g = shadow log-amplitude\n")
    for c_val in [1, 13, 25, 26]:
        c = Fraction(c_val)
        kappa = virasoro_kappa(c)
        z1 = shadow_zeta_exact(1, kappa, 10)
        print(f"  c={c_val:2d} (kappa={str(kappa):>5s}):  Z_A(1) = {float(z1):+.15e}")
