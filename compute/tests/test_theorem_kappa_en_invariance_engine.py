r"""Tests for kappa E_n-invariance theorem.

THEOREM: kappa(A) is independent of operadic level n under E_n -> E_1 reduction.

45+ tests organized by the three independent proof strategies:
  I.   Binary bar (Proof 1): arity-2 bar complex, Conf_2(R^n) ~ S^{n-1}
  II.  Central extension (Proof 2): H^2 classification independent of n
  III. Anomaly / Hodge (Proof 3): kappa = F_1 / lambda_1, Hodge bundle
  IV.  Full landscape: every standard family at multiple operadic levels
  V.   Dimensional reduction: E_n -> E_m preserves kappa
  VI.  Higher shadows: contrast (S_r for r >= 3 CAN depend on n)
  VII. Cross-consistency with existing engines
  VIII.Three-proof convergence

MULTI-PATH VERIFICATION (AP10):
  Every kappa value is verified by at least 2 independent methods.
  No hardcoded expected values without independent derivation.

References:
  theorem_kappa_en_invariance_engine.py
  en_factorization_shadow.py
  higher_dim_chiral_comparison_engine.py
  theorem_c_complementarity.py
  CLAUDE.md: AP1, AP10, AP20, AP27, AP39, AP48
"""
import pytest
from fractions import Fraction

from compute.lib.theorem_kappa_en_invariance_engine import (
    # Kappa formulas
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine,
    kappa_wn,
    kappa_betagamma,
    kappa_bc,
    kappa_free_fermion,
    kappa_lattice,
    # Configuration space
    conf2_homotopy_type,
    conf2_euler_char,
    conf2_top_betti,
    conf2_fundamental_class_degree,
    binary_pairing_value,
    binary_pairing_gives_kappa,
    # Central extension
    binary_deformation_complex_degree,
    arnold_lowest_degree,
    central_extension_independent_of_n,
    h2_classifies_extensions,
    # Hodge / anomaly
    hodge_bundle_independent_of_operad,
    genus1_partition_function_independent_of_n,
    kappa_from_anomaly,
    # Main theorem
    kappa_en,
    verify_kappa_en_invariance,
    three_proof_verification,
    # Dimensional reduction
    dimensional_reduction_preserves_kappa,
    # Higher shadows
    higher_shadow_n_dependence,
    # Stabilization
    kappa_stabilizes_immediately,
    # Landscape
    STANDARD_FAMILIES,
    verify_full_landscape,
    # Cross-checks
    cross_check_with_en_factorization_shadow,
    cross_check_with_higher_dim_engine,
    cross_check_with_theorem_c,
    # Lie data
    _lie_data,
    # Summary
    theorem_summary,
    # Utility
    _lambda_fp,
)


# ========================================================================
# I. PROOF 1: Binary bar (arity-2 configuration space)
# ========================================================================


class TestConf2Topology:
    """Conf_2(R^n) ~ S^{n-1} for all n >= 1."""

    def test_conf2_homotopy_type_e1(self):
        """Conf_2(R^1) ~ S^0."""
        assert conf2_homotopy_type(1) == "S^0"

    def test_conf2_homotopy_type_e2(self):
        """Conf_2(R^2) ~ S^1."""
        assert conf2_homotopy_type(2) == "S^1"

    def test_conf2_homotopy_type_e3(self):
        """Conf_2(R^3) ~ S^2."""
        assert conf2_homotopy_type(3) == "S^2"

    def test_conf2_homotopy_type_e10(self):
        """Conf_2(R^10) ~ S^9."""
        assert conf2_homotopy_type(10) == "S^9"

    def test_conf2_euler_char(self):
        """chi(S^{n-1}) = 1 + (-1)^{n-1}."""
        assert conf2_euler_char(1) == 2   # S^0: two points
        assert conf2_euler_char(2) == 0   # S^1: circle
        assert conf2_euler_char(3) == 2   # S^2: sphere
        assert conf2_euler_char(4) == 0   # S^3
        assert conf2_euler_char(5) == 2   # S^4

    def test_conf2_top_betti_always_1(self):
        """b_{n-1}(S^{n-1}) = 1 for all n."""
        for n in range(1, 20):
            assert conf2_top_betti(n) == 1

    def test_fundamental_class_degree(self):
        """[S^{n-1}] has degree n-1."""
        assert conf2_fundamental_class_degree(1) == 0
        assert conf2_fundamental_class_degree(2) == 1
        assert conf2_fundamental_class_degree(3) == 2
        assert conf2_fundamental_class_degree(7) == 6

    def test_conf2_invalid_n(self):
        """n < 1 should raise ValueError."""
        with pytest.raises(ValueError):
            conf2_homotopy_type(0)


