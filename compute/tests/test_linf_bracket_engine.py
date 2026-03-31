r"""Tests for the L-infinity bracket engine.

Verifies:
1. Virasoro OPE bracket correctness (Jacobi identity)
2. Invariant bilinear form properties (symmetry, ad-invariance)
3. ell_3 computation for the four archetype classes (G/L/C/M)
4. Shadow--formality identification (S_r = ell_r^{(0),tr})
5. Operadic complexity theorem (r_max = d_infinity = f_infinity)
6. Cross-checks against virasoro_shadow_all_arity.py

KEY RESULT: ell_3 = S_3 = 2 for Virasoro (NONZERO, confirming
non-formality of the genus-0 L-infinity structure for class M algebras).

References:
  prop:shadow-formality-low-arity (higher_genus_modular_koszul.tex)
  thm:operadic-complexity-detailed (higher_genus_modular_koszul.tex)
  ex:operadic-complexity-verification (higher_genus_modular_koszul.tex)
"""

import pytest
from fractions import Fraction

F = Fraction

from compute.lib.linf_bracket_engine import (
    virasoro_bracket,
    witt_bracket,
    virasoro_jacobi_check,
    shapovalov_inner_product,
    killing_form_virasoro,
    propagator_virasoro,
    ell3_virasoro_on_modes,
    VirasoroDefComplex,
    LInfBracketComputer,
    ell3_virasoro_explicit,
    ell3_virasoro_three_channel,
    ell3_heisenberg,
    ell3_affine_sl2,
    ell3_betagamma,
    verify_operadic_complexity,
)


# ============================================================================
# 1. Virasoro OPE bracket correctness
# ============================================================================

class TestVirasoroOPE:
    """Test the Virasoro commutation relations."""

    def test_bracket_basic(self):
        """[L_1, L_{-1}] = 2 L_0."""
        result = virasoro_bracket(1, -1, F(0))
        assert result.get(('L', 0)) == F(2)

    def test_bracket_with_central(self):
        """[L_2, L_{-2}] = 4 L_0 + (c/12)*2*(4-1) = 4 L_0 + c/2."""
        c = F(25)
        result = virasoro_bracket(2, -2, c)
        assert result.get(('L', 0)) == F(4)
        assert result.get(('c',)) == c / F(2)

    def test_bracket_central_m1(self):
        """[L_1, L_{-1}] = 2 L_0 + 0 (central charge piece = 0)."""
        c = F(25)
        result = virasoro_bracket(1, -1, c)
        assert result.get(('L', 0)) == F(2)
        # Central: c/12 * 1 * (1-1) = 0
        assert result.get(('c',), F(0)) == F(0)

    def test_bracket_central_m2(self):
        """[L_2, L_{-2}]: central piece = c/12 * 2 * 3 = c/2."""
        c = F(26)
        result = virasoro_bracket(2, -2, c)
        assert result[('c',)] == c * F(2) * F(3) / F(12)
        assert result[('c',)] == c / F(2)

    def test_bracket_central_m3(self):
        """[L_3, L_{-3}]: central piece = c/12 * 3 * 8 = 2c."""
        c = F(10)
        result = virasoro_bracket(3, -3, c)
        assert result[('c',)] == c * F(3) * F(8) / F(12)
        assert result[('c',)] == F(2) * c

    def test_bracket_L0_eigenvalue(self):
        """[L_0, L_n] = -n L_n."""
        for n in range(-5, 6):
            if n == 0:
                continue
            result = virasoro_bracket(0, n, F(25))
            assert result.get(('L', n)) == F(-n)

    def test_bracket_antisymmetry(self):
        """[L_m, L_n] = -[L_n, L_m]."""
        c = F(7, 3)
        for m in range(-4, 5):
            for n in range(-4, 5):
                r1 = virasoro_bracket(m, n, c)
                r2 = virasoro_bracket(n, m, c)
                for key in set(list(r1.keys()) + list(r2.keys())):
                    assert r1.get(key, F(0)) == -r2.get(key, F(0)), \
                        f"Antisymmetry failed for m={m}, n={n}, key={key}"


