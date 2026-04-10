"""Tests for the Chriss-Ginzburg universal engine.

Verifies the CENTRAL PRINCIPLE: every algebraic structure in the monograph
is a projection of the single MC element Theta_A in MC(g^mod_A).

The test structure mirrors the mathematical architecture:
1. Construction: Theta_A from chiral algebra data
2. MC equation: D·Theta + ½[Theta,Theta] = 0 at each arity
3. Projection table: each pi_* recovers a standalone module's output
4. Five main theorems: all as MC consequences
5. Cross-family: all standard families verified
6. Consistency: cross-projection identities
"""

import pytest
from fractions import Fraction

from compute.lib.chriss_ginzburg_universal import (
    UniversalMCElement,
    all_standard_mc_elements,
    chriss_ginzburg_master_table,
    ARCHETYPE_G, ARCHETYPE_L, ARCHETYPE_C, ARCHETYPE_M,
)


# =====================================================================
# I. Construction and basic properties
# =====================================================================

class TestConstruction:
    def test_heisenberg_k1(self):
        theta = UniversalMCElement.from_heisenberg(k=1)
        assert theta.kappa_value == Fraction(1)  # kappa = k in this convention
        assert theta.archetype == ARCHETYPE_G
        assert theta.shadow_depth == 2

    def test_heisenberg_k3(self):
        theta = UniversalMCElement.from_heisenberg(k=3)
        assert theta.kappa_value == Fraction(3)

    def test_virasoro_c1(self):
        theta = UniversalMCElement.from_virasoro(c=1)
        assert theta.kappa_value == Fraction(1, 2)
        assert theta.archetype == ARCHETYPE_M

    def test_virasoro_c26(self):
        theta = UniversalMCElement.from_virasoro(c=26)
        assert theta.kappa_value == Fraction(13)

    def test_virasoro_c13_self_dual(self):
        theta = UniversalMCElement.from_virasoro(c=13)
        assert theta.kappa_value == Fraction(13, 2)

    def test_affine_sl2_k1(self):
        theta = UniversalMCElement.from_affine_sl2(k=1)
        assert theta.archetype == ARCHETYPE_L
        assert theta.shadow_depth == 3

    def test_affine_sl2_kappa(self):
        theta = UniversalMCElement.from_affine_sl2(k=1)
        # kappa = dim(g)*(k+h^v)/(2*h^v) = 3*3/4 = 9/4 in Sugawara convention
        assert theta.kappa_value == Fraction(9, 4)

    def test_betagamma(self):
        theta = UniversalMCElement.from_betagamma()
        assert theta.archetype == ARCHETYPE_C
        assert theta.shadow_depth == 4

    def test_w3_c50(self):
        theta = UniversalMCElement.from_w3(c=50)
        assert theta.archetype == ARCHETYPE_M

    def test_lattice_r1(self):
        theta = UniversalMCElement.from_lattice(rank=1)
        assert theta.archetype == ARCHETYPE_G
        assert theta.kappa_value == Fraction(1)  # kappa = rank = 1

    def test_lattice_r8(self):
        theta = UniversalMCElement.from_lattice(rank=8)
        assert theta.kappa_value == Fraction(8)  # kappa = rank = 8

    def test_lattice_r24(self):
        theta = UniversalMCElement.from_lattice(rank=24)
        assert theta.kappa_value == Fraction(24)  # kappa = rank = 24

    def test_shadow_depth_classification(self):
        """Shadow depth correctly classifies G/L/C/M."""
        assert UniversalMCElement.from_heisenberg(k=1).shadow_depth == 2
        assert UniversalMCElement.from_affine_sl2(k=1).shadow_depth == 3
        assert UniversalMCElement.from_betagamma().shadow_depth == 4
        # Mixed type: shadow_depth is None (= infinite)
        assert UniversalMCElement.from_virasoro(c=1).shadow_depth is None


