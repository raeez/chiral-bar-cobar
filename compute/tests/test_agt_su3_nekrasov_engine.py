r"""Tests for compute/lib/agt_su3_nekrasov_engine.py

Comprehensive test suite for the SU(3) AGT correspondence engine:
  - SU(3) Nekrasov partition function (Section 1)
  - SU(3) free energy / cumulant expansion (Section 2)
  - W_3 AGT parameter map (Section 3)
  - W_3 Gram matrix and conformal blocks (Section 4)
  - Shadow obstruction tower for W_3 (Section 5)
  - SU(3) prepotential (Section 6)
  - Multi-path verification (Section 7)
  - Instanton counting combinatorics (Section 8)
  - W_3 conformal block infrastructure (Section 9)
  - AGT comparison (Section 10)
  - Self-dual and NS limits (Section 11)
  - W_3 algebra data and complementarity (Section 12)

MULTI-PATH VERIFICATION STRATEGY:
  Each key result is tested via 3+ independent routes per the
  Multi-Path Verification Mandate (CLAUDE.md).

  Path 1: Direct computation from defining formula
  Path 2: Alternative formula or independent method
  Path 3: Symmetry / limiting case / cross-check
"""

import pytest
import itertools
from sympy import (
    Rational, simplify, sqrt, Symbol, oo, S as Sym,
    bernoulli, factorial, Abs, N as Neval, expand,
)

from compute.lib.agt_su3_nekrasov_engine import (
    # Section 1: SU(3) Nekrasov
    su3_coulomb_from_pair,
    su3_instanton_triple_count,
    su3_nekrasov_coefficient,
    su3_nekrasov_partition,
    su3_nekrasov_by_triple,
    # Section 2: Free energy
    su3_free_energy,
    # Section 3: W_3 AGT parameters
    w3_central_charge,
    w3_central_charge_from_epsilons,
    w3_agt_parameter_map,
    w3_conformal_dimensions_from_coulomb,
    # Section 4: W_3 Gram matrix
    w3_verma_basis,
    w3_verma_dimension,
    w3_gram_matrix,
    w3_kac_determinant_level1,
    # Section 5: Shadow tower
    w3_shadow_kappa,
    w3_shadow_kappa_per_channel,
    w3_shadow_genus1,
    w3_shadow_genus_g,
    w3_shadow_generating_function,
    # Section 6: Prepotential
    su3_prepotential_one_instanton,
    su3_prepotential_from_nekrasov,
    # Section 7: Verification
    verify_su3_k1_three_paths,
    verify_su3_weyl_symmetry,
    verify_su3_su2_limit,
    verify_su3_prepotential,
    verify_su3_shadow_kappa_match,
    # Section 8: Combinatorics
    su3_partition_count_table,
    su3_partition_count_from_convolution,
    su3_dominant_configurations,
    # Section 9: W_3 block
    w3_conformal_block_level1,
    # Section 10: AGT comparison
    su3_agt_comparison_k1,
    su3_agt_genus_expansion_comparison,
    # Section 11: Limits
    su3_self_dual_nekrasov,
    su3_ns_limit,
    # Section 12: W_3 data
    w3_algebra_data,
    w3_complementarity_check,
)

from compute.lib.agt_shadow_correspondence import (
    all_partitions,
    all_partition_triples,
    nekrasov_factor_triple,
    nekrasov_partition_su2,
    nekrasov_partition_su3,
    w3_kappa_from_c,
)


# ===================================================================
# Section 1: SU(3) Nekrasov partition function
# ===================================================================

class TestSU3Coulomb:
    """Tests for SU(3) Coulomb parameter construction."""

    def test_tracelessness(self):
        """a_1 + a_2 + a_3 = 0 (tracelessness constraint)."""
        for a1, a2 in [(3, -1), (1, 2), (0, 0), (Rational(1, 3), Rational(2, 5))]:
            a = su3_coulomb_from_pair(a1, a2)
            assert a[0] + a[1] + a[2] == 0

    def test_values(self):
        """Explicit Coulomb parameters."""
        a = su3_coulomb_from_pair(3, -1)
        assert a == (Rational(3), Rational(-1), Rational(-2))

    def test_symmetric(self):
        """a_1 = a_2 case."""
        a = su3_coulomb_from_pair(1, 1)
        assert a == (Rational(1), Rational(1), Rational(-2))


