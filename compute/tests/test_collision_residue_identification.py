"""Tests for collision-residue identification (Yangian-shadow theorem).

Verifies: r(z) = Res^coll_{0,2}(Theta_A)

The key claim: the dg-shifted Yangian r-matrix r(z) controlling the
binary OPE of A! is the binary collision residue of the full modular
MC class Theta_A (Theorem thm:mc2-bar-intrinsic).

Test coverage:
  1. OPE data construction for all standard families
  2. Binary r-matrix extraction from OPE with one-pole absorption
  3. Collision residue computation from Theta_A|_{n=2,g=0}
  4. Identification verification: collision residue = r-matrix
  5. Additivity: Res(Theta_{A+B}) = Res(Theta_A) + Res(Theta_B)
  6. Level-polynomiality for affine families
  7. Gaussian collapse for Heisenberg
  8. Shadow depth classification
  9. Kappa-r-matrix consistency
 10. Master verification across all families

Mathematical references:
  - Theorem thm:mc2-bar-intrinsic (bar-intrinsic construction)
  - Remark rem:theta-modular-twisting (modular twisting cochain)
  - Corollary cor:exact-r-matrix (exactness for standard families)
  - Theorem D (modular characteristic kappa)
"""

from __future__ import annotations

from fractions import Fraction

import pytest

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'lib'))

from collision_residue_identification import (
    OPEData,
    heisenberg_ope,
    affine_sl2_ope,
    betagamma_ope,
    virasoro_ope,
    kappa_value,
    BinaryRMatrix,
    CollisionResidueEngine,
    HigherArityCollisionResidue,
    verify_additivity,
    verify_level_polynomiality_sl2,
    master_collision_residue_verification,
    verify_kappa_r_matrix_consistency,
)


# ========================================================================
# OPE data construction
# ========================================================================

class TestOPEData:
    """Test OPE data construction for standard families."""

    def test_heisenberg_ope_default(self):
        """Heisenberg at default level kappa=1."""
        ope = heisenberg_ope()
        assert ope.name == "Heisenberg(kappa=1)"
        assert ope.generators == ["J"]
        assert ope.pole_orders[("J", "J")] == 2
        assert ope.leading_coefficients[("J", "J")] == Fraction(1)
        assert ope.central_charge == Fraction(1)

    def test_heisenberg_ope_level_k(self):
        """Heisenberg at level kappa=3."""
        ope = heisenberg_ope(Fraction(3))
        assert ope.leading_coefficients[("J", "J")] == Fraction(3)

    def test_heisenberg_ope_fractional_level(self):
        """Heisenberg at fractional level kappa=1/2."""
        ope = heisenberg_ope(Fraction(1, 2))
        assert ope.leading_coefficients[("J", "J")] == Fraction(1, 2)

    def test_affine_sl2_ope_level1(self):
        """Affine sl_2 at level k=1."""
        ope = affine_sl2_ope(Fraction(1))
        assert len(ope.generators) == 3
        # Double pole coefficient for diagonal pairs = k = 1
        assert ope.leading_coefficients[("J1", "J1")] == Fraction(1)
        assert ope.leading_coefficients[("J2", "J2")] == Fraction(1)
        # Off-diagonal leading coefficients are 0 (simple poles only)
        assert ope.leading_coefficients[("J1", "J2")] == Fraction(0)
        # Central charge: c = 1*3/(1+2) = 1
        assert ope.central_charge == Fraction(1)

    def test_affine_sl2_central_charge(self):
        """Central charge c = k*dim/(k+h^v) = 3k/(k+2)."""
        for k, expected_c in [
            (Fraction(1), Fraction(1)),       # 3/(1+2) = 1
            (Fraction(2), Fraction(3, 2)),    # 6/(2+2) = 3/2
            (Fraction(4), Fraction(2)),       # 12/(4+2) = 2
        ]:
            ope = affine_sl2_ope(k)
            assert ope.central_charge == expected_c, \
                f"Expected c={expected_c} at k={k}, got {ope.central_charge}"

    def test_affine_sl2_critical_level_raises(self):
        """Critical level k=-2 should raise ValueError."""
        with pytest.raises(ValueError, match="Critical level"):
            affine_sl2_ope(Fraction(-2))

    def test_betagamma_ope_default(self):
        """betagamma at default weight lambda=1."""
        ope = betagamma_ope()
        assert len(ope.generators) == 2
        assert ope.pole_orders[("beta", "gamma")] == 1
        assert ope.pole_orders[("beta", "beta")] == 0
        assert ope.leading_coefficients[("beta", "gamma")] == Fraction(1)
        assert ope.leading_coefficients[("beta", "beta")] == Fraction(0)
        # c = +2*(6 - 6 + 1) = +2 for lambda=1
        assert ope.central_charge == Fraction(2)

    def test_betagamma_central_charge_half(self):
        """betagamma at lambda=1/2: c = +2*(6/4 - 3 + 1) = +2*(-1/2+1) = -1... wait:
        c = +2*(6*(1/4) - 6*(1/2) + 1) = +2*(3/2 - 3 + 1) = +2*(-1/2) = -1."""
        ope = betagamma_ope(Fraction(1, 2))
        assert ope.central_charge == Fraction(-1)

    def test_virasoro_ope(self):
        """Virasoro OPE at central charge c=25."""
        ope = virasoro_ope(Fraction(25))
        assert ope.generators == ["T"]
        assert ope.pole_orders[("T", "T")] == 4
        assert ope.leading_coefficients[("T", "T")] == Fraction(25, 2)
        assert ope.central_charge == Fraction(25)

    def test_virasoro_ope_c26(self):
        """Virasoro at c=26 (bosonic string)."""
        ope = virasoro_ope(Fraction(26))
        assert ope.leading_coefficients[("T", "T")] == Fraction(13)


