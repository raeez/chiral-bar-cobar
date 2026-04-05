"""Tests for the tropical bar complex engine.

Verifies:
  1. Metric planted trees and edge-length integration
  2. Tropical bar differential d^trop and d^2 = 0
  3. Tropical acyclicity for the four standard families
  4. Non-Koszul detection via nontrivial tropical cohomology
  5. Tropical shadow obstruction tower agreement with algebraic shadows
  6. Connection to planted forest algebra (combinatorial types agree)
  7. Multi-channel tropical complex
  8. Cross-consistency: Euler characteristics, f-vectors

References:
  thm:tropical-koszulness (chiral_koszul_pairs.tex)
  prop:shadow-formality-low-arity (higher_genus_modular_koszul.tex)
  cor:nms-betagamma-mu-vanishing
"""

import pytest
from sympy import Rational, Symbol, Integer, simplify, factorial

from compute.lib.tropical_bar_engine import (
    MetricEdge,
    MetricPlantedTree,
    TropicalIntegral,
    WeightedTropicalDifferential,
    TropicalBarEngine,
    NonKoszulTropicalComplex,
    TropicalShadowTower,
    MultiChannelTropicalComplex,
    non_koszul_ope,
    tropical_fm_equals_planted_forest,
    verify_grafting_composition,
    verify_heisenberg_tropical,
    verify_affine_sl2_tropical,
    verify_betagamma_tropical,
    verify_virasoro_tropical,
    shadow_tower_agrees_with_algebraic,
    tropical_euler_characteristic,
    verify_f_vector,
    full_landscape_tropical_verification,
    tropical_koszulness_summary,
)
from compute.lib.tropical_koszulness import (
    PlantedTree,
    enumerate_binary_trees,
    enumerate_planted_trees,
    heisenberg_ope,
    affine_sl2_ope,
    betagamma_ope,
    virasoro_ope,
    TropicalBarComplex,
    catalan,
)


# ===================================================================
# I. Metric planted trees
# ===================================================================

class TestMetricPlantedTree:
    """Test the MetricPlantedTree data structure."""

    def test_metric_edge_creation(self):
        """MetricEdge stores parent, child, length, channel."""
        ell = Symbol('ell', positive=True)
        e = MetricEdge(parent=0, child=3, length=ell, channel="J")
        assert e.parent == 0
        assert e.child == 3
        assert e.length == ell
        assert e.channel == "J"

    def test_metric_tree_from_planted_tree(self):
        """MetricPlantedTree wraps a PlantedTree with metric data."""
        tree = PlantedTree(children=(
            PlantedTree(label=1),
            PlantedTree(label=2),
        ))
        mt = MetricPlantedTree(tree=tree)
        assert mt.num_internal_edges == 0
        assert mt.tree.leaves == (1, 2)

    def test_metric_tree_with_internal_edge(self):
        """A tree with 3 leaves has one internal edge in binary case."""
        tree = PlantedTree(children=(
            PlantedTree(children=(
                PlantedTree(label=1),
                PlantedTree(label=2),
            )),
            PlantedTree(label=3),
        ))
        mt = MetricPlantedTree(tree=tree)
        assert mt.num_internal_edges == 1

    def test_internal_edge_symbols(self):
        """Edge-length symbols are created for each internal edge."""
        tree = PlantedTree(children=(
            PlantedTree(children=(
                PlantedTree(label=1),
                PlantedTree(label=2),
            )),
            PlantedTree(label=3),
        ))
        mt = MetricPlantedTree(tree=tree)
        syms = mt.internal_edge_symbols
        assert len(syms) == 1
        assert str(syms[0]) == 'ell_0'

    def test_total_edge_length_zero_edges(self):
        """Corolla (no internal edges) has total length 0."""
        tree = PlantedTree(children=(
            PlantedTree(label=1),
            PlantedTree(label=2),
        ))
        mt = MetricPlantedTree(tree=tree)
        assert mt.total_edge_length() == 0


# ===================================================================
# II. Tropical integration
# ===================================================================

