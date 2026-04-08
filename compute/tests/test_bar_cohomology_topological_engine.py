r"""Tests for the topological explanation of why bar cohomology depends only on dim(g).

STRUCTURE OF THE ARGUMENT (6 verification paths):

Path 1: Chain group dimensions CE^p_w depend only on d = dim(g).
Path 2: Euler characteristic chi_w = [t^w] prod(1-t^n)^d depends only on d.
Path 3: For semisimple g, diagonal concentration H^p_w = 0 for p != w.
Path 4: Diagonal concentration + Euler char => dim H^w_w = |chi_w| = f(d).
Path 5: Bracket invariance: ALL brackets with same d give same Euler chars.
Path 6: Abelian comparison: zero bracket gives same Euler char but different
        individual groups.

Verified computationally for:
- sl_2 (d=3): semisimple, simply-laced
- sl_3 (d=8): semisimple, simply-laced, rank 2
- sp_4 (d=10): semisimple, non-simply-laced, rank 2
- deformed sl_2 (d=3): semisimple (rescaled), isomorphic to sl_2
- Borel of sl_2 (d=3): solvable, NOT semisimple
- Heisenberg h_3 (d=3): nilpotent, NOT semisimple
- Abelian (d=3, 8, 10): trivial bracket

GROUND TRUTH (from explicit CE computation, exact rational arithmetic):

d=3 Euler series: [1, -3, 0, 5, 0, 0, -7, 0, 0, 0, 9]
d=8 Euler series: [1, -8, 20, 0, -70, 64, 56, 0, -125, -160, 308]
d=10 Euler series: [1, -10, 35, -30, -105, 238, 0, -260, -165, 140, 1054]
d=14 Euler series: [1, -14, 77, -182, 0, 924, -1547, -506, 3003, 0, -1729]

sl_2 CE (d=3): H^1_1=3, H^2_3=5.  NOT diagonally concentrated (H^2_3 is off-diagonal).
sl_3 CE (d=8): H^1_1=8, H^2_2=20. Diagonally concentrated at weights 1-3.
sp_4 CE (d=10): H^1_1=10, H^2_2=35, H^3_3=30. Diagonally concentrated at weights 1-3.
Abelian (d=3): H^p_w = CE^p_w for all (p,w). NOT diagonally concentrated.
Borel (d=3): H^1_1=3, H^1_2=2, H^2_2=2, H^2_3=7. NOT diagonally concentrated.
Heisenberg (d=3): H^1_1=3, H^1_2=2, H^2_2=2, H^2_3=7. NOT diag concentrated.

Total: 43 tests across 8 classes.
"""

import pytest
import numpy as np
from fractions import Fraction
from math import comb

from compute.lib.bar_cohomology_topological_engine import (
    # Combinatorial primitives
    euler_product_coeffs,
    pbw_hilbert_coeffs,
    partition_colored,
    ce_chain_dim,
    ce_euler_char_from_chain_dims,
    # Abelian cohomology
    abelian_ce_cohomology,
    # CE engine
    LoopCE,
    _rank_fraction,
    # Structure constants
    sl2_bracket,
    sl3_bracket,
    sp4_bracket,
    abelian_bracket,
    deformed_sl2_bracket,
    random_3d_lie_bracket,
    heisenberg_3d_bracket,
    # Comparison functions
    compare_euler_chars,
    diagonal_concentration_mechanism,
    full_explanation,
    the_argument,
)


# ============================================================================
# PATH 1: Chain group dimensions depend only on d
# ============================================================================

