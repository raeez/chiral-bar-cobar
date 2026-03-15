"""Tests for pro-Weyl M-level (chain-level) convergence of Y(sl_2).

Upgrades the S-level tests in test_pro_weyl_sl2.py to the chain/dg level:
  - Verma module resolutions of Weyl truncations
  - Hom complexes and Ext groups between truncations
  - Mapping cones of transition maps
  - Derived inverse limits at the chain level
  - DG module structure and sl_2 representation theory
  - Transition map equivariance and composition
  - Full M-level convergence verification

All tests verify conj:pro-weyl-recovery (yangians.tex) at M-level:
  M(Psi) = R lim_m W_m  (as objects in the dg category)

CONVENTIONS:
  - Cohomological grading: |d| = +1
  - Ext in cohomological convention
"""

import pytest

from compute.lib.sl2_baxter import (
    FormalCharacter,
    formal_character_equal,
    sl2_verma_character,
)
from compute.lib.pro_weyl_sl2 import (
    weyl_truncation,
)
from compute.lib.pro_weyl_m_level import (
    # Weight utilities
    hom_space_dim,
    # Verma resolutions
    verma_resolution_of_weyl,
    resolution_character_check,
    # Hom complexes
    weyl_hom_complex,
    # Ext groups
    weyl_ext_groups,
    # Ext stabilization
    ext_stabilization_check,
    # Mapping cones
    chain_map_cone,
    verify_mapping_cones,
    # Derived inverse limit
    derived_inverse_limit_chain,
    # Mittag-Leffler chain level
    mittag_leffler_chain_level,
    # DG module structure
    dg_module_structure,
    verify_weight_grading,
    # Transition maps
    transition_map_matrix,
    verify_transition_weight_compatibility,
    verify_transition_composition,
    # Full verification
    verify_m_level_convergence,
    verify_m_level_multi_lambda,
    s_vs_m_level_comparison,
    verify_all,
)


# ============================================================================
# Hom space dimensions
# ============================================================================

class TestHomSpaceDim:
    """Test Hom(W_{m1}, W_{m2}) dimensions."""

    @pytest.mark.parametrize("m1,m2,expected", [
        (1, 1, 1), (2, 1, 1), (5, 3, 1), (10, 1, 1),  # m1 >= m2: dim = 1
        (1, 2, 0), (3, 5, 0), (1, 10, 0),               # m1 < m2: dim = 0
    ])
    def test_hom_dim(self, m1, m2, expected):
        """Hom(W_{m1}, W_{m2}) = C if m1 >= m2, else 0."""
        assert hom_space_dim(0, m1, m2) == expected

    def test_hom_dim_independent_of_lambda(self):
        """Hom dimension does not depend on lambda."""
        for lam in [0, 1, 3, 7, 10]:
            assert hom_space_dim(lam, 5, 3) == 1
            assert hom_space_dim(lam, 3, 5) == 0

    def test_hom_diagonal(self):
        """Hom(W_m, W_m) = C (the identity map)."""
        for m in range(1, 15):
            assert hom_space_dim(0, m, m) == 1

    def test_hom_degenerate(self):
        """Hom involving W_0 is zero."""
        assert hom_space_dim(0, 0, 5) == 0
        assert hom_space_dim(0, 5, 0) == 0

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_hom_monotone_in_source(self, lam):
        """For fixed target, Hom(W_m, W_n) is monotone nondecreasing in m."""
        n = 5
        for m in range(1, 15):
            dim = hom_space_dim(lam, m, n)
            assert dim == (1 if m >= n else 0)


# ============================================================================
# Verma resolutions
# ============================================================================

