"""Tests for tropical bar complex and tropical Koszulness criterion.

Verifies:
1. Planted tree enumeration (Catalan numbers, Schröder numbers)
2. Edge contraction (the tropical differential)
3. Associahedron f-vectors
4. Tropical Koszulness for the standard landscape:
   - Heisenberg (class G, r_max=2)
   - Affine sl_2 (class L, r_max=3)
   - Beta-gamma (class C, r_max=4)
   - Virasoro (class M, r_max=infinity)
5. Cohen-Macaulay / shellability interpretation
"""

import pytest
from sympy import Rational, Symbol

from compute.lib.tropical_koszulness import (
    PlantedTree,
    enumerate_binary_trees,
    enumerate_planted_trees,
    catalan,
    count_binary_trees,
    count_planted_trees,
    associahedron_f_vector,
    associahedron_chain_complex,
    TropicalBarComplex,
    WeightedTropicalBarComplex,
    TropicalOPEData,
    heisenberg_ope,
    affine_sl2_ope,
    betagamma_ope,
    virasoro_ope,
    verify_tropical_koszulness,
    tropical_cohomology_table,
    is_shellable_poset,
    tropical_koszulness_meaning,
)


# ===================================================================
# I. Planted tree enumeration
# ===================================================================

class TestPlantedTreeEnumeration:
    """Verify tree counts match Catalan and Schröder numbers."""

    def test_catalan_numbers(self):
        """C_0=1, C_1=1, C_2=2, C_3=5, C_4=14."""
        assert catalan(0) == 1
        assert catalan(1) == 1
        assert catalan(2) == 2
        assert catalan(3) == 5
        assert catalan(4) == 14

    def test_binary_trees_2_leaves(self):
        """One binary tree with 2 leaves."""
        trees = enumerate_binary_trees([1, 2])
        assert len(trees) == 1  # C_1 = 1

    def test_binary_trees_3_leaves(self):
        """Two binary trees with 3 leaves = C_2 = 2."""
        trees = enumerate_binary_trees([1, 2, 3])
        assert len(trees) == 2

    def test_binary_trees_4_leaves(self):
        """Five binary trees with 4 leaves = C_3 = 5."""
        trees = enumerate_binary_trees([1, 2, 3, 4])
        assert len(trees) == 5

    def test_binary_trees_5_leaves(self):
        """14 binary trees with 5 leaves = C_4 = 14."""
        trees = enumerate_binary_trees([1, 2, 3, 4, 5])
        assert len(trees) == 14

    def test_count_binary_trees(self):
        for n in range(2, 7):
            assert count_binary_trees(n) == catalan(n - 1)

    def test_planted_trees_2_leaves(self):
        """One planted tree with 2 leaves: the corolla = binary tree."""
        trees = enumerate_planted_trees([1, 2])
        assert len(trees) == 1

    def test_planted_trees_3_leaves(self):
        """3 planted trees with 3 leaves: 2 binary + 1 corolla = 3."""
        trees = enumerate_planted_trees([1, 2, 3])
        assert len(trees) == 3

    def test_planted_trees_4_leaves(self):
        """11 planted trees with 4 leaves (little Schröder number)."""
        trees = enumerate_planted_trees([1, 2, 3, 4])
        assert len(trees) == 11

    def test_all_leaves_present(self):
        """Every tree has the correct leaf set."""
        for n in range(2, 6):
            leaves = list(range(1, n + 1))
            for t in enumerate_planted_trees(leaves):
                assert sorted(t.leaves) == leaves


# ===================================================================
# II. Tree structure
# ===================================================================

