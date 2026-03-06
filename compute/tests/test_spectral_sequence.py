"""Tests for spectral sequence computations.

Ground truth from prop:virasoro-koszul-acyclic, prop:E8-koszul-acyclic,
comp:virasoro-dim-table.
"""

import pytest

from compute.lib.spectral_sequence import (
    VIRASORO_BAR_COH,
    HEISENBERG_BAR_COH_E2_LEADING,
    SL2_BAR_COH,
    spectral_sequence_collapse,
    e2_page_virasoro,
    e2_page_heisenberg,
    e2_page_sl2,
    catalan,
    associahedron_f_vector,
    check_koszul_property,
    verify_spectral_sequences,
)


class TestVirasoroBarCoh:
    def test_first_dims(self):
        assert VIRASORO_BAR_COH[1] == 1
        assert VIRASORO_BAR_COH[2] == 2
        assert VIRASORO_BAR_COH[3] == 5

    def test_dim_5(self):
        assert VIRASORO_BAR_COH[5] == 30

    def test_dim_10(self):
        assert VIRASORO_BAR_COH[10] == 3610

    def test_e2_page(self):
        page = e2_page_virasoro(5)
        assert page == {1: 1, 2: 2, 3: 5, 4: 12, 5: 30}


class TestHeisenbergBarCoh:
    def test_all_one(self):
        for n in range(1, 11):
            assert HEISENBERG_BAR_COH_E2_LEADING[n] == 1

    def test_e2_page(self):
        page = e2_page_heisenberg(5)
        assert all(d == 1 for d in page.values())


class TestSl2BarCoh:
    def test_first_dims(self):
        """Riordan R(n+3): R(4)=3, R(5)=6, R(6)=15."""
        assert SL2_BAR_COH[1] == 3
        assert SL2_BAR_COH[2] == 6
        assert SL2_BAR_COH[3] == 15


class TestCollapsePages:
    def test_kac_moody_E1(self):
        for alg in ["sl2", "sl3", "E8"]:
            data = spectral_sequence_collapse(alg)
            assert data["collapse_page"] == 1, f"{alg} should collapse at E_1"

    def test_heisenberg_E1(self):
        assert spectral_sequence_collapse("Heisenberg")["collapse_page"] == 1

    def test_virasoro_E2(self):
        assert spectral_sequence_collapse("Virasoro")["collapse_page"] == 2

    def test_betagamma_E2(self):
        assert spectral_sequence_collapse("beta_gamma")["collapse_page"] == 2

    def test_bc_E2(self):
        assert spectral_sequence_collapse("bc")["collapse_page"] == 2


class TestCatalan:
    def test_values(self):
        assert catalan(1) == 1
        assert catalan(2) == 2
        assert catalan(3) == 5
        assert catalan(4) == 14
        assert catalan(5) == 42


class TestAssociahedron:
    def test_K2(self):
        assert associahedron_f_vector(2) == [1]

    def test_K3(self):
        assert associahedron_f_vector(3) == [2, 1]

    def test_K4_pentagon(self):
        """K_4 = pentagon: 5 vertices, 5 edges, 1 face."""
        assert associahedron_f_vector(4) == [5, 5, 1]

    def test_K5(self):
        """K_5 = 3d associahedron: 14 vertices, 21 edges, 9 faces, 1 cell."""
        assert associahedron_f_vector(5) == [14, 21, 9, 1]

    def test_K6(self):
        """K_6 = 4d associahedron: 42 vertices, ..., 1 top cell."""
        fv = associahedron_f_vector(6)
        assert fv == [42, 84, 56, 14, 1]

    def test_vertices_are_catalan(self):
        """Number of vertices of K_n = Catalan C_{n-1}."""
        from math import comb
        for n in range(2, 9):
            fv = associahedron_f_vector(n)
            catalan = comb(2 * (n - 1), n - 1) // n
            assert fv[0] == catalan, f"K_{n} vertices: {fv[0]} != C_{n-1} = {catalan}"

    def test_top_cell_is_one(self):
        """Top-dimensional cell of K_n is always 1."""
        for n in range(2, 9):
            fv = associahedron_f_vector(n)
            assert fv[-1] == 1

    def test_invalid_n_raises(self):
        """K_n requires n >= 2."""
        with pytest.raises(ValueError):
            associahedron_f_vector(1)
        with pytest.raises(ValueError):
            associahedron_f_vector(0)
        with pytest.raises(ValueError):
            associahedron_f_vector(-1)


