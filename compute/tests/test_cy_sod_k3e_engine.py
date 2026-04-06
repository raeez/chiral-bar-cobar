r"""Tests for cy_sod_k3e_engine.py -- CY-21: Semiorthogonal decomposition of
D^b(K3 x E) and its relation to glued quiver CY categories.

Verification paths (multi-path mandate, >= 3 per claim):
  Path A: K-theory ranks from lattice theory (Mukai lattice)
  Path B: Euler form computation and bilinear algebra
  Path C: Autoequivalence group structure and SL(2,Z) relations
  Path D: Hodge-theoretic computation (Kunneth + HKR)
  Path E: Topological Euler characteristic (product formula)
  Path F: Serre duality / CY3 constraints (antisymmetry, no exceptionals)
  Path G: ADE quiver categories (McKay correspondence)
  Path H: Glued category K-theory comparison

120+ tests covering:
  1. K-theory ranks (K3, E, K3 x E, Mukai lattice)
  2. Euler form matrix properties (antisymmetry, rank, Kunneth)
  3. Hodge numbers and Betti numbers (Kunneth, product formula)
  4. Autoequivalence groups (SL(2,Z) relations, generators)
  5. SOD indecomposability (K3 theorem, CY3 constraints)
  6. Exceptional objects obstruction (Serre duality on CY3)
  7. Hochschild homology via HKR
  8. Phantom categories
  9. ADE singularities and quiver categories
  10. Glued category comparison (K-theory ranks, Euler forms)
  11. Lattice-theoretic invariants (signature, determinant, unimodularity)
  12. Cross-verification and multi-path consistency

CAUTION (AP10): All values independently verified by multiple methods.
CAUTION (AP38): K3 lattice conventions verified against Huybrechts (2006).
"""

import math
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np

from compute.lib import cy_sod_k3e_engine as engine


# ============================================================================
# Section 1: K-theory ranks
# ============================================================================

class TestKTheoryRanks:
    """Tests for K_0 ranks of K3, E, and K3 x E."""

    def test_mukai_lattice_rank_is_24(self):
        """Mukai lattice H-tilde(K3, Z) has rank 24."""
        assert engine.mukai_lattice_rank() == 24

    def test_k0_k3_rank_is_24(self):
        """K_0(K3) = Z^{24} via Mukai vector isomorphism."""
        assert engine.k0_k3_rank() == 24

    def test_k0_elliptic_rank_is_2(self):
        """K_0(E) = Z^2 for elliptic curve E."""
        assert engine.k0_elliptic_rank() == 2

    def test_k0_k3e_rank_is_48(self):
        """K_0(K3 x E) = Z^{48} by Kunneth."""
        assert engine.k0_k3e_rank() == 48

    def test_k0_product_formula(self):
        """K_0(K3 x E) = K_0(K3) otimes K_0(E)."""
        assert engine.k0_k3e_rank() == engine.k0_k3_rank() * engine.k0_elliptic_rank()

    def test_mukai_rank_equals_betti_sum_even(self):
        """rk K_0(K3) = sum of even Betti numbers of K3.

        b_0 + b_2 + b_4 = 1 + 22 + 1 = 24 = rk K_0(K3).
        (For a surface, K_0 has rank = sum of even Betti.)
        """
        assert engine.k0_k3_rank() == 1 + 22 + 1

    def test_k0_e_equals_betti_sum_even_curve(self):
        """rk K_0(E) = b_0 + b_2 = 1 + 1 = 2 (but wait, this is wrong for a curve).

        Actually: for a smooth projective variety, rk K_0 = sum b_{2i}
        by Chern character.  For E: b_0 = 1, b_2 = 1, so rk K_0 = 2.
        """
        assert engine.k0_elliptic_rank() == 2


# ============================================================================
# Section 2: Euler characteristics
# ============================================================================

class TestEulerCharacteristics:
    """Tests for topological and holomorphic Euler characteristics."""

    def test_euler_char_k3_is_24(self):
        """chi(K3) = 24."""
        assert engine.euler_char_k3() == 24

    def test_euler_char_elliptic_is_0(self):
        """chi(E) = 0 for elliptic curve."""
        assert engine.euler_char_elliptic() == 0

    def test_euler_char_k3e_is_0(self):
        """chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0."""
        assert engine.euler_char_k3e() == 0

    def test_euler_char_product_formula(self):
        """chi(S x E) = chi(S) * chi(E)."""
        assert engine.euler_char_k3e() == engine.euler_char_k3() * engine.euler_char_elliptic()

    def test_holomorphic_euler_k3_is_2(self):
        """chi(O_S) = 2 for K3 (NOT 1; h^{2,0} = 1 contributes)."""
        assert engine.holomorphic_euler_char_k3() == 2

    def test_holomorphic_euler_elliptic_is_0(self):
        """chi(O_E) = 0 for elliptic curve."""
        assert engine.holomorphic_euler_char_elliptic() == 0

    def test_holomorphic_euler_k3e_is_0(self):
        """chi(O_{K3 x E}) = 0."""
        assert engine.holomorphic_euler_char_k3e() == 0

    def test_holomorphic_euler_product(self):
        """chi(O_{SxE}) = chi(O_S) * chi(O_E)."""
        assert engine.holomorphic_euler_char_k3e() == (
            engine.holomorphic_euler_char_k3() * engine.holomorphic_euler_char_elliptic()
        )

    def test_euler_from_betti(self):
        """chi = sum (-1)^k b_k = 0 for K3 x E."""
        betti = engine.betti_numbers_k3e()
        chi = sum((-1)**k * betti[k] for k in range(len(betti)))
        assert chi == 0

    def test_noether_formula_k3(self):
        """chi(O_S) = (c_1^2 + c_2)/12 = (0 + 24)/12 = 2 for K3."""
        c2 = engine.euler_char_k3()  # c_2 = chi(K3) = 24
        c1_sq = 0  # trivial canonical
        chi_noether = (c1_sq + c2) // 12
        assert chi_noether == 2
        assert chi_noether == engine.holomorphic_euler_char_k3()