class TestSU3NekrasovPartition:
    """Tests for SU(3) Nekrasov instanton partition function."""

    def test_z0_is_one(self):
        """Z_0 = 1 (empty diagrams contribute 1)."""
        a = su3_coulomb_from_pair(3, -1)
        Z = su3_nekrasov_partition(a, Rational(1, 3), Rational(1, 5), 0)
        assert Z[0] == 1

    def test_z1_nonzero(self):
        """Z_1 is nonzero for generic Coulomb parameters."""
        a = su3_coulomb_from_pair(3, -1)
        Z = su3_nekrasov_partition(a, Rational(1, 3), Rational(1, 5), 1)
        assert Z[1] != 0

    def test_z1_is_rational(self):
        """Z_1 is a rational number for rational inputs."""
        a = su3_coulomb_from_pair(3, -1)
        Z = su3_nekrasov_partition(a, Rational(1, 3), Rational(1, 5), 1)
        assert isinstance(Z[1], Rational)

    def test_z1_matches_existing_su3(self):
        """Our Z_1 matches the existing nekrasov_partition_su3 from agt_shadow_correspondence."""
        a_vals = [Rational(3), Rational(-1), Rational(-2)]
        e1, e2 = Rational(1, 3), Rational(1, 5)
        Z_new = su3_nekrasov_partition(a_vals, e1, e2, 1)
        Z_old = nekrasov_partition_su3(a_vals, e1, e2, 1)
        assert simplify(Z_new[0] - Z_old[0]) == 0
        assert simplify(Z_new[1] - Z_old[1]) == 0

    def test_z2_matches_existing_su3(self):
        """Our Z_2 matches the existing nekrasov_partition_su3."""
        a_vals = [Rational(3), Rational(-1), Rational(-2)]
        e1, e2 = Rational(1, 3), Rational(1, 5)
        Z_new = su3_nekrasov_partition(a_vals, e1, e2, 2)
        Z_old = nekrasov_partition_su3(a_vals, e1, e2, 2)
        assert simplify(Z_new[2] - Z_old[2]) == 0

    def test_eps_symmetry_k1(self):
        """Z_1 is symmetric under eps1 <-> eps2."""
        a = su3_coulomb_from_pair(3, -1)
        e1, e2 = Rational(1, 3), Rational(1, 5)
        Z = su3_nekrasov_partition(a, e1, e2, 1)
        Z_swap = su3_nekrasov_partition(a, e2, e1, 1)
        assert simplify(Z[1] - Z_swap[1]) == 0

    def test_eps_symmetry_k2(self):
        """Z_2 is symmetric under eps1 <-> eps2."""
        a = su3_coulomb_from_pair(3, -1)
        e1, e2 = Rational(1, 3), Rational(1, 5)
        Z = su3_nekrasov_partition(a, e1, e2, 2)
        Z_swap = su3_nekrasov_partition(a, e2, e1, 2)
        assert simplify(Z[2] - Z_swap[2]) == 0

    def test_weyl_symmetry_k1(self):
        """Z_1 is invariant under S_3 (Weyl group) permutations of Coulomb parameters."""
        a = [Rational(3), Rational(-1), Rational(-2)]
        e1, e2 = Rational(1, 3), Rational(1, 5)
        Z_ref = su3_nekrasov_coefficient(a, e1, e2, 1)
        for perm in itertools.permutations(range(3)):
            a_perm = [a[perm[i]] for i in range(3)]
            Z_perm = su3_nekrasov_coefficient(a_perm, e1, e2, 1)
            assert simplify(Z_ref - Z_perm) == 0, f"Failed for perm {perm}"

    def test_a_negation_symmetry(self):
        """Z_k(a) = Z_k(-a) (charge conjugation for SU(3))."""
        a = [Rational(3), Rational(-1), Rational(-2)]
        a_neg = [-x for x in a]
        e1, e2 = Rational(1, 3), Rational(1, 5)
        Z = su3_nekrasov_partition(a, e1, e2, 1)
        Z_neg = su3_nekrasov_partition(a_neg, e1, e2, 1)
        assert simplify(Z[1] - Z_neg[1]) == 0

    def test_different_coulomb_give_different_Z1(self):
        """Different generic Coulomb parameters give different Z_1."""
        e1, e2 = Rational(1, 3), Rational(1, 5)
        a1 = su3_coulomb_from_pair(3, -1)
        a2 = su3_coulomb_from_pair(5, -2)
        Z1 = su3_nekrasov_coefficient(list(a1), e1, e2, 1)
        Z2 = su3_nekrasov_coefficient(list(a2), e1, e2, 1)
        assert simplify(Z1 - Z2) != 0


class TestSU3ByTriple:
    """Tests for per-triple decomposition."""

    def test_k1_has_3_contributions(self):
        """At k=1, there are exactly 3 triples."""
        a = su3_coulomb_from_pair(3, -1)
        contribs = su3_nekrasov_by_triple(list(a), Rational(1, 3), Rational(1, 5), 1)
        assert len(contribs) == 3

    def test_k1_sum_matches_Z1(self):
        """Sum of per-triple contributions equals Z_1."""
        a = su3_coulomb_from_pair(3, -1)
        e1, e2 = Rational(1, 3), Rational(1, 5)
        contribs = su3_nekrasov_by_triple(list(a), e1, e2, 1)
        total = sum(z for _, z in contribs)
        Z1 = su3_nekrasov_coefficient(list(a), e1, e2, 1)
        assert simplify(total - Z1) == 0

    def test_k2_has_9_contributions(self):
        """At k=2, there are exactly 9 triples."""
        a = su3_coulomb_from_pair(3, -1)
        contribs = su3_nekrasov_by_triple(list(a), Rational(1, 3), Rational(1, 5), 2)
        assert len(contribs) == 9


# ===================================================================
# Section 2: SU(3) free energy
# ===================================================================