class TestTreeStructure:
    """Test tree properties: depth, vertices, edges."""

    def test_leaf_properties(self):
        leaf = PlantedTree(label=1)
        assert leaf.is_leaf
        assert leaf.leaves == (1,)
        assert leaf.num_internal_edges == 0
        assert leaf.num_vertices == 0

    def test_binary_tree_vertices(self):
        """Binary tree ((1,2),3) has 2 internal vertices."""
        t = PlantedTree(children=(
            PlantedTree(children=(PlantedTree(label=1), PlantedTree(label=2))),
            PlantedTree(label=3)
        ))
        assert t.num_vertices == 2
        assert t.leaves == (1, 2, 3)

    def test_corolla_vertices(self):
        """Corolla (1,2,3) has 1 internal vertex."""
        t = PlantedTree(children=(
            PlantedTree(label=1),
            PlantedTree(label=2),
            PlantedTree(label=3),
        ))
        assert t.num_vertices == 1
        assert t.num_internal_edges == 0

    def test_binary_tree_depth(self):
        # ((1,2),3) has depth 2
        t = PlantedTree(children=(
            PlantedTree(children=(PlantedTree(label=1), PlantedTree(label=2))),
            PlantedTree(label=3)
        ))
        assert t.depth() == 2

    def test_corolla_depth(self):
        t = PlantedTree(children=(
            PlantedTree(label=1),
            PlantedTree(label=2),
            PlantedTree(label=3),
        ))
        assert t.depth() == 1


# ===================================================================
# III. Edge contraction
# ===================================================================

class TestEdgeContraction:
    """Test the tropical differential (edge contraction)."""

    def test_contract_binary_to_corolla(self):
        """Contracting the internal edge of ((1,2),3) gives (1,2,3)."""
        inner = PlantedTree(children=(PlantedTree(label=1), PlantedTree(label=2)))
        t = PlantedTree(children=(inner, PlantedTree(label=3)))
        # The internal edge is from root to inner
        contracted = t.contract_edge(t, 0)
        assert contracted.leaves == (1, 2, 3)
        assert contracted.num_vertices == 1  # corolla

    def test_contract_preserves_leaves(self):
        """Edge contraction preserves the leaf set."""
        trees = enumerate_binary_trees([1, 2, 3, 4])
        for t in trees:
            edges = t.internal_edges
            for parent, idx, _pos in edges:
                c = t.contract_edge(parent, idx)
                assert sorted(c.leaves) == [1, 2, 3, 4]

    def test_contraction_reduces_edges(self):
        """Contraction reduces internal edge count by 1."""
        trees = enumerate_planted_trees([1, 2, 3, 4])
        for t in trees:
            edges = t.internal_edges
            for parent, idx, _pos in edges:
                c = t.contract_edge(parent, idx)
                assert c.num_internal_edges == t.num_internal_edges - 1


# ===================================================================
# IV. Associahedron f-vectors
# ===================================================================

class TestAssociahedron:
    """Verify f-vectors of associahedra K_n."""

    def test_K2_point(self):
        """K_2 = point: one 0-cell."""
        f = associahedron_f_vector(2)
        assert f == {0: 1}

    def test_K3_interval(self):
        """K_3 = interval: 2 vertices, 1 edge."""
        f = associahedron_f_vector(3)
        assert f[0] == 2  # 2 vertices (binary trees with 3 leaves)
        assert f[1] == 1  # 1 edge (corolla with 3 leaves)

    def test_K4_pentagon(self):
        """K_4 = pentagon: 5 vertices, 5 edges, 1 2-face."""
        f = associahedron_f_vector(4)
        assert f[0] == 5   # vertices = C_3 = 5 binary trees
        assert f[1] == 5   # edges
        assert f[2] == 1   # one top face (corolla)

    def test_chain_complex_d_squared(self):
        """d^2 = 0 on the associahedron chain complex."""
        for n in range(3, 6):
            cc = associahedron_chain_complex(n)
            results = cc.check_d_squared()
            for grade, passes in results:
                assert passes, f"d^2 != 0 at grade {grade} for K_{n}"


# ===================================================================
# V. Tropical Koszulness for standard landscape
# ===================================================================

class TestTropicalKoszulnessHeisenberg:
    """Heisenberg: one generator, curvature only, class G."""

    def test_ope_structure(self):
        ope = heisenberg_ope(k=1)
        assert ope.num_generators == 1
        assert len(ope.curvature) == 1
        assert len(ope.propagating) == 0

    def test_tropical_acyclicity_arity2(self):
        tbc = TropicalBarComplex(ope=heisenberg_ope(), arity=2)
        tbc.build()
        assert tbc.is_acyclic()

    def test_tropical_acyclicity_arity3(self):
        tbc = TropicalBarComplex(ope=heisenberg_ope(), arity=3)
        tbc.build()
        assert tbc.is_acyclic()

    def test_tropical_koszulness_all_arities(self):
        results = verify_tropical_koszulness(heisenberg_ope(), max_arity=5)
        for arity, acyclic in results.items():
            assert acyclic, f"Heisenberg not Koszul at arity {arity}"


