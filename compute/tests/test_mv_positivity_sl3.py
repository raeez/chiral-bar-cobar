"""Tests for MV positivity of Y(sl₃) asymptotic characters (task B8).

Verifies:
1. sl₃ Weyl character formula and Freudenthal weight multiplicities
2. Tensor product decomposition (LR coefficients) non-negativity
3. Yangian bar dimensions compatibility with conjectured generating functions
4. Bar Euler characteristic compatibility with MV positivity
5. MV cone membership for adjoint tensor characters
6. Koszul dual dimension positivity

Cross-references:
  - sl3_casimir_decomp.py: Casimir eigenspace data
  - yangian_bar.py: Y(sl₂) bar cohomology
  - concordance.tex: MC3 status (DK-2/3 for fd type A)
"""

import pytest
import numpy as np

from compute.lib.mv_positivity_sl3 import (
    # Root system
    CARTAN_MATRIX,
    POSITIVE_ROOTS,
    RHO,
    weyl_reflect_s1,
    weyl_reflect_s2,
    weyl_orbit,
    weight_inner_product,
    weight_norm_sq,
    pairing_weight_root,
    root_to_dynkin,
    # Characters
    sl3_irrep_dim,
    weyl_character,
    character_dim,
    weight_multiplicities,
    # Tensor products
    tensor_product_character,
    decompose_character,
    littlewood_richardson,
    # MV cone
    mv_basis_small_weights,
    build_mv_cone_matrix,
    check_mv_positivity,
    # Bar data
    SL3_BAR_DIMS,
    YSL2_BAR_DIMS,
    bar_euler_characteristic,
    bar_euler_chars_partial,
    # Asymptotic characters
    adjoint_tensor_character,
    adjoint_tensor_decomp,
    # Koszul dual
    koszul_dual_dims,
    koszul_dual_positivity_check,
    # Verification
    verify_lr_nonnegativity,
    verify_adjoint_decomp_positivity,
    verify_bar_euler_mv_compatibility,
)


# ============================================================
# Root system
# ============================================================

class TestRootSystem:
    def test_cartan_matrix(self):
        """Cartan matrix of sl₃ is [[2,-1],[-1,2]]."""
        expected = np.array([[2, -1], [-1, 2]])
        np.testing.assert_array_equal(CARTAN_MATRIX, expected)

    def test_cartan_determinant(self):
        """det(A) = 3 for sl₃."""
        assert int(np.linalg.det(CARTAN_MATRIX).round()) == 3

    def test_positive_roots_count(self):
        """sl₃ has 3 positive roots."""
        assert len(POSITIVE_ROOTS) == 3

    def test_rho(self):
        """ρ = ω₁ + ω₂ = (1, 1) in Dynkin coords."""
        assert RHO == (1, 1)

    def test_rho_norm_squared(self):
        """⟨ρ, ρ⟩ = ⟨ω₁+ω₂, ω₁+ω₂⟩ = (2+1+1+2)/3 = 2."""
        assert abs(weight_norm_sq(RHO) - 2.0) < 1e-12


class TestWeylReflections:
    def test_s1_on_omega1(self):
        """s₁(ω₁) = ω₁ - α₁ = ω₁ - (2ω₁-ω₂) = -ω₁+ω₂ = (-1, 1)."""
        assert weyl_reflect_s1(1, 0) == (-1, 1)

    def test_s2_on_omega2(self):
        """s₂(ω₂) = ω₂ - α₂ = ω₂ - (-ω₁+2ω₂) = ω₁-ω₂ = (1, -1)."""
        assert weyl_reflect_s2(0, 1) == (1, -1)

    def test_s1_involution(self):
        """s₁² = id."""
        for a, b in [(1, 0), (0, 1), (1, 1), (2, 1), (3, 0)]:
            result = weyl_reflect_s1(*weyl_reflect_s1(a, b))
            assert result == (a, b)

    def test_s2_involution(self):
        """s₂² = id."""
        for a, b in [(1, 0), (0, 1), (1, 1), (2, 1), (3, 0)]:
            result = weyl_reflect_s2(*weyl_reflect_s2(a, b))
            assert result == (a, b)

    def test_s1s2s1_equals_s2s1s2(self):
        """Braid relation: s₁s₂s₁ = s₂s₁s₂ (S₃ presentation)."""
        for a, b in [(1, 0), (0, 1), (1, 1), (2, 1)]:
            lhs = weyl_reflect_s1(*weyl_reflect_s2(*weyl_reflect_s1(a, b)))
            rhs = weyl_reflect_s2(*weyl_reflect_s1(*weyl_reflect_s2(a, b)))
            assert lhs == rhs


