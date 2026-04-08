r"""Tests for bar_differential_sl2_matrices_engine.py.

Verifies explicit bar differential matrices for V_k(sl_2) at each
(CE degree p, conformal weight h).  All computations use exact rational
arithmetic (Fraction).

MULTI-PATH VERIFICATION:
  Path 1: d^2 = 0 as exact matrix identity (chain-level Borcherds identity)
  Path 2: Cohomology dimensions match the proved formula dim H^n = 2n+1
  Path 3: Cohomology weight concentration at h = n(n+1)/2
  Path 4: Explicit matrix entries verified against hand computation
  Path 5: Cross-check with bar_cohomology_sl2_explicit_engine.py
  Path 6: Chain group dimensions match comp:sl2-ce-verification
  Path 7: k-independence (all matrix entries are integers)
  Path 8: Desuspension sign verification (AP45)
  Path 9: Euler characteristic consistency

SIGN CONVENTION:
  AP45: |s^{-1}v| = |v| - 1. Desuspension LOWERS degree by 1.
  The CE differential sign: (-1)^{pos_c + pos_beta + pos_gamma}.

References:
  comp:sl2-ce-verification (bar_complex_tables.tex)
  lem:bar-deg2-symmetric-square (landscape_census.tex)
  CLAUDE.md: sl_2 bar H^2 = 5 (not 6; Riordan WRONG at n=2)
"""

import pytest
from fractions import Fraction

from compute.lib.bar_differential_sl2_matrices_engine import (
    BarDifferentialSl2Engine,
    DIM_SL2,
    SL2_BRACKET,
    SL2_KILLING,
    SL2_NAMES,
    LoopGenerator,
    compute_differential_matrix,
    verify_d_squared_all,
    h1_cocycle_representatives,
    h2_cocycle_representatives_weight3,
    weight1_arity2_verification,
    sl2_bracket,
    sl2_killing,
    _frac,
    _frac_array,
    _frac_matmul,
)


# ============================================================
# Fixtures
# ============================================================

@pytest.fixture(scope='module')
def engine_w6():
    """Engine with max_weight=6 for fast tests."""
    return BarDifferentialSl2Engine(max_weight=6)


@pytest.fixture(scope='module')
def engine_w8():
    """Engine with max_weight=8 for medium tests."""
    return BarDifferentialSl2Engine(max_weight=8)


@pytest.fixture(scope='module')
def engine_w10():
    """Engine with max_weight=10 for extended tests."""
    return BarDifferentialSl2Engine(max_weight=10)


# ============================================================
# 1. sl_2 Lie algebra data
# ============================================================

class TestSl2LieAlgebra:
    """Verify sl_2 structure constants and Killing form."""

    def test_bracket_ef_is_h(self):
        """[e, f] = h."""
        br = sl2_bracket(0, 2)
        assert br == {1: Fraction(1)}

    def test_bracket_fe_is_minus_h(self):
        """[f, e] = -h."""
        br = sl2_bracket(2, 0)
        assert br == {1: Fraction(-1)}

    def test_bracket_he_is_2e(self):
        """[h, e] = 2e."""
        br = sl2_bracket(1, 0)
        assert br == {0: Fraction(2)}

    def test_bracket_eh_is_minus_2e(self):
        """[e, h] = -2e."""
        br = sl2_bracket(0, 1)
        assert br == {0: Fraction(-2)}

    def test_bracket_hf_is_minus_2f(self):
        """[h, f] = -2f."""
        br = sl2_bracket(1, 2)
        assert br == {2: Fraction(-2)}

    def test_bracket_fh_is_2f(self):
        """[f, h] = 2f."""
        br = sl2_bracket(2, 1)
        assert br == {2: Fraction(2)}

    def test_bracket_ee_vanishes(self):
        """[e, e] = 0."""
        assert sl2_bracket(0, 0) == {}

    def test_bracket_hh_vanishes(self):
        """[h, h] = 0."""
        assert sl2_bracket(1, 1) == {}

    def test_bracket_ff_vanishes(self):
        """[f, f] = 0."""
        assert sl2_bracket(2, 2) == {}

    def test_jacobi_identity(self):
        """Jacobi identity: [e, [h, f]] + [h, [f, e]] + [f, [e, h]] = 0.

        Checks that the structure constants satisfy the Jacobi identity
        for all triples of basis elements.
        """
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    # [a, [b,c]] + [b, [c,a]] + [c, [a,b]] = 0
                    total = {}
                    for (x, y, z) in [(a, b, c), (b, c, a), (c, a, b)]:
                        br_yz = sl2_bracket(y, z)
                        for d, coeff_d in br_yz.items():
                            br_xd = sl2_bracket(x, d)
                            for e, coeff_e in br_xd.items():
                                total[e] = total.get(e, Fraction(0)) + coeff_d * coeff_e
                    for val in total.values():
                        assert val == Fraction(0), \
                            f"Jacobi failed for ({a},{b},{c})"

    def test_killing_form_symmetric(self):
        """kappa(a,b) = kappa(b,a)."""
        for a in range(3):
            for b in range(3):
                assert sl2_killing(a, b) == sl2_killing(b, a)

    def test_killing_ef(self):
        """kappa(e,f) = 1."""
        assert sl2_killing(0, 2) == Fraction(1)

    def test_killing_hh(self):
        """kappa(h,h) = 2."""
        assert sl2_killing(1, 1) == Fraction(2)

    def test_killing_ee_vanishes(self):
        """kappa(e,e) = 0."""
        assert sl2_killing(0, 0) == Fraction(0)

    def test_killing_invariance(self):
        """kappa([a,b], c) + kappa(b, [a,c]) = 0 (ad-invariance)."""
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    # kappa([a,b], c) + kappa(b, [a,c]) = 0
                    total = Fraction(0)
                    br_ab = sl2_bracket(a, b)
                    for d, coeff in br_ab.items():
                        total += coeff * sl2_killing(d, c)
                    br_ac = sl2_bracket(a, c)
                    for d, coeff in br_ac.items():
                        total += coeff * sl2_killing(b, d)
                    assert total == Fraction(0), \
                        f"Invariance failed for ({a},{b},{c})"


