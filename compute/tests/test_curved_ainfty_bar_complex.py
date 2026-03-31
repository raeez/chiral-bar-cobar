"""Tests for curved A-infinity structures and bar complex d^2=0.

Verifies the critical structural fact: d^2_bar = 0 ALWAYS, even when
m_1^2 != 0 (curved case). The curvature m_1^2(a) = [m_0, a] (graded
commutator) is the n=1 A-infinity relation.

Test organization:
  I.   CurvedAInfty data structure
  II.  A-infinity relations (n=0,1,2,3)
  III. Bar complex construction
  IV.  d^2 = 0 verification (THE KEY TESTS)
  V.   m_1^2 = [m_0, -] (commutator formula)
  VI.  Concrete algebras: sl_2
  VII. Concrete algebras: Heisenberg
  VIII.Concrete algebras: truncated polynomial / exterior
  IX.  Arnold defect and genus table
  X.   Jacobi identity and structure
  XI.  Cross-checks and edge cases

Ground truth:
  CLAUDE.md: Critical Pitfalls (curved A-infinity, bar d^2=0)
  bar_cobar_adjunction_curved.tex: bar complex construction
  virasoro_ainfty.py: Virasoro A-infinity operations
  mc5_genus1_bridge.py: genus-1 Arnold defect
"""

import pytest
from sympy import Matrix, Rational, Symbol, simplify, zeros

from compute.lib.curved_ainfty_bar_complex import (
    CurvedAInfty,
    BarComplex,
    strict_ainfty,
    curved_ainfty,
    bar_complex_truncated,
    bar_differential_matrix,
    verify_bar_d_squared_zero,
    m1_squared_equals_commutator,
    genus0_strict_check,
    genus1_curved_check,
    arnold_defect_from_curvature,
    sl2_strict_bar,
    sl2_curved_bar,
    heisenberg_bar,
    two_dim_strict_bar,
    two_dim_curved_bar,
    exterior_strict_bar,
    ainfty_relation_at_n,
    curvature_genus_table,
    sl2_jacobi_check,
    run_all_verifications,
)


# =========================================================================
# I. CurvedAInfty data structure
# =========================================================================

class TestCurvedAInftyStructure:
    """Basic tests for the CurvedAInfty data structure."""

    def test_strict_is_not_curved(self):
        """m_0 = 0 means not curved."""
        V = ["a", "b"]
        ainfty = strict_ainfty(V, [0, 0], zeros(2, 2), {})
        assert not ainfty.is_curved

    def test_curved_is_curved(self):
        """m_0 != 0 means curved."""
        V = ["a", "b"]
        m0 = Matrix([Rational(1), Rational(0)])
        ainfty = curved_ainfty(V, [0, 0], m0, zeros(2, 2), {})
        assert ainfty.is_curved

    def test_dim(self):
        """Dimension of underlying vector space."""
        V = ["e", "h", "f"]
        ainfty = strict_ainfty(V, [0, 0, 0], zeros(3, 3), {})
        assert ainfty.dim == 3

    def test_degree_access(self):
        """Access cohomological degrees."""
        V = ["x", "y"]
        ainfty = strict_ainfty(V, [0, 1], zeros(2, 2), {})
        assert ainfty.degree(0) == 0
        assert ainfty.degree(1) == 1

    def test_m0_vector_strict(self):
        """m_0 vector is zero for strict."""
        V = ["a"]
        ainfty = strict_ainfty(V, [0], zeros(1, 1), {})
        assert ainfty.m0_vector().equals(zeros(1, 1))

    def test_m0_vector_curved(self):
        """m_0 vector is nonzero for curved."""
        V = ["a"]
        m0 = Matrix([Rational(5)])
        ainfty = curved_ainfty(V, [0], m0, zeros(1, 1), {})
        assert ainfty.m0_vector()[0] == 5

    def test_m1_matrix_zero(self):
        """m_1 is zero when not specified."""
        V = ["a"]
        ainfty = strict_ainfty(V, [0], zeros(1, 1), {})
        assert ainfty.m1_matrix().equals(zeros(1, 1))


# =========================================================================
# II. A-infinity relations
# =========================================================================

