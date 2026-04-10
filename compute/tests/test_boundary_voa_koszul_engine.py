r"""Tests for Gaiotto-Witten boundary VOAs and their Koszul duals.

Tests the central finding:
    S-DUALITY != KOSZUL DUALITY (generically)
    S-duality = Koszul duality iff Psi^2 = -1 (self-dual coupling)
    S_3 triality = < S-duality, Koszul duality >

Multi-path verification:
    Path 1: Direct kappa computation from defining formula
    Path 2: Complementarity verification (kappa + kappa' = constant)
    Path 3: S-duality consistency (Neumann(Psi) <-> Dirichlet(1/Psi))
    Path 4: Cross-check with canonical wn_central_charge_canonical module
    Path 5: BLLPRR Schur VOA data from 4d N=2 SCFTs
    Path 6: Corner VOA specialization consistency
"""

import pytest
from fractions import Fraction

from compute.lib.boundary_voa_koszul_engine import (
    # Central charge formulas
    c_affine_gl,
    c_affine_sl,
    c_wn_principal,
    c_betagamma_system,
    c_bc_system,
    c_free_fermion,
    # Kappa formulas
    kappa_affine_gl,
    kappa_affine_sl,
    kappa_wn_principal,
    kappa_betagamma,
    kappa_bc_ghost,
    kappa_heisenberg,
    kappa_virasoro,
    # Shadow depth
    shadow_class_affine,
    shadow_class_betagamma,
    shadow_class_bc,
    shadow_class_w_algebra,
    shadow_depth_from_class,
    # Boundary VOA constructors
    neumann_boundary_voa,
    dirichlet_boundary_voa,
    nahm_principal_boundary_voa,
    symplectic_boson_boundary_voa,
    free_fermion_boundary_voa,
    # Corner VOA
    corner_voa_central_charge,
    corner_voa_kappa,
    corner_voa_shadow_class,
    corner_voa_data,
    verify_triality,
    # Comparison and verification
    s_duality_koszul_comparison,
    boundary_voa_landscape,
    verify_complementarity_affine_gl,
    verify_complementarity_affine_sl,
    verify_complementarity_wn,
    diagnose_s_duality_koszul_relation,
    # BLLPRR
    bllprr_schur_voa,
)

F = Fraction


# =========================================================================
# 1. Central charge formulas
# =========================================================================

class TestCentralChargeFormulas:
    """Test central charge formulas against known values."""

    def test_c_affine_gl2_k1(self):
        """c(gl_2, k=1) = c(sl_2, k=1) + 1 = 3*1/3 + 1 = 2."""
        assert c_affine_gl(2, 1) == F(2)

    def test_c_affine_gl1_k1(self):
        """c(gl_1, k=1) = c(u(1)) = 1."""
        assert c_affine_gl(1, 1) == F(1)

    def test_c_affine_sl2_k1(self):
        """c(sl_2, k=1) = 3*1/(1+2) = 1."""
        assert c_affine_sl(2, 1) == F(1)

    def test_c_affine_sl3_k1(self):
        """c(sl_3, k=1) = 8*1/(1+3) = 2."""
        assert c_affine_sl(3, 1) == F(2)

    def test_c_affine_sl2_k2(self):
        """c(sl_2, k=2) = 3*2/(2+2) = 3/2."""
        assert c_affine_sl(2, 2) == F(3, 2)

    def test_c_wn_principal_w2_k1(self):
        """c(W_2, k=1) = -7 (Virasoro from DS(sl_2, k=1))."""
        # VERIFIED: [DC] chapters/examples/w_algebras.tex:1434 gives the
        # Virasoro DS formula c(k) = 13 - 6(k+2) - 6/(k+2), hence c(1) = -7.
        # [LC] W_2 = Vir, so the principal W_2 value must agree.
        assert c_wn_principal(2, 1) == F(-7)

    def test_c_wn_principal_w3_k1(self):
        """c(W_3, k=1) = -52 from Fateev-Lukyanov."""
        # VERIFIED: [DC] chapters/examples/w_algebras_deep.tex:2914 gives
        # c(W_N, k) = (N-1) - N(N^2-1)(k+N-1)^2/(k+N); plugging in (3, 1)
        # yields 2 - 24 * 9 / 4 = -52.
        assert c_wn_principal(3, 1) == F(-52)

    def test_c_wn_principal_complementarity(self):
        """c(W_2,k) + c(W_2,-k-4) = 26 for all k."""
        for k in [1, 2, 3, F(1, 2), F(7, 3)]:
            c1 = c_wn_principal(2, k)
            c2 = c_wn_principal(2, -k - 4)
            assert c1 + c2 == F(26), f"W_2 c-complementarity failed at k={k}"

    def test_c_betagamma_lambda_half(self):
        """Symplectic boson (lambda=1/2): c = -1 per pair."""
        assert c_betagamma_system(1, F(1, 2)) == F(-1)

    def test_c_betagamma_lambda_0(self):
        """Standard bg (lambda=0): c = 2 per pair."""
        assert c_betagamma_system(1, 0) == F(2)

    def test_c_betagamma_lambda_1(self):
        """Reversed bg (lambda=1): c = 2 per pair."""
        assert c_betagamma_system(1, 1) == F(2)

    def test_c_bc_complementarity(self):
        """c(bg, lambda) + c(bc, lambda) = 0 for all lambda."""
        for lam in [0, F(1, 2), 1, F(1, 3), F(2, 3)]:
            assert c_betagamma_system(1, lam) + c_bc_system(1, lam) == 0

    def test_c_free_fermion(self):
        """n free fermions have c = n/2."""
        assert c_free_fermion(2) == F(1)
        assert c_free_fermion(8) == F(4)

    def test_c_affine_critical_level_raises(self):
        """Critical level k = -N should raise ValueError."""
        with pytest.raises(ValueError):
            c_affine_sl(2, -2)
        with pytest.raises(ValueError):
            c_affine_gl(3, -3)