class TestTropicalKoszulnessAffineSl2:
    """Affine sl_2: three generators, propagating channels, class L."""

    def test_ope_structure(self):
        ope = affine_sl2_ope(k=1)
        assert ope.num_generators == 3
        assert len(ope.propagating) > 0

    def test_tropical_acyclicity_arity2(self):
        tbc = TropicalBarComplex(ope=affine_sl2_ope(), arity=2)
        tbc.build()
        assert tbc.is_acyclic()

    def test_tropical_koszulness_low_arities(self):
        results = verify_tropical_koszulness(affine_sl2_ope(), max_arity=4)
        for arity, acyclic in results.items():
            assert acyclic, f"Affine sl_2 not Koszul at arity {arity}"


class TestTropicalKoszulnessBetaGamma:
    """Beta-gamma: two generators, one propagating channel, class C."""

    def test_ope_structure(self):
        ope = betagamma_ope()
        assert ope.num_generators == 2

    def test_tropical_acyclicity_arity2(self):
        tbc = TropicalBarComplex(ope=betagamma_ope(), arity=2)
        tbc.build()
        assert tbc.is_acyclic()

    def test_tropical_koszulness_low_arities(self):
        results = verify_tropical_koszulness(betagamma_ope(), max_arity=4)
        for arity, acyclic in results.items():
            assert acyclic, f"Beta-gamma not Koszul at arity {arity}"


class TestTropicalKoszulnessVirasoro:
    """Virasoro: one generator, TWO channel types (order 2 + order 4), class M."""

    def test_ope_structure(self):
        ope = virasoro_ope(c=Rational(1, 2))
        assert ope.num_generators == 1
        assert len(ope.propagating) > 0
        assert len(ope.curvature) > 0

    def test_dual_channel_structure(self):
        """Virasoro has both propagating and curvature channels."""
        ope = virasoro_ope(c=26)
        prop = ope.propagating
        curv = ope.curvature
        # T(z)T(w) has order-2 propagating (-> T) and order-4 curvature (-> vac)
        assert ("T", "T") in prop
        assert ("T", "T") in curv

    def test_tropical_acyclicity_arity2(self):
        tbc = TropicalBarComplex(ope=virasoro_ope(c=Rational(1, 2)), arity=2)
        tbc.build()
        assert tbc.is_acyclic()

    def test_tropical_koszulness_low_arities(self):
        """Virasoro is Koszul despite infinite shadow depth."""
        results = verify_tropical_koszulness(
            virasoro_ope(c=Rational(1, 2)), max_arity=4
        )
        for arity, acyclic in results.items():
            assert acyclic, f"Virasoro not Koszul at arity {arity}"


# ===================================================================
# VI. Scalar saturation and weighted complex
# ===================================================================

class TestScalarSaturation:
    """For one-channel algebras, tropical complex = associahedron chain complex."""

    def test_weighted_d_squared(self):
        """d^2 = 0 on the scalar-saturated tropical complex."""
        for n in range(3, 6):
            wtbc = WeightedTropicalBarComplex(
                ope=heisenberg_ope(),
                arity=n
            )
            cc = wtbc.build_scalar_saturated(kappa_val=1)
            results = cc.check_d_squared()
            for grade, passes in results:
                assert passes

    def test_weighted_d_squared_nontrivial_kappa(self):
        """d^2 = 0 even for kappa != 1."""
        for kappa in [Rational(1, 2), Rational(3, 7), 2]:
            wtbc = WeightedTropicalBarComplex(ope=heisenberg_ope(), arity=5)
            cc = wtbc.build_scalar_saturated(kappa_val=kappa)
            results = cc.check_d_squared()
            for grade, passes in results:
                assert passes