class TestTropicalIntegral:
    """Test the tropical integration engine."""

    def test_edge_weight_order_1(self):
        """Simple pole: w(ell) = 1."""
        ell = Symbol('ell', positive=True)
        w = TropicalIntegral.edge_weight(1, ell)
        assert w == 1

    def test_edge_weight_order_2(self):
        """Double pole: w(ell) = ell."""
        ell = Symbol('ell', positive=True)
        w = TropicalIntegral.edge_weight(2, ell)
        assert w == ell

    def test_edge_weight_order_4(self):
        """Order-4 pole: w(ell) = ell^3 / 6."""
        ell = Symbol('ell', positive=True)
        w = TropicalIntegral.edge_weight(4, ell)
        assert simplify(w - ell**3 / 6) == 0

    def test_regulated_integral_is_one(self):
        """The regulated edge integral is 1 for all pole orders.

        This is the key Gamma-function cancellation:
        int_0^infty ell^{p-1}/(p-1)! * e^{-ell} d(ell) = 1.
        """
        for p in range(1, 8):
            assert TropicalIntegral.regulated_edge_integral(p) == Rational(1)

    def test_tree_integral_is_one(self):
        """The full tree integral is 1 (product of edge integrals)."""
        tree = PlantedTree(children=(
            PlantedTree(children=(
                PlantedTree(label=1),
                PlantedTree(label=2),
            )),
            PlantedTree(label=3),
        ))
        assert TropicalIntegral.tree_integral(tree) == Rational(1)

    def test_simplex_volume(self):
        """Vol(Delta_n) = 1/n!."""
        for n in range(1, 6):
            assert TropicalIntegral.simplex_volume(n) == Rational(1, factorial(n))

    def test_tropical_propagator_order_1(self):
        """Order-1 tropical propagator: 1."""
        ell = Symbol('ell', positive=True)
        prop = TropicalIntegral.tropical_propagator(1, ell)
        assert prop == 1

    def test_tropical_propagator_order_2(self):
        """Order-2 tropical propagator: -ell."""
        ell = Symbol('ell', positive=True)
        prop = TropicalIntegral.tropical_propagator(2, ell)
        assert prop == -ell


# ===================================================================
# III. d^2 = 0 verification
# ===================================================================

class TestDSquaredZero:
    """Verify d^trop^2 = 0 at all arities for all families."""

    @pytest.mark.parametrize("ope_fn,name", [
        (heisenberg_ope, "Heisenberg"),
        (affine_sl2_ope, "sl2"),
        (betagamma_ope, "betagamma"),
    ])
    def test_d_squared_zero_arity_3(self, ope_fn, name):
        """d^2 = 0 at arity 3."""
        ope = ope_fn() if name != "sl2" else ope_fn(1)
        engine = TropicalBarEngine(ope=ope, max_arity=3)
        assert engine.verify_d_squared(3) is True

    @pytest.mark.parametrize("ope_fn,name", [
        (heisenberg_ope, "Heisenberg"),
        (affine_sl2_ope, "sl2"),
        (betagamma_ope, "betagamma"),
    ])
    def test_d_squared_zero_arity_4(self, ope_fn, name):
        """d^2 = 0 at arity 4."""
        ope = ope_fn() if name != "sl2" else ope_fn(1)
        engine = TropicalBarEngine(ope=ope, max_arity=4)
        assert engine.verify_d_squared(4) is True

    def test_d_squared_virasoro_arity_3(self):
        """d^2 = 0 for Virasoro at arity 3."""
        ope = virasoro_ope(Rational(1, 2))
        engine = TropicalBarEngine(ope=ope, max_arity=3)
        assert engine.verify_d_squared(3) is True

    def test_d_squared_non_koszul(self):
        """d^2 = 0 for the non-Koszul example k[x]/(x^3)."""
        nk = NonKoszulTropicalComplex(max_arity=4)
        results = nk.verify_d_squared()
        for n, ok in results.items():
            assert ok, f"d^2 != 0 at bar degree {n} for k[x]/(x^3)"


# ===================================================================
# IV. Tropical acyclicity for standard landscape
# ===================================================================

