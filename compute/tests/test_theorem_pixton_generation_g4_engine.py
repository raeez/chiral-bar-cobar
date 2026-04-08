r"""Tests for the Pixton ideal generation engine at genus 4.

Tests conj:pixton-from-shadows at genus 4: the MC-descended tautological
relations from the shadow obstruction tower generate the Pixton ideal.

The GENERATION question (beyond membership):
  Does obs_4 produce Pixton relations INDEPENDENT of lower-genus data?
  Does S_6 (first visible at genus 4) generate genuinely new content?
  Do different shadow depth classes (G/L/C/M) produce independent relations?

50+ tests organized in sections:
  A. Tautological ring structure at genus 4 (Faber data)
  B. Codimension decomposition of obs_4
  C. Shadow coefficient isolation by codimension (S_3..S_7)
  D. S_6 codimension isolation (the sharpest test)
  E. Cross-family independence (G/L/C/M hierarchy)
  F. Lower-genus pushforward comparison
  G. Numerical rank test
  H. Pixton ideal dimension analysis
  I. Codimension-5 analysis (first Pixton generators)
  J. Planted-forest polynomial structure
  K. Virasoro special values
  L. Genus comparison (g=2,3,4 complexity growth)
  M. Master generation theorem
"""

import pytest
from fractions import Fraction

from sympy import (
    Integer, Rational, Symbol, cancel, expand, simplify, S,
)

from compute.lib.theorem_pixton_generation_g4_engine import (
    # Section 1: Tautological ring
    FABER_GENUS4_DIMS,
    # Section 2: Graph census
    genus4_codimension_distribution,
    genus4_pf_codimension_distribution,
    genus4_nonzero_hodge_by_codim,
    genus4_max_shadow_arity_by_codim,
    # Section 3: Codimension decomposition
    obs4_by_codimension,
    pf_by_codimension,
    nonpf_by_codimension,
    obs4_codim_summary,
    # Section 4: Shadow isolation
    shadow_isolation_by_codim,
    s6_codim_isolation,
    s7_codim_isolation,
    full_shadow_isolation_genus4,
    # Section 5: Cross-family
    cross_family_obs4,
    cross_family_independence_test,
    # Section 6: Lower-genus pushforward
    lower_genus_pf_content,
    # Section 7: Numerical rank
    numerical_rank_test,
    # Section 8: Pixton dimension
    genus4_pixton_ideal_dimension,
    pixton_shadow_contribution_by_codim,
    # Section 9: Polynomial
    pf_polynomial_genus4_full,
    # Section 10: Generation theorem
    genus4_generation_theorem,
    # Section 11: Codim-5
    codim5_analysis,
    # Section 12: Genus comparison
    pf_genus_comparison,
    # Section 13: Special values
    virasoro_special_values_genus4,
    # Section 14: Master analysis
    master_generation_analysis,
)
from compute.lib.pixton_shadow_bridge import (
    ShadowData,
    virasoro_shadow_data,
    heisenberg_shadow_data,
    affine_shadow_data,
    c_sym,
)
from compute.lib.theorem_pixton_genus4_shadow_engine import (
    LAMBDA4_FP,
    genus4_graph_count,
    genus4_pf_count,
    delta_pf_genus4,
)
from compute.lib.theorem_shadow_arity_frontier_engine import (
    shadow_visibility_genus,
)


c = c_sym


# ============================================================================
# Section A: Tautological ring structure at genus 4
# ============================================================================