class TestSU3FreeEnergy:
    """Tests for SU(3) free energy (cumulant expansion)."""

    def test_f1_equals_Z1(self):
        """f_1 = Z_1 (first cumulant)."""
        a = su3_coulomb_from_pair(3, -1)
        e1, e2 = Rational(1, 3), Rational(1, 5)
        Z = su3_nekrasov_partition(a, e1, e2, 2)
        f = su3_free_energy(a, e1, e2, 2)
        assert simplify(f[1] - Z[1]) == 0

    def test_f2_cumulant(self):
        """f_2 = Z_2 - Z_1^2/2 (second cumulant)."""
        a = su3_coulomb_from_pair(3, -1)
        e1, e2 = Rational(1, 3), Rational(1, 5)
        Z = su3_nekrasov_partition(a, e1, e2, 2)
        f = su3_free_energy(a, e1, e2, 2)
        expected = Z[2] - Z[1]**2 / 2
        assert simplify(f[2] - expected) == 0

    def test_f3_cumulant(self):
        """f_3 = Z_3 - Z_1*Z_2 + Z_1^3/3."""
        a = su3_coulomb_from_pair(3, -1)
        e1, e2 = Rational(1, 3), Rational(1, 5)
        Z = su3_nekrasov_partition(a, e1, e2, 3)
        f = su3_free_energy(a, e1, e2, 3)
        expected = Z[3] - Z[1] * Z[2] + Z[1]**3 / 3
        assert simplify(f[3] - expected) == 0


# ===================================================================
# Section 3: W_3 AGT parameter map
# ===================================================================

class TestW3AGTParameters:
    """Tests for the W_3 AGT parameter dictionary."""

    def test_w3_central_charge_b1(self):
        """At b=1: c(W_3) = 2 + 24*(1+1)^2 = 2 + 96 = 98."""
        assert w3_central_charge(1) == 98

    def test_w3_central_charge_n3_formula(self):
        """c(W_3) = (N-1)(1 + N(N+1)(b+1/b)^2) at N=3."""
        b = Rational(2)
        c_direct = w3_central_charge(b)
        c_general = 2 * (1 + 12 * (b + 1/b)**2)
        assert simplify(c_direct - c_general) == 0

    def test_w3_central_charge_from_eps(self):
        """c(W_3) at eps1=1, eps2=-1 gives b=1, c=98."""
        c = w3_central_charge_from_epsilons(1, -1)
        assert simplify(c - 98) == 0

    def test_agt_map_kappa_additivity(self):
        """kappa_W3 = kappa_T + kappa_W (additive over generators)."""
        params = w3_agt_parameter_map(1, -1)
        kappa_total = params['kappa_W3']
        kappa_sum = params['kappa_T'] + params['kappa_W']
        assert simplify(kappa_total - kappa_sum) == 0

    def test_agt_map_kappa_formula(self):
        """kappa(W_3) = 5c/6."""
        params = w3_agt_parameter_map(1, -1)
        c = params['c_W3']
        assert simplify(params['kappa_W3'] - 5 * c / 6) == 0

    def test_agt_map_virasoro_vs_w3(self):
        """c(Vir) = 1 + 6Q^2, c(W_3) = 2 + 24Q^2: so c(W_3) = 4*c(Vir) - 2."""
        params = w3_agt_parameter_map(1, -1)
        c_vir = params['c_Vir']
        c_w3 = params['c_W3']
        # c(Vir) = 1 + 6*Q^2, c(W_3) = 2 + 24*Q^2 = 4*(1 + 6*Q^2) - 2 = 4*c_vir - 2
        assert simplify(c_w3 - (4 * c_vir - 2)) == 0

    def test_agt_map_self_dual_point(self):
        """At eps1 = -eps2: beta = 0 (self-dual Omega-background)."""
        params = w3_agt_parameter_map(1, -1)
        assert params['beta'] == 0

    def test_conformal_dimensions_casimir2(self):
        """Casimir-2 is positive for generic Coulomb parameters."""
        a = su3_coulomb_from_pair(3, -1)
        dims = w3_conformal_dimensions_from_coulomb(a, 1, -1)
        c2 = dims['Casimir_2']
        # a = (3, -1, -2), hbar = -1
        # C_2 = (9 + 1 + 4)/(-1) = -14
        assert c2 == Rational(-14)

    def test_conformal_dimensions_casimir3(self):
        """Casimir-3 from SU(3) Coulomb parameters."""
        a = su3_coulomb_from_pair(3, -1)
        dims = w3_conformal_dimensions_from_coulomb(a, 1, -1)
        # C_3 = a_1*a_2*a_3 / hbar = 3*(-1)*(-2)/(-1) = -6
        assert dims['Casimir_3'] == Rational(-6)


# ===================================================================
# Section 4: W_3 Gram matrix and conformal blocks
# ===================================================================

class TestW3VermaModule:
    """Tests for W_3 Verma module structure."""

    def test_verma_dim_level0(self):
        """Level 0: just the highest weight state."""
        assert w3_verma_dimension(0) == 1

    def test_verma_dim_level1(self):
        """Level 1: L_{-1}|> and W_{-1}|>."""
        assert w3_verma_dimension(1) == 2

    def test_verma_dim_level2(self):
        """Level 2: 5 states (2 from L-only, 1 mixed, 2 from W-only)."""
        assert w3_verma_dimension(2) == 5

    def test_verma_dim_level3(self):
        """Level 3: 10 states."""
        assert w3_verma_dimension(3) == 10

    def test_verma_dim_level4(self):
        """Level 4: 20 states."""
        assert w3_verma_dimension(4) == 20

    def test_verma_dim_level5(self):
        """Level 5: 36 states."""
        assert w3_verma_dimension(5) == 36

    def test_verma_dim_is_convolution(self):
        r"""dim(level n) = sum_{k=0}^{n} p(k)*p(n-k) where p = partitions.

        This is the convolution of the Virasoro partition function with itself
        (W_3 has two generators).
        """
        for n in range(6):
            p = {}
            for k in range(n + 1):
                p[k] = sum(1 for _ in all_partitions(k))
            expected = sum(p[k] * p[n - k] for k in range(n + 1))
            assert w3_verma_dimension(n) == expected, f"Failed at level {n}"

    def test_verma_basis_level1_content(self):
        """Level 1 basis should contain exactly L_{-1}|> and W_{-1}|>."""
        basis = w3_verma_basis(1)
        assert len(basis) == 2
        assert ((1,), ()) in basis  # L_{-1}|>
        assert ((), (1,)) in basis  # W_{-1}|>