class TestJacobi:
    """Verify the Jacobi identity for the Virasoro algebra."""

    def test_jacobi_small_modes(self):
        """Jacobi identity for small modes."""
        c = F(25)
        for m in range(-3, 4):
            for n in range(-3, 4):
                for p in range(-3, 4):
                    assert virasoro_jacobi_check(m, n, p, c), \
                        f"Jacobi failed for m={m}, n={n}, p={p}"

    def test_jacobi_witt(self):
        """Jacobi identity for the Witt algebra (c=0)."""
        for m in range(-4, 5):
            for n in range(-4, 5):
                for p in range(-4, 5):
                    assert virasoro_jacobi_check(m, n, p, F(0))

    def test_jacobi_various_c(self):
        """Jacobi identity at various central charges."""
        for c_val in [F(1), F(1, 2), F(26), F(-2), F(25, 7)]:
            for m in range(-2, 3):
                for n in range(-2, 3):
                    for p in range(-2, 3):
                        assert virasoro_jacobi_check(m, n, p, c_val)


class TestJacobiatorVanishing:
    """Verify that the three-channel sum vanishes (Jacobi identity).

    ell_3 on the LIE ALGEBRA modes vanishes because
    [a,[b,c]] + [b,[c,a]] + [c,[a,b]] = 0 by Jacobi.
    """

    def test_three_channel_vanishes(self):
        """The three-channel sum vanishes for all mode triples."""
        c = F(25)
        for m in range(-3, 4):
            for n in range(-3, 4):
                for p in range(-3, 4):
                    result = ell3_virasoro_on_modes(m, n, p, c)
                    for key, val in result.items():
                        assert val == F(0), \
                            f"Three-channel nonzero at m={m},n={n},p={p}: {key}={val}"


# ============================================================================
# 2. Invariant bilinear form
# ============================================================================

class TestBilinearForm:
    """Test the invariant bilinear form on Virasoro."""

    def test_symmetry(self):
        """eta(L_m, L_n) = eta(L_n, L_m)."""
        c = F(25)
        for m in range(-5, 6):
            for n in range(-5, 6):
                assert killing_form_virasoro(m, n, c) == killing_form_virasoro(n, m, c)

    def test_pairing_modes(self):
        """eta(L_m, L_n) = 0 unless m+n = 0."""
        c = F(25)
        for m in range(-5, 6):
            for n in range(-5, 6):
                if m + n != 0:
                    assert killing_form_virasoro(m, n, c) == F(0)

    def test_specific_values(self):
        """eta(L_m, L_{-m}) = (c/12) m(m^2-1)."""
        c = F(25)
        assert killing_form_virasoro(0, 0, c) == F(0)  # m=0: 0*(0-1)=0
        assert killing_form_virasoro(1, -1, c) == F(0)  # m=1: 1*(1-1)=0
        assert killing_form_virasoro(2, -2, c) == c * F(6) / F(12)  # = c/2
        assert killing_form_virasoro(3, -3, c) == c * F(24) / F(12)  # = 2c
        assert killing_form_virasoro(4, -4, c) == c * F(60) / F(12)  # = 5c

    def test_kernel(self):
        """L_0, L_1, L_{-1} are in the kernel (the sl_2 subalgebra)."""
        c = F(25)
        for m in range(-5, 6):
            # eta(L_0, L_m) = 0 for all m
            assert killing_form_virasoro(0, m, c) == F(0)
            # eta(L_1, L_m) = 0 for all m (since m*(m^2-1)=0 at m=1)
            assert killing_form_virasoro(1, m, c) == F(0) or m + 1 != 0
            # eta(L_{-1}, L_m) = 0 for all m
            if m + (-1) == 0:
                # eta(L_{-1}, L_1) = (c/12)(-1)(1-1) = 0
                assert killing_form_virasoro(-1, m, c) == F(0)

    def test_contragredient_invariance(self):
        """The cyclic pairing satisfies eta(L_m, L_n) = eta(L_{-n}, L_{-m}).

        The Shapovalov form is contragredient-invariant:
          <omega(a) v, w> = <v, a w>
        where omega is the Cartan anti-involution omega(L_m) = L_{-m}.
        At the bilinear form level: eta(L_m, L_n) = eta(L_{-n}, L_{-m}).
        """
        c = F(25)
        for m in range(-5, 6):
            for n in range(-5, 6):
                assert killing_form_virasoro(m, n, c) == \
                    killing_form_virasoro(-n, -m, c), \
                    f"Contragredient invariance failed: m={m}, n={n}"

    def test_mode_pairing_structure(self):
        """The pairing has the right structure: nondegenerate for |m| >= 2."""
        c = F(25)
        for m in range(2, 6):
            val = killing_form_virasoro(m, -m, c)
            assert val > 0, f"Pairing should be positive for m={m}, got {val}"
            assert val == c * F(m) * F(m * m - 1) / F(12)