# ============================================================================
# Section 3: Hodge numbers
# ============================================================================

class TestHodgeNumbers:
    """Tests for Hodge numbers of K3, E, and K3 x E."""

    def test_hodge_k3_h00(self):
        assert engine.hodge_numbers_k3()[(0, 0)] == 1

    def test_hodge_k3_h10(self):
        assert engine.hodge_numbers_k3()[(1, 0)] == 0

    def test_hodge_k3_h20(self):
        assert engine.hodge_numbers_k3()[(2, 0)] == 1

    def test_hodge_k3_h11(self):
        assert engine.hodge_numbers_k3()[(1, 1)] == 20

    def test_hodge_k3_symmetry(self):
        """h^{p,q} = h^{q,p} for K3."""
        h = engine.hodge_numbers_k3()
        for (p, q), v in h.items():
            assert v == h.get((q, p), 0), f"h^{p},{q} != h^{q},{p}"

    def test_hodge_k3_serre_duality(self):
        """h^{p,q} = h^{2-p, 2-q} for K3 (surface, dim 2)."""
        h = engine.hodge_numbers_k3()
        for (p, q), v in h.items():
            assert v == h.get((2 - p, 2 - q), 0), f"Serre: h^{p},{q} != h^{2-p},{2-q}"

    def test_hodge_elliptic_h10_is_1(self):
        """h^{1,0}(E) = 1 (genus 1)."""
        assert engine.hodge_numbers_elliptic()[(1, 0)] == 1

    def test_hodge_k3e_kunneth(self):
        """h^{p,q}(S x E) = sum h^{p1,q1}(S) * h^{p2,q2}(E) by Kunneth."""
        h = engine.hodge_numbers_k3e()
        # Verify h^{1,1}(S x E)
        h_s = engine.hodge_numbers_k3()
        h_e = engine.hodge_numbers_elliptic()
        # h^{1,1}(SxE) = h^{0,0}*h^{1,1} + h^{1,1}*h^{0,0} + h^{0,1}*h^{1,0} + h^{1,0}*h^{0,1}
        val = (h_s.get((0, 0), 0) * h_e.get((1, 1), 0)
               + h_s.get((1, 1), 0) * h_e.get((0, 0), 0)
               + h_s.get((0, 1), 0) * h_e.get((1, 0), 0)
               + h_s.get((1, 0), 0) * h_e.get((0, 1), 0))
        assert h[(1, 1)] == val

    def test_hodge_k3e_h10(self):
        """h^{1,0}(K3 x E) = 1 (from h^{0,0}*h^{1,0} + h^{1,0}*h^{0,0} = 0 + 1 = 1)."""
        h = engine.hodge_numbers_k3e()
        assert h[(1, 0)] == 1

    def test_hodge_k3e_h20(self):
        """h^{2,0}(K3 x E) = 1 (from h^{2,0}*h^{0,0} + h^{1,0}*h^{1,0} = 1 + 0 = 1)."""
        h = engine.hodge_numbers_k3e()
        assert h[(2, 0)] == 1

    def test_hodge_k3e_h30(self):
        """h^{3,0}(K3 x E) = 1 (CY3 has unique holomorphic 3-form)."""
        h = engine.hodge_numbers_k3e()
        assert h[(3, 0)] == 1

    def test_hodge_k3e_h11_value(self):
        """h^{1,1}(K3 x E) = 1*1 + 20*1 + 0*1 + 0*1 = 21."""
        h = engine.hodge_numbers_k3e()
        assert h[(1, 1)] == 21

    def test_hodge_k3e_h21_value(self):
        """h^{2,1}(K3 x E) = 21 (by explicit Kunneth)."""
        h = engine.hodge_numbers_k3e()
        assert h[(2, 1)] == 21

    def test_hodge_k3e_serre_duality(self):
        """h^{p,q} = h^{3-p, 3-q} for a 3-fold with trivial canonical."""
        h = engine.hodge_numbers_k3e()
        for (p, q), v in h.items():
            dual = h.get((3 - p, 3 - q), 0)
            assert v == dual, f"Serre: h^{p},{q}={v} != h^{3-p},{3-q}={dual}"

    def test_hodge_k3e_conjugate_symmetry(self):
        """h^{p,q} = h^{q,p} (Hodge symmetry)."""
        h = engine.hodge_numbers_k3e()
        for (p, q), v in h.items():
            assert v == h.get((q, p), 0), f"h^{p},{q} != h^{q},{p}"

    def test_holomorphic_euler_from_hodge(self):
        """chi(O) = h^{0,0} - h^{0,1} + h^{0,2} - h^{0,3} = 1 - 1 + 1 - 1 = 0."""
        h = engine.hodge_numbers_k3e()
        chi = sum((-1)**q * h.get((0, q), 0) for q in range(4))
        assert chi == 0
        assert chi == engine.holomorphic_euler_char_k3e()


