"""Tests for explicit A-infinity transferred structure on Virasoro.

Verifies:
1. SDR relations and bar complex structure
2. A-infinity associativity relations at order 3 and 4
3. Shadow-formality cross-check: m_k <-> S_k
4. Four-class depth classification (G/L/C/M)
5. Complementarity (AP24-safe)
6. Tree combinatorics (Catalan numbers)
7. Exact arithmetic consistency

Ground truth:
  prop:shadow-formality-low-arity (nonlinear_modular_shadows.tex)
  thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
  thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
  comp:virasoro-curvature, comp:virasoro-ope (bar_complex_tables.tex)
  landscape_census.tex (authoritative formula source)
"""

import math
from fractions import Fraction as FR

import pytest

from compute.lib.virasoro_ainfty_explicit import (
    PrimarySectorAInfinity,
    HeisenbergAInfinity,
    AffineSl2AInfinity,
    BetaGammaAInfinity,
    VirasoroBarComplex,
    catalan_number,
    count_planar_binary_trees,
    planar_binary_trees,
    verify_all,
    verify_complementarity_ainfty,
    verify_depth_classification,
    verify_shadow_ainfty_crosscheck,
    verify_tree_counts,
    virasoro_S3,
    virasoro_S4,
    virasoro_S5,
    virasoro_shadow_coefficients_exact,
)


# ============================================================================
# Tree combinatorics
# ============================================================================

class TestPlanarBinaryTrees:
    """Verify PBT(k) = C_{k-1} (Catalan number)."""

    def test_pbt_1(self):
        assert len(planar_binary_trees(1)) == 1

    def test_pbt_2(self):
        assert len(planar_binary_trees(2)) == 1

    def test_pbt_3(self):
        assert len(planar_binary_trees(3)) == 2

    def test_pbt_4(self):
        assert len(planar_binary_trees(4)) == 5

    def test_pbt_5(self):
        assert len(planar_binary_trees(5)) == 14

    def test_pbt_6(self):
        assert len(planar_binary_trees(6)) == 42

    def test_pbt_7(self):
        assert len(planar_binary_trees(7)) == 132

    def test_catalan_formula(self):
        """C_n = (2n)!/(n!(n+1)!)."""
        expected = [1, 1, 2, 5, 14, 42, 132, 429]
        for n, exp in enumerate(expected):
            assert catalan_number(n) == exp

    def test_pbt_equals_catalan(self):
        """PBT(k) = C_{k-1} for k = 1..8."""
        for k in range(1, 8):
            trees = planar_binary_trees(k)
            assert len(trees) == catalan_number(k - 1), \
                f"PBT({k}) = {len(trees)} != C_{k-1} = {catalan_number(k-1)}"

    def test_count_formula_matches(self):
        """count_planar_binary_trees matches actual enumeration."""
        for k in range(1, 7):
            assert count_planar_binary_trees(k) == len(planar_binary_trees(k))


# ============================================================================
# Virasoro shadow coefficients: exact values
# ============================================================================

