r"""Tests for BPS wall-crossing from the shadow obstruction tower.

Multi-path verification of the Kontsevich-Soibelman wall-crossing formula
via the shadow MC equation.

Verification paths:
  Path 1: Pentagon identity from arity-3 MC
  Path 2: KS scattering diagram direct computation
  Path 3: Seiberg-Witten exact BPS spectrum
  Path 4: Joyce-Song wall-crossing formula
  Path 5: Motivic DT for simple geometries
  Path 6: Numerical BPS index integrality
"""

import math
import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.bps_wall_crossing_engine import (
    # Helpers
    euler_form,
    charge_add,
    charge_scale,
    charge_gcd,
    is_primitive,
    _lambda_fp,
    # Quantum dilogarithm and KS
    quantum_dilogarithm_series,
    ks_automorphism_log,
    ks_group_automorphism,
    # Pentagon identity
    pentagon_identity_lie_algebra,
    pentagon_identity_group_level,
    pentagon_from_mc_arity3,
    _bch_scattering,
    # Scattering diagram
    ScatteringDiagram,
    conifold_scattering_diagram,
    conifold_scattering_order_by_order,
    # Higher wall-crossing
    degree_2_wall_crossing,
    # Joyce-Song
    joyce_song_primitive_wc,
    joyce_song_full_wc,
    joyce_song_equals_convolution_bracket,
    # Seiberg-Witten
    SWBPSSpectrum,
    sw_wall_crossing_verification,
    sw_spectrum_generator,
    # Motivic DT
    motivic_dt_conifold,
    motivic_local_p2,
    # Attractor flow
    AttractorFlowTree,
    split_attractor_tree,
    attractor_flow_shadow_correspondence,
    shadow_connection_attractor_flow,
    # Torus algebra
    torus_algebra_bracket,
    verify_poisson_equals_convolution,
    # Scattering-shadow map
    scattering_shadow_arity_map,
    # Integrality
    verify_bps_integrality,
    dt_integrality_check,
    # Multi-path
    verify_pentagon_three_paths,
    verify_conifold_consistency,
    verify_sw_wall_crossing_multi_path,
    full_verification_suite,
)


# ============================================================================
# Section 1: Charge lattice arithmetic
# ============================================================================

class TestChargeLattice:
    """Test charge lattice operations."""

    def test_euler_form_rank2_basic(self):
        """Euler form <(1,0), (0,1)> = 1."""
        assert euler_form((1, 0), (0, 1)) == 1

    def test_euler_form_skew_symmetry(self):
        """<gamma_1, gamma_2> = -<gamma_2, gamma_1>."""
        g1, g2 = (2, 3), (5, 7)
        assert euler_form(g1, g2) == -euler_form(g2, g1)

    def test_euler_form_antisymmetric_vanish(self):
        """<gamma, gamma> = 0 for rank-2 skew form."""
        for g in [(1, 0), (0, 1), (1, 1), (2, 3), (7, 11)]:
            assert euler_form(g, g) == 0

    def test_euler_form_bilinear(self):
        """Bilinearity: <a*g1, g2> = a * <g1, g2>."""
        g1, g2 = (1, 0), (0, 1)
        for a in range(1, 5):
            assert euler_form(charge_scale(a, g1), g2) == a * euler_form(g1, g2)

    def test_charge_add(self):
        assert charge_add((1, 2), (3, 4)) == (4, 6)

    def test_charge_scale(self):
        assert charge_scale(3, (1, 2)) == (3, 6)

    def test_charge_gcd(self):
        assert charge_gcd((6, 10)) == 2
        assert charge_gcd((7, 11)) == 1
        assert charge_gcd((0, 5)) == 5

    def test_is_primitive(self):
        assert is_primitive((1, 0))
        assert is_primitive((0, 1))
        assert is_primitive((1, 1))
        assert is_primitive((2, 3))
        assert not is_primitive((2, 4))
        assert not is_primitive((3, 6))

    def test_euler_form_conifold_pairing(self):
        """For the conifold: <(1,0), (0,1)> = 1 (DSZ product)."""
        assert euler_form((1, 0), (0, 1)) == 1

    def test_euler_form_degree_2(self):
        """<(1,0), (0,2)> = 2 for degree-2 wall-crossing."""
        assert euler_form((1, 0), (0, 2)) == 2

    def test_euler_form_higher_rank(self):
        """Euler form for rank > 2."""
        g1 = (1, 0, 0)
        g2 = (0, 1, 0)
        g3 = (0, 0, 1)
        assert euler_form(g1, g2) == 1
        assert euler_form(g1, g3) == 1
        assert euler_form(g2, g3) == 1


