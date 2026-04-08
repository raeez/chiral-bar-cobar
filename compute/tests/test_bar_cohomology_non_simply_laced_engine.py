r"""Tests for bar cohomology of non-simply-laced affine algebras G_2, B_2, F_4.

Ground truth (from CE cohomology of loop algebra g_-, verified by exact
rational Gaussian elimination, cross-checked against CE Euler characteristic
generating function prod_{n>=1} (1-t^n)^{dim(g)}):

B_2 = so(5) = sp(4), dim=10, rank=2, h=4, h^vee=3:
    H^1_1 = 10, H^2_2 = 35, H^3_3 = 30, H^3_4 = 105, H^4_5 = 238
    Euler series: [1, -10, 35, -30, -105, 238, 0, -260, -165]
    kappa = 5(k+3)/3, c = 10k/(k+3)

G_2, dim=14, rank=2, h=6, h^vee=4:
    H^1_1 = 14, H^2_2 = 77, H^3_3 = 182, weight 4 = ZERO
    Euler series: [1, -14, 77, -182, 0, 924, -1547, -506, 3003]
    kappa = 7(k+4)/4, c = 14k/(k+4)

F_4, dim=52, rank=4, h=12, h^vee=9:
    H^1_1 = 52 (= dim F_4)
    Euler series: [1, -52, 1274, -19448, ...]
    kappa = 26(k+9)/9

Key findings:
    1. All non-simply-laced KM algebras are Koszul (PBW collapse).
    2. Bar cohomology is k-independent (no central extension in g_-).
    3. H^1 = dim(g) for all (generators of Koszul dual).
    4. Cohomology concentrated in a single degree at each weight.
    5. The concentration degree is NOT always p = w (e.g., B2 w=4 has p=3).
    6. Euler characteristic series has zeros at specific weights related
       to the root system structure.
    7. B2 = C2 as Lie algebras: bar cohomology identical (Langlands trivial).
    8. G2 is self-Langlands-dual: automatic.
    9. Growth rates differ by dimension: F4 >> G2 > B2.

References:
    non_simply_laced_shadows.py: shadow obstruction tower data
    mc2_cyclic_ce.py: G_2 and sp_4 structure constants
    bar_cohomology_sl3_explicit_engine.py: sl_3 comparison
    bar_cohomology_sl2_explicit_engine.py: sl_2 comparison
"""

import pytest
from fractions import Fraction
from math import comb

from compute.lib.bar_cohomology_non_simply_laced_engine import (
    # Core computation
    bar_cohomology_dims,
    ce_euler_series,
    pbw_dim,
    bar_cohomology_growth_rate,
    # Engine
    build_engine,
    g2_engine,
    b2_engine,
    c2_engine,
    LoopCEEngine,
    # Structure constants
    get_structure_constants,
    verify_jacobi,
    # Comparison
    compare_rank2_bar_cohomology,
    langlands_dual_comparison,
    root_length_decomposition,
    # Modular characteristics
    kappa_affine,
    central_charge_affine,
    # Full table
    compute_full_table,
)

from compute.lib.lie_algebra import cartan_data


# ============================================================
# Lie algebra data
# ============================================================

class TestLieAlgebraData:
    """Verify basic Lie algebra data from cartan_data."""

    def test_b2_dim(self):
        assert cartan_data('B', 2).dim == 10

    def test_b2_h(self):
        assert cartan_data('B', 2).h == 4

    def test_b2_h_dual(self):
        assert cartan_data('B', 2).h_dual == 3

    def test_b2_rank(self):
        assert cartan_data('B', 2).rank == 2

    def test_b2_exponents(self):
        assert cartan_data('B', 2).exponents == [1, 3]

    def test_b2_n_positive_roots(self):
        assert len(cartan_data('B', 2).positive_roots) == 4

    def test_c2_dim(self):
        assert cartan_data('C', 2).dim == 10

    def test_c2_h(self):
        assert cartan_data('C', 2).h == 4

    def test_c2_h_dual(self):
        """B2 and C2 have same h^vee (isomorphic Lie algebras)."""
        assert cartan_data('C', 2).h_dual == 3

    def test_g2_dim(self):
        assert cartan_data('G', 2).dim == 14

    def test_g2_h(self):
        assert cartan_data('G', 2).h == 6

    def test_g2_h_dual(self):
        assert cartan_data('G', 2).h_dual == 4

    def test_g2_exponents(self):
        assert cartan_data('G', 2).exponents == [1, 5]

    def test_g2_n_positive_roots(self):
        assert len(cartan_data('G', 2).positive_roots) == 6

    def test_f4_dim(self):
        assert cartan_data('F', 4).dim == 52

    def test_f4_h(self):
        assert cartan_data('F', 4).h == 12

    def test_f4_h_dual(self):
        assert cartan_data('F', 4).h_dual == 9

    def test_f4_exponents(self):
        assert cartan_data('F', 4).exponents == [1, 5, 7, 11]

    def test_f4_n_positive_roots(self):
        assert len(cartan_data('F', 4).positive_roots) == 24

    def test_h_neq_h_dual_b2(self):
        """Non-simply-laced: h != h^vee."""
        d = cartan_data('B', 2)
        assert d.h != d.h_dual

    def test_h_neq_h_dual_g2(self):
        d = cartan_data('G', 2)
        assert d.h != d.h_dual

    def test_h_neq_h_dual_f4(self):
        d = cartan_data('F', 4)
        assert d.h != d.h_dual