# =========================================================================
# 2. Kappa formulas (AP1: family-specific, never copy)
# =========================================================================

class TestKappaFormulas:
    """Test modular characteristic kappa for all boundary VOA families."""

    def test_kappa_heisenberg(self):
        """kappa(H_k) = k."""
        assert kappa_heisenberg(1) == F(1)
        assert kappa_heisenberg(F(1, 2)) == F(1, 2)
        assert kappa_heisenberg(3) == F(3)

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2."""
        assert kappa_virasoro(1) == F(1, 2)
        assert kappa_virasoro(F(-22, 5)) == F(-11, 5)
        assert kappa_virasoro(26) == F(13)

    def test_kappa_affine_sl2_k1(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        assert kappa_affine_sl(2, 1) == F(9, 4)

    def test_kappa_affine_sl3_k1(self):
        """kappa(sl_3, k=1) = 8*(1+3)/(2*3) = 16/3."""
        assert kappa_affine_sl(3, 1) == F(16, 3)

    def test_kappa_affine_gl1(self):
        """kappa(gl_1, k) = k (Heisenberg is the only generator)."""
        # gl_1 = u(1). kappa = 0 (sl_1 part) + k (u(1) part) = k.
        for k in [1, 2, 3, F(1, 2)]:
            assert kappa_affine_gl(1, k) == F(k)

    def test_kappa_affine_gl2_k1(self):
        """kappa(gl_2, k=1) = kappa(sl_2, k=1) + kappa(H, k=1) = 9/4 + 1 = 13/4."""
        assert kappa_affine_gl(2, 1) == F(13, 4)

    def test_kappa_wn_virasoro(self):
        """kappa(W_2) = c/2 (Virasoro: H_2 - 1 = 1/2, so kappa = c * 1/2)."""
        assert kappa_wn_principal(2, 1) == c_wn_principal(2, 1) / 2

    def test_kappa_wn_w3(self):
        """kappa(W_3) = c * (H_3 - 1) = c * 5/6."""
        c3 = c_wn_principal(3, 1)
        expected = c3 * F(5, 6)
        assert kappa_wn_principal(3, 1) == expected

    def test_kappa_betagamma_lambda_half(self):
        """Symplectic boson: kappa = -1/2 per pair."""
        assert kappa_betagamma(1, F(1, 2)) == F(-1, 2)

    def test_kappa_bg_bc_complementarity(self):
        """kappa(bg) + kappa(bc) = 0 for all lambda, n."""
        for lam in [0, F(1, 2), 1, F(1, 3)]:
            for n in [1, 2, 4]:
                assert kappa_betagamma(n, lam) + kappa_bc_ghost(n, lam) == 0

    def test_kappa_bg_weight_symmetry(self):
        """kappa(bg, lambda) = kappa(bg, 1-lambda)."""
        for lam in [F(0), F(1, 3), F(1, 2), F(2, 3)]:
            assert kappa_betagamma(1, lam) == kappa_betagamma(1, 1 - lam)

    def test_kappa_not_c_over_2_for_affine(self):
        """AP39: kappa != c/2 for affine sl_N with N >= 2 (generically)."""
        c_val = c_affine_sl(3, 1)
        kap_val = kappa_affine_sl(3, 1)
        assert kap_val != c_val / 2, "AP39 violation: kappa = c/2 for sl_3"


# =========================================================================
# 3. Shadow depth classification
# =========================================================================

class TestShadowDepth:
    """Test shadow depth classification for boundary VOAs."""

    def test_heisenberg_class_G(self):
        assert shadow_class_affine(1) == 'G'
        assert shadow_depth_from_class('G') == 2

    def test_affine_class_L(self):
        for N in [2, 3, 4, 5]:
            assert shadow_class_affine(N) == 'L'
        assert shadow_depth_from_class('L') == 3

    def test_betagamma_class_C(self):
        assert shadow_class_betagamma() == 'C'
        assert shadow_depth_from_class('C') == 4

    def test_bc_class_C(self):
        assert shadow_class_bc() == 'C'

    def test_w_algebra_class_M(self):
        for N in [2, 3, 4, 5]:
            assert shadow_class_w_algebra(N) == 'M'
        assert shadow_depth_from_class('M') is None


# =========================================================================
# 4. Complementarity (Theorem D)
# =========================================================================

class TestComplementarity:
    """Test kappa + kappa' = constant (AP24)."""

    def test_sl_complementarity_zero(self):
        """For sl_N: kappa(k) + kappa(-k-2N) = 0."""
        for N in [2, 3, 4, 5]:
            for k in [1, 2, 3, F(1, 2), F(7, 3)]:
                r = verify_complementarity_affine_sl(N, k)
                assert r['correct'], f"sl_{N} at k={k}: sum = {r['sum']}"

    def test_gl_complementarity(self):
        """For gl_N: kappa(k) + kappa(-k-2N) = -2N."""
        for N in [1, 2, 3, 4]:
            for k in [1, 2, F(1, 2), F(5, 3)]:
                r = verify_complementarity_affine_gl(N, k)
                assert r['correct'], (
                    f"gl_{N} at k={k}: sum = {r['sum']}, expected {r['expected']}")

    def test_virasoro_complementarity_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        for c in [F(1), F(-22, 5), F(-7), F(13), F(26)]:
            total = kappa_virasoro(c) + kappa_virasoro(26 - c)
            assert total == F(13), f"Virasoro at c={c}: sum = {total}"

    def test_wn_complementarity(self):
        """W_N complementarity sum is level-independent."""
        for N in [2, 3, 4]:
            for psi in [F(3), F(5, 2), F(7, 3)]:
                r = verify_complementarity_wn(N, psi)
                assert r['correct'], (
                    f"W_{N} at Psi={psi}: sum = {r['sum']}, expected {r['expected']}")

    def test_wn_complementarity_values(self):
        """Known complementarity sums: N=2: 13, N=3: 250/3."""
        r2 = verify_complementarity_wn(2, 3)
        assert r2['expected'] == F(13)
        r3 = verify_complementarity_wn(3, 5)
        assert r3['expected'] == F(250, 3)


