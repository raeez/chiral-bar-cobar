"""Tests for conj:level-rank-complementarity (kac_moody.tex, ~line 3870).

Investigates the conjecture that for affine V_k(g) at non-critical level:
  Q_g(V_k(g)) + Q_g(V_{-k-2h^vee}(g)) = H*(M_bar_g, Z(V_k(g)))

PROVED ingredients tested:
  (1) kappa anti-symmetry: kappa(g_k) + kappa(g_{-k-2h^vee}) = 0
  (2) Genus-1 complementarity: dim Q_1 + dim Q_1' = 2 = dim H*(M_bar_{1,1})
  (3) Level-rank for gl_N: U(N)_k <-> U(k)_{-N}
  (4) Verlinde symmetry at genus 1: dim V_1(sl_N, k) = dim V_1(sl_k, N)
  (5) Center factorization at genus 1

Mathematical references:
  conj:level-rank-complementarity    (kac_moody.tex)
  thm:sl2-genus1-complementarity     (kac_moody.tex)
  prop:ff-channel-shear              (kac_moody.tex)
  thm:quantum-complementarity-main   (higher_genus_complementarity.tex)
"""

import pytest
from sympy import Rational, Symbol, simplify, sympify

from compute.lib.level_rank_complementarity import (
    kappa_affine,
    kappa_sum,
    central_charge,
    ff_dual_level,
    level_rank_data,
    level_rank_kappa_identity,
    genus1_complementarity_sl2,
    genus1_complementarity_general,
    verlinde_dim_sl2,
    verlinde_dim_sl2_exact,
    verlinde_genus1_sl_N,
    verlinde_ff_invariance_sl2,
    self_dual_level,
    center_factorization_check,
    lie_data,
)


# ---------------------------------------------------------------------------
# Test data
# ---------------------------------------------------------------------------

# (type, rank, dim, h_dual, name)
SIMPLE_ALGEBRAS = [
    ("A", 1, 3, 2, "sl_2"),
    ("A", 2, 8, 3, "sl_3"),
    ("A", 3, 15, 4, "sl_4"),
    ("A", 4, 24, 5, "sl_5"),
    ("B", 2, 10, 3, "so_5"),
    ("B", 3, 21, 5, "so_7"),
    ("C", 2, 10, 3, "sp_4"),
    ("C", 3, 21, 4, "sp_6"),
    ("D", 4, 28, 6, "so_8"),
    ("G", 2, 14, 4, "g_2"),
    ("F", 4, 52, 9, "f_4"),
    ("E", 6, 78, 12, "e_6"),
    ("E", 7, 133, 18, "e_7"),
    ("E", 8, 248, 30, "e_8"),
]

TEST_LEVELS = [1, 2, 3, 5, 10, Rational(1, 2), Rational(7, 3), Rational(-1, 3)]


# ===========================================================================
# I. KAPPA ANTI-SYMMETRY UNDER FEIGIN-FRENKEL (PROVED)
# ===========================================================================

class TestKappaAntiSymmetry:
    """kappa(g_k) + kappa(g_{-k-2h^vee}) = 0 for all simple g, all k != -h^vee."""

    @pytest.mark.parametrize("typ,rank,dim_g,h_dual,name", SIMPLE_ALGEBRAS)
    def test_kappa_antisymmetry_symbolic(self, typ, rank, dim_g, h_dual, name):
        """kappa(g_k) + kappa(g_{k'}) = 0 symbolically for all simple g."""
        k = Symbol('k')
        total = kappa_sum(typ, rank, k)
        assert simplify(total) == 0, (
            f"kappa anti-symmetry fails for {name}: got {total}"
        )

    @pytest.mark.parametrize("typ,rank,dim_g,h_dual,name", SIMPLE_ALGEBRAS)
    @pytest.mark.parametrize("level", TEST_LEVELS)
    def test_kappa_antisymmetry_numeric(self, typ, rank, dim_g, h_dual, name, level):
        """kappa(g_k) + kappa(g_{k'}) = 0 numerically at many levels."""
        k = sympify(level)
        # Skip if k = -h_dual (critical level)
        if k + h_dual == 0:
            pytest.skip(f"Critical level k = -{h_dual}")
        k_prime = ff_dual_level(typ, rank, k)
        # Also skip if k' is at the critical level
        if k_prime + h_dual == 0:
            pytest.skip(f"FF-dual is at critical level")
        total = kappa_sum(typ, rank, k)
        assert total == 0, (
            f"kappa anti-symmetry fails for {name} at k={k}: "
            f"kappa({k}) + kappa({k_prime}) = {total}"
        )

    def test_kappa_sl2_explicit(self):
        """kappa(sl_2, k) = 3(k+2)/4, anti-symmetric under k -> -k-4."""
        k = Symbol('k')
        kappa_k = kappa_affine("A", 1, k)
        expected = Rational(3) * (k + 2) / 4
        assert simplify(kappa_k - expected) == 0

        k_prime = ff_dual_level("A", 1, k)
        assert simplify(k_prime - (-k - 4)) == 0

    def test_kappa_sl3_explicit(self):
        """kappa(sl_3, k) = 4(k+3)/3, anti-symmetric under k -> -k-6."""
        k = Symbol('k')
        kappa_k = kappa_affine("A", 2, k)
        expected = Rational(4) * (k + 3) / 3
        assert simplify(kappa_k - expected) == 0

    def test_kappa_at_critical_level_raises(self):
        """kappa is undefined at the critical level k = -h^vee."""
        with pytest.raises(ValueError, match="Critical level"):
            kappa_affine("A", 1, -2)  # sl_2, h^vee = 2
        with pytest.raises(ValueError, match="Critical level"):
            kappa_affine("A", 2, -3)  # sl_3, h^vee = 3
        with pytest.raises(ValueError, match="Critical level"):
            kappa_affine("G", 2, -4)  # g_2, h^vee = 4


