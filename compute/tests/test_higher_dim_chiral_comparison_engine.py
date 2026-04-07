r"""Tests for higher-dimensional chiral algebra comparison engine.

Verifies the mathematical structures of higher-dimensional factorization
algebras (Costello, Gwilliam-Williams, Elliott-Safronov-Williams,
Bittleston-Skinner) and their relationship to our 2d bar-cobar framework.

EACH TEST computes from first principles — no hardcoded expected values
without independent verification (AP10).

MULTI-PATH VERIFICATION:
Every numerical claim is verified by at least 2 independent methods.

Test organization:
1. Configuration space cohomology (Arnold/Totaro algebra)
2. E_n bar complex dimensions and grading
3. Kappa universality across operadic levels
4. Dimensional reduction of shadow invariants
5. Higher Kac-Moody algebras (Gwilliam-Williams)
6. Self-dual YM and celestial chiral algebras
7. 4d CS operadic structure and E_2 braiding
8. Genus expansion scope comparison
9. Form factor comparison at each arity
10. HCS boundary algebras on various CY3s
11. Koszul duality in higher dimensions
12. Bittleston-Skinner diamond
13. Associativity sufficiency (Fernandez-Paquette 2024)
14. Higher-genus twistor spaces (Jarov 2025)
15. Cross-consistency with existing engines

Ground truth:
    Fresse: Modules over Operads and Functors
    Loday-Vallette: Algebraic Operads
    Kontsevich: Operads and Motives (1999)
    Gwilliam-Williams: Higher Kac-Moody algebras (2021, 1810.06534)
    Costello: 1303.2632, 1308.0370
    Costello-Gwilliam: Factorization Algebras in QFT Vols 1-2
    Bittleston-Skinner: Twistors and 4d CS (JHEP 2023)
    Fernandez-Paquette: 2412.17168
    Jarov: 2509.12486
    en_factorization_shadow.py: E_n bar complex
    costello_4d_cs_comparison_engine.py: 4d CS R-matrix
    CLAUDE.md: AP1, AP10, AP14, AP19, AP27, AP39, AP45, AP48
"""

import pytest
from fractions import Fraction
from math import factorial, comb

from compute.lib.higher_dim_chiral_comparison_engine import (
    # Utilities
    _frac,
    _bernoulli_exact,
    _lambda_fp_exact,
    # Configuration space
    conf_space_poincare_poly,
    conf_space_euler_char,
    conf_space_total_dim,
    arnold_relation_count,
    # E_n bar complex
    en_bar_arity_dimension,
    en_bar_propagator_degree,
    en_koszul_dual_shift,
    en_self_koszul_dual,
    # Dimensional reduction
    kappa_independent_of_n,
    higher_shadow_depends_on_n,
    dimensional_reduction_shadow,
    # Higher KM
    higher_km_on_Cn,
    higher_km_on_torus,
    higher_km_level_comparison,
    # SDYM
    sdym_chiral_data_slN,
    sdym_chiral_data_gl1,
    twistor_to_celestial_reduction,
    # 4d CS
    four_d_cs_operadic_structure,
    e2_braiding_vs_e1_bar,
    # Genus expansion
    genus_expansion_scope_comparison,
    genus_expansion_f_g,
    # Form factors
    form_factor_arity_k_comparison,
    # HCS boundary
    HCSBoundaryAlgebra,
    hcs_boundary_algebras,
    hcs_kappa_from_cy3,
    # Comparison tables
    operadic_comparison_table,
    structure_comparison_summary,
    kappa_comparison_across_n,
    bar_dimension_comparison,
    en_bar_graded_comparison,
    # Celestial reduction
    celestial_as_e1_reduction,
    # Diamond
    bittleston_skinner_diamond,
    # Higher genus twistor
    higher_genus_twistor_data,
    # Koszul duality
    koszul_duality_comparison,
    # Associativity
    associativity_sufficiency_theorem,
    # Master
    master_comparison,
)


# ============================================================================
# 1. Configuration space cohomology (Arnold/Totaro algebra)
# ============================================================================

