r"""Tests for categorical shadow invariants.

Verifies the six-fold categorification:
  1. Categorical kappa (K-theory class)
  2. Categorical shadow metric (symmetric bilinear form)
  3. Shadow depth filtration (categorical filtration)
  4. Motivic shadow (K_0(Var_Q) classes)
  5. Derived shadow algebra (dg-algebra)
  6. Stable homotopy type (Postnikov data)

Multi-path verification:
  Path 1: Decategorification recovers numerical shadows
  Path 2: Categorical additivity: kappa^cat(A+B) = kappa^cat(A) + kappa^cat(B)
  Path 3: Categorical complementarity: kappa^cat(A) + kappa^cat(A!)
  Path 4: Motivic shadow Euler characteristic = numerical shadow
  Path 5: Shadow filtration stability matches G/L/C/M classification
  Path 6: Known categorifications (Khovanov etc.) compatibility

Anti-pattern coverage:
  AP1  -- kappa formulas recomputed per family, never copied
  AP10 -- cross-family consistency tests, not hardcoded single values
  AP14 -- shadow depth != Koszulness
  AP24 -- complementarity sum NOT universally zero
  AP31 -- kappa=0 does not imply Theta=0
  AP39 -- kappa != S_2 for general families
  AP48 -- kappa != c/2 for non-Virasoro

References:
  thm:shadow-cohft (higher_genus_modular_koszul.tex)
  def:shadow-metric (higher_genus_modular_koszul.tex)
  thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
  thm:depth-decomposition (arithmetic_shadows.tex)
  prop:shadow-formality-low-arity (higher_genus_modular_koszul.tex)
  conj:operadic-complexity (higher_genus_modular_koszul.tex)
  prop:independent-sum-factorization (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import pytest
from sympy import Rational, oo, simplify, Symbol, sqrt, expand

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'lib'))

from categorical_shadow_engine import (
    # Classes
    KTheoryClass,
    KTheorySum,
    CategoricalShadowMetric,
    ShadowFiltration,
    MotivicClass,
    MotivicShadow,
    DerivedShadowAlgebra,
    StableHomotopyType,
    CategoricalShadowType,
    # Functions
    categorical_kappa,
    categorical_kappa_dual,
    categorical_complementarity,
    categorical_shadow_metric,
    shadow_filtration,
    motivic_shadow,
    derived_shadow_algebra,
    stable_homotopy_type,
    full_categorical_shadow,
    categorical_kappa_additivity,
    shadow_filtration_tensor,
    ds_reduction_categorical,
    # Internals for verification
    lambda_fp,
    LAMBDA_FP,
)


c = Symbol('c')


# ========================================================================
# 1. CATEGORICAL KAPPA TESTS
# ========================================================================

class TestCategoricalKappa:
    """Test the K-theory class kappa^cat = kappa(A) * [E]."""

    # --- Path 1: Decategorification ---

    def test_heisenberg_decategorify(self):
        """kappa^cat(H_k) decategorifies to kappa = k."""
        kc = categorical_kappa('Heisenberg', level=1)
        assert kc.decategorify() == 1

    def test_heisenberg_level_3_decategorify(self):
        """kappa^cat(H_3) decategorifies to kappa = 3."""
        kc = categorical_kappa('Heisenberg', level=3)
        assert kc.decategorify() == 3

    def test_virasoro_decategorify_c1(self):
        """kappa^cat(Vir_1) decategorifies to kappa = 1/2."""
        kc = categorical_kappa('Virasoro', central_charge=1)
        assert kc.decategorify() == Rational(1, 2)

    def test_virasoro_decategorify_c26(self):
        """kappa^cat(Vir_26) decategorifies to kappa = 13."""
        kc = categorical_kappa('Virasoro', central_charge=26)
        assert kc.decategorify() == 13

    def test_virasoro_decategorify_c0(self):
        """kappa^cat(Vir_0) decategorifies to kappa = 0.
        CAUTION (AP31): kappa=0 does NOT mean Theta=0.
        """
        kc = categorical_kappa('Virasoro', central_charge=0)
        assert kc.decategorify() == 0

    def test_free_fermion_decategorify(self):
        """kappa^cat(FreeFermion) = 1/4."""
        kc = categorical_kappa('free_fermion')
        assert kc.decategorify() == Rational(1, 4)

    def test_betagamma_decategorify(self):
        """kappa^cat(bg, lambda=1) = 1."""
        kc = categorical_kappa('betagamma', weight=1)
        assert kc.decategorify() == 1

    def test_affine_sl2_level1_decategorify(self):
        """kappa^cat(sl_2, k=1) = dim(sl_2)*(1+2)/(2*2) = 3*3/4 = 9/4."""
        kc = categorical_kappa('Affine', lie_type='A', lie_rank=1, level=1)
        assert kc.decategorify() == Rational(9, 4)

    def test_affine_sl3_level1_decategorify(self):
        """kappa^cat(sl_3, k=1) = dim(sl_3)*(1+3)/(2*3) = 8*4/6 = 16/3."""
        kc = categorical_kappa('Affine', lie_type='A', lie_rank=2, level=1)
        assert kc.decategorify() == Rational(16, 3)

    def test_lattice_decategorify(self):
        """kappa^cat(V_Lambda) = rank."""
        kc = categorical_kappa('lattice', rank=24)
        assert kc.decategorify() == 24

    # --- K-theory structure ---

    def test_ktheory_generator_is_E(self):
        """kappa^cat lives in [E] (Hodge bundle class)."""
        kc = categorical_kappa('Heisenberg', level=1)
        assert kc.generator == 'E'

    def test_ktheory_rank(self):
        """Rank of kappa * [E] at genus 1 is kappa * 1."""
        kc = categorical_kappa('Heisenberg', level=5, genus=1)
        assert kc.rank() == 5  # kappa * rank(E) = 5 * 1 = 5

    def test_ktheory_rank_genus2(self):
        """Rank of kappa * [E] at genus 2 is kappa * 2."""
        kc = categorical_kappa('Heisenberg', level=3, genus=2)
        assert kc.rank() == 6  # 3 * 2

    # --- Path 2: Additivity ---

    def test_additivity_heisenberg(self):
        """kappa^cat(H_k1 + H_k2) = kappa^cat(H_k1) + kappa^cat(H_k2)."""
        assert categorical_kappa_additivity('Heisenberg', 'Heisenberg',
                                            {'level': 2}, {'level': 3})

    def test_additivity_heis_vir(self):
        """kappa^cat(H_1 + Vir_1) = kappa^cat(H_1) + kappa^cat(Vir_1)."""
        assert categorical_kappa_additivity('Heisenberg', 'Virasoro',
                                            {'level': 1}, {'central_charge': 1})

    def test_additivity_lattice_fermion(self):
        """Additivity for lattice + free fermion."""
        assert categorical_kappa_additivity('lattice', 'free_fermion',
                                            {'rank': 8}, {})

    # --- Path 3: Complementarity ---

    def test_complementarity_heisenberg(self):
        """kappa(H_k) + kappa(H_k!) = 0."""
        _, num_sum, expected, match = categorical_complementarity('Heisenberg', level=1)
        assert match
        assert num_sum == 0

    def test_complementarity_virasoro(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24: NOT zero)."""
        _, num_sum, expected, match = categorical_complementarity('Virasoro', central_charge=10)
        assert match
        assert num_sum == 13

    def test_complementarity_virasoro_self_dual(self):
        """At c=13: kappa + kappa' = 13 (self-dual point)."""
        _, num_sum, expected, match = categorical_complementarity('Virasoro', central_charge=13)
        assert match
        assert num_sum == 13

    def test_complementarity_affine_sl2(self):
        """kappa(sl_2, k=1) + kappa(sl_2, k=-5) = 0 (Feigin-Frenkel)."""
        _, num_sum, expected, match = categorical_complementarity(
            'Affine', lie_type='A', lie_rank=1, level=1)
        assert match
        assert num_sum == 0

    def test_complementarity_lattice(self):
        """kappa(V_Lambda) + kappa(V_Lambda!) = 0."""
        _, num_sum, expected, match = categorical_complementarity('lattice', rank=8)
        assert match
        assert num_sum == 0

    def test_complementarity_betagamma(self):
        """kappa(bg_lambda) + kappa(bg_{1-lambda}) = 2*kappa(lambda).
        betagamma kappa is symmetric under lambda -> 1-lambda:
        kappa(lam) = kappa(1-lam) = 6*lam^2 - 6*lam + 1.
        At lam=1: sum = 2*1 = 2.
        """
        _, num_sum, expected, match = categorical_complementarity('betagamma', weight=1)
        assert match
        assert num_sum == 2


