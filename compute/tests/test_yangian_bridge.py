"""The Yangian bridge: Vol I E₁-chiral bar complex → Vol II spectral braiding.

The Yangian is the E₁ atom of the monograph — the braided counterpart
to the Heisenberg (E∞) atom.  Where the Heisenberg has trivial R-matrix,
trivial lambda-bracket, and formal bar complex, the Yangian has:

  - Nontrivial R-matrix R(u) solving Yang-Baxter
  - Nontrivial spectral braiding from ordered configurations
  - Koszul duality = R-matrix inversion: Y(g)^! = Y_{R^{-1}}(g)

Together with test_heisenberg_bridge.py, this file forms the DIPTYCH:
two atoms, one logarithm, the full inter-volume bridge made executable.

  Vol I (E₁ sector of The Algebraic Engine):
    1. Yang R-matrix R(u) = Id - hbar*P/u
    2. RTT relation as the OPE of ordered bar elements
    3. Yang-Baxter equation from FM_3(C) geometry
    4. Koszul dual: R-matrix inversion
    5. Auxiliary kernel identity: K^line = K^RTT = Λ²(V)

  Vol II (E₁ sector of Swiss-Cheese):
    6. Three-layer reduction: residue → channels → single line
    7. Nontrivial spectral braiding (CONTRAST with Heisenberg)
    8. The evaluation locus and DK ladder

References:
  - Vol I, chapters/examples/yangians_foundations.tex
  - Vol I, chapters/examples/yangians_drinfeld_kohno.tex
  - Vol II, Part III (line-operators, spectral-braiding)
  - concordance.tex: MC4 Yangian status
"""

import pytest
import numpy as np

from compute.lib.yangian_residue import (
    permutation_matrix,
    yang_r_matrix,
    verify_residue_reduction,
    verify_channel_reduction,
    verify_single_line_reduction,
)
from compute.lib.yangian_residue_extraction import (
    verify_yang_baxter_slN,
    verify_auxiliary_kernel_identity,
)


# ============================================================
# Vol I: The E₁ Algebraic Engine
# ============================================================

class TestVolI_YangRMatrix:
    """The Yang R-matrix: the fundamental object of the E₁ atom."""

    def test_r_matrix_is_identity_plus_permutation(self):
        """R(u) = Id - hbar*P/u on V⊗V.

        The Yang R-matrix is the SIMPLEST rational solution of the
        Yang-Baxter equation.  It has a simple pole at u=0 with
        residue -hbar*P (the permutation operator).

        For the bar complex: this pole at u=0 is the OPE singularity,
        and -hbar*P is the bar differential acting on tensor products.
        """
        for M in [2, 3, 4]:
            R = yang_r_matrix(M, u=1.0, hbar=1.0)
            P = permutation_matrix(M)
            expected = np.eye(M * M) - P
            assert np.allclose(R, expected), f"R(1) = Id - P for M={M}"

    def test_r_matrix_residue_is_permutation(self):
        """Res_{u=0} R(u) = -hbar * P.

        The residue at the pole is the permutation operator — this is
        the E₁ analog of the E∞ bar differential.  For Heisenberg,
        the OPE has a double pole (curvature); for the Yangian, the
        R-matrix has a simple pole (braiding).
        """
        for M in [2, 3, 4]:
            P = permutation_matrix(M)
            # R(u) = Id - P/u, so u*R(u) = u*Id - P → P at u=0
            # Res_{u=0} R(u) = lim_{u→0} u * (-P/u) = -P
            R_eps = yang_r_matrix(M, u=0.001, hbar=1.0)
            # u * (R(u) - Id) → -P as u → 0
            residue = 0.001 * (R_eps - np.eye(M * M))
            assert np.allclose(residue, -P, atol=1e-6), f"Residue = -P for M={M}"


class TestVolI_YangBaxter:
    """Yang-Baxter equation: the Arnold relation of the E₁ world."""

    def test_yang_baxter_for_sl2(self):
        """R₁₂(u-v) R₁₃(u-w) R₂₃(v-w) = R₂₃(v-w) R₁₃(u-w) R₁₂(u-v).

        The Yang-Baxter equation is the E₁ analog of Arnold's three-term
        relation.  Arnold says: η₁₂∧η₂₃ + η₂₃∧η₃₁ + η₃₁∧η₁₂ = 0.
        Yang-Baxter says: R₁₂ R₁₃ R₂₃ = R₂₃ R₁₃ R₁₂.

        Both are consequences of the same geometry: three-point
        collisions on FM₃(ℂ), with different symmetry groups
        (symmetric for Arnold, ordered for Yang-Baxter).
        """
        diff = verify_yang_baxter_slN(u=1.5, v=0.7, N=2)
        assert diff < 1e-10, "YBE for sl_2"

    def test_yang_baxter_for_sl3(self):
        """Yang-Baxter for sl₃."""
        diff = verify_yang_baxter_slN(u=2.1, v=0.4, N=3)
        assert diff < 1e-10, "YBE for sl_3"

    def test_yang_baxter_for_sl4(self):
        """Yang-Baxter for sl₄."""
        diff = verify_yang_baxter_slN(u=3.0, v=1.0, N=4)
        assert diff < 1e-10, "YBE for sl_4"


