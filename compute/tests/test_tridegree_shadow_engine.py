"""Tests for the tridegree shadow engine.

Verifies the decomposition Theta_A = Sum_{g,n,d} Theta_A^{(g,n,d)}
for all standard families: Heisenberg, affine sl_2, beta-gamma,
Virasoro, W_3, and three lattice VOAs.

Ground truth:
    - shadow_tower_atlas.py: tree-level shadows
    - virasoro_shadow_tower.py: Virasoro master equation
    - modular_shadow_tower.py: genus loop, delta_H^{(1)}
    - higher_genus_modular_koszul.tex: tridegree filtration
    - nonlinear_modular_shadows.tex: shadow depth classification
"""

import pytest
from sympy import Symbol, Rational, simplify, factor

from compute.lib.tridegree_shadow_engine import (
    cubic_shadow,
    depth_spectrum,
    genus0_tree_shadows,
    genus1_shadows,
    genus2_shadows,
    genus_free_energy,
    kappa,
    mc_equation_check,
    planted_forest_corrections,
    propagator,
    quartic_contact,
    shadow_class,
    shadow_depth_value,
    terminates,
    tridegree_shadow,
    tridegree_table,
)

c = Symbol('c')
k = Symbol('k')


# =========================================================================
# 1. HEISENBERG: class G, depth 2, only (g, 2, 0) nonzero
# =========================================================================

class TestHeisenbergTridegree:
    """Heisenberg H_k: Gaussian class, shadow depth 2."""

    def test_kappa(self):
        assert kappa('heisenberg') == k

    def test_kappa_numeric(self):
        assert kappa('heisenberg', level=Rational(1)) == 1

    def test_class_G(self):
        assert shadow_class('heisenberg') == 'G'

    def test_depth_2(self):
        assert shadow_depth_value('heisenberg') == 2

    def test_terminates(self):
        assert terminates('heisenberg') is True

    def test_tree_level_only_sh2(self):
        """Only Sh_2 = kappa is nonzero at tree level."""
        tree = genus0_tree_shadows('heisenberg', max_n=8)
        assert tree[2] == k
        for n in range(3, 9):
            assert tree[n] == 0, f"Sh_{n} should be 0 for Heisenberg"

    def test_cubic_zero(self):
        assert cubic_shadow('heisenberg') == 0

    def test_quartic_zero(self):
        assert quartic_contact('heisenberg') == 0

    def test_genus1_free_energy(self):
        """F_1 = kappa/24 = k/24."""
        g1 = genus1_shadows('heisenberg')
        assert (1, 0, 0) in g1
        assert simplify(g1[(1, 0, 0)] - k / 24) == 0

    def test_genus1_no_hessian_correction(self):
        """delta_H^{(1)} = 0 since Q = 0."""
        g1 = genus1_shadows('heisenberg')
        assert (1, 2, 0) not in g1

    def test_genus2_free_energy(self):
        """F_2 = kappa * 7/5760 = k * 7/5760."""
        g2 = genus2_shadows('heisenberg')
        assert (2, 0, 0) in g2
        assert simplify(g2[(2, 0, 0)] - k * Rational(7, 5760)) == 0

    def test_no_planted_forest(self):
        """No d >= 1 corrections for Gaussian class."""
        pf = planted_forest_corrections('heisenberg')
        assert len(pf) == 0

    def test_depth_spectrum_all_d0(self):
        """All nonzero entries at depth 0."""
        spec = depth_spectrum('heisenberg')
        assert 0 in spec
        assert all(d == 0 for d in spec.keys())

    def test_full_tridegree_count(self):
        """Heisenberg has exactly: (0,2,0), (1,0,0), (2,0,0) = 3 entries."""
        full = tridegree_shadow('heisenberg')
        assert len(full) == 3

    def test_mc_check_tree_seed(self):
        """MC check at (0, 2, 0): seed, passes trivially."""
        result = mc_equation_check('heisenberg', 0, 2, 0)
        assert result['passes'] is True

    def test_mc_check_tree_cubic(self):
        """MC check at (0, 3, 0): cubic = 0, passes."""
        result = mc_equation_check('heisenberg', 0, 3, 0)
        assert result['passes'] is True


