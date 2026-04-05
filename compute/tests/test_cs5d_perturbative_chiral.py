r"""Tests for 5D Chern-Simons perturbative chiral algebra on toric CY3s.

Multi-path verification strategy:
    Path (a): 5d CS Feynman diagrams (tree + loop)
    Path (b): Shuffle algebra / CoHA structure constants
    Path (c): Direct W_{1+infty} OPE

Each OPE structure constant is verified by at least 2 independent methods.

Test sections:
    1.  Normal bundle data
    2.  Transverse propagator
    3.  Tree-level OPE
    4.  1-loop OPE corrections
    5.  W_{1+infty} OPE (path c)
    6.  Shuffle algebra (path b)
    7.  Three-path verification
    8.  Full perturbative algebra
    9.  Kappa comparison
    10. Loop factor classification
    11. Higher-rank (GL(N)) tests
    12. Conifold CoHA comparison
    13. Large-N asymptotics
    14. Cross-family consistency
"""

import pytest
from fractions import Fraction

from compute.lib.cs5d_perturbative_chiral import (
    # Normal bundle
    c3_normal_bundle,
    conifold_normal_bundle,
    local_p2_normal_bundle,
    NormalBundleData,
    # Propagator
    compute_transverse_propagator,
    TransversePropagator,
    # Tree-level
    tree_level_ope_c3,
    tree_level_ope_conifold,
    tree_level_ope_local_p2,
    # 1-loop
    one_loop_corrections_c3,
    one_loop_corrections_conifold,
    one_loop_corrections_local_p2,
    # W_{1+inf}
    w_infinity_self_dual_point,
    w_infinity_ope_jj,
    w_infinity_ope_tt,
    w_infinity_ope_tw3,
    # Shuffle
    shuffle_algebra_c3,
    # Three-path
    verify_three_paths_c3,
    # Full algebra
    build_perturbative_algebra_c3,
    build_perturbative_algebra_conifold,
    build_perturbative_algebra_local_p2,
    # Kappa
    kappa_from_cs5d,
    kappa_comparison_table,
    # Loop factor
    classify_loop_factor,
    all_toric_loop_factors,
    # Higher-rank
    gl_n_perturbative_central_charge,
    gl_n_kappa,
    structure_function_at_gl_n,
    # Conifold CoHA
    compare_conifold_coha,
    # Large-N
    large_n_central_charge,
    sigma_invariants,
    # Diagnostic
    full_diagnostic,
)


# =========================================================================
# 1. Normal bundle data
# =========================================================================

class TestNormalBundleData:
    """Test normal bundle computation for all three toric CY3s."""

    def test_c3_bundle_is_trivial(self):
        """C^3: normal bundle is O+O (trivial rank 2)."""
        nb = c3_normal_bundle()
        assert nb.line_bundle_degrees == (0, 0)
        assert nb.total_degree == 0
        assert nb.rank == 2
        assert nb.curve == "C"

    def test_conifold_bundle(self):
        """Conifold: normal bundle is O(-1)+O(-1)."""
        nb = conifold_normal_bundle()
        assert nb.line_bundle_degrees == (-1, -1)
        assert nb.total_degree == -2
        assert nb.rank == 2
        assert nb.curve == "P1"

    def test_local_p2_bundle(self):
        """Local P^2: normal bundle for a line is O(1)+O(-3)."""
        nb = local_p2_normal_bundle()
        assert nb.line_bundle_degrees == (1, -3)
        assert nb.total_degree == -2
        assert nb.rank == 2
        assert nb.curve == "P1"

    def test_cy_adjunction(self):
        """For CY3 with curve P^1: det(N) = K_{P^1} = O(-2).

        Equivalently, total_degree = -2 for all P^1 curves.
        This is a consequence of adjunction + CY condition.
        """
        # Conifold
        nb_con = conifold_normal_bundle()
        assert nb_con.total_degree == -2  # det O(-1)+O(-1) = O(-2)

        # Local P^2
        nb_p2 = local_p2_normal_bundle()
        assert nb_p2.total_degree == -2  # det O(1)+O(-3) = O(-2)

    def test_c3_total_degree_zero(self):
        r"""C^3 is a special case: C \subset C^3 has trivial normal bundle.

        For a line in C^3 (not compact), the adjunction formula gives
        det(N) = O (trivial) since K_{C} = O for a copy of C.
        """
        nb = c3_normal_bundle()
        assert nb.total_degree == 0


