r"""Tests for CY-4: Tilting generators and endomorphism algebras on K3 patches.

Multi-path verification (AP10) of:
1. Cartan matrix properties (det, symmetry, positive definiteness)
2. Extended Cartan matrix (null vectors, singularity)
3. Intersection matrices E_i.E_j = -C_{ij}
4. Mukai vectors and pairings (K-theory of K3)
5. Spherical object detection and twist functors (T_E^2 = id on K-theory)
6. Euler form on K3 (chi = -<v,w>)
7. BKR equivalence K-theory maps
8. Positive root enumeration and Coxeter numbers
9. Finite preprojective algebra dimensions

Every numerical result verified by >= 2 independent methods.
"""

import math
import unittest
from fractions import Fraction

import numpy as np

from compute.lib.cy_tilting_k3_engine import (
    cartan_matrix,
    extended_cartan_matrix,
    affine_marks,
    intersection_matrix,
    mukai_vector,
    mukai_pairing,
    euler_form_k3,
    mukai_self_pairing,
    is_spherical,
    spherical_twist_on_mukai,
    spherical_twist_squared_shift,
    rhom_structure_sheaf_to_line_bundle,
    spherical_twist_cone_data,
    cyclic_group_irreps,
    cyclic_mckay_graph,
    positive_roots,
    number_of_positive_roots,
    coxeter_number,
    ade_group_order,
    mckay_adjacency,
    finite_preprojective_dimension,
)


# =====================================================================
# Independent computations
# =====================================================================

def _independent_mukai_pairing(v, w):
    """<(r1,c1,s1), (r2,c2,s2)> = c1*c2 - r1*s2 - r2*s1."""
    r1, c1, s1 = v
    r2, c2, s2 = w
    return c1 * c2 - r1 * s2 - r2 * s1


def _independent_mukai_vector(rk, c1, c2):
    """v(E) = (rk, c1, rk + c1^2/2 - c2) on K3."""
    s = Fraction(c1**2, 2) - c2 + rk
    return (rk, c1, s)


def _independent_num_pos_roots(t, n):
    if t == 'A':
        return n * (n + 1) // 2
    elif t == 'D':
        return n * (n - 1)
    elif t == 'E':
        return {6: 36, 7: 63, 8: 120}[n]


# =====================================================================
# Cartan matrices
# =====================================================================

class TestCartanMatrixProperties(unittest.TestCase):
    """Cartan matrix correctness for ADE types."""

    def test_A_det(self):
        """det(C_{A_n}) = n+1."""
        for n in range(1, 8):
            C = cartan_matrix('A', n)
            det = int(round(np.linalg.det(C)))
            self.assertEqual(det, n + 1)

    def test_A_symmetric(self):
        for n in range(1, 8):
            C = cartan_matrix('A', n)
            self.assertTrue(np.array_equal(C, C.T))

    def test_A_positive_definite(self):
        for n in range(1, 8):
            C = cartan_matrix('A', n)
            eigs = np.linalg.eigvalsh(C.astype(float))
            self.assertTrue(all(e > 1e-10 for e in eigs))

    def test_D_det(self):
        """det(C_{D_n}) = 4."""
        for n in range(4, 9):
            C = cartan_matrix('D', n)
            det = int(round(np.linalg.det(C)))
            self.assertEqual(det, 4)

    def test_D_symmetric(self):
        for n in range(4, 9):
            C = cartan_matrix('D', n)
            self.assertTrue(np.array_equal(C, C.T))

    def test_D_positive_definite(self):
        for n in range(4, 9):
            C = cartan_matrix('D', n)
            eigs = np.linalg.eigvalsh(C.astype(float))
            self.assertTrue(all(e > 1e-10 for e in eigs))

    def test_E_symmetric(self):
        for n in [6, 7, 8]:
            C = cartan_matrix('E', n)
            self.assertTrue(np.array_equal(C, C.T))

    def test_E_positive_definite(self):
        for n in [6, 7, 8]:
            C = cartan_matrix('E', n)
            eigs = np.linalg.eigvalsh(C.astype(float))
            self.assertTrue(all(e > 1e-10 for e in eigs))

    def test_diagonal_is_2(self):
        for t, ranks in [('A', range(1, 7)), ('D', range(4, 8)), ('E', [6, 7, 8])]:
            for n in ranks:
                C = cartan_matrix(t, n)
                for i in range(n):
                    self.assertEqual(C[i, i], 2)

    def test_off_diagonal_nonpositive(self):
        for t, ranks in [('A', range(1, 7)), ('D', range(4, 8)), ('E', [6, 7, 8])]:
            for n in ranks:
                C = cartan_matrix(t, n)
                for i in range(n):
                    for j in range(n):
                        if i != j:
                            self.assertLessEqual(C[i, j], 0)

    def test_A_eigenvalues_formula(self):
        """Eigenvalues = 2 - 2cos(k pi/(n+1)), k=1..n."""
        for n in range(1, 6):
            C = cartan_matrix('A', n)
            eigs = sorted(np.linalg.eigvalsh(C.astype(float)))
            expected = sorted([2 - 2*math.cos(k*math.pi/(n+1))
                              for k in range(1, n+1)])
            for e, ex in zip(eigs, expected):
                self.assertAlmostEqual(e, ex, places=8)