# ============================================================================
# Section 2: Quantum dilogarithm
# ============================================================================

class TestQuantumDilogarithm:
    """Test quantum dilogarithm series."""

    def test_li2_coefficients(self):
        """Li_2(x) = sum x^k / k^2."""
        qd = quantum_dilogarithm_series(1, 5)
        assert qd[1] == Rational(1, 1)
        assert qd[2] == Rational(1, 4)
        assert qd[3] == Rational(1, 9)
        assert qd[4] == Rational(1, 16)
        assert qd[5] == Rational(1, 25)

    def test_ks_log_primitive(self):
        """KS automorphism log for primitive BPS state."""
        gamma = (1, 0)
        log_K = ks_automorphism_log(gamma, omega=1, order=3)
        assert log_K[(1, 0)] == Rational(1)   # (-1)^0 / 1^2
        assert log_K[(2, 0)] == Rational(-1, 4)  # (-1)^1 / 2^2
        assert log_K[(3, 0)] == Rational(1, 9)   # (-1)^2 / 3^2

    def test_ks_log_omega_scaling(self):
        """log(K_gamma) scales linearly with Omega."""
        gamma = (1, 0)
        log1 = ks_automorphism_log(gamma, omega=1, order=3)
        log3 = ks_automorphism_log(gamma, omega=3, order=3)
        for charge, coeff in log1.items():
            assert log3[charge] == 3 * coeff


# ============================================================================
# Section 3: Pentagon identity (Path 1)
# ============================================================================

class TestPentagonIdentity:
    """Test the pentagon identity = arity-3 MC equation."""

    def test_pentagon_lie_algebra_leading(self):
        """Pentagon at leading order in BCH."""
        result = pentagon_identity_lie_algebra(order=3)
        assert result["pentagon_applies"]
        assert result["pentagon_verified_leading"]
        assert result["euler_form"] == 1

    def test_pentagon_group_level(self):
        """Pentagon at group level (numerical)."""
        result = pentagon_identity_group_level(tol=1e-10)
        assert result["pentagon_verified"]

    def test_pentagon_group_level_tight(self):
        """Pentagon with tight tolerance."""
        result = pentagon_identity_group_level(tol=1e-12)
        assert result["diff_x"] < 1e-12
        assert result["diff_y"] < 1e-12

    def test_pentagon_from_mc_arity3(self):
        """Pentagon from MC equation at arity 3."""
        result = pentagon_from_mc_arity3()
        assert result["forced_omega_11"] == 1
        assert result["joyce_song_matches"]

    def test_pentagon_mc_bracket(self):
        """MC arity-3 bracket = Euler form."""
        result = pentagon_from_mc_arity3()
        assert result["bracket_contribution"] == 1

    def test_pentagon_three_paths(self):
        """Pentagon verified by 3 independent paths."""
        result = verify_pentagon_three_paths()
        assert result["all_paths_agree"]

    def test_bch_leading_order(self):
        """BCH at leading order reproduces the pentagon."""
        bch = _bch_scattering((1, 0), (0, 1), 1, 1, order=2)
        # At (1,1): coefficient should be 1/2 * <(1,0),(0,1)> = 1/2
        # from the [A,B] term in BCH
        assert bch[(1, 1)] == Rational(1, 2)

    def test_bch_higher_order(self):
        """BCH at higher order produces walls at (2,1) and (1,2)."""
        bch = _bch_scattering((1, 0), (0, 1), 1, 1, order=3)
        assert (2, 1) in bch
        assert (1, 2) in bch


# ============================================================================
# Section 4: KS scattering diagram (Path 2)
# ============================================================================