# ============================================================================
# Section 4: Betti numbers
# ============================================================================

class TestBettiNumbers:
    """Tests for Betti numbers of K3 x E."""

    def test_betti_0(self):
        assert engine.betti_numbers_k3e()[0] == 1

    def test_betti_1(self):
        assert engine.betti_numbers_k3e()[1] == 2

    def test_betti_2(self):
        assert engine.betti_numbers_k3e()[2] == 23

    def test_betti_3(self):
        assert engine.betti_numbers_k3e()[3] == 44

    def test_betti_4(self):
        assert engine.betti_numbers_k3e()[4] == 23

    def test_betti_5(self):
        assert engine.betti_numbers_k3e()[5] == 2

    def test_betti_6(self):
        assert engine.betti_numbers_k3e()[6] == 1

    def test_betti_poincare_duality(self):
        """b_k = b_{6-k} for a compact oriented 6-manifold."""
        b = engine.betti_numbers_k3e()
        for k in range(7):
            assert b[k] == b[6 - k], f"b_{k} != b_{6-k}"

    def test_betti_sum_is_96(self):
        """sum b_k = 1 + 2 + 23 + 44 + 23 + 2 + 1 = 96."""
        b = engine.betti_numbers_k3e()
        assert sum(b) == 96

    def test_euler_from_betti_is_0(self):
        """chi = sum (-1)^k b_k = 0."""
        b = engine.betti_numbers_k3e()
        assert sum((-1)**k * b[k] for k in range(7)) == 0

    def test_betti_from_hodge_consistency(self):
        """b_k = sum_{p+q=k} h^{p,q}."""
        h = engine.hodge_numbers_k3e()
        b = engine.betti_numbers_k3e()
        for k in range(7):
            bk_from_hodge = sum(h.get((p, k - p), 0) for p in range(4))
            assert b[k] == bk_from_hodge, f"b_{k}: Betti={b[k]} vs Hodge sum={bk_from_hodge}"

    def test_b2_k3e_cross_check(self):
        """b_2(S x E) = b_0(S)*b_2(E) + b_1(S)*b_1(E) + b_2(S)*b_0(E)
                      = 1*1 + 0*2 + 22*1 = 23."""
        assert engine.betti_numbers_k3e()[2] == 23


# ============================================================================
# Section 5: Euler form
# ============================================================================

class TestEulerForm:
    """Tests for the Euler form on K3, E, and K3 x E."""

    def test_euler_form_elliptic_is_symplectic(self):
        """chi_E is the standard symplectic form [[0,1],[-1,0]]."""
        chi = engine.euler_form_elliptic()
        expected = np.array([[0, 1], [-1, 0]], dtype=int)
        assert np.array_equal(chi, expected)

    def test_euler_form_elliptic_antisymmetric(self):
        """chi_E is antisymmetric (genus-1 curve is CY1)."""
        chi = engine.euler_form_elliptic()
        assert np.array_equal(chi, -chi.T)

    def test_euler_form_elliptic_det(self):
        """det(chi_E) = 1."""
        chi = engine.euler_form_elliptic()
        assert int(round(np.linalg.det(chi.astype(float)))) == 1

    def test_euler_form_k3_is_symmetric(self):
        """chi_{K3} is symmetric (surface with trivial canonical)."""
        chi = engine.euler_form_k3_from_mukai()
        assert np.array_equal(chi, chi.T)

    def test_euler_form_k3_size(self):
        """chi_{K3} is 24 x 24."""
        chi = engine.euler_form_k3_from_mukai()
        assert chi.shape == (24, 24)

    def test_euler_form_k3e_size(self):
        """chi_{K3 x E} is 48 x 48."""
        chi = engine.euler_form_k3e()
        assert chi.shape == (48, 48)

    def test_euler_form_k3e_antisymmetric(self):
        """chi_{K3 x E} is antisymmetric (CY3)."""
        chi = engine.euler_form_k3e()
        is_antisym, max_dev = engine.verify_euler_form_antisymmetric(chi)
        assert is_antisym, f"Euler form not antisymmetric, max deviation = {max_dev}"

    def test_euler_form_antisymmetry_from_serre(self):
        """On CY3: chi(E,F) = -chi(F,E) by Serre duality.

        Serre: Ext^k(E,F) = Ext^{3-k}(F,E)^* => chi(E,F) = -chi(F,E).
        The Euler form chi = A otimes B where A = sym, B = antisym => antisym.
        """
        chi = engine.euler_form_k3e()
        assert np.array_equal(chi, -chi.T)

    def test_euler_form_k3e_is_kronecker(self):
        """chi_{SxE} = chi_S otimes chi_E (Kunneth for Euler forms)."""
        chi_s = engine.euler_form_k3_from_mukai()
        chi_e = engine.euler_form_elliptic()
        chi_product = np.kron(chi_s, chi_e)
        chi_k3e = engine.euler_form_k3e()
        assert np.array_equal(chi_k3e, chi_product)

    def test_euler_form_k3e_rank(self):
        """Rank of chi_{K3 x E}: should be 48 (full rank) for generic K3.

        chi_S has rank 24 (nondegenerate Mukai pairing => nondegenerate Euler form).
        chi_E has rank 2 (symplectic form is nondegenerate).
        chi_{SxE} = chi_S otimes chi_E has rank 24 * 2 = 48.
        """
        rank = engine.euler_form_rank(engine.euler_form_k3e())
        assert rank == 48

    def test_euler_form_k3_rank(self):
        """Rank of chi_{K3}: 24 (Mukai lattice is unimodular, hence nondegenerate)."""
        rank = engine.euler_form_rank(engine.euler_form_k3_from_mukai())
        assert rank == 24

    def test_euler_form_self_pairing_zero_cy3(self):
        """chi(E,E) = 0 for all E on CY3.

        For the Euler form matrix: diagonal of chi_{SxE} (viewed as bilinear form)
        need not be zero (it IS zero because chi is antisymmetric, so chi(e_i, e_i) = 0).
        """
        chi = engine.euler_form_k3e()
        diag = np.diag(chi)
        assert np.all(diag == 0), "Diagonal of antisymmetric form must be zero"