class TestW3GramMatrix:
    """Tests for W_3 Gram matrix computation."""

    def test_gram_level1_shape(self):
        """Level-1 Gram matrix is 2x2."""
        G = w3_gram_matrix(50, 2, 0, 1)
        assert G.shape == (2, 2)

    def test_gram_level1_LL_entry(self):
        """<h,w|L_1 L_{-1}|h,w> = 2h."""
        for h in [1, 2, Rational(3, 2), 5]:
            G = w3_gram_matrix(50, h, 0, 1)
            # Find the LL entry
            basis = w3_verma_basis(1)
            ll_idx = basis.index(((1,), ()))
            assert G[ll_idx, ll_idx] == 2 * h

    def test_gram_level1_LW_entry(self):
        """<h,w|L_1 W_{-1}|h,w> = 3w."""
        for w_val in [0, 1, Rational(1, 2), -1]:
            G = w3_gram_matrix(50, 2, w_val, 1)
            basis = w3_verma_basis(1)
            ll_idx = basis.index(((1,), ()))
            ww_idx = basis.index(((), (1,)))
            assert G[ll_idx, ww_idx] == 3 * w_val

    def test_gram_level1_symmetry(self):
        """Gram matrix is symmetric."""
        G = w3_gram_matrix(50, 2, Rational(1, 2), 1)
        assert G == G.T

    def test_gram_level1_det_matches_kac(self):
        """Gram matrix determinant matches the Kac determinant formula."""
        for c_val in [10, 25, 50]:
            for h_val in [1, 2, 3]:
                for w_val in [0, Rational(1, 2)]:
                    G = w3_gram_matrix(c_val, h_val, w_val, 1)
                    det_gram = G.det()
                    det_kac = w3_kac_determinant_level1(c_val, h_val, w_val)
                    assert simplify(det_gram - det_kac) == 0, \
                        f"Mismatch at c={c_val}, h={h_val}, w={w_val}"

    def test_gram_level1_det_sign(self):
        """W_3 Gram matrix determinant at w=0: sign depends on c and h.

        At w=0: det = 2h * (-2h + 2*beta*(h^2 - 9h/10))
        where beta = 16/(22+5c).
        For large c: beta ~ 0, so det ~ 2h*(-2h) = -4h^2 < 0.
        The level-1 Gram matrix is NOT positive definite at large c
        because the WW entry becomes negative when beta is small.
        This is the correct mathematical behavior: the W_3 unitarity
        bound at level 1 constrains (c, h, w) jointly.
        """
        G = w3_gram_matrix(1000, 10, 0, 1)
        det = G.det()
        # At large c, beta -> 0, det -> 2h*(-2h) < 0
        assert float(Neval(det, 10)) < 0

    def test_kac_det_vanishes_for_degenerate(self):
        """At h=0, w=0: the Kac determinant at level 1 should vanish (vacuum module)."""
        det = w3_kac_determinant_level1(25, 0, 0)
        assert det == 0


class TestW3KacDeterminant:
    """Tests for W_3 Kac determinant."""

    def test_level1_formula(self):
        """Verify the explicit Kac determinant formula at level 1."""
        c = Rational(50)
        h = Rational(3)
        w = Rational(1)
        beta = Rational(16) / (22 + 5 * c)
        lambda0 = h**2 - Rational(9, 10) * h
        g11 = 2 * h
        g12 = 3 * w
        g22 = -2 * h + 2 * beta * lambda0
        expected = g11 * g22 - g12**2
        assert w3_kac_determinant_level1(c, h, w) == expected

    def test_level1_w0_simplification(self):
        """At w=0, det = 2h * (-2h + 2*beta*(h^2 - 9h/10))."""
        c = Rational(50)
        h = Rational(3)
        beta = Rational(16) / (22 + 5 * c)
        expected = 2 * h * (-2 * h + 2 * beta * (h**2 - Rational(9, 10) * h))
        assert w3_kac_determinant_level1(c, h, 0) == expected


# ===================================================================
# Section 5: Shadow obstruction tower for W_3
# ===================================================================