class TestVermaResolution:
    """Test Verma module resolutions of Weyl truncations."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    @pytest.mark.parametrize("m", [1, 2, 3, 5, 8])
    def test_resolution_character(self, lam, m):
        """ch(M(lam)) - ch(M(lam-2m)) = ch(W_m) (Verma resolution check)."""
        assert resolution_character_check(lam, m)

    def test_resolution_structure(self):
        """Resolution has length 1 (two terms)."""
        for m in [1, 3, 5]:
            res = verma_resolution_of_weyl(5, m)
            assert res["resolution_length"] == 1
            assert "M(5)" in res["P_0"]
            assert f"M({5 - 2 * m})" in res["P_minus1"]

    def test_resolution_hw_of_submodule(self):
        """Submodule has highest weight lambda - 2m."""
        for lam in [0, 3, 7]:
            for m in [1, 4]:
                res = verma_resolution_of_weyl(lam, m)
                assert res["hw_of_submodule"] == lam - 2 * m


# ============================================================================
# Hom complexes
# ============================================================================

class TestHomComplex:
    """Test the Hom complex RHom(W_{m1}, W_{m2})."""

    def test_hom_complex_m1_ge_m2(self):
        """When m1 >= m2: complex is C in degree 0, 0 in degree 1."""
        for m1, m2 in [(5, 3), (3, 3), (10, 1)]:
            data = weyl_hom_complex(0, m1, m2)
            assert data["spaces"][0] == 1
            assert data["spaces"][1] == 0

    def test_hom_complex_m1_lt_m2(self):
        """When m1 < m2: complex is C in both degrees, d is an isomorphism."""
        for m1, m2 in [(1, 5), (3, 10), (2, 4)]:
            data = weyl_hom_complex(0, m1, m2)
            assert data["spaces"][0] == 1
            assert data["spaces"][1] == 1
            d0 = data["differentials"][0]
            assert d0.rank() == 1  # d is an isomorphism

    def test_hom_complex_diagonal(self):
        """RHom(W_m, W_m): complex is C -> 0."""
        for m in [1, 3, 7]:
            data = weyl_hom_complex(0, m, m)
            assert data["spaces"][0] == 1
            assert data["spaces"][1] == 0

    @pytest.mark.parametrize("lam", [0, 1, 2, 5])
    def test_hom_complex_independent_of_lambda(self, lam):
        """Hom complex structure is independent of lambda (sl_2 universality)."""
        d1 = weyl_hom_complex(lam, 5, 3)
        d2 = weyl_hom_complex(lam + 7, 5, 3)
        assert d1["spaces"] == d2["spaces"]


# ============================================================================
# Ext groups
# ============================================================================

class TestExtGroups:
    """Test Ext^p(W_{m1}, W_{m2}) dimensions."""

    @pytest.mark.parametrize("m1,m2", [(5, 3), (3, 3), (10, 1), (7, 2)])
    def test_ext0_when_m1_ge_m2(self, m1, m2):
        """Ext^0(W_{m1}, W_{m2}) = 1 when m1 >= m2."""
        ext = weyl_ext_groups(0, m1, m2)
        assert ext[0] == 1

    @pytest.mark.parametrize("m1,m2", [(1, 3), (2, 5), (3, 10)])
    def test_ext0_when_m1_lt_m2(self, m1, m2):
        """Ext^0(W_{m1}, W_{m2}) = 0 when m1 < m2."""
        ext = weyl_ext_groups(0, m1, m2)
        assert ext[0] == 0

    @pytest.mark.parametrize("m1", [1, 2, 3, 5, 8])
    @pytest.mark.parametrize("m2", [1, 2, 3, 5, 8])
    def test_ext1_always_zero(self, m1, m2):
        """Ext^1(W_{m1}, W_{m2}) = 0 for all m1, m2 (sl_2 semisimplicity)."""
        ext = weyl_ext_groups(0, m1, m2)
        assert ext[1] == 0

    @pytest.mark.parametrize("p", [2, 3, 4])
    def test_higher_ext_zero(self, p):
        """Ext^p = 0 for p >= 2 (length-1 Verma resolution)."""
        for m1 in [1, 3, 5]:
            for m2 in [1, 3, 5]:
                ext = weyl_ext_groups(0, m1, m2, max_degree=p)
                assert ext[p] == 0

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_ext_independent_of_lambda(self, lam):
        """Ext groups are independent of lambda."""
        ext1 = weyl_ext_groups(lam, 5, 3)
        ext2 = weyl_ext_groups(lam + 100, 5, 3)
        assert ext1 == ext2

    def test_ext_euler_characteristic(self):
        """chi(RHom(W_m1, W_m2)) = Ext^0 - Ext^1 = hom_space_dim."""
        for m1 in [1, 3, 5, 8]:
            for m2 in [1, 3, 5, 8]:
                ext = weyl_ext_groups(0, m1, m2)
                chi = ext[0] - ext[1]
                expected = hom_space_dim(0, m1, m2)
                assert chi == expected


# ============================================================================
# Ext stabilization
# ============================================================================

class TestExtStabilization:
    """Test that Ext groups stabilize as truncation levels increase."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 5])
    def test_ext_stable(self, lam):
        """Ext^p(W_m, W_{m'}) has the expected pattern for all m, m'."""
        data = ext_stabilization_check(lam, max_m=8)
        assert data["stable"], f"Failures: {data['failures']}"

    def test_consistent_with_verma_ext(self):
        """Stabilization pattern is consistent with Verma module Ext."""
        data = ext_stabilization_check(0, max_m=5)
        assert data["consistent_with_verma_ext"]

    def test_expected_pattern(self):
        """The pattern is: Ext^0 = 1 iff m >= m', all higher Ext vanish."""
        data = ext_stabilization_check(0, max_m=6)
        assert "Ext^0(W_m, W_{m'}) = 1 iff m >= m'" in data["pattern"]