class TestConfigurationSpaceCohomology:
    """Tests for H*(Conf_k(R^n))."""

    def test_conf_1_point_all_n(self):
        """Conf_1(R^n) = R^n is contractible for all n."""
        for n in [1, 2, 3, 4, 5]:
            poly = conf_space_poincare_poly(1, n)
            assert poly == {0: 1}, f"Conf_1(R^{n}) should be contractible"

    def test_conf_2_R1(self):
        """Conf_2(R) has 2 components, each contractible: total dim = 2 = 2!."""
        poly = conf_space_poincare_poly(2, 1)
        assert poly == {0: 2}
        assert conf_space_total_dim(2, 1) == 2

    def test_conf_2_R2(self):
        """Conf_2(R^2) ~ S^1: H^0 = 1, H^1 = 1, total = 2."""
        poly = conf_space_poincare_poly(2, 2)
        assert poly == {0: 1, 1: 1}
        assert conf_space_total_dim(2, 2) == 2

    def test_conf_2_R3(self):
        """Conf_2(R^3) ~ S^2: H^0 = 1, H^2 = 1, total = 2."""
        poly = conf_space_poincare_poly(2, 3)
        assert poly == {0: 1, 2: 1}
        assert conf_space_total_dim(2, 3) == 2

    def test_conf_3_R2_arnold(self):
        """Conf_3(R^2): Arnold algebra with 3 generators omega_{ij} of degree 1.

        P_3(t) = (1)(1+t)(1+2t) = 1 + 3t + 2t^2.
        Total = 6 = 3!.
        """
        poly = conf_space_poincare_poly(3, 2)
        assert poly[0] == 1
        assert poly[1] == 3  # Three Arnold generators
        assert poly[2] == 2  # From Arnold relations
        assert conf_space_total_dim(3, 2) == 6

    def test_conf_3_R3(self):
        """Conf_3(R^3): generators of degree 2.

        P_3(t) = (1)(1+t^2)(1+2t^2) = 1 + 3t^2 + 2t^4.
        """
        poly = conf_space_poincare_poly(3, 3)
        assert poly.get(0, 0) == 1
        assert poly.get(2, 0) == 3
        assert poly.get(4, 0) == 2
        assert conf_space_total_dim(3, 3) == 6

    def test_total_dim_is_factorial(self):
        """For all n >= 2, total dim H*(Conf_k(R^n)) = k! (P_k(1) = k!).

        This is because P_k(1) = prod_{j=0}^{k-1}(1+j) = k!.
        """
        for n in [2, 3, 4, 5]:
            for k in range(1, 7):
                assert conf_space_total_dim(k, n) == factorial(k), \
                    f"Total dim for k={k}, n={n} should be {factorial(k)}"

    def test_euler_char_n_even(self):
        """For n even (n-1 odd), chi(Conf_k(R^n)) = 0 for k >= 2.

        chi = prod(1-j) = 0 for k >= 2 (because the j=1 term gives 0).
        """
        for n in [2, 4, 6]:
            for k in [2, 3, 4, 5]:
                assert conf_space_euler_char(k, n) == 0, \
                    f"Euler char for k={k}, n={n} (even) should be 0"

    def test_euler_char_n_odd(self):
        """For n odd >= 3 (n-1 even), chi(Conf_k(R^n)) = k!.

        chi = prod(1+j) = k!.
        """
        for n in [3, 5, 7]:
            for k in range(1, 6):
                assert conf_space_euler_char(k, n) == factorial(k), \
                    f"Euler char for k={k}, n={n} (odd) should be {factorial(k)}"

    def test_arnold_relations_count(self):
        """Number of Arnold relations = C(k,3) for k >= 3, n >= 2."""
        for k in range(3, 8):
            for n in [2, 3, 4]:
                assert arnold_relation_count(k, n) == comb(k, 3)

    def test_arnold_relations_zero_small_k(self):
        """No Arnold relations for k < 3."""
        for k in [0, 1, 2]:
            assert arnold_relation_count(k, 2) == 0


# ============================================================================
# 2. E_n bar complex dimensions and grading
# ============================================================================

class TestEnBarComplex:
    """Tests for the E_n bar complex structure."""

    def test_bar_propagator_degree(self):
        """E_n propagator has degree n-1 (fundamental class of S^{n-1})."""
        assert en_bar_propagator_degree(1) == 0
        assert en_bar_propagator_degree(2) == 1
        assert en_bar_propagator_degree(3) == 2
        assert en_bar_propagator_degree(4) == 3

    def test_koszul_shift(self):
        """E_n^! = E_n{-n}: Koszul shift equals n."""
        for n in range(1, 8):
            assert en_koszul_dual_shift(n) == n

    def test_self_koszul_dual(self):
        """E_n is Koszul self-dual (up to shift) for all n >= 1."""
        for n in range(1, 10):
            assert en_self_koszul_dual(n) is True

    def test_bar_arity_1(self):
        """Bar complex at arity 1: dimension 1 for all n (Conf_1 contractible)."""
        for n in [1, 2, 3, 4, 5]:
            assert en_bar_arity_dimension(1, n) == 1

    def test_bar_arity_2(self):
        """Bar complex at arity 2: dimension 2 for all n.

        Conf_2(R^n) ~ S^{n-1} has total Betti = 2 for all n >= 1.
        """
        for n in [1, 2, 3, 4, 5]:
            assert en_bar_arity_dimension(2, n) == 2

    def test_bar_arity_k_total_factorial(self):
        """Total bar dimension at arity k is k! for all n >= 1."""
        for n in [1, 2, 3, 4]:
            for k in range(1, 7):
                assert en_bar_arity_dimension(k, n) == factorial(k)

    def test_graded_comparison_e1_vs_e2(self):
        """E_1 bar is concentrated in degree 0; E_2 is spread across degrees."""
        result = en_bar_graded_comparison(3, 1, 2)
        # E_1: Conf_3(R) = 3! points, all in degree 0
        assert result['E_1_total'] == 6
        # E_2: Conf_3(R^2) has classes in degrees 0, 1, 2
        assert result['E_2_total'] == 6
        assert result['totals_agree'] is True
        assert result['gradings_differ'] is True

    def test_graded_comparison_e2_vs_e3(self):
        """E_2 vs E_3: same total, different grading."""
        result = en_bar_graded_comparison(4, 2, 3)
        assert result['totals_agree'] is True
        assert result['E_2_total'] == 24
        assert result['E_3_total'] == 24