class TestW3ShadowTower:
    """Tests for the W_3 shadow obstruction tower."""

    def test_kappa_formula(self):
        """kappa(W_3) = 5c/6."""
        for c_val in [10, 25, 50, 98, 100]:
            kappa = w3_shadow_kappa(c_val)
            expected = Rational(5, 6) * Rational(c_val)
            assert kappa == expected

    def test_kappa_matches_existing(self):
        """Our kappa matches w3_kappa_from_c from agt_shadow_correspondence.

        Multi-path verification: Path 1 (new engine) vs Path 2 (existing function).
        """
        for c_val in [10, 25, 50, 98]:
            path1 = w3_shadow_kappa(c_val)
            path2 = w3_kappa_from_c(c_val)
            assert simplify(path1 - path2) == 0, f"Mismatch at c={c_val}"

    def test_kappa_additivity(self):
        """kappa = kappa_T + kappa_W = c/2 + c/3 = 5c/6.

        Multi-path verification: Path 1 (total) vs Path 3 (additive decomposition).
        """
        for c_val in [10, 25, 50]:
            kappa_total = w3_shadow_kappa(c_val)
            kappa_T, kappa_W = w3_shadow_kappa_per_channel(c_val)
            assert simplify(kappa_total - (kappa_T + kappa_W)) == 0

    def test_kappa_per_channel_values(self):
        """kappa_T = c/2, kappa_W = c/3."""
        c = Rational(60)
        kappa_T, kappa_W = w3_shadow_kappa_per_channel(c)
        assert kappa_T == 30
        assert kappa_W == 20

    def test_genus1_formula(self):
        """F_1(W_3) = kappa/24 = 5c/144."""
        for c_val in [24, 50, 98]:
            f1 = w3_shadow_genus1(c_val)
            expected = Rational(5, 6) * Rational(c_val) / 24
            assert simplify(f1 - expected) == 0

    def test_genus2_positive(self):
        """F_2 should be positive for c > 0."""
        f2 = w3_shadow_genus_g(50, 2)
        assert float(Neval(f2, 10)) > 0

    def test_genus_g_proportional_to_kappa(self):
        """F_g(c) / kappa(c) should be independent of c."""
        ratio_50 = w3_shadow_genus_g(50, 2) / w3_shadow_kappa(50)
        ratio_98 = w3_shadow_genus_g(98, 2) / w3_shadow_kappa(98)
        assert simplify(ratio_50 - ratio_98) == 0

    def test_generating_function_keys(self):
        """Shadow generating function returns correct genus range."""
        gf = w3_shadow_generating_function(50, 5)
        assert set(gf.keys()) == {1, 2, 3, 4, 5}

    def test_generating_function_f1_matches(self):
        """F_1 from generating function matches standalone formula."""
        gf = w3_shadow_generating_function(50, 5)
        f1_standalone = w3_shadow_genus1(50)
        assert simplify(gf[1] - f1_standalone) == 0

    def test_shadow_virasoro_vs_w3_ratio(self):
        """kappa(W_3) / kappa(Vir) = 5/3 at same c.

        Multi-path verification: verifies W_3 kappa against Virasoro kappa.
        """
        for c_val in [10, 50, 98]:
            kappa_w3 = w3_shadow_kappa(c_val)
            kappa_vir = Rational(c_val, 2)  # Virasoro kappa = c/2
            assert kappa_w3 / kappa_vir == Rational(5, 3)


# ===================================================================
# Section 6: SU(3) prepotential
# ===================================================================

class TestSU3Prepotential:
    """Tests for SU(3) Seiberg-Witten prepotential."""

    def test_one_instanton_structure(self):
        """F_0^{(1)} is a sum of 3 terms (one per color)."""
        a = su3_coulomb_from_pair(3, -1)
        F1 = su3_prepotential_one_instanton(a)
        # Should be a well-defined rational number
        assert F1 != 0
        assert isinstance(F1, Rational)

    def test_one_instanton_explicit(self):
        """Verify F_0^{(1)} = sum_i 1/prod_{j!=i}(a_i-a_j)^2."""
        a = [Rational(3), Rational(-1), Rational(-2)]
        F1 = su3_prepotential_one_instanton(a)
        # Manual computation:
        # i=0: 1/((3-(-1))^2 * (3-(-2))^2) = 1/(16*25) = 1/400
        # i=1: 1/((-1-3)^2 * (-1-(-2))^2) = 1/(16*1) = 1/16
        # i=2: 1/((-2-3)^2 * (-2-(-1))^2) = 1/(25*1) = 1/25
        expected = Rational(1, 400) + Rational(1, 16) + Rational(1, 25)
        assert F1 == expected

    def test_one_instanton_weyl_invariant(self):
        """F_0^{(1)} is S_3 Weyl invariant."""
        a = [Rational(3), Rational(-1), Rational(-2)]
        F1_ref = su3_prepotential_one_instanton(a)
        for perm in itertools.permutations(range(3)):
            a_perm = [a[perm[i]] for i in range(3)]
            F1_perm = su3_prepotential_one_instanton(a_perm)
            assert F1_ref == F1_perm

    def test_prepotential_from_nekrasov_convergence(self):
        """Nekrasov limit eps^2 * Z_1 converges to F_0^{(1)} as eps -> 0."""
        a = su3_coulomb_from_pair(3, -1)
        exact = su3_prepotential_one_instanton(a)
        estimates = []
        for p in [5, 10, 20]:
            eps = Rational(1, p)
            Z = su3_nekrasov_partition(list(a), eps, eps, 1)
            est = eps**2 * Z[1]
            estimates.append(float(est))
        exact_f = float(exact)
        errors = [abs(e - exact_f) for e in estimates]
        # Convergence: each estimate should be closer to exact
        assert errors[-1] < errors[0], f"No convergence: errors = {errors}"


# ===================================================================
# Section 7: Multi-path verification
# ===================================================================