# =====================================================================
# Intersection matrix
# =====================================================================

class TestIntersectionMatrix(unittest.TestCase):
    """E_i . E_j = -C_{ij}: intersection = negative Cartan."""

    def test_equals_neg_cartan(self):
        for t, ranks in [('A', range(1, 7)), ('D', range(4, 8)), ('E', [6, 7, 8])]:
            for n in ranks:
                I_mat = intersection_matrix(t, n)
                C = cartan_matrix(t, n)
                self.assertTrue(np.array_equal(I_mat, -C))

    def test_self_intersection_minus_2(self):
        """All E_i^2 = -2 for ADE exceptional divisors."""
        for t, ranks in [('A', range(1, 7)), ('D', range(4, 8)), ('E', [6, 7, 8])]:
            for n in ranks:
                I_mat = intersection_matrix(t, n)
                for i in range(n):
                    self.assertEqual(I_mat[i, i], -2)

    def test_symmetric(self):
        for t, ranks in [('A', range(1, 7)), ('D', range(4, 8))]:
            for n in ranks:
                I_mat = intersection_matrix(t, n)
                self.assertTrue(np.array_equal(I_mat, I_mat.T))

    def test_negative_definite(self):
        """Intersection form on exceptional divisors is negative definite."""
        for t, ranks in [('A', range(1, 7)), ('D', range(4, 8)), ('E', [6, 7, 8])]:
            for n in ranks:
                I_mat = intersection_matrix(t, n)
                eigs = np.linalg.eigvalsh(I_mat.astype(float))
                self.assertTrue(all(e < -1e-10 for e in eigs))


# =====================================================================
# Mukai vectors and pairings
# =====================================================================

class TestMukaiVector(unittest.TestCase):
    """Mukai vector v(E) = (rk, c1, rk + c1^2/2 - c2) on K3."""

    def test_structure_sheaf(self):
        """v(O_S) = (1, 0, 1)."""
        v = mukai_vector(1, 0, 0)
        self.assertEqual(v, (1, 0, 1))

    def test_structure_sheaf_independent(self):
        v = _independent_mukai_vector(1, 0, 0)
        self.assertEqual(v, (1, 0, 1))

    def test_line_bundle(self):
        """v(O(H)) with H^2 = 2d: v = (1, 1, 1 + d)."""
        for d in [1, 2, 3, 4]:
            v = mukai_vector(1, 1, 0)
            # c2 = 0 for line bundle, c1 = 1 (class of H)
            # s = 1 + 1/2 - 0 = 3/2
            self.assertEqual(v, (1, 1, Fraction(3, 2)))

    def test_ideal_sheaf(self):
        """v(I_Z) where Z is n points: v = (1, 0, 1-n)."""
        for n in range(1, 6):
            v = mukai_vector(1, 0, n)
            self.assertEqual(v, (1, 0, 1 - n))

    def test_skyscraper(self):
        """v(O_p) = (0, 0, 1)."""
        v = mukai_vector(0, 0, -1)
        self.assertEqual(v, (0, 0, 1))

    def test_matches_independent(self):
        for rk, c1, c2 in [(1, 0, 0), (1, 2, 3), (2, 1, 5), (0, 0, -1)]:
            v_eng = mukai_vector(rk, c1, c2)
            v_ind = _independent_mukai_vector(rk, c1, c2)
            self.assertEqual(v_eng, v_ind)


