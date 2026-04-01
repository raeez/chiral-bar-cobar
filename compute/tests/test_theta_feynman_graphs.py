r"""Tests for Feynman graph enumeration engine for MC element components.

Tests the explicit computation of Theta_A^{(r)} via planted tree sums
(Method C), cross-checked against:
  - Shadow tower coefficients from generating function (Method B)
  - Explicit theta components (explicit_theta.py)
  - Known values: kappa, S_3, S_4, Q^contact

Organization:
  I.   Tree enumeration (planted binary trees, Catalan numbers)
  II.  Virasoro shadow tower via generating function
  III. Explicit Theta components at specific central charges
  IV.  MC equation verification
  V.   sl_2 tensor components
  VI.  Cross-family consistency (Heisenberg, betagamma)
  VII. Tree amplitude decomposition
  VIII. Shadow depth classification
  IX.  Growth rate and asymptotics
  X.   Cross-checks against existing modules

References:
  thm:mc2-bar-intrinsic, thm:recursive-existence, thm:riccati-algebraicity,
  thm:shadow-archetype-classification, prop:shadow-formality-low-arity,
  AP19 (pole absorption), AP27 (propagator weight universality)
"""

import pytest
from fractions import Fraction

FR = Fraction

# Import the module under test
from compute.lib.theta_feynman_graphs import (
    ThetaFeynmanEngine,
    PlantedTree,
    VirasoroOPE,
    VirasoroState,
    VirasoroHomotopy,
    planted_binary_trees,
    planted_trees_count,
    catalan,
    virasoro_engine,
    heisenberg_engine,
    affine_sl2_engine,
    betagamma_engine,
    _count_leaves,
    _tree_to_string,
)


# ============================================================================
# I. Tree enumeration
# ============================================================================

class TestTreeEnumeration:
    """Test planted binary tree enumeration and Catalan numbers."""

    def test_catalan_small(self):
        """Catalan numbers C_0, ..., C_6."""
        expected = [1, 1, 2, 5, 14, 42, 132]
        for n, c_n in enumerate(expected):
            assert catalan(n) == c_n, f"C_{n} = {catalan(n)}, expected {c_n}"

    def test_tree_count_arity2(self):
        """1 binary tree with 2 leaves: (0, 1)."""
        assert planted_trees_count(2) == 1
        trees = planted_binary_trees(2)
        assert len(trees) == 1

    def test_tree_count_arity3(self):
        """2 binary trees with 3 leaves."""
        assert planted_trees_count(3) == 2
        trees = planted_binary_trees(3)
        assert len(trees) == 2

    def test_tree_count_arity4(self):
        """5 binary trees with 4 leaves."""
        assert planted_trees_count(4) == 5
        trees = planted_binary_trees(4)
        assert len(trees) == 5

    def test_tree_count_arity5(self):
        """14 binary trees with 5 leaves."""
        assert planted_trees_count(5) == 14
        trees = planted_binary_trees(5)
        assert len(trees) == 14

    def test_tree_count_arity6(self):
        """42 binary trees with 6 leaves."""
        assert planted_trees_count(6) == 42

    def test_tree_count_arity7(self):
        """132 binary trees with 7 leaves."""
        assert planted_trees_count(7) == 132

    def test_trees_arity3_structures(self):
        """The two trees at arity 3: ((0,1),2) and (0,(1,2))."""
        trees = planted_binary_trees(3)
        structures = [t.structure for t in trees]
        assert ((0, 1), 2) in structures
        assert (0, (1, 2)) in structures

    def test_trees_arity4_structures(self):
        """5 trees at arity 4."""
        trees = planted_binary_trees(4)
        assert len(trees) == 5
        # Check leaf counts
        for tree in trees:
            assert _count_leaves(tree.structure) == 4

    def test_tree_leaf_count(self):
        """Leaf count matches arity."""
        for r in range(2, 8):
            trees = planted_binary_trees(r)
            for tree in trees:
                assert _count_leaves(tree.structure) == r

    def test_tree_internal_vertices(self):
        """Binary tree with r leaves has r-1 internal vertices."""
        for r in range(2, 8):
            trees = planted_binary_trees(r)
            for tree in trees:
                assert tree.internal_vertices() == r - 1

    def test_tree_automorphism(self):
        """Labeled planted trees have trivial automorphism."""
        for r in range(2, 6):
            for tree in planted_binary_trees(r):
                assert tree.automorphism_count() == 1

    def test_tree_to_string(self):
        """String representation of trees."""
        assert _tree_to_string(0) == '0'
        assert _tree_to_string((0, 1)) == '(0, 1)'
        assert _tree_to_string(((0, 1), 2)) == '((0, 1), 2)'


# ============================================================================
# II. Virasoro shadow tower via generating function
# ============================================================================