# =========================================================================
# 2. LATTICE VOAs: class G, depth 2, same structure as Heisenberg
# =========================================================================

class TestLatticeTridegree:
    """Lattice VOAs V_Z, V_{Z^2}, V_{A_2}: Gaussian class, depth 2."""

    @pytest.mark.parametrize("family,expected_kappa", [
        ('lattice_Z', 1),
        ('lattice_Z2', 2),
        ('lattice_A2', 2),
    ])
    def test_kappa_equals_rank(self, family, expected_kappa):
        assert kappa(family) == expected_kappa

    @pytest.mark.parametrize("family", ['lattice_Z', 'lattice_Z2', 'lattice_A2'])
    def test_class_G(self, family):
        assert shadow_class(family) == 'G'

    @pytest.mark.parametrize("family", ['lattice_Z', 'lattice_Z2', 'lattice_A2'])
    def test_depth_2(self, family):
        assert shadow_depth_value(family) == 2

    @pytest.mark.parametrize("family", ['lattice_Z', 'lattice_Z2', 'lattice_A2'])
    def test_tree_only_sh2(self, family):
        tree = genus0_tree_shadows(family, max_n=8)
        assert tree[2] == kappa(family)
        for n in range(3, 9):
            assert tree[n] == 0

    @pytest.mark.parametrize("family,rank", [
        ('lattice_Z', 1),
        ('lattice_Z2', 2),
        ('lattice_A2', 2),
    ])
    def test_genus1_free_energy(self, family, rank):
        g1 = genus1_shadows(family)
        assert (1, 0, 0) in g1
        assert simplify(g1[(1, 0, 0)] - Rational(rank, 24)) == 0

    @pytest.mark.parametrize("family,rank", [
        ('lattice_Z', 1),
        ('lattice_Z2', 2),
        ('lattice_A2', 2),
    ])
    def test_genus2_free_energy(self, family, rank):
        g2 = genus2_shadows(family)
        assert (2, 0, 0) in g2
        assert simplify(g2[(2, 0, 0)] - rank * Rational(7, 5760)) == 0

    @pytest.mark.parametrize("family", ['lattice_Z', 'lattice_Z2', 'lattice_A2'])
    def test_no_planted_forest(self, family):
        pf = planted_forest_corrections(family)
        assert len(pf) == 0

    @pytest.mark.parametrize("family", ['lattice_Z', 'lattice_Z2', 'lattice_A2'])
    def test_depth_spectrum_all_d0(self, family):
        spec = depth_spectrum(family)
        assert all(d == 0 for d in spec.keys())


# =========================================================================
# 3. AFFINE sl_2: class L, depth 3
# =========================================================================