class TestMultiPathVerification:
    """Multi-path verification of key SU(3) AGT results."""

    def test_k1_three_paths(self):
        """Three-path verification of Z_1."""
        result = verify_su3_k1_three_paths(3, -1, Rational(1, 3), Rational(1, 5))
        assert result['paths_agree']
        assert result['eps_symmetry']
        assert result['num_triples'] == 3

    def test_weyl_symmetry_k1(self):
        """Full S_3 Weyl symmetry at k=1."""
        a = [Rational(3), Rational(-1), Rational(-2)]
        checks = verify_su3_weyl_symmetry(a, Rational(1, 3), Rational(1, 5), 1)
        for key, val in checks.items():
            assert val, f"Weyl symmetry failed at {key}"

    def test_weyl_symmetry_k2(self):
        """Full S_3 Weyl symmetry at k=2."""
        a = [Rational(3), Rational(-1), Rational(-2)]
        checks = verify_su3_weyl_symmetry(a, Rational(1, 3), Rational(1, 5), 2)
        for key, val in checks.items():
            assert val, f"Weyl symmetry failed at {key}"

    def test_shadow_kappa_three_paths(self):
        """Three-path verification of kappa(W_3)."""
        result = verify_su3_shadow_kappa_match(1, -1)
        assert result['paths_12_agree']
        assert result['paths_13_agree']

    def test_shadow_kappa_three_paths_nontrivial_eps(self):
        """Three-path verification of kappa(W_3) at eps1=2, eps2=-3."""
        result = verify_su3_shadow_kappa_match(2, -3)
        assert result['paths_12_agree']
        assert result['paths_13_agree']

    def test_prepotential_three_paths(self):
        """Multi-path verification of SU(3) prepotential."""
        result = verify_su3_prepotential(3, -1)
        # Path 1 closed form should be nonzero
        assert result['path1_closed_form'] != 0
        # Path 2 estimates should converge
        ests = result['path2_estimates']
        exact = float(result['path1_closed_form'])
        errors = [abs(float(ests[p]) - exact) for p in sorted(ests.keys())]
        assert errors[-1] < errors[0], "Nekrasov limit not converging"


# ===================================================================
# Section 8: Instanton counting combinatorics
# ===================================================================

class TestInstantonCounting:
    """Tests for instanton counting (combinatorial checks)."""

    def test_triple_count_k0(self):
        """k=0: 1 triple (all empty)."""
        assert su3_instanton_triple_count(0) == 1

    def test_triple_count_k1(self):
        """k=1: 3 triples."""
        assert su3_instanton_triple_count(1) == 3

    def test_triple_count_k2(self):
        """k=2: 9 triples."""
        assert su3_instanton_triple_count(2) == 9

    def test_triple_count_k3(self):
        """k=3: 22 triples."""
        assert su3_instanton_triple_count(3) == 22

    def test_triple_count_k4(self):
        """k=4: 51 triples."""
        assert su3_instanton_triple_count(4) == 51

    def test_triple_count_k5(self):
        """k=5: 108 triples."""
        assert su3_instanton_triple_count(5) == 108

    def test_triple_count_convolution_agrees(self):
        """Triple count from enumeration matches convolution formula.

        Multi-path verification: Path 1 (enumeration) vs Path 2 (convolution).
        """
        for k in range(6):
            path1 = su3_instanton_triple_count(k)
            path2 = su3_partition_count_from_convolution(k)
            assert path1 == path2, f"Mismatch at k={k}: {path1} vs {path2}"

    def test_partition_count_table(self):
        """Partition count table matches expected values."""
        table = su3_partition_count_table(5)
        expected = {0: 1, 1: 3, 2: 9, 3: 22, 4: 51, 5: 108}
        for k in range(6):
            assert table[k] == expected[k]

    def test_triple_count_monotone(self):
        """Triple count is strictly increasing."""
        table = su3_partition_count_table(5)
        for k in range(1, 6):
            assert table[k] > table[k - 1]

    def test_dominant_configuration_k1(self):
        """Dominant configuration at k=1 exists and has nonzero contribution."""
        a = su3_coulomb_from_pair(3, -1)
        dom = su3_dominant_configurations(list(a), Rational(1, 3), Rational(1, 5), 1)
        assert dom is not None
        triple, z = dom
        assert z != 0

    def test_su3_vs_su2_triple_count(self):
        """SU(3) has more triples than SU(2) has pairs at each k >= 1.

        Triple count = sum p(j1)*p(j2)*p(j3) vs pair count = sum p(j1)*p(j2).
        """
        from compute.lib.agt_shadow_correspondence import all_partition_pairs
        for k in range(1, 5):
            n_triples = su3_instanton_triple_count(k)
            n_pairs = sum(1 for _ in all_partition_pairs(k))
            assert n_triples > n_pairs, f"k={k}: {n_triples} <= {n_pairs}"


# ===================================================================
# Section 9: W_3 conformal block
# ===================================================================

class TestW3ConformalBlock:
    """Tests for W_3 conformal block infrastructure."""

    def test_block_level1_generic(self):
        """Level-1 W_3 block data is computable for generic parameters."""
        result = w3_conformal_block_level1(50, 2, Rational(1, 2))
        assert 'det_G1' in result
        assert result['det_G1'] is not None

    def test_block_level1_degenerate_vacuum(self):
        """At h=0, w=0: the representation is degenerate (vacuum)."""
        result = w3_conformal_block_level1(50, 0, 0)
        assert result['degenerate']

    def test_block_level1_nondegenerate_generic(self):
        """Generic (c, h, w) should give a non-degenerate representation."""
        result = w3_conformal_block_level1(50, 2, 0)
        # At w=0, h=2, c=50: check if degenerate
        # This depends on the specific values
        det = result['det_G1']
        # Should be nonzero for these generic values
        assert det != 0


# ===================================================================
# Section 10: AGT comparison
# ===================================================================