class TestKoszulProperty:
    def test_consistent(self):
        # Trivial check: bar coh matches itself
        assert check_koszul_property(VIRASORO_BAR_COH, VIRASORO_BAR_COH)

    def test_inconsistent(self):
        wrong = {1: 1, 2: 3}  # dim H^2 should be 2
        assert not check_koszul_property(VIRASORO_BAR_COH, wrong)


class TestSelfConsistency:
    def test_all_pass(self):
        for name, ok in verify_spectral_sequences().items():
            assert ok, f"Failed: {name}"


# ---------------------------------------------------------------------------
# Tests for the CE cohomology engine and PBW E_1 computation
# ---------------------------------------------------------------------------

class TestCECohomology:
    """Verify CE cohomology computation against known results."""

    def test_sl2_ce_cohomology(self):
        """H*(sl_2, k) = Lambda(x_3): dims [1, 0, 0, 1]."""
        from compute.lib.spectral_sequence import ce_cohomology_dims
        from compute.lib.chiral_bar import sl2_structure_constants
        dims = ce_cohomology_dims(3, sl2_structure_constants())
        assert dims == [1, 0, 0, 1]

    def test_sl2_euler_char_zero(self):
        """Euler characteristic of CE(sl_2) = 0 (odd-dim simple Lie algebra)."""
        from compute.lib.spectral_sequence import ce_cohomology_dims
        from compute.lib.chiral_bar import sl2_structure_constants
        dims = ce_cohomology_dims(3, sl2_structure_constants())
        chi = sum((-1)**i * d for i, d in enumerate(dims))
        assert chi == 0

    def test_abelian_ce_is_exterior(self):
        """CE cohomology of abelian g = Lambda(g*): dims = binomial."""
        from compute.lib.spectral_sequence import ce_cohomology_dims
        from math import comb
        for d in [1, 2, 3, 4]:
            dims = ce_cohomology_dims(d, {})  # empty bracket = abelian
            expected = [comb(d, k) for k in range(d + 1)]
            assert dims == expected, f"Abelian dim {d}: {dims} != {expected}"

    def test_ce_differential_d_squared_zero(self):
        """d^2 = 0 for sl_2 CE complex."""
        from sympy import zeros
        from compute.lib.spectral_sequence import ce_differential_matrix
        from compute.lib.chiral_bar import sl2_structure_constants
        sc = sl2_structure_constants()
        d0 = ce_differential_matrix(3, sc, 0)
        d1 = ce_differential_matrix(3, sc, 1)
        d2 = ce_differential_matrix(3, sc, 2)
        assert (d1 * d0) == zeros(3, 1)
        assert (d2 * d1) == zeros(1, 3)


class TestSymModuleDims:
    """Verify coefficient module dimensions for PBW computation."""

    def test_weight_0(self):
        """Weight 0 part of Sym is always 1-dimensional (the scalars)."""
        from compute.lib.spectral_sequence import _sym_module_dim
        for d in [1, 2, 3, 8]:
            assert _sym_module_dim(d, 0) == 1

    def test_weight_1_is_dim_g(self):
        """Weight 1: only mode -1 generators, one of each -> dim g."""
        from compute.lib.spectral_sequence import _sym_module_dim
        for d in [1, 2, 3, 8]:
            assert _sym_module_dim(d, 1) == d

    def test_heisenberg_weight_is_partition(self):
        """For dim g = 1, Sym module dims = partition numbers p(h)."""
        from compute.lib.spectral_sequence import _sym_module_dim
        from compute.lib.utils import partition_number
        for h in range(0, 10):
            assert _sym_module_dim(1, h) == partition_number(h), \
                f"weight {h}: {_sym_module_dim(1, h)} != p({h})"

    def test_sl2_weight_2(self):
        """Weight 2 for sl_2 (d=3): 3 at mode -2 + C(3+1,2)=6 at mode -1,-1 = 9."""
        from compute.lib.spectral_sequence import _sym_module_dim
        # Partitions of 2: (2) and (1,1)
        # (2): 3 generators at mode -2 -> C(3,1) = 3
        # (1,1): Sym^2 of 3 generators at mode -1 -> C(3+1,2) = 6
        assert _sym_module_dim(3, 2) == 9

    def test_generating_function_d1(self):
        """For d=1: prod_{m>=1} 1/(1-q^m) gives partition numbers."""
        from compute.lib.spectral_sequence import _sym_module_dim
        # p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7
        expected = [1, 1, 2, 3, 5, 7]
        for h, val in enumerate(expected):
            assert _sym_module_dim(1, h) == val