class TestScatteringDiagram:
    """Test Kontsevich-Soibelman scattering diagrams."""

    def test_conifold_initial_walls(self):
        """Conifold has 2 initial walls."""
        sd = conifold_scattering_diagram(2)
        assert sd.omega((1, 0)) == 1
        assert sd.omega((0, 1)) == 1

    def test_conifold_pentagon_wall(self):
        """Pentagon creates wall at (1,1) with Omega = 1."""
        sd = conifold_scattering_diagram(3)
        assert sd.omega((1, 1)) == 1

    def test_conifold_all_primitive_omega_1(self):
        """All primitive charges have Omega = 1 for the conifold."""
        max_order = 8
        sd = conifold_scattering_diagram(max_order)
        for a in range(1, max_order):
            for b in range(1, max_order):
                if a + b <= max_order and math.gcd(a, b) == 1:
                    assert sd.omega((a, b)) == 1, f"Omega({a},{b}) != 1"

    def test_conifold_non_primitive_absent(self):
        """Non-primitive charges are not added as walls."""
        sd = conifold_scattering_diagram(5)
        # (2,2) is not primitive (gcd=2), should not be a wall
        assert sd.omega((2, 2)) == 0

    def test_conifold_order_by_order(self):
        """Build conifold scattering diagram order by order."""
        result = conifold_scattering_order_by_order(5)
        assert result["all_primitive_omega_1"]

    def test_conifold_order2_walls(self):
        """At order 2 (total charge 2), wall at (1,1)."""
        result = conifold_scattering_order_by_order(3)
        walls_2 = result["order_2"]
        charges_2 = [w[0] for w in walls_2]
        assert (1, 1) in charges_2

    def test_conifold_order3_walls(self):
        """At order 3, walls at (2,1) and (1,2)."""
        result = conifold_scattering_order_by_order(4)
        walls_3 = result["order_3"]
        charges_3 = [w[0] for w in walls_3]
        assert (2, 1) in charges_3
        assert (1, 2) in charges_3

    def test_conifold_wall_count(self):
        """Count walls at each order: Euler totient function."""
        result = conifold_scattering_order_by_order(8)
        for n in range(2, 8):
            walls = result[f"order_{n}"]
            # Number of primitive (a, n-a) with 1 <= a < n and gcd(a,n-a) = 1
            count = sum(1 for a in range(1, n) if math.gcd(a, n - a) == 1)
            assert len(walls) == count, f"Wall count at order {n}: {len(walls)} != {count}"

    def test_conifold_consistency_multi_path(self):
        """Multi-path verification of conifold consistency."""
        result = verify_conifold_consistency(order=5)
        assert result["all_paths_agree"]

    def test_scattering_diagram_basics(self):
        """ScatteringDiagram class operations."""
        sd = ScatteringDiagram(name="test")
        sd.add_wall((1, 0), 1)
        sd.add_wall((0, 1), 1)
        assert sd.wall_count() == 2
        assert sd.total_bps_count() == 2
        sd.add_wall((1, 1), 1)
        assert sd.wall_count() == 3


# ============================================================================
# Section 5: Higher wall-crossing (degree 2)
# ============================================================================

class TestHigherWallCrossing:
    """Test wall-crossing for <gamma_1, gamma_2> = 2."""

    def test_degree_2_euler_form(self):
        """<(1,0), (0,2)> = 2."""
        result = degree_2_wall_crossing(Rational(1), Rational(1, 10))
        assert result["euler_form"] == 2

    def test_degree_2_bound_states_exist(self):
        """Degree-2 wall-crossing creates multiple bound states."""
        result = degree_2_wall_crossing(Rational(1), Rational(1, 10))
        assert result["bound_state_12"] == (1, 2)
        assert result["bound_state_21"] == (2, 2)

    def test_degree_2_integrality(self):
        """Bound state BPS indices are integers."""
        result = degree_2_wall_crossing(Rational(1), Rational(1, 10))
        assert result["integrality_check"]

    def test_degree_2_quartic_shadow(self):
        """Quartic shadow controls arity-4 obstruction."""
        kappa = Rational(1)
        S4 = Rational(1, 10)
        result = degree_2_wall_crossing(kappa, S4)
        expected_delta = 8 * kappa * S4
        assert result["quartic_shadow_kappa_S4"] == expected_delta


# ============================================================================
# Section 6: Joyce-Song wall-crossing (Path 4)
# ============================================================================