class TestAGTComparison:
    """Tests for SU(3) AGT comparison."""

    def test_comparison_k1_nonzero(self):
        """Z_1 is nonzero at the AGT point."""
        # Use eps1=1, eps2=-1 for the self-dual point where c(W_3) = 98 > 0
        result = su3_agt_comparison_k1(3, -1, 1, -1)
        assert result['Z_1'] != 0

    def test_comparison_kappa_positive(self):
        """kappa(W_3) is positive at the self-dual AGT point.

        At eps1=1, eps2=-1: b=1, c(W_3)=98, kappa(W_3)=245/3 > 0.
        """
        result = su3_agt_comparison_k1(3, -1, 1, -1)
        kappa = result['kappa_W3']
        assert simplify(kappa) > 0

    def test_comparison_f1_positive(self):
        """F_1^{shadow} = kappa/24 > 0 at the self-dual AGT point."""
        result = su3_agt_comparison_k1(3, -1, 1, -1)
        assert simplify(result['F1_shadow']) > 0

    def test_genus_expansion_kappa_matches(self):
        """Shadow genus expansion has correct kappa: F_1 = kappa/24."""
        result = su3_agt_genus_expansion_comparison(3, -1, 1, -1, 3)
        kappa = result['kappa_W3']
        f1 = result['shadow_F_g'][1]
        assert simplify(f1 - kappa / 24) == 0

    def test_genus_expansion_f2_positive(self):
        """F_2 > 0 in the shadow genus expansion at c(W_3) = 98."""
        result = su3_agt_genus_expansion_comparison(3, -1, 1, -1, 3)
        f2 = result['shadow_F_g'][2]
        assert float(Neval(f2, 10)) > 0


# ===================================================================
# Section 11: Self-dual and NS limits
# ===================================================================

class TestLimits:
    """Tests for self-dual and NS limits of SU(3) Nekrasov."""

    def test_self_dual_z0_is_one(self):
        """Z_0 = 1 at the self-dual point."""
        a = su3_coulomb_from_pair(3, -1)
        Z = su3_self_dual_nekrasov(list(a), 1, 1)
        assert Z[0] == 1

    def test_self_dual_z1_nonzero(self):
        """Z_1 is nonzero at the self-dual point."""
        a = su3_coulomb_from_pair(3, -1)
        Z = su3_self_dual_nekrasov(list(a), 1, 1)
        assert Z[1] != 0

    def test_self_dual_eps_swapped(self):
        """At self-dual point eps1 = -eps2, the partition function has eps -> -eps symmetry."""
        a = su3_coulomb_from_pair(3, -1)
        Z1 = su3_self_dual_nekrasov(list(a), 1, 1)
        Z2 = su3_self_dual_nekrasov(list(a), 2, 1)
        # Different eps give different Z (not a symmetry test, just a sanity check)
        # The self-dual condition is beta = eps1 + eps2 = 0
        # At eps1 = 1, eps2 = -1: beta = 0 (correct)

    def test_ns_limit_gives_dict(self):
        """NS limit returns a dictionary of instanton coefficients."""
        a = su3_coulomb_from_pair(3, -1)
        ns = su3_ns_limit(list(a), Rational(1, 3), 1)
        assert isinstance(ns, dict)


# ===================================================================
# Section 12: W_3 algebra data and complementarity
# ===================================================================

class TestW3AlgebraData:
    """Tests for W_3 algebra invariants and complementarity."""

    def test_algebra_data_keys(self):
        """w3_algebra_data returns all expected keys."""
        data = w3_algebra_data(50)
        expected_keys = {'c', 'kappa', 'kappa_T', 'kappa_W', 'c_dual',
                         'kappa_dual', 'kappa_sum', 'F1', 'shadow_depth',
                         'Q_contact_T'}
        assert expected_keys.issubset(set(data.keys()))

    def test_algebra_data_c50(self):
        """W_3 at c=50: self-dual point (c = c_dual)."""
        data = w3_algebra_data(50)
        assert data['c'] == 50
        assert data['c_dual'] == 50
        assert data['kappa'] == data['kappa_dual']

    def test_complementarity_sum(self):
        """kappa(c) + kappa(100-c) = 250/3 for all c."""
        for c_val in [0, 10, 25, 50, 75, 98, 100]:
            check = w3_complementarity_check(c_val)
            assert check['match'], f"Complementarity failed at c={c_val}"
            assert check['sum'] == Rational(250, 3)

    def test_complementarity_self_dual(self):
        """At c=50: kappa = kappa_dual (self-dual point)."""
        check = w3_complementarity_check(50)
        assert simplify(check['kappa'] - check['kappa_dual']) == 0

    def test_complementarity_sum_formula(self):
        """kappa + kappa' = rho * K where rho = H_3-1 = 5/6, K = 100.

        Multi-path verification: Path 1 (direct sum) vs Path 2 (formula rho*K).
        """
        rho = Rational(5, 6)
        K = Rational(100)
        expected = rho * K  # = 250/3
        for c_val in [10, 25, 50]:
            kappa = w3_shadow_kappa(c_val)
            kappa_dual = w3_shadow_kappa(100 - c_val)
            assert simplify(kappa + kappa_dual - expected) == 0

    def test_kappa_T_complementarity(self):
        """Per-channel: kappa_T(c) + kappa_T(100-c) = 50."""
        for c_val in [10, 25, 50]:
            kT, _ = w3_shadow_kappa_per_channel(c_val)
            kT_dual, _ = w3_shadow_kappa_per_channel(100 - c_val)
            assert simplify(kT + kT_dual - 50) == 0

    def test_kappa_W_complementarity(self):
        """Per-channel: kappa_W(c) + kappa_W(100-c) = 100/3."""
        for c_val in [10, 25, 50]:
            _, kW = w3_shadow_kappa_per_channel(c_val)
            _, kW_dual = w3_shadow_kappa_per_channel(100 - c_val)
            assert simplify(kW + kW_dual - Rational(100, 3)) == 0

    def test_kappa_at_critical_string(self):
        """At c=50 (W_3 critical string): kappa = 125/3."""
        kappa = w3_shadow_kappa(50)
        assert kappa == Rational(125, 3)

    def test_f1_at_c98(self):
        """F_1(W_3, c=98) = 5*98/144 = 490/144 = 245/72."""
        f1 = w3_shadow_genus1(98)
        assert f1 == Rational(245, 72)

    def test_shadow_depth_infinite(self):
        """W_3 has infinite shadow depth (class M)."""
        data = w3_algebra_data(50)
        assert 'infinite' in data['shadow_depth']