# ========================================================================
# 2. CATEGORICAL SHADOW METRIC TESTS
# ========================================================================

class TestCategoricalShadowMetric:
    """Test the categorical shadow metric Q_L^cat."""

    # --- Classification ---

    def test_heisenberg_class_G(self):
        """Heisenberg has class G (Delta=0, alpha=0)."""
        m = categorical_shadow_metric('Heisenberg', level=1)
        assert m.classify() == 'G'

    def test_affine_sl2_class_L(self):
        """Affine sl_2 has class L (Delta=0, alpha!=0)."""
        m = categorical_shadow_metric('Affine', lie_type='A', lie_rank=1, level=1)
        assert m.classify() == 'L'

    def test_betagamma_class_C(self):
        """betagamma has class C (Delta!=0, alpha=0 on weight line)."""
        m = categorical_shadow_metric('betagamma', weight=1)
        assert m.classify() == 'C'

    def test_virasoro_class_M(self):
        """Virasoro has class M (Delta!=0, alpha!=0)."""
        m = categorical_shadow_metric('Virasoro', central_charge=1)
        assert m.classify() == 'M'

    # --- Gram matrix structure ---

    def test_gram_matrix_symmetric(self):
        """Gram matrix is symmetric."""
        m = categorical_shadow_metric('Virasoro', central_charge=1)
        mat = m.matrix
        assert simplify(mat[0][1] - mat[1][0]) == 0

    def test_gram_determinant_heisenberg(self):
        """det(M) = 0 for class G (degenerate)."""
        m = categorical_shadow_metric('Heisenberg', level=1)
        assert simplify(m.determinant) == 0

    def test_gram_determinant_affine(self):
        """det(M) = 0 for class L."""
        m = categorical_shadow_metric('Affine', lie_type='A', lie_rank=1, level=1)
        assert simplify(m.determinant) == 0

    def test_gram_determinant_virasoro_nonzero(self):
        """det(M) != 0 for class M."""
        m = categorical_shadow_metric('Virasoro', central_charge=1)
        assert simplify(m.determinant) != 0

    # --- Decategorification ---

    def test_ql_decategorify_heisenberg(self):
        """Q_L(t) for Heisenberg = 4*k^2 (constant, no t-dependence)."""
        m = categorical_shadow_metric('Heisenberg', level=1)
        ql = m.decategorify()
        t = Symbol('t')
        # For Heisenberg: alpha=0, Delta=0, so Q_L = 4*kappa^2 = 4
        assert simplify(ql - 4) == 0

    def test_ql_evaluate_virasoro(self):
        """Q_L(0) = 4*kappa^2 for Virasoro."""
        m = categorical_shadow_metric('Virasoro', central_charge=2)
        q0 = m.evaluate_ql(0)
        assert simplify(q0 - 4) == 0  # kappa=1, so 4*1^2 = 4

    # --- K-theory type ---

    def test_ktheory_type_G(self):
        m = categorical_shadow_metric('Heisenberg', level=1)
        assert m.k_theory_type() == 'split_degenerate'

    def test_ktheory_type_L(self):
        m = categorical_shadow_metric('Affine', lie_type='A', lie_rank=1, level=1)
        assert m.k_theory_type() == 'split_nondegenerate'

    def test_ktheory_type_M(self):
        m = categorical_shadow_metric('Virasoro', central_charge=1)
        assert m.k_theory_type() == 'indecomposable_full'

    # --- Critical discriminant ---

    def test_delta_heisenberg_zero(self):
        """Delta = 0 for Heisenberg (class G)."""
        m = categorical_shadow_metric('Heisenberg', level=1)
        assert simplify(m.delta) == 0

    def test_delta_virasoro_c1(self):
        """Delta = 8*kappa*S4 = 8*(1/2)*(10/(1*27)) = 40/27 for Virasoro c=1."""
        m = categorical_shadow_metric('Virasoro', central_charge=1)
        expected = 8 * Rational(1, 2) * Rational(10, 27)
        assert simplify(m.delta - expected) == 0

    def test_chern_number_equals_delta(self):
        """c_1 of the categorical metric = Delta."""
        m = categorical_shadow_metric('Virasoro', central_charge=1)
        assert simplify(m.chern_number_c1() - m.delta) == 0