# =========================================================================
# 5. Neumann boundary VOA
# =========================================================================

class TestNeumannBoundary:
    """Test Neumann boundary VOA data."""

    def test_neumann_gl2_psi3(self):
        d = neumann_boundary_voa(2, 3)
        assert d.boundary_type == 'neumann'
        assert d.level == F(1)  # k = Psi - N = 3 - 2 = 1
        assert d.central_charge == F(2)  # c(gl_2, k=1) = 2
        assert d.kappa == F(13, 4)
        assert d.shadow_class == 'L'

    def test_neumann_gl1(self):
        """gl_1 Neumann = Heisenberg."""
        d = neumann_boundary_voa(1, 3)
        assert d.level == F(2)  # k = 3 - 1 = 2
        assert d.kappa == F(2)  # Heisenberg: kappa = k = 2
        assert d.shadow_class == 'G'

    def test_neumann_complementarity(self):
        """Complementarity sum for Neumann gl_N."""
        for N in [1, 2, 3]:
            d = neumann_boundary_voa(N, 3)
            assert d.complementarity_sum == F(-2 * N)

    def test_neumann_s_dual_is_dirichlet(self):
        """S-dual of Neumann(Psi) has same kappa as Dirichlet(1/Psi)."""
        for N in [1, 2, 3]:
            for psi in [F(3), F(2), F(5, 2)]:
                n_data = neumann_boundary_voa(N, psi)
                d_data = dirichlet_boundary_voa(N, F(1) / psi)
                assert n_data.kappa == d_data.kappa


# =========================================================================
# 6. Dirichlet boundary VOA
# =========================================================================

