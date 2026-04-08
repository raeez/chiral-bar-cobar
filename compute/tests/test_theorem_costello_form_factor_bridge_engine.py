r"""Tests for the Costello form factor bridge engine.

Verifies the bridge between:
- Costello's QCD form factor computations (arXiv:2302.00770)
- Bittleston-Costello-Zeng self-dual gauge theory (arXiv:2412.02680)
- Fernandez-Paquette all-orders OPE (arXiv:2412.17168)
- The shadow obstruction tower framework (thm:mc2-bar-intrinsic)

TEST ORGANIZATION:
1. Exact arithmetic helpers (Bernoulli, lambda_fp, harmonic)
2. Lie algebra data (sl_N for N = 2..6)
3. Kappa formulas (AP1 cross-verification, AP9 != c/2)
4. SDYM chiral algebra construction
5. Shadow tower (class L termination, depth 3)
6. All-plus amplitudes (1-loop, 2-loop, L-loop)
7. MC equation = bootstrap associativity
8. Collinear splitting from shadow r-matrix
9. Soft theorem tower from shadow projections
10. Genus expansion of form factors
11. Costello two-loop comparison
12. Twisted holography bridge (AP24 complementarity)
13. Celestial OPE = genus-0 shadow identification
14. Cross-framework dictionary completeness
15. Full bridge analysis integration
16. Multi-path verification (3+ independent paths per claim)

Ground truth (independently computed):
    kappa(V_k(sl_N)) = (N^2-1)(k+N)/(2N)     [AP1, from definition]
    kappa(Vir_c) = c/2                          [AP1]
    lambda_1^FP = 1/24                          [Faber-Pandharipande]
    lambda_2^FP = 7/5760                        [Faber-Pandharipande]
    lambda_3^FP = 31/967680                     [Faber-Pandharipande]
    S_4(Vir_c) = 10/[c(5c+22)]                 [quartic contact]
    r-matrix pole = OPE pole - 1                [AP19]
    kappa(A) + kappa(A!) = 0 for KM             [AP24]
    class L: S_r = 0 for r >= 4                 [shadow depth 3]
"""

from fractions import Fraction

import pytest

from compute.lib.theorem_costello_form_factor_bridge_engine import (
    # Helpers
    _frac,
    _bernoulli_exact,
    _lambda_fp_exact,
    harmonic,
    # Lie algebra
    LieAlgebraData,
    sl_N_data,
    # Kappa
    kappa_affine_slN,
    central_charge_affine_slN,
    kappa_virasoro,
    # SDYM algebra
    SDYMChiralAlgebra,
    make_sdym_algebra,
    # Quantum OPE
    QuantumOPECorrection,
    one_loop_ope_correction_sdym,
    two_loop_ope_correction_sdym,
    quantum_ope_all_orders,
    # Shadow tower
    shadow_tower_sdym,
    shadow_tower_sdgr_tline,
    # All-plus amplitudes
    AllPlusAmplitude,
    all_plus_amplitude_1loop,
    all_plus_amplitude_2loop,
    all_plus_amplitude_L_loops,
    # MC bootstrap
    MCBootstrapEquivalence,
    verify_mc_bootstrap_genus0,
    mc_residual_at_arity,
    # Collinear splitting
    CollinearSplitting,
    tree_splitting_gluon_pp,
    one_loop_splitting_gluon_pp,
    tree_splitting_graviton_pp,
    # Soft theorems
    SoftTheoremFromShadow,
    soft_theorem_tower_gluon,
    soft_theorem_tower_graviton,
    # Genus expansion
    FormFactorGenusExpansion,
    form_factor_genus_expansion_sdym,
    form_factor_genus_expansion_sdgr,
    # Costello comparison
    CostelloTwoLoopComparison,
    compare_costello_two_loop,
    # Twisted holography
    TwistedHolographyBridge,
    twisted_holography_d3,
    # Celestial OPE
    CelestialOPEShadowIdentification,
    celestial_ope_from_shadow_g0,
    # Full analysis
    full_bridge_analysis,
    # Dictionary
    COSTELLO_SHADOW_DICTIONARY,
    # Verification predicates
    verify_kappa_complementarity_km,
    verify_shadow_tower_terminates_class_L,
    verify_genus_expansion_positivity,
    verify_mc_equation_all_arities,
    verify_loop_genus_identification,
)


# ============================================================================
# 1. Exact arithmetic helpers
# ============================================================================

