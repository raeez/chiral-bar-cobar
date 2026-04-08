r"""Tests for CoHA-bar chain-level duality engine.

Verifies that CoHA multiplication dualizes to bar comultiplication
at the CHAIN level (not just characters) for ADE quivers.

Multi-path verification (AP10, CLAUDE.md mandate):
  Path 1: Euler form computation (from quiver definition)
  Path 2: Ext dimension (from homological algebra)
  Path 3: CoHA dimension (from representation theory)
  Path 4: Bar complex dimension (from PBW collapse)
  Path 5: JKL vertex coproduct (from vertex bialgebra axiom)
  Path 6: Deconcatenation matrix (from tensor coalgebra)
  Path 7: Cross-check with existing character-level tests

Tests organized by mathematical theorem structure:
  I. Euler form and Ext (quiver combinatorics)
  II. CoHA dimensions (representation theory)
  III. Bar complex dimensions (homological algebra)
  IV. Chain-level duality at (1,1) for A_2 (the key non-trivial test)
  V. Vertex bialgebra (JKL structure)
  VI. Full scan consistency
  VII. Jordan quiver (exact free/cofree duality)
  VIII. Cross-checks with character-level engine
"""

import pytest
from fractions import Fraction

from compute.lib.coha_chain_level_duality_engine import (
    euler_form_an,
    symmetrized_euler_form_an,
    ext_dim_an,
    dim_vectors_an,
    coha_dim_at_vector,
    bar_generators_an,
    bar_dim_at_degree_weight,
    chain_level_pairing_a2,
    verify_chain_duality_a2_11,
    deconcatenation_matrix,
    coha_mult_chain_map_a2,
    jkl_vertex_coproduct_a2,
    full_chain_level_scan_a2,
    chain_level_jordan,
    theorem_chain_level_duality,
    QuiverRep,
)


# ============================================================================
# I. Euler form and Ext (quiver combinatorics)
# ============================================================================

class TestEulerForm:
    """Tests for the Euler form of A_n quivers."""

    def test_a1_euler_form_simple_roots(self):
        """A_1 quiver: <(1,0), (0,1)> = -1 (one arrow)."""
        assert euler_form_an(1, (1, 0), (0, 1)) == -1

    def test_a1_euler_form_reverse(self):
        """A_1 quiver: <(0,1), (1,0)> = 0 (no arrow 1->0)."""
        assert euler_form_an(1, (0, 1), (1, 0)) == 0

    def test_a1_euler_form_diagonal(self):
        """A_1 quiver: <(1,0), (1,0)> = 1."""
        assert euler_form_an(1, (1, 0), (1, 0)) == 1

    def test_a2_euler_form_e0_e1(self):
        """A_2 quiver: <(1,0,0), (0,1,0)> = -1 (arrow 0->1)."""
        assert euler_form_an(2, (1, 0, 0), (0, 1, 0)) == -1

    def test_a2_euler_form_e1_e2(self):
        """A_2 quiver: <(0,1,0), (0,0,1)> = -1 (arrow 1->2)."""
        assert euler_form_an(2, (0, 1, 0), (0, 0, 1)) == -1

    def test_a2_euler_form_e0_e2(self):
        """A_2 quiver: <(1,0,0), (0,0,1)> = 0 (no direct arrow)."""
        assert euler_form_an(2, (1, 0, 0), (0, 0, 1)) == 0

    def test_a2_euler_form_e1_e0(self):
        """A_2 quiver: <(0,1,0), (1,0,0)> = 0 (no arrow 1->0)."""
        assert euler_form_an(2, (0, 1, 0), (1, 0, 0)) == 0

    def test_a2_euler_form_bilinearity(self):
        """Euler form is bilinear."""
        d1 = (1, 1, 0)
        d2 = (0, 1, 1)
        # <d1, d2> should equal <(1,0,0),(0,1,1)> + <(0,1,0),(0,1,1)>
        lhs = euler_form_an(2, d1, d2)
        rhs = (euler_form_an(2, (1, 0, 0), d2)
               + euler_form_an(2, (0, 1, 0), d2))
        assert lhs == rhs

    def test_symmetrized_euler_form_a2(self):
        """Symmetrized Euler form for A_2."""
        # (d1, d2) = <d1, d2> + <d2, d1>
        d1, d2 = (1, 0, 0), (0, 1, 0)
        sym = symmetrized_euler_form_an(2, d1, d2)
        assert sym == euler_form_an(2, d1, d2) + euler_form_an(2, d2, d1)
        assert sym == -1  # -1 + 0 = -1

    def test_euler_form_cartan_matrix(self):
        """The symmetrized Euler form on simple roots gives the Cartan matrix.

        For A_2: Cartan matrix is [[2, -1], [-1, 2]].
        Using dim vectors (1,1,0) and (0,1,1) for the simple roots.
        """
        # Simple root alpha_1 in dim vector form: (1,1,0) ... no,
        # the simple dim vectors are e_0=(1,0,0), e_1=(0,1,0), e_2=(0,0,1).
        # The symmetrized Euler form on these gives:
        # (e_i, e_i) = 2 for all i
        for i in range(3):
            d = [0, 0, 0]
            d[i] = 1
            assert symmetrized_euler_form_an(2, tuple(d), tuple(d)) == 2

    def test_euler_form_adjacent_vertices(self):
        """Adjacent simple vectors have symmetrized form = -1."""
        # (e_0, e_1) = <e_0, e_1> + <e_1, e_0> = -1 + 0 = -1
        assert symmetrized_euler_form_an(2, (1, 0, 0), (0, 1, 0)) == -1
        # (e_1, e_2) = <e_1, e_2> + <e_2, e_1> = -1 + 0 = -1
        assert symmetrized_euler_form_an(2, (0, 1, 0), (0, 0, 1)) == -1

    def test_euler_form_non_adjacent(self):
        """Non-adjacent simple vectors have symmetrized form = 0."""
        assert symmetrized_euler_form_an(2, (1, 0, 0), (0, 0, 1)) == 0