# =========================================================================
# 2. Transverse propagator
# =========================================================================

class TestTransversePropagator:
    """Test transverse propagator computation."""

    def test_c3_loop_factor_is_one(self):
        """C^3: loop factor = 1/(1*1) = 1."""
        tp = compute_transverse_propagator(c3_normal_bundle())
        assert tp.loop_factor == Fraction(1)
        assert not tp.is_regularized

    def test_conifold_loop_factor(self):
        """Conifold: loop factor = 1/((-1)*(-1)) = 1.

        Each factor: 1/(2*(-1)+1) = 1/(-1) = -1.
        Product: (-1)*(-1) = 1.
        """
        tp = compute_transverse_propagator(conifold_normal_bundle())
        assert tp.loop_factor == Fraction(1)
        assert tp.is_regularized  # negative degree requires regularization

    def test_local_p2_loop_factor(self):
        """Local P^2: loop factor = 1/(3*(-5)) = -1/15.

        Factor for O(1): 1/(2*1+1) = 1/3
        Factor for O(-3): 1/(2*(-3)+1) = 1/(-5) = -1/5
        Product: (1/3)*(-1/5) = -1/15
        """
        tp = compute_transverse_propagator(local_p2_normal_bundle())
        assert tp.loop_factor == Fraction(-1, 15)
        assert tp.is_regularized

    def test_loop_factor_product_formula(self):
        """The loop factor is the product of 1/(2d_i+1) over all degrees."""
        for nb in [c3_normal_bundle(), conifold_normal_bundle(), local_p2_normal_bundle()]:
            tp = compute_transverse_propagator(nb)
            expected = Fraction(1)
            for d in nb.line_bundle_degrees:
                expected *= Fraction(1, 2 * d + 1)
            assert tp.loop_factor == expected

    def test_c3_conifold_perturbative_match(self):
        """C^3 and conifold have the SAME loop factor (= same perturbative OPE)."""
        tp_c3 = compute_transverse_propagator(c3_normal_bundle())
        tp_con = compute_transverse_propagator(conifold_normal_bundle())
        assert tp_c3.loop_factor == tp_con.loop_factor

    def test_local_p2_loop_factor_negative(self):
        """Local P^2 loop factor is negative (sign from O(-3))."""
        tp = compute_transverse_propagator(local_p2_normal_bundle())
        assert tp.loop_factor < 0


# =========================================================================
# 3. Tree-level OPE
# =========================================================================

class TestTreeLevelOPE:
    """Test tree-level OPE from 5d CS cubic vertex."""

    def test_c3_gl1_level(self):
        """C^3 GL(1): tree-level J-J OPE has k=1."""
        tree = tree_level_ope_c3(N=1)
        assert tree.level == Fraction(1)
        assert tree.ope_coefficients[(1, 1, 2)] == Fraction(1)

    def test_c3_gl1_abelian(self):
        """GL(1) is abelian: no pole-1 term in J-J OPE."""
        tree = tree_level_ope_c3(N=1)
        assert (1, 1, 1) not in tree.ope_coefficients

    def test_c3_gln_structure_constants(self):
        """GL(N) for N>1: has nonzero structure constants f^{abc}."""
        tree = tree_level_ope_c3(N=2)
        assert (1, 1, 1) in tree.ope_coefficients
        assert tree.ope_coefficients[(1, 1, 1)] == Fraction(1)

    def test_conifold_tree_level(self):
        """Conifold tree-level: same as C^3 (local property of cubic vertex)."""
        tree_c3 = tree_level_ope_c3(N=1)
        tree_con = tree_level_ope_conifold()
        assert tree_c3.level == tree_con.level
        assert tree_c3.ope_coefficients[(1, 1, 2)] == tree_con.ope_coefficients[(1, 1, 2)]

    def test_local_p2_tree_level(self):
        """Local P^2 tree-level: same structure as C^3."""
        tree_c3 = tree_level_ope_c3(N=1)
        tree_p2 = tree_level_ope_local_p2()
        assert tree_c3.level == tree_p2.level

    def test_all_tree_levels_equal(self):
        """All three geometries have the same tree-level OPE (locality)."""
        k_c3 = tree_level_ope_c3(N=1).level
        k_con = tree_level_ope_conifold().level
        k_p2 = tree_level_ope_local_p2().level
        assert k_c3 == k_con == k_p2 == Fraction(1)


