"""Tests for thm:platonic-conductor (kappa-conductor universal formula).

Independent verification via the BRST ghost central-charge formula
matched against Friedan-Martinec-Shenker tabulated values.
"""
from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.independent_verification import independent_verification


# =========================================================================
# INDEPENDENT VERIFICATION (HZ3-11) — thm:platonic-conductor
# =========================================================================


class TestPlatonicConductorIV:
    """Independent verification of the platonic kappa-conductor formula.

    The theorem states K(A) = sum (-1)^{ε+1} · 2(6λ² - 6λ + 1) per
    quasi-free BRST generator, equivalent to -c_ghost(BRST(A)).

    Disjoint sources:
    - DERIVATION: ghost central charge formula from BRST quantisation +
      additivity over independent generators.
    - VERIFICATION: explicit ghost central charges at canonical (b, c)
      ghost systems (Friedan-Martinec-Shenker tabulated values).
    """

    @independent_verification(
        claim="thm:platonic-conductor",
        derived_from=[
            "K(A) := sum_α (-1)^{ε_α+1} · 2(6λ_α² - 6λ_α + 1) "
            "(platonic conductor formula)",
            "BRST quantisation ghost central charge "
            "c_ghost = (-1)^{ε+1} · 2(6λ² - 6λ + 1) per generator",
            "Additivity of K over quasi-free BRST resolution generators",
        ],
        verified_against=[
            "Friedan-Martinec-Shenker (FMS) tabulated values:",
            "(b, c) reparametrisation ghost at λ=2 fermionic: c_ghost = -26 "
            "(string theory critical dim from -c_ghost = +26 = K)",
            "(β, γ) superghost at λ=3/2 bosonic: c_ghost = +11",
            "(b, c) gauge-fixing ghost at λ=1 fermionic: c_ghost = -2",
            "All three FMS values from Polyakov-Friedan-Martinec-Shenker "
            "1985 string theory ghost analysis (independent of BRST "
            "categorical framework)",
        ],
        disjoint_rationale=(
            "The DERIVATION uses the BRST quantisation framework + "
            "additivity over generators in the quasi-free resolution. "
            "The VERIFICATION uses Friedan-Martinec-Shenker tabulated "
            "ghost central charges from the conformal field theory "
            "literature (1985 string theory analysis, independent of "
            "the BRST categorical framework used in the derivation). "
            "Three canonical (b,c) and (β,γ) systems at λ ∈ {2, 3/2, 1} "
            "give c_ghost ∈ {-26, +11, -2} matching both paths."
        ),
    )
    def test_FMS_ghost_central_charges_at_canonical_lambdas(self):
        """The KEY THEOREM: ghost central charge formula c_ghost =
        (-1)^{ε+1} · 2(6λ² - 6λ + 1) verified against Friedan-Martinec-
        Shenker (FMS) tabulated values at canonical (b, c)-system pairs.
        """
        # Reparametrisation (b, c) ghost system at λ = 2, fermionic ε=1.
        # K = (-1)^{1+1} · 2(6·4 - 12 + 1) = 1 · 2 · 13 = 26
        # c_ghost = -K = -26 ✓ (FMS string theory critical dim)
        lambda_repar = 2
        eps_fermi = 1
        K_repar = ((-1)**(eps_fermi + 1)
                   * 2 * (6 * lambda_repar**2 - 6 * lambda_repar + 1))
        c_ghost_repar = -K_repar
        assert c_ghost_repar == -26, (
            f"Reparam ghost (b,c) at λ=2: c_ghost = {c_ghost_repar}, "
            f"expected -26 (string theory critical dim)"
        )

        # Superghost (β, γ) at λ = 3/2, bosonic ε=0.
        # K = (-1)^{0+1} · 2(6·9/4 - 9 + 1) = -1 · 2 · (27/2 - 8) = -2·11/2 = -11
        # c_ghost = -K = +11 ✓
        lambda_super = Fraction(3, 2)
        eps_bose = 0
        K_super = ((-1)**(eps_bose + 1)
                   * 2 * (6 * lambda_super**2 - 6 * lambda_super + 1))
        c_ghost_super = -K_super
        assert c_ghost_super == 11, (
            f"Superghost (β,γ) at λ=3/2: c_ghost = {c_ghost_super}, "
            f"expected +11"
        )

        # Gauge-fixing (b, c) at λ = 1, fermionic ε=1.
        # K = (-1)^{1+1} · 2(6 - 6 + 1) = 1 · 2 · 1 = 2
        # c_ghost = -K = -2 ✓
        lambda_gauge = 1
        K_gauge = ((-1)**(eps_fermi + 1)
                   * 2 * (6 * lambda_gauge**2 - 6 * lambda_gauge + 1))
        c_ghost_gauge = -K_gauge
        assert c_ghost_gauge == -2, (
            f"Gauge ghost (b,c) at λ=1: c_ghost = {c_ghost_gauge}, "
            f"expected -2"
        )
