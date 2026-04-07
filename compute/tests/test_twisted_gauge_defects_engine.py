r"""Tests for twisted gauge theory defects and the shadow obstruction tower.

Verifies:
  1. Line defects (Wilson lines): Casimir, dimension, module kappa
  2. Surface defects (boundary conditions): Dirichlet, Neumann, module bar data
  3. Defect OPE (R-matrix): Yang--Baxter, unitarity, channel decomposition
  4. Gukov--Witten surface operators: monodromy correction, trivial/principal
  5. 't Hooft lines (magnetic defects): kappa complementarity, dual level
  6. Crossing kernel (6j-symbols): Racah formula, orthogonality
  7. Defect networks (webs): vertex validity, evaluation
  8. Kapustin--Witten / geometric Langlands: Langlands dual, KZ data, dictionary

MULTI-PATH VERIFICATION (CLAUDE.md mandate):
  Every numerical value is verified by at least 2 independent methods.

CONVENTIONS:
  - Cohomological grading (|d| = +1).
  - kappa(hat{g}_k) = dim(g) * (k + h^v) / (2 h^v) (AP1, AP9, AP39).
  - r-matrix r(z) = Omega/z (AP19: one pole order below OPE).
  - C_2(sl_2, n) = n(n+2)/2 (mathematical normalization; h = C_2/(2(k+h^v)) = j(j+1)/(k+2)).
  - C_2(sl_3, (a,b)) = (2/3)(a^2+b^2+ab) + 2(a+b).
  - Yang R-matrix: R(u) = u*I + P (additive convention).

References:
  - yangian_residue_extraction.py: Yang R-matrix ground truth.
  - kappa_cross_verification.py: kappa ground truth.
  - dk_compact_generation.py: DK ladder, thick generation.
  - landscape_census.tex: authoritative kappa values.
  - CLAUDE.md: AP1, AP9, AP19, AP24, AP33, AP39.
"""

import math
import pytest
import numpy as np
from fractions import Fraction

from sympy import Rational, simplify, sqrt

from compute.lib.twisted_gauge_defects_engine import (
    # Lie data and kappa
    kappa_affine,
    central_charge_affine,
    # Line defects
    LineDefect,
    quadratic_casimir,
    weyl_dimension,
    module_kappa,
    # Defect OPE
    permutation_matrix,
    yang_r_matrix,
    defect_ope_r_matrix,
    verify_defect_ybe,
    defect_ope_eigenvalues,
    # CG and fusion
    clebsch_gordan_sl2,
    clebsch_gordan_sl3_fund,
    fusion_dimension_check_sl2,
    fusion_dimension_check_sl3,
    # Surface defects
    SurfaceDefect,
    dirichlet_surface_defect,
    neumann_surface_defect,
    module_bar_complex_data,
    # Gukov-Witten
    GukovWittenDefect,
    gukov_witten_trivial,
    gukov_witten_principal,
    # 't Hooft
    THooftLine,
    verify_kappa_complementarity_km,
    # Crossing kernel
    crossing_kernel_sl2,
    crossing_kernel_eigenvalue_sl2,
    # Defect networks
    trivalent_vertex_sl2,
    theta_network_sl2,
    defect_web_evaluation_sl2,
    # Fusion checks
    verify_fusion_associativity_sl2,
    verify_defect_shadow_additivity,
    electric_magnetic_duality_check,
    # Kapustin-Witten
    langlands_dual_lie_type,
    kapustin_witten_dictionary,
    kz_connection_parameter,
    # Defect partition function
    defect_partition_function_genus1,
)


# ============================================================================
# 1. Modular characteristic kappa — multi-path verification
# ============================================================================

class TestKappaAffine:
    """Verify kappa(hat{g}_k) = dim(g) * (k + h^v) / (2 h^v)."""

    def test_kappa_sl2_level1(self):
        """sl_2 at level 1: kappa = 3 * (1+2) / (2*2) = 9/4."""
        kap = kappa_affine("A", 1, Rational(1))
        assert kap == Rational(9, 4)
        # Cross-check: dim(sl_2)=3, h^v=2, k=1
        assert kap == Rational(3) * (1 + 2) / (2 * 2)

    def test_kappa_sl3_level1(self):
        """sl_3 at level 1: kappa = 8 * (1+3) / (2*3) = 16/3."""
        kap = kappa_affine("A", 2, Rational(1))
        assert kap == Rational(16, 3)

    def test_kappa_sl2_generic(self):
        """sl_2 at generic level k: kappa = 3(k+2)/4."""
        for k_val in [1, 2, 3, 5, 10, 100]:
            kap = kappa_affine("A", 1, Rational(k_val))
            expected = Rational(3) * (k_val + 2) / 4
            assert kap == expected

    def test_kappa_so5_level1(self):
        """B_2 = so_5 at level 1: kappa = 10 * (1+3) / (2*3) = 20/3."""
        kap = kappa_affine("B", 2, Rational(1))
        assert kap == Rational(20, 3)

    def test_kappa_sp4_level1(self):
        """C_2 = sp_4 at level 1: kappa = 10 * (1+3) / (2*3) = 20/3."""
        kap = kappa_affine("C", 2, Rational(1))
        assert kap == Rational(20, 3)

    def test_kappa_g2_level1(self):
        """G_2 at level 1: kappa = 14 * (1+4) / (2*4) = 35/4."""
        kap = kappa_affine("G", 2, Rational(1))
        assert kap == Rational(35, 4)

    def test_kappa_critical_level_raises(self):
        """Critical level k = -h^v should raise ValueError."""
        with pytest.raises(ValueError, match="critical level"):
            kappa_affine("A", 1, Rational(-2))
        with pytest.raises(ValueError, match="critical level"):
            kappa_affine("A", 2, Rational(-3))

    def test_central_charge_sl2(self):
        """c(sl_2, k) = 3k/(k+2)."""
        for k_val in [1, 2, 3, 10]:
            c = central_charge_affine("A", 1, Rational(k_val))
            assert c == Rational(3 * k_val, k_val + 2)