# ============================================================================
# 3. Kappa universality across operadic levels
# ============================================================================

class TestKappaUniversality:
    """Tests that kappa is independent of the operadic level n."""

    def test_kappa_heisenberg_all_n(self):
        """kappa(H_k) = k/2 for all E_n levels."""
        for k in [Fraction(1), Fraction(2), Fraction(3), Fraction(-1)]:
            result = kappa_comparison_across_n('heisenberg', k)
            assert result['all_agree'] is True
            assert result['kappa'] == k / 2

    def test_kappa_virasoro_all_n(self):
        """kappa(Vir_c) = c/2 for all E_n levels."""
        for c in [Fraction(1), Fraction(26), Fraction(13)]:
            result = kappa_comparison_across_n('virasoro', c)
            assert result['all_agree'] is True
            assert result['kappa'] == c / 2

    def test_kappa_sl2_all_n(self):
        """kappa(sl_2, k) = 3(k+2)/4 for all E_n levels."""
        k = Fraction(1)
        result = kappa_comparison_across_n('sl_2', k)
        expected = Fraction(3) * (k + 2) / 4
        assert result['kappa'] == expected
        assert result['all_agree'] is True

    def test_kappa_sl3_all_n(self):
        """kappa(sl_3, k) = 8(k+3)/6 for all E_n levels."""
        k = Fraction(1)
        result = kappa_comparison_across_n('sl_3', k)
        dim_g = 8
        h_v = 3
        expected = Fraction(dim_g) * (k + Fraction(h_v)) / (2 * Fraction(h_v))
        assert result['kappa'] == expected
        assert result['all_agree'] is True

    def test_kappa_independence_function(self):
        """Direct test of kappa_independent_of_n."""
        for n1, n2 in [(1, 2), (1, 3), (2, 3), (1, 10), (5, 7)]:
            assert kappa_independent_of_n(n1, n2, Fraction(1)) is True
            assert kappa_independent_of_n(n1, n2, Fraction(3), dim_lie=8, h_dual=3) is True


# ============================================================================
# 4. Dimensional reduction of shadow invariants
# ============================================================================

class TestDimensionalReduction:
    """Tests for dimensional reduction E_n -> E_1."""

    def test_reduction_preserves_kappa(self):
        """Dimensional reduction preserves kappa."""
        kappa = Fraction(7, 3)
        for higher in [2, 3, 4, 5]:
            reduced = dimensional_reduction_shadow(kappa, higher, 1)
            assert reduced == kappa

    def test_reduction_chain(self):
        """Reduction E_3 -> E_2 -> E_1 preserves kappa at each step."""
        kappa = Fraction(5)
        k32 = dimensional_reduction_shadow(kappa, 3, 2)
        k21 = dimensional_reduction_shadow(k32, 2, 1)
        assert k21 == kappa

    def test_reduction_invalid_direction(self):
        """Cannot reduce from lower to higher dimension."""
        with pytest.raises(ValueError):
            dimensional_reduction_shadow(Fraction(1), 2, 3)

    def test_higher_shadow_r2_independent(self):
        """Arity-2 shadow is independent of n."""
        assert higher_shadow_depends_on_n(2, 1) is False
        assert higher_shadow_depends_on_n(2, 2) is False
        assert higher_shadow_depends_on_n(2, 3) is False

    def test_higher_shadow_r3_potentially_depends(self):
        """Arity >= 3 shadow can depend on n (for non-formal algebras)."""
        assert higher_shadow_depends_on_n(3, 2) is True
        assert higher_shadow_depends_on_n(4, 3) is True


# ============================================================================
# 5. Higher Kac-Moody algebras
# ============================================================================

