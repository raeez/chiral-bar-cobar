"""Tests for E1 tridegree shadows: ordered R-matrices, CYBE, genus-1, coinvariants.

Ground truth:
  - e1_shadow_tower.py: archetype shadow data (Heisenberg, affine, Virasoro)
  - shadow_tower_atlas.py: closed-form shadow tower computations
  - ordered_modular_bar.py: Weierstrass p numerical implementation
  - nonlinear_modular_shadows.tex: shadow depth classification
  - higher_genus_modular_koszul.tex: collision residue, coinvariant projection

TARGET: 50+ tests across 8 test classes.
"""

import numpy as np
import pytest
from sympy import Rational, Symbol, simplify, Matrix

from compute.lib.e1_tridegree_shadows import (
    e1_r_matrix,
    e1_cybe_check,
    e1_cybe_check_detailed,
    e1_genus1_r_matrix,
    e1_coinvariant_projection,
    e1_tridegree_table,
    e1_kappa_from_r_matrix,
    e1_shadow_depth,
    e1_depth_class,
    e1_tridegree_summary,
    weierstrass_p,
    weierstrass_p_deriv,
    weierstrass_invariants,
    eisenstein_g2k,
    FAMILIES,
)


z = Symbol('z')
k = Symbol('k')
c = Symbol('c')


# =========================================================================
# 1. R-matrix structure for all 5 families
# =========================================================================

class TestRMatrix:
    """Genus-0 E₁ scalar shadow r^{sc}(z) for all five families.

    These are the *scalar/vacuum projection* r-matrices, NOT the full
    collision r-matrices r^{coll}(z).  For Virasoro, r^{sc}(z) = c/(2z)
    is the primary-line projection; the full r^{coll}(z) has a cubic
    pole from the central extension.  See rem:three-r-matrices in
    e1_modular_koszul.tex.
    """

    def test_heisenberg_r_matrix(self):
        """Heisenberg: r(z) = k/z (scalar)."""
        r = e1_r_matrix('heisenberg')
        assert simplify(r - k / z) == 0

    def test_heisenberg_r_matrix_numerical(self):
        """Heisenberg at k=3: r(z) = 3/z."""
        r = e1_r_matrix('heisenberg', k=3)
        assert simplify(r - 3 / z) == 0

    def test_affine_sl2_r_matrix_is_matrix(self):
        """Affine sl_2: r(z) = k * Omega / z is a 4x4 Matrix."""
        r = e1_r_matrix('affine_sl2')
        assert isinstance(r, Matrix)
        assert r.shape == (4, 4)

    def test_affine_sl2_r_matrix_casimir_structure(self):
        """Affine sl_2 Casimir: diagonal entries are +/- 1/2 * k/z."""
        r = e1_r_matrix('affine_sl2')
        # r[0,0] = k * (1/2) / z
        assert simplify(r[0, 0] - k / (2 * z)) == 0
        # r[1,1] = k * (-1/2) / z
        assert simplify(r[1, 1] + k / (2 * z)) == 0

    def test_affine_sl2_r_matrix_off_diagonal(self):
        """Affine sl_2: off-diagonal entries encode e x f + f x e."""
        r = e1_r_matrix('affine_sl2')
        # r[1,2] = k * 1 / z  (from e x f)
        assert simplify(r[1, 2] - k / z) == 0
        # r[2,1] = k * 1 / z  (from f x e)
        assert simplify(r[2, 1] - k / z) == 0

    def test_virasoro_r_matrix(self):
        """Virasoro: r(z) = (c/2)/z on primary line."""
        r = e1_r_matrix('virasoro')
        assert simplify(r - c / (2 * z)) == 0

    def test_virasoro_r_matrix_numerical(self):
        """Virasoro at c=26: r(z) = 13/z."""
        r = e1_r_matrix('virasoro', c=26)
        assert simplify(r - 13 / z) == 0

    def test_lattice_vz_r_matrix(self):
        """Lattice V_Z: r(z) = 1/z (Heisenberg at k=1)."""
        r = e1_r_matrix('lattice_vz')
        assert simplify(r - 1 / z) == 0

    def test_lattice_va2_r_matrix(self):
        """Lattice V_{A2}: r(z) = 2/z (rank-2 Heisenberg)."""
        r = e1_r_matrix('lattice_va2')
        assert simplify(r - 2 / z) == 0

    def test_lattice_vz_equals_heisenberg_k1(self):
        """V_Z R-matrix equals Heisenberg at k=1."""
        r_vz = e1_r_matrix('lattice_vz')
        r_heis = e1_r_matrix('heisenberg', k=1)
        assert simplify(r_vz - r_heis) == 0

    def test_lattice_va2_equals_2_times_lattice_vz(self):
        """V_{A2} = 2 * V_Z (rank additivity)."""
        r_va2 = e1_r_matrix('lattice_va2')
        r_vz = e1_r_matrix('lattice_vz')
        assert simplify(r_va2 - 2 * r_vz) == 0