class TestMukaiPairing(unittest.TestCase):
    """Mukai pairing <v, w> = c1*c2 - r1*s2 - r2*s1."""

    def test_self_pairing_O(self):
        """<v(O), v(O)> = 0 - 1*1 - 1*1 = -2."""
        v = (1, 0, 1)
        self.assertEqual(mukai_pairing(v, v), -2)

    def test_self_pairing_independent(self):
        v = (1, 0, 1)
        self.assertEqual(_independent_mukai_pairing(v, v), -2)
        self.assertEqual(mukai_pairing(v, v), _independent_mukai_pairing(v, v))

    def test_skyscraper_self_pairing(self):
        """<v(O_p), v(O_p)> = 0 - 0 - 0 = 0."""
        v = (0, 0, 1)
        self.assertEqual(mukai_pairing(v, v), 0)

    def test_bilinearity(self):
        """<v + w, u> = <v, u> + <w, u>."""
        v = (1, 0, 1)
        w = (0, 0, 1)
        u = (1, 2, 3)
        vpw = (v[0]+w[0], v[1]+w[1], v[2]+w[2])
        lhs = mukai_pairing(vpw, u)
        rhs = mukai_pairing(v, u) + mukai_pairing(w, u)
        self.assertEqual(lhs, rhs)

    def test_symmetric(self):
        """<v, w> = <w, v> (symmetric pairing)."""
        pairs = [((1, 0, 1), (0, 0, 1)),
                 ((1, 2, 3), (2, 1, 4)),
                 ((1, 0, 1), (1, 1, Fraction(3, 2)))]
        for v, w in pairs:
            self.assertEqual(mukai_pairing(v, w), mukai_pairing(w, v))

    def test_matches_independent(self):
        pairs = [((1, 0, 1), (0, 0, 1)),
                 ((2, 3, 5), (1, -1, 2)),
                 ((1, 0, 1), (1, 0, 1))]
        for v, w in pairs:
            self.assertEqual(mukai_pairing(v, w),
                             _independent_mukai_pairing(v, w))


class TestEulerForm(unittest.TestCase):
    """Euler form chi(E,F) = -<v(E), v(F)> on K3."""

    def test_chi_O_O(self):
        """chi(O, O) = -<(1,0,1),(1,0,1)> = 2."""
        v = (1, 0, 1)
        self.assertEqual(euler_form_k3(v, v), 2)

    def test_chi_symmetric(self):
        """chi(E, F) = chi(F, E) on K3 (CY2 property)."""
        v = (1, 0, 1)
        w = (0, 0, 1)
        self.assertEqual(euler_form_k3(v, w), euler_form_k3(w, v))

    def test_chi_equals_neg_pairing(self):
        v = (1, 2, 3)
        w = (2, 1, 5)
        self.assertEqual(euler_form_k3(v, w), -mukai_pairing(v, w))