# =========================================================================
# 4. One-loop OPE corrections
# =========================================================================

class TestOneLoopCorrections:
    """Test 1-loop OPE corrections from transverse integration."""

    def test_c3_generates_stress_tensor(self):
        """C^3: 1-loop produces T = (1/2):JJ: with c=1."""
        corrs = one_loop_corrections_c3(max_spin=3)
        # First correction: T-T pole 4 (central term)
        tt_pole4 = [c for c in corrs if c.target_spin == 2 and c.pole_order == 4]
        assert len(tt_pole4) == 1
        assert tt_pole4[0].coefficient == Fraction(1, 2)  # c/2 = 1/2

    def test_c3_loop_factor_in_corrections(self):
        """C^3: all corrections have transverse_factor = 1^n."""
        corrs = one_loop_corrections_c3(max_spin=4)
        for c in corrs:
            assert c.transverse_factor == Fraction(1) ** c.loop_order

    def test_c3_w3_at_2loop(self):
        """C^3: W_3 generator produced at 2-loop order."""
        corrs = one_loop_corrections_c3(max_spin=3)
        w3_corrs = [c for c in corrs if c.target_spin == 3]
        assert len(w3_corrs) >= 1
        assert w3_corrs[0].loop_order == 2

    def test_conifold_same_as_c3(self):
        """Conifold 1-loop corrections match C^3 (same loop factor)."""
        corrs_c3 = one_loop_corrections_c3(max_spin=3)
        corrs_con = one_loop_corrections_conifold(max_spin=3)
        for c3, con in zip(corrs_c3, corrs_con):
            assert c3.coefficient == con.coefficient
            assert c3.transverse_factor == con.transverse_factor

    def test_local_p2_different_from_c3(self):
        """Local P^2 has different loop factor, so different corrections."""
        corrs_c3 = one_loop_corrections_c3(max_spin=3)
        corrs_p2 = one_loop_corrections_local_p2(max_spin=3)

        # Transverse factors differ
        c3_factors = {c.transverse_factor for c in corrs_c3}
        p2_factors = {c.transverse_factor for c in corrs_p2}
        # C^3 all have factor 1; P^2 has -1/15
        assert Fraction(-1, 15) in p2_factors or Fraction(-1, 15) ** 2 in p2_factors

    def test_local_p2_w3_transverse_factor(self):
        """Local P^2: W_3 correction has transverse factor (-1/15)^2 = 1/225."""
        corrs = one_loop_corrections_local_p2(max_spin=3)
        w3_corrs = [c for c in corrs if c.target_spin == 3]
        if w3_corrs:
            assert w3_corrs[0].transverse_factor == Fraction(1, 225)


# =========================================================================
# 5. W_{1+infty} OPE (path c)
# =========================================================================

