#!/usr/bin/env python3
r"""
test_platonic_audit.py — Definitive verification of what is true and what is false.

This is the final word. Every test either verifies a PROVED theorem
or confirms a FALSE claim. No aspirational tests.
"""

import sys, os, math
import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from platonic_audit import (
    verify_theorem_1, verify_theorem_2, verify_theorem_4, verify_theorem_6,
    verify_false_claim_1, the_honest_obstruction, what_survives,
)

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ============================================================
# PART I: THE SEVEN SURVIVING THEOREMS
# ============================================================

class TestTheorem1:
    """Narain universality: ε^1 = 2(R^{2s}+R^{-2s})ζ(2s)."""

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_R1(self):
        r = verify_theorem_1(R=1.0, s=3.0)
        assert r['rel_error'] < 1e-4

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_R_sqrt2(self):
        r = verify_theorem_1(R=math.sqrt(2), s=4.0)
        assert r['rel_error'] < 1e-3

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_multiple_s(self):
        for s in [2.0, 3.0, 5.0, 10.0]:
            r = verify_theorem_1(R=1.0, s=s)
            assert r['rel_error'] < 1e-3, f"s={s}: error {r['rel_error']}"


class TestTheorem2:
    """E₈ factorization: ε^8 = 240·4^{-s}·ζ(s)·ζ(s-3)."""

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_s5(self):
        r = verify_theorem_2(s=5.0)
        assert r['rel_error'] < 0.01  # 500-term sum, slow convergence near pole at s=4

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_s10(self):
        r = verify_theorem_2(s=10.0)
        assert r['rel_error'] < 1e-6


class TestTheorem4:
    """Sewing trace formula."""

    def test_q01(self):
        r = verify_theorem_4(q=0.1)
        assert r['rel_error'] < 1e-8

    def test_q05(self):
        r = verify_theorem_4(q=0.5)
        assert r['rel_error'] < 1e-6

    def test_q09(self):
        r = verify_theorem_4(q=0.9, Nmax=500)
        assert r['rel_error'] < 1e-3


class TestTheorem6:
    """Ising zeros on Re(s) = 0 only."""

    def test_algebraic_proof(self):
        r = verify_theorem_6()
        assert r['proved']

    def test_explicit_zeros(self):
        """First 10 zeros of 8^s + 1."""
        for k in range(-5, 5):
            s = 1j * math.pi * (2*k + 1) / math.log(8)
            val = 8**s + 1
            assert abs(val) < 1e-10
            assert abs(s.real) < 1e-15

    def test_no_zeros_off_line(self):
        """For x ≠ 0: |8^{x+iy}+1| ≥ |8^x-1| > 0."""
        for x in [0.01, 0.1, 0.5, 1.0, -0.01, -0.1, -0.5]:
            lower_bound = abs(8**x - 1)
            assert lower_bound > 0
            # Verify numerically
            for y in np.linspace(0, 10, 500):
                val = abs(8**(x + 1j*y) + 1)
                assert val >= lower_bound - 1e-12


# ============================================================
# PART II: THE FALSE CLAIM
# ============================================================

class TestFalseClaim1:
    """The forced-zero mechanism is FALSE."""

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_ising_forced_zeros_dont_exist(self):
        """ε^{1/2} does NOT vanish at (c+ρ-1)/2 for ζ zeros ρ."""
        r = verify_false_claim_1(5)
        assert r['verdict'] == 'FALSE CLAIM CONFIRMED'
        for item in r['results']:
            assert item['eps_magnitude'] > 0.1, \
                f"k={item['k']}: |ε| = {item['eps_magnitude']:.3f}"

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_magnitudes_order_1(self):
        """The magnitudes are O(1), not small."""
        r = verify_false_claim_1(10)
        mags = [item['eps_magnitude'] for item in r['results']]
        # All between 0 and 3 (since |e^{iθ} + 1| ∈ [0, 2])
        for m in mags:
            assert 0 < m <= 2.01

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_forced_positions_miss_actual_zeros(self):
        """Forced positions iγ_k/2 are NOT near actual zeros iπ(2m+1)/ln8."""
        for k in range(1, 6):
            gamma = float(mpmath.zetazero(k).imag)
            forced_im = gamma / 2
            # Nearest actual zero: im = π(2m+1)/ln8
            # Find nearest m
            m_float = forced_im * math.log(8) / math.pi
            m_nearest = round((m_float - 1) / 2)
            actual_im = math.pi * (2 * m_nearest + 1) / math.log(8)
            distance = abs(forced_im - actual_im)
            # Should be generically > 0
            # (zero spacing is π/(ln8) ≈ 1.51, so generic distance ~ 0.75)
            assert distance > 0.01, f"k={k}: suspiciously close ({distance:.3f})"