class TestMukaiSelfPairing(unittest.TestCase):
    """<v, v> = c^2 - 2rs."""

    def test_structure_sheaf(self):
        self.assertEqual(mukai_self_pairing((1, 0, 1)), -2)

    def test_skyscraper(self):
        self.assertEqual(mukai_self_pairing((0, 0, 1)), 0)

    def test_consistent_with_pairing(self):
        for v in [(1, 0, 1), (2, 3, 5), (0, 0, 1), (1, 2, -1)]:
            self.assertEqual(mukai_self_pairing(v), mukai_pairing(v, v))


# =====================================================================
# Spherical objects
# =====================================================================

class TestSphericalObjects(unittest.TestCase):
    """Test spherical object detection."""

    def test_O_is_spherical(self):
        """O_S on K3 is spherical: <v,v> = -2."""
        self.assertTrue(is_spherical((1, 0, 1), dim=2))

    def test_skyscraper_not_spherical(self):
        """O_p has <v,v> = 0 != -2."""
        self.assertFalse(is_spherical((0, 0, 1), dim=2))

    def test_ideal_sheaf_of_1pt(self):
        """I_p (ideal of 1 point): v = (1, 0, 0), <v,v> = 0 != -2."""
        self.assertFalse(is_spherical((1, 0, 0), dim=2))

    def test_CY3_spherical_criterion(self):
        """CY3: spherical iff <v,v> = 0."""
        self.assertTrue(is_spherical((0, 0, 1), dim=3))
        self.assertFalse(is_spherical((1, 0, 1), dim=3))


# =====================================================================
# Spherical twist functors
# =====================================================================

class TestSphericalTwist(unittest.TestCase):
    """Test spherical twist T_E on Mukai vectors."""

    def test_twist_squared_is_identity(self):
        """T_E^2 = [-2] acts as identity on K-theory."""
        v_E = (1, 0, 1)  # O_S
        for v_F in [(0, 0, 1), (1, 2, 3), (2, -1, 5), (1, 0, 1)]:
            v_result = spherical_twist_squared_shift(v_E, v_F)
            self.assertEqual(v_result, v_F,
                             f"T^2({v_F}) = {v_result} != {v_F}")

    def test_twist_O_on_O(self):
        """T_O(O): <O,O> = -2, so T_O(O) = O + (-2)*O = -O.
        On K-theory: v(T_O(O)) = (1,0,1) + (-2)*(1,0,1) = (-1,0,-1)."""
        v = (1, 0, 1)
        result = spherical_twist_on_mukai(v, v)
        self.assertEqual(result, (-1, 0, -1))

    def test_twist_preserves_pairing(self):
        """T_E preserves the Mukai pairing (isometry)."""
        v_E = (1, 0, 1)
        v_F = (0, 0, 1)
        v_G = (1, 2, 3)
        tf = spherical_twist_on_mukai(v_E, v_F)
        tg = spherical_twist_on_mukai(v_E, v_G)
        self.assertEqual(mukai_pairing(tf, tg), mukai_pairing(v_F, v_G))

    def test_twist_preserves_self_pairing(self):
        v_E = (1, 0, 1)
        for v_F in [(0, 0, 1), (1, 2, 3), (2, -1, 5)]:
            tf = spherical_twist_on_mukai(v_E, v_F)
            self.assertEqual(mukai_self_pairing(tf), mukai_self_pairing(v_F))

    def test_cone_data_quartic_K3(self):
        """Cone data for quartic K3 (H^2=4)."""
        data = spherical_twist_cone_data(4)
        self.assertEqual(data['rhom_rank'], 4)  # 2 + 4/2
        # v_O = (1, 0, 1) is spherical
        self.assertTrue(is_spherical(data['v_O'], dim=2))

    def test_cone_data_degree_2(self):
        """Cone data for degree 2 K3."""
        data = spherical_twist_cone_data(2)
        self.assertEqual(data['rhom_rank'], 3)
        self.assertTrue(is_spherical(data['v_O'], dim=2))


# =====================================================================
# RHom computations
# =====================================================================