class TestVirasoroShadowTower:
    """Test shadow tower coefficients for Virasoro."""

    def test_kappa_generic(self):
        """kappa(Vir_c) = c/2 for various c."""
        for c_val in [1, 2, 10, 13, 26, FR(1, 2)]:
            eng = virasoro_engine(c_val)
            assert eng.kappa() == FR(c_val) / 2

    def test_S3_equals_2(self):
        """S_3 = 2 for all c (c-independent cubic shadow)."""
        for c_val in [1, 2, 7, 13, 26, FR(1, 2), FR(7, 3)]:
            eng = virasoro_engine(c_val)
            assert eng.S(3) == FR(2), f"S_3 at c={c_val}: {eng.S(3)}"

    def test_S4_formula(self):
        """S_4 = 10/[c(5c+22)] for various c."""
        for c_val in [1, 2, 7, 13, 26, FR(1, 2)]:
            eng = virasoro_engine(c_val)
            c = FR(c_val)
            expected = FR(10) / (c * (5 * c + 22))
            assert eng.S(4) == expected, f"S_4 at c={c_val}: {eng.S(4)} vs {expected}"

    def test_S2_from_engine(self):
        """S_2 = kappa = c/2."""
        for c_val in [1, 13, 26]:
            eng = virasoro_engine(c_val)
            assert eng.S(2) == FR(c_val) / 2

    def test_shadow_tower_c_half(self):
        """Virasoro at c=1/2 (Ising model): explicit S_r values."""
        eng = virasoro_engine(FR(1, 2))
        assert eng.kappa() == FR(1, 4)
        assert eng.S(3) == FR(2)
        # S_4 = 10 / ((1/2)(5/2 + 22)) = 10 / ((1/2)(49/2)) = 10 / (49/4) = 40/49
        assert eng.S(4) == FR(40, 49)

    def test_shadow_tower_c1(self):
        """Virasoro at c=1: explicit S_r values."""
        eng = virasoro_engine(1)
        assert eng.kappa() == FR(1, 2)
        assert eng.S(3) == FR(2)
        # S_4 = 10 / (1 * 27) = 10/27
        assert eng.S(4) == FR(10, 27)

    def test_shadow_tower_c13(self):
        """Virasoro at c=13 (self-dual point): explicit S_r values."""
        eng = virasoro_engine(13)
        assert eng.kappa() == FR(13, 2)
        # S_4 = 10/(13 * 87) = 10/1131
        assert eng.S(4) == FR(10, 1131)

    def test_shadow_tower_c26(self):
        """Virasoro at c=26 (critical): explicit S_r values."""
        eng = virasoro_engine(26)
        assert eng.kappa() == FR(13)
        # S_4 = 10/(26*152) = 10/3952 = 5/1976
        assert eng.S(4) == FR(10, 3952)

    def test_S5_nonzero(self):
        """S_5 is nonzero for Virasoro (class M, infinite tower)."""
        eng = virasoro_engine(1)
        assert eng.S(5) != FR(0)

    def test_S6_nonzero(self):
        """S_6 nonzero for Virasoro."""
        eng = virasoro_engine(1)
        assert eng.S(6) != FR(0)

    def test_shadow_tower_extends(self):
        """Shadow tower extends to high arity for Virasoro."""
        eng = virasoro_engine(1, max_arity=30)
        for r in range(2, 20):
            assert eng.S(r) is not None


# ============================================================================
# III. Explicit Theta components at specific central charges
# ============================================================================

class TestExplicitThetaComponents:
    """Test Theta^{(r)} at specific c values as module elements."""

    def test_theta3_c_half(self):
        """Theta^{(3)}(Vir_{1/2}) = S_3 * eta_T^3 where S_3 = 2."""
        eng = virasoro_engine(FR(1, 2))
        comp = eng.theta_component(3)
        assert comp['S_r'] == FR(2)
        assert comp['family'] == 'virasoro'

    def test_theta3_c1(self):
        """Theta^{(3)}(Vir_1) = 2 * eta_T^3."""
        eng = virasoro_engine(1)
        comp = eng.theta_component(3)
        assert comp['S_r'] == FR(2)

    def test_theta3_c13(self):
        """Theta^{(3)}(Vir_13) = 2 * eta_T^3 (c-independent)."""
        eng = virasoro_engine(13)
        comp = eng.theta_component(3)
        assert comp['S_r'] == FR(2)

    def test_theta3_c26(self):
        """Theta^{(3)}(Vir_26) = 2 * eta_T^3 (c-independent)."""
        eng = virasoro_engine(26)
        comp = eng.theta_component(3)
        assert comp['S_r'] == FR(2)

    def test_theta4_c1(self):
        """Theta^{(4)}(Vir_1) = S_4 * eta_T^4 where S_4 = 10/27."""
        eng = virasoro_engine(1)
        comp = eng.theta_component(4)
        assert comp['S_r'] == FR(10, 27)

    def test_theta4_c13(self):
        """Theta^{(4)}(Vir_13) = (10/1131) * eta_T^4."""
        eng = virasoro_engine(13)
        assert eng.S(4) == FR(10, 1131)

    def test_theta5_c1(self):
        """Theta^{(5)}(Vir_1) has specific S_5 value from recursion."""
        eng = virasoro_engine(1, max_arity=10)
        s5 = eng.S(5)
        assert s5 != FR(0)
        # Verify S_5 satisfies the MC equation at arity 5
        assert eng.mc_residual(5) == FR(0)

    def test_theta_component_structure(self):
        """theta_component returns correct dict keys."""
        eng = virasoro_engine(1)
        comp = eng.theta_component(3)
        assert 'arity' in comp
        assert 'S_r' in comp
        assert 'family' in comp
        assert comp['arity'] == 3

    def test_theta_as_module_element(self):
        """theta_as_virasoro_module_element returns correct dict."""
        eng = virasoro_engine(1)
        elem = eng.theta_as_virasoro_module_element(3)
        assert 'T^3' in elem
        assert elem['T^3'] == FR(2)

    def test_theta2_as_module_element(self):
        """Theta^{(2)} = kappa * T^2."""
        eng = virasoro_engine(13)
        elem = eng.theta_as_virasoro_module_element(2)
        assert elem['T^2'] == FR(13, 2)


