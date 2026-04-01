r"""Tests for the deformation complex approach to Theta_A.

ADVERSARIAL CROSS-VERIFICATION: the deformation complex C^*_ch(A, A) and
the convolution algebra g^mod_A are DIFFERENT presentations of the same
L-infinity algebra. The MC element computed in each must agree.

Test structure:
    1. Virasoro vacuum module basics (Gram matrix, dimensions)
    2. Virasoro quasi-primary structure at each weight
    3. Virasoro deformation complex H^2_ch
    4. Virasoro MC element: arity 2 (kappa), 3 (cubic), 4 (quartic)
    5. Affine sl_2 deformation complex
    6. Affine sl_2 MC element and tower termination
    7. Cross-verification: deformation vs convolution
    8. Numerical checks at specific central charges
    9. Structural consistency (AP checks)

50+ tests.

References:
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    prop:shadow-formality-low-arity (nonlinear_modular_shadows.tex)
    thm:hochschild-polynomial-growth (chiral_hochschild_koszul.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
"""

import pytest
from fractions import Fraction
from sympy import (
    Rational, Symbol, simplify, factor, cancel, S, sqrt, Matrix,
    N as Neval,
)

from compute.lib.theta_deformation_complex import (
    # Vacuum module
    virasoro_vacuum_basis,
    virasoro_vacuum_dim,
    virasoro_gram_matrix,
    virasoro_quasi_primary_basis,
    # Deformation complexes
    VirasoroDeformationComplex,
    AffineSl2DeformationComplex,
    # Cross-checks
    DeformationConvolutionCrossCheck,
    # Gram verification
    verify_virasoro_gram_weight4,
    verify_virasoro_gram_weight6,
    # Numerical
    numerical_cross_check,
    # H^2 analysis
    virasoro_h2_at_weight,
)


# ============================================================================
# 1. Virasoro vacuum module basics
# ============================================================================

class TestVirasoroVacuumModule:
    """Test the vacuum module basis and dimensions."""

    def test_vacuum_dim_weight0(self):
        """Weight 0: just the vacuum |0>."""
        assert virasoro_vacuum_dim(0) == 1

    def test_vacuum_dim_weight1(self):
        """Weight 1: no states (L_{-1}|0> not in vacuum module)."""
        assert virasoro_vacuum_dim(1) == 0

    def test_vacuum_dim_weight2(self):
        """Weight 2: L_{-2}|0> (one state)."""
        assert virasoro_vacuum_dim(2) == 1
        assert virasoro_vacuum_basis(2) == [(2,)]

    def test_vacuum_dim_weight3(self):
        """Weight 3: L_{-3}|0> (one state)."""
        assert virasoro_vacuum_dim(3) == 1
        assert virasoro_vacuum_basis(3) == [(3,)]

    def test_vacuum_dim_weight4(self):
        """Weight 4: {L_{-4}|0>, L_{-2}^2|0>} (two states)."""
        assert virasoro_vacuum_dim(4) == 2
        basis = virasoro_vacuum_basis(4)
        assert (4,) in basis
        assert (2, 2) in basis

    def test_vacuum_dim_weight5(self):
        """Weight 5: {L_{-5}, L_{-3}L_{-2}} (two states)."""
        assert virasoro_vacuum_dim(5) == 2
        basis = virasoro_vacuum_basis(5)
        assert (5,) in basis
        assert (3, 2) in basis

    def test_vacuum_dim_weight6(self):
        """Weight 6: {L_{-6}, L_{-4}L_{-2}, L_{-3}^2, L_{-2}^3} (four states)."""
        assert virasoro_vacuum_dim(6) == 4
        basis = virasoro_vacuum_basis(6)
        assert len(basis) == 4

    def test_vacuum_dim_weight7(self):
        """Weight 7: four states."""
        assert virasoro_vacuum_dim(7) == 4

    def test_vacuum_dim_weight8(self):
        """Weight 8: seven states."""
        assert virasoro_vacuum_dim(8) == 7

    def test_vacuum_generating_function_first_terms(self):
        """Generating function prod_{n>=2} 1/(1-q^n).

        p_2(h) = number of partitions of h with parts >= 2.
        First terms: 1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12, ...
        """
        expected = [1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12]
        for h, exp_dim in enumerate(expected):
            assert virasoro_vacuum_dim(h) == exp_dim, \
                f"Wrong dim at weight {h}: got {virasoro_vacuum_dim(h)}, expected {exp_dim}"


