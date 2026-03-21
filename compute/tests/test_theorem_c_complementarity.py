"""Tests for Theorem C complementarity: Q_g(A) + Q_g(A!) = H*(M_bar_g, Z(A)).

50+ tests verifying:
  - Scalar complementarity: kappa(A) + kappa(A!) = constant
  - Genus-g complementarity: F_g(A) + F_g(A!) = (kappa+kappa!) * lambda_g^FP
  - Feigin-Frenkel dual parameters
  - Self-dual points (Virasoro at c=13, NOT c=26)
  - Level independence of complementarity sums
  - Lagrangian indicators
  - Two-channel decomposition for affine algebras
  - Full landscape verification

All arithmetic is exact (Fraction).

References:
  thm:quantum-complementarity-main (higher_genus_complementarity.tex)
  prop:kappa-anti-symmetry-ff (kac_moody.tex)
  CLAUDE.md: Theorem C, Critical Pitfalls
"""
import pytest
from fractions import Fraction

from compute.lib.theorem_c_complementarity import (
    kappa,
    kappa_dual,
    complementarity_sum,
    verify_complementarity_scalar,
    ff_dual_parameters,
    self_dual_point,
    genus_g_complementarity,
    verify_genus_g_complementarity,
    complementarity_table,
    virasoro_self_dual_check,
    lagrangian_complementarity_check,
    complementarity_independent_of_level,
    all_families_complementary,
    w3_central_charge_complementarity,
    virasoro_central_charge_complementarity,
    affine_kappa_two_channel,
    _lambda_fp,
    _F_g,
    _sigma_invariant,
    _lie_dim_hdual,
    kappa_from_ope,
    kappa_dual_derived,
    genus_g_complementarity_graph_sum,
    lagrangian_complementarity_computed,
    _ope_product,
)


# ========================================================================
# I. kappa values (ground truth from Master Table)
# ========================================================================


class TestKappaValues:
    """Verify kappa(A) for each standard family against the Master Table."""

    def test_heisenberg_kappa_is_level(self):
        """kappa(H_k) = k (the level IS the obstruction coefficient)."""
        assert kappa("heisenberg", k=1) == Fraction(1)
        assert kappa("heisenberg", k=3) == Fraction(3)
        assert kappa("heisenberg", k=-5) == Fraction(-5)
        assert kappa("heisenberg", k=Fraction(1, 2)) == Fraction(1, 2)

    def test_virasoro_kappa_is_c_over_2(self):
        """kappa(Vir_c) = c/2."""
        assert kappa("virasoro", c=1) == Fraction(1, 2)
        assert kappa("virasoro", c=26) == Fraction(13)
        assert kappa("virasoro", c=13) == Fraction(13, 2)
        assert kappa("virasoro", c=Fraction(7, 10)) == Fraction(7, 20)

    def test_affine_sl2_kappa(self):
        """kappa(sl_2_k) = 3(k+2)/4 = dim*(k+h^v)/(2*h^v)."""
        # sl_2: dim=3, h^v=2
        assert kappa("affine", lie_type="A", rank=1, k=1) == Fraction(9, 4)
        assert kappa("affine", lie_type="A", rank=1, k=0) == Fraction(3, 2)
        assert kappa("affine", lie_type="A", rank=1, k=2) == Fraction(3)

    def test_affine_sl3_kappa(self):
        """kappa(sl_3_k) = 8(k+3)/6 = 4(k+3)/3."""
        # sl_3: dim=8, h^v=3
        assert kappa("affine", lie_type="A", rank=2, k=1) == Fraction(16, 3)
        assert kappa("affine", lie_type="A", rank=2, k=0) == Fraction(4)

    def test_affine_slN_kappa_formula(self):
        """kappa(sl_N_k) = (N^2-1)(k+N)/(2N)."""
        for N in range(2, 8):
            k_val = 1
            expected = Fraction(N * N - 1) * (k_val + N) / (2 * N)
            assert kappa("affine", lie_type="A", rank=N - 1, k=k_val) == expected

    def test_affine_critical_level_raises(self):
        """kappa undefined at critical level k = -h^v."""
        with pytest.raises(ValueError, match="Critical level"):
            kappa("affine", lie_type="A", rank=1, k=-2)
        with pytest.raises(ValueError, match="Critical level"):
            kappa("affine", lie_type="A", rank=2, k=-3)

    def test_betagamma_kappa_formula(self):
        """kappa(bg) = c/2 = 6*lam^2 - 6*lam + 1."""
        # At lam = 1/2: kappa = 6*(1/4) - 6*(1/2) + 1 = 3/2 - 3 + 1 = -1/2
        assert kappa("betagamma", lam=Fraction(1, 2)) == Fraction(-1, 2)
        # At lam = 1: kappa = 6 - 6 + 1 = 1
        assert kappa("betagamma", lam=1) == Fraction(1)
        # At lam = 0: kappa = 0 - 0 + 1 = 1
        assert kappa("betagamma", lam=0) == Fraction(1)

    def test_betagamma_kappa_from_c(self):
        """kappa(bg) = c/2 when c is given directly."""
        assert kappa("betagamma", c=-2) == Fraction(-1)
        assert kappa("betagamma", c=2) == Fraction(1)

    def test_w3_kappa_is_5c_over_6(self):
        """kappa(W_3) = 5c/6."""
        assert kappa("w3", c=6) == Fraction(5)
        assert kappa("w3", c=12) == Fraction(10)
        assert kappa("w3", c=50) == Fraction(125, 3)

    def test_lattice_kappa_is_rank_over_2(self):
        """kappa(V_Lambda) = rank/2."""
        assert kappa("lattice", rank=1) == Fraction(1, 2)
        assert kappa("lattice", rank=8) == Fraction(4)
        assert kappa("lattice", rank=24) == Fraction(12)

    def test_non_simply_laced_kappa(self):
        """kappa for non-simply-laced types: B_2 (so_5), G_2."""
        # B_2: dim=10, h^v=3. kappa = 10*(k+3)/6 = 5(k+3)/3
        assert kappa("affine", lie_type="B", rank=2, k=1) == Fraction(20, 3)
        # G_2: dim=14, h^v=4. kappa = 14*(k+4)/8 = 7(k+4)/4
        assert kappa("affine", lie_type="G", rank=2, k=1) == Fraction(35, 4)