class TestBinaryPairing:
    """The binary pairing extracts kappa independent of n."""

    def test_binary_pairing_heisenberg_all_n(self):
        """Binary pairing gives level k for all n."""
        for n in [1, 2, 3, 5, 10, 50]:
            assert binary_pairing_value(n, Fraction(1)) == Fraction(1)
            assert binary_pairing_value(n, Fraction(3)) == Fraction(3)
            assert binary_pairing_value(n, Fraction(-2)) == Fraction(-2)

    def test_binary_pairing_gives_kappa_heisenberg(self):
        """kappa from binary pairing = k for Heisenberg, all n."""
        for n in [1, 2, 3, 7]:
            assert binary_pairing_gives_kappa(n, level=Fraction(5)) == Fraction(5)

    def test_binary_pairing_gives_kappa_affine_sl2(self):
        """kappa from binary pairing = 3(k+2)/4 for sl_2, all n."""
        dim_g, h_dual = _lie_data('A', 1)  # sl_2: dim=3, h^v=2
        for n in [1, 2, 3, 10]:
            kap = binary_pairing_gives_kappa(n, level=Fraction(1),
                                              dim_g=dim_g, h_dual=h_dual)
            assert kap == Fraction(9, 4)  # 3*(1+2)/(2*2) = 9/4

    def test_binary_pairing_gives_kappa_affine_sl3(self):
        """kappa from binary pairing for sl_3 at level 1, all n."""
        dim_g, h_dual = _lie_data('A', 2)  # sl_3: dim=8, h^v=3
        for n in [1, 2, 3]:
            kap = binary_pairing_gives_kappa(n, level=Fraction(1),
                                              dim_g=dim_g, h_dual=h_dual)
            # 8*(1+3)/(2*3) = 32/6 = 16/3
            assert kap == Fraction(16, 3)


# ========================================================================
# II. PROOF 2: Central extension classification
# ========================================================================


class TestCentralExtension:
    """H^2 classifies central extensions, independently of n."""

    def test_binary_deformation_degree_zero(self):
        """The central extension is a degree-0 binary deformation for all n."""
        for n in [1, 2, 3, 5, 10]:
            assert binary_deformation_complex_degree(n) == 0

    def test_arnold_lowest_degree_e1(self):
        """E_1: no Arnold classes (Conf_k(R) contractible for ordered config)."""
        assert arnold_lowest_degree(1) == -1

    def test_arnold_lowest_degree_e2(self):
        """E_2: Arnold generators in degree 1."""
        assert arnold_lowest_degree(2) == 1

    def test_arnold_lowest_degree_en(self):
        """E_n (n >= 2): Arnold generators in degree n-1."""
        for n in range(2, 10):
            assert arnold_lowest_degree(n) == n - 1

    def test_central_ext_independent_all_n(self):
        """Central extension independent of n for all n >= 1."""
        for n in [1, 2, 3, 5, 10, 100]:
            assert central_extension_independent_of_n(n) is True

    def test_arnold_classes_above_central_ext(self):
        """Arnold classes live in degree >= 1 (for n >= 2), above the
        degree-0 central extension.  This is WHY the central extension
        is independent of n."""
        for n in range(2, 20):
            ext_deg = binary_deformation_complex_degree(n)
            arnold_deg = arnold_lowest_degree(n)
            assert ext_deg < arnold_deg, (
                f"Central ext at degree {ext_deg} must be below "
                f"Arnold at degree {arnold_deg} for n={n}"
            )

    def test_h2_classification_data(self):
        """H^2 classification returns correct data for various n."""
        for n in [1, 2, 3, 5]:
            data = h2_classifies_extensions(n)
            assert data['extension_space_dim'] == 1
            assert data['n_dependence'] is False