class TestWeylOrbit:
    def test_trivial(self):
        """Weyl orbit of (0,0) is just {(0,0)}."""
        assert weyl_orbit(0, 0) == [(0, 0)]

    def test_fundamental(self):
        """Orbit of ω₁ has 3 elements (= dim V(1,0))."""
        orbit = weyl_orbit(1, 0)
        assert len(orbit) == 3

    def test_adjoint(self):
        """Orbit of ω₁+ω₂ has 6 elements (= |W| since stabilizer is trivial)."""
        orbit = weyl_orbit(1, 1)
        assert len(orbit) == 6

    def test_symmetric_rep(self):
        """Orbit of 2ω₁ has 3 elements (same stabilizer as ω₁)."""
        orbit = weyl_orbit(2, 0)
        assert len(orbit) == 3


class TestWeightInnerProduct:
    def test_omega1_norm(self):
        """⟨ω₁, ω₁⟩ = 2/3."""
        assert abs(weight_norm_sq((1, 0)) - 2.0 / 3) < 1e-12

    def test_omega2_norm(self):
        """⟨ω₂, ω₂⟩ = 2/3."""
        assert abs(weight_norm_sq((0, 1)) - 2.0 / 3) < 1e-12

    def test_omega12_inner(self):
        """⟨ω₁, ω₂⟩ = 1/3."""
        assert abs(weight_inner_product((1, 0), (0, 1)) - 1.0 / 3) < 1e-12

    def test_alpha1_norm(self):
        """⟨α₁, α₁⟩ = 2 (for sl₃ with normalized roots).
        α₁ = (2, -1) in Dynkin coords."""
        alpha1_dynkin = root_to_dynkin((1, 0))
        assert alpha1_dynkin == (2, -1)
        assert abs(weight_norm_sq(alpha1_dynkin) - 2.0) < 1e-12

    def test_pairing_omega_alpha(self):
        """⟨ω₁, α₁⟩ = 1 (defining property of fundamental weights)."""
        assert abs(pairing_weight_root((1, 0), (1, 0)) - 1.0) < 1e-12
        assert abs(pairing_weight_root((1, 0), (0, 1)) - 0.0) < 1e-12
        assert abs(pairing_weight_root((0, 1), (1, 0)) - 0.0) < 1e-12
        assert abs(pairing_weight_root((0, 1), (0, 1)) - 1.0) < 1e-12


# ============================================================
# Weyl character and weight multiplicities
# ============================================================

class TestWeylDimensionFormula:
    @pytest.mark.parametrize("a,b,expected", [
        (0, 0, 1), (1, 0, 3), (0, 1, 3), (1, 1, 8),
        (2, 0, 6), (0, 2, 6), (3, 0, 10), (0, 3, 10),
        (2, 1, 15), (1, 2, 15), (2, 2, 27),
        (3, 1, 24), (1, 3, 24), (4, 0, 15), (0, 4, 15),
        (4, 1, 35), (1, 4, 35), (3, 3, 64),
        (5, 0, 21), (0, 5, 21),
    ])
    def test_dim(self, a, b, expected):
        assert sl3_irrep_dim(a, b) == expected

    def test_negative_weight(self):
        """V(a,b) with a<0 or b<0 has dimension 0."""
        assert sl3_irrep_dim(-1, 0) == 0
        assert sl3_irrep_dim(0, -1) == 0