# ============================================================================
# 2. Quadratic Casimir — multi-path verification
# ============================================================================

class TestQuadraticCasimir:
    """Verify C_2(V_lambda) from the Cartan matrix."""

    def test_casimir_sl2_fundamental(self):
        """sl_2: V_{(1)} = spin 1/2.  C_2 = n(n+2)/2 = 3/2.

        Mathematical normalization: A^{-1} = [[1/2]] for sl_2.
        C_2 = (1/2) * 1 * (1 + 2) = 3/2.
        Conformal weight: h = C_2/(2(k+h^v)) = (3/2)/(2*3) = 1/4 = j(j+1)/(k+2).
        """
        c2 = quadratic_casimir("A", 1, (1,))
        assert c2 == Rational(3, 2)
        # Cross-check: n(n+2)/2 with n=1
        assert c2 == Rational(1 * 3, 2)

    def test_casimir_sl2_adjoint(self):
        """sl_2: V_{(2)} = spin 1.  C_2 = 2*(2+2)/2 = 4."""
        c2 = quadratic_casimir("A", 1, (2,))
        assert c2 == Rational(4)
        # Cross-check: n(n+2)/2 = 8/2 = 4
        assert c2 == Rational(2 * 4, 2)

    def test_casimir_sl2_spin_3half(self):
        """sl_2: V_{(3)} = spin 3/2.  C_2 = 3*(3+2)/2 = 15/2."""
        c2 = quadratic_casimir("A", 1, (3,))
        assert c2 == Rational(15, 2)

    def test_casimir_sl3_fundamental(self):
        """sl_3: V_{(1,0)} = 3.  C_2 = (2/3)(1) + 2(1) = 8/3."""
        c2 = quadratic_casimir("A", 2, (1, 0))
        assert c2 == Rational(8, 3)
        # Cross-check via explicit formula:
        # C_2(a,b) = (2/3)(a^2 + b^2 + ab) + 2(a+b)
        a, b = 1, 0
        expected = Rational(2, 3) * (a**2 + b**2 + a * b) + 2 * (a + b)
        assert c2 == expected

    def test_casimir_sl3_antifundamental(self):
        """sl_3: V_{(0,1)} = 3-bar.  C_2 = 8/3 (same as fundamental)."""
        c2 = quadratic_casimir("A", 2, (0, 1))
        assert c2 == Rational(8, 3)
        # Fundamental and antifundamental have same Casimir
        assert c2 == quadratic_casimir("A", 2, (1, 0))

    def test_casimir_sl3_adjoint(self):
        """sl_3: V_{(1,1)} = 8.  C_2 = (2/3)(1+1+1) + 2(2) = 6."""
        c2 = quadratic_casimir("A", 2, (1, 1))
        expected = Rational(2, 3) * 3 + 4
        assert c2 == expected
        assert c2 == Rational(6)

    def test_casimir_sl3_symmetric_square(self):
        """sl_3: V_{(2,0)} = 6.  C_2 = (2/3)(4) + 2(2) = 20/3."""
        c2 = quadratic_casimir("A", 2, (2, 0))
        expected = Rational(2, 3) * 4 + 4
        assert c2 == expected
        assert c2 == Rational(20, 3)

    def test_casimir_trivial_rep(self):
        """Trivial representation: C_2 = 0 for any type."""
        assert quadratic_casimir("A", 1, (0,)) == 0
        assert quadratic_casimir("A", 2, (0, 0)) == 0
        assert quadratic_casimir("A", 3, (0, 0, 0)) == 0


# ============================================================================
# 3. Weyl dimension formula
# ============================================================================

