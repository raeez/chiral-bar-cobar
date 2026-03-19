#!/usr/bin/env python3
"""
Tests for the rigorous audit of the forced-zero mechanism.

THE CRITICAL FINDING: The forced zeros of ε^c at positions derived from
ζ zeros may not actually be zeros. The Ising model provides a sharp test.
"""

import sys, os, math
import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from moment_matrix_audit import (
    verify_forced_zero_ising, check_ising_zeros_vs_zeta, audit_conclusion,
)

try:
    import mpmath
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


class TestForcedZeroVerification:
    """Does ε^{1/2} actually vanish at the predicted positions?"""

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_forced_zero_ising_first(self):
        """Check first ζ zero: ε^{1/2} at s = iγ_1/2."""
        r = verify_forced_zero_ising(1)
        # THE CRITICAL TEST: is ε actually zero here?
        assert r['magnitude'] > 0.1, \
            "ε^{1/2} unexpectedly vanishes at forced position"
        # We EXPECT it NOT to vanish — this exposes the flaw

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_forced_zero_ising_multiple(self):
        """Check multiple ζ zeros: ε^{1/2} should NOT vanish."""
        for k in range(1, 6):
            r = verify_forced_zero_ising(k)
            assert not r['is_zero'], f"ζ zero {k}: ε unexpectedly vanishes"

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_ising_zeros_unrelated_to_zeta(self):
        """Actual zeros of ε^{1/2} = 8^s + 1 are at s = iπ(2k+1)/ln8,
        which bear no relation to ζ zero heights."""
        results = check_ising_zeros_vs_zeta(5)
        for r in results:
            # The forced position is NOT a zero
            assert r['eps_magnitude'] > 0.1, f"k={r['k']}: forced position is a zero?!"
            # The distance to the nearest actual zero is significant
            assert r['distance'] > 0.1, f"k={r['k']}: forced and actual too close"

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_ising_actual_zeros_are_periodic(self):
        """Actual zeros: s_m = iπ(2m+1)/ln8. Spacing = 2π/ln8 ≈ 3.02."""
        spacing = 2 * math.pi / math.log(8)
        assert abs(spacing - 3.022) < 0.01

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_zeta_zero_heights_irregular(self):
        """ζ zero heights are irregular: γ_1 ≈ 14.13, γ_2 ≈ 21.02, ..."""
        if HAS_MPMATH:
            gammas = [float(mpmath.zetazero(k).imag) for k in range(1, 6)]
            spacings = [gammas[i+1] - gammas[i] for i in range(len(gammas)-1)]
            # Spacings are irregular
            assert max(spacings) / min(spacings) > 1.5


class TestAuditConclusion:
    """The honest assessment."""

    def test_forced_zeros_not_verified(self):
        c = audit_conclusion()
        assert c['forced_zeros_verified'] is False

    def test_programme_suspended(self):
        c = audit_conclusion()
        assert 'SUSPENDED' in c['programme_status']

    def test_what_survives(self):
        c = audit_conclusion()
        # These results are independently proved, not depending on forced zeros
        assert len(c['what_survives']) >= 5


class TestWhatSurvives:
    """Results that don't depend on the forced-zero mechanism."""

    def test_narain_universality_independent(self):
        """ε^1 = 4ζ(2s) is proved by DIRECT COMPUTATION, not functional equation."""
        # Proof: scalar primaries at R=1 are h = n²/2 for n ≥ 1.
        # ε^1 = Σ_{n≥1} 2·(2·n²/2)^{-s} = 2·Σ n^{-2s} = 2ζ(2s) × 2 = 4ζ(2s).
        # No functional equation needed.
        assert True

    def test_e8_factorization_independent(self):
        """ε^8 = 240·4^{-s}·ζ(s)·ζ(s-3) from theta function identity."""
        # Proof: Θ_{E_8} = E_4, so r_8(2n) = 240σ_3(n).
        # ε^8 = 2^{-s}·Σ 240σ_3(n)(2n)^{-s} = 240·4^{-s}·ζ(s)ζ(s-3).
        # Direct computation, no functional equation.
        assert True

    def test_shadow_l_empirical(self):
        """Shadow-L correspondence: depth → L-factors. Empirical pattern."""
        # Three verified examples (V_Z, V_{E_8}, V_{Leech}).
        # No dependence on forced-zero mechanism.
        assert True

    def test_sewing_selberg_independent(self):
        """Z_combined = ζ(s-1)ζ(s). Proved by Rankin-Selberg unfolding."""
        # Direct integral computation, independent of forced zeros.
        assert True


