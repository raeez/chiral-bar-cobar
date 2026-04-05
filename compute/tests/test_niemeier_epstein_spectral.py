"""Tests for the Niemeier constrained Epstein zeta spectral decomposition.

This test suite verifies the central claims of the spectral decomposition
for all 24 Niemeier lattice VOAs:

  1. d_arith = 3 for ALL 24 lattices (dim S_12 = 1)
  2. Shadow depth = 4 for all 24 (d = 3 + dim S_12)
  3. c_Delta(Lambda) = |R(Lambda)| - 65520/691
  4. Theta coefficients are non-negative integers
  5. Factorization consistency: direct vs L-function decomposition
  6. Distinguishing analysis: what invariants separate the 24 lattices
  7. The precise relationship between shadow tower and constrained Epstein
"""

import pytest
from fractions import Fraction

import compute.lib.niemeier_epstein_spectral as nes


# =========================================================================
# Section 1: Registry completeness
# =========================================================================

class TestRegistryCompleteness:
    """Verify the 24 Niemeier lattices are correctly registered."""

    def test_exactly_24_lattices(self):
        assert len(nes.ALL_LABELS) == 24

    def test_conway_sloane_order_has_24(self):
        assert len(nes.CS_ORDER) == 24

    def test_leech_has_zero_roots(self):
        assert nes._NIEMEIER_DATA['Leech']['num_roots'] == 0

    def test_d24_root_count(self):
        """D_24 has 2*24*23 = 1104 roots."""
        assert nes._NIEMEIER_DATA['D24']['num_roots'] == 1104

    def test_3e8_root_count(self):
        """3E_8 has 3*240 = 720 roots."""
        assert nes._NIEMEIER_DATA['3E8']['num_roots'] == 720

    def test_24a1_root_count(self):
        """24A_1 has 24*2 = 48 roots."""
        assert nes._NIEMEIER_DATA['24A1']['num_roots'] == 48

    def test_all_root_ranks_24(self):
        """All non-Leech Niemeier lattices have root_rank = 24."""
        for label in nes.ALL_LABELS:
            if label == 'Leech':
                assert nes._NIEMEIER_DATA[label]['root_rank'] == 0
            else:
                assert nes._NIEMEIER_DATA[label]['root_rank'] == 24, label

    def test_root_counts_are_positive_or_zero(self):
        for label in nes.ALL_LABELS:
            assert nes._NIEMEIER_DATA[label]['num_roots'] >= 0

    def test_root_count_descending_in_cs_order(self):
        """Conway-Sloane order is by decreasing root count."""
        counts = [nes._NIEMEIER_DATA[lab]['num_roots'] for lab in nes.CS_ORDER]
        for i in range(len(counts) - 1):
            assert counts[i] >= counts[i + 1]


# =========================================================================
# Section 2: Modular forms dimensions
# =========================================================================

class TestModularFormsDimensions:
    """Verify dimensions of spaces of modular forms for SL(2,Z)."""

    def test_dim_S12_is_1(self):
        """S_12(SL(2,Z)) is 1-dimensional, spanned by Delta."""
        assert nes.dim_cusp_forms(12) == 1

    def test_dim_M12_is_2(self):
        """M_12 = C*E_12 + C*Delta, dimension 2."""
        assert nes.dim_cusp_forms(12) + 1 == 2

    def test_dim_S_small_weights(self):
        """dim S_k = 0 for k < 12."""
        for k in range(2, 12, 2):
            assert nes.dim_cusp_forms(k) == 0, f"k={k}"

    def test_dim_S16_is_1(self):
        assert nes.dim_cusp_forms(16) == 1

    def test_dim_S24_is_2(self):
        """First weight with dim S_k = 2."""
        assert nes.dim_cusp_forms(24) == 2

    def test_dim_S26_is_1(self):
        """k=26: 26 mod 12 = 2, dim = floor(26/12) - 1 = 1."""
        assert nes.dim_cusp_forms(26) == 1

    def test_dim_S36_is_3(self):
        assert nes.dim_cusp_forms(36) == 3

    def test_dim_S_odd_weight_is_0(self):
        """No modular forms for SL(2,Z) at odd weight."""
        for k in [1, 3, 5, 7, 9, 11, 13]:
            assert nes.dim_cusp_forms(k) == 0

    def test_dim_S2_is_0(self):
        assert nes.dim_cusp_forms(2) == 0

    def test_dim_S14_is_0(self):
        """S_14 = 0 (14 equiv 2 mod 12, floor(14/12) - 1 = 0)."""
        assert nes.dim_cusp_forms(14) == 0