class TestAffineSl2Tridegree:
    """Affine V_k(sl_2): Lie class, shadow depth 3."""

    def test_kappa(self):
        expected = Rational(3) * (k + 2) / 4
        assert simplify(kappa('affine_sl2') - expected) == 0

    def test_class_L(self):
        assert shadow_class('affine_sl2') == 'L'

    def test_depth_3(self):
        assert shadow_depth_value('affine_sl2') == 3

    def test_terminates(self):
        assert terminates('affine_sl2') is True

    def test_tree_sh2_nonzero(self):
        tree = genus0_tree_shadows('affine_sl2')
        assert simplify(tree[2] - Rational(3) * (k + 2) / 4) == 0

    def test_tree_sh3_nonzero(self):
        """Cubic shadow = 1 (normalized Killing 3-cocycle)."""
        tree = genus0_tree_shadows('affine_sl2')
        assert tree[3] == 1

    def test_tree_sh4_zero(self):
        """Quartic = 0 by Jacobi identity."""
        tree = genus0_tree_shadows('affine_sl2')
        assert tree[4] == 0

    def test_tree_sh5_through_sh8_zero(self):
        tree = genus0_tree_shadows('affine_sl2', max_n=8)
        for n in range(4, 9):
            assert tree[n] == 0, f"Sh_{n} should be 0 for affine sl_2"

    def test_genus1_free_energy(self):
        g1 = genus1_shadows('affine_sl2')
        expected = Rational(3) * (k + 2) / 4 / 24
        assert (1, 0, 0) in g1
        assert simplify(g1[(1, 0, 0)] - expected) == 0

    def test_genus1_one_point(self):
        """(1, 1, 0) from Lambda_P(Sh_3): should be nonzero."""
        g1 = genus1_shadows('affine_sl2')
        assert (1, 1, 0) in g1
        # Lambda_P(1 * x^3) = C(3,2) * P * 1 = 3 * (4/(3(k+2))) * 1
        P = propagator('affine_sl2')
        expected = 3 * P * 1  # binomial(3,2) = 3
        assert simplify(g1[(1, 1, 0)] - expected) == 0

    def test_genus1_no_hessian_correction(self):
        """delta_H^{(1)} = Lambda_P(Q) = 0 since Q = 0."""
        g1 = genus1_shadows('affine_sl2')
        assert (1, 2, 0) not in g1

    def test_genus2_free_energy(self):
        g2 = genus2_shadows('affine_sl2')
        expected = Rational(3) * (k + 2) / 4 * Rational(7, 5760)
        assert (2, 0, 0) in g2
        assert simplify(g2[(2, 0, 0)] - expected) == 0

    def test_no_planted_forest(self):
        pf = planted_forest_corrections('affine_sl2')
        assert len(pf) == 0

    def test_mc_check_tree_quartic(self):
        """MC check at (0, 4, 0): quartic = 0, consistent."""
        result = mc_equation_check('affine_sl2', 0, 4, 0)
        assert result['passes'] is True


# =========================================================================
# 4. BETA-GAMMA: class C, depth 4
# =========================================================================

class TestBetaGammaTridegree:
    """Beta-gamma system: Contact class, shadow depth 4."""

    def test_kappa(self):
        assert kappa('betagamma') == Rational(-1)

    def test_class_C(self):
        assert shadow_class('betagamma') == 'C'

    def test_depth_4(self):
        assert shadow_depth_value('betagamma') == 4

    def test_terminates(self):
        assert terminates('betagamma') is True

    def test_tree_sh2(self):
        tree = genus0_tree_shadows('betagamma')
        assert tree[2] == Rational(-1)

    def test_tree_sh3_zero(self):
        """Cubic = 0 on the contact / weight-changing line."""
        tree = genus0_tree_shadows('betagamma')
        assert tree[3] == 0

    def test_tree_sh4_nonzero(self):
        """Quartic = -5/12."""
        tree = genus0_tree_shadows('betagamma')
        assert tree[4] == Rational(-5, 12)

    def test_tree_sh5_zero(self):
        """Quintic = 0 (terminates at depth 4)."""
        tree = genus0_tree_shadows('betagamma')
        assert tree[5] == 0

    def test_tree_sh6_through_sh8_zero(self):
        tree = genus0_tree_shadows('betagamma', max_n=8)
        for n in range(5, 9):
            assert tree[n] == 0

    def test_genus1_free_energy(self):
        g1 = genus1_shadows('betagamma')
        assert (1, 0, 0) in g1
        assert simplify(g1[(1, 0, 0)] - Rational(-1, 24)) == 0

    def test_genus1_hessian_correction(self):
        """delta_H^{(1)} = Lambda_P(Q) = 6 * (-1) * (-5/12) = 5/2."""
        g1 = genus1_shadows('betagamma')
        # P = 1/kappa = 1/(-1) = -1
        # Lambda_P(Q x^4) = C(4,2) * P * Q = 6 * (-1) * (-5/12) = 5/2
        assert (1, 2, 0) in g1
        expected = 6 * Rational(-1) * Rational(-5, 12)  # = 5/2
        assert simplify(g1[(1, 2, 0)] - expected) == 0

    def test_genus2_free_energy(self):
        g2 = genus2_shadows('betagamma')
        assert (2, 0, 0) in g2
        assert simplify(g2[(2, 0, 0)] - Rational(-1) * Rational(7, 5760)) == 0

    def test_no_planted_forest(self):
        """Contact class: no d >= 1 corrections."""
        pf = planted_forest_corrections('betagamma')
        assert len(pf) == 0