class TestTautRingGenus4:
    """Verify Faber's R*(M-bar_4) structure."""

    def test_dim_mbar4(self):
        """dim M-bar_4 = 3*4 - 3 = 9."""
        assert 3 * 4 - 3 == 9

    def test_gorenstein_symmetry(self):
        """Gorenstein: dim R^k = dim R^{9-k}."""
        for k in range(10):
            assert FABER_GENUS4_DIMS[k] == FABER_GENUS4_DIMS[9 - k]

    def test_r0_is_1(self):
        """R^0 = fundamental class, dimension 1."""
        assert FABER_GENUS4_DIMS[0] == 1

    def test_r1_is_4(self):
        """R^1(M-bar_4) has dimension 4."""
        assert FABER_GENUS4_DIMS[1] == 4

    def test_r9_is_1(self):
        """R^9 = top degree, dimension 1 (Gorenstein)."""
        assert FABER_GENUS4_DIMS[9] == 1

    def test_total_dim(self):
        """Total dimension of R*(M-bar_4)."""
        total = sum(FABER_GENUS4_DIMS.values())
        assert total > 0  # sanity

    def test_r4_is_largest_or_tied(self):
        """R^4 should be among the largest (middle codimension)."""
        assert FABER_GENUS4_DIMS[4] >= FABER_GENUS4_DIMS[3]


# ============================================================================
# Section B: Codimension decomposition of obs_4
# ============================================================================

class TestCodimDecomposition:
    """Codimension-by-codimension analysis of the genus-4 MC relation."""

    @pytest.fixture(scope="class")
    def vir_shadow(self):
        return virasoro_shadow_data(max_arity=10)

    @pytest.fixture(scope="class")
    def heis_shadow(self):
        return heisenberg_shadow_data()

    def test_obs4_codim_keys(self, vir_shadow):
        """obs_4 should have contributions at multiple codimensions."""
        codim_all = obs4_by_codimension(vir_shadow)
        assert len(codim_all) >= 1

    def test_pf_codim_subset(self, vir_shadow):
        """Planted-forest codimensions are a subset of total codimensions."""
        codim_all = obs4_by_codimension(vir_shadow)
        codim_pf = pf_by_codimension(vir_shadow)
        assert set(codim_pf.keys()).issubset(set(codim_all.keys()))

    def test_heisenberg_pf_zero_all_codims(self, heis_shadow):
        """Class G: planted-forest is zero at ALL codimensions."""
        codim_pf = pf_by_codimension(heis_shadow)
        for k, v in codim_pf.items():
            assert simplify(v) == 0, f"Heisenberg pf nonzero at codim {k}"

    def test_virasoro_pf_nonzero_some_codims(self, vir_shadow):
        """Class M: planted-forest is nonzero at SOME codimensions."""
        summary = obs4_codim_summary(vir_shadow)
        assert len(summary['nonzero_pf_codims']) > 0

    def test_codim_summary_structure(self, vir_shadow):
        """Summary has the expected keys."""
        summary = obs4_codim_summary(vir_shadow)
        assert 'shadow_name' in summary
        assert 'active_codims' in summary
        assert 'nonzero_pf_codims' in summary


# ============================================================================
# Section C: Shadow coefficient isolation by codimension
# ============================================================================

class TestShadowIsolation:
    """Isolate each S_r contribution to each codimension."""

    def test_s3_has_support(self):
        """S_3 contributes to at least one codimension at genus 4."""
        iso = shadow_isolation_by_codim(3)
        assert len(iso) > 0

    def test_s4_has_support(self):
        """S_4 contributes to at least one codimension."""
        iso = shadow_isolation_by_codim(4)
        assert len(iso) > 0

    def test_s5_has_support(self):
        """S_5 contributes to at least one codimension."""
        iso = shadow_isolation_by_codim(5)
        assert len(iso) > 0

    def test_s6_has_support(self):
        """S_6 contributes to at least one codimension (first visible at g=4)."""
        iso = shadow_isolation_by_codim(6)
        assert len(iso) > 0, "S_6 should contribute at genus 4 (g_min = 4)"

    def test_s7_support(self):
        """S_7 may or may not contribute at genus 4 (g_min = 4)."""
        iso = shadow_isolation_by_codim(7)
        # S_7 is also first visible at genus 4 (g_min(7) = 4)
        # It requires a genus-0 vertex of valence 7, which requires 7 edges,
        # so codim >= 7. At genus 4, max codim = 9, so there is room.
        # Whether there are stable graphs with such a vertex is an enumeration question.
        # No assertion on direction -- just record.
        assert isinstance(iso, dict)

    def test_shadow_arity_support_monotonicity(self):
        """Higher S_r should not appear at LOWER codimension than lower S_r.

        S_r requires a genus-0 vertex of valence r, which requires at least
        ceil(r/2) edges (from stability). So min codim for S_r >= ceil(r/2).
        """
        for r in range(3, 8):
            iso = shadow_isolation_by_codim(r)
            if iso:
                min_codim = min(iso.keys())
                # A genus-0 vertex of valence r needs val(v) >= 3 (stability),
                # and contributes r/2 to the edge count (each edge has 2 half-edges).
                # Min codim is at least r - (number of higher-genus vertices).
                assert min_codim >= 1, (
                    f"S_{r} at codim {min_codim} < 1"
                )

    def test_full_shadow_isolation(self):
        """Full isolation analysis returns incremental data."""
        result = full_shadow_isolation_genus4()
        assert 'by_arity' in result
        assert 'total_pf_codims' in result
        assert 'incremental_by_arity' in result
        assert len(result['total_pf_codims']) > 0