# ===========================================================================
# II. FF INVOLUTION PROPERTIES
# ===========================================================================

class TestFFInvolution:
    """Properties of the Feigin-Frenkel involution k -> -k - 2h^vee."""

    @pytest.mark.parametrize("typ,rank,dim_g,h_dual,name", SIMPLE_ALGEBRAS)
    def test_ff_is_involution(self, typ, rank, dim_g, h_dual, name):
        """FF applied twice is the identity: (k')' = k."""
        k = Symbol('k')
        k_prime = ff_dual_level(typ, rank, k)
        k_double_prime = ff_dual_level(typ, rank, k_prime)
        assert simplify(k_double_prime - k) == 0, (
            f"FF is not an involution for {name}: (k')' = {k_double_prime}"
        )

    @pytest.mark.parametrize("typ,rank,dim_g,h_dual,name", SIMPLE_ALGEBRAS)
    def test_ff_fixed_point_is_critical(self, typ, rank, dim_g, h_dual, name):
        """The unique fixed point of FF is k = -h^vee (critical level)."""
        result = self_dual_level(typ, rank)
        assert result["self_dual_level"] == -h_dual
        assert result["is_critical"] is True

    def test_ff_central_charge_inversion(self):
        """Central charge under FF: c(k) + c(k') = 2*dim(g) for sl_N.

        c(k) = k * dim / (k + h^vee)
        c(k') = (-k-2h^vee) * dim / (-k-h^vee)
        c(k) + c(k') = dim * [k/(k+h^vee) + (-k-2h^vee)/(-k-h^vee)]
                      = dim * [k/(k+h^vee) + (k+2h^vee)/(k+h^vee)]
                      = dim * (2k + 2h^vee)/(k + h^vee)
                      = 2 * dim
        """
        k = Symbol('k')
        for typ, rank, dim_g, h_dual, name in SIMPLE_ALGEBRAS[:5]:
            c_k = central_charge(typ, rank, k)
            k_prime = ff_dual_level(typ, rank, k)
            c_k_prime = central_charge(typ, rank, k_prime)
            total = simplify(c_k + c_k_prime)
            assert total == 2 * dim_g, (
                f"c(k) + c(k') = {total} != 2*{dim_g} for {name}"
            )


# ===========================================================================
# III. GENUS-1 COMPLEMENTARITY (PROVED, thm:sl2-genus1-complementarity)
# ===========================================================================