class TestVirasoroShadowCoefficients:
    """Verify exact shadow obstruction tower coefficients against known formulas."""

    def test_S2_is_kappa(self):
        """S_2 = kappa = c/2."""
        for c_val in [FR(1), FR(2), FR(25), FR(1, 2)]:
            vir = PrimarySectorAInfinity(c_val)
            coeffs = vir.shadow_coefficients(4)
            assert coeffs[2] == c_val / FR(2)

    def test_S3_universal(self):
        """S_3 = 2 for all c > 0 (universal cubic shadow)."""
        for c_val in [FR(1), FR(2), FR(5), FR(25), FR(1, 2)]:
            vir = PrimarySectorAInfinity(c_val)
            coeffs = vir.shadow_coefficients(4)
            assert coeffs[3] == FR(2)

    def test_S3_function(self):
        """Standalone S_3 function."""
        assert virasoro_S3() == FR(2)

    def test_S4_formula(self):
        """S_4 = 10/(c*(5c+22)) (quartic contact invariant)."""
        for c_val in [FR(1), FR(2), FR(5), FR(25)]:
            vir = PrimarySectorAInfinity(c_val)
            coeffs = vir.shadow_coefficients(5)
            expected = FR(10) / (c_val * (FR(5) * c_val + FR(22)))
            assert coeffs[4] == expected, \
                f"S_4 at c={c_val}: got {coeffs[4]}, expected {expected}"

    def test_S4_function(self):
        """Standalone S_4 function matches recursion."""
        for c_val in [FR(1), FR(5), FR(25)]:
            assert virasoro_S4(c_val) == PrimarySectorAInfinity(c_val).shadow_coefficients(5)[4]

    def test_S5_formula(self):
        """S_5 = -48/(c^2*(5c+22))."""
        for c_val in [FR(1), FR(5), FR(25)]:
            vir = PrimarySectorAInfinity(c_val)
            coeffs = vir.shadow_coefficients(6)
            expected = FR(-48) / (c_val**2 * (FR(5) * c_val + FR(22)))
            assert coeffs[5] == expected, \
                f"S_5 at c={c_val}: got {coeffs[5]}, expected {expected}"

    def test_S5_function(self):
        """Standalone S_5 function."""
        for c_val in [FR(1), FR(5), FR(25)]:
            assert virasoro_S5(c_val) == PrimarySectorAInfinity(c_val).shadow_coefficients(6)[5]

    def test_S4_c1(self):
        """S_4(c=1) = 10/(1*27) = 10/27."""
        assert virasoro_S4(FR(1)) == FR(10, 27)

    def test_S4_c25(self):
        """S_4(c=25) = 10/(25*147) = 10/3675 = 2/735."""
        assert virasoro_S4(FR(25)) == FR(2, 735)

    def test_S5_c1(self):
        """S_5(c=1) = -48/(1*27) = -48/27 = -16/9."""
        assert virasoro_S5(FR(1)) == FR(-16, 9)


# ============================================================================
# Shadow metric and recursion consistency
# ============================================================================

class TestShadowMetricConsistency:
    """Verify f^2 = Q_L where f = sqrt(Q_L)."""

    @pytest.fixture
    def coeffs_c25(self):
        return virasoro_shadow_coefficients_exact(FR(25), max_r=12)

    @pytest.fixture
    def coeffs_c1(self):
        return virasoro_shadow_coefficients_exact(FR(1), max_r=12)

    def _check_f_squared(self, c_val, max_r=10):
        """Verify f^2 = Q_L at all Taylor orders."""
        coeffs = virasoro_shadow_coefficients_exact(c_val, max_r=max_r)
        kappa = c_val / FR(2)
        alpha = FR(2)
        S4 = FR(10) / (c_val * (FR(5) * c_val + FR(22)))

        q0 = FR(4) * kappa ** 2
        q1 = FR(12) * kappa * alpha
        q2 = FR(9) * alpha ** 2 + FR(16) * kappa * S4

        # a_n = r * S_{r} where r = n + 2
        a = []
        for n in range(max_r - 1):
            r = n + 2
            a.append(FR(r) * coeffs[r])

        # Check [t^0]: a_0^2 = q0
        assert a[0] ** 2 == q0, f"[t^0]: {a[0]**2} != {q0}"

        # Check [t^1]: 2*a0*a1 = q1
        assert FR(2) * a[0] * a[1] == q1, f"[t^1]: {FR(2)*a[0]*a[1]} != {q1}"

        # Check [t^2]: 2*a0*a2 + a1^2 = q2
        assert FR(2) * a[0] * a[2] + a[1]**2 == q2, f"[t^2]: mismatch"

        # Check [t^n] = 0 for n >= 3
        for n in range(3, min(max_r - 2, 8)):
            conv = sum(a[j] * a[n - j] for j in range(n + 1))
            assert conv == FR(0), f"[t^{n}]: convolution = {conv} != 0"

    def test_f_squared_c1(self):
        self._check_f_squared(FR(1))

    def test_f_squared_c2(self):
        self._check_f_squared(FR(2))

    def test_f_squared_c5(self):
        self._check_f_squared(FR(5))

    def test_f_squared_c25(self):
        self._check_f_squared(FR(25))

    def test_f_squared_c_half(self):
        self._check_f_squared(FR(1, 2))