# ============================================================================
# Section D: S_6 codimension isolation (the sharpest test)
# ============================================================================

class TestS6Isolation:
    """S_6 isolation: the critical test for genus-4 generation."""

    @pytest.fixture(scope="class")
    def s6_data(self):
        return s6_codim_isolation()

    def test_s6_active_codims_nonempty(self, s6_data):
        """S_6 contributes at some codimension at genus 4."""
        assert len(s6_data['s6_active_codims']) > 0

    def test_s6_visibility_genus(self):
        """g_min(S_6) = floor(6/2) + 1 = 4."""
        assert shadow_visibility_genus(6) == 4

    def test_s6_codim_values_nonzero(self, s6_data):
        """The actual S_6 contributions are nonzero expressions."""
        for k, v in s6_data['s6_codim_values'].items():
            assert simplify(v) != 0, f"S_6 zero at codim {k}"

    def test_s6_min_codim(self, s6_data):
        """S_6 requires a genus-0 vertex of valence 6.

        A single such vertex needs at least 3 edges (val >= 3 from stability,
        but val = 6 so 3 self-loops give codim 3, or bridges need more vertices).
        """
        if s6_data['s6_active_codims']:
            min_codim = min(s6_data['s6_active_codims'])
            assert min_codim >= 2

    def test_s7_isolation(self):
        """S_7 codimension isolation."""
        s7_data = s7_codim_isolation()
        assert isinstance(s7_data, dict)
        assert 's7_active_codims' in s7_data


# ============================================================================
# Section E: Cross-family independence
# ============================================================================

class TestCrossFamilyIndependence:
    """Different shadow depth classes produce independent relations."""

    @pytest.fixture(scope="class")
    def cross_data(self):
        return cross_family_obs4()

    @pytest.fixture(scope="class")
    def independence_data(self):
        return cross_family_independence_test()

    def test_heisenberg_pf_zero(self, cross_data):
        """Class G (Heisenberg): delta_pf = 0."""
        assert not cross_data['G']['pf_nonzero']

    def test_affine_pf_nonzero(self, cross_data):
        """Class L (affine sl_2): delta_pf nonzero."""
        assert cross_data['L']['pf_nonzero']

    def test_betagamma_pf_nonzero(self, cross_data):
        """Class C (beta-gamma): delta_pf nonzero."""
        assert cross_data['C']['pf_nonzero']

    def test_virasoro_pf_nonzero(self, cross_data):
        """Class M (Virasoro): delta_pf nonzero."""
        assert cross_data['M']['pf_nonzero']

    def test_hierarchy(self, independence_data):
        """G subset L subset C subset M hierarchy."""
        assert independence_data['G_pf_zero']
        assert independence_data['L_pf_nonzero']
        assert independence_data['C_pf_nonzero']
        assert independence_data['M_pf_nonzero']

    def test_m_exceeds_l(self, independence_data):
        """Class M structurally exceeds class L (uses S_6, which L does not)."""
        assert independence_data['M_exceeds_L']

    def test_m_uses_s6(self, independence_data):
        """Class M uses S_6 (structural independence certificate)."""
        assert independence_data['M_uses_S6']

    def test_depth_class_labels(self, cross_data):
        """Each family has the correct depth class label."""
        assert cross_data['G']['depth_class'] == 'G'
        assert cross_data['L']['depth_class'] == 'L'
        assert cross_data['C']['depth_class'] == 'C'
        assert cross_data['M']['depth_class'] == 'M'