class TestExactArithmetic:
    """Tests for Bernoulli numbers, lambda_fp, and harmonic numbers."""

    def test_bernoulli_b0(self):
        assert _bernoulli_exact(0) == Fraction(1)

    def test_bernoulli_b1(self):
        assert _bernoulli_exact(1) == Fraction(-1, 2)

    def test_bernoulli_b2(self):
        assert _bernoulli_exact(2) == Fraction(1, 6)

    def test_bernoulli_b4(self):
        assert _bernoulli_exact(4) == Fraction(-1, 30)

    def test_bernoulli_b6(self):
        assert _bernoulli_exact(6) == Fraction(1, 42)

    def test_bernoulli_odd_vanish(self):
        """B_n = 0 for odd n >= 3."""
        for n in [3, 5, 7, 9, 11]:
            assert _bernoulli_exact(n) == Fraction(0)

    def test_lambda_fp_g1(self):
        """lambda_1^FP = 1/24."""
        assert _lambda_fp_exact(1) == Fraction(1, 24)

    def test_lambda_fp_g2(self):
        """lambda_2^FP = 7/5760."""
        assert _lambda_fp_exact(2) == Fraction(7, 5760)

    def test_lambda_fp_g3(self):
        """lambda_3^FP = 31/967680."""
        assert _lambda_fp_exact(3) == Fraction(31, 967680)

    def test_lambda_fp_positive(self):
        """lambda_g^FP > 0 for all g >= 1 (Bernoulli sign pattern)."""
        for g in range(1, 8):
            assert _lambda_fp_exact(g) > 0

    def test_harmonic_h1(self):
        assert harmonic(1) == Fraction(1)

    def test_harmonic_h2(self):
        assert harmonic(2) == Fraction(3, 2)

    def test_harmonic_h3(self):
        assert harmonic(3) == Fraction(11, 6)

    def test_harmonic_h0(self):
        assert harmonic(0) == Fraction(0)


# ============================================================================
# 2. Lie algebra data
# ============================================================================

class TestLieAlgebraData:
    """Tests for sl_N Lie algebra data."""

    @pytest.mark.parametrize("N,dim,rank,hv", [
        (2, 3, 1, 2),
        (3, 8, 2, 3),
        (4, 15, 3, 4),
        (5, 24, 4, 5),
        (6, 35, 5, 6),
    ])
    def test_sl_n_dimensions(self, N, dim, rank, hv):
        g = sl_N_data(N)
        assert g.dim == dim
        assert g.rank == rank
        assert g.dual_coxeter == hv

    def test_sl_n_casimir_adjoint(self):
        """C_2(adj) = 2*h^v for sl_N."""
        for N in range(2, 7):
            g = sl_N_data(N)
            assert g.casimir_adjoint == Fraction(2 * N)

    def test_sl_n_casimir_fundamental(self):
        """C_2(fund) = (N^2-1)/(2N) for sl_N."""
        for N in range(2, 7):
            g = sl_N_data(N)
            assert g.casimir_fundamental == Fraction(N * N - 1, 2 * N)

    def test_sl_1_raises(self):
        with pytest.raises(ValueError):
            sl_N_data(1)


# ============================================================================
# 3. Kappa formulas (AP1 cross-verification, AP9 check)
# ============================================================================

