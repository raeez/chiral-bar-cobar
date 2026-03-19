#!/usr/bin/env python3
r"""
moment_matrix_audit.py — Rigorous audit of the moment matrix argument.

THE CLAIMED ARGUMENT:
  The functional equation forces ε^c((c+ρ-1)/2) = 0 for each ζ zero ρ.
  For ρ_k = σ + iγ_k: Σ_j b_j e^{-iγ_k ω_j} = 0 for all k.
  Moment matrix has full rank → b = 0 → contradiction.

THE CRITICAL QUESTION:
  Is the functional equation ε^c_{c/2-s} = F(s,c)·ε^c_{c/2+s-1}
  actually TRUE for minimal model CFTs? And does the pole of F
  at s = (1+ρ)/2 actually force a zero of ε^c?

  The functional equation comes from the Rankin-Selberg transform of
  the partition function Z(τ). But for MINIMAL MODELS (c < 1, rational CFTs),
  the partition function Z(τ) is a FINITE sum of modular-covariant terms.
  The Rankin-Selberg integral may not produce the simple functional equation
  ε^c_{c/2-s} = F(s,c)·ε^c_{c/2+s-1} that we assumed.

  Let me audit this carefully.

AUDIT 1: Does the Rankin-Selberg transform of a minimal model partition
  function Z(τ) produce a functional equation for ε^c?

  Z(τ) = Σ |χ_i(τ)|² (diagonal modular invariant)
  where χ_i are Virasoro characters.

  The Rankin-Selberg integral:
  I(s) = ∫_{SL₂\H} |Z̃(τ)|² y^s dμ(τ)

  Wait — the constrained Epstein zeta is NOT the Rankin-Selberg integral.
  Let me re-derive what ε^c actually is and where its functional equation
  comes from.

AUDIT 2: What IS ε^c?

  In Benjamin-Chang (2208.02259), the constrained Epstein zeta is:
  ε^c_s = Σ_{scalar primaries (h,h)} (2h)^{-s}

  This is the Mellin transform of the "scalar primary counting function":
  N^c(x) = #{scalar primaries with h ≤ x}

  The functional equation of ε^c comes from the modular properties of
  the partition function Z(τ) = Σ_{h,h̄} d(h,h̄) q^{h-c/24} q̄^{h̄-c/24}.

  For SCALAR primaries (h = h̄): contribute to the Rankin-Selberg integral
  ∫_{F} Z(τ) E_s(τ) dμ(τ) as the CONSTANT TERM in the Fourier expansion
  of Z(τ) with respect to Re(τ).

  The key step: the Rankin-Selberg unfolding gives
  ∫_F Z(τ) E_s(τ) dμ = Σ_{scalar} d(h,h) ∫_0^∞ y^{s+h-c/24} dy/y² + ...

  But this integral DIVERGES unless properly regularized.
  The regularized version involves the completed L-function Λ(s, Z̃).

  FOR MINIMAL MODELS: Z(τ) is a FINITE SUM of products of Virasoro characters.
  The characters are q-series with specific modular properties.
  The Rankin-Selberg integral IS well-defined (after regularization)
  and DOES satisfy a functional equation.

  But the functional equation relates ε^c_s to ε^c_{c-1-s} (NOT to itself),
  with the factor F(s,c) involving the Eisenstein scattering matrix.

  THIS IS THE SAME FUNCTIONAL EQUATION WE USED. ✓

AUDIT 3: Does the pole of F force a zero of ε^c?

  F(s,c) = Λ(s,c) / Λ(c-s,c) (schematically) where Λ involves
  Gamma functions and ζ(2s)/ζ(2s-1).

  At s = s_0 where ζ(2s_0 - 1) = 0: F has a simple pole.
  The equation ε^c_{c/2-s} = F(s,c)·ε^c_{c/2+s-1} at s = s_0 gives:

  [finite LHS] = [pole] × ε^c_{c/2+s_0-1}

  For the RHS to be finite: ε^c_{c/2+s_0-1} must have a ZERO of the
  same order as the pole of F.

  BUT WAIT: maybe the LHS is ALSO infinite (pole of ε^c).
  For minimal models: ε^c is a finite sum of (2h)^{-s}, which is ENTIRE.
  So the LHS is always finite. The RHS must also be finite.
  Therefore ε^c at the RHS argument must vanish. ✓

  For LATTICE theories: ε^c = (product of L-functions), which has poles.
  Need to check whether ε^c has a pole at the LHS argument that
  cancels the pole of F on the RHS.

  For c = 1: ε = 4ζ(2s). ε has a pole at s = 1/2 (from ζ(1)).
  The LHS argument is c/2 - s = 1/2 - s. At s = s_0 = (1+ρ)/2:
  LHS argument = 1/2 - (1+ρ)/2 = -ρ/2.
  If ρ = 1/2 + iγ: LHS arg = -1/4 - iγ/2. ε(-1/4-iγ/2) = 4ζ(-1/2-iγ).
  This is finite (ζ has no pole at -1/2-iγ for γ ≠ 0).
  RHS argument: c/2 + s_0 - 1 = 1/2 + (1+ρ)/2 - 1 = ρ/2.
  ε(ρ/2) = 4ζ(ρ). IF ρ is a ζ zero, then ε(ρ/2) = 0. ✓

  So for c = 1: the zero-forcing works ONLY for the TRUE ζ zeros.
  The question is: does it ALSO force zeros for hypothetical ρ with σ ≠ 1/2?

  At s = s_0 where 2s_0 - 1 is a hypothetical zero of ζ:
  F has a pole (from ζ(2s-1) = 0 in denominator).
  ε at RHS = 4ζ(ρ) where ρ = 2s_0 - 1.
  If ρ is a hypothetical zero: ε(ρ/2) = 4ζ(ρ) = 0. Trivially. ✓

  Wait — this is CIRCULAR for c = 1! The zero of ε at ρ/2 IS the zero
  of ζ at ρ. The argument reduces to: ζ has zeros where it has zeros.

  THE CIRCULARITY FOR LATTICE THEORIES:
  When ε^c = f(ζ), the forced zeros of ε^c are EQUIVALENT to ζ zeros.
  No new information.

  FOR MINIMAL MODELS: ε^c is NOT a function of ζ. It's a finite polynomial.
  The forced zeros give genuine constraints. The moment matrix works.

  FOR VIRASORO AT c > 1: ε^c is determined by the CFT, NOT by ζ.
  The forced zeros are genuine constraints (not circular).
  BUT ε^c is infinite-dimensional, so the moment matrix needs extension.

  CONCLUSION: The argument is VALID for minimal models (finite, non-circular).
  For lattice theories: the zero-line mismatch works WITHOUT the moment matrix.
  For Virasoro at c > 1: non-circular but needs the infinite-dim extension.
"""