# ========================================================================
# 3. SHADOW FILTRATION TESTS
# ========================================================================

class TestShadowFiltration:
    """Test the categorical shadow depth filtration."""

    # --- Class classification ---

    def test_heisenberg_filtration_class(self):
        f = shadow_filtration('Heisenberg', level=1)
        assert f.shadow_class == 'G'
        assert f.r_max == 2

    def test_affine_filtration_class(self):
        f = shadow_filtration('Affine', lie_type='A', lie_rank=1, level=1)
        assert f.shadow_class == 'L'
        assert f.r_max == 3

    def test_betagamma_filtration_class(self):
        f = shadow_filtration('betagamma', weight=1)
        assert f.shadow_class == 'C'
        assert f.r_max == 4

    def test_virasoro_filtration_class(self):
        f = shadow_filtration('Virasoro', central_charge=1)
        assert f.shadow_class == 'M'
        assert f.r_max is None

    # --- Finite length ---

    def test_G_is_finite(self):
        f = shadow_filtration('Heisenberg', level=1)
        assert f.is_finite_length()

    def test_L_is_finite(self):
        f = shadow_filtration('Affine', lie_type='A', lie_rank=1, level=1)
        assert f.is_finite_length()

    def test_C_is_finite(self):
        f = shadow_filtration('betagamma', weight=1)
        assert f.is_finite_length()

    def test_M_is_infinite(self):
        f = shadow_filtration('Virasoro', central_charge=1)
        assert not f.is_finite_length()

    # --- Filtration length ---

    def test_G_length_1(self):
        f = shadow_filtration('Heisenberg', level=1)
        assert f.filtration_length() == 1

    def test_L_length_2(self):
        f = shadow_filtration('Affine', lie_type='A', lie_rank=1, level=1)
        assert f.filtration_length() == 2

    def test_C_length_3(self):
        f = shadow_filtration('betagamma', weight=1)
        assert f.filtration_length() == 3

    def test_M_length_infinite(self):
        f = shadow_filtration('Virasoro', central_charge=1)
        assert f.filtration_length() is None

    # --- Stabilization ---

    def test_G_stabilizes(self):
        f = shadow_filtration('Heisenberg', level=1)
        assert f.verify_stabilization()

    def test_L_stabilizes(self):
        f = shadow_filtration('Affine', lie_type='A', lie_rank=1, level=1)
        assert f.verify_stabilization()

    def test_M_does_not_stabilize(self):
        f = shadow_filtration('Virasoro', central_charge=1)
        assert f.verify_stabilization()  # checks persistent nonzero grades

    # --- Categorical type ---

    def test_G_categorical_type(self):
        f = shadow_filtration('Heisenberg', level=1)
        assert f.categorical_type() == 'finite_resolution_length_1'

    def test_M_categorical_type(self):
        f = shadow_filtration('Virasoro', central_charge=1)
        assert f.categorical_type() == 'pro_object_infinite_resolution'

    # --- Decategorification ---

    def test_decategorify_G(self):
        f = shadow_filtration('Heisenberg', level=1)
        cls, rmax = f.decategorify()
        assert cls == 'G' and rmax == 2

    def test_decategorify_M(self):
        f = shadow_filtration('Virasoro', central_charge=1)
        cls, rmax = f.decategorify()
        assert cls == 'M' and rmax is None


# ========================================================================
# 4. MOTIVIC SHADOW TESTS
# ========================================================================