class TestKappaFormulas:
    """Multi-path verification of kappa formulas."""

    @pytest.mark.parametrize("N,k,expected", [
        (2, 0, Fraction(3, 4)),       # (4-1)*2/(2*2) = 3/4? No: (4-1)(0+2)/(2*2) = 3*2/4 = 3/2. Wait:
        # kappa(V_0(sl_2)) = (4-1)(0+2)/(2*2) = 3*2/4 = 6/4 = 3/2
        # Let me recompute: dim=3, k=0, h^v=2. kappa = 3*(0+2)/(2*2) = 6/4 = 3/2
    ])
    def test_kappa_sl2_k0_direct(self, N, k, expected):
        """kappa(V_0(sl_2)) = 3*2/4 = 3/2. Direct computation."""
        # Recompute: dim(sl_2)=3, h^v=2, k=0
        # kappa = 3*(0+2)/(2*2) = 6/4 = 3/2
        result = kappa_affine_slN(2, Fraction(0))
        assert result == Fraction(3, 2)

    def test_kappa_sl2_k0(self):
        """kappa(V_0(sl_2)) = (N^2-1)/2 = 3/2 at k=0."""
        assert kappa_affine_slN(2, Fraction(0)) == Fraction(3, 2)

    def test_kappa_sl3_k0(self):
        """kappa(V_0(sl_3)) = (9-1)/2 = 4 at k=0."""
        # dim=8, h^v=3, k=0. kappa = 8*3/6 = 4
        assert kappa_affine_slN(3, Fraction(0)) == Fraction(4)

    def test_kappa_sl4_k0(self):
        """kappa(V_0(sl_4)) = (16-1)/2 = 15/2 at k=0."""
        # dim=15, h^v=4, k=0. kappa = 15*4/8 = 60/8 = 15/2
        assert kappa_affine_slN(4, Fraction(0)) == Fraction(15, 2)

    def test_kappa_sl2_k1(self):
        """kappa(V_1(sl_2)) = 3*3/4 = 9/4."""
        assert kappa_affine_slN(2, Fraction(1)) == Fraction(9, 4)

    def test_kappa_sl3_k1(self):
        """kappa(V_1(sl_3)) = 8*4/6 = 16/3."""
        assert kappa_affine_slN(3, Fraction(1)) == Fraction(16, 3)

    def test_kappa_not_c_over_2_ap9(self):
        """AP9: kappa(V_k(sl_N)) != c(V_k(sl_N))/2 for N >= 2.

        kappa = dim(g)(k+h^v)/(2h^v)
        c/2 = k*dim(g)/[2(k+h^v)]

        These differ by a factor of (k+h^v)^2 / (h^v * k) when k != 0.
        At k=0: c=0 but kappa = dim(g)/2 != 0.
        """
        for N in range(2, 6):
            k = Fraction(1)
            kap = kappa_affine_slN(N, k)
            c = central_charge_affine_slN(N, k)
            assert kap != c / 2, f"AP9 violation: kappa = c/2 for sl_{N} at k=1"

    def test_kappa_at_k0_c_is_zero(self):
        """At k=0 (self-dual): c = 0 but kappa = dim(g)/2 != 0."""
        for N in range(2, 6):
            c = central_charge_affine_slN(N, Fraction(0))
            kap = kappa_affine_slN(N, Fraction(0))
            assert c == 0, f"c should be 0 at k=0 for sl_{N}"
            assert kap > 0, f"kappa should be > 0 at k=0 for sl_{N}"

    def test_kappa_formula_consistency(self):
        """Cross-check: kappa = dim*(k+h^v)/(2*h^v) via two paths.

        Path 1: direct formula
        Path 2: dim/2 + dim*k/(2*h^v)
        """
        for N in range(2, 7):
            for k_int in range(0, 5):
                k = Fraction(k_int)
                dim_g = N * N - 1
                h_v = N
                path1 = kappa_affine_slN(N, k)
                path2 = Fraction(dim_g) / 2 + Fraction(dim_g) * k / (2 * h_v)
                assert path1 == path2, f"Kappa inconsistency for sl_{N}, k={k}"


# ============================================================================
# 4. SDYM chiral algebra
# ============================================================================

class TestSDYMAlgebra:
    """Tests for the SDYM chiral algebra construction."""

    def test_sdym_sl2_k0_is_self_dual(self):
        alg = make_sdym_algebra(2, k=0)
        assert alg.is_self_dual

    def test_sdym_sl3_k1_not_self_dual(self):
        alg = make_sdym_algebra(3, k=1)
        assert not alg.is_self_dual

    def test_sdym_shadow_class(self):
        """All affine KM algebras are class L (shadow depth 3)."""
        for N in range(2, 6):
            alg = make_sdym_algebra(N)
            assert alg.shadow_class == "L"
            assert alg.shadow_depth == 3

    def test_sdym_kappa_matches(self):
        """Algebra's kappa matches directly computed kappa."""
        for N in range(2, 6):
            alg = make_sdym_algebra(N)
            assert alg.kappa == kappa_affine_slN(N, Fraction(0))


# ============================================================================
# 5. Shadow tower (class L termination)
# ============================================================================