# =========================================================================
# 2. CYBE verification
# =========================================================================

class TestCYBE:
    """Classical Yang-Baxter equation verification for all families."""

    def test_cybe_heisenberg(self):
        """CYBE trivially satisfied for Heisenberg (scalar, 1d)."""
        assert e1_cybe_check('heisenberg') is True

    def test_cybe_virasoro(self):
        """CYBE trivially satisfied for Virasoro (scalar on primary line)."""
        assert e1_cybe_check('virasoro') is True

    def test_cybe_lattice_vz(self):
        """CYBE trivially satisfied for V_Z (scalar)."""
        assert e1_cybe_check('lattice_vz') is True

    def test_cybe_lattice_va2(self):
        """CYBE trivially satisfied for V_{A2} (scalar)."""
        assert e1_cybe_check('lattice_va2') is True

    def test_cybe_affine_sl2_k1(self):
        """Strict CYBE for skew part of affine sl_2 at k=1."""
        assert e1_cybe_check('affine_sl2', k=1.0) is True

    def test_cybe_affine_sl2_k2(self):
        """Strict CYBE for skew part at k=2."""
        assert e1_cybe_check('affine_sl2', k=2.0) is True

    def test_cybe_affine_sl2_k5(self):
        """Strict CYBE for skew part at k=5."""
        assert e1_cybe_check('affine_sl2', k=5.0) is True

    def test_cybe_affine_sl2_k_fractional(self):
        """Strict CYBE for skew part at k=1/3."""
        assert e1_cybe_check('affine_sl2', k=1.0 / 3.0) is True

    def test_cybe_detailed_heisenberg(self):
        """Detailed CYBE: Heisenberg norm = 0."""
        result = e1_cybe_check_detailed('heisenberg')
        assert result['cybe_satisfied'] is True
        assert result['norm'] == 0.0

    def test_cybe_detailed_affine_skew_norm(self):
        """Detailed: skew CYBE norm < 1e-9 for affine sl_2."""
        result = e1_cybe_check_detailed('affine_sl2', k=1.0)
        assert result['cybe_skew_norm'] < 1e-9

    def test_cybe_detailed_affine_mcybe_nonzero(self):
        """Full Casimir satisfies MODIFIED CYBE: LHS is nonzero."""
        result = e1_cybe_check_detailed('affine_sl2', k=1.0)
        assert result['mcybe_nonzero'] is True
        assert result['mcybe_full_norm'] > 1e-9

    def test_cybe_all_families(self):
        """CYBE satisfied for all 5 families."""
        for fam in FAMILIES:
            assert e1_cybe_check(fam) is True, f"CYBE failed for {fam}"


# =========================================================================
# 3. Kappa from R-matrix
# =========================================================================

class TestKappaFromRMatrix:
    """Verify kappa = av(r(z)) = Res_{z=0}[r(z)] for all families."""

    def test_heisenberg_kappa(self):
        """Heisenberg: kappa = k."""
        kappa = e1_kappa_from_r_matrix('heisenberg')
        assert simplify(kappa - k) == 0

    def test_heisenberg_kappa_numerical(self):
        """Heisenberg at k=5: kappa = 5."""
        kappa = e1_kappa_from_r_matrix('heisenberg', k=5)
        assert kappa == 5

    def test_affine_sl2_kappa(self):
        """Affine sl_2: kappa = 3(k+2)/4."""
        kappa = e1_kappa_from_r_matrix('affine_sl2')
        expected = 3 * (k + 2) / 4
        assert simplify(kappa - expected) == 0

    def test_affine_sl2_kappa_k1(self):
        """Affine sl_2 at k=1: kappa = 9/4."""
        kappa = e1_kappa_from_r_matrix('affine_sl2', k=1)
        assert float(kappa) == pytest.approx(2.25)

    def test_affine_sl2_kappa_k4(self):
        """Affine sl_2 at k=4: kappa = 3*6/4 = 4.5."""
        kappa = e1_kappa_from_r_matrix('affine_sl2', k=4)
        assert float(kappa) == pytest.approx(4.5)

    def test_virasoro_kappa(self):
        """Virasoro: kappa = c/2."""
        kappa = e1_kappa_from_r_matrix('virasoro')
        assert simplify(kappa - c / 2) == 0

    def test_virasoro_kappa_c26(self):
        """Virasoro at c=26: kappa = 13."""
        kappa = e1_kappa_from_r_matrix('virasoro', c=26)
        assert float(kappa) == pytest.approx(13.0)

    def test_lattice_vz_kappa(self):
        """V_Z: kappa = 1."""
        assert e1_kappa_from_r_matrix('lattice_vz') == 1

    def test_lattice_va2_kappa(self):
        """V_{A2}: kappa = 2 (rank 2)."""
        assert e1_kappa_from_r_matrix('lattice_va2') == 2