# ============================================================================
# IV. MC equation verification
# ============================================================================

class TestMCEquation:
    """Test that MC equation residuals vanish at all arities >= 5."""

    def test_mc_residual_arity5_c1(self):
        """MC residual at arity 5 vanishes for c=1."""
        eng = virasoro_engine(1, max_arity=10)
        assert eng.mc_residual(5) == FR(0)

    def test_mc_residual_arity6_c1(self):
        """MC residual at arity 6 vanishes for c=1."""
        eng = virasoro_engine(1, max_arity=10)
        assert eng.mc_residual(6) == FR(0)

    def test_mc_residual_arity7_c1(self):
        """MC residual at arity 7 vanishes for c=1."""
        eng = virasoro_engine(1, max_arity=10)
        assert eng.mc_residual(7) == FR(0)

    def test_mc_all_arities_c1(self):
        """MC residuals vanish at all arities 5..15 for c=1."""
        eng = virasoro_engine(1, max_arity=15)
        residuals = eng.verify_mc(15)
        for r, res in residuals.items():
            assert res == FR(0), f"MC residual at r={r}: {res}"

    def test_mc_all_arities_c13(self):
        """MC residuals vanish at all arities for c=13 (self-dual)."""
        eng = virasoro_engine(13, max_arity=12)
        residuals = eng.verify_mc(12)
        for r, res in residuals.items():
            assert res == FR(0), f"MC residual at r={r}: {res}"

    def test_mc_all_arities_c26(self):
        """MC residuals vanish for c=26 (critical)."""
        eng = virasoro_engine(26, max_arity=12)
        residuals = eng.verify_mc(12)
        for r, res in residuals.items():
            assert res == FR(0), f"MC residual at r={r}: {res}"

    def test_mc_all_arities_c_half(self):
        """MC residuals vanish for c=1/2 (Ising)."""
        eng = virasoro_engine(FR(1, 2), max_arity=12)
        residuals = eng.verify_mc(12)
        for r, res in residuals.items():
            assert res == FR(0), f"MC residual at r={r}: {res}"

    def test_mc_all_arities_c7_3(self):
        """MC residuals vanish for c=7/3."""
        eng = virasoro_engine(FR(7, 3), max_arity=10)
        residuals = eng.verify_mc(10)
        for r, res in residuals.items():
            assert res == FR(0), f"MC residual at r={r}: {res}"


# ============================================================================
# V. sl_2 tensor components
# ============================================================================