# ========================================================================
# Kappa values
# ========================================================================

class TestKappaValues:
    """Test modular characteristic kappa computation."""

    def test_heisenberg_kappa(self):
        """kappa(H) = level."""
        assert kappa_value("heisenberg", level=1) == Fraction(1)
        assert kappa_value("heisenberg", level=3) == Fraction(3)
        assert kappa_value("heisenberg", level=Fraction(1, 2)) == Fraction(1, 2)

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        assert kappa_value("virasoro", c=25) == Fraction(25, 2)
        assert kappa_value("virasoro", c=26) == Fraction(13)
        assert kappa_value("virasoro", c=1) == Fraction(1, 2)

    def test_affine_sl2_kappa(self):
        """kappa(sl_2_k) = 3(k+2)/4."""
        assert kappa_value("affine_sl2", k=1) == Fraction(9, 4)
        assert kappa_value("affine_sl2", k=2) == Fraction(3)
        assert kappa_value("affine_sl2", k=0) == Fraction(3, 2)

    def test_affine_slN_kappa(self):
        """kappa(sl_N_k) = dim(g)(k+h^v)/(2h^v) = (N^2-1)(k+N)/(2N)."""
        # sl_3 at k=1: (8)(4)/6 = 32/6 = 16/3
        assert kappa_value("affine_slN", k=1, N=3) == Fraction(16, 3)

    def test_betagamma_kappa(self):
        """kappa(betagamma) = c/2."""
        # lambda=1: c=+2, kappa=+1
        assert kappa_value("betagamma", **{"lambda": 1}) == Fraction(1)
        # lambda=1/2: c=-1, kappa=-1/2
        assert kappa_value("betagamma", **{"lambda": Fraction(1, 2)}) == Fraction(-1, 2)


# ========================================================================
# Binary r-matrix
# ========================================================================

class TestBinaryRMatrix:
    """Test binary r-matrix extraction from OPE."""

    def test_heisenberg_r_matrix(self):
        """Heisenberg r-matrix: r(z) = kappa/z."""
        ope = heisenberg_ope(Fraction(3))
        r = BinaryRMatrix(ope)
        rv = r.r_value("J", "J")
        assert rv['pole_order'] == 1
        assert rv['ope_pole_order'] == 2
        assert rv['coefficient'] == Fraction(3)

    def test_heisenberg_scalar_trace(self):
        """Heisenberg scalar trace = kappa = level."""
        ope = heisenberg_ope(Fraction(5))
        r = BinaryRMatrix(ope)
        assert r.scalar_trace() == Fraction(5)

    def test_affine_sl2_r_matrix(self):
        """Affine sl_2 r-matrix: diagonal entries = k/z."""
        ope = affine_sl2_ope(Fraction(3))
        r = BinaryRMatrix(ope)
        for gen in ["J1", "J2", "J3"]:
            rv = r.r_value(gen, gen)
            assert rv['pole_order'] == 1
            assert rv['ope_pole_order'] == 2
            assert rv['coefficient'] == Fraction(3)

    def test_affine_sl2_scalar_trace(self):
        """Affine sl_2 scalar trace = 3k (Casimir trace)."""
        ope = affine_sl2_ope(Fraction(2))
        r = BinaryRMatrix(ope)
        # trace = k + k + k = 3k = 6
        assert r.scalar_trace() == Fraction(6)

    def test_betagamma_r_matrix(self):
        """betagamma r-matrix: the simple OPE pole becomes a regular term."""
        ope = betagamma_ope()
        r = BinaryRMatrix(ope)
        rv = r.r_value("beta", "gamma")
        assert rv['pole_order'] == 0
        assert rv['ope_pole_order'] == 1
        assert rv['coefficient'] == Fraction(1)
        # Diagonal entries are zero
        rv_diag = r.r_value("beta", "beta")
        assert rv_diag['coefficient'] == Fraction(0)

    def test_betagamma_scalar_trace(self):
        """betagamma scalar trace = 0 (off-diagonal propagator)."""
        ope = betagamma_ope()
        r = BinaryRMatrix(ope)
        assert r.scalar_trace() == Fraction(0)

    def test_virasoro_r_matrix(self):
        """Virasoro r-matrix: r(z) = (c/2)/z^3."""
        ope = virasoro_ope(Fraction(25))
        r = BinaryRMatrix(ope)
        rv = r.r_value("T", "T")
        assert rv['pole_order'] == 3
        assert rv['ope_pole_order'] == 4
        assert rv['coefficient'] == Fraction(25, 2)

    def test_virasoro_scalar_trace(self):
        """Virasoro scalar trace = c/2 = kappa."""
        ope = virasoro_ope(Fraction(26))
        r = BinaryRMatrix(ope)
        assert r.scalar_trace() == Fraction(13)

    def test_zero_r_matrix_for_noninteracting(self):
        """Zero r-matrix when no poles exist."""
        ope = betagamma_ope()
        r = BinaryRMatrix(ope)
        rv = r.r_value("gamma", "gamma")
        assert rv['pole_order'] == 0
        assert rv['coefficient'] == Fraction(0)