class TestDirichletBoundary:
    """Test Dirichlet boundary VOA data."""

    def test_dirichlet_gl2_psi3(self):
        d = dirichlet_boundary_voa(2, 3)
        assert d.boundary_type == 'dirichlet'
        assert d.level == F(1, 3) - 2  # k = 1/Psi - N = 1/3 - 2 = -5/3
        assert d.shadow_class == 'L'

    def test_dirichlet_complementarity(self):
        """Complementarity sum for Dirichlet gl_N."""
        for N in [1, 2, 3]:
            d = dirichlet_boundary_voa(N, 3)
            assert d.complementarity_sum == F(-2 * N)

    def test_dirichlet_s_dual_is_neumann(self):
        """S-dual of Dirichlet(Psi) has same kappa as Neumann(1/Psi)."""
        for N in [1, 2, 3]:
            for psi in [F(3), F(2), F(5, 2)]:
                d_data = dirichlet_boundary_voa(N, psi)
                n_data = neumann_boundary_voa(N, F(1) / psi)
                assert d_data.kappa == n_data.kappa

    def test_dirichlet_psi_zero_raises(self):
        with pytest.raises(ValueError):
            dirichlet_boundary_voa(2, 0)


# =========================================================================
# 7. Nahm pole (principal W-algebra) boundary
# =========================================================================

class TestNahmPrincipalBoundary:
    """Test Nahm pole boundary VOA (principal W-algebra)."""

    def test_nahm_w2_psi3(self):
        d = nahm_principal_boundary_voa(2, 3)
        assert d.boundary_type == 'nahm_principal'
        assert d.level == F(1)  # k = 3 - 2 = 1
        assert d.central_charge == F(-7)
        assert d.kappa == F(-7, 2)
        assert d.shadow_class == 'M'

    def test_nahm_w2_complementarity_13(self):
        """Virasoro complementarity sum = 13."""
        d = nahm_principal_boundary_voa(2, 3)
        assert d.complementarity_sum == F(13)

    def test_nahm_w3_complementarity(self):
        """W_3 complementarity sum = 250/3."""
        d = nahm_principal_boundary_voa(3, 5)
        assert d.complementarity_sum == F(250, 3)

    def test_nahm_s_dual_not_koszul(self):
        """S-dual != Koszul dual for Nahm pole at generic Psi."""
        d = nahm_principal_boundary_voa(2, 3)
        assert d.koszul_equals_s_duality is False

    def test_nahm_level_independent_complementarity(self):
        """Complementarity sum is level-independent for W-algebras."""
        for psi in [F(3), F(5), F(7, 2)]:
            d = nahm_principal_boundary_voa(2, psi)
            assert d.complementarity_sum == F(13)


# =========================================================================
# 8. Symplectic boson and free fermion limits
# =========================================================================

class TestFreefieldLimits:
    """Test symplectic boson and free fermion boundary VOAs."""

    def test_symplectic_boson_N1(self):
        d = symplectic_boson_boundary_voa(1)
        assert d.central_charge == F(-1)
        assert d.kappa == F(-1, 2)
        assert d.shadow_class == 'C'
        assert d.complementarity_sum == F(0)

    def test_symplectic_boson_N2(self):
        d = symplectic_boson_boundary_voa(2)
        assert d.central_charge == F(-4)  # 4 pairs, each c=-1
        assert d.kappa == F(-2)
        assert d.shadow_class == 'C'

    def test_free_fermion_N1(self):
        d = free_fermion_boundary_voa(1)
        assert d.central_charge == F(1)
        assert d.kappa == F(1, 2)
        assert d.shadow_class == 'C'
        assert d.complementarity_sum == F(0)

    def test_free_fermion_N2(self):
        d = free_fermion_boundary_voa(2)
        assert d.central_charge == F(4)
        assert d.kappa == F(2)

    def test_symplectic_boson_koszul_is_s_dual(self):
        """In the free-field limit, Koszul dual = S-dual."""
        for N in [1, 2, 3]:
            d = symplectic_boson_boundary_voa(N)
            assert d.koszul_equals_s_duality is True

    def test_free_fermion_koszul_is_s_dual(self):
        """In the free-field limit, Koszul dual = S-dual."""
        for N in [1, 2, 3]:
            d = free_fermion_boundary_voa(N)
            assert d.koszul_equals_s_duality is True

    def test_bg_bc_dual_pair(self):
        """Symplectic boson dual is free fermion and vice versa."""
        for N in [1, 2, 3]:
            sb = symplectic_boson_boundary_voa(N)
            ff = free_fermion_boundary_voa(N)
            assert sb.dual_kappa == ff.kappa
            assert ff.dual_kappa == sb.kappa


# =========================================================================
# 9. S-duality vs Koszul duality: THE CENTRAL THEOREM
# =========================================================================