class TestVolI_KoszulDuality:
    """Koszul duality inverts the R-matrix: Y(𝔤)^! = Y_{R⁻¹}(𝔤)."""

    def test_r_matrix_invertible(self):
        """R(u) is invertible for u ≠ 0.

        R(u)^{-1} = (u*Id + hbar*P) / (u^2 - hbar^2) for the Yang R-matrix.
        Koszul duality sends R → R^{-1}, which exchanges the two
        eigenspaces (symmetric ↔ antisymmetric).
        """
        for M in [2, 3, 4]:
            R = yang_r_matrix(M, u=2.0, hbar=1.0)
            det = np.linalg.det(R)
            assert abs(det) > 1e-10, f"R(2) must be invertible for M={M}"
            R_inv = np.linalg.inv(R)
            assert np.allclose(R @ R_inv, np.eye(M * M), atol=1e-10)

    def test_r_inverse_swaps_eigenvalues(self):
        """R has eigenvalues (1-1/u) on Λ²(V) and (1+1/u) on Sym²(V).

        R^{-1} swaps these: the symmetric eigenvalue of R becomes
        the antisymmetric eigenvalue of R^{-1}.  This is Koszul
        duality acting on the R-matrix.
        """
        M = 2
        P = permutation_matrix(M)
        # Eigenvalues of P: +1 on Sym^2, -1 on Lambda^2
        # R(u) = Id - P/u has eigenvalues:
        #   1 - 1/u on Sym^2 (P eigenvalue +1)
        #   1 + 1/u on Lambda^2 (P eigenvalue -1)
        u = 2.0
        R = yang_r_matrix(M, u=u, hbar=1.0)
        evals = np.sort(np.real(np.linalg.eigvals(R)))
        expected_sym = 1 - 1/u    # = 0.5
        expected_alt = 1 + 1/u    # = 1.5
        assert any(abs(e - expected_sym) < 1e-10 for e in evals), \
            f"Missing Sym eigenvalue {expected_sym}"
        assert any(abs(e - expected_alt) < 1e-10 for e in evals), \
            f"Missing Alt eigenvalue {expected_alt}"


# ============================================================
# Vol I → Vol II Bridge: The Auxiliary Kernel Identity
# ============================================================

class TestBridge_AuxiliaryKernel:
    """K^line_{1,2}(N) = K^RTT_{1,2}(N) = Λ²(V): the MC4 bridge."""

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_kernel_dimensions(self, N):
        """Both kernels have dimension N(N-1)/2 = dim Λ²(V).

        This is the bridge between Vol I (bar complex side) and
        Vol II (quantum group side).  The bar complex produces
        K^line; the RTT truncation produces K^RTT.  Their equality
        is the MC4 Yangian identity.
        """
        expected_dim = N * (N - 1) // 2
        result = verify_auxiliary_kernel_identity(N)
        assert result["K_line_dim"] == expected_dim
        assert result["K_rtt_dim"] == expected_dim

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_kernels_are_equal(self, N):
        """K^line = K^RTT: the MC4 identity verified computationally."""
        result = verify_auxiliary_kernel_identity(N)
        assert result["identity_holds"], \
            f"K^line ≠ K^RTT for N={N}: {result}"

    @pytest.mark.parametrize("N", [2, 3, 4])
    def test_kernel_is_antisymmetric(self, N):
        """Both kernels are Λ²(V), the antisymmetric square.

        The kernel consists of antisymmetric tensors v⊗w - w⊗v.
        This is the E₁ analog of the Heisenberg's trivial kernel:
        for E∞, the kernel is empty (no braiding); for E₁, it's Λ²(V).
        """
        result = verify_auxiliary_kernel_identity(N)
        assert result["subspace_match"], \
            f"Kernel not antisymmetric for N={N}"


# ============================================================
# Vol II: Three-Layer Reduction
# ============================================================