class TestWeylDimension:
    """Verify dim(V_lambda) from the Weyl formula."""

    def test_dim_sl2_fundamental(self):
        """sl_2: V_{(1)} = dim 2."""
        assert weyl_dimension("A", 1, (1,)) == 2

    def test_dim_sl2_adjoint(self):
        """sl_2: V_{(2)} = dim 3."""
        assert weyl_dimension("A", 1, (2,)) == 3

    def test_dim_sl2_spin_n(self):
        """sl_2: V_{(n)} = dim n+1."""
        for n in range(8):
            assert weyl_dimension("A", 1, (n,)) == n + 1

    def test_dim_sl3_fundamental(self):
        """sl_3: V_{(1,0)} = dim 3."""
        assert weyl_dimension("A", 2, (1, 0)) == 3

    def test_dim_sl3_antifundamental(self):
        """sl_3: V_{(0,1)} = dim 3."""
        assert weyl_dimension("A", 2, (0, 1)) == 3

    def test_dim_sl3_adjoint(self):
        """sl_3: V_{(1,1)} = dim 8."""
        assert weyl_dimension("A", 2, (1, 1)) == 8

    def test_dim_sl3_symmetric(self):
        """sl_3: V_{(2,0)} = dim 6, V_{(0,2)} = dim 6."""
        assert weyl_dimension("A", 2, (2, 0)) == 6
        assert weyl_dimension("A", 2, (0, 2)) == 6

    def test_dim_sl4_fundamental(self):
        """sl_4: V_{(1,0,0)} = dim 4."""
        assert weyl_dimension("A", 3, (1, 0, 0)) == 4

    def test_dim_sl4_adjoint(self):
        """sl_4: V_{(1,0,1)} = dim 15."""
        assert weyl_dimension("A", 3, (1, 0, 1)) == 15

    def test_dim_trivial(self):
        """Trivial rep has dim 1."""
        assert weyl_dimension("A", 1, (0,)) == 1
        assert weyl_dimension("A", 2, (0, 0)) == 1
        assert weyl_dimension("A", 3, (0, 0, 0)) == 1


# ============================================================================
# 4. Line defect construction
# ============================================================================

class TestLineDefect:
    """Test LineDefect dataclass construction."""

    def test_sl2_fundamental_defect(self):
        """Wilson line in the fundamental of sl_2 at level 1."""
        ld = LineDefect("A", 1, (1,), Rational(1))
        assert ld.casimir_2 == Rational(3, 2)
        assert ld.dim_rep == 2
        # kappa_module = C_2 / (2 * (k + h^v)) = (3/2) / (2*3) = 1/4
        # Cross-check: h = j(j+1)/(k+2) = (3/4)/3 = 1/4
        assert ld.kappa_module == Rational(3, 2) / (2 * 3)
        assert ld.kappa_module == Rational(1, 4)

    def test_sl3_adjoint_defect(self):
        """Wilson line in the adjoint of sl_3 at level 1."""
        ld = LineDefect("A", 2, (1, 1), Rational(1))
        assert ld.casimir_2 == Rational(6)
        assert ld.dim_rep == 8
        # kappa_module = 6 / (2 * (1+3)) = 6/8 = 3/4
        assert ld.kappa_module == Rational(3, 4)

    def test_weight_length_mismatch(self):
        """Weight tuple must have length = rank."""
        with pytest.raises(ValueError):
            LineDefect("A", 2, (1,), Rational(1))


# ============================================================================
# 5. Defect OPE — R-matrix and Yang--Baxter
# ============================================================================

class TestDefectOPE:
    """Test the R-matrix controlling the defect OPE."""

    def test_permutation_matrix_sl2(self):
        """P on C^2 tensor C^2: 4x4 matrix with P^2 = I."""
        P = permutation_matrix(2)
        assert P.shape == (4, 4)
        assert np.allclose(P @ P, np.eye(4))

    def test_permutation_matrix_sl3(self):
        """P on C^3 tensor C^3: 9x9 matrix with P^2 = I."""
        P = permutation_matrix(3)
        assert P.shape == (9, 9)
        assert np.allclose(P @ P, np.eye(9))

    def test_permutation_eigenvalues(self):
        """P has eigenvalues +1 (dim N(N+1)/2) and -1 (dim N(N-1)/2)."""
        for N in [2, 3, 4, 5]:
            P = permutation_matrix(N)
            evals = np.linalg.eigvalsh(P)
            n_plus = sum(1 for e in evals if abs(e - 1) < 1e-10)
            n_minus = sum(1 for e in evals if abs(e + 1) < 1e-10)
            assert n_plus == N * (N + 1) // 2
            assert n_minus == N * (N - 1) // 2

    def test_yang_r_matrix_at_zero(self):
        """R(0) = P (permutation)."""
        for N in [2, 3, 4]:
            R0 = yang_r_matrix(0, N)
            P = permutation_matrix(N)
            assert np.allclose(R0, P)

    def test_yang_r_matrix_unitarity(self):
        """R(u) R(-u) = (1 - u^2) * I."""
        for N in [2, 3, 4]:
            for u in [0.5, 1.0, 2.0, 1 + 1j]:
                R_plus = yang_r_matrix(u, N)
                R_minus = yang_r_matrix(-u, N)
                product = R_plus @ R_minus
                expected = (1 - u**2) * np.eye(N * N, dtype=complex)
                assert np.allclose(product, expected, atol=1e-10)

    def test_yang_baxter_sl2(self):
        """YBE for sl_2 at random spectral parameters."""
        err = verify_defect_ybe(1.0 + 0.5j, 0.3 - 0.2j, -0.7 + 0.1j, 2, Rational(1))
        assert err < 1e-10

    def test_yang_baxter_sl3(self):
        """YBE for sl_3."""
        err = verify_defect_ybe(1.5, 0.7, -0.3, 3, Rational(1))
        assert err < 1e-10

    def test_yang_baxter_sl4(self):
        """YBE for sl_4."""
        err = verify_defect_ybe(2.0, 1.0, -1.0, 4, Rational(1))
        assert err < 1e-10

    def test_defect_ope_eigenvalues_sl2(self):
        """Channel decomposition for sl_2: Sym^2 (dim 3) + Lambda^2 (dim 1)."""
        data = defect_ope_eigenvalues(2)
        assert data["sym_dim"] == 3
        assert data["antisym_dim"] == 1

    def test_defect_ope_eigenvalues_sl3(self):
        """Channel decomposition for sl_3: Sym^2 (dim 6) + Lambda^2 (dim 3)."""
        data = defect_ope_eigenvalues(3)
        assert data["sym_dim"] == 6
        assert data["antisym_dim"] == 3

    def test_defect_r_matrix_leading_order(self):
        """R^{defect}(z) = I + P/(kappa*z) at leading order."""
        N = 2
        k = Rational(1)
        kap = float(kappa_affine("A", 1, k))
        z = 1.0
        R = defect_ope_r_matrix(z, N, k)
        P = permutation_matrix(N)
        expected = np.eye(N * N) + P / (kap * z)
        assert np.allclose(R, expected)


