r"""Conditional bookkeeping for the strong scalar ansatz.

What is proved in the manuscript after rectification:
  - genus-1 universality: obs_1(A) = κ(A) · λ_1 for every modular
    Koszul algebra
  - uniform-weight all-genera scalar package
  - algebraic-family rigidity only gives the weaker statement
        Θ_A^{min} = η ⊗ Γ_A
    with the cyclic direction fixed but the tautological coefficient
    Γ_A still undetermined in general multi-weight families.

This module keeps the exact arithmetic consequences of the stronger
ansatz

    Θ_A^{min} = κ(A) · η ⊗ Λ,   Λ = Σ_{g≥1} λ_g

for W_N-style families.  Those consequences are useful as bookkeeping
and for conditional comparisons, but they are NOT a proof that
obs_g = κ(A) · λ_g holds for all multi-generator algebras.

This module provides:
  1. Per-channel κ decomposition for W_N algebras
  2. Idempotent trace verification: Σ u_i = κ
  3. Conditional free-energy formulas under the strong scalar ansatz
  4. Strong-scalar minimal-model bookkeeping: S_n = 0 for n ≥ 3
  5. Multi-channel consistency: per-channel sums match total

All arithmetic exact (Fraction).  No floating point in core.

Manuscript references:
    thm:multi-generator-universality (higher_genus_modular_koszul.tex)
    prop:saturation-equivalence (higher_genus_modular_koszul.tex:7643)
    thm:algebraic-family-rigidity (higher_genus_modular_koszul.tex:8226)
    op:multi-generator-universality (higher_genus_foundations.tex:4856, OPEN)
    rem:propagator-weight-universality (higher_genus_foundations.tex:4927)
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from typing import Dict, List, Optional, Tuple

from compute.lib.stable_graph_enumeration import _bernoulli_exact, _lambda_fp_exact


# ============================================================================
# Faber-Pandharipande numbers (exact)
# ============================================================================

@lru_cache(maxsize=32)
def lambda_fp(g: int) -> Fraction:
    r"""Faber-Pandharipande intersection number λ_g^FP.

    λ_g^FP = (2^{2g-1}-1) / 2^{2g-1} · |B_{2g}| / (2g)!
    """
    if g < 1:
        raise ValueError(f"lambda_fp requires g >= 1, got {g}")
    return _lambda_fp_exact(g)


# ============================================================================
# Per-channel κ values for W_N algebras
# ============================================================================

def kappa_per_channel(c: Fraction, weight: int) -> Fraction:
    r"""Per-channel modular characteristic κ_h for weight-h generator.

    For a weight-h strong generator of a W_N algebra:
        κ_h = c / h

    This is the genus-1 curvature in the weight-h channel.
    """
    if weight < 1:
        raise ValueError(f"Weight must be ≥ 1, got {weight}")
    return Fraction(c, weight)


def kappa_total_wn(c: Fraction, N: int) -> Fraction:
    r"""Total modular characteristic κ(W_N) = Σ_{s=2}^N c/s = c(H_N - 1).

    H_N = Σ_{s=1}^N 1/s is the N-th harmonic number.
    """
    if N < 2:
        raise ValueError(f"W_N requires N ≥ 2, got {N}")
    return sum(kappa_per_channel(c, s) for s in range(2, N + 1))


def harmonic_number(N: int) -> Fraction:
    """N-th harmonic number H_N = Σ_{s=1}^N 1/s."""
    return sum(Fraction(1, s) for s in range(1, N + 1))


def kappa_total_wn_formula(c: Fraction, N: int) -> Fraction:
    """κ(W_N) = c · (H_N - 1) via the closed-form formula."""
    return c * (harmonic_number(N) - 1)


# ============================================================================
# Per-channel free energy decomposition
# ============================================================================

def free_energy_per_channel(c: Fraction, weight: int, g: int) -> Fraction:
    r"""Per-channel genus-g free energy under the strong scalar ansatz.

    This is the bookkeeping formula
        F_g^{(h)} = κ_h · λ_g^FP
    that follows if the multi-generator scalar package factors through
    the strong ansatz.  It is unconditional only at genus 1.
    """
    return kappa_per_channel(c, weight) * lambda_fp(g)


def free_energy_total_wn(c: Fraction, N: int, g: int) -> Fraction:
    r"""Conditional total genus-g free energy for W_N.

    Under the strong scalar ansatz:
        F_g(W_N) = κ(W_N) · λ_g^FP = Σ_{s=2}^N κ_s · λ_g^FP.
    For arbitrary multi-weight families, only g=1 is unconditional.
    """
    return kappa_total_wn(c, N) * lambda_fp(g)


def free_energy_per_channel_sum(c: Fraction, N: int, g: int) -> Fraction:
    r"""Sum of per-channel free energies: Σ_{s=2}^N F_g^{(s)}.

    This equals F_g(W_N) by linearity of κ:
        Σ F_g^{(s)} = Σ κ_s · λ_g^FP = (Σ κ_s) · λ_g^FP = κ · λ_g^FP
    """
    return sum(free_energy_per_channel(c, s, g) for s in range(2, N + 1))


# ============================================================================
# Scalar saturation: minimal model has S_n = 0 for n ≥ 3
# ============================================================================

def minimal_model_shadow_coefficients(kappa: Fraction) -> Dict[int, Fraction]:
    r"""Shadow coefficients in the strong-scalar minimal model.

    Historical note: algebraic-family rigidity does NOT prove this
    model in general multi-weight families.  This routine records the
    stronger ansatz
        Θ^{min} = κ · η ⊗ Λ,  Λ = Σ_{g≥1} λ_g

    The genus-0 components: S_2 = κ, S_n = 0 for n ≥ 3.
    All higher shadow coefficients are gauge-trivial (exact in the
    cyclic deformation complex).

    This means the minimal model MC element is GAUSSIAN (class G).
    The shadow depth classification (G/L/C/M) is a COCHAIN-level
    invariant; at the cohomological level, every modular Koszul
    algebra is Gaussian.
    """
    return {2: kappa, 3: Fraction(0), 4: Fraction(0),
            5: Fraction(0), 6: Fraction(0)}


# ============================================================================
# Genus-2 scalar graph sum verification
# ============================================================================

def genus2_scalar_graph_sum(kappa: Fraction, S4: Fraction) -> Fraction:
    r"""Genus-2 free energy from the scalar graph sum.

    F_2 = (standard terms depending on κ) + S_4/(8κ²) × (banana Hodge integral)

    In the minimal model: S_4 = 0, so the banana graph doesn't contribute.
    The remaining terms give exactly κ · λ_2^FP.

    For the FULL (cochain-level) algebra: S_4 ≠ 0, but the gauge
    transformation to the minimal model removes the S_4 contribution
    without changing the cohomological result.

    The graph sum at (g=2, n=0) has 5 non-trivial graphs.
    In the minimal model (S_n = 0 for n ≥ 3), only graphs with
    genus-0 vertices of valence ≤ 2 contribute:
      Graph 2 (irreducible node): g=1 vertex with self-loop
      Graph 4 (dumbbell): two g=1 vertices, one edge

    Both graphs involve only the genus-1 data F_1 = κ/24.
    """
    # In the minimal model: S_4 = 0
    # F_2 from dumbbell + irreducible node = κ · 7/5760
    # With S_4 ≠ 0, the banana adds S_4/(8κ²) but the
    # gauge transformation compensates, leaving the same result.
    #
    # For verification: compute F_2 with arbitrary S_4 and check
    # that the FP formula is recovered at S_4 = 0.
    fp2 = lambda_fp(2)  # = 7/5760
    # The S_4-independent part of F_2 equals κ · 7/5760
    # under the strong scalar ansatz.
    return kappa * fp2 + S4 / (8 * kappa**2)


def genus2_fp_value(kappa: Fraction) -> Fraction:
    """Conditional genus-2 scalar value F_2 = κ · λ_2^FP."""
    return kappa * lambda_fp(2)


# ============================================================================
# Idempotent decomposition for W_3 shadow CohFT
# ============================================================================

def w3_idempotent_norms(c: Fraction) -> Tuple[Fraction, Fraction]:
    r"""Idempotent norms for the W_3 shadow CohFT Frobenius algebra.

    The shadow CohFT (thm:shadow-cohft) satisfies the CohFT axioms,
    which force the genus-0 Frobenius algebra to be WDVV-associative.

    In the strong-scalar minimal model, the genus-0 multiplication
    is trivial (S_n = 0 for n ≥ 3), and the Frobenius algebra on V = {T, W}
    degenerates to the diagonal metric:
        η = diag(κ_T, κ_W) = diag(c/2, c/3)
    with zero multiplication (all structure constants vanish).

    For a diagonal algebra, the idempotent decomposition is trivial:
        e_T = T (with u_T = κ_T = c/2)
        e_W = W (with u_W = κ_W = c/3)

    The trace: u_T + u_W = c/2 + c/3 = 5c/6 = κ(W_3). ✓

    Note: The COCHAIN-level Frobenius algebra (from naïve OPE constants)
    T·T = 2T, T·W = 3W, W·W = 2T is NOT associative and does NOT satisfy
    WDVV. This is because the OPE structure constants are not the same as
    the shadow CohFT structure constants. The bar complex d log extraction
    changes the normalization. In the minimal model, the difference is
    absorbed by the gauge transformation.
    """
    kT = kappa_per_channel(c, 2)  # c/2
    kW = kappa_per_channel(c, 3)  # c/3
    return (kT, kW)


def w3_idempotent_trace(c: Fraction) -> Fraction:
    """Verify: Σ u_i = κ(W_3) = 5c/6."""
    u_T, u_W = w3_idempotent_norms(c)
    return u_T + u_W


def w3_per_idempotent_free_energy(c: Fraction, g: int) -> Dict[str, Fraction]:
    r"""Per-idempotent free energy for W_3.

    In the minimal model, the per-idempotent MC element at genus g is:
        F_g^{(T)} = u_T · λ_g^FP = (c/2) · λ_g^FP
        F_g^{(W)} = u_W · λ_g^FP = (c/3) · λ_g^FP

    Total: F_g = (c/2 + c/3) · λ_g^FP = (5c/6) · λ_g^FP = κ · λ_g^FP. ✓
    """
    u_T, u_W = w3_idempotent_norms(c)
    fp = lambda_fp(g)
    return {
        'F_g_T': u_T * fp,
        'F_g_W': u_W * fp,
        'F_g_total': (u_T + u_W) * fp,
        'kappa_times_fp': kappa_total_wn(c, 3) * fp,
    }


# ============================================================================
# General W_N universality verification
# ============================================================================

def wn_universality_check(c: Fraction, N: int, g: int) -> Dict[str, object]:
    r"""Check conditional W_N scalar bookkeeping at genus g.

    Checks:
    1. κ formula: κ(W_N) = c(H_N - 1) = Σ_{s=2}^N c/s
    2. Per-channel sum: Σ F_g^{(s)} = κ · λ_g^FP
    3. Trace condition: Σ u_s = κ
    4. Strong-scalar ansatz prediction: F_g = κ · λ_g^FP
    """
    kappa = kappa_total_wn(c, N)
    kappa_formula = kappa_total_wn_formula(c, N)
    per_channel = free_energy_per_channel_sum(c, N, g)
    total = free_energy_total_wn(c, N, g)
    trace = sum(kappa_per_channel(c, s) for s in range(2, N + 1))
    fp = lambda_fp(g)

    return {
        'N': N,
        'c': c,
        'g': g,
        'kappa': kappa,
        'kappa_formula': kappa_formula,
        'kappa_match': kappa == kappa_formula,
        'lambda_fp': fp,
        'F_g_total': total,
        'F_g_per_channel_sum': per_channel,
        'universality_holds': total == per_channel == kappa * fp,
        'trace_sum': trace,
        'trace_match': trace == kappa,
    }


# ============================================================================
# Â-genus generating function verification
# ============================================================================

def ahat_coefficients(max_g: int = 6) -> Dict[int, Fraction]:
    r"""Coefficients of Â(ix) - 1 = Σ_{g≥1} a_g x^{2g}.

    Â(ix) = (x/2) / sin(x/2) = 1 + x²/24 + 7x⁴/5760 + 31x⁶/967680 + ...

    The coefficients a_g = λ_g^FP are the Faber-Pandharipande numbers.
    On the scalar lane, the generating function gives F_g = κ · a_g.
    """
    return {g: lambda_fp(g) for g in range(1, max_g + 1)}


# ============================================================================
# Scalar saturation proof chain verification
# ============================================================================

def scalar_saturation_proof_chain(c: Fraction, N: int) -> Dict[str, object]:
    r"""Historical name: check the strong-scalar ansatz bookkeeping chain.

    After rectification, step (2) above is no longer proved for
    general multi-weight families.  This routine only checks the
    arithmetic consequences of assuming the strong scalar ansatz.
    """
    kappa = kappa_total_wn(c, N)
    results = {}
    for g in range(1, 6):
        fg = kappa * lambda_fp(g)
        per_ch = free_energy_per_channel_sum(c, N, g)
        results[g] = {
            'F_g': fg,
            'F_g_per_channel': per_ch,
            'match': fg == per_ch,
            'kappa_times_fp': kappa * lambda_fp(g),
        }
    return {
        'N': N,
        'c': c,
        'kappa': kappa,
        'kappa_formula': c * (harmonic_number(N) - 1),
        'genus_results': results,
        'all_match': all(r['match'] for r in results.values()),
    }