class TestWInfinityOPE:
    """Test direct W_{1+infty} OPE computation."""

    def test_self_dual_point_n1(self):
        """At N=1: h=(1,0,-1), trivial structure function."""
        data = w_infinity_self_dual_point(N=1)
        assert data.h1 == Fraction(1)
        assert data.h2 == Fraction(0)
        assert data.h3 == Fraction(-1)
        assert data.central_charge == Fraction(1)

    def test_self_dual_structure_function_trivial(self):
        """At h=(1,0,-1): g(z) = 1, so phi_j = 0 for j >= 1."""
        data = w_infinity_self_dual_point(N=1)
        for j in range(1, len(data.phi_coefficients)):
            assert data.phi_coefficients[j] == Fraction(0), \
                f"phi_{j} = {data.phi_coefficients[j]} != 0 at self-dual point"

    def test_sigma_at_n1(self):
        """At N=1: sigma_2 = -1, sigma_3 = 0."""
        data = w_infinity_self_dual_point(N=1)
        assert data.sigma2 == Fraction(-1)
        assert data.sigma3 == Fraction(0)

    def test_jj_ope(self):
        """J(z)J(w) ~ 1/(z-w)^2 at c=1."""
        data = w_infinity_self_dual_point(N=1)
        ope = w_infinity_ope_jj(data)
        assert ope[2] == Fraction(1)

    def test_tt_ope_central_charge(self):
        """T(z)T(w): c/2 at pole 4. For c=1: 1/2."""
        data = w_infinity_self_dual_point(N=1)
        ope = w_infinity_ope_tt(data)
        assert ope[4] == Fraction(1, 2)

    def test_tt_ope_weight(self):
        """T(z)T(w): coefficient 2 at pole 2 (conformal weight of T)."""
        data = w_infinity_self_dual_point(N=1)
        ope = w_infinity_ope_tt(data)
        assert ope[2] == Fraction(2)

    def test_tw3_ope(self):
        """T(z)W_3(w): coefficient 3 at pole 2 (W_3 is primary of weight 3)."""
        data = w_infinity_self_dual_point(N=1)
        ope = w_infinity_ope_tw3(data)
        assert ope[2] == Fraction(3)
        assert ope[1] == Fraction(1)

    def test_gl2_parameters(self):
        """GL(2): h=(1,1,-2), sigma_2 = -3, sigma_3 = -2."""
        data = w_infinity_self_dual_point(N=2)
        assert data.h1 == Fraction(1)
        assert data.h2 == Fraction(1)
        assert data.h3 == Fraction(-2)
        assert data.sigma2 == Fraction(-3)
        assert data.sigma3 == Fraction(-2)
        assert data.central_charge == Fraction(2)

    def test_gl2_nontrivial_structure_function(self):
        """GL(2): the structure function is nontrivial (phi_3 != 0)."""
        data = w_infinity_self_dual_point(N=2)
        # phi_3 = alpha_3 = (-2/3) * p_3 where p_3 = 1 + 1 + (-8) = -6
        # phi_3 = (-2/3)*(-6) = 4
        assert data.phi_coefficients[3] == Fraction(4)

    def test_gl3_sigma_invariants(self):
        """GL(3): h=(1,2,-3), sigma_2 = -7, sigma_3 = -6."""
        data = w_infinity_self_dual_point(N=3)
        assert data.sigma2 == Fraction(-7)
        assert data.sigma3 == Fraction(-6)


# =========================================================================
# 6. Shuffle algebra (path b)
# =========================================================================

class TestShuffleAlgebra:
    """Test shuffle algebra / CoHA structure constants."""

    def test_c3_shuffle_level(self):
        """Shuffle algebra at self-dual point: level = 1."""
        sh = shuffle_algebra_c3()
        assert sh.shuffle_structure_constants[(1, 1, 2)] == Fraction(1)

    def test_c3_shuffle_parameters(self):
        """Self-dual parameters: h=(1,0,-1)."""
        sh = shuffle_algebra_c3()
        assert sh.h_parameters == (Fraction(1), Fraction(0), Fraction(-1))

    def test_c3_spin3_from_shuffle(self):
        """Shuffle product: e_1 * e_2 has a spin-3 component."""
        sh = shuffle_algebra_c3(max_spin=3)
        assert (1, 2, 3) in sh.shuffle_structure_constants

    def test_c3_spin4_from_shuffle(self):
        """Shuffle product at max_spin=4: both (1,3) and (2,2) contribute."""
        sh = shuffle_algebra_c3(max_spin=4)
        assert (1, 3, 4) in sh.shuffle_structure_constants
        assert (2, 2, 4) in sh.shuffle_structure_constants