import numpy as np
import math

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


def verify_forced_zero_ising(gamma_index=1):
    r"""
    AUDIT: Verify the forced zero mechanism for the Ising model.

    ε^{1/2}_s = 8^s + 1.

    The functional equation:
    ε^{1/2}_{1/4 - s} = F(s, 1/2) · ε^{1/2}_{s - 1/4}

    (using c/2 = 1/4.)

    At s = s_0 = (1+ρ)/2 where ρ is a ζ zero at 1/2 + iγ:
    s_0 = 3/4 + iγ/2.

    RHS argument: s_0 - 1/4 = 1/2 + iγ/2.
    ε(1/2 + iγ/2) = 8^{1/2+iγ/2} + 1 = 2√2 · e^{iγ ln8/2} + 1.

    For this to vanish: 2√2 · e^{iθ} = -1 where θ = γ ln(8)/2.
    |2√2| ≈ 2.83 ≠ 1, so this CANNOT vanish.

    WAIT. This means the forced zero mechanism DOESN'T WORK for Ising?!

    Let me re-derive more carefully.

    The functional equation from Benjamin-Chang is for the FULL partition
    function Z(τ), not just the scalar primaries. The Rankin-Selberg
    integral involves:

    Λ(s, Z̃) = ∫_{SL₂\H} Z̃(τ) E_s(τ) dμ(τ)

    where Z̃ = Z - (constant term). The functional equation is:
    Λ(s, Z̃) = Λ(1-s, Z̃)

    This relates the Rankin-Selberg L-function to itself under s → 1-s.
    The poles come from the Eisenstein series E_s, which has poles at
    s = 0 and s = 1.

    The RESIDUES at these poles give information about Z, but the
    functional equation Λ(s) = Λ(1-s) does NOT directly say anything
    about ε^c having zeros at ζ zero positions.

    THE ACTUAL MECHANISM (BC 2208.02259):
    The spectral decomposition of Z on SL₂\H involves the Eisenstein
    scattering matrix φ(s). The SPECTRAL COEFFICIENTS c(t) of Z
    (in the continuous spectrum) satisfy:
    c(-t) = φ(1/2 + it) · c(t)

    This is a REFLECTION EQUATION for the spectral coefficients, NOT
    a forcing of zeros. The spectral coefficients c(t) are GIVEN by
    the CFT data and satisfy this equation automatically.

    CRITICAL REALIZATION: The "forced zeros" I postulated are NOT
    what Benjamin-Chang says. Let me re-read the actual mechanism.
    """
    if not HAS_MPMATH:
        return {'error': 'mpmath required'}

    gamma = float(mpmath.zetazero(gamma_index).imag)

    # Check if ε^{1/2} actually vanishes at the "forced" position
    s_forced = (0.5 - 1 + 0.5 + 1j * gamma) / 2  # (c-1+ρ)/2 = (ρ-1/2)/2
    s_forced = (0.5 + 1j * gamma - 0.5) / 2  # = iγ/2
    eps_at_forced = 8 ** s_forced + 1

    # Also check at (c+ρ-1)/2 = (1/2 + 1/2 + iγ - 1)/2 = iγ/2
    # Same position.

    return {
        's_forced': complex(s_forced),
        'eps_at_forced': complex(eps_at_forced),
        'magnitude': abs(eps_at_forced),
        'is_zero': abs(eps_at_forced) < 1e-8,
        'FINDING': 'ε^{1/2} does NOT vanish at the forced position!'
        if abs(eps_at_forced) > 0.1 else 'vanishes',
    }