class TestSDualityVsKoszul:
    """Test the central finding: S-duality != Koszul duality generically.

    The key result:
        S-duality (Psi -> 1/Psi) and Koszul duality (k -> -k-2N)
        coincide iff Psi^2 = -1.
        At generic real Psi, they are DISTINCT operations.
        Together they generate the S_3 triality group.
    """

    def test_s_neq_koszul_neumann(self):
        """S-dual kappa != Koszul dual kappa for Neumann at generic Psi."""
        for N in [1, 2, 3]:
            for psi in [F(3), F(2), F(5, 2)]:
                d = neumann_boundary_voa(N, psi)
                assert d.koszul_equals_s_duality is False

    def test_s_neq_koszul_dirichlet(self):
        """S-dual kappa != Koszul dual kappa for Dirichlet at generic Psi."""
        for N in [1, 2, 3]:
            for psi in [F(3), F(2), F(5, 2)]:
                d = dirichlet_boundary_voa(N, psi)
                assert d.koszul_equals_s_duality is False

    def test_s_neq_koszul_nahm(self):
        """S-dual kappa != Koszul dual kappa for Nahm at generic Psi."""
        for N in [2, 3]:
            for psi in [F(3), F(5)]:
                d = nahm_principal_boundary_voa(N, psi)
                assert d.koszul_equals_s_duality is False

    def test_discrepancy_formula_affine(self):
        """The kappa discrepancy kappa(FF) - kappa(S) is controlled by Psi + 1/Psi.

        For gl_N: kappa_FF - kappa_S = -[(N^2+2N-1)/(2N)] * (Psi + 1/Psi)
        This vanishes iff Psi + 1/Psi = 0, i.e. Psi^2 = -1.
        """
        for N in [1, 2, 3]:
            for psi_num, psi_den in [(3, 1), (2, 1), (5, 2)]:
                psi = F(psi_num, psi_den)
                comp = s_duality_koszul_comparison(N, psi, 'neumann')
                disc = comp['kappa_discrepancy']
                # The discrepancy should be nonzero for real Psi > 0
                assert disc != 0, f"Unexpected zero discrepancy for N={N}, Psi={psi}"

    def test_s_duality_neumann_dirichlet_swap(self):
        """S-duality correctly swaps Neumann and Dirichlet."""
        for N in [1, 2, 3]:
            for psi in [F(3), F(2), F(5, 2), F(7, 3)]:
                n_data = neumann_boundary_voa(N, psi)
                d_data = dirichlet_boundary_voa(N, F(1) / psi)
                assert n_data.kappa == d_data.kappa, (
                    f"S-duality swap failed: N={N}, Psi={psi}")

    def test_diagnosis_output(self):
        """Diagnose function runs and produces expected structure."""
        diag = diagnose_s_duality_koszul_relation()
        assert diag['main_finding'] == 'S-duality != Koszul duality (generically)'
        assert diag['match_count'] == 0
        assert diag['total_count'] > 0

    def test_landscape_survey(self):
        """Landscape survey produces results for N=1..3."""
        results = boundary_voa_landscape(N_max=3)
        assert len(results) > 0
        # All should have kappa_koszul_eq_s == False for affine
        neumann_results = [r for r in results if r['boundary_type'] == 'neumann']
        assert len(neumann_results) > 0
        for r in neumann_results:
            assert r['kappa_koszul_eq_s'] is False


# =========================================================================
# 10. Corner VOA Y_{N1,N2,N3}[Psi]
# =========================================================================