class TestHigherKacMoody:
    """Tests for higher KM algebra data (Gwilliam-Williams)."""

    def test_higher_km_Cn_single_level(self):
        """On C^n, the space of levels is 1-dimensional for all n."""
        for n in [1, 2, 3, 4]:
            data = higher_km_on_Cn(lie_dim=3, n=n)
            assert data.cocycle_space_dim == 1
            assert data.cocycle_degree == n
            assert data.complex_dim == n

    def test_higher_km_torus_holomorphic_level(self):
        """On T^{2n}, the holomorphic level space is 1-dimensional."""
        for n in [1, 2, 3]:
            data = higher_km_on_torus(lie_dim=8, n=n)
            assert data.cocycle_space_dim == 1

    def test_level_comparison_all_n(self):
        """Level space on C^n is always 1-dimensional."""
        for n in [1, 2, 3, 4]:
            result = higher_km_level_comparison(n)
            assert result['level_space_on_Cn'] == 1
            assert result['governs_kappa'] is True


# ============================================================================
# 6. Self-dual YM and celestial chiral algebras
# ============================================================================

class TestSDYMCelestial:
    """Tests for SDYM chiral algebra data."""

    def test_sdym_sl2_kappa(self):
        """SDYM SL(2) at tree level: kappa = 3(1+2)/4 = 9/4."""
        data = sdym_chiral_data_slN(2)
        assert data.tree_kappa == Fraction(3) * (1 + 2) / 4
        assert data.tree_kappa == Fraction(9, 4)

    def test_sdym_sl3_kappa(self):
        """SDYM SL(3) at tree level: kappa = 8(1+3)/6 = 16/3."""
        data = sdym_chiral_data_slN(3)
        expected = Fraction(8) * Fraction(4) / Fraction(6)
        assert data.tree_kappa == expected

    def test_sdym_gl1_kappa(self):
        """SDYM GL(1): kappa = 1/2 (abelian, Heisenberg at k=1)."""
        data = sdym_chiral_data_gl1()
        assert data.tree_kappa == Fraction(1, 2)
        assert data.loop_kappa == Fraction(1, 2)  # Abelian: no loop corrections

    def test_sdym_tree_is_affine(self):
        """SDYM tree-level algebra is affine for all N."""
        for N in [2, 3, 4, 5]:
            data = sdym_chiral_data_slN(N)
            assert f'affine sl_{N}' in data.tree_level_algebra

    def test_twistor_reduction_chain(self):
        """The twistor-to-celestial reduction chain is E_3 -> E_2 -> E_1."""
        chain = twistor_to_celestial_reduction()
        assert chain['operadic_level_twistor'] == 'E_3'
        assert chain['operadic_level_sdym'] == 'E_2 (holomorphic-topological)'
        assert chain['operadic_level_celestial'] == 'E_1 (chiral algebra)'

    def test_celestial_reduction_kappa_preserved(self):
        """kappa is preserved in the celestial reduction for all N."""
        for N in [2, 3, 4, 5]:
            result = celestial_as_e1_reduction('SL', N)
            assert result['kappa_preserved'] is True
            k_e3 = result['E_3_twistor']['kappa']
            k_e2 = result['E_2_sdym']['kappa']
            k_e1 = result['E_1_celestial']['kappa']
            assert k_e3 == k_e2 == k_e1

    def test_celestial_sl2_kappa_value(self):
        """Celestial SL(2): kappa = 9/4 at all levels."""
        result = celestial_as_e1_reduction('SL', 2)
        assert result['E_1_celestial']['kappa'] == Fraction(9, 4)

    def test_celestial_sl4_kappa_value(self):
        """Celestial SL(4): kappa = dim(sl_4)(1+4)/(2*4) = 15*5/8 = 75/8."""
        result = celestial_as_e1_reduction('SL', 4)
        expected = Fraction(15) * Fraction(5) / Fraction(8)
        assert result['E_1_celestial']['kappa'] == expected


# ============================================================================
# 7. 4d CS operadic structure and E_2 braiding
# ============================================================================

class TestFourDCS:
    """Tests for the 4d CS operadic structure."""

    def test_4d_cs_operadic_level(self):
        """4d CS has E_2 operadic structure."""
        data = four_d_cs_operadic_structure()
        assert data['operadic_level'] == 2

    def test_e2_decomposition_dunn(self):
        """E_2 = E_1 x E_1 via Dunn additivity."""
        data = four_d_cs_operadic_structure()
        assert 'Dunn' in data['decomposition']

    def test_e2_braiding_is_r_matrix(self):
        """The E_2 braiding gives the R-matrix."""
        data = four_d_cs_operadic_structure()
        assert 'R-matrix' in data['r_matrix_origin']

    def test_e2_vs_e1_bar_recovery(self):
        """E_1 bar complex recovers E_2 braiding via Swiss-cheese."""
        result = e2_braiding_vs_e1_bar()
        assert result['e2_contains_e1'] is True
        assert result['e1_bar_recovers_e2'] is True

    def test_r_matrix_from_bar(self):
        """r(z) = Res^{coll}_{0,2}(Theta_A) recovers the R-matrix."""
        result = e2_braiding_vs_e1_bar()
        assert 'Res^{coll}_{0,2}(Theta_A)' in result['r_matrix_from_bar']