# ============================================================================
# Mapping cones
# ============================================================================

class TestMappingCones:
    """Test the mapping cone of pi_m: W_{m+1} -> W_m."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    @pytest.mark.parametrize("m", [1, 2, 3, 5, 8])
    def test_kernel_dim_one(self, lam, m):
        """Kernel of pi_m is 1-dimensional."""
        cone = chain_map_cone(lam, m)
        assert cone["kernel_dim"] == 1

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    @pytest.mark.parametrize("m", [1, 2, 3, 5, 8])
    def test_kernel_weight(self, lam, m):
        """Kernel sits at weight lambda - 2m."""
        cone = chain_map_cone(lam, m)
        assert cone["kernel_weight"] == lam - 2 * m

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    @pytest.mark.parametrize("m", [1, 2, 3, 5, 8])
    def test_cokernel_zero(self, lam, m):
        """Cokernel of pi_m is 0 (surjective)."""
        cone = chain_map_cone(lam, m)
        assert cone["cokernel_dim"] == 0

    def test_cone_cohomology(self):
        """Cone has H^{-1} = C (at killed weight) and H^0 = 0."""
        cone = chain_map_cone(5, 3)
        assert cone["cone_cohomology"][-1] == 1
        assert cone["cone_cohomology"][0] == 0

    def test_pi_matrix_shape(self):
        """pi_m is m x (m+1) matrix."""
        for m in [1, 3, 5, 8]:
            cone = chain_map_cone(0, m)
            pi = cone["pi_matrix"]
            assert pi.rows == m
            assert pi.cols == m + 1

    def test_pi_matrix_rank(self):
        """pi_m has rank m (full rank on the target)."""
        for m in [1, 3, 5]:
            cone = chain_map_cone(0, m)
            assert cone["pi_rank"] == m

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_verify_all_cones(self, lam):
        """All mapping cones for lam have the expected structure."""
        assert verify_mapping_cones(lam, max_m=15)

    def test_cone_acyclic_in_stable_range(self):
        """Cone is acyclic in the stable range (H^0 = 0)."""
        for lam in [0, 2, 5]:
            for m in [1, 3, 7]:
                cone = chain_map_cone(lam, m)
                assert cone["is_acyclic_in_stable_range"]

    def test_killed_weight_decreases(self):
        """Killed weight decreases by 2 at each level."""
        lam = 5
        for m in range(1, 10):
            cone_m = chain_map_cone(lam, m)
            cone_m1 = chain_map_cone(lam, m + 1)
            assert cone_m["killed_weight"] - cone_m1["killed_weight"] == 2


# ============================================================================
# Derived inverse limit
# ============================================================================

class TestDerivedInverseLimit:
    """Test R lim_m W_m at the chain level."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_limit_matches_verma(self, lam):
        """lim_m W_m = M(lambda) as formal characters."""
        data = derived_inverse_limit_chain(lam, max_m=20)
        assert data["limit_matches_verma"]

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_r1_zero(self, lam):
        """R^1 lim_m W_m = 0."""
        data = derived_inverse_limit_chain(lam, max_m=20)
        assert data["r1_is_zero"]

    def test_weight_stabilization_levels(self):
        """Weight lambda - 2k stabilizes at m = k + 1."""
        lam = 5
        data = derived_inverse_limit_chain(lam, max_m=15)
        for k in range(15):
            mu = lam - 2 * k
            wd = data["weight_data"][mu]
            assert wd["stabilization_level"] == k + 1

    def test_limit_character_equals_verma(self):
        """The limit character is exactly the Verma character."""
        for lam in [0, 3, 7]:
            depth = 20
            data = derived_inverse_limit_chain(lam, max_m=depth)
            verma = sl2_verma_character(lam, depth=depth)
            assert formal_character_equal(data["limit_character"], verma)

    def test_r1_character_empty(self):
        """R^1 character has no nonzero entries."""
        for lam in [0, 1, 5]:
            data = derived_inverse_limit_chain(lam, max_m=15)
            assert data["r1_character"] == {}

    def test_all_limit_dims_one(self):
        """Every weight space in the limit has dimension 1."""
        data = derived_inverse_limit_chain(5, max_m=20)
        for mu, wd in data["weight_data"].items():
            assert wd["limit_dim"] == 1

    def test_all_r1_dims_zero(self):
        """Every weight space has R^1 = 0."""
        data = derived_inverse_limit_chain(5, max_m=20)
        for mu, wd in data["weight_data"].items():
            assert wd["r1_lim_dim"] == 0