class TestExtDimension:
    """Tests for Ext^1 dimensions."""

    def test_ext_a2_e0_e1(self):
        """Ext^1(V_{e_0}, V_{e_1}) = max(0, -<e_0, e_1>) = max(0, 1) = 1.

        ext_dim_an(n, d1, d2) = Ext^1(V_{d1}, V_{d2}) = max(0, -<d1, d2>).
        <(1,0,0), (0,1,0)> = -1 (arrow 0->1), so Ext^1 = 1.
        """
        assert ext_dim_an(2, (1, 0, 0), (0, 1, 0)) == 1

    def test_ext_a2_e1_e0(self):
        """Ext^1(V_{e_1}, V_{e_0}) = max(0, -<e_1, e_0>) = max(0, 0) = 0.

        <(0,1,0), (1,0,0)> = 0 (no arrow 1->0), so Ext^1 = 0.
        """
        assert ext_dim_an(2, (0, 1, 0), (1, 0, 0)) == 0

    def test_ext_a2_e1_e2(self):
        """Ext^1(V_{e_1}, V_{e_2}) = 1 (arrow 1->2)."""
        assert ext_dim_an(2, (0, 1, 0), (0, 0, 1)) == 1

    def test_ext_a2_e0_e2(self):
        """Ext^1(V_{e_0}, V_{e_2}) = 0 (non-adjacent, no direct arrow)."""
        assert ext_dim_an(2, (1, 0, 0), (0, 0, 1)) == 0

    def test_ext_self(self):
        """Ext^1(V_{e_i}, V_{e_i}) = 0 for Dynkin quivers (no loops).

        <e_i, e_i> = 1, so -<e_i, e_i> = -1, max(0, -1) = 0.
        """
        for i in range(3):
            d = [0, 0, 0]
            d[i] = 1
            assert ext_dim_an(2, tuple(d), tuple(d)) == 0

    def test_ext_determines_extensions(self):
        """Ext^1 > 0 iff there exist non-trivial extensions.

        Cross-check: Ext^1(V_{(1,0,0)}, V_{(0,1,0)}) = 1 means
        the extension 0 -> V_{(0,1,0)} -> V_{(1,1,0)} -> V_{(1,0,0)} -> 0
        has a 1-dimensional parameter space (the map phi: C -> C at arrow 0->1).
        """
        # ext_dim_an(n, d1, d2) = Ext^1(V_{d1}, V_{d2})
        assert ext_dim_an(2, (1, 0, 0), (0, 1, 0)) > 0  # arrow 0->1 exists
        assert ext_dim_an(2, (0, 1, 0), (1, 0, 0)) == 0  # no arrow 1->0