class TestAdjointInvariants:
    """Test adjoint representation and invariant dimension computations."""

    def test_sl2_adjoint_matrices(self):
        """ad(h) = diag(2, 0, -2) for sl_2 in basis (e, h, f)."""
        from compute.lib.spectral_sequence import adjoint_rep_matrices
        from compute.lib.chiral_bar import sl2_structure_constants
        mats = adjoint_rep_matrices(3, sl2_structure_constants())
        # ad(e_1) = ad(h) should be diag(2, 0, -2)
        ad_h = mats[1]
        assert ad_h[0, 0] == 2
        assert ad_h[1, 1] == 0
        assert ad_h[2, 2] == -2

    def test_sl2_ad_e_is_nilpotent(self):
        """ad(e) is strictly upper triangular (nilpotent)."""
        from compute.lib.spectral_sequence import adjoint_rep_matrices
        from compute.lib.chiral_bar import sl2_structure_constants
        mats = adjoint_rep_matrices(3, sl2_structure_constants())
        ad_e = mats[0]
        assert (ad_e ** 3) == ad_e * 0  # ad(e)^3 = 0

    def test_weight_0_invariant(self):
        """Weight 0: always 1 (scalars)."""
        from compute.lib.spectral_sequence import adjoint_invariant_dim
        from compute.lib.chiral_bar import sl2_structure_constants
        assert adjoint_invariant_dim(3, sl2_structure_constants(), 0) == 1

    def test_weight_1_no_invariant(self):
        """Weight 1 = adjoint: no invariants for simple g."""
        from compute.lib.spectral_sequence import adjoint_invariant_dim
        from compute.lib.chiral_bar import sl2_structure_constants
        assert adjoint_invariant_dim(3, sl2_structure_constants(), 1) == 0

    def test_weight_2_casimir(self):
        """Weight 2: one invariant (Casimir element)."""
        from compute.lib.spectral_sequence import adjoint_invariant_dim
        from compute.lib.chiral_bar import sl2_structure_constants
        assert adjoint_invariant_dim(3, sl2_structure_constants(), 2) == 1

    def test_weight_3(self):
        """Weight 3: one invariant (from ad tensor ad cross-mode)."""
        from compute.lib.spectral_sequence import adjoint_invariant_dim
        from compute.lib.chiral_bar import sl2_structure_constants
        assert adjoint_invariant_dim(3, sl2_structure_constants(), 3) == 1

    def test_weight_4(self):
        """Weight 4: three invariants."""
        from compute.lib.spectral_sequence import adjoint_invariant_dim
        from compute.lib.chiral_bar import sl2_structure_constants
        assert adjoint_invariant_dim(3, sl2_structure_constants(), 4) == 3

    def test_abelian_all_invariant(self):
        """Abelian g: everything is invariant, so dim = _sym_module_dim."""
        from compute.lib.spectral_sequence import adjoint_invariant_dim, _sym_module_dim
        for h in range(5):
            assert adjoint_invariant_dim(1, {}, h) == _sym_module_dim(1, h)

    def test_jacobi_identity(self):
        """ad([x,y]) = [ad(x), ad(y)] for sl_2."""
        from compute.lib.spectral_sequence import adjoint_rep_matrices
        from compute.lib.chiral_bar import sl2_structure_constants
        sc = sl2_structure_constants()
        mats = adjoint_rep_matrices(3, sc)
        # [e, f] = h => ad(h) = [ad(e), ad(f)]
        commutator = mats[0] * mats[2] - mats[2] * mats[0]
        # sc has (0,2) -> {1: 1}, so [e_0, e_2] = e_1 (h)
        # But we need to check which convention: is it (e,h,f) or (e,f,h)?
        bracket_02 = sc.get((0, 2), {})
        for j, coeff in bracket_02.items():
            assert commutator == coeff * mats[j]