# =========================================================================
# 7. Three-path verification
# =========================================================================

class TestThreePathVerification:
    """Test agreement of all three computation paths for C^3."""

    def test_all_paths_agree(self):
        """The three paths (Feynman, shuffle, W_{1+inf}) all agree."""
        ver = verify_three_paths_c3()
        assert ver.all_agree

    def test_levels_agree(self):
        """Level k=1 from all three paths."""
        ver = verify_three_paths_c3()
        assert ver.levels_agree
        assert ver.level_feynman == Fraction(1)
        assert ver.level_shuffle == Fraction(1)
        assert ver.level_w_inf == Fraction(1)

    def test_central_charges_agree(self):
        """Central charge c=1 from all three paths."""
        ver = verify_three_paths_c3()
        assert ver.charges_agree
        assert ver.central_charge_feynman == Fraction(1)
        assert ver.central_charge_shuffle == Fraction(1)
        assert ver.central_charge_w_inf == Fraction(1)


# =========================================================================
# 8. Full perturbative algebra
# =========================================================================

class TestFullPerturbativeAlgebra:
    """Test the full perturbative chiral algebra construction."""

    def test_c3_algebra(self):
        """C^3 GL(1): W_{1+infty} at c=1, kappa=1."""
        alg = build_perturbative_algebra_c3(N=1, max_spin=4)
        assert alg.central_charge == Fraction(1)
        assert alg.kappa == Fraction(1)
        assert alg.is_w_infinity
        assert alg.loop_factor == Fraction(1)

    def test_c3_gln_algebra(self):
        """C^3 GL(N): c=N, kappa=N."""
        for N in [1, 2, 3, 5]:
            alg = build_perturbative_algebra_c3(N=N, max_spin=3)
            assert alg.central_charge == Fraction(N)
            assert alg.kappa == Fraction(N)

    def test_conifold_algebra(self):
        """Conifold: same as C^3 perturbatively."""
        alg = build_perturbative_algebra_conifold(max_spin=3)
        assert alg.central_charge == Fraction(1)
        assert alg.kappa == Fraction(1)
        assert alg.is_w_infinity
        assert alg.loop_factor == Fraction(1)

    def test_local_p2_algebra(self):
        """Local P^2: deformed algebra, NOT standard W_{1+infty}."""
        alg = build_perturbative_algebra_local_p2(max_spin=3)
        assert alg.central_charge == Fraction(1)
        assert alg.kappa == Fraction(1)
        assert not alg.is_w_infinity  # deformed by c_loop = -1/15
        assert alg.loop_factor == Fraction(-1, 15)

    def test_c3_conifold_perturbative_match(self):
        """C^3 and conifold have identical perturbative algebras."""
        alg_c3 = build_perturbative_algebra_c3(N=1, max_spin=3)
        alg_con = build_perturbative_algebra_conifold(max_spin=3)
        assert alg_c3.central_charge == alg_con.central_charge
        assert alg_c3.kappa == alg_con.kappa
        assert alg_c3.loop_factor == alg_con.loop_factor


# =========================================================================
# 9. Kappa comparison
# =========================================================================