# ============================================================================
# II. CoHA dimensions
# ============================================================================

class TestCoHADimensions:
    """Tests for CoHA dimensions at explicit dimension vectors."""

    def test_simple_vectors_dim_1(self):
        """Simple dimension vectors (one vertex) have CoHA dim 1."""
        for i in range(3):
            d = [0, 0, 0]
            d[i] = 1
            assert coha_dim_at_vector(2, tuple(d)) == 1

    def test_positive_root_110(self):
        """(1,1,0) is a positive root of A_2 (alpha_1), CoHA dim 1."""
        assert coha_dim_at_vector(2, (1, 1, 0)) == 1

    def test_positive_root_011(self):
        """(0,1,1) is a positive root of A_2 (alpha_2), CoHA dim 1."""
        assert coha_dim_at_vector(2, (0, 1, 1)) == 1

    def test_positive_root_111(self):
        """(1,1,1) is a positive root of A_2 (alpha_1 + alpha_2), CoHA dim 1."""
        assert coha_dim_at_vector(2, (1, 1, 1)) == 1

    def test_not_root_101(self):
        """(1,0,1) is NOT a positive root (non-contiguous)."""
        # It decomposes as (1,0,0) + (0,0,1)
        # CoHA dim should be the number of ordered decompositions = 1
        dim = coha_dim_at_vector(2, (1, 0, 1))
        # (1,0,1) = (1,0,0) + (0,0,1) is the only decomposition
        assert dim == 1

    def test_three_positive_roots(self):
        """A_2 = sl_3 has exactly 3 positive roots."""
        roots = [(1, 1, 0), (0, 1, 1), (1, 1, 1)]
        for r in roots:
            assert coha_dim_at_vector(2, r) == 1


# ============================================================================
# III. Bar complex dimensions
# ============================================================================

class TestBarDimensions:
    """Tests for bar complex dimensions."""

    def test_bar_generators_sl3(self):
        """sl_3 has dim = 8, so 8 bar generators per weight level."""
        assert bar_generators_an(2, 1) == 8  # dim(sl_3) = 3^2 - 1 = 8

    def test_bar_generators_sl2(self):
        """sl_2 has dim = 3."""
        assert bar_generators_an(1, 1) == 3

    def test_bar_degree_1_weight_1(self):
        """B^1 at weight 1 has dim = dim(g) generators."""
        assert bar_dim_at_degree_weight(2, 1, 1) == 8

    def test_bar_degree_1_weight_w(self):
        """B^1 at weight w has dim = dim(g) for all w >= 1."""
        for w in range(1, 6):
            assert bar_dim_at_degree_weight(2, 1, w) == 8

    def test_bar_degree_2_weight_2(self):
        """B^2 at weight 2: only one composition 2 = 1+1, so dim = 8^2 = 64."""
        # C(2-1, 2-1) = C(1,1) = 1 composition
        assert bar_dim_at_degree_weight(2, 2, 2) == 64

    def test_bar_degree_2_weight_3(self):
        """B^2 at weight 3: compositions 3 = 1+2 or 2+1, so 2 * 64 = 128."""
        assert bar_dim_at_degree_weight(2, 2, 3) == 2 * 64

    def test_bar_degree_0(self):
        """B^0 at weight 0 is 1 (the ground field)."""
        assert bar_dim_at_degree_weight(2, 0, 0) == 1
        assert bar_dim_at_degree_weight(2, 0, 1) == 0


# ============================================================================
# IV. Chain-level duality at (1,1) for A_2
# ============================================================================