# =========================================================================
# 4. Coinvariant projection
# =========================================================================

class TestCoinvariantProjection:
    """Verify coinvariant projection FAss -> FCom recovers unordered shadows."""

    def test_coinvariant_arity2_equals_kappa_heisenberg(self):
        """av(r(z)) = kappa for Heisenberg."""
        proj = e1_coinvariant_projection('heisenberg', 2)
        kappa = e1_kappa_from_r_matrix('heisenberg')
        assert simplify(proj - kappa) == 0

    def test_coinvariant_arity2_equals_kappa_affine(self):
        """av(r(z)) = kappa for affine sl_2."""
        proj = e1_coinvariant_projection('affine_sl2', 2)
        kappa = e1_kappa_from_r_matrix('affine_sl2')
        assert simplify(proj - kappa) == 0

    def test_coinvariant_arity2_equals_kappa_virasoro(self):
        """av(r(z)) = kappa for Virasoro."""
        proj = e1_coinvariant_projection('virasoro', 2)
        kappa = e1_kappa_from_r_matrix('virasoro')
        assert simplify(proj - kappa) == 0

    def test_coinvariant_arity2_equals_kappa_lattice_vz(self):
        """av(r(z)) = kappa for V_Z."""
        proj = e1_coinvariant_projection('lattice_vz', 2)
        assert proj == 1

    def test_coinvariant_arity2_equals_kappa_lattice_va2(self):
        """av(r(z)) = kappa for V_{A2}."""
        proj = e1_coinvariant_projection('lattice_va2', 2)
        assert proj == 2

    def test_coinvariant_arity3_heisenberg_zero(self):
        """Cubic shadow C = 0 for Heisenberg (Gaussian class)."""
        assert e1_coinvariant_projection('heisenberg', 3) == 0

    def test_coinvariant_arity3_affine_nonzero(self):
        """Cubic shadow C != 0 for affine sl_2 (structure constants)."""
        c3 = e1_coinvariant_projection('affine_sl2', 3)
        # At symbolic level: k/(k+2) which is nonzero for generic k
        assert c3 != 0

    def test_coinvariant_arity3_virasoro(self):
        """Cubic shadow C = 2 for Virasoro."""
        c3 = e1_coinvariant_projection('virasoro', 3)
        assert c3 == 2

    def test_coinvariant_arity3_lattice_zero(self):
        """Cubic shadow C = 0 for lattice VOAs (Gaussian)."""
        assert e1_coinvariant_projection('lattice_vz', 3) == 0
        assert e1_coinvariant_projection('lattice_va2', 3) == 0

    def test_coinvariant_arity4_heisenberg_zero(self):
        """Quartic shadow = 0 for Heisenberg."""
        assert e1_coinvariant_projection('heisenberg', 4) == 0

    def test_coinvariant_arity4_affine_zero(self):
        """Quartic shadow = 0 for affine sl_2 (Jacobi kills it)."""
        assert e1_coinvariant_projection('affine_sl2', 4) == 0

    def test_coinvariant_arity4_virasoro(self):
        """Quartic shadow Q = 10/[c(5c+22)] for Virasoro."""
        q4 = e1_coinvariant_projection('virasoro', 4)
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(q4 - expected) == 0


# =========================================================================
# 5. Shadow depth
# =========================================================================