def audit_functional_equation_derivation():
    r"""
    AUDIT: Trace the functional equation from Benjamin-Chang.

    The paper 2208.02259 considers:
    Z_c(s) = ∫_{SL₂\H} Φ_c(τ) · E(τ,s) · y^{c/2} dμ(τ)

    where Φ_c encodes the CFT data. The functional equation of E(τ,s)
    (Eisenstein series) gives:

    Z_c(s) = φ(s) · Z_c(1-s)   (*)

    where φ(s) = Λ(1-s)/Λ(s) is the scattering matrix.

    Now, Z_c(s) is related to ε^c by:
    Z_c(s) = (normalization) · ε^c_{s+α} for some shift α.

    The key: (*) is a relation between Z_c(s) and Z_c(1-s),
    i.e., between ε^c at two different arguments.

    φ(s) has POLES at s = ρ/2 (half the ζ zeros, from Λ(s) in denominator).
    At such a pole: Z_c(1-s) must vanish (to keep Z_c(s) finite on LHS).

    So: Z_c(1 - ρ/2) = 0 for each ζ zero ρ.

    For ρ = 1/2 + iγ: Z_c(1 - 1/4 - iγ/2) = Z_c(3/4 - iγ/2) = 0.
    For ρ = σ + iγ:   Z_c(1 - σ/2 - iγ/2) = 0.

    Now: Z_c(s) = (normalization) · Σ d(h) (4πh)^{-s} · (something).

    The exact relation between Z_c and ε^c depends on the normalization
    and the precise definition. Let me check for c=1.

    For c=1 (free boson at R=1):
    Z_1(τ) = Σ_{n,w} q^{n²/2} q̄^{w²/2} (ignoring oscillators)
    The scalar sector (n=w): Z_scalar(τ) = Σ_n |q|^{n²} = Σ_n y^{-n²}·e^{2πin²x}
    Wait, this is getting complicated. Let me just CHECK numerically
    whether ε^{1/2} vanishes at the predicted positions.
    """
    return {
        'mechanism': 'Z_c(1-ρ/2) = 0 from φ(s) pole cancellation',
        'key_relation': 'Z_c relates to ε^c via Rankin-Selberg normalization',
        'needs_verification': 'exact shift between Z_c and ε^c arguments',
    }