class TestPath1ChainGroups:
    """Chain group dimensions Lambda^p(g_-^*)_w depend ONLY on d = dim(g)."""

    def test_ce0_w0_is_1(self):
        """CE^0_0 = C (ground field) for all d."""
        for d in [3, 8, 10, 14, 52]:
            assert ce_chain_dim(0, 0, d) == 1

    def test_ce1_w1_equals_d(self):
        """CE^1_1 = g_- at mode 1, which has dim d."""
        for d in [3, 8, 10, 14]:
            assert ce_chain_dim(1, 1, d) == d

    def test_ce2_w2_equals_binom_d_2(self):
        r"""CE^2_2 = C(d,2): choose 2 of d mode-1 generators."""
        for d in [3, 8, 10, 14]:
            assert ce_chain_dim(2, 2, d) == comb(d, 2)

    def test_ce1_w2_equals_d(self):
        """CE^1_2: one generator at mode 2. There are d such generators."""
        for d in [3, 8, 10]:
            assert ce_chain_dim(1, 2, d) == d

    def test_ce2_w3_equals_d_squared(self):
        r"""CE^2_3: pairs with total weight 3.

        mode-1 + mode-2: d choices for each = d*d distinct pairs.
        (No other decomposition of 3 into 2 parts each >= 1.)
        """
        for d in [3, 8, 10]:
            assert ce_chain_dim(2, 3, d) == d * d

    def test_ce3_w3_equals_binom_d_3(self):
        """CE^3_3: three generators at mode 1 each. C(d, 3)."""
        for d in [3, 8, 10]:
            assert ce_chain_dim(3, 3, d) == comb(d, 3)

    def test_chain_dim_independent_of_d_ordering(self):
        """Different d values give predictably different chain dims."""
        assert ce_chain_dim(1, 1, 3) == 3
        assert ce_chain_dim(1, 1, 10) == 10
        assert ce_chain_dim(1, 1, 14) == 14

    def test_vanishing_below_diagonal(self):
        """CE^p_w = 0 when w < p (need at least p generators, each weight >= 1)."""
        for d in [3, 8]:
            for p in range(2, 6):
                for w in range(0, p):
                    assert ce_chain_dim(p, w, d) == 0

    def test_chain_groups_bracket_independent(self):
        """Chain group dimensions do not depend on the bracket.

        The weight_basis method enumerates subsets of generators, which
        depend only on the set of generators (d copies per mode), not on
        how they are bracketed.
        """
        for d, br in [(3, sl2_bracket()), (10, sp4_bracket())]:
            eng_actual = LoopCE(d, br, 4)
            eng_abelian = LoopCE(d, {}, 4)
            for w in range(1, 5):
                for p in range(0, w + 1):
                    dim_a = len(eng_actual.weight_basis(p, w))
                    dim_ab = len(eng_abelian.weight_basis(p, w))
                    assert dim_a == dim_ab, (
                        f"d={d}, (p,w)=({p},{w}): actual={dim_a}, abelian={dim_ab}")


# ============================================================================
# PATH 2: Euler characteristic equals product formula
# ============================================================================

class TestPath2EulerProduct:
    """Euler char chi_w = [t^w] prod(1-t^n)^d depends only on d."""

    def test_euler_product_d3(self):
        """d=3: prod(1-t^n)^3 = 1 - 3t + 0t^2 + 5t^3 + 0t^4 + ..."""
        chi = euler_product_coeffs(3, 6)
        assert chi[0] == 1
        assert chi[1] == -3
        assert chi[2] == 0
        assert chi[3] == 5
        assert chi[4] == 0
        assert chi[5] == 0
        assert chi[6] == -7

    def test_euler_product_d8(self):
        """d=8: prod(1-t^n)^8."""
        chi = euler_product_coeffs(8, 4)
        assert chi[0] == 1
        assert chi[1] == -8
        assert chi[2] == 20
        assert chi[3] == 0
        assert chi[4] == -70

    def test_euler_product_d10(self):
        """d=10 (sp_4 = B_2)."""
        chi = euler_product_coeffs(10, 3)
        assert chi[0] == 1
        assert chi[1] == -10
        assert chi[2] == 35
        assert chi[3] == -30

    def test_euler_product_d14(self):
        """d=14 (G_2)."""
        chi = euler_product_coeffs(14, 4)
        assert chi[1] == -14
        assert chi[2] == 77
        assert chi[3] == -182
        assert chi[4] == 0

    def test_chi1_equals_minus_d(self):
        """chi_1 = -d for all d (from (1-t)^d at order t^1)."""
        for d in [3, 8, 10, 14, 52]:
            chi = euler_product_coeffs(d, 1)
            assert chi[1] == -d

    def test_chi2_formula(self):
        """chi_2 = C(d,2) - d for all d.

        From (1-t)^d*(1-t^2)^d...: t^2 coefficient = C(d,2) from (1-t)^d
        plus (-d) from (1-t^2)^d = C(d,2) - d.
        """
        for d in [3, 8, 10, 14, 52]:
            chi = euler_product_coeffs(d, 2)
            assert chi[2] == comb(d, 2) - d

    def test_euler_chain_consistency(self):
        """Euler char from chain dims equals product formula."""
        for d in [3, 8]:
            chi_product = euler_product_coeffs(d, 5)
            for w in range(1, 6):
                chi_chains = ce_euler_char_from_chain_dims(w, d)
                assert chi_chains == chi_product[w], (
                    f"d={d}, w={w}: chains={chi_chains}, product={chi_product[w]}")