# ========================================================================
# II. Feigin-Frenkel dual parameters
# ========================================================================


class TestFFDualParameters:
    """Verify Feigin-Frenkel dual parameter computation."""

    def test_heisenberg_dual_negates_level(self):
        """H_k! = H_{-k}."""
        d = ff_dual_parameters("heisenberg", k=3)
        assert d["k"] == Fraction(-3)

    def test_virasoro_dual_is_26_minus_c(self):
        """Vir_c! = Vir_{26-c}."""
        d = ff_dual_parameters("virasoro", c=1)
        assert d["c"] == Fraction(25)
        d = ff_dual_parameters("virasoro", c=13)
        assert d["c"] == Fraction(13)

    def test_affine_ff_involution(self):
        """k' = -k - 2h^v. NOT -k - h^v."""
        d = ff_dual_parameters("affine", lie_type="A", rank=1, k=1)
        # sl_2: h^v = 2, so k' = -1 - 4 = -5
        assert d["k"] == Fraction(-5)

        d = ff_dual_parameters("affine", lie_type="A", rank=2, k=1)
        # sl_3: h^v = 3, so k' = -1 - 6 = -7
        assert d["k"] == Fraction(-7)

    def test_ff_involution_is_involution(self):
        """k'' = k (FF is an involution)."""
        for N in range(2, 6):
            for k_val in [1, 2, 3, -1]:
                d1 = ff_dual_parameters("affine", lie_type="A", rank=N - 1, k=k_val)
                d2 = ff_dual_parameters("affine", lie_type="A", rank=N - 1, k=d1["k"])
                assert d2["k"] == Fraction(k_val)

    def test_virasoro_ff_involution_is_involution(self):
        """c'' = c for Virasoro."""
        d1 = ff_dual_parameters("virasoro", c=7)
        d2 = ff_dual_parameters("virasoro", c=d1["c"])
        assert d2["c"] == Fraction(7)

    def test_w3_dual_is_100_minus_c(self):
        """W_3(c)! = W_3(100-c)."""
        d = ff_dual_parameters("w3", c=2)
        assert d["c"] == Fraction(98)

    def test_betagamma_dual_negates_c(self):
        """bg! = bc, with c -> -c."""
        d = ff_dual_parameters("betagamma", c=2)
        assert d["c"] == Fraction(-2)


# ========================================================================
# III. Scalar complementarity sums
# ========================================================================