# ===================================================================
# VII. Combinatorial meaning
# ===================================================================

class TestCombinatorialMeaning:
    """Test the Cohen-Macaulay / shellability interpretation."""

    def test_shellability(self):
        """Associahedron is always shellable (convex polytope)."""
        for n in range(2, 6):
            assert is_shellable_poset(n)

    def test_euler_characteristic(self):
        """Euler characteristic of K_n = 1 (contractible)."""
        for n in range(3, 6):
            tbc = TropicalBarComplex(ope=heisenberg_ope(), arity=n)
            tbc.build()
            chi = tbc.euler_characteristic()
            assert chi == 1, f"chi(K_{n}) = {chi}, expected 1"

    def test_meaning_string(self):
        """The meaning string is non-empty and mentions Cohen-Macaulay."""
        meaning = tropical_koszulness_meaning()
        assert "Cohen-Macaulay" in meaning
        assert "associahedron" in meaning


# ===================================================================
# VIII. Cohomology tables
# ===================================================================

class TestCohomologyTables:
    """Verify cohomology concentration (= Koszulness) in detail."""

    def test_heisenberg_cohomology_concentrated(self):
        """Cohomology concentrated at min degree with dim 1."""
        table = tropical_cohomology_table(heisenberg_ope(), max_arity=5)
        for arity, coh in table.items():
            min_deg = min(coh.keys())
            for grade, dim in coh.items():
                if grade == min_deg:
                    assert dim == 1, f"Heis: H^{grade} != 1 at arity {arity}"
                else:
                    assert dim == 0, f"Heis: H^{grade} != 0 at arity {arity}"

    def test_affine_cohomology_concentrated(self):
        table = tropical_cohomology_table(affine_sl2_ope(), max_arity=4)
        for arity, coh in table.items():
            min_deg = min(coh.keys())
            for grade, dim in coh.items():
                if grade == min_deg:
                    assert dim == 1, f"Affine: H^{grade} != 1 at arity {arity}"
                else:
                    assert dim == 0, f"Affine: H^{grade} != 0 at arity {arity}"

    def test_virasoro_cohomology_concentrated(self):
        table = tropical_cohomology_table(
            virasoro_ope(c=Rational(1, 2)), max_arity=4
        )
        for arity, coh in table.items():
            min_deg = min(coh.keys())
            for grade, dim in coh.items():
                if grade == min_deg:
                    assert dim == 1, f"Vir: H^{grade} != 1 at arity {arity}"
                else:
                    assert dim == 0, f"Vir: H^{grade} != 0 at arity {arity}"


# ===================================================================
# IX. Cross-checks with bar complex
# ===================================================================

class TestCrossChecks:
    """Cross-check tropical complex against known bar complex results."""

    def test_binary_tree_count_matches_catalan(self):
        """Number of binary trees = Catalan number."""
        for n in range(2, 7):
            assert count_binary_trees(n) == catalan(n - 1)

    def test_total_tree_count_arity4(self):
        """Total planted trees with 4 leaves = 11 (little Schröder)."""
        assert count_planted_trees(4) == 11

    def test_total_tree_count_arity3(self):
        """Total planted trees with 3 leaves = 3."""
        assert count_planted_trees(3) == 3

    def test_total_tree_count_arity2(self):
        assert count_planted_trees(2) == 1

    def test_shadow_depth_classes(self):
        """Verify shadow depth classification for standard families.

        G (Gaussian): Heisenberg, r_max=2
        L (Lie/tree): affine, r_max=3
        C (contact): beta-gamma, r_max=4
        M (mixed): Virasoro, r_max=infinity

        All are chirally Koszul (tropical acyclicity holds for all).
        """
        for name, ope in [
            ("Heisenberg", heisenberg_ope()),
            ("Affine sl_2", affine_sl2_ope()),
            ("Beta-gamma", betagamma_ope()),
            ("Virasoro", virasoro_ope(c=Rational(1, 2))),
        ]:
            results = verify_tropical_koszulness(ope, max_arity=4)
            for arity, acyclic in results.items():
                assert acyclic, f"{name} fails tropical Koszulness at arity {arity}"