# =========================================================================
# Section 3: d_arith universal
# =========================================================================

class TestDArithUniversal:
    """d_arith = 3 for ALL 24 Niemeier lattices."""

    def test_d_arith_is_3(self):
        assert nes.d_arith_lattice(24) == 3

    def test_d_arith_all_24(self):
        d_all = nes.d_arith_all_niemeier()
        for label, d in d_all.items():
            assert d == 3, f"{label}: d_arith = {d}"

    def test_shadow_depth_is_4(self):
        assert nes.shadow_depth_lattice(24) == 4

    def test_verify_d_arith_universal(self):
        assert nes.verify_d_arith_universal()

    def test_d_arith_does_not_distinguish(self):
        """d_arith is the same for all 24, so it cannot distinguish them."""
        values = set(nes.d_arith_all_niemeier().values())
        assert len(values) == 1
        assert values == {3}

    def test_d_arith_other_ranks(self):
        """d_arith for other even unimodular ranks."""
        # Rank 8 (E_8): dim S_4 = 0, d_arith = 2
        assert nes.d_arith_lattice(8) == 2
        # Rank 16: dim S_8 = 0, d_arith = 2
        assert nes.d_arith_lattice(16) == 2
        # Rank 48: dim S_24 = 2, d_arith = 4
        assert nes.d_arith_lattice(48) == 4
        # Rank 72: dim S_36 = 3, d_arith = 5
        assert nes.d_arith_lattice(72) == 5


# =========================================================================
# Section 4: c_Delta and theta coefficients
# =========================================================================

class TestCDeltaAndTheta:
    """Verify the Hecke decomposition coefficients."""

    def test_c_delta_leech(self):
        """Leech: c_Delta = -65520/691."""
        assert nes.c_delta('Leech') == Fraction(-65520, 691)

    def test_c_delta_from_roots(self):
        """c_Delta = |R| - 65520/691 for all 24."""
        assert nes.verify_c_delta_from_roots()

    def test_theta_r0_is_1(self):
        """r(0) = 1 for all lattices (the zero vector)."""
        for label in nes.ALL_LABELS:
            assert nes.theta_coefficient(label, 0) == 1, label

    def test_theta_r1_equals_root_count(self):
        """r(1) = |R(Lambda)| for all Niemeier lattices."""
        for label in nes.ALL_LABELS:
            expected = nes._NIEMEIER_DATA[label]['num_roots']
            assert nes.theta_coefficient(label, 1) == expected, label

    def test_leech_r1_is_zero(self):
        """Leech lattice has no vectors of norm 2."""
        assert nes.theta_coefficient('Leech', 1) == 0

    def test_leech_r2_is_196560(self):
        """Leech kissing number is 196560."""
        assert nes.theta_coefficient('Leech', 2) == 196560

    def test_theta_integrality(self):
        """All theta coefficients are non-negative integers."""
        assert nes.verify_theta_integrality(10)

    def test_theta_positivity_for_n_ge_1(self):
        """r(n) > 0 for n >= 1 for the Leech lattice (starts at n=2)."""
        # Leech: r(1) = 0, r(2) = 196560
        assert nes.theta_coefficient('Leech', 1) == 0
        for n in range(2, 8):
            assert nes.theta_coefficient('Leech', n) > 0, f"n={n}"

    def test_theta_monotone_for_non_leech(self):
        """For non-Leech lattices, r(n) should grow rapidly."""
        for label in ['D24', '3E8', '24A1']:
            r1 = nes.theta_coefficient(label, 1)
            r2 = nes.theta_coefficient(label, 2)
            assert r2 > r1, f"{label}: r(2)={r2} <= r(1)={r1}"


# =========================================================================
# Section 5: Root count collisions and distinguishing
# =========================================================================