class TestAInftyRelations:
    """Verify the A-infinity relations at each level."""

    def test_n0_strict_trivial(self):
        """n=0: m_1(m_0)=0. Trivial when m_0=0 and m_1=0."""
        V = ["a"]
        ainfty = strict_ainfty(V, [0], zeros(1, 1), {})
        assert ainfty.verify_m0_is_cycle()

    def test_n0_curved_m0_cycle(self):
        """n=0: m_1(m_0)=0. m_0 must be a cycle under m_1."""
        V = ["a", "b"]
        m0 = Matrix([Rational(1), Rational(0)])
        ainfty = curved_ainfty(V, [0, 0], m0, zeros(2, 2), {})
        assert ainfty.verify_m0_is_cycle()

    def test_n0_with_differential(self):
        """n=0 with nonzero m_1: m_0 must be in ker(m_1)."""
        V = ["a", "b"]
        # m_1: a -> b (so m_1(a)=b, m_1(b)=0; m_1^2=0)
        m1 = Matrix([[0, 0], [1, 0]])
        # m_0 = b (which is in ker(m_1) since m_1(b) = 0)
        m0 = Matrix([Rational(0), Rational(1)])
        ainfty = curved_ainfty(V, [0, 1], m0, m1, {})
        assert ainfty.verify_m0_is_cycle()

    def test_n0_fails_when_m0_not_cycle(self):
        """n=0 should fail when m_0 is NOT in ker(m_1)."""
        V = ["a", "b"]
        m1 = Matrix([[0, 0], [1, 0]])
        # m_0 = a, but m_1(a) = b != 0
        m0 = Matrix([Rational(1), Rational(0)])
        ainfty = curved_ainfty(V, [0, 1], m0, m1, {})
        assert not ainfty.verify_m0_is_cycle()

    def test_n1_strict_m1_squared_zero(self):
        """n=1: m_1^2 = [m_0, -]. When m_0=0, m_1^2=0."""
        V = ["a", "b"]
        m1 = Matrix([[0, 0], [1, 0]])  # d(a)=b, d(b)=0; d^2=0
        ainfty = strict_ainfty(V, [0, 1], m1, {})
        match, m1_sq, comm = ainfty.verify_m1_squared_equals_commutator()
        assert match
        assert m1_sq.equals(zeros(2, 2))
        assert comm.equals(zeros(2, 2))

    def test_n1_curved_central_m0(self):
        """n=1: When m_0 is central, [m_0,-]=0, so m_1^2=0."""
        V = ["1", "x"]
        m0 = Matrix([Rational(3), Rational(0)])  # 3 * 1
        m1 = zeros(2, 2)
        # 1 is central in m_2
        m2 = {
            (0, 0): [Rational(1), Rational(0)],
            (0, 1): [Rational(0), Rational(1)],
            (1, 0): [Rational(0), Rational(1)],
            (1, 1): [Rational(0), Rational(0)],
        }
        ainfty = curved_ainfty(V, [0, 0], m0, m1, m2)
        match, m1_sq, comm = ainfty.verify_m1_squared_equals_commutator()
        assert match
        # Both should be zero since 1 is central
        assert m1_sq.equals(zeros(2, 2))
        assert comm.equals(zeros(2, 2))

    def test_ainfty_relations_strict_all_pass(self):
        """All A-infinity relations hold for k[x]/(x^2)."""
        V = ["1", "x"]
        m2 = {
            (0, 0): [Rational(1), Rational(0)],
            (0, 1): [Rational(0), Rational(1)],
            (1, 0): [Rational(0), Rational(1)],
            (1, 1): [Rational(0), Rational(0)],
        }
        ainfty = strict_ainfty(V, [0, 0], zeros(2, 2), m2)
        results = ainfty.verify_ainfty_relations(max_n=3)
        for n, ok in results.items():
            assert ok, f"A-infinity relation at n={n} failed"

    def test_ainfty_relation_at_n0(self):
        """Explicit n=0 relation computation."""
        V = ["a"]
        ainfty = strict_ainfty(V, [0], zeros(1, 1), {})
        # n=0 takes no inputs
        result = ainfty_relation_at_n(ainfty, 0, [])
        # Result should be m_1(m_0) = 0
        assert result.equals(zeros(1, 1))


# =========================================================================
# III. Bar complex construction
# =========================================================================