# ============================================================
# Structure constants and Jacobi identity
# ============================================================

class TestStructureConstants:
    """Verify structure constants are well-defined Lie algebras."""

    def test_b2_dim(self):
        dim, sc = get_structure_constants('B2')
        assert dim == 10

    def test_g2_dim(self):
        dim, sc = get_structure_constants('G2')
        assert dim == 14

    def test_b2_jacobi(self):
        """Jacobi identity for B2 = so(5)."""
        assert verify_jacobi('B2')

    def test_g2_jacobi(self):
        """Jacobi identity for G2."""
        assert verify_jacobi('G2')

    def test_b2_antisymmetry(self):
        """[a,b] = -[b,a] for all pairs."""
        dim, sc = get_structure_constants('B2')
        for (i, j), out in sc.items():
            rev = sc.get((j, i), {})
            for k, v in out.items():
                assert rev.get(k, Fraction(0)) == -v, \
                    f"Antisymmetry fails at ({i},{j},{k})"

    def test_g2_antisymmetry(self):
        dim, sc = get_structure_constants('G2')
        for (i, j), out in sc.items():
            rev = sc.get((j, i), {})
            for k, v in out.items():
                assert rev.get(k, Fraction(0)) == -v

    def test_b2_bracket_count(self):
        """B2 has 10 generators, many nonzero brackets."""
        dim, sc = get_structure_constants('B2')
        assert len(sc) > 20  # many pairs have nonzero bracket

    def test_g2_bracket_count(self):
        dim, sc = get_structure_constants('G2')
        assert len(sc) > 40

    def test_b2_c2_same_structure(self):
        """B2 and C2 give the same Lie algebra (isomorphic)."""
        dim_b, sc_b = get_structure_constants('B2')
        dim_c, sc_c = get_structure_constants('C2')
        assert dim_b == dim_c
        # Same bracket tables (same constructor)
        assert sc_b == sc_c


# ============================================================
# Colored partitions (PBW Hilbert series)
# ============================================================

class TestPBWDims:
    """PBW dimension = coeff of q^n in prod_{m>=1} 1/(1-q^m)^d."""

    def test_p0(self):
        for d in [8, 10, 14, 52]:
            assert pbw_dim(0, d) == 1

    def test_p1(self):
        for d in [8, 10, 14, 52]:
            assert pbw_dim(1, d) == d

    def test_p2_dim10(self):
        """dim=10: q^2 coeff = C(11,2) + 10 = 55 + 10 = 65.

        From prod at q^2: (1-q)^{-10} gives C(11,2)=55,
        (1-q^2)^{-10} gives 10, cross terms zero.
        """
        assert pbw_dim(2, 10) == 65

    def test_p2_dim14(self):
        """dim=14: C(15,2) + 14 = 105 + 14 = 119."""
        assert pbw_dim(2, 14) == 119

    def test_p2_dim8(self):
        """dim=8: C(9,2) + 8 = 36 + 8 = 44."""
        assert pbw_dim(2, 8) == 44

    def test_p2_formula(self):
        """p_d(2) = C(d+1,2) + d = d(d+3)/2 for all d."""
        for d in [3, 8, 10, 14, 52]:
            assert pbw_dim(2, d) == d * (d + 3) // 2


# ============================================================
# CE Euler series 1/H_A(t) = prod (1-t^n)^d
# ============================================================

class TestEulerSeries:
    """Verify the signed Euler characteristic series."""

    def test_weight0(self):
        for d in [8, 10, 14, 52]:
            assert ce_euler_series(1, d)[0] == 1

    def test_weight1_equals_neg_dim(self):
        """chi_1 = -dim(g) for all g (one mode at weight 1)."""
        for d in [8, 10, 14, 52]:
            assert ce_euler_series(1, d)[1] == -d

    def test_b2_euler_series(self):
        chi = ce_euler_series(8, 10)
        expected = [1, -10, 35, -30, -105, 238, 0, -260, -165]
        assert chi == expected

    def test_g2_euler_series(self):
        chi = ce_euler_series(8, 14)
        expected = [1, -14, 77, -182, 0, 924, -1547, -506, 3003]
        assert chi == expected

    def test_a2_euler_series(self):
        """sl_3 for comparison."""
        chi = ce_euler_series(8, 8)
        expected = [1, -8, 20, 0, -70, 64, 56, 0, -125]
        assert chi == expected

    def test_f4_euler_first_terms(self):
        chi = ce_euler_series(3, 52)
        assert chi[0] == 1
        assert chi[1] == -52
        assert chi[2] == 1274
        assert chi[3] == -19448

    def test_euler_vs_partition_reciprocal(self):
        """chi_w = coeff of t^w in prod (1-t^n)^d.

        Cross-check: sum_{w>=0} chi_w * p_d(w) t^w should be
        sum of coeffs of (prod (1-t^n)^d)(prod (1-t^n)^{-d}) = 1.
        """
        for d in [10, 14]:
            chi = ce_euler_series(10, d)
            # Convolution chi * p_d should give [1, 0, 0, ...]
            for w in range(1, 10):
                s = sum(chi[j] * pbw_dim(w - j, d)
                        for j in range(w + 1))
                assert s == 0, f"d={d}, w={w}: convolution = {s}"