# ========================================================================
# Collision residue engine
# ========================================================================

class TestCollisionResidueEngine:
    """Test the collision residue engine."""

    def test_heisenberg_theta_arity2(self):
        """Theta_A|_{n=2,g=0} for Heisenberg."""
        engine = CollisionResidueEngine("heisenberg", level=Fraction(2))
        theta = engine.theta_arity2_genus0()
        assert theta['genus'] == 0
        assert theta['arity'] == 2
        assert ("J", "J") in theta['components']
        comp = theta['components'][("J", "J")]
        assert comp['pole_order'] == 2
        assert comp['coefficient'] == Fraction(2)

    def test_virasoro_theta_arity2(self):
        """Theta_A|_{n=2,g=0} for Virasoro."""
        engine = CollisionResidueEngine("virasoro", c=Fraction(25))
        theta = engine.theta_arity2_genus0()
        comp = theta['components'][("T", "T")]
        assert comp['pole_order'] == 4
        assert comp['coefficient'] == Fraction(25, 2)

    def test_heisenberg_collision_residue(self):
        """Collision residue of Theta_{Heis}."""
        engine = CollisionResidueEngine("heisenberg", level=Fraction(3))
        coll = engine.collision_residue()
        assert coll['matches_r_matrix']
        residues = coll['residues']
        assert ("J", "J") in residues
        assert residues[("J", "J")]['pole_order'] == 1
        assert residues[("J", "J")]['ope_pole_order'] == 2
        assert residues[("J", "J")]['residue'] == Fraction(3)

    def test_betagamma_collision_residue(self):
        """Collision residue of Theta_{betagamma}."""
        engine = CollisionResidueEngine("betagamma", **{"lambda": Fraction(1)})
        coll = engine.collision_residue()
        residues = coll['residues']
        assert ("beta", "gamma") in residues
        assert residues[("beta", "gamma")]['pole_order'] == 0
        assert residues[("beta", "gamma")]['ope_pole_order'] == 1
        assert residues[("beta", "gamma")]['residue'] == Fraction(1)
        assert ("beta", "beta") not in residues  # zero entries excluded


# ========================================================================
# Identification verification (the main theorem)
# ========================================================================

class TestIdentification:
    """Test the Yangian-shadow identification: r(z) = Res^coll_{0,2}(Theta_A)."""

    def test_heisenberg_identification(self):
        """Identification holds for Heisenberg at all levels."""
        for level in [1, 2, 5, Fraction(1, 2), Fraction(7, 3)]:
            engine = CollisionResidueEngine("heisenberg", level=level)
            v = engine.verify_identification()
            assert v['identification_holds'], \
                f"Identification failed for Heisenberg at level={level}"
            assert v['n_mismatches'] == 0

    def test_affine_sl2_identification(self):
        """Identification holds for affine sl_2 at various levels."""
        for k in [Fraction(1), Fraction(2), Fraction(3),
                  Fraction(-1, 2), Fraction(1, 3)]:
            engine = CollisionResidueEngine("affine_sl2", k=k)
            v = engine.verify_identification()
            assert v['identification_holds'], \
                f"Identification failed for sl_2 at k={k}"

    def test_betagamma_identification(self):
        """Identification holds for betagamma at various weights."""
        for lam in [Fraction(1), Fraction(1, 2), Fraction(2)]:
            engine = CollisionResidueEngine("betagamma", **{"lambda": lam})
            v = engine.verify_identification()
            assert v['identification_holds'], \
                f"Identification failed for betagamma at lambda={lam}"

    def test_virasoro_identification(self):
        """Identification holds for Virasoro at various c."""
        for c in [Fraction(1), Fraction(25), Fraction(26),
                  Fraction(1, 2), Fraction(-22, 5), Fraction(13)]:
            engine = CollisionResidueEngine("virasoro", c=c)
            v = engine.verify_identification()
            assert v['identification_holds'], \
                f"Identification failed for Virasoro at c={c}"

    def test_identification_match_count(self):
        """Each family has the expected number of matches."""
        # Heisenberg: 1 generator, 1 diagonal match (J,J)
        engine = CollisionResidueEngine("heisenberg", level=Fraction(1))
        v = engine.verify_identification()
        assert v['n_matches'] == 1

        # Affine sl_2: 3 generators, 3 diagonal matches
        engine = CollisionResidueEngine("affine_sl2", k=Fraction(1))
        v = engine.verify_identification()
        assert v['n_matches'] == 3

        # betagamma: 2 generators, 2 off-diagonal matches
        engine = CollisionResidueEngine("betagamma", **{"lambda": Fraction(1)})
        v = engine.verify_identification()
        assert v['n_matches'] == 2

        # Virasoro: 1 generator, 1 match (T,T)
        engine = CollisionResidueEngine("virasoro", c=Fraction(25))
        v = engine.verify_identification()
        assert v['n_matches'] == 1