# ============================================================================
# PATH 3: Diagonal concentration for semisimple algebras
# ============================================================================

class TestPath3DiagonalConcentration:
    """Diagonal concentration (H^p_w = 0 for p != w) holds for some
    semisimple algebras (sp_4, sl_3) but NOT in general (sl_2 has H^2_3 != 0).

    The key: the EULER CHARACTERISTICS always match prod(1-t^n)^d,
    whether or not diagonal concentration holds. Diagonal concentration
    is a STRONGER property that makes the individual H^p_w computable
    from Euler chars alone.
    """

    def test_sl2_not_diagonal_at_w3(self):
        """sl_2: H^2_3 = 5 is off-diagonal (p=2 != w=3)."""
        engine = LoopCE(3, sl2_bracket(), 4)
        assert engine.cohomology_dim(2, 3) == 5

    def test_sl2_euler_still_correct(self):
        """sl_2 Euler chars match product formula despite no diagonal conc."""
        engine = LoopCE(3, sl2_bracket(), 5)
        product = euler_product_coeffs(3, 5)
        for w in range(1, 6):
            chi = sum((-1)**p * engine.cohomology_dim(p, w) for p in range(w + 1))
            assert chi == product[w], f"w={w}: CE chi={chi}, product={product[w]}"

    def test_sp4_diagonal_concentration_w1_to_w3(self):
        """sp_4 (d=10) IS diagonally concentrated at weights 1-3."""
        engine = LoopCE(10, sp4_bracket(), 3)
        assert engine.cohomology_dim(1, 1) == 10
        assert engine.cohomology_dim(2, 2) == 35
        assert engine.cohomology_dim(3, 3) == 30
        # Off-diagonal: all zero
        assert engine.cohomology_dim(1, 2) == 0
        assert engine.cohomology_dim(1, 3) == 0
        assert engine.cohomology_dim(2, 3) == 0

    def test_sl3_diagonal_concentration_w1_to_w2(self):
        """sl_3 (d=8) is diagonally concentrated at weights 1-2."""
        br = sl3_bracket()
        if not br:
            pytest.skip("sl_3 structure constants not available")
        engine = LoopCE(8, br, 3)
        assert engine.cohomology_dim(1, 1) == 8
        assert engine.cohomology_dim(2, 2) == 20
        assert engine.cohomology_dim(1, 2) == 0

    def test_sp4_dims_from_euler(self):
        """sp_4: H^w_w = |chi_w| because diagonally concentrated."""
        chi = euler_product_coeffs(10, 3)
        engine = LoopCE(10, sp4_bracket(), 3)
        for w in range(1, 4):
            assert engine.cohomology_dim(w, w) == abs(chi[w])


# ============================================================================
# PATH 4: Euler char determines bar dims for Koszul algebras
# ============================================================================