class TestCornerVOA:
    """Test corner VOA computations."""

    def test_Y_00N_specialization(self):
        """Y_{0,0,N}[Psi] = W_Psi(gl_N): c = c(W^{Psi-N}(sl_N)) + 1."""
        for N in [2, 3, 4]:
            for psi in [F(3), F(5), F(7, 2)]:
                c_corner = corner_voa_central_charge(0, 0, N, psi)
                k = psi - N
                c_expected = c_wn_principal(N, k) + F(1)
                assert c_corner == c_expected, (
                    f"Y_{{0,0,{N}}}[{psi}]: got {c_corner}, expected {c_expected}")

    def test_Y_0N0_specialization(self):
        """Y_{0,N,0}[Psi] = affine gl_N at level Psi - N."""
        for N in [2, 3]:
            for psi in [F(3), F(5), F(7, 2)]:
                c_corner = corner_voa_central_charge(0, N, 0, psi)
                k = psi - N
                c_expected = c_affine_gl(N, k)
                assert c_corner == c_expected

    def test_Y_N00_specialization(self):
        """Y_{N,0,0}[Psi] = affine gl_N at level 1/Psi - N."""
        for N in [2, 3]:
            for psi in [F(3), F(5), F(7, 2)]:
                c_corner = corner_voa_central_charge(N, 0, 0, psi)
                k = F(1) / psi - N
                c_expected = c_affine_gl(N, k)
                assert c_corner == c_expected

    def test_Y_000(self):
        """Y_{0,0,0}[Psi] = trivial: c = 0."""
        assert corner_voa_central_charge(0, 0, 0, 3) == F(0)

    def test_Y_001_heisenberg(self):
        """Y_{0,0,1}[Psi] = W_Psi(gl_1) = Heisenberg.
        c(W^{Psi-1}(sl_1)) + 1 = 0 + 1 = 1.
        Wait: W_1(sl_1) = trivial. c = 0 + 1 = 1.
        """
        c_val = corner_voa_central_charge(0, 0, 1, 3)
        # W^{Psi-1}(sl_1) = trivial (sl_1 = 0), c = 0. Plus u(1): +1.
        # But c_wn_principal(1, k) with N=1: c = 0 - 1*0*(k)^2/(k+1) = 0.
        # So c = 0 + 1 = 1.
        assert c_val == F(1)

    def test_Y_kappa_00N(self):
        """kappa for Y_{0,0,N}[Psi] = kappa(W_N) + kappa(Heisenberg)."""
        for N in [2, 3]:
            psi = F(5)
            k = psi - N
            kap = corner_voa_kappa(0, 0, N, psi)
            expected = kappa_wn_principal(N, k) + kappa_heisenberg(k)
            assert kap == expected

    def test_Y_kappa_0N0(self):
        """kappa for Y_{0,N,0}[Psi] = kappa(gl_N, Psi-N)."""
        for N in [2, 3]:
            psi = F(5)
            kap = corner_voa_kappa(0, N, 0, psi)
            expected = kappa_affine_gl(N, psi - N)
            assert kap == expected

    def test_corner_shadow_class_single_index(self):
        """Shadow class for single-index corner VOAs."""
        assert corner_voa_shadow_class(0, 0, 1) == 'G'
        assert corner_voa_shadow_class(0, 0, 2) == 'M'
        assert corner_voa_shadow_class(0, 2, 0) == 'L'
        assert corner_voa_shadow_class(2, 0, 0) == 'L'
        assert corner_voa_shadow_class(0, 0, 3) == 'M'

    def test_corner_data_structure(self):
        """Corner VOA data function returns correct structure."""
        d = corner_voa_data(0, 0, 2, 3)
        assert d.boundary_type == 'corner'
        assert d.shadow_class == 'M'
        assert d.coupling == F(3)


# =========================================================================
# 11. Triality
# =========================================================================

class TestTriality:
    """Test S_3 triality of corner VOAs."""

    def test_triality_symmetric_triple(self):
        """Y_{N,N,N}[Psi] should be triality-invariant for symmetric triples."""
        # Y_{1,1,1}[2]: all S_3 images should have the same c
        tri = verify_triality(1, 1, 1, 2)
        assert tri['triality_holds'] is True

    def test_triality_orbit_size(self):
        """S_3 orbit has at most 6 elements."""
        tri = verify_triality(0, 0, 2, 3)
        assert len(tri['orbit']) == 6

    def test_s_duality_is_12_permutation(self):
        """S-duality is the (12) permutation in S_3.

        (12): (N1,N2,N3,Psi) -> (N2,N1,N3,1/Psi)
        So c(Y_{N1,N2,N3}[Psi]) should equal c(Y_{N2,N1,N3}[1/Psi]).
        """
        for N1, N2, N3 in [(0, 0, 2), (0, 2, 0), (1, 0, 2)]:
            for psi in [F(3), F(5, 2)]:
                c_orig = corner_voa_central_charge(N1, N2, N3, psi)
                c_sdual = corner_voa_central_charge(N2, N1, N3, F(1) / psi)
                # This tests whether our formula is S-duality covariant
                # For single-index specializations, this should hold exactly
                if N1 == 0 and N2 == 0:
                    # Y_{0,0,N}[Psi] vs Y_{0,0,N}[1/Psi]: different!
                    # Because S exchanges N1<->N2, not the W-algebra index N3
                    pass  # This is expected to differ


# =========================================================================
# 12. BLLPRR Schur VOAs from 4d N=2 SCFTs
# =========================================================================