# ============================================================================
# Mittag-Leffler at chain level
# ============================================================================

class TestMittagLefflerChainLevel:
    """Test Mittag-Leffler condition at the chain level."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 5, 10])
    def test_ml_holds(self, lam):
        """Mittag-Leffler condition holds at chain level."""
        data = mittag_leffler_chain_level(lam, max_m=15)
        assert data["ml_holds"]

    def test_all_surjective(self):
        """All transition maps are surjective (chain-level check)."""
        data = mittag_leffler_chain_level(5, max_m=15)
        assert data["all_surjective"]

    def test_chain_level_consistent(self):
        """Chain-level analysis is self-consistent."""
        data = mittag_leffler_chain_level(5, max_m=10)
        assert data["chain_level_consistent"]

    def test_weight_stabilization(self):
        """Each weight space stabilizes at the expected level."""
        lam = 5
        data = mittag_leffler_chain_level(lam, max_m=15)
        for k in range(15):
            mu = lam - 2 * k
            wd = data["weight_level_data"][mu]
            assert wd["first_nonzero"] == k + 1
            assert wd["ml_stabilization"] == k + 1


# ============================================================================
# DG module structure
# ============================================================================

class TestDGModuleStructure:
    """Test the dg module structure on W_m."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 3, 5])
    @pytest.mark.parametrize("m", [1, 2, 3, 5])
    def test_dimension(self, lam, m):
        """W_m has dimension m."""
        data = dg_module_structure(lam, m)
        assert data["dimension"] == m

    @pytest.mark.parametrize("lam", [0, 1, 2, 5])
    @pytest.mark.parametrize("m", [1, 2, 3, 5])
    def test_weights(self, lam, m):
        """Weights are lambda, lambda-2, ..., lambda-2(m-1)."""
        data = dg_module_structure(lam, m)
        expected = [lam - 2 * k for k in range(m)]
        assert data["weights"] == expected

    def test_differential_zero(self):
        """Differential is zero (plain module)."""
        data = dg_module_structure(5, 3)
        assert "zero" in data["differential"]

    def test_concentrated_in_degree_zero(self):
        """Module is concentrated in dg degree 0."""
        data = dg_module_structure(5, 3)
        assert data["dg_degree"] == 0

    def test_degenerate_input(self):
        """m <= 0 gives trivial structure."""
        data = dg_module_structure(5, 0)
        assert data["dimension"] == 0
        data_neg = dg_module_structure(5, -1)
        assert data_neg["dimension"] == 0

    def test_action_matrices_shapes(self):
        """e, f, h matrices are m x m."""
        for m in [1, 3, 5]:
            data = dg_module_structure(5, m)
            for gen in ["e", "f", "h"]:
                mat = data["action_matrices"][gen]
                assert mat.rows == m
                assert mat.cols == m

    def test_h_eigenvalues(self):
        """h acts diagonally with eigenvalues lambda, lambda-2, ..."""
        for lam in [0, 2, 5]:
            for m in [1, 3, 5]:
                data = dg_module_structure(lam, m)
                H = data["action_matrices"]["h"]
                for k in range(m):
                    assert H[k, k] == lam - 2 * k
                    # Off-diagonal entries are 0
                    for j in range(m):
                        if j != k:
                            assert H[k, j] == 0

    def test_e_annihilates_hw(self):
        """e annihilates the highest weight vector v_0."""
        for lam in [0, 1, 3, 5]:
            data = dg_module_structure(lam, 5)
            E = data["action_matrices"]["e"]
            # Column 0 of E should be zero (e . v_0 = 0)
            for i in range(5):
                assert E[i, 0] == 0

    def test_f_lowers_weight(self):
        """f . v_k = v_{k+1} (for k < m-1) and f . v_{m-1} = 0."""
        data = dg_module_structure(5, 5)
        F = data["action_matrices"]["f"]
        for k in range(4):
            assert F[k + 1, k] == 1
        # f . v_{m-1} = 0
        for i in range(5):
            assert F[i, 4] == 0

    def test_e_raises_weight(self):
        """e . v_k = k(lam-k+1) * v_{k-1} for k >= 1."""
        lam = 5
        m = 5
        data = dg_module_structure(lam, m)
        E = data["action_matrices"]["e"]
        for k in range(1, m):
            expected = k * (lam - k + 1)
            assert E[k - 1, k] == expected