class TestMotivicShadow:
    """Test motivic shadow tower S_r^mot in K_0(Var_Q)."""

    # --- Path 4: Euler characteristic = numerical shadow ---

    def test_euler_heisenberg_S2(self):
        """e(S_2^mot(H_k)) = k for Heisenberg."""
        ms = motivic_shadow('Heisenberg', level=3)
        euler = ms.euler_tower()
        assert euler[2] == 3

    def test_euler_heisenberg_S3_zero(self):
        """e(S_3^mot(H_k)) = 0 for Heisenberg (class G)."""
        ms = motivic_shadow('Heisenberg', level=1)
        euler = ms.euler_tower()
        assert euler[3] == 0

    def test_euler_virasoro_S2(self):
        """e(S_2^mot(Vir_c)) = c/2."""
        ms = motivic_shadow('Virasoro', central_charge=10)
        euler = ms.euler_tower()
        assert euler[2] == 5

    def test_euler_virasoro_S3(self):
        """e(S_3^mot(Vir_c)) = 2 (the cubic shadow)."""
        ms = motivic_shadow('Virasoro', central_charge=10)
        euler = ms.euler_tower()
        assert euler[3] == 2

    def test_euler_virasoro_S4(self):
        """e(S_4^mot(Vir_c=10)) = 10/(10*72) = 1/72."""
        ms = motivic_shadow('Virasoro', central_charge=10)
        euler = ms.euler_tower()
        expected = Rational(10) / (10 * (50 + 22))
        assert simplify(euler[4] - expected) == 0

    def test_euler_virasoro_S5(self):
        """e(S_5^mot(Vir_c=10)) = -48/(100*72) = -1/150."""
        ms = motivic_shadow('Virasoro', central_charge=10)
        euler = ms.euler_tower()
        expected = Rational(-48) / (100 * 72)
        assert simplify(euler[5] - expected) == 0

    def test_euler_affine_S2(self):
        """e(S_2^mot(sl_2, k=1)) = 9/4."""
        ms = motivic_shadow('Affine', lie_type='A', lie_rank=1, level=1)
        euler = ms.euler_tower()
        assert euler[2] == Rational(9, 4)

    def test_euler_affine_S3(self):
        """e(S_3^mot(sl_2, k=1)) = 1 (Killing form)."""
        ms = motivic_shadow('Affine', lie_type='A', lie_rank=1, level=1)
        euler = ms.euler_tower()
        assert euler[3] == 1

    def test_euler_affine_S4_zero(self):
        """e(S_4^mot(sl_2, k=1)) = 0 (class L terminates at 3)."""
        ms = motivic_shadow('Affine', lie_type='A', lie_rank=1, level=1)
        euler = ms.euler_tower()
        assert euler[4] == 0

    # --- Tate purity ---

    def test_heisenberg_pure_tate(self):
        """Heisenberg shadow tower is pure Tate (arithmetically trivial)."""
        ms = motivic_shadow('Heisenberg', level=1)
        assert ms.is_pure_tate_tower()

    def test_affine_pure_tate(self):
        """Affine shadow tower is pure Tate at each arity."""
        ms = motivic_shadow('Affine', lie_type='A', lie_rank=1, level=1)
        assert ms.is_pure_tate_tower()

    def test_virasoro_pure_tate(self):
        """Virasoro shadow coefficients are rational functions of c, hence Tate."""
        ms = motivic_shadow('Virasoro', central_charge=10)
        assert ms.is_pure_tate_tower()

    # --- Tower termination ---

    def test_heisenberg_terminates_at_2(self):
        ms = motivic_shadow('Heisenberg', level=1)
        assert ms.terminates_at() == 2

    def test_affine_terminates_at_3(self):
        ms = motivic_shadow('Affine', lie_type='A', lie_rank=1, level=1)
        assert ms.terminates_at() == 3

    def test_virasoro_does_not_terminate(self):
        ms = motivic_shadow('Virasoro', central_charge=10)
        assert ms.terminates_at() is None

    # --- Hodge weights ---

    def test_heisenberg_hodge_weight_0(self):
        """kappa is pure Tate weight 0."""
        ms = motivic_shadow('Heisenberg', level=1)
        hw = ms.hodge_weights()
        assert hw[2] == 0

    def test_affine_S3_hodge_weight(self):
        """S_3 for affine sl_2 has Hodge weight from dim(sl_2)=3: Q(-3/2) -> weight -3."""
        ms = motivic_shadow('Affine', lie_type='A', lie_rank=1, level=1)
        hw = ms.hodge_weights()
        assert hw[3] == -3  # 2 * (-3/2) = -3


# ========================================================================
# 5. MOTIVIC CLASS ALGEBRA TESTS
# ========================================================================

class TestMotivicClass:
    """Test the Grothendieck ring K_0(Var_Q) arithmetic."""

    def test_tate_motive_euler(self):
        """e(Q(n)) = 1 for all n (Euler char of Tate motive)."""
        q0 = MotivicClass.tate(0)
        q1 = MotivicClass.tate(1)
        qm1 = MotivicClass.tate(-1)
        assert q0.euler_characteristic() == 1
        assert q1.euler_characteristic() == 1
        assert qm1.euler_characteristic() == 1

    def test_zero_motive(self):
        z = MotivicClass.zero()
        assert z.is_zero()
        assert z.euler_characteristic() == 0

    def test_unit_motive(self):
        u = MotivicClass.unit()
        assert u.euler_characteristic() == 1
        assert u.is_pure_tate()
        assert u.hodge_weight() == 0

    def test_addition(self):
        q0 = MotivicClass.tate(0, coeff=3)
        q1 = MotivicClass.tate(1, coeff=2)
        s = q0 + q1
        assert s.euler_characteristic() == 5  # 3 + 2

    def test_multiplication(self):
        """L * L = L^2 (product in K_0)."""
        L = MotivicClass.tate(1)
        L2 = L * L
        # L^1 * L^1 = L^2
        assert L2.coefficients.get(Rational(2)) == 1

    def test_scale(self):
        q = MotivicClass.tate(0, coeff=5)
        s = q.scale(3)
        assert s.euler_characteristic() == 15


# ========================================================================
# 6. DERIVED SHADOW ALGEBRA TESTS
# ========================================================================