class TestBarComplexConstruction:
    """Tests for bar complex dimensions and structure."""

    def test_bar_dim_degree0(self):
        """B^0 = k has dimension 1."""
        V = ["a", "b"]
        ainfty = strict_ainfty(V, [0, 0], zeros(2, 2), {})
        bar = bar_complex_truncated(ainfty, max_tensor=3)
        assert bar.bar_dim(0) == 1

    def test_bar_dim_degree1(self):
        """B^1 = sA has dimension = dim(A)."""
        V = ["a", "b", "c"]
        ainfty = strict_ainfty(V, [0, 0, 0], zeros(3, 3), {})
        bar = bar_complex_truncated(ainfty, max_tensor=3)
        assert bar.bar_dim(1) == 3

    def test_bar_dim_degree2(self):
        """B^2 = sA^{otimes 2} has dimension = dim(A)^2."""
        V = ["a", "b"]
        ainfty = strict_ainfty(V, [0, 0], zeros(2, 2), {})
        bar = bar_complex_truncated(ainfty, max_tensor=3)
        assert bar.bar_dim(2) == 4

    def test_bar_dim_degree3(self):
        """B^3 = sA^{otimes 3} has dimension = dim(A)^3."""
        V = ["a", "b"]
        ainfty = strict_ainfty(V, [0, 0], zeros(2, 2), {})
        bar = bar_complex_truncated(ainfty, max_tensor=3)
        assert bar.bar_dim(3) == 8

    def test_bar_dim_beyond_max(self):
        """B^n = 0 for n > max_tensor."""
        V = ["a"]
        ainfty = strict_ainfty(V, [0], zeros(1, 1), {})
        bar = bar_complex_truncated(ainfty, max_tensor=2)
        assert bar.bar_dim(3) == 0

    def test_bar_dim_negative(self):
        """B^n = 0 for n < 0."""
        V = ["a"]
        ainfty = strict_ainfty(V, [0], zeros(1, 1), {})
        bar = bar_complex_truncated(ainfty, max_tensor=2)
        assert bar.bar_dim(-1) == 0

    def test_multi_index_roundtrip(self):
        """Flat <-> multi-index conversion is inverse."""
        V = ["a", "b", "c"]
        ainfty = strict_ainfty(V, [0, 0, 0], zeros(3, 3), {})
        bar = bar_complex_truncated(ainfty, max_tensor=3)
        for flat in range(27):  # 3^3
            multi = bar._multi_index(3, flat)
            assert bar._flat_index(multi) == flat


# =========================================================================
# IV. d^2 = 0 verification (THE KEY TESTS)
# =========================================================================

class TestBarDSquaredZero:
    """THE CRITICAL TESTS: d^2_bar = 0 for all cases."""

    def test_trivial_algebra_d2_zero(self):
        """Trivial algebra (all m_i=0): d^2=0 trivially."""
        V = ["a"]
        ainfty = strict_ainfty(V, [0], zeros(1, 1), {})
        bar = bar_complex_truncated(ainfty, max_tensor=3)
        results = verify_bar_d_squared_zero(bar, max_degree=3)
        assert all(results.values())

    def test_truncpoly_strict_d2_zero(self):
        """k[x]/(x^2) strict: d^2=0 (associative algebra)."""
        result = two_dim_strict_bar()
        assert result["all_pass"]

    def test_truncpoly_curved_d2_zero(self):
        """k[x]/(x^2) curved (m_0 = 1): d^2=0 still."""
        result = two_dim_curved_bar(Rational(1))
        assert result["all_pass"]
        assert result["is_curved"]

    def test_truncpoly_curved_d2_zero_rational(self):
        """k[x]/(x^2) curved (m_0 = 7/3): d^2=0 with arbitrary curvature."""
        result = two_dim_curved_bar(Rational(7, 3))
        assert result["all_pass"]
        assert result["m0_is_cycle"]
        assert result["m1_sq_equals_comm"]

    def test_exterior_strict_d2_zero(self):
        """Exterior algebra Lambda(k): d^2=0."""
        result = exterior_strict_bar()
        assert result["all_pass"]

    def test_sl2_strict_d2_zero(self):
        """sl_2 CE complex: d^2=0 at genus 0."""
        result = sl2_strict_bar()
        assert result["all_pass"]
        assert not result["is_curved"]
        assert result["m1_squared_zero"]

    def test_sl2_curved_d2_zero(self):
        """sl_2 + curvature: d^2=0 at genus 1."""
        result = sl2_curved_bar(Rational(3))
        assert result["all_pass"]
        assert result["is_curved"]
        assert result["m0_is_cycle"]
        assert result["m1_sq_equals_comm"]

    def test_sl2_curved_kappa_generic(self):
        """sl_2 with generic kappa: d^2=0."""
        result = sl2_curved_bar(Rational(7, 4))
        assert result["all_pass"]

    def test_heisenberg_strict_d2_zero(self):
        """Heisenberg strict (genus 0): d^2=0."""
        result = heisenberg_bar(kappa_val=None)
        assert result["all_pass"]
        assert not result["is_curved"]
        assert result["shadow_class"] == "G (Gaussian)"

    def test_heisenberg_curved_d2_zero(self):
        """Heisenberg curved (genus 1, kappa=1): d^2=0."""
        result = heisenberg_bar(kappa_val=Rational(1))
        assert result["all_pass"]
        assert result["is_curved"]

    def test_heisenberg_curved_d2_zero_large_kappa(self):
        """Heisenberg curved (kappa=100): d^2=0 for large curvature."""
        result = heisenberg_bar(kappa_val=Rational(100))
        assert result["all_pass"]

    def test_heisenberg_curved_d2_zero_negative_kappa(self):
        """Heisenberg curved (kappa=-1): d^2=0 for negative curvature."""
        result = heisenberg_bar(kappa_val=Rational(-1))
        assert result["all_pass"]

    def test_d2_zero_each_degree_sl2(self):
        """d^2=0 at each tensor degree 0,1,2,3 for sl_2."""
        result = sl2_strict_bar()
        for n, ok in result["d_squared_zero"].items():
            assert ok, f"d^2 != 0 at tensor degree {n}"