class TestShadowTower:
    """Tests for shadow tower computation and class L termination."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_class_L_terminates(self, N):
        """Class L: S_r = 0 for all r >= 4."""
        tower = shadow_tower_sdym(N, k=0, max_arity=20)
        for r in range(4, 21):
            assert tower[r] == Fraction(0), f"S_{r} != 0 for sl_{N}"

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_s2_equals_kappa(self, N):
        """S_2 = kappa for all algebras."""
        tower = shadow_tower_sdym(N, k=0, max_arity=3)
        assert tower[2] == kappa_affine_slN(N, Fraction(0))

    def test_s3_nonzero(self):
        """S_3 is nonzero for sl_N, N >= 3 (cubic Casimir nonzero)."""
        for N in range(3, 6):
            tower = shadow_tower_sdym(N, k=0, max_arity=4)
            assert tower[3] != Fraction(0), f"S_3 should be nonzero for sl_{N}"

    def test_verify_termination_predicate(self):
        for N in range(2, 6):
            assert verify_shadow_tower_terminates_class_L(N, k=0)

    def test_sdgr_tline_virasoro_s2(self):
        """For SDGR T-line: S_2 = kappa(Vir_c) = c/2."""
        for c_int in [1, 2, 10, 26]:
            c = Fraction(c_int)
            tower = shadow_tower_sdgr_tline(c, max_arity=3)
            assert tower[2] == c / 2

    def test_sdgr_tline_s3(self):
        """For Virasoro: S_3 = 2 (c-independent)."""
        # S_3 = a_1/3 where a_1 = q_1/(2c) = 12c/(2c) = 6.
        # So S_3 = 6/3 = 2.
        for c_int in [1, 2, 5, 10, 26]:
            c = Fraction(c_int)
            tower = shadow_tower_sdgr_tline(c, max_arity=4)
            assert tower[3] == Fraction(2), f"S_3 != 2 at c={c}"

    def test_sdgr_tline_s4_quartic_contact(self):
        """For Virasoro: S_4 = 10/[c(5c+22)] (quartic contact invariant)."""
        for c_int in [1, 2, 5, 10, 26]:
            c = Fraction(c_int)
            tower = shadow_tower_sdgr_tline(c, max_arity=5)
            expected = Fraction(10) / (c * (5 * c + 22))
            assert tower[4] == expected, f"S_4 mismatch at c={c}"


# ============================================================================
# 6. All-plus amplitudes
# ============================================================================

class TestAllPlusAmplitudes:
    """Tests for all-plus amplitude computation."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_1loop_kappa_positive(self, N):
        amp = all_plus_amplitude_1loop(4, N)
        assert amp.kappa > 0
        assert amp.free_energy_contribution > 0

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_1loop_F1_equals_kappa_over_24(self, N):
        """F_1 = kappa/24."""
        amp = all_plus_amplitude_1loop(4, N)
        assert amp.free_energy_contribution == amp.kappa / 24

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_2loop_F2_positive(self, N):
        amp = all_plus_amplitude_2loop(4, N)
        assert amp.free_energy_contribution > 0

    def test_2loop_F2_formula(self):
        """F_2 = kappa * 7/5760 for SU(2)."""
        amp = all_plus_amplitude_2loop(4, 2)
        expected = Fraction(3, 2) * Fraction(7, 5760)
        assert amp.free_energy_contribution == expected

    def test_L_loop_genus_L(self):
        """The L-loop amplitude sits at genus L."""
        for L in range(1, 5):
            amp = all_plus_amplitude_L_loops(4, 3, L)
            assert amp.loop_order == L

    def test_positivity_all_loops(self):
        """F_L > 0 for all L >= 1 (kappa > 0 and lambda_fp > 0)."""
        for N in range(2, 5):
            assert verify_genus_expansion_positivity(N, max_genus=6)


# ============================================================================
# 7. MC equation = bootstrap associativity
# ============================================================================