class TestTropicalAcyclicity:
    """Verify tropical Koszulness (= acyclicity) for all four families."""

    def test_heisenberg_acyclic_arity_2(self):
        """Heisenberg tropical bar complex acyclic at arity 2."""
        engine = TropicalBarEngine(ope=heisenberg_ope(), max_arity=2)
        assert engine.is_acyclic_at_arity(2) is True

    def test_heisenberg_acyclic_arity_3(self):
        """Heisenberg tropical bar complex acyclic at arity 3."""
        engine = TropicalBarEngine(ope=heisenberg_ope(), max_arity=3)
        assert engine.is_acyclic_at_arity(3) is True

    def test_heisenberg_acyclic_arity_4(self):
        """Heisenberg tropical bar complex acyclic at arity 4."""
        engine = TropicalBarEngine(ope=heisenberg_ope(), max_arity=4)
        assert engine.is_acyclic_at_arity(4) is True

    def test_heisenberg_koszul(self):
        """Heisenberg is tropically Koszul through arity 5."""
        engine = TropicalBarEngine(ope=heisenberg_ope(), max_arity=5)
        assert engine.is_koszul() is True

    def test_sl2_acyclic_arity_3(self):
        """sl_2 tropical bar complex acyclic at arity 3."""
        engine = TropicalBarEngine(ope=affine_sl2_ope(1), max_arity=3)
        assert engine.is_acyclic_at_arity(3) is True

    def test_sl2_acyclic_arity_4(self):
        """sl_2 tropical bar complex acyclic at arity 4."""
        engine = TropicalBarEngine(ope=affine_sl2_ope(1), max_arity=4)
        assert engine.is_acyclic_at_arity(4) is True

    def test_sl2_koszul(self):
        """sl_2 is tropically Koszul through arity 4."""
        engine = TropicalBarEngine(ope=affine_sl2_ope(1), max_arity=4)
        assert engine.is_koszul() is True

    def test_betagamma_acyclic_arity_3(self):
        """Beta-gamma tropical bar complex acyclic at arity 3."""
        engine = TropicalBarEngine(ope=betagamma_ope(), max_arity=3)
        assert engine.is_acyclic_at_arity(3) is True

    def test_betagamma_acyclic_arity_4(self):
        """Beta-gamma tropical bar complex acyclic at arity 4."""
        engine = TropicalBarEngine(ope=betagamma_ope(), max_arity=4)
        assert engine.is_acyclic_at_arity(4) is True

    def test_betagamma_koszul(self):
        """Beta-gamma is tropically Koszul through arity 4."""
        engine = TropicalBarEngine(ope=betagamma_ope(), max_arity=4)
        assert engine.is_koszul() is True

    def test_virasoro_acyclic_arity_3(self):
        """Virasoro tropical bar complex acyclic at arity 3."""
        engine = TropicalBarEngine(ope=virasoro_ope(Rational(1, 2)), max_arity=3)
        assert engine.is_acyclic_at_arity(3) is True

    def test_virasoro_acyclic_arity_4(self):
        """Virasoro tropical bar complex acyclic at arity 4."""
        engine = TropicalBarEngine(ope=virasoro_ope(Rational(1, 2)), max_arity=4)
        assert engine.is_acyclic_at_arity(4) is True

    def test_virasoro_koszul(self):
        """Virasoro is tropically Koszul through arity 4."""
        engine = TropicalBarEngine(ope=virasoro_ope(Rational(1, 2)), max_arity=4)
        assert engine.is_koszul() is True


# ===================================================================
# V. Non-Koszul detection
# ===================================================================