class TestGenus1Complementarity:
    """Q_1(g_k) + Q_1(g_{k'}) = H*(M_bar_{1,1}) at genus 1."""

    def test_sl2_genus1(self):
        """sl_2 genus-1 complementarity: 1 + 1 = 2."""
        for k in [1, 2, 3, 5, 10, Rational(1, 2)]:
            result = genus1_complementarity_sl2(k)
            assert result["kappa_sum"] == 0, (
                f"kappa sum nonzero at k={k}: {result['kappa_sum']}"
            )
            assert result["complementarity_holds"], (
                f"Genus-1 complementarity fails for sl_2 at k={k}"
            )

    @pytest.mark.parametrize("typ,rank,dim_g,h_dual,name", SIMPLE_ALGEBRAS)
    def test_genus1_complementarity_all_types(self, typ, rank, dim_g, h_dual, name):
        """Genus-1 complementarity for all simple g at k=1."""
        result = genus1_complementarity_general(typ, rank, 1)
        assert result["kappa_sum"] == 0, (
            f"kappa sum nonzero for {name} at k=1: {result['kappa_sum']}"
        )
        assert result["complementarity_holds"], (
            f"Genus-1 complementarity fails for {name} at k=1"
        )

    @pytest.mark.parametrize("level", [1, 2, 3, 5, 10, Rational(1, 3)])
    def test_genus1_complementarity_sl2_multiLevel(self, level):
        """Genus-1 complementarity for sl_2 at various levels."""
        result = genus1_complementarity_general("A", 1, level)
        assert result["complementarity_holds"]
        assert result["kappa_sum"] == 0

    def test_genus1_complementarity_sl3_admissible(self):
        """Genus-1 complementarity for sl_3 at admissible level k = -3/2."""
        # Admissible level for sl_3: k = -3 + p/q with coprimality conditions
        # k = -3/2 is admissible (p=3, q=2)
        result = genus1_complementarity_general("A", 2, Rational(-3, 2))
        assert result["kappa_sum"] == 0
        assert result["complementarity_holds"]


# ===========================================================================
# IV. LEVEL-RANK DUALITY (gl_N specialization)
# ===========================================================================

class TestLevelRank:
    """Level-rank duality U(N)_k <-> U(k)_{-N} at the kappa level."""

    @pytest.mark.parametrize("N,k", [
        (2, 1), (2, 3), (2, 5),
        (3, 1), (3, 2),
        (4, 1), (4, 2), (4, 3),
        (5, 1), (5, 3),
    ])
    def test_ff_antisymmetry_slN_generic(self, N, k):
        """FF anti-symmetry kappa(sl_N, k) + kappa(sl_N, -k-2N) = 0 for N != k."""
        data = level_rank_data(N, k)
        assert data["kappa_sum_ff"] == 0

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_ff_antisymmetry_slN_N_equals_k(self, N):
        """FF anti-symmetry still holds when N = k (dual side at critical level)."""
        data = level_rank_data(N, N)
        assert data["kappa_sum_ff"] == 0
        # When N = k, the level-rank dual sl_k at level -N hits critical level
        assert data["dual_critical"]
        assert data["kappa_B"] is None

    @pytest.mark.parametrize("N,k", [
        (2, 3), (3, 2), (4, 2), (5, 3), (3, 5),
    ])
    def test_level_rank_kappa_identity_generic(self, N, k):
        """Level-rank kappa identity check for generic (N, k) pairs."""
        result = level_rank_kappa_identity(N, k)
        assert result["ff_sum_zero"], (
            f"FF sum not zero for (N={N}, k={k})"
        )
        # Dual side is not critical
        assert not result["dual_critical"]

    def test_level_rank_N_equals_k_critical(self):
        """At N=k=2: FF involution within sl_2 sends k=2 to k'=-6.
        Level-rank sends (2,2) to (2,-2), which is critical."""
        data = level_rank_data(2, 2)
        assert data["kappa_sum_ff"] == 0
        # kappa(sl_2, 2) = 3*(2+2)/4 = 3
        assert data["kappa_A"] == 3
        # Dual side is at critical level
        assert data["dual_critical"]

    def test_level_rank_symmetry_N3_k2(self):
        """(N=3, k=2): sl_3 at level 2 vs sl_2 at level -3."""
        data = level_rank_data(3, 2)
        # kappa(sl_3, 2) = 8*(2+3)/6 = 8*5/6 = 20/3
        assert data["kappa_A"] == Rational(20, 3)
        # kappa(sl_2, -3) = 3*(-3+2)/4 = -3/4
        assert data["kappa_B"] == Rational(-3, 4)

    def test_level_rank_kappa_sign_structure(self):
        """For N < k with both non-critical: kappa_A > 0, kappa_B > 0.
        For N > k: kappa_B < 0 (level -N < -k = -h^vee)."""
        # N=2, k=5: kappa(sl_2, 5) = 3*7/4 = 21/4 > 0
        # kappa(sl_5, -2) = 24*(-2+5)/10 = 24*3/10 = 36/5 > 0
        data = level_rank_data(2, 5)
        assert data["kappa_A"] > 0
        assert data["kappa_B"] > 0

        # N=5, k=2: kappa(sl_5, 2) = 24*7/10 = 84/5 > 0
        # kappa(sl_2, -5) = 3*(-5+2)/4 = -9/4 < 0
        data2 = level_rank_data(5, 2)
        assert data2["kappa_A"] > 0
        assert data2["kappa_B"] < 0