# ============================================================================
# Weight grading
# ============================================================================

class TestWeightGrading:
    """Test weight grading properties on W_m.

    W_m is a weight-graded vector space. The sl_2 generators e, f, h
    act as inherited from the Verma module, but [e,f]=h only holds
    in the interior (not at the boundary vector v_{m-1}).
    """

    @pytest.mark.parametrize("lam", [0, 1, 2, 3, 5, 10])
    @pytest.mark.parametrize("m", [1, 2, 3, 5, 8])
    def test_all_grading_properties(self, lam, m):
        """All weight grading properties hold on W_m."""
        props = verify_weight_grading(lam, m)
        assert props["h_diagonal"], f"h not diagonal at lam={lam}, m={m}"
        assert props["[h,e]=2e"], f"[h,e]=2e failed at lam={lam}, m={m}"
        assert props["[h,f]=-2f"], f"[h,f]=-2f failed at lam={lam}, m={m}"
        assert props["[e,f]=h_interior"], f"[e,f]=h interior failed at lam={lam}, m={m}"

    def test_ef_commutator_interior(self):
        """[e, f] = h holds on interior vectors v_0, ..., v_{m-2}."""
        lam, m = 5, 5
        data = dg_module_structure(lam, m)
        E = data["action_matrices"]["e"]
        F = data["action_matrices"]["f"]
        H = data["action_matrices"]["h"]
        comm = E * F - F * E
        # Check interior: rows 0 to m-2
        for k in range(m - 1):
            assert comm[k, k] == H[k, k], f"[e,f] != h at v_{k}"

    def test_ef_boundary_failure(self):
        """[e, f] != h at boundary v_{m-1} for generic (lam, m).

        At v_{m-1}: [e,f].v_{m-1} = -f(e.v_{m-1}) since f.v_{m-1}=0
        = -(m-1)(lam-m+2)*v_{m-1}
        But h.v_{m-1} = (lam-2m+2)*v_{m-1}.
        These are unequal unless lam = m-1 (the fd irreducible case).
        """
        lam, m = 5, 3  # lam != m-1 = 2
        data = dg_module_structure(lam, m)
        E = data["action_matrices"]["e"]
        F = data["action_matrices"]["f"]
        H = data["action_matrices"]["h"]
        comm = E * F - F * E
        # At boundary k=m-1=2: comm[2,2] != H[2,2]
        assert comm[m - 1, m - 1] != H[m - 1, m - 1]

    def test_ef_equals_h_for_fd_irreducible(self):
        """[e, f] = h on ALL of W_m when lam = m - 1 (fd irreducible V_lam)."""
        for lam in [0, 1, 2, 3, 5]:
            m = lam + 1  # fd irreducible V_lam
            data = dg_module_structure(lam, m)
            E = data["action_matrices"]["e"]
            F = data["action_matrices"]["f"]
            H = data["action_matrices"]["h"]
            assert (E * F - F * E - H).is_zero_matrix, \
                f"[e,f] != h on V_{lam} (should be an sl_2 module)"

    def test_casimir_on_fd_irreducible(self):
        """Casimir C = h^2 + 2h + 4fe acts as lam(lam+2)*I on V_lam."""
        from sympy import eye
        for lam in [0, 1, 2, 3, 5]:
            m = lam + 1
            data = dg_module_structure(lam, m)
            E = data["action_matrices"]["e"]
            F = data["action_matrices"]["f"]
            H = data["action_matrices"]["h"]
            I_m = eye(m)
            Casimir = H * H + 2 * H + 4 * F * E
            expected = lam * (lam + 2)
            assert (Casimir - expected * I_m).is_zero_matrix

    def test_degenerate(self):
        """Grading properties hold vacuously for m <= 0."""
        props = verify_weight_grading(5, 0)
        assert all(props.values())