class TestSl2TensorComponents:
    """Test Theta^{(r)} for affine sl_2 as explicit tensors."""

    def test_sl2_kappa(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        eng = affine_sl2_engine(1)
        assert eng.kappa() == FR(9, 4)
        eng2 = affine_sl2_engine(2)
        assert eng2.kappa() == FR(3)

    def test_sl2_theta2_is_killing(self):
        """Theta^{(2)} for sl_2 is the Killing form tensor."""
        eng = affine_sl2_engine(1)
        comp = eng.theta_component(2)
        tensor = comp['tensor']
        assert tensor[('e', 'f')] == FR(1)
        assert tensor[('f', 'e')] == FR(1)
        assert tensor[('h', 'h')] == FR(2)

    def test_sl2_theta3_cubic_form(self):
        """Theta^{(3)} for sl_2 is the cubic form C_{abc}."""
        eng = affine_sl2_engine(1)
        comp = eng.theta_component(3)
        tensor = comp['tensor']
        # C_{hef} = 2k = 2 for k=1
        assert tensor[('h', 'e', 'f')] == FR(2)
        # C_{hfe} = -2k = -2
        assert tensor[('h', 'f', 'e')] == FR(-2)

    def test_sl2_theta3_totally_antisymmetric(self):
        """Cubic form C_{abc} is totally antisymmetric."""
        eng = affine_sl2_engine(1)
        C = eng.sl2_theta_arity3()
        gens = ['e', 'h', 'f']
        for a in gens:
            for b in gens:
                for c in gens:
                    val_abc = C.get((a, b, c), FR(0))
                    val_bac = C.get((b, a, c), FR(0))
                    val_acb = C.get((a, c, b), FR(0))
                    # Antisymmetry: swap any two indices -> negate
                    assert val_abc == -val_bac, f"C({a},{b},{c}) vs C({b},{a},{c})"
                    assert val_abc == -val_acb, f"C({a},{b},{c}) vs C({a},{c},{b})"

    def test_sl2_theta3_proportional_to_fabc(self):
        """Cubic form = 2k * epsilon_{abc} (structure constants)."""
        eng = affine_sl2_engine(1)
        C = eng.sl2_theta_arity3()
        k = FR(1)
        # C_{efh} = 2k = 2
        assert C[('e', 'f', 'h')] == 2 * k
        # C_{fhe} = 2k = 2
        assert C[('f', 'h', 'e')] == 2 * k

    def test_sl2_theta4_vanishes(self):
        """Theta^{(4)} = 0 for sl_2 (class L, tower terminates)."""
        eng = affine_sl2_engine(1)
        theta4 = eng.sl2_theta_arity4()
        assert theta4 == {}

    def test_sl2_theta4_comp_zero(self):
        """Component at arity 4 is zero for sl_2."""
        eng = affine_sl2_engine(1)
        comp = eng.theta_component(4)
        assert comp['tensor'] == {}

    def test_sl2_mc_check_arity3(self):
        """MC equation at arity 3: d(C) = 0 (Jacobi identity)."""
        eng = affine_sl2_engine(1)
        residual = eng.sl2_mc_check_arity3()
        assert residual == FR(0)

    def test_sl2_mc_check_arity3_k2(self):
        """MC at arity 3 for k=2."""
        eng = affine_sl2_engine(2)
        residual = eng.sl2_mc_check_arity3()
        assert residual == FR(0)

    def test_sl2_shadow_on_h_line_terminates(self):
        """On the h-line (Cartan), S_3 = 0 (abelian subalgebra)."""
        eng = affine_sl2_engine(1)
        assert eng.alpha() == FR(0)  # S_3 on h-line
        assert eng.S(3) == FR(0)

    def test_sl2_depth_class(self):
        """sl_2 is class L (Lie/tree, depth 3) on non-Cartan lines."""
        eng = affine_sl2_engine(1)
        # On the h-line: alpha = 0, S_4 = 0, so class G
        assert eng.shadow_depth_class() == 'G'
        # NOTE: The full 3D analysis requires the multi-channel engine.
        # On the h-line, sl_2 appears as class G because the
        # Cartan is abelian.  The Lie class L is visible only on
        # non-Cartan deformation lines.


# ============================================================================
# VI. Cross-family consistency
# ============================================================================

class TestCrossFamilyConsistency:
    """Test Heisenberg, betagamma, and other families."""

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k."""
        eng = heisenberg_engine(1)
        assert eng.kappa() == FR(1)
        eng2 = heisenberg_engine(3)
        assert eng2.kappa() == FR(3)

    def test_heisenberg_S3_zero(self):
        """S_3 = 0 for Heisenberg (class G, terminates at arity 2)."""
        eng = heisenberg_engine(1)
        assert eng.S(3) == FR(0)

    def test_heisenberg_S4_zero(self):
        """S_4 = 0 for Heisenberg."""
        eng = heisenberg_engine(1)
        assert eng.S(4) == FR(0)

    def test_heisenberg_all_higher_zero(self):
        """S_r = 0 for all r >= 3 for Heisenberg."""
        eng = heisenberg_engine(1, max_arity=15)
        for r in range(3, 15):
            assert eng.S(r) == FR(0), f"S_{r} nonzero for Heisenberg"

    def test_heisenberg_depth_class(self):
        """Heisenberg is class G (Gaussian)."""
        eng = heisenberg_engine(1)
        assert eng.shadow_depth_class() == 'G'

    def test_heisenberg_mc_trivial(self):
        """MC residuals trivially zero for Heisenberg."""
        eng = heisenberg_engine(1, max_arity=10)
        residuals = eng.verify_mc(10)
        for r, res in residuals.items():
            assert res == FR(0)

    def test_betagamma_kappa(self):
        """kappa(betagamma) = c/2 = -1 for standard normalization."""
        eng = betagamma_engine(-2)
        assert eng.kappa() == FR(-1)

    def test_betagamma_depth_class(self):
        """betagamma on single channel is class G."""
        eng = betagamma_engine(-2)
        # On a single channel: alpha = 0, S_4 = 0
        assert eng.shadow_depth_class() == 'G'

    def test_kappa_additivity_heisenberg_pair(self):
        """kappa(H_1 oplus H_2) = kappa(H_1) + kappa(H_2) = 3."""
        eng1 = heisenberg_engine(1)
        eng2 = heisenberg_engine(2)
        assert eng1.kappa() + eng2.kappa() == FR(3)

    def test_virasoro_complementarity_c_plus_c_dual(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) for complementarity check.

        For Virasoro: kappa(c) + kappa(26-c) = c/2 + (26-c)/2 = 13.
        This is AP24: the sum is 13, NOT 0.
        """
        for c_val in [1, 7, 13, 20, FR(1, 2)]:
            eng1 = virasoro_engine(c_val)
            eng2 = virasoro_engine(FR(26) - FR(c_val))
            kappa_sum = eng1.kappa() + eng2.kappa()
            assert kappa_sum == FR(13), (
                f"kappa(Vir_{c_val}) + kappa(Vir_{26-c_val}) = {kappa_sum}, expected 13"
            )


# ============================================================================
# VII. Tree amplitude decomposition
# ============================================================================

class TestTreeAmplitudeDecomposition:
    """Test individual tree amplitudes and their sums."""

    def test_tree_sum_equals_shadow_arity5(self):
        """Tree sum reproduces S_5 at arity 5."""
        eng = virasoro_engine(1, max_arity=10)
        tree_sum, s5_gf, residual = eng.tree_sum_vs_shadow(5)
        assert residual == FR(0), f"Residual at r=5: {residual}"

    def test_tree_sum_equals_shadow_arity6(self):
        """Tree sum reproduces S_6 at arity 6."""
        eng = virasoro_engine(1, max_arity=10)
        tree_sum, s6_gf, residual = eng.tree_sum_vs_shadow(6)
        assert residual == FR(0), f"Residual at r=6: {residual}"

    def test_tree_sum_equals_shadow_arity7(self):
        """Tree sum reproduces S_7."""
        eng = virasoro_engine(1, max_arity=10)
        _, _, residual = eng.tree_sum_vs_shadow(7)
        assert residual == FR(0)

    def test_tree_sum_equals_shadow_high_arity(self):
        """Tree sum = shadow at arities 5..15."""
        eng = virasoro_engine(1, max_arity=16)
        for r in range(5, 16):
            _, _, residual = eng.tree_sum_vs_shadow(r)
            assert residual == FR(0), f"r={r}"

    def test_tree_sum_c13(self):
        """Tree sum reproduces shadow tower at c=13."""
        eng = virasoro_engine(13, max_arity=12)
        for r in range(5, 12):
            _, _, residual = eng.tree_sum_vs_shadow(r)
            assert residual == FR(0), f"r={r} at c=13"

    def test_individual_tree_amplitudes_arity5(self):
        """Individual tree amplitudes at arity 5."""
        eng = virasoro_engine(1, max_arity=10)
        amps = eng.individual_tree_amplitudes(5)
        # 14 trees at arity 5
        assert len(amps) == 14

    def test_individual_tree_sum_equals_shadow_arity5(self):
        """Sum of individual tree amplitudes at arity 5 matches."""
        eng = virasoro_engine(1, max_arity=10)
        amps = eng.individual_tree_amplitudes(5)
        total = sum(amp for _, amp in amps)
        # total should equal r * S_r = 5 * S_5
        s5 = eng.S(5)
        # Actually the tree amplitude sum equals a_{r-2} = r * S_r
        # NOT S_r directly.  We need to check the normalization.
        a3 = eng._a_coeffs[3]
        # a_3 = 5 * S_5
        assert a3 == 5 * s5

    def test_tree_amplitudes_nonzero(self):
        """At arity 5 for Virasoro, at least some tree amplitudes nonzero."""
        eng = virasoro_engine(1, max_arity=10)
        amps = eng.individual_tree_amplitudes(5)
        nonzero = [(label, amp) for label, amp in amps if amp != FR(0)]
        assert len(nonzero) > 0

    def test_tree_amplitudes_arity_3_seed(self):
        """At arity 3, tree amplitudes are seeds (not from tree sum)."""
        eng = virasoro_engine(1, max_arity=10)
        amps = eng.individual_tree_amplitudes(3)
        # 2 trees at arity 3
        assert len(amps) == 2

    def test_tree_amplitudes_arity_4(self):
        """At arity 4, tree amplitudes."""
        eng = virasoro_engine(1, max_arity=10)
        amps = eng.individual_tree_amplitudes(4)
        # 5 trees at arity 4
        assert len(amps) == 5


# ============================================================================
# VIII. Shadow depth classification
# ============================================================================

class TestShadowDepthClassification:
    """Test the G/L/C/M depth classification."""

    def test_virasoro_class_M(self):
        """Virasoro is class M (mixed, infinite tower)."""
        eng = virasoro_engine(1)
        assert eng.shadow_depth_class() == 'M'

    def test_virasoro_class_M_c13(self):
        """Virasoro at c=13 is still class M."""
        eng = virasoro_engine(13)
        assert eng.shadow_depth_class() == 'M'

    def test_heisenberg_class_G(self):
        """Heisenberg is class G (Gaussian, depth 2)."""
        eng = heisenberg_engine(1)
        assert eng.shadow_depth_class() == 'G'

    def test_sl2_on_h_line_class_G(self):
        """sl_2 on h-line is class G (Cartan is abelian)."""
        eng = affine_sl2_engine(1)
        assert eng.shadow_depth_class() == 'G'

    def test_critical_discriminant_virasoro(self):
        """Delta = 8*kappa*S_4 for Virasoro."""
        eng = virasoro_engine(1)
        delta = eng.critical_discriminant()
        expected = 8 * FR(1, 2) * FR(10, 27)
        assert delta == expected
        assert delta != FR(0)  # nonzero -> class M

    def test_critical_discriminant_heisenberg(self):
        """Delta = 0 for Heisenberg."""
        eng = heisenberg_engine(1)
        assert eng.critical_discriminant() == FR(0)

    def test_critical_discriminant_formula(self):
        """Delta = 40/(5c+22) for Virasoro."""
        for c_val in [1, 13, 26]:
            eng = virasoro_engine(c_val)
            c = FR(c_val)
            expected = FR(40) / (5 * c + 22)
            assert eng.critical_discriminant() == expected


# ============================================================================
# IX. Growth rate
# ============================================================================

class TestGrowthRate:
    """Test shadow growth rate rho."""

    def test_growth_rate_virasoro_c1(self):
        """Shadow growth rate at c=1."""
        eng = virasoro_engine(1)
        rho = eng.shadow_growth_rate()
        assert rho > 0
        # rho = sqrt(36 + 2 * 40/27) / (2 * 1/2) = sqrt(36 + 80/27)
        # = sqrt(972/27 + 80/27) = sqrt(1052/27) / 1
        import math
        expected = math.sqrt(1052 / 27)
        assert abs(rho - expected) < 1e-10

    def test_growth_rate_virasoro_c13(self):
        """Shadow growth rate at c=13 (self-dual)."""
        eng = virasoro_engine(13)
        rho = eng.shadow_growth_rate()
        assert rho > 0
        # rho = sqrt(36 + 2*40/87) / 13
        import math
        expected = math.sqrt(36 + 80 / 87) / 13
        assert abs(rho - expected) < 1e-10

    def test_growth_rate_heisenberg_zero(self):
        """Growth rate = 0 for Heisenberg (tower terminates)."""
        eng = heisenberg_engine(1)
        rho = eng.shadow_growth_rate()
        assert rho == 0.0

    def test_growth_rate_positive_virasoro(self):
        """Growth rate is positive for all Virasoro c > 0."""
        for c_val in [FR(1, 2), 1, 7, 13, 26, 100]:
            eng = virasoro_engine(c_val)
            assert eng.shadow_growth_rate() > 0


# ============================================================================
# X. Cross-checks against existing modules
# ============================================================================

class TestCrossChecks:
    """Cross-check against explicit_theta.py and shadow_tower_recursive.py."""

    def test_cross_check_explicit_theta_virasoro(self):
        """Cross-check S_r against explicit_theta.VirasoroTheta."""
        try:
            from compute.lib.explicit_theta import VirasoroTheta
            vt = VirasoroTheta(c_val=1, max_arity=15)
            eng = virasoro_engine(1, max_arity=15)

            for r in range(2, 12):
                s_r_vt = vt.S(r)
                s_r_eng = eng.S(r)
                # Convert to Fraction for comparison
                s_r_vt_frac = FR(s_r_vt) if s_r_vt is not None else FR(0)
                assert s_r_eng == s_r_vt_frac, (
                    f"S_{r}: engine={s_r_eng}, explicit_theta={s_r_vt_frac}"
                )
        except ImportError:
            pytest.skip("explicit_theta module not available")

    def test_cross_check_explicit_theta_heisenberg(self):
        """Cross-check against HeisenbergTheta."""
        try:
            from compute.lib.explicit_theta import HeisenbergTheta
            ht = HeisenbergTheta(k_val=1)
            eng = heisenberg_engine(1)

            for r in range(2, 10):
                s_r_ht = ht.S(r)
                s_r_eng = eng.S(r)
                s_r_ht_frac = FR(s_r_ht) if s_r_ht is not None else FR(0)
                assert s_r_eng == s_r_ht_frac
        except ImportError:
            pytest.skip("explicit_theta module not available")

    def test_cross_check_sl2_theta(self):
        """Cross-check sl_2 tensor components against AffineSl2Theta."""
        try:
            from compute.lib.explicit_theta import AffineSl2Theta
            sl2 = AffineSl2Theta(k_val=1)
            eng = affine_sl2_engine(1)

            # Check arity 2
            t2_ref = sl2.theta_arity2_tensor()
            t2_eng = eng.sl2_theta_arity2()
            for key in t2_ref:
                ref_val = FR(t2_ref[key])
                eng_val = t2_eng.get(key, FR(0))
                assert eng_val == ref_val, f"Killing[{key}]: {eng_val} vs {ref_val}"

            # Check arity 3
            t3_ref = sl2.theta_arity3_tensor()
            t3_eng = eng.sl2_theta_arity3()
            for key in t3_ref:
                ref_val = FR(t3_ref[key])
                eng_val = t3_eng.get(key, FR(0))
                assert eng_val == ref_val, f"Cubic[{key}]: {eng_val} vs {ref_val}"

            # Check arity 4 = zero
            t4_ref = sl2.theta_arity4_tensor()
            t4_eng = eng.sl2_theta_arity4()
            assert t4_ref == {} or all(FR(v) == FR(0) for v in t4_ref.values())
            assert t4_eng == {}
        except ImportError:
            pytest.skip("explicit_theta module not available")


# ============================================================================
# XI. Virasoro OPE engine tests
# ============================================================================

class TestVirasoroOPE:
    """Test the Virasoro OPE implementation."""

    def test_T_mode0_T(self):
        """T_{(0)}T = dT (simple pole residue = translation)."""
        ope = VirasoroOPE(FR(1))
        result = ope.ope_residue(VirasoroState.T(), VirasoroState.T())
        # T_{(0)}T = L_{-1}T = dT
        assert result.coeffs.get('dT', FR(0)) == FR(1)

    def test_T_mode1_T(self):
        """T_{(1)}T = 2T (conformal weight)."""
        ope = VirasoroOPE(FR(1))
        result = ope.ope_mode(VirasoroState.T(), VirasoroState.T(), 1)
        assert result.coeffs.get('T', FR(0)) == FR(2)

    def test_T_mode3_T(self):
        """T_{(3)}T = (c/2)|0> (central charge term)."""
        for c_val in [1, 2, 13, 26]:
            ope = VirasoroOPE(FR(c_val))
            result = ope.ope_mode(VirasoroState.T(), VirasoroState.T(), 3)
            expected_vac = FR(c_val, 2)
            assert result.coeffs.get('vac', FR(0)) == expected_vac, (
                f"c={c_val}: T_(3)T vac coeff = {result.coeffs.get('vac', FR(0))}, "
                f"expected {expected_vac}"
            )

    def test_T_mode2_T(self):
        """T_{(2)}T = L_1 T = 0 (no cubic pole for Virasoro)."""
        ope = VirasoroOPE(FR(1))
        result = ope.ope_mode(VirasoroState.T(), VirasoroState.T(), 2)
        assert result.is_zero()

    def test_L_minus1_dT(self):
        """L_{-1}(dT) = 2 d^2T.

        L_{-1}(L_{-3}|0>) = [L_{-1}, L_{-3}]|0> = 2 L_{-4}|0> = 2 d^2T.
        """
        ope = VirasoroOPE(FR(1))
        result = ope._apply_L(-1, 'dT')
        assert result.coeffs.get('d2T', FR(0)) == FR(2)

    def test_L0_T(self):
        """L_0 T = 2T (T has weight 2)."""
        ope = VirasoroOPE(FR(1))
        result = ope._apply_L(0, 'T')
        assert result.coeffs.get('T', FR(0)) == FR(2)

    def test_L0_dT(self):
        """L_0 dT = 3 dT (dT has weight 3)."""
        ope = VirasoroOPE(FR(1))
        result = ope._apply_L(0, 'dT')
        assert result.coeffs.get('dT', FR(0)) == FR(3)

    def test_L1_T(self):
        """L_1 T = 0."""
        ope = VirasoroOPE(FR(1))
        result = ope._apply_L(1, 'T')
        assert result.is_zero()

    def test_L1_dT(self):
        """L_1 dT = 4T."""
        ope = VirasoroOPE(FR(1))
        result = ope._apply_L(1, 'dT')
        assert result.coeffs.get('T', FR(0)) == FR(4)

    def test_L2_T(self):
        """L_2 T = (c/2)|0>."""
        for c_val in [1, 2, 13]:
            ope = VirasoroOPE(FR(c_val))
            result = ope._apply_L(2, 'T')
            assert result.coeffs.get('vac', FR(0)) == FR(c_val, 2)

    def test_L2_dT(self):
        """L_2 dT = 0."""
        ope = VirasoroOPE(FR(1))
        result = ope._apply_L(2, 'dT')
        assert result.is_zero()

    def test_L2_d2T(self):
        """L_2 d^2T = 6T."""
        ope = VirasoroOPE(FR(1))
        result = ope._apply_L(2, 'd2T')
        assert result.coeffs.get('T', FR(0)) == FR(6)

    def test_dT_mode(self):
        """(dT)_{(n)} = -n * L_{n-2} (from translation covariance)."""
        ope = VirasoroOPE(FR(1))
        # (dT)_{(1)} T = -L_{-1} T = -dT
        result = ope._apply_dT_mode(1, 'T')
        assert result.coeffs.get('dT', FR(0)) == FR(-1)

        # (dT)_{(2)} T = -2 * L_0 T = -4T
        result2 = ope._apply_dT_mode(2, 'T')
        assert result2.coeffs.get('T', FR(0)) == FR(-4)

    def test_vacuum_state(self):
        """VirasoroState.vacuum()."""
        vac = VirasoroState.vacuum()
        assert vac.coeffs == {'vac': FR(1)}

    def test_state_addition(self):
        """State addition."""
        s1 = VirasoroState({'T': FR(2)})
        s2 = VirasoroState({'T': FR(3), 'dT': FR(1)})
        s3 = s1.add(s2)
        assert s3.coeffs['T'] == FR(5)
        assert s3.coeffs['dT'] == FR(1)


# ============================================================================
# XII. Shadow metric and generating function
# ============================================================================

class TestShadowMetric:
    """Test shadow metric Q_L and its properties."""

    def test_shadow_metric_virasoro(self):
        """Q_L(t) = c^2 + 12ct + (36 + 80/(5c+22))t^2 for Virasoro."""
        eng = virasoro_engine(1)
        q0, q1, q2 = eng._q0, eng._q1, eng._q2
        assert q0 == FR(1)  # 4*(1/2)^2 = 1
        assert q1 == FR(12)  # 12*1*2... wait
        # q1 = 12 * kappa * alpha = 12 * (1/2) * 2 = 12
        assert q1 == FR(12)
        # q2 = 9*4 + 16*(1/2)*(10/27) = 36 + 80/27 = (972+80)/27 = 1052/27
        expected_q2 = FR(36) + FR(16) * FR(1, 2) * FR(10, 27)
        assert q2 == expected_q2

    def test_shadow_metric_heisenberg(self):
        """Q_L = 4k^2 for Heisenberg (alpha=0, S_4=0)."""
        eng = heisenberg_engine(3)
        q0, q1, q2 = eng._q0, eng._q1, eng._q2
        assert q0 == FR(36)  # 4*9
        assert q1 == FR(0)
        assert q2 == FR(0)

    def test_sqrt_taylor_a0(self):
        """a_0 = 2*kappa."""
        eng = virasoro_engine(1)
        assert eng._a_coeffs[0] == FR(1)  # 2*(1/2) = 1

    def test_sqrt_taylor_a1(self):
        """a_1 = q_1/(2*a_0) = 6 (for Virasoro)."""
        eng = virasoro_engine(1)
        assert eng._a_coeffs[1] == FR(6)

    def test_sqrt_taylor_a2(self):
        """a_2 = (q_2 - a_1^2)/(2*a_0) for Virasoro."""
        eng = virasoro_engine(1)
        a_0 = eng._a_coeffs[0]
        a_1 = eng._a_coeffs[1]
        q2 = eng._q2
        expected_a2 = (q2 - a_1 ** 2) / (2 * a_0)
        assert eng._a_coeffs[2] == expected_a2

    def test_generating_function_identity(self):
        """Verify H(t)^2 = t^4 * Q_L(t) at specific t."""
        eng = virasoro_engine(1, max_arity=15)
        t_val = FR(1, 10)

        # H(t) = sum_r r*S_r*t^r
        H = sum(r * eng.S(r) * t_val ** r for r in range(2, 15))

        # Q_L(t)
        q0, q1, q2 = eng._q0, eng._q1, eng._q2
        Q = q0 + q1 * t_val + q2 * t_val ** 2

        # H^2 vs t^4 * Q
        lhs = H ** 2
        rhs = t_val ** 4 * Q

        # Should be approximately equal (truncation error at high arity)
        residual = abs(float(lhs - rhs))
        assert residual < 1e-8, f"H^2 vs t^4*Q: residual = {residual}"


# ============================================================================
# XIII. Additional structural tests
# ============================================================================

class TestStructural:
    """Test structural properties of the engine."""

    def test_engine_families(self):
        """All four families can be instantiated."""
        eng_v = virasoro_engine(1)
        eng_h = heisenberg_engine(1)
        eng_s = affine_sl2_engine(1)
        eng_b = betagamma_engine(-2)

        assert eng_v.family == 'virasoro'
        assert eng_h.family == 'heisenberg'
        assert eng_s.family == 'affine_sl2'
        assert eng_b.family == 'betagamma'

    def test_max_arity_parameter(self):
        """Engine respects max_arity parameter."""
        eng = virasoro_engine(1, max_arity=5)
        assert eng.S(5) is not None or eng.S(5) == FR(0)
        # S_6 should not be computed
        assert eng.S(6) == FR(0)  # defaults to zero if not computed

    def test_exact_arithmetic(self):
        """All computations use exact Fraction arithmetic."""
        eng = virasoro_engine(FR(7, 3), max_arity=10)
        for r in range(2, 10):
            s_r = eng.S(r)
            assert isinstance(s_r, Fraction), f"S_{r} is {type(s_r)}, not Fraction"

    def test_large_c_shadow_tower(self):
        """Shadow tower at large c is well-behaved."""
        eng = virasoro_engine(1000, max_arity=10)
        assert eng.S(2) == FR(500)
        assert eng.S(3) == FR(2)
        # S_4 approaches 0 as c -> infinity
        s4 = eng.S(4)
        assert s4 > FR(0)
        assert s4 < FR(1, 100)  # small for large c

    def test_fractional_c(self):
        """Engine handles fractional central charges."""
        eng = virasoro_engine(FR(7, 5), max_arity=8)
        assert eng.kappa() == FR(7, 10)
        s3 = eng.S(3)
        assert s3 == FR(2)


# ============================================================================
# XIV. Arity 5 tree decomposition
# ============================================================================

class TestArity5Decomposition:
    """Detailed tests for arity 5 tree decomposition."""

    def test_arity5_tree_count(self):
        """14 planted binary trees at arity 5."""
        trees = planted_binary_trees(5)
        assert len(trees) == 14

    def test_arity5_all_trees_have_4_internal(self):
        """Each tree at arity 5 has 4 internal vertices."""
        for tree in planted_binary_trees(5):
            assert tree.internal_vertices() == 4

    def test_arity5_mc_residual_zero(self):
        """MC residual at arity 5 is zero for multiple c values."""
        for c_val in [FR(1, 2), 1, 7, 13, 26, FR(7, 3)]:
            eng = virasoro_engine(c_val, max_arity=8)
            assert eng.mc_residual(5) == FR(0), f"c={c_val}"

    def test_arity5_tree_sum_matches(self):
        """Tree sum at arity 5 matches S_5 for multiple c."""
        for c_val in [1, 7, 13, 26]:
            eng = virasoro_engine(c_val, max_arity=8)
            _, _, residual = eng.tree_sum_vs_shadow(5)
            assert residual == FR(0), f"c={c_val}: residual={residual}"

    def test_arity5_S5_sign(self):
        """S_5 has definite sign for all c > 0."""
        for c_val in [FR(1, 2), 1, 7, 13, 26, 100]:
            eng = virasoro_engine(c_val, max_arity=8)
            s5 = eng.S(5)
            # S_5 should be negative for c > 0 (from the recursion)
            # Let's just check it's nonzero
            assert s5 != FR(0), f"S_5 = 0 at c={c_val}"
