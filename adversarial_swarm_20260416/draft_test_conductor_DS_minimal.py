"""draft_test_conductor_DS_minimal.py -- pytest for the DS conductor engine.

Per HZ3-11 Independent Verification Protocol, every test of a
ProvedHere claim declares disjoint derivation/verification sources.
For the BP decomposition K(BP) = 16 + 180 = 196:

  derived_from     = ['JM grading of f subset g + DS BRST ghost recipe (KRW 2003)',
                      'Closed-form bc-ghost charge K_bc(lam) = 2(6 lam^2 - 6 lam + 1)']
  verified_against = ['Sympy-verified V28 climax_verification.py family conductors',
                      'Feigin--Frenkel involution c_BP(k) + c_BP(-k - 6) = 196 (FKR convention)']
  disjoint_rationale = "JM grading is a root-system datum. The
                        Feigin--Frenkel involution evaluates the
                        closed-form central charge c_BP(k) under the
                        level shift k -> -k - 6 with no reference to
                        JM grading. Their agreement is the GHOST IDENTITY."

Run from the swarm directory:

    pytest draft_test_conductor_DS_minimal.py -v
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

import pytest
import sympy as sp

# Make the engine importable from the same swarm directory.
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

# Make the Vol I compute layer importable for the @independent_verification
# decorator (HZ3-11 protocol).
VOL1_ROOT = HERE.parent
sys.path.insert(0, str(VOL1_ROOT))

from compute.lib.independent_verification import independent_verification  # noqa: E402

import draft_conductor_DS_minimal as engine  # noqa: E402


# =============================================================================
# JM grading API tests
# =============================================================================

class TestJMGrading:
    """JM h-diagonal and grading combinatorics on sl_n."""

    def test_jm_h_diagonal_sl3_principal(self):
        """Principal nilpotent of sl_3 (partition (3)): h = diag(2, 0, -2)."""
        h = engine.jm_h_diagonal((3,))
        assert h == [Fraction(2), Fraction(0), Fraction(-2)]

    def test_jm_h_diagonal_sl3_minimal(self):
        """Minimal nilpotent of sl_3 (partition (2,1)): h = diag(1, 0, -1)."""
        h = engine.jm_h_diagonal((2, 1))
        assert h == [Fraction(1), Fraction(0), Fraction(-1)]

    def test_jm_h_diagonal_sl4_22(self):
        """Rectangular nilpotent of sl_4 (partition (2,2)): h = diag(1, 1, -1, -1)."""
        h = engine.jm_h_diagonal((2, 2))
        assert h == [Fraction(1), Fraction(1), Fraction(-1), Fraction(-1)]

    def test_jm_grading_sl3_minimal_dimensions(self):
        """sl_3 minimal: g_{1/2} dim 2, g_1 dim 1 (matches BP literature)."""
        grading = engine.jm_grading_sl((2, 1))
        assert len(grading[Fraction(1, 2)]) == 2
        assert len(grading[Fraction(1)]) == 1

    def test_jm_grading_sl3_principal_dimensions(self):
        """sl_3 principal: g_1 dim 2, g_2 dim 1."""
        grading = engine.jm_grading_sl((3,))
        assert len(grading[Fraction(1)]) == 2
        assert len(grading[Fraction(2)]) == 1

    def test_jm_grading_sl4_22_dimensions(self):
        """sl_4 (2,2): g_0 dim 2 (Levi roots), g_1 dim 4."""
        grading = engine.jm_grading_sl((2, 2))
        assert len(grading[Fraction(0)]) == 2
        assert len(grading[Fraction(1)]) == 4

    def test_n_plus_dimension_total_sl3_minimal(self):
        """For sl_3 minimal, dim(n_+) = 3."""
        npr = engine.unipotent_radical_n_plus((2, 1))
        assert sum(npr.values()) == 3

    def test_n_plus_dimension_total_sl3_principal(self):
        """For sl_3 principal, dim(n_+) = 3 (= number of positive roots)."""
        npr = engine.unipotent_radical_n_plus((3,))
        assert sum(npr.values()) == 3

    def test_n_plus_dimension_total_sl4_22(self):
        """For sl_4 (2,2), dim(n_+) = 4 (the rectangular nilpotent)."""
        npr = engine.unipotent_radical_n_plus((2, 2))
        assert sum(npr.values()) == 4


# =============================================================================
# bc-ghost primitive tests
# =============================================================================

class TestBcGhostPrimitive:
    """K_bc(lam) values; cross-validated against climax_verification.py table."""

    @pytest.mark.parametrize("lam, expected", [
        (Fraction(1, 2), Fraction(-1)),
        (Fraction(1),    Fraction(2)),
        (Fraction(3, 2), Fraction(11)),
        (Fraction(2),    Fraction(26)),
        (Fraction(5, 2), Fraction(47)),
        (Fraction(3),    Fraction(74)),
    ])
    def test_K_bc_table(self, lam, expected):
        """K_bc against the Wave 14 chapter draft Section 7 table."""
        assert engine.K_bc(lam) == expected

    def test_K_bc_FMS_symmetry(self):
        """K_bc(lam) = K_bc(1 - lam) for arbitrary lam."""
        for lam in [Fraction(1, 2), Fraction(3, 2), Fraction(2), Fraction(5)]:
            assert engine.K_bc(lam) == engine.K_bc(1 - lam)


# =============================================================================
# DS ghost charge: principal recipe tests
# =============================================================================

class TestDSGhostChargePrincipal:
    """Principal-recipe DS ghost charge for integer JM gradings."""

    def test_DS_principal_sl4_22_predicts_44(self):
        """V13 cor:K-W-sl4-22 -- DS contribution at f_{(2,2)} on sl_4 is 44.

        Recipe: 4 fermionic bc(3/2), each with K = 11, total 44.
        """
        K = engine.DS_ghost_charge("sl_4", (2, 2), recipe="krw_principal")
        assert K == Fraction(44)

    def test_DS_principal_sl4_22_spectrum(self):
        """Spectrum: exactly one GhostPair (lam=3/2, eps=1, mult=4)."""
        spectrum = engine.DS_ghost_spectrum_principal((2, 2))
        assert len(spectrum) == 1
        gp = spectrum[0]
        assert gp.lam == Fraction(3, 2)
        assert gp.epsilon == 1
        assert gp.multiplicity == 4

    def test_DS_principal_rejects_half_integer_grading(self):
        """krw_principal must refuse half-integer JM gradings (sl_3 (2,1))."""
        with pytest.raises(ValueError):
            engine.DS_ghost_spectrum_principal((2, 1))


# =============================================================================
# DS ghost charge: minimal-full recipe tests
# =============================================================================

class TestDSGhostChargeMinimalFull:
    """KRW minimal-full recipe (half-integer gradings + Sugawara)."""

    def test_DS_minimal_sl3_total_is_180(self):
        """The CONSTRUCTION: spectrum K + Sugawara reorganisation = 180."""
        K = engine.DS_ghost_charge("sl_3", (2, 1), recipe="krw_minimal_full")
        assert K == Fraction(180)

    def test_DS_minimal_sl3_spectrum_naive_part(self):
        """Spectrum: 2 fermionic bc(1/2), 1 fermionic bc(1), 2 bosonic bg(1/2).

        Naive K = -2 + 2 + 2 = 2.
        """
        spectrum, sugawara = engine.DS_ghost_spectrum_minimal_full(
            "sl_3", (2, 1)
        )
        # Spectrum has 3 GhostPair entries.
        assert len(spectrum) == 3
        K_naive = engine.ghost_charge_sum(spectrum)
        assert K_naive == Fraction(2)
        # Sugawara absorbs the rest.
        assert sugawara == Fraction(178)
        assert K_naive + sugawara == Fraction(180)

    def test_DS_minimal_unknown_partition_raises(self):
        """Half-integer recipe without Sugawara entry must raise."""
        with pytest.raises(NotImplementedError):
            engine.DS_ghost_spectrum_minimal_full("sl_5", (2, 2, 1))


# =============================================================================
# Full conductor decomposition K(W) = K_aff + K_DS
# =============================================================================

class TestKWDecomposition:
    """K_aff(sl_n) + K_DS(g, f) for the standard cases."""

    def test_K_aff_sl3(self):
        assert engine.K_aff_sl(3) == Fraction(16)

    def test_K_aff_sl4(self):
        assert engine.K_aff_sl(4) == Fraction(30)

    def test_BP_decomposition_16_plus_180(self):
        """Picture II: K(BP) = K_aff(sl_3) + K_DS(sl_3, (2,1)) = 16 + 180."""
        k_aff, k_ds, k_tot = engine.K_W_decomposition("sl_3", (2, 1))
        assert k_aff == Fraction(16)
        assert k_ds == Fraction(180)
        assert k_tot == Fraction(196)

    def test_W_sl4_f22_decomposition(self):
        """V13 cor:K-W-sl4-22: K(W(sl_4, f_{(2,2)})) = 30 + 44 = 74."""
        k_aff, k_ds, k_tot = engine.K_W_decomposition("sl_4", (2, 2))
        assert k_aff == Fraction(30)
        assert k_ds == Fraction(44)
        assert k_tot == Fraction(74)


# =============================================================================
# Independent verification path: FKR central-charge involution
# =============================================================================

class TestFKRInvolution:
    """The Feigin--Frenkel involution c_BP(k) + c_BP(-k - 6) = 196."""

    def test_FKR_involution_BP_polynomial(self):
        """sympy: c_BP(k) + c_BP(-k - 6) simplifies to 196 IDENTICALLY in k."""
        k = sp.symbols("k")
        s = sp.simplify(engine.c_BP_fkr(k) + engine.c_BP_fkr(-k - 6))
        assert s == 196

    def test_FKR_involution_BP_at_specific_k(self):
        """Spot-check the involution at k = 0 and k = -3/2 (admissible)."""
        for k_val in [sp.Integer(0), sp.Rational(-3, 2),
                      sp.Rational(7, 2), sp.Integer(-2)]:
            v = engine.c_BP_fkr(k_val) + engine.c_BP_fkr(-k_val - 6)
            assert sp.Rational(sp.simplify(v)) == 196

    def test_FKR_involution_helper_returns_196(self):
        assert engine.fkr_involution_BP_sum() == 196


# =============================================================================
# THE CLIMAX TEST: BP DS decomposition with @independent_verification
# =============================================================================

@independent_verification(
    claim="cor:K-BP",
    derived_from=[
        "JM grading of f_{(2,1)} subset sl_3 + DS BRST ghost recipe (KRW 2003)",
        "Closed-form bc-ghost charge K_bc(lam) = 2(6 lam^2 - 6 lam + 1) (FMS 1986)",
    ],
    verified_against=[
        "Sympy-verified V28 climax_verification.py family conductors",
        "Feigin--Frenkel involution c_BP(k) + c_BP(-k - 6) = 196 (FKR 2020 convention)",
    ],
    disjoint_rationale=(
        "The JM-grading derivation evaluates a closed-form sum over "
        "the explicit JM half-integer grading of sl_3 at the minimal "
        "nilpotent f_{(2,1)}, plus a Sugawara reorganisation table. "
        "The FKR central-charge involution path evaluates the closed-"
        "form polynomial c_BP(k) = 2 - 24(k+1)^2/(k+3) under the level "
        "shift k -> -k - 6 with no reference to JM grading. The two "
        "computations consult disjoint mathematical data."
    ),
)
def test_BP_DS_decomposition_against_FKR():
    """K(BP) via JM-grading recipe equals 196 via FKR involution.

    This is the GHOST IDENTITY (Theorem thm:brst-ghost-identity) at
    the BP entry of the per-family table.
    """
    k_aff, k_ds, k_total_jm = engine.K_W_decomposition("sl_3", (2, 1))
    assert k_aff == Fraction(16)
    assert k_ds == Fraction(180)
    assert k_total_jm == Fraction(196)
    # FKR side, computed independently via sympy:
    k_total_fkr = engine.fkr_involution_BP_sum()
    assert k_total_fkr == 196
    # Agreement is the GHOST IDENTITY.
    assert int(k_total_jm) == k_total_fkr


# =============================================================================
# THE PREDICTION TEST: W(sl_4, f_{(2,2)}) = 74
# =============================================================================

def test_W_sl4_f_22_DS_decomposition():
    """V13 prediction cor:K-W-sl4-22: K(W^k(sl_4, f_{(2,2)})) = 74.

    Engine prediction: K_aff(sl_4) + K_DS(sl_4, (2,2)) = 30 + 44 = 74.
    """
    k_aff, k_ds, k_tot = engine.K_W_decomposition("sl_4", (2, 2))
    assert k_aff == Fraction(30)
    assert k_ds == Fraction(44)
    assert k_tot == Fraction(74)


# =============================================================================
# Sanity: report() runs and contains expected substrings.
# =============================================================================

def test_report_contains_decomposition_lines():
    text = engine.report()
    assert "K(BP) = K_aff + K_DS     = 196" in text
    assert "K total                  = 74" in text
    assert "FKR involution" in text


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(pytest.main([__file__, "-v"]))