class TestScalarComplementarity:
    """Verify kappa(A) + kappa(A!) = constant for all families."""

    def test_heisenberg_sum_is_zero(self):
        """kappa(H_k) + kappa(H_{-k}) = 0 for all k."""
        for k_val in [1, -1, 2, Fraction(1, 2), Fraction(7, 3), 100]:
            assert complementarity_sum("heisenberg", k=k_val) == Fraction(0)

    def test_virasoro_sum_is_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c."""
        for c_val in [0, 1, 13, 26, Fraction(1, 2), Fraction(7, 10), -5]:
            assert complementarity_sum("virasoro", c=c_val) == Fraction(13)

    def test_affine_sl2_sum_is_zero(self):
        """kappa(sl_2_k) + kappa(sl_2_{-k-4}) = 0."""
        for k_val in [1, 2, 3, -1, Fraction(1, 2)]:
            assert complementarity_sum(
                "affine", lie_type="A", rank=1, k=k_val
            ) == Fraction(0)

    def test_affine_slN_sum_is_zero(self):
        """kappa(sl_N_k) + kappa(sl_N_{-k-2N}) = 0 for all N, k."""
        for N in range(2, 8):
            for k_val in [1, 2, -1, Fraction(1, 3)]:
                s = complementarity_sum(
                    "affine", lie_type="A", rank=N - 1, k=k_val
                )
                assert s == Fraction(0), f"sl_{N} at k={k_val}: got {s}"

    def test_affine_non_simply_laced_sum_is_zero(self):
        """kappa anti-symmetry for B_2, G_2, etc."""
        for (lt, rk) in [("B", 2), ("B", 3), ("C", 2), ("D", 4), ("G", 2)]:
            s = complementarity_sum("affine", lie_type=lt, rank=rk, k=1)
            assert s == Fraction(0), f"{lt}_{rk} at k=1: got {s}"

    def test_betagamma_sum_is_zero(self):
        """kappa(bg) + kappa(bc) = 0 for all lambda."""
        for lam_val in [Fraction(1, 2), 1, 2, Fraction(1, 3), 0]:
            assert complementarity_sum("betagamma", lam=lam_val) == Fraction(0)

    def test_w3_sum_is_250_over_3(self):
        """kappa(W_3_c) + kappa(W_3_{100-c}) = 250/3."""
        for c_val in [2, 50, 80, -10, Fraction(1, 7)]:
            s = complementarity_sum("w3", c=c_val)
            assert s == Fraction(250, 3), f"W_3 at c={c_val}: got {s}"

    def test_lattice_sum_is_zero(self):
        """kappa(V_Lambda) + kappa(V_Lambda!) = 0."""
        for rank_val in [1, 2, 8, 16, 24]:
            assert complementarity_sum("lattice", rank=rank_val) == Fraction(0)


# ========================================================================
# IV. Self-dual points
# ========================================================================


class TestSelfDualPoints:
    """Verify self-dual parameter values."""

    def test_virasoro_self_dual_at_c_13(self):
        """Virasoro is self-dual at c = 13, NOT c = 26."""
        sd = self_dual_point("virasoro")
        assert sd["value"] == Fraction(13)

    def test_virasoro_c_13_kappas_equal(self):
        """At c = 13: kappa = kappa! = 13/2."""
        assert kappa("virasoro", c=13) == Fraction(13, 2)
        assert kappa_dual("virasoro", c=13) == Fraction(13, 2)

    def test_virasoro_c_26_NOT_self_dual(self):
        """At c = 26: kappa = 13, kappa! = 0. NOT self-dual."""
        assert kappa("virasoro", c=26) == Fraction(13)
        assert kappa_dual("virasoro", c=26) == Fraction(0)
        assert kappa("virasoro", c=26) != kappa_dual("virasoro", c=26)

    def test_virasoro_self_dual_check_function(self):
        """Full self-dual check returns correct results."""
        vsd = virasoro_self_dual_check()
        assert vsd["c_13_is_self_dual"] is True
        assert vsd["c_26_is_self_dual"] is False
        assert vsd["correct_self_dual_point"] == Fraction(13)

    def test_w3_self_dual_at_c_50(self):
        """W_3 is self-dual at c = 50."""
        sd = self_dual_point("w3")
        assert sd["value"] == Fraction(50)
        assert kappa("w3", c=50) == kappa_dual("w3", c=50)

    def test_heisenberg_self_dual_at_k_0(self):
        """Heisenberg self-dual at k = 0 (degenerate)."""
        sd = self_dual_point("heisenberg")
        assert sd["value"] == Fraction(0)


# ========================================================================
# V. Genus-g complementarity
# ========================================================================


class TestGenusGComplementarity:
    """Verify F_g(A) + F_g(A!) = (kappa+kappa!) * lambda_g^FP."""

    def test_heisenberg_genus_g_sum_vanishes(self):
        """For Heisenberg: F_g(H_k) + F_g(H_{-k}) = 0 for all g."""
        for g in range(1, 8):
            r = genus_g_complementarity("heisenberg", g, k=3)
            assert r["verified"]
            assert r["F_g_sum"] == Fraction(0)

    def test_virasoro_genus_g_sum(self):
        """For Virasoro: F_g(Vir_c) + F_g(Vir_{26-c}) = 13 * lambda_g."""
        for g in range(1, 6):
            r = genus_g_complementarity("virasoro", g, c=7)
            assert r["verified"]
            assert r["F_g_sum"] == Fraction(13) * _lambda_fp(g)

    def test_virasoro_genus1_sum_is_13_over_24(self):
        """F_1(Vir_c) + F_1(Vir_{26-c}) = 13/24."""
        # lambda_1^FP = 1/24
        r = genus_g_complementarity("virasoro", 1, c=1)
        assert r["F_g_sum"] == Fraction(13, 24)

    def test_affine_sl2_genus_g_sum_vanishes(self):
        """For affine sl_2: F_g + F_g! = 0 for all g."""
        for g in range(1, 6):
            r = genus_g_complementarity(
                "affine", g, lie_type="A", rank=1, k=1
            )
            assert r["verified"]
            assert r["F_g_sum"] == Fraction(0)

    def test_w3_genus_g_sum(self):
        """For W_3: F_g + F_g! = (250/3) * lambda_g."""
        for g in range(1, 5):
            r = genus_g_complementarity("w3", g, c=20)
            assert r["verified"]
            assert r["F_g_sum"] == Fraction(250, 3) * _lambda_fp(g)

    def test_verify_all_genera(self):
        """Full genus-g verification for Virasoro up to genus 5."""
        r = verify_genus_g_complementarity("virasoro", max_g=5, c=10)
        assert r["all_verified"]

    def test_lattice_genus_g_sum_vanishes(self):
        """For lattice VOA: F_g + F_g! = 0 for all g."""
        for g in range(1, 5):
            r = genus_g_complementarity("lattice", g, rank=24)
            assert r["verified"]
            assert r["F_g_sum"] == Fraction(0)


# ========================================================================
# VI. Level independence
# ========================================================================


class TestLevelIndependence:
    """Verify that kappa + kappa! depends only on root datum, not level."""

    def test_sl2_level_independence(self):
        """For sl_2: kappa + kappa! = 0 at all levels."""
        r = complementarity_independent_of_level("A", rank=1)
        assert r["verified"]
        assert r["constant_value"] == Fraction(0)

    def test_sl3_level_independence(self):
        r = complementarity_independent_of_level("A", rank=2)
        assert r["verified"]
        assert r["constant_value"] == Fraction(0)

    def test_g2_level_independence(self):
        r = complementarity_independent_of_level("G", rank=2)
        assert r["verified"]
        assert r["constant_value"] == Fraction(0)

    def test_d4_level_independence(self):
        r = complementarity_independent_of_level("D", rank=4)
        assert r["verified"]
        assert r["constant_value"] == Fraction(0)

    def test_many_levels_sl5(self):
        """sl_5 at 7 different levels all give kappa + kappa! = 0."""
        levels = [1, 2, 3, 10, -1, Fraction(1, 3), Fraction(7, 11)]
        r = complementarity_independent_of_level("A", rank=4, test_levels=levels)
        assert r["verified"]
        assert r["all_equal"]


# ========================================================================
# VII. Central charge complementarity (W-algebra DS level)
# ========================================================================


class TestCentralChargeComplementarity:
    """Verify c + c' is constant under FF duality for DS reductions."""

    def test_virasoro_c_plus_c_is_26(self):
        """c(Vir, k) + c(Vir, k') = 26 for all k."""
        for k_val in [0, 1, 2, 3, -1, Fraction(1, 2), Fraction(7, 3)]:
            r = virasoro_central_charge_complementarity(Fraction(k_val))
            assert r["verified"], f"Failed at k = {k_val}"
            assert r["c_sum"] == Fraction(26)

    def test_w3_c_plus_c_is_100(self):
        """c(W_3, k) + c(W_3, k') = 100 for all k."""
        for k_val in [0, 1, 2, -1, Fraction(1, 2), Fraction(5, 7)]:
            r = w3_central_charge_complementarity(Fraction(k_val))
            assert r["verified"], f"Failed at k = {k_val}"
            assert r["c_sum"] == Fraction(100)

    def test_virasoro_c_at_k1(self):
        """c(k=1) = 1 - 6*4/3 = 1 - 8 = -7. c(k'=-5) = 1 - 6*16/(-3) = 1+32 = 33."""
        r = virasoro_central_charge_complementarity(Fraction(1))
        assert r["c_k"] == Fraction(-7)
        assert r["c_k_prime"] == Fraction(33)

    def test_w3_c_at_k0(self):
        """c(k=0) = 2 - 24*4/3 = 2 - 32 = -30."""
        r = w3_central_charge_complementarity(Fraction(0))
        assert r["c_k"] == Fraction(-30)
        assert r["c_k_prime"] == Fraction(130)