# ========================================================================
# Higher-arity collision residues and shadow depth
# ========================================================================

class TestHigherArityCollisionResidue:
    """Test higher-arity collision residues and shadow depth."""

    def test_heisenberg_gaussian_class(self):
        """Heisenberg is class G (Gaussian), shadow depth 2."""
        ha = HigherArityCollisionResidue("heisenberg", level=Fraction(1))
        assert ha.shadow_class == 'G'
        assert ha.shadow_depth == 2

    def test_affine_sl2_lie_class(self):
        """Affine sl_2 is class L (Lie/tree), shadow depth 3."""
        ha = HigherArityCollisionResidue("affine_sl2", k=Fraction(1))
        assert ha.shadow_class == 'L'
        assert ha.shadow_depth == 3

    def test_betagamma_contact_class(self):
        """betagamma is class C (contact/quartic), shadow depth 4."""
        ha = HigherArityCollisionResidue("betagamma", **{"lambda": Fraction(1)})
        assert ha.shadow_class == 'C'
        assert ha.shadow_depth == 4

    def test_virasoro_mixed_class(self):
        """Virasoro is class M (mixed), infinite shadow depth."""
        ha = HigherArityCollisionResidue("virasoro", c=Fraction(25))
        assert ha.shadow_class == 'M'
        assert ha.shadow_depth is None

    def test_heisenberg_arity2_nonzero(self):
        """Arity-2 correction is always nonzero (the binary r-matrix)."""
        ha = HigherArityCollisionResidue("heisenberg", level=Fraction(1))
        corr = ha.arity_r_correction(2)
        assert corr['nonzero']
        assert corr['arity'] == 2

    def test_heisenberg_arity3_vanishes(self):
        """Arity-3 correction vanishes for Heisenberg (Gaussian)."""
        ha = HigherArityCollisionResidue("heisenberg", level=Fraction(1))
        corr = ha.arity_r_correction(3)
        assert not corr['nonzero']

    def test_heisenberg_all_higher_vanish(self):
        """All arity >= 3 corrections vanish for Heisenberg."""
        ha = HigherArityCollisionResidue("heisenberg", level=Fraction(1))
        for r in range(3, 10):
            corr = ha.arity_r_correction(r)
            assert not corr['nonzero'], \
                f"Arity-{r} correction should vanish for Heisenberg"

    def test_affine_sl2_arity3_nonzero(self):
        """Arity-3 correction is nonzero for affine (Lie/tree)."""
        ha = HigherArityCollisionResidue("affine_sl2", k=Fraction(1))
        corr = ha.arity_r_correction(3)
        assert corr['nonzero']

    def test_affine_sl2_arity4_vanishes(self):
        """Arity-4 correction vanishes for affine (terminates at 3)."""
        ha = HigherArityCollisionResidue("affine_sl2", k=Fraction(1))
        corr = ha.arity_r_correction(4)
        assert not corr['nonzero']

    def test_betagamma_arity4_nonzero(self):
        """Arity-4 correction is nonzero for betagamma (contact)."""
        ha = HigherArityCollisionResidue("betagamma", **{"lambda": Fraction(1)})
        corr = ha.arity_r_correction(4)
        assert corr['nonzero']

    def test_betagamma_arity5_vanishes(self):
        """Arity-5 correction vanishes for betagamma (terminates at 4)."""
        ha = HigherArityCollisionResidue("betagamma", **{"lambda": Fraction(1)})
        corr = ha.arity_r_correction(5)
        assert not corr['nonzero']

    def test_virasoro_arity5_nonzero(self):
        """Arity-5 correction is nonzero for Virasoro (infinite tower)."""
        ha = HigherArityCollisionResidue("virasoro", c=Fraction(25))
        corr = ha.arity_r_correction(5)
        assert corr['nonzero']

    def test_virasoro_all_arities_nonzero(self):
        """All arity >= 2 corrections are nonzero for Virasoro (mixed class)."""
        ha = HigherArityCollisionResidue("virasoro", c=Fraction(25))
        for r in range(2, 10):
            corr = ha.arity_r_correction(r)
            assert corr['nonzero'], \
                f"Arity-{r} should be nonzero for Virasoro"

    def test_arity_below_2_raises(self):
        """Arity < 2 should raise ValueError."""
        ha = HigherArityCollisionResidue("heisenberg", level=Fraction(1))
        with pytest.raises(ValueError, match="Arity must be >= 2"):
            ha.arity_r_correction(1)


# ========================================================================
# Gaussian collapse
# ========================================================================