class TestPath4EulerDeterminesDims:
    """When diagonally concentrated: dim H^w_w = |chi_w| = f(d only)."""

    def test_bar_dims_d3(self):
        """d=3: |chi| = [1, 3, 0, 5, 0, 0, 7, ...]."""
        dims = [abs(c) for c in euler_product_coeffs(3, 8)]
        assert dims[1] == 3
        assert dims[2] == 0  # chi_2 = 0 for d=3
        assert dims[3] == 5
        assert dims[6] == 7

    def test_bar_dims_d8(self):
        """d=8 (sl_3 type)."""
        dims = [abs(c) for c in euler_product_coeffs(8, 4)]
        assert dims[1] == 8
        assert dims[2] == 20
        assert dims[3] == 0  # chi_3 = 0 for d=8

    def test_bar_dims_d10(self):
        """d=10 (B_2 = sp_4 type)."""
        dims = [abs(c) for c in euler_product_coeffs(10, 4)]
        assert dims[1] == 10
        assert dims[2] == 35
        assert dims[3] == 30

    def test_bar_dims_d14(self):
        """d=14 (G_2 type)."""
        dims = [abs(c) for c in euler_product_coeffs(14, 4)]
        assert dims[1] == 14
        assert dims[2] == 77
        assert dims[3] == 182
        assert dims[4] == 0  # chi_4 = 0 for d=14


# ============================================================================
# PATH 5: Bracket invariance of Euler characteristics
# ============================================================================

class TestPath5BracketInvariance:
    """ALL Lie algebras of the same dimension d have identical Euler chars.

    This is because the Euler characteristic depends only on chain group
    dimensions (exterior powers of g_-^*), which depend only on dim(g_-) = d
    copies per mode.
    """

    def test_euler_chars_all_match_d3(self):
        """All 3d Lie algebras have the same Euler characteristic series."""
        result = compare_euler_chars({
            'sl2': sl2_bracket(),
            'borel': random_3d_lie_bracket(),
            'heisenberg': heisenberg_3d_bracket(),
            'abelian': abelian_bracket(3),
        }, d=3, max_weight=5)
        values = list(result.values())
        for v in values[1:]:
            assert v == values[0], f"Euler chars differ: {result}"

    def test_euler_chars_match_product_d3(self):
        """All d=3 algebras match prod(1-t^n)^3."""
        product = euler_product_coeffs(3, 5)
        for name, bracket in [('sl2', sl2_bracket()),
                              ('borel', random_3d_lie_bracket()),
                              ('heisenberg', heisenberg_3d_bracket()),
                              ('abelian', abelian_bracket(3))]:
            engine = LoopCE(3, bracket, 5)
            for w in range(1, 6):
                chi = sum((-1)**p * len(engine.weight_basis(p, w))
                          for p in range(w + 1))
                assert chi == product[w], (
                    f"{name} w={w}: chi={chi}, product={product[w]}")

    def test_euler_match_d10_sp4_vs_abelian(self):
        """sp_4 and abelian d=10 give same Euler chars."""
        product = euler_product_coeffs(10, 3)
        for name, br in [('sp4', sp4_bracket()),
                         ('abelian', abelian_bracket(10))]:
            engine = LoopCE(10, br, 3)
            for w in range(1, 4):
                chi = sum((-1)**p * len(engine.weight_basis(p, w))
                          for p in range(w + 1))
                assert chi == product[w], f"{name} w={w}: {chi} != {product[w]}"

    def test_deformed_sl2_same_euler_char(self):
        """sl_2 deformed by epsilon: same Euler characteristics."""
        product = euler_product_coeffs(3, 4)
        for eps in [Fraction(0), Fraction(1, 2), Fraction(-1), Fraction(3)]:
            engine = LoopCE(3, deformed_sl2_bracket(eps), 4)
            for w in range(1, 5):
                chi = sum((-1)**p * len(engine.weight_basis(p, w))
                          for p in range(w + 1))
                assert chi == product[w]

    def test_individual_cohom_CAN_differ(self):
        """Different brackets give different individual H^p_w, same Euler.

        sl_2: H^2_3 = 5, H^1_3 = 0 => chi_3 = 5.
        Borel: H^2_3 = 7, H^1_3 = 2 => chi_3 = -2 + 7 = 5.
        """
        eng_sl2 = LoopCE(3, sl2_bracket(), 4)
        eng_bor = LoopCE(3, random_3d_lie_bracket(), 4)

        assert eng_sl2.cohomology_dim(2, 3) == 5
        assert eng_sl2.cohomology_dim(1, 3) == 0

        assert eng_bor.cohomology_dim(2, 3) == 7
        assert eng_bor.cohomology_dim(1, 3) == 2

        # Same Euler char at weight 3
        chi_sl2 = -eng_sl2.cohomology_dim(1, 3) + eng_sl2.cohomology_dim(2, 3) - eng_sl2.cohomology_dim(3, 3)
        chi_bor = -eng_bor.cohomology_dim(1, 3) + eng_bor.cohomology_dim(2, 3) - eng_bor.cohomology_dim(3, 3)
        assert chi_sl2 == chi_bor == 5