class TestWeylCharacter:
    @pytest.mark.parametrize("a,b", [
        (0, 0), (1, 0), (0, 1), (1, 1),
        (2, 0), (0, 2), (3, 0), (0, 3),
        (2, 1), (1, 2), (2, 2),
    ])
    def test_dim_matches(self, a, b):
        """Character total dimension matches Weyl formula."""
        char = weyl_character(a, b)
        assert character_dim(char) == sl3_irrep_dim(a, b)

    def test_trivial(self):
        """V(0,0) = trivial, character is {(0,0): 1}."""
        char = weyl_character(0, 0)
        assert char == {(0, 0): 1}

    def test_fundamental(self):
        """V(1,0) has weights (1,0), (-1,1), (0,-1) each with mult 1."""
        char = weyl_character(1, 0)
        assert len(char) == 3
        assert all(m == 1 for m in char.values())

    def test_adjoint_zero_weight(self):
        """V(1,1) has zero weight (0,0) with multiplicity 2 (rank of sl₃)."""
        char = weyl_character(1, 1)
        assert char[(0, 0)] == 2

    def test_adjoint_nonzero_weights(self):
        """V(1,1): all 6 non-zero weights have multiplicity 1."""
        char = weyl_character(1, 1)
        nonzero = {mu: m for mu, m in char.items() if mu != (0, 0)}
        assert len(nonzero) == 6
        assert all(m == 1 for m in nonzero.values())

    def test_v20_weights(self):
        """V(2,0) (symmetric square of fund) has dim 6."""
        char = weyl_character(2, 0)
        assert character_dim(char) == 6
        # Highest weight (2,0) with mult 1
        assert char[(2, 0)] == 1

    @pytest.mark.parametrize("a,b", [
        (1, 0), (0, 1), (1, 1), (2, 0), (2, 1), (3, 0), (2, 2),
    ])
    def test_all_multiplicities_positive(self, a, b):
        """All weight multiplicities are positive integers."""
        char = weyl_character(a, b)
        assert all(m > 0 and isinstance(m, int) for m in char.values())

    @pytest.mark.parametrize("a,b", [
        (1, 0), (0, 1), (1, 1), (2, 0), (2, 1), (3, 0),
    ])
    def test_weyl_orbit_invariance(self, a, b):
        """Weight multiplicities are constant on Weyl orbits."""
        char = weyl_character(a, b)
        # Check that weights in the same Weyl orbit have the same mult
        checked = set()
        for mu, m in char.items():
            if mu in checked:
                continue
            orbit = weyl_orbit(mu[0], mu[1])
            for mu2 in orbit:
                if mu2 in char:
                    assert char[mu2] == m, (
                        f"V({a},{b}): weights {mu} and {mu2} in same orbit "
                        f"but mults {m} and {char[mu2]} differ"
                    )
                    checked.add(mu2)


class TestFreudenthalSpecific:
    """Specific weight multiplicity tests against known values."""

    def test_v22_zero_weight(self):
        """V(2,2): m(0,0) = 3 (rank + 1 correction for higher reps)."""
        # Actually: the zero weight mult for V(2,2) can be computed.
        # V(2,2) has dim 27. The zero weight space has dim = 3.
        char = weyl_character(2, 2)
        # The number of weights at (0,0) for V(a,a) is min(a+1, rank+1)
        # For a=2, rank=2: min(3, 3) = 3.
        assert char[(0, 0)] == 3

    def test_v30_zero_weight(self):
        """V(3,0): m(0,0) = 1 (only one copy of trivial in S³(fund))."""
        char = weyl_character(3, 0)
        # V(3,0) = S³(V(1,0)). Zero weight mult = 1.
        assert char.get((0, 0), 0) == 1

    def test_v21_highest_weight(self):
        """Highest weight always has multiplicity 1."""
        char = weyl_character(2, 1)
        assert char[(2, 1)] == 1


# ============================================================
# Tensor products and Littlewood-Richardson
# ============================================================