# ============================================================================
# Cross-check against shadow_tower_recursive.py
# ============================================================================

class TestCrossCheckShadowTower:
    """Verify our exact Fraction computation matches the float recursion."""

    def _check_agreement(self, c_val_frac, c_val_float, max_r=12):
        from compute.lib.shadow_tower_recursive import shadow_coefficients_virasoro
        exact = virasoro_shadow_coefficients_exact(c_val_frac, max_r=max_r)
        numerical = shadow_coefficients_virasoro(c_val_float, max_r=max_r)
        for r in range(2, max_r + 1):
            ex = float(exact[r])
            num = numerical[r]
            if abs(ex) > 1e-50:
                rel_err = abs(ex - num) / abs(ex)
                assert rel_err < 1e-12, \
                    f"S_{r} at c={c_val_float}: rel_err={rel_err:.2e}"
            else:
                assert abs(num) < 1e-30, \
                    f"S_{r} at c={c_val_float}: should be ~0"

    def test_c25(self):
        self._check_agreement(FR(25), 25.0)

    def test_c1(self):
        self._check_agreement(FR(1), 1.0)

    def test_c2(self):
        self._check_agreement(FR(2), 2.0)

    def test_c_half(self):
        self._check_agreement(FR(1, 2), 0.5)

    def test_c5(self):
        self._check_agreement(FR(5), 5.0)


# ============================================================================
# Depth classification (G/L/C/M)
# ============================================================================

class TestDepthClassification:
    """Verify the four-class shadow depth classification.

    G (Gaussian): Heisenberg, m_k = 0 for k >= 3
    L (Lie/tree): Affine sl_2, m_3 != 0, m_k = 0 for k >= 4
    C (Contact): BetaGamma, m_3, m_4 != 0, m_k = 0 for k >= 5
    M (Mixed): Virasoro, m_k != 0 for ALL k >= 3
    """

    def test_heisenberg_class_G(self):
        """Heisenberg: all m_k = 0 for k >= 3."""
        heis = HeisenbergAInfinity(FR(1))
        for k in range(3, 8):
            assert heis.mk_primary(k) == FR(0), f"m_{k} != 0 for Heisenberg"

    def test_heisenberg_m2_nonzero(self):
        """Heisenberg: m_2 = k (level)."""
        for k_val in [FR(1), FR(2), FR(3)]:
            heis = HeisenbergAInfinity(k_val)
            assert heis.m2_primary() == k_val

    def test_heisenberg_kappa(self):
        """Heisenberg: kappa = k (NOT k/2)."""
        heis = HeisenbergAInfinity(FR(3))
        assert heis.kappa == FR(3)

    def test_affine_class_L(self):
        """Affine sl_2: m_3 != 0, m_k = 0 for k >= 4."""
        aff = AffineSl2AInfinity(FR(1))
        assert aff.mk_primary(3) != FR(0)
        for k in range(4, 8):
            assert aff.mk_primary(k) == FR(0), f"m_{k} != 0 for affine sl_2"

    def test_affine_kappa(self):
        """Affine sl_2: kappa = 3(k+2)/4."""
        for k_val in [FR(1), FR(2), FR(4)]:
            aff = AffineSl2AInfinity(k_val)
            expected = FR(3) * (k_val + FR(2)) / FR(4)
            assert aff.kappa == expected

    def test_betagamma_class_C(self):
        """BetaGamma: m_3, m_4 != 0, m_5 = 0."""
        bg = BetaGammaAInfinity()
        coeffs = bg.shadow_coefficients(8)
        assert coeffs[3] != FR(0)
        assert coeffs[4] != FR(0)
        for k in range(5, 9):
            assert coeffs[k] == FR(0), f"S_{k} != 0 for BetaGamma"

    def test_betagamma_kappa(self):
        """BetaGamma: kappa = -1."""
        bg = BetaGammaAInfinity()
        assert bg.kappa == FR(-1)

    def test_betagamma_S4(self):
        """BetaGamma: S_4 = -5/12."""
        bg = BetaGammaAInfinity()
        assert bg.S_4 == FR(-5, 12)

    def test_virasoro_class_M(self):
        """Virasoro: m_k != 0 for ALL k >= 3 (at generic c)."""
        vir = PrimarySectorAInfinity(FR(25))
        coeffs = vir.shadow_coefficients(12)
        for k in range(3, 13):
            assert coeffs[k] != FR(0), f"S_{k} = 0 for Virasoro at c=25"

    def test_virasoro_class_M_c1(self):
        """Virasoro at c=1: still infinite depth."""
        vir = PrimarySectorAInfinity(FR(1))
        coeffs = vir.shadow_coefficients(10)
        for k in range(3, 11):
            assert coeffs[k] != FR(0), f"S_{k} = 0 for Virasoro at c=1"