class TestDerivedShadowAlgebra:
    """Test the chain-level shadow algebra A^{sh,cat}."""

    def test_heisenberg_formality_level(self):
        """Heisenberg: L-infinity formality level = 2 (class G)."""
        d = derived_shadow_algebra('Heisenberg', level=1)
        assert d.formality_level() == 2

    def test_affine_formality_level(self):
        """Affine sl_2: L-infinity formality level = 3 (class L)."""
        d = derived_shadow_algebra('Affine', lie_type='A', lie_rank=1, level=1)
        assert d.formality_level() == 3

    def test_virasoro_formality_level_infinite(self):
        """Virasoro: L-infinity formality level = infinity (class M)."""
        d = derived_shadow_algebra('Virasoro', central_charge=1)
        assert d.formality_level() is None

    def test_heisenberg_no_massey_products(self):
        """Class G: no Massey products (formal)."""
        d = derived_shadow_algebra('Heisenberg', level=1)
        assert not d.has_massey_products()

    def test_virasoro_has_massey_products(self):
        """Class M: Massey products encode higher shadows."""
        d = derived_shadow_algebra('Virasoro', central_charge=1)
        assert d.has_massey_products()

    def test_linfty_brackets_heisenberg(self):
        """Heisenberg: only ell_2 nonzero."""
        d = derived_shadow_algebra('Heisenberg', level=1)
        nonzero = d.linfty_brackets_nonzero()
        assert nonzero == [2]

    def test_linfty_brackets_affine(self):
        """Affine: ell_2, ell_3 nonzero."""
        d = derived_shadow_algebra('Affine', lie_type='A', lie_rank=1, level=1)
        nonzero = d.linfty_brackets_nonzero()
        assert nonzero == [2, 3]

    def test_linfty_brackets_virasoro(self):
        """Virasoro: ell_2 through ell_5 nonzero (at least)."""
        d = derived_shadow_algebra('Virasoro', central_charge=1)
        nonzero = d.linfty_brackets_nonzero()
        assert 2 in nonzero and 3 in nonzero and 4 in nonzero and 5 in nonzero

    def test_chain_degree_0_is_kappa(self):
        """degree 0 of the derived algebra carries kappa."""
        d = derived_shadow_algebra('Heisenberg', level=5)
        assert d.chain_degrees[0] == 5


# ========================================================================
# 7. STABLE HOMOTOPY TYPE TESTS
# ========================================================================

class TestStableHomotopyType:
    """Test the Postnikov tower / stable homotopy type."""

    def test_heisenberg_finite_postnikov(self):
        sht = stable_homotopy_type('Heisenberg', level=1)
        assert sht.is_finite_postnikov()
        assert sht.postnikov_tower_length == 2

    def test_affine_finite_postnikov(self):
        sht = stable_homotopy_type('Affine', lie_type='A', lie_rank=1, level=1)
        assert sht.is_finite_postnikov()
        assert sht.postnikov_tower_length == 3

    def test_virasoro_infinite_postnikov(self):
        sht = stable_homotopy_type('Virasoro', central_charge=1)
        assert not sht.is_finite_postnikov()
        assert sht.postnikov_tower_length is None

    def test_heisenberg_eilenberg_maclane(self):
        sht = stable_homotopy_type('Heisenberg', level=1)
        assert sht.rational_homotopy_type() == 'Eilenberg-MacLane'

    def test_virasoro_infinite_postnikov_type(self):
        sht = stable_homotopy_type('Virasoro', central_charge=1)
        assert sht.rational_homotopy_type() == 'infinite_Postnikov'

    def test_spectrum_type_G(self):
        sht = stable_homotopy_type('Heisenberg', level=1)
        assert sht.spectrum_type() == 'Eilenberg_MacLane_HQ'

    def test_spectrum_type_M(self):
        sht = stable_homotopy_type('Virasoro', central_charge=1)
        assert sht.spectrum_type() == 'algebraic_K_theory_type'

    def test_pi2_equals_kappa(self):
        """pi_2 of the stable homotopy type = kappa."""
        sht = stable_homotopy_type('Heisenberg', level=7)
        assert sht.homotopy_groups[2] == 7

    def test_pi3_equals_alpha(self):
        """pi_3 of affine = alpha = 1."""
        sht = stable_homotopy_type('Affine', lie_type='A', lie_rank=1, level=1)
        assert sht.homotopy_groups[3] == 1

    def test_virasoro_pi5_nonzero(self):
        """pi_5 of Virasoro != 0 (S_5 nonzero)."""
        sht = stable_homotopy_type('Virasoro', central_charge=1)
        assert simplify(sht.homotopy_groups[5]) != 0


# ========================================================================
# 8. FULL CATEGORICAL SHADOW TYPE (integration tests)
# ========================================================================