class TestMCBootstrap:
    """Tests verifying MC equation = Costello/Fernandez-Paquette bootstrap."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_mc_residual_vanishes_all_arities(self, N):
        """MC residual = 0 at all arities >= 5 (class L tower)."""
        assert verify_mc_equation_all_arities(N, max_arity=15)

    def test_mc_bootstrap_genus0_verified(self):
        """All MC bootstrap equivalences verified at genus 0."""
        for N in range(2, 5):
            checks = verify_mc_bootstrap_genus0(N, max_arity=10)
            for check in checks:
                assert check.verified, (
                    f"MC bootstrap failed at arity {check.arity} for sl_{N}: "
                    f"residual = {check.mc_residual}"
                )

    def test_mc_arity3_is_jacobi(self):
        """Arity-3 MC equation = Jacobi identity / CYBE."""
        checks = verify_mc_bootstrap_genus0(3, max_arity=4)
        jacobi = [c for c in checks if c.arity == 3][0]
        assert "Jacobi" in jacobi.physical_interpretation

    def test_mc_sdgr_virasoro_tower(self):
        """MC residual vanishes for the Virasoro shadow tower (class M)."""
        for c_int in [1, 2, 10, 26]:
            c = Fraction(c_int)
            tower = shadow_tower_sdgr_tline(c, max_arity=15)
            for r in range(5, 16):
                residual = mc_residual_at_arity(r, tower)
                assert residual == 0, f"MC residual nonzero at arity {r}, c={c}"


# ============================================================================
# 8. Collinear splitting from shadow r-matrix
# ============================================================================

class TestCollinearSplitting:
    """Tests for collinear splitting functions."""

    def test_tree_gluon_pp_simple_pole(self):
        """Tree-level gluon ++ -> + has a simple pole."""
        split = tree_splitting_gluon_pp(3)
        assert split.pole_order == 1
        assert split.loop_order == 0

    def test_one_loop_gluon_pp_level_shift(self):
        """One-loop gluon splitting: coefficient = h^v = N."""
        for N in range(2, 6):
            split = one_loop_splitting_gluon_pp(N)
            assert split.coefficient == Fraction(N)
            assert split.loop_order == 1

    def test_tree_graviton_pp_pole_3(self):
        """Tree-level graviton ++ -> + has leading pole z^{-3} (AP19)."""
        split = tree_splitting_graviton_pp(Fraction(26))
        assert split.pole_order == 3

    def test_graviton_coefficient_c_over_2(self):
        """Graviton splitting leading coefficient = c/2."""
        for c_int in [1, 2, 10, 26]:
            c = Fraction(c_int)
            split = tree_splitting_graviton_pp(c)
            assert split.coefficient == c / 2


# ============================================================================
# 9. Soft theorem tower
# ============================================================================

class TestSoftTheoremTower:
    """Tests for soft theorem extraction from shadow projections."""

    def test_gluon_soft_leading_from_kappa(self):
        """Leading soft gluon theorem comes from S_2 = kappa."""
        for N in range(2, 5):
            tower = soft_theorem_tower_gluon(N)
            leading = tower[0]
            assert leading.order == 0
            assert leading.shadow_arity == 2
            assert leading.shadow_value == kappa_affine_slN(N, Fraction(0))

    def test_gluon_soft_vanishes_beyond_class_L(self):
        """For class L: soft theorems at order >= 2 have S_r = 0."""
        for N in range(2, 5):
            tower = soft_theorem_tower_gluon(N, max_order=5)
            for soft in tower:
                if soft.order >= 2:
                    assert soft.shadow_value == 0

    def test_graviton_soft_s0_from_kappa(self):
        """Leading soft graviton = supertranslation from kappa = c/2."""
        c = Fraction(26)
        tower = soft_theorem_tower_graviton(c, max_order=3)
        assert tower[0].shadow_value == c / 2

    def test_graviton_soft_s1_universal(self):
        """Subleading soft graviton: S_3 = 2 (c-independent)."""
        for c_int in [1, 10, 26]:
            c = Fraction(c_int)
            tower = soft_theorem_tower_graviton(c)
            assert tower[1].shadow_value == Fraction(2)

    def test_graviton_soft_s2_quartic(self):
        """Sub-subleading soft graviton: S_4 = 10/[c(5c+22)]."""
        c = Fraction(10)
        tower = soft_theorem_tower_graviton(c, max_order=3)
        expected = Fraction(10) / (c * (5 * c + 22))
        assert tower[2].shadow_value == expected


# ============================================================================
# 10. Genus expansion of form factors
# ============================================================================

class TestGenusExpansion:
    """Tests for genus expansion of form factors."""

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_genus1_scalar(self, N):
        """F_1 = kappa * lambda_1 = kappa/24."""
        exp = form_factor_genus_expansion_sdym(N, max_genus=1)
        f1 = exp[0]
        assert f1.genus == 1
        assert f1.scalar_contribution == f1.kappa / 24

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_genus2_with_planted_forest(self, N):
        """F_2 = kappa*lambda_2 + delta_pf^{(2)} for class L."""
        exp = form_factor_genus_expansion_sdym(N, max_genus=2)
        f2 = exp[1]
        assert f2.genus == 2
        assert f2.total == f2.scalar_contribution + f2.planted_forest_correction

    def test_genus_expansion_positive_all_N(self):
        """F_g > 0 at the scalar level for all N >= 2, g >= 1."""
        for N in range(2, 6):
            exp = form_factor_genus_expansion_sdym(N, max_genus=5)
            for fg in exp:
                assert fg.scalar_contribution > 0, (
                    f"F_{fg.genus} scalar < 0 for sl_{N}"
                )

    def test_sdgr_genus1(self):
        """SDGR genus-1: F_1 = c/48."""
        c = Fraction(26)
        exp = form_factor_genus_expansion_sdgr(c, max_genus=1)
        f1 = exp[0]
        assert f1.scalar_contribution == c / 2 * Fraction(1, 24)
        assert f1.scalar_contribution == Fraction(26, 48)


# ============================================================================
# 11. Costello two-loop comparison
# ============================================================================

class TestCostelloComparison:
    """Tests comparing shadow tower with Costello's results."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_costello_matches(self, N):
        """The shadow tower reproduces Costello's two-loop result."""
        result = compare_costello_two_loop(N)
        assert result.costello_matches_shadow

    def test_F2_shadow_exact_sl2(self):
        """F_2 for SU(2): kappa * 7/5760 = (3/2)(7/5760) = 21/11520 = 7/3840."""
        result = compare_costello_two_loop(2)
        expected = Fraction(3, 2) * Fraction(7, 5760)
        assert result.F_2_shadow == expected
        assert expected == Fraction(7, 3840)

    def test_F2_shadow_exact_sl3(self):
        """F_2 for SU(3): kappa * 7/5760 = 4 * 7/5760 = 7/1440."""
        result = compare_costello_two_loop(3)
        expected = Fraction(4) * Fraction(7, 5760)
        assert result.F_2_shadow == expected

    def test_total_genus2_includes_planted_forest(self):
        """Total genus-2 includes planted-forest correction."""
        result = compare_costello_two_loop(3)
        assert result.total_genus_2 == result.F_2_shadow + result.delta_pf_2