def check_ising_zeros_vs_zeta(n_zeros=5):
    r"""
    DIRECT CHECK: Does ε^{1/2}_s = 8^s + 1 have zeros related to ζ zeros?

    ε = 0 iff 8^s = -1 iff s = iπ(2k+1)/ln(8).

    ζ zeros at ρ_k = 1/2 + iγ_k where γ_1 ≈ 14.13, γ_2 ≈ 21.02, ...

    The predicted forced zeros are at s = (c+ρ-1)/2 = (-1/2 + ρ)/2 = ρ/2 - 1/4.
    For ρ_1: s ≈ -1/4 + i·7.07. Re(s) = -1/4, Im(s) ≈ 7.07.

    The actual zeros of ε have Re(s) = 0 and Im = π(2k+1)/ln(8) ≈ 1.51(2k+1).

    The NEAREST actual zero to the first "forced" zero:
    Forced: s ≈ -0.25 + 7.07i.
    Nearest actual: s = i·π·5/ln(8) ≈ i·7.55 (k=2). Off by Re=-0.25 and Im≈0.48.

    THEY DON'T MATCH. The "forced" zeros are NOT actual zeros of ε^{1/2}.

    THIS MEANS: either the forced-zero derivation is wrong, or the
    exact shift between Z_c and ε^c is different from what I assumed.
    """
    if not HAS_MPMATH:
        return {'error': 'mpmath required'}

    results = []
    for k in range(1, n_zeros + 1):
        gamma = float(mpmath.zetazero(k).imag)
        rho = 0.5 + 1j * gamma

        # "Forced" zero position (my derivation)
        s_forced = (0.5 + rho - 1) / 2  # = (rho - 1/2)/2 = iγ/2
        eps_forced = 8 ** s_forced + 1

        # Nearest actual zero of 8^s + 1
        # s_actual = i·π(2m+1)/ln8 for integer m
        target_im = s_forced.imag
        m_nearest = round(target_im * math.log(8) / math.pi - 0.5)
        if m_nearest < 0:
            m_nearest = 0
        # Try m and m±1
        candidates = []
        for m in [m_nearest - 1, m_nearest, m_nearest + 1]:
            s_actual = 1j * math.pi * (2 * m + 1) / math.log(8)
            dist = abs(s_forced - s_actual)
            candidates.append((s_actual, dist, m))
        best = min(candidates, key=lambda x: x[1])

        results.append({
            'k': k,
            'gamma': gamma,
            's_forced': complex(s_forced),
            'eps_at_forced': complex(eps_forced),
            'eps_magnitude': abs(eps_forced),
            'is_zero': abs(eps_forced) < 0.01,
            'nearest_actual_zero': complex(best[0]),
            'distance': best[1],
        })

    return results


def audit_conclusion():
    r"""
    THE AUDIT CONCLUSION.

    FINDING 1: The "forced zeros" of ε^c at s = (c+ρ-1)/2 are based on
    the functional equation ε^c_{c/2-s} = F(s,c)·ε^c_{c/2+s-1}.
    This functional equation involves the PRECISE normalization relating
    the Rankin-Selberg integral Z_c(s) to the constrained Epstein zeta ε^c_s.

    FINDING 2: For the Ising model (c=1/2), the "forced" zeros at
    s = iγ/2 are NOT actual zeros of ε^{1/2} = 8^s + 1.
    The actual zeros are at s = iπ(2k+1)/ln(8), which are unrelated
    to ζ zeros.

    FINDING 3: This means EITHER:
    (a) The forced-zero derivation has an error in the argument shifts, OR
    (b) The functional equation F(s,c) is not what I assumed, OR
    (c) The pole of F does NOT force a zero of ε^c (because both sides
        of the equation vanish/diverge in a more subtle way).

    FINDING 4: The moment matrix argument, the zero-line mismatch, and
    the Cartwright-Levinson argument ALL depend on the forced-zero mechanism.
    If the forced zeros don't exist, the entire programme collapses.

    STATUS: THE FORCED-ZERO MECHANISM NEEDS RIGOROUS RE-DERIVATION
    FROM THE ACTUAL BENJAMIN-CHANG FUNCTIONAL EQUATION.

    The issue is likely in the precise identification of ε^c_s with the
    Rankin-Selberg spectral data. The BC paper works with a DIFFERENT
    object (the spectral coefficients c(t) in the continuous spectrum),
    not directly with ε^c.
    """
    return {
        'forced_zeros_verified': False,
        'ising_check': 'FAILS — forced positions are not zeros of ε',
        'root_cause': 'Possible mismatch between Rankin-Selberg Z_c and ε^c',
        'programme_status': 'SUSPENDED pending re-derivation',
        'what_survives': [
            'Narain universality (P1): ε^1 = 4ζ(2s). Independent proof.',
            'E_8 factorization: ε^8 = 240·4^{-s}·ζ(s)·ζ(s-3). Direct computation.',
            'Leech factorization: ε^{24} = (65520/691)·4^{-s}·[ζζ - L]. Direct.',
            'Shadow-L correspondence: depth → L-factor count. Empirical.',
            'Sewing-Selberg formula: Z_combined = ζ(s-1)ζ(s). Proved.',
        ],
    }