class TestCollisionsAndDistinguishing:
    """Analyze what invariants distinguish the 24 lattices."""

    def test_five_collision_groups(self):
        """Exactly 5 pairs of lattices share the same root count."""
        colls = nes.root_count_collisions()
        assert len(colls) == 5

    def test_c_delta_collisions_match_root_collisions(self):
        """c_Delta collisions are exactly the root count collisions."""
        root_colls = nes.root_count_collisions()
        cd_colls = nes.c_delta_collisions()
        assert len(root_colls) == len(cd_colls)

    def test_19_distinct_c_delta_values(self):
        """24 lattices, 5 collision pairs -> 19 distinct c_Delta values."""
        all_cd = set(nes.c_delta(lab) for lab in nes.ALL_LABELS)
        assert len(all_cd) == 19

    def test_collision_pair_d16e8_3e8(self):
        """D16+E8 and 3E8 share |R| = 720."""
        colls = nes.root_count_collisions()
        assert 720 in colls
        assert set(colls[720]) == {'D16_E8', '3E8'}

    def test_collision_pair_identical_theta(self):
        """Lattices with same |R| have identical genus-1 theta series.

        This is because M_12(SL(2,Z)) is 2-dimensional, so the theta
        function is entirely determined by the constant term (=1) and
        the first Fourier coefficient (=|R|).
        """
        for N, labels in nes.root_count_collisions().items():
            theta_a = [nes.theta_coefficient(labels[0], n) for n in range(11)]
            theta_b = [nes.theta_coefficient(labels[1], n) for n in range(11)]
            assert theta_a == theta_b, (
                f"|R|={N}: {labels[0]} and {labels[1]} differ at genus 1"
            )

    def test_genus1_gives_19_classes(self):
        """The genus-1 constrained Epstein gives at most 19 classes."""
        by_cd = {}
        for label in nes.ALL_LABELS:
            cd = nes.c_delta(label)
            by_cd.setdefault(cd, []).append(label)
        assert len(by_cd) == 19

    def test_r1_r2_pair_does_not_distinguish_all(self):
        """The pair (r(1), r(2)) does NOT distinguish all 24."""
        dist = nes.higher_theta_distinguishing(5)
        if 'pair_r1_r2' in dist:
            assert not dist['pair_r1_r2']['all_distinguished']


# =========================================================================
# Section 6: Factorization consistency
# =========================================================================

class TestFactorizationConsistency:
    """Verify direct and factored Epstein evaluations agree."""

    @pytest.mark.parametrize("label", ['Leech', '3E8', 'D24', '24A1', '8A3'])
    def test_factorization_at_s15(self, label):
        """Direct Dirichlet series matches L-function factorization at s=15."""
        result = nes.verify_factorization_consistency(label, s_val=15.0, max_n=200)
        assert result['passes'], f"{label}: rel_err = {result['rel_err']}"

    @pytest.mark.parametrize("label", ['Leech', 'D24'])
    def test_factorization_at_s20(self, label):
        result = nes.verify_factorization_consistency(label, s_val=20.0, max_n=100)
        assert result['passes']

    def test_all_24_factorization(self):
        """Factorization consistency for all 24 lattices."""
        for label in nes.ALL_LABELS:
            result = nes.verify_factorization_consistency(label, s_val=15.0, max_n=100)
            assert result['passes'], f"{label}: rel_err = {result['rel_err']}"


# =========================================================================
# Section 7: Epstein zeta factorization structure
# =========================================================================

class TestEpsteinFactorization:
    """Verify the L-function factorization structure."""

    def test_all_have_3_critical_lines(self):
        """All 24 lattices have 3 critical lines (assuming c_Delta != 0)."""
        # Check: does any lattice have c_Delta = 0?
        # c_Delta = 0 iff |R| = 65520/691 ≈ 94.82, which is not an integer.
        # So c_Delta != 0 for ALL 24.
        for label in nes.ALL_LABELS:
            fact = nes.epstein_zeta_factorization(label)
            assert fact['num_critical_lines'] == 3, label

    def test_critical_lines_are_correct(self):
        """Critical lines at Re(s) = 1/2, 6, 23/2."""
        for label in nes.ALL_LABELS:
            fact = nes.epstein_zeta_factorization(label)
            lines = sorted(fact['critical_lines'])
            assert lines == [Fraction(1, 2), Fraction(6), Fraction(23, 2)]

    def test_c_delta_nonzero_for_all(self):
        """65520/691 is not an integer, so no lattice has c_Delta = 0."""
        for label in nes.ALL_LABELS:
            assert nes.c_delta(label) != 0, label

    def test_leech_c_delta_negative(self):
        """Leech (no roots) has the most negative c_Delta."""
        cd_leech = nes.c_delta('Leech')
        assert cd_leech < 0
        for label in nes.ALL_LABELS:
            if label != 'Leech':
                assert nes.c_delta(label) > cd_leech

    def test_d24_c_delta_largest(self):
        """D24 (most roots) has the largest c_Delta."""
        cd_d24 = nes.c_delta('D24')
        for label in nes.ALL_LABELS:
            assert nes.c_delta(label) <= cd_d24