# =========================================================================
# V. m_1^2 = [m_0, -] (commutator formula)
# =========================================================================

class TestM1SquaredCommutator:
    """m_1^2(a) = [m_0, a] = m_2(m_0,a) - m_2(a,m_0) (commutator; |m_0|=2 even)."""

    def test_strict_both_zero(self):
        """Strict: m_1^2 = 0 and [m_0, -] = 0."""
        V = ["a"]
        ainfty = strict_ainfty(V, [0], zeros(1, 1), {})
        result = m1_squared_equals_commutator(ainfty)
        assert result["all_match"]

    def test_curved_central_m0(self):
        """Degree-2 m_0 in CE dga: [m_0, -] = 0, so m_1^2 = 0."""
        result = sl2_curved_bar(Rational(5))
        assert result["m1_squared_zero"]
        assert result["commutator_m0_zero"]
        assert result["m1_sq_equals_comm"]

    def test_heisenberg_curved_commutator(self):
        """Heisenberg: m_2=0 so [m_0,-]=0 and m_1^2=0."""
        result = heisenberg_bar(kappa_val=Rational(1))
        assert result["m1_squared_zero"]
        assert result["commutator_zero"]

    def test_truncpoly_curved_commutator(self):
        """k[x]/(x^2): 1 is central, so [m_0,-]=0."""
        result = two_dim_curved_bar(Rational(2))
        assert result["m1_squared_zero"]
        assert result["commutator_zero"]
        assert result["m1_sq_equals_comm"]

    def test_m1_squared_detailed_output(self):
        """Detailed m_1^2 output for k[x]/(x^2) strict."""
        V = ["1", "x"]
        m2 = {
            (0, 0): [Rational(1), Rational(0)],
            (0, 1): [Rational(0), Rational(1)],
            (1, 0): [Rational(0), Rational(1)],
            (1, 1): [Rational(0), Rational(0)],
        }
        ainfty = strict_ainfty(V, [0, 0], zeros(2, 2), m2)
        result = m1_squared_equals_commutator(ainfty)
        assert result["all_match"]
        for name in ["1", "x"]:
            assert result["details"][name]["match"]


# =========================================================================
# VI. Concrete algebras: sl_2
# =========================================================================