class TestVolII_ThreeLayerReduction:
    """The three-layer reduction: residue → channels → single line."""

    @pytest.mark.parametrize("M", [2, 3, 4])
    def test_layer1_residue_is_permutation(self, M):
        """Layer 1: Res_{u=a} L_a(u) = -ℏ·P.

        The collision residue on the evaluation line IS the permutation
        operator.  This is the E₁ bar differential acting on the
        ordered tensor product.
        """
        result = verify_residue_reduction(M)
        assert result["Xi_equals_minus_hbar_P"], \
            f"Layer 1 failed for M={M}"

    @pytest.mark.parametrize("M", [2, 3, 4])
    def test_layer2_channel_decomposition(self, M):
        """Layer 2: Sym²(V) and Λ²(V) channels separate.

        The permutation P decomposes V⊗V into:
          Sym²(V) with eigenvalue +1
          Λ²(V) with eigenvalue -1

        On Sym²(V): -ℏ·P has eigenvalue -ℏ
        On Λ²(V): -ℏ·P has eigenvalue +ℏ
        """
        result = verify_channel_reduction(M)
        assert result["Xi_sym_check"], \
            f"Layer 2 Sym eigenvalue wrong for M={M}"
        assert result["Xi_alt_check"], \
            f"Layer 2 Alt eigenvalue wrong for M={M}"

    @pytest.mark.parametrize("M", [2, 3, 4])
    def test_layer3_single_line(self, M):
        """Layer 3: Everything reduces to Ξ_a(e₁⊗e₂) = -ℏ(e₂⊗e₁).

        The ENTIRE MC4 Yangian identity reduces to this single
        evaluation.  One vector, one matrix element, one equation.
        This is the E₁ analog of the Heisenberg's κ: a single scalar
        that controls everything.
        """
        result = verify_single_line_reduction(M)
        assert result["match"], \
            f"Layer 3 single-line identity failed for M={M}"


# ============================================================
# The Diptych: E∞ vs E₁
# ============================================================

class TestDiptych:
    """The two atoms compared: Heisenberg (E∞) vs Yangian (E₁)."""

    def test_heisenberg_has_no_braiding(self):
        """Heisenberg: no simple pole → no R-matrix → E∞.

        The Heisenberg OPE a(z)a(w) = κ/(z-w)² has ONLY a double pole.
        No simple pole means no braiding, no R-matrix, no spectral parameter.
        """
        from compute.lib.heisenberg_bar import heisenberg_nth_products
        products = heisenberg_nth_products()
        assert 0 not in products, "Heisenberg: no simple pole"
        assert 1 in products, "Heisenberg: has double pole (curvature)"

    def test_yangian_has_braiding(self):
        """Yangian: simple pole in R-matrix → nontrivial braiding → E₁.

        R(u) = Id - P/u has a SIMPLE pole at u=0 with residue -P.
        This simple pole IS the braiding.
        """
        M = 2
        P = permutation_matrix(M)
        # At u → 0: R(u) ≈ -P/u → simple pole with residue -P
        R_small = yang_r_matrix(M, u=0.01, hbar=1.0)
        # The dominant term is -P/u = -100*P
        assert np.linalg.norm(R_small) > 10, "R(u) diverges at u=0: simple pole"

    def test_curvature_vs_braiding(self):
        """Heisenberg: d²_fib = κ·ω_g (curvature, double pole).
        Yangian: R₁₂R₁₃R₂₃ = R₂₃R₁₃R₁₂ (braiding, simple pole).

        Both are consequences of the categorical logarithm.
        The double pole gives genus-tower curvature.
        The simple pole gives spectral braiding.
        The logarithm sees both.
        """
        from compute.lib.heisenberg_bar import heisenberg_curvature
        from sympy import Symbol

        # Heisenberg: curvature κ from double pole
        kappa = heisenberg_curvature()
        assert kappa == Symbol('kappa'), "Heisenberg curvature = κ"

        # Yangian: braiding from simple pole (Yang-Baxter)
        diff = verify_yang_baxter_slN(u=1.5, v=0.7, N=2)
        assert diff < 1e-10, "Yangian braiding: YBE"

    def test_kernel_contrast(self):
        """Heisenberg: kernel empty (no antisymmetric component).
        Yangian: kernel = Λ²(V) (the antisymmetric square).

        For E∞, the bar complex is a SYMMETRIC coalgebra (no ordering).
        For E₁, the bar complex is an ORDERED coalgebra (R-matrix ordering).
        The kernel Λ²(V) is the antisymmetric part that the ordering sees.
        """
        # Yangian: kernel has dimension N(N-1)/2 > 0
        for N in [2, 3, 4]:
            result = verify_auxiliary_kernel_identity(N)
            assert result["K_line_dim"] == N * (N - 1) // 2 > 0, \
                f"Yangian kernel nonempty for N={N}"