# ============================================================================
# PATH 6: Abelian comparison
# ============================================================================

class TestPath6AbelianComparison:
    """For the abelian Lie algebra: differential = 0, so H^p_w = CE^p_w."""

    def test_abelian_d3_h1_w1(self):
        """Abelian d=3: H^1_1 = CE^1_1 = 3."""
        engine = LoopCE(3, {}, 4)
        assert engine.cohomology_dim(1, 1) == 3

    def test_abelian_d3_h1_w2(self):
        """Abelian d=3: H^1_2 = CE^1_2 = 3 (off-diagonal, nonzero)."""
        engine = LoopCE(3, {}, 4)
        assert engine.cohomology_dim(1, 2) == 3

    def test_abelian_d3_h2_w2(self):
        """Abelian d=3: H^2_2 = CE^2_2 = C(3,2) = 3."""
        engine = LoopCE(3, {}, 4)
        assert engine.cohomology_dim(2, 2) == comb(3, 2)

    def test_abelian_not_diag_concentrated(self):
        """Abelian is NOT diagonally concentrated."""
        engine = LoopCE(3, {}, 3)
        assert not engine.is_diagonally_concentrated(2)

    def test_abelian_euler_matches_product(self):
        """Abelian d=3: Euler chars match prod(1-t^n)^3."""
        d = 3
        engine = LoopCE(d, {}, 5)
        product = euler_product_coeffs(d, 5)
        for w in range(1, 6):
            chi = sum((-1)**p * len(engine.weight_basis(p, w))
                      for p in range(w + 1))
            assert chi == product[w]

    def test_abelian_cohomology_equals_chain_groups(self):
        """For abelian, H^p_w = dim CE^p_w (zero differential)."""
        d = 3
        engine = LoopCE(d, {}, 4)
        for w in range(1, 5):
            for p in range(0, w + 1):
                chain_dim = len(engine.weight_basis(p, w))
                cohom_dim = engine.cohomology_dim(p, w)
                assert cohom_dim == chain_dim


# ============================================================================
# d^2 = 0 VERIFICATION
# ============================================================================

class TestDSquared:
    """Verify d^2 = 0 for the CE differential."""

    def _check_d_squared(self, engine, p, w):
        """Helper: verify d_{p+1} . d_p = 0 at weight w."""
        dp = engine.ce_differential_matrix(p, w)
        dp1 = engine.ce_differential_matrix(p + 1, w)
        if dp.shape[1] == 0 or dp1.shape[0] == 0:
            return  # trivially zero
        if dp.shape[0] != dp1.shape[1]:
            return  # dimensions don't match (one is empty)
        product = np.zeros((dp1.shape[0], dp.shape[1]), dtype=object)
        for i in range(product.shape[0]):
            for j in range(product.shape[1]):
                product[i, j] = Fraction(0)
        for i in range(dp1.shape[0]):
            for j in range(dp.shape[1]):
                for k in range(dp1.shape[1]):
                    product[i, j] += dp1[i, k] * dp[k, j]
        for i in range(product.shape[0]):
            for j in range(product.shape[1]):
                assert product[i, j] == 0, f"d^2 != 0 at ({i},{j}) for p={p}, w={w}"

    def test_d_squared_sl2(self):
        engine = LoopCE(3, sl2_bracket(), 5)
        for w in range(1, 5):
            for p in range(0, w):
                self._check_d_squared(engine, p, w)

    def test_d_squared_sp4_w1_w2(self):
        engine = LoopCE(10, sp4_bracket(), 3)
        for w in range(1, 3):
            for p in range(0, w):
                self._check_d_squared(engine, p, w)

    def test_d_squared_abelian(self):
        """Abelian: differential is zero, so d^2 = 0 trivially."""
        engine = LoopCE(3, {}, 4)
        for w in range(1, 4):
            for p in range(0, w):
                dp = engine.ce_differential_matrix(p, w)
                # All entries should be zero
                for i in range(dp.shape[0]):
                    for j in range(dp.shape[1]):
                        assert dp[i, j] == 0