class TestPropagator:
    """Test the propagator (inverse Gram matrix)."""

    def test_propagator_m2(self):
        """P(2) = 12/(c * 2 * 3) = 2/c."""
        c = F(25)
        assert propagator_virasoro(2, c) == F(12) / (c * F(2) * F(3))
        assert propagator_virasoro(2, c) == F(2) / c

    def test_propagator_m3(self):
        """P(3) = 12/(c * 3 * 8) = 1/(2c)."""
        c = F(25)
        assert propagator_virasoro(3, c) == F(12) / (c * F(3) * F(8))
        assert propagator_virasoro(3, c) == F(1) / (F(2) * c)

    def test_propagator_kernel(self):
        """P(0), P(1), P(-1) are undefined (in the kernel)."""
        c = F(25)
        assert propagator_virasoro(0, c) is None
        assert propagator_virasoro(1, c) is None
        assert propagator_virasoro(-1, c) is None

    def test_propagator_inverse(self):
        """P(m) * G(m) = 1 for |m| >= 2."""
        c = F(25)
        for m in range(-6, 7):
            if abs(m) >= 2:
                P = propagator_virasoro(m, c)
                G = killing_form_virasoro(m, -m, c)
                assert P * G == F(1), f"Failed for m={m}: P*G = {P*G}"


# ============================================================================
# 3. ell_3 computation: the cubic shadow
# ============================================================================

class TestEll3Virasoro:
    """Test ell_3 for the Virasoro algebra (class M)."""

    def test_ell3_equals_S3(self):
        """ell_3^{(0),tr} = S_3 = 2 for Virasoro."""
        c = F(25)
        assert ell3_virasoro_explicit(c) == F(2)

    def test_ell3_c_independent(self):
        """S_3 = 2 is independent of c (for c =/= 0)."""
        for c_val in [F(1), F(1, 2), F(25), F(26), F(100), F(1, 10)]:
            assert ell3_virasoro_explicit(c_val) == F(2), \
                f"S_3 =/= 2 at c = {c_val}"

    def test_ell3_three_channel(self):
        """Three-channel computation gives S_3 = 2."""
        c = F(25)
        assert ell3_virasoro_three_channel(c) == F(2)

    def test_ell3_deformation_complex(self):
        """Deformation complex computation gives S_3 = 2."""
        c = F(25)
        dc = VirasoroDefComplex(c, N=4)
        assert dc.ell3_cubic_shadow() == F(2)

    def test_ell3_mode_sum(self):
        """Mode sum gives S_3 = 2."""
        c = F(25)
        dc = VirasoroDefComplex(c, N=4)
        assert dc.ell3_mode_sum() == F(2)

    def test_ell3_propagator_sum(self):
        """Propagator sum gives S_3 = 2."""
        c = F(25)
        dc = VirasoroDefComplex(c, N=4)
        assert dc.ell3_propagator_sum() == F(2)

    def test_ell3_nonzero(self):
        """ell_3 =/= 0 for Virasoro: the algebra is NOT formal at arity 3."""
        c = F(25)
        s3 = ell3_virasoro_explicit(c)
        assert s3 != F(0), "ell_3 should be nonzero for Virasoro (class M)"

    def test_ell3_at_c26(self):
        """Special case c = 26 (bosonic string): S_3 = 2."""
        assert ell3_virasoro_explicit(F(26)) == F(2)

    def test_ell3_at_c_half(self):
        """c = 1/2 (Ising model): S_3 = 2."""
        assert ell3_virasoro_explicit(F(1, 2)) == F(2)

    def test_ell3_at_c13(self):
        """c = 13 (self-dual point): S_3 = 2."""
        assert ell3_virasoro_explicit(F(13)) == F(2)