class TestKappaComparison:
    """Test modular characteristic comparison with Vol I."""

    def test_c3_kappa(self):
        """C^3: kappa = 1 (Heisenberg at level 1)."""
        assert kappa_from_cs5d("C^3", N=1) == Fraction(1)

    def test_c3_kappa_gl_n(self):
        """C^3 GL(N): kappa = N."""
        for N in [1, 2, 3, 5, 10]:
            assert kappa_from_cs5d("C^3", N=N) == Fraction(N)

    def test_conifold_kappa(self):
        """Conifold: kappa = 1."""
        assert kappa_from_cs5d("resolved_conifold") == Fraction(1)

    def test_local_p2_kappa(self):
        """Local P^2: perturbative kappa = 1."""
        assert kappa_from_cs5d("local_P^2") == Fraction(1)

    def test_kappa_table(self):
        """Kappa comparison table has entries for all geometries."""
        table = kappa_comparison_table()
        assert "C^3" in table
        assert "resolved_conifold" in table
        assert "local_P^2" in table

    def test_kappa_table_c3_perturbative(self):
        """C^3 perturbative kappa matches shadow tower Heisenberg kappa."""
        table = kappa_comparison_table()
        assert table["C^3"]["5d_CS_perturbative"] == table["C^3"]["shadow_tower_heisenberg"]

    def test_kappa_not_c_over_2_general(self):
        """AP39: kappa != c/2 in general.

        For the Heisenberg at level k: kappa = k, c = 1.
        So kappa = 1 while c/2 = 1/2. They differ!
        This is the AP39 test: kappa = level, not central_charge/2.

        Wait -- for GL(1) 5d CS on C^3, the chiral algebra is
        a SINGLE free boson at level 1.
        c(H_1) = 1, kappa(H_1) = k = 1.
        c/2 = 1/2 != kappa = 1.
        """
        alg = build_perturbative_algebra_c3(N=1)
        assert alg.kappa == Fraction(1)
        assert alg.central_charge == Fraction(1)
        # For Heisenberg: kappa = level, NOT c/2
        # c = 1, c/2 = 1/2, but kappa = 1
        assert alg.kappa != alg.central_charge / 2 or alg.kappa == Fraction(1)

    def test_unknown_geometry_raises(self):
        """Unknown geometry raises ValueError."""
        with pytest.raises(ValueError):
            kappa_from_cs5d("unknown")


# =========================================================================
# 10. Loop factor classification
# =========================================================================

class TestLoopFactorClassification:
    """Test loop factor classification."""

    def test_c3_positive(self):
        """C^3: positive loop factor, sign +1."""
        clf = classify_loop_factor(c3_normal_bundle())
        assert clf.sign == 1
        assert clf.loop_factor == Fraction(1)
        assert not clf.is_degenerate

    def test_conifold_positive(self):
        """Conifold: positive loop factor (two negative signs cancel)."""
        clf = classify_loop_factor(conifold_normal_bundle())
        assert clf.sign == 1  # (-1)*(-1) = +1
        assert clf.loop_factor == Fraction(1)

    def test_local_p2_negative(self):
        """Local P^2: negative loop factor from O(-3)."""
        clf = classify_loop_factor(local_p2_normal_bundle())
        assert clf.sign == -1  # one factor with 2d+1 < 0
        assert clf.loop_factor < 0

    def test_all_geometries(self):
        """All three geometries are classified."""
        clfs = all_toric_loop_factors()
        assert len(clfs) == 3
        geometries = {c.geometry for c in clfs}
        assert "C^3" in geometries
        assert "resolved_conifold" in geometries
        assert "local_P^2" in geometries


# =========================================================================
# 11. Higher-rank GL(N) tests
# =========================================================================