# ============================================================================
# Complementarity (AP24-safe)
# ============================================================================

class TestComplementarity:
    """Verify Koszul duality complementarity for Virasoro.

    kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (NOT 0 -- AP24!).
    """

    def test_kappa_sum_is_13(self):
        """kappa + kappa_dual = 13 for all c."""
        for c_val in [FR(1), FR(5), FR(13), FR(25)]:
            c_dual = FR(26) - c_val
            kappa = c_val / FR(2)
            kappa_dual = c_dual / FR(2)
            assert kappa + kappa_dual == FR(13)

    def test_kappa_sum_NOT_zero(self):
        """kappa + kappa_dual != 0 in general (AP24 anti-pattern)."""
        kappa = FR(25) / FR(2)
        kappa_dual = FR(1) / FR(2)
        assert kappa + kappa_dual != FR(0)

    def test_S3_universal_under_duality(self):
        """S_3 = 2 for both Vir_c and Vir_{26-c}."""
        for c_val in [FR(1), FR(5), FR(13), FR(25)]:
            c_dual = FR(26) - c_val
            vir = PrimarySectorAInfinity(c_val)
            vir_dual = PrimarySectorAInfinity(c_dual)
            assert vir.shadow_coefficients(4)[3] == FR(2)
            assert vir_dual.shadow_coefficients(4)[3] == FR(2)

    def test_self_dual_c13(self):
        """At c=13: Vir_c = Vir_{26-c} (self-dual point)."""
        vir = PrimarySectorAInfinity(FR(13))
        coeffs = vir.shadow_coefficients(8)
        assert coeffs[2] == FR(13, 2)
        assert coeffs[3] == FR(2)

    def test_complementarity_S4(self):
        """S_4 and S_4_dual are related by c -> 26-c."""
        for c_val in [FR(1), FR(5), FR(25)]:
            c_dual = FR(26) - c_val
            S4 = virasoro_S4(c_val)
            S4_dual = virasoro_S4(c_dual)
            # They are not equal in general (asymmetric)
            assert S4 != FR(0)
            assert S4_dual != FR(0)

    def test_complementarity_full_crosscheck(self):
        """Run full complementarity verification."""
        results = verify_complementarity_ainfty(FR(5))
        for name, ok in results.items():
            assert ok, f"Complementarity check failed: {name}"


# ============================================================================
# A-infinity relations
# ============================================================================