class TestTensorProduct:
    def test_fund_x_antifund(self):
        """V(1,0) ⊗ V(0,1) = V(1,1) + V(0,0) [3 × 3 = 8 + 1]."""
        lr = littlewood_richardson((1, 0), (0, 1))
        assert lr == {(1, 1): 1, (0, 0): 1}

    def test_fund_x_fund(self):
        """V(1,0) ⊗ V(1,0) = V(2,0) + V(0,1) [3 × 3 = 6 + 3]."""
        lr = littlewood_richardson((1, 0), (1, 0))
        assert lr == {(2, 0): 1, (0, 1): 1}

    def test_adj_x_adj(self):
        """V(1,1) ⊗ V(1,1) = V(0,0) + 2·V(1,1) + V(3,0) + V(0,3) + V(2,2).

        8 × 8 = 1 + 2·8 + 10 + 10 + 27 = 64.
        """
        lr = littlewood_richardson((1, 1), (1, 1))
        assert lr[(0, 0)] == 1
        assert lr[(1, 1)] == 2
        assert lr[(3, 0)] == 1
        assert lr[(0, 3)] == 1
        assert lr[(2, 2)] == 1
        dim_sum = sum(n * sl3_irrep_dim(a, b) for (a, b), n in lr.items())
        assert dim_sum == 64

    def test_v20_x_v01(self):
        """V(2,0) ⊗ V(0,1) = V(2,1) + V(1,0) [6 × 3 = 15 + 3]."""
        lr = littlewood_richardson((2, 0), (0, 1))
        assert lr == {(2, 1): 1, (1, 0): 1}

    def test_v20_x_v02(self):
        """V(2,0) ⊗ V(0,2) = V(2,2) + V(1,1) + V(0,0) [6 × 6 = 27 + 8 + 1]."""
        lr = littlewood_richardson((2, 0), (0, 2))
        assert lr == {(2, 2): 1, (1, 1): 1, (0, 0): 1}

    def test_dimension_conservation(self):
        """dim(V₁ ⊗ V₂) = Σ N^ν dim(V(ν)) for several examples."""
        pairs = [
            ((1, 0), (1, 0)), ((1, 0), (0, 1)), ((1, 1), (1, 0)),
            ((2, 0), (1, 0)), ((2, 0), (0, 2)), ((1, 1), (1, 1)),
            ((2, 1), (1, 0)), ((3, 0), (0, 1)),
        ]
        for lam1, lam2 in pairs:
            lr = littlewood_richardson(lam1, lam2)
            dim_prod = sl3_irrep_dim(*lam1) * sl3_irrep_dim(*lam2)
            dim_sum = sum(n * sl3_irrep_dim(a, b) for (a, b), n in lr.items())
            assert dim_prod == dim_sum, (
                f"V{lam1} x V{lam2}: {dim_prod} != {dim_sum}"
            )


class TestLRNonNegativity:
    def test_max_sum_3(self):
        """All LR coefficients non-negative for a+b ≤ 3."""
        result = verify_lr_nonnegativity(3)
        assert result["all_nonneg"] is True
        assert result["n_pairs_tested"] > 0
        assert len(result["violations"]) == 0

    def test_max_sum_4(self):
        """All LR coefficients non-negative for a+b ≤ 4."""
        result = verify_lr_nonnegativity(4)
        assert result["all_nonneg"] is True

    @pytest.mark.slow
    def test_max_sum_5(self):
        """All LR coefficients non-negative for a+b ≤ 5."""
        result = verify_lr_nonnegativity(5)
        assert result["all_nonneg"] is True


# ============================================================
# Adjoint tensor decomposition
# ============================================================

class TestAdjointTensorDecomp:
    def test_n1(self):
        """g^{⊗1} = V(1,1) (adjoint)."""
        decomp = adjoint_tensor_decomp(1)
        assert decomp == {(1, 1): 1}

    def test_n2(self):
        """g^{⊗2} = V(0,0) + 2·V(1,1) + V(3,0) + V(0,3) + V(2,2)."""
        decomp = adjoint_tensor_decomp(2)
        assert decomp[(0, 0)] == 1
        assert decomp[(1, 1)] == 2
        assert decomp[(3, 0)] == 1
        assert decomp[(0, 3)] == 1
        assert decomp[(2, 2)] == 1
        total = sum(m * sl3_irrep_dim(a, b) for (a, b), m in decomp.items())
        assert total == 64

    def test_n3_dim(self):
        """g^{⊗3} has total dimension 512."""
        decomp = adjoint_tensor_decomp(3)
        total = sum(m * sl3_irrep_dim(a, b) for (a, b), m in decomp.items())
        assert total == 512

    def test_n3_all_positive(self):
        decomp = adjoint_tensor_decomp(3)
        assert all(m > 0 for m in decomp.values())

    @pytest.mark.slow
    def test_n4_dim(self):
        """g^{⊗4} has total dimension 4096."""
        decomp = adjoint_tensor_decomp(4)
        total = sum(m * sl3_irrep_dim(a, b) for (a, b), m in decomp.items())
        assert total == 4096

    def test_positivity_through_n3(self):
        """Adjoint tensor decomp has all positive coefficients through n=3."""
        result = verify_adjoint_decomp_positivity(3)
        for n in range(1, 4):
            assert result[n]["all_positive"] is True
            assert result[n]["dim_match"] is True