class TestShadowDepth:
    """Ordered shadow depth matches unordered for all families."""

    def test_heisenberg_depth(self):
        assert e1_shadow_depth('heisenberg') == 2

    def test_affine_sl2_depth(self):
        assert e1_shadow_depth('affine_sl2') == 3

    def test_virasoro_depth(self):
        assert e1_shadow_depth('virasoro') == float('inf')

    def test_lattice_vz_depth(self):
        assert e1_shadow_depth('lattice_vz') == 2

    def test_lattice_va2_depth(self):
        assert e1_shadow_depth('lattice_va2') == 2

    def test_depth_class_gaussian(self):
        """Heisenberg, V_Z, V_{A2} are all Gaussian (G)."""
        assert e1_depth_class('heisenberg') == 'G'
        assert e1_depth_class('lattice_vz') == 'G'
        assert e1_depth_class('lattice_va2') == 'G'

    def test_depth_class_lie(self):
        """Affine sl_2 is Lie (L)."""
        assert e1_depth_class('affine_sl2') == 'L'

    def test_depth_class_mixed(self):
        """Virasoro is Mixed (M)."""
        assert e1_depth_class('virasoro') == 'M'

    def test_ordered_equals_unordered_depth(self):
        """Ordered shadow depth = unordered shadow depth for all families.

        The coinvariant projection preserves termination arity.
        """
        expected_depths = {
            'heisenberg': 2,
            'affine_sl2': 3,
            'virasoro': float('inf'),
            'lattice_vz': 2,
            'lattice_va2': 2,
        }
        for fam, exp_d in expected_depths.items():
            assert e1_shadow_depth(fam) == exp_d, f"Depth mismatch for {fam}"

    def test_lattice_voas_same_structure_as_heisenberg(self):
        """Lattice VOAs have same depth/class as Heisenberg at their rank."""
        assert e1_shadow_depth('lattice_vz') == e1_shadow_depth('heisenberg')
        assert e1_depth_class('lattice_vz') == e1_depth_class('heisenberg')
        assert e1_shadow_depth('lattice_va2') == e1_shadow_depth('heisenberg')
        assert e1_depth_class('lattice_va2') == e1_depth_class('heisenberg')


# =========================================================================
# 6. Weierstrass p-function
# =========================================================================

class TestWeierstrassP:
    """Weierstrass p-function numerical verification."""

    @pytest.fixture
    def tau_val(self):
        """Standard test tau with Im(tau) > 0."""
        return 0.1 + 0.9j

    def test_laurent_leading_term(self, tau_val):
        """p(z; tau) ~ 1/z^2 for z -> 0."""
        z_small = 0.001
        wp = weierstrass_p(z_small, tau_val, terms=5)
        # Leading term: 1/z^2 = 10^6
        assert abs(wp - 1.0 / z_small ** 2) / abs(1.0 / z_small ** 2) < 0.01

    def test_laurent_moderate_z(self, tau_val):
        """p(z; tau) has correct 1/z^2 pole at moderate z."""
        z_val = 0.01
        wp = weierstrass_p(z_val, tau_val, terms=8)
        leading = 1.0 / z_val ** 2
        # The correction is O(z^2), so relative error ~ z^4
        rel_err = abs(wp - leading) / abs(leading)
        # At z=0.01, correction is ~ G_4 * z^2 ~ small
        assert rel_err < 0.1

    def test_p_even_function(self, tau_val):
        """p(-z; tau) = p(z; tau) (p is even)."""
        z_val = 0.05 + 0.02j
        wp_plus = weierstrass_p(z_val, tau_val, terms=8)
        wp_minus = weierstrass_p(-z_val, tau_val, terms=8)
        assert abs(wp_plus - wp_minus) / max(abs(wp_plus), 1) < 1e-8

    def test_p_derivative_leading(self, tau_val):
        """p'(z; tau) ~ -2/z^3 for z -> 0."""
        z_small = 0.005
        wp_prime = weierstrass_p_deriv(z_small, tau_val, terms=5)
        leading = -2.0 / z_small ** 3
        rel_err = abs(wp_prime - leading) / abs(leading)
        assert rel_err < 0.05

    def test_p_derivative_odd(self, tau_val):
        """p'(-z) = -p'(z) (derivative is odd)."""
        z_val = 0.05 + 0.02j
        d_plus = weierstrass_p_deriv(z_val, tau_val, terms=8)
        d_minus = weierstrass_p_deriv(-z_val, tau_val, terms=8)
        assert abs(d_plus + d_minus) / max(abs(d_plus), 1) < 1e-8

    def test_differential_equation(self, tau_val):
        """p satisfies (p')^2 = 4 p^3 - g2 p - g3 (spot check).

        This is the Weierstrass differential equation with invariants
        g2 = 60 G_4(tau), g3 = 140 G_6(tau).
        """
        z_val = 0.1 + 0.05j
        wp = weierstrass_p(z_val, tau_val, terms=12)
        wp_prime = weierstrass_p_deriv(z_val, tau_val, terms=12)
        g2, g3 = weierstrass_invariants(tau_val)

        lhs = wp_prime ** 2
        rhs = 4.0 * wp ** 3 - g2 * wp - g3

        rel_err = abs(lhs - rhs) / max(abs(lhs), 1)
        assert rel_err < 0.05, f"DE residual: {rel_err}"

    def test_eisenstein_g4_positive(self):
        """G_4(i) is real and positive."""
        tau_val = 1.0j  # tau = i
        g4 = eisenstein_g2k(2, tau_val)
        assert np.real(g4) > 0
        assert abs(np.imag(g4)) < 1e-10

    def test_eisenstein_g4_vanishes_at_rho(self):
        """G_4(rho) = 0 where rho = (-1 + i sqrt(3))/2 (hexagonal lattice).

        At the hexagonal point, E_4(rho) = 0 by the Z_3 symmetry:
        E_4(-1/tau) = tau^4 E_4(tau), and rho satisfies rho^2 + rho + 1 = 0,
        so E_4(rho) = rho^4 E_4(rho) = rho E_4(rho), forcing E_4(rho) = 0.
        """
        rho = (-1 + 1j * np.sqrt(3)) / 2.0
        g4_rho = eisenstein_g2k(2, rho, n_terms=50)
        assert abs(g4_rho) < 1e-10, f"G_4(rho) = {g4_rho}"


