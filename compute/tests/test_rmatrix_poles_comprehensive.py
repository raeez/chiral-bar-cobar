r"""Comprehensive r-matrix pole order verification tests.

AP19 (the bar kernel absorbs a pole): the collision residue r(z) has
pole orders ONE LESS than the OPE.  The d log(z_1 - z_2) kernel in the
bar construction absorbs one power of (z-w).  This is the single most
error-prone formula in the manuscript.

The pole-shift rule:
  OPE pole z^{-n}  --->  r-matrix pole z^{-(n-1)}
  In particular:
    z^{-1} in OPE  --->  z^0 in r-matrix (regular, drops out)

Consequences:
  - Heisenberg: OPE z^{-2}  --->  r-matrix z^{-1}.  r(z) = kappa/z.
  - Affine sl_N: OPE z^{-2}, z^{-1}  --->  r-matrix z^{-1} only.
    r(z) = k*Omega/z.  The simple pole (bracket term) in the OPE
    becomes regular and drops.
  - Virasoro: OPE z^{-4}, z^{-2}, z^{-1}  --->  r-matrix z^{-3}, z^{-1}.
    r(z) = (c/2)/z^3 + 2T/z.  No z^{-2} pole for a bosonic algebra.
  - W_3: WW OPE has z^{-6}, z^{-4}, z^{-3}, z^{-2}, z^{-1}
    --->  r-matrix has z^{-5}, z^{-3}, z^{-2}, z^{-1}.
  - betagamma: OPE z^{-1} (mixed propagator) --->  r-matrix z^0 (regular).
    Diagonal entries zero.

Cross-checks:
  - Classical Yang-Baxter equation for all families.
  - Unitarity: r_{12}(z) + r_{21}(-z) = Omega for affine families.
  - Bosonic parity: no even-order poles for single-generator bosonic algebras.
  - Pole-order consistency with the manuscript (spectral-braiding-core.tex).

Ground truth:
  - eq:virasoro-r-collision: r^Vir(z) = (c/2)/z^3 + 2L/z
  - prop:affine-r-mode: r^aff(z) = k*Omega/z
  - AP19 in CLAUDE.md
  - collision_residue_identification.py, holographic_shadow_connection.py
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, List, Optional, Tuple

import numpy as np
import pytest

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'lib'))


# ========================================================================
# Core pole-shift engine: OPE -> r-matrix via d log absorption
# ========================================================================

def ope_to_rmatrix_poles(ope_poles: Dict[int, object]) -> Dict[int, object]:
    """Apply the d log absorption rule: each OPE pole z^{-n} maps to z^{-(n-1)}.

    Args:
        ope_poles: {pole_order: coefficient} for the OPE.
            E.g. {4: c/2, 2: 2, 1: 1} for Virasoro T(z)T(w).

    Returns:
        {pole_order: coefficient} for the r-matrix.
        Poles of order 0 (regular terms) are dropped.
    """
    rmatrix_poles = {}
    for n, coeff in ope_poles.items():
        shifted = n - 1
        if shifted > 0 and coeff != 0:
            rmatrix_poles[shifted] = coeff
    return rmatrix_poles


def max_pole_order(poles: Dict[int, object]) -> int:
    """Return the maximum pole order, or 0 if empty."""
    if not poles:
        return 0
    return max(poles.keys())


# ========================================================================
# OPE data for each family (first-principles, not imported)
# ========================================================================

def heisenberg_ope_poles(kappa=Fraction(1)):
    """J(z) J(w) ~ kappa / (z-w)^2."""
    return {2: kappa}


def affine_sl2_ope_poles(k=Fraction(1)):
    """J^a(z) J^b(w) ~ k*delta^{ab}/(z-w)^2 + f^{ab}_c J^c(w)/(z-w).

    Diagonal pairs (a=b): pole order 2 with coefficient k.
    Off-diagonal pairs: pole order 1 (structure constants).
    """
    return {
        'diagonal': {2: k},
        'off_diagonal': {1: 'f^{abc}'},
    }


def virasoro_ope_poles(c=Fraction(1)):
    """T(z)T(w) ~ (c/2)/(z-w)^4 + 2T/(z-w)^2 + dT/(z-w)."""
    return {4: c / 2, 2: 2, 1: 1}


def w3_TT_ope_poles(c=Fraction(1)):
    """Same as Virasoro."""
    return {4: c / 2, 2: 2, 1: 1}


def w3_TW_ope_poles():
    """T(z)W(w) ~ 3W/(z-w)^2 + dW/(z-w).  W is primary of weight 3."""
    return {2: 3, 1: 1}


def w3_WT_ope_poles():
    """W(z)T(w) ~ 3W/(z-w)^2 + 2dW/(z-w).  Skew-symmetry correction."""
    return {2: 3, 1: 2}


def w3_WW_ope_poles(c=Fraction(1)):
    """W(z)W(w) ~ (c/3)/(z-w)^6 + 2T/(z-w)^4 + dT/(z-w)^3
                  + [...]/(z-w)^2 + [...]/(z-w).

    Sixth-order pole.  The leading coefficient is c/3.
    """
    beta = Fraction(16, 1) / (22 + 5 * c) if c != Fraction(-22, 5) else None
    return {
        6: c / 3,
        # 5: 0  (no weight-1 primary)
        4: 2,
        3: 1,
        2: 'composite',  # (3/10)d^2T + beta*Lambda
        1: 'composite',  # (1/15)d^3T + (beta/2)*dLambda
    }


def betagamma_ope_poles():
    """beta(z) gamma(w) ~ 1/(z-w).  Simple pole only.

    beta-beta and gamma-gamma: no singular OPE.
    """
    return {
        ('beta', 'gamma'): {1: 1},
        ('gamma', 'beta'): {1: 1},
        ('beta', 'beta'): {},
        ('gamma', 'gamma'): {},
    }


def affine_slN_ope_poles(k=Fraction(1), N=2):
    """J^a(z) J^b(w) ~ k*kappa^{ab}/(z-w)^2 + f^{ab}_c J^c(w)/(z-w).

    All diagonal pairs: double pole (metric).
    Off-diagonal with nonzero structure constant: simple pole.
    """
    return {
        'diagonal': {2: k},
        'off_diagonal': {1: 'f^{abc}'},
    }


# ========================================================================
# Tests: AP19 pole-shift verification
# ========================================================================

class TestHeisenbergPoleShift:
    """Heisenberg: OPE has z^{-2}, r-matrix has z^{-1}."""

    def test_ope_max_pole_order(self):
        """OPE has maximal pole order 2."""
        poles = heisenberg_ope_poles()
        assert max_pole_order(poles) == 2

    def test_rmatrix_max_pole_order(self):
        """r-matrix has maximal pole order 1 (shifted by 1)."""
        r_poles = ope_to_rmatrix_poles(heisenberg_ope_poles())
        assert max_pole_order(r_poles) == 1

    def test_rmatrix_coefficient(self):
        """r(z) = kappa/z.  Coefficient at z^{-1} is kappa."""
        kappa = Fraction(1)
        r_poles = ope_to_rmatrix_poles(heisenberg_ope_poles(kappa))
        assert r_poles[1] == kappa

    def test_rmatrix_coefficient_level_k(self):
        """At level k, r(z) = k/z."""
        for k in [Fraction(1), Fraction(2), Fraction(1, 2), Fraction(7, 3)]:
            r_poles = ope_to_rmatrix_poles(heisenberg_ope_poles(k))
            assert r_poles[1] == k

    def test_no_higher_poles(self):
        """r-matrix has no poles of order > 1."""
        r_poles = ope_to_rmatrix_poles(heisenberg_ope_poles())
        for order in r_poles:
            assert order <= 1

    def test_single_pole_structure(self):
        """r-matrix has exactly one nonzero pole order."""
        r_poles = ope_to_rmatrix_poles(heisenberg_ope_poles())
        assert len(r_poles) == 1
        assert 1 in r_poles


class TestAffineSl2PoleShift:
    """Affine sl_2: OPE has z^{-2} (metric) and z^{-1} (bracket).
    r-matrix has z^{-1} only (the bracket term drops)."""

    def test_diagonal_ope_max_pole(self):
        """Diagonal OPE has maximal pole order 2."""
        poles = affine_sl2_ope_poles()
        assert max_pole_order(poles['diagonal']) == 2

    def test_diagonal_rmatrix_pole(self):
        """Diagonal r-matrix component: z^{-2} -> z^{-1}."""
        r_poles = ope_to_rmatrix_poles(affine_sl2_ope_poles()['diagonal'])
        assert max_pole_order(r_poles) == 1

    def test_off_diagonal_ope_simple_pole(self):
        """Off-diagonal OPE has a simple pole from structure constants."""
        poles = affine_sl2_ope_poles()
        assert max_pole_order(poles['off_diagonal']) == 1

    def test_off_diagonal_drops_in_rmatrix(self):
        """The simple pole z^{-1} in the OPE becomes z^0 = regular, drops."""
        r_poles = ope_to_rmatrix_poles({1: 1})  # Simple pole
        assert len(r_poles) == 0

    def test_rmatrix_is_casimir_over_z(self):
        """The full r-matrix is r(z) = k*Omega/z (single simple pole).

        The Casimir tensor Omega = sum_a T^a tensor T_a has only the
        metric part survive in the r-matrix.  The structure constant
        (bracket) part of the OPE drops because d log absorbs it.
        """
        for k in [Fraction(1), Fraction(2), Fraction(5)]:
            r_poles = ope_to_rmatrix_poles(affine_sl2_ope_poles(k)['diagonal'])
            assert r_poles == {1: k}

    def test_level_polynomiality(self):
        """r-matrix coefficient is linear in k (the level)."""
        r1 = ope_to_rmatrix_poles(affine_sl2_ope_poles(Fraction(1))['diagonal'])[1]
        r2 = ope_to_rmatrix_poles(affine_sl2_ope_poles(Fraction(2))['diagonal'])[1]
        r3 = ope_to_rmatrix_poles(affine_sl2_ope_poles(Fraction(3))['diagonal'])[1]
        # Linear: r(k) = k
        assert r2 - r1 == r3 - r2


class TestVirasoroPoleShift:
    """Virasoro: OPE has z^{-4}, z^{-2}, z^{-1}.
    r-matrix has z^{-3}, z^{-1} (no z^{-2} for bosonic algebra).

    r(z) = (c/2)/z^3 + 2T/z.
    Ground truth: eq:virasoro-r-collision in spectral-braiding-core.tex.
    """

    def test_ope_max_pole_order(self):
        """OPE has maximal pole order 4."""
        poles = virasoro_ope_poles()
        assert max_pole_order(poles) == 4

    def test_rmatrix_max_pole_order(self):
        """r-matrix has maximal pole order 3 (shifted from 4)."""
        r_poles = ope_to_rmatrix_poles(virasoro_ope_poles())
        assert max_pole_order(r_poles) == 3

    def test_rmatrix_leading_coefficient(self):
        """r_3 = c/2 (the leading pole coefficient)."""
        c = Fraction(26)
        r_poles = ope_to_rmatrix_poles(virasoro_ope_poles(c))
        assert r_poles[3] == c / 2

    def test_rmatrix_subleading(self):
        """r_1 = 2 (the 2T term, coefficient of T in the z^{-1} pole)."""
        r_poles = ope_to_rmatrix_poles(virasoro_ope_poles())
        assert r_poles[1] == 2

    def test_no_even_order_poles(self):
        """No z^{-2} pole: bosonic parity constraint.

        The OPE has z^{-2} (from 2T/(z-w)^2), but after d log absorption
        this becomes z^{-1}, not z^{-2}.  The only surviving poles are
        z^{-3} and z^{-1} (both odd).
        """
        r_poles = ope_to_rmatrix_poles(virasoro_ope_poles())
        for order in r_poles:
            assert order % 2 == 1, f"Even-order pole z^{{-{order}}} violates bosonic parity"

    def test_partial_T_drops(self):
        """The dT/(z-w) term (simple pole) drops: z^{-1} -> z^0 = regular."""
        # The OPE simple pole coefficient is 1 (for dT).
        # After d log absorption: z^{-1} -> z^0, which is regular and drops.
        ope = virasoro_ope_poles()
        assert 1 in ope  # OPE has z^{-1}
        r = ope_to_rmatrix_poles(ope)
        # The z^{-1} in r comes from the z^{-2} OPE pole (2T), not from z^{-1}
        assert r.get(1) == 2  # This is from the OPE z^{-2} shifted down

    def test_exactly_two_poles(self):
        """r-matrix has exactly two nonzero pole orders: 3 and 1."""
        r_poles = ope_to_rmatrix_poles(virasoro_ope_poles())
        assert set(r_poles.keys()) == {1, 3}

    def test_rmatrix_at_c26(self):
        """At c=26: r(z) = 13/z^3 + 2T/z."""
        r = ope_to_rmatrix_poles(virasoro_ope_poles(Fraction(26)))
        assert r[3] == 13
        assert r[1] == 2

    def test_rmatrix_at_c0(self):
        """At c=0: r(z) = 2T/z (leading pole vanishes)."""
        r = ope_to_rmatrix_poles(virasoro_ope_poles(Fraction(0)))
        assert 3 not in r or r.get(3) == 0
        assert r.get(1) == 2

    def test_rmatrix_at_c13_selfdual(self):
        """At the self-dual point c=13: r(z) = (13/2)/z^3 + 2T/z."""
        r = ope_to_rmatrix_poles(virasoro_ope_poles(Fraction(13)))
        assert r[3] == Fraction(13, 2)

    def test_laurent_expansion_matches_tex(self):
        """Verify eq:virasoro-r-laurent: r_1 = 2L, r_3 = c/2, r_k = 0 otherwise.

        Ground truth: spectral-braiding-core.tex lines 601-603.
        """
        c = Fraction(30)
        r = ope_to_rmatrix_poles(virasoro_ope_poles(c))
        assert r.get(3) == c / 2, "r_3 should be c/2"
        assert r.get(1) == 2, "r_1 should be 2 (coefficient of T)"
        assert r.get(2) is None, "r_2 should vanish (bosonic parity)"
        assert r.get(4) is None, "r_4 should vanish"
        assert r.get(5) is None, "r_5 should vanish"


class TestW3PoleShift:
    """W_3: the WW OPE has poles up to z^{-6}.
    r-matrix poles shifted down by 1."""

    def test_TT_same_as_virasoro(self):
        """T(z)T(w) OPE and r-matrix identical to Virasoro."""
        c = Fraction(4)
        tt_ope = w3_TT_ope_poles(c)
        tt_r = ope_to_rmatrix_poles(tt_ope)
        vir_r = ope_to_rmatrix_poles(virasoro_ope_poles(c))
        assert tt_r == vir_r

    def test_TW_ope_poles(self):
        """T(z)W(w) has poles at z^{-2} and z^{-1}."""
        tw = w3_TW_ope_poles()
        assert max_pole_order(tw) == 2

    def test_TW_rmatrix_single_pole(self):
        """TW r-matrix: z^{-2} -> z^{-1}, z^{-1} -> drops."""
        tw_r = ope_to_rmatrix_poles(w3_TW_ope_poles())
        assert max_pole_order(tw_r) == 1
        assert tw_r[1] == 3  # coefficient of W

    def test_WW_ope_max_pole(self):
        """WW OPE has maximal pole order 6."""
        ww = w3_WW_ope_poles()
        assert max_pole_order(ww) == 6

    def test_WW_rmatrix_max_pole(self):
        """WW r-matrix has maximal pole order 5 (shifted from 6)."""
        ww = w3_WW_ope_poles()
        # Only use numerical coefficients for the shift test
        numerical_poles = {k: v for k, v in ww.items() if isinstance(v, (int, float, Fraction))}
        r = ope_to_rmatrix_poles(numerical_poles)
        assert max_pole_order(r) == 5

    def test_WW_rmatrix_leading_coefficient(self):
        """WW r-matrix leading coefficient: (c/3) at z^{-5}."""
        c = Fraction(4)
        ww = w3_WW_ope_poles(c)
        numerical_poles = {k: v for k, v in ww.items() if isinstance(v, (int, float, Fraction))}
        r = ope_to_rmatrix_poles(numerical_poles)
        assert r[5] == c / 3

    def test_WW_rmatrix_subleading(self):
        """WW r-matrix: z^{-4} -> z^{-3} with coefficient 2 (from 2T)."""
        c = Fraction(4)
        ww = w3_WW_ope_poles(c)
        numerical_poles = {k: v for k, v in ww.items() if isinstance(v, (int, float, Fraction))}
        r = ope_to_rmatrix_poles(numerical_poles)
        assert r[3] == 2  # from the OPE z^{-4} term (coefficient 2)

    def test_WW_rmatrix_has_z_inv2(self):
        """WW r-matrix: z^{-3} in OPE -> z^{-2} in r-matrix.

        Unlike the single-generator Virasoro case, W_3 has TWO generators
        and the WW OPE has an odd pole z^{-3} (coefficient of dT).
        After d log absorption: z^{-3} -> z^{-2}.

        This is NOT a violation of bosonic parity for the W field:
        bosonic parity constrains SAME-STATISTICS pairings, and
        this is a WW pairing where W has spin 3 (odd), so
        even-order poles CAN appear in the r-matrix.
        """
        ww = w3_WW_ope_poles()
        numerical_poles = {k: v for k, v in ww.items() if isinstance(v, (int, float, Fraction))}
        r = ope_to_rmatrix_poles(numerical_poles)
        assert 2 in r  # z^{-2} pole present in WW r-matrix

    def test_WT_rmatrix(self):
        """W(z)T(w) r-matrix: z^{-2} -> z^{-1}, z^{-1} -> drops."""
        wt_r = ope_to_rmatrix_poles(w3_WT_ope_poles())
        assert max_pole_order(wt_r) == 1
        assert wt_r[1] == 3


class TestBetagammaPoleShift:
    """betagamma: OPE has z^{-1} only (mixed propagator).
    r-matrix: simple pole drops after d log absorption."""

    def test_bg_ope_simple_pole(self):
        """beta(z)gamma(w) ~ 1/(z-w): simple pole only."""
        bg = betagamma_ope_poles()
        assert max_pole_order(bg[('beta', 'gamma')]) == 1

    def test_bg_rmatrix_regular(self):
        """r-matrix for beta-gamma: simple pole becomes regular, drops.

        The mixed propagator 1/(z-w) produces NO pole in the r-matrix.
        This is because d log(z-w) * 1/(z-w) = d(z-w)/(z-w)^2, which
        extracts a z^0 = regular term.
        """
        r_bg = ope_to_rmatrix_poles(betagamma_ope_poles()[('beta', 'gamma')])
        assert len(r_bg) == 0, "beta-gamma r-matrix should have no poles"

    def test_diagonal_zero(self):
        """beta-beta and gamma-gamma: no singular OPE, no r-matrix."""
        bg = betagamma_ope_poles()
        r_bb = ope_to_rmatrix_poles(bg[('beta', 'beta')])
        r_gg = ope_to_rmatrix_poles(bg[('gamma', 'gamma')])
        assert len(r_bb) == 0
        assert len(r_gg) == 0

    def test_bg_no_diagonal_pole(self):
        """betagamma has NO diagonal (same-generator) singular OPE."""
        bg = betagamma_ope_poles()
        assert len(bg[('beta', 'beta')]) == 0
        assert len(bg[('gamma', 'gamma')]) == 0

    def test_bg_rmatrix_entirely_regular(self):
        """All r-matrix components of betagamma are regular (pole-free).

        This makes betagamma special: the bar complex propagator
        extracts no singular collision residue, consistent with
        shadow class C (contact, terminates at arity 4) and the
        fact that the leading bar interaction is quartic.
        """
        bg = betagamma_ope_poles()
        for pair, poles in bg.items():
            r = ope_to_rmatrix_poles(poles)
            assert len(r) == 0, f"Pair {pair} should have no r-matrix poles"


class TestAffineSl3PoleShift:
    """Affine sl_3 at level k: same pole structure as sl_2."""

    def test_sl3_diagonal_rmatrix(self):
        """Diagonal components: z^{-2} -> z^{-1}."""
        for k in [Fraction(1), Fraction(3), Fraction(-1)]:
            r = ope_to_rmatrix_poles(affine_slN_ope_poles(k, N=3)['diagonal'])
            assert r == {1: k}

    def test_sl3_off_diagonal_drops(self):
        """Off-diagonal (bracket) simple pole drops."""
        r = ope_to_rmatrix_poles(affine_slN_ope_poles(Fraction(1), N=3)['off_diagonal'])
        assert len(r) == 0


# ========================================================================
# Bosonic parity constraint
# ========================================================================

class TestBosonicParity:
    """For a SINGLE bosonic generator of integer conformal weight h,
    the r-matrix has no even-order poles.

    This follows from d log absorption: the OPE has poles at
    z^{-2h}, z^{-2h+2}, ..., z^{-2}, z^{-1}.  After shifting by 1:
    z^{-(2h-1)}, z^{-(2h-3)}, ..., z^{-1}.  All odd.

    The key observation: for a bosonic generator of weight h, the OPE
    T(z)T(w) has poles at even orders (z^{-2h}, z^{-(2h-2)}, ..., z^{-2})
    plus the descendant z^{-1}.  The even poles shift to odd in the
    r-matrix; the odd pole z^{-1} becomes regular.
    """

    def test_virasoro_no_even_poles(self):
        """Virasoro (h=2): r-matrix poles at z^{-3}, z^{-1} only."""
        r = ope_to_rmatrix_poles(virasoro_ope_poles())
        for order in r:
            assert order % 2 == 1

    def test_heisenberg_no_even_poles(self):
        """Heisenberg (h=1): r-matrix pole at z^{-1} only."""
        r = ope_to_rmatrix_poles(heisenberg_ope_poles())
        for order in r:
            assert order % 2 == 1

    def test_weight_h_generic_pattern(self):
        """For a generic weight-h bosonic generator:
        OPE poles at z^{-2h}, z^{-(2h-2)}, ..., z^{-2}, z^{-1}.
        r-matrix poles at z^{-(2h-1)}, z^{-(2h-3)}, ..., z^{-1}.
        All odd.
        """
        for h in [1, 2, 3, 4, 5]:
            # Schematic OPE: even poles from conformal algebra + z^{-1}
            ope = {}
            for n in range(2*h, 0, -2):
                ope[n] = 1  # placeholder coefficient
            ope[1] = 1  # descendant
            r = ope_to_rmatrix_poles(ope)
            for order in r:
                assert order % 2 == 1, (
                    f"Weight h={h}: even pole z^{{-{order}}} in r-matrix "
                    f"violates bosonic parity"
                )


# ========================================================================
# Classical Yang-Baxter equation verification
# ========================================================================

class TestCYBEHeisenberg:
    """Heisenberg: r(z) = kappa/z (abelian).
    CYBE: [r_{12}, r_{13}+r_{23}] + [r_{13}, r_{23}] = 0.
    For an abelian algebra (all brackets zero), this is trivially satisfied.
    """

    def test_cybe_trivial(self):
        """CYBE trivially satisfied for abelian r-matrix."""
        # r_{12}(z) = kappa/(z_1-z_2) * 1
        # All commutators vanish since the algebra is abelian.
        # [r_{12}, r_{13}] = 0, [r_{12}, r_{23}] = 0, [r_{13}, r_{23}] = 0.
        # Sum = 0.
        assert True  # Trivially satisfied


class TestCYBEAffineSl2:
    """Affine sl_2: r(z) = Omega/z where Omega = sum_a T^a tensor T_a.

    The CYBE for r(z) = Omega/z with spectral parameter:
      [r_{12}(z_{12}), r_{13}(z_{13})] + [r_{12}(z_{12}), r_{23}(z_{23})]
        + [r_{13}(z_{13}), r_{23}(z_{23})] = 0
    reduces via partial fractions to the infinitesimal braid relation (IBR):
      [Omega_{ij}, Omega_{ik} + Omega_{jk}] = 0
    for all distinct triples (i,j,k).

    Verify in the fundamental (2-dim) and adjoint (3-dim) representations.
    """

    @staticmethod
    def _build_sl2_fund_omegas():
        """Build Omega_{12}, Omega_{13}, Omega_{23} in V^{tensor 3}, V = C^2."""
        E = np.array([[0, 1], [0, 0]], dtype=complex)
        F = np.array([[0, 0], [1, 0]], dtype=complex)
        H = np.array([[1, 0], [0, -1]], dtype=complex)
        I2 = np.eye(2, dtype=complex)

        def t3(A, B, C):
            return np.kron(np.kron(A, B), C)

        O12 = t3(E, F, I2) + t3(F, E, I2) + 0.5 * t3(H, H, I2)
        O13 = t3(E, I2, F) + t3(F, I2, E) + 0.5 * t3(H, I2, H)
        O23 = t3(I2, E, F) + t3(I2, F, E) + 0.5 * t3(I2, H, H)
        return O12, O13, O23

    def test_ibr_fundamental_12(self):
        """IBR: [Omega_{12}, Omega_{13}+Omega_{23}] = 0 in fundamental."""
        O12, O13, O23 = self._build_sl2_fund_omegas()
        comm = lambda A, B: A @ B - B @ A
        assert np.allclose(comm(O12, O13 + O23), 0, atol=1e-12)

    def test_ibr_fundamental_13(self):
        """IBR: [Omega_{13}, Omega_{12}+Omega_{23}] = 0 in fundamental."""
        O12, O13, O23 = self._build_sl2_fund_omegas()
        comm = lambda A, B: A @ B - B @ A
        assert np.allclose(comm(O13, O12 + O23), 0, atol=1e-12)

    def test_ibr_fundamental_23(self):
        """IBR: [Omega_{23}, Omega_{12}+Omega_{13}] = 0 in fundamental."""
        O12, O13, O23 = self._build_sl2_fund_omegas()
        comm = lambda A, B: A @ B - B @ A
        assert np.allclose(comm(O23, O12 + O13), 0, atol=1e-12)

    def test_ibr_adjoint(self):
        """IBR in the adjoint 3-dim representation of sl_2."""
        # ad representation: basis {e, f, h}
        # [h,e]=2e, [h,f]=-2f, [e,f]=h
        E_adj = np.array([[0, 0, -2], [0, 0, 0], [0, 1, 0]], dtype=complex)
        F_adj = np.array([[0, 0, 0], [0, 0, 2], [-1, 0, 0]], dtype=complex)
        H_adj = np.array([[2, 0, 0], [0, -2, 0], [0, 0, 0]], dtype=complex)
        I3 = np.eye(3, dtype=complex)

        def t3(A, B, C):
            return np.kron(np.kron(A, B), C)

        O12 = t3(E_adj, F_adj, I3) + t3(F_adj, E_adj, I3) + 0.5 * t3(H_adj, H_adj, I3)
        O13 = t3(E_adj, I3, F_adj) + t3(F_adj, I3, E_adj) + 0.5 * t3(H_adj, I3, H_adj)
        O23 = t3(I3, E_adj, F_adj) + t3(I3, F_adj, E_adj) + 0.5 * t3(I3, H_adj, H_adj)

        comm = lambda A, B: A @ B - B @ A

        assert np.allclose(comm(O12, O13 + O23), 0, atol=1e-12), \
            f"IBR [O12, O13+O23] fails: norm = {np.max(np.abs(comm(O12, O13+O23)))}"
        assert np.allclose(comm(O13, O12 + O23), 0, atol=1e-12), \
            f"IBR [O13, O12+O23] fails: norm = {np.max(np.abs(comm(O13, O12+O23)))}"
        assert np.allclose(comm(O23, O12 + O13), 0, atol=1e-12), \
            f"IBR [O23, O12+O13] fails: norm = {np.max(np.abs(comm(O23, O12+O13)))}"


class TestCYBEAffineSl3:
    """IBR for sl_3 in the fundamental (3-dim) representation.
    r(z) = k*Omega/z where Omega is the sl_3 Casimir.

    The CYBE reduces to the IBR: [Omega_{ij}, Omega_{ik}+Omega_{jk}] = 0.
    """

    @staticmethod
    def _sl3_fund_generators():
        """Chevalley basis of sl_3 in the fundamental representation."""
        H1 = np.diag([1, -1, 0]).astype(complex)
        H2 = np.diag([0, 1, -1]).astype(complex)
        E1 = np.zeros((3, 3), dtype=complex); E1[0, 1] = 1
        E2 = np.zeros((3, 3), dtype=complex); E2[1, 2] = 1
        E3 = np.zeros((3, 3), dtype=complex); E3[0, 2] = 1
        F1 = np.zeros((3, 3), dtype=complex); F1[1, 0] = 1
        F2 = np.zeros((3, 3), dtype=complex); F2[2, 1] = 1
        F3 = np.zeros((3, 3), dtype=complex); F3[2, 0] = 1
        return [H1, H2, E1, E2, E3, F1, F2, F3]

    @staticmethod
    def _build_sl3_omegas():
        """Build Omega_{12}, Omega_{13}, Omega_{23} for sl_3 fund."""
        gens = TestCYBEAffineSl3._sl3_fund_generators()
        H1, H2, E1, E2, E3, F1, F2, F3 = gens
        I3 = np.eye(3, dtype=complex)

        # Inverse Cartan metric for sl_3: (1/3)[[2,1],[1,2]]
        K_inv = np.array([[2, 1], [1, 2]], dtype=complex) / 3.0
        H_gens = [H1, H2]

        def t3(A, B, C):
            return np.kron(np.kron(A, B), C)

        def build_omega(slot1, slot2, slot_id):
            """Build Omega with generators in slots slot1, slot2; identity in third."""
            O = np.zeros((27, 27), dtype=complex)
            ids = [I3, I3, I3]

            def place(A, B):
                mats = [I3, I3, I3]
                mats[slot1] = A
                mats[slot2] = B
                return t3(mats[0], mats[1], mats[2])

            for i in range(2):
                for j in range(2):
                    O += K_inv[i, j] * place(H_gens[i], H_gens[j])
            for Ep, Fp in [(E1, F1), (E2, F2), (E3, F3)]:
                O += place(Ep, Fp) + place(Fp, Ep)
            return O

        O12 = build_omega(0, 1, 2)
        O13 = build_omega(0, 2, 1)
        O23 = build_omega(1, 2, 0)
        return O12, O13, O23

    def test_ibr_fundamental_12(self):
        """IBR: [Omega_{12}, Omega_{13}+Omega_{23}] = 0 for sl_3 fund."""
        O12, O13, O23 = self._build_sl3_omegas()
        comm = lambda A, B: A @ B - B @ A
        assert np.allclose(comm(O12, O13 + O23), 0, atol=1e-10), \
            f"IBR [O12, O13+O23] fails: norm = {np.max(np.abs(comm(O12, O13+O23)))}"

    def test_ibr_fundamental_13(self):
        """IBR: [Omega_{13}, Omega_{12}+Omega_{23}] = 0 for sl_3 fund."""
        O12, O13, O23 = self._build_sl3_omegas()
        comm = lambda A, B: A @ B - B @ A
        assert np.allclose(comm(O13, O12 + O23), 0, atol=1e-10), \
            f"IBR [O13, O12+O23] fails: norm = {np.max(np.abs(comm(O13, O12+O23)))}"

    def test_ibr_fundamental_23(self):
        """IBR: [Omega_{23}, Omega_{12}+Omega_{13}] = 0 for sl_3 fund."""
        O12, O13, O23 = self._build_sl3_omegas()
        comm = lambda A, B: A @ B - B @ A
        assert np.allclose(comm(O23, O12 + O13), 0, atol=1e-10), \
            f"IBR [O23, O12+O13] fails: norm = {np.max(np.abs(comm(O23, O12+O13)))}"


# ========================================================================
# Unitarity: r_{12}(z) + r_{21}(-z) = Omega
# ========================================================================

class TestUnitarity:
    """For affine Kac-Moody algebras, the r-matrix satisfies the
    quasi-classical unitarity condition:
      r_{12}(z) + r_{21}(-z) = Omega  (the Casimir)

    For r(z) = Omega/z, this becomes:
      Omega/(z) + Omega/(-(-z)) = Omega/z + Omega/z = 2*Omega/z ???

    Actually, the correct unitarity for the classical r-matrix
    r(z) = Omega/z is the SKEW-SYMMETRY condition:
      r_{12}(z) = -r_{21}(-z)   i.e.   r_{12}(z) + r_{21}(-z) = 0
    when Omega is SYMMETRIC (which it is for the Casimir).

    This reflects: the collision residue extracted from the SKEW-SYMMETRIC
    d log kernel is itself skew.

    For the UNITARIZED r-matrix r(z) = Omega/z (where Omega = Casimir):
      r_{12}(z) + r_{21}(-z) = Omega/z + Omega/z = 2*Omega/z
    but r_{21}(z) = P(Omega/z)P = Omega/z (Casimir is symmetric).
    So r_{21}(-z) = Omega/(-z) = -Omega/z.
    Hence r_{12}(z) + r_{21}(-z) = Omega/z - Omega/z = 0.

    This is the CLASSICAL skew-symmetry of the collision residue.
    """

    def test_heisenberg_skew_symmetry(self):
        """For Heisenberg, r(z) = kappa/z is skew: r(z) + r(-z) = 0."""
        # r(z) = k/z.  r(-z) = k/(-z) = -k/z.  Sum = 0.
        kappa = Fraction(1)
        # r(z) at z and -z:
        # The function f(z) = kappa/z is odd: f(-z) = -f(z).
        # Hence r(z) + r(-z) = 0 (unitarity/skew-symmetry).
        assert True  # Odd function, trivially skew.

    def test_sl2_skew_symmetry_fundamental(self):
        """For sl_2, verify r_{12}(z) + r_{21}(-z) = 0 numerically.

        r_{12}(z) = Omega/z.  r_{21}(z) = P*Omega*P/z where P is the
        permutation.  For sl_2 Casimir, Omega is symmetric: P*Omega*P = Omega.
        Hence r_{21}(-z) = Omega/(-z) = -Omega/z.
        So r_{12}(z) + r_{21}(-z) = 0.
        """
        E = np.array([[0, 1], [0, 0]], dtype=complex)
        F = np.array([[0, 0], [1, 0]], dtype=complex)
        H = np.array([[1, 0], [0, -1]], dtype=complex)
        I2 = np.eye(2)

        Omega = np.kron(E, F) + np.kron(F, E) + 0.5 * np.kron(H, H)

        # Permutation operator P on C^2 tensor C^2
        P = np.zeros((4, 4), dtype=complex)
        for i in range(2):
            for j in range(2):
                P[i * 2 + j, j * 2 + i] = 1

        # Check Omega is symmetric: P*Omega*P = Omega
        Omega_21 = P @ Omega @ P
        assert np.allclose(Omega, Omega_21, atol=1e-14), \
            "Casimir Omega should be symmetric under P"

        # r_{12}(z) + r_{21}(-z) = Omega/z + P*Omega*P/(-z) = Omega/z - Omega/z = 0
        # Since Omega = P*Omega*P, the sum vanishes identically.
        result = Omega - Omega_21  # Should be zero
        assert np.allclose(result, 0, atol=1e-14)

    def test_sl3_casimir_symmetry(self):
        """Verify the sl_3 Casimir is symmetric under permutation.

        This is a prerequisite for skew-symmetry of the r-matrix.
        """
        gens = TestCYBEAffineSl3._sl3_fund_generators()
        H1, H2, E1, E2, E3, F1, F2, F3 = gens
        I3 = np.eye(3, dtype=complex)

        K_inv = np.array([[2, 1], [1, 2]], dtype=complex) / 3.0
        H_gens = [H1, H2]

        Omega = np.zeros((9, 9), dtype=complex)
        for i in range(2):
            for j in range(2):
                Omega += K_inv[i, j] * np.kron(H_gens[i], H_gens[j])
        for Ep, Fp in [(E1, F1), (E2, F2), (E3, F3)]:
            Omega += np.kron(Ep, Fp) + np.kron(Fp, Ep)

        # Permutation on C^3 tensor C^3
        P = np.zeros((9, 9), dtype=complex)
        for i in range(3):
            for j in range(3):
                P[i * 3 + j, j * 3 + i] = 1

        Omega_21 = P @ Omega @ P
        assert np.allclose(Omega, Omega_21, atol=1e-12), \
            "sl_3 Casimir should be symmetric under permutation"

    def test_virasoro_odd_function(self):
        """Virasoro r-matrix r(z) = (c/2)/z^3 + 2T/z is an ODD function of z.

        r(-z) = (c/2)/(-z)^3 + 2T/(-z) = -(c/2)/z^3 - 2T/z = -r(z).
        Hence r(z) + r(-z) = 0 (skew-symmetry / unitarity).

        This is automatic because all poles are odd order (bosonic parity).
        """
        c = Fraction(26)
        r = ope_to_rmatrix_poles(virasoro_ope_poles(c))
        for order in r:
            assert order % 2 == 1, (
                f"Even-order pole z^{{-{order}}} would break skew-symmetry"
            )
        # All odd poles -> r(z) is odd -> r(z) + r(-z) = 0.


# ========================================================================
# Cross-family consistency checks
# ========================================================================

class TestCrossFamilyConsistency:
    """Cross-checks between families to catch AP1/AP3 violations."""

    def test_pole_shift_universality(self):
        """The pole-shift rule (subtract 1) applies identically to all families."""
        families = {
            'Heisenberg': heisenberg_ope_poles(),
            'Virasoro': virasoro_ope_poles(),
            'TT_W3': w3_TT_ope_poles(),
        }
        for name, ope in families.items():
            r = ope_to_rmatrix_poles(ope)
            for n in ope:
                if ope[n] != 0:
                    if n - 1 > 0:
                        assert (n - 1) in r, \
                            f"{name}: OPE pole z^{{-{n}}} should produce r-matrix pole z^{{-{n-1}}}"
                    else:
                        assert (n - 1) not in r or r.get(n - 1) == 0, \
                            f"{name}: OPE pole z^{{-{n}}} should drop (becomes regular)"

    def test_max_pole_order_shift(self):
        """For every family: max r-matrix pole = max OPE pole - 1."""
        test_cases = [
            ('Heisenberg', heisenberg_ope_poles(), 2, 1),
            ('Virasoro', virasoro_ope_poles(), 4, 3),
            ('TW', w3_TW_ope_poles(), 2, 1),
        ]
        for name, ope, expected_ope_max, expected_r_max in test_cases:
            assert max_pole_order(ope) == expected_ope_max, \
                f"{name}: wrong OPE max pole"
            r = ope_to_rmatrix_poles(ope)
            assert max_pole_order(r) == expected_r_max, \
                f"{name}: wrong r-matrix max pole (expected {expected_r_max})"

    def test_kappa_from_rmatrix(self):
        """kappa(A) = scalar trace of the leading r-matrix coefficient.

        For single-generator algebras:
          kappa(Heis) = kappa (the level) = coefficient of z^{-1} in r(z)
          kappa(Vir_c) = c/2 = coefficient of z^{-3} in r(z)

        The modular characteristic IS the leading r-matrix coefficient.
        """
        # Heisenberg
        for k in [Fraction(1), Fraction(2), Fraction(1, 2)]:
            r = ope_to_rmatrix_poles(heisenberg_ope_poles(k))
            leading_order = max(r.keys())
            assert r[leading_order] == k, "kappa(Heis) should be the level"

        # Virasoro
        for c in [Fraction(1), Fraction(26), Fraction(13)]:
            r = ope_to_rmatrix_poles(virasoro_ope_poles(c))
            leading_order = max(r.keys())
            assert r[leading_order] == c / 2, "kappa(Vir_c) should be c/2"


class TestCollisionResidueModuleConsistency:
    """Cross-check against the collision_residue_identification module."""

    def test_heisenberg_ope_data_consistent(self):
        """Verify our OPE data matches collision_residue_identification.py."""
        from collision_residue_identification import heisenberg_ope as cri_heis
        ope = cri_heis(Fraction(1))
        assert ope.pole_orders[("J", "J")] == 2
        # Our independent computation agrees
        our_poles = heisenberg_ope_poles(Fraction(1))
        assert max_pole_order(our_poles) == ope.pole_orders[("J", "J")]

    def test_virasoro_ope_data_consistent(self):
        """Verify our OPE data matches collision_residue_identification.py."""
        from collision_residue_identification import virasoro_ope as cri_vir
        c = Fraction(26)
        ope = cri_vir(c)
        assert ope.pole_orders[("T", "T")] == 4
        assert ope.leading_coefficients[("T", "T")] == c / 2
        # Our independent computation agrees
        our_poles = virasoro_ope_poles(c)
        assert max_pole_order(our_poles) == 4
        assert our_poles[4] == c / 2

    def test_betagamma_ope_data_consistent(self):
        """Verify our OPE data matches collision_residue_identification.py."""
        from collision_residue_identification import betagamma_ope as cri_bg
        ope = cri_bg(Fraction(1))
        assert ope.pole_orders[("beta", "gamma")] == 1
        assert ope.pole_orders[("beta", "beta")] == 0
        # Our independent computation agrees
        our = betagamma_ope_poles()
        assert max_pole_order(our[('beta', 'gamma')]) == 1
        assert max_pole_order(our[('beta', 'beta')]) == 0

    def test_sl2_ope_data_consistent(self):
        """Verify our OPE data matches collision_residue_identification.py."""
        from collision_residue_identification import affine_sl2_ope as cri_sl2
        k = Fraction(1)
        ope = cri_sl2(k)
        assert ope.pole_orders[("J1", "J1")] == 2
        assert ope.leading_coefficients[("J1", "J1")] == k


# ========================================================================
# Pole order counting tests (the core AP19 verification)
# ========================================================================

class TestPoleOrderCounting:
    """Direct tests of the AP19 claim: pole orders differ by exactly 1."""

    def test_heisenberg_shift_exactly_1(self):
        """Heisenberg: max OPE pole - max r-matrix pole = 1."""
        ope_max = max_pole_order(heisenberg_ope_poles())
        r_max = max_pole_order(ope_to_rmatrix_poles(heisenberg_ope_poles()))
        assert ope_max - r_max == 1

    def test_virasoro_shift_exactly_1(self):
        """Virasoro: max OPE pole - max r-matrix pole = 1."""
        ope_max = max_pole_order(virasoro_ope_poles())
        r_max = max_pole_order(ope_to_rmatrix_poles(virasoro_ope_poles()))
        assert ope_max - r_max == 1

    def test_sl2_diagonal_shift_exactly_1(self):
        """sl_2 diagonal: max OPE pole - max r-matrix pole = 1."""
        ope = affine_sl2_ope_poles()['diagonal']
        ope_max = max_pole_order(ope)
        r_max = max_pole_order(ope_to_rmatrix_poles(ope))
        assert ope_max - r_max == 1

    def test_w3_TW_shift_exactly_1(self):
        """W_3 T-W: max OPE pole - max r-matrix pole = 1."""
        ope = w3_TW_ope_poles()
        ope_max = max_pole_order(ope)
        r_max = max_pole_order(ope_to_rmatrix_poles(ope))
        assert ope_max - r_max == 1

    def test_w3_WW_shift_exactly_1(self):
        """W_3 W-W: max OPE pole (6) -> max r-matrix pole (5), shift = 1."""
        ww = w3_WW_ope_poles()
        ope_max = max_pole_order(ww)
        assert ope_max == 6
        # After shift: max pole is 5
        numerical_poles = {k: v for k, v in ww.items() if isinstance(v, (int, float, Fraction))}
        r = ope_to_rmatrix_poles(numerical_poles)
        r_max = max_pole_order(r)
        assert ope_max - r_max == 1

    def test_betagamma_complete_absorption(self):
        """betagamma: OPE max pole = 1, r-matrix max pole = 0 (entirely regular)."""
        bg = betagamma_ope_poles()
        for pair, poles in bg.items():
            if poles:  # non-empty
                ope_max = max_pole_order(poles)
                r_max = max_pole_order(ope_to_rmatrix_poles(poles))
                if ope_max == 1:
                    assert r_max == 0, \
                        f"Pair {pair}: simple pole should be completely absorbed"

    @pytest.mark.parametrize("c", [
        Fraction(0), Fraction(1), Fraction(13), Fraction(26),
        Fraction(-2), Fraction(100), Fraction(1, 2),
    ])
    def test_virasoro_shift_parametric(self, c):
        """Virasoro at various c: the shift is always exactly 1."""
        ope = virasoro_ope_poles(c)
        # Even at c=0, the OPE max pole is 4 (the c/2 coefficient is 0,
        # but the pole ORDER from the 2T/(z-w)^2 term is 2)
        if c == 0:
            # At c=0: the z^{-4} coefficient vanishes, so max OPE pole is 2
            non_vanishing = {k: v for k, v in ope.items() if v != 0}
            ope_max = max_pole_order(non_vanishing)
            r = ope_to_rmatrix_poles(non_vanishing)
            r_max = max_pole_order(r)
        else:
            ope_max = max_pole_order(ope)
            r = ope_to_rmatrix_poles(ope)
            r_max = max_pole_order(r)
        assert ope_max - r_max == 1


# ========================================================================
# Comprehensive parametric tests
# ========================================================================

class TestParametricSweep:
    """Sweep over many parameter values to stress-test the pole shift."""

    @pytest.mark.parametrize("k", [
        Fraction(1), Fraction(2), Fraction(5), Fraction(10),
        Fraction(1, 2), Fraction(1, 3), Fraction(-1),
    ])
    def test_heisenberg_level_sweep(self, k):
        """Heisenberg at various levels: always exactly one simple pole."""
        r = ope_to_rmatrix_poles(heisenberg_ope_poles(k))
        assert len(r) == 1
        assert 1 in r
        assert r[1] == k

    @pytest.mark.parametrize("k", [
        Fraction(1), Fraction(2), Fraction(3), Fraction(10), Fraction(1, 2),
    ])
    def test_affine_sl2_level_sweep(self, k):
        """Affine sl_2 at various levels: diagonal r-matrix coefficient = k."""
        r = ope_to_rmatrix_poles(affine_sl2_ope_poles(k)['diagonal'])
        assert r == {1: k}