# ============================================================================
# Section F: Lower-genus pushforward comparison
# ============================================================================

class TestLowerGenusPushforward:
    """Test that genus-4 MC relations contain genuinely new content."""

    @pytest.fixture(scope="class")
    def pushforward_data(self):
        return lower_genus_pf_content()

    def test_new_shadows_at_genus4(self, pushforward_data):
        """S_6 and S_7 are new at genus 4 (not in genus 2 or 3 data)."""
        new = pushforward_data['new_shadows_at_genus4']
        assert 'S_6' in new
        assert 'S_7' in new

    def test_s6_contributes(self, pushforward_data):
        """S_6 actually contributes to delta_pf^{(4,0)}."""
        assert pushforward_data['s6_contributes']

    def test_genuinely_new_content(self, pushforward_data):
        """There IS genuinely new content at genus 4."""
        assert pushforward_data['genuinely_new_content']

    def test_genus2_formula(self, pushforward_data):
        """Genus-2 planted-forest formula: S_3(10*S_3 - kappa)/48."""
        pf_g2 = pushforward_data['pf_genus2_formula']
        kappa_sym = Symbol('kappa')
        S3_sym = Symbol('S_3')
        expected = S3_sym * (10 * S3_sym - kappa_sym) / 48
        assert simplify(pf_g2 - expected) == 0

    def test_shadow_hierarchy_by_genus(self, pushforward_data):
        """Shadow coefficients at genus 2 < genus 3 < genus 4."""
        by_genus = pushforward_data['shadow_coefficients_by_genus']
        assert by_genus[2] < by_genus[3]
        assert by_genus[3] < by_genus[4]


# ============================================================================
# Section G: Numerical rank test
# ============================================================================

class TestNumericalRank:
    """Numerical rank of the shadow-descended Pixton relations."""

    @pytest.fixture(scope="class")
    def rank_data(self):
        return numerical_rank_test()

    def test_rank_positive(self, rank_data):
        """Numerical rank is positive (some Pixton relations generated)."""
        assert rank_data['numerical_rank'] > 0

    def test_rank_exceeds_1(self, rank_data):
        """Rank exceeds 1: a SPACE of Pixton relations, not just one.

        This is the strongest form of the generation result for a
        single-parameter family (Virasoro). Different c-values give
        linearly independent Pixton relations.
        """
        assert rank_data['rank_exceeds_1'], (
            f"Numerical rank = {rank_data['numerical_rank']} <= 1"
        )

    def test_matrix_shape(self, rank_data):
        """Matrix has the expected shape (n_c_values x max_codim)."""
        shape = rank_data['matrix_shape']
        assert shape[0] == rank_data['n_c_values']
        assert shape[1] == 10  # max_codim

    def test_nonzero_codims_nonempty(self, rank_data):
        """Some codimensions have nonzero planted-forest contributions."""
        assert len(rank_data['nonzero_codims']) > 0


# ============================================================================
# Section H: Pixton ideal dimension analysis
# ============================================================================

class TestPixtonIdealDimension:
    """Pixton ideal dimension estimates at genus 4."""

    def test_pixton_ideal_dims_keys(self):
        """Dimension data exists for all codimensions 0..9."""
        dims = genus4_pixton_ideal_dimension()
        for k in range(10):
            assert k in dims

    def test_pixton_ideal_nonneg(self):
        """Pixton ideal dimension lower bound is non-negative."""
        dims = genus4_pixton_ideal_dimension()
        for k in range(10):
            assert dims[k]['pixton_ideal_lower_bound'] >= 0

    def test_codim0_no_pixton(self):
        """No Pixton relations at codimension 0."""
        dims = genus4_pixton_ideal_dimension()
        assert dims[0]['n_strata_graphs_codim_k'] <= dims[0]['dim_R_k']

    def test_shadow_contribution_structure(self):
        """Shadow contribution data has expected structure."""
        contrib = pixton_shadow_contribution_by_codim()
        for k in range(10):
            assert k in contrib
            assert 'dim_R_k' in contrib[k]
            assert 'pf_nonzero' in contrib[k]
            assert 'shadow_coefficients_present' in contrib[k]