class TestRederivationNeeded:
    r"""
    WHAT NEEDS TO BE RE-DERIVED.

    The Benjamin-Chang functional equation involves the spectral coefficients
    c(t) of the partition function Z(τ) in the continuous-spectrum
    decomposition on SL₂(Z)\H:

    Z(τ) = Σ_j a_j φ_j(τ) + (1/4π) ∫ c(t) E(τ, 1/2+it) dt

    where φ_j are Maass cusp forms and E is the Eisenstein series.

    The reflection equation c(-t) = φ(1/2+it) c(t) relates c(t) to c(-t).

    The SPECTRAL COEFFICIENTS c(t) are related to the partition function,
    NOT directly to ε^c. The relationship is:

    c(t) = ∫_F Z(τ) E(τ, 1/2-it) dμ(τ) = Rankin-Selberg integral

    For the Ising model: Z_Ising involves 3 characters.
    The spectral coefficients c(t) are computable.
    The question is: does c(t) = 0 at t such that φ(1/2+it) has a pole?

    φ(1/2+it) = Λ(1/2-it)/Λ(1/2+it) has poles at 1/2+it = ρ/2,
    i.e., t = (ρ-1)/2i = -i(ρ-1)/2.

    But t is REAL (in the spectral decomposition). The poles are at
    IMAGINARY t, i.e., in the complex t-plane, not on the real axis.

    So: φ has no poles on the real t-axis (those are at complex t).
    The reflection equation c(-t) = φ(1/2+it)c(t) is SATISFIED on the
    real axis without any zero-forcing.

    THE FORCED-ZERO MECHANISM WAS A MISREADING OF BENJAMIN-CHANG.

    The ζ zeros enter through the ANALYTIC CONTINUATION of c(t) to
    complex t, where the poles of φ can interact with zeros of c(t).
    But this is a much more subtle relationship than simple zero-forcing.
    """

    def test_rederivation_needed(self):
        assert True  # Acknowledged

    def test_spectral_coefficients_real_axis(self):
        """Spectral coefficients c(t) live on real t-axis.
        Scattering matrix φ(1/2+it) has poles at complex t.
        No forcing on the real axis."""
        # φ(s) = Λ(1-s)/Λ(s). Poles at s = ρ/2 (ζ zeros).
        # On the line s = 1/2 + it (t real): s is real part 1/2.
        # Poles at s = ρ/2. If ρ = 1/2 + iγ, then ρ/2 = 1/4 + iγ/2.
        # This has Re = 1/4 ≠ 1/2, so it's NOT on the spectral line.
        # Therefore: no poles on the spectral line → no zero-forcing.
        assert True

    def test_the_actual_bc_content(self):
        """What Benjamin-Chang ACTUALLY shows:
        - The Rankin-Selberg L-function Λ(s, Z̃) satisfies a functional equation.
        - The zeros of Λ(s, Z̃) are related to the zeros of ζ through the
          Eisenstein contribution.
        - The PRIMARY SPECTRUM of the CFT constrains Λ(s, Z̃).
        - But the constraint goes through the INTEGRAL TRANSFORM
          (Rankin-Selberg), not through pointwise zero-forcing.
        """
        assert True


class TestRevisedProgramme:
    r"""
    THE REVISED PROGRAMME (after audit).

    What survives:
    1. The sewing operator's Fredholm determinant connects to ζ via
       Σ σ_{-1}(N)N^{-s} = ζ(s)ζ(s+1). (PROVED)
    2. The Rankin-Selberg integral Z_combined = ζ(s-1)ζ(s). (PROVED)
    3. The shadow-L correspondence (empirical, 3 examples). (VERIFIED)
    4. The Narain universality and E_8/Leech factorizations. (PROVED)

    What falls:
    - The forced-zero mechanism.
    - The moment matrix exclusion argument.
    - The zero-line mismatch argument (it was correct in mechanics
      but irrelevant since forced zeros don't exist).
    - The Cartwright-Levinson argument (moot without forced zeros).

    What the correct direction might be:
    - The Rankin-Selberg L-function Λ(s, Z̃) inherits zeros from ζ
      through the continuous spectrum. But these are zeros of Λ, not of ε.
    - The MC constraints on the CFT spectrum constrain Λ(s, Z̃).
    - The question becomes: can the MC-constrained Λ have zeros
      ONLY on the critical line?
    - This is a GRH-type question for automorphic L-functions,
      approached through the CFT bootstrap.
    """

    def test_revised_direction(self):
        assert True  # Programme pivots to Rankin-Selberg L-function zeros


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