class TestGaussianCollapse:
    """Test Gaussian collapse: for Heisenberg, collision residue = r(z) exactly."""

    def test_heisenberg_gaussian_collapse(self):
        """Heisenberg is Gaussian: collision residue = r(z) with no corrections."""
        ha = HigherArityCollisionResidue("heisenberg", level=Fraction(1))
        gc = ha.gaussian_collapse_check()
        assert gc['is_gaussian']
        assert gc['all_higher_corrections_vanish']
        assert gc['r_matrix_is_exact']

    def test_heisenberg_at_various_levels(self):
        """Gaussian collapse holds at all levels for Heisenberg."""
        for level in [1, 2, 5, Fraction(1, 3), Fraction(7)]:
            ha = HigherArityCollisionResidue("heisenberg", level=level)
            gc = ha.gaussian_collapse_check()
            assert gc['is_gaussian'], \
                f"Heisenberg should be Gaussian at level={level}"
            assert gc['r_matrix_is_exact'], \
                f"r-matrix should be exact at level={level}"

    def test_affine_not_gaussian(self):
        """Affine sl_2 is NOT Gaussian (class L, depth 3)."""
        ha = HigherArityCollisionResidue("affine_sl2", k=Fraction(1))
        gc = ha.gaussian_collapse_check()
        assert not gc['is_gaussian']
        assert gc['shadow_class'] == 'L'

    def test_virasoro_not_gaussian(self):
        """Virasoro is NOT Gaussian (class M, infinite depth)."""
        ha = HigherArityCollisionResidue("virasoro", c=Fraction(25))
        gc = ha.gaussian_collapse_check()
        assert not gc['is_gaussian']
        assert gc['shadow_class'] == 'M'


# ========================================================================
# Truncation analysis
# ========================================================================

class TestTruncationAnalysis:
    """Test the truncation behavior of the collision residue series."""

    def test_heisenberg_finite_truncation(self):
        """Heisenberg has finite truncation (r_max = 2)."""
        ha = HigherArityCollisionResidue("heisenberg", level=Fraction(1))
        ta = ha.truncation_analysis()
        assert ta['is_finite']
        assert ta['shadow_depth'] == 2
        assert ta['r_matrix_exact_at_tree_level']

    def test_affine_finite_truncation(self):
        """Affine sl_2 has finite truncation (r_max = 3)."""
        ha = HigherArityCollisionResidue("affine_sl2", k=Fraction(1))
        ta = ha.truncation_analysis()
        assert ta['is_finite']
        assert ta['shadow_depth'] == 3

    def test_virasoro_infinite_tower(self):
        """Virasoro has infinite tower (no truncation)."""
        ha = HigherArityCollisionResidue("virasoro", c=Fraction(25))
        ta = ha.truncation_analysis()
        assert not ta['is_finite']
        assert ta['shadow_depth'] is None

    def test_all_families_exact_at_tree_level(self):
        """All standard families have exact r-matrix at tree level.

        This is Corollary cor:exact-r-matrix: for quasi-linear theories,
        the tree-level r-matrix receives no loop corrections.
        """
        families = [
            ("heisenberg", {"level": Fraction(1)}),
            ("affine_sl2", {"k": Fraction(1)}),
            ("betagamma", {"lambda": Fraction(1)}),
            ("virasoro", {"c": Fraction(25)}),
        ]
        for atype, params in families:
            ha = HigherArityCollisionResidue(atype, **params)
            ta = ha.truncation_analysis()
            assert ta['r_matrix_exact_at_tree_level'], \
                f"r-matrix should be exact at tree level for {atype}"


# ========================================================================
# Additivity
# ========================================================================

class TestAdditivity:
    """Test additivity of collision residues."""

    def test_heisenberg_plus_heisenberg(self):
        """Additivity: Theta_{H_a + H_b} = Theta_{H_a} + Theta_{H_b}."""
        engine_a = CollisionResidueEngine("heisenberg", level=Fraction(3))
        engine_b = CollisionResidueEngine("heisenberg", level=Fraction(5))
        result = verify_additivity(engine_a, engine_b)
        assert result['kappa_additive']
        assert result['kappa_sum'] == Fraction(8)
        assert result['collision_residue_additive']

    def test_heisenberg_plus_virasoro(self):
        """Additivity: different algebra types."""
        engine_a = CollisionResidueEngine("heisenberg", level=Fraction(1))
        engine_b = CollisionResidueEngine("virasoro", c=Fraction(25))
        result = verify_additivity(engine_a, engine_b)
        assert result['kappa_A'] == Fraction(1)
        assert result['kappa_B'] == Fraction(25, 2)
        assert result['kappa_sum'] == Fraction(27, 2)
        assert result['kappa_additive']

    def test_affine_plus_affine(self):
        """Additivity for two affine algebras."""
        engine_a = CollisionResidueEngine("affine_sl2", k=Fraction(1))
        engine_b = CollisionResidueEngine("affine_sl2", k=Fraction(2))
        result = verify_additivity(engine_a, engine_b)
        # kappa(sl_2, k=1) = 9/4, kappa(sl_2, k=2) = 3
        assert result['kappa_A'] == Fraction(9, 4)
        assert result['kappa_B'] == Fraction(3)
        assert result['kappa_sum'] == Fraction(21, 4)

    def test_three_algebras_additive(self):
        """Additivity extends to three or more summands."""
        e1 = CollisionResidueEngine("heisenberg", level=Fraction(1))
        e2 = CollisionResidueEngine("heisenberg", level=Fraction(2))
        e3 = CollisionResidueEngine("heisenberg", level=Fraction(3))
        r12 = verify_additivity(e1, e2)
        # kappa(H_1 + H_2) = 3, kappa(H_3) = 3
        assert r12['kappa_sum'] == Fraction(3)
        # Total should be 6
        total_kappa = r12['kappa_sum'] + e3.kappa
        assert total_kappa == Fraction(6)