# ============================================================
# 2. Chain group dimensions
# ============================================================

class TestChainDimensions:
    """Verify chain group dim Lambda^p(g_-^*)_h."""

    def test_weight_0(self, engine_w6):
        """Lambda^0_0 = 1, all others zero."""
        assert engine_w6.chain_dim(0, 0) == 1
        for p in range(1, 5):
            assert engine_w6.chain_dim(p, 0) == 0

    def test_weight_1(self, engine_w6):
        """Weight 1: Lambda^1_1 = 3, rest zero."""
        assert engine_w6.chain_dim(0, 1) == 0
        assert engine_w6.chain_dim(1, 1) == 3
        assert engine_w6.chain_dim(2, 1) == 0

    def test_weight_2(self, engine_w6):
        """Weight 2: L^1=3, L^2=3."""
        assert engine_w6.chain_dim(1, 2) == 3
        assert engine_w6.chain_dim(2, 2) == 3
        assert engine_w6.chain_dim(3, 2) == 0

    def test_weight_3(self, engine_w6):
        """Weight 3: L^1=3, L^2=9, L^3=1."""
        assert engine_w6.chain_dim(1, 3) == 3
        assert engine_w6.chain_dim(2, 3) == 9
        assert engine_w6.chain_dim(3, 3) == 1
        assert engine_w6.chain_dim(4, 3) == 0

    def test_weight_4(self, engine_w6):
        """Weight 4: L^1=3, L^2=12, L^3=9."""
        assert engine_w6.chain_dim(1, 4) == 3
        assert engine_w6.chain_dim(2, 4) == 12
        assert engine_w6.chain_dim(3, 4) == 9
        assert engine_w6.chain_dim(4, 4) == 0

    def test_weight_5(self, engine_w6):
        """Weight 5: L^1=3, L^2=18, L^3=18, L^4=3."""
        assert engine_w6.chain_dim(1, 5) == 3
        assert engine_w6.chain_dim(2, 5) == 18
        assert engine_w6.chain_dim(3, 5) == 18
        assert engine_w6.chain_dim(4, 5) == 3
        assert engine_w6.chain_dim(5, 5) == 0

    def test_weight_6(self, engine_w6):
        """Weight 6: L^1=3, L^2=21, L^3=37, L^4=12."""
        assert engine_w6.chain_dim(1, 6) == 3
        assert engine_w6.chain_dim(2, 6) == 21
        assert engine_w6.chain_dim(3, 6) == 37
        assert engine_w6.chain_dim(4, 6) == 12

    def test_weight_1_generators(self, engine_w6):
        """Weight-1 basis: (e_1, h_1, f_1) with flat indices (0, 1, 2)."""
        basis = engine_w6.weight_basis(1, 1)
        assert len(basis) == 3
        assert basis == [(0,), (1,), (2,)]

    def test_weight_2_degree_2_basis(self, engine_w6):
        """Lambda^2_2: three 2-subsets from {e_1, h_1, f_1}."""
        basis = engine_w6.weight_basis(2, 2)
        assert len(basis) == 3
        assert basis == [(0, 1), (0, 2), (1, 2)]

    def test_euler_char_weight_h(self, engine_w6):
        """Euler characteristic chi_h = sum (-1)^p dim L^p_h.

        Must equal sum (-1)^p dim H^p_h by d^2 = 0.
        """
        for h in range(7):
            chi_chain = sum((-1)**p * engine_w6.chain_dim(p, h) for p in range(h + 2))
            chi_coh = sum((-1)**p * engine_w6.cohomology_dim(p, h) for p in range(h + 2))
            assert chi_chain == chi_coh, \
                f"Euler char mismatch at weight {h}: {chi_chain} != {chi_coh}"


# ============================================================
# 3. d^2 = 0 as exact matrix identity
# ============================================================