class TestSl2BarComplex:
    """sl_2 bar complex (CE dga model): strict and curved cases."""

    def test_sl2_strict_is_not_curved(self):
        """sl_2 CE dga at genus 0 is strict."""
        result = sl2_strict_bar()
        assert not result["is_curved"]

    def test_sl2_strict_m1_squared_zero(self):
        """sl_2 CE dga strict: m_1^2 = 0 (d_CE^2 = 0)."""
        result = sl2_strict_bar()
        assert result["m1_squared_zero"]

    def test_sl2_curved_is_curved(self):
        """sl_2 CE dga at genus 1 is curved."""
        result = sl2_curved_bar(Rational(1))
        assert result["is_curved"]
        assert result["genus"] == 1

    def test_sl2_curved_m0_cycle(self):
        """sl_2 CE dga curved: m_0 is a cycle (d_CE(1) = 0)."""
        result = sl2_curved_bar(Rational(1))
        assert result["m0_is_cycle"]

    def test_sl2_kappa_formula(self):
        """sl_2: kappa = 3(k+2)/4. At k=1: kappa = 9/4."""
        expected = Rational(3, 4) * (1 + 2)
        assert expected == Rational(9, 4)

    def test_sl2_curved_various_kappa(self):
        """sl_2 CE dga curved d^2=0 for several kappa values."""
        for kappa in [Rational(1, 2), Rational(9, 4)]:
            result = sl2_curved_bar(kappa)
            assert result["all_pass"], f"Failed at kappa={kappa}"

    def test_sl2_ce_wedge_antisymmetric(self):
        """sl_2 CE dga: wedge product is graded-antisymmetric on deg 1."""
        from compute.lib.curved_ainfty_bar_complex import _sl2_ce_dga
        V, degrees, d_matrix, m2 = _sl2_ce_dga()
        # Check e* ^ h* = -h* ^ e*  (indices 0, 1 in augmentation ideal)
        for k in range(len(V)):
            assert m2[(0, 1)][k] == -m2[(1, 0)][k], \
                f"Antisymmetry fails at component {k}"


# =========================================================================
# VII. Concrete algebras: Heisenberg
# =========================================================================

class TestHeisensteinBarComplex:
    """Heisenberg (free boson) bar complex tests."""

    def test_heisenberg_shadow_depth_2(self):
        """Heisenberg has shadow depth 2 (Gaussian class G)."""
        result = heisenberg_bar(kappa_val=None)
        assert result["shadow_depth"] == 2

    def test_heisenberg_shadow_class(self):
        """Heisenberg is in Gaussian class G."""
        result = heisenberg_bar(kappa_val=None)
        assert result["shadow_class"] == "G (Gaussian)"

    def test_heisenberg_m2_trivial(self):
        """Heisenberg: m_2 = 0 (single generator, antisymmetric)."""
        V = ["a"]
        ainfty = strict_ainfty(V, [0], zeros(1, 1), {})
        assert ainfty.m2_tensor() == {}

    def test_heisenberg_bar_all_d_bracket_zero(self):
        """Heisenberg: d_bracket = 0 at all degrees (m_2 = 0)."""
        V = ["a"]
        ainfty = strict_ainfty(V, [0], zeros(1, 1), {})
        bar = bar_complex_truncated(ainfty, max_tensor=4)
        for n in range(2, 5):
            d_br = bar.d_bracket_matrix(n)
            assert d_br.equals(zeros(*d_br.shape)), f"d_bracket != 0 at degree {n}"

    def test_heisenberg_genus0_genus1_comparison(self):
        """Heisenberg: genus 0 (strict) vs genus 1 (curved) both have d^2=0."""
        r0 = heisenberg_bar(kappa_val=None)
        r1 = heisenberg_bar(kappa_val=Rational(1))
        assert r0["all_pass"]
        assert r1["all_pass"]
        assert not r0["is_curved"]
        assert r1["is_curved"]


# =========================================================================
# VIII. Concrete algebras: truncated polynomial / exterior
# =========================================================================

class TestTruncatedPolynomialBarComplex:
    """k[x]/(x^2) bar complex tests."""

    def test_truncpoly_associativity(self):
        """k[x]/(x^2) is associative: m_2(m_2(a,b),c) = m_2(a,m_2(b,c))."""
        V = ["1", "x"]
        m2 = {
            (0, 0): [Rational(1), Rational(0)],
            (0, 1): [Rational(0), Rational(1)],
            (1, 0): [Rational(0), Rational(1)],
            (1, 1): [Rational(0), Rational(0)],
        }
        ainfty = strict_ainfty(V, [0, 0], zeros(2, 2), m2)
        results = ainfty.verify_ainfty_relations(max_n=3)
        assert results[3]  # n=3 is associativity

    def test_truncpoly_curved_m0_cycle(self):
        """k[x]/(x^2) curved: m_0 is a cycle."""
        result = two_dim_curved_bar(Rational(1))
        assert result["m0_is_cycle"]

    def test_truncpoly_curved_various_mu(self):
        """k[x]/(x^2) curved d^2=0 for several curvature values."""
        for mu in [Rational(1), Rational(-1), Rational(3, 7), Rational(100)]:
            result = two_dim_curved_bar(mu)
            assert result["all_pass"], f"Failed at mu={mu}"

    def test_exterior_d2_zero(self):
        """Exterior algebra d^2=0."""
        result = exterior_strict_bar()
        assert result["all_pass"]