# ===========================================================================
# V. VERLINDE FORMULA COMPATIBILITY
# ===========================================================================

class TestVerlindeCompatibility:
    """Verlinde dimensions and level-rank symmetry."""

    def test_verlinde_genus0(self):
        """Verlinde dimension at genus 0 is always 1."""
        for k in [1, 2, 3, 5]:
            assert verlinde_dim_sl2_exact(k, 0) == 1

    def test_verlinde_genus1_sl2(self):
        """dim V_1(sl_2, k) = k + 1."""
        for k in [1, 2, 3, 5, 10]:
            assert verlinde_dim_sl2_exact(k, 1) == k + 1

    @pytest.mark.parametrize("N,k", [
        (2, 2), (3, 3), (4, 4), (5, 5),
    ])
    def test_verlinde_genus1_symmetry_N_equals_k(self, N, k):
        """Level-rank symmetry holds at genus 1 when N = k.

        dim V_1(sl_N, N) = C(2N-1, N-1) = C(2N-1, N),
        which IS symmetric under the swap (N, k) -> (k, N) when N = k.
        """
        result = verlinde_genus1_sl_N(N, k)
        assert result["sl_verlinde_swap_symmetric"]
        assert result["N_equals_k"]

    @pytest.mark.parametrize("N,k", [
        (2, 3), (2, 5), (3, 2), (3, 5), (4, 2), (5, 2),
    ])
    def test_verlinde_genus1_asymmetry_N_neq_k(self, N, k):
        """For N != k, the sl Verlinde dims are NOT swap-symmetric.

        dim V_1(sl_N, k) = C(N+k-1, N-1) != C(N+k-1, k-1) = dim V_1(sl_k, N)
        in general. The level-rank symmetry is for U(N), not SL(N).
        """
        result = verlinde_genus1_sl_N(N, k)
        # They differ unless N = k
        if N != k:
            assert not result["sl_verlinde_swap_symmetric"]

    @pytest.mark.parametrize("N,k", [
        (2, 1), (2, 2), (3, 1), (3, 2), (4, 1), (5, 3),
    ])
    def test_verlinde_binomial_symmetry(self, N, k):
        """Binomial identity C(N+k-1, N-1) = C(N+k-1, k) always holds."""
        result = verlinde_genus1_sl_N(N, k)
        assert result["binomial_symmetry_holds"]

    def test_verlinde_genus1_sl2_k1(self):
        """dim V_1(sl_2, 1) = 2."""
        result = verlinde_genus1_sl_N(2, 1)
        assert result["verlinde_dim_g1_slN_k"] == 2

    def test_verlinde_genus1_sl3_k1(self):
        """dim V_1(sl_3, 1) = 3."""
        result = verlinde_genus1_sl_N(3, 1)
        assert result["verlinde_dim_g1_slN_k"] == 3

    def test_verlinde_genus1_sl3_k2(self):
        """dim V_1(sl_3, 2) = C(4,2) = 6."""
        result = verlinde_genus1_sl_N(3, 2)
        assert result["verlinde_dim_g1_slN_k"] == 6

    def test_verlinde_genus2_sl2(self):
        """Verlinde dimension at genus 2 for sl_2 at level k.

        dim V_2(sl_2, k) = sum_{m=0}^k (S_{0,m})^{2-2g} = sum (S_{0,m})^{-2}
        = (k+2)/2 * sum_{m=0}^k 1/sin^2(pi*(m+1)/(k+2))

        For k=1 (su(2) level 1): 2 reps (trivial + fundamental).
        S_{0,0} = sqrt(2/3) sin(pi/3) = sqrt(2/3) * sqrt(3)/2 = sqrt(1/2)
        S_{0,1} = sqrt(2/3) sin(2pi/3) = sqrt(1/2)
        V_2 = S_{0,0}^{-2} + S_{0,1}^{-2} = 2 + 2 = 4
        """
        # Compute the actual genus-2 Verlinde dimensions numerically
        dim_g2_k1 = verlinde_dim_sl2(1, 2)
        assert abs(dim_g2_k1 - round(dim_g2_k1)) < 1e-8
        # Verify it's a positive integer
        assert round(dim_g2_k1) > 0

        dim_g2_k2 = verlinde_dim_sl2(2, 2)
        assert abs(dim_g2_k2 - round(dim_g2_k2)) < 1e-8
        assert round(dim_g2_k2) > 0