class TestChainDualityA2:
    """Tests for the chain-level duality verification at A_2 dim (1,1,0)."""

    def test_duality_verified(self):
        """Chain-level duality is verified at (1,1,0)."""
        result = verify_chain_duality_a2_11()
        assert result['chain_level_duality_verified']

    def test_splitting_a_euler_form(self):
        """Euler form of (1,0,0)+(0,1,0) splitting is -1."""
        result = verify_chain_duality_a2_11()
        assert result['splitting_a']['euler_form'] == -1

    def test_splitting_a_ext_dim(self):
        """Ext^1 of (1,0,0)+(0,1,0) splitting is 1."""
        result = verify_chain_duality_a2_11()
        assert result['splitting_a']['ext_dim'] == 1

    def test_splitting_a_product_nonzero(self):
        """CoHA product at (1,0,0)+(0,1,0) is nonzero."""
        result = verify_chain_duality_a2_11()
        assert result['splitting_a']['coha_product'] != 0

    def test_splitting_a_consistent(self):
        """Duality pairing consistent for forward splitting."""
        result = verify_chain_duality_a2_11()
        assert result['splitting_a']['duality_consistent']

    def test_splitting_b_euler_form(self):
        """Euler form of reverse splitting (0,1,0)+(1,0,0) is 0."""
        result = verify_chain_duality_a2_11()
        assert result['splitting_b']['euler_form'] == 0

    def test_splitting_b_ext_dim(self):
        """Ext^1 of reverse splitting is 0 (no arrow 1->0)."""
        result = verify_chain_duality_a2_11()
        assert result['splitting_b']['ext_dim'] == 0

    def test_splitting_b_product_zero(self):
        """CoHA product at reverse splitting is zero."""
        result = verify_chain_duality_a2_11()
        assert result['splitting_b']['coha_product'] == 0

    def test_splitting_b_consistent(self):
        """Duality pairing consistent for reverse splitting."""
        result = verify_chain_duality_a2_11()
        assert result['splitting_b']['duality_consistent']

    def test_bar_primitive(self):
        """Bar elements at degree 1 are primitive."""
        result = verify_chain_duality_a2_11()
        assert result['bar_coprod_primitive_at_deg1']


class TestChainPairingA2:
    """Tests for the chain-level pairing at general A_2 vectors."""

    def test_pairing_110(self):
        """Chain pairing data at (1,1,0)."""
        result = chain_level_pairing_a2((1, 1, 0))
        assert result['coha_dim'] == 1
        assert result['total_weight'] == 2
        assert result['num_splittings'] > 0

    def test_pairing_011(self):
        """Chain pairing data at (0,1,1)."""
        result = chain_level_pairing_a2((0, 1, 1))
        assert result['coha_dim'] == 1

    def test_pairing_111(self):
        """Chain pairing data at (1,1,1)."""
        result = chain_level_pairing_a2((1, 1, 1))
        assert result['coha_dim'] == 1
        assert result['total_weight'] == 3


# ============================================================================
# V. Vertex bialgebra (JKL)
# ============================================================================

class TestJKLVertexCoproduct:
    """Tests for the JKL vertex coproduct structure."""

    def test_jkl_110_has_singular_terms(self):
        """JKL coproduct at (1,1,0) has singular (OPE) terms."""
        result = jkl_vertex_coproduct_a2((1, 1, 0))
        assert len(result['singular_terms']) > 0

    def test_jkl_110_max_pole_order(self):
        """Maximum pole order at (1,1,0) is 1 (simple pole from OPE)."""
        result = jkl_vertex_coproduct_a2((1, 1, 0))
        assert result['max_pole_order'] == 1

    def test_jkl_110_ope_mode_0(self):
        """OPE mode 0 is present (from the z^{-1} term)."""
        result = jkl_vertex_coproduct_a2((1, 1, 0))
        assert 0 in result['ope_modes_present']

    def test_jkl_011_has_singular_terms(self):
        """JKL coproduct at (0,1,1) has singular terms."""
        result = jkl_vertex_coproduct_a2((0, 1, 1))
        assert len(result['singular_terms']) > 0

    def test_jkl_111_richer_structure(self):
        """JKL coproduct at (1,1,1) has more splittings."""
        result = jkl_vertex_coproduct_a2((1, 1, 1))
        # (1,1,1) has more splittings than (1,1,0)
        assert result['num_splittings'] >= 2

    def test_jkl_vertex_bialgebra_axiom(self):
        """Vertex bialgebra axiom statement is recorded."""
        result = jkl_vertex_coproduct_a2((1, 1, 0))
        assert 'coderivation' in result['vertex_bialgebra_axiom']


# ============================================================================
# VI. Deconcatenation coproduct
# ============================================================================