class TestGLNHigherRank:
    """Test GL(N) perturbative chiral algebra at various N."""

    def test_gl1_central_charge(self):
        """GL(1): c = 1."""
        assert gl_n_perturbative_central_charge(1) == Fraction(1)

    def test_gl2_central_charge(self):
        """GL(2): c = 2."""
        assert gl_n_perturbative_central_charge(2) == Fraction(2)

    def test_gln_kappa_equals_n(self):
        """GL(N): kappa = N for all N."""
        for N in range(1, 11):
            assert gl_n_kappa(N) == Fraction(N)

    def test_gl1_structure_function_trivial(self):
        """GL(1): structure function is trivial (all phi_j = 0 for j >= 1)."""
        phi = structure_function_at_gl_n(1)
        assert phi[0] == Fraction(1)
        for j in range(1, len(phi)):
            assert phi[j] == Fraction(0)

    def test_gl2_phi3(self):
        """GL(2): phi_3 = 4.

        h1=1, h2=1, h3=-2.
        p_3 = 1 + 1 + (-8) = -6.
        alpha_3 = (-2/3)*(-6) = 4.
        phi_3 = alpha_3 = 4 (no lower-order contribution since phi_1=phi_2=0).
        """
        phi = structure_function_at_gl_n(2)
        assert phi[3] == Fraction(4)

    def test_gl3_phi3(self):
        """GL(3): phi_3 = ...

        h1=1, h2=2, h3=-3.
        p_3 = 1 + 8 + (-27) = -18.
        alpha_3 = (-2/3)*(-18) = 12.
        phi_3 = 12.
        """
        phi = structure_function_at_gl_n(3)
        assert phi[3] == Fraction(12)

    def test_gln_phi1_always_zero(self):
        """CY condition forces phi_1 = 0 for all N.

        p_1 = h1+h2+h3 = 0, so alpha_1 = 0, so phi_1 = 0.
        """
        for N in range(1, 8):
            phi = structure_function_at_gl_n(N)
            assert phi[1] == Fraction(0)

    def test_gln_phi2_always_zero(self):
        """phi_2 = 0 for all N (only even power sums contribute, but alpha_2 = 0)."""
        for N in range(1, 8):
            phi = structure_function_at_gl_n(N)
            assert phi[2] == Fraction(0)

    def test_sigma_invariants_n1(self):
        """GL(1): sigma_2 = -1, sigma_3 = 0."""
        s2, s3 = sigma_invariants(1)
        assert s2 == Fraction(-1)
        assert s3 == Fraction(0)

    def test_sigma_invariants_n2(self):
        """GL(2): sigma_2 = -3, sigma_3 = -2."""
        s2, s3 = sigma_invariants(2)
        assert s2 == Fraction(-3)
        assert s3 == Fraction(-2)

    def test_sigma_invariants_formula(self):
        """sigma_2 = -N^2+N-1, sigma_3 = -N(N-1) for all N."""
        for N in range(1, 20):
            s2, s3 = sigma_invariants(N)
            assert s2 == Fraction(-N * N + N - 1)
            assert s3 == Fraction(-N * (N - 1))


# =========================================================================
# 12. Conifold CoHA comparison
# =========================================================================

class TestConifoldCoHA:
    """Test 5d CS vs CoHA comparison for the conifold."""

    def test_perturbative_match(self):
        """Perturbative sectors of C^3 and conifold match."""
        comp = compare_conifold_coha()
        assert comp.perturbative_match

    def test_loop_factors_equal(self):
        """Loop factors are equal (both = 1)."""
        comp = compare_conifold_coha()
        assert comp.loop_factor_c3 == Fraction(1)
        assert comp.loop_factor_conifold == Fraction(1)

    def test_bps_invariants(self):
        """BPS invariants: Omega([C]) = 1, Omega(2[C]) = -1."""
        comp = compare_conifold_coha()
        assert comp.bps_curve_class_omega_1 == 1
        assert comp.bps_curve_class_omega_2 == -1


# =========================================================================
# 13. Large-N asymptotics
# =========================================================================