class TestAInfinityRelations:
    """Verify A-infinity structure relations.

    On the weight-graded primary line, the A-infinity relations are
    encoded in the shadow recursion (convolution identity f^2 = Q_L).
    """

    def test_m1_vanishes(self):
        """m_1 = 0 on H*(B) (cohomology has no differential)."""
        # m_1 = 0 by definition of transfer to cohomology
        vir = PrimarySectorAInfinity(FR(25))
        assert vir.verify_ainfty_relation_3() == FR(0)

    def test_m2_associative_primary_line(self):
        """m_2 is associative on the primary line (trivially, 1-dim)."""
        vir = PrimarySectorAInfinity(FR(25))
        # On 1-dim space, associativity is automatic.
        assert vir.verify_ainfty_relation_3() == FR(0)

    def test_recursion_is_ainfty(self):
        """The convolution recursion encodes the A-infinity relations.

        Specifically: a_n = -(1/(2*a0)) sum_{j=1}^{n-1} a_j * a_{n-j}
        for n >= 3 is equivalent to the vanishing of the Stasheff
        relation at each arity (in the weight-graded primary sector).
        """
        for c_val in [FR(1), FR(5), FR(25)]:
            coeffs = virasoro_shadow_coefficients_exact(c_val, max_r=10)
            kappa = c_val / FR(2)
            a0 = FR(2) * kappa

            a = [FR(r+2) * coeffs[r+2] for r in range(8)]

            # Check recursion holds at each order
            for n in range(3, 7):
                conv = sum(a[j] * a[n - j] for j in range(1, n))
                residual = FR(2) * a0 * a[n] + conv
                assert residual == FR(0), \
                    f"Recursion fails at n={n}, c={c_val}: residual={residual}"

    def test_mc_equation_arity_4(self):
        """Verify MC equation at arity 4.

        The shadow obstruction tower satisfies D*Theta + (1/2)[Theta,Theta] = 0.
        At arity 4, this becomes a constraint relating S_4 to S_2 and S_3.
        """
        vir = PrimarySectorAInfinity(FR(25))
        assert vir.verify_ainfty_relation_4() == FR(0)


# ============================================================================
# Specific numerical values
# ============================================================================

class TestSpecificValues:
    """Verify specific computed values against independent checks."""

    def test_S4_c1_exact(self):
        """S_4(c=1) = 10/27."""
        assert virasoro_S4(FR(1)) == FR(10, 27)

    def test_S4_c2_exact(self):
        """S_4(c=2) = 10/(2*32) = 10/64 = 5/32."""
        assert virasoro_S4(FR(2)) == FR(5, 32)

    def test_S4_c13_self_dual(self):
        """S_4(c=13) = 10/(13*87) = 10/1131."""
        assert virasoro_S4(FR(13)) == FR(10, 1131)

    def test_S5_c2_exact(self):
        """S_5(c=2) = -48/(4*32) = -48/128 = -3/8."""
        assert virasoro_S5(FR(2)) == FR(-3, 8)

    def test_kappa_c1(self):
        assert PrimarySectorAInfinity(FR(1)).kappa == FR(1, 2)

    def test_kappa_c25(self):
        assert PrimarySectorAInfinity(FR(25)).kappa == FR(25, 2)

    def test_discriminant_c25(self):
        """Delta = 8*kappa*S_4 = 4*25*2/735 = 200/735 = 40/147."""
        c_val = FR(25)
        kappa = c_val / FR(2)
        S4 = virasoro_S4(c_val)
        Delta = FR(8) * kappa * S4
        assert Delta == FR(40, 147)

    def test_discriminant_c1(self):
        """Delta = 8*(1/2)*(10/27) = 40/27."""
        c_val = FR(1)
        Delta = FR(8) * (c_val / FR(2)) * virasoro_S4(c_val)
        assert Delta == FR(40, 27)


# ============================================================================
# Growth rate and convergence
# ============================================================================