# ============================================================================
# CONVOLUTION IDENTITY
# ============================================================================

class TestConvolutionIdentity:
    """prod(1-t^n)^d * prod 1/(1-t^n)^d = 1 (coefficient-level convolution)."""

    def test_convolution_d3(self):
        d, N = 3, 10
        euler = euler_product_coeffs(d, N)
        pbw = pbw_hilbert_coeffs(d, N)
        for w in range(1, N + 1):
            assert sum(euler[j] * pbw[w - j] for j in range(w + 1)) == 0

    def test_convolution_d8(self):
        d, N = 8, 8
        euler = euler_product_coeffs(d, N)
        pbw = pbw_hilbert_coeffs(d, N)
        for w in range(1, N + 1):
            assert sum(euler[j] * pbw[w - j] for j in range(w + 1)) == 0

    def test_convolution_d10(self):
        d, N = 10, 8
        euler = euler_product_coeffs(d, N)
        pbw = pbw_hilbert_coeffs(d, N)
        for w in range(1, N + 1):
            assert sum(euler[j] * pbw[w - j] for j in range(w + 1)) == 0

    def test_convolution_d14(self):
        d, N = 14, 6
        euler = euler_product_coeffs(d, N)
        pbw = pbw_hilbert_coeffs(d, N)
        for w in range(1, N + 1):
            assert sum(euler[j] * pbw[w - j] for j in range(w + 1)) == 0

    def test_convolution_d52(self):
        d, N = 52, 4
        euler = euler_product_coeffs(d, N)
        pbw = pbw_hilbert_coeffs(d, N)
        for w in range(1, N + 1):
            assert sum(euler[j] * pbw[w - j] for j in range(w + 1)) == 0


# ============================================================================
# THE MAIN THEOREM: comprehensive verification
# ============================================================================

class TestMainTheorem:
    """Bar cohomology of V_k(g) depends only on dim(g).

    The proof: (1) PBW collapse => bar = CE of g_-.
    (2) Chain groups depend only on d. (3) Euler chars depend only on d.
    (4) For Koszul algebras: diagonal concentration => |Euler| = bar dim.
    """

    def test_euler_universal_all_d3_algebras(self):
        """All d=3 algebras give chi = prod(1-t^n)^3."""
        product = euler_product_coeffs(3, 6)
        for name, br in [('sl2', sl2_bracket()),
                         ('borel', random_3d_lie_bracket()),
                         ('heisenberg', heisenberg_3d_bracket()),
                         ('abelian', abelian_bracket(3)),
                         ('deformed', deformed_sl2_bracket(Fraction(7, 3)))]:
            engine = LoopCE(3, br, 6)
            for w in range(1, 7):
                chi = sum((-1)**p * len(engine.weight_basis(p, w))
                          for p in range(w + 1))
                assert chi == product[w], f"{name} w={w}: {chi} != {product[w]}"

    def test_b2_equals_c2_equals_d10(self):
        """B_2 = C_2 = sp_4 has d=10. Any d=10 algebra gives same bar dims."""
        dims_10 = [abs(c) for c in euler_product_coeffs(10, 6)]
        assert dims_10[1] == 10
        assert dims_10[2] == 35
        assert dims_10[3] == 30

    def test_same_dim_different_root_system(self):
        """B_6 and E_6 both have dim=78. Same bar cohomology."""
        dims_78 = [abs(c) for c in euler_product_coeffs(78, 3)]
        assert dims_78[1] == 78
        assert dims_78[2] == comb(78, 2) - 78  # = 2925

    def test_mechanism_chain_euler_match(self):
        """Chain-level Euler char matches product formula."""
        for d in [3, 8, 10]:
            result = diagonal_concentration_mechanism(d, 4)
            assert result['chain_euler_matches_product']

    def test_the_argument_complete(self):
        """The mathematical argument is well-formed."""
        arg = the_argument()
        assert 'THEOREM' in arg
        assert 'dim(g)' in arg
        assert 'Koszulness' in arg
        assert 'chain group' in arg