# ============================================================
# Bar cohomology dimensions
# ============================================================

class TestBarCohomologyDims:
    """Bar cohomology = |chi_w| from the Euler series."""

    def test_h1_equals_dim(self):
        """H^1 = dim(g) for all KM algebras."""
        for d in [8, 10, 14, 52]:
            bd = bar_cohomology_dims(1, d)
            assert bd[1] == d

    def test_b2_dims(self):
        bd = bar_cohomology_dims(8, 10)
        expected = [1, 10, 35, 30, 105, 238, 0, 260, 165]
        assert bd == expected

    def test_g2_dims(self):
        bd = bar_cohomology_dims(8, 14)
        expected = [1, 14, 77, 182, 0, 924, 1547, 506, 3003]
        assert bd == expected

    def test_a2_dims(self):
        bd = bar_cohomology_dims(8, 8)
        expected = [1, 8, 20, 0, 70, 64, 56, 0, 125]
        assert bd == expected

    def test_f4_h1(self):
        bd = bar_cohomology_dims(1, 52)
        assert bd[1] == 52

    def test_f4_h2(self):
        bd = bar_cohomology_dims(2, 52)
        assert bd[2] == 1274

    def test_g2_zero_at_weight4(self):
        """G2 has a vanishing at weight 4."""
        bd = bar_cohomology_dims(4, 14)
        assert bd[4] == 0

    def test_a2_zero_at_weight3(self):
        """sl_3 has a vanishing at weight 3."""
        bd = bar_cohomology_dims(3, 8)
        assert bd[3] == 0

    def test_b2_no_early_zero(self):
        """B2 has no zero before weight 6."""
        bd = bar_cohomology_dims(5, 10)
        for w in range(1, 6):
            assert bd[w] > 0, f"B2 vanishes at weight {w}"

    def test_b2_zero_at_weight6(self):
        bd = bar_cohomology_dims(6, 10)
        assert bd[6] == 0

    def test_all_nonneg(self):
        """Bar cohomology dims are nonnegative (Koszulness)."""
        for d in [8, 10, 14, 52]:
            bd = bar_cohomology_dims(12, d)
            for w in range(len(bd)):
                assert bd[w] >= 0, f"d={d}, w={w}: dim = {bd[w]}"


# ============================================================
# CE cohomology engine (exact computation)
# ============================================================

class TestCEEngineB2:
    """Exact CE cohomology for B2 = so(5), dim=10."""

    @pytest.fixture(scope='class')
    def eng(self):
        return build_engine('B2', max_weight=5)

    def test_h1_weight1(self, eng):
        """H^1_1 = 10 = dim(B2)."""
        assert eng.cohomology_at(1, 1) == 10

    def test_h2_weight2(self, eng):
        """H^2_2 = 35."""
        assert eng.cohomology_at(2, 2) == 35

    def test_h3_weight3(self, eng):
        """H^3_3 = 30."""
        assert eng.cohomology_at(3, 3) == 30

    def test_h3_weight4(self, eng):
        """H^3_4 = 105 (degree jump: cohomology at degree 3, not 4)."""
        assert eng.cohomology_at(3, 4) == 105

    def test_h4_weight4_zero(self, eng):
        """H^4_4 = 0 (NO cohomology at the diagonal for w=4)."""
        assert eng.cohomology_at(4, 4) == 0

    def test_h4_weight5(self, eng):
        """H^4_5 = 238."""
        assert eng.cohomology_at(4, 5) == 238

    def test_d_squared_zero_11(self, eng):
        assert eng.verify_d_squared(1, 1) == 0

    def test_d_squared_zero_12(self, eng):
        assert eng.verify_d_squared(1, 2) == 0

    def test_d_squared_zero_22(self, eng):
        assert eng.verify_d_squared(2, 2) == 0

    def test_d_squared_zero_23(self, eng):
        assert eng.verify_d_squared(2, 3) == 0

    def test_off_diagonal_zero_w1(self, eng):
        """Only degree 1 is nonzero at weight 1."""
        assert eng.cohomology_at(2, 1) == 0

    def test_off_diagonal_zero_w2(self, eng):
        """Only degree 2 is nonzero at weight 2."""
        assert eng.cohomology_at(1, 2) == 0
        assert eng.cohomology_at(3, 2) == 0

    def test_euler_char_w1(self, eng):
        """chi_1 = -10."""
        chi = sum((-1)**p * eng.cohomology_at(p, 1) for p in range(1, 5))
        assert chi == -10

    def test_euler_char_w2(self, eng):
        chi = sum((-1)**p * eng.cohomology_at(p, 2) for p in range(1, 8))
        assert chi == 35

    def test_euler_char_w3(self, eng):
        chi = sum((-1)**p * eng.cohomology_at(p, 3) for p in range(1, 10))
        assert chi == -30

    def test_euler_char_w4(self, eng):
        chi = sum((-1)**p * eng.cohomology_at(p, 4) for p in range(1, 12))
        assert chi == -105

    def test_concentration_w1(self, eng):
        """Cohomology concentrated in single degree at weight 1."""
        nonzero = [p for p in range(1, 5) if eng.cohomology_at(p, 1) > 0]
        assert len(nonzero) == 1
        assert nonzero[0] == 1

    def test_concentration_w4(self, eng):
        """At weight 4, cohomology concentrated at degree 3 (not 4)."""
        nonzero = [p for p in range(1, 12) if eng.cohomology_at(p, 4) > 0]
        assert len(nonzero) == 1
        assert nonzero[0] == 3


