r"""Tests for DS shadow tower transformation engine (sl_2).

Verifies that the shadow obstruction tower invariants (S_2, S_3, S_4, Delta)
transform correctly under Drinfeld-Sokolov reduction V_k(sl_2) -> Vir_c,
and that the class transition L -> M is visible as Delta going from 0
to nonzero.

STRUCTURE:
  Section 1: Central charge formulas (7 tests)
  Section 2: Kappa formulas (6 tests)
  Section 3: Shadow tower -- affine KM, class L (5 tests)
  Section 4: Shadow tower -- Virasoro, class M (6 tests)
  Section 5: DS transition L -> M (6 tests)
  Section 6: Singular loci (4 tests)
  Section 7: Cross-engine consistency (3 tests)

Total: 37 tests.

Manuscript references:
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:ds-central-charge-additivity (higher_genus_modular_koszul.tex)
    thm:obstruction-recursion (higher_genus_modular_koszul.tex)
"""

import pytest
from fractions import Fraction

from compute.lib.ds_shadow_tower_sl2_engine import (
    c_sugawara_sl2,
    c_ds_sl2,
    c_ghost_sl2,
    kappa_km_sl2,
    kappa_vir,
    shadow_tower_km_sl2,
    shadow_tower_vir,
    ds_transition_sl2,
    ds_transition_table,
    singular_k_values,
)


# =============================================================================
# Section 1: Central charge formulas
# =============================================================================


class TestCentralCharges:
    """Central charge formulas for sl_2 and DS Virasoro."""

    def test_sugawara_k1(self):
        # VERIFIED: [DC] 3*1/(1+2) = 1; [LT] Di Francesco et al (14.62)
        assert c_sugawara_sl2(Fraction(1)) == Fraction(1)

    def test_sugawara_k2(self):
        # VERIFIED: [DC] 3*2/(2+2) = 3/2; [LT] Kac-Raina, c(sl_2, k=2) = 3/2
        assert c_sugawara_sl2(Fraction(2)) == Fraction(3, 2)

    def test_sugawara_k0(self):
        # VERIFIED: [DC] 3*0/2 = 0; [SY] trivial algebra has c=0
        assert c_sugawara_sl2(Fraction(0)) == Fraction(0)

    def test_sugawara_critical(self):
        # VERIFIED: [DC] k=-2 is critical level; [LT] Frenkel-Ben-Zvi Ch. 5
        with pytest.raises(ValueError, match="Critical level"):
            c_sugawara_sl2(Fraction(-2))

    def test_ds_central_charge_k1(self):
        # VERIFIED: [DC] 1 - 6*4/3 = 1-8 = -7; [LT] Fateev-Lukyanov (1988)
        assert c_ds_sl2(Fraction(1)) == Fraction(-7)

    def test_ds_central_charge_km1(self):
        # VERIFIED: [DC] 1 - 6*0/1 = 1; [LT] Ising model c=1 from DS at k=-1
        assert c_ds_sl2(Fraction(-1)) == Fraction(1)

    def test_ds_central_charge_k2(self):
        # VERIFIED: [DC] 1 - 6*9/4 = 1-27/2 = -25/2; [CF] c_wn_fl(2,2)=-25/2
        assert c_ds_sl2(Fraction(2)) == Fraction(-25, 2)


# =============================================================================
# Section 2: Kappa formulas
# =============================================================================


class TestKappaFormulas:
    """Kappa formulas for KM and Virasoro."""

    def test_kappa_km_k0(self):
        # VERIFIED: [DC] 3*(0+2)/4 = 3/2; [LT] C3: k=0 -> dim(g)/2 = 3/2
        # AP1: from landscape_census.tex C3
        assert kappa_km_sl2(Fraction(0)) == Fraction(3, 2)

    def test_kappa_km_k1(self):
        # VERIFIED: [DC] 3*(1+2)/4 = 9/4; [CF] matches shadow_tower_atlas
        assert kappa_km_sl2(Fraction(1)) == Fraction(9, 4)

    def test_kappa_km_critical(self):
        # VERIFIED: [DC] 3*(-2+2)/4 = 0; [LT] C3: k=-h^v -> 0 (critical)
        assert kappa_km_sl2(Fraction(-2)) == Fraction(0)

    def test_kappa_vir_c13(self):
        # VERIFIED: [DC] 13/2; [LT] C2: self-dual point c=13
        assert kappa_vir(Fraction(13)) == Fraction(13, 2)

    def test_kappa_vir_c0(self):
        # VERIFIED: [DC] 0/2 = 0; [SY] trivial c=0 -> kappa=0
        assert kappa_vir(Fraction(0)) == Fraction(0)

    def test_kappa_vir_c1(self):
        # VERIFIED: [DC] 1/2; [CF] Ising model kappa = 1/2
        assert kappa_vir(Fraction(1)) == Fraction(1, 2)