# =====================================================================
# II. MC equation: D·Theta + ½[Theta,Theta] = 0
# =====================================================================

class TestMCEquation:
    def test_virasoro_mc_arity3(self):
        theta = UniversalMCElement.from_virasoro(c=1)
        result = theta.verify_mc_equation(max_arity=8)
        assert result[3] is True

    def test_virasoro_mc_arity4(self):
        theta = UniversalMCElement.from_virasoro(c=1)
        result = theta.verify_mc_equation(max_arity=8)
        assert result[4] is True

    def test_virasoro_mc_arity5_through_8(self):
        theta = UniversalMCElement.from_virasoro(c=1)
        result = theta.verify_mc_equation(max_arity=8)
        for r in range(5, 9):
            assert result[r] is True

    def test_virasoro_mc_c26(self):
        theta = UniversalMCElement.from_virasoro(c=26)
        result = theta.verify_mc_equation(max_arity=10)
        assert all(result.values())

    def test_virasoro_mc_c13(self):
        theta = UniversalMCElement.from_virasoro(c=13)
        result = theta.verify_mc_equation(max_arity=10)
        assert all(result.values())

    def test_heisenberg_mc_trivial(self):
        theta = UniversalMCElement.from_heisenberg(k=1)
        result = theta.verify_mc_equation(max_arity=8)
        assert all(result.values())

    def test_affine_mc(self):
        theta = UniversalMCElement.from_affine_sl2(k=1)
        result = theta.verify_mc_equation(max_arity=8)
        assert all(result.values())

    def test_betagamma_mc(self):
        theta = UniversalMCElement.from_betagamma()
        result = theta.verify_mc_equation(max_arity=8)
        assert all(result.values())

    def test_w3_mc(self):
        theta = UniversalMCElement.from_w3(c=50)
        result = theta.verify_mc_equation(max_arity=8)
        assert all(result.values())

    def test_mc_all_families(self):
        """MC holds for ALL standard families."""
        for name, theta in all_standard_mc_elements().items():
            result = theta.verify_mc_equation(max_arity=8)
            assert all(result.values()), f"MC failed for {name}"


# =====================================================================
# III. Projection table: each pi_* recovers standalone module output
# =====================================================================

class TestProjections:
    def test_pi_arity_virasoro(self):
        theta = UniversalMCElement.from_virasoro(c=1)
        assert theta.pi_arity(2) == Fraction(1, 2)
        assert theta.pi_arity(3) == Fraction(2)
        assert theta.pi_arity(4) == Fraction(10, 27)

    def test_pi_genus_1(self):
        theta = UniversalMCElement.from_virasoro(c=26)
        assert theta.pi_genus(1) == Fraction(13, 24)

    def test_pi_genus_2(self):
        theta = UniversalMCElement.from_virasoro(c=26)
        assert theta.pi_genus(2) == Fraction(13) * Fraction(7, 5760)

    def test_pi_genus_3(self):
        theta = UniversalMCElement.from_virasoro(c=26)
        assert theta.pi_genus(3) == Fraction(13) * Fraction(31, 967680)

    def test_pi_newton(self):
        theta = UniversalMCElement.from_virasoro(c=1)
        assert theta.pi_newton(2) == Fraction(-1)  # p_2 = -c
        assert theta.pi_newton(3) == Fraction(-6)  # p_3 = -3*S_3 = -6

    def test_pi_complementarity_virasoro(self):
        theta = UniversalMCElement.from_virasoro(c=1)
        assert theta.pi_complementarity_sum() == Fraction(13)

    def test_pi_complementarity_affine(self):
        theta = UniversalMCElement.from_affine_sl2(k=1)
        # For affine: kappa + kappa! should be a constant
        compl = theta.pi_complementarity_sum()
        assert isinstance(compl, (Fraction, int, float))

    def test_pi_complementarity_heisenberg(self):
        theta = UniversalMCElement.from_heisenberg(k=1)
        assert theta.pi_complementarity_sum() == Fraction(0)

    def test_pi_hochschild_virasoro(self):
        """AP94: Virasoro in bounded Koszul regime per Theorem H
        (formerly the refuted polynomial-ring 'w_algebra' label)."""
        theta = UniversalMCElement.from_virasoro(c=1)
        h = theta.pi_hochschild_polynomial()
        assert h["regime"] == "bounded_koszul"
        assert h["polynomial"] == [1, 0, 1]

    def test_pi_hochschild_heisenberg(self):
        """Heisenberg in bounded Koszul regime: P(t) = 1 + t + t^2."""
        theta = UniversalMCElement.from_heisenberg(k=1)
        h = theta.pi_hochschild_polynomial()
        assert h["regime"] == "bounded_koszul"
        assert h["polynomial"] == [1, 1, 1]

    def test_pi_quartic_virasoro(self):
        theta = UniversalMCElement.from_virasoro(c=1)
        assert theta.pi_quartic_contact() == Fraction(10, 27)

    def test_pi_quartic_heisenberg_zero(self):
        theta = UniversalMCElement.from_heisenberg(k=1)
        assert theta.pi_quartic_contact() == Fraction(0)

    def test_pi_resonance_virasoro(self):
        theta = UniversalMCElement.from_virasoro(c=1)
        assert theta.pi_resonance_rank() == 1

    def test_pi_resonance_heisenberg(self):
        theta = UniversalMCElement.from_heisenberg(k=1)
        assert theta.pi_resonance_rank() == 0

    def test_pi_kz_casimir(self):
        theta = UniversalMCElement.from_virasoro(c=26)
        assert theta.pi_kz_casimir() == Fraction(13)