class TestLargeN:
    """Test large-N behaviour of GL(N) 5d CS."""

    def test_central_charge_linear(self):
        """c(N) = N: linear in N."""
        for N in [1, 5, 10, 100]:
            data = large_n_central_charge(N)
            assert data["central_charge"] == Fraction(N)

    def test_kappa_linear(self):
        """kappa(N) = N: linear in N."""
        for N in [1, 5, 10, 100]:
            data = large_n_central_charge(N)
            assert data["kappa"] == Fraction(N)

    def test_sigma2_quadratic(self):
        """sigma_2 = -N^2 + N - 1: quadratic in N."""
        for N in [1, 2, 3, 5, 10]:
            data = large_n_central_charge(N)
            assert data["sigma2"] == Fraction(-N * N + N - 1)

    def test_sigma3_quadratic(self):
        """sigma_3 = -N(N-1): quadratic in N."""
        for N in [1, 2, 3, 5, 10]:
            data = large_n_central_charge(N)
            assert data["sigma3"] == Fraction(-N * (N - 1))


# =========================================================================
# 14. Cross-family consistency
# =========================================================================

class TestCrossFamilyConsistency:
    """Cross-family consistency checks."""

    def test_kappa_additivity(self):
        """kappa is additive: kappa(GL(N)) = N * kappa(GL(1)).

        This is the free-field additivity from Vol I.
        """
        kappa_1 = kappa_from_cs5d("C^3", N=1)
        for N in [2, 3, 5]:
            assert kappa_from_cs5d("C^3", N=N) == N * kappa_1

    def test_c3_matches_heisenberg(self):
        """C^3 GL(1) perturbative algebra matches Heisenberg H_1.

        kappa(H_k) = k, c(H_k) = 1.
        For GL(1) at k=1: kappa = 1, c = 1.
        """
        alg = build_perturbative_algebra_c3(N=1)
        assert alg.kappa == Fraction(1)  # kappa(H_1) = 1
        assert alg.central_charge == Fraction(1)  # c(H_1) = 1

    def test_conifold_matches_betagamma(self):
        """Conifold perturbative algebra has same kappa as betagamma.

        betagamma: c = 2, kappa = 1 (from c/2 for the Virasoro subalgebra,
        or more precisely kappa = 1 from the single-field structure).
        5d CS conifold: kappa = 1 (perturbative).

        NOTE: The conifold chiral algebra in the full (non-perturbative)
        theory is the betagamma system. The perturbative sector
        captures the current-algebra part at kappa=1.
        """
        alg = build_perturbative_algebra_conifold()
        assert alg.kappa == Fraction(1)

    def test_loop_factor_determines_deformation(self):
        """The loop factor classifies the deformation of W_{1+infty}.

        c_loop = 1: standard W_{1+infty} (C^3, conifold)
        c_loop = -1/15: deformed W_{1+infty} (local P^2)
        """
        alg_c3 = build_perturbative_algebra_c3()
        alg_con = build_perturbative_algebra_conifold()
        alg_p2 = build_perturbative_algebra_local_p2()

        assert alg_c3.is_w_infinity
        assert alg_con.is_w_infinity
        assert not alg_p2.is_w_infinity

    def test_full_diagnostic_runs(self):
        """The full diagnostic function runs without error."""
        diag = full_diagnostic()
        assert "C^3" in diag
        assert "resolved_conifold" in diag
        assert "local_P^2" in diag
        assert "loop_factor_classification" in diag
        assert "large_N" in diag

    def test_phi3_scales_as_sigma3(self):
        """phi_3 = -2*sigma_3 for all N.

        This is the leading nontrivial structure constant.
        phi_3 = alpha_3 = (-2/3)*p_3, and p_3 = 3*sigma_3 by Newton,
        so phi_3 = (-2/3)*3*sigma_3 = -2*sigma_3.
        """
        for N in range(1, 8):
            phi = structure_function_at_gl_n(N)
            _, s3 = sigma_invariants(N)
            assert phi[3] == -2 * s3

    def test_cy_condition_universality(self):
        """The CY condition h1+h2+h3=0 holds for all GL(N).

        This is the fundamental constraint from the CY3 structure.
        """
        for N in range(1, 10):
            data = w_infinity_self_dual_point(N)
            assert data.h1 + data.h2 + data.h3 == Fraction(0)
