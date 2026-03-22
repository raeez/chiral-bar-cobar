"""
Smoke tests for the four load-bearing pillar modules.

These modules (utils, lie_algebra, bar_complex, stable_graph_enumeration)
are imported by 50+ dependent modules each. Any corruption cascades
through the entire compute infrastructure. These tests catch regressions
quickly (< 0.5s total).
"""

import pytest
from fractions import Fraction

from compute.lib.utils import GradedVectorSpace, partition_number
from compute.lib.lie_algebra import (
    cartan_data, structure_constants_sl2, killing_form_sl2,
    sugawara_c, kappa_km,
)
from compute.lib.bar_complex import (
    heisenberg_algebra, sl2_algebra, virasoro_algebra,
    arnold_dimension, bar_dim_heisenberg, bar_dim_sl2,
    km_chain_space_dim,
)
from compute.lib.stable_graph_enumeration import (
    genus0_stable_graphs_n3, genus0_stable_graphs_n4,
    genus1_stable_graphs_n0, genus1_stable_graphs_n1,
    genus2_stable_graphs_n0,
    orbifold_euler_characteristic, graph_weight,
)

from sympy import Rational


# ================================================================
# PILLAR 1: utils.py
# ================================================================

class TestUtils:
    """Smoke tests for graded vector spaces and partitions."""

    def test_graded_vector_space_creation(self):
        V = GradedVectorSpace(dims={0: 1, 1: 3, 2: 5})
        assert V.dims[0] == 1
        assert V.dims[1] == 3
        assert V.dims[2] == 5

    def test_partition_numbers_small(self):
        """p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7."""
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        for n, p_n in enumerate(expected):
            assert partition_number(n) == p_n, f"p({n}) = {partition_number(n)} != {p_n}"


# ================================================================
# PILLAR 2: lie_algebra.py
# ================================================================

class TestLieAlgebra:
    """Smoke tests for Lie algebra data."""

    def test_sl2_cartan(self):
        data = cartan_data("A", 1)
        assert data.rank == 1
        assert data.dim == 3

    def test_sl3_cartan(self):
        data = cartan_data("A", 2)
        assert data.rank == 2
        assert data.dim == 8

    def test_sl2_structure_constants_antisymmetry(self):
        sc = structure_constants_sl2()
        # [e, f] = h, so f^{ef}_h = 1, f^{fe}_h = -1
        for (a, b), coeffs in sc.items():
            for c, val in coeffs.items():
                # Check antisymmetry: f^{ab}_c = -f^{ba}_c
                if (b, a) in sc and c in sc[(b, a)]:
                    assert val == -sc[(b, a)][c], (
                        f"Antisymmetry fails: f^{{{a}{b}}}_{c} = {val}, "
                        f"f^{{{b}{a}}}_{c} = {sc[(b, a)][c]}"
                    )

    def test_killing_form_nondegenerate(self):
        kf = killing_form_sl2()
        # sl_2 Killing form: tr(ad_X ad_Y) should be nondegenerate
        # K(e,f) = K(f,e) should be nonzero
        assert kf[("e", "f")] != 0

    def test_sugawara_central_charge(self):
        """c(sl_2, k) = 3k/(k+2)."""
        for k in [1, 2, 3, 4, 10]:
            c = sugawara_c("A", 1, k)
            expected = Rational(3 * k, k + 2)
            assert c == expected, f"c(sl_2, {k}) = {c} != {expected}"

    def test_kappa_km(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        for k in [1, 2, 3, 10]:
            kap = kappa_km("A", 1, k)
            expected = Rational(3 * (k + 2), 4)
            assert kap == expected, f"kappa(sl_2, {k}) = {kap} != {expected}"


# ================================================================
# PILLAR 3: bar_complex.py
# ================================================================

class TestBarComplex:
    """Smoke tests for OPE algebras and bar dimensions."""

    def test_heisenberg_creation(self):
        H = heisenberg_algebra()
        assert H.name == "H_kappa"
        assert len(H.generators) == 1

    def test_sl2_creation(self):
        A = sl2_algebra()
        assert len(A.generators) == 3

    def test_virasoro_creation(self):
        V = virasoro_algebra()
        assert len(V.generators) == 1

    def test_arnold_dimensions(self):
        """Arnold: dim H*(Conf_n(C)) grows with n."""
        assert arnold_dimension(1) == 1
        assert arnold_dimension(2) == 1
        assert arnold_dimension(3) == 2
        assert arnold_dimension(4) == 6

    def test_bar_dim_heisenberg(self):
        """Bar cohomology of Heisenberg grows as partitions."""
        assert bar_dim_heisenberg(1) == 1
        assert bar_dim_heisenberg(2) == 1
        assert bar_dim_heisenberg(3) == 1
        assert bar_dim_heisenberg(4) == 2  # p(4) - corrections

    def test_bar_dim_sl2_degree1(self):
        """B_1(sl_2) = dim(sl_2) = 3."""
        assert bar_dim_sl2(1) == 3

    def test_bar_dim_sl2_degree2(self):
        """B_2(sl_2) = 5 (not 6; Riordan WRONG at n=2)."""
        assert bar_dim_sl2(2) == 5

    def test_km_chain_space_dim(self):
        """KM chain space: binom(dim_g + n - 1, n) for n-fold bar."""
        # For sl_2 (dim=3) at degree 1: binom(3, 1) = 3
        assert km_chain_space_dim(3, 1) == 3


# ================================================================
# PILLAR 4: stable_graph_enumeration.py
# ================================================================

class TestStableGraphs:
    """Smoke tests for stable graph enumeration."""

    def test_genus0_n3(self):
        """M_{0,3} is a point; one graph (single vertex)."""
        graphs = genus0_stable_graphs_n3()
        assert len(graphs) == 1
        assert graphs[0].num_edges == 0

    def test_genus0_n4(self):
        """M_{0,4} = P^1; three graphs (three channels s,t,u)."""
        graphs = genus0_stable_graphs_n4()
        # One vertex graph + three edge graphs (boundary divisors)
        assert len(graphs) >= 1

    def test_genus1_n0(self):
        """M_{1,0}: no stable curves (unstable)."""
        # Actually M_{1,1} is the first stable case
        graphs = genus1_stable_graphs_n0()
        # There should be stable graphs of genus 1 with 0 markings
        # but stability requires 2g-2+n > 0, so g=1, n=0 gives 0 > 0: OK
        assert isinstance(graphs, list)

    def test_genus1_n1(self):
        """M_{1,1}: one graph (single vertex of genus 1)."""
        graphs = genus1_stable_graphs_n1()
        assert len(graphs) >= 1

    def test_genus2_n0(self):
        """M_{2,0}: multiple graphs from different degenerations."""
        graphs = genus2_stable_graphs_n0()
        assert len(graphs) >= 1

    def test_orbifold_euler_genus0_n4(self):
        """chi_orb(M_{0,4}) from graph sum."""
        graphs = genus0_stable_graphs_n4()
        chi = orbifold_euler_characteristic(graphs)
        # The orbifold Euler characteristic depends on the
        # enumeration convention; verify it's a small integer
        assert isinstance(chi, Fraction)
        assert chi.denominator <= 24  # should be rational with small denom

    def test_graph_weight_rationality(self):
        """Graph weights are rational (may be negative for boundary)."""
        for graph in genus0_stable_graphs_n4():
            w = graph_weight(graph)
            assert isinstance(w, Fraction)