# ============================================================================
# Section 6: Mukai lattice
# ============================================================================

class TestMukaiLattice:
    """Tests for the Mukai lattice structure."""

    def test_mukai_lattice_signature(self):
        """Mukai lattice has signature (4, 20)."""
        assert engine.mukai_lattice_signature() == (4, 20)

    def test_mukai_lattice_signature_numerical(self):
        """Verify signature by eigenvalue computation."""
        sig = engine.mukai_lattice_signature_numerical()
        assert sig == (4, 20)

    def test_mukai_lattice_unimodular(self):
        """det(Lambda_{4,20}) = +-1 (unimodular)."""
        det = engine.mukai_lattice_determinant()
        assert abs(det) == 1

    def test_mukai_lattice_rank_24(self):
        """Mukai lattice matrix is 24 x 24."""
        M = engine.euler_form_k3_mukai()
        assert M.shape == (24, 24)

    def test_mukai_lattice_symmetric(self):
        """Mukai pairing is symmetric."""
        M = engine.euler_form_k3_mukai()
        assert np.array_equal(M, M.T)

    def test_mukai_lattice_integral(self):
        """Mukai lattice is integral (integer entries)."""
        M = engine.euler_form_k3_mukai()
        assert M.dtype in (np.int64, np.int32, int)

    def test_intersection_form_k3_signature(self):
        """H^2(K3) intersection form has signature (3, 19)."""
        sig = engine.intersection_form_signature()
        assert sig == (3, 19)

    def test_intersection_form_k3_rank(self):
        """H^2(K3) intersection form has rank 22."""
        M = engine.intersection_form_k3()
        assert M.shape == (22, 22)
        assert int(np.linalg.matrix_rank(M.astype(float))) == 22

    def test_mukai_contains_intersection_form(self):
        """The Mukai lattice (rank 24) contains the intersection lattice (rank 22)
        plus an extra U from H^0 + H^4."""
        assert engine.mukai_lattice_rank() == 22 + 2

    def test_e8_cartan_determinant(self):
        """det(E_8 Cartan matrix) = 1 (E_8 is unimodular).

        E_8 Dynkin diagram (Bourbaki, 0-indexed):
            0 - 1 - 2 - 3 - 4 - 5 - 6
                        |
                        7
        Node 2 is the branch node (degree 3).
        """
        E8 = np.array([
            [2, -1, 0, 0, 0, 0, 0, 0],
            [-1, 2, -1, 0, 0, 0, 0, 0],
            [0, -1, 2, -1, 0, 0, 0, -1],
            [0, 0, -1, 2, -1, 0, 0, 0],
            [0, 0, 0, -1, 2, -1, 0, 0],
            [0, 0, 0, 0, -1, 2, -1, 0],
            [0, 0, 0, 0, 0, -1, 2, 0],
            [0, 0, -1, 0, 0, 0, 0, 2],
        ], dtype=int)
        assert np.array_equal(E8, E8.T), "E8 Cartan matrix must be symmetric"
        assert int(round(np.linalg.det(E8.astype(float)))) == 1

    def test_hyperbolic_plane_det(self):
        """det(U) = -1 (hyperbolic plane)."""
        U = np.array([[0, 1], [1, 0]], dtype=int)
        assert int(round(np.linalg.det(U.astype(float)))) == -1


# ============================================================================
# Section 7: Autoequivalences
# ============================================================================