# ========================================================================
# VIII. Two-channel decomposition (affine)
# ========================================================================


class TestTwoChannelDecomposition:
    """Verify the two-channel decomposition of affine kappa."""

    def test_sl2_channels(self):
        """sl_2 at k=1: channel_1 = 3/4, channel_2 = 3/2."""
        r = affine_kappa_two_channel("A", 1, Fraction(1))
        assert r["channel_1"] == Fraction(3, 4)
        assert r["channel_2"] == Fraction(3, 2)
        assert r["kappa"] == Fraction(9, 4)

    def test_channel_sum_cancels(self):
        """Total sum of channels under FF duality is 0."""
        for N in range(2, 6):
            r = affine_kappa_two_channel("A", N - 1, Fraction(1))
            assert r["total_sum"] == Fraction(0)

    def test_channel_1_sum_is_neg_dim(self):
        """Channel 1 (k-dependent) sums to -dim under FF."""
        for N in range(2, 6):
            dim_g = N * N - 1
            r = affine_kappa_two_channel("A", N - 1, Fraction(1))
            assert r["channel_1_sum"] == -Fraction(dim_g)

    def test_channel_2_sum_is_dim(self):
        """Channel 2 (constant) sums to dim."""
        for N in range(2, 6):
            dim_g = N * N - 1
            r = affine_kappa_two_channel("A", N - 1, Fraction(1))
            assert r["channel_2_sum"] == Fraction(dim_g)