class TestCEWithCoefficients:
    """Test CE cohomology with nontrivial coefficient modules."""

    def test_d_squared_zero_sl2_adjoint(self):
        """d² = 0 for CE(sl₂, ad) at all degrees."""
        from sympy import zeros
        from compute.lib.spectral_sequence import (
            ce_differential_with_coefficients,
            adjoint_rep_matrices,
        )
        from compute.lib.chiral_bar import sl2_structure_constants
        sc = sl2_structure_constants()
        rho = adjoint_rep_matrices(3, sc)
        for p in range(3):
            dp = ce_differential_with_coefficients(3, sc, 3, rho, p)
            dp1 = ce_differential_with_coefficients(3, sc, 3, rho, p + 1)
            assert (dp1 * dp) == zeros(dp1.rows, dp.cols), f"d² ≠ 0 at degree {p}"

    def test_sl2_adjoint_cohomology_vanishes(self):
        """H*(sl₂, ad) = 0 (Whitehead + center = 0 + Poincaré duality)."""
        from compute.lib.spectral_sequence import (
            ce_cohomology_with_coefficients_dims,
            adjoint_rep_matrices,
        )
        from compute.lib.chiral_bar import sl2_structure_constants
        sc = sl2_structure_constants()
        rho = adjoint_rep_matrices(3, sc)
        dims = ce_cohomology_with_coefficients_dims(3, sc, 3, rho)
        assert dims == [0, 0, 0, 0]

    def test_trivial_module_matches_ce(self):
        """CE(g, k) with trivial 1-dim module = CE(g, k)."""
        from sympy import zeros
        from compute.lib.spectral_sequence import (
            ce_cohomology_with_coefficients_dims,
            ce_cohomology_dims,
        )
        from compute.lib.chiral_bar import sl2_structure_constants
        sc = sl2_structure_constants()
        triv = [zeros(1, 1) for _ in range(3)]
        dims_coeff = ce_cohomology_with_coefficients_dims(3, sc, 1, triv)
        dims_plain = ce_cohomology_dims(3, sc)
        assert dims_coeff == dims_plain

    def test_abelian_nontrivial_module(self):
        """CE(abelian, M) with nontrivial M can have interesting cohomology."""
        from sympy import Matrix, zeros
        from compute.lib.spectral_sequence import (
            ce_differential_with_coefficients,
        )
        # 1-dim abelian, 2-dim module with nontrivial action
        rho = [Matrix([[0, 1], [0, 0]])]
        d0 = ce_differential_with_coefficients(1, {}, 2, rho, 0)
        d1 = ce_differential_with_coefficients(1, {}, 2, rho, 1)
        # d² = 0 (abelian, nilpotent action)
        assert (d1 * d0) == zeros(d1.rows, d0.cols)


class TestPBWE1Page:
    """Test PBW spectral sequence E_1 page computation."""

    def test_abelian_e1_all_survive(self):
        """For abelian g (Heisenberg), all CE degrees survive."""
        from compute.lib.spectral_sequence import pbw_e1_page
        page = pbw_e1_page(1, {}, max_weight=3)
        # CE(abelian dim 1) = [1, 1], all entries nonzero
        assert page[(0, 0)] == 1  # H^0 at weight 0
        assert page[(1, 0)] == 1  # H^1 at weight 0
        assert page[(0, 1)] == 1  # H^0 at weight 1
        assert page[(1, 1)] == 1  # H^1 at weight 1

    def test_sl2_e1_middle_vanish(self):
        """For sl_2, CE degrees 1 and 2 vanish (Whitehead)."""
        from compute.lib.spectral_sequence import pbw_e1_page
        from compute.lib.chiral_bar import sl2_structure_constants
        page = pbw_e1_page(3, sl2_structure_constants(), max_weight=2)
        # CE dims for sl_2: [1, 0, 0, 1]
        for h in range(3):
            assert page[(1, h)] == 0, f"E_1^{{1,{h}}} should be 0"
            assert page[(2, h)] == 0, f"E_1^{{2,{h}}} should be 0"