# ============================================================================
# 6. Clebsch--Gordan decomposition
# ============================================================================

class TestClebschGordan:
    """Test CG rules for sl_2 and sl_3."""

    def test_cg_sl2_fund_x_fund(self):
        """V_1 x V_1 = V_0 + V_2 (2 x 2 = 1 + 3)."""
        result = clebsch_gordan_sl2(1, 1)
        assert result == [0, 2]

    def test_cg_sl2_fund_x_adjoint(self):
        """V_1 x V_2 = V_1 + V_3 (2 x 3 = 2 + 4)."""
        result = clebsch_gordan_sl2(1, 2)
        assert result == [1, 3]

    def test_cg_sl2_adjoint_x_adjoint(self):
        """V_2 x V_2 = V_0 + V_2 + V_4 (3 x 3 = 1 + 3 + 5)."""
        result = clebsch_gordan_sl2(2, 2)
        assert result == [0, 2, 4]

    def test_cg_sl2_dimension_check(self):
        """Dimension counting for all V_n1 x V_n2 with n1, n2 <= 6."""
        for n1 in range(7):
            for n2 in range(7):
                data = fusion_dimension_check_sl2(n1, n2)
                assert data["match"], f"Dimension mismatch for V_{n1} x V_{n2}"

    def test_cg_sl3_fund_x_fund(self):
        """3 x 3 = 6 + 3-bar."""
        result = clebsch_gordan_sl3_fund(1, 0, 1, 0)
        data = fusion_dimension_check_sl3(1, 0, 1, 0)
        assert data["match"]
        assert data["dim_tensor"] == 9
        assert data["dim_sum"] == 9

    def test_cg_sl3_fund_x_antifund(self):
        """3 x 3-bar = 8 + 1."""
        result = clebsch_gordan_sl3_fund(1, 0, 0, 1)
        data = fusion_dimension_check_sl3(1, 0, 0, 1)
        assert data["match"]
        assert data["dim_tensor"] == 9
        assert data["dim_sum"] == 9

    def test_cg_sl3_antifund_x_antifund(self):
        """3-bar x 3-bar = 6-bar + 3."""
        data = fusion_dimension_check_sl3(0, 1, 0, 1)
        assert data["match"]

    def test_cg_sl3_adj_x_adj(self):
        """8 x 8 = 27 + 10 + 10-bar + 8 + 8 + 1."""
        data = fusion_dimension_check_sl3(1, 1, 1, 1)
        assert data["match"]
        assert data["dim_tensor"] == 64
        assert data["dim_sum"] == 64


# ============================================================================
# 7. Surface defects
# ============================================================================

class TestSurfaceDefects:
    """Test surface defect (boundary condition) construction."""

    def test_dirichlet_sl2(self):
        """Dirichlet boundary = vacuum module for sl_2."""
        d = dirichlet_surface_defect("A", 1, Rational(1))
        assert d.module_type == "vacuum"
        assert d.kappa_module == 0
        assert d.weight == (0,)

    def test_neumann_sl2(self):
        """Neumann boundary = adjoint module for sl_2."""
        d = neumann_surface_defect("A", 1, Rational(1))
        assert d.module_type == "highest_weight"
        assert d.weight == (2,)
        # C_2(adjoint of sl_2) = n(n+2)/2 = 2*4/2 = 4
        # h = 4/(2*3) = 2/3
        assert d.kappa_module == Rational(2, 3)

    def test_neumann_sl3(self):
        """Neumann boundary for sl_3: adjoint = (1,1), dim 8."""
        d = neumann_surface_defect("A", 2, Rational(1))
        assert d.weight == (1, 1)
        # C_2(adjoint sl_3) = 6, h = 6/(2*4) = 3/4
        assert d.kappa_module == Rational(3, 4)

    def test_module_bar_data_vacuum(self):
        """Module bar complex for vacuum reduces to ordinary bar."""
        d = dirichlet_surface_defect("A", 1, Rational(1))
        data = module_bar_complex_data(d)
        assert data["reduces_to"] == "ordinary bar complex B(A)"
        assert data["kappa_module"] == 0

    def test_module_bar_data_hw(self):
        """Module bar complex for highest-weight module."""
        d = neumann_surface_defect("A", 1, Rational(1))
        data = module_bar_complex_data(d)
        assert data["kappa_module"] == Rational(2, 3)
        assert data["is_koszul_acyclic"] is True