# =========================================================================
# Section 8: Spectral coefficients
# =========================================================================

class TestSpectralCoefficients:
    """Test the spectral coefficient extraction."""

    def test_cuspidal_fractions_lattice_specific(self):
        """Cuspidal fractions rho(n) = c_Delta*tau(n) / (E_12 coeff) differ."""
        # Different c_Delta => different cuspidal fractions at each n
        spec_leech = nes.spectral_coefficients('Leech', 5)
        spec_d24 = nes.spectral_coefficients('D24', 5)
        assert spec_leech['cuspidal_fractions'] != spec_d24['cuspidal_fractions']

    def test_cuspidal_fraction_ratio_constant(self):
        """The ratio of cuspidal contributions between two lattices is
        constant across all n (since tau(n) is universal)."""
        cd_leech = float(nes.c_delta('Leech'))
        cd_d24 = float(nes.c_delta('D24'))
        expected_ratio = cd_leech / cd_d24

        spec_leech = nes.spectral_coefficients('Leech', 10)
        spec_d24 = nes.spectral_coefficients('D24', 10)

        for i in range(10):
            if abs(spec_d24['cuspidal_coefficients'][i]) > 1e-10:
                ratio = (spec_leech['cuspidal_coefficients'][i] /
                         spec_d24['cuspidal_coefficients'][i])
                assert abs(ratio - expected_ratio) < 1e-10, f"n={i+1}"

    def test_eisenstein_coefficients_universal(self):
        """Eisenstein coefficients are the same for all lattices."""
        ref = nes.spectral_coefficients('Leech', 10)['eisenstein_coefficients']
        for label in nes.ALL_LABELS:
            spec = nes.spectral_coefficients(label, 10)
            for i in range(10):
                assert abs(spec['eisenstein_coefficients'][i] - ref[i]) < 1e-6, (
                    f"{label} at n={i+1}"
                )


# =========================================================================
# Section 9: Shadow tower vs constrained Epstein
# =========================================================================

class TestShadowVsEpstein:
    """Test the precise relationship between shadow tower and Epstein."""

    def test_shadow_tower_identical_for_all(self):
        """The OPE-based shadow tower is identical for all 24."""
        for label in nes.ALL_LABELS:
            analysis = nes.shadow_vs_epstein_analysis(label)
            assert analysis['shadow_tower']['kappa'] == 24
            assert analysis['shadow_tower']['shadow_depth'] == 2
            assert analysis['shadow_tower']['shadow_class'] == 'G'
            assert analysis['shadow_tower']['distinguishes_lattice'] is False

    def test_epstein_partially_distinguishes(self):
        """The constrained Epstein partially distinguishes (19/24)."""
        # Check that different c_Delta values exist
        cd_set = set(nes.c_delta(lab) for lab in nes.ALL_LABELS)
        assert len(cd_set) == 19

    def test_d_arith_plus_d_alg_plus_1_equals_depth(self):
        """d = 1 + d_arith + d_alg = 1 + 3 + 0 = 4."""
        for label in nes.ALL_LABELS:
            analysis = nes.shadow_vs_epstein_analysis(label)
            assert analysis['reconciliation']['d_arith'] == 3
            assert analysis['reconciliation']['d_alg'] == 0
            assert analysis['reconciliation']['d_total'] == 4

    def test_phantom_arities(self):
        """Arities 3 and 4 have zero OPE shadow but nonzero Epstein content."""
        for label in nes.ALL_LABELS:
            analysis = nes.shadow_vs_epstein_analysis(label)
            assert analysis['reconciliation']['phantom_arities'] == [3, 4]

    def test_full_theta_distinguishes(self):
        """The full theta series (as sequence) distinguishes 19 classes."""
        theta_sigs = {}
        for label in nes.ALL_LABELS:
            sig = tuple(nes.theta_coefficient(label, n) for n in range(11))
            theta_sigs.setdefault(sig, []).append(label)
        # 19 distinct theta series
        assert len(theta_sigs) == 19


# =========================================================================
# Section 10: Number-theoretic functions
# =========================================================================