class TestAutoequivalences:
    """Tests for autoequivalence groups."""

    def test_sl2z_generators_det_1(self):
        """S and T have determinant 1."""
        S, T = engine.sl2z_generators_on_k0e()
        assert int(round(np.linalg.det(S.astype(float)))) == 1
        assert int(round(np.linalg.det(T.astype(float)))) == 1

    def test_sl2z_S_squared(self):
        """S^2 = -I."""
        S, T = engine.sl2z_generators_on_k0e()
        S2 = S @ S
        assert np.array_equal(S2, -np.eye(2, dtype=int))

    def test_sl2z_S4_is_identity(self):
        """S^4 = I (standard SL(2,Z) relation)."""
        rels = engine.verify_sl2z_relations()
        assert rels['S4_eq_I']

    def test_sl2z_ST3_is_S2(self):
        """(ST)^3 = S^2 (standard SL(2,Z) relation)."""
        rels = engine.verify_sl2z_relations()
        assert rels['ST3_eq_S2']

    def test_sl2z_det_S(self):
        rels = engine.verify_sl2z_relations()
        assert rels['det_S'] == 1

    def test_sl2z_det_T(self):
        rels = engine.verify_sl2z_relations()
        assert rels['det_T'] == 1

    def test_sl2z_S_matrix_values(self):
        """S = [[0, 1], [-1, 0]]."""
        S, T = engine.sl2z_generators_on_k0e()
        assert S[0, 0] == 0 and S[0, 1] == 1 and S[1, 0] == -1 and S[1, 1] == 0

    def test_sl2z_T_matrix_values(self):
        """T = [[1, 0], [1, 1]]."""
        S, T = engine.sl2z_generators_on_k0e()
        assert T[0, 0] == 1 and T[0, 1] == 0 and T[1, 0] == 1 and T[1, 1] == 1

    def test_autoequivalence_generators_k3_count(self):
        """At least 3 generators for generic K3."""
        gens = engine.autoequivalence_generators_k3(picard_rank=1)
        assert len(gens) >= 3

    def test_autoequivalence_generators_with_degree(self):
        """With degree specified, get 4 generators."""
        gens = engine.autoequivalence_generators_k3(picard_rank=1, degree=4)
        assert len(gens) == 4

    def test_autoequivalence_group_elliptic_structure(self):
        """Aut(D^b(E)) has the right group structure."""
        grp = engine.autoequivalence_group_elliptic()
        assert 'SL(2,Z)' in grp['group']
        assert 'E x E^vee' in grp['group']

    def test_combined_autoequivalence_acts_on_48(self):
        """Combined autoequivalences act on K_0(K3 x E) = Z^{48}."""
        assert engine.combined_autoequivalence_k0_action_rank() == 48


# ============================================================================
# Section 8: SOD and indecomposability
# ============================================================================

class TestSOD:
    """Tests for semiorthogonal decompositions and indecomposability."""

    def test_k3_no_proper_sod(self):
        """D^b(K3) admits no proper SOD (Bridgeland-Kawamata-Huybrechts)."""
        assert engine.k3_admits_proper_sod() is False

    def test_k3e_no_proper_sod(self):
        """D^b(K3 x E) admits no proper SOD."""
        assert engine.k3e_admits_proper_sod() is False

    def test_no_exceptional_objects_cy3(self):
        """No exceptional objects on any CY3."""
        assert engine.exceptional_objects_exist_k3e() is False

    def test_chi_self_zero_cy3(self):
        """chi(E,E) = 0 for all E on CY3."""
        assert engine.chi_self_pairing_cy3() == 0

    def test_ext_obstruction_details(self):
        """Detailed obstruction to exceptional objects."""
        obs = engine.ext_obstruction_exceptional_cy3()
        assert obs['ext0'] == 1
        assert obs['ext3'] == 1
        assert obs['ext1_equals_ext2'] is True
        assert obs['chi_self'] == 0
        assert obs['exceptional_possible'] is False

    def test_serre_duality_forces_ext3(self):
        """For a simple object on CY3: ext^3 = ext^0 = 1, so ext^3 >= 1."""
        obs = engine.ext_obstruction_exceptional_cy3()
        assert obs['ext3'] >= 1

    def test_chi_self_from_euler_form(self):
        """Every diagonal entry of the antisymmetric Euler form is 0.

        This is the Euler form's way of saying chi(E,E) = 0.
        """
        chi = engine.euler_form_k3e()
        for i in range(48):
            assert chi[i, i] == 0


# ============================================================================
# Section 9: Hochschild homology
# ============================================================================