# =========================================================================
# 7. Genus-1 R-matrix
# =========================================================================

class TestGenus1RMatrix:
    """Genus-1 ordered shadow (elliptic R-matrix)."""

    @pytest.fixture
    def tau_val(self):
        return 0.1 + 1.0j

    def test_heisenberg_genus1_scalar(self):
        """Heisenberg genus-1 R-matrix descriptor is scalar."""
        desc = e1_genus1_r_matrix('heisenberg')
        assert desc['type'] == 'scalar'

    def test_heisenberg_genus1_formula(self):
        """Heisenberg: r^{(1)}(z; tau) = k * p(z; tau)."""
        desc = e1_genus1_r_matrix('heisenberg', k=3.0)
        assert desc['formula'] == 'k * p(z; tau)'
        assert desc['coefficient'] == 3.0

    def test_heisenberg_genus1_numerical(self, tau_val):
        """Heisenberg genus-1: numerical evaluation = k * p(z)."""
        z_val = 0.1 + 0.05j
        k_val = 2.0
        r1 = e1_genus1_r_matrix('heisenberg', tau_val=tau_val,
                                 z_val=z_val, k=k_val, terms=8)
        wp = weierstrass_p(z_val, tau_val, terms=8)
        assert abs(r1 - k_val * wp) / max(abs(r1), 1) < 1e-12

    def test_lattice_vz_genus1_equals_p(self, tau_val):
        """V_Z: r^{(1)} = p(z; tau) (Heisenberg at k=1)."""
        z_val = 0.08
        r1 = e1_genus1_r_matrix('lattice_vz', tau_val=tau_val,
                                 z_val=z_val, terms=8)
        wp = weierstrass_p(z_val, tau_val, terms=8)
        assert abs(r1 - wp) / max(abs(wp), 1) < 1e-12

    def test_lattice_va2_genus1_equals_2p(self, tau_val):
        """V_{A2}: r^{(1)} = 2 * p(z; tau) (rank 2)."""
        z_val = 0.08
        r1 = e1_genus1_r_matrix('lattice_va2', tau_val=tau_val,
                                 z_val=z_val, terms=8)
        wp = weierstrass_p(z_val, tau_val, terms=8)
        assert abs(r1 - 2.0 * wp) / max(abs(wp), 1) < 1e-12

    def test_affine_sl2_genus1_is_matrix(self, tau_val):
        """Affine sl_2 genus-1 R-matrix is 4x4."""
        z_val = 0.1
        r1 = e1_genus1_r_matrix('affine_sl2', tau_val=tau_val,
                                 z_val=z_val, k=1.0, terms=5)
        assert r1.shape == (4, 4)

    def test_virasoro_genus1_scalar(self, tau_val):
        """Virasoro genus-1: r^{(1)} = (c/2) * p(z; tau) (scalar)."""
        z_val = 0.1
        c_val = 10.0
        r1 = e1_genus1_r_matrix('virasoro', tau_val=tau_val,
                                 z_val=z_val, c=c_val, terms=8)
        wp = weierstrass_p(z_val, tau_val, terms=8)
        assert abs(r1 - (c_val / 2.0) * wp) / max(abs(r1), 1) < 1e-12

    def test_genus1_reduces_to_genus0_in_cusp_limit(self):
        """As tau -> i * infty (q -> 0), p(z; tau) -> 1/z^2 + const.

        In the cusp limit, the genus-1 R-matrix reduces to the
        genus-0 form up to a constant shift.
        """
        tau_cusp = 5.0j  # large Im(tau) => q ~ e^{-10 pi} ~ 0
        z_val = 0.2
        wp = weierstrass_p(z_val, tau_cusp, terms=5)
        leading = 1.0 / z_val ** 2
        # In the cusp limit, Eisenstein series G_{2k} -> 2 zeta(2k)
        # so the correction is a known constant
        rel_diff = abs(wp - leading) / abs(leading)
        # The correction should be small but nonzero (from G_4 * z^2)
        assert rel_diff < 0.5