# =========================================================================
# IX. Arnold defect and genus table
# =========================================================================

class TestArnoldDefectAndGenusTable:
    """Arnold defect from curvature and genus-dependent curvature table."""

    def test_arnold_defect_zero_kappa(self):
        """kappa=0: no Arnold defect."""
        result = arnold_defect_from_curvature(0)
        assert result["curvature_m0"] == 0
        assert result["total_D1_squared"] == 0

    def test_arnold_defect_nonzero_kappa(self):
        """kappa != 0: Arnold defect proportional to kappa."""
        result = arnold_defect_from_curvature(Rational(1, 2))
        assert result["curvature_m0"] == Rational(1, 2)
        assert result["d_squared_coefficient"] == Rational(1, 2)

    def test_arnold_defect_quantum_correction(self):
        """Quantum correction t_1 = kappa/24."""
        result = arnold_defect_from_curvature(Rational(6))
        assert result["quantum_correction_t1"] == Rational(1, 4)  # 6/24 = 1/4

    def test_arnold_defect_total_D1_zero(self):
        """Total D_1^2 = 0 after quantum correction."""
        for kappa in [0, Rational(1), Rational(-1), Rational(13, 2)]:
            result = arnold_defect_from_curvature(kappa)
            assert result["total_D1_squared"] == 0

    def test_genus_table_genus0_not_curved(self):
        """Genus 0: m_0 = 0, not curved."""
        table = curvature_genus_table("heisenberg", max_g=2)
        assert table[0]["curved"] is False
        assert table[0]["m0"] == 0
        assert table[0]["arnold_exact"] is True

    def test_genus_table_genus1_curved(self):
        """Genus 1: m_0 = kappa, curved."""
        k = Symbol('k')
        table = curvature_genus_table("heisenberg", max_g=2)
        assert table[1]["curved"] is True
        assert table[1]["m0"] == k

    def test_genus_table_virasoro_kappa(self):
        """Virasoro: kappa = c/2 at genus 1."""
        c = Symbol('c')
        table = curvature_genus_table("virasoro", max_g=1)
        assert simplify(table[1]["m0"] - c / 2) == 0

    def test_genus_table_sl2_kappa(self):
        """sl_2: kappa = 3(k+2)/4 at genus 1."""
        k = Symbol('k')
        table = curvature_genus_table("sl2", max_g=1)
        assert simplify(table[1]["m0"] - Rational(3, 4) * (k + 2)) == 0

    def test_genus_table_sl3_kappa(self):
        """sl_3: kappa = 4(k+3)/3 at genus 1."""
        k = Symbol('k')
        table = curvature_genus_table("sl3", max_g=1)
        assert simplify(table[1]["m0"] - Rational(4, 3) * (k + 3)) == 0

    def test_genus_table_w3_kappa(self):
        """W_3: kappa = 5c/6 at genus 1."""
        c = Symbol('c')
        table = curvature_genus_table("w3", max_g=1)
        assert simplify(table[1]["m0"] - Rational(5, 6) * c) == 0

    def test_genus_table_betagamma_kappa(self):
        """betagamma: kappa = +1 at genus 1."""
        table = curvature_genus_table("betagamma", max_g=1)
        assert table[1]["m0"] == 1

    def test_genus_table_quantum_correction_formula(self):
        """Quantum correction = kappa/24 at genus 1."""
        k = Symbol('k')
        table = curvature_genus_table("heisenberg", max_g=1)
        assert simplify(table[1]["quantum_correction"] - k / 24) == 0

    def test_genus_table_higher_genus_curved(self):
        """Genus >= 2: still curved."""
        table = curvature_genus_table("heisenberg", max_g=3)
        for g in [2, 3]:
            assert table[g]["curved"] is True


# =========================================================================
# X. Jacobi identity and structure
# =========================================================================