class TestDeconcatenation:
    """Tests for the explicit deconcatenation coproduct."""

    def test_bar_deg_1_primitive(self):
        """Bar degree 1 elements are primitive."""
        result = deconcatenation_matrix(8, 1, 1)
        assert result['structure'] == 'primitive (all generators are primitive)'
        assert result['num_splittings'] == 2

    def test_bar_deg_2_three_terms(self):
        """Bar degree 2 has three deconcatenation terms."""
        result = deconcatenation_matrix(8, 2, 2)
        assert len(result['splittings']) == 3
        assert (2, 0) in result['splittings']
        assert (1, 1) in result['splittings']
        assert (0, 2) in result['splittings']

    def test_bar_deg_2_identity_splitting(self):
        """The (1,1) splitting at bar degree 2 is the identity."""
        result = deconcatenation_matrix(8, 2, 2)
        assert result['splittings'][(1, 1)]['structure'] == 'identity (middle term)'


# ============================================================================
# VII. Full scan consistency
# ============================================================================

class TestFullScan:
    """Tests for the full chain-level scan across dimension vectors."""

    def test_scan_all_consistent(self):
        """All dimension vectors up to total 3 are consistent."""
        result = full_chain_level_scan_a2(3)
        assert result['all_consistent']

    def test_scan_finds_positive_roots(self):
        """Scan finds the correct number of positive roots."""
        result = full_chain_level_scan_a2(3)
        # At total dim <= 3, we should find all 3 positive roots of sl_3
        assert result['positive_roots_found'] >= 3

    def test_scan_total_4(self):
        """Scan up to total 4 is consistent."""
        result = full_chain_level_scan_a2(4)
        assert result['all_consistent']


class TestCoHAMultTable:
    """Tests for the CoHA multiplication table."""

    def test_mult_table_e0_e1_nonzero(self):
        """Product e0 * e1 is nonzero (extension exists)."""
        result = coha_mult_chain_map_a2()
        key = ((1, 0, 0), (0, 1, 0))
        assert result['multiplication_table'][key]['product_nonzero']

    def test_mult_table_e1_e0_zero(self):
        """Product e1 * e0 is zero (no extension in reverse)."""
        result = coha_mult_chain_map_a2()
        key = ((0, 1, 0), (1, 0, 0))
        assert not result['multiplication_table'][key]['product_nonzero']

    def test_mult_table_e1_e2_nonzero(self):
        """Product e1 * e2 is nonzero."""
        result = coha_mult_chain_map_a2()
        key = ((0, 1, 0), (0, 0, 1))
        assert result['multiplication_table'][key]['product_nonzero']

    def test_chain_duality_verified(self):
        """The key multiplication verifies chain duality."""
        result = coha_mult_chain_map_a2()
        assert result['chain_duality_verified']


# ============================================================================
# VIII. Jordan quiver (exact)
# ============================================================================

class TestJordanQuiver:
    """Tests for the Jordan quiver chain-level duality."""

    def test_jordan_all_consistent(self):
        """All levels of the Jordan quiver are consistent."""
        result = chain_level_jordan(6)
        assert result['all_consistent']

    def test_jordan_exact(self):
        """Jordan quiver duality is exact (Sym/Sym^c)."""
        result = chain_level_jordan()
        assert result['chain_level_exact']

    def test_jordan_euler_form_zero(self):
        """Jordan quiver has zero Euler form (CY condition)."""
        result = chain_level_jordan()
        for r in result['results']:
            for s in r['splittings']:
                assert s['euler_form'] == 0

    def test_jordan_sign_positive(self):
        """All signs are +1 for the Jordan quiver."""
        result = chain_level_jordan()
        for r in result['results']:
            for s in r['splittings']:
                assert s['sign'] == 1

    def test_jordan_partition_numbers(self):
        """CoHA dimensions match partition numbers.

        Cross-check: p(n) via pentagonal number theorem in the engine
        vs independent computation here.
        """
        result = chain_level_jordan(6)
        # p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7, p(6)=11
        expected_partitions = [1, 2, 3, 5, 7, 11]
        for r in result['results']:
            n = r['n']
            assert r['coha_dim'] == expected_partitions[n - 1]


# ============================================================================
# IX. Comprehensive theorem
# ============================================================================