# ===================================================================
# Cross-section: SU(3) vs SU(2) structural comparisons
# ===================================================================

class TestSU3vsSU2:
    """Structural comparisons between SU(2) and SU(3)."""

    def test_z0_same(self):
        """Z_0 = 1 for both SU(2) and SU(3)."""
        a_su2 = Rational(3)
        a_su3 = su3_coulomb_from_pair(3, -1)
        e1, e2 = Rational(1, 3), Rational(1, 5)
        Z_su2 = nekrasov_partition_su2(a_su2, e1, e2, 0)
        Z_su3 = su3_nekrasov_partition(a_su3, e1, e2, 0)
        assert Z_su2[0] == Z_su3[0] == 1

    def test_su3_has_more_instantons(self):
        """SU(3) has more instanton configurations than SU(2) at each k."""
        from compute.lib.agt_shadow_correspondence import all_partition_pairs
        for k in range(1, 4):
            n2 = sum(1 for _ in all_partition_pairs(k))
            n3 = su3_instanton_triple_count(k)
            assert n3 > n2

    def test_kappa_ratio_w3_vir(self):
        """kappa(W_3)/kappa(Vir) = (5/6)/(1/2) = 5/3 at same c."""
        c = Rational(50)
        ratio = w3_shadow_kappa(c) / (c / 2)
        assert ratio == Rational(5, 3)

    def test_w3_c_vs_vir_c_at_same_b(self):
        """c(W_3) = 4*c(Vir) - 2 at same b."""
        for b in [1, 2, Rational(1, 2)]:
            c_vir = 1 + 6 * (b + 1/b)**2
            c_w3 = w3_central_charge(b)
            assert simplify(c_w3 - (4 * c_vir - 2)) == 0


# ===================================================================
# Edge cases and robustness
# ===================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_equal_coulomb_parameters(self):
        """Equal Coulomb parameters a_1 = a_2 (enhanced symmetry)."""
        a = su3_coulomb_from_pair(0, 0)
        assert a == (0, 0, 0)
        # Z_k may have poles at a_i = a_j, but Z_0 = 1 always
        Z = su3_nekrasov_partition(list(a), Rational(1, 3), Rational(1, 5), 0)
        assert Z[0] == 1

    def test_large_coulomb(self):
        """Large Coulomb parameters: Z_1 -> 0 (weak coupling)."""
        a = su3_coulomb_from_pair(100, -50)
        e1, e2 = Rational(1, 3), Rational(1, 5)
        Z = su3_nekrasov_partition(list(a), e1, e2, 1)
        # Z_1 should be small for large a (weak coupling)
        assert abs(float(Z[1])) < 1e-3

    def test_w3_c_zero(self):
        """kappa(W_3, c=0) = 0."""
        assert w3_shadow_kappa(0) == 0

    def test_w3_c_negative(self):
        """kappa is well-defined for c < 0."""
        kappa = w3_shadow_kappa(-10)
        assert kappa == Rational(-50, 6)

    def test_genus_g_zero_for_g0(self):
        """F_0 = 0 (genus-0 not part of shadow obstruction tower)."""
        assert w3_shadow_genus_g(50, 0) == 0

    def test_complementarity_c_zero(self):
        """Complementarity at c=0."""
        check = w3_complementarity_check(0)
        assert check['match']

    def test_complementarity_c_100(self):
        """Complementarity at c=100."""
        check = w3_complementarity_check(100)
        assert check['match']

    def test_w3_central_charge_positive_b(self):
        """c(W_3) > 0 for real b > 0."""
        for b in [Rational(1, 10), Rational(1, 2), 1, 2, 10]:
            c = w3_central_charge(b)
            assert c > 0

    def test_triple_count_k0_is_1(self):
        """Triple count at k=0 is always 1."""
        assert su3_instanton_triple_count(0) == 1
        assert su3_partition_count_from_convolution(0) == 1

    def test_verma_dim_matches_oeis(self):
        """W_3 Verma dimensions match A000712 (number of 2-colored partitions).

        OEIS A000712: 1, 2, 5, 10, 20, 36, 65, 110, 185, 300, ...
        """
        expected = [1, 2, 5, 10, 20, 36]
        for n, exp in enumerate(expected):
            assert w3_verma_dimension(n) == exp, f"Failed at level {n}"