# ============================================================================
# Transition maps
# ============================================================================

class TestTransitionMaps:
    """Test the transition maps pi_m: W_{m+1} -> W_m."""

    @pytest.mark.parametrize("m", [1, 2, 3, 5, 8])
    def test_matrix_shape(self, m):
        """pi_m is m x (m+1)."""
        pi = transition_map_matrix(0, m)
        assert pi.rows == m
        assert pi.cols == m + 1

    @pytest.mark.parametrize("m", [1, 2, 3, 5, 8])
    def test_matrix_rank(self, m):
        """pi_m has full rank m."""
        pi = transition_map_matrix(0, m)
        assert pi.rank() == m

    def test_matrix_structure(self):
        """pi_m = [I_m | 0] (identity on first m columns)."""
        m = 5
        pi = transition_map_matrix(0, m)
        for i in range(m):
            for j in range(m + 1):
                if i == j:
                    assert pi[i, j] == 1
                else:
                    assert pi[i, j] == 0

    @pytest.mark.parametrize("lam", [0, 1, 2, 5])
    @pytest.mark.parametrize("m", [1, 2, 3, 5])
    def test_weight_compatibility(self, lam, m):
        """pi_m preserves weight grading and commutes with h and e."""
        compat = verify_transition_weight_compatibility(lam, m)
        for prop, ok in compat.items():
            assert ok, f"Weight compatibility failed for {prop} at lam={lam}, m={m}"

    @pytest.mark.parametrize("lam", [0, 1, 2, 5])
    def test_composition(self, lam):
        """Transition maps compose correctly."""
        assert verify_transition_composition(lam, max_m=8)

    def test_composition_specific(self):
        """pi_1 . pi_2 equals direct map W_3 -> W_1."""
        from sympy import zeros as sz
        pi1 = transition_map_matrix(0, 1)  # 1x2
        pi2 = transition_map_matrix(0, 2)  # 2x3
        composite = pi1 * pi2              # 1x3
        direct = sz(1, 3)
        direct[0, 0] = 1
        assert (composite - direct).is_zero_matrix

    def test_kernel_is_last_basis_vector(self):
        """Kernel of pi_m is spanned by the last basis vector of W_{m+1}."""
        from sympy import Matrix as M
        m = 5
        pi = transition_map_matrix(0, m)
        # The kernel should be spanned by e_{m+1} = (0,...,0,1)^T
        last_vec = M([0] * m + [1])
        result = pi * last_vec
        assert result.is_zero_matrix

    def test_surjectivity(self):
        """pi_m is surjective (rank = m = number of rows)."""
        for m in [1, 3, 7, 12]:
            pi = transition_map_matrix(0, m)
            assert pi.rank() == m