class TestAdjointDecompConsistency:
    """Cross-check adjoint tensor decomposition with sl3_casimir_decomp.py data."""

    def test_n2_matches_casimir_eigenspaces(self):
        """adj⊗adj decomposition matches Casimir eigenspace data from MEMORY.md.

        Casimir eigenspaces: {0:1, 18:16, 36:20, 48:27}
        Decomposition: V(0,0)=1, V(1,1)=8×2=16, V(3,0)+V(0,3)=10+10=20, V(2,2)=27
        """
        decomp = adjoint_tensor_decomp(2)
        # Casimir eigenvalue 0 -> V(0,0)
        assert decomp.get((0, 0), 0) * sl3_irrep_dim(0, 0) == 1
        # Casimir eigenvalue 18 -> V(1,1) × 2
        assert decomp.get((1, 1), 0) * sl3_irrep_dim(1, 1) == 16
        # Casimir eigenvalue 36 -> V(3,0) + V(0,3)
        ev36 = (decomp.get((3, 0), 0) * sl3_irrep_dim(3, 0) +
                decomp.get((0, 3), 0) * sl3_irrep_dim(0, 3))
        assert ev36 == 20
        # Casimir eigenvalue 48 -> V(2,2)
        assert decomp.get((2, 2), 0) * sl3_irrep_dim(2, 2) == 27

    def test_n3_matches_casimir(self):
        """adj^{⊗3} decomposition matches {0:2, 18:64, 36:80, 48:162, 72:140, 90:64}."""
        from compute.lib.sl3_casimir_decomp import sl3_casimir_eigenvalue
        decomp = adjoint_tensor_decomp(3)

        # Group by Casimir eigenvalue
        ev_to_dim: dict = {}
        for (a, b), mult in decomp.items():
            ev = sl3_casimir_eigenvalue(a, b)
            ev_to_dim[ev] = ev_to_dim.get(ev, 0) + mult * sl3_irrep_dim(a, b)

        expected = {0: 2, 18: 64, 36: 80, 48: 162, 72: 140, 90: 64}
        assert ev_to_dim == expected


# ============================================================
# Bar cohomology data
# ============================================================

class TestBarDims:
    def test_sl3_bar_dims_count(self):
        """sl₃ bar dims list has 8 entries (degrees 0-7)."""
        assert len(SL3_BAR_DIMS) == 8

    def test_sl3_bar_h0(self):
        assert SL3_BAR_DIMS[0] == 1

    def test_sl3_bar_h1(self):
        assert SL3_BAR_DIMS[1] == 8

    def test_sl3_bar_h2(self):
        assert SL3_BAR_DIMS[2] == 36

    def test_sl3_bar_h3(self):
        assert SL3_BAR_DIMS[3] == 204

    def test_sl3_bar_h4(self):
        """H⁴ = 1352 (from conjectured recurrence)."""
        assert SL3_BAR_DIMS[4] == 1352

    def test_sl3_recurrence(self):
        """sl₃ bar recurrence: a(n) = 11a(n-1) - 23a(n-2) - 8a(n-3)."""
        a = SL3_BAR_DIMS
        for n in range(3, len(a)):
            predicted = 11 * a[n - 1] - 23 * a[n - 2] - 8 * a[n - 3]
            assert a[n] == predicted, f"Recurrence fails at n={n}: {predicted} != {a[n]}"

    def test_ysl2_bar_dims_count(self):
        assert len(YSL2_BAR_DIMS) == 8

    def test_ysl2_formula(self):
        """Y(sl₂): H^n = 3^n + 1 for n ≥ 1."""
        for n in range(1, len(YSL2_BAR_DIMS)):
            assert YSL2_BAR_DIMS[n] == 3**n + 1


# ============================================================
# Koszul dual positivity
# ============================================================