class TestEll3Heisenberg:
    """Test ell_3 for the Heisenberg algebra (class G)."""

    def test_ell3_vanishes(self):
        """ell_3 = 0 for Heisenberg: the algebra IS formal."""
        for k in [F(1), F(1, 2), F(3), F(10)]:
            assert ell3_heisenberg(k) == F(0)

    def test_shadow_depth_2(self):
        """Shadow depth = 2 (all S_r = 0 for r >= 3)."""
        shadows = LInfBracketComputer.heisenberg_shadows(F(1))
        assert LInfBracketComputer.formality_level(shadows) == 2

    def test_full_formality(self):
        """Formal through all computed arities."""
        shadows = LInfBracketComputer.heisenberg_shadows(F(1))
        assert LInfBracketComputer.is_formal_through_arity(shadows, 6)


class TestEll3AffineSl2:
    """Test ell_3 for affine sl_2 (class L)."""

    def test_ell3_nonzero(self):
        """ell_3 =/= 0 for affine sl_2: non-formal at arity 3."""
        k = F(3)
        s3 = ell3_affine_sl2(k)
        assert s3 != F(0)
        assert s3 == F(4) / F(5)  # 4/(k+2) = 4/5

    def test_ell3_formula(self):
        """S_3 = 4/(k+2) for affine sl_2."""
        for k_val, expected in [
            (F(1), F(4, 3)),
            (F(2), F(1)),
            (F(3), F(4, 5)),
            (F(10), F(1, 3)),
        ]:
            assert ell3_affine_sl2(k_val) == expected

    def test_shadow_depth_3(self):
        """Shadow depth = 3 (S_3 =/= 0, S_4 = 0)."""
        shadows = LInfBracketComputer.affine_sl2_shadows(F(3))
        assert LInfBracketComputer.formality_level(shadows) == 3

    def test_formal_from_arity_4(self):
        """Formal from arity 4 onwards."""
        shadows = LInfBracketComputer.affine_sl2_shadows(F(3))
        assert not LInfBracketComputer.is_formal_through_arity(shadows, 3)
        assert LInfBracketComputer.is_formal_through_arity(
            {r: v for r, v in shadows.items() if r >= 4}, 6
        )

    def test_ell3_critical_level(self):
        """At critical level k = -h^v = -2: S_3 = 0 (degenerate)."""
        assert ell3_affine_sl2(F(-2)) == F(0)


# ============================================================================
# 4. Shadow tower cross-checks
# ============================================================================

class TestShadowTowerCrossCheck:
    """Cross-check shadow tower values against virasoro_shadow_all_arity.py."""

    def test_virasoro_S2_equals_kappa(self):
        """S_2 = kappa = c/2."""
        c = F(25)
        shadows = LInfBracketComputer.virasoro_shadows(c)
        assert shadows[2] == c / F(2)

    def test_virasoro_S3_equals_2(self):
        """S_3 = 2 (c-independent)."""
        shadows = LInfBracketComputer.virasoro_shadows(F(25))
        assert shadows[3] == F(2)

    def test_virasoro_S4_formula(self):
        """S_4 = 10/[c(5c+22)]."""
        c = F(25)
        shadows = LInfBracketComputer.virasoro_shadows(c)
        expected = F(10) / (c * (F(5) * c + F(22)))
        assert shadows[4] == expected

    def test_virasoro_S5_formula(self):
        """S_5 = -48/[c^2(5c+22)]."""
        c = F(25)
        shadows = LInfBracketComputer.virasoro_shadows(c)
        expected = F(-48) / (c * c * (F(5) * c + F(22)))
        assert shadows[5] == expected

    def test_virasoro_all_nonzero(self):
        """All S_r =/= 0 for r >= 2 (class M, infinite tower)."""
        shadows = LInfBracketComputer.virasoro_shadows(F(25), max_r=8)
        for r in range(2, 9):
            val = shadows.get(r)
            assert val is not None and val != F(0), \
                f"S_{r} should be nonzero for Virasoro"

    def test_heisenberg_all_zero_from_3(self):
        """S_r = 0 for r >= 3 (class G)."""
        shadows = LInfBracketComputer.heisenberg_shadows(F(1))
        for r in range(3, 7):
            assert shadows[r] == F(0)