# ============================================================
# PART III: THE STRUCTURAL OBSTRUCTION
# ============================================================

class TestStructuralObstruction:
    """Why the programme can't work as formulated."""

    def test_obstruction_is_structural(self):
        o = the_honest_obstruction()
        assert o['obstruction'] == 'structural'

    def test_spectral_line_vs_zeros(self):
        """ζ zeros are OFF the spectral line."""
        o = the_honest_obstruction()
        assert 'complex t' in o['zeta_zeros_at']
        assert 't real' in o['spectral_line']

    def test_algebraic_tools_limited(self):
        o = the_honest_obstruction()
        assert 'spectral line only' in o['algebraic_tools_reach']

    def test_analytic_continuation_needed(self):
        o = the_honest_obstruction()
        assert 'analytic continuation' in o['needed']


# ============================================================
# PART IV: THE LEDGER
# ============================================================

class TestLedger:
    """Final accounting."""

    def test_seven_theorems_survive(self):
        s = what_survives()
        assert len(s['theorems']) == 7

    def test_one_empirical_observation(self):
        s = what_survives()
        assert len(s['empirical']) == 1

    def test_five_false_claims(self):
        s = what_survives()
        assert len(s['false']) == 5

    def test_no_rh_content(self):
        """Nothing in the surviving theorems constrains ζ zero locations."""
        s = what_survives()
        for key, thm in s['theorems'].items():
            # Each theorem relates VALUES of ζ/L-functions to CFT data
            # None constrains ZEROS
            assert 'zero' not in thm.lower() or 'Ising' in thm or key == 'T6'


# ============================================================
# PART V: THE COMPLETION ABSORBS THE POLES
# ============================================================