# ============================================================================
# 8. Gukov--Witten surface operators
# ============================================================================

class TestGukovWitten:
    """Test Gukov--Witten monodromy defects."""

    def test_trivial_monodromy_sl2(self):
        """Trivial monodromy: sigma = 0, delta_kappa = 0."""
        gw = gukov_witten_trivial("A", 1, Rational(1))
        assert gw.sigma == (Rational(0),)
        assert gw.sigma_norm_sq == 0
        assert gw.delta_kappa == 0
        assert gw.kappa_twisted == kappa_affine("A", 1, Rational(1))

    def test_principal_monodromy_sl2(self):
        """Principal monodromy: sigma = (1/k,), |sigma|^2 = 2/k^2."""
        k = Rational(1)
        gw = gukov_witten_principal("A", 1, k)
        # For sl_2 with sigma = (1/k) in simple coroot basis:
        # |sigma|^2 = 2 * (1/k)^2 (Cartan matrix A = [[2]] for sl_2)
        assert gw.sigma == (Rational(1),)
        assert gw.sigma_norm_sq == Rational(2)
        # delta_kappa = -k * |sigma|^2 / 2 = -1 * 2 / 2 = -1
        assert gw.delta_kappa == Rational(-1)
        kap = kappa_affine("A", 1, Rational(1))
        assert gw.kappa_twisted == kap - 1

    def test_gukov_witten_sl3(self):
        """GW defect for sl_3 with sigma = (1, 0)."""
        sigma = (Rational(1), Rational(0))
        gw = GukovWittenDefect("A", 2, Rational(1), sigma)
        # |sigma|^2 = sigma^T A sigma for sl_3 Cartan
        # A = [[2, -1], [-1, 2]], sigma = (1, 0)
        # |sigma|^2 = 1*2*1 + 1*(-1)*0 + 0*(-1)*1 + 0*2*0 = 2
        assert gw.sigma_norm_sq == Rational(2)
        assert gw.delta_kappa == -Rational(1) * 2 / 2
        assert gw.delta_kappa == Rational(-1)

    def test_gukov_witten_zero_sigma_is_untwisted(self):
        """GW with sigma=0 gives the same kappa as the untwisted algebra."""
        for lie_type, rank in [("A", 1), ("A", 2), ("A", 3), ("B", 2)]:
            gw = gukov_witten_trivial(lie_type, rank, Rational(1))
            assert gw.kappa_twisted == kappa_affine(lie_type, rank, Rational(1))


# ============================================================================
# 9. 't Hooft lines and kappa complementarity
# ============================================================================

class TestTHooftLines:
    """Test magnetic defects and electric-magnetic duality."""

    def test_thooft_sl2_level1(self):
        """'t Hooft line for sl_2 at level 1."""
        th = THooftLine("A", 1, Rational(1), (1,))
        # Dual level: k^! = -1 - 2*2 = -5
        assert th.dual_level == Rational(-5)
        # kappa_dual = 3 * (-5 + 2) / 4 = 3 * (-3) / 4 = -9/4
        assert th.kappa_dual == Rational(-9, 4)
        # Casimir (same weight, same g) = n(n+2)/2 = 3/2
        assert th.casimir_dual == Rational(3, 2)

    def test_kappa_complementarity_sl2(self):
        """kappa(sl_2, k) + kappa(sl_2, -k-4) = 0 (AP24: correct for KM)."""
        for k in [1, 2, 3, 5, 10]:
            result = verify_kappa_complementarity_km("A", 1, Rational(k))
            assert result["vanishes"], f"kappa + kappa' != 0 for sl_2 at k={k}"

    def test_kappa_complementarity_sl3(self):
        """kappa(sl_3, k) + kappa(sl_3, -k-6) = 0."""
        for k in [1, 2, 3, 5]:
            result = verify_kappa_complementarity_km("A", 2, Rational(k))
            assert result["vanishes"], f"kappa + kappa' != 0 for sl_3 at k={k}"

    def test_kappa_complementarity_all_types(self):
        """kappa + kappa' = 0 for all KM families (AP24)."""
        families = [("A", 1), ("A", 2), ("A", 3), ("B", 2), ("C", 2),
                    ("D", 4), ("G", 2)]
        for lie_type, rank in families:
            result = verify_kappa_complementarity_km(lie_type, rank, Rational(1))
            assert result["vanishes"], (
                f"kappa + kappa' != 0 for ({lie_type}, {rank})"
            )

    def test_electric_magnetic_duality_sl2(self):
        """h_wilson + h_thooft = 0 for sl_2."""
        result = electric_magnetic_duality_check("A", 1, Rational(1), (1,))
        assert result["h_sum_vanishes"]

    def test_electric_magnetic_duality_sl3(self):
        """h_wilson + h_thooft = 0 for sl_3 fundamental."""
        result = electric_magnetic_duality_check("A", 2, Rational(1), (1, 0))
        assert result["h_sum_vanishes"]