class TestKoszulDualPositivity:
    def test_sl3_through_deg7(self):
        """All Koszul dual dims for sl₃ are positive through degree 7."""
        kd = koszul_dual_dims(SL3_BAR_DIMS)
        assert all(x > 0 for x in kd)

    def test_sl3_known_values(self):
        """Koszul dual dims match [1, 8, 28, 140, 392, ...]."""
        kd = koszul_dual_dims(SL3_BAR_DIMS)
        assert kd[:5] == [1, 8, 28, 140, 392]

    def test_sl3_deg0_1_classical(self):
        """Degrees 0-2 match classical exterior algebra C(8,n)."""
        from math import comb
        kd = koszul_dual_dims(SL3_BAR_DIMS)
        assert kd[0] == comb(8, 0)  # 1
        assert kd[1] == comb(8, 1)  # 8
        assert kd[2] == comb(8, 2)  # 28

    def test_sl3_chiral_excess_nonneg(self):
        """Chiral excess (A!)_n - C(8,n) ≥ 0 through degree 4."""
        from math import comb
        kd = koszul_dual_dims(SL3_BAR_DIMS)
        for n in range(5):
            excess = kd[n] - comb(8, n)
            assert excess >= 0, f"Negative chiral excess at degree {n}: {excess}"

    def test_sl3_chiral_excess_values(self):
        """Chiral excess = [0, 0, 0, 84, 322] through degree 4."""
        from math import comb
        kd = koszul_dual_dims(SL3_BAR_DIMS)
        excess = [kd[n] - comb(8, n) for n in range(5)]
        assert excess == [0, 0, 0, 84, 322]

    def test_ysl2_all_positive(self):
        """Y(sl₂) Koszul dual dims are all positive."""
        kd = koszul_dual_dims(YSL2_BAR_DIMS)
        assert all(x > 0 for x in kd)

    def test_ysl2_known_values(self):
        """Y(sl₂) Koszul dual matches [1, 4, 6, 12, 18, 36, 54, 108]."""
        kd = koszul_dual_dims(YSL2_BAR_DIMS)
        assert kd == [1, 4, 6, 12, 18, 36, 54, 108]

    def test_ysl2_pattern(self):
        """Y(sl₂) Koszul dual: even = 2·3^{n/2}, odd = 4·3^{(n-1)/2} for n ≥ 2."""
        kd = koszul_dual_dims(YSL2_BAR_DIMS)
        for n in range(2, len(kd)):
            if n % 2 == 0:
                assert kd[n] == 2 * 3 ** (n // 2)
            else:
                assert kd[n] == 4 * 3 ** ((n - 1) // 2)

    def test_koszul_product_identity(self):
        """H_A(t) · H_{A!}(-t) = 1 through degree 7 for sl₃."""
        a = SL3_BAR_DIMS
        kd = koszul_dual_dims(a)
        N = len(a)
        for k in range(N):
            prod_k = sum(
                a[i] * ((-1)**j) * kd[j]
                for i in range(k + 1)
                for j in [k - i]
                if 0 <= j < N
            )
            if k == 0:
                assert prod_k == 1
            else:
                assert prod_k == 0


class TestKoszulDualPositivityCheck:
    def test_sl3(self):
        result = koszul_dual_positivity_check(SL3_BAR_DIMS)
        assert result["all_positive"] is True

    def test_ysl2(self):
        result = koszul_dual_positivity_check(YSL2_BAR_DIMS)
        assert result["all_positive"] is True


# ============================================================
# Bar Euler characteristics
# ============================================================

class TestBarEulerCharacteristic:
    def test_sl3_partial_euler_n0(self):
        assert bar_euler_chars_partial(SL3_BAR_DIMS)[0] == 1

    def test_sl3_partial_euler_n1(self):
        # 1 - 8 = -7
        assert bar_euler_chars_partial(SL3_BAR_DIMS)[1] == -7

    def test_sl3_partial_euler_n2(self):
        # 1 - 8 + 36 = 29
        assert bar_euler_chars_partial(SL3_BAR_DIMS)[2] == 29

    def test_sl3_partial_euler_alternating(self):
        """Partial Euler chars alternate in sign for sl₃."""
        euler = bar_euler_chars_partial(SL3_BAR_DIMS)
        for i in range(len(euler)):
            expected_sign = (-1)**i
            actual_sign = 1 if euler[i] > 0 else -1
            assert actual_sign == expected_sign, (
                f"Sign at degree {i}: expected {expected_sign}, got {actual_sign}"
            )

    def test_ysl2_partial_euler_alternating(self):
        """Partial Euler chars alternate in sign for Y(sl₂)."""
        euler = bar_euler_chars_partial(YSL2_BAR_DIMS)
        for i in range(len(euler)):
            expected_sign = (-1)**i
            actual_sign = 1 if euler[i] > 0 else -1
            assert actual_sign == expected_sign

    def test_ysl2_partial_euler_formula(self):
        """Y(sl₂) partial Euler: χ_N = Σ_{n=0}^{N} (-1)^n (3^n + 1).

        For n ≥ 1: Σ (-1)^n 3^n = -(3 - 3² + ... ± 3^N) = -3(1-(-3)^N)/(1+3).
        Plus Σ (-1)^n = ±1.
        Total: 1 + (-3 + 9 - 27 + ...) + (-1 + 1 - 1 + ...)
        """
        euler = bar_euler_chars_partial(YSL2_BAR_DIMS)
        for N in range(len(euler)):
            expected = sum((-1)**n * YSL2_BAR_DIMS[n] for n in range(N + 1))
            assert euler[N] == expected

    def test_growth_bounded_sl3(self):
        """Growth ratio |χ_N| / H^N is bounded for sl₃."""
        result = verify_bar_euler_mv_compatibility(SL3_BAR_DIMS)
        assert result["growth_bounded"] is True

    def test_growth_bounded_ysl2(self):
        """Growth ratio |χ_N| / H^N is bounded for Y(sl₂)."""
        result = verify_bar_euler_mv_compatibility(YSL2_BAR_DIMS)
        assert result["growth_bounded"] is True


# ============================================================
# MV cone membership
# ============================================================

class TestMVCone:
    def test_adjoint_in_cone(self):
        """V(1,1) character lies in MV cone (trivially)."""
        basis = mv_basis_small_weights(3)
        char = weyl_character(1, 1)
        result = check_mv_positivity(char, basis)
        assert result["is_mv_positive"]
        assert result["decomposition"] == {(1, 1): 1}

    def test_adj_tensor2_in_cone(self):
        """g^{⊗2} character lies in MV cone."""
        basis = mv_basis_small_weights(4)
        char = adjoint_tensor_character(2)
        result = check_mv_positivity(char, basis)
        assert result["is_mv_positive"]
        # Decomposition should match adj ⊗ adj
        assert result["decomposition"][(1, 1)] == 2
        assert result["decomposition"][(0, 0)] == 1

    def test_adj_tensor3_in_cone(self):
        """g^{⊗3} character lies in MV cone.

        g^{⊗3} contains V(3,3) (a+b=6), so basis must include max_sum >= 6.
        """
        basis = mv_basis_small_weights(6)
        char = adjoint_tensor_character(3)
        result = check_mv_positivity(char, basis)
        assert result["is_mv_positive"]

    def test_irreducible_in_cone(self):
        """Every irreducible character trivially lies in MV cone."""
        basis = mv_basis_small_weights(4)
        for a in range(4):
            for b in range(4 - a):
                char = weyl_character(a, b)
                result = check_mv_positivity(char, basis)
                assert result["is_mv_positive"], (
                    f"V({a},{b}) not in MV cone"
                )

    def test_mv_cone_matrix_shape(self):
        """MV cone matrix has correct shape."""
        basis = mv_basis_small_weights(3)
        M, weights = build_mv_cone_matrix(basis)
        # Columns = number of basis irreps
        assert M.shape[1] == len(basis)
        # Rows = number of weights appearing
        assert M.shape[0] == len(weights)
        assert M.shape[0] > 0

    def test_mv_cone_matrix_nonneg(self):
        """All entries of MV cone matrix are non-negative (weight mults ≥ 0)."""
        basis = mv_basis_small_weights(3)
        M, _ = build_mv_cone_matrix(basis)
        assert np.all(M >= 0)


# ============================================================
# Comprehensive positivity verification
# ============================================================

class TestComprehensiveLR:
    """Comprehensive Littlewood-Richardson non-negativity."""

    @pytest.mark.parametrize("a1,b1,a2,b2", [
        (1, 0, 1, 0), (1, 0, 0, 1), (1, 0, 1, 1),
        (0, 1, 0, 1), (0, 1, 1, 1),
        (1, 1, 1, 1),
        (2, 0, 1, 0), (2, 0, 0, 1), (2, 0, 1, 1), (2, 0, 2, 0),
        (0, 2, 1, 0), (0, 2, 0, 1),
        (3, 0, 1, 0), (3, 0, 0, 1),
        (2, 1, 1, 0), (2, 1, 0, 1), (2, 1, 1, 1),
        (1, 2, 1, 0), (1, 2, 0, 1),
    ])
    def test_lr_nonneg(self, a1, b1, a2, b2):
        """LR coefficients for V(a₁,b₁) ⊗ V(a₂,b₂) are non-negative."""
        lr = littlewood_richardson((a1, b1), (a2, b2))
        for nu, coeff in lr.items():
            assert coeff > 0, (
                f"Negative LR coeff: V({a1},{b1}) x V({a2},{b2}) -> "
                f"V{nu} with coeff {coeff}"
            )
        # Dimension check
        dim_prod = sl3_irrep_dim(a1, b1) * sl3_irrep_dim(a2, b2)
        dim_sum = sum(n * sl3_irrep_dim(a, b) for (a, b), n in lr.items())
        assert dim_prod == dim_sum


class TestBarCompatibility:
    """Bar cohomology compatibility with representation theory."""

    def test_sl3_h1_equals_dim_g(self):
        """H¹(B(sl₃)) = dim(sl₃) = 8."""
        assert SL3_BAR_DIMS[1] == 8

    def test_sl3_h2_equals_adj_tensor2_invariant_plus_relations(self):
        """H² = 36 = C(8,2) + 8 = 28 + 8 (classical + chiral correction).

        Actually: 36 is the chiral bar cohomology, which counts
        the quadratic OPE relations. For classical U(g):
        H² = C(8,2) = 28 (antisymmetric part).
        The extra 8 comes from the Killing form (double pole in OPE).
        """
        from math import comb
        classical = comb(8, 2)  # 28
        assert SL3_BAR_DIMS[2] == 36
        assert SL3_BAR_DIMS[2] - classical == 8  # = dim(g)

    def test_ysl2_h1_equals_total_generators(self):
        """H¹(B(Y(sl₂))) = 4 = dim(sl₂) + 1 (level 0 + spectral parameter)."""
        assert YSL2_BAR_DIMS[1] == 4


class TestMVPositivitySummary:
    """Summary tests: everything passes."""

    def test_all_weyl_dims_match(self):
        """All Weyl character dimensions match the formula for a+b ≤ 5."""
        for a in range(6):
            for b in range(6 - a):
                char = weyl_character(a, b)
                assert character_dim(char) == sl3_irrep_dim(a, b)

    def test_sl3_koszul_dual_positive(self):
        assert koszul_dual_positivity_check(SL3_BAR_DIMS)["all_positive"] is True

    def test_ysl2_koszul_dual_positive(self):
        assert koszul_dual_positivity_check(YSL2_BAR_DIMS)["all_positive"] is True

    def test_sl3_euler_alternating(self):
        """Partial Euler characters strictly alternate in sign."""
        euler = bar_euler_chars_partial(SL3_BAR_DIMS)
        for i, val in enumerate(euler):
            assert val != 0
            assert (val > 0) == (i % 2 == 0)

    def test_ysl2_euler_alternating(self):
        euler = bar_euler_chars_partial(YSL2_BAR_DIMS)
        for i, val in enumerate(euler):
            assert val != 0
            assert (val > 0) == (i % 2 == 0)

    def test_adj_tensors_mv_positive(self):
        """g^{⊗n} characters lie in MV cone for n = 1, 2, 3."""
        basis = mv_basis_small_weights(6)  # need max_sum=6 for V(3,3) in g^{⊗3}
        for n in range(1, 4):
            char = adjoint_tensor_character(n)
            result = check_mv_positivity(char, basis)
            assert result["is_mv_positive"], f"g^{n} not MV-positive"