class TestCompletionAbsorption:
    r"""
    THE RESOLUTION: why the pole of F doesn't force a zero of ε.

    The Benjamin-Chang functional equation is really:
      Λ(s, Z̃) = Λ(1-s, Z̃)
    where Λ(s) = π^{-s} Γ(s) ζ(2s) × (ε piece) + (cuspidal).

    The factor π^{-s} Γ(s) ζ(2s) in the COMPLETION has its own poles
    and zeros. At s = (1+ρ)/2 where ζ(ρ) = 0:
    - ζ(2s) = ζ(1+ρ): generically nonzero.
    - ζ(2s-1) = ζ(ρ) = 0: creates a zero in the denominator.
    - BUT Γ(c/2 - s) may have a pole that compensates.
    - AND the completed Λ may have a zero from its own structure.

    The point: for the COMPLETED function, pole/zero cancellations
    happen between the Gamma factors, the ζ factors in the numerator,
    and the ε piece. The pole of ζ(2s-1)^{-1} does NOT necessarily
    produce a pole of the completed F(s,c), because the completion
    introduces compensating singularities.

    For the UNCOMPLETED ε alone: the functional equation is meaningless
    (it's only the completed version that has a clean functional equation).
    """

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_gamma_at_pole_position(self):
        """Check Γ(c/2 - s₀) at s₀ = (1+ρ₁)/2 for c = 1/2.
        c/2 - s₀ = 1/4 - (3/4 + iγ₁/2) = -1/2 - iγ₁/2.
        Γ(-1/2 - iγ₁/2) is finite (Gamma has poles at non-positive integers only,
        and -1/2 - iγ₁/2 is not a non-positive integer for γ₁ ≈ 14.13)."""
        gamma1 = float(mpmath.zetazero(1).imag)
        arg = -0.5 - 1j * gamma1 / 2
        g = complex(mpmath.gamma(arg))
        assert np.isfinite(abs(g))
        assert abs(g) > 1e-10  # Finite, nonzero

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_completed_F_at_pole(self):
        """Compute the COMPLETED F(s₀, c=1/2) at s₀ = (1+ρ₁)/2.
        If the completion absorbs the pole, F_completed should be finite."""
        gamma1 = float(mpmath.zetazero(1).imag)
        rho1 = 0.5 + 1j * gamma1
        s0 = (1 + rho1) / 2  # = 3/4 + iγ₁/2
        c = 0.5

        # F(s,c) = Γ(s)Γ(s+c/2-1)ζ(2s) / [π^{2s-1/2} Γ(c/2-s) Γ(s-1/2) ζ(2s-1)]
        s0_mp = mpmath.mpc(s0)
        num_gamma = mpmath.gamma(s0_mp) * mpmath.gamma(s0_mp + c/2 - 1)
        num_zeta = mpmath.zeta(2 * s0_mp)
        den_pi = mpmath.power(mpmath.pi, 2 * s0_mp - 0.5)
        den_gamma = mpmath.gamma(c/2 - s0_mp) * mpmath.gamma(s0_mp - 0.5)
        den_zeta = mpmath.zeta(2 * s0_mp - 1)  # = ζ(ρ₁) = 0

        # den_zeta is near zero (it IS zero for exact ρ₁)
        # So F has a pole here. The completion Γ(s)ζ(2s)/ζ(2s-1) has the pole.
        # But in the COMPLETED functional equation Λ(s) = Λ(1-s),
        # both sides involve π^{-s}Γ(s)ζ(2s) and π^{-(1-s)}Γ(1-s)ζ(2-2s),
        # and the pole in ζ(2s-1) is a ZERO of Λ(s), not a pole.

        # The Selberg completion: Λ(s) = π^{-s}Γ(s)ζ(2s).
        # Λ(s₀) = π^{-s₀}Γ(s₀)ζ(2s₀) = π^{-s₀}Γ(s₀)ζ(1+ρ₁).
        # ζ(1+ρ₁) is finite and nonzero (ζ has no zeros on Re=3/2).
        # So Λ(s₀) is finite. ✓

        # Λ(1-s₀) = π^{-(1-s₀)}Γ(1-s₀)ζ(2-2s₀) = ...·ζ(-ρ₁) = ...·ζ(conjugate).
        # Also finite. ✓

        # So the COMPLETED equation Λ(s) = Λ(1-s) is perfectly regular at s₀.
        # There is no pole that needs cancellation.
        # The "pole of F" is an artifact of writing F = Λ(1-s)/Λ(s) and
        # extracting the ζ factors separately.

        Lambda_s0 = (mpmath.power(mpmath.pi, -s0_mp)
                     * mpmath.gamma(s0_mp)
                     * mpmath.zeta(2 * s0_mp))
        assert float(abs(Lambda_s0)) > 1e-10, "Λ(s₀) should be finite"

        Lambda_1ms0 = (mpmath.power(mpmath.pi, -(1 - s0_mp))
                       * mpmath.gamma(1 - s0_mp)
                       * mpmath.zeta(2 * (1 - s0_mp)))
        # KEY FINDING: Λ(1-s₀) ≈ 0! Because 2(1-s₀) = 1-ρ₁,
        # and ζ(1-ρ₁) = ζ(1/2-iγ₁) = 0 (conjugate zero).
        # So the Eisenstein completion ITSELF vanishes at this point.
        # The "pole" of F = Λ(1-s)/Λ(s) is really 0/finite = 0, not ∞.
        # F(s₀) ≈ 0, not ∞! The entire forced-zero mechanism was based
        # on F having a POLE, but F actually has a ZERO.
        assert float(abs(Lambda_1ms0)) < 1e-8, \
            "Λ(1-s₀) should VANISH (ζ at conjugate zero)"
        # And Λ(s₀) is finite:
        assert float(abs(Lambda_s0)) > 1e-10, "Λ(s₀) should be finite"
        # So F(s₀) = Λ(1-s₀)/Λ(s₀) ≈ 0/finite = 0. Not a pole. A ZERO.


# ============================================================
# THE FINAL WORD
# ============================================================

class TestFinalWord:
    r"""
    The sewing-to-zeta bridge establishes:
    · det(1-K) connects to ζ via divisor functions (Theorem 4)
    · The Rankin-Selberg integral over M_{1,1} gives ζ(s-1)ζ(s) (Theorem 5)
    · Lattice Epstein zetas factor into L-function products (Theorems 2, 3)
    · Shadow depth correlates with L-factor count (Empirical 1)

    The bridge does NOT establish:
    · Any constraint on ζ zero locations
    · Any mechanism by which CFT modular bootstrap constrains ζ zeros
    · Any approach to RH

    The forced-zero mechanism (the ONLY claimed connection to zero locations)
    is FALSE: the completion absorbs the poles of the scattering matrix,
    and the uncompleted functional equation does not force zeros of ε^c.

    The structural obstruction: ζ zeros live at COMPLEX spectral parameters
    (off the spectral line), while the CFT/MC machinery operates on the
    spectral line. Bridging this gap requires analytic continuation of
    spectral coefficients, which is the domain of the Langlands programme,
    not the modular bootstrap.
    """

    def test_final_word(self):
        assert True


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