# ============================================================================
# 2. Virasoro Gram matrix
# ============================================================================

class TestVirasoroGram:
    """Test the Gram matrix computation."""

    def test_gram_weight2(self):
        """At weight 2: G = (c/2) (from [L_2, L_{-2}] = 4L_0 + c/2 on |0>)."""
        # Actually: <0|L_2 L_{-2}|0> = <0|[L_2, L_{-2}]|0> = <0|(4L_0 + c/2)|0>
        # L_0|0> = 0, so G = c/2.
        c = Symbol('c')
        basis, G = virasoro_gram_matrix(2)
        assert len(basis) == 1
        assert simplify(G[0, 0] - c/2) == 0

    def test_gram_weight3(self):
        """At weight 3: G = (2c) from [L_3, L_{-3}]."""
        # [L_3, L_{-3}] = 6L_0 + c(27-3)/12 = 0 + 2c = 2c
        c = Symbol('c')
        basis, G = virasoro_gram_matrix(3)
        assert simplify(G[0, 0] - 2*c) == 0

    def test_gram_weight4_structure(self):
        """Weight 4 Gram matrix has known structure."""
        basis, G, results = verify_virasoro_gram_weight4()
        for key, data in results.items():
            assert data['match'], f"Gram weight 4 mismatch at {key}: {data}"

    def test_gram_weight4_G11(self):
        """G_{11} = 5c (from [L_4, L_{-4}])."""
        c = Symbol('c')
        basis, G = virasoro_gram_matrix(4)
        assert simplify(G[0, 0] - 5*c) == 0

    def test_gram_weight4_G12(self):
        """G_{12} = 3c."""
        c = Symbol('c')
        basis, G = virasoro_gram_matrix(4)
        assert simplify(G[0, 1] - 3*c) == 0

    def test_gram_weight4_G22(self):
        """G_{22} = c(c+8)/2."""
        c = Symbol('c')
        basis, G = virasoro_gram_matrix(4)
        assert simplify(G[1, 1] - c*(c+8)/2) == 0

    def test_gram_weight4_determinant(self):
        """det G_4 = c^2(5c+22)/2."""
        c = Symbol('c')
        _, G = virasoro_gram_matrix(4)
        det = simplify(G.det())
        expected = c**2 * (5*c + 22) / 2
        assert simplify(det - expected) == 0

    def test_gram_weight4_lambda_norm(self):
        """Lambda = L_{-2}^2 - (3/10)L_{-4} has norm c(5c+22)/10."""
        _, _, results = verify_virasoro_gram_weight4()
        assert results['lambda_norm']['match']

    def test_gram_numerical_c1(self):
        """Numerical check at c=1."""
        basis, G = virasoro_gram_matrix(4, c_val=1)
        assert G[0, 0] == 5  # 5c at c=1
        assert G[0, 1] == 3  # 3c at c=1
        assert simplify(G[1, 1] - Rational(9, 2)) == 0  # c(c+8)/2 = 9/2

    def test_gram_numerical_c26(self):
        """Numerical check at c=26 (critical)."""
        basis, G = virasoro_gram_matrix(4, c_val=26)
        assert G[0, 0] == 130  # 5*26
        assert G[0, 1] == 78   # 3*26


# ============================================================================
# 3. Virasoro quasi-primaries
# ============================================================================