# ============================================================================
# 12. Twisted holography bridge (AP24)
# ============================================================================

class TestTwistedHolography:
    """Tests for the twisted holography bridge."""

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
    def test_kappa_complementarity_ap24(self, N):
        """AP24: kappa(A) + kappa(A!) = 0 for KM families."""
        bridge = twisted_holography_d3(N)
        assert bridge.anomaly_cancellation, (
            f"AP24 violated for sl_{N}: kappa + kappa_dual = "
            f"{bridge.kappa + bridge.kappa_dual}"
        )

    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_verify_complementarity_predicate(self, N):
        """Verify kappa complementarity via the predicate function."""
        assert verify_kappa_complementarity_km(N, Fraction(1))
        assert verify_kappa_complementarity_km(N, Fraction(0))
        assert verify_kappa_complementarity_km(N, Fraction(5))

    def test_feigin_frenkel_dual_level(self):
        """Feigin-Frenkel: k' = -k - 2h^v."""
        bridge = twisted_holography_d3(3)
        expected_dual = -Fraction(1) - 2 * 3  # = -7
        assert bridge.koszul_dual_level == expected_dual

    def test_d3_boundary_algebra(self):
        """D3 brane boundary algebra is V_1(sl_N)."""
        bridge = twisted_holography_d3(4)
        assert bridge.level == Fraction(1)


# ============================================================================
# 13. Celestial OPE = genus-0 shadow
# ============================================================================

class TestCelestialOPEIdentification:
    """Tests for the celestial OPE <-> shadow identification."""

    def test_genus0_arity2_is_kappa(self):
        """At genus 0, arity 2: shadow value = kappa."""
        for N in range(2, 5):
            ident = celestial_ope_from_shadow_g0(N, k=0)
            assert ident.shadow_value == kappa_affine_slN(N, Fraction(0))

    def test_self_dual_single_pole(self):
        """At k=0 (self-dual): OPE has only simple pole."""
        ident = celestial_ope_from_shadow_g0(3, k=0)
        assert ident.ope_pole_order == 1

    def test_non_self_dual_double_pole(self):
        """At k != 0: OPE has double pole."""
        ident = celestial_ope_from_shadow_g0(3, k=1)
        assert ident.ope_pole_order == 2

    def test_identification_verified(self):
        for N in range(2, 5):
            ident = celestial_ope_from_shadow_g0(N)
            assert ident.identification_verified