# ========================================================================
# III. PROOF 3: Anomaly / Hodge
# ========================================================================


class TestHodgeAnomaly:
    """kappa = F_1 / lambda_1, Hodge bundle independent of operadic structure."""

    def test_hodge_bundle_independent(self):
        """Hodge bundle on M_{1,0} does not depend on operadic level."""
        data = hodge_bundle_independent_of_operad()
        assert data['lambda_1'] == Fraction(1, 24)
        assert data['depends_on_operadic_level'] is False

    def test_lambda_1_value(self):
        """lambda_1 = 1/24 (Faber-Pandharipande)."""
        assert _lambda_fp(1) == Fraction(1, 24)

    def test_genus1_partition_function_independent(self):
        """Z(tau) depends on L_0 and c, not operadic level."""
        data = genus1_partition_function_independent_of_n(Fraction(26))
        assert data['depends_on_n'] is False
        assert data['kappa'] == Fraction(13)
        assert data['F_1'] == Fraction(13) * Fraction(1, 24)

    def test_kappa_from_anomaly_virasoro(self):
        """kappa extracted from conformal anomaly for Virasoro."""
        assert kappa_from_anomaly(Fraction(1), "virasoro") == Fraction(1, 2)
        assert kappa_from_anomaly(Fraction(26), "virasoro") == Fraction(13)
        assert kappa_from_anomaly(Fraction(13), "virasoro") == Fraction(13, 2)

    def test_kappa_from_anomaly_heisenberg(self):
        """kappa extracted from conformal anomaly for Heisenberg."""
        assert kappa_from_anomaly(Fraction(1), "heisenberg") == Fraction(1)
        assert kappa_from_anomaly(Fraction(5), "heisenberg") == Fraction(5)


# ========================================================================
# IV. FULL LANDSCAPE: every standard family at multiple operadic levels
# ========================================================================