class TestDSquaredZero:
    """Verify d_{CE}^2 = 0 at all (degree, weight) pairs.

    This is the chain-level Borcherds identity: the Jacobi identity
    for the loop algebra g_- implies d^2 = 0 on the CE complex.
    """

    @pytest.mark.parametrize('degree,weight', [
        (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
        (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
        (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
        (3, 5), (3, 6), (3, 7),
    ])
    def test_d_squared_zero_ce(self, engine_w8, degree, weight):
        """d^{p+1} o d^p = 0 exactly (all entries zero over Q)."""
        res = engine_w8.verify_d_squared_ce(degree, weight)
        assert res['d_squared_zero'], \
            f"d^2 != 0 at (p={degree}, h={weight}): {res.get('nonzero_entries', [])}"

    def test_d_squared_zero_all_low(self, engine_w6):
        """Systematic d^2 = 0 for all nontrivial (p, h) with h <= 6."""
        for h in range(1, 7):
            for p in range(h):
                src_dim = engine_w6.chain_dim(p, h)
                mid_dim = engine_w6.chain_dim(p + 1, h)
                tgt_dim = engine_w6.chain_dim(p + 2, h)
                if src_dim > 0 and mid_dim > 0 and tgt_dim > 0:
                    res = engine_w6.verify_d_squared_ce(p, h)
                    assert res['d_squared_zero'], \
                        f"d^2 != 0 at (p={p}, h={h})"

    def test_d_squared_zero_bar_direction(self, engine_w6):
        """d_bar^2 = 0 (transpose direction)."""
        for h in range(2, 7):
            for n in range(3, min(h + 1, 5)):
                res = engine_w6.verify_d_squared_bar(n, h)
                assert res['d_squared_zero'], \
                    f"d_bar^2 != 0 at (n={n}, h={h})"


# ============================================================
# 4. Explicit matrix entries (hand-verified)
# ============================================================

class TestExplicitMatrixEntries:
    """Verify specific matrix entries against hand computation."""

    def test_d_at_degree1_weight2_shape(self, engine_w6):
        """d: L^1_2 -> L^2_2 is a 3x3 matrix."""
        D = engine_w6.differential_matrix(1, 2)
        assert D.shape == (3, 3)

    def test_d_at_degree1_weight2_entries(self, engine_w6):
        """d: L^1_2 -> L^2_2 encodes the sl_2 Lie bracket.

        Source: [e_2, h_2, f_2]
        Target: [e_1^h_1, e_1^f_1, h_1^f_1]

        The matrix is:
            [-2,  0,  0]   d(e_2) = -2 * e_1^h_1
            [ 0,  1,  0]   d(h_2) =  1 * e_1^f_1
            [ 0,  0, -2]   d(f_2) = -2 * h_1^f_1

        These encode:
            [e, h] = -2e => d(e_2) involves e_1^h_1 with coeff -2
            [e, f] = h   => d(h_2) involves e_1^f_1 with coeff 1
            [h, f] = -2f => d(f_2) involves h_1^f_1 with coeff -2
        """
        D = engine_w6.differential_matrix(1, 2)
        # Row 0 (e_1^h_1), Col 0 (e_2)
        assert D[0, 0] == Fraction(-2)
        # Row 0, Col 1 (h_2)
        assert D[0, 1] == Fraction(0)
        # Row 0, Col 2 (f_2)
        assert D[0, 2] == Fraction(0)
        # Row 1 (e_1^f_1), Col 1 (h_2)
        assert D[1, 1] == Fraction(1)
        # Row 2 (h_1^f_1), Col 2 (f_2)
        assert D[2, 2] == Fraction(-2)
        # Off-diagonal zeros
        assert D[1, 0] == Fraction(0)
        assert D[1, 2] == Fraction(0)
        assert D[2, 0] == Fraction(0)
        assert D[2, 1] == Fraction(0)

    def test_d_at_degree1_weight2_rank(self, engine_w6):
        """rank(d: L^1_2 -> L^2_2) = 3 (full rank, isomorphism)."""
        D = engine_w6.differential_matrix(1, 2)
        assert engine_w6._exact_rank(D) == 3

    def test_d_at_degree1_weight3_shape(self, engine_w6):
        """d: L^1_3 -> L^2_3 is 9x3."""
        D = engine_w6.differential_matrix(1, 3)
        assert D.shape == (9, 3)

    def test_d_at_degree1_weight3_rank(self, engine_w6):
        """rank(d: L^1_3 -> L^2_3) = 3 (injective)."""
        D = engine_w6.differential_matrix(1, 3)
        assert engine_w6._exact_rank(D) == 3

    def test_d_at_degree1_weight3_specific_entries(self, engine_w6):
        """Verify specific entries of d: L^1_3 -> L^2_3.

        Source: [e_3, h_3, f_3]
        Target: [e1^e2, e1^h2, e1^f2, h1^e2, h1^h2, h1^f2, f1^e2, f1^h2, f1^f2]

        d(e_3): [h,e]=2e gives e_3. Which brackets produce e at mode 3?
        [(h,1),(e,2)] = 2*(e,3) and [(e,1),(h,2)] = -2*(e,3)
        and [(h,2),(e,1)] = 2*(e,3) and [(e,2),(h,1)] = -2*(e,3)
        In our table with i<j, the relevant brackets are:
        (0,1) = [e_1,h_1] at mode 2: not mode 3
        Actually (flat indices): e_1=0, h_1=1, f_1=2, e_2=3, h_2=4, f_2=5
        Brackets producing e_3 (flat=6): need (a,m)+(b,n) with m+n=3
        (0,4) = [e_1, h_2]: [e,h]=-2e => -2*e_3. delta=6, beta=0, gamma=4
        (1,3) = [h_1, e_2]: [h,e]=2e => 2*e_3. delta=6, beta=1, gamma=3
        """
        D = engine_w6.differential_matrix(1, 3)
        # d(e_3) = col 0
        # Target row for e_1^h_2 = (0, 4): that's row 1
        assert D[1, 0] == Fraction(-2)  # from [e_1, h_2]=-2e_3
        # Target row for h_1^e_2 = (1, 3): that's row 3
        assert D[3, 0] == Fraction(2)   # from [h_1, e_2]=2e_3

    def test_d_at_degree2_weight3_shape(self, engine_w6):
        """d: L^2_3 -> L^3_3 is 1x9."""
        D = engine_w6.differential_matrix(2, 3)
        assert D.shape == (1, 9)

    def test_d_at_degree2_weight3_rank(self, engine_w6):
        """rank(d: L^2_3 -> L^3_3) = 1."""
        D = engine_w6.differential_matrix(2, 3)
        assert engine_w6._exact_rank(D) == 1

    def test_d_at_degree2_weight3_entries(self, engine_w6):
        """d: L^2_3 -> L^3_3 has specific nonzero entries.

        Target: e_1^h_1^f_1
        Source: [e1^e2, e1^h2, e1^f2, h1^e2, h1^h2, h1^f2, f1^e2, f1^h2, f1^f2]

        Expected from engine output: [0, 0, 2, 0, 1, 0, 2, 0, 0]
        """
        D = engine_w6.differential_matrix(2, 3)
        expected = [0, 0, 2, 0, 1, 0, 2, 0, 0]
        for j in range(9):
            assert D[0, j] == Fraction(expected[j]), \
                f"Entry [0,{j}]: got {D[0, j]}, expected {expected[j]}"

    def test_d_squared_explicit_weight3(self, engine_w6):
        """d^2 = 0 at weight 3: d_2 o d_1 is the zero matrix.

        d_1: L^1_3 -> L^2_3 is 9x3
        d_2: L^2_3 -> L^3_3 is 1x9
        d_2 o d_1: L^1_3 -> L^3_3 is 1x3, should be zero.
        """
        D1 = engine_w6.differential_matrix(1, 3)
        D2 = engine_w6.differential_matrix(2, 3)
        prod = _frac_matmul(D2, D1)
        assert prod.shape == (1, 3)
        for j in range(3):
            assert prod[0, j] == Fraction(0), \
                f"d^2[0,{j}] = {prod[0, j]} != 0"

    def test_all_entries_integer(self, engine_w6):
        """All differential matrix entries are integers (k-independent)."""
        for h in range(1, 7):
            for p in range(min(h, 4)):
                D = engine_w6.differential_matrix(p, h)
                if D.size == 0:
                    continue
                for i in range(D.shape[0]):
                    for j in range(D.shape[1]):
                        assert D[i, j].denominator == 1, \
                            f"Non-integer at (p={p}, h={h})[{i},{j}]: {D[i, j]}"


# ============================================================
# 5. Cohomology dimensions
# ============================================================

class TestCohomologyDimensions:
    """Verify bar cohomology dimensions."""

    def test_h0_is_ground_field(self, engine_w6):
        """H^0 = 1 at weight 0, zero elsewhere."""
        assert engine_w6.cohomology_dim(0, 0) == 1
        for h in range(1, 7):
            assert engine_w6.cohomology_dim(0, h) == 0

    def test_h1_weight_1_equals_3(self, engine_w6):
        """H^1_1 = 3: the three sl_2 generators."""
        assert engine_w6.cohomology_dim(1, 1) == 3

    def test_h1_higher_weights_vanish(self, engine_w8):
        """H^1_h = 0 for h >= 2."""
        for h in range(2, 9):
            assert engine_w8.cohomology_dim(1, h) == 0

    def test_h1_total_equals_3(self, engine_w8):
        """Total dim H^1 = 3."""
        total = sum(engine_w8.cohomology_dim(1, h) for h in range(9))
        assert total == 3

    def test_h2_weight_2_equals_0(self, engine_w6):
        """H^2_2 = 0 (lem:bar-deg2-symmetric-square, correcting Riordan).

        d: L^1_2 -> L^2_2 has rank 3 = dim L^1_2 = dim L^2_2.
        So ker = 0 and H^2_2 = 0.
        """
        assert engine_w6.cohomology_dim(2, 2) == 0

    def test_h2_weight_3_equals_5(self, engine_w6):
        """H^2_3 = 5 (not 6 = Riordan R(5); CLAUDE.md Critical Pitfalls)."""
        assert engine_w6.cohomology_dim(2, 3) == 5

    def test_h2_total_equals_5(self, engine_w8):
        """Total dim H^2 = 5."""
        total = sum(engine_w8.cohomology_dim(2, h) for h in range(9))
        assert total == 5

    def test_h3_weight_6_equals_7(self, engine_w8):
        """H^3_6 = 7."""
        assert engine_w8.cohomology_dim(3, 6) == 7

    def test_h3_total_equals_7(self, engine_w8):
        """Total dim H^3 = 7."""
        total = sum(engine_w8.cohomology_dim(3, h) for h in range(9))
        assert total == 7

    def test_h4_weight_10_equals_9(self, engine_w10):
        """H^4_10 = 9."""
        assert engine_w10.cohomology_dim(4, 10) == 9

    def test_h4_total_equals_9(self, engine_w10):
        """Total dim H^4 = 9."""
        total = sum(engine_w10.cohomology_dim(4, h) for h in range(11))
        assert total == 9

    @pytest.mark.parametrize('n,expected', [
        (0, 1), (1, 3), (2, 5), (3, 7), (4, 9),
    ])
    def test_total_hn_equals_2n_plus_1(self, engine_w10, n, expected):
        """Total dim H^n = 2n + 1 (the (2n+1)-dim sl_2 representation)."""
        max_h = n * (n + 1) // 2 + 1
        total = sum(engine_w10.cohomology_dim(n, h)
                    for h in range(min(max_h, 11)))
        assert total == expected, f"H^{n} = {total}, expected {expected}"

    @pytest.mark.parametrize('n', [1, 2, 3, 4])
    def test_cohomology_weight_concentration(self, engine_w10, n):
        """H^n is concentrated at weight h = n(n+1)/2 (triangular number)."""
        target_weight = n * (n + 1) // 2
        if target_weight > 10:
            pytest.skip(f"Weight {target_weight} exceeds max_weight=10")
        for h in range(min(target_weight + 2, 11)):
            dim = engine_w10.cohomology_dim(n, h)
            if h == target_weight:
                assert dim == 2 * n + 1, \
                    f"H^{n}_{h} = {dim}, expected {2*n+1}"
            else:
                assert dim == 0, \
                    f"H^{n}_{h} = {dim}, expected 0"


# ============================================================
# 6. H^2 at weight 3: detailed verification
# ============================================================

class TestH2Weight3:
    """Detailed verification of the 5-dimensional H^2_3 space."""

    def test_chain_dims(self, engine_w6):
        """Chain dimensions at weight 3: L^1=3, L^2=9, L^3=1."""
        assert engine_w6.chain_dim(1, 3) == 3
        assert engine_w6.chain_dim(2, 3) == 9
        assert engine_w6.chain_dim(3, 3) == 1

    def test_ranks(self, engine_w6):
        """rank(d_1) = 3, rank(d_2) = 1."""
        D1 = engine_w6.differential_matrix(1, 3)
        D2 = engine_w6.differential_matrix(2, 3)
        assert engine_w6._exact_rank(D1) == 3
        assert engine_w6._exact_rank(D2) == 1

    def test_ker_im_dims(self, engine_w6):
        """ker(d_2) = 8, im(d_1) = 3, H^2 = 5."""
        D1 = engine_w6.differential_matrix(1, 3)
        D2 = engine_w6.differential_matrix(2, 3)
        ker_d2 = 9 - engine_w6._exact_rank(D2)
        im_d1 = engine_w6._exact_rank(D1)
        assert ker_d2 == 8
        assert im_d1 == 3
        assert ker_d2 - im_d1 == 5

    def test_five_cocycle_representatives(self, engine_w6):
        """There are exactly 5 linearly independent cocycle representatives."""
        reps = engine_w6.cohomology_representatives(2, 3)
        assert len(reps) == 5

    def test_cocycles_are_in_kernel(self, engine_w6):
        """Each representative is in ker(d_2)."""
        D2 = engine_w6.differential_matrix(2, 3)
        reps = engine_w6.cohomology_representatives(2, 3)
        for v in reps:
            image = _frac_matmul(D2, v.reshape(-1, 1))
            for i in range(image.shape[0]):
                assert image[i, 0] == Fraction(0)

    def test_cocycles_independent_modulo_image(self, engine_w6):
        """Representatives are linearly independent and not in im(d_1)."""
        D1 = engine_w6.differential_matrix(1, 3)
        reps = engine_w6.cohomology_representatives(2, 3)
        image_vecs = engine_w6._image_basis(D1)
        assert len(image_vecs) == 3
        # Reps are linearly independent (rank 5)
        reps_mat = _frac_array((5, 9))
        for i, v in enumerate(reps):
            for j in range(9):
                reps_mat[i, j] = v[j]
        assert engine_w6._exact_rank(reps_mat) == 5
        # Kernel has dimension 8 = 5 + 3
        D2 = engine_w6.differential_matrix(2, 3)
        ker_dim = 9 - engine_w6._exact_rank(D2)
        assert ker_dim == 8
        assert ker_dim == len(reps) + len(image_vecs)

    def test_convenience_function(self):
        """h2_cocycle_representatives_weight3() returns correct data."""
        data = h2_cocycle_representatives_weight3()
        assert data['H2_dim'] == 5
        assert data['rank_d1'] == 3
        assert data['rank_d2'] == 1
        assert data['ker_d2'] == 8
        assert len(data['cocycle_representatives']) == 5


# ============================================================
# 7. H^1 cocycle representatives
# ============================================================

class TestH1CocycleRepresentatives:
    """Verify H^1 representatives are the sl_2 generators."""

    def test_three_representatives_at_weight_1(self, engine_w6):
        """H^1 has 3 representatives, all at weight 1."""
        reps = engine_w6.cohomology_representatives(1, 1)
        assert len(reps) == 3

    def test_representatives_are_standard_basis(self, engine_w6):
        """The 3 representatives at weight 1 are e_1, h_1, f_1.

        Since Lambda^1_1 has no incoming differential (from Lambda^0_1=0)
        and the outgoing differential d: Lambda^1_1 -> Lambda^2_1 targets
        the zero space (Lambda^2_1=0), every element is a cocycle and
        the cohomology IS the chain space.
        """
        reps = engine_w6.cohomology_representatives(1, 1)
        # Check that they form a basis of the 3-dim space
        assert len(reps) == 3
        # Each should be a unit vector (standard basis)
        for idx, v in enumerate(reps):
            assert v[idx] == Fraction(1)
            for j in range(3):
                if j != idx:
                    assert v[j] == Fraction(0)

    def test_no_h1_at_higher_weights(self, engine_w8):
        """H^1_h = 0 for h >= 2."""
        for h in range(2, 9):
            reps = engine_w8.cohomology_representatives(1, h)
            assert len(reps) == 0, \
                f"H^1_{h} has {len(reps)} representatives (expected 0)"

    def test_convenience_function(self):
        """h1_cocycle_representatives returns correct data."""
        result = h1_cocycle_representatives(max_weight=6)
        assert 1 in result
        assert len(result[1]) == 3
        # Only weight 1 should have representatives
        for h in result:
            if h != 1:
                assert len(result[h]) == 0 or h not in result


# ============================================================
# 8. Weight-1 bracket verification
# ============================================================

class TestWeight1BracketVerification:
    """Verify that d at (p=1, h=2) reproduces the sl_2 Lie bracket."""

    def test_d_e2_is_minus2_e1_h1(self, engine_w6):
        """d(e_2) = -2 * (e_1 ^ h_1) from [e, h] = -2e."""
        D = engine_w6.differential_matrix(1, 2)
        assert D[0, 0] == Fraction(-2)  # coeff of e_1^h_1
        assert D[1, 0] == Fraction(0)   # coeff of e_1^f_1
        assert D[2, 0] == Fraction(0)   # coeff of h_1^f_1

    def test_d_h2_is_1_e1_f1(self, engine_w6):
        """d(h_2) = 1 * (e_1 ^ f_1) from [e, f] = h."""
        D = engine_w6.differential_matrix(1, 2)
        assert D[0, 1] == Fraction(0)
        assert D[1, 1] == Fraction(1)   # coeff of e_1^f_1
        assert D[2, 1] == Fraction(0)

    def test_d_f2_is_minus2_h1_f1(self, engine_w6):
        """d(f_2) = -2 * (h_1 ^ f_1) from [h, f] = -2f."""
        D = engine_w6.differential_matrix(1, 2)
        assert D[0, 2] == Fraction(0)
        assert D[1, 2] == Fraction(0)
        assert D[2, 2] == Fraction(-2)  # coeff of h_1^f_1

    def test_weight1_bracket_convenience(self):
        """weight1_arity2_verification returns correct data."""
        result = weight1_arity2_verification()
        mc = result['manual_check']
        assert mc['d_e2_on_e1h1'] == Fraction(-2)
        assert mc['d_h2_on_e1f1'] == Fraction(1)
        assert mc['d_f2_on_h1f1'] == Fraction(-2)


# ============================================================
# 9. Curvature / k-independence
# ============================================================

class TestCurvatureKIndependence:
    """Verify the central term (curvature) is absent from the CE differential.

    For modes m, n >= 1: m + n >= 2, so delta_{m+n,0} = 0.
    Consequence: all differential matrix entries are integers from sl_2
    structure constants, with NO dependence on the level k.
    """

    def test_curvature_check(self, engine_w6):
        """All matrix entries are integers (no k-dependence)."""
        result = engine_w6.curvature_central_term_check()
        for key, val in result['verification'].items():
            assert val['all_integer'], \
                f"Non-integer entry at {key}"
            assert val['k_independent']

    @pytest.mark.parametrize('weight', [1, 2, 3, 4, 5, 6])
    def test_integer_entries_by_weight(self, engine_w6, weight):
        """All entries integer at given weight, across degrees."""
        for p in range(min(weight, 5)):
            D = engine_w6.differential_matrix(p, weight)
            if D.size == 0:
                continue
            for i in range(D.shape[0]):
                for j in range(D.shape[1]):
                    assert D[i, j].denominator == 1, \
                        f"Non-integer at (p={p}, h={weight})[{i},{j}]: {D[i, j]}"


# ============================================================
# 10. Desuspension signs (AP45)
# ============================================================

class TestDesuspensionSigns:
    """Verify desuspension sign conventions from AP45.

    |s^{-1}v| = |v| - 1. For PBW states v with |v| = 0:
    |s^{-1}v| = -1, which is ODD.

    The Koszul sign for the bar differential contraction at position i
    (0-indexed) is (-1)^i. In the CE dual, this becomes the standard
    exterior algebra sign.
    """

    def test_sign_data_structure(self, engine_w6):
        """desuspension_signs returns well-formed data."""
        data = engine_w6.desuspension_signs(1, 2)
        assert 'elements' in data
        assert len(data['elements']) == 3  # three source elements

    def test_sign_consistency_degree1_weight2(self, engine_w6):
        """Signs at (p=1, h=2) are consistent with matrix entries."""
        data = engine_w6.desuspension_signs(1, 2)
        D = engine_w6.differential_matrix(1, 2)
        target_basis = engine_w6.weight_basis(2, 2)
        target_labels = [' ^ '.join(repr(engine_w6.generators[i]) for i in alpha)
                         for alpha in target_basis]

        for col, elem_data in enumerate(data['elements']):
            for term in elem_data['image_terms']:
                row = target_labels.index(term['target'])
                assert D[row, col] == term['coefficient'], \
                    f"Sign mismatch at col={col}, target={term['target']}"


# ============================================================
# 11. Cross-check with bar_cohomology_sl2_explicit_engine
# ============================================================

class TestCrossCheckWithCEEngine:
    """Cross-check against the existing bar_cohomology_sl2_explicit_engine.

    Both engines compute the same CE cohomology; verify dimensions match.
    """

    def test_cross_check_cohomology_dims(self, engine_w8):
        """Cohomology dimensions match across engines."""
        try:
            from compute.lib.bar_cohomology_sl2_explicit_engine import (
                BarCohomologySl2Engine as CEEngine,
            )
        except ImportError:
            pytest.skip("bar_cohomology_sl2_explicit_engine not available")

        ce_engine = CEEngine(max_weight=8)
        for h in range(9):
            for p in range(min(h + 2, 6)):
                dim_new = engine_w8.cohomology_dim(p, h)
                dim_ce = ce_engine.cohomology_dim(p, h)
                assert dim_new == dim_ce, \
                    f"Mismatch at (p={p}, h={h}): new={dim_new}, CE={dim_ce}"

    def test_cross_check_chain_dims(self, engine_w8):
        """Chain group dimensions match across engines."""
        try:
            from compute.lib.bar_cohomology_sl2_explicit_engine import (
                BarCohomologySl2Engine as CEEngine,
            )
        except ImportError:
            pytest.skip("bar_cohomology_sl2_explicit_engine not available")

        ce_engine = CEEngine(max_weight=8)
        for h in range(9):
            for p in range(min(h + 2, 6)):
                dim_new = engine_w8.chain_dim(p, h)
                dim_ce = ce_engine.chain_dim(p, h)
                assert dim_new == dim_ce, \
                    f"Chain dim mismatch at (p={p}, h={h}): new={dim_new}, CE={dim_ce}"

    def test_cross_check_d_squared(self, engine_w6):
        """d^2 = 0 verified in BOTH engines."""
        try:
            from compute.lib.bar_cohomology_sl2_explicit_engine import (
                BarCohomologySl2Engine as CEEngine,
            )
        except ImportError:
            pytest.skip("bar_cohomology_sl2_explicit_engine not available")

        ce_engine = CEEngine(max_weight=6)
        for h in range(1, 7):
            for p in range(min(h, 4)):
                new_ok = engine_w6.verify_d_squared_ce(p, h)['d_squared_zero']
                ce_ok = ce_engine.verify_d_squared(p, h)
                assert new_ok == ce_ok, \
                    f"d^2 mismatch at (p={p}, h={h})"


# ============================================================
# 12. Matrix rank table
# ============================================================

class TestDifferentialRanks:
    """Verify differential ranks determine cohomology correctly."""

    def test_rank_table_weight_2(self, engine_w6):
        """At weight 2: rank(d_0)=0, rank(d_1)=3."""
        D0 = engine_w6.differential_matrix(0, 2)
        D1 = engine_w6.differential_matrix(1, 2)
        assert engine_w6._exact_rank(D0) == 0
        assert engine_w6._exact_rank(D1) == 3

    def test_rank_table_weight_3(self, engine_w6):
        """At weight 3: rank(d_0)=0, rank(d_1)=3, rank(d_2)=1."""
        D0 = engine_w6.differential_matrix(0, 3)
        D1 = engine_w6.differential_matrix(1, 3)
        D2 = engine_w6.differential_matrix(2, 3)
        assert engine_w6._exact_rank(D0) == 0
        assert engine_w6._exact_rank(D1) == 3
        assert engine_w6._exact_rank(D2) == 1

    def test_rank_table_weight_4(self, engine_w6):
        """At weight 4: rank(d_1)=3, rank(d_2)=9."""
        D1 = engine_w6.differential_matrix(1, 4)
        D2 = engine_w6.differential_matrix(2, 4)
        assert engine_w6._exact_rank(D1) == 3
        assert engine_w6._exact_rank(D2) == 9

    def test_rank_implies_h2_weight4_zero(self, engine_w6):
        """At weight 4: H^2 = ker(d_2)/im(d_1) = (12-9)-(3) = 0."""
        dim_L2 = engine_w6.chain_dim(2, 4)
        rank_d1 = engine_w6._exact_rank(engine_w6.differential_matrix(1, 4))
        rank_d2 = engine_w6._exact_rank(engine_w6.differential_matrix(2, 4))
        ker_d2 = dim_L2 - rank_d2
        im_d1 = rank_d1
        assert ker_d2 - im_d1 == 0
        assert engine_w6.cohomology_dim(2, 4) == 0


# ============================================================
# 13. Exact arithmetic consistency
# ============================================================

class TestExactArithmetic:
    """Verify exact rational arithmetic is used throughout."""

    def test_frac_matmul_simple(self):
        """2x2 Fraction matrix multiplication."""
        A = _frac_array((2, 2))
        A[0, 0] = Fraction(1, 3)
        A[0, 1] = Fraction(1, 2)
        A[1, 0] = Fraction(2)
        A[1, 1] = Fraction(0)
        B = _frac_array((2, 1))
        B[0, 0] = Fraction(3)
        B[1, 0] = Fraction(4)
        C = _frac_matmul(A, B)
        assert C[0, 0] == Fraction(1, 3) * 3 + Fraction(1, 2) * 4  # 1 + 2 = 3
        assert C[1, 0] == Fraction(6)

    def test_kernel_basis_exact(self, engine_w6):
        """Kernel basis vectors have exact Fraction entries."""
        D = engine_w6.differential_matrix(2, 3)
        kernel = engine_w6._exact_kernel_basis(D)
        for v in kernel:
            for entry in v:
                assert isinstance(entry, Fraction)

    def test_no_floating_point(self, engine_w6):
        """No floating-point numbers in any matrix."""
        for h in range(1, 5):
            for p in range(min(h, 3)):
                D = engine_w6.differential_matrix(p, h)
                if D.size == 0:
                    continue
                for i in range(D.shape[0]):
                    for j in range(D.shape[1]):
                        assert isinstance(D[i, j], Fraction), \
                            f"Non-Fraction at (p={p},h={h})[{i},{j}]: {type(D[i,j])}"


# ============================================================
# 14. Convenience function tests
# ============================================================

class TestConvenienceFunctions:
    """Test the module-level convenience functions."""

    def test_compute_differential_matrix(self):
        """compute_differential_matrix returns correct data."""
        data = compute_differential_matrix(1, 2, max_weight=4)
        assert data['degree'] == 1
        assert data['weight'] == 2
        assert data['source_dim'] == 3
        assert data['target_dim'] == 3
        assert data['rank'] == 3
        assert len(data['matrix']) == 3
        assert len(data['matrix'][0]) == 3

    def test_verify_d_squared_all(self):
        """verify_d_squared_all returns all OK."""
        results = verify_d_squared_all(max_degree=3, max_weight=5)
        for key, res in results.items():
            assert res['d_squared_zero'], f"d^2 != 0 at {key}"

    def test_h1_cocycle_representatives(self):
        """h1_cocycle_representatives returns 3 at weight 1."""
        result = h1_cocycle_representatives(max_weight=4)
        assert 1 in result
        assert len(result[1]) == 3

    def test_h2_at_weight_3(self):
        """h2_cocycle_representatives_weight3 returns 5 representatives."""
        data = h2_cocycle_representatives_weight3()
        assert data['H2_dim'] == 5
        assert len(data['cocycle_representatives']) == 5


# ============================================================
# 15. Differential shape consistency
# ============================================================

class TestDifferentialShapes:
    """Verify differential matrices have correct shapes."""

    @pytest.mark.parametrize('degree,weight', [
        (0, 1), (0, 2), (0, 3),
        (1, 1), (1, 2), (1, 3), (1, 4),
        (2, 2), (2, 3), (2, 4), (2, 5),
        (3, 3), (3, 4), (3, 5), (3, 6),
    ])
    def test_shape_consistency(self, engine_w6, degree, weight):
        """Matrix shape = (target_dim, source_dim)."""
        D = engine_w6.differential_matrix(degree, weight)
        src = engine_w6.chain_dim(degree, weight)
        tgt = engine_w6.chain_dim(degree + 1, weight)
        if src == 0 or tgt == 0:
            assert D.size == 0 or D.shape == (tgt, src)
        else:
            assert D.shape == (tgt, src), \
                f"Shape {D.shape} != ({tgt}, {src}) at (p={degree}, h={weight})"

    @pytest.mark.parametrize('degree,weight', [
        (1, 2), (1, 3), (1, 4),
        (2, 3), (2, 4), (2, 5),
    ])
    def test_rank_bounded_by_min_dim(self, engine_w6, degree, weight):
        """rank(d) <= min(source_dim, target_dim)."""
        D = engine_w6.differential_matrix(degree, weight)
        if D.size == 0:
            return
        rank = engine_w6._exact_rank(D)
        assert rank <= min(D.shape[0], D.shape[1])


# ============================================================
# 16. Riordan number comparison
# ============================================================

class TestRiordanComparison:
    """Verify where H^n agrees/disagrees with Riordan numbers R(n+3)."""

    @staticmethod
    def riordan(n: int) -> int:
        """Riordan number R(n), OEIS A005043."""
        if n == 0:
            return 1
        if n == 1:
            return 0
        R = [1, 0]
        for k in range(2, n + 1):
            R.append(((k - 1) * (2 * R[k - 1] + 3 * R[k - 2])) // (k + 1))
        return R[n]

    def test_h1_agrees_with_riordan(self, engine_w8):
        """H^1 = 3 = R(4). Agreement."""
        assert engine_w8.total_cohomology(max_degree=1, max_weight=8)[1] == 3
        assert self.riordan(4) == 3

    def test_h2_disagrees_with_riordan(self, engine_w8):
        """H^2 = 5 != 6 = R(5). DISAGREEMENT (Riordan WRONG at n=2)."""
        assert engine_w8.total_cohomology(max_degree=2, max_weight=8)[2] == 5
        assert self.riordan(5) == 6
        assert 5 != 6  # explicit assertion of disagreement


# ============================================================
# 17. H^3 at weight 6: cocycle representatives
# ============================================================

class TestH3Weight6:
    """Verify 7 cocycle representatives at (degree=3, weight=6)."""

    def test_dim_equals_7(self, engine_w8):
        """dim H^3_6 = 7."""
        assert engine_w8.cohomology_dim(3, 6) == 7

    def test_seven_representatives(self, engine_w8):
        """7 linearly independent representatives."""
        reps = engine_w8.cohomology_representatives(3, 6)
        assert len(reps) == 7

    def test_representatives_in_kernel(self, engine_w8):
        """All representatives are in ker(d_3)."""
        D = engine_w8.differential_matrix(3, 6)
        reps = engine_w8.cohomology_representatives(3, 6)
        for v in reps:
            if D.size > 0:
                image = _frac_matmul(D, v.reshape(-1, 1))
                for i in range(image.shape[0]):
                    assert image[i, 0] == Fraction(0)

    def test_representatives_are_exact(self, engine_w8):
        """All entries are Fractions."""
        reps = engine_w8.cohomology_representatives(3, 6)
        for v in reps:
            for entry in v:
                assert isinstance(entry, Fraction)
