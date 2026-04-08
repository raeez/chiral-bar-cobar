r"""Tests for SC^{ch,top} homotopy-Koszulity verification engine.

Verifies Theorem thm:homotopy-Koszul (Vol II):
  SC^{ch,top} is homotopy-Koszul, i.e. Omega(B(SC^{ch,top})) -> SC^{ch,top}
  is a quasi-isomorphism of two-colored dg operads.

Three independent verification paths:
  Path 1: Transfer from classical SC (Kontsevich formality + Livernet/Vallette)
  Path 2: Associated graded decomposition (Francis-Gaitsgory + spectral sequence)
  Path 3: Euler characteristic consistency at each arity

Multi-path verification per CLAUDE.md mandate.

References:
  Vol II: thm:homotopy-Koszul, thm:bar-cobar-adjunction, prop:gr-chiral
  Ginzburg-Kapranov (1994), Voronov (1999), Kontsevich (2003),
  Livernet (2006), Vallette (2007), Loday-Vallette (2012)
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from math import factorial, comb

from lib.sc_homotopy_koszul_engine import (
    # AOS algebra
    aos_betti_numbers,
    aos_euler_characteristic,
    aos_top_betti,
    aos_total_betti,
    # Koszul dual
    sc_koszul_dual_dimensions,
    # Bar complex of classical SC
    bar_complex_sc_classical_arity,
    # Kontsevich formality
    kontsevich_formality_dimensions,
    transfer_square_verification,
    # Bar-cobar resolution
    bar_cobar_resolution_arity,
    # Explicit bar differential
    bar_differential_arity2,
    bar_differential_arity3,
    bar_differential_arity4,
    # Euler characteristics
    bar_euler_characteristic_com,
    bar_euler_characteristic_ass,
    bar_euler_characteristic_sc,
    # Consequences
    quillen_equivalence_consequences,
    # Associated graded
    associated_graded_decomposition,
    # Full verification
    homotopy_koszulity_full_verification,
    # Reference audit
    livernet_reference_audit,
    # Bar complex dimensions
    bar_complex_dims_com,
    verify_bar_euler_formula,
)


# ===================================================================
# 1. AOS ALGEBRA: Betti numbers of FM_n(C)
# ===================================================================

class TestAOSBettiNumbers:
    """Betti numbers via the Poincare polynomial P_n(t) = prod(1 + jt)."""

    def test_fm1(self):
        assert aos_betti_numbers(1) == [1]

    def test_fm2(self):
        assert aos_betti_numbers(2) == [1, 1]

    def test_fm3(self):
        assert aos_betti_numbers(3) == [1, 3, 2]

    def test_fm4(self):
        assert aos_betti_numbers(4) == [1, 6, 11, 6]

    def test_fm5(self):
        assert aos_betti_numbers(5) == [1, 10, 35, 50, 24]

    def test_fm6(self):
        b = aos_betti_numbers(6)
        assert b == [1, 15, 85, 225, 274, 120]

    def test_total_betti_is_factorial(self):
        """sum b_q(FM_n) = n! for n = 1..8."""
        for n in range(1, 9):
            assert aos_total_betti(n) == factorial(n), f"Failed at n={n}"

    def test_top_betti_is_lie_dim(self):
        """b_{n-1}(FM_n) = (n-1)! = dim Lie(n) for n = 1..8."""
        for n in range(1, 9):
            assert aos_top_betti(n) == factorial(n - 1), f"Failed at n={n}"

    def test_euler_vanishes_for_n_geq_2(self):
        """chi(FM_n) = P_n(-1) = 0 for n >= 2."""
        for n in range(2, 9):
            assert aos_euler_characteristic(n) == 0, f"Failed at n={n}"

    def test_euler_fm1(self):
        """chi(FM_1) = 1 (a point)."""
        assert aos_euler_characteristic(1) == 1

    def test_h1_equals_generators(self):
        """b_1(FM_n) = C(n,2) (number of Arnold generators)."""
        for n in range(2, 8):
            b = aos_betti_numbers(n)
            assert b[1] == comb(n, 2), f"Failed at n={n}"


# ===================================================================
# 2. KOSZUL DUAL OF CLASSICAL SC
# ===================================================================

class TestSCKoszulDual:
    """Koszul dual dimensions: Com^! = Lie, Ass^! = Ass."""

    def test_closed_color_is_lie(self):
        """Closed-color Koszul dual: dim = (n-1)!."""
        dims = sc_koszul_dual_dimensions(6)
        for n in range(1, 7):
            assert dims['closed'][n] == factorial(n - 1), f"Failed at n={n}"

    def test_open_color_is_ass(self):
        """Open-color Koszul dual: dim = 1 (non-Sigma)."""
        dims = sc_koszul_dual_dimensions(6)
        for n in range(1, 7):
            assert dims['open'][n] == 1

    def test_mixed_factorizes(self):
        """Mixed Koszul dual at (k,m): dim = (k-1)!."""
        dims = sc_koszul_dual_dimensions(5)
        for k in range(1, 5):
            for m in range(0, 5 - k):
                assert dims['mixed'][(k, m)] == factorial(k - 1)


# ===================================================================
# 3. BAR COMPLEX OF CLASSICAL SC
# ===================================================================

class TestBarComplexClassical:
    """Bar complex concentration for the classical SC (Koszul => concentrated)."""

    def test_closed_arity2(self):
        data = bar_complex_sc_classical_arity(2, 'closed')
        assert data['koszul_dual_dim'] == 1
        assert data['concentration_degree'] == 1
        assert data['is_concentrated']

    def test_closed_arity3(self):
        data = bar_complex_sc_classical_arity(3, 'closed')
        assert data['koszul_dual_dim'] == 2
        assert data['concentration_degree'] == 2
        assert data['is_concentrated']

    def test_closed_arity4(self):
        data = bar_complex_sc_classical_arity(4, 'closed')
        assert data['koszul_dual_dim'] == 6
        assert data['concentration_degree'] == 3
        assert data['is_concentrated']

    def test_closed_arity5(self):
        data = bar_complex_sc_classical_arity(5, 'closed')
        assert data['koszul_dual_dim'] == 24
        assert data['concentration_degree'] == 4

    def test_open_arity2(self):
        data = bar_complex_sc_classical_arity(2, 'open')
        assert data['koszul_dual_dim'] == 1
        assert data['concentration_degree'] == 1
        assert data['is_concentrated']

    def test_open_arity3(self):
        data = bar_complex_sc_classical_arity(3, 'open')
        assert data['koszul_dual_dim'] == 1

    def test_open_arity_k(self):
        """Open color: Ass^! has dim 1 at each arity."""
        for n in range(2, 8):
            data = bar_complex_sc_classical_arity(n, 'open')
            assert data['koszul_dual_dim'] == 1


# ===================================================================
# 4. KONTSEVICH FORMALITY (Step 2 of proof)
# ===================================================================

class TestKontsevichFormality:
    """Formality: H*(FM_k(C)) gives correct Betti numbers."""

    def test_total_equals_factorial(self):
        results = kontsevich_formality_dimensions(6)
        for k in range(1, 7):
            assert results[k]['total_equals_factorial']

    def test_top_betti_equals_lie_dim(self):
        results = kontsevich_formality_dimensions(6)
        for k in range(1, 7):
            assert results[k]['top_betti_equals_lie_dim']

    def test_euler_zero(self):
        results = kontsevich_formality_dimensions(6)
        for k in range(2, 7):
            assert results[k]['euler_zero']

    def test_kunneth_trivial_open(self):
        """E_1(m) is contractible, so Kunneth gives H*(FM) x k = H*(FM)."""
        results = kontsevich_formality_dimensions(6)
        for k in range(1, 7):
            assert results[k]['kunneth_trivial_open']


# ===================================================================
# 5. TRANSFER SQUARE (Step 3 of proof)
# ===================================================================

class TestTransferSquare:
    """Two-out-of-three argument for the commutative square."""

    def test_phi_is_qi(self):
        results = transfer_square_verification(6)
        for n in range(2, 7):
            assert results[n]['phi_is_qi']

    def test_lie_dim_correct(self):
        results = transfer_square_verification(6)
        for n in range(2, 7):
            assert results[n]['lie_dim_equals_n_minus_1_factorial']

    def test_two_out_of_three(self):
        results = transfer_square_verification(6)
        for n in range(2, 7):
            assert results[n]['two_out_of_three_applicable']


# ===================================================================
# 6. BAR-COBAR RESOLUTION AT SMALL ARITIES
# ===================================================================

class TestBarCobarResolution:
    """Bar-cobar resolution Omega(P^!) -> P at each arity."""

    def test_arity2(self):
        data = bar_cobar_resolution_arity(2)
        assert data['lie_dim'] == 1
        assert data['com_dim'] == 1
        assert data['bar_cohomology_closed_concentrated']

    def test_arity3(self):
        data = bar_cobar_resolution_arity(3)
        assert data['lie_dim'] == 2
        assert data['bar_cohomology_closed_dim'] == 2
        assert data['bar_cohomology_closed_degree'] == 2

    def test_arity4(self):
        data = bar_cobar_resolution_arity(4)
        assert data['lie_dim'] == 6
        assert data['bar_cohomology_closed_dim'] == 6
        assert data['bar_cohomology_closed_degree'] == 3

    def test_arity5(self):
        data = bar_cobar_resolution_arity(5)
        assert data['lie_dim'] == 24
        assert data['bar_cohomology_closed_dim'] == 24


# ===================================================================
# 7. EXPLICIT BAR DIFFERENTIAL
# ===================================================================

class TestExplicitBarDifferential:
    """Explicit bar complex of Com at arities 2, 3, 4."""

    def test_arity2_concentrated(self):
        data = bar_differential_arity2()
        assert data['concentrated']
        assert data['bar_cohomology'] == {0: 1}
        assert data['koszul_dual_dim'] == 1

    def test_arity3_euler(self):
        data = bar_differential_arity3()
        assert data['euler_matches_lie']
        assert data['lie_3_dim'] == 2
        assert data['euler_characteristic'] == 2

    def test_arity3_bar_dims(self):
        data = bar_differential_arity3()
        assert data['bar_dims_by_weight'] == {1: 1, 2: 3}

    def test_arity4_euler(self):
        data = bar_differential_arity4()
        assert data['euler_matches_lie']
        assert data['lie_4_dim'] == 6
        assert data['euler_characteristic'] == -6
        assert data['expected_euler'] == -6

    def test_arity4_bar_dims(self):
        data = bar_differential_arity4()
        assert data['bar_dims_by_weight'] == {1: 1, 2: 10, 3: 15}


# ===================================================================
# 8. EULER CHARACTERISTIC FORMULA
# ===================================================================

class TestEulerCharacteristic:
    """chi(B(Com)(n)) = (-1)^{n-1} * (n-1)!."""

    def test_com_euler_arity2(self):
        assert bar_euler_characteristic_com(2) == -1

    def test_com_euler_arity3(self):
        assert bar_euler_characteristic_com(3) == 2

    def test_com_euler_arity4(self):
        assert bar_euler_characteristic_com(4) == -6

    def test_com_euler_arity5(self):
        assert bar_euler_characteristic_com(5) == 24

    def test_com_euler_general(self):
        for n in range(2, 9):
            expected = (-1) ** (n - 1) * factorial(n - 1)
            assert bar_euler_characteristic_com(n) == expected, f"Failed at n={n}"

    def test_ass_euler(self):
        for n in range(2, 9):
            assert bar_euler_characteristic_ass(n) == (-1) ** (n - 1)

    def test_sc_combined(self):
        for n in range(2, 7):
            ec = bar_euler_characteristic_sc(n)
            assert ec['closed'] == (-1) ** (n - 1) * factorial(n - 1)
            assert ec['open'] == (-1) ** (n - 1)
            assert ec['closed_abs'] == factorial(n - 1)
            assert ec['open_abs'] == 1


# ===================================================================
# 9. CONSEQUENCES FOR ALGEBRAS
# ===================================================================

class TestQuillenEquivalenceConsequences:
    """Consequences of homotopy-Koszulity for specific algebra types."""

    def test_heisenberg_class_g(self):
        data = quillen_equivalence_consequences('heisenberg')
        assert data['quillen_equivalence']
        assert data['unit_is_qi']
        assert data['shadow_class'] == 'G'
        assert data['shadow_depth'] == 2
        assert data['bar_diff_trivial']
        assert data['bar_cobar_terminates']

    def test_affine_km_class_l(self):
        data = quillen_equivalence_consequences('affine_km')
        assert data['quillen_equivalence']
        assert data['shadow_class'] == 'L'
        assert data['shadow_depth'] == 3
        assert not data['bar_diff_trivial']
        assert data['bar_cobar_terminates']

    def test_virasoro_class_m(self):
        data = quillen_equivalence_consequences('virasoro')
        assert data['quillen_equivalence']
        assert data['shadow_class'] == 'M'
        assert data['shadow_depth'] == 'infinity'
        assert not data['bar_diff_trivial']
        assert not data['bar_cobar_terminates']

    def test_beta_gamma_class_c(self):
        data = quillen_equivalence_consequences('beta_gamma')
        assert data['quillen_equivalence']
        assert data['shadow_class'] == 'C'
        assert data['shadow_depth'] == 4
        assert data['bar_cobar_terminates']


# ===================================================================
# 10. ASSOCIATED GRADED (prop:gr-chiral)
# ===================================================================

class TestAssociatedGraded:
    """gr SC^{ch,top} = P_ch amalg E_1."""

    def test_p_ch_is_lie_dim(self):
        results = associated_graded_decomposition(6)
        for n in range(2, 7):
            assert results[n]['p_ch_dim'] == factorial(n - 1)

    def test_both_factors_koszul(self):
        results = associated_graded_decomposition(6)
        for n in range(2, 7):
            assert results[n]['francis_gaitsgory_koszul']
            assert results[n]['ass_koszul']
            assert results[n]['free_product_koszul']


# ===================================================================
# 11. FULL MULTI-PATH VERIFICATION
# ===================================================================

class TestFullVerification:
    """The complete 3-path verification of homotopy-Koszulity."""

    def test_all_paths_consistent(self):
        result = homotopy_koszulity_full_verification(6)
        assert result['all_paths_consistent']

    def test_path1_transfer(self):
        result = homotopy_koszulity_full_verification(6)
        assert result['path1_transfer']['verdict'] == 'PASS'

    def test_path2_associated_graded(self):
        result = homotopy_koszulity_full_verification(6)
        assert result['path2_associated_graded']['verdict'] == 'PASS'

    def test_path3_euler(self):
        result = homotopy_koszulity_full_verification(6)
        assert result['path3_euler_characteristics']['verdict'] == 'PASS'

    def test_conclusion(self):
        result = homotopy_koszulity_full_verification(6)
        assert 'homotopy-Koszul' in result['conclusion']
        assert 'quasi-isomorphism' in result['conclusion']


# ===================================================================
# 12. LIVERNET REFERENCE AUDIT
# ===================================================================

class TestLivernetReferenceAudit:
    """Audit: [Liv06] is indirect but the proof is still correct."""

    def test_proof_correct(self):
        audit = livernet_reference_audit()
        assert audit['proof_correct']

    def test_liv06_not_direct(self):
        audit = livernet_reference_audit()
        assert not audit['direct_sc_koszulity']

    def test_classical_sc_is_koszul(self):
        """The classical SC IS Koszul (quadratic, distributive law)."""
        audit = livernet_reference_audit()
        assert audit['classical_sc_is_koszul']
        assert audit['classical_sc_is_quadratic']

    def test_sc_chtop_not_koszul(self):
        """SC^{ch,top} is NOT Koszul (not quadratic), only homotopy-Koszul."""
        audit = livernet_reference_audit()
        assert not audit['sc_chtop_is_koszul']
        assert audit['sc_chtop_is_homotopy_koszul']
        assert not audit['sc_chtop_is_quadratic']


# ===================================================================
# 13. BAR COMPLEX DIMENSIONS AND EULER FORMULA
# ===================================================================

class TestBarComplexDimensions:
    """Explicit bar complex dimensions for B(Com)(n)."""

    def test_arity2(self):
        dims = bar_complex_dims_com(2)
        assert dims == {1: 1}

    def test_arity3(self):
        dims = bar_complex_dims_com(3)
        assert dims == {1: 1, 2: 3}

    def test_arity4(self):
        dims = bar_complex_dims_com(4)
        assert dims == {1: 1, 2: 10, 3: 15}

    def test_arity5(self):
        dims = bar_complex_dims_com(5)
        assert dims == {1: 1, 2: 25, 3: 105, 4: 105}

    def test_arity6(self):
        dims = bar_complex_dims_com(6)
        assert dims == {1: 1, 2: 56, 3: 490, 4: 1260, 5: 945}

    def test_euler_formula_all_arities(self):
        """chi(B(Com)(n)) = (-1)^{n-1} * (n-1)! for n=2..6."""
        results = verify_bar_euler_formula(6)
        for n in range(2, 7):
            assert results[n]['match'], f"Euler mismatch at n={n}: {results[n]}"

    def test_arity2_euler_detail(self):
        results = verify_bar_euler_formula(6)
        assert results[2]['euler'] == -1
        assert results[2]['expected'] == -1

    def test_arity3_euler_detail(self):
        results = verify_bar_euler_formula(6)
        assert results[3]['euler'] == 2
        assert results[3]['expected'] == 2

    def test_arity4_euler_detail(self):
        results = verify_bar_euler_formula(6)
        assert results[4]['euler'] == -6
        assert results[4]['expected'] == -6

    def test_arity5_euler_detail(self):
        results = verify_bar_euler_formula(6)
        assert results[5]['euler'] == 24
        assert results[5]['expected'] == 24

    def test_arity6_euler_detail(self):
        results = verify_bar_euler_formula(6)
        assert results[6]['euler'] == -120
        assert results[6]['expected'] == -120


# ===================================================================
# 14. CROSS-CHECKS: Koszul dual dim = top Betti number
# ===================================================================

class TestKoszulDualVsBetti:
    """The Koszul dual cooperad dimension = top Betti number of FM_n(C)."""

    def test_lie_dim_equals_top_betti(self):
        """dim Lie(n) = b_{n-1}(FM_n(C)) = (n-1)! for n=1..8."""
        for n in range(1, 9):
            betti = aos_betti_numbers(n)
            top = betti[-1]
            lie = factorial(n - 1)
            assert top == lie, f"Failed at n={n}: top={top}, lie={lie}"

    def test_bar_concentration_degree(self):
        """Bar cohomology concentrated in degree n-1."""
        for n in range(2, 7):
            data = bar_complex_sc_classical_arity(n, 'closed')
            assert data['concentration_degree'] == n - 1

    def test_ass_self_dual(self):
        """Ass^! = Ass: the associative operad is self-dual."""
        for n in range(2, 7):
            data = bar_complex_sc_classical_arity(n, 'open')
            assert data['koszul_dual_dim'] == 1  # non-Sigma


# ===================================================================
# 15. DIMENSIONAL CONSISTENCY
# ===================================================================

class TestDimensionalConsistency:
    """Cross-check: all dimensional formulas agree."""

    def test_factorial_three_ways(self):
        """n! = sum(betti) = P_n(1) = total dim H*(FM_n)."""
        for n in range(1, 8):
            b = aos_betti_numbers(n)
            assert sum(b) == factorial(n)
            assert aos_total_betti(n) == factorial(n)

    def test_lie_three_ways(self):
        """(n-1)! = top Betti = Koszul dual dim = bar_euler_abs."""
        for n in range(2, 7):
            top = aos_top_betti(n)
            kd = sc_koszul_dual_dimensions(n)['closed'][n]
            euler_abs = abs(bar_euler_characteristic_com(n))
            assert top == factorial(n - 1)
            assert kd == factorial(n - 1)
            assert euler_abs == factorial(n - 1)

    def test_bar_dims_euler_matches_formula(self):
        """Euler from explicit bar dims matches the formula."""
        for n in range(2, 7):
            dims = bar_complex_dims_com(n)
            if dims:
                euler_explicit = sum((-1) ** s * d for s, d in dims.items())
                euler_formula = bar_euler_characteristic_com(n)
                assert euler_explicit == euler_formula, (
                    f"n={n}: explicit={euler_explicit}, formula={euler_formula}"
                )