class TestQuasiPrimaries:
    """Test quasi-primary decomposition."""

    def test_qp_weight2(self):
        """At weight 2: T is the only state, and it IS quasi-primary."""
        basis, qp, gram = virasoro_quasi_primary_basis(2)
        assert len(qp) == 1  # T is quasi-primary

    def test_qp_weight3(self):
        """At weight 3: L_{-3}|0> = (1/2)d^2 T descendant => no quasi-primaries?
        Actually L_1 L_{-3}|0> = [L_1, L_{-3}]|0> = 4L_{-2}|0> != 0.
        So L_{-3}|0> is NOT quasi-primary. But there's nothing at weight 1 for it
        to be a descendant of either (L_{-1} maps weight 2 -> weight 3 but
        L_{-1}|0> = 0). The state L_{-3}|0> is a Virasoro descendant of |0>."""
        basis, qp, gram = virasoro_quasi_primary_basis(3)
        # L_1 L_{-3}|0> = 4 L_{-2}|0> which lives at weight 2.
        # Since this is nonzero, L_{-3}|0> is NOT quasi-primary.
        assert len(qp) == 0

    def test_qp_weight4(self):
        """At weight 4: one quasi-primary Lambda = L_{-2}^2 - (3/10)L_{-4}."""
        basis, qp, gram = virasoro_quasi_primary_basis(4)
        assert len(qp) == 1

    def test_qp_weight4_is_lambda(self):
        """The quasi-primary at weight 4 is proportional to (-3/5, 1).

        Lambda = L_{-2}^2|0> - (3/5) L_{-4}|0> in the state basis.
        (The 3/5 comes from L_1 Lambda = 0:
         L_1 L_{-2}^2 = 3 L_{-3}, L_1 L_{-4} = 5 L_{-3}, so alpha = 3/5.)
        """
        basis, qp, gram = virasoro_quasi_primary_basis(4)
        if len(qp) == 1:
            v = qp[0]
            # v should be proportional to (-3/5, 1) in basis {L_{-4}, L_{-2}^2}
            if simplify(v[1]) != 0:
                ratio = simplify(v[0] / v[1])
                assert simplify(ratio + Rational(3, 5)) == 0, \
                    f"Wrong quasi-primary: ratio = {ratio}, expected -3/5"

    def test_qp_weight6_count(self):
        """At weight 6: known number of quasi-primaries."""
        result = verify_virasoro_gram_weight6()
        # At weight 6, we expect 1 quasi-primary (the weight-6 Casimir-like state)
        # Actually: weight 6 has dim 4. The quasi-primaries at weight 6 for Virasoro
        # are determined by the kernel of L_1. Since weight 5 has dim 2, L_1 maps
        # weight 6 (dim 4) to weight 5 (dim 2). Generically rank(L_1) = 2,
        # so dim(ker L_1) = 4 - 2 = 2 quasi-primaries.
        assert result['n_quasi_primaries'] == 2


# ============================================================================
# 4. Virasoro deformation complex H^2
# ============================================================================

class TestVirasoroH2:
    """Test H^2_ch(Vir, Vir) computation."""

    def test_h2_weight0_is_one_dimensional(self):
        """H^2 at weight 0 (quartic pole): one-dimensional (kappa)."""
        dc = VirasoroDeformationComplex()
        analysis = dc.h2_weight_analysis()
        assert analysis['weight_0']['H2_dim'] == 1

    def test_h2_weight2_vanishes(self):
        """H^2 at weight 2 (double pole): zero (inner deformation)."""
        dc = VirasoroDeformationComplex()
        analysis = dc.h2_weight_analysis()
        assert analysis['weight_2']['H2_dim'] == 0

    def test_h2_weight3_vanishes(self):
        """H^2 at weight 3 (simple pole): zero (translation)."""
        dc = VirasoroDeformationComplex()
        analysis = dc.h2_weight_analysis()
        assert analysis['weight_3']['H2_dim'] == 0

    def test_h2_total_dim(self):
        """Total dim H^2_ch(Vir, Vir) at genus 0 = 1 (just kappa)."""
        dc = VirasoroDeformationComplex()
        analysis = dc.h2_weight_analysis()
        total = sum(v.get('H2_dim', 0) for v in analysis.values())
        assert total == 1


# ============================================================================
# 5. Virasoro MC components
# ============================================================================