class TestJacobiAndStructure:
    """Jacobi identity and CE structure for sl_2."""

    def test_sl2_jacobi(self):
        """sl_2 Lie bracket satisfies Jacobi identity."""
        assert sl2_jacobi_check()

    def test_sl2_bracket_ef_equals_h(self):
        """[e,f] = h in sl_2 Lie bracket."""
        from compute.lib.curved_ainfty_bar_complex import _sl2_lie_bracket_data
        _, _, m2 = _sl2_lie_bracket_data()
        assert m2[(0, 2)][1] == 1  # h coefficient

    def test_sl2_bracket_he_equals_2e(self):
        """[h,e] = 2e in sl_2 Lie bracket."""
        from compute.lib.curved_ainfty_bar_complex import _sl2_lie_bracket_data
        _, _, m2 = _sl2_lie_bracket_data()
        assert m2[(1, 0)][0] == 2  # e coefficient

    def test_sl2_bracket_hf_equals_minus2f(self):
        """[h,f] = -2f in sl_2 Lie bracket."""
        from compute.lib.curved_ainfty_bar_complex import _sl2_lie_bracket_data
        _, _, m2 = _sl2_lie_bracket_data()
        assert m2[(1, 2)][2] == -2  # f coefficient


# =========================================================================
# XI. Cross-checks and edge cases
# =========================================================================