class TestHochschildHomology:
    """Tests for Hochschild homology via HKR."""

    def test_hh_0_k3e(self):
        """HH_0(K3 x E) = h^{0,0} + h^{1,1} + h^{2,2} + h^{3,3} = 1 + 21 + 21 + 1 = 44."""
        hh = engine.hochschild_homology_k3e()
        assert hh[0] == 44

    def test_hh_1_k3e(self):
        """HH_1 = h^{0,1} + h^{1,2} + h^{2,3} = 1 + 21 + 1 = 23."""
        hh = engine.hochschild_homology_k3e()
        assert hh[1] == 23

    def test_hh_2_k3e(self):
        """HH_2 = h^{0,2} + h^{1,3} = 1 + 1 = 2."""
        hh = engine.hochschild_homology_k3e()
        assert hh[2] == 2

    def test_hh_3_k3e(self):
        """HH_3 = h^{0,3} = 1."""
        hh = engine.hochschild_homology_k3e()
        assert hh[3] == 1

    def test_hh_neg1_k3e(self):
        """HH_{-1} = h^{1,0} + h^{2,1} + h^{3,2} = 1 + 21 + 1 = 23."""
        hh = engine.hochschild_homology_k3e()
        assert hh[-1] == 23

    def test_hh_neg2_k3e(self):
        """HH_{-2} = h^{2,0} + h^{3,1} = 1 + 1 = 2."""
        hh = engine.hochschild_homology_k3e()
        assert hh[-2] == 2

    def test_hh_neg3_k3e(self):
        """HH_{-3} = h^{3,0} = 1."""
        hh = engine.hochschild_homology_k3e()
        assert hh[-3] == 1

    def test_hh_total_dim(self):
        """Total dim HH_* = sum h^{p,q} = sum b_k = 96."""
        hh = engine.hochschild_homology_k3e()
        assert sum(hh.values()) == 96

    def test_hh_symmetry(self):
        """HH_k = HH_{-k} for a CY3 (by Serre duality / HKR).

        On a CY3: h^{p,q} = h^{3-p, 3-q}.
        HH_k = sum_p h^{p, p+k}.
        HH_{-k} = sum_p h^{p, p-k} = sum_p h^{3-p, 3-p+k} = sum_p' h^{p', p'+k} = HH_k.
        """
        hh = engine.hochschild_homology_k3e()
        for k in range(4):
            assert hh.get(k, 0) == hh.get(-k, 0), f"HH_{k} != HH_{-k}"

    def test_hh_0_equals_sum_hodge_diagonal(self):
        """HH_0 = sum_p h^{p,p} = Hodge diagonal sum."""
        h = engine.hodge_numbers_k3e()
        diag_sum = sum(h.get((p, p), 0) for p in range(4))
        hh = engine.hochschild_homology_k3e()
        assert hh[0] == diag_sum


# ============================================================================
# Section 10: Phantom categories
# ============================================================================

class TestPhantomCategories:
    """Tests for phantom category analysis."""

    def test_no_phantoms_k3e(self):
        """K3 x E does not admit phantom subcategories."""
        assert engine.phantom_possible_k3e() is False

    def test_phantom_requires_sod(self):
        """Phantoms require a proper SOD, which K3 x E lacks."""
        assert not engine.k3e_admits_proper_sod()
        assert not engine.phantom_possible_k3e()


# ============================================================================
# Section 11: ADE singularities and quiver categories
# ============================================================================

class TestADEQuiver:
    """Tests for ADE singularity data and quiver categories."""

    def test_ade_rank_An(self):
        for n in range(1, 10):
            assert engine.ade_rank(f'A{n}') == n

    def test_ade_rank_Dn(self):
        for n in range(4, 10):
            assert engine.ade_rank(f'D{n}') == n

    def test_ade_rank_E6(self):
        assert engine.ade_rank('E6') == 6

    def test_ade_rank_E7(self):
        assert engine.ade_rank('E7') == 7

    def test_ade_rank_E8(self):
        assert engine.ade_rank('E8') == 8

    def test_quiver_k0_A1(self):
        """K_0(quiver A_1) = Z^2 (2 vertices in McKay quiver)."""
        assert engine.quiver_category_k0_rank('A1') == 2

    def test_quiver_k0_A2(self):
        assert engine.quiver_category_k0_rank('A2') == 3

    def test_quiver_k0_E8(self):
        assert engine.quiver_category_k0_rank('E8') == 9

    def test_exceptional_collection_length(self):
        """Exceptional collection length = ADE rank."""
        for t in ['A1', 'A2', 'A5', 'D4', 'D5', 'E6', 'E7', 'E8']:
            assert engine.ade_exceptional_collection_length(t) == engine.ade_rank(t)

    def test_k3_ade_not_proper_sod(self):
        """ADE "partial SOD" on K3 is NOT a proper SOD."""
        data = engine.k3_ade_partial_sod('A2')
        assert data['is_proper_sod'] is False

    def test_k3_ade_partial_sod_rank(self):
        """ADE partial SOD has rank matching ADE rank."""
        data = engine.k3_ade_partial_sod('D4')
        assert data['rank'] == 4

    def test_ade_euler_form_An_antisymmetric(self):
        """Euler form of A_n quiver (CY3 version) is antisymmetric."""
        for n in range(1, 8):
            C = engine.euler_form_ade_quiver(f'A{n}')
            assert np.array_equal(C, -C.T), f"A_{n} Euler form not antisymmetric"

    def test_ade_euler_form_Dn_antisymmetric(self):
        """Euler form of D_n quiver (CY3 version) is antisymmetric."""
        for n in range(4, 8):
            C = engine.euler_form_ade_quiver(f'D{n}')
            assert np.array_equal(C, -C.T), f"D_{n} Euler form not antisymmetric"

    def test_ade_euler_form_E_antisymmetric(self):
        """Euler form of E_6, E_7, E_8 quiver (CY3 version) is antisymmetric."""
        for t in ['E6', 'E7', 'E8']:
            C = engine.euler_form_ade_quiver(t)
            assert np.array_equal(C, -C.T), f"{t} Euler form not antisymmetric"

    def test_ade_euler_form_An_size(self):
        """A_n quiver Euler form is (n+1) x (n+1)."""
        for n in range(1, 8):
            C = engine.euler_form_ade_quiver(f'A{n}')
            assert C.shape == (n + 1, n + 1)

    def test_ade_euler_form_zero_diagonal(self):
        """Diagonal is zero for antisymmetric forms."""
        for t in ['A3', 'D5', 'E6']:
            C = engine.euler_form_ade_quiver(t)
            assert np.all(np.diag(C) == 0)