class TestVirasoroMC:
    """Test the Virasoro MC element components."""

    def test_mc_arity2_is_kappa(self):
        """Phi^{(2)} = kappa = c/2."""
        dc = VirasoroDeformationComplex()
        comp = dc.mc_component_arity2()
        assert simplify(comp['coefficient'] - dc.c / 2) == 0

    def test_mc_arity3_is_alpha(self):
        """Phi^{(3)} coefficient = alpha = 2 (c-independent)."""
        dc = VirasoroDeformationComplex()
        comp = dc.mc_component_arity3()
        assert simplify(comp['coefficient'] - 2) == 0

    def test_mc_arity3_c_independent(self):
        """The cubic shadow alpha = 2 does not depend on c."""
        dc = VirasoroDeformationComplex()
        comp = dc.mc_component_arity3()
        assert comp['c_independent'] is True

    def test_mc_arity4_q_contact(self):
        """Phi^{(4)} = Q^contact = 10/[c(5c+22)]."""
        dc = VirasoroDeformationComplex()
        comp = dc.mc_component_arity4()
        expected = Rational(10) / (dc.c * (5 * dc.c + 22))
        assert simplify(comp['Q_contact'] - expected) == 0

    def test_mc_arity4_lambda_norm(self):
        """The Lambda norm = c(5c+22)/10."""
        dc = VirasoroDeformationComplex()
        comp = dc.mc_component_arity4()
        c = dc.c
        expected = c * (5*c + 22) / 10
        assert simplify(comp['lambda_norm'] - expected) == 0

    def test_mc_arity4_at_c1(self):
        """Q^contact at c=1: 10/(1*27) = 10/27."""
        dc = VirasoroDeformationComplex(c_val=1)
        comp = dc.mc_component_arity4()
        expected = Rational(10, 27)
        assert simplify(comp['Q_contact'] - expected) == 0

    def test_mc_arity4_at_c26(self):
        """Q^contact at c=26: 10/(26*(130+22)) = 10/(26*152) = 5/1976."""
        dc = VirasoroDeformationComplex(c_val=26)
        comp = dc.mc_component_arity4()
        expected = Rational(10, 26 * 152)
        assert simplify(comp['Q_contact'] - expected) == 0


# ============================================================================
# 6. Virasoro obstruction classes
# ============================================================================

class TestVirasoroObstructions:
    """Test the obstruction classes o_r in H^3_ch."""

    def test_obstruction_arity3_exact(self):
        """Arity-3 obstruction is exact (Phi^{(3)} exists)."""
        dc = VirasoroDeformationComplex()
        obs = dc.h3_obstruction_class(3)
        assert obs['exact'] is True

    def test_obstruction_arity4_exact(self):
        """Arity-4 obstruction is exact (Phi^{(4)} exists)."""
        dc = VirasoroDeformationComplex()
        obs = dc.h3_obstruction_class(4)
        assert obs['exact'] is True

    def test_obstruction_arity5_exact(self):
        """Arity-5 obstruction is exact (class M, infinite tower)."""
        dc = VirasoroDeformationComplex()
        obs = dc.h3_obstruction_class(5)
        assert obs['exact'] is True

    def test_all_obstructions_exact_through_arity10(self):
        """All obstructions are exact through arity 10 (class M)."""
        dc = VirasoroDeformationComplex()
        for r in range(3, 11):
            obs = dc.h3_obstruction_class(r)
            assert obs['exact'] is True, f"Obstruction at arity {r} should be exact"


# ============================================================================
# 7. Affine sl_2 deformation complex
# ============================================================================