# ============================================================================
# 14. Cross-framework dictionary
# ============================================================================

class TestDictionary:
    """Tests for the Costello-shadow dictionary completeness."""

    def test_dictionary_nonempty(self):
        assert len(COSTELLO_SHADOW_DICTIONARY) > 0

    def test_key_entries_present(self):
        required_keys = [
            "celestial_chiral_algebra",
            "collinear_OPE",
            "splitting_function",
            "bootstrap_associativity",
            "all_plus_at_L_loops",
        ]
        for key in required_keys:
            assert key in COSTELLO_SHADOW_DICTIONARY, f"Missing key: {key}"

    def test_dictionary_values_nonempty(self):
        for key, val in COSTELLO_SHADOW_DICTIONARY.items():
            assert len(val) > 0, f"Empty value for key: {key}"


# ============================================================================
# 15. Full bridge analysis integration
# ============================================================================

class TestFullBridgeAnalysis:
    """Integration tests for the full bridge analysis."""

    def test_full_analysis_runs(self):
        """Full analysis completes without error for SU(2)."""
        result = full_bridge_analysis(2)
        assert "algebra" in result
        assert "shadow_tower" in result
        assert "amplitudes" in result

    def test_full_analysis_sl3(self):
        result = full_bridge_analysis(3, max_genus=2, max_arity=6)
        assert result["algebra"]["N"] == 3
        assert result["algebra"]["shadow_class"] == "L"

    def test_full_analysis_kappa_consistency(self):
        """Kappa in the full analysis matches direct computation."""
        for N in range(2, 5):
            result = full_bridge_analysis(N)
            assert result["algebra"]["kappa"] == kappa_affine_slN(N, Fraction(0))

    def test_full_analysis_costello_comparison(self):
        result = full_bridge_analysis(3)
        assert result["costello_comparison"].costello_matches_shadow

    def test_full_analysis_twisted_holography(self):
        result = full_bridge_analysis(4)
        assert result["twisted_holography"].anomaly_cancellation


# ============================================================================
# 16. Multi-path verification (3+ paths per claim)
# ============================================================================