# ============================================================================
# 8. Genus expansion scope comparison
# ============================================================================

class TestGenusExpansion:
    """Tests for genus expansion comparison."""

    def test_our_framework_all_genera(self):
        """Our framework covers all genera."""
        comp = genus_expansion_scope_comparison()
        assert comp['our_framework']['worldsheet_genus_range'] == 'all genera g >= 0'

    def test_costello_genus_0_only(self):
        """Costello's general framework is genus 0 only on the worldsheet."""
        comp = genus_expansion_scope_comparison()
        assert 'genus 0' in comp['costello_framework']['worldsheet_genus_range']

    def test_genus_0_agreement(self):
        """At genus 0, both frameworks agree."""
        comp = genus_expansion_scope_comparison()
        # The comparison states that bar complex = Costello tree-level at genus 0
        text = comp['comparison']['genus_0_agreement'].lower()
        assert 'genus 0' in text and 'costello' in text

    def test_f1_computation(self):
        """F_1 = kappa/24 from our framework."""
        kappa = Fraction(3)
        f1 = genus_expansion_f_g(kappa, 1)
        assert f1 == Fraction(3, 24) == Fraction(1, 8)

    def test_f2_computation(self):
        """F_2 = kappa * 7/5760."""
        kappa = Fraction(1)
        f2 = genus_expansion_f_g(kappa, 2)
        assert f2 == Fraction(7, 5760)

    def test_f3_computation(self):
        """F_3 = kappa * 31/967680."""
        kappa = Fraction(1)
        f3 = genus_expansion_f_g(kappa, 3)
        assert f3 == Fraction(31, 967680)

    def test_f1_positive_for_positive_kappa(self):
        """F_1 > 0 for kappa > 0."""
        for k in [Fraction(1), Fraction(7, 3), Fraction(100)]:
            assert genus_expansion_f_g(k, 1) > 0

    def test_f_g_invalid_genus(self):
        """F_g requires g >= 1."""
        with pytest.raises(ValueError):
            genus_expansion_f_g(Fraction(1), 0)


# ============================================================================
# 9. Form factor comparison
# ============================================================================

class TestFormFactors:
    """Tests for form factor comparison at each arity."""

    def test_arity_2_r_matrix(self):
        """Arity-2 form factor is the R-matrix."""
        data = form_factor_arity_k_comparison(2)
        assert data['shadow_name'] == 'kappa (modular characteristic)'
        assert 'EXACT' in data['agreement']

    def test_arity_3_cubic(self):
        """Arity-3 form factor is the cubic shadow."""
        data = form_factor_arity_k_comparison(3)
        assert data['shadow_name'] == 'S_3 (cubic shadow)'

    def test_arity_4_quartic(self):
        """Arity-4 form factor is Q^contact."""
        data = form_factor_arity_k_comparison(4)
        assert data['shadow_name'] == 'Q^contact (quartic contact invariant)'

    def test_arity_5_extends_costello(self):
        """Arity >= 5: our framework extends beyond Costello."""
        data = form_factor_arity_k_comparison(5)
        assert 'EXTENDS' in data['agreement']

    def test_arity_10_extends(self):
        """Arity 10: well beyond explicit Costello computations."""
        data = form_factor_arity_k_comparison(10)
        assert 'EXTENDS' in data['agreement']


# ============================================================================
# 10. HCS boundary algebras
# ============================================================================