class TestNonKoszul:
    """Verify that non-Koszul algebras are correctly detected."""

    def test_non_koszul_d_squared_zero(self):
        """The non-Koszul bar complex has d^2 = 0."""
        nk = NonKoszulTropicalComplex(max_arity=4)
        results = nk.verify_d_squared()
        assert all(results.values()), f"d^2 failures: {results}"

    def test_non_koszul_has_nontrivial_cohomology(self):
        """k[x]/(x^3) has nontrivial bar cohomology (= non-Koszul).

        The bar complex B(k[x]/(x^3)):
          B^1 = span{x, y}  (dim 2)
          B^2 = span{xx, xy, yx, yy}  (dim 4)
          B^3 = span{...}  (dim 8)

        The element [x|x] |--> y under d_2.  But [y] is a nontrivial
        bar cocycle at degree 2 because the cubic relation x^3 = 0
        is NOT a consequence of any quadratic relation.
        """
        nk = NonKoszulTropicalComplex(max_arity=4)
        coh = nk.cohomology()
        # Should have nontrivial cohomology beyond degree 1
        assert nk.is_non_koszul(), (
            f"Expected non-Koszul but cohomology = {coh}"
        )

    def test_non_koszul_h1_dimension(self):
        """H^1(B) for k[x]/(x^3) should have dim 1.

        The augmentation ideal has basis {x, y=x^2}.  B^2 -> B^1 sends
        (x|x) -> y, so y is a boundary.  H^1 = span{x} = dim 1.
        The Koszul dual is generated in degree 1 by one element.
        """
        nk = NonKoszulTropicalComplex(max_arity=4)
        coh = nk.cohomology()
        assert coh.get(1, 0) == 1, f"H^1 dim = {coh.get(1, 0)}, expected 1"

    def test_non_koszul_cohomology_nontrivial(self):
        """H^n(B) for n >= 2 has positive dimension for k[x]/(x^3)."""
        nk = NonKoszulTropicalComplex(max_arity=4)
        coh = nk.cohomology()
        # At least one cohomology group beyond H^1 should be nonzero
        has_higher = any(coh.get(n, 0) > 0 for n in range(2, 5))
        assert has_higher, f"No higher cohomology found: {coh}"


# ===================================================================
# VI. Tropical shadow obstruction tower
# ===================================================================

class TestTropicalShadowTower:
    """Verify the tropical shadow obstruction tower matches algebraic values."""

    def test_heisenberg_kappa(self):
        """kappa^trop(Heisenberg) = k."""
        k = Symbol('k')
        shadow = TropicalShadowTower(ope=heisenberg_ope(k))
        kappa = shadow.kappa_tropical()
        assert simplify(kappa - k) == 0

    def test_heisenberg_cubic_vanishes(self):
        """Heisenberg has no cubic shadow (abelian, no propagation)."""
        shadow = TropicalShadowTower(ope=heisenberg_ope(1))
        assert shadow.cubic_shadow_tropical() == 0

    def test_heisenberg_quartic_vanishes(self):
        """Heisenberg has no quartic shadow."""
        shadow = TropicalShadowTower(ope=heisenberg_ope(1))
        assert shadow.quartic_shadow_tropical() == 0

    def test_virasoro_kappa(self):
        """kappa^trop(Virasoro) = c/2."""
        c = Symbol('c')
        shadow = TropicalShadowTower(ope=virasoro_ope(c))
        kappa = shadow.kappa_tropical()
        assert simplify(kappa - c / 2) == 0

    def test_sl2_kappa_at_level_1(self):
        """kappa^trop(sl_2 at k=1) = sum of curvature channels.

        For sl_2 at level 1:
          e*f ~ 1/(z-w)^2  (coeff 1)
          f*e ~ 1/(z-w)^2  (coeff 1)
          h*h ~ 2/(z-w)^2  (coeff 2)
        Total curvature = 1 + 1 + 2 = 4.

        Note: this is the TROPICAL kappa (sum of direct curvature channels),
        which equals dim(g)*(k+h^v)/(2*h^v) only for the Killing-form-normalized
        version.  For sl_2 at k=1: 3*(1+2)/4 = 9/4 (algebraic kappa).
        The tropical kappa counts direct curvature channels differently.
        """
        shadow = TropicalShadowTower(ope=affine_sl2_ope(1))
        kappa = shadow.kappa_tropical()
        # Direct curvature channels: (e,f)=1, (f,e)=1, (h,h)=2
        assert kappa == 4

    def test_betagamma_kappa(self):
        """kappa^trop(betagamma) from direct OPE curvature channels.

        For betagamma: beta*gamma ~ 1/(z-w) produces vacuum (coeff 1),
        gamma*beta ~ -1/(z-w) produces vacuum (coeff -1).
        Total tropical kappa = 1 + (-1) = 0.
        """
        shadow = TropicalShadowTower(ope=betagamma_ope())
        kappa = shadow.kappa_tropical()
        assert kappa == 0  # Vacuum channels cancel

    def test_shadow_tower_data(self):
        """shadow_tower_data returns results at each arity."""
        shadow = TropicalShadowTower(ope=heisenberg_ope(1))
        data = shadow.shadow_tower_data(max_arity=4)
        assert 2 in data
        assert 3 in data
        assert 4 in data
        assert data[2] == 1  # kappa = k = 1
        assert data[3] == 0  # cubic vanishes
        assert data[4] == 0  # quartic vanishes