class TestMultiPathVerification:
    """Multi-path verification of key claims (verification mandate: 3+ paths)."""

    def test_kappa_3_paths(self):
        """kappa(V_0(sl_3)) via 3 independent paths.

        Path 1: direct formula kappa = dim*(k+h^v)/(2h^v) = 8*3/6 = 4
        Path 2: kappa = (N^2-1)/2 at k=0 = 8/2 = 4
        Path 3: S_2 from shadow tower = 4
        """
        N = 3
        # Path 1: direct formula
        path1 = Fraction(8) * (0 + 3) / (2 * 3)
        # Path 2: simplified formula at k=0
        path2 = Fraction(N * N - 1, 2)
        # Path 3: from shadow tower
        tower = shadow_tower_sdym(N, k=0, max_arity=3)
        path3 = tower[2]

        assert path1 == Fraction(4)
        assert path2 == Fraction(4)
        assert path3 == Fraction(4)
        assert path1 == path2 == path3

    def test_F1_3_paths(self):
        """F_1(SDYM, SU(3)) via 3 paths.

        Path 1: kappa/24 = 4/24 = 1/6
        Path 2: kappa * lambda_1 = 4 * 1/24 = 1/6
        Path 3: from all_plus_amplitude_1loop
        """
        N = 3
        kap = kappa_affine_slN(N, Fraction(0))

        path1 = kap / 24
        path2 = kap * _lambda_fp_exact(1)
        path3 = all_plus_amplitude_1loop(4, N).free_energy_contribution

        assert path1 == Fraction(1, 6)
        assert path2 == Fraction(1, 6)
        assert path3 == Fraction(1, 6)

    def test_class_L_termination_3_paths(self):
        """Class L termination via 3 paths.

        Path 1: shadow_tower_sdym returns 0 for r >= 4
        Path 2: verify_shadow_tower_terminates_class_L predicate
        Path 3: mc_residual vanishes at all arities
        """
        N = 3
        # Path 1
        tower = shadow_tower_sdym(N, k=0, max_arity=10)
        path1 = all(tower[r] == 0 for r in range(4, 11))

        # Path 2
        path2 = verify_shadow_tower_terminates_class_L(N)

        # Path 3
        path3 = verify_mc_equation_all_arities(N, max_arity=10)

        assert path1
        assert path2
        assert path3

    def test_complementarity_3_paths(self):
        """AP24 complementarity via 3 paths for sl_3.

        Path 1: direct computation kappa(k) + kappa(-k-2h^v) = 0
        Path 2: twisted_holography_d3 anomaly_cancellation
        Path 3: verify_kappa_complementarity_km predicate
        """
        N = 3
        k = Fraction(1)

        # Path 1
        k_dual = -k - 2 * N
        path1 = kappa_affine_slN(N, k) + kappa_affine_slN(N, k_dual) == 0

        # Path 2
        bridge = twisted_holography_d3(N)
        path2 = bridge.anomaly_cancellation

        # Path 3
        path3 = verify_kappa_complementarity_km(N, k)

        assert path1
        assert path2
        assert path3

    def test_virasoro_s3_universality_3_paths(self):
        """S_3(Vir_c) = 2 for all c, via 3 paths.

        Path 1: shadow_tower at c=1
        Path 2: shadow_tower at c=26
        Path 3: direct computation a_1/3 = (12c/(2c))/3 = 6/3 = 2
        """
        # Path 1
        tower_1 = shadow_tower_sdgr_tline(Fraction(1))
        path1 = tower_1[3]

        # Path 2
        tower_26 = shadow_tower_sdgr_tline(Fraction(26))
        path2 = tower_26[3]

        # Path 3: a_1 = q_1/(2*c) = 12c/(2c) = 6, S_3 = a_1/3 = 2
        path3 = Fraction(6, 3)

        assert path1 == Fraction(2)
        assert path2 == Fraction(2)
        assert path3 == Fraction(2)

    def test_loop_genus_identification_3_paths(self):
        """Loop-genus identification for L=1, SU(3), via 3 paths.

        Path 1: verify_loop_genus_identification
        Path 2: all_plus_amplitude_1loop
        Path 3: genus expansion F_1
        """
        N = 3
        # Path 1
        ident = verify_loop_genus_identification(N, 1)
        path1 = ident["F_L"]

        # Path 2
        amp = all_plus_amplitude_1loop(4, N)
        path2 = amp.free_energy_contribution

        # Path 3
        exp = form_factor_genus_expansion_sdym(N, max_genus=1)
        path3 = exp[0].scalar_contribution

        assert path1 == path2 == path3


# ============================================================================
# 17. Quantum OPE corrections
# ============================================================================

class TestQuantumOPE:
    """Tests for quantum-corrected OPE (loop-level deformation)."""

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_one_loop_correction_level_hv(self, N):
        """One-loop OPE correction has effective level = h^v = N."""
        corrections = one_loop_ope_correction_sdym(N)
        assert len(corrections) == 1
        assert corrections[0].coefficient == Fraction(N)
        assert corrections[0].loop_order == 1
        assert corrections[0].pole_order == 2

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_two_loop_correction_exists(self, N):
        """Two-loop OPE correction is nonzero."""
        corrections = two_loop_ope_correction_sdym(N)
        assert len(corrections) >= 1
        assert corrections[0].loop_order == 2

    def test_all_orders_ope_consistent(self):
        """Quantum OPE at all orders is consistent (coefficients positive)."""
        N = 3
        ope = quantum_ope_all_orders(N, max_loop=4)
        for L, corrections in ope.items():
            assert L >= 1
            for corr in corrections:
                assert corr.loop_order == L
                assert corr.coefficient > 0


# ============================================================================
# 18. Edge cases and error handling
# ============================================================================

class TestEdgeCases:
    """Tests for edge cases and error handling."""

    def test_sl_1_raises(self):
        with pytest.raises(ValueError):
            sl_N_data(1)

    def test_critical_level_raises(self):
        with pytest.raises(ValueError):
            central_charge_affine_slN(3, Fraction(-3))

    def test_sdgr_c0_raises(self):
        with pytest.raises(ValueError):
            shadow_tower_sdgr_tline(Fraction(0))

    def test_sdgr_c_minus_22_over_5_raises(self):
        with pytest.raises(ValueError):
            shadow_tower_sdgr_tline(Fraction(-22, 5))

    def test_loop_order_0_raises(self):
        with pytest.raises(ValueError):
            all_plus_amplitude_L_loops(4, 3, 0)

    def test_lambda_fp_g0_raises(self):
        with pytest.raises(ValueError):
            _lambda_fp_exact(0)