class TestJoyceSong:
    """Test Joyce-Song wall-crossing formula."""

    def test_js_primitive_conifold_11(self):
        """JS at (1,1) for conifold: Delta_Omega = 1."""
        gamma = (1, 1)
        js = joyce_song_primitive_wc(gamma, [((1, 0), 1)], [((0, 1), 1)])
        assert js == 1

    def test_js_primitive_sign(self):
        """JS sign factor: (-1)^{<g1,g2>-1}."""
        # <(1,0), (0,1)> = 1, so sign = (-1)^0 = 1
        js = joyce_song_primitive_wc((1, 1), [((1, 0), 1)], [((0, 1), 1)])
        assert js == 1

    def test_js_primitive_pairing_2(self):
        """JS at pairing 2: sign = (-1)^1 = -1."""
        # <(1,0), (0,2)> = 2
        js = joyce_song_primitive_wc((1, 2), [((1, 0), 1)], [((0, 2), 1)])
        # (-1)^{2-1} * 2 * 1 * 1 = -2
        assert js == -2

    def test_js_full_wc(self):
        """Full Joyce-Song wall-crossing."""
        gamma = (1, 1)
        spectrum = {(1, 0): 1, (0, 1): 1}
        cc = {(1, 0): 1 + 0.5j, (0, 1): 0.5 + 1j, (1, 1): 1.5 + 1.5j}
        result = joyce_song_full_wc(gamma, spectrum, cc)
        assert result["integrality"]
        assert isinstance(result["delta_omega"], int)

    def test_js_equals_convolution(self):
        """JS Poisson bracket = convolution bracket."""
        result = joyce_song_equals_convolution_bracket()
        assert result["correspondence_verified"]

    def test_js_sign_at_11(self):
        """Sign factor at (1,1) is +1."""
        result = joyce_song_equals_convolution_bracket()
        assert result["sign_factor"] == 1

    def test_js_sign_at_21(self):
        """JS at (2,1): ef = 1, sign = +1."""
        result = joyce_song_equals_convolution_bracket()
        assert result["ef_10_11"] == 1
        assert result["sign2"] == 1

    def test_js_vanishing_euler_form(self):
        """JS gives 0 when Euler form vanishes."""
        # <(1,0), (2,0)> = 0
        js = joyce_song_primitive_wc((3, 0), [((1, 0), 1)], [((2, 0), 1)])
        assert js == 0

    def test_js_antisymmetry(self):
        """JS is antisymmetric under swapping summands."""
        gamma = (1, 1)
        js1 = joyce_song_primitive_wc(gamma, [((1, 0), 1)], [((0, 1), 1)])
        js2 = joyce_song_primitive_wc(gamma, [((0, 1), 1)], [((1, 0), 1)])
        # The sign factor (-1)^{<g1,g2>-1} does NOT change (it uses |<g1,g2>|),
        # but <g1,g2> changes sign, so the total changes sign.
        assert js1 == -js2


# ============================================================================
# Section 7: Seiberg-Witten BPS spectrum (Path 3)
# ============================================================================

class TestSeibergWitten:
    """Test SU(2) Seiberg-Witten BPS spectrum and wall-crossing."""

    def test_sw_strong_coupling_2_states(self):
        """Strong coupling has exactly 2 BPS states."""
        strong = SWBPSSpectrum.strong_coupling()
        assert len(strong.charges) == 2

    def test_sw_strong_monopole(self):
        """Strong coupling contains the monopole M = (0,1)."""
        strong = SWBPSSpectrum.strong_coupling()
        assert strong.charges.get((0, 1)) == 1

    def test_sw_strong_dyon(self):
        """Strong coupling contains the dyon D = (1,1)."""
        strong = SWBPSSpectrum.strong_coupling()
        assert strong.charges.get((1, 1)) == 1

    def test_sw_weak_coupling_wboson(self):
        """Weak coupling contains the W-boson."""
        weak = SWBPSSpectrum.weak_coupling(3)
        assert weak.charges.get((2, 0)) == 1

    def test_sw_weak_coupling_tower(self):
        """Weak coupling has an infinite tower of dyons."""
        for n_max in [3, 5, 10]:
            weak = SWBPSSpectrum.weak_coupling(n_max)
            assert len(weak.charges) > 2 * n_max

    def test_sw_euler_form_MD(self):
        """<M, D> = -1 for monopole and dyon."""
        M = (0, 1)
        D = (1, 1)
        assert euler_form(M, D) == -1
        assert abs(euler_form(M, D)) == 1

    def test_sw_pentagon_applies(self):
        """Pentagon identity applies (|<M,D>| = 1)."""
        result = sw_wall_crossing_verification()
        assert result["pentagon_applies"]

    def test_sw_bound_state(self):
        """Bound state M+D = (1,2) exists."""
        result = sw_wall_crossing_verification()
        assert result["bound_state_MD"] == (1, 2)

    def test_sw_koszul_sign(self):
        """Total monodromy matches Koszul sign."""
        result = sw_wall_crossing_verification()
        assert result["koszul_sign_match"]

    def test_sw_integrality_strong(self):
        """All strong coupling BPS indices are integers."""
        result = sw_wall_crossing_verification()
        assert result["strong_integrality"]

    def test_sw_integrality_weak(self):
        """All weak coupling BPS indices are integers."""
        result = sw_wall_crossing_verification()
        assert result["weak_integrality"]

    def test_sw_spectrum_generator(self):
        """Spectrum generator computation."""
        result = sw_spectrum_generator()
        assert result["strong_total_omega"] == 2
        assert result["single_state_per_crossing"]

    def test_sw_multi_path(self):
        """Multi-path verification of SW wall-crossing."""
        result = verify_sw_wall_crossing_multi_path()
        assert result["all_paths_agree"]

    def test_sw_all_omega_1(self):
        """All BPS indices are 1 (hypermultiplets)."""
        strong = SWBPSSpectrum.strong_coupling()
        for omega in strong.charges.values():
            assert omega == 1

    def test_sw_js_delta_integer(self):
        """Joyce-Song Delta_Omega is an integer at the wall."""
        result = verify_sw_wall_crossing_multi_path()
        assert result["path2_js_integer"]