# ============================================================================
# Full M-level convergence
# ============================================================================

class TestMLevelConvergence:
    """Test the full M-level convergence verification."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 5])
    def test_full_convergence(self, lam):
        """Full M-level convergence passes for standard lambda values."""
        data = verify_m_level_convergence(lam, max_m=8)
        assert data["m_level_convergence_verified"], \
            f"M-level convergence failed at lam={lam}: " \
            f"{[k for k, v in data.items() if not v and k != 'm_level_convergence_verified']}"

    def test_all_subcheck_pass(self):
        """Every individual subcheck passes."""
        data = verify_m_level_convergence(2, max_m=8)
        for key, val in data.items():
            if key != "m_level_convergence_verified":
                assert val, f"Subcheck {key} failed"

    def test_negative_lambda(self):
        """M-level convergence also works for negative lambda."""
        data = verify_m_level_convergence(-3, max_m=8)
        assert data["m_level_convergence_verified"]


class TestMLevelMultiLambda:
    """Test multi-lambda M-level verification."""

    def test_default_lambdas(self):
        """Default lambda values all pass."""
        results = verify_m_level_multi_lambda(max_m=8)
        for lam, data in results.items():
            assert data["m_level_convergence_verified"], f"Failed at lam={lam}"

    def test_custom_lambdas(self):
        """Custom lambda values pass."""
        results = verify_m_level_multi_lambda(lambdas=[-2, 0, 3, 7], max_m=8)
        for lam, data in results.items():
            assert data["m_level_convergence_verified"], f"Failed at lam={lam}"


# ============================================================================
# S-level vs M-level comparison
# ============================================================================

class TestSvsMLevel:
    """Test that M-level refines S-level."""

    @pytest.mark.parametrize("lam", [0, 1, 2, 5])
    def test_m_refines_s(self, lam):
        """M-level implies S-level."""
        comp = s_vs_m_level_comparison(lam, max_m=10)
        assert comp["m_level_refines_s_level"]

    @pytest.mark.parametrize("lam", [0, 1, 2, 5])
    def test_both_pass(self, lam):
        """Both S-level and M-level pass."""
        comp = s_vs_m_level_comparison(lam, max_m=10)
        assert comp["s_level_all_pass"]
        assert comp["m_level_all_pass"]


# ============================================================================
# Integration tests
# ============================================================================

class TestIntegration:
    """Integration tests combining multiple M-level aspects."""

    def test_verify_all(self):
        """Complete M-level verification suite passes."""
        results = verify_all()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_full_pipeline(self):
        """Full M-level pipeline for lambda=3.

        Verify the entire chain of M-level data:
        1. Verma resolutions
        2. sl_2 action
        3. Transition maps
        4. Mapping cones
        5. Ext groups
        6. Derived inverse limit
        """
        lam = 3

        # 1. Verma resolutions
        for m in range(1, 8):
            assert resolution_character_check(lam, m)

        # 2. Weight grading
        for m in range(1, 8):
            props = verify_weight_grading(lam, m)
            assert all(props.values()), f"Weight grading failed at m={m}"

        # 3. Transition maps weight-compatible
        for m in range(1, 7):
            compat = verify_transition_weight_compatibility(lam, m)
            assert all(compat.values()), f"Weight compatibility failed at m={m}"

        # 4. Mapping cones
        for m in range(1, 8):
            cone = chain_map_cone(lam, m)
            assert cone["kernel_dim"] == 1
            assert cone["kernel_weight"] == lam - 2 * m
            assert cone["cokernel_dim"] == 0

        # 5. Ext groups
        for m1 in range(1, 6):
            for m2 in range(1, 6):
                ext = weyl_ext_groups(lam, m1, m2)
                assert ext[0] == (1 if m1 >= m2 else 0)
                assert ext[1] == 0

        # 6. Derived inverse limit
        dlim = derived_inverse_limit_chain(lam, max_m=15)
        assert dlim["limit_matches_verma"]
        assert dlim["r1_is_zero"]

    def test_convergence_consistency(self):
        """M-level and S-level give consistent convergence data.

        The S-level error dimension at truncation m is depth - m.
        The M-level mapping cone at level m captures exactly one
        weight space. After m mapping cones, exactly m weight spaces
        are captured. This is consistent with the S-level error
        dim = depth - m.
        """
        lam, depth = 5, 20
        for m in range(1, depth):
            # M-level: cone at level m kills weight lam - 2m
            cone = chain_map_cone(lam, m)
            assert cone["killed_weight"] == lam - 2 * m

            # S-level: error has depth - m weight spaces remaining
            from compute.lib.pro_weyl_sl2 import error_dimension
            err_dim = error_dimension(lam, m, depth=depth)
            assert err_dim == depth - m

            # The number of captured weight spaces is m, which equals
            # the number of cones we've processed
            assert m == depth - err_dim

    def test_hom_ext_consistency(self):
        """Hom and Ext^0 agree (they should be the same thing)."""
        for lam in [0, 2, 5]:
            for m1 in [1, 3, 5, 7]:
                for m2 in [1, 3, 5, 7]:
                    hom = hom_space_dim(lam, m1, m2)
                    ext = weyl_ext_groups(lam, m1, m2)
                    assert hom == ext[0], \
                        f"Hom({m1},{m2})={hom} but Ext^0={ext[0]}"

    def test_resolution_ext_consistency(self):
        """Ext computed from Hom complex matches resolution-based Ext.

        The Hom complex approach (from Verma resolution) should give
        the same Ext as the direct computation.
        """
        for lam in [0, 1, 5]:
            for m1 in [1, 3, 5]:
                for m2 in [1, 3, 5]:
                    ext = weyl_ext_groups(lam, m1, m2)
                    hom_data = weyl_hom_complex(lam, m1, m2)

                    # Compute cohomology of the Hom complex directly
                    spaces = hom_data["spaces"]
                    diffs = hom_data["differentials"]

                    # H^0
                    d0 = diffs.get(0)
                    if d0 is not None and d0.rows > 0 and d0.cols > 0:
                        h0 = spaces[0] - d0.rank()
                    else:
                        h0 = spaces[0]
                    assert h0 == ext[0]

                    # H^1
                    if d0 is not None and d0.rows > 0 and d0.cols > 0:
                        im0 = d0.rank()
                    else:
                        im0 = 0
                    h1 = spaces.get(1, 0) - im0
                    assert h1 == ext[1]


# ============================================================================
# Edge cases
# ============================================================================

class TestEdgeCases:
    """Edge cases and boundary behavior."""

    def test_lam_zero_m_one(self):
        """W_1 for lambda=0 is the trivial module {0:1}."""
        data = dg_module_structure(0, 1)
        assert data["dimension"] == 1
        assert data["weights"] == [0]
        # All action matrices should be 1x1 zero
        for gen in ["e", "f", "h"]:
            assert data["action_matrices"][gen].is_zero_matrix

    def test_large_m(self):
        """Large m works without issues."""
        m = 50
        data = dg_module_structure(10, m)
        assert data["dimension"] == m
        # Weight grading holds
        props = verify_weight_grading(10, m)
        assert all(props.values())

    def test_negative_lambda(self):
        """Negative lambda (non-dominant Verma) works."""
        data = verify_m_level_convergence(-5, max_m=8)
        assert data["m_level_convergence_verified"]

    def test_lambda_equals_one(self):
        """Special case lambda=1: Verma has singular vector at weight -1."""
        # The M-level structure should still work
        data = verify_m_level_convergence(1, max_m=8)
        assert data["m_level_convergence_verified"]

    def test_ext_degenerate(self):
        """Ext for degenerate inputs (m=0) gives all zeros."""
        ext = weyl_ext_groups(0, 0, 5)
        for p in range(4):
            assert ext[p] == 0

    def test_cone_m_zero(self):
        """Mapping cone for m=0 (boundary case)."""
        # pi_0: W_1 -> W_0 maps the 1-dim module to 0
        cone = chain_map_cone(5, 0)
        # W_0 has dim 0, W_1 has dim 1
        # kernel of the 0x1 matrix is all of W_1
        assert cone["kernel_dim"] == 1
        assert cone["killed_weight"] == 5  # lam - 2*0 = lam