# ========================================================================
# IX. Lagrangian indicators
# ========================================================================


class TestLagrangianIndicators:
    """Verify Lagrangian complementarity indicators."""

    def test_virasoro_lagrangian(self):
        r = lagrangian_complementarity_check("virasoro", c=10)
        assert r["lagrangian_splitting_scalar"]
        assert r["sum"] == Fraction(13)

    def test_heisenberg_lagrangian(self):
        r = lagrangian_complementarity_check("heisenberg", k=5)
        assert r["lagrangian_splitting_scalar"]
        assert r["sum"] == Fraction(0)

    def test_w3_lagrangian(self):
        r = lagrangian_complementarity_check("w3", c=20)
        assert r["lagrangian_splitting_scalar"]
        assert r["sum"] == Fraction(250, 3)


# ========================================================================
# X. Full landscape verification
# ========================================================================


class TestFullLandscape:
    """Verify all families pass complementarity."""

    def test_complementarity_table_all_pass(self):
        """Every entry in the complementarity table is verified."""
        table = complementarity_table()
        assert len(table) > 20  # sanity: we have many entries
        for r in table:
            assert r["verified"], f"Failed: {r.get('family_display', r['family'])}"

    def test_all_families_complementary(self):
        """Full landscape: all standard families pass."""
        r = all_families_complementary()
        assert r["all_pass"], f"Failed families: {r['failed']}"
        assert r["total_checks"] >= 40

    def test_verify_scalar_returns_correct_structure(self):
        """verify_complementarity_scalar returns all expected keys."""
        r = verify_complementarity_scalar("virasoro", c=1)
        assert "kappa" in r
        assert "kappa_dual" in r
        assert "sum" in r
        assert "expected" in r
        assert "verified" in r


# ========================================================================
# XI. Exact arithmetic checks
# ========================================================================


class TestExactArithmetic:
    """Verify exact rational arithmetic throughout."""

    def test_lambda_fp_genus1(self):
        """lambda_1^FP = 1/24."""
        assert _lambda_fp(1) == Fraction(1, 24)

    def test_lambda_fp_genus2(self):
        """lambda_2^FP = 7/5760."""
        assert _lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_fp_genus3(self):
        """lambda_3^FP = 31/967680."""
        assert _lambda_fp(3) == Fraction(31, 967680)

    def test_F_g_linearity(self):
        """F_g(a*kappa) = a * F_g(kappa) (linearity in kappa)."""
        kap = Fraction(7, 3)
        a = Fraction(5, 11)
        for g in range(1, 6):
            assert _F_g(a * kap, g) == a * _F_g(kap, g)

    def test_sigma_sl2(self):
        """sigma(sl_2) = 1/2 (exponents: [1])."""
        assert _sigma_invariant("A", 1) == Fraction(1, 2)

    def test_sigma_sl3(self):
        """sigma(sl_3) = 1/2 + 1/3 = 5/6 (exponents: [1, 2])."""
        assert _sigma_invariant("A", 2) == Fraction(5, 6)

    def test_sigma_g2(self):
        """sigma(G_2) = 1/2 + 1/6 = 2/3 (exponents: [1, 5])."""
        assert _sigma_invariant("G", 2) == Fraction(2, 3)

    def test_lie_dim_hdual_sl2(self):
        """sl_2: dim = 3, h^v = 2."""
        assert _lie_dim_hdual("A", 1) == (3, 2)

    def test_lie_dim_hdual_e8(self):
        """e_8: dim = 248, h^v = 30."""
        assert _lie_dim_hdual("E", 8) == (248, 30)

    def test_all_kappas_are_fractions(self):
        """Every kappa computation returns an exact Fraction."""
        families_params = [
            ("heisenberg", {"k": 3}),
            ("virasoro", {"c": 7}),
            ("affine", {"lie_type": "A", "rank": 1, "k": 1}),
            ("betagamma", {"lam": Fraction(1, 2)}),
            ("w3", {"c": 10}),
            ("lattice", {"rank": 8}),
        ]
        for fam, params in families_params:
            k = kappa(fam, **params)
            assert isinstance(k, Fraction), f"{fam}: got {type(k)}"


# ========================================================================
# XII. Edge cases and pitfalls
# ========================================================================