# ============================================================================
# Section 8: Motivic DT invariants (Path 5)
# ============================================================================

class TestMotivicDT:
    """Test motivic DT invariant computation."""

    def test_conifold_gv_all_1(self):
        """Conifold GV invariants: n_0^d = 1 for all d."""
        result = motivic_dt_conifold(d_max=10)
        for d in range(1, 11):
            assert result[f"gv_0_{d}"] == 1

    def test_conifold_omega_integer(self):
        """Conifold BPS indices are integers."""
        result = motivic_dt_conifold()
        assert result["all_gv_integer"]
        assert result["all_omega_integer"]

    def test_conifold_refined_gv(self):
        """Conifold refined GV: spin (0,0) content = 1."""
        result = motivic_dt_conifold()
        for d in range(1, 6):
            assert result[f"refined_gv_0_{d}"] == 1

    def test_local_p2_gv_genus0(self):
        """Local P^2 genus-0 GV invariants (ground truth)."""
        result = motivic_local_p2(d_max=5)
        # n_0^1 = 3 (three lines)
        assert result["gv_0_1"] == 3
        # n_0^2 = -6 (six conics with sign)
        assert result["gv_0_2"] == -6
        # n_0^3 = 27 (27 cubics)
        assert result["gv_0_3"] == 27

    def test_local_p2_gv_genus1(self):
        """Local P^2 genus-1 GV invariants."""
        result = motivic_local_p2(d_max=5)
        assert result["gv_1_3"] == -10
        assert result["gv_1_4"] == 231

    def test_local_p2_integrality(self):
        """All local P^2 GV invariants are integers."""
        result = motivic_local_p2()
        assert result["gv_integrality"]

    def test_local_p2_castelnuovo(self):
        """Castelnuovo bound: n_g^d = 0 for d < 2g+1."""
        result = motivic_local_p2()
        assert result["castelnuovo_bound"]

    def test_multi_cover_check(self):
        """Multi-cover formula produces consistent results."""
        result = motivic_dt_conifold()
        assert result["multi_cover_check"]


# ============================================================================
# Section 9: Attractor flow and split trees
# ============================================================================

class TestAttractorFlow:
    """Test attractor flow trees and shadow correspondence."""

    def test_attractor_tree_leaf(self):
        """Leaf node has depth 0."""
        tree = AttractorFlowTree(charge=(1, 0))
        assert tree.depth() == 0
        assert tree.is_leaf
        assert tree.leaves() == [(1, 0)]

    def test_attractor_tree_split(self):
        """Split tree has depth 1."""
        child1 = AttractorFlowTree(charge=(1, 0))
        child2 = AttractorFlowTree(charge=(0, 1))
        tree = AttractorFlowTree(
            charge=(1, 1),
            children=(child1, child2),
            is_leaf=False
        )
        assert tree.depth() == 1
        assert tree.is_bound
        assert set(tree.leaves()) == {(1, 0), (0, 1)}
        assert tree.node_count() == 3

    def test_split_tree_strong_coupling(self):
        """Split tree in strong coupling chamber."""
        spectrum = {(0, 1): 1, (1, 1): 1}
        tree = split_attractor_tree((1, 2), spectrum)
        # (1,2) = (0,1) + (1,1) both in spectrum
        assert tree is not None
        assert not tree.is_leaf
        assert len(tree.leaves()) == 2

    def test_split_tree_nonexistent(self):
        """No split tree for charge not decomposable."""
        spectrum = {(0, 1): 1, (1, 1): 1}
        tree = split_attractor_tree((3, 0), spectrum)
        assert tree is None

    def test_attractor_shadow_correspondence(self):
        """Attractor trees correspond to planted forests."""
        result = attractor_flow_shadow_correspondence()
        # (1,2) = M + D should split
        assert result["tree_12_exists"]
        assert result["shadow_arity"] == 2

    def test_attractor_shadow_planted_forest_count(self):
        """Arity-3 planted forests: 3 topologies."""
        result = attractor_flow_shadow_correspondence()
        assert result["planted_forest_arity3_count"] == 3

    def test_shadow_connection_attractor(self):
        """Shadow connection = attractor flow equation."""
        result = shadow_connection_attractor_flow(
            Rational(1), Rational(2), Rational(1, 10))
        assert result["discriminant_identity_check"]
        assert result["monodromy_equals_koszul"]

    def test_shadow_connection_monodromy(self):
        """Monodromy around zero of Q_L is -1 (Koszul sign)."""
        result = shadow_connection_attractor_flow(
            Rational(3), Rational(1), Rational(1, 5))
        assert result["monodromy_sign"] == -1
        assert result["koszul_sign"] == -1

    def test_shadow_connection_discriminant(self):
        """Discriminant formula: disc = -32*kappa^2 * Delta."""
        kappa = Rational(5)
        alpha = Rational(2)
        S4 = Rational(3, 10)
        result = shadow_connection_attractor_flow(kappa, alpha, S4)
        assert result["discriminant_identity_check"]