# ============================================================================
# 5. Operadic complexity theorem verification
# ============================================================================

class TestOperadicComplexity:
    """Test the operadic complexity theorem r_max = d_inf = f_inf."""

    def test_heisenberg_class_G(self):
        """Heisenberg: r_max = 2, class G."""
        results = verify_operadic_complexity()
        h = results['heisenberg']
        assert h['S_3'] == F(0)
        assert h['formality_level'] == 2
        assert h['class'] == 'G'

    def test_affine_sl2_class_L(self):
        """Affine sl_2: r_max = 3, class L."""
        results = verify_operadic_complexity()
        a = results['affine_sl2']
        assert a['S_3'] != F(0)
        assert a['formality_level'] == 3
        assert a['class'] == 'L'

    def test_virasoro_class_M(self):
        """Virasoro: r_max = infinity, class M."""
        results = verify_operadic_complexity()
        v = results['virasoro']
        assert v['S_3'] == F(2)
        assert v['formality_level'] >= 8  # all S_r nonzero through 8
        assert v['class'] == 'M'

    def test_formality_hierarchy(self):
        """G is formal, L is non-formal at 3, M is non-formal at all arities."""
        results = verify_operadic_complexity()
        assert results['heisenberg']['formal_through_3'] is True
        assert results['affine_sl2']['formal_through_3'] is False
        assert results['virasoro']['formal_through_3'] is False

    def test_formality_level_ordering(self):
        """f_inf: Heisenberg (2) < Affine (3) < Virasoro (inf)."""
        results = verify_operadic_complexity()
        assert results['heisenberg']['formality_level'] < results['affine_sl2']['formality_level']
        assert results['affine_sl2']['formality_level'] < results['virasoro']['formality_level']


# ============================================================================
# 6. Shadow--formality identification (Proposition)
# ============================================================================

class TestShadowFormalityIdentification:
    """Test prop:shadow-formality-low-arity.

    (i) kappa = ell_2^{(0)}(Theta, Theta)
    (ii) C = -h(ell_3^{(0)}(Theta^{<=2}, Theta^{<=2}, Theta^{<=2}))
    (iii) Q = [ell_4^{(0),tr}(Theta^{<=3}, ...)]
    """

    def test_arity2_is_kappa(self):
        """S_2 = kappa: the binary bracket ell_2 is the curvature."""
        for c_val in [F(1), F(25), F(26)]:
            shadows = LInfBracketComputer.virasoro_shadows(c_val)
            assert shadows[2] == c_val / F(2)

    def test_arity3_is_cubic_shadow(self):
        """S_3 = ell_3^{(0),tr} evaluated on the MC element."""
        for c_val in [F(1), F(25), F(26)]:
            s3_from_shadows = LInfBracketComputer.virasoro_shadows(c_val)[3]
            s3_from_ell3 = ell3_virasoro_explicit(c_val)
            assert s3_from_shadows == s3_from_ell3 == F(2)

    def test_arity4_is_quartic_shadow(self):
        """S_4 = ell_4^{(0),tr}: the quartic formality obstruction."""
        c = F(25)
        shadows = LInfBracketComputer.virasoro_shadows(c)
        # S_4 = 10/(c(5c+22)) = 10/(25*147) = 10/3675 = 2/735
        expected = F(10) / (c * (F(5) * c + F(22)))
        assert shadows[4] == expected
        assert shadows[4] != F(0)  # Nonzero for Virasoro (class M)


# ============================================================================
# 7. Consistency with the convolution recursion
# ============================================================================