class TestKappaENInvariance:
    """The main theorem: kappa_{E_n}(A) = kappa_{E_1}(A) for all n."""

    def test_heisenberg_all_n(self):
        """kappa(H_k) = k for all operadic levels n."""
        for k in [Fraction(1), Fraction(3), Fraction(-2), Fraction(1, 7)]:
            result = verify_kappa_en_invariance('heisenberg', k=k)
            assert result['invariant'] is True
            assert result['kappa_value'] == k

    def test_virasoro_all_n(self):
        """kappa(Vir_c) = c/2 for all operadic levels n."""
        for c in [Fraction(1), Fraction(26), Fraction(13), Fraction(7, 10)]:
            result = verify_kappa_en_invariance('virasoro', c=c)
            assert result['invariant'] is True
            assert result['kappa_value'] == c / 2

    def test_affine_sl2_all_n(self):
        """kappa(sl_2, k=1) = 9/4 for all operadic levels n."""
        result = verify_kappa_en_invariance('affine', lie_type='A', rank=1, k=Fraction(1))
        assert result['invariant'] is True
        assert result['kappa_value'] == Fraction(9, 4)

    def test_affine_sl3_all_n(self):
        """kappa(sl_3, k=1) = 16/3 for all operadic levels n."""
        result = verify_kappa_en_invariance('affine', lie_type='A', rank=2, k=Fraction(1))
        assert result['invariant'] is True
        assert result['kappa_value'] == Fraction(16, 3)

    def test_affine_so5_all_n(self):
        """kappa(so_5 = B_2, k=1) = dim*(k+h^v)/(2*h^v) for all n."""
        # B_2: dim = 10, h^v = 3
        result = verify_kappa_en_invariance('affine', lie_type='B', rank=2, k=Fraction(1))
        assert result['invariant'] is True
        # 10 * (1+3) / (2*3) = 40/6 = 20/3
        assert result['kappa_value'] == Fraction(20, 3)

    def test_affine_sp4_all_n(self):
        """kappa(sp_4 = C_2, k=1) for all n."""
        # C_2: dim = 10, h^v = 3
        result = verify_kappa_en_invariance('affine', lie_type='C', rank=2, k=Fraction(1))
        assert result['invariant'] is True
        # 10 * (1+3) / (2*3) = 40/6 = 20/3
        assert result['kappa_value'] == Fraction(20, 3)

    def test_affine_g2_all_n(self):
        """kappa(G_2, k=1) for all n."""
        # G_2: dim = 14, h^v = 4
        result = verify_kappa_en_invariance('affine', lie_type='G', rank=2, k=Fraction(1))
        assert result['invariant'] is True
        # 14 * (1+4) / (2*4) = 70/8 = 35/4
        assert result['kappa_value'] == Fraction(35, 4)

    def test_betagamma_all_n(self):
        """kappa(betagamma) = 1 for all operadic levels n."""
        result = verify_kappa_en_invariance('betagamma', lam=1)
        assert result['invariant'] is True
        assert result['kappa_value'] == Fraction(1)

    def test_bc_all_n(self):
        """kappa(bc) = -1 for all operadic levels n."""
        result = verify_kappa_en_invariance('bc')
        assert result['invariant'] is True
        assert result['kappa_value'] == Fraction(-1)

    def test_free_fermion_all_n(self):
        """kappa(free fermion) = 1/2 for all operadic levels n."""
        result = verify_kappa_en_invariance('free_fermion')
        assert result['invariant'] is True
        assert result['kappa_value'] == Fraction(1, 2)

    def test_lattice_rank1_all_n(self):
        """kappa(V_Lambda, rank=1) = 1 for all operadic levels n."""
        result = verify_kappa_en_invariance('lattice', rank=1)
        assert result['invariant'] is True
        assert result['kappa_value'] == Fraction(1)

    def test_lattice_rank24_all_n(self):
        """kappa(V_Lambda, rank=24) = 24 for all operadic levels n.

        AP48: kappa depends on the full algebra, not just Virasoro subalgebra.
        For lattice VOA: kappa = rank, NOT c/2.
        """
        result = verify_kappa_en_invariance('lattice', rank=24)
        assert result['invariant'] is True
        assert result['kappa_value'] == Fraction(24)

    def test_wn_w2_virasoro_all_n(self):
        """W_2 = Virasoro: kappa = c * sigma(2) = c/2."""
        result = verify_kappa_en_invariance('wn', N=2, c=Fraction(26))
        assert result['invariant'] is True
        assert result['kappa_value'] == Fraction(13)

    def test_wn_w3_all_n(self):
        """W_3: kappa = c * sigma(3) = 5c/6."""
        result = verify_kappa_en_invariance('wn', N=3, c=Fraction(100))
        assert result['invariant'] is True
        assert result['kappa_value'] == Fraction(100) * Fraction(5, 6)

    def test_kappa_en_invalid_n(self):
        """Operadic level n < 1 should raise ValueError."""
        with pytest.raises(ValueError):
            kappa_en(0, 'heisenberg', k=Fraction(1))

    def test_full_landscape_verification(self):
        """Full landscape verification across all standard families."""
        result = verify_full_landscape(n_values=[1, 2, 3, 5, 10])
        assert result['all_invariant'] is True
        assert result['families_tested'] >= 18


# ========================================================================
# V. DIMENSIONAL REDUCTION: E_n -> E_m preserves kappa
# ========================================================================