# ============================================================================
# Section 12: Glued category comparison
# ============================================================================

class TestGluedCategory:
    """Tests for glued quiver category comparison with K3 x E."""

    def test_glued_k0_k3_single_A1(self):
        """Single A_1 chart: glued K_0 of K3 is still Z^{24}."""
        assert engine.glued_k0_rank_k3(['A1']) == 24

    def test_glued_k0_k3_single_E8(self):
        assert engine.glued_k0_rank_k3(['E8']) == 24

    def test_glued_k0_k3_multiple_charts(self):
        """Multiple ADE charts still give K_0(K3) = Z^{24}."""
        assert engine.glued_k0_rank_k3(['A1', 'A2', 'D4']) == 24

    def test_glued_k0_k3e_is_48(self):
        """Glued K_0(K3 x E) = 48 for any chart configuration."""
        assert engine.glued_k0_rank_k3e(['A3']) == 48
        assert engine.glued_k0_rank_k3e(['D4', 'A1']) == 48
        assert engine.glued_k0_rank_k3e(['E8']) == 48

    def test_glued_k0_matches_direct(self):
        """Glued K_0 rank matches direct computation."""
        for charts in [['A1'], ['A2', 'A3'], ['D4'], ['E6'], ['E8']]:
            assert engine.glued_k0_rank_k3e(charts) == engine.k0_k3e_rank()

    def test_verification_consistency_A2(self):
        """Full consistency check for A_2 chart."""
        result = engine.verify_glued_euler_form_consistency(['A2'])
        assert result['k0_matches_48']
        assert result['all_antisymmetric']
        assert result['k3_k0_total'] == 24

    def test_verification_consistency_D4(self):
        result = engine.verify_glued_euler_form_consistency(['D4'])
        assert result['k0_matches_48']
        assert result['all_antisymmetric']

    def test_verification_consistency_E8(self):
        result = engine.verify_glued_euler_form_consistency(['E8'])
        assert result['k0_matches_48']
        assert result['all_antisymmetric']

    def test_verification_consistency_multi(self):
        """Multiple charts."""
        result = engine.verify_glued_euler_form_consistency(['A1', 'A2', 'D4'])
        assert result['k0_matches_48']
        assert result['all_antisymmetric']

    def test_smooth_complement_k0_A1(self):
        """Smooth complement of A_1: Z^{23 - 1} = Z^{22}."""
        assert engine.smooth_complement_k0_rank('A1') == 22

    def test_smooth_complement_k0_E8(self):
        """Smooth complement of E_8: Z^{23 - 8} = Z^{15}."""
        assert engine.smooth_complement_k0_rank('E8') == 15

    def test_quiver_plus_complement_is_24(self):
        """quiver_k0 + smooth_complement_k0 = 24 for any ADE type.

        (rank+1) + (23-rank) = 24.  Always.
        """
        for t in ['A1', 'A3', 'D4', 'D6', 'E6', 'E7', 'E8']:
            total = engine.quiver_category_k0_rank(t) + engine.smooth_complement_k0_rank(t)
            assert total == 24, f"Type {t}: {total} != 24"

    def test_quiver_plus_complement_times_2_is_48(self):
        """(quiver + complement) * 2 = 48 for K3 x E."""
        for t in ['A1', 'A3', 'D4', 'E6', 'E8']:
            total = (engine.quiver_category_k0_rank(t) + engine.smooth_complement_k0_rank(t)) * 2
            assert total == 48


# ============================================================================
# Section 13: Full comparison summary
# ============================================================================

class TestFullComparison:
    """Tests for the full multi-path comparison."""

    def test_summary_k0_product(self):
        s = engine.full_comparison_summary()
        assert s['k0_product_check']

    def test_summary_euler_antisymmetric(self):
        s = engine.full_comparison_summary()
        assert s['euler_form_antisymmetric']

    def test_summary_euler_rank(self):
        s = engine.full_comparison_summary()
        assert s['euler_form_rank'] == 48

    def test_summary_euler_consistent(self):
        s = engine.full_comparison_summary()
        assert s['euler_consistent']

    def test_summary_hodge_betti(self):
        s = engine.full_comparison_summary()
        assert s['hodge_betti_consistent']

    def test_summary_sl2z(self):
        s = engine.full_comparison_summary()
        assert s['sl2z_relations']['S4_eq_I']
        assert s['sl2z_relations']['ST3_eq_S2']

    def test_summary_no_sod(self):
        s = engine.full_comparison_summary()
        assert not s['k3_proper_sod']
        assert not s['k3e_proper_sod']

    def test_summary_no_exceptionals(self):
        s = engine.full_comparison_summary()
        assert not s['exceptional_objects_exist']

    def test_summary_chi_self_zero(self):
        s = engine.full_comparison_summary()
        assert s['chi_self_cy3'] == 0

    def test_summary_no_phantoms(self):
        s = engine.full_comparison_summary()
        assert not s['phantoms_possible']

    def test_summary_hh_total(self):
        s = engine.full_comparison_summary()
        assert s['hh_total_dim'] == 96

    def test_summary_euler_char_zero(self):
        s = engine.full_comparison_summary()
        assert s['euler_char_k3e'] == 0
        assert s['holomorphic_euler_k3e'] == 0