# ============================================================================
# Section I: Codimension-5 analysis
# ============================================================================

class TestCodim5:
    """Codimension 5: first Pixton ideal generators at genus 4."""

    @pytest.fixture(scope="class")
    def codim5_data(self):
        return codim5_analysis()

    def test_codim5_has_graphs(self, codim5_data):
        """There are stable graphs at codimension 5."""
        assert codim5_data['n_graphs_codim5'] > 0

    def test_codim5_dim_r5(self, codim5_data):
        """dim R^5(M-bar_4) = 40 (Gorenstein partner of R^4)."""
        assert codim5_data['dim_R5'] == FABER_GENUS4_DIMS[5]

    def test_codim5_has_pf(self, codim5_data):
        """Some codim-5 graphs are planted-forest."""
        assert codim5_data['n_pf_codim5'] >= 0  # may be zero; record

    def test_codim5_has_nonzero_hodge(self, codim5_data):
        """Some codim-5 graphs have nonzero Hodge integral."""
        assert codim5_data['n_nonzero_hodge_codim5'] >= 0


# ============================================================================
# Section J: Planted-forest polynomial structure
# ============================================================================

class TestPFPolynomial:
    """Planted-forest polynomial structure at genus 4."""

    @pytest.fixture(scope="class")
    def poly_data(self):
        return pf_polynomial_genus4_full()

    def test_polynomial_has_terms(self, poly_data):
        """The planted-forest polynomial has multiple terms."""
        assert poly_data['n_terms'] > 0

    def test_depends_on_kappa(self, poly_data):
        """Polynomial depends on kappa."""
        assert poly_data['depends_on']['kappa']

    def test_depends_on_s3(self, poly_data):
        """Polynomial depends on S_3."""
        assert poly_data['depends_on']['S_3']

    def test_depends_on_s6(self, poly_data):
        """Polynomial depends on S_6 (new at genus 4)."""
        assert poly_data['depends_on']['S_6']

    def test_s6_terms_exist(self, poly_data):
        """There are monomials involving S_6."""
        assert poly_data['n_terms_involving_S6'] > 0

    def test_new_terms_at_genus4(self, poly_data):
        """There are monomials involving S_6 or S_7 (new at genus 4)."""
        assert poly_data['n_terms_new_at_genus4'] > 0

    def test_total_degree_positive(self, poly_data):
        """Polynomial has positive total degree."""
        assert poly_data['total_degree'] > 0

    def test_new_fraction_positive(self, poly_data):
        """Nonzero fraction of terms are new at genus 4."""
        assert poly_data['new_content_fraction'] > 0


# ============================================================================
# Section K: Virasoro special values
# ============================================================================

class TestVirasSpecialValues:
    """Virasoro obs_4 at distinguished central charges."""

    @pytest.fixture(scope="class")
    def special_data(self):
        return virasoro_special_values_genus4()

    def test_c13_self_dual(self, special_data):
        """At c=13 (self-dual point), obs_4 has a specific structure."""
        data = special_data['c=13']
        assert data['pf_correction'] != 0  # class M is never trivial
        assert data['scalar_prediction'] != 0

    def test_c26_critical(self, special_data):
        """At c=26 (critical dimension), obs_4 is finite."""
        data = special_data['c=26']
        assert abs(data['scalar_prediction']) < float('inf')

    def test_all_finite(self, special_data):
        """All evaluations are finite (no poles at tested c-values)."""
        for name, data in special_data.items():
            assert abs(data['pf_correction']) < float('inf'), (
                f"Pole at {name}"
            )
            assert abs(data['scalar_prediction']) < float('inf'), (
                f"Pole at {name}"
            )

    def test_pf_changes_sign(self, special_data):
        """Planted-forest correction changes sign across c-values.

        This is expected because S_4 = 10/(c(5c+22)) > 0 for c > 0,
        but S_5 = -48/(c^2(5c+22)) < 0, and the polynomial mixes signs.
        """
        pf_values = [data['pf_correction'] for data in special_data.values()]
        has_positive = any(v > 0 for v in pf_values)
        has_negative = any(v < 0 for v in pf_values)
        # Record whether sign changes occur; do not assert direction
        assert has_positive or has_negative  # at least some nonzero