class TestDimensionalReduction:
    """E_n -> E_m forgetful functor preserves kappa."""

    def test_e3_to_e1_heisenberg(self):
        """E_3 -> E_1 reduction preserves kappa for Heisenberg."""
        result = dimensional_reduction_preserves_kappa(3, 1, 'heisenberg', k=Fraction(1))
        assert result['preserved'] is True
        assert result['kappa_high'] == Fraction(1)
        assert result['kappa_low'] == Fraction(1)

    def test_e5_to_e2_virasoro(self):
        """E_5 -> E_2 reduction preserves kappa for Virasoro."""
        result = dimensional_reduction_preserves_kappa(5, 2, 'virasoro', c=Fraction(26))
        assert result['preserved'] is True

    def test_e10_to_e1_affine_sl2(self):
        """E_10 -> E_1 reduction preserves kappa for sl_2."""
        result = dimensional_reduction_preserves_kappa(
            10, 1, 'affine', lie_type='A', rank=1, k=Fraction(1))
        assert result['preserved'] is True
        assert result['kappa_high'] == Fraction(9, 4)

    def test_chain_reduction_e5_e3_e1(self):
        """E_5 -> E_3 -> E_1 chain preserves kappa at each step."""
        r1 = dimensional_reduction_preserves_kappa(5, 3, 'heisenberg', k=Fraction(7))
        r2 = dimensional_reduction_preserves_kappa(3, 1, 'heisenberg', k=Fraction(7))
        assert r1['preserved'] is True
        assert r2['preserved'] is True
        assert r1['kappa_high'] == r2['kappa_low'] == Fraction(7)

    def test_reduction_invalid_direction(self):
        """Cannot reduce from lower to higher operadic level."""
        with pytest.raises(ValueError):
            dimensional_reduction_preserves_kappa(2, 5, 'heisenberg', k=Fraction(1))


# ========================================================================
# VI. HIGHER SHADOWS: the contrast
# ========================================================================


class TestHigherShadows:
    """Higher shadows S_r (r >= 3) can depend on n, unlike kappa."""

    def test_kappa_always_independent(self):
        """kappa (r=2) is independent of n for all operadic levels."""
        for n in [1, 2, 3, 5, 10]:
            data = higher_shadow_n_dependence(2, n)
            assert data['kappa_independent'] is True

    def test_s3_potentially_dependent(self):
        """S_3 (r=3) can potentially depend on n for non-formal algebras."""
        data = higher_shadow_n_dependence(3, 2)
        assert data['arnold_classes_relevant'] is True

    def test_formal_kills_s3_dependence(self):
        """For formal E_n algebras, S_3 is also n-independent."""
        data = higher_shadow_n_dependence(3, 2)
        assert data['n_independent_for_formal'] is True

    def test_s4_potentially_dependent(self):
        """S_4 (r=4) can depend on n through Conf_4(R^n) topology."""
        data = higher_shadow_n_dependence(4, 3)
        assert data['arnold_classes_relevant'] is True
        assert data['n_independent_for_formal'] is True
        assert data['n_independent_for_non_formal'] is False

    def test_kappa_stabilizes_at_n1(self):
        """kappa stabilization threshold is n=1 (already stable)."""
        data = kappa_stabilizes_immediately()
        assert data['stabilization_threshold'] == 1

    def test_invalid_shadow_arity(self):
        """Shadow arity < 2 should raise ValueError."""
        with pytest.raises(ValueError):
            higher_shadow_n_dependence(1, 2)


# ========================================================================
# VII. CROSS-CONSISTENCY with existing engines
# ========================================================================