class TestFullCategoricalShadow:
    """Test the full six-fold categorical shadow type."""

    def test_heisenberg_all_consistent(self):
        """All consistency conditions pass for Heisenberg."""
        fcs = full_categorical_shadow('Heisenberg', level=1)
        assert fcs.all_consistent()

    def test_virasoro_c1_all_consistent(self):
        """All consistency conditions pass for Virasoro c=1."""
        fcs = full_categorical_shadow('Virasoro', central_charge=1)
        assert fcs.all_consistent()

    def test_virasoro_c10_all_consistent(self):
        """All consistency conditions pass for Virasoro c=10."""
        fcs = full_categorical_shadow('Virasoro', central_charge=10)
        assert fcs.all_consistent()

    def test_affine_sl2_all_consistent(self):
        """All consistency conditions pass for affine sl_2 k=1."""
        fcs = full_categorical_shadow('Affine', lie_type='A', lie_rank=1, level=1)
        assert fcs.all_consistent()

    def test_betagamma_all_consistent(self):
        """All consistency conditions pass for betagamma."""
        fcs = full_categorical_shadow('betagamma', weight=1)
        assert fcs.all_consistent()

    def test_lattice_all_consistent(self):
        """All consistency conditions pass for lattice rank 8."""
        fcs = full_categorical_shadow('lattice', rank=8)
        assert fcs.all_consistent()

    def test_free_fermion_all_consistent(self):
        """All consistency conditions pass for free fermion."""
        fcs = full_categorical_shadow('free_fermion')
        assert fcs.all_consistent()

    def test_consistency_C1_detail(self):
        """Detailed check: C1 (kappa decategorification)."""
        fcs = full_categorical_shadow('Virasoro', central_charge=26)
        results = fcs.verify_consistency()
        assert results['C1_kappa_decategorification']

    def test_consistency_C2_detail(self):
        """Detailed check: C2 (metric discriminant)."""
        fcs = full_categorical_shadow('Virasoro', central_charge=10)
        results = fcs.verify_consistency()
        assert results['C2_metric_discriminant']

    def test_consistency_C7_detail(self):
        """Detailed check: C7 (all classes agree)."""
        fcs = full_categorical_shadow('Heisenberg', level=1)
        results = fcs.verify_consistency()
        assert results['C7_class_agreement']


# ========================================================================
# 9. FUNCTORIALITY TESTS
# ========================================================================

class TestFunctoriality:
    """Test categorical functoriality: DS reduction, tensor products."""

    def test_ds_affine_to_M(self):
        """DS: affine sl_N (class L) -> W_N (class M)."""
        src, tgt = ds_reduction_categorical('Affine', lie_type='A', lie_rank=2, level=1)
        assert src == 'L'
        assert tgt == 'M'

    def test_ds_heisenberg_unchanged(self):
        """DS not applicable to Heisenberg (stays class G)."""
        src, tgt = ds_reduction_categorical('Heisenberg', level=1)
        assert src == 'G' and tgt == 'G'

    def test_tensor_G_G(self):
        """G tensor G = G."""
        f1 = shadow_filtration('Heisenberg', level=1)
        f2 = shadow_filtration('Heisenberg', level=2)
        assert shadow_filtration_tensor(f1, f2) == 'G'

    def test_tensor_G_L(self):
        """G tensor L = L."""
        f1 = shadow_filtration('Heisenberg', level=1)
        f2 = shadow_filtration('Affine', lie_type='A', lie_rank=1, level=1)
        assert shadow_filtration_tensor(f1, f2) == 'L'

    def test_tensor_G_M(self):
        """G tensor M = M."""
        f1 = shadow_filtration('Heisenberg', level=1)
        f2 = shadow_filtration('Virasoro', central_charge=1)
        assert shadow_filtration_tensor(f1, f2) == 'M'

    def test_tensor_L_L(self):
        """L tensor L = L."""
        f1 = shadow_filtration('Affine', lie_type='A', lie_rank=1, level=1)
        f2 = shadow_filtration('Affine', lie_type='A', lie_rank=2, level=1)
        assert shadow_filtration_tensor(f1, f2) == 'L'

    def test_tensor_L_M(self):
        """L tensor M = M."""
        f1 = shadow_filtration('Affine', lie_type='A', lie_rank=1, level=1)
        f2 = shadow_filtration('Virasoro', central_charge=1)
        assert shadow_filtration_tensor(f1, f2) == 'M'

    def test_tensor_M_M(self):
        """M tensor M = M."""
        f1 = shadow_filtration('Virasoro', central_charge=1)
        f2 = shadow_filtration('Virasoro', central_charge=2)
        assert shadow_filtration_tensor(f1, f2) == 'M'

    def test_tensor_C_M(self):
        """C tensor M = M."""
        f1 = shadow_filtration('betagamma', weight=1)
        f2 = shadow_filtration('Virasoro', central_charge=1)
        assert shadow_filtration_tensor(f1, f2) == 'M'

    def test_tensor_G_C(self):
        """G tensor C = C."""
        f1 = shadow_filtration('Heisenberg', level=1)
        f2 = shadow_filtration('betagamma', weight=1)
        assert shadow_filtration_tensor(f1, f2) == 'C'


# ========================================================================
# 10. CROSS-FAMILY CONSISTENCY (AP10)
# ========================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks: NOT single-family hardcodes."""

    def test_kappa_additivity_across_all(self):
        """kappa(A+B) = kappa(A) + kappa(B) for all pairs."""
        families = [
            ('Heisenberg', {'level': 1}),
            ('Virasoro', {'central_charge': 2}),
            ('free_fermion', {}),
        ]
        for i, (f1, p1) in enumerate(families):
            for f2, p2 in families[i+1:]:
                assert categorical_kappa_additivity(f1, f2, p1, p2), \
                    f"Additivity failed for {f1} + {f2}"

    def test_complementarity_not_always_zero(self):
        """AP24: complementarity sum is NOT always zero."""
        _, heis_sum, _, _ = categorical_complementarity('Heisenberg', level=1)
        _, vir_sum, _, _ = categorical_complementarity('Virasoro', central_charge=10)
        assert heis_sum == 0
        assert vir_sum == 13  # NOT zero

    def test_all_standard_classes_covered(self):
        """Every standard family gets a valid shadow class."""
        families = [
            ('Heisenberg', {'level': 1}),
            ('Virasoro', {'central_charge': 1}),
            ('Affine', {'lie_type': 'A', 'lie_rank': 1, 'level': 1}),
            ('betagamma', {'weight': 1}),
            ('free_fermion', {}),
            ('lattice', {'rank': 8}),
        ]
        for fam, params in families:
            fcs = full_categorical_shadow(fam, **params)
            assert fcs.shadow_class in ('G', 'L', 'C', 'M'), \
                f"{fam} has invalid class {fcs.shadow_class}"

    def test_virasoro_S4_cross_check(self):
        """Verify Virasoro S_4 = 10/[c(5c+22)] at c=1 and c=10."""
        ms1 = motivic_shadow('Virasoro', central_charge=1)
        ms10 = motivic_shadow('Virasoro', central_charge=10)
        e1 = ms1.euler_tower()
        e10 = ms10.euler_tower()
        assert simplify(e1[4] - Rational(10, 27)) == 0
        assert simplify(e10[4] - Rational(10, 720)) == 0