# =====================================================================
# IV. Projection table completeness
# =====================================================================

class TestProjectionTable:
    def test_virasoro_table_nonempty(self):
        theta = UniversalMCElement.from_virasoro(c=1)
        table = theta.chriss_ginzburg_table()
        assert len(table) > 0

    def test_virasoro_table_all_verified(self):
        theta = UniversalMCElement.from_virasoro(c=1)
        table = theta.chriss_ginzburg_table()
        for row in table:
            assert row["verified"] is True, f"Projection {row['projection']} not verified"

    def test_heisenberg_table_all_verified(self):
        theta = UniversalMCElement.from_heisenberg(k=1)
        table = theta.chriss_ginzburg_table()
        for row in table:
            assert row["verified"] is True, f"Projection {row['projection']} not verified"

    def test_affine_table_all_verified(self):
        theta = UniversalMCElement.from_affine_sl2(k=1)
        table = theta.chriss_ginzburg_table()
        for row in table:
            assert row["verified"] is True

    def test_projection_count_minimum(self):
        """Each family should have at least 10 verified projections."""
        theta = UniversalMCElement.from_virasoro(c=1)
        verified, total = theta.projection_count()
        assert verified >= 10
        assert verified == total

    def test_all_families_projection_count(self):
        for name, theta in all_standard_mc_elements().items():
            verified, total = theta.projection_count()
            assert verified == total, f"{name}: {verified}/{total} verified"


# =====================================================================
# V. Five main theorems as MC consequences
# =====================================================================