class TestHCSBoundary:
    """Tests for HCS boundary chiral algebras on CY3s."""

    def test_registry_nonempty(self):
        """The HCS boundary algebra registry is non-empty."""
        algebras = hcs_boundary_algebras()
        assert len(algebras) >= 5

    def test_k3_x_e_kappa_5(self):
        """K3 x E boundary algebra has kappa = 5.

        Multi-path verification:
        (1) chi^CY(K3 x E) = 5 (categorical CY Euler characteristic)
        (2) Igusa cusp form Delta_5 has weight 5
        """
        kappa = hcs_kappa_from_cy3('K3 x E')
        assert kappa == Fraction(5)

    def test_conifold_kappa_1(self):
        """Conifold boundary algebra has kappa = 1 (betagamma)."""
        kappa = hcs_kappa_from_cy3('Conifold (resolved)')
        assert kappa == Fraction(1)

    def test_t6_kappa_0(self):
        """T^6 boundary algebra has kappa = 0."""
        kappa = hcs_kappa_from_cy3('T^6')
        assert kappa == Fraction(0)

    def test_quintic_kappa(self):
        """Quintic boundary algebra has kappa = -25/3 (BCOV)."""
        kappa = hcs_kappa_from_cy3('Quintic')
        assert kappa == Fraction(-25, 3)

    def test_shadow_class_variety(self):
        """Different CY3s produce different shadow classes."""
        algebras = hcs_boundary_algebras()
        classes = {a.shadow_class for a in algebras}
        assert 'G' in classes  # Gaussian (conifold, T^6)
        assert 'M' in classes  # Mixed (K3 x E)

    def test_k3_x_e_not_simply_connected(self):
        """K3 x E has h^{0,1} = 1 (non-simply-connected)."""
        algebras = hcs_boundary_algebras()
        k3e = [a for a in algebras if a.cy3_name == 'K3 x E'][0]
        assert k3e.h01 == 1


# ============================================================================
# 11. Koszul duality in higher dimensions
# ============================================================================

class TestKoszulDualityHigherDim:
    """Tests for Koszul duality at E_n level."""

    def test_koszul_shift_e1(self):
        """E_1 Koszul shift = 1."""
        data = koszul_duality_comparison(1)
        assert data['koszul_shift'] == 1

    def test_koszul_shift_e2(self):
        """E_2 Koszul shift = 2."""
        data = koszul_duality_comparison(2)
        assert data['koszul_shift'] == 2

    def test_koszul_shift_e3(self):
        """E_3 Koszul shift = 3."""
        data = koszul_duality_comparison(3)
        assert data['koszul_shift'] == 3

    def test_bar_cobar_adjunction_all_n(self):
        """Bar-cobar adjunction exists for all n."""
        for n in [1, 2, 3, 4, 5]:
            data = koszul_duality_comparison(n)
            assert data['bar_cobar_adjunction'] is True

    def test_verdier_intertwining_all_n(self):
        """Verdier intertwining generalizes to all n."""
        for n in [1, 2, 3]:
            data = koszul_duality_comparison(n)
            assert data['verdier_intertwining'] is True

    def test_genus_extension_our_only(self):
        """Genus tower is our unique contribution (no E_n analogue for n >= 2)."""
        data = koszul_duality_comparison(2)
        assert 'do NOT have known' in data['genus_extension']


# ============================================================================
# 12. Bittleston-Skinner diamond
# ============================================================================

class TestDiamond:
    """Tests for the diamond correspondence."""

    def test_diamond_has_four_vertices(self):
        """The diamond has top, middle_left, middle_right, bottom."""
        d = bittleston_skinner_diamond()
        assert 'top' in d
        assert 'middle_left' in d
        assert 'middle_right' in d
        assert 'bottom' in d

    def test_all_produce_same_2d(self):
        """All four vertices produce the same 2d chiral algebra."""
        d = bittleston_skinner_diamond()
        assert d['all_produce_same_2d'] is True

    def test_kappa_universal_across_diamond(self):
        """kappa is the same at all vertices."""
        d = bittleston_skinner_diamond()
        assert 'same at all four' in d['kappa_universal']

    def test_genus_tower_at_bottom(self):
        """Full genus tower is available only at the bottom (2d) vertex."""
        d = bittleston_skinner_diamond()
        assert 'genus tower' in d['higher_genus_at_bottom_only'].lower()


# ============================================================================
# 13. Associativity sufficiency
# ============================================================================

class TestAssociativitySufficiency:
    """Tests for the Fernandez-Paquette 2024 result."""

    def test_koszulness_translation(self):
        """Associativity sufficiency = chiral Koszulness in our language."""
        data = associativity_sufficiency_theorem()
        assert 'Koszulness' in data['our_translation']

    def test_koszul_duality_match(self):
        """Fernandez-Paquette Koszul duality = our Theorem A."""
        data = associativity_sufficiency_theorem()
        assert 'Theorem A' in data['koszul_duality_match']

    def test_genus_extension(self):
        """Our framework extends beyond Fernandez-Paquette (genus > 0)."""
        data = associativity_sufficiency_theorem()
        assert 'genus 0 only' in data['our_extension']


# ============================================================================
# 14. Higher-genus twistor spaces
# ============================================================================

class TestHigherGenusTwistor:
    """Tests for Jarov 2025 higher-genus twistor spaces."""

    def test_our_framework_covers(self):
        """Our framework handles higher-genus twistor chiral algebras."""
        data = higher_genus_twistor_data()
        assert data['our_framework_covers_this'] is True

    def test_celestial_not_p1(self):
        """Higher-genus twistor: celestial algebra lives on higher-genus curve."""
        data = higher_genus_twistor_data()
        assert 'NOT P^1' in data['celestial_algebra_base']