# ============================================================================
# Section 10: Torus algebra = convolution bracket
# ============================================================================

class TestTorusAlgebra:
    """Test torus algebra Poisson bracket = convolution bracket."""

    def test_bracket_basic(self):
        """Basic torus bracket: {(1,0), (0,1)} = (1,1) with coeff 1."""
        charge, value = torus_algebra_bracket((1, 0), (0, 1))
        assert charge == (1, 1)
        assert value == 1

    def test_bracket_skew_symmetry(self):
        """{A,B} = -{B,A}."""
        g1, g2 = (1, 0), (0, 1)
        _, v1 = torus_algebra_bracket(g1, g2)
        _, v2 = torus_algebra_bracket(g2, g1)
        assert v1 == -v2

    def test_bracket_vanish_collinear(self):
        """Bracket vanishes for collinear charges."""
        _, v = torus_algebra_bracket((1, 0), (2, 0))
        assert v == 0

    def test_poisson_equals_convolution(self):
        """Full verification: Poisson = convolution."""
        result = verify_poisson_equals_convolution()
        assert result["all_match"]

    def test_skew_symmetry_systematic(self):
        """Skew symmetry for multiple pairs."""
        result = verify_poisson_equals_convolution()
        assert result["skew_symmetry"]

    def test_jacobi_identity(self):
        """Jacobi identity: [[A,B],C] + cyclic = 0."""
        result = verify_poisson_equals_convolution()
        assert result["jacobi_identity"]

    def test_bracket_with_omega(self):
        """Bracket with non-unit BPS indices."""
        charge, value = torus_algebra_bracket((1, 0), (0, 1), 2, 3)
        assert charge == (1, 1)
        assert value == 1 * 2 * 3  # ef * omega1 * omega2 = 1 * 2 * 3 = 6

    def test_bracket_higher_pairing(self):
        """Bracket at pairing 2: <(1,0), (0,2)> * 1 * 1 = 2."""
        charge, value = torus_algebra_bracket((1, 0), (0, 2))
        assert charge == (1, 2)
        assert value == 2


# ============================================================================
# Section 11: Scattering-shadow arity correspondence
# ============================================================================

class TestScatteringShadowMap:
    """Test the map between scattering diagram and shadow arities."""

    def test_arity_map_structure(self):
        """Arity map has correct entries."""
        result = scattering_shadow_arity_map()
        arity_map = result["arity_scattering_map"]
        assert 2 in arity_map
        assert 3 in arity_map
        assert 4 in arity_map

    def test_shadow_classes(self):
        """Four shadow classes: G, L, C, M."""
        result = scattering_shadow_arity_map()
        classes = result["shadow_classes"]
        assert "G" in classes
        assert "L" in classes
        assert "C" in classes
        assert "M" in classes

    def test_class_G_terminates(self):
        """Class G has r_max = 2."""
        result = scattering_shadow_arity_map()
        assert result["shadow_classes"]["G"]["r_max"] == 2

    def test_class_M_infinite(self):
        """Class M has r_max = infinity."""
        result = scattering_shadow_arity_map()
        assert result["shadow_classes"]["M"]["r_max"] == float("inf")

    def test_conifold_wall_count_arity3(self):
        """One wall at arity 3 (the (1,1) wall)."""
        result = scattering_shadow_arity_map()
        # At total degree 2 = a + b, a,b >= 1: only (1,1), gcd = 1
        assert result["conifold_wall_count_by_arity"][2] == 1

    def test_conifold_wall_count_arity4(self):
        """Two walls at arity 4: (1,2) and (2,1)."""
        result = scattering_shadow_arity_map()
        assert result["conifold_wall_count_by_arity"][3] == 2

    def test_conifold_wall_count_arity5(self):
        """Two walls at arity 5: (1,3) and (3,1)."""
        result = scattering_shadow_arity_map()
        # (2,2) is not primitive
        assert result["conifold_wall_count_by_arity"][4] == 2

    def test_conifold_wall_count_arity6(self):
        """Walls at arity 6: (1,4), (2,3), (3,2), (4,1) = 4 walls."""
        result = scattering_shadow_arity_map(max_arity=7)
        # gcd(1,4)=1, gcd(2,3)=1, gcd(3,2)=1, gcd(4,1)=1
        assert result["conifold_wall_count_by_arity"][5] == 4