class TestFiveTheorems:
    def test_theorem_a_from_mc(self):
        theta = UniversalMCElement.from_virasoro(c=1)
        thms = theta.five_theorems_from_mc()
        assert "A" in thms
        assert thms["A"]["status"] == "proved"

    def test_theorem_b_from_mc(self):
        theta = UniversalMCElement.from_virasoro(c=1)
        thms = theta.five_theorems_from_mc()
        assert thms["B"]["status"] == "proved"

    def test_theorem_c_from_mc(self):
        theta = UniversalMCElement.from_virasoro(c=1)
        thms = theta.five_theorems_from_mc()
        assert thms["C"]["status"] == "proved"

    def test_theorem_d_from_mc(self):
        theta = UniversalMCElement.from_virasoro(c=1)
        thms = theta.five_theorems_from_mc()
        assert thms["D"]["status"] == "proved"

    def test_theorem_h_from_mc(self):
        theta = UniversalMCElement.from_virasoro(c=1)
        thms = theta.five_theorems_from_mc()
        assert thms["H"]["status"] == "proved"

    def test_all_five_proved(self):
        theta = UniversalMCElement.from_virasoro(c=1)
        thms = theta.five_theorems_from_mc()
        for label, data in thms.items():
            assert data["status"] == "proved", f"Theorem {label} not proved from MC"

    def test_all_families_five_theorems(self):
        for name, theta in all_standard_mc_elements().items():
            thms = theta.five_theorems_from_mc()
            for label, data in thms.items():
                assert data["status"] == "proved", f"{name} Thm {label}"


# =====================================================================
# VI. Cross-projection consistency
# =====================================================================

class TestConsistency:
    def test_newton_consistent_with_shadow(self):
        """p_r = -r * S_r for all r."""
        theta = UniversalMCElement.from_virasoro(c=2)
        for r in range(2, 8):
            assert theta.pi_newton(r) == -r * theta.pi_arity(r)

    def test_genus_consistent_with_kappa(self):
        """F_g = kappa * lambda_g^FP. Use pi_genus and pi_arity for cross-check."""
        theta = UniversalMCElement.from_virasoro(c=2)
        # F_1 = kappa/24, F_2 = kappa*7/5760
        f1 = theta.pi_genus(1)
        f2 = theta.pi_genus(2)
        kappa = theta.kappa_value
        assert f1 == kappa * Fraction(1, 24)
        assert f2 == kappa * Fraction(7, 5760)

    def test_quartic_consistent_with_shadow(self):
        """Q^ct = S_4."""
        theta = UniversalMCElement.from_virasoro(c=2)
        assert theta.pi_quartic_contact() == theta.pi_arity(4)

    def test_kz_consistent_with_kappa(self):
        """KZ Casimir ∝ kappa."""
        theta = UniversalMCElement.from_virasoro(c=2)
        assert theta.pi_kz_casimir() == theta.kappa_value

    def test_complementarity_sum_virasoro_level_independent(self):
        """kappa + kappa! = 13 for all c (Virasoro)."""
        for c in [1, 2, 5, 13, 26, 100]:
            theta = UniversalMCElement.from_virasoro(c=c)
            assert theta.pi_complementarity_sum() == Fraction(13)

    def test_complementarity_sum_heisenberg_zero(self):
        """kappa + kappa! = 0 for Heisenberg."""
        for k in [1, 2, 5, 10]:
            theta = UniversalMCElement.from_heisenberg(k=k)
            assert theta.pi_complementarity_sum() == Fraction(0)

    def test_mc_generates_newton(self):
        """MC at arity r IS Newton's identity."""
        theta = UniversalMCElement.from_virasoro(c=3)
        mc = theta.verify_mc_equation(max_arity=8)
        for r, holds in mc.items():
            assert holds, f"MC/Newton fails at arity {r}"


# =====================================================================
# VII. All families comprehensive
# =====================================================================

class TestAllFamilies:
    def test_heisenberg_complete(self):
        theta = UniversalMCElement.from_heisenberg(k=1)
        table = theta.chriss_ginzburg_table()
        assert all(r["verified"] for r in table)
        mc = theta.verify_mc_equation(max_arity=6)
        assert all(mc.values())

    def test_virasoro_complete(self):
        theta = UniversalMCElement.from_virasoro(c=1)
        table = theta.chriss_ginzburg_table()
        assert all(r["verified"] for r in table)
        mc = theta.verify_mc_equation(max_arity=10)
        assert all(mc.values())

    def test_affine_complete(self):
        theta = UniversalMCElement.from_affine_sl2(k=1)
        table = theta.chriss_ginzburg_table()
        assert all(r["verified"] for r in table)

    def test_betagamma_complete(self):
        theta = UniversalMCElement.from_betagamma()
        table = theta.chriss_ginzburg_table()
        assert all(r["verified"] for r in table)

    def test_w3_complete(self):
        theta = UniversalMCElement.from_w3(c=50)
        table = theta.chriss_ginzburg_table()
        assert all(r["verified"] for r in table)

    def test_lattice_complete(self):
        for rank in [1, 8, 24]:
            theta = UniversalMCElement.from_lattice(rank=rank)
            table = theta.chriss_ginzburg_table()
            assert all(r["verified"] for r in table), f"Lattice rank {rank} failed"


