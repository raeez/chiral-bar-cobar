"""Tests for primitive modular master-kernel profiles and metaplectic shadows.

Verifies:
  - Primitive kernel component structure for all standard families
  - Shell equation stratification by regime
  - W3 quartic coefficient 16/(22+5c)
  - Metaplectic half-density squares to spectral determinant
  - Profile table consistency
"""
import pytest
from sympy import Matrix, Rational, Symbol, expand, simplify

from compute.lib.modular_master import (
    AFFINE_SL2,
    HEISENBERG,
    PROFILES,
    VIRASORO,
    W3,
    determinant_series,
    formal_metaplectic_half_density,
    get_profile,
    profile_table,
    w3_quartic_factor,
)


# ── Primitive kernel structure ──────────────────────────────────

class TestPrimitiveKernel:
    def test_heisenberg_kernel(self):
        k = HEISENBERG.primitive_kernel()
        assert k == ("K02", "K11")

    def test_affine_kernel(self):
        k = AFFINE_SL2.primitive_kernel()
        assert k == ("K02", "K03", "K11")

    def test_virasoro_kernel(self):
        k = VIRASORO.primitive_kernel()
        assert "K04" in k
        assert "Rpf2" in k
        assert "Rpf3" in k

    def test_w3_kernel(self):
        k = W3.primitive_kernel()
        assert k == ("K02", "K03", "K04", "K11", "Rpf2", "Rpf3")

    def test_all_profiles_have_K02_K11(self):
        for name, p in PROFILES.items():
            k = p.primitive_kernel()
            assert "K02" in k, f"{name} missing K02"
            assert "K11" in k, f"{name} missing K11"


# ── Regime classification ───────────────────────────────────────

class TestRegime:
    def test_heisenberg_pure_quadratic(self):
        assert HEISENBERG.regime() == "pure quadratic"

    def test_affine_cubic_tree(self):
        assert AFFINE_SL2.regime() == "cubic-tree"

    def test_virasoro_quartic_rigid(self):
        assert VIRASORO.regime() == "quartic-rigid"

    def test_w3_quartic_rigid(self):
        assert W3.regime() == "quartic-rigid"


# ── Shell equations ─────────────────────────────────────────────

class TestShellEquations:
    def test_heisenberg_g2_pure_loop(self):
        g2 = HEISENBERG.genus_two_forcing()
        assert g2 == ("Delta(K11)",)

    def test_affine_g2_adds_bracket(self):
        g2 = AFFINE_SL2.genus_two_forcing()
        assert "Delta(K11)" in g2
        assert "1/2[K11,K11]" in g2
        assert len(g2) == 2

    def test_virasoro_g2_all_channels(self):
        g2 = VIRASORO.genus_two_forcing()
        assert len(g2) == 3
        assert "Rpf2(K02)" in g2

    def test_heisenberg_g3_pure_loop(self):
        g3 = HEISENBERG.genus_three_forcing()
        assert g3 == ("Delta(K2.)",)

    def test_affine_g3_adds_bracket_and_triple(self):
        g3 = AFFINE_SL2.genus_three_forcing()
        assert "Delta(K2.)" in g3
        assert "[K11,K2.]" in g3
        assert "1/6[K11,K11,K11]" in g3

    def test_virasoro_g3_all_channels(self):
        g3 = VIRASORO.genus_three_forcing()
        assert "Rpf2(K11)" in g3
        assert "Rpf3(K02)" in g3


# ── Master action terms ─────────────────────────────────────────

class TestMasterAction:
    def test_heisenberg_purely_quadratic(self):
        terms = HEISENBERG.master_action_terms()
        assert terms == ("S2",)

    def test_affine_cubic(self):
        terms = AFFINE_SL2.master_action_terms()
        assert terms == ("S2", "S3")

    def test_w3_quartic_with_rigid(self):
        terms = W3.master_action_terms()
        assert "S4" in terms
        assert "Sigma2" in terms
        assert "Sigma3" in terms


# ── QME shells ──────────────────────────────────────────────────

class TestQMEShells:
    def test_heisenberg_shells(self):
        shells = HEISENBERG.qme_shells()
        assert "K03=0" in shells
        assert "dK11=0" in shells
        assert "K04=0" in shells

    def test_affine_shells(self):
        shells = AFFINE_SL2.qme_shells()
        assert "dK03=0" in shells
        assert "dK11+Delta_ns(K03)=0" in shells
        assert "K04=0" in shells

    def test_virasoro_shells(self):
        shells = VIRASORO.qme_shells()
        assert "dK04+K03*K03=0" in shells


# ── W3 quartic factor ──────────────────────────────────────────

class TestW3Quartic:
    def test_rational_value(self):
        c = Symbol("c")
        f = w3_quartic_factor(c)
        assert simplify(f - 16 / (22 + 5 * c)) == 0

    def test_numeric_c_eq_2(self):
        f = w3_quartic_factor(2)
        assert f == Rational(1, 2)

    def test_pole_at_minus_22_over_5(self):
        from sympy import zoo, oo, nan
        c = Rational(-22, 5)
        result = w3_quartic_factor(c)
        assert result in (zoo, oo, -oo, nan) or not result.is_finite


# ── Metaplectic half-density ────────────────────────────────────

class TestMetaplecticHalfDensity:
    def test_rank1_squaring(self):
        """delta(x)^2 = det(1 - xT) for rank-1 operator."""
        x = Symbol("x")
        T = Matrix([[Rational(1, 3)]])
        delta = formal_metaplectic_half_density(T, x, 5)
        det_series = determinant_series(T, x, 5)
        diff = expand(delta**2 - det_series)
        # Truncate to order 5
        for k in range(6):
            assert diff.coeff(x, k) == 0

    def test_rank2_squaring(self):
        """delta(x)^2 = det(1 - xT) for rank-2 operator."""
        x = Symbol("x")
        T = Matrix([[Rational(1, 2), Rational(1, 4)],
                     [0, Rational(1, 3)]])
        delta = formal_metaplectic_half_density(T, x, 4)
        det_series = determinant_series(T, x, 4)
        diff = expand(delta**2 - det_series)
        for k in range(5):
            assert diff.coeff(x, k) == 0

    def test_identity_operator(self):
        """Half-density of identity: exp(1/2 * log(1-x)) = (1-x)^{1/2}."""
        x = Symbol("x")
        T = Matrix([[1]])
        delta = formal_metaplectic_half_density(T, x, 4)
        det_series = determinant_series(T, x, 4)
        diff = expand(delta**2 - det_series)
        for k in range(5):
            assert diff.coeff(x, k) == 0

    def test_nonsquare_raises(self):
        x = Symbol("x")
        T = Matrix([[1, 2, 3], [4, 5, 6]])
        with pytest.raises(ValueError):
            formal_metaplectic_half_density(T, x, 3)


# ── Profile table ───────────────────────────────────────────────

class TestProfileTable:
    def test_all_profiles_present(self):
        table = profile_table()
        assert len(table) == 4

    def test_get_profile(self):
        p = get_profile("heisenberg")
        assert p is HEISENBERG

    def test_branch_ranks(self):
        assert HEISENBERG.branch_rank == 1
        assert AFFINE_SL2.branch_rank == 2
        assert VIRASORO.branch_rank == 2
        assert W3.branch_rank == 3