# =========================================================================
# 5. VIRASORO: class M, depth infinity
# =========================================================================

class TestVirasoroTridegree:
    """Virasoro Vir_c: Mixed class, infinite shadow depth."""

    def test_kappa(self):
        assert simplify(kappa('virasoro') - c / 2) == 0

    def test_class_M(self):
        assert shadow_class('virasoro') == 'M'

    def test_depth_infinite(self):
        assert shadow_depth_value('virasoro') is None

    def test_does_not_terminate(self):
        assert terminates('virasoro') is False

    def test_tree_sh2(self):
        tree = genus0_tree_shadows('virasoro', max_n=4)
        assert simplify(tree[2] - c / 2) == 0

    def test_tree_sh3(self):
        tree = genus0_tree_shadows('virasoro', max_n=4)
        assert simplify(tree[3] - 2) == 0

    def test_tree_sh4(self):
        """Q^contact_Vir = 10/[c(5c+22)]."""
        tree = genus0_tree_shadows('virasoro', max_n=4)
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(tree[4] - expected) == 0

    def test_tree_sh5(self):
        """Sh_5 = -48/[c^2(5c+22)] from master equation."""
        tree = genus0_tree_shadows('virasoro', max_n=5)
        expected = Rational(-48) / (c**2 * (5 * c + 22))
        assert simplify(tree[5] - expected) == 0

    def test_tree_sh5_nonzero(self):
        """Quintic is FORCED nonzero (Virasoro = class M)."""
        tree = genus0_tree_shadows('virasoro', max_n=5)
        assert simplify(tree[5]) != 0

    def test_tree_sh6_nonzero(self):
        """Sextic is nonzero for Virasoro (infinite tower)."""
        tree = genus0_tree_shadows('virasoro', max_n=6)
        assert simplify(tree[6]) != 0

    def test_tree_sh7_nonzero(self):
        tree = genus0_tree_shadows('virasoro', max_n=7)
        assert simplify(tree[7]) != 0

    def test_tree_sh8_nonzero(self):
        tree = genus0_tree_shadows('virasoro', max_n=8)
        assert simplify(tree[8]) != 0

    def test_genus1_free_energy(self):
        """F_1 = kappa/24 = c/48."""
        g1 = genus1_shadows('virasoro')
        assert (1, 0, 0) in g1
        assert simplify(g1[(1, 0, 0)] - c / 48) == 0

    def test_genus1_hessian_correction(self):
        """delta_H^{(1)} = 120/[c^2(5c+22)]."""
        g1 = genus1_shadows('virasoro')
        assert (1, 2, 0) in g1
        expected = Rational(120) / (c**2 * (5 * c + 22))
        assert simplify(g1[(1, 2, 0)] - expected) == 0

    def test_genus1_one_point(self):
        """(1, 1, 0) = Lambda_P(Sh_3) = C(3,2) * (2/c) * 2 = 12/c."""
        g1 = genus1_shadows('virasoro')
        assert (1, 1, 0) in g1
        assert simplify(g1[(1, 1, 0)] - Rational(12) / c) == 0

    def test_genus2_free_energy(self):
        """F_2 = kappa * 7/5760 = c * 7/11520."""
        g2 = genus2_shadows('virasoro')
        assert (2, 0, 0) in g2
        expected = c / 2 * Rational(7, 5760)
        assert simplify(g2[(2, 0, 0)] - expected) == 0

    def test_planted_forest_nonzero(self):
        """Class M has nonzero d=1 corrections."""
        pf = planted_forest_corrections('virasoro')
        assert len(pf) > 0

    def test_planted_forest_quartic(self):
        """(0, 4, 1): clutching correction to quartic."""
        pf = planted_forest_corrections('virasoro')
        assert (0, 4, 1) in pf

    def test_mc_check_sh2(self):
        result = mc_equation_check('virasoro', 0, 2, 0)
        assert result['passes'] is True

    def test_mc_check_sh3(self):
        result = mc_equation_check('virasoro', 0, 3, 0)
        assert result['passes'] is True

    def test_mc_check_sh4(self):
        result = mc_equation_check('virasoro', 0, 4, 0)
        assert result['passes'] is True

    def test_mc_check_sh5(self):
        result = mc_equation_check('virasoro', 0, 5, 0)
        assert result['passes'] is True

    def test_mc_check_sh6(self):
        result = mc_equation_check('virasoro', 0, 6, 0)
        assert result['passes'] is True

    def test_mc_check_sh7(self):
        result = mc_equation_check('virasoro', 0, 7, 0)
        assert result['passes'] is True

    def test_mc_check_sh8(self):
        result = mc_equation_check('virasoro', 0, 8, 0)
        assert result['passes'] is True

    def test_depth_spectrum_has_d0_and_d1(self):
        spec = depth_spectrum('virasoro')
        assert 0 in spec
        assert 1 in spec

    def test_consistency_with_virasoro_tower(self):
        """Cross-check with shadow_tower_atlas.virasoro_tower."""
        from compute.lib.shadow_tower_atlas import virasoro_tower
        atlas = virasoro_tower(8)
        tree = genus0_tree_shadows('virasoro', max_n=8)
        for n in range(2, 9):
            assert simplify(tree[n] - atlas[n]) == 0, \
                f"Mismatch at arity {n}: {tree[n]} vs {atlas[n]}"

    def test_numerical_genus1_c_equals_1(self):
        """Numerical check at c=1."""
        g1 = genus1_shadows('virasoro', c=Rational(1))
        assert (1, 0, 0) in g1
        assert g1[(1, 0, 0)] == Rational(1, 48)

    def test_numerical_genus1_c_equals_26(self):
        """At c=26: F_1 = 26/48 = 13/24."""
        g1 = genus1_shadows('virasoro', c=Rational(26))
        assert (1, 0, 0) in g1
        assert g1[(1, 0, 0)] == Rational(13, 24)