class TestConvolutionRecursion:
    """Verify ell_3 is consistent with the shadow metric recursion."""

    def test_a1_equals_6(self):
        """a_1 = q_1/(2*a_0) = 12c/(2c) = 6."""
        c = F(25)
        q_1 = F(12) * c
        a_0 = c
        a_1 = q_1 / (F(2) * a_0)
        assert a_1 == F(6)

    def test_S3_from_recursion(self):
        """S_3 = a_1/3 = 6/3 = 2."""
        a_1 = F(6)
        assert a_1 / F(3) == F(2)

    def test_shadow_metric_q1(self):
        """q_1 = 12c (coefficient of t in Q_L(t) for Virasoro)."""
        c = F(25)
        # Q_L(t) = (c + 6t)^2 + 80t^2/(5c+22)
        # = c^2 + 12ct + 36t^2 + 80t^2/(5c+22)
        # q_1 = 12c
        q_1 = F(12) * c
        assert q_1 == F(300)

    def test_consistency_all_c(self):
        """S_3 from the recursion matches S_3 from ell_3 for various c."""
        for c_val in [F(1), F(2), F(10), F(25), F(1, 3), F(100)]:
            # From recursion
            q_1 = F(12) * c_val
            a_0 = c_val
            a_1 = q_1 / (F(2) * a_0)
            s3_recursion = a_1 / F(3)

            # From ell_3 computation
            s3_ell3 = ell3_virasoro_explicit(c_val)

            assert s3_recursion == s3_ell3 == F(2), \
                f"Inconsistency at c = {c_val}"


# ============================================================================
# 8. Non-formality confirmation
# ============================================================================

class TestNonFormality:
    """Confirm non-formality of Virasoro L-infinity structure."""

    def test_virasoro_not_formal_at_arity3(self):
        """ell_3 =/= 0 confirms non-formality at arity 3."""
        for c_val in [F(1), F(25), F(26)]:
            assert ell3_virasoro_explicit(c_val) != F(0)

    def test_virasoro_not_formal_at_arity4(self):
        """S_4 =/= 0 confirms non-formality at arity 4."""
        c = F(25)
        shadows = LInfBracketComputer.virasoro_shadows(c)
        assert shadows[4] != F(0)

    def test_virasoro_not_formal_at_arity5(self):
        """S_5 =/= 0 confirms non-formality at arity 5."""
        c = F(25)
        shadows = LInfBracketComputer.virasoro_shadows(c)
        assert shadows[5] != F(0)

    def test_virasoro_infinite_tower(self):
        """All S_r =/= 0 through computed range confirms infinite tower."""
        c = F(25)
        shadows = LInfBracketComputer.virasoro_shadows(c, max_r=8)
        for r in range(2, 9):
            assert shadows.get(r) is not None and shadows[r] != F(0), \
                f"S_{r} should be nonzero for Virasoro (class M)"

    def test_heisenberg_IS_formal(self):
        """Heisenberg is L-infinity formal: ell_k = 0 for all k >= 3."""
        assert ell3_heisenberg(F(1)) == F(0)

    def test_affine_partial_formality(self):
        """Affine sl_2: ell_3 =/= 0 but formal from arity 4."""
        k = F(3)
        assert ell3_affine_sl2(k) != F(0)
        shadows = LInfBracketComputer.affine_sl2_shadows(k)
        for r in range(4, 7):
            assert shadows[r] == F(0)


# ============================================================================
# 9. Deformation complex constructor
# ============================================================================

class TestDefComplex:
    """Test the VirasoroDefComplex class."""

    def test_kappa(self):
        """kappa = c/2."""
        c = F(25)
        dc = VirasoroDefComplex(c)
        assert dc.kappa() == c / F(2)

    def test_eta_symmetry(self):
        """eta is symmetric."""
        c = F(25)
        dc = VirasoroDefComplex(c, N=4)
        for m in dc.modes:
            for n in dc.modes:
                assert dc.eta(m, n) == dc.eta(n, m)

    def test_eta_pairing(self):
        """eta(L_m, L_n) = 0 unless m+n=0."""
        c = F(25)
        dc = VirasoroDefComplex(c, N=4)
        for m in dc.modes:
            for n in dc.modes:
                if m + n != 0:
                    assert dc.eta(m, n) == F(0)

    def test_bracket_structure(self):
        """[L_m, L_n] has the right coefficients."""
        c = F(25)
        dc = VirasoroDefComplex(c, N=5)
        # [L_2, L_3] = -1 * L_5
        result = dc.bracket(2, 3)
        assert len(result) == 1
        assert result[0] == (5, F(-1))

        # [L_0, L_{-2}] = 2 L_{-2}
        result = dc.bracket(0, -2)
        assert result == [(-2, F(2))]

    def test_ell3_matches_explicit(self):
        """Deformation complex S_3 matches the explicit computation."""
        c = F(25)
        dc = VirasoroDefComplex(c, N=4)
        assert dc.ell3_cubic_shadow() == F(2)