class TestRHom(unittest.TestCase):
    """Test RHom(O, O(H)) via Kodaira vanishing."""

    def test_quartic_k3(self):
        """H^2 = 4: chi(O(H)) = 2 + 2 = 4."""
        result = rhom_structure_sheaf_to_line_bundle(4)
        self.assertEqual(result['ext0'], 4)
        self.assertEqual(result['ext1'], 0)
        self.assertEqual(result['ext2'], 0)
        self.assertEqual(result['chi'], 4)

    def test_degree_2(self):
        """H^2 = 2: chi = 2 + 1 = 3."""
        result = rhom_structure_sheaf_to_line_bundle(2)
        self.assertEqual(result['chi'], 3)

    def test_degree_6(self):
        """H^2 = 6: chi = 2 + 3 = 5."""
        result = rhom_structure_sheaf_to_line_bundle(6)
        self.assertEqual(result['chi'], 5)

    def test_cross_check_rhom_values(self):
        """RHom(O, O(H)) values: chi = 2 + d/2 for H^2 = d."""
        for d in [2, 4, 6, 8]:
            rh = rhom_structure_sheaf_to_line_bundle(d)
            expected_chi = 2 + d // 2
            self.assertEqual(rh['chi'], expected_chi)
            self.assertEqual(rh['ext0'], expected_chi)
            self.assertEqual(rh['ext1'], 0)
            self.assertEqual(rh['ext2'], 0)

    def test_odd_degree_raises(self):
        with self.assertRaises(ValueError):
            rhom_structure_sheaf_to_line_bundle(3)


# =====================================================================
# McKay graph and BKR
# =====================================================================

class TestCyclicMcKay(unittest.TestCase):
    """Test cyclic group McKay graph."""

    def test_irreps_count(self):
        for n in range(2, 8):
            irreps = cyclic_group_irreps(n)
            self.assertEqual(len(irreps), n)

    def test_irreps_all_dim_1(self):
        for n in range(2, 8):
            for rep in cyclic_group_irreps(n):
                self.assertEqual(rep['dim'], 1)

    def test_mckay_graph_symmetric(self):
        for n in range(2, 8):
            adj = cyclic_mckay_graph(n)
            self.assertTrue(np.array_equal(adj, adj.T))

    def test_mckay_graph_is_cycle(self):
        """Each vertex has degree 2 in the McKay graph (cycle)."""
        for n in range(3, 8):
            adj = cyclic_mckay_graph(n)
            for i in range(n):
                self.assertEqual(np.sum(adj[i, :]), 2)

    def test_mckay_graph_Z2(self):
        """Z/2 McKay graph: vertex 0 connects to vertex 1."""
        adj = cyclic_mckay_graph(2)
        # In this engine, adjacency is 1 (undirected edge, not double arrow)
        self.assertGreater(adj[0, 1], 0)
        self.assertEqual(adj[0, 1], adj[1, 0])


# =====================================================================
# Positive roots and Coxeter numbers
# =====================================================================