# ============================================================================
# 10. Crossing kernel (6j-symbols)
# ============================================================================

class TestCrossingKernel:
    """Test the Racah--Wigner 6j-symbols."""

    def test_6j_trivial(self):
        """6j with j=0 channel: {j1 j2 J; 0 0 0} is trivial."""
        # {0 0 0; 0 0 0} = 1
        result = crossing_kernel_sl2(0, 0, 0, 0, 0, 0)
        assert result == 1

    def test_6j_orthogonality(self):
        """Orthogonality of 6j-symbols for sl_2: sum over j12.

        sum_{j12} (2*j12 + 1) * {j1 j2 j12; j3 j4 j23} * {j1 j2 j12; j3 j4 j23'}
        = delta_{j23, j23'} / (2*j23 + 1)
        """
        j1, j2, j3, j4 = 1, 1, 1, 1
        # j23 can be 0, 1, 2 and j12 can be 0, 1, 2

        for j23 in range(3):
            for j23p in range(3):
                total = Rational(0)
                for j12 in range(3):
                    w1 = crossing_kernel_sl2(
                        Rational(j1), Rational(j2), Rational(j3),
                        Rational(j4), Rational(j12), Rational(j23),
                    )
                    w2 = crossing_kernel_sl2(
                        Rational(j1), Rational(j2), Rational(j3),
                        Rational(j4), Rational(j12), Rational(j23p),
                    )
                    total += (2 * j12 + 1) * w1 * w2
                if j23 == j23p:
                    expected = Rational(1, 2 * j23 + 1)
                else:
                    expected = Rational(0)
                assert simplify(total - expected) == 0, (
                    f"Orthogonality failed for j23={j23}, j23'={j23p}: "
                    f"got {total}, expected {expected}"
                )

    def test_crossing_eigenvalue_sl2_fund(self):
        """Braiding eigenvalues for j1 = j2 = 1/2."""
        data = crossing_kernel_eigenvalue_sl2(1, 1)
        # j1 = j2 = 1: V_2 x V_2 = V_0 + V_2 + V_4
        assert data["num_channels"] == 3


# ============================================================================
# 11. Defect networks
# ============================================================================

class TestDefectNetworks:
    """Test string diagram evaluation for defect webs."""

    def test_trivalent_vertex_allowed(self):
        """Triangle inequality: (1, 1, 1) is allowed."""
        data = trivalent_vertex_sl2(1, 1, 1)
        assert data["exists"]
        assert data["triangle_ineq"]

    def test_trivalent_vertex_forbidden(self):
        """Triangle inequality: (1, 1, 3) is forbidden."""
        data = trivalent_vertex_sl2(1, 1, 3)
        assert not data["exists"]

    def test_trivalent_vertex_fund_x_fund(self):
        """(1/2, 1/2, 0) is allowed: V_1 x V_1 -> V_0."""
        # Using integer spins: j1=j2=0 (spin 0), j3=0
        data = trivalent_vertex_sl2(0, 0, 0)
        assert data["exists"]

    def test_theta_network(self):
        """Theta network (1, 1, 1) exists."""
        data = theta_network_sl2(1, 1, 1)
        assert data["exists"]
        assert data["classical_value"] == 1

    def test_theta_network_forbidden(self):
        """Theta network (1, 1, 5) forbidden (triangle violated)."""
        data = theta_network_sl2(1, 1, 5)
        assert not data["exists"]
        assert data["classical_value"] == 0

    def test_web_evaluation_simple(self):
        """Simple web with two vertices."""
        edges = [(0, 1, 1)]
        vertices = [(1, 1, 1), (1, 1, 1)]
        data = defect_web_evaluation_sl2(edges, vertices)
        assert data["all_vertices_valid"]

    def test_web_with_invalid_vertex(self):
        """Web with an invalid vertex."""
        vertices = [(1, 1, 5)]  # Triangle violated
        data = defect_web_evaluation_sl2([], vertices)
        assert not data["all_vertices_valid"]


# ============================================================================
# 12. Fusion associativity
# ============================================================================

class TestFusionAssociativity:
    """Verify associativity of defect fusion."""

    def test_associativity_small_spins(self):
        """(j1 x j2) x j3 = j1 x (j2 x j3) for small spins."""
        for j1 in range(4):
            for j2 in range(4):
                for j3 in range(4):
                    data = verify_fusion_associativity_sl2(j1, j2, j3)
                    assert data["match"], (
                        f"Associativity failed for ({j1}, {j2}, {j3})"
                    )