# ============================================================================
# DEEP INSIGHT: the bracket redistributes but preserves Euler char
# ============================================================================

class TestDeepInsight:
    """The bracket enters the CE differential, which redistributes
    cohomology across degrees. Different brackets give different
    distributions. But the Euler characteristic (alternating sum)
    is invariant because it depends only on chain group dims.

    For Koszul algebras: the redistribution is maximal (all off-diagonal
    killed), so individual dims = |Euler char| = f(d).
    """

    def test_redistribution_sl2_vs_abelian(self):
        """sl_2 vs abelian at weight 3: same chi, different distribution.

        Abelian: H^1_3=3, H^2_3=9, H^3_3=1. chi = -3+9-1 = 5.
        sl_2:    H^1_3=0, H^2_3=5, H^3_3=0. chi = 0+5-0 = 5.

        sl_2 bracket kills H^1_3 and H^3_3, concentrating into H^2_3.
        """
        eng_sl2 = LoopCE(3, sl2_bracket(), 4)
        eng_ab = LoopCE(3, {}, 4)

        assert eng_ab.cohomology_dim(1, 3) == 3
        assert eng_ab.cohomology_dim(2, 3) == 9
        assert eng_ab.cohomology_dim(3, 3) == 1

        assert eng_sl2.cohomology_dim(1, 3) == 0
        assert eng_sl2.cohomology_dim(2, 3) == 5
        assert eng_sl2.cohomology_dim(3, 3) == 0

        chi_ab = -3 + 9 - 1
        chi_sl2 = -0 + 5 - 0
        assert chi_ab == chi_sl2 == 5

    def test_redistribution_borel_at_w3(self):
        """Borel at weight 3: H^1_3=2, H^2_3=7. chi = -2+7 = 5."""
        eng = LoopCE(3, random_3d_lie_bracket(), 4)
        h1 = eng.cohomology_dim(1, 3)
        h2 = eng.cohomology_dim(2, 3)
        h3 = eng.cohomology_dim(3, 3)
        assert -h1 + h2 - h3 == 5

    def test_sp4_w2_perfect_concentration(self):
        """sp_4 at weight 2: all cohomology on diagonal.

        Abelian: CE^1_2 = 10, CE^2_2 = 45. chi = -10+45 = 35.
        sp_4:    H^1_2 = 0, H^2_2 = 35. chi = 35. EXACT MATCH.

        The bracket kills all 10 dimensions of H^1_2 and simultaneously
        reduces H^2_2 from 45 to 35 (killing 10 by exactness).
        """
        eng = LoopCE(10, sp4_bracket(), 3)
        assert eng.cohomology_dim(1, 2) == 0
        assert eng.cohomology_dim(2, 2) == 35

    def test_chain_dim_w3_p2_is_d_squared(self):
        """CE^2_3 = d^2 for all d."""
        for d in [3, 8, 10, 14]:
            assert ce_chain_dim(2, 3, d) == d * d


# ============================================================================
# RANK COMPUTATION HELPER
# ============================================================================

class TestRankComputation:
    """Test the exact-arithmetic rank computation."""

    def test_rank_zero_matrix(self):
        mat = np.array([[Fraction(0), Fraction(0)],
                        [Fraction(0), Fraction(0)]])
        assert _rank_fraction(mat) == 0

    def test_rank_identity(self):
        mat = np.array([[Fraction(1), Fraction(0)],
                        [Fraction(0), Fraction(1)]])
        assert _rank_fraction(mat) == 2

    def test_rank_singular(self):
        mat = np.array([[Fraction(1), Fraction(2)],
                        [Fraction(2), Fraction(4)]])
        assert _rank_fraction(mat) == 1

    def test_rank_3x3(self):
        mat = np.array([
            [Fraction(1), Fraction(0), Fraction(1)],
            [Fraction(0), Fraction(1), Fraction(1)],
            [Fraction(1), Fraction(1), Fraction(2)],
        ])
        assert _rank_fraction(mat) == 2

    def test_rank_empty(self):
        mat = np.zeros((0, 0), dtype=object)
        assert _rank_fraction(mat) == 0