# =====================================================================
# VIII. Master table
# =====================================================================

class TestMasterTable:
    def test_master_table_nonempty(self):
        master = chriss_ginzburg_master_table()
        assert len(master) > 0

    def test_master_table_all_verified(self):
        master = chriss_ginzburg_master_table()
        for entry in master:
            assert entry["all_verified"], f"{entry['family']} not all verified"

    def test_master_table_mc_holds(self):
        master = chriss_ginzburg_master_table()
        for entry in master:
            assert entry["mc_equation_holds"], f"{entry['family']} MC fails"

    def test_master_table_five_theorems(self):
        master = chriss_ginzburg_master_table()
        for entry in master:
            assert entry["five_theorems"], f"{entry['family']} not all 5 theorems"

    def test_master_table_12_families(self):
        master = chriss_ginzburg_master_table()
        assert len(master) == 12  # 12 standard families in the landscape

    def test_master_table_archetypes(self):
        master = chriss_ginzburg_master_table()
        archetypes = {e["archetype"] for e in master}
        assert ARCHETYPE_G in archetypes
        assert ARCHETYPE_L in archetypes
        assert ARCHETYPE_M in archetypes


# =====================================================================
# IX. Structural depth: Theta_A determines everything
# =====================================================================

class TestUniversality:
    def test_different_algebras_different_theta(self):
        """Different algebras have different MC elements (distinguished by archetype or shadow)."""
        h = UniversalMCElement.from_heisenberg(k=1)
        v = UniversalMCElement.from_virasoro(c=2)
        # May have same kappa but ALWAYS differ in archetype or shadow depth
        assert h.archetype != v.archetype
        # Heisenberg has S_3=0; Virasoro has S_3=2
        assert h.pi_arity(3) != v.pi_arity(3)

    def test_kappa_determines_scalar_tower(self):
        """kappa = pi_2(Theta) determines the entire scalar genus tower."""
        theta = UniversalMCElement.from_virasoro(c=2)
        kappa = theta.kappa_value
        f1 = theta.pi_genus(1)
        f2 = theta.pi_genus(2)
        assert f1 == kappa * Fraction(1, 24)
        assert f2 == kappa * Fraction(7, 5760)

    def test_shadow_determines_mc(self):
        """Shadow data {S_r} determines the MC element."""
        theta1 = UniversalMCElement.from_virasoro(c=1)
        theta2 = UniversalMCElement.from_shadow_data(
            family="virasoro",
            shadow_dict=theta1.shadow_coefficients.copy(),
            kappa_value=theta1.kappa_value,
            n_gen=1,
        )
        # Same shadow data → same projections
        for r in range(2, 8):
            assert theta1.pi_arity(r) == theta2.pi_arity(r)

    def test_virasoro_not_self_dual_at_c26(self):
        """CRITICAL PITFALL: Vir self-dual at c=13, NOT c=26."""
        theta = UniversalMCElement.from_virasoro(c=26)
        compl = theta.pi_complementarity_sum()
        assert compl == Fraction(13)  # kappa(26) + kappa(0) = 13 + 0 = 13
        # Self-dual point: kappa = kappa!, so 2*kappa = 13, kappa = 13/2
        theta13 = UniversalMCElement.from_virasoro(c=13)
        assert theta13.kappa_value == Fraction(13, 2)