# ============================================================================
# Section 14: Multi-path cross-verification
# ============================================================================

class TestMultiPathVerification:
    """Cross-verification of results via independent paths."""

    def test_path_a_b_k_theory_euler_form_rank(self):
        """Path A (lattice) vs Path B (Euler form): both give rank 48."""
        assert engine.k0_k3e_rank() == 48
        assert engine.euler_form_rank(engine.euler_form_k3e()) == 48

    def test_path_a_d_k_theory_betti(self):
        """Path A (K-theory rank) vs Path D (Betti numbers).

        rk K_0(SxE) = 48.
        sum of even Betti = b_0 + b_2 + b_4 + b_6 = 1 + 23 + 23 + 1 = 48.
        """
        b = engine.betti_numbers_k3e()
        even_betti_sum = b[0] + b[2] + b[4] + b[6]
        assert even_betti_sum == engine.k0_k3e_rank()

    def test_path_d_e_betti_euler(self):
        """Path D (Betti) vs Path E (product Euler char): both give chi = 0."""
        b = engine.betti_numbers_k3e()
        chi_betti = sum((-1)**k * b[k] for k in range(7))
        assert chi_betti == 0
        assert chi_betti == engine.euler_char_k3e()

    def test_path_b_f_euler_form_serre(self):
        """Path B (Euler form matrix) vs Path F (Serre duality):
        both require antisymmetry on CY3."""
        chi = engine.euler_form_k3e()
        # Serre duality implies antisymmetry
        assert np.array_equal(chi, -chi.T)
        # Matrix computation confirms
        is_antisym, _ = engine.verify_euler_form_antisymmetric(chi)
        assert is_antisym

    def test_path_c_sl2z_well_defined(self):
        """Path C: SL(2,Z) generators satisfy all relations."""
        rels = engine.verify_sl2z_relations()
        assert all(v if isinstance(v, bool) else v == 1 for v in rels.values())

    def test_path_a_g_glued_k0(self):
        """Path A (direct K-theory) vs Path G (ADE gluing): both give 48."""
        for charts in [['A1'], ['A2', 'D4'], ['E8']]:
            assert engine.glued_k0_rank_k3e(charts) == engine.k0_k3e_rank()

    def test_path_d_hkr_betti_hh(self):
        """Path D (Betti) vs HKR: total dim HH = total dim H = sum Betti."""
        hh = engine.hochschild_homology_k3e()
        b = engine.betti_numbers_k3e()
        assert sum(hh.values()) == sum(b)

    def test_three_paths_euler_char(self):
        """Three paths to chi(K3 x E) = 0:
        (1) Product: 24 * 0 = 0
        (2) Betti: 1-2+23-44+23-2+1 = 0
        (3) Hodge: sum (-1)^{p+q} h^{p,q} = 0
        """
        # Path 1
        chi1 = engine.euler_char_k3e()
        # Path 2
        b = engine.betti_numbers_k3e()
        chi2 = sum((-1)**k * b[k] for k in range(7))
        # Path 3
        h = engine.hodge_numbers_k3e()
        chi3 = sum((-1)**(p + q) * v for (p, q), v in h.items())
        assert chi1 == chi2 == chi3 == 0

    def test_three_paths_k0_rank(self):
        """Three paths to rk K_0(K3 x E) = 48:
        (1) Kunneth: 24 * 2
        (2) Even Betti: b_0 + b_2 + b_4 + b_6
        (3) Euler form: rank of chi matrix
        """
        # Path 1
        r1 = engine.k0_k3e_rank()
        # Path 2
        b = engine.betti_numbers_k3e()
        r2 = b[0] + b[2] + b[4] + b[6]
        # Path 3
        r3 = engine.euler_form_rank(engine.euler_form_k3e())
        assert r1 == r2 == r3 == 48

    def test_three_paths_chi_self_zero(self):
        """Three paths to chi(E,E) = 0 on CY3:
        (1) Serre duality argument (ext^k = ext^{3-k})
        (2) Diagonal of antisymmetric Euler form is 0
        (3) HRR: chi(E,E) = rk^2 * chi(O) + ... = 0 because chi(O) = 0
        """
        # Path 1
        assert engine.chi_self_pairing_cy3() == 0
        # Path 2
        chi = engine.euler_form_k3e()
        assert all(chi[i, i] == 0 for i in range(48))
        # Path 3
        assert engine.holomorphic_euler_char_k3e() == 0

    def test_mukai_lattice_determinant_two_paths(self):
        """det(Mukai lattice):
        Path 1: direct computation
        Path 2: det(U)^4 * det(E8(-1))^2 = (-1)^4 * 1 = 1
        """
        # Path 1
        det1 = engine.mukai_lattice_determinant()
        # Path 2
        det2 = (-1)**4 * 1**2
        assert det1 == det2 == 1

    def test_mukai_signature_two_paths(self):
        """Mukai lattice signature:
        Path 1: U^4 + E_8(-1)^2 => (4, 20)
        Path 2: numerical eigenvalue computation
        """
        sig1 = engine.mukai_lattice_signature()
        sig2 = engine.mukai_lattice_signature_numerical()
        assert sig1 == sig2 == (4, 20)