# =========================================================================
# 8. E1 tridegree table
# =========================================================================

class TestTridegreeTable:
    """E1 tridegree table: nonzero (g, n, d) components."""

    def test_heisenberg_genus0_has_binary(self):
        """Heisenberg genus 0 has (0, 2, 1) entry."""
        table = e1_tridegree_table('heisenberg')
        assert (0, 2, 1) in table

    def test_heisenberg_genus1_has_correction(self):
        """Heisenberg genus 1 has (1, 2, 0) entry (p-function)."""
        table = e1_tridegree_table('heisenberg', max_g=1)
        assert (1, 2, 0) in table

    def test_heisenberg_no_arity3(self):
        """Heisenberg (Gaussian) has no arity-3 genus-0 entry."""
        table = e1_tridegree_table('heisenberg')
        assert (0, 3, 1) not in table

    def test_affine_has_arity3(self):
        """Affine sl_2 has arity-3 genus-0 entry."""
        table = e1_tridegree_table('affine_sl2')
        assert (0, 3, 1) in table

    def test_virasoro_has_all_arities(self):
        """Virasoro (Mixed) has entries at all arities 2..6."""
        table = e1_tridegree_table('virasoro', max_n=6)
        for n in range(2, 7):
            assert (0, n, 1) in table, f"Missing arity {n}"

    def test_virasoro_genus1_entries(self):
        """Virasoro has genus-1 entries."""
        table = e1_tridegree_table('virasoro', max_g=1)
        assert (1, 2, 0) in table

    def test_table_max_g0_no_genus1(self):
        """With max_g=0, no genus-1 entries appear."""
        table = e1_tridegree_table('heisenberg', max_g=0)
        for key in table:
            assert key[0] == 0, f"Unexpected genus-1 entry: {key}"

    def test_lattice_vz_same_structure_as_heisenberg(self):
        """V_Z tridegree table has same structure as Heisenberg."""
        t_vz = e1_tridegree_table('lattice_vz')
        t_heis = e1_tridegree_table('heisenberg')
        assert set(t_vz.keys()) == set(t_heis.keys())

    def test_lattice_va2_same_structure_as_heisenberg(self):
        """V_{A2} tridegree table has same structure as Heisenberg."""
        t_va2 = e1_tridegree_table('lattice_va2')
        t_heis = e1_tridegree_table('heisenberg')
        assert set(t_va2.keys()) == set(t_heis.keys())

    def test_tridegree_summary_has_all_families(self):
        """Summary table covers all 5 families."""
        summary = e1_tridegree_summary()
        for fam in FAMILIES:
            assert fam in summary

    def test_tridegree_summary_cybe_all_pass(self):
        """Summary: CYBE satisfied for all families."""
        summary = e1_tridegree_summary()
        for fam in FAMILIES:
            assert summary[fam]['cybe_satisfied'] is True