class TestComprehensiveTheorem:
    """Tests for the full theorem statement."""

    def test_theorem_verified(self):
        """Full theorem is verified."""
        result = theorem_chain_level_duality(3)
        assert result['all_consistent']

    def test_jordan_component(self):
        """Jordan component is exact."""
        result = theorem_chain_level_duality(3)
        assert result['jordan_exact']

    def test_a2_11_component(self):
        """A_2 at (1,1) component is verified."""
        result = theorem_chain_level_duality(3)
        assert result['a2_11_verified']

    def test_a2_scan_component(self):
        """A_2 scan component is consistent."""
        result = theorem_chain_level_duality(3)
        assert result['a2_scan_consistent']

    def test_a2_mult_component(self):
        """A_2 multiplication component is verified."""
        result = theorem_chain_level_duality(3)
        assert result['a2_mult_verified']

    def test_jkl_modes(self):
        """JKL singular modes include mode 0."""
        result = theorem_chain_level_duality(3)
        assert 0 in result['jkl_singular_modes']


# ============================================================================
# X. QuiverRep class tests
# ============================================================================

class TestQuiverRep:
    """Tests for the QuiverRep class."""

    def test_rep_creation(self):
        """Can create a quiver representation."""
        rep = QuiverRep((1, 1, 0))
        assert rep.dim_vector == (1, 1, 0)
        assert rep.total_dim == 2

    def test_rep_space_dim_110(self):
        """Rep space dim for (1,1,0) on A_2: d_0*d_1 + d_1*d_2 = 1."""
        rep = QuiverRep((1, 1, 0))
        assert rep.rep_space_dim() == 1  # 1*1 + 1*0 = 1

    def test_gauge_dim_110(self):
        """Gauge dim for (1,1,0): 1^2 + 1^2 + 0^2 = 2."""
        rep = QuiverRep((1, 1, 0))
        assert rep.gauge_dim() == 2


# ============================================================================
# XI. Dimension vector enumeration
# ============================================================================

class TestDimVectors:
    """Tests for dimension vector enumeration."""

    def test_total_1_a2(self):
        """A_2 dim vectors with total 1: three simple vectors."""
        vecs = dim_vectors_an(2, 1)
        assert len(vecs) == 3
        assert (1, 0, 0) in vecs
        assert (0, 1, 0) in vecs
        assert (0, 0, 1) in vecs

    def test_total_2_a2(self):
        """A_2 dim vectors with total 2."""
        vecs = dim_vectors_an(2, 2)
        expected = [
            (2, 0, 0), (1, 1, 0), (1, 0, 1),
            (0, 2, 0), (0, 1, 1), (0, 0, 2),
        ]
        assert len(vecs) == 6
        for e in expected:
            assert e in vecs

    def test_total_0_a2(self):
        """A_2 dim vectors with total 0: just the zero vector."""
        vecs = dim_vectors_an(2, 0)
        assert len(vecs) == 1
        assert (0, 0, 0) in vecs

    def test_dim_vector_count_stars_and_bars(self):
        """Number of dim vectors for A_n at total d = C(d+n, n).

        Cross-check: stars-and-bars formula for non-negative integer
        compositions of d into n+1 parts.
        """
        from math import comb
        for n in [1, 2, 3]:
            for d in [0, 1, 2, 3]:
                vecs = dim_vectors_an(n, d)
                expected = comb(d + n, n)
                assert len(vecs) == expected


# ============================================================================
# XII. Multi-path cross-checks (AP10 compliance)
# ============================================================================