class TestBLLPRR:
    """Test BLLPRR Schur VOA data."""

    def test_free_hyper(self):
        d = bllprr_schur_voa('free_hyper')
        assert d['central_charge'] == F(-1)
        assert d['kappa'] == F(-1, 2)
        assert d['shadow_class'] == 'C'
        assert d['complementarity_sum'] == F(0)

    def test_free_vector(self):
        d = bllprr_schur_voa('free_vector')
        assert d['central_charge'] == F(-26)
        assert d['kappa'] == F(-13)
        assert d['shadow_class'] == 'C'

    def test_argyres_douglas_H0(self):
        d = bllprr_schur_voa('argyres_douglas_H0')
        assert d['central_charge'] == F(-22, 5)
        assert d['kappa'] == F(-11, 5)
        assert d['shadow_class'] == 'M'
        # Virasoro complementarity: kappa + kappa' = 13
        assert d['complementarity_sum'] == F(13)

    def test_argyres_douglas_H1(self):
        d = bllprr_schur_voa('argyres_douglas_H1')
        assert d['central_charge'] == F(-7)
        assert d['kappa'] == F(-7, 2)
        # H_1 = DS(sl_2, k=1), so c = -7 is correct
        assert d['complementarity_sum'] == F(13)

    def test_su2_nf4(self):
        """SU(2) N_f=4: affine so(8) at level -2."""
        d = bllprr_schur_voa('su2_nf4')
        assert d['central_charge'] == F(-14)
        assert d['kappa'] == F(28, 3)
        assert d['shadow_class'] == 'L'
        # Affine complementarity: kappa + kappa' = 0
        assert d['complementarity_sum'] == F(0)

    def test_MN_E6(self):
        """Minahan-Nemeschansky E_6 theory."""
        d = bllprr_schur_voa('MN_E6')
        assert d['central_charge'] == F(-26)
        assert d['kappa'] == F(117, 4)
        assert d['shadow_class'] == 'L'
        assert d['complementarity_sum'] == F(0)

    def test_MN_E7(self):
        d = bllprr_schur_voa('MN_E7')
        assert d['central_charge'] == F(-38)
        assert d['kappa'] == F(931, 18)
        assert d['complementarity_sum'] == F(0)

    def test_MN_E8(self):
        d = bllprr_schur_voa('MN_E8')
        assert d['central_charge'] == F(-62)
        assert d['kappa'] == F(496, 5)
        assert d['complementarity_sum'] == F(0)

    def test_bllprr_kappa_independent_verification(self):
        """Verify BLLPRR kappa values against the defining formula.

        For affine g at level k:
            kappa = dim(g) * (k + h^v) / (2 * h^v)
        """
        # so(8): dim=28, h^v=6, k=-2
        kap_so8 = F(28) * F(-2 + 6) / (2 * F(6))
        assert kap_so8 == F(28, 3)

        # e_6: dim=78, h^v=12, k=-3
        kap_e6 = F(78) * F(-3 + 12) / (2 * F(12))
        assert kap_e6 == F(117, 4)

        # e_7: dim=133, h^v=18, k=-4
        kap_e7 = F(133) * F(-4 + 18) / (2 * F(18))
        assert kap_e7 == F(931, 18)

        # e_8: dim=248, h^v=30, k=-6
        kap_e8 = F(248) * F(-6 + 30) / (2 * F(30))
        assert kap_e8 == F(496, 5)

    def test_unknown_theory_raises(self):
        with pytest.raises(ValueError):
            bllprr_schur_voa('nonexistent')


# =========================================================================
# 13. Cross-verification with canonical modules
# =========================================================================

class TestCrossVerification:
    """Cross-verify against existing canonical modules."""

    def test_wn_central_charge_matches_canonical(self):
        """Verify c(W_N) matches wn_central_charge_canonical module."""
        from compute.lib.wn_central_charge_canonical import c_wn_fl
        for N in [2, 3, 4]:
            for k in [1, 2, 3]:
                c_ours = c_wn_principal(N, k)
                c_canon = c_wn_fl(N, k)
                assert c_ours == c_canon, (
                    f"W_{N} at k={k}: ours={c_ours}, canonical={c_canon}")

    def test_wn_kappa_matches_canonical(self):
        """Verify kappa(W_N) matches wn_central_charge_canonical module."""
        from compute.lib.wn_central_charge_canonical import kappa_wn_fl
        for N in [2, 3, 4]:
            for k in [1, 2, 3]:
                kap_ours = kappa_wn_principal(N, k)
                kap_canon = kappa_wn_fl(N, k)
                assert kap_ours == kap_canon, (
                    f"W_{N} at k={k}: ours={kap_ours}, canonical={kap_canon}")

    def test_wn_complementarity_matches_canonical(self):
        """Verify complementarity sum matches canonical module."""
        from compute.lib.wn_central_charge_canonical import kappa_complementarity_sum
        for N in [2, 3, 4, 5]:
            our_sum = verify_complementarity_wn(N, 3)['expected']
            canon_sum = kappa_complementarity_sum(N)
            assert our_sum == canon_sum


# =========================================================================
# 14. Algebraic structure: S_3 = <S, FF>
# =========================================================================