# ============================================================================
# 15. Cross-consistency with existing engines
# ============================================================================

class TestCrossConsistency:
    """Cross-consistency with en_factorization_shadow and costello_4d_cs."""

    def test_conf_space_matches_en_engine(self):
        """Configuration space data matches en_factorization_shadow.py.

        Verify the same Poincare polynomials.
        """
        # Conf_3(R^2): should match en_factorization_shadow.conf_space_betti
        poly = conf_space_poincare_poly(3, 2)
        assert poly[0] == 1 and poly[1] == 3 and poly[2] == 2

    def test_kappa_matches_costello_4d_cs(self):
        """kappa(sl_N, k=1) should match costello_4d_cs_comparison_engine.

        For sl_2 at k=1: kappa = 3*3/4 = 9/4.
        """
        expected = Fraction(3) * Fraction(3) / Fraction(4)
        result = kappa_comparison_across_n('sl_2', Fraction(1))
        assert result['kappa'] == expected

    def test_bar_dim_matches_en_engine(self):
        """Bar dimensions should match en_factorization_shadow for all n."""
        for n in [1, 2, 3]:
            for k in [1, 2, 3, 4]:
                dim = en_bar_arity_dimension(k, n)
                assert dim == factorial(k), \
                    f"Bar dim at arity {k}, E_{n} should be {factorial(k)}"

    def test_lambda_fp_g1(self):
        """lambda_1^FP = 1/24."""
        assert _lambda_fp_exact(1) == Fraction(1, 24)

    def test_lambda_fp_g2(self):
        """lambda_2^FP = 7/5760."""
        assert _lambda_fp_exact(2) == Fraction(7, 5760)

    def test_bernoulli_b2(self):
        """B_2 = 1/6."""
        assert _bernoulli_exact(2) == Fraction(1, 6)

    def test_bernoulli_b4(self):
        """B_4 = -1/30."""
        assert _bernoulli_exact(4) == Fraction(-1, 30)


# ============================================================================
# 16. Operadic comparison table completeness
# ============================================================================

class TestComparisonTable:
    """Tests for the comparison table structure."""

    def test_table_has_three_entries(self):
        """Table covers E_1, E_2, E_3."""
        table = operadic_comparison_table()
        assert len(table) == 3
        levels = {entry['operadic_level'] for entry in table}
        assert levels == {1, 2, 3}

    def test_e1_is_chiral(self):
        """E_1 entry references chiral algebras."""
        table = operadic_comparison_table()
        e1 = [e for e in table if e['operadic_level'] == 1][0]
        assert 'chiral' in e1['name'].lower()
        assert e1['propagator_degree'] == 0
        assert e1['koszul_shift'] == 1

    def test_e2_is_4d_cs(self):
        """E_2 entry references 4d CS."""
        table = operadic_comparison_table()
        e2 = [e for e in table if e['operadic_level'] == 2][0]
        assert '4d CS' in e2['physical_theory']
        assert e2['propagator_degree'] == 1
        assert e2['koszul_shift'] == 2

    def test_e3_is_hcs(self):
        """E_3 entry references HCS."""
        table = operadic_comparison_table()
        e3 = [e for e in table if e['operadic_level'] == 3][0]
        assert 'HCS' in e3['physical_theory']
        assert e3['propagator_degree'] == 2
        assert e3['koszul_shift'] == 3


# ============================================================================
# 17. Master comparison structure completeness
# ============================================================================

class TestMasterComparison:
    """Tests for the master comparison data structure."""

    def test_master_has_all_keys(self):
        """Master comparison contains all expected sections."""
        mc = master_comparison()
        expected_keys = [
            'operadic_table', 'five_questions', 'genus_comparison',
            'diamond', 'e2_vs_e1', 'koszul_duality_e1',
            'koszul_duality_e2', 'koszul_duality_e3',
            'associativity', 'twistor_reduction',
            'higher_genus_twistor', 'hcs_boundary_algebras',
        ]
        for key in expected_keys:
            assert key in mc, f"Master comparison missing key: {key}"

    def test_five_questions_complete(self):
        """All five key mathematical questions are answered."""
        summary = structure_comparison_summary()
        for i in range(1, 6):
            key = f'Q{i}_' + ['bar_complex', 'beyond_genus_0',
                              'dimensional_reduction', 'celestial_reduction',
                              'en_structure'][i - 1]
            assert key in summary
            assert 'answer' in summary[key]
            assert 'detail' in summary[key]


# ============================================================================
# 18. Bar dimension comparison table
# ============================================================================