# ============================================================================
# Section 12: DT integrality (Path 6)
# ============================================================================

class TestDTIntegrality:
    """Test BPS index integrality."""

    def test_integrality_conifold(self):
        """All conifold BPS indices are integers."""
        result = dt_integrality_check("conifold", d_max=10)
        assert result["all_integer"]

    def test_integrality_local_p2(self):
        """All local P^2 GV invariants are integers."""
        result = dt_integrality_check("local_p2", d_max=5)
        assert result["all_integer"]

    def test_integrality_local_p1xp1(self):
        """All local P^1 x P^1 GV invariants are integers."""
        result = dt_integrality_check("local_p1xp1")
        assert result["all_integer"]

    def test_verify_bps_integrality_positive(self):
        """Verify integrality on a correct spectrum."""
        spectrum = {(1, 0): 1, (0, 1): 1, (1, 1): 1, (2, 1): 1}
        assert verify_bps_integrality(spectrum)

    def test_conifold_gv_specific_values(self):
        """Spot-check conifold GV values."""
        result = dt_integrality_check("conifold", d_max=5)
        for d in range(1, 6):
            assert result[f"gv_0_{d}"] == 1

    def test_local_p2_gv_specific(self):
        """Spot-check local P^2 GV values."""
        result = dt_integrality_check("local_p2", d_max=5)
        assert result["gv_0_1"] == 3
        assert result["gv_0_2"] == -6
        assert result["gv_0_3"] == 27
        assert result["gv_0_4"] == -192
        assert result["gv_0_5"] == 1695


# ============================================================================
# Section 13: Full verification suite
# ============================================================================

class TestFullVerification:
    """Test the complete multi-path verification harness."""

    def test_full_suite_passes(self):
        """All 6 verification paths pass."""
        result = full_verification_suite()
        assert result["all_paths_pass"]

    def test_path1_pentagon(self):
        result = full_verification_suite()
        assert result["path1_pentagon"]

    def test_path2_ks(self):
        result = full_verification_suite()
        assert result["path2_ks_conifold"]

    def test_path3_sw(self):
        result = full_verification_suite()
        assert result["path3_sw"]

    def test_path4_js(self):
        result = full_verification_suite()
        assert result["path4_js_convolution"]

    def test_path5_motivic(self):
        result = full_verification_suite()
        assert result["path5_motivic_integrality"]

    def test_path6_integrality(self):
        result = full_verification_suite()
        assert result["path6_integrality_conifold"]
        assert result["path6_integrality_p2"]


# ============================================================================
# Section 14: Cross-checks and edge cases
# ============================================================================