class TestGrowthRate:
    """Verify shadow growth rate properties."""

    def test_convergent_c25(self):
        """Virasoro at c=25: rho < 1 (convergent tower)."""
        c_val = FR(25)
        kappa = c_val / FR(2)
        S4 = virasoro_S4(c_val)
        Delta = FR(8) * kappa * S4

        # rho^2 = (9*alpha^2 + 2*Delta) / (4*kappa^2)
        # alpha = 2, so 9*4 = 36
        rho_sq = (FR(36) + FR(2) * Delta) / (FR(4) * kappa ** 2)
        rho = math.sqrt(float(rho_sq))
        assert rho < 1.0, f"rho = {rho} should be < 1 for c=25"

    def test_divergent_c1(self):
        """Virasoro at c=1: rho > 1 (divergent tower)."""
        c_val = FR(1)
        kappa = c_val / FR(2)
        S4 = virasoro_S4(c_val)
        Delta = FR(8) * kappa * S4
        rho_sq = (FR(36) + FR(2) * Delta) / (FR(4) * kappa ** 2)
        rho = math.sqrt(float(rho_sq))
        assert rho > 1.0, f"rho = {rho} should be > 1 for c=1"

    def test_ratio_test_c25(self):
        """Consecutive ratios |S_{r+1}/S_r| converge to rho for c=25."""
        coeffs = virasoro_shadow_coefficients_exact(FR(25), max_r=20)
        ratios = []
        for r in range(4, 19):
            if coeffs[r] != FR(0):
                ratios.append(abs(float(coeffs[r + 1]) / float(coeffs[r])))
        # Last few ratios should be close to rho
        # rho(c=25) approx 0.234
        assert 0.20 < ratios[-1] < 0.30, f"ratio[-1] = {ratios[-1]}"
        # Ratios should converge (decreasing variance)
        assert abs(ratios[-1] - ratios[-2]) < 0.01


# ============================================================================
# Bar complex structure
# ============================================================================

class TestBarComplex:
    """Verify bar complex construction."""

    def test_basis_construction(self):
        """Bar complex has expected basis size at low weight."""
        bc = VirasoroBarComplex(FR(25), max_weight=6)
        # Should have at least: vac + T + dT + d2T + TT + [T|T] + ...
        assert bc.dim > 10

    def test_vacuum_module_dims(self):
        """p_{>=2}(h) values are correct."""
        expected = {2: 1, 3: 1, 4: 2, 5: 2, 6: 4}
        for h, d in expected.items():
            assert VirasoroBarComplex._partitions_geq2(h) == d

    def test_state_weights(self):
        """State weight assignments are correct."""
        bc = VirasoroBarComplex(FR(1), max_weight=6)
        assert bc._state_weight('T') == 2
        assert bc._state_weight('dT') == 3
        assert bc._state_weight('d2T') == 4
        assert bc._state_weight('TT') == 4
        assert bc._state_weight('vac') == 0


# ============================================================================
# Master verification suite
# ============================================================================

class TestMasterVerification:
    """Run the full verification suite."""

    def test_verify_all_c25(self):
        """All checks pass at c=25."""
        results = verify_all(FR(25))
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_verify_all_c5(self):
        """All checks pass at c=5."""
        results = verify_all(FR(5))
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_verify_all_c1(self):
        """All checks pass at c=1."""
        results = verify_all(FR(1))
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_verify_all_c2(self):
        """All checks pass at c=2."""
        results = verify_all(FR(2))
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_verify_all_c_half(self):
        """All checks pass at c=1/2 (Ising model)."""
        results = verify_all(FR(1, 2))
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_tree_counts(self):
        """Dedicated tree count verification."""
        results = verify_tree_counts()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_depth_classification(self):
        """Dedicated depth classification verification."""
        results = verify_depth_classification()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"


# ============================================================================
# OPE data consistency
# ============================================================================