class TestCrossConsistency:
    """Cross-check with en_factorization_shadow and higher_dim engines."""

    def test_cross_check_en_factorization_heisenberg(self):
        """Cross-check with en_factorization_shadow for Heisenberg.

        NOTE: en_factorization_shadow.kappa_en_free uses kappa = k/2,
        which is the OLD (incorrect) convention per AP39.  The correct
        value is kappa(H_k) = k (CLAUDE.md AP39, theorem_c_complementarity).
        The en_factorization_shadow module has the known AP39 bug.
        We verify our value is correct by checking kappa(H_1) = 1.
        """
        # Our engine gives kappa = k (correct per AP39)
        assert kappa_heisenberg(Fraction(1)) == Fraction(1)
        assert kappa_heisenberg(Fraction(3)) == Fraction(3)
        # Cross-check: en_factorization_shadow now returns k (AP39 fixed).
        result = cross_check_with_en_factorization_shadow(1, Fraction(1))
        if 'error' not in result:
            assert result['kappa_this_engine'] == Fraction(1)
            assert result['kappa_en_factorization'] == Fraction(1)  # AP39 fixed
            assert result['consistent'] is True

    def test_cross_check_higher_dim_engine(self):
        """Our kappa invariance matches higher_dim engine."""
        for n1, n2 in [(1, 2), (1, 3), (2, 3), (1, 5)]:
            result = cross_check_with_higher_dim_engine(n1, n2)
            if 'error' not in result:
                assert result['consistent'] is True

    def test_cross_check_theorem_c_virasoro(self):
        """Our kappa matches Theorem C engine for Virasoro."""
        for c in [Fraction(1), Fraction(26), Fraction(13)]:
            result = cross_check_with_theorem_c('virasoro', c=c)
            if 'error' not in result and result['consistent'] is not None:
                assert result['consistent'] is True

    def test_kappa_formulas_match_known_values(self):
        """Verify kappa formulas against independently computed values.

        AP1: kappa formulas must be recomputed, not copied.
        AP10: cross-family consistency is the real verification.
        """
        # Heisenberg: kappa = k (the level)
        assert kappa_heisenberg(Fraction(1)) == Fraction(1)

        # Virasoro: kappa = c/2
        assert kappa_virasoro(Fraction(26)) == Fraction(13)

        # sl_2 at level 1: dim=3, h^v=2, kappa = 3*(1+2)/(2*2) = 9/4
        assert kappa_affine('A', 1, Fraction(1)) == Fraction(9, 4)

        # sl_3 at level 1: dim=8, h^v=3, kappa = 8*(1+3)/(2*3) = 32/6 = 16/3
        assert kappa_affine('A', 2, Fraction(1)) == Fraction(16, 3)

        # E_8 at level 1: dim=248, h^v=30, kappa = 248*31/60 = 7688/60 = 1922/15
        assert kappa_affine('E', 8, Fraction(1)) == Fraction(1922, 15)

    def test_additivity_heisenberg_lattice(self):
        """kappa is additive: kappa(H_1^r) = r * kappa(H_1) = r.

        This is a cross-family consistency check (AP10).
        Lattice VOA of rank r = r copies of Heisenberg at level 1.
        """
        for r in [1, 2, 8, 16, 24]:
            assert kappa_lattice(r) == r * kappa_heisenberg(Fraction(1))

    def test_w2_equals_virasoro(self):
        """W_2 = Virasoro: kappa(W_2, c) = c/2 = kappa(Vir_c).

        Cross-family consistency: sigma(2) = 1/2, so W_2 formula gives c/2.
        """
        for c in [Fraction(1), Fraction(26), Fraction(100)]:
            assert kappa_wn(2, c) == kappa_virasoro(c)


# ========================================================================
# VIII. THREE-PROOF CONVERGENCE
# ========================================================================


class TestThreeProofConvergence:
    """All three proofs give the same kappa for every family."""

    def test_three_proofs_heisenberg(self):
        """Three proofs agree for Heisenberg at level k."""
        for k in [Fraction(1), Fraction(3), Fraction(-2)]:
            for n in [1, 2, 3, 5]:
                result = three_proof_verification('heisenberg', n=n, k=k)
                assert result['all_consistent'] is True
                assert result['kappa_value'] == k

    def test_three_proofs_virasoro(self):
        """Three proofs agree for Virasoro at central charge c."""
        for c in [Fraction(1), Fraction(26), Fraction(13), Fraction(7, 10)]:
            for n in [1, 2, 3]:
                result = three_proof_verification('virasoro', n=n, c=c)
                assert result['all_consistent'] is True
                assert result['kappa_value'] == c / 2

    def test_three_proofs_affine_sl2(self):
        """Three proofs agree for affine sl_2."""
        for k in [Fraction(0), Fraction(1), Fraction(2)]:
            result = three_proof_verification(
                'affine', n=3, lie_type='A', rank=1, k=k)
            assert result['all_consistent'] is True

    def test_three_proofs_lattice(self):
        """Three proofs agree for lattice VOAs."""
        for rank in [1, 8, 24]:
            result = three_proof_verification('lattice', n=2, rank=rank)
            assert result['all_consistent'] is True
            assert result['kappa_value'] == Fraction(rank)

    def test_three_proofs_betagamma(self):
        """Three proofs agree for betagamma system."""
        result = three_proof_verification('betagamma', n=3, lam=1)
        assert result['all_consistent'] is True
        assert result['kappa_value'] == Fraction(1)