# ========================================================================
# Level polynomiality
# ========================================================================

class TestLevelPolynomiality:
    """Test level-polynomiality for affine families."""

    def test_sl2_r_coefficient_linear_in_k(self):
        """The r-matrix coefficient is linear in k for sl_2."""
        result = verify_level_polynomiality_sl2()
        assert result['r_coefficient_linear_in_k'], \
            "r-coefficient should be linear in k"
        assert result['r_degree'] == 1

    def test_sl2_kappa_polynomial_in_k(self):
        """kappa = 3(k+2)/4 is polynomial in k (degree 1)."""
        result = verify_level_polynomiality_sl2()
        assert result['kappa_polynomial_in_k'], \
            "kappa should be polynomial in k"
        assert result['kappa_degree'] == 1

    def test_sl2_many_levels(self):
        """Polynomiality holds at many levels."""
        levels = [Fraction(n) for n in range(1, 21)]
        result = verify_level_polynomiality_sl2(levels)
        assert result['n_levels_tested'] == 20
        assert result['r_coefficient_linear_in_k']

    def test_sl2_fractional_levels(self):
        """Polynomiality holds at fractional levels."""
        levels = [Fraction(p, q) for p in range(1, 8) for q in range(1, 5)
                  if p != 2 * q]  # exclude critical level k=-2
        result = verify_level_polynomiality_sl2(levels)
        assert result['r_coefficient_linear_in_k']

    @pytest.mark.parametrize("k", [
        Fraction(1), Fraction(-1, 2), Fraction(-4, 3),
        Fraction(1, 3), Fraction(10),
    ])
    def test_individual_level_r_equals_k(self, k):
        """At each level, the diagonal r-coefficient equals k."""
        engine = CollisionResidueEngine("affine_sl2", k=k)
        r_data = engine.known_r_matrix()
        # Check J1-J1 coefficient = k
        assert r_data['components'][("J1", "J1")]['coefficient'] == k


# ========================================================================
# Kappa-r-matrix consistency
# ========================================================================

class TestKappaRMatrixConsistency:
    """Test consistency between kappa and r-matrix."""

    def test_heisenberg_kappa_equals_r_trace(self):
        """For Heisenberg: kappa = level = trace(r)."""
        for level in [1, 2, 5]:
            engine = CollisionResidueEngine("heisenberg", level=Fraction(level))
            assert engine.kappa == engine.r_matrix.scalar_trace(), \
                f"kappa != trace(r) for Heisenberg at level={level}"

    def test_virasoro_kappa_equals_r_trace(self):
        """For Virasoro: kappa = c/2 = trace(r)."""
        for c in [1, 25, 26]:
            engine = CollisionResidueEngine("virasoro", c=Fraction(c))
            assert engine.kappa == engine.r_matrix.scalar_trace(), \
                f"kappa != trace(r) for Virasoro at c={c}"

    def test_affine_kappa_differs_from_r_trace(self):
        """For affine sl_2: kappa = 3(k+2)/4 != 3k = trace(r).

        The discrepancy is the dual Coxeter shift: kappa includes the
        h^v correction while the r-matrix trace is the bare Casimir.
        """
        for k in [1, 2, 3]:
            engine = CollisionResidueEngine("affine_sl2", k=Fraction(k))
            kappa = engine.kappa
            r_trace = engine.r_matrix.scalar_trace()
            # kappa = 3(k+2)/4, r_trace = 3k
            assert kappa != r_trace, \
                f"kappa should differ from trace(r) for affine at k={k}"
            # But the relationship is structural:
            # kappa = dim(g)(k+h^v)/(2h^v), trace(r) = dim(g)*k
            assert r_trace == Fraction(3) * Fraction(k), \
                f"trace(r) should be 3k, got {r_trace}"
            assert kappa == Fraction(3) * (Fraction(k) + 2) / Fraction(4), \
                f"kappa should be 3(k+2)/4, got {kappa}"

    def test_betagamma_kappa_vs_r_trace(self):
        """For betagamma: kappa = c/2, trace(r) = 0 (off-diagonal).

        The off-diagonal nature of the betagamma propagator means
        the diagonal r-matrix trace vanishes, even though kappa != 0.
        """
        engine = CollisionResidueEngine("betagamma", **{"lambda": Fraction(1)})
        assert engine.kappa == Fraction(1)
        assert engine.r_matrix.scalar_trace() == Fraction(0)
        # kappa != trace(r) because the propagator is off-diagonal

    def test_consistency_report(self):
        """Run the full consistency report."""
        results = verify_kappa_r_matrix_consistency()
        assert len(results) >= 9
        # Check Heisenberg entries have kappa = r_trace
        heis_results = [r for r in results if 'Heisenberg' in r['algebra']]
        assert all(r['kappa_equals_r_trace'] for r in heis_results)
        # Check Virasoro entries have kappa = r_trace
        vir_results = [r for r in results if 'Virasoro' in r['algebra']]
        assert all(r['kappa_equals_r_trace'] for r in vir_results)