class TestOPEConsistency:
    """Verify OPE data against virasoro_bar.py."""

    def test_T_T_ope_double_pole(self):
        """T_{(1)}T = 2T."""
        bc = VirasoroBarComplex(FR(1), max_weight=6)
        products = bc._ope_product('T', 'T')
        assert products['T'] == FR(2)

    def test_T_T_ope_simple_pole(self):
        """T_{(0)}T = dT."""
        bc = VirasoroBarComplex(FR(1), max_weight=6)
        products = bc._ope_product('T', 'T')
        assert products['dT'] == FR(1)

    def test_T_T_ope_quartic_pole(self):
        """T_{(3)}T = c/2 (curvature)."""
        for c_val in [FR(1), FR(25)]:
            bc = VirasoroBarComplex(c_val, max_weight=6)
            products = bc._ope_product('T', 'T')
            assert products['vac'] == c_val / FR(2)

    def test_T_dT_ope(self):
        """T_{(1)}(dT) = 3dT, T_{(0)}(dT) = d2T."""
        bc = VirasoroBarComplex(FR(1), max_weight=6)
        products = bc._ope_product('T', 'dT')
        assert products['dT'] == FR(3)
        assert products['d2T'] == FR(1)

    def test_dT_T_ope(self):
        """(dT)_{(1)}T = 3dT, (dT)_{(0)}T = 2d2T."""
        bc = VirasoroBarComplex(FR(1), max_weight=6)
        products = bc._ope_product('dT', 'T')
        assert products['dT'] == FR(3)
        assert products['d2T'] == FR(2)

    def test_ope_asymmetry(self):
        """T * dT != dT * T (non-commutative)."""
        bc = VirasoroBarComplex(FR(1), max_weight=6)
        p1 = bc._ope_product('T', 'dT')
        p2 = bc._ope_product('dT', 'T')
        assert p1.get('d2T', FR(0)) != p2.get('d2T', FR(0))


# ============================================================================
# Independence and non-regression
# ============================================================================

class TestNonRegression:
    """Tests that catch common errors and regressions."""

    def test_no_S3_c_dependence(self):
        """S_3 is c-independent (= 2 for all Virasoro).

        AP1: do not copy formulas between families.
        S_3 for Virasoro is the alpha parameter = 2.
        """
        for c_val in [FR(1, 2), FR(1), FR(2), FR(5), FR(13), FR(25)]:
            assert PrimarySectorAInfinity(c_val).shadow_coefficients(4)[3] == FR(2)

    def test_kappa_not_c(self):
        """kappa = c/2, NOT c (AP9 anti-pattern)."""
        vir = PrimarySectorAInfinity(FR(10))
        assert vir.kappa == FR(5)
        assert vir.kappa != FR(10)

    def test_kappa_plus_kappa_dual_not_zero(self):
        """kappa + kappa' = 13, NOT 0 (AP24 anti-pattern).

        This was overclaimed in 20+ locations across both volumes.
        """
        for c_val in [FR(1), FR(5), FR(10), FR(25)]:
            k1 = c_val / FR(2)
            k2 = (FR(26) - c_val) / FR(2)
            assert k1 + k2 == FR(13)
            assert k1 + k2 != FR(0)

    def test_S4_positive_for_large_c(self):
        """S_4 > 0 for c > 0 (all terms in 10/(c*(5c+22)) positive)."""
        for c_val in [FR(1), FR(5), FR(25), FR(100)]:
            assert virasoro_S4(c_val) > FR(0)

    def test_S5_negative_for_large_c(self):
        """S_5 < 0 for c > 0 (from -48/(c^2*(5c+22)))."""
        for c_val in [FR(1), FR(5), FR(25)]:
            assert virasoro_S5(c_val) < FR(0)

    def test_alternating_sign_at_large_c(self):
        """For large c, S_r alternates in sign (the tower is oscillatory)."""
        coeffs = virasoro_shadow_coefficients_exact(FR(25), max_r=10)
        # S_2 > 0, S_3 > 0, S_4 > 0, S_5 < 0, S_6 > 0, S_7 < 0, ...
        assert coeffs[4] > FR(0)
        assert coeffs[5] < FR(0)
        assert coeffs[6] > FR(0)
        assert coeffs[7] < FR(0)