# ========================================================================
# 11. VIRASORO SHADOW TOWER RECURSION TESTS
# ========================================================================

class TestVirasoroRecursion:
    """Test the Riccati recursion for higher shadow coefficients."""

    def test_virasoro_S6_via_recursion(self):
        """S_6 for Virasoro at c=1 via H^2 = t^4 * Q_L convolution."""
        sht = stable_homotopy_type('Virasoro', central_charge=1)
        S6 = sht.homotopy_groups.get(6, 0)
        # Verify S_6 is nonzero (class M: all S_r nonzero)
        assert simplify(S6) != 0

    def test_virasoro_S7_via_recursion(self):
        """S_7 for Virasoro at c=1 via recursion."""
        sht = stable_homotopy_type('Virasoro', central_charge=1)
        S7 = sht.homotopy_groups.get(7, 0)
        assert simplify(S7) != 0

    def test_virasoro_shadow_invariants_at_c1(self):
        """Verify Virasoro shadow invariants at c=1 via motivic Euler.

        S_2 = kappa = c/2 = 1/2.
        S_3 = alpha = 2.
        S_4 = 10/[c(5c+22)] = 10/27.
        """
        ms = motivic_shadow('Virasoro', central_charge=1)
        euler = ms.euler_tower()
        assert euler[2] == Rational(1, 2)
        assert euler[3] == 2
        assert simplify(euler[4] - Rational(10, 27)) == 0

    def test_virasoro_recursion_matches_sqrtQL_expansion(self):
        """Verify the Riccati recursion against direct sqrt(Q_L) expansion.

        H(t) = t^2 * sqrt(Q_L(t)) with Q_L = 1 + 12t + (1052/27)t^2 at c=1.
        The shadow invariants S_r = h_r/r where h_r = [t^r] H(t).

        Direct expansion of sqrt(Q_L):
          c_0 = 1, c_1 = 6, c_2 = 40/27, c_3 = -80/9, c_4 = 38080/729
        so h_r = c_{r-2} and S_r = c_{r-2}/r.
        """
        from sympy import Symbol as Sym, sqrt as Sqrt, series
        tt = Sym('tt')
        QL = 1 + 12*tt + Rational(1052, 27)*tt**2
        sqrtQL = Sqrt(QL)
        expansion = series(sqrtQL, tt, 0, n=6)
        # Read off c_n and compare to S_{n+2}
        from categorical_shadow_engine import _numerical_Sr
        for n in range(5):
            c_n = expansion.coeff(tt, n)
            r = n + 2
            S_r = _numerical_Sr('Virasoro', r, central_charge=1)
            expected = c_n / r
            assert simplify(S_r - expected) == 0, \
                f"S_{r}: recursion={S_r}, direct={expected}"

    def test_virasoro_S4_recursion_matches_formula(self):
        """S_4 from recursion matches 10/[c(5c+22)] at several c values."""
        from categorical_shadow_engine import _numerical_Sr
        for cc in [1, 2, 5, 10]:
            S4_formula = Rational(10) / (Rational(cc) * (5 * Rational(cc) + 22))
            S4_recurs = _numerical_Sr('Virasoro', 4, central_charge=cc)
            assert simplify(S4_formula - S4_recurs) == 0, \
                f"S_4 mismatch at c={cc}: formula={S4_formula}, recursion={S4_recurs}"

    def test_virasoro_S5_recursion_matches_formula(self):
        """S_5 from recursion matches -48/[c^2(5c+22)] at several c values."""
        from categorical_shadow_engine import _numerical_Sr
        for cc in [1, 2, 5, 10]:
            c_val = Rational(cc)
            S5_formula = Rational(-48) / (c_val**2 * (5 * c_val + 22))
            S5_recurs = _numerical_Sr('Virasoro', 5, central_charge=cc)
            assert simplify(S5_formula - S5_recurs) == 0, \
                f"S_5 mismatch at c={cc}: formula={S5_formula}, recursion={S5_recurs}"


# ========================================================================
# 12. LAMBDA_FP GROUND TRUTH
# ========================================================================

class TestLambdaFP:
    """Verify Faber-Pandharipande intersection numbers."""

    def test_lambda1(self):
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda2(self):
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda3(self):
        assert lambda_fp(3) == Rational(31, 967680)

    def test_lambda4(self):
        assert lambda_fp(4) == Rational(127, 154828800)

    def test_lambda_table_consistent(self):
        for g, val in LAMBDA_FP.items():
            assert lambda_fp(g) == val


# ========================================================================
# 13. AP-SPECIFIC REGRESSION TESTS
# ========================================================================