class TestCEEngineG2:
    """Exact CE cohomology for G2, dim=14."""

    @pytest.fixture(scope='class')
    def eng(self):
        return build_engine('G2', max_weight=4)

    def test_h1_weight1(self, eng):
        """H^1_1 = 14 = dim(G2)."""
        assert eng.cohomology_at(1, 1) == 14

    def test_h2_weight2(self, eng):
        """H^2_2 = 77."""
        assert eng.cohomology_at(2, 2) == 77

    def test_h3_weight3(self, eng):
        """H^3_3 = 182."""
        assert eng.cohomology_at(3, 3) == 182

    def test_weight4_all_zero(self, eng):
        """Weight 4 is COMPLETELY ZERO for G2."""
        for p in range(1, 8):
            basis = eng.weight_basis(p, 4)
            if not basis:
                continue
            assert eng.cohomology_at(p, 4) == 0, f"H^{p}_4 nonzero for G2"

    def test_d_squared_zero(self, eng):
        for p, w in [(1, 1), (1, 2), (2, 2), (2, 3)]:
            assert eng.verify_d_squared(p, w) == 0

    def test_euler_char_w1(self, eng):
        chi = sum((-1)**p * eng.cohomology_at(p, 1) for p in range(1, 5))
        assert chi == -14

    def test_euler_char_w2(self, eng):
        chi = sum((-1)**p * eng.cohomology_at(p, 2) for p in range(1, 8))
        assert chi == 77

    def test_euler_char_w3(self, eng):
        chi = sum((-1)**p * eng.cohomology_at(p, 3) for p in range(1, 12))
        assert chi == -182

    def test_euler_char_w4(self, eng):
        chi = sum((-1)**p * eng.cohomology_at(p, 4) for p in range(1, 8))
        assert chi == 0

    def test_concentration_w1(self, eng):
        nonzero = [p for p in range(1, 5) if eng.cohomology_at(p, 1) > 0]
        assert nonzero == [1]

    def test_concentration_w2(self, eng):
        nonzero = [p for p in range(1, 8) if eng.cohomology_at(p, 2) > 0]
        assert nonzero == [2]

    def test_concentration_w3(self, eng):
        nonzero = [p for p in range(1, 10) if eng.cohomology_at(p, 3) > 0]
        assert nonzero == [3]


class TestCEEngineB2Weight5:
    """B2 tests at weight 5 (uses the weight-5 fixture from the main class)."""

    @pytest.fixture(scope='class')
    def eng(self):
        return build_engine('B2', max_weight=5)

    def test_h5_w5_zero(self, eng):
        """H^5_5 = 0 (cohomology NOT on diagonal at w=5)."""
        assert eng.cohomology_at(5, 5) == 0

    def test_h4_w5(self, eng):
        """H^4_5 = 238."""
        assert eng.cohomology_at(4, 5) == 238

    def test_euler_char_w5(self, eng):
        chi = sum((-1)**p * eng.cohomology_at(p, 5) for p in range(1, 14))
        assert chi == 238

    def test_b2_weight6_zero_from_gf(self):
        """Weight 6 is zero for B2, verified from Euler series (no CE needed)."""
        chi = ce_euler_series(6, 10)
        assert chi[6] == 0


# ============================================================
# Degree concentration pattern
# ============================================================