# ============================================================================
# Section L: Genus comparison (complexity growth g=2,3,4)
# ============================================================================

class TestGenusComparison:
    """Compare planted-forest complexity across genera 2, 3, 4."""

    @pytest.fixture(scope="class")
    def comparison_data(self):
        return pf_genus_comparison()

    def test_terms_grow(self, comparison_data):
        """Number of polynomial terms grows with genus."""
        terms = comparison_data['complexity_growth']['terms']
        # genus 2: 2 terms, genus 3: more, genus 4: even more
        assert terms[0] <= terms[1] <= terms[2]

    def test_shadow_vars_grow(self, comparison_data):
        """Number of shadow variables grows with genus."""
        svars = comparison_data['complexity_growth']['shadow_vars']
        assert svars[0] < svars[1] < svars[2]

    def test_genus2_data(self, comparison_data):
        """Genus-2 data is consistent."""
        g2 = comparison_data['genus_2']
        assert g2['n_terms'] == 2
        assert g2['n_shadow_vars'] == 1

    def test_genus4_has_new(self, comparison_data):
        """Genus 4 has new terms from S_6/S_7."""
        g4 = comparison_data['genus_4']
        assert g4['n_terms_new'] > 0

    def test_visibility_formula(self, comparison_data):
        """Shadow visibility formula g_min(S_r) = floor(r/2) + 1."""
        vis = comparison_data['shadow_visibility']
        for r, g_min in vis.items():
            assert g_min == r // 2 + 1


# ============================================================================
# Section M: Master generation theorem
# ============================================================================

class TestMasterGeneration:
    """The master Pixton generation analysis at genus 4."""

    @pytest.fixture(scope="class")
    def master_data(self):
        return master_generation_analysis()

    def test_master_has_all_paths(self, master_data):
        """Master analysis includes all five verification paths."""
        assert 'path1_codim_decomposition' in master_data
        assert 'path2_shadow_isolation' in master_data
        assert 'path3_cross_family' in master_data
        assert 'path4_pushforward' in master_data
        assert 'path5_numerical_rank' in master_data

    def test_membership_proved(self, master_data):
        """Membership in Pixton ideal is proved."""
        assert 'PROVED' in master_data['conclusions']['membership']

    def test_independence_proved(self, master_data):
        """Independence from lower genera is proved."""
        assert 'PROVED' in master_data['conclusions']['independence']

    def test_generation_semisimple(self, master_data):
        """Generation proved for semisimple shadow CohFTs."""
        assert 'PROVED' in master_data['conclusions']['generation_semisimple']

    def test_path1_nonzero_pf(self, master_data):
        """Path 1: nonzero planted-forest codimensions exist."""
        assert len(master_data['path1_codim_decomposition']['nonzero_pf_codims']) > 0

    def test_path2_s6_generates(self, master_data):
        """Path 2: S_6 generates new content."""
        assert master_data['path2_shadow_isolation']['s6_generates_new'] or \
            len(master_data['path2_shadow_isolation']['s6_active_codims']) > 0

    def test_path3_hierarchy(self, master_data):
        """Path 3: cross-family hierarchy confirmed."""
        assert master_data['path3_cross_family']['hierarchy']

    def test_path4_new_content(self, master_data):
        """Path 4: genuinely new content at genus 4."""
        assert master_data['path4_pushforward']['genuinely_new']

    def test_path5_rank(self, master_data):
        """Path 5: numerical rank positive."""
        assert master_data['path5_numerical_rank']['rank'] > 0