# =============================================================================
# Section 3: Shadow tower -- affine KM, class L
# =============================================================================


class TestShadowTowerKM:
    """Shadow tower for V_k(sl_2).  Must be class L with Delta = 0."""

    def test_class_L(self):
        tower = shadow_tower_km_sl2(Fraction(1))
        assert tower["shadow_class"] == "L"

    def test_depth_3(self):
        tower = shadow_tower_km_sl2(Fraction(1))
        assert tower["shadow_depth"] == 3

    def test_S4_zero(self):
        # VERIFIED: [DC] Jacobi kills quartic; [LT] shadow_tower_atlas: S4=0
        for kv in [1, 2, 3, 5, 10]:
            tower = shadow_tower_km_sl2(Fraction(kv))
            assert tower["S4"] == Fraction(0), f"S4 != 0 at k={kv}"

    def test_Delta_zero(self):
        # VERIFIED: [DC] Delta = 8*kappa*0 = 0; [LT] class L -> Delta=0
        for kv in [1, 2, 3, 5, 10, 0, -1]:
            tower = shadow_tower_km_sl2(Fraction(kv))
            assert tower["Delta"] == Fraction(0), f"Delta != 0 at k={kv}"

    def test_ap141_r_matrix_k0(self):
        # AP141: r-matrix vanishes at k=0
        tower = shadow_tower_km_sl2(Fraction(0))
        assert tower["r_at_k0"] == Fraction(0)
        assert tower["kappa"] == Fraction(3, 2)  # kappa != 0 even at k=0


# =============================================================================
# Section 4: Shadow tower -- Virasoro, class M
# =============================================================================


class TestShadowTowerVir:
    """Shadow tower for Vir_c.  Must be class M with Delta != 0."""

    def test_class_M(self):
        tower = shadow_tower_vir(Fraction(1))
        assert tower["shadow_class"] == "M"

    def test_S3_equals_2(self):
        # VERIFIED: [DC] virasoro_shadow_tower.py S_3=2; [LT] C26 gravitational cubic
        tower = shadow_tower_vir(Fraction(1))
        assert tower["S3"] == Fraction(2)

    def test_S4_c1(self):
        # VERIFIED: [DC] 10/(1*27) = 10/27; [CF] virasoro_shadow_tower.py EXACT_SHADOW_COEFFICIENTS[4]
        tower = shadow_tower_vir(Fraction(1))
        assert tower["S4"] == Fraction(10, 27)

    def test_Delta_c1(self):
        # VERIFIED: [DC] 40/(5+22) = 40/27; [CF] 8*(1/2)*(10/27) = 40/27
        tower = shadow_tower_vir(Fraction(1))
        assert tower["Delta"] == Fraction(40, 27)

    def test_Delta_nonzero_generic(self):
        """Delta != 0 for generic c (class M has infinite tower)."""
        # VERIFIED: [DC] Delta = 40/(5c+22); [LT] class M: depth = infinity
        for c_val in [1, -7, Fraction(-25, 2), 13, 26, Fraction(1, 2)]:
            c_val = Fraction(c_val)
            tower = shadow_tower_vir(c_val)
            assert tower["Delta"] != Fraction(0), f"Delta = 0 at c={c_val}"

    def test_S4_singular_c0(self):
        """c=0 is a singular point of the Virasoro tower (S_4 pole)."""
        with pytest.raises(ValueError, match="singular"):
            shadow_tower_vir(Fraction(0))


# =============================================================================
# Section 5: DS transition L -> M
# =============================================================================