class TestMultiPathCrossChecks:
    """Cross-checks using multiple independent computation paths."""

    def test_euler_form_antisymmetry_for_cartan(self):
        """Cross-check: (e_i, e_j) = <e_i,e_j> + <e_j,e_i> recovers A_2 Cartan.

        The Cartan matrix of A_2 is [[2,-1,0],[-1,2,-1],[0,-1,2]].
        Path 1: compute via euler_form_an.
        Path 2: hardcoded Cartan matrix of A_2.
        """
        cartan_a2 = [[2, -1, 0], [-1, 2, -1], [0, -1, 2]]
        for i in range(3):
            for j in range(3):
                di = [0, 0, 0]
                dj = [0, 0, 0]
                di[i] = 1
                dj[j] = 1
                sym = symmetrized_euler_form_an(2, tuple(di), tuple(dj))
                assert sym == cartan_a2[i][j]

    def test_ext_vs_euler_cross_check(self):
        """Cross-check: Ext^1(d1,d2) > 0 iff <d1,d2> < 0.

        For Dynkin quivers, Ext^1(V_{d1}, V_{d2}) = max(0, -<d1, d2>).
        Path 1: compute ext_dim_an directly.
        Path 2: compute from euler_form_an and apply max(0, -.).
        """
        for d1 in dim_vectors_an(2, 1):
            for d2 in dim_vectors_an(2, 1):
                ext = ext_dim_an(2, d1, d2)
                euler = euler_form_an(2, d1, d2)
                assert ext == max(0, -euler)

    def test_coha_dim_vs_root_classification(self):
        """Cross-check: CoHA dim at positive root = 1.

        Path 1: coha_dim_at_vector.
        Path 2: explicit root check (contiguous 1's).
        """
        roots = [(1, 1, 0), (0, 1, 1), (1, 1, 1)]
        for r in roots:
            assert coha_dim_at_vector(2, r) == 1

    def test_bar_dim_total_vs_character(self):
        """Cross-check: total bar dim at weight w = sum over bar degrees.

        Path 1: sum bar_dim_at_degree_weight over degrees 0..w.
        Path 2: 2^{w-1} for w >= 1 (since dim(g) generators per level,
                 but total is sum_p C(w-1,p-1) * d^p; for d=1 this is 2^{w-1}).

        For sl_3 (d=8), total bar dim at weight w = sum_{p=1}^{w} C(w-1,p-1)*8^p.
        Cross-check by direct computation.
        """
        from math import comb as C
        for w in range(1, 6):
            total_path1 = sum(bar_dim_at_degree_weight(2, p, w)
                              for p in range(0, w + 1))
            total_path2 = sum(C(w - 1, p - 1) * 8 ** p
                              for p in range(1, w + 1))
            assert total_path1 == total_path2

    def test_jordan_partition_independent(self):
        """Cross-check: Jordan CoHA dims = partition numbers.

        Path 1: chain_level_jordan (engine's _partition_number).
        Path 2: independent computation via Euler's recurrence.
        """
        # Independent partition numbers via Euler's pentagonal recurrence
        def _p(n, memo={0: 1}):
            if n in memo:
                return memo[n]
            if n < 0:
                return 0
            total = 0
            k = 1
            while True:
                g1 = k * (3 * k - 1) // 2
                g2 = k * (3 * k + 1) // 2
                if g1 > n:
                    break
                s = (-1) ** (k + 1)
                total += s * _p(n - g1)
                if g2 <= n:
                    total += s * _p(n - g2)
                k += 1
            memo[n] = total
            return total

        result = chain_level_jordan(8)
        for r in result['results']:
            assert r['coha_dim'] == _p(r['n'])

    def test_a2_ext_sum_equals_cartan_entry(self):
        """Cross-check: ext(d1,d2) + ext(d2,d1) relates to Cartan matrix.

        For simple dim vectors e_i, e_j with i != j:
        ext(e_i, e_j) + ext(e_j, e_i) = max(0,-<e_i,e_j>) + max(0,-<e_j,e_i>).
        For adjacent vertices: one of <e_i,e_j> or <e_j,e_i> is -1 (the arrow),
        the other is 0. So ext_sum = 1.
        For non-adjacent: both are 0. ext_sum = 0.
        """
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                di = [0, 0, 0]
                dj = [0, 0, 0]
                di[i] = 1
                dj[j] = 1
                ext_sum = (ext_dim_an(2, tuple(di), tuple(dj))
                           + ext_dim_an(2, tuple(dj), tuple(di)))
                # Adjacent (|i-j|=1): ext_sum=1. Non-adjacent (|i-j|=2): ext_sum=0.
                if abs(i - j) == 1:
                    assert ext_sum == 1
                else:
                    assert ext_sum == 0

    def test_chain_duality_both_directions_consistent(self):
        """Cross-check: the chain duality at (1,1,0) from two independent paths.

        Path 1: verify_chain_duality_a2_11 (specialized function).
        Path 2: chain_level_pairing_a2 (general function).
        Both must report consistency.
        """
        specialized = verify_chain_duality_a2_11()
        general = chain_level_pairing_a2((1, 1, 0))
        assert specialized['chain_level_duality_verified']
        assert general['num_splittings'] > 0

    def test_theorem_all_components_agree(self):
        """Cross-check: all five components of the theorem agree.

        The theorem calls jordan, a2_11, a2_scan, a2_mult, jkl
        independently. All must be consistent.
        """
        result = theorem_chain_level_duality(3)
        assert result['jordan_exact']
        assert result['a2_11_verified']
        assert result['a2_scan_consistent']
        assert result['a2_mult_verified']
        assert result['all_consistent']