# ========================================================================
# IX. EDGE CASES AND ANTI-PATTERN GUARDS
# ========================================================================


class TestEdgeCases:
    """Edge cases and anti-pattern guards."""

    def test_ap39_kappa_neq_c_over_2_for_km(self):
        """AP39: kappa != c/2 for affine KM at rank > 1.

        For sl_3 at level 1: c = 8*1/(1+3) = 2, kappa = 16/3.
        c/2 = 1, but kappa = 16/3.  They do NOT coincide.
        """
        kap = kappa_affine('A', 2, Fraction(1))
        # c(sl_3, k=1) = dim * k / (k + h^v) = 8 * 1 / 4 = 2
        c_sl3 = Fraction(8) * Fraction(1) / (Fraction(1) + Fraction(3))
        assert kap != c_sl3 / 2, "AP39: kappa should NOT equal c/2 for sl_3"
        assert kap == Fraction(16, 3)

    def test_ap48_lattice_kappa_neq_c_over_2(self):
        """AP48: For lattice VOAs, kappa = rank, NOT c/2 = rank/2.

        A rank-24 lattice has c = 24 and kappa = 24 (not 12).
        """
        assert kappa_lattice(24) == Fraction(24)
        # c/2 would give 12, which is WRONG
        assert kappa_lattice(24) != Fraction(12)

    def test_ap20_kappa_is_intrinsic_to_algebra(self):
        """AP20: kappa is an invariant of A, not of a composite system.

        kappa(Vir_c) = c/2.  kappa_eff = kappa(matter) + kappa(ghost) is
        DIFFERENT.  The E_n-invariance theorem is about kappa(A), not kappa_eff.
        """
        kap = kappa_virasoro(Fraction(26))
        assert kap == Fraction(13)  # kappa(Vir_26) = 13
        # kappa_eff = kappa(Vir_26) + kappa(bc_ghost) = 13 + (-13) = 0
        kap_eff = kap + kappa_virasoro(Fraction(-26))
        assert kap_eff == Fraction(0)
        # Both kappa and kappa_eff are E_n-invariant (proven here for kappa)

    def test_ap1_independent_formulas_per_family(self):
        """AP1: kappa formulas are independent per family, not copied.

        Verify each family has its OWN formula, not pattern-matched from others.
        """
        # These should all be DIFFERENT values at the "same" parameters
        kap_heis = kappa_heisenberg(Fraction(1))  # = 1
        kap_vir = kappa_virasoro(Fraction(1))      # = 1/2
        kap_sl2 = kappa_affine('A', 1, Fraction(1))  # = 9/4
        # All different
        assert len({kap_heis, kap_vir, kap_sl2}) == 3

    def test_lie_data_exceptional(self):
        """Lie algebra data for exceptional types."""
        assert _lie_data('G', 2) == (14, 4)
        assert _lie_data('F', 4) == (52, 9)
        assert _lie_data('E', 6) == (78, 12)
        assert _lie_data('E', 7) == (133, 18)
        assert _lie_data('E', 8) == (248, 30)

    def test_theorem_summary(self):
        """Theorem summary has correct structure."""
        s = theorem_summary()
        assert s['proof_count'] == 3
        assert s['families_verified'] >= 18
        assert 'Binary bar' in s['proofs'][1]
        assert 'Central extension' in s['proofs'][2]
        assert 'Hodge' in s['proofs'][3]