# ========================================================================
# Complementarity of collision residues
# ========================================================================

class TestComplementarity:
    """Test complementarity properties of the collision residue."""

    def test_virasoro_kappa_antisymmetry(self):
        """Virasoro: kappa(c) + kappa(26-c) = 13.

        Vir_c^! = Vir_{26-c} (Theorem thm:w-algebra-koszul-main).
        kappa(c) = c/2, kappa(26-c) = (26-c)/2.
        Sum = c/2 + (26-c)/2 = 13.
        """
        for c in [Fraction(1), Fraction(13), Fraction(25),
                  Fraction(0), Fraction(26)]:
            kappa_c = kappa_value("virasoro", c=c)
            kappa_dual = kappa_value("virasoro", c=Fraction(26) - c)
            assert kappa_c + kappa_dual == Fraction(13), \
                f"kappa(c) + kappa(26-c) should be 13, got {kappa_c + kappa_dual}"

    def test_virasoro_self_dual_at_c13(self):
        """Virasoro is self-dual at c=13.

        CRITICAL: self-dual at c=13, NOT c=26 (CLAUDE.md pitfall).
        kappa(13) = 13/2. The dual is Vir_{26-13} = Vir_13. Self-dual.
        """
        c = Fraction(13)
        kappa_c = kappa_value("virasoro", c=c)
        kappa_dual = kappa_value("virasoro", c=Fraction(26) - c)
        assert kappa_c == kappa_dual == Fraction(13, 2)

    def test_affine_sl2_complementarity(self):
        """Affine sl_2: kappa(k) + kappa(k') = dim(g)/2 = 3/2.

        Feigin-Frenkel: k' = -k - 2h^v = -k - 4.
        kappa(k) = 3(k+2)/4, kappa(k') = 3(k'+2)/4 = 3(-k-4+2)/4 = 3(-k-2)/4
        Sum = 3(k+2)/4 + 3(-k-2)/4 = 0.

        Wait: actually kappa(A) + kappa(A!) = 0 by Theorem D(iv) anti-symmetry.
        """
        for k in [Fraction(1), Fraction(2), Fraction(-1, 2)]:
            k_dual = -k - Fraction(4)
            if k_dual == Fraction(-2):
                continue  # skip critical level
            kappa_k = kappa_value("affine_sl2", k=k)
            kappa_dual = kappa_value("affine_sl2", k=k_dual)
            assert kappa_k + kappa_dual == Fraction(0), \
                f"kappa(k) + kappa(k') should be 0, got {kappa_k + kappa_dual}"


# ========================================================================
# Master verification
# ========================================================================

class TestMasterVerification:
    """Comprehensive master verification across all families."""

    def test_master_runs(self):
        """Master verification completes without errors."""
        results = master_collision_residue_verification()
        assert len(results) >= 15

    def test_master_all_identify(self):
        """All families pass the identification check."""
        results = master_collision_residue_verification()
        for r in results:
            assert r['identification_holds'], \
                f"Identification failed for {r['algebra']}"
            assert r['n_mismatches'] == 0, \
                f"Mismatches found for {r['algebra']}: {r['mismatches']}"

    def test_master_heisenberg_family(self):
        """Heisenberg family results are correct."""
        results = master_collision_residue_verification()
        heis = [r for r in results if r.get('family') == 'Heisenberg']
        assert len(heis) == 5
        for r in heis:
            assert r['identification_holds']

    def test_master_affine_family(self):
        """Affine sl_2 family results are correct."""
        results = master_collision_residue_verification()
        affine = [r for r in results if r.get('family') == 'Affine sl_2']
        assert len(affine) == 5
        for r in affine:
            assert r['identification_holds']

    def test_master_virasoro_family(self):
        """Virasoro family results are correct."""
        results = master_collision_residue_verification()
        vir = [r for r in results if r.get('family') == 'Virasoro']
        assert len(vir) == 5
        for r in vir:
            assert r['identification_holds']

    def test_master_betagamma_family(self):
        """betagamma family results are correct."""
        results = master_collision_residue_verification()
        bg = [r for r in results if r.get('family') == 'betagamma']
        assert len(bg) == 3
        for r in bg:
            assert r['identification_holds']


# ========================================================================
# Pole order consistency
# ========================================================================