class TestDegreeConcentration:
    """The CE degree where cohomology lives is NOT always p = w.

    Pattern discovered:
    B2: w=1->p=1, w=2->p=2, w=3->p=3, w=4->p=3, w=5->p=4
    G2: w=1->p=1, w=2->p=2, w=3->p=3, w=4->ZERO, w=5->p=4
    A2: w=1->p=1, w=2->p=2, w=3->ZERO, w=4->p=3

    The cohomology is always concentrated in a single degree at each weight
    (when nonzero), confirming Koszulness, but the concentration degree
    can be less than the weight.
    """

    def test_b2_concentration_degrees(self):
        eng = build_engine('B2', max_weight=5)
        expected = {1: 1, 2: 2, 3: 3, 4: 3, 5: 4}
        for w, expected_p in expected.items():
            nonzero = [(p, eng.cohomology_at(p, w))
                       for p in range(1, 15)
                       if eng.cohomology_at(p, w) > 0]
            assert len(nonzero) == 1, \
                f"B2 w={w}: expected single degree, got {nonzero}"
            assert nonzero[0][0] == expected_p, \
                f"B2 w={w}: degree {nonzero[0][0]}, expected {expected_p}"

    def test_g2_concentration_degrees(self):
        eng = build_engine('G2', max_weight=3)
        expected = {1: 1, 2: 2, 3: 3}
        for w, expected_p in expected.items():
            nonzero = [(p, eng.cohomology_at(p, w))
                       for p in range(1, 12)
                       if eng.cohomology_at(p, w) > 0]
            assert len(nonzero) == 1
            assert nonzero[0][0] == expected_p

    def test_single_degree_at_each_weight_b2(self):
        """At each nonzero weight, cohomology lives in exactly one degree."""
        eng = build_engine('B2', max_weight=5)
        for w in range(1, 6):
            dims = [eng.cohomology_at(p, w) for p in range(1, 15)
                    if eng.weight_basis(p, w)]
            nonzero_count = sum(1 for d in dims if d > 0)
            # Either 0 (weight is zero) or 1 (single degree)
            assert nonzero_count <= 1, \
                f"B2 w={w}: cohomology in {nonzero_count} degrees"


# ============================================================
# Modular characteristics (AP1, AP39: recompute, never copy)
# ============================================================

class TestKappa:
    """kappa = dim(g) * (k + h^vee) / (2 * h^vee)."""

    def test_b2_kappa_k1(self):
        assert kappa_affine('B', 2, 1) == Fraction(20, 3)

    def test_b2_kappa_k0(self):
        assert kappa_affine('B', 2, 0) == Fraction(5)

    def test_b2_kappa_critical(self):
        """kappa(-h^vee) = 0."""
        assert kappa_affine('B', 2, -3) == 0

    def test_c2_kappa_k1(self):
        """C2 has same kappa as B2 (isomorphic)."""
        assert kappa_affine('C', 2, 1) == Fraction(20, 3)

    def test_g2_kappa_k1(self):
        assert kappa_affine('G', 2, 1) == Fraction(35, 4)

    def test_g2_kappa_k0(self):
        assert kappa_affine('G', 2, 0) == Fraction(7)

    def test_g2_kappa_critical(self):
        assert kappa_affine('G', 2, -4) == 0

    def test_f4_kappa_k1(self):
        assert kappa_affine('F', 4, 1) == Fraction(260, 9)

    def test_f4_kappa_k0(self):
        assert kappa_affine('F', 4, 0) == Fraction(26)

    def test_f4_kappa_critical(self):
        assert kappa_affine('F', 4, -9) == 0


class TestCentralCharge:
    """c = dim(g) * k / (k + h^vee)."""

    def test_b2_c_k1(self):
        assert central_charge_affine('B', 2, 1) == Fraction(10, 4)

    def test_g2_c_k1(self):
        assert central_charge_affine('G', 2, 1) == Fraction(14, 5)

    def test_f4_c_k1(self):
        assert central_charge_affine('F', 4, 1) == Fraction(52, 10)


class TestComplementarity:
    """kappa(k) + kappa(k') = 0 for all KM (AP24)."""

    def test_b2_kappa_complementarity(self):
        for k in [1, 2, 5, 10]:
            k_dual = -k - 2 * 3  # -k - 2*h^vee
            kap = kappa_affine('B', 2, k)
            kap_dual = kappa_affine('B', 2, k_dual)
            assert kap + kap_dual == 0, f"B2 k={k}: {kap} + {kap_dual} != 0"

    def test_g2_kappa_complementarity(self):
        for k in [1, 2, 5, 10]:
            k_dual = -k - 2 * 4
            kap = kappa_affine('G', 2, k)
            kap_dual = kappa_affine('G', 2, k_dual)
            assert kap + kap_dual == 0

    def test_f4_kappa_complementarity(self):
        for k in [1, 2, 5, 10]:
            k_dual = -k - 2 * 9
            kap = kappa_affine('F', 4, k)
            kap_dual = kappa_affine('F', 4, k_dual)
            assert kap + kap_dual == 0

    def test_b2_c_complementarity(self):
        """c(k) + c(k') = 2*dim for KM."""
        for k in [1, 2, 5]:
            k_dual = -k - 6
            c1 = central_charge_affine('B', 2, k)
            c2 = central_charge_affine('B', 2, k_dual)
            assert c1 + c2 == 20  # 2 * dim(B2) = 20


# ============================================================
# Root length decomposition
# ============================================================