# ============================================================================
# 10. The key theorem-level result
# ============================================================================

class TestMainResult:
    """The main theorem-level result of this computation.

    THEOREM (from prop:shadow-formality-low-arity + thm:operadic-complexity-detailed):

    For the Virasoro algebra at any central charge c =/= 0:
    (1) The genus-0 transferred L-infinity bracket ell_3^{(0),tr} is NONZERO.
    (2) ell_3^{(0),tr}(Theta^{<=2}, Theta^{<=2}, Theta^{<=2}) = S_3 = 2 (c-independent).
    (3) The L-infinity formality level f_infinity(Vir_c) = infinity.
    (4) The convolution algebra g_A^mod is NOT formal at genus 0.
    (5) This confirms class M (mixed) status: infinite shadow depth.
    (6) In contrast, Heisenberg (class G) has ell_3 = 0 (full formality).
    """

    def test_ell3_nonzero_for_virasoro(self):
        """THE KEY RESULT: ell_3 =/= 0 for Virasoro at any c =/= 0."""
        for c_val in [F(1, 2), F(1), F(25, 7), F(13), F(25), F(26), F(100)]:
            s3 = ell3_virasoro_explicit(c_val)
            assert s3 == F(2), f"S_3 should be 2 at c = {c_val}, got {s3}"
            assert s3 != F(0), "ell_3 must be nonzero for Virasoro"

    def test_ell3_is_c_independent(self):
        """S_3 = 2 regardless of c: the cubic shadow is universal."""
        values = set()
        for c_val in [F(1, 10), F(1), F(7), F(13), F(26), F(50)]:
            values.add(ell3_virasoro_explicit(c_val))
        assert values == {F(2)}

    def test_four_class_hierarchy(self):
        """The four archetype classes have distinct formality levels.

        G (Gaussian, r_max=2): ell_3 = 0
        L (Lie/tree, r_max=3): ell_3 =/= 0, ell_4 = 0
        M (mixed, r_max=inf): ell_k =/= 0 for all k >= 3
        """
        # Heisenberg (G)
        assert ell3_heisenberg(F(1)) == F(0)

        # Affine sl_2 (L)
        assert ell3_affine_sl2(F(3)) != F(0)
        assert LInfBracketComputer.affine_sl2_shadows(F(3))[4] == F(0)

        # Virasoro (M)
        assert ell3_virasoro_explicit(F(25)) == F(2)
        assert LInfBracketComputer.virasoro_shadows(F(25))[4] != F(0)
        assert LInfBracketComputer.virasoro_shadows(F(25))[5] != F(0)


# ============================================================================
# 11. Cross-validation with virasoro_shadow_all_arity.py
# ============================================================================

class TestCrossValidation:
    """Cross-validate against the existing shadow tower implementation."""

    def test_shadow_coefficients_match(self):
        """Shadow tower from linf engine matches virasoro_shadow_all_arity."""
        try:
            from compute.lib.virasoro_shadow_all_arity import shadow_coefficients
        except ImportError:
            pytest.skip("virasoro_shadow_all_arity not available")

        from sympy import Rational, Symbol, cancel
        c_sym = Symbol('c')

        vsa_shadows = shadow_coefficients(max_r=8)
        for c_val in [F(1), F(25), F(26)]:
            linf_shadows = LInfBracketComputer.virasoro_shadows(c_val, max_r=8)
            for r in range(2, 9):
                # Evaluate the sympy expression at c = c_val
                vsa_val = vsa_shadows[r].subs(c_sym, Rational(c_val.numerator, c_val.denominator))
                vsa_frac = F(int(vsa_val.p), int(vsa_val.q))
                assert linf_shadows[r] == vsa_frac, \
                    f"Mismatch at r={r}, c={c_val}: {linf_shadows[r]} vs {vsa_frac}"

    def test_alpha_vir_matches(self):
        """alpha_vir() = 2 matches our S_3 = 2."""
        try:
            from compute.lib.virasoro_shadow_all_arity import alpha_vir
        except ImportError:
            pytest.skip("virasoro_shadow_all_arity not available")

        from sympy import Rational
        assert int(alpha_vir()) == 2
        assert ell3_virasoro_explicit(F(25)) == F(2)