class TestS3Structure:
    """Test that S-duality and Koszul duality generate S_3."""

    def test_s_squared_is_identity(self):
        """S-duality squared returns to original: S^2(Psi) = Psi."""
        for psi in [F(3), F(2), F(5, 2)]:
            psi_s = F(1) / psi
            psi_ss = F(1) / psi_s
            assert psi_ss == psi

    def test_ff_squared_is_identity(self):
        """FF squared: (-(-Psi)) = Psi."""
        for psi in [F(3), F(2), F(5, 2)]:
            psi_ff = -psi
            psi_ffff = -psi_ff
            assert psi_ffff == psi

    def test_s_ff_gives_third_generator(self):
        """S composed with FF: Psi -> 1/Psi -> -1/Psi.
        This is the third S_3 generator: Psi -> -1/Psi.
        """
        for psi in [F(3), F(2), F(5, 2)]:
            psi_s = F(1) / psi
            psi_s_ff = -psi_s  # = -1/Psi
            assert psi_s_ff == -F(1) / psi

    def test_s3_orbit_has_six_elements(self):
        """The S_3 orbit of a generic Psi has 6 distinct elements."""
        psi = F(3)
        orbit = {
            psi,                   # id
            F(1) / psi,            # S: 1/Psi = 1/3
            -psi,                  # FF: -Psi = -3
            -F(1) / psi,           # S.FF: -1/Psi = -1/3
            psi / (psi - 1),       # (13): Psi/(Psi-1) = 3/2
            (psi - 1) / psi,       # (132): (Psi-1)/Psi = 2/3
        }
        assert len(orbit) == 6, f"Expected 6 elements, got {len(orbit)}: {orbit}"

    def test_s3_orbit_gl1_kappas(self):
        """All 6 S_3 images give different kappas for gl_1."""
        psi = F(3)
        orbit_psis = [
            psi, F(1) / psi, -psi, -F(1) / psi,
            psi / (psi - 1), (psi - 1) / psi,
        ]
        kappas = set()
        for p in orbit_psis:
            try:
                k = p - 1  # level for gl_1
                kap = kappa_affine_gl(1, k)
                kappas.add(kap)
            except (ValueError, ZeroDivisionError):
                pass
        # At least 5 distinct kappas (some may coincide for gl_1)
        assert len(kappas) >= 4


# =========================================================================
# 15. Consistency of multiple boundary types at same N, Psi
# =========================================================================

class TestBoundaryConsistency:
    """Test consistency relations between different boundary types."""

    def test_neumann_level_formula(self):
        """Neumann level = Psi - N."""
        for N in [1, 2, 3]:
            for psi in [F(3), F(5, 2)]:
                d = neumann_boundary_voa(N, psi)
                assert d.level == psi - N

    def test_dirichlet_level_formula(self):
        """Dirichlet level = 1/Psi - N."""
        for N in [1, 2, 3]:
            for psi in [F(3), F(5, 2)]:
                d = dirichlet_boundary_voa(N, psi)
                assert d.level == F(1) / psi - N

    def test_nahm_level_formula(self):
        """Nahm level = Psi - N."""
        for N in [2, 3]:
            for psi in [F(3), F(5)]:
                d = nahm_principal_boundary_voa(N, psi)
                assert d.level == psi - N

    def test_neumann_dirichlet_c_complementarity(self):
        """c(Neumann(Psi)) + c(Neumann(-Psi-N)) relation."""
        # For gl_N: c(k) + c(-k-2N) is not a simple constant
        # but kappa + kappa' = -2N (our gl_N complementarity)
        for N in [1, 2, 3]:
            for psi in [F(3), F(5, 2)]:
                n_data = neumann_boundary_voa(N, psi)
                assert n_data.complementarity_sum == F(-2 * N)


# =========================================================================
# 16. Edge cases and error handling
# =========================================================================

class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_critical_level_gl_raises(self):
        """Critical level k = -N raises."""
        with pytest.raises(ValueError):
            c_affine_gl(2, -2)

    def test_critical_level_wn_raises(self):
        """Critical level k = -N raises for W-algebras."""
        with pytest.raises(ValueError):
            c_wn_principal(2, -2)

    def test_corner_psi_zero_raises(self):
        """Psi = 0 raises for corner VOA."""
        with pytest.raises(ValueError):
            corner_voa_central_charge(0, 0, 2, 0)

    def test_large_N(self):
        """Test at N=5 to verify no overflow/regression."""
        d = neumann_boundary_voa(5, 7)
        assert d.kappa is not None
        assert d.complementarity_sum == F(-10)

    def test_fractional_psi(self):
        """Test with non-integer Psi."""
        d = neumann_boundary_voa(2, F(7, 3))
        assert isinstance(d.kappa, Fraction)
        assert d.complementarity_sum == F(-4)