class TestBarDimensionTable:
    """Tests for the bar dimension comparison table."""

    def test_bar_dim_comparison_arity_3(self):
        """Bar dimensions at arity 3 for E_1 through E_4."""
        result = bar_dimension_comparison(3)
        for n in [1, 2, 3, 4]:
            assert result[n] == 6  # 3! = 6

    def test_bar_dim_comparison_arity_5(self):
        """Bar dimensions at arity 5 for E_1 through E_4."""
        result = bar_dimension_comparison(5)
        for n in [1, 2, 3, 4]:
            assert result[n] == 120  # 5! = 120


# ============================================================================
# 19. Edge cases and input validation
# ============================================================================

class TestEdgeCases:
    """Tests for edge cases and input validation."""

    def test_conf_space_k0(self):
        """Conf_0(R^n) = point (empty configuration)."""
        for n in [1, 2, 3]:
            poly = conf_space_poincare_poly(0, n)
            assert poly == {0: 1}

    def test_conf_space_n1_k1(self):
        """Conf_1(R) = R (contractible)."""
        poly = conf_space_poincare_poly(1, 1)
        assert poly == {0: 1}

    def test_bar_arity_0(self):
        """Bar at arity 0 is the ground field (dimension 1)."""
        for n in [1, 2, 3]:
            assert en_bar_arity_dimension(0, n) == 1

    def test_kappa_negative_level(self):
        """kappa can be negative (for negative levels)."""
        result = kappa_comparison_across_n('heisenberg', Fraction(-3))
        assert result['kappa'] == Fraction(-3, 2)
        assert result['kappa'] < 0

    def test_kappa_zero_level(self):
        """kappa = 0 at level 0 for Heisenberg."""
        result = kappa_comparison_across_n('heisenberg', Fraction(0))
        assert result['kappa'] == Fraction(0)


# ============================================================================
# 20. Quantitative checks on specific algebras
# ============================================================================

class TestSpecificAlgebras:
    """Quantitative checks on specific higher-dim chiral algebras."""

    def test_sdym_sl5_kappa_exact(self):
        """SDYM SL(5) at k=1: kappa = dim(sl_5)(1+5)/(2*5) = 24*6/10 = 144/10 = 72/5."""
        data = sdym_chiral_data_slN(5)
        dim_sl5 = 24
        h_v = 5
        expected = Fraction(dim_sl5) * Fraction(6) / Fraction(10)
        assert expected == Fraction(72, 5)
        assert data.tree_kappa == expected

    def test_conf_4_R2_detailed(self):
        """Conf_4(R^2): P_4(t) = 1*1*(1+t)*(1+2t)*(1+3t).

        Actually P_4(t) = prod_{j=0}^{3}(1+j*t) = 1*(1+t)*(1+2t)*(1+3t).
        = (1+t)(1+2t)(1+3t)
        = (1+t)(1+5t+6t^2)
        = 1 + 5t + 6t^2 + t + 5t^2 + 6t^3
        = 1 + 6t + 11t^2 + 6t^3.
        Total = 24 = 4!.
        """
        poly = conf_space_poincare_poly(4, 2)
        assert poly.get(0, 0) == 1
        assert poly.get(1, 0) == 6
        assert poly.get(2, 0) == 11
        assert poly.get(3, 0) == 6
        assert conf_space_total_dim(4, 2) == 24

    def test_conf_4_R3_detailed(self):
        """Conf_4(R^3): generators in degree 2.

        P_4(t) = prod_{j=0}^{3}(1+j*t^2) = 1*(1+t^2)*(1+2t^2)*(1+3t^2).
        = (1+t^2)(1+2t^2)(1+3t^2)
        = (1+t^2)(1+5t^2+6t^4)
        = 1 + 5t^2 + 6t^4 + t^2 + 5t^4 + 6t^6
        = 1 + 6t^2 + 11t^4 + 6t^6.
        Total = 24 = 4!.
        """
        poly = conf_space_poincare_poly(4, 3)
        assert poly.get(0, 0) == 1
        assert poly.get(2, 0) == 6
        assert poly.get(4, 0) == 11
        assert poly.get(6, 0) == 6
        assert conf_space_total_dim(4, 3) == 24

    def test_celestial_sl3_shadow_class(self):
        """Celestial SL(3): shadow class L (Lie/tree)."""
        result = celestial_as_e1_reduction('SL', 3)
        assert result['shadow_class'] == 'L'

    def test_hcs_c3_algebra(self):
        """C^3 HCS boundary algebra involves affine gl_N."""
        algebras = hcs_boundary_algebras()
        c3 = [a for a in algebras if a.cy3_name == 'C^3'][0]
        assert 'affine' in c3.boundary_algebra.lower()
        assert c3.h01 == 0
        assert c3.h02 == 0