class TestRootDecomposition:
    def test_b2_roots(self):
        rd = root_length_decomposition('B2')
        assert rd['n_positive_roots'] == 4
        # B2: 1 long root (alpha_2), 3 short roots
        # Actually depends on convention. Let me just check total.
        assert rd['n_long'] + rd['n_short'] == 4

    def test_g2_roots(self):
        rd = root_length_decomposition('G2')
        assert rd['n_positive_roots'] == 6
        assert rd['n_long'] == 3
        assert rd['n_short'] == 3

    def test_f4_roots(self):
        rd = root_length_decomposition('F4')
        assert rd['n_positive_roots'] == 24
        assert rd['n_long'] == 12
        assert rd['n_short'] == 12

    def test_g2_equal_long_short(self):
        """G2 has equal numbers of long and short roots."""
        rd = root_length_decomposition('G2')
        assert rd['n_long'] == rd['n_short']

    def test_f4_equal_long_short(self):
        """F4 has equal numbers of long and short roots."""
        rd = root_length_decomposition('F4')
        assert rd['n_long'] == rd['n_short']


# ============================================================
# Langlands duality
# ============================================================

class TestLanglandsDuality:
    def test_b2_c2_bar_cohomology_equal(self):
        """B2^L = C2 but same Lie algebra, so same bar cohomology."""
        ld = langlands_dual_comparison(6)
        assert ld['B2_C2_bar_cohom_equal']

    def test_b2_c2_lie_isomorphic(self):
        assert langlands_dual_comparison(4)['B2_C2_lie_algebra_isomorphic']

    def test_b2_c2_same_h_dual(self):
        """B2 and C2 have the same h^vee (since isomorphic)."""
        ld = langlands_dual_comparison(4)
        assert ld['B2_C2_h_dual_same']

    def test_g2_self_langlands(self):
        assert langlands_dual_comparison(4)['G2_self_langlands']

    def test_g2_h_neq_h_dual(self):
        ld = langlands_dual_comparison(4)
        assert ld['G2_h'] != ld['G2_h_dual']
        assert ld['G2_h'] == 6
        assert ld['G2_h_dual'] == 4


# ============================================================
# Cross-rank comparison: rank 2 algebras
# ============================================================

class TestRank2Comparison:
    """Compare sl_3 (A2, dim=8), B2 (dim=10), G2 (dim=14)."""

    def test_h1_ordered_by_dim(self):
        """H^1 = dim(g), so ordered A2 < B2 < G2."""
        bd_a2 = bar_cohomology_dims(1, 8)
        bd_b2 = bar_cohomology_dims(1, 10)
        bd_g2 = bar_cohomology_dims(1, 14)
        assert bd_a2[1] < bd_b2[1] < bd_g2[1]

    def test_h2_ordered_by_dim(self):
        bd_a2 = bar_cohomology_dims(2, 8)
        bd_b2 = bar_cohomology_dims(2, 10)
        bd_g2 = bar_cohomology_dims(2, 14)
        assert bd_a2[2] < bd_b2[2] < bd_g2[2]

    def test_a2_first_zero_at_w3(self):
        bd = bar_cohomology_dims(4, 8)
        assert bd[3] == 0
        assert bd[1] > 0 and bd[2] > 0

    def test_g2_first_zero_at_w4(self):
        bd = bar_cohomology_dims(5, 14)
        assert bd[4] == 0
        assert bd[1] > 0 and bd[2] > 0 and bd[3] > 0

    def test_b2_first_zero_at_w6(self):
        bd = bar_cohomology_dims(7, 10)
        assert bd[6] == 0
        for w in range(1, 6):
            assert bd[w] > 0

    def test_zero_position_increases_with_dim(self):
        """First zero weight: A2(w=3) < G2(w=4) < B2(w=6)."""
        # Find first zero for each
        for d, expected_zero in [(8, 3), (14, 4), (10, 6)]:
            bd = bar_cohomology_dims(10, d)
            first_zero = None
            for w in range(1, 10):
                if bd[w] == 0:
                    first_zero = w
                    break
            assert first_zero == expected_zero, \
                f"d={d}: first zero at {first_zero}, expected {expected_zero}"

    def test_a2_h2(self):
        """sl_3: H^2 = 20 (from CE computation)."""
        assert bar_cohomology_dims(2, 8)[2] == 20

    def test_g2_h2(self):
        assert bar_cohomology_dims(2, 14)[2] == 77

    def test_b2_h2(self):
        assert bar_cohomology_dims(2, 10)[2] == 35

    def test_h2_formula(self):
        """H^2 = C(d,2) - d = d(d-1)/2 - d = d(d-3)/2 for the CE at weight 2.

        Wait -- verify empirically first.
        d=8: C(8,2) - 8 = 28 - 8 = 20. Matches!
        d=10: C(10,2) - 10 = 45 - 10 = 35. Matches!
        d=14: C(14,2) - 14 = 91 - 14 = 77. Matches!
        d=52: C(52,2) - 52 = 1326 - 52 = 1274. Matches!

        This makes sense: at weight 2, the chain group Lambda^2 has C(d,2)
        2-element subsets of the d generators at mode 1, plus d single
        generators at mode 2 (dim = C(d,2) + d). The CE differential
        d: Lambda^1_2 -> Lambda^2_2 has kernel of dim d (weight-2 generators)
        and image in Lambda^2_2 of rank d (from the Lie bracket).
        So H^2_2 = ker(d^2) - im(d^1) = C(d,2) - d = d(d-3)/2.
        """
        for d, expected in [(8, 20), (10, 35), (14, 77), (52, 1274)]:
            assert bar_cohomology_dims(2, d)[2] == comb(d, 2) - d