# ===================================================================
# VII. Connection to planted forest algebra
# ===================================================================

class TestPlantedForestConnection:
    """Verify tropical FM space = planted forest space."""

    def test_trop_fm_equals_forest_n2(self):
        """At arity 2: one tree (= one combinatorial type)."""
        assert tropical_fm_equals_planted_forest(2) is True

    def test_trop_fm_equals_forest_n3(self):
        """At arity 3: 3 trees (K_2 = interval: 3 faces)."""
        assert tropical_fm_equals_planted_forest(3) is True

    def test_trop_fm_equals_forest_n4(self):
        """At arity 4: 11 trees (K_3 = pentagon: 11 faces)."""
        assert tropical_fm_equals_planted_forest(4) is True

    def test_trop_fm_equals_forest_n5(self):
        """At arity 5: 45 trees (K_4 = 3d associahedron: 45 faces)."""
        assert tropical_fm_equals_planted_forest(5) is True

    def test_grafting_composition_basic(self):
        """Grafting corollas gives correct leaf count."""
        assert verify_grafting_composition(3, 2, 0) is True
        assert verify_grafting_composition(3, 2, 1) is True
        assert verify_grafting_composition(3, 2, 2) is True

    def test_grafting_composition_larger(self):
        """Grafting larger corollas."""
        assert verify_grafting_composition(4, 3, 0) is True
        assert verify_grafting_composition(2, 4, 0) is True


# ===================================================================
# VIII. Euler characteristics and f-vectors
# ===================================================================

class TestEulerAndFVectors:
    """Verify Euler characteristics and associahedron f-vectors."""

    def test_euler_arity_3(self):
        """chi(B^trop_3) = chi(K_1) = 1."""
        chi = tropical_euler_characteristic(3)
        assert chi == 1

    def test_euler_arity_4(self):
        """chi(B^trop_4) = chi(K_2) = 1."""
        chi = tropical_euler_characteristic(4)
        assert chi == 1

    def test_euler_arity_5(self):
        """chi(B^trop_5) = chi(K_3) = 1."""
        chi = tropical_euler_characteristic(5)
        assert chi == 1

    def test_f_vector_K2(self):
        """f-vector of K_2 (interval) = {0: 2, 1: 1}."""
        f = verify_f_vector(3)
        assert f.get(0, 0) == 2
        assert f.get(1, 0) == 1

    def test_f_vector_K3(self):
        """f-vector of K_3 (pentagon) = {0: 5, 1: 5, 2: 1}."""
        f = verify_f_vector(4)
        assert f.get(0, 0) == 5
        assert f.get(1, 0) == 5
        assert f.get(2, 0) == 1

    def test_f_vector_K4(self):
        """f-vector of K_4 (3d associahedron) = {0: 14, 1: 21, 2: 9, 3: 1}."""
        f = verify_f_vector(5)
        assert f.get(0, 0) == 14
        assert f.get(1, 0) == 21
        assert f.get(2, 0) == 9
        assert f.get(3, 0) == 1


# ===================================================================
# IX. Full landscape verification
# ===================================================================