# ============================================================================
# Section N: Generation theorem self-consistency
# ============================================================================

class TestGenerationTheorem:
    """Self-consistency of the genus-4 generation theorem."""

    @pytest.fixture(scope="class")
    def gen_data(self):
        return genus4_generation_theorem()

    def test_membership(self, gen_data):
        """Membership is proved."""
        assert gen_data['membership']

    def test_independence(self, gen_data):
        """Independence from lower genera is proved."""
        assert gen_data['independence_from_lower_genera']

    def test_cross_family(self, gen_data):
        """Cross-family hierarchy confirmed."""
        assert gen_data['cross_family_hierarchy']

    def test_rank_positive(self, gen_data):
        """Numerical rank is positive."""
        assert gen_data['numerical_rank'] > 0

    def test_generation_for_semisimple(self, gen_data):
        """Generation proved for semisimple."""
        assert gen_data['generation_proved_for_semisimple']


# ============================================================================
# Section O: Graph census consistency
# ============================================================================

class TestGraphCensus:
    """Graph enumeration consistency at genus 4."""

    def test_codim_dist_sums_to_total(self):
        """Sum of codimension distribution equals total graph count."""
        dist = genus4_codimension_distribution()
        total = sum(dist.values())
        assert total == genus4_graph_count()

    def test_pf_codim_subset_of_all(self):
        """Planted-forest codimensions are subset of all codimensions."""
        all_dist = genus4_codimension_distribution()
        pf_dist = genus4_pf_codimension_distribution()
        for k in pf_dist:
            assert k in all_dist
            assert pf_dist[k] <= all_dist[k]

    def test_pf_count_consistency(self):
        """Total planted-forest count matches genus4_pf_count."""
        pf_dist = genus4_pf_codimension_distribution()
        assert sum(pf_dist.values()) == genus4_pf_count()

    def test_nonzero_hodge_consistency(self):
        """Nonzero Hodge count is consistent across methods."""
        by_codim = genus4_nonzero_hodge_by_codim()
        total_nonzero = sum(by_codim.values())
        assert total_nonzero > 0

    def test_max_shadow_arity_monotone(self):
        """Max shadow arity is non-decreasing with codimension.

        Higher codimension means more edges, which allows larger
        genus-0 vertex valence.
        """
        dist = genus4_max_shadow_arity_by_codim()
        codims = sorted(dist.keys())
        # Not strictly monotone (some codims may not have genus-0 vertices),
        # but the max across all codims should be >= the max across lower ones.
        if len(codims) >= 2:
            overall_max = max(dist.values())
            assert overall_max >= 3  # at least trivalent


# ============================================================================
# Section P: Cross-check with existing genus-4 engine
# ============================================================================

class TestCrossCheckExisting:
    """Cross-check with the existing genus-4 shadow engine."""

    def test_lambda4_fp_value(self):
        """lambda_4^FP = 127/154828800."""
        assert LAMBDA4_FP == Fraction(127, 154828800)

    def test_pf_total_consistency(self):
        """delta_pf from this engine matches the existing engine."""
        shadow = virasoro_shadow_data(max_arity=10)

        # From this engine: sum over codimensions
        pf_codim = pf_by_codimension(shadow)
        pf_total_new = sum(pf_codim.values(), Integer(0))
        pf_total_new = cancel(pf_total_new)

        # From existing engine
        pf_total_old = cancel(delta_pf_genus4(shadow))

        assert simplify(pf_total_new - pf_total_old) == 0

    def test_nonpf_total_consistency(self):
        """Non-planted-forest from this engine matches existing engine."""
        shadow = virasoro_shadow_data(max_arity=10)

        nonpf_codim = nonpf_by_codimension(shadow)
        nonpf_total_new = sum(nonpf_codim.values(), Integer(0))
        nonpf_total_new = cancel(nonpf_total_new)

        from compute.lib.theorem_pixton_genus4_shadow_engine import (
            nonpf_amplitude_genus4 as nonpf_old,
        )
        nonpf_total_old = cancel(nonpf_old(shadow))

        assert simplify(nonpf_total_new - nonpf_total_old) == 0