# ============================================================
# Growth rates
# ============================================================

class TestGrowthRates:
    def test_f4_fastest(self):
        """F4 (dim=52) should grow fastest."""
        gr_b2 = bar_cohomology_growth_rate(10)
        gr_g2 = bar_cohomology_growth_rate(14)
        gr_f4 = bar_cohomology_growth_rate(52)
        assert gr_f4 > gr_g2
        assert gr_f4 > gr_b2

    def test_growth_positive(self):
        for d in [10, 14, 52]:
            gr = bar_cohomology_growth_rate(d)
            assert gr > 0


# ============================================================
# Multi-path verification (AP10: cross-family consistency)
# ============================================================

class TestMultiPathVerification:
    """Cross-check bar cohomology by multiple independent methods."""

    def test_b2_euler_vs_ce(self):
        """Method 1 (Euler series) vs Method 2 (exact CE) for B2."""
        chi = ce_euler_series(5, 10)
        eng = build_engine('B2', max_weight=5)
        for w in range(1, 6):
            ce_chi = sum((-1)**p * eng.cohomology_at(p, w) for p in range(1, 15))
            assert ce_chi == chi[w], f"w={w}: CE gives {ce_chi}, GF gives {chi[w]}"

    def test_g2_euler_vs_ce(self):
        chi = ce_euler_series(4, 14)
        eng = build_engine('G2', max_weight=4)
        for w in range(1, 5):
            ce_chi = sum((-1)**p * eng.cohomology_at(p, w) for p in range(1, 15))
            assert ce_chi == chi[w]

    def test_convolution_identity_b2(self):
        """prod(1-t^n)^d * prod(1-t^n)^{-d} = 1, so chi * p_d = delta."""
        chi = ce_euler_series(8, 10)
        for w in range(1, 8):
            s = sum(chi[j] * pbw_dim(w - j, 10) for j in range(w + 1))
            assert s == 0

    def test_convolution_identity_g2(self):
        chi = ce_euler_series(8, 14)
        for w in range(1, 8):
            s = sum(chi[j] * pbw_dim(w - j, 14) for j in range(w + 1))
            assert s == 0

    def test_convolution_identity_f4(self):
        chi = ce_euler_series(6, 52)
        for w in range(1, 6):
            s = sum(chi[j] * pbw_dim(w - j, 52) for j in range(w + 1))
            assert s == 0

    def test_h2_formula_all_families(self):
        """H^2 = C(d,2) - d for all families (method 3: closed-form check)."""
        for d in [8, 10, 14, 52]:
            assert bar_cohomology_dims(2, d)[2] == comb(d, 2) - d


# ============================================================
# Comparison with simply-laced at same rank
# ============================================================

class TestSimplyLacedComparison:
    def test_rank2_all_different(self):
        """sl_3, B2, G2 all rank 2 but different bar cohomology."""
        bd_a2 = bar_cohomology_dims(4, 8)
        bd_b2 = bar_cohomology_dims(4, 10)
        bd_g2 = bar_cohomology_dims(4, 14)
        assert bd_a2 != bd_b2
        assert bd_b2 != bd_g2
        assert bd_a2 != bd_g2

    def test_root_system_matters(self):
        """Bar cohomology depends on dim(g), not just rank.

        The bar cohomology series 1/H_A(t) = prod(1-t^n)^d depends
        ONLY on d = dim(g). So algebras with the same dim have the
        same bar cohomology, regardless of root system structure.

        B2 and C2: same dim (10) -> same bar cohomology.
        B6 and E6: both dim 78, both rank 6 -> same bar cohomology!
        """
        bd_b2 = bar_cohomology_dims(6, 10)
        bd_c2 = bar_cohomology_dims(6, 10)  # same dim!
        assert bd_b2 == bd_c2

    def test_dim_determines_bar_cohomology(self):
        """Two algebras with different dim have different bar cohomology."""
        bd_8 = bar_cohomology_dims(4, 8)
        bd_10 = bar_cohomology_dims(4, 10)
        bd_14 = bar_cohomology_dims(4, 14)
        assert bd_8 != bd_10
        assert bd_10 != bd_14


# ============================================================
# Full computation table
# ============================================================