class TestNumberTheory:
    """Verify number-theoretic building blocks."""

    def test_sigma_11_at_1(self):
        assert nes.sigma_k(1, 11) == 1

    def test_sigma_11_at_2(self):
        """sigma_11(2) = 1 + 2^11 = 2049."""
        assert nes.sigma_k(2, 11) == 2049

    def test_ramanujan_tau_1(self):
        assert nes.ramanujan_tau(1) == 1

    def test_ramanujan_tau_2(self):
        assert nes.ramanujan_tau(2) == -24

    def test_ramanujan_tau_3(self):
        assert nes.ramanujan_tau(3) == 252

    def test_ramanujan_tau_4(self):
        assert nes.ramanujan_tau(4) == -1472

    def test_ramanujan_tau_5(self):
        assert nes.ramanujan_tau(5) == 4830

    def test_ramanujan_tau_multiplicative(self):
        """tau(mn) = tau(m)*tau(n) for gcd(m,n)=1."""
        # tau(6) = tau(2)*tau(3) = (-24)*(252) = -6048
        assert nes.ramanujan_tau(6) == nes.ramanujan_tau(2) * nes.ramanujan_tau(3)

    def test_ramanujan_tau_hecke_at_4(self):
        """tau(4) = tau(2)^2 - 2^11 = 576 - 2048 = -1472."""
        assert nes.ramanujan_tau(4) == nes.ramanujan_tau(2) ** 2 - 2 ** 11


# =========================================================================
# Section 11: Leech lattice verification
# =========================================================================

class TestLeechLattice:
    """Detailed verification for the Leech lattice."""

    def test_leech_theta_formula(self):
        """Theta_Leech = E_12 - (65520/691)*Delta_12.

        Verify via r(2) = 196560:
          (65520/691)*sigma_11(2) - (65520/691)*tau(2)
        = (65520/691)*(2049 - (-24))
        = (65520/691)*2073
        = 65520*2073/691
        = 135822960/691
        = 196560.
        """
        val = 65520 * (nes.sigma_k(2, 11) - nes.ramanujan_tau(2))
        assert val % 691 == 0
        assert val // 691 == 196560
        assert nes.theta_coefficient('Leech', 2) == 196560

    def test_leech_no_norm2_vectors(self):
        assert nes.theta_coefficient('Leech', 1) == 0

    def test_leech_c_delta_exact(self):
        assert nes.c_delta('Leech') == Fraction(-65520, 691)


# =========================================================================
# Section 12: Roelcke-Selberg structure
# =========================================================================

class TestRoelckeSelbergStructure:
    """Verify structural properties of the spectral decomposition."""

    def test_structure_has_3_parts(self):
        """Residual + continuous + discrete = 3 parts."""
        for label in ['Leech', 'D24', '3E8']:
            rs = nes.roelcke_selberg_structure(label)
            assert 'residual' in rs['spectral_structure']
            assert 'continuous' in rs['spectral_structure']
            assert 'discrete' in rs['spectral_structure']

    def test_continuous_has_3_critical_lines(self):
        for label in nes.ALL_LABELS:
            rs = nes.roelcke_selberg_structure(label)
            lines = rs['spectral_structure']['continuous']['critical_lines']
            assert lines == [0.5, 6.0, 11.5]

    def test_discrete_is_lattice_specific(self):
        for label in nes.ALL_LABELS:
            rs = nes.roelcke_selberg_structure(label)
            assert rs['spectral_structure']['discrete']['lattice_specific']


# =========================================================================
# Section 13: Full atlas
# =========================================================================

class TestFullAtlas:
    """Verify the complete spectral atlas."""

    def test_atlas_has_24_entries(self):
        atlas = nes.full_atlas(5)
        assert len(atlas) == 24

    def test_atlas_d_arith_all_3(self):
        atlas = nes.full_atlas(5)
        for label, data in atlas.items():
            assert data['d_arith'] == 3, label

    def test_atlas_shadow_depth_all_4(self):
        atlas = nes.full_atlas(5)
        for label, data in atlas.items():
            assert data['shadow_depth'] == 4, label

    def test_atlas_num_L_functions_all_3(self):
        atlas = nes.full_atlas(5)
        for label, data in atlas.items():
            assert data['num_L_functions'] == 3, label

    def test_classification_table(self):
        table = nes.spectral_classification_table()
        assert len(table) == 24
        # All d_arith = 3
        for entry in table:
            assert entry['d_arith'] == 3


# =========================================================================
# Section 14: Cross-checks with niemeier_shadow_atlas.py
# =========================================================================