class TestPoleOrders:
    """Test pole order consistency across families.

    AP19: the collision r-matrix loses one pole relative to the OPE:
      - Heisenberg: OPE p=2 -> r p=1
      - Affine: OPE p=2 -> r p=1
      - betagamma: OPE p=1 -> r p=0
      - Virasoro: OPE p=4 -> r p=3
    """

    def test_heisenberg_simple_pole(self):
        engine = CollisionResidueEngine("heisenberg", level=Fraction(1))
        v = engine.verify_identification()
        for m in v['matches']:
            assert m['pole_order'] == 1
            assert m['ope_pole_order'] == 2

    def test_affine_simple_pole(self):
        engine = CollisionResidueEngine("affine_sl2", k=Fraction(1))
        v = engine.verify_identification()
        for m in v['matches']:
            assert m['pole_order'] == 1
            assert m['ope_pole_order'] == 2

    def test_betagamma_regular_term(self):
        engine = CollisionResidueEngine("betagamma", **{"lambda": Fraction(1)})
        v = engine.verify_identification()
        for m in v['matches']:
            assert m['pole_order'] == 0
            assert m['ope_pole_order'] == 1

    def test_virasoro_cubic_pole(self):
        engine = CollisionResidueEngine("virasoro", c=Fraction(25))
        v = engine.verify_identification()
        for m in v['matches']:
            assert m['pole_order'] == 3
            assert m['ope_pole_order'] == 4

    @pytest.mark.parametrize("atype,expected_pole", [
        ("heisenberg", 1),
        ("virasoro", 3),
    ])
    def test_pole_order_parametric(self, atype, expected_pole):
        """Pole order matches AP19 after one-pole absorption."""
        params = {"level": Fraction(1)} if atype == "heisenberg" \
            else {"c": Fraction(25)}
        engine = CollisionResidueEngine(atype, **params)
        v = engine.verify_identification()
        assert all(m['pole_order'] == expected_pole for m in v['matches'])


# ========================================================================
# Edge cases and robustness
# ========================================================================

class TestEdgeCases:
    """Test edge cases and robustness."""

    def test_heisenberg_level_zero(self):
        """Heisenberg at level 0: trivial r-matrix."""
        engine = CollisionResidueEngine("heisenberg", level=Fraction(0))
        v = engine.verify_identification()
        # kappa = 0, no nonzero r-matrix entries
        assert v['n_matches'] == 0
        assert v['n_mismatches'] == 0
        assert v['identification_holds']

    def test_virasoro_c_zero(self):
        """Virasoro at c=0: trivial r-matrix."""
        engine = CollisionResidueEngine("virasoro", c=Fraction(0))
        v = engine.verify_identification()
        assert v['n_matches'] == 0
        assert v['identification_holds']

    def test_affine_negative_level(self):
        """Affine sl_2 at negative non-critical level."""
        engine = CollisionResidueEngine("affine_sl2", k=Fraction(-1))
        v = engine.verify_identification()
        assert v['identification_holds']
        # kappa = 3*(-1+2)/4 = 3/4
        assert engine.kappa == Fraction(3, 4)

    def test_large_level(self):
        """Affine sl_2 at large level k=100."""
        engine = CollisionResidueEngine("affine_sl2", k=Fraction(100))
        v = engine.verify_identification()
        assert v['identification_holds']
        assert engine.kappa == Fraction(3) * Fraction(102) / Fraction(4)

    def test_unknown_algebra_raises(self):
        """Unknown algebra type raises ValueError."""
        with pytest.raises(ValueError, match="Unknown algebra type"):
            CollisionResidueEngine("unknown_algebra")

    def test_betagamma_negative_weight(self):
        """betagamma at negative weight lambda=-1."""
        engine = CollisionResidueEngine("betagamma", **{"lambda": Fraction(-1)})
        v = engine.verify_identification()
        assert v['identification_holds']


# ========================================================================
# Virasoro self-duality point
# ========================================================================

class TestVirasoroSelfDuality:
    """Test properties at the Virasoro self-duality point c=13.

    CRITICAL (from CLAUDE.md): Virasoro is self-dual at c=13, NOT c=26.
    The dual is Vir_{26-c}, so c=13 gives Vir_13^! = Vir_{26-13} = Vir_13.
    """

    def test_self_dual_kappa(self):
        """At c=13: kappa = 13/2."""
        engine = CollisionResidueEngine("virasoro", c=Fraction(13))
        assert engine.kappa == Fraction(13, 2)

    def test_self_dual_r_matrix(self):
        """At c=13: r(z) = (13/2)/z^3."""
        engine = CollisionResidueEngine("virasoro", c=Fraction(13))
        rv = engine.r_matrix.r_value("T", "T")
        assert rv['coefficient'] == Fraction(13, 2)
        assert rv['pole_order'] == 3
        assert rv['ope_pole_order'] == 4

    def test_dual_symmetry(self):
        """r-matrix at c and 26-c are related by Koszul duality."""
        for c in [Fraction(1), Fraction(13), Fraction(25)]:
            c_dual = Fraction(26) - c
            engine = CollisionResidueEngine("virasoro", c=c)
            engine_dual = CollisionResidueEngine("virasoro", c=c_dual)
            # The r-matrix coefficients are c/2 and (26-c)/2
            r_c = engine.r_matrix.r_value("T", "T")['coefficient']
            r_dual = engine_dual.r_matrix.r_value("T", "T")['coefficient']
            assert r_c + r_dual == Fraction(13), \
                f"r(c) + r(26-c) should be 13, got {r_c + r_dual}"