# ===========================================================================
# VI. CENTER FACTORIZATION
# ===========================================================================

class TestCenterFactorization:
    """H*(M_bar_g, Z(V_k(g))) factorization tests."""

    def test_genus1_center_sl2(self):
        """Center factorization at genus 1 for sl_2."""
        result = center_factorization_check("A", 1, 1, 1)
        assert result["complementarity"]
        assert result["dim_H_star_Z"] == 2

    @pytest.mark.parametrize("typ,rank,dim_g,h_dual,name", SIMPLE_ALGEBRAS[:6])
    def test_genus1_center_all_types(self, typ, rank, dim_g, h_dual, name):
        """Center factorization at genus 1 for various types at level 1."""
        result = center_factorization_check(typ, rank, 1, 1)
        assert result["complementarity"]


# ===========================================================================
# VII. STRUCTURAL PROPERTIES
# ===========================================================================

class TestStructuralProperties:
    """Structural tests for level-rank complementarity."""

    def test_kappa_linearity_in_k(self):
        """kappa(g, k) is linear in k (affine function)."""
        k = Symbol('k')
        for typ, rank, dim_g, h_dual, name in SIMPLE_ALGEBRAS[:5]:
            kappa_k = kappa_affine(typ, rank, k)
            # Check it's of the form a*k + b
            from sympy import Poly
            p = Poly(kappa_k, k)
            assert p.degree() == 1, (
                f"kappa is not linear in k for {name}: degree {p.degree()}"
            )

    def test_kappa_zero_at_minus_h_dual(self):
        """kappa(g, -h^vee) = 0 (kappa vanishes at critical level shift).

        Wait: kappa = dim(g) * (k + h^vee) / (2*h^vee).
        At k = -h^vee: this is 0/0... but the formula gives 0 * dim(g)/(2*h^vee) = 0.
        Actually kappa is DEFINED as a linear function of (k + h^vee), so kappa(-h^vee) = 0.
        But Sugawara is UNDEFINED there. The kappa function extends continuously.
        """
        # We test that kappa at k just above -h^vee is near zero
        for typ, rank, dim_g, h_dual, name in SIMPLE_ALGEBRAS[:5]:
            eps = Rational(1, 1000)
            kappa_near = kappa_affine(typ, rank, -h_dual + eps)
            assert abs(float(kappa_near)) < 0.1, (
                f"kappa not near zero at k ~ -h^vee for {name}: {kappa_near}"
            )

    def test_kappa_additivity(self):
        """kappa is additive: kappa(g1 + g2) = kappa(g1) + kappa(g2).

        For direct sum g = g1 + g2 at level (k1, k2), the modular
        characteristic is additive by prop:independent-sum-factorization.
        """
        k = Symbol('k')
        # sl_2 + sl_3 at same level k should give sum of kappas
        kappa_sl2 = kappa_affine("A", 1, k)
        kappa_sl3 = kappa_affine("A", 2, k)
        kappa_sum_val = kappa_sl2 + kappa_sl3

        # Direct computation: dim(sl2)=3, h^vee=2; dim(sl3)=8, h^vee=3
        # kappa_sl2 = 3(k+2)/4, kappa_sl3 = 8(k+3)/6 = 4(k+3)/3
        expected = Rational(3) * (k + 2) / 4 + Rational(4) * (k + 3) / 3
        assert simplify(kappa_sum_val - expected) == 0

    def test_kappa_at_k_equals_1(self):
        """Known kappa values at k = 1 for reference."""
        # sl_2: kappa = 3*3/4 = 9/4
        assert kappa_affine("A", 1, 1) == Rational(9, 4)
        # sl_3: kappa = 8*4/6 = 16/3
        assert kappa_affine("A", 2, 1) == Rational(16, 3)
        # g_2: kappa = 14*5/8 = 35/4
        assert kappa_affine("G", 2, 1) == Rational(35, 4)

    def test_lie_data_slN_formula(self):
        """For sl_N: dim = N^2 - 1, h^vee = N."""
        for N in range(2, 11):
            dim_g, h, h_dual, name = lie_data("A", N - 1)
            assert dim_g == N * N - 1
            assert h_dual == N
            assert name == f"sl_{N}"