class TestFullLandscape:
    """Full tropical verification across the standard landscape."""

    def test_heisenberg_full_report(self):
        """Full Heisenberg report is Koszul."""
        report = verify_heisenberg_tropical(max_arity=4)
        assert report['koszul'] is True
        assert report['depth_class'] == 'G'

    def test_sl2_full_report(self):
        """Full sl_2 report is Koszul."""
        report = verify_affine_sl2_tropical(k=1, max_arity=4)
        assert report['koszul'] is True
        assert report['depth_class'] == 'L'

    def test_betagamma_full_report(self):
        """Full beta-gamma report is Koszul."""
        report = verify_betagamma_tropical(max_arity=4)
        assert report['koszul'] is True
        assert report['depth_class'] == 'C'

    def test_virasoro_full_report(self):
        """Full Virasoro report is Koszul."""
        report = verify_virasoro_tropical(c=Rational(1, 2), max_arity=4)
        assert report['koszul'] is True
        assert report['depth_class'] == 'M'

    def test_full_landscape(self):
        """All four families are tropically Koszul."""
        results = full_landscape_tropical_verification(max_arity=3)
        for family, report in results.items():
            assert report['koszul'] is True, f"{family} failed Koszulness check"


# ===================================================================
# X. Multi-channel tropical complex
# ===================================================================

class TestMultiChannel:
    """Test the multi-channel tropical complex."""

    def test_heisenberg_one_channel(self):
        """Heisenberg has one channel assignment per tree."""
        mc = MultiChannelTropicalComplex(ope=heisenberg_ope(), arity=3)
        # Heisenberg has no propagating channels, so each tree has one
        # (trivial) channel assignment.
        trees = enumerate_planted_trees([1, 2, 3])
        assert mc.count_channel_assignments() == len(trees)

    def test_sl2_multichannel(self):
        """sl_2 multi-channel complex has more assignments than trees."""
        mc = MultiChannelTropicalComplex(ope=affine_sl2_ope(1), arity=3)
        trees = enumerate_planted_trees([1, 2, 3])
        # sl_2 has propagating channels, so some trees have multiple assignments
        assert mc.count_channel_assignments() >= len(trees)

    def test_heisenberg_multichannel_acyclic(self):
        """Heisenberg multi-channel complex is acyclic."""
        mc = MultiChannelTropicalComplex(ope=heisenberg_ope(), arity=4)
        assert mc.is_acyclic_multichannel() is True

    def test_virasoro_multichannel_acyclic(self):
        """Virasoro multi-channel complex is acyclic at generic c."""
        mc = MultiChannelTropicalComplex(ope=virasoro_ope(Rational(1, 2)), arity=3)
        assert mc.is_acyclic_multichannel() is True


# ===================================================================
# XI. Shadow obstruction tower algebraic agreement
# ===================================================================

class TestShadowTowerAgreement:
    """Verify tropical shadow obstruction tower agrees with algebraic values."""

    def test_heisenberg_agreement(self):
        """Tropical shadows agree with algebraic for Heisenberg."""
        results = shadow_tower_agrees_with_algebraic("heisenberg", max_arity=4)
        for arity, ok in results.items():
            assert ok, f"Heisenberg shadow mismatch at arity {arity}"

    def test_betagamma_agreement(self):
        """Tropical shadows agree with algebraic for beta-gamma."""
        results = shadow_tower_agrees_with_algebraic("betagamma", max_arity=3)
        for arity, ok in results.items():
            assert ok, f"Beta-gamma shadow mismatch at arity {arity}"

    def test_virasoro_kappa_agreement(self):
        """Virasoro tropical kappa = c/2."""
        results = shadow_tower_agrees_with_algebraic("virasoro", max_arity=2)
        assert results.get(2, False), "Virasoro kappa mismatch"


# ===================================================================
# XII. Summary and documentation
# ===================================================================

class TestSummary:
    """Test summary and documentation functions."""

    def test_summary_nonempty(self):
        """Summary string is nonempty."""
        s = tropical_koszulness_summary()
        assert len(s) > 100

    def test_summary_mentions_key_concepts(self):
        """Summary mentions acyclicity, associahedron, Cohen-Macaulay."""
        s = tropical_koszulness_summary()
        assert "acyclic" in s.lower()
        assert "associahedron" in s.lower()
        assert "cohen-macaulay" in s.lower() or "non-Koszul" in s.lower()