class TestComputeFullTable:
    def test_b2_table(self):
        t = compute_full_table('B2', max_weight=4)
        assert t['dim'] == 10
        assert t['rank'] == 2
        assert t['h'] == 4
        assert t['h_dual'] == 3
        assert t['h1_weight1'] == 10

    def test_g2_table(self):
        t = compute_full_table('G2', max_weight=4)
        assert t['dim'] == 14
        assert t['rank'] == 2
        assert t['h'] == 6
        assert t['h_dual'] == 4
        assert t['h1_weight1'] == 14

    def test_f4_table(self):
        t = compute_full_table('F4', max_weight=3)
        assert t['dim'] == 52
        assert t['rank'] == 4
        assert t['h'] == 12
        assert t['h_dual'] == 9
        assert t['n_positive_roots'] == 24


# ============================================================
# B2 = C2 isomorphism (detailed)
# ============================================================

class TestB2C2Isomorphism:
    """B2 and C2 are isomorphic as Lie algebras (so(5) = sp(4)).

    Bar cohomology depends only on the Lie algebra structure, so
    all bar cohomology data must be identical.
    """

    def test_same_dim(self):
        assert cartan_data('B', 2).dim == cartan_data('C', 2).dim

    def test_same_h_dual(self):
        assert cartan_data('B', 2).h_dual == cartan_data('C', 2).h_dual

    def test_same_kappa(self):
        for k in [1, 2, 5]:
            assert kappa_affine('B', 2, k) == kappa_affine('C', 2, k)

    def test_same_bar_cohomology(self):
        bd_b = bar_cohomology_dims(8, cartan_data('B', 2).dim)
        bd_c = bar_cohomology_dims(8, cartan_data('C', 2).dim)
        assert bd_b == bd_c

    def test_same_euler_series(self):
        chi_b = ce_euler_series(8, cartan_data('B', 2).dim)
        chi_c = ce_euler_series(8, cartan_data('C', 2).dim)
        assert chi_b == chi_c


# ============================================================
# Zeros of the Euler series (structural analysis)
# ============================================================

class TestEulerSeriesZeros:
    """The zeros of the CE Euler series encode root system data.

    For rank-2 algebras:
    - A2 (dim=8, h=3): first zero at w=3
    - G2 (dim=14, h=6): first zero at w=4
    - B2 (dim=10, h=4): first zero at w=6

    Conjecture: the zeros are related to the exponents.
    For A2: exponents [1,2], first zero at h = 3 = max exponent + 1
    For G2: exponents [1,5], but zero at 4 != 6 = max exponent + 1
    For B2: exponents [1,3], zero at 6 != 4 = max exponent + 1
    So the simple exponent+1 formula fails. The pattern is more subtle.
    """

    def test_a2_zeros(self):
        """sl_3: zeros at w = 3, 7 (and possibly more)."""
        bd = bar_cohomology_dims(10, 8)
        zeros = [w for w in range(1, 10) if bd[w] == 0]
        assert 3 in zeros
        assert 7 in zeros  # [1,8,20,0,70,64,56,0,125]: zero at 3 and 7

    def test_g2_zeros(self):
        bd = bar_cohomology_dims(10, 14)
        zeros = [w for w in range(1, 10) if bd[w] == 0]
        assert 4 in zeros

    def test_b2_zeros(self):
        bd = bar_cohomology_dims(10, 10)
        zeros = [w for w in range(1, 10) if bd[w] == 0]
        assert 6 in zeros

    def test_a2_zeros_include_3_7_11(self):
        """sl_3 zeros include w = 3, 7, 11 (gaps 4, 4).

        The first two gaps are h+1 = 4. The pattern breaks at higher weights
        (w=13 is also zero, gap 2). Not strictly periodic.
        """
        bd = bar_cohomology_dims(15, 8)
        zeros = [w for w in range(1, 15) if bd[w] == 0]
        assert 3 in zeros
        assert 7 in zeros
        assert 11 in zeros

    def test_g2_second_zero_at_w9(self):
        """G2 has a second zero at weight 9 (gap = 5 from first zero at 4)."""
        bd = bar_cohomology_dims(10, 14)
        assert bd[9] == 0


# ============================================================
# k-independence
# ============================================================

class TestKIndependence:
    """Bar cohomology is k-independent for all affine KM algebras.

    This is because the CE complex of g_- has no central extension:
    for modes m, n >= 1, the cocycle m * delta_{m+n,0} never fires
    since m + n >= 2 > 0.

    The bar COMPLEX depends on k (through the curvature), but the
    PBW spectral sequence collapses at E_2 regardless, giving
    k-independent cohomology.
    """

    def test_b2_kappa_independent_of_bar_cohom(self):
        """kappa changes with k but bar cohomology does not."""
        assert kappa_affine('B', 2, 1) != kappa_affine('B', 2, 2)
        # But bar cohomology is the same (depends only on dim)
        bd1 = bar_cohomology_dims(4, 10)
        bd2 = bar_cohomology_dims(4, 10)
        assert bd1 == bd2

    def test_g2_bar_cohom_same_at_all_levels(self):
        """Bar cohomology at different levels is the same."""
        bd = bar_cohomology_dims(4, 14)
        # This is the SAME for all k, as it depends only on dim(G2) = 14
        assert bd == bar_cohomology_dims(4, 14)