# =========================================================================
# 6. W_3: class M, depth infinity
# =========================================================================

class TestW3Tridegree:
    """W_3 algebra on the T-line: Mixed class, infinite tower."""

    def test_kappa(self):
        assert simplify(kappa('w3') - 5 * c / 6) == 0

    def test_class_M(self):
        assert shadow_class('w3') == 'M'

    def test_depth_infinite(self):
        assert shadow_depth_value('w3') is None

    def test_tree_sh2(self):
        tree = genus0_tree_shadows('w3', max_n=4)
        assert simplify(tree[2] - 5 * c / 6) == 0

    def test_tree_sh3(self):
        """Cubic = 2 on the T-line (same as Virasoro T-line)."""
        tree = genus0_tree_shadows('w3', max_n=4)
        assert simplify(tree[3] - 2) == 0

    def test_tree_sh4(self):
        """Quartic on T-line: same formula as Virasoro."""
        tree = genus0_tree_shadows('w3', max_n=4)
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(tree[4] - expected) == 0

    def test_genus1_free_energy(self):
        g1 = genus1_shadows('w3')
        assert (1, 0, 0) in g1
        expected = 5 * c / 6 / 24
        assert simplify(g1[(1, 0, 0)] - expected) == 0

    def test_planted_forest_nonzero(self):
        pf = planted_forest_corrections('w3')
        assert len(pf) > 0


# =========================================================================
# 7. MC EQUATION CHECKS across families
# =========================================================================