class TestEdgeCases:
    """Edge cases, critical pitfalls, and degenerate parameters."""

    def test_heisenberg_not_self_dual(self):
        """H_k is NOT self-dual for k != 0: kappa(H_k) = k != -k = kappa(H_k!)."""
        assert kappa("heisenberg", k=1) != kappa_dual("heisenberg", k=1)

    def test_virasoro_c0_dual_is_c26(self):
        """Vir_0! = Vir_26 (c=0 -> c=26)."""
        d = ff_dual_parameters("virasoro", c=0)
        assert d["c"] == Fraction(26)

    def test_negative_kappa(self):
        """kappa can be negative (e.g., H_{-1}, or affine at negative level)."""
        assert kappa("heisenberg", k=-1) == Fraction(-1)
        # sl_2 at k = -1: kappa = 3(-1+2)/4 = 3/4 > 0
        assert kappa("affine", lie_type="A", rank=1, k=-1) == Fraction(3, 4)
        # sl_2 at k = -3: kappa = 3(-3+2)/4 = -3/4 < 0
        assert kappa("affine", lie_type="A", rank=1, k=-3) == Fraction(-3, 4)

    def test_fractional_level(self):
        """Complementarity works at fractional levels (admissible levels)."""
        s = complementarity_sum("affine", lie_type="A", rank=1, k=Fraction(-1, 2))
        assert s == Fraction(0)

    def test_large_rank_lattice(self):
        """Complementarity at rank 24 (Leech lattice)."""
        assert complementarity_sum("lattice", rank=24) == Fraction(0)
        assert kappa("lattice", rank=24) == Fraction(12)

    def test_betagamma_standard_weight(self):
        """Standard bg system at lam = 1: c = 2, kappa = 1."""
        assert kappa("betagamma", lam=1) == Fraction(1)
        assert kappa_dual("betagamma", lam=1) == Fraction(-1)
        assert complementarity_sum("betagamma", lam=1) == Fraction(0)

    def test_unknown_family_raises(self):
        """Unknown family raises ValueError."""
        with pytest.raises(ValueError, match="Unknown family"):
            kappa("unknown_family", k=1)


# ========================================================================
# XIII. kappa DERIVED from OPE data (not hardcoded)
# ========================================================================


class TestKappaFromOPE:
    """Verify kappa is correctly derived from OPE product coefficients."""

    def test_heisenberg_kappa_from_ope(self):
        """kappa(H_k) = alpha_{(1)} alpha = k, derived from OPE."""
        assert kappa_from_ope("heisenberg", k=1) == Fraction(1)
        assert kappa_from_ope("heisenberg", k=3) == Fraction(3)
        assert kappa_from_ope("heisenberg", k=-5) == Fraction(-5)
        assert kappa_from_ope("heisenberg", k=Fraction(1, 2)) == Fraction(1, 2)

    def test_virasoro_kappa_from_ope(self):
        """kappa(Vir_c) = T_{(3)} T = c/2, derived from OPE."""
        assert kappa_from_ope("virasoro", c=1) == Fraction(1, 2)
        assert kappa_from_ope("virasoro", c=26) == Fraction(13)
        assert kappa_from_ope("virasoro", c=13) == Fraction(13, 2)

    def test_affine_sl2_kappa_from_ope(self):
        """kappa(sl_2_k) derived from J_{(1)} J OPE + one-loop shift."""
        result = kappa_from_ope("affine", lie_type="A", rank=1, k=1)
        assert result == Fraction(9, 4)

    def test_affine_sl3_kappa_from_ope(self):
        """kappa(sl_3_k) derived from OPE."""
        result = kappa_from_ope("affine", lie_type="A", rank=2, k=1)
        assert result == Fraction(16, 3)

    def test_betagamma_kappa_from_ope(self):
        """kappa(bg) derived from beta-gamma OPE."""
        assert kappa_from_ope("betagamma", lam=Fraction(1, 2)) == Fraction(-1, 2)
        assert kappa_from_ope("betagamma", lam=1) == Fraction(1)

    def test_w3_kappa_from_ope(self):
        """kappa(W_3) = c * sigma(sl_3) = 5c/6, derived from OPE."""
        assert kappa_from_ope("w3", c=6) == Fraction(5)
        assert kappa_from_ope("w3", c=12) == Fraction(10)

    def test_lattice_kappa_from_ope(self):
        """kappa(V_Lambda) = rank/2, derived from pairing trace."""
        assert kappa_from_ope("lattice", rank=1) == Fraction(1, 2)
        assert kappa_from_ope("lattice", rank=8) == Fraction(4)
        assert kappa_from_ope("lattice", rank=24) == Fraction(12)

    def test_ope_matches_formula_all_families(self):
        """kappa_from_ope matches kappa (formula) for all standard families."""
        test_cases = [
            ("heisenberg", {"k": 3}),
            ("heisenberg", {"k": Fraction(-7, 3)}),
            ("virasoro", {"c": 7}),
            ("virasoro", {"c": Fraction(7, 10)}),
            ("affine", {"lie_type": "A", "rank": 1, "k": 1}),
            ("affine", {"lie_type": "A", "rank": 2, "k": 2}),
            ("affine", {"lie_type": "A", "rank": 4, "k": 1}),
            ("affine", {"lie_type": "B", "rank": 2, "k": 1}),
            ("affine", {"lie_type": "G", "rank": 2, "k": 1}),
            ("betagamma", {"lam": Fraction(1, 2)}),
            ("betagamma", {"c": -2}),
            ("w3", {"c": 50}),
            ("lattice", {"rank": 24}),
        ]
        for fam, params in test_cases:
            k_formula = kappa(fam, **params)
            k_ope = kappa_from_ope(fam, **params)
            assert k_formula == k_ope, (
                f"{fam}({params}): formula={k_formula}, ope={k_ope}"
            )


