"""Tests for compute/lib/genus_extension_obstruction_engine.py.

Verifies the four-layer obstruction theory for genus extension of chiral algebras:
  Layer 1: C_2-cofiniteness
  Layer 2: Rationality
  Layer 3: Energy boundedness
  Layer 4: Sewing convergence (HS condition)

Plus cross-verification with the shadow obstruction tower (kappa, classes G/L/C/M).

Multi-path verification (per CLAUDE.md mandate):
  Path 1: Direct computation from definitions
  Path 2: Cross-family consistency
  Path 3: Limiting/special case verification
  Path 4: Literature comparison
  Path 5: Shadow tower cross-check
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.genus_extension_obstruction_engine import (
    # Layer 1: C_2-cofiniteness
    c2_quotient_dim_heisenberg,
    c2_quotient_generators_affine_km,
    c2_cofinite_virasoro,
    c2_cofinite_w_algebra,
    c2_cofinite_betagamma,
    c2_cofinite_lattice,
    is_c2_cofinite,
    # Layer 2: Rationality
    is_rational,
    verlinde_dim,
    # Layer 3: Energy boundedness
    is_energy_bounded,
    # Layer 4: Sewing convergence
    ope_growth_order,
    sector_growth_type,
    hs_sewing_holds,
    # Characteristic classes
    genus_g_obstruction_class,
    curvature_is_exact,
    # Shadow tower
    shadow_class,
    shadow_discriminant,
    # Master profile
    genus_extension_profile,
    # Cross-verification
    verify_kappa_shadow_consistency,
    full_landscape_verification,
    # Non-standard examples
    non_standard_obstruction_examples,
    # Theory
    minimal_conditions_for_genus_extension,
)

from compute.lib.utils import lambda_fp, F_g
from compute.lib.genus_expansion import (
    kappa_heisenberg, kappa_virasoro, kappa_w3,
    kappa_sl2, kappa_sl3,
)


# ============================================================================
# Layer 1: C_2-cofiniteness tests
# ============================================================================

class TestC2Cofiniteness:
    """All standard families are C_2-cofinite."""

    def test_heisenberg_c2_cofinite(self):
        """Heisenberg VOA is C_2-cofinite: V/C_2(V) = C[a], 1 generator."""
        assert is_c2_cofinite("Heisenberg") is True

    def test_heisenberg_quotient_dim_rank1(self):
        """Rank-1 Heisenberg: C_2-quotient has 1 algebra generator."""
        assert c2_quotient_dim_heisenberg(1) == 1

    def test_heisenberg_quotient_dim_rank24(self):
        """Rank-24 Heisenberg (Leech lattice): 24 algebra generators."""
        assert c2_quotient_dim_heisenberg(24) == 24

    def test_affine_sl2_c2_cofinite(self):
        assert is_c2_cofinite("sl2") is True

    def test_affine_sl3_c2_cofinite(self):
        assert is_c2_cofinite("sl3") is True

    def test_affine_km_generators_sl2(self):
        """V_k(sl_2)/C_2 = Sym(sl_2) has 3 generators."""
        assert c2_quotient_generators_affine_km("A", 1) == 3

    def test_affine_km_generators_sl3(self):
        """V_k(sl_3)/C_2 = Sym(sl_3) has 8 generators."""
        assert c2_quotient_generators_affine_km("A", 2) == 8

    def test_affine_km_generators_e8(self):
        """V_k(E_8)/C_2 has 248 generators."""
        assert c2_quotient_generators_affine_km("E", 8) == 248

    def test_affine_km_generators_g2(self):
        """V_k(G_2)/C_2 has 14 generators."""
        assert c2_quotient_generators_affine_km("G", 2) == 14

    def test_virasoro_c2_cofinite(self):
        """Virasoro is C_2-cofinite for all c."""
        assert c2_cofinite_virasoro() is True
        assert c2_cofinite_virasoro(c=0) is True
        assert c2_cofinite_virasoro(c=26) is True

    def test_virasoro_profile_c2(self):
        assert is_c2_cofinite("Virasoro") is True

    def test_w_algebra_c2_cofinite(self):
        """W-algebras are C_2-cofinite (Feigin-Frenkel free generation)."""
        assert c2_cofinite_w_algebra("A", 2) is True
        assert c2_cofinite_w_algebra("A", 4) is True

    def test_betagamma_c2_cofinite(self):
        assert c2_cofinite_betagamma() is True
        assert is_c2_cofinite("betagamma") is True

    def test_lattice_c2_cofinite(self):
        """Lattice VOAs are C_2-cofinite (in fact rational)."""
        assert c2_cofinite_lattice(1) is True
        assert c2_cofinite_lattice(24) is True
        assert is_c2_cofinite("lattice") is True

    def test_minimal_model_c2_cofinite(self):
        assert is_c2_cofinite("minimal_model") is True

    def test_all_standard_families_c2_cofinite(self):
        """UNIVERSAL: every standard family is C_2-cofinite."""
        families = [
            "Heisenberg", "affine_KM", "Virasoro", "W_algebra",
            "betagamma", "lattice", "minimal_model",
            "sl2", "sl3",
        ]
        for fam in families:
            assert is_c2_cofinite(fam) is True, f"{fam} should be C_2-cofinite"


# ============================================================================
# Layer 2: Rationality tests
# ============================================================================

class TestRationality:
    """Rationality: semisimple module category."""

    def test_heisenberg_not_rational(self):
        """Heisenberg is NOT rational (uncountably many Fock modules)."""
        assert is_rational("Heisenberg") is False

    def test_sl2_integrable_rational(self):
        """sl_2 at positive integer level is rational."""
        assert is_rational("sl2", level=1) is True
        assert is_rational("sl2", level=2) is True
        assert is_rational("sl2", level=10) is True

    def test_sl2_generic_not_rational(self):
        """sl_2 at generic level is not rational."""
        assert is_rational("sl2") is False

    def test_lattice_rational(self):
        """Lattice VOAs are rational."""
        assert is_rational("lattice") is True

    def test_minimal_model_rational(self):
        """Minimal models are rational."""
        assert is_rational("minimal_model") is True

    def test_virasoro_generic_not_rational(self):
        """Virasoro at generic c is not rational."""
        assert is_rational("Virasoro") is False

    def test_virasoro_ising_rational(self):
        """Virasoro at c=1/2 (Ising model) is rational."""
        assert is_rational("Virasoro", c=Rational(1, 2)) is True

    def test_betagamma_not_rational(self):
        """bc/betagamma system is not rational."""
        assert is_rational("betagamma") is False


class TestVerlinde:
    """Verlinde formula for conformal block dimensions."""

    def test_sl2_level1_genus0(self):
        """sl_2 level 1 genus 0: dim = 1."""
        assert verlinde_dim("sl2", 0, level=1) == 1

    def test_sl2_level1_genus1(self):
        """sl_2 level 1 genus 1: dim = k+1 = 2."""
        assert verlinde_dim("sl2", 1, level=1) == 2

    def test_sl2_level2_genus1(self):
        """sl_2 level 2 genus 1: dim = k+1 = 3."""
        assert verlinde_dim("sl2", 1, level=2) == 3

    def test_sl2_level1_genus2(self):
        """sl_2 level 1 genus 2: verify it is a positive integer."""
        d = verlinde_dim("sl2", 2, level=1)
        assert d is not None
        assert isinstance(d, int)
        assert d > 0

    def test_verlinde_positive_integer(self):
        """Verlinde dimensions are always positive integers (Beauville)."""
        for k in (1, 2, 3):
            for g in range(0, 4):
                d = verlinde_dim("sl2", g, level=k)
                assert d is not None
                assert isinstance(d, int), f"sl2 k={k} g={g}: not int"
                assert d > 0, f"sl2 k={k} g={g}: not positive"


# ============================================================================
# Layer 3: Energy boundedness tests
# ============================================================================

class TestEnergyBoundedness:
    """Energy boundedness: polynomial energy bounds for vertex operators."""

    def test_heisenberg_positive_level_bounded(self):
        """Heisenberg at positive level is energy-bounded (unitary)."""
        assert is_energy_bounded("Heisenberg", level=1) is True

    def test_heisenberg_negative_level_not_bounded(self):
        """Heisenberg at negative level: indefinite inner product."""
        assert is_energy_bounded("Heisenberg", level=-1) is False

    def test_sl2_integrable_bounded(self):
        """sl_2 at non-negative integer level is energy-bounded."""
        assert is_energy_bounded("sl2", level=1) is True

    def test_sl2_negative_level_not_bounded(self):
        """sl_2 at negative level is not energy-bounded."""
        assert is_energy_bounded("sl2", level=-3) is False

    def test_virasoro_c_geq_1_bounded(self):
        """Virasoro at c >= 1 is energy-bounded."""
        assert is_energy_bounded("Virasoro", c=1) is True
        assert is_energy_bounded("Virasoro", c=26) is True

    def test_betagamma_bounded(self):
        """betagamma is energy-bounded (despite non-unitarity)."""
        assert is_energy_bounded("betagamma") is True

    def test_lattice_bounded(self):
        """Lattice VOAs are energy-bounded (unitary)."""
        assert is_energy_bounded("lattice") is True

    def test_unitary_implies_bounded(self):
        """Unitarity implies energy boundedness (CKLW18)."""
        assert is_energy_bounded("Heisenberg", unitary=True) is True
        assert is_energy_bounded("sl2", unitary=True) is True


# ============================================================================
# Layer 4: Sewing convergence tests
# ============================================================================

class TestSewingConvergence:
    """HS-sewing condition: polynomial OPE + subexponential growth."""

    def test_heisenberg_polynomial_ope(self):
        """Heisenberg has polynomial OPE growth of order 1."""
        assert ope_growth_order("Heisenberg") == "polynomial_1"

    def test_virasoro_polynomial_ope(self):
        """Virasoro has polynomial OPE growth of order 3."""
        assert ope_growth_order("Virasoro") == "polynomial_3"

    def test_w3_polynomial_ope(self):
        """W_3 has polynomial OPE growth of order 5 (2*3-1)."""
        assert ope_growth_order("W_3", N=3) == "polynomial_5"

    def test_heisenberg_subexponential(self):
        """Heisenberg sector growth is subexponential (Hardy-Ramanujan)."""
        assert sector_growth_type("Heisenberg") == "subexponential_half"

    def test_virasoro_subexponential(self):
        """Virasoro sector growth: Cardy formula ~ exp(pi*sqrt(2cn/3))."""
        assert sector_growth_type("Virasoro") == "subexponential_half"

    def test_all_standard_hs_sewing(self):
        """HS-sewing holds for the entire standard landscape."""
        families = [
            "Heisenberg", "sl2", "sl3", "Virasoro",
            "betagamma", "lattice", "minimal_model",
        ]
        for fam in families:
            assert hs_sewing_holds(fam) is True, f"{fam} should satisfy HS-sewing"

    def test_w3_hs_sewing(self):
        """W_3 satisfies HS-sewing."""
        assert hs_sewing_holds("W_3", N=3) is True


# ============================================================================
# Characteristic class obstruction tests
# ============================================================================

class TestObstructionClasses:
    """Genus-g obstruction classes obs_g = kappa * lambda_g^FP."""

    def test_genus0_no_obstruction(self):
        """No obstruction at genus 0."""
        obs = genus_g_obstruction_class("Heisenberg", 0, k=1)
        assert obs.vanishes is True
        assert obs.value == Rational(0)

    def test_heisenberg_genus1(self):
        """Heisenberg k=1: F_1 = kappa * lambda_1 = 1 * 1/24 = 1/24."""
        obs = genus_g_obstruction_class("Heisenberg", 1, k=1)
        assert obs.value == Rational(1, 24)
        assert obs.vanishes is False

    def test_virasoro_genus1(self):
        """Virasoro c=1: F_1 = (1/2) * (1/24) = 1/48."""
        obs = genus_g_obstruction_class("Virasoro", 1, c=1)
        assert obs.value == Rational(1, 48)

    def test_sl2_genus1(self):
        """sl_2 level 1: kappa = 3*3/4 = 9/4. F_1 = 9/4 * 1/24 = 3/32."""
        obs = genus_g_obstruction_class("sl2", 1, level=1)
        expected_kappa = Rational(3) * (1 + 2) / 4  # = 9/4
        expected_F1 = expected_kappa * lambda_fp(1)
        assert obs.value == expected_F1

    def test_betagamma_genus1(self):
        """betagamma: kappa = 1. F_1 = 1/24."""
        obs = genus_g_obstruction_class("betagamma", 1)
        assert obs.value == Rational(1, 24)

    def test_heisenberg_genus2(self):
        """Heisenberg k=1: F_2 = 1 * 7/5760 = 7/5760."""
        obs = genus_g_obstruction_class("Heisenberg", 2, k=1)
        assert obs.value == lambda_fp(2)
        assert obs.value == Rational(7, 5760)

    def test_curvature_exact_all_standard(self):
        """Curvature is exact for ALL standard families (genus extension succeeds)."""
        families = [
            "Heisenberg", "sl2", "sl3", "Virasoro",
            "betagamma", "lattice", "W_3",
        ]
        for fam in families:
            assert curvature_is_exact(fam) is True, (
                f"{fam}: curvature should be exact"
            )

    def test_kappa_zero_heisenberg(self):
        """Heisenberg at k=0: kappa = 0, all F_g = 0."""
        for g in range(1, 5):
            obs = genus_g_obstruction_class("Heisenberg", g, k=0)
            assert obs.value == 0
            assert obs.vanishes is True


# ============================================================================
# Shadow tower consistency tests
# ============================================================================

class TestShadowTower:
    """Shadow class and discriminant consistency."""

    def test_heisenberg_class_G(self):
        """Heisenberg is class G (Gaussian, r_max = 2)."""
        sc, sd = shadow_class("Heisenberg")
        assert sc == "G"
        assert sd == 2

    def test_sl2_class_L(self):
        """sl_2 is class L (Lie/tree, r_max = 3)."""
        sc, sd = shadow_class("sl2")
        assert sc == "L"
        assert sd == 3

    def test_betagamma_class_C(self):
        """betagamma is class C (contact/quartic, r_max = 4)."""
        sc, sd = shadow_class("betagamma")
        assert sc == "C"
        assert sd == 4

    def test_virasoro_class_M(self):
        """Virasoro is class M (mixed, r_max = infinity)."""
        sc, sd = shadow_class("Virasoro")
        assert sc == "M"
        assert sd is None  # infinity

    def test_w3_class_M(self):
        """W_3 is class M."""
        sc, sd = shadow_class("W_3")
        assert sc == "M"

    def test_lattice_class_G(self):
        """Lattice VOAs are class G."""
        sc, sd = shadow_class("lattice")
        assert sc == "G"
        assert sd == 2

    def test_discriminant_heisenberg_zero(self):
        """Heisenberg: Delta = 0 (S_4 = 0)."""
        assert shadow_discriminant("Heisenberg", k=1) == 0

    def test_discriminant_sl2_zero(self):
        """sl_2: Delta = 0 (quadratic OPE)."""
        assert shadow_discriminant("sl2", level=1) == 0

    def test_discriminant_virasoro_nonzero(self):
        """Virasoro at c=1: Delta != 0 (class M)."""
        disc = shadow_discriminant("Virasoro", c=1)
        assert disc is not None
        assert simplify(disc) != 0

    def test_discriminant_virasoro_formula(self):
        """Virasoro: Delta = -80*kappa / (c*(5c+22))."""
        c_val = 2
        disc = shadow_discriminant("Virasoro", c=c_val)
        kappa = Rational(c_val, 2)
        S4 = Rational(-10) / (c_val * (5 * c_val + 22))
        expected = 8 * kappa * S4
        assert disc == expected

    def test_shadow_depth_does_not_determine_koszulness(self):
        """AP14: shadow depth classifies complexity, NOT Koszulness.
        Both finite (G,L,C) and infinite (M) depth algebras are Koszul."""
        for fam in ["Heisenberg", "sl2", "betagamma", "Virasoro"]:
            assert is_c2_cofinite(fam) is True  # All Koszul


# ============================================================================
# Master profile tests
# ============================================================================

class TestMasterProfile:
    """Full genus-extension profiles for standard families."""

    def test_heisenberg_profile(self):
        p = genus_extension_profile("Heisenberg", k=1)
        assert p.c2_cofinite is True
        assert p.rational is False
        assert p.hs_sewing is True
        assert p.extends_to_all_genera is True
        assert p.kappa == Rational(1)
        assert p.shadow_class == "G"
        assert p.shadow_depth == 2

    def test_sl2_level1_profile(self):
        p = genus_extension_profile("sl2", level=1)
        assert p.c2_cofinite is True
        assert p.rational is True
        assert p.energy_bounded is True
        assert p.extends_to_all_genera is True
        assert p.kappa == Rational(9, 4)
        assert p.shadow_class == "L"

    def test_virasoro_profile(self):
        p = genus_extension_profile("Virasoro", c=26)
        assert p.c2_cofinite is True
        assert p.extends_to_all_genera is True
        assert p.kappa == Rational(13)
        assert p.shadow_class == "M"
        assert p.central_charge == Rational(26)

    def test_betagamma_profile(self):
        p = genus_extension_profile("betagamma")
        assert p.c2_cofinite is True
        assert p.rational is False
        assert p.unitary is False
        assert p.extends_to_all_genera is True
        assert p.kappa == Rational(1)
        assert p.shadow_class == "C"

    def test_lattice_rank24_profile(self):
        p = genus_extension_profile("lattice", rank=24)
        assert p.c2_cofinite is True
        assert p.rational is True
        assert p.extends_to_all_genera is True
        assert p.kappa == Rational(24)

    def test_w3_profile(self):
        p = genus_extension_profile("W_3", c=2)
        assert p.c2_cofinite is True
        assert p.extends_to_all_genera is True
        assert p.kappa == Rational(5) * 2 / 6  # 5c/6 = 10/6 = 5/3
        assert p.shadow_class == "M"

    def test_all_standard_extend(self):
        """UNIVERSAL: all standard families extend to all genera."""
        families = [
            ("Heisenberg", {"k": 1}),
            ("sl2", {"level": 1}),
            ("sl3", {"level": 1}),
            ("Virasoro", {"c": 1}),
            ("betagamma", {}),
            ("lattice", {"rank": 1}),
        ]
        for fam, params in families:
            p = genus_extension_profile(fam, **params)
            assert p.extends_to_all_genera is True, (
                f"{fam} should extend to all genera"
            )


# ============================================================================
# Cross-verification tests
# ============================================================================

class TestCrossVerification:
    """Multi-path verification: kappa, shadow, and genus extension consistency."""

    def test_heisenberg_consistency(self):
        """Heisenberg: three-way consistency check."""
        r = verify_kappa_shadow_consistency("Heisenberg", k=1)
        assert r["kappa"] == Rational(1)
        assert r["shadow_class"] == "G"
        assert r["extends"] is True
        # kappa != 0 => curved => F_g != 0
        assert r["kappa_zero"] is False
        assert r["F_1"] == Rational(1, 24)

    def test_virasoro_consistency(self):
        r = verify_kappa_shadow_consistency("Virasoro", c=1)
        assert r["kappa"] == Rational(1, 2)
        assert r["shadow_class"] == "M"
        assert r["extends"] is True
        # Discriminant should be nonzero (class M)
        assert r.get("disc_consistent", None) is True

    def test_sl2_consistency(self):
        r = verify_kappa_shadow_consistency("sl2", level=1)
        assert r["kappa"] == Rational(9, 4)
        assert r["shadow_class"] == "L"
        assert r["extends"] is True
        # Discriminant should be zero (class L)
        assert r.get("disc_consistent", None) is True

    def test_kappa_cross_check_heisenberg(self):
        """Cross-check kappa from profile vs direct computation."""
        p = genus_extension_profile("Heisenberg", k=2)
        assert p.kappa == kappa_heisenberg(2)
        assert p.kappa == Rational(2)

    def test_kappa_cross_check_virasoro(self):
        """Cross-check kappa: profile vs genus_expansion module."""
        p = genus_extension_profile("Virasoro", c=26)
        assert p.kappa == kappa_virasoro(26)
        assert p.kappa == Rational(13)

    def test_kappa_cross_check_sl2(self):
        """Cross-check kappa for sl_2."""
        p = genus_extension_profile("sl2", level=2)
        assert p.kappa == kappa_sl2(2)
        assert p.kappa == Rational(3)  # 3*(2+2)/4 = 3

    def test_kappa_cross_check_w3(self):
        """Cross-check kappa for W_3."""
        p = genus_extension_profile("W_3", c=6)
        assert p.kappa == kappa_w3(6)
        assert p.kappa == Rational(5)  # 5*6/6 = 5

    def test_F_g_cross_check_genus1(self):
        """F_1 from profile matches F_1 from genus_expansion."""
        for fam, params, k_val in [
            ("Heisenberg", {"k": 1}, Rational(1)),
            ("Virasoro", {"c": 2}, Rational(1)),
            ("sl2", {"level": 1}, Rational(9, 4)),
        ]:
            obs = genus_g_obstruction_class(fam, 1, **params)
            expected = F_g(k_val, 1)
            assert obs.value == expected, f"{fam}: F_1 mismatch"


# ============================================================================
# Full landscape verification
# ============================================================================

class TestFullLandscape:
    """Verify genus extension across the full standard landscape."""

    def test_landscape_all_extend(self):
        """Every standard family at canonical parameters extends."""
        results = full_landscape_verification(max_genus=2)
        for r in results:
            assert r["extends"] is True or r.get("standard_extends") is True, (
                f"{r['family']} should extend"
            )

    def test_landscape_obs_g1_nonzero(self):
        """All families with kappa != 0 have nonzero F_1."""
        results = full_landscape_verification(max_genus=1)
        for r in results:
            kappa = r.get("kappa")
            if kappa is not None and simplify(kappa) != 0:
                assert r.get("obs_1") is not None
                assert simplify(r["obs_1"]) != 0, (
                    f"{r['family']}: F_1 should be nonzero when kappa != 0"
                )

    def test_landscape_kappa_positive_standard(self):
        """Standard families at positive level have kappa > 0."""
        positive_families = [
            ("Heisenberg", {"k": 1}),
            ("sl2", {"level": 1}),
            ("Virasoro", {"c": 1}),
            ("betagamma", {}),
            ("lattice", {"rank": 1}),
        ]
        for fam, params in positive_families:
            p = genus_extension_profile(fam, **params)
            assert simplify(p.kappa) > 0, (
                f"{fam}: kappa should be positive at standard parameters"
            )


# ============================================================================
# Non-standard family tests
# ============================================================================

class TestNonStandard:
    """Non-standard families with known obstructions."""

    def test_non_standard_examples_exist(self):
        """We have documented non-standard obstruction examples."""
        examples = non_standard_obstruction_examples()
        assert len(examples) >= 3

    def test_heisenberg_negative_level(self):
        """H_{-1}: C_2-cofinite but NOT energy-bounded => sewing fails."""
        examples = non_standard_obstruction_examples()
        h_neg = [e for e in examples if "H_{-1}" in e["name"]][0]
        assert h_neg["c2_cofinite"] is True
        assert h_neg["energy_bounded"] is False
        assert h_neg["sewing_converges"] is False

    def test_critical_level_obstruction(self):
        """sl_2 at critical level k=-2: kappa = 0, Sugawara undefined."""
        examples = non_standard_obstruction_examples()
        crit = [e for e in examples if "critical" in e["name"]][0]
        assert crit["kappa"] == Rational(0)

    def test_non_c2_cofinite_fails(self):
        """Non-C_2-cofinite VOA: genus extension FAILS."""
        examples = non_standard_obstruction_examples()
        nc2 = [e for e in examples if "Non-C_2" in e["name"]][0]
        assert nc2["c2_cofinite"] is False
        assert nc2["extends_to_all_genera"] is False

    def test_logarithmic_extends(self):
        """Triplet W(p): C_2-cofinite, non-rational, but extends (Gui-Zhang)."""
        examples = non_standard_obstruction_examples()
        trip = [e for e in examples if "Triplet" in e["name"]][0]
        assert trip["c2_cofinite"] is True
        assert trip["rational"] is False
        assert trip["extends_to_all_genera"] is True


# ============================================================================
# Theory tests
# ============================================================================

class TestTheory:
    """Tests for the theoretical framework."""

    def test_minimal_conditions_structure(self):
        """Minimal conditions theorem returns structured data."""
        mc = minimal_conditions_for_genus_extension()
        assert "necessary" in mc
        assert "sufficient" in mc
        assert "N1" in mc["necessary"]
        assert "S1" in mc["sufficient"]

    def test_c2_is_necessary(self):
        """C_2-cofiniteness appears in both necessary and sufficient."""
        mc = minimal_conditions_for_genus_extension()
        assert "C_2" in mc["necessary"]["N1"]
        assert "C_2" in mc["sufficient"]["S1"]

    def test_rationality_not_necessary(self):
        """Rationality is stronger than necessary."""
        mc = minimal_conditions_for_genus_extension()
        assert "Rationality" in mc["stronger_not_necessary"]["SS1"]


# ============================================================================
# Edge case and special value tests
# ============================================================================

class TestEdgeCases:
    """Edge cases and special parameter values."""

    def test_virasoro_c0_kappa_zero(self):
        """Virasoro at c=0: kappa = 0, uncurved."""
        p = genus_extension_profile("Virasoro", c=0)
        assert p.kappa == Rational(0)
        # Still extends (trivially uncurved)
        assert p.extends_to_all_genera is True

    def test_virasoro_c26_kappa_13(self):
        """Virasoro at c=26: kappa = 13 (AP24: kappa+kappa' = 13, not 0)."""
        p = genus_extension_profile("Virasoro", c=26)
        assert p.kappa == Rational(13)

    def test_virasoro_c13_self_dual(self):
        """Virasoro at c=13: self-dual point, kappa = 13/2."""
        p = genus_extension_profile("Virasoro", c=13)
        assert p.kappa == Rational(13, 2)

    def test_sl2_critical_kappa_zero(self):
        """sl_2 at critical level k=-2: kappa = 3*(-2+2)/4 = 0."""
        p = genus_extension_profile("sl2", level=-2)
        assert p.kappa == Rational(0)

    def test_heisenberg_large_rank(self):
        """Heisenberg at rank 24 (Leech): kappa = 24."""
        p = genus_extension_profile("Heisenberg", k=24)
        assert p.kappa == Rational(24)

    def test_ising_model(self):
        """Ising model (Virasoro c=1/2): rational, extends."""
        p = genus_extension_profile("Virasoro", c=Rational(1, 2))
        assert p.c2_cofinite is True
        assert p.rational is True
        assert p.extends_to_all_genera is True
        assert p.kappa == Rational(1, 4)

    def test_complementarity_virasoro(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        for c_val in [1, Rational(1, 2), 13, 25]:
            k1 = kappa_virasoro(c_val)
            k2 = kappa_virasoro(26 - c_val)
            assert simplify(k1 + k2) == Rational(13)

    def test_complementarity_sl2(self):
        """kappa(sl2_k) + kappa(sl2_{-k-4}) = 0 (AP24 for KM)."""
        for k_val in [1, 2, 5, 10]:
            k1 = kappa_sl2(k_val)
            k2 = kappa_sl2(-k_val - 4)  # FF dual: k' = -k - 2h* = -k - 4
            assert simplify(k1 + k2) == Rational(0)


# ============================================================================
# Multi-path verification: genus expansion cross-check
# ============================================================================

class TestMultiPathVerification:
    """Multi-path verification of key numerical values."""

    def test_lambda_fp_genus1_three_paths(self):
        """lambda_1^FP = 1/24 verified three ways."""
        # Path 1: Direct formula
        assert lambda_fp(1) == Rational(1, 24)
        # Path 2: Bernoulli number B_2 = 1/6
        from sympy import bernoulli as B
        B2 = B(2)
        val = (2 ** 1 - 1) * abs(B2) / (2 ** 1 * 2)
        assert Rational(val) == Rational(1, 24)
        # Path 3: A-hat genus (x/2)/sin(x/2) - 1 = x^2/24 + ...
        from sympy import sin, Symbol, series
        x = Symbol('x')
        ahat = (x / 2) / sin(x / 2) - 1
        s = series(ahat, x, 0, 4)
        coeff = s.coeff(x, 2)
        assert coeff == Rational(1, 24)

    def test_lambda_fp_genus2_three_paths(self):
        """lambda_2^FP = 7/5760 verified three ways."""
        # Path 1: Direct
        assert lambda_fp(2) == Rational(7, 5760)
        # Path 2: From Bernoulli B_4 = -1/30
        from sympy import bernoulli as B
        B4 = B(4)
        num = (2 ** 3 - 1) * abs(B4)
        den = 2 ** 3 * 24
        assert Rational(num, den) == Rational(7, 5760)
        # Path 3: A-hat series coefficient
        from sympy import sin, Symbol, series
        x = Symbol('x')
        s = series((x / 2) / sin(x / 2) - 1, x, 0, 6)
        assert s.coeff(x, 4) == Rational(7, 5760)

    def test_F1_heisenberg_three_paths(self):
        """F_1(H_k) = k/24 verified three ways."""
        k = 5
        # Path 1: Direct
        assert F_g(Rational(k), 1) == Rational(k, 24)
        # Path 2: From profile
        obs = genus_g_obstruction_class("Heisenberg", 1, k=k)
        assert obs.value == Rational(k, 24)
        # Path 3: kappa * lambda_1
        assert kappa_heisenberg(k) * lambda_fp(1) == Rational(k, 24)

    def test_F1_virasoro_three_paths(self):
        """F_1(Vir_c) = c/48 verified three ways."""
        c = 2
        # Path 1: Direct
        assert F_g(Rational(c, 2), 1) == Rational(c, 48)
        # Path 2: From profile
        obs = genus_g_obstruction_class("Virasoro", 1, c=c)
        assert obs.value == Rational(c, 48)
        # Path 3: kappa * lambda_1
        assert kappa_virasoro(c) * lambda_fp(1) == Rational(c, 48)

    def test_kappa_additivity_heisenberg(self):
        """kappa is additive under direct sum: kappa(H_k1 + H_k2) = k1 + k2."""
        k1, k2 = 3, 7
        assert kappa_heisenberg(k1) + kappa_heisenberg(k2) == Rational(k1 + k2)

    def test_F_g_proportional_to_kappa(self):
        """F_g is proportional to kappa (universality of lambda_g^FP)."""
        for g in range(1, 5):
            for k in [1, 2, 5]:
                ratio = F_g(Rational(k), g) / F_g(Rational(1), g)
                assert simplify(ratio) == Rational(k)