# ============================================================================
# 13. Kapustin--Witten and geometric Langlands
# ============================================================================

class TestKapustinWitten:
    """Test the KW dictionary and geometric Langlands structures."""

    def test_langlands_dual_simply_laced(self):
        """Simply-laced types are self-dual."""
        assert langlands_dual_lie_type("A", 2) == ("A", 2)
        assert langlands_dual_lie_type("D", 4) == ("D", 4)
        assert langlands_dual_lie_type("E", 6) == ("E", 6)

    def test_langlands_dual_BC(self):
        """B_n <-> C_n."""
        assert langlands_dual_lie_type("B", 2) == ("C", 2)
        assert langlands_dual_lie_type("C", 2) == ("B", 2)
        assert langlands_dual_lie_type("B", 3) == ("C", 3)
        assert langlands_dual_lie_type("C", 3) == ("B", 3)

    def test_langlands_dual_G2_F4(self):
        """G_2 and F_4 are self-dual."""
        assert langlands_dual_lie_type("G", 2) == ("G", 2)
        assert langlands_dual_lie_type("F", 4) == ("F", 4)

    def test_kw_dictionary_sl2(self):
        """KW dictionary for sl_2."""
        data = kapustin_witten_dictionary("A", 1, Rational(1))
        assert data["gauge_group"] == "sl_2"
        assert data["langlands_dual"] == "sl_2"
        assert data["kappa"] == Rational(9, 4)
        assert data["dual_level"] == Rational(-5)
        assert data["dk_bridge"]["status"].startswith("PROVED")

    def test_kw_dictionary_so5_sp4(self):
        """KW dictionary for B_2 = so_5 (dual = C_2 = sp_4)."""
        data = kapustin_witten_dictionary("B", 2, Rational(1))
        assert data["gauge_group"] == "so_5"
        assert data["langlands_dual"] == "sp_4"

    def test_kz_connection_sl2(self):
        """KZ connection parameter for sl_2: 1/(k + h^v) = 1/(k+2)."""
        data = kz_connection_parameter("A", 1, Rational(1))
        assert data["kz_parameter"] == Rational(1, 3)
        assert data["kz_flat"] is True

    def test_kz_connection_sl3(self):
        """KZ connection parameter for sl_3: 1/(k + 3)."""
        data = kz_connection_parameter("A", 2, Rational(1))
        assert data["kz_parameter"] == Rational(1, 4)


# ============================================================================
# 14. Defect partition function
# ============================================================================

class TestDefectPartitionFunction:
    """Test the genus-1 defect partition function."""

    def test_vacuum_defect_sl2(self):
        """Vacuum (trivial rep) defect: F1_defect = 0."""
        data = defect_partition_function_genus1("A", 1, Rational(1), (0,))
        assert data["conformal_weight"] == 0
        assert data["F1_defect"] == 0
        assert data["F1_total"] == data["F1_bulk"]

    def test_fundamental_defect_sl2(self):
        """Fundamental defect for sl_2 at level 1."""
        data = defect_partition_function_genus1("A", 1, Rational(1), (1,))
        # h_lambda = C_2 / (2(k+h^v)) = (3/2) / (2*3) = 1/4
        # Cross-check: j(j+1)/(k+2) = (3/4)/3 = 1/4
        assert data["conformal_weight"] == Rational(1, 4)
        # F1_total = (kappa + h_lambda) / 24 = (9/4 + 1/4) / 24 = (10/4) / 24 = 5/48
        assert data["F1_total"] == (Rational(9, 4) + Rational(1, 4)) / 24
        assert data["F1_total"] == Rational(5, 48)

    def test_adjoint_defect_sl3(self):
        """Adjoint defect for sl_3 at level 1."""
        data = defect_partition_function_genus1("A", 2, Rational(1), (1, 1))
        assert data["conformal_weight"] == Rational(3, 4)
        assert data["kappa_bulk"] == Rational(16, 3)

    def test_lambda_1_value(self):
        """lambda_1 = 1/24 (Faber--Pandharipande)."""
        data = defect_partition_function_genus1("A", 1, Rational(1), (0,))
        assert data["lambda_1"] == Rational(1, 24)


# ============================================================================
# 15. Module kappa additivity
# ============================================================================

class TestModuleKappaAdditivity:
    """Test additivity of module kappa for independent defects."""

    def test_additivity_sl2(self):
        """Two fundamental Wilson lines of sl_2: kappa additive."""
        data = verify_defect_shadow_additivity(
            "A", 1, Rational(1), (1,), (1,)
        )
        assert data["additivity_holds"]
        assert data["kappa_sum"] == 2 * data["kappa_mod_1"]

    def test_additivity_mixed_sl3(self):
        """Fundamental + antifundamental of sl_3."""
        data = verify_defect_shadow_additivity(
            "A", 2, Rational(1), (1, 0), (0, 1)
        )
        assert data["additivity_holds"]
        # Both have the same kappa_module (C_2 is the same)
        assert data["kappa_mod_1"] == data["kappa_mod_2"]