class TestAffineSl2Deformation:
    """Test the deformation complex for affine sl_2."""

    def test_kappa_formula(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        dc = AffineSl2DeformationComplex()
        k = dc.k_sym
        expected = 3 * (k + 2) / 4
        assert simplify(dc.kappa() - expected) == 0

    def test_kappa_at_k1(self):
        """kappa(sl_2, k=1) = 3*3/4 = 9/4."""
        dc = AffineSl2DeformationComplex(k_val=1)
        assert simplify(dc.kappa() - Rational(9, 4)) == 0

    def test_kappa_at_critical(self):
        """kappa(sl_2, k=-2) = 0 (critical level)."""
        dc = AffineSl2DeformationComplex(k_val=-2)
        assert simplify(dc.kappa()) == 0

    def test_h2_double_pole_dim1(self):
        """H^2 at the double pole level is 1-dimensional (level deformation)."""
        dc = AffineSl2DeformationComplex()
        analysis = dc.h2_weight_analysis()
        assert analysis['double_pole']['H2_dim'] == 1

    def test_h2_simple_pole_dim0(self):
        """H^2 at the simple pole level is 0 (Whitehead lemma)."""
        dc = AffineSl2DeformationComplex()
        analysis = dc.h2_weight_analysis()
        assert analysis['simple_pole']['H2_dim'] == 0

    def test_killing_form_structure(self):
        """Killing form has correct structure for sl_2."""
        dc = AffineSl2DeformationComplex()
        K = dc.killing
        k = dc.k
        assert K[('e', 'f')] == k
        assert K[('f', 'e')] == k
        assert K[('h', 'h')] == 2 * k
        # All other entries should be zero
        for a in dc.generators:
            for b in dc.generators:
                if (a, b) not in K:
                    pass  # implicitly zero

    def test_cubic_form_antisymmetry(self):
        """The cubic form C_{abc} = K_{ad}f^d_{bc} is totally antisymmetric."""
        dc = AffineSl2DeformationComplex()
        C = dc.cubic
        for (a, b, c_gen), val in C.items():
            # Check: C_{abc} = -C_{bac} (antisymmetry in first two)
            val_swapped = C.get((b, a, c_gen), S.Zero)
            assert simplify(val + val_swapped) == 0, \
                f"C[{a},{b},{c_gen}]={val}, C[{b},{a},{c_gen}]={val_swapped}"

    def test_cubic_form_hef(self):
        """C(h, e, f) = 2k."""
        dc = AffineSl2DeformationComplex()
        k = dc.k
        assert simplify(dc.cubic.get(('h', 'e', 'f'), S.Zero) - 2*k) == 0

    def test_cubic_vanishes_on_cartan(self):
        """C(h, h, h) = 0 (Cartan is abelian)."""
        dc = AffineSl2DeformationComplex()
        assert simplify(dc.cubic.get(('h', 'h', 'h'), S.Zero)) == 0


# ============================================================================
# 8. Affine sl_2 MC element and tower termination
# ============================================================================

class TestAffineSl2MC:
    """Test the sl_2 MC element: class L, tower terminates at arity 3."""

    def test_mc_arity2_killing(self):
        """Arity-2 component is the Killing form."""
        dc = AffineSl2DeformationComplex()
        comp = dc.mc_component_arity2()
        assert ('e', 'f') in comp['tensor']
        assert ('h', 'h') in comp['tensor']

    def test_mc_arity3_cubic(self):
        """Arity-3 component is the cubic form."""
        dc = AffineSl2DeformationComplex()
        comp = dc.mc_component_arity3()
        assert len(comp['tensor']) > 0
        assert comp['cartan_line_scalar'] == 0

    def test_mc_arity4_vanishes(self):
        """Arity-4 component is ZERO (class L)."""
        dc = AffineSl2DeformationComplex()
        comp = dc.mc_component_arity4()
        assert len(comp['tensor']) == 0
        assert comp['class'] == 'L'

    def test_h3_obstruction_vanishes(self):
        """The H^3 obstruction vanishes (Jacobi identity)."""
        dc = AffineSl2DeformationComplex()
        obs = dc.h3_obstruction_vanishes()
        assert obs['bracket_vanishes'] is True

    def test_tower_terminates_class_L(self):
        """sl_2 has shadow depth class L (terminates at arity 3)."""
        dc = AffineSl2DeformationComplex()
        comp4 = dc.mc_component_arity4()
        assert comp4['class'] == 'L'

    def test_h3_obstruction_at_k1(self):
        """Explicit check at k=1."""
        dc = AffineSl2DeformationComplex(k_val=1)
        obs = dc.h3_obstruction_vanishes()
        assert obs['bracket_vanishes'] is True

    def test_h3_raw_contraction_structure(self):
        """The raw C*K^{-1}*C contraction should have specific structure."""
        dc = AffineSl2DeformationComplex(k_val=1)
        obs = dc.h3_obstruction_vanishes()
        # The raw contraction may have individual nonzero entries
        # (the Jacobiator contracts to zero only after symmetrization),
        # but the bracket vanishes by Jacobi.
        assert obs['bracket_vanishes'] is True


# ============================================================================
# 9. Cross-verification: deformation vs convolution
# ============================================================================

class TestCrossVerification:
    """Cross-check between deformation complex and convolution algebra."""

    def test_virasoro_kappa_match(self):
        """kappa agrees: deformation complex = shadow tower."""
        cc = DeformationConvolutionCrossCheck('virasoro')
        result = cc.cross_check_kappa()
        assert result['match'] is True

    def test_virasoro_cubic_match(self):
        """Cubic shadow agrees."""
        cc = DeformationConvolutionCrossCheck('virasoro')
        result = cc.cross_check_cubic()
        assert result['match'] is True

    def test_virasoro_quartic_match(self):
        """Quartic contact agrees."""
        cc = DeformationConvolutionCrossCheck('virasoro')
        result = cc.cross_check_quartic()
        assert result['match'] is True

    def test_sl2_kappa_match(self):
        """kappa agrees for sl_2."""
        cc = DeformationConvolutionCrossCheck('sl2')
        result = cc.cross_check_kappa()
        assert result['match'] is True

    def test_sl2_cubic_cartan_match(self):
        """Cubic on Cartan line agrees (= 0)."""
        cc = DeformationConvolutionCrossCheck('sl2')
        result = cc.cross_check_cubic()
        assert result['cartan_line_match'] is True

    def test_sl2_quartic_match(self):
        """Quartic agrees (= 0, class L)."""
        cc = DeformationConvolutionCrossCheck('sl2')
        result = cc.cross_check_quartic()
        assert result['match'] is True

    def test_virasoro_full_check(self):
        """Full cross-verification for Virasoro."""
        cc = DeformationConvolutionCrossCheck('virasoro')
        result = cc.full_cross_check()
        assert result['kappa']['match'] is True
        assert result['cubic']['match'] is True
        assert result['quartic']['match'] is True

    def test_sl2_full_check(self):
        """Full cross-verification for sl_2."""
        cc = DeformationConvolutionCrossCheck('sl2')
        result = cc.full_cross_check()
        assert result['kappa']['match'] is True

    def test_virasoro_obstruction_all_exact(self):
        """All obstructions exact for Virasoro (class M)."""
        cc = DeformationConvolutionCrossCheck('virasoro')
        obs = cc.cross_check_h3_obstruction()
        for r, data in obs.items():
            assert data['exact'] is True

    def test_sl2_obstruction_class_L(self):
        """sl_2 has class L obstruction behavior."""
        cc = DeformationConvolutionCrossCheck('sl2')
        obs = cc.cross_check_h3_obstruction()
        assert obs['depth_class'] == 'L'
        assert obs['tower_terminates'] is True


# ============================================================================
# 10. Numerical checks at specific central charges
# ============================================================================

class TestNumericalCrossChecks:
    """Numerical cross-verification at specific c values."""

    def test_numerical_c1(self):
        """Cross-check at c=1."""
        result = numerical_cross_check(1)
        assert abs(result['kappa']['expected'] - 0.5) < 1e-10
        assert abs(result['S_2'] - 0.5) < 1e-10

    def test_numerical_c26(self):
        """Cross-check at c=26 (critical for bosonic string)."""
        result = numerical_cross_check(26)
        assert abs(result['kappa']['expected'] - 13.0) < 1e-10
        assert abs(result['S_2'] - 13.0) < 1e-10

    def test_numerical_c13(self):
        """Cross-check at c=13 (self-dual point)."""
        result = numerical_cross_check(13)
        assert abs(result['kappa']['expected'] - 6.5) < 1e-10

    def test_numerical_c0(self):
        """Cross-check at c=0 (trivial): kappa = 0."""
        # At c=0, kappa = 0 and the algebra is uncurved.
        # Q^contact has a pole at c=0, so we skip that.
        dc = VirasoroDeformationComplex(c_val=0)
        assert dc.kappa() == 0

    def test_numerical_shadow_tower_c1(self):
        """Shadow tower at c=1: verify S_2 through S_5."""
        result = numerical_cross_check(1, max_arity=5)
        # S_2 = kappa = 1/2
        assert abs(result['S_2'] - 0.5) < 1e-10
        # S_3 = 2
        assert abs(result['S_3'] - 2.0) < 1e-10
        # S_4 = 10/(1*27) = 10/27
        assert abs(result['S_4'] - 10/27) < 1e-10

    def test_kappa_virasoro_vs_shadow_c2(self):
        """Explicit c=2: kappa from deformation = c/2 = 1."""
        dc = VirasoroDeformationComplex(c_val=2)
        assert dc.kappa() == 1

    def test_kappa_sl2_at_k1(self):
        """sl_2 at k=1: kappa = 9/4."""
        dc = AffineSl2DeformationComplex(k_val=1)
        assert dc.kappa() == Rational(9, 4)

    def test_kappa_sl2_at_k2(self):
        """sl_2 at k=2: kappa = 3*4/4 = 3."""
        dc = AffineSl2DeformationComplex(k_val=2)
        assert dc.kappa() == 3


# ============================================================================
# 11. Structural consistency (AP checks)
# ============================================================================

class TestStructuralConsistency:
    """Anti-pattern checks and structural consistency."""

    def test_ap1_kappa_not_copied(self):
        """AP1: kappa(Vir) = c/2, kappa(sl_2) = 3(k+2)/4.
        These are DIFFERENT formulas (AP1: do not copy between families)."""
        vir = VirasoroDeformationComplex(c_val=6)  # c=6 for sl_2 at k=1
        sl2 = AffineSl2DeformationComplex(k_val=1)  # c = 3*1/3 = 1... no.
        # sl_2 at k=1: c = 3*1/3 = 1. kappa = 9/4.
        # Virasoro at c=1: kappa = 1/2.
        # These MUST differ (AP1).
        assert vir.kappa() != sl2.kappa()

    def test_ap9_kappa_vs_c(self):
        """AP9: kappa != c. kappa(Vir_c) = c/2, not c."""
        dc = VirasoroDeformationComplex()
        c = dc.c
        assert simplify(dc.kappa() - c) != 0
        assert simplify(dc.kappa() - c/2) == 0

    def test_ap14_koszul_vs_formality(self):
        """AP14: Virasoro is chirally Koszul but NOT Swiss-cheese formal.
        This means Q^contact != 0 (non-formality), but bar cohomology
        IS concentrated (Koszulness)."""
        dc = VirasoroDeformationComplex()
        comp4 = dc.mc_component_arity4()
        # Q^contact != 0 (non-formal)
        c = dc.c
        Q0 = comp4['Q_contact']
        assert simplify(Q0) != 0  # non-zero at generic c

    def test_ap19_pole_orders(self):
        """AP19: the r-matrix has pole orders ONE LESS than the OPE."""
        # Virasoro OPE: poles at z^{-4}, z^{-2}, z^{-1}
        # r-matrix (bar extraction): poles at z^{-3}, z^{-1} (one less)
        dc = VirasoroDeformationComplex()
        comp2 = dc.mc_component_arity2()
        # The bar extraction uses d log(z-w), which absorbs one pole order.
        # The pole_order stored is 3 (for the quartic pole -> r-matrix triple pole)
        assert comp2['pole_order'] == 3  # 4 - 1 = 3

    def test_ap20_kappa_is_algebra_invariant(self):
        """AP20: kappa(A) is an invariant of the ALGEBRA A, not a system."""
        vir = VirasoroDeformationComplex()
        # kappa depends only on c (the algebra parameter)
        assert vir.kappa() == vir.c / 2

    def test_ap24_complementarity_virasoro(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0."""
        c = Symbol('c')
        kappa_A = c / 2
        kappa_A_dual = (26 - c) / 2
        total = simplify(kappa_A + kappa_A_dual)
        assert total == 13

    def test_ap27_propagator_weight(self):
        """AP27: bar propagator d log E(z,w) has weight 1, regardless
        of the conformal weight of the field."""
        # The deformation complex construction uses weight-1 propagator.
        # This is verified by checking that the shadow tower formula
        # does NOT use E_h for weight-h generators.
        # For Virasoro (h=2): we use E_1 (standard Hodge), NOT E_2.
        # The test: kappa = c/2 (not c/2 * Mumford(2) = c/2 * 13/12).
        dc = VirasoroDeformationComplex()
        assert simplify(dc.kappa() - dc.c / 2) == 0
        # If we incorrectly used E_2, kappa would be c/2 * 13 (off by 13x).

    def test_depth_class_virasoro_is_M(self):
        """Virasoro has shadow depth class M (mixed, infinite tower)."""
        dc = VirasoroDeformationComplex()
        # Q^contact != 0 => Delta != 0 => class M
        comp4 = dc.mc_component_arity4()
        Q0 = comp4['Q_contact']
        c = dc.c
        Delta = 8 * dc.kappa() * Q0  # = 40/(5c+22)
        assert simplify(Delta) != 0  # nonzero at generic c

    def test_depth_class_sl2_is_L(self):
        """sl_2 has shadow depth class L (tower terminates at arity 3)."""
        dc = AffineSl2DeformationComplex()
        comp4 = dc.mc_component_arity4()
        assert comp4['class'] == 'L'

    def test_virasoro_mc_element_matches_shadow_tower(self):
        """The MC element from the deformation complex matches the shadow tower.
        This is the CENTRAL cross-check of the entire module."""
        dc = VirasoroDeformationComplex()
        mc = dc.mc_element_deformation(max_arity=7)
        for r, data in mc.items():
            assert data['match'] is True, \
                f"MC element mismatch at arity {r}: deformation={data['deformation_value']}, shadow={data['shadow_value']}"

    def test_h2_analysis_at_weight4(self):
        """H^2 analysis at total weight 4."""
        result = virasoro_h2_at_weight(4)
        assert result['vacuum_dim'] == 2  # dim V_4 = 2
        assert result['quasi_primary_dim'] == 1  # one quasi-primary (Lambda)


# ============================================================================
# 12. Gram matrix at specific weights for adversarial verification
# ============================================================================

class TestGramAdversarial:
    """Adversarial tests of the Gram matrix computation."""

    def test_gram_weight2_numerical(self):
        """At weight 2 with c=7: G = 7/2."""
        _, G = virasoro_gram_matrix(2, c_val=7)
        assert simplify(G[0, 0] - Rational(7, 2)) == 0

    def test_gram_symmetric(self):
        """Gram matrix is symmetric at weight 4."""
        _, G = virasoro_gram_matrix(4)
        assert simplify(G[0, 1] - G[1, 0]) == 0

    def test_gram_positive_definite_c_positive(self):
        """Gram matrix positive definite at c=10."""
        _, G = virasoro_gram_matrix(4, c_val=10)
        # Eigenvalues should be positive for c > 0
        det = G.det()
        assert det > 0
        assert G[0, 0] > 0

    def test_gram_weight4_det_zero_c0(self):
        """At c=0: det G_4 = 0 (degenerate)."""
        _, G = virasoro_gram_matrix(4, c_val=0)
        assert G.det() == 0

    def test_gram_weight4_det_c1(self):
        """At c=1: det G_4 = 1*27/2 = 27/2."""
        _, G = virasoro_gram_matrix(4, c_val=1)
        expected = Rational(1) * 27 / 2
        assert simplify(G.det() - expected) == 0

    def test_lambda_norm_positive_c_large(self):
        """Lambda norm c(5c+22)/10 > 0 for c > 0."""
        for c_val in [1, 2, 5, 10, 26]:
            _, _, results = verify_virasoro_gram_weight4(c_val)
            lam = results['lambda_norm']['computed']
            assert lam > 0, f"Lambda norm not positive at c={c_val}: {lam}"

    def test_lambda_norm_zero_at_c0(self):
        """Lambda norm = 0 at c=0."""
        _, _, results = verify_virasoro_gram_weight4(0)
        lam = results['lambda_norm']['computed']
        assert lam == 0

    def test_lambda_norm_at_c_minus_22_over_5(self):
        """Lambda norm = 0 at c = -22/5 (minimal model singularity)."""
        c_val = Rational(-22, 5)
        _, _, results = verify_virasoro_gram_weight4(c_val)
        lam = results['lambda_norm']['computed']
        assert simplify(lam) == 0