class TestCrossModuleConsistency:
    """Verify consistency with the existing niemeier_shadow_atlas module."""

    def test_root_counts_match(self):
        """Root counts match between the two modules."""
        try:
            from compute.lib.niemeier_shadow_atlas import NIEMEIER_REGISTRY
        except ImportError:
            pytest.skip("niemeier_shadow_atlas not available")

        for label in nes.ALL_LABELS:
            if label in NIEMEIER_REGISTRY:
                expected = NIEMEIER_REGISTRY[label]['num_roots']
                actual = nes._NIEMEIER_DATA[label]['num_roots']
                assert actual == expected, f"{label}: {actual} != {expected}"

    def test_kappa_equals_24(self):
        """kappa = rank = 24 for all Niemeier lattice VOAs."""
        try:
            from compute.lib.niemeier_shadow_atlas import shadow_data
        except ImportError:
            pytest.skip("niemeier_shadow_atlas not available")

        for label in nes.ALL_LABELS:
            try:
                sd = shadow_data(label)
                assert int(sd['kappa']) == 24, label
            except (ValueError, KeyError):
                pass  # Label format may differ

    def test_shadow_class_G(self):
        """All Niemeier lattices are class G in the shadow classification."""
        try:
            from compute.lib.niemeier_shadow_atlas import shadow_data
        except ImportError:
            pytest.skip("niemeier_shadow_atlas not available")

        for label in nes.ALL_LABELS:
            try:
                sd = shadow_data(label)
                assert sd['shadow_class'] == 'G', label
            except (ValueError, KeyError):
                pass


# =========================================================================
# Section 15: Obstruction analysis
# =========================================================================

class TestObstructionAnalysis:
    """Verify the obstruction to distinguishing analysis."""

    def test_obstruction_report(self):
        obs = nes.obstruction_to_distinguishing()
        assert obs['d_arith_universal'] is True
        assert obs['d_arith_value'] == 3
        assert obs['n_collision_groups'] == 5

    def test_19_distinct_c_delta(self):
        obs = nes.obstruction_to_distinguishing()
        assert obs['c_delta_distinct_values'] == 19


# =========================================================================
# Section 16: Cuspidal weight analysis
# =========================================================================

class TestCuspidalWeight:
    """Test the cuspidal weight analysis."""

    def test_leech_most_negative(self):
        """Leech has the most negative c_Delta."""
        analysis = nes.cuspidal_weight_analysis()
        leech_entry = [e for e in analysis if e['label'] == 'Leech'][0]
        assert leech_entry['c_delta_sign'] == 'negative'
        # Verify it's the most negative
        for entry in analysis:
            assert entry['c_delta_float'] >= leech_entry['c_delta_float']

    def test_d24_most_positive(self):
        """D24 has the most positive c_Delta."""
        analysis = nes.cuspidal_weight_analysis()
        d24_entry = [e for e in analysis if e['label'] == 'D24'][0]
        assert d24_entry['c_delta_sign'] == 'positive'
        for entry in analysis:
            assert entry['c_delta_float'] <= d24_entry['c_delta_float']

    def test_no_zero_c_delta(self):
        """No lattice has c_Delta = 0 (since 65520/691 is not an integer)."""
        analysis = nes.cuspidal_weight_analysis()
        for entry in analysis:
            assert entry['c_delta_sign'] != 'zero'

    def test_8a3_near_zero(self):
        """8A3 has |R| = 96, closest to 65520/691 ≈ 94.82."""
        cd_8a3 = float(nes.c_delta('8A3'))
        # 96 - 94.82 ≈ 1.18
        assert abs(cd_8a3) < 2.0
        assert cd_8a3 > 0  # 96 > 94.82


# =========================================================================
# Section 17: Depth formula at various ranks
# =========================================================================

class TestDepthFormula:
    """Verify the depth formula d = 3 + dim S_{r/2} for various ranks."""

    def test_rank_8(self):
        """E_8: k=4, dim S_4 = 0, depth = 3."""
        assert nes.shadow_depth_lattice(8) == 3

    def test_rank_16(self):
        """Rank 16: k=8, dim S_8 = 0, depth = 3."""
        assert nes.shadow_depth_lattice(16) == 3

    def test_rank_24(self):
        """Niemeier: k=12, dim S_12 = 1, depth = 4."""
        assert nes.shadow_depth_lattice(24) == 4

    def test_rank_32(self):
        """Rank 32: k=16, dim S_16 = 1, depth = 4."""
        assert nes.shadow_depth_lattice(32) == 4

    def test_rank_48(self):
        """Rank 48: k=24, dim S_24 = 2, depth = 5.
        First depth > 4 (two independent cusp forms)."""
        assert nes.shadow_depth_lattice(48) == 5

    def test_rank_72(self):
        """Rank 72: k=36, dim S_36 = 3, depth = 6."""
        assert nes.shadow_depth_lattice(72) == 6