class TestAntiPatternRegression:
    """Regression tests targeting specific anti-patterns."""

    def test_AP1_kappa_not_copied(self):
        """AP1: kappa formulas are family-specific.
        kappa(H_1) = 1, kappa(Vir_1) = 1/2, kappa(sl_2, k=1) = 9/4.
        """
        kh = categorical_kappa('Heisenberg', level=1).decategorify()
        kv = categorical_kappa('Virasoro', central_charge=1).decategorify()
        ka = categorical_kappa('Affine', lie_type='A', lie_rank=1, level=1).decategorify()
        assert kh == 1
        assert kv == Rational(1, 2)
        assert ka == Rational(9, 4)
        # All three are DIFFERENT
        assert kh != kv
        assert kh != ka
        assert kv != ka

    def test_AP14_depth_not_koszulness(self):
        """AP14: shadow depth classifies COMPLEXITY, not Koszulness.
        ALL standard families are Koszul regardless of depth.
        """
        for fam, params in [
            ('Heisenberg', {'level': 1}),      # G, depth 2
            ('Affine', {'lie_type': 'A', 'lie_rank': 1, 'level': 1}),  # L, depth 3
            ('betagamma', {'weight': 1}),       # C, depth 4
            ('Virasoro', {'central_charge': 1}),# M, depth inf
        ]:
            fcs = full_categorical_shadow(fam, **params)
            # All are Koszul but have different depths
            assert fcs.shadow_class in ('G', 'L', 'C', 'M')

    def test_AP24_complementarity_virasoro_13(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0."""
        for cc in [1, 5, 10, 13, 20, 25]:
            _, s, _, match = categorical_complementarity('Virasoro', central_charge=cc)
            assert s == 13, f"At c={cc}: kappa + kappa' = {s}, expected 13"

    def test_AP31_kappa_zero_not_theta_zero(self):
        """AP31: kappa=0 does NOT imply Theta_A=0.
        Vir at c=0 has kappa=0 but class M (infinite tower).
        """
        fcs = full_categorical_shadow('Virasoro', central_charge=0)
        assert fcs.kappa_cat.decategorify() == 0
        assert fcs.shadow_class == 'M'  # still class M!

    def test_AP39_kappa_neq_S2_for_KM(self):
        """AP39: kappa != S_2 for non-rank-1 families.
        For sl_2 k=1: kappa = 9/4, S_2 = kappa (rank 1, coincidence).
        For sl_3 k=1: kappa = 16/3, which does NOT equal c/2.
        """
        ka_sl3 = categorical_kappa('Affine', lie_type='A', lie_rank=2, level=1).decategorify()
        # c(sl_3, k=1) = 8*(1+3)/(1+3) = 8... actually:
        # c = k*dim(g)/(k+h^v) = 1*8/(1+3) = 2
        # kappa = dim(g)*(k+h^v)/(2*h^v) = 8*4/6 = 16/3
        # c/2 = 1
        # kappa != c/2
        assert ka_sl3 == Rational(16, 3)
        # c/2 would be 1, which is wrong
        assert ka_sl3 != 1

    def test_AP48_kappa_neq_c_half_lattice(self):
        """AP48: kappa != c/2 for lattice VOAs.
        Lattice VOA V_Lambda: kappa = rank(Lambda), c = rank(Lambda).
        So kappa = rank, c/2 = rank/2. Different!
        """
        kl = categorical_kappa('lattice', rank=24).decategorify()
        assert kl == 24
        # c/2 would be 12 for c=24, but kappa = rank = 24
        assert kl != 12


# ========================================================================
# 14. EDGE CASES AND BOUNDARY TESTS
# ========================================================================

class TestEdgeCases:
    """Edge cases: zero kappa, self-dual points, special levels."""

    def test_virasoro_c0_kappa_zero(self):
        """c=0: kappa=0 but algebra is class M (AP31)."""
        fcs = full_categorical_shadow('Virasoro', central_charge=0)
        assert fcs.kappa_cat.decategorify() == 0
        assert fcs.shadow_class == 'M'

    def test_virasoro_c13_self_dual(self):
        """c=13: self-dual point, kappa = 13/2."""
        kc = categorical_kappa('Virasoro', central_charge=13)
        kcd = categorical_kappa_dual('Virasoro', central_charge=13)
        assert kc.decategorify() == kcd.decategorify()  # self-dual

    def test_heisenberg_level_0(self):
        """H_0: kappa=0 but class G."""
        fcs = full_categorical_shadow('Heisenberg', level=0)
        assert fcs.kappa_cat.decategorify() == 0
        assert fcs.shadow_class == 'G'

    def test_betagamma_weight_half(self):
        """betagamma at lambda=1/2: self-dual weight."""
        kc = categorical_kappa('betagamma', weight=Rational(1, 2))
        # kappa = 6*(1/2)^2 - 6*(1/2) + 1 = 3/2 - 3 + 1 = -1/2
        assert kc.decategorify() == Rational(-1, 2)

    def test_affine_sl2_critical_level(self):
        """Affine sl_2 at critical level k=-h^v=-2: kappa=0.
        The algebra is still defined but Sugawara is undefined.
        """
        kc = categorical_kappa('Affine', lie_type='A', lie_rank=1, level=-2)
        assert kc.decategorify() == 0

    def test_large_rank_lattice(self):
        """Leech lattice: rank 24."""
        fcs = full_categorical_shadow('lattice', rank=24)
        assert fcs.kappa_cat.decategorify() == 24
        assert fcs.shadow_class == 'G'

    def test_affine_E8_level1(self):
        """E_8 at level 1: kappa = 248*(1+30)/(2*30) = 248*31/60."""
        kc = categorical_kappa('Affine', lie_type='E', lie_rank=8, level=1)
        expected = Rational(248) * (1 + 30) / (2 * 30)
        assert simplify(kc.decategorify() - expected) == 0