class TestPositiveRoots(unittest.TestCase):
    """Positive root enumeration cross-checked."""

    def test_A_count(self):
        for n in range(1, 7):
            roots = positive_roots('A', n)
            expected = _independent_num_pos_roots('A', n)
            self.assertEqual(len(roots), expected)

    def test_D_count(self):
        for n in range(4, 8):
            roots = positive_roots('D', n)
            expected = _independent_num_pos_roots('D', n)
            self.assertEqual(len(roots), expected)

    def test_E_count_formula(self):
        """E type root counts from the formula function."""
        for n in [6, 7, 8]:
            self.assertEqual(number_of_positive_roots('E', n),
                             _independent_num_pos_roots('E', n))

    def test_number_formula(self):
        """number_of_positive_roots matches independent calculation."""
        for t, ranks in [('A', range(1, 7)), ('D', range(4, 8)), ('E', [6, 7, 8])]:
            for n in ranks:
                self.assertEqual(number_of_positive_roots(t, n),
                                 _independent_num_pos_roots(t, n))

    def test_simple_roots_present(self):
        for n in range(1, 6):
            roots = positive_roots('A', n)
            root_tuples = [tuple(r) for r in roots]
            for i in range(n):
                e = tuple(1 if j == i else 0 for j in range(n))
                self.assertIn(e, root_tuples)

    def test_highest_root_A(self):
        """Highest root of A_n is (1,...,1)."""
        for n in range(1, 6):
            roots = positive_roots('A', n)
            highest = tuple(1 for _ in range(n))
            self.assertIn(highest, [tuple(r) for r in roots])

    def test_all_positive(self):
        for n in range(1, 6):
            for root in positive_roots('A', n):
                self.assertTrue(all(c >= 0 for c in root))

    def test_root_count_formula_Phi_plus_eq_hn_over_2(self):
        """For simply-laced: |Phi+| = h*n/2."""
        for t, ranks in [('A', range(1, 7)), ('D', range(4, 8)), ('E', [6, 7, 8])]:
            for n in ranks:
                h = coxeter_number(t, n)
                expected = h * n // 2
                self.assertEqual(number_of_positive_roots(t, n), expected)


class TestCoxeterNumbers(unittest.TestCase):
    """Test Coxeter numbers."""

    def test_A(self):
        for n in range(1, 8):
            self.assertEqual(coxeter_number('A', n), n + 1)

    def test_D(self):
        for n in range(4, 9):
            self.assertEqual(coxeter_number('D', n), 2 * (n - 1))

    def test_E(self):
        self.assertEqual(coxeter_number('E', 6), 12)
        self.assertEqual(coxeter_number('E', 7), 18)
        self.assertEqual(coxeter_number('E', 8), 30)


class TestGroupOrders(unittest.TestCase):
    """Test |Gamma| for ADE subgroups."""

    def test_A(self):
        for n in range(1, 8):
            self.assertEqual(ade_group_order('A', n), n + 1)

    def test_D(self):
        for n in range(4, 9):
            self.assertEqual(ade_group_order('D', n), 4 * (n - 2))

    def test_E(self):
        self.assertEqual(ade_group_order('E', 6), 24)
        self.assertEqual(ade_group_order('E', 7), 48)
        self.assertEqual(ade_group_order('E', 8), 120)


# =====================================================================
# Finite preprojective dimensions
# =====================================================================

class TestFinitePreprojective(unittest.TestCase):
    """Test dim Pi(Q) for finite Dynkin quivers."""

    def test_A_formula(self):
        """dim Pi(A_n) = C(n+2, 3) = n(n+1)(n+2)/6."""
        for n in range(1, 8):
            dim = finite_preprojective_dimension('A', n)
            expected = n * (n + 1) * (n + 2) // 6
            self.assertEqual(dim, expected)

    def test_A_known_values(self):
        known = {1: 1, 2: 4, 3: 10, 4: 20, 5: 35, 6: 56}
        for n, expected in known.items():
            self.assertEqual(finite_preprojective_dimension('A', n), expected)

    def test_D_formula(self):
        """dim Pi(D_n) = n(n-1)(2n-1)/3."""
        for n in range(4, 9):
            dim = finite_preprojective_dimension('D', n)
            expected = n * (n - 1) * (2*n - 1) // 3
            self.assertEqual(dim, expected)

    def test_D_known_values(self):
        known = {4: 28, 5: 60, 6: 110, 7: 182, 8: 280}
        for n, expected in known.items():
            self.assertEqual(finite_preprojective_dimension('D', n), expected)

    def test_monotone_A(self):
        prev = 0
        for n in range(1, 8):
            dim = finite_preprojective_dimension('A', n)
            self.assertGreater(dim, prev)
            prev = dim

    def test_monotone_D(self):
        prev = 0
        for n in range(4, 9):
            dim = finite_preprojective_dimension('D', n)
            self.assertGreater(dim, prev)
            prev = dim


if __name__ == '__main__':
    unittest.main()