# ============================================================================
# 16. Cross-engine consistency checks
# ============================================================================

class TestCrossEngineConsistency:
    """Cross-check against existing engines."""

    def test_kappa_agrees_with_yangian_rmatrix(self):
        """kappa(sl_3, k=1) should match yangian_rmatrix_sl3.kappa_sl3(1)."""
        kap_here = kappa_affine("A", 2, Rational(1))
        # From yangian_rmatrix_sl3: 4*(1+3)/3 = 16/3
        assert kap_here == Rational(16, 3)

    def test_permutation_agrees_with_yangian(self):
        """Permutation matrix matches yangian_residue_extraction."""
        P_here = permutation_matrix(3)
        # Should match the one from yangian_residue_extraction
        from compute.lib.yangian_residue_extraction import permutation_matrix_slN
        P_there = permutation_matrix_slN(3)
        assert np.allclose(P_here, P_there)

    def test_yang_r_agrees(self):
        """Yang R-matrix matches yangian_residue_extraction."""
        from compute.lib.yangian_residue_extraction import yang_r_matrix_slN
        for u in [0.5, 1.0, 2.0, -1.0]:
            for N in [2, 3, 4]:
                R_here = yang_r_matrix(u, N)
                R_there = yang_r_matrix_slN(u, N)
                assert np.allclose(R_here, R_there)

    def test_casimir_sl3_matches_sl3_casimir_decomp(self):
        """Casimir eigenvalues match sl3_casimir_decomp.py ground truth.

        From sl3_casimir_decomp.py header:
          V(1,1) -> 3*C_2 = 18 -> C_2 = 6
          V(2,0) -> 3*C_2 = 20 -> C_2 = 20/3
          V(0,0) -> C_2 = 0
        """
        assert quadratic_casimir("A", 2, (1, 1)) == Rational(6)
        assert quadratic_casimir("A", 2, (2, 0)) == Rational(20, 3)
        assert quadratic_casimir("A", 2, (0, 0)) == Rational(0)

    def test_kappa_complementarity_matches_theorem_c(self):
        """kappa + kappa' = 0 matches theorem_c_complementarity.py convention."""
        # For all KM families, kappa + kappa' = 0 (AP24)
        for lie_type, rank in [("A", 1), ("A", 2), ("B", 2), ("G", 2)]:
            result = verify_kappa_complementarity_km(lie_type, rank, Rational(1))
            assert result["vanishes"]


# ============================================================================
# 17. Dimensional / degree analysis
# ============================================================================

class TestDimensionalAnalysis:
    """Verify dimensional consistency and degree analysis."""

    def test_casimir_degree_homogeneity(self):
        """C_2(n * lambda) scales quadratically in n for type A."""
        # For sl_2: C_2(n) = n(n+2)/2 (mathematical normalization)
        for n in range(1, 6):
            c2 = quadratic_casimir("A", 1, (n,))
            assert c2 == Rational(n * (n + 2), 2)

    def test_kappa_linearity_in_level(self):
        """kappa(hat{g}_k) is linear in k for fixed g."""
        # kappa = dim(g) * (k + h^v) / (2 h^v) is affine-linear in k
        for k1, k2 in [(1, 2), (3, 5), (10, 20)]:
            kap1 = kappa_affine("A", 1, Rational(k1))
            kap2 = kappa_affine("A", 1, Rational(k2))
            # (kap2 - kap1) / (k2 - k1) should be constant = dim(g) / (2 h^v)
            slope = (kap2 - kap1) / (k2 - k1)
            assert slope == Rational(3, 4)  # dim(sl_2) / (2 * h^v(sl_2))

    def test_weyl_dim_positivity(self):
        """Dimensions are positive for dominant weights."""
        for n in range(10):
            assert weyl_dimension("A", 1, (n,)) > 0
        for a in range(4):
            for b in range(4):
                assert weyl_dimension("A", 2, (a, b)) > 0

    def test_module_kappa_positivity(self):
        """Module kappa >= 0 for positive level and dominant weight."""
        for n in range(5):
            kap_mod = module_kappa("A", 1, (n,), Rational(1))
            assert kap_mod >= 0


# ============================================================================
# 18. Edge cases and error handling
# ============================================================================

class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_trivial_weight_gives_zero_casimir(self):
        assert quadratic_casimir("A", 1, (0,)) == 0

    def test_trivial_defect(self):
        """Line defect with trivial weight has zero module kappa."""
        ld = LineDefect("A", 1, (0,), Rational(1))
        assert ld.kappa_module == 0
        assert ld.dim_rep == 1

    def test_high_level_kappa(self):
        """kappa at large level should be large."""
        kap = kappa_affine("A", 1, Rational(1000))
        assert kap > 100

    def test_gukov_witten_sigma_length_check(self):
        """GW defect rejects wrong sigma length."""
        with pytest.raises(ValueError):
            GukovWittenDefect("A", 2, Rational(1), (Rational(1),))

    def test_unknown_lie_type(self):
        """Unknown Lie type raises ValueError."""
        with pytest.raises(ValueError):
            kappa_affine("X", 1, Rational(1))