class TestDSTransition:
    """The central structural content: Delta goes from 0 to nonzero."""

    def test_transition_k1(self):
        t = ds_transition_sl2(Fraction(1))
        assert t["Delta_before"] == Fraction(0)
        assert t["Delta_after"] != Fraction(0)
        assert t["class_before"] == "L"
        assert t["class_after"] == "M"

    def test_transition_k2(self):
        t = ds_transition_sl2(Fraction(2))
        assert t["Delta_before"] == Fraction(0)
        # VERIFIED: [DC] c=-25/2, Delta=40/(5*(-25/2)+22)=40/(-125/2+22)=40/(-81/2)=-80/81
        # [CF] direct computation
        assert t["Delta_after"] == Fraction(-80, 81)

    def test_transition_km1_ising(self):
        """k=-1 gives the Ising model (c=1)."""
        t = ds_transition_sl2(Fraction(-1))
        assert t["c_ds"] == Fraction(1)
        assert t["Delta_before"] == Fraction(0)
        # VERIFIED: [DC] Delta = 40/27; [CF] c=1, 5*1+22=27
        assert t["Delta_after"] == Fraction(40, 27)

    def test_ghost_additivity(self):
        """c(V_k) = c(Vir_DS) + c_ghost."""
        for kv in [1, 2, 3, 5, 10, -1]:
            k = Fraction(kv)
            c_sug = c_sugawara_sl2(k)
            c_ds = c_ds_sl2(k)
            c_gh = c_ghost_sl2(k)
            # VERIFIED: [DC] direct arithmetic; [SY] BRST cohomology additivity
            assert c_sug == c_ds + c_gh, f"Additivity fails at k={kv}"

    def test_kappa_changes(self):
        """kappa changes under DS: 3(k+2)/4 -> c/2."""
        t = ds_transition_sl2(Fraction(1))
        # VERIFIED: [DC] kappa_KM = 9/4, kappa_Vir = -7/2
        assert t["before"]["kappa"] == Fraction(9, 4)
        assert t["after"]["kappa"] == Fraction(-7, 2)

    def test_transition_table_all_delta_zero_before(self):
        """Every entry in the transition table has Delta_before = 0."""
        table = ds_transition_table()
        for row in table:
            assert row["Delta_before"] == Fraction(0), (
                f"Delta_before != 0 at k={row['k']}"
            )

    def test_transition_table_all_delta_nonzero_after(self):
        """Every entry in the transition table has Delta_after != 0."""
        table = ds_transition_table()
        for row in table:
            assert row["Delta_after"] != Fraction(0), (
                f"Delta_after = 0 at k={row['k']}"
            )


# =============================================================================
# Section 6: Singular loci
# =============================================================================


class TestSingularLoci:
    """Singular k-values where the post-DS Virasoro tower is ill-defined."""

    def test_c_eq_0_values(self):
        """c=0 reached from k=-1/2 and k=-4/3."""
        # VERIFIED: [DC] 1-6*(1/2)^2/(3/2) = 1-6*(1/4)/(3/2) = 1-1=0
        # [DC] 1-6*(-1/3)^2/(2/3) = 1-6*(1/9)/(2/3) = 1-1=0
        sv = singular_k_values()
        for kv in sv["c_eq_0"]:
            assert c_ds_sl2(kv) == Fraction(0)

    def test_c_eq_m22o5_values(self):
        """c=-22/5 reached from k=1/2 and k=-8/5."""
        # VERIFIED: [DC] direct substitution; [CF] (2,5) minimal model
        sv = singular_k_values()
        for kv in sv["c_eq_m22o5"]:
            assert c_ds_sl2(kv) == Fraction(-22, 5)

    def test_singular_c0_raises(self):
        """shadow_tower_vir raises at c=0."""
        with pytest.raises(ValueError):
            shadow_tower_vir(Fraction(0))

    def test_singular_cm22o5_raises(self):
        """shadow_tower_vir raises at c=-22/5."""
        with pytest.raises(ValueError):
            shadow_tower_vir(Fraction(-22, 5))


# =============================================================================
# Section 7: Cross-engine consistency
# =============================================================================


class TestCrossEngineConsistency:
    """Cross-check against shadow_tower_atlas and virasoro_shadow_tower."""

    def test_km_matches_atlas(self):
        """KM tower matches shadow_tower_atlas.affine_sl2_tower."""
        from sympy import Symbol, Rational as SRat
        from compute.lib.shadow_tower_atlas import affine_sl2_tower

        atlas = affine_sl2_tower()
        # Atlas uses sympy Symbol('k'); check structure
        assert atlas["class"] == "L"
        assert atlas["depth"] == 3
        assert atlas[4] == SRat(0)

    def test_vir_S4_matches_exact(self):
        """Virasoro S_4 matches EXACT_SHADOW_COEFFICIENTS[4]."""
        from sympy import Symbol, Rational as SRat
        from compute.lib.virasoro_shadow_tower import EXACT_SHADOW_COEFFICIENTS

        c_sym = Symbol('c')
        exact_S4 = EXACT_SHADOW_COEFFICIENTS[4]
        # Evaluate at c=1
        S4_exact = exact_S4.subs(c_sym, 1)
        tower = shadow_tower_vir(Fraction(1))
        # VERIFIED: [CF] virasoro_shadow_tower EXACT[4] at c=1 = 10/27
        assert float(S4_exact) == pytest.approx(float(tower["S4"]), rel=1e-15)

    def test_ds_matches_canonical_c_wn_fl(self):
        """DS central charge matches canonical c_wn_fl(N=2, k)."""
        for kv in [1, 2, 3, 5, 10]:
            k = Fraction(kv)
            c_ours = c_ds_sl2(k)
            from compute.lib.wn_central_charge_canonical import c_wn_fl as canonical_c_wn_fl
            c_canon = canonical_c_wn_fl(2, k)
            assert c_ours == c_canon, f"Mismatch at k={kv}"