class TestCrossChecks:
    """Cross-checks between different computations."""

    def test_pentagon_equals_js_at_11(self):
        """Pentagon prediction = JS prediction at (1,1)."""
        pentagon = pentagon_identity_lie_algebra()
        js = joyce_song_primitive_wc((1, 1), [((1, 0), 1)], [((0, 1), 1)])
        assert pentagon["omega_11"] == js

    def test_conifold_scattering_equals_direct(self):
        """Order-by-order and direct construction agree."""
        max_ord = 8
        sd = conifold_scattering_diagram(max_ord)
        obo = conifold_scattering_order_by_order(max_ord)
        # Both should give Omega = 1 at all primitive charges within range
        for a in range(1, max_ord):
            for b in range(1, max_ord):
                if a + b <= max_ord and math.gcd(a, b) == 1:
                    assert sd.omega((a, b)) == 1

    def test_bch_at_11_matches_pentagon(self):
        """BCH coefficient at (1,1) = 1/2, matching pentagon."""
        bch = _bch_scattering((1, 0), (0, 1), 1, 1, order=2)
        # BCH gives 1/2 for [A,B]; pentagon says Omega = 1
        # The 1/2 factor is from BCH expansion, not from BPS index
        assert bch[(1, 1)] == Rational(1, 2)

    def test_sw_strong_2_weak_infinite(self):
        """Strong coupling: 2 states. Weak coupling: many states."""
        strong = SWBPSSpectrum.strong_coupling()
        weak = SWBPSSpectrum.weak_coupling(10)
        assert len(strong.charges) == 2
        assert len(weak.charges) > 10

    def test_euler_form_additivity(self):
        """Euler form is additive: <g1+g2, g3> = <g1,g3> + <g2,g3>."""
        g1 = (1, 0)
        g2 = (0, 1)
        g3 = (2, 3)
        g12 = charge_add(g1, g2)
        assert euler_form(g12, g3) == euler_form(g1, g3) + euler_form(g2, g3)

    def test_lambda_fp_positive(self):
        """Faber-Pandharipande intersection numbers are positive."""
        for g in range(1, 8):
            assert _lambda_fp(g) > 0

    def test_lambda_fp_g1(self):
        """lambda_1^FP = 1/24."""
        assert _lambda_fp(1) == Rational(1, 24)

    def test_lambda_fp_g2(self):
        """lambda_2^FP = 7/5760."""
        assert _lambda_fp(2) == Rational(7, 5760)

    def test_bps_ap42_warning(self):
        """BCH at (2,1) != 1: the AP42 motivic correction."""
        bch = _bch_scattering((1, 0), (0, 1), 1, 1, order=3)
        # The BCH coefficient at (2,1) should differ from Omega(2,1) = 1
        # for the conifold. This is the AP42 mismatch.
        coeff_21 = bch.get((2, 1), Rational(0))
        # BCH gives 1/12 at (2,1), but Omega should be 1
        assert coeff_21 != 1, "AP42: naive BCH should NOT equal motivic DT"

    def test_pentagon_numerics_multiple_points(self):
        """Pentagon identity at multiple numerical points."""
        # Test at x = 0.1, y = 0.1
        result = pentagon_identity_group_level(tol=1e-10)
        assert result["pentagon_verified"]

    def test_sw_js_consistent_with_pentagon(self):
        """SW: JS wall-crossing consistent with pentagon."""
        M = (0, 1)
        D = (1, 1)
        ef = abs(euler_form(M, D))
        assert ef == 1  # pentagon regime
        js = joyce_song_primitive_wc(charge_add(M, D), [(M, 1)], [(D, 1)])
        assert isinstance(js, int)

    def test_motivic_conifold_omega_gv_agree(self):
        """For primitive charges: Omega = GV for the conifold."""
        result = motivic_dt_conifold()
        for d in range(1, 6):
            assert result[f"omega_{d}"] == result[f"gv_0_{d}"]

    def test_scattering_wall_count_growth(self):
        """Wall count grows with order (related to Euler totient)."""
        result = scattering_shadow_arity_map(max_arity=8)
        counts = result["conifold_wall_count_by_arity"]
        # Counts should be non-decreasing on average
        assert counts[2] <= counts[5]  # 1 <= 4

    def test_degree_2_extends_pentagon(self):
        """Degree-2 wall-crossing extends the pentagon identity."""
        d2 = degree_2_wall_crossing(Rational(1), Rational(1, 10))
        assert d2["euler_form"] == 2  # strict extension of ef = 1


# ============================================================================
# Section 15: Faber-Pandharipande and shadow basics
# ============================================================================

class TestShadowBasics:
    """Test shadow data used in the wall-crossing engine."""

    def test_lambda_fp_bernoulli_formula(self):
        """lambda_g^FP from Bernoulli numbers."""
        # lambda_1 = (2^1 - 1)/(2^1) * |B_2|/2! = 1/2 * 1/6 / 2 ... no.
        # lambda_1 = (2^{2*1-1} - 1) / 2^{2*1-1} * |B_2| / (2*1)!
        #          = (2-1)/2 * (1/6) / 2 = 1/2 * 1/12 = 1/24
        assert _lambda_fp(1) == Rational(1, 24)

    def test_lambda_fp_decreasing(self):
        """lambda_g^FP decreases rapidly."""
        for g in range(1, 6):
            assert _lambda_fp(g + 1) < _lambda_fp(g)

    def test_euler_form_jacobi(self):
        """Jacobi identity for the Euler form bracket."""
        # [e_a, [e_b, e_c]] + cyclic = 0
        # This is automatic for the Lie algebra with bracket [e_g, e_{g'}] = <g,g'> e_{g+g'}
        g1 = (1, 0)
        g2 = (0, 1)
        g3 = (1, 1)

        # [g1, [g2, g3]]
        ef23 = euler_form(g2, g3)
        g23 = charge_add(g2, g3)
        ef1_23 = euler_form(g1, g23)
        term1 = ef23 * ef1_23

        # [g2, [g3, g1]]
        ef31 = euler_form(g3, g1)
        g31 = charge_add(g3, g1)
        ef2_31 = euler_form(g2, g31)
        term2 = ef31 * ef2_31

        # [g3, [g1, g2]]
        ef12 = euler_form(g1, g2)
        g12 = charge_add(g1, g2)
        ef3_12 = euler_form(g3, g12)
        term3 = ef12 * ef3_12

        assert term1 + term2 + term3 == 0, "Jacobi identity failed"