class TestMCEquation:
    """Verify MC equation at multiple tridegrees."""

    @pytest.mark.parametrize("family", [
        'heisenberg', 'affine_sl2', 'betagamma', 'virasoro',
    ])
    def test_mc_seed_sh2(self, family):
        result = mc_equation_check(family, 0, 2, 0)
        assert result['passes'] is True

    @pytest.mark.parametrize("family", [
        'heisenberg', 'affine_sl2', 'betagamma', 'virasoro',
    ])
    def test_mc_genus1_f1(self, family):
        result = mc_equation_check(family, 1, 0, 0)
        assert result['passes'] is True

    @pytest.mark.parametrize("family", [
        'heisenberg', 'affine_sl2', 'betagamma', 'virasoro',
    ])
    def test_mc_genus2_f2(self, family):
        result = mc_equation_check(family, 2, 0, 0)
        assert result['passes'] is True

    def test_virasoro_mc_arity_range(self):
        """MC check at arities 3-8 for Virasoro."""
        for n in range(3, 9):
            result = mc_equation_check('virasoro', 0, n, 0)
            assert result['passes'] is True, \
                f"MC failed at (0, {n}, 0) for Virasoro"


# =========================================================================
# 8. DEPTH SPECTRUM tests
# =========================================================================

class TestDepthSpectrum:
    """Verify depth spectrum for each shadow class."""

    def test_heisenberg_all_d0(self):
        spec = depth_spectrum('heisenberg')
        assert set(spec.keys()) == {0}

    def test_affine_all_d0(self):
        spec = depth_spectrum('affine_sl2')
        assert set(spec.keys()) == {0}

    def test_betagamma_all_d0(self):
        spec = depth_spectrum('betagamma')
        assert set(spec.keys()) == {0}

    def test_virasoro_has_d1(self):
        spec = depth_spectrum('virasoro')
        assert 1 in spec

    def test_w3_has_d1(self):
        spec = depth_spectrum('w3')
        assert 1 in spec


# =========================================================================
# 9. TABLE OUTPUT tests
# =========================================================================

class TestTableOutput:
    """Verify table formatting."""

    def test_heisenberg_table_nonempty(self):
        table = tridegree_table('heisenberg')
        assert len(table) > 0
        assert 'Heisenberg' in table

    def test_virasoro_table_nonempty(self):
        table = tridegree_table('virasoro')
        assert len(table) > 0
        assert 'Virasoro' in table

    def test_table_contains_class(self):
        table = tridegree_table('affine_sl2')
        assert 'Class: L' in table

    def test_table_contains_depth(self):
        table = tridegree_table('betagamma')
        assert 'Depth: 4' in table

    def test_table_contains_total_count(self):
        table = tridegree_table('lattice_Z')
        assert 'Total nonzero entries' in table

    def test_table_contains_depth_spectrum(self):
        table = tridegree_table('virasoro')
        assert 'Depth spectrum' in table


# =========================================================================
# 10. CROSS-CONSISTENCY with existing modules
# =========================================================================