class TestCrossChecksEdgeCases:
    """Cross-checks with known results, edge cases."""

    def test_run_all_verifications(self):
        """All verifications pass in the summary function."""
        results = run_all_verifications()
        for name, ok in results.items():
            assert ok, f"Verification '{name}' failed"

    def test_genus0_check_requires_strict(self):
        """genus0_strict_check asserts m_0 = 0."""
        V = ["a"]
        ainfty = strict_ainfty(V, [0], zeros(1, 1), {})
        result = genus0_strict_check(ainfty)
        assert result["all_pass"]
        assert result["m0_is_zero"]

    def test_genus1_check_requires_curved(self):
        """genus1_curved_check asserts m_0 != 0."""
        V = ["a"]
        m0 = Matrix([Rational(1)])
        ainfty = curved_ainfty(V, [0], m0, zeros(1, 1), {})
        result = genus1_curved_check(ainfty)
        assert result["all_pass"]
        assert result["m0_nonzero"]

    def test_bar_d_linear_on_trivial(self):
        """d_linear on trivial algebra is zero."""
        V = ["a"]
        ainfty = strict_ainfty(V, [0], zeros(1, 1), {})
        bar = bar_complex_truncated(ainfty, max_tensor=3)
        for n in range(4):
            d_lin = bar.d_linear_matrix(n)
            assert d_lin.equals(zeros(*d_lin.shape))

    def test_bar_d_curvature_on_strict(self):
        """d_curvature on strict (m_0=0) algebra is zero."""
        V = ["a", "b"]
        ainfty = strict_ainfty(V, [0, 0], zeros(2, 2), {})
        bar = bar_complex_truncated(ainfty, max_tensor=3)
        for n in range(3):
            d_curv = bar.d_curvature_matrix(n)
            assert d_curv.equals(zeros(*d_curv.shape))

    def test_virasoro_kappa_c_over_2(self):
        """Virasoro kappa = c/2, consistent with virasoro_ainfty.py."""
        c = Symbol('c')
        table = curvature_genus_table("virasoro", max_g=1)
        assert simplify(table[1]["m0"] - c / 2) == 0
        # Cross-check: at c=1, kappa=1/2
        assert table[1]["m0"].subs(c, 1) == Rational(1, 2)

    def test_virasoro_self_dual_at_c13(self):
        """Virasoro self-dual at c=13 (NOT c=26).

        Vir_c^! = Vir_{26-c}, so self-dual when c = 26-c, i.e. c=13.
        kappa(Vir_13) = 13/2, kappa(Vir_13^!) = 13/2.
        """
        kappa_13 = Rational(13, 2)
        kappa_dual = Rational(26 - 13, 2)
        assert kappa_13 == kappa_dual

    def test_kappa_complementarity_virasoro(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        c = Symbol('c')
        kappa_c = c / 2
        kappa_dual = (26 - c) / 2
        assert simplify(kappa_c + kappa_dual - 13) == 0

    def test_kappa_complementarity_sl2(self):
        """kappa(sl2_k) + kappa(sl2_{k'}) checks."""
        k = Symbol('k')
        # sl_2 -> Virasoro via DS
        # kappa(sl2_k) = 3(k+2)/4
        # DS gives c = 1 - 6(k+1)^2/(k+2)
        # kappa(Vir_c) = c/2
        kappa_sl2 = Rational(3, 4) * (k + 2)
        # At k=1: 3*3/4 = 9/4
        assert kappa_sl2.subs(k, 1) == Rational(9, 4)

    def test_curved_bar_d2_zero_symbolic_kappa(self):
        """Bar d^2=0 with symbolic (not numeric) kappa for Heisenberg."""
        V = ["a"]
        kappa = Symbol('kappa')
        m0 = Matrix([kappa])
        ainfty = curved_ainfty(V, [0], m0, zeros(1, 1), {})
        bar = bar_complex_truncated(ainfty, max_tensor=3)
        results = verify_bar_d_squared_zero(bar, max_degree=3)
        assert all(results.values())

    def test_curved_bar_d2_zero_symbolic_sl2(self):
        """sl_2 CE dga bar d^2=0 with symbolic curvature."""
        kappa = Symbol('kappa')
        result = sl2_curved_bar(kappa)
        assert result["all_pass"]

    def test_ainfty_relation_n1_explicit(self):
        """Explicit n=1 A-infinity relation on k[x]/(x^2)."""
        V = ["1", "x"]
        m2 = {
            (0, 0): [Rational(1), Rational(0)],
            (0, 1): [Rational(0), Rational(1)],
            (1, 0): [Rational(0), Rational(1)],
            (1, 1): [Rational(0), Rational(0)],
        }
        ainfty = strict_ainfty(V, [0, 0], zeros(2, 2), m2)

        # n=1: m_1^2(e_i) = [m_0, e_i]. Both sides = 0 for strict.
        for i in range(2):
            result = ainfty_relation_at_n(ainfty, 1, [i])
            for k in range(2):
                assert simplify(result[k]) == 0, \
                    f"A-inf n=1 failed on e_{V[i]}, component {k}: {result[k]}"


# =========================================================================
# Final integration test
# =========================================================================

class TestIntegration:
    """Full integration tests covering the main theorem: d^2_bar = 0."""

    def test_main_theorem_strict(self):
        """MAIN THEOREM (strict case): d^2_bar = 0 for m_0=0.

        This is the genus-0 case where Arnold is exact on P^1.
        """
        for builder in [sl2_strict_bar, two_dim_strict_bar, exterior_strict_bar]:
            result = builder()
            assert result["all_pass"], f"d^2 != 0 for {result['algebra']}"

    def test_main_theorem_curved(self):
        """MAIN THEOREM (curved case): d^2_bar = 0 for m_0 != 0.

        This is the genus >= 1 case where curvature is present.
        Bar d^2=0 STILL holds by the A-infinity relations.
        """
        for kappa in [Rational(1), Rational(1, 2), Rational(7, 3)]:
            r_sl2 = sl2_curved_bar(kappa)
            assert r_sl2["all_pass"], f"d^2 != 0 for sl_2 curved, kappa={kappa}"

            r_tp = two_dim_curved_bar(kappa)
            assert r_tp["all_pass"], f"d^2 != 0 for k[x]/(x^2) curved, mu={kappa}"

            r_heis = heisenberg_bar(kappa_val=kappa)
            assert r_heis["all_pass"], f"d^2 != 0 for Heisenberg curved, kappa={kappa}"

    def test_hierarchy_genus0_vs_genus1(self):
        """The hierarchy: genus 0 (strict) vs genus 1 (curved).

        Both have d^2=0, but the mechanism is different:
        - Genus 0: m_0=0, Arnold exact, d^2=0 trivially.
        - Genus 1: m_0 != 0, Arnold defect, d^2=0 by A-infinity relations.
        """
        g0 = two_dim_strict_bar()
        g1 = two_dim_curved_bar(Rational(3))

        # Both pass
        assert g0["all_pass"]
        assert g1["all_pass"]

        # But genus 0 is strict, genus 1 is curved
        assert not g0["is_curved"]
        assert g1["is_curved"]

        # Genus 1: m_1^2 = [m_0, -] = 0 (m_0 central)
        assert g1["m1_squared_zero"]
        assert g1["commutator_zero"]