# ========================================================================
# XIV. kappa! DERIVED from Feigin-Frenkel involution
# ========================================================================


class TestKappaDualDerived:
    """Verify kappa! is correctly derived from FF dual + OPE re-evaluation."""

    def test_heisenberg_dual_derived(self):
        """kappa!(H_k) = -k derived via FF then OPE."""
        r = kappa_dual_derived("heisenberg", k=3)
        assert r["match"]
        assert r["kappa_dual_from_ope"] == Fraction(-3)

    def test_virasoro_dual_derived(self):
        """kappa!(Vir_c) = (26-c)/2 derived via FF then OPE."""
        r = kappa_dual_derived("virasoro", c=1)
        assert r["match"]
        assert r["kappa_dual_from_ope"] == Fraction(25, 2)

    def test_virasoro_self_dual_derived(self):
        """At c=13: kappa! = 13/2 = kappa."""
        r = kappa_dual_derived("virasoro", c=13)
        assert r["match"]
        assert r["kappa_dual_from_ope"] == Fraction(13, 2)

    def test_affine_sl2_dual_derived(self):
        """kappa!(sl_2_k) derived via FF k'=-k-4 then OPE."""
        r = kappa_dual_derived("affine", lie_type="A", rank=1, k=1)
        assert r["match"]

    def test_affine_sl3_dual_derived(self):
        r = kappa_dual_derived("affine", lie_type="A", rank=2, k=1)
        assert r["match"]

    def test_betagamma_dual_derived(self):
        r = kappa_dual_derived("betagamma", lam=1)
        assert r["match"]

    def test_w3_dual_derived(self):
        r = kappa_dual_derived("w3", c=20)
        assert r["match"]

    def test_lattice_dual_derived(self):
        r = kappa_dual_derived("lattice", rank=8)
        assert r["match"]

    def test_dual_derived_matches_all_families(self):
        """kappa_dual_derived matches for ALL standard families."""
        test_cases = [
            ("heisenberg", {"k": Fraction(1, 2)}),
            ("virasoro", {"c": Fraction(7, 10)}),
            ("affine", {"lie_type": "A", "rank": 3, "k": 2}),
            ("betagamma", {"lam": Fraction(3, 2)}),
            ("w3", {"c": 80}),
            ("lattice", {"rank": 16}),
        ]
        for fam, params in test_cases:
            r = kappa_dual_derived(fam, **params)
            assert r["match"], f"{fam}({params}): mismatch"


# ========================================================================
# XV. OPE product coefficients
# ========================================================================


class TestOPEProduct:
    """Verify individual OPE product coefficients."""

    def test_heisenberg_ope_r1(self):
        """alpha_{(1)} alpha = k."""
        assert _ope_product("heisenberg", 1, k=5) == Fraction(5)

    def test_heisenberg_ope_r0(self):
        """alpha_{(0)} alpha = 0 (no regular part from pairing)."""
        assert _ope_product("heisenberg", 0, k=5) == Fraction(0)

    def test_virasoro_ope_r3(self):
        """T_{(3)} T = c/2."""
        assert _ope_product("virasoro", 3, c=26) == Fraction(13)

    def test_virasoro_ope_r1(self):
        """T_{(1)} T = 2 (conformal weight coefficient)."""
        assert _ope_product("virasoro", 1, c=26) == Fraction(2)

    def test_affine_ope_r1(self):
        """J^a_{(1)} J^b = k (per-generator)."""
        assert _ope_product("affine", 1, lie_type="A", rank=1, k=3) == Fraction(3)


# ========================================================================
# XVI. Genus-g complementarity from graph sums
# ========================================================================