class TestCrossConsistency:
    """Cross-check against shadow_tower_atlas and modular_shadow_tower."""

    def test_atlas_virasoro_match(self):
        """Tree-level shadows match virasoro_tower from atlas."""
        from compute.lib.shadow_tower_atlas import virasoro_tower
        atlas = virasoro_tower(8)
        ours = genus0_tree_shadows('virasoro', max_n=8)
        for n in range(2, 9):
            assert simplify(ours[n] - atlas[n]) == 0

    def test_atlas_affine_sl2_match(self):
        """kappa matches affine_sl2_tower from atlas."""
        from compute.lib.shadow_tower_atlas import affine_sl2_tower
        atlas = affine_sl2_tower()
        assert simplify(kappa('affine_sl2') - atlas[2]) == 0
        assert cubic_shadow('affine_sl2') == atlas[3]
        assert quartic_contact('affine_sl2') == atlas[4]

    def test_atlas_lattice_match(self):
        """kappa matches lattice_tower from atlas."""
        from compute.lib.shadow_tower_atlas import lattice_tower
        for family, rank in [('lattice_Z', 1), ('lattice_Z2', 2), ('lattice_A2', 2)]:
            atlas = lattice_tower(rank)
            assert kappa(family) == atlas[2]
            assert cubic_shadow(family) == atlas[3]
            assert quartic_contact(family) == atlas[4]

    def test_atlas_betagamma_match(self):
        """kappa and quartic match betagamma_tower from atlas."""
        from compute.lib.shadow_tower_atlas import betagamma_tower
        atlas = betagamma_tower()
        assert kappa('betagamma') == atlas[2]
        assert quartic_contact('betagamma') == atlas[4]

    def test_modular_genus1_hessian(self):
        """delta_H^{(1)}_Vir = 120/[c^2(5c+22)] matches modular_shadow_tower."""
        from compute.lib.modular_shadow_tower import virasoro_genus1_hessian_correction
        expected = virasoro_genus1_hessian_correction()
        g1 = genus1_shadows('virasoro')
        assert simplify(g1[(1, 2, 0)] - expected) == 0

    def test_modular_loop_ratio(self):
        """rho^{(1)}_Vir = 240/[c^3(5c+22)] matches modular_shadow_tower."""
        from compute.lib.modular_shadow_tower import virasoro_loop_ratio
        expected = virasoro_loop_ratio()
        g1 = genus1_shadows('virasoro')
        kap = kappa('virasoro')
        rho = simplify(g1[(1, 2, 0)] / kap)
        assert simplify(rho - expected) == 0


# =========================================================================
# 11. GENUS FREE ENERGY convenience function
# =========================================================================

class TestGenusFreeEnergy:

    @pytest.mark.parametrize("family", [
        'heisenberg', 'affine_sl2', 'betagamma', 'virasoro', 'w3',
        'lattice_Z', 'lattice_Z2', 'lattice_A2',
    ])
    def test_f1_equals_kappa_over_24(self, family):
        F1 = genus_free_energy(family, 1)
        kap = kappa(family)
        assert simplify(F1 - kap / 24) == 0

    @pytest.mark.parametrize("family", [
        'heisenberg', 'affine_sl2', 'betagamma', 'virasoro', 'w3',
        'lattice_Z', 'lattice_Z2', 'lattice_A2',
    ])
    def test_f2_equals_kappa_7_5760(self, family):
        F2 = genus_free_energy(family, 2)
        kap = kappa(family)
        assert simplify(F2 - kap * Rational(7, 5760)) == 0

    @pytest.mark.parametrize("family", [
        'heisenberg', 'affine_sl2', 'betagamma', 'virasoro',
    ])
    def test_f0_is_none(self, family):
        assert genus_free_energy(family, 0) is None


# =========================================================================
# 12. PROPAGATOR tests
# =========================================================================

class TestPropagator:

    def test_virasoro_propagator(self):
        P = propagator('virasoro')
        assert simplify(P - 2 / c) == 0

    def test_heisenberg_propagator(self):
        P = propagator('heisenberg')
        assert simplify(P - 1 / k) == 0

    def test_affine_propagator(self):
        P = propagator('affine_sl2')
        expected = 4 / (Rational(3) * (k + 2))
        assert simplify(P - expected) == 0

    def test_betagamma_propagator(self):
        P = propagator('betagamma')
        assert P == Rational(-1)

    def test_w3_propagator(self):
        P = propagator('w3')
        expected = 6 / (5 * c)
        assert simplify(P - expected) == 0


# =========================================================================
# 13. ERROR HANDLING
# =========================================================================

class TestErrorHandling:

    def test_unknown_family_raises(self):
        with pytest.raises(ValueError, match="Unknown family"):
            kappa('nonexistent')

    def test_unknown_family_tridegree_raises(self):
        with pytest.raises(ValueError, match="Unknown family"):
            tridegree_shadow('nonexistent')

    def test_unknown_family_tree_raises(self):
        with pytest.raises(ValueError, match="Unknown family"):
            genus0_tree_shadows('nonexistent')