class TestGraphSumComplementarity:
    """Verify F_g(A) + F_g(A!) via independent graph sums and Hodge-weighted computation."""

    def test_heisenberg_genus1_hodge_complementarity(self):
        """F_1(H_k) + F_1(H_{-k}) = 0 from Hodge-weighted computation."""
        r = genus_g_complementarity_graph_sum("heisenberg", 1, k=3)
        assert r["complementarity_verified"]
        assert r["F_g_sum"] == Fraction(0)

    def test_virasoro_genus1_hodge_complementarity(self):
        """F_1(Vir_c) + F_1(Vir_{26-c}) = 13 * lambda_1 from Hodge-weighted."""
        r = genus_g_complementarity_graph_sum("virasoro", 1, c=7)
        assert r["complementarity_verified"]
        assert r["F_g_sum"] == Fraction(13) * _lambda_fp(1)

    def test_affine_sl2_genus1_hodge_complementarity(self):
        """F_1(sl_2_k) + F_1(sl_2_{k'}) = 0 from Hodge-weighted."""
        r = genus_g_complementarity_graph_sum(
            "affine", 1, lie_type="A", rank=1, k=1
        )
        assert r["complementarity_verified"]
        assert r["F_g_sum"] == Fraction(0)

    def test_virasoro_genus2_hodge_complementarity(self):
        """Genus 2 Hodge-weighted complementarity for Virasoro."""
        r = genus_g_complementarity_graph_sum("virasoro", 2, c=10)
        assert r["complementarity_verified"]
        assert r["n_graphs"] > 1  # genus 2 has multiple graphs

    def test_w3_genus1_hodge_complementarity(self):
        """W_3 Hodge-weighted complementarity at genus 1."""
        r = genus_g_complementarity_graph_sum("w3", 1, c=20)
        assert r["complementarity_verified"]
        assert r["F_g_sum"] == Fraction(250, 3) * _lambda_fp(1)

    def test_lattice_genus1_hodge_complementarity(self):
        """Lattice Hodge-weighted complementarity."""
        r = genus_g_complementarity_graph_sum("lattice", 1, rank=24)
        assert r["complementarity_verified"]

    def test_graph_sum_polynomial_computed(self):
        """Graph-sum polynomial is computed from stable graph enumeration."""
        r = genus_g_complementarity_graph_sum("virasoro", 1, c=10)
        assert "graph_sum_polynomial" in r
        assert len(r["graph_sum_polynomial"]) > 0

    def test_genus2_has_multiple_graphs(self):
        """At genus 2, the graph-sum polynomial has multiple terms."""
        r = genus_g_complementarity_graph_sum("virasoro", 2, c=5)
        poly = r["graph_sum_polynomial"]
        assert len(poly) >= 2, f"Expected >= 2 terms, got {len(poly)}"

    def test_genus3_complementarity(self):
        """Genus 3 Hodge-weighted complementarity."""
        r = genus_g_complementarity_graph_sum("virasoro", 3, c=5)
        assert r["complementarity_verified"]
        assert r["n_graphs"] >= 5

    def test_heisenberg_all_genera_hodge(self):
        """Heisenberg: F_g + F_g! = 0 at all genera via Hodge-weighted."""
        for g in range(1, 4):
            r = genus_g_complementarity_graph_sum("heisenberg", g, k=2)
            assert r["complementarity_verified"], f"genus {g} failed"
            assert r["F_g_sum"] == Fraction(0), f"genus {g} sum != 0"


# ========================================================================
# XVII. Lagrangian complementarity COMPUTED (Gram matrix)
# ========================================================================


class TestLagrangianComputed:
    """Verify Lagrangian complementarity from computed Gram matrices."""

    def test_virasoro_gram_matrix(self):
        """Virasoro: Gram matrix computed, cross pairings match."""
        r = lagrangian_complementarity_computed("virasoro", max_genus=3, c=10)
        assert r["all_cross_pairings_match"]
        assert r["all_both_nonzero"]

    def test_heisenberg_gram_matrix(self):
        """Heisenberg: Gram matrix computed."""
        r = lagrangian_complementarity_computed("heisenberg", max_genus=3, k=5)
        assert r["all_cross_pairings_match"]
        assert r["all_both_nonzero"]

    def test_affine_gram_matrix(self):
        """Affine: Gram matrix, cross pairing = 0."""
        r = lagrangian_complementarity_computed(
            "affine", max_genus=2, lie_type="A", rank=1, k=1
        )
        assert r["all_cross_pairings_match"]

    def test_scalar_gram_rank_one(self):
        """Scalar Gram matrix has rank 1 (F_g and F_g! proportional)."""
        r = lagrangian_complementarity_computed("virasoro", max_genus=2, c=10)
        for g, gr in r["genus_results"].items():
            assert gr["scalar_rank"] == 1, f"genus {g}: expected rank 1"

    def test_gram_determinant_zero_scalar(self):
        """Scalar Gram det = 0 (both vectors proportional to lambda_g)."""
        r = lagrangian_complementarity_computed("virasoro", max_genus=2, c=7)
        for g, gr in r["genus_results"].items():
            assert gr["gram_det"] == Fraction(0)

    def test_cross_pairing_equals_sum_times_lambda(self):
        """Cross pairing F_g + F_g! = (kappa+kappa!) * lambda_g."""
        r = lagrangian_complementarity_computed("w3", max_genus=3, c=50)
        for g, gr in r["genus_results"].items():
            assert gr["cross_match"], f"genus {g}: cross pairing mismatch"

    def test_degenerate_case_kappa_zero(self):
        """When kappa = 0 (Heisenberg k=0): both_nonzero is False."""
        r = lagrangian_complementarity_computed("heisenberg", max_genus=1, k=0)
        assert not r["all_both_nonzero"]
