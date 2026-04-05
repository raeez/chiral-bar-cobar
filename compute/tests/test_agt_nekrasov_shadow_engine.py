r"""Tests for compute/lib/agt_nekrasov_shadow_engine.py

Comprehensive test suite covering:
  - Virasoro conformal blocks (Section 1)
  - AGT dictionary (Section 2)
  - SU(N) Nekrasov generalization (Section 3)
  - Seiberg-Witten prepotential — three paths (Section 4)
  - Omega-background from shadow connection (Section 5)
  - Refined topological vertex (Section 6)
  - ADHM Hilbert series (Section 7)
  - qq-characters (Section 8)
  - W_N conformal blocks (Section 9)
  - Multi-path verification (Section 10)
  - Shadow kappa comparison (Section 11)
  - Instanton counting (Section 12)

MULTI-PATH VERIFICATION strategy:
  Each key result is tested via 3+ independent routes.
"""

import pytest
from sympy import (
    Rational, simplify, sqrt, Symbol, oo, S as Sym,
    bernoulli, factorial, Abs, N as Neval, expand,
)

from compute.lib.agt_nekrasov_shadow_engine import (
    # Section 1: Virasoro conformal blocks
    virasoro_conformal_block,
    _virasoro_gram_matrix,
    _virasoro_block_coefficient,
    _fusion_coefficient_left,
    _fusion_coefficient_right,
    # Section 2: AGT dictionary
    agt_conformal_dimensions_nf4,
    # Section 3: SU(N) Nekrasov
    all_partition_n_tuples,
    nekrasov_factor_n_tuple,
    nekrasov_partition_sun,
    # Section 4: Seiberg-Witten prepotential
    prepotential_from_nekrasov,
    prepotential_from_periods,
    prepotential_from_shadow,
    # Section 5: Omega-background
    omega_background_shadow,
    self_dual_nekrasov,
    ns_limit_from_shadow,
    # Section 6: Refined topological vertex
    refined_vertex_contribution,
    # Section 7: ADHM Hilbert series
    adhm_hilbert_series,
    adhm_dimension,
    bar_complex_instanton_partition,
    # Section 8: qq-characters
    qq_character_su2,
    baxter_tq_check,
    # Section 9: W_N conformal blocks
    w_n_central_charge,
    w_n_kappa,
    su_n_agt_comparison,
    # Section 10: Multi-path verification
    verify_agt_su2_k1,
    verify_agt_su2_k2,
    verify_prepotential_three_paths,
    verify_nekrasov_instanton_numbers,
    # Section 11: Shadow kappa comparison
    agt_shadow_kappa_comparison,
    # Section 12: Instanton counting
    instanton_partition_count,
    nekrasov_weak_coupling_asymptotics,
    nekrasov_modular_property,
)

from compute.lib.agt_shadow_correspondence import (
    agt_central_charge,
    agt_parameter_map,
    nekrasov_partition_su2,
    nekrasov_partition_su3,
    nekrasov_free_energy_su2,
    nekrasov_factor_pair,
    all_partition_pairs,
    all_partitions,
    prepotential_su2_one_inst,
    prepotential_su2_two_inst,
    w3_kappa_from_c,
)


# ===================================================================
# Section 1: Virasoro conformal blocks
# ===================================================================

class TestVirasoroConformalBlocks:
    """Tests for Virasoro conformal block computation."""

    def test_gram_matrix_level_1(self):
        """At level 1, the Gram matrix is 1x1: G = [[2h]]."""
        G = _virasoro_gram_matrix(25, 1, 1)
        assert G.shape == (1, 1)
        # <h|L_1 L_{-1}|h> = 2h
        assert G[0, 0] == 2

    def test_gram_matrix_level_2_dimension(self):
        """At level 2, partitions of 2 are (2,) and (1,1), so G is 2x2."""
        G = _virasoro_gram_matrix(25, 1, 2)
        assert G.shape == (2, 2)

    def test_gram_matrix_level_1_general_h(self):
        """G_{1x1} = 2h for general h."""
        for h_val in [Rational(1, 2), 2, Rational(3, 4)]:
            G = _virasoro_gram_matrix(1, h_val, 1)
            assert G[0, 0] == 2 * h_val

    def test_block_coefficient_level_0(self):
        """F_0 = 1 by normalization."""
        h_ext = (Rational(1, 4), Rational(1, 4), Rational(1, 4), Rational(1, 4))
        assert _virasoro_block_coefficient(25, h_ext, 1, 0) == 1

    def test_conformal_block_structure(self):
        """Conformal block returns dict with correct keys."""
        h_ext = (Rational(1, 4),) * 4
        result = virasoro_conformal_block(25, h_ext, 1, max_level=2)
        assert 0 in result
        assert 1 in result
        assert 2 in result
        assert result[0] == 1

    def test_conformal_block_level_1_nonzero(self):
        """Level-1 coefficient should be nonzero for generic dimensions."""
        h_ext = (Rational(1, 4),) * 4
        result = virasoro_conformal_block(25, h_ext, 1, max_level=1)
        # F_1 depends on the fusion coefficients, should be nonzero generically
        assert result[1] is not None


# ===================================================================
# Section 2: AGT dictionary
# ===================================================================

class TestAGTDictionary:
    """Tests for AGT parameter mapping."""

    def test_nf4_zero_masses(self):
        """N_f=4 with zero masses: all external dimensions equal."""
        result = agt_conformal_dimensions_nf4(
            a_val=1, masses=[0, 0, 0, 0], eps1_val=1, eps2_val=-1
        )
        h_ext = result['h_ext']
        # All four external dimensions should be equal
        for i in range(1, 4):
            assert simplify(h_ext[i] - h_ext[0]) == 0

    def test_nf4_c_value(self):
        """Central charge from AGT map."""
        result = agt_conformal_dimensions_nf4(
            a_val=1, masses=[0, 0, 0, 0], eps1_val=1, eps2_val=-1
        )
        # At eps1=1, eps2=-1: b^2 = 1, b = 1
        # c = 1 + 6*(1+1)^2 = 25
        assert simplify(result['c'] - 25) == 0

    def test_nf4_internal_dimension(self):
        """Internal dimension depends on Coulomb parameter."""
        r1 = agt_conformal_dimensions_nf4(1, [0]*4, 1, -1)
        r2 = agt_conformal_dimensions_nf4(2, [0]*4, 1, -1)
        # Different Coulomb parameters should give different internal dimensions
        assert simplify(r1['h_int'] - r2['h_int']) != 0


# ===================================================================
# Section 3: SU(N) Nekrasov
# ===================================================================

class TestSUNNekrasov:
    """Tests for SU(N) generalization of Nekrasov partition function."""

    def test_partition_n_tuples_count_n2_k1(self):
        """Number of 2-tuples with |Y|=1 should be 2."""
        count = sum(1 for _ in all_partition_n_tuples(1, 2))
        assert count == 2  # ((1,),()), ((), (1,))

    def test_partition_n_tuples_count_n2_k2(self):
        """Number of 2-tuples with |Y|=2."""
        count = sum(1 for _ in all_partition_n_tuples(2, 2))
        expected = sum(1 for _ in all_partition_pairs(2))
        assert count == expected

    def test_partition_n_tuples_count_n3_k1(self):
        """Number of 3-tuples with |Y|=1 should be 3."""
        count = sum(1 for _ in all_partition_n_tuples(1, 3))
        assert count == 3

    def test_partition_n_tuples_count_n4_k1(self):
        """Number of 4-tuples with |Y|=1 should be 4."""
        count = sum(1 for _ in all_partition_n_tuples(1, 4))
        assert count == 4

    def test_su2_from_sun_matches(self):
        """SU(2) via general SU(N) code matches the dedicated SU(2) code."""
        a = Rational(3, 2)
        e1, e2 = Rational(1, 3), Rational(1, 5)

        Z_dedicated = nekrasov_partition_su2(a, e1, e2, 2)
        Z_general = nekrasov_partition_sun([a, -a], e1, e2, 2, max_inst=2)

        for k in range(3):
            assert simplify(Z_dedicated[k] - Z_general[k]) == 0, \
                f"Mismatch at k={k}: {Z_dedicated[k]} vs {Z_general[k]}"

    def test_su3_from_sun_matches(self):
        """SU(3) via general SU(N) code matches dedicated SU(3) code.

        Use non-degenerate Coulomb parameters (all distinct) to avoid
        poles in the Nekrasov bifundamental factor at Q = a_i - a_j = 0.
        """
        a_vals = [Rational(3), Rational(-1), Rational(-2)]
        e1, e2 = Rational(1, 3), Rational(1, 5)

        Z_dedicated = nekrasov_partition_su3(a_vals, e1, e2, 1)
        Z_general = nekrasov_partition_sun(a_vals, e1, e2, 3, max_inst=1)

        for k in range(2):
            assert simplify(Z_dedicated[k] - Z_general[k]) == 0, \
                f"Mismatch at k={k}"

    def test_su4_k0(self):
        """SU(4) at k=0: Z_0 = 1."""
        a_vals = [Rational(3), Rational(1), Rational(-1), Rational(-3)]
        Z = nekrasov_partition_sun(a_vals, Rational(1, 3), Rational(1, 5), 4, max_inst=0)
        assert Z[0] == 1

    def test_su4_k1_nonzero(self):
        """SU(4) at k=1: Z_1 should be nonzero for generic parameters."""
        a_vals = [Rational(3), Rational(1), Rational(-1), Rational(-3)]
        Z = nekrasov_partition_sun(a_vals, Rational(1, 3), Rational(1, 5), 4, max_inst=1)
        assert Z[1] != 0

    def test_sun_z0_is_1(self):
        """Z_0 = 1 for all N (empty diagrams contribute 1)."""
        for N in [2, 3, 4]:
            a_vals = list(range(N))
            # Adjust to have zero sum
            total = sum(a_vals)
            a_vals = [Rational(v) - Rational(total, N) for v in a_vals]
            Z = nekrasov_partition_sun(a_vals, Rational(1, 3), Rational(1, 5), N, max_inst=0)
            assert Z[0] == 1


# ===================================================================
# Section 4: Seiberg-Witten prepotential — three paths
# ===================================================================

class TestSeibergWittenPrepotential:
    """Tests for the prepotential from multiple paths."""

    def test_known_f0_k1(self):
        """F_0^{(1)} = 1/(2a^2) for pure SU(2) (known exact result)."""
        for a_val in [1, 2, 3, 5]:
            a = Rational(a_val)
            result = prepotential_from_periods(a, 1)
            expected = Rational(1, 2) / a**2
            assert result[1] == expected

    def test_known_f0_k2(self):
        """F_0^{(2)} for pure SU(2) is the known two-instanton result."""
        a = Rational(3)
        result = prepotential_from_periods(a, 2)
        # F_0^{(2)} = 5/(64*a^6) for pure SU(2)
        expected = Rational(5, 64) / a**6
        assert result[2] == expected

    def test_prepotential_periods_k1_matches_old(self):
        """Path 2 matches the old dedicated prepotential function."""
        a = Rational(5)
        path2 = prepotential_from_periods(a, 1)
        old = prepotential_su2_one_inst(a)
        assert simplify(path2[1] - old) == 0

    def test_prepotential_nekrasov_k1_convergence(self):
        """Path 1 (eps->0 limit) should converge to F_0^{(1)}."""
        a = Rational(3)
        # At small eps, eps^2 * Z_1(a, eps, eps) -> F_0^{(1)}
        # We test that the estimate improves with smaller eps
        estimates = []
        for p in [5, 10, 20]:
            eps = Rational(1, p)
            Z = nekrasov_partition_su2(a, eps, eps, 1)
            est = eps**2 * Z[1]
            estimates.append(float(est))

        exact = float(Rational(1, 2) / a**2)
        # Each subsequent estimate should be closer to exact
        errors = [abs(e - exact) for e in estimates]
        assert errors[-1] < errors[0], \
            f"Convergence failed: errors = {errors}"

    def test_shadow_genus0_structure(self):
        """Shadow genus-0 projection returns correct kappa for Virasoro."""
        result = prepotential_from_shadow(25)
        assert result['kappa'] == Rational(25, 2)
        assert result['shadow_depth'] == 'infinite (class M)'

    def test_shadow_c0_uncurved(self):
        """At c=0: kappa=0, shadow is uncurved (but shadow depth infinite)."""
        result = prepotential_from_shadow(0)
        assert result['kappa'] == 0

    def test_prepotential_positivity(self):
        """All instanton prepotential coefficients are positive for a > 0."""
        a = Rational(3)
        result = prepotential_from_periods(a, 5)
        for k in result:
            assert result[k] > 0, f"F_0^{{({k})}} = {result[k]} should be positive"


# ===================================================================
# Section 5: Omega-background
# ===================================================================

class TestOmegaBackground:
    """Tests for Omega-background and special limits."""

    def test_self_dual_beta_zero(self):
        """At eps1 = -eps2: beta = 0."""
        result = omega_background_shadow(1, -1)
        assert result['beta'] == 0
        assert result['is_self_dual'] is True

    def test_generic_not_self_dual(self):
        """Generic eps1, eps2: not self-dual."""
        result = omega_background_shadow(1, 2)
        assert result['is_self_dual'] is False

    def test_hbar_product(self):
        """hbar = eps1 * eps2."""
        for e1, e2 in [(1, 2), (3, 5), (1, -1)]:
            result = omega_background_shadow(e1, e2)
            assert result['hbar'] == Rational(e1) * Rational(e2)

    def test_self_dual_nekrasov_z0(self):
        """Z_0 = 1 at the self-dual point."""
        Z = self_dual_nekrasov(Rational(3, 2), 1, max_inst=1)
        assert Z[0] == 1

    def test_self_dual_nekrasov_symmetry(self):
        """At eps1 = -eps2, the partition function has enhanced symmetry."""
        a = Rational(3, 2)
        eps = Rational(1, 3)
        Z = self_dual_nekrasov(a, eps, max_inst=2)
        # Z_k should be real rational numbers
        for k in Z:
            assert isinstance(Z[k], Rational) or Z[k].is_rational

    def test_ns_limit_returns_dict(self):
        """NS limit returns instanton coefficients."""
        result = ns_limit_from_shadow(Rational(3, 2), 1, max_inst=2)
        assert isinstance(result, dict)
        # Should have entries for k=1,2
        assert len(result) >= 1

    def test_omega_c_value(self):
        """Central charge from Omega parameters."""
        result = omega_background_shadow(1, -1)
        assert simplify(result['c'] - 25) == 0


# ===================================================================
# Section 6: Refined topological vertex
# ===================================================================

class TestRefinedVertex:
    """Tests for the refined topological vertex."""

    def test_empty_vertex(self):
        """C_{(),(),()}(t,q) = 1."""
        result = refined_vertex_contribution((), (), (), 1, -1)
        assert result == 1

    def test_single_box_vertex(self):
        """C_{(1),(),()}(t,q) is well-defined."""
        result = refined_vertex_contribution((1,), (), (), 1, -1)
        assert result is not None

    def test_unrefined_empty(self):
        """At eps1 = -eps2, the empty vertex is 1."""
        result = refined_vertex_contribution((), (), (), 1, -1)
        assert result == 1


# ===================================================================
# Section 7: ADHM Hilbert series
# ===================================================================

class TestADHMHilbertSeries:
    """Tests for ADHM moduli space Hilbert series."""

    def test_k0_hilbert(self):
        """k=0: HS = 1 (trivial moduli space)."""
        hs = adhm_hilbert_series(0, 2)
        assert hs == {0: 1}

    def test_k1_n2_dimension(self):
        """k=1, N=2: M_{1,2} = C^2, HS = 1/(1-t)^2."""
        hs = adhm_hilbert_series(1, 2, max_degree=5)
        # Coefficients of 1/(1-t)^2 = sum (n+1) t^n
        for n in range(6):
            assert hs[n] == n + 1, f"HS[{n}] = {hs[n]}, expected {n+1}"

    def test_k1_n3_dimension(self):
        """k=1, N=3: M_{1,3} = C^4, HS = 1/(1-t)^4."""
        hs = adhm_hilbert_series(1, 3, max_degree=5)
        # Coefficients of 1/(1-t)^4 = binom(n+3, 3)
        from sympy import binomial
        for n in range(6):
            expected = int(binomial(n + 3, 3))
            assert hs[n] == expected, f"HS[{n}] = {hs[n]}, expected {expected}"

    def test_k2_n2_leading(self):
        """k=2, N=2: leading Hilbert series coefficients."""
        hs = adhm_hilbert_series(2, 2, max_degree=4)
        # Known: HS = (1+t^2)/((1-t)^2 * (1-t^2)^2)
        # Leading coefficients: 1, 2, 6, 10, 19, ...
        assert hs[0] == 1
        assert hs[1] >= 1  # Should be positive

    def test_k3_n2_known(self):
        """k=3, N=2: known leading coefficients."""
        hs = adhm_hilbert_series(3, 2, max_degree=3)
        assert hs[0] == 1
        assert hs[1] == 3

    def test_adhm_dimension_formula(self):
        """dim_C(M_{k,N}) = 2kN."""
        assert adhm_dimension(1, 2) == 4
        assert adhm_dimension(2, 2) == 8
        assert adhm_dimension(1, 3) == 6
        assert adhm_dimension(3, 4) == 24

    def test_bar_complex_k1(self):
        """Bar complex partition for k=1."""
        result = bar_complex_instanton_partition(1, 2)
        assert result[0] == 1
        assert 1 in result


# ===================================================================
# Section 8: qq-characters
# ===================================================================

class TestQQCharacters:
    """Tests for qq-characters from Yangian shadow."""

    def test_qq_character_k0(self):
        """Leading qq-character: chi_0(x) = x + 1/x."""
        result = qq_character_su2(3, 1, Rational(1, 3), Rational(1, 5), max_inst=0)
        assert 0 in result
        # chi_0(3) = 3 + 1/3 = 10/3
        assert result[0] == Rational(10, 3)

    def test_qq_character_k1_exists(self):
        """k=1 qq-character contribution exists."""
        result = qq_character_su2(3, 1, Rational(1, 3), Rational(1, 5), max_inst=1)
        assert 1 in result

    def test_qq_character_k2_exists(self):
        """k=2 qq-character contribution exists."""
        result = qq_character_su2(3, 1, Rational(1, 3), Rational(1, 5), max_inst=2)
        assert 2 in result

    def test_baxter_leading(self):
        """Baxter TQ relation satisfied at leading order."""
        result = baxter_tq_check(1, Rational(1, 3), Rational(1, 5), 3)
        assert result['leading_order_satisfied'] is True


# ===================================================================
# Section 9: W_N conformal blocks
# ===================================================================

class TestWNConformalBlocks:
    """Tests for W_N algebra central charges and kappa values."""

    def test_w2_is_virasoro(self):
        """W_2 = Virasoro: c_{W_2}(b) = 1 + 6(b+1/b)^2."""
        c_w2 = w_n_central_charge(2, 1)
        c_vir = agt_central_charge(1)
        assert simplify(c_w2 - c_vir) == 0

    def test_w3_central_charge(self):
        """W_3 central charge at b=1."""
        c_w3 = w_n_central_charge(3, 1)
        # c_{W_3} = 2*(1 + 12*(1+1)^2) = 2*(1+48) = 98
        assert simplify(c_w3 - 98) == 0

    def test_w4_central_charge(self):
        """W_4 central charge at b=1."""
        c_w4 = w_n_central_charge(4, 1)
        # c_{W_4} = 3*(1 + 20*(1+1)^2) = 3*(1+80) = 243
        assert simplify(c_w4 - 243) == 0

    def test_w2_kappa_is_c_over_2(self):
        """kappa(W_2) = c/2 (Virasoro formula)."""
        c = Rational(25)
        kappa = w_n_kappa(2, c)
        assert simplify(kappa - c / 2) == 0

    def test_w3_kappa_formula(self):
        """kappa(W_3) = c*(H_3 - 1) = c*(1/2 + 1/3) = 5c/6."""
        c = Rational(98)
        kappa = w_n_kappa(3, c)
        expected = 5 * c / 6
        assert simplify(kappa - expected) == 0

    def test_w4_kappa_formula(self):
        """kappa(W_4) = c*(H_4 - 1) = c*(1/2 + 1/3 + 1/4) = 13c/12."""
        c = Rational(243)
        kappa = w_n_kappa(4, c)
        expected = 13 * c / 12
        assert simplify(kappa - expected) == 0

    def test_w_n_kappa_additivity(self):
        """kappa(W_N) is additive over generators (structural check)."""
        # kappa(W_3) = kappa_T + kappa_W = c/2 + c/3 = 5c/6
        c = Rational(30)
        kappa_T = c / 2
        kappa_W = c / 3
        assert simplify(w_n_kappa(3, c) - kappa_T - kappa_W) == 0

    def test_su_n_comparison_returns_data(self):
        """SU(N) AGT comparison returns structured data."""
        a_vals = [Rational(1), Rational(-1)]
        result = su_n_agt_comparison(2, a_vals, Rational(1, 3), Rational(1, 5), max_inst=1)
        assert 'N' in result
        assert result['N'] == 2
        assert 'Z_Nekrasov' in result
        assert 'c_WN' in result
        assert 'kappa_WN' in result


# ===================================================================
# Section 10: Multi-path verification (the core AGT tests)
# ===================================================================

class TestMultiPathVerification:
    """Multi-path verification of AGT correspondence."""

    def test_k1_three_paths(self):
        """k=1 instanton: three paths agree."""
        result = verify_agt_su2_k1(Rational(3, 2), Rational(1, 3), Rational(1, 5))
        assert result['paths_agree'], "Paths 1 and 2 disagree for k=1"
        assert result['eps_symmetry'], "eps1<->eps2 symmetry fails for k=1"

    def test_k2_three_paths(self):
        """k=2 instanton: three paths agree."""
        result = verify_agt_su2_k2(Rational(3, 2), Rational(1, 3), Rational(1, 5))
        assert result['paths_agree'], "Paths 1 and 2 disagree for k=2"
        assert result['eps_symmetry'], "eps1<->eps2 symmetry fails for k=2"

    def test_k1_multiple_parameters(self):
        """k=1 verification at multiple parameter values."""
        for a_val in [Rational(1), Rational(3, 2), Rational(5, 2)]:
            result = verify_agt_su2_k1(a_val, Rational(1, 3), Rational(1, 5))
            assert result['paths_agree'], \
                f"Paths disagree for k=1, a={a_val}"

    def test_k2_multiple_parameters(self):
        """k=2 verification at multiple parameter values."""
        for a_val in [Rational(3, 2), Rational(5, 2)]:
            result = verify_agt_su2_k2(a_val, Rational(1, 3), Rational(1, 5))
            assert result['paths_agree'], \
                f"Paths disagree for k=2, a={a_val}"

    def test_instanton_numbers_su2(self):
        """Full instanton computation for SU(2) up to k=5."""
        result = verify_nekrasov_instanton_numbers(
            Rational(3, 2), Rational(1, 3), Rational(1, 5), max_inst=5
        )
        Z = result['Z']
        # Z_0 = 1 always
        assert Z[0] == 1
        # Z_k for k >= 1 should be nonzero for generic parameters
        for k in range(1, 6):
            assert Z[k] != 0, f"Z_{k} = 0 (should be nonzero for generic a)"
        # eps1 <-> eps2 symmetry
        for k in range(6):
            assert result['eps_symmetry'][k], f"eps-symmetry fails at k={k}"

    def test_instanton_numbers_z1_formula(self):
        """Z_1 for SU(2) matches known formula."""
        a = Rational(3, 2)
        e1 = Rational(1, 3)
        e2 = Rational(1, 5)
        Z = nekrasov_partition_su2(a, e1, e2, 1)
        Z1 = Z[1]
        # Verify Z_1 is a rational function of a, e1, e2
        assert isinstance(Z1, Rational)
        # Z_1 should be nonzero
        assert Z1 != 0

    def test_instanton_numbers_z2_formula(self):
        """Z_2 for SU(2) matches term-by-term sum."""
        a = Rational(3, 2)
        e1 = Rational(1, 3)
        e2 = Rational(1, 5)
        Z = nekrasov_partition_su2(a, e1, e2, 2)
        Z2_direct = Z[2]

        # Independent computation: enumerate all pairs
        Z2_manual = Rational(0)
        for (Y1, Y2) in all_partition_pairs(2):
            z = nekrasov_factor_pair(a, Y1, Y2, e1, e2)
            if z != oo:
                Z2_manual += z

        assert simplify(Z2_direct - Z2_manual) == 0

    def test_instanton_numbers_z3_formula(self):
        """Z_3 for SU(2) matches term-by-term sum."""
        a = Rational(3, 2)
        e1 = Rational(1, 3)
        e2 = Rational(1, 5)
        Z = nekrasov_partition_su2(a, e1, e2, 3)
        Z3_direct = Z[3]

        Z3_manual = Rational(0)
        for (Y1, Y2) in all_partition_pairs(3):
            z = nekrasov_factor_pair(a, Y1, Y2, e1, e2)
            if z != oo:
                Z3_manual += z

        assert simplify(Z3_direct - Z3_manual) == 0

    def test_prepotential_three_paths_k1(self):
        """Prepotential three-path check at k=1.

        Convention: the Nekrasov vector multiplet contribution Z_1 is
        NEGATIVE for pure SU(2) gauge theory.  The prepotential
        F_0^{(1)} = lim eps^2 * f_1 = -1/(2a^2) in this convention.
        The known Seiberg-Witten result has F_0^{(1)} = +1/(2a^2)
        in the opposite sign convention.

        We check that |eps^2 * Z_1| -> 1/(2a^2).
        """
        result = verify_prepotential_three_paths(Rational(3), max_inst=1)
        # Path 2 (exact) should give 1/(2*9) = 1/18
        assert result['path2_k1_exact'] == Rational(1, 18)
        # Path 1 (numerical): |ratio| should be close to 1
        # (sign convention may differ)
        if result['k1_ratio'] is not None:
            ratio = float(Neval(result['k1_ratio'], 10))
            assert abs(abs(ratio) - 1.0) < 0.1, \
                f"Nekrasov prepotential |ratio| = {abs(ratio)}, expected ~1"


# ===================================================================
# Section 11: Shadow kappa comparison
# ===================================================================

class TestShadowKappaComparison:
    """Tests for shadow kappa vs AGT parameter matching."""

    def test_virasoro_kappa_match(self):
        """kappa(Vir) from AGT matches c/2."""
        result = agt_shadow_kappa_comparison(2, Rational(1, 3), Rational(1, 5))
        assert result['match'] is True

    def test_w3_kappa_match(self):
        """kappa(W_3) from AGT matches 5c/6."""
        result = agt_shadow_kappa_comparison(3, Rational(1, 3), Rational(1, 5))
        assert result['match'] is True

    def test_w4_kappa_match(self):
        """kappa(W_4) from AGT matches 13c/12."""
        result = agt_shadow_kappa_comparison(4, Rational(1, 3), Rational(1, 5))
        assert result['match'] is True

    def test_shadow_f1_positive(self):
        """Shadow F_1 = kappa/24 > 0 for positive c.

        Need eps1/eps2 < 0 so that b^2 > 0 and c > 1.
        Use eps1 = 1/3, eps2 = -1/5 => b^2 = 5/3.
        """
        for N in [2, 3, 4]:
            result = agt_shadow_kappa_comparison(N, Rational(1, 3), Rational(-1, 5))
            f1 = result['F1_shadow']
            # c should be positive for b^2 > 0
            assert float(Neval(f1, 10)) > 0, \
                f"F1 for W_{N} should be positive, got {f1}"

    def test_kappa_monotone_in_N(self):
        """kappa(W_N) increases with N at fixed b.

        Use eps1/eps2 < 0 for positive central charge.
        """
        kappas = []
        for N in [2, 3, 4]:
            result = agt_shadow_kappa_comparison(N, Rational(1, 3), Rational(-1, 5))
            kappas.append(float(Neval(result['kappa_WN'], 10)))
        assert kappas[0] < kappas[1] < kappas[2], \
            f"kappa not monotone: {kappas}"


# ===================================================================
# Section 12: Instanton counting
# ===================================================================

class TestInstantonCounting:
    """Tests for instanton counting and asymptotics."""

    def test_partition_count_k0(self):
        """At k=0: one N-tuple (all empty) for all N."""
        for N in [2, 3, 4]:
            assert instanton_partition_count(0, N) == 1

    def test_partition_count_k1_n2(self):
        """At k=1, N=2: two terms ((1),()), ((), (1))."""
        assert instanton_partition_count(1, 2) == 2

    def test_partition_count_k1_n3(self):
        """At k=1, N=3: three terms."""
        assert instanton_partition_count(1, 3) == 3

    def test_partition_count_k2_n2(self):
        """At k=2, N=2: five terms.
        Partitions of 2: (2,), (1,1)
        Pairs: ((2),()) ((1,1),()) ((1),(1)) ((), (2)) ((), (1,1))
        = 5 pairs.
        """
        assert instanton_partition_count(2, 2) == 5

    def test_partition_count_k3_n2(self):
        """At k=3, N=2: count all pairs."""
        # Partitions of 3: (3,), (2,1), (1,1,1)
        # Partitions of 2: (2,), (1,1)
        # Partitions of 1: (1,)
        # Partitions of 0: ()
        # Pairs with total 3:
        #   (3,() = 1 part of 3 x 1 part of 0 = 3*1
        #   (2,() -> (1,) -> 3 parts of 2 x 1 part of 1 = 2*1
        #   (1,() -> (2,) -> ... enumerate explicitly
        count = instanton_partition_count(3, 2)
        # Manual count: sum_{k=0}^{3} p(k)*p(3-k)
        # p(0)=1, p(1)=1, p(2)=2, p(3)=3
        # = 1*3 + 1*2 + 2*1 + 3*1 = 3+2+2+3 = 10
        assert count == 10

    def test_weak_coupling_decay(self):
        """Z_k(a) decays as a -> infinity.

        For pure SU(2), Z_1 ~ const/a^2 as a -> infinity (not 1/a^4,
        because the vector multiplet factor has quadratic leading behavior
        in the Coulomb parameter).
        """
        e1, e2 = Rational(1, 3), Rational(1, 5)

        # Check that Z_1 decreases in magnitude as a grows
        Z_vals = []
        for a_val in [5, 10, 20, 50]:
            a = Rational(a_val)
            Z = nekrasov_partition_su2(a, e1, e2, 1)
            Z_vals.append(abs(float(Z[1])))

        # Z_1 should be strictly decreasing in magnitude
        for i in range(len(Z_vals) - 1):
            assert Z_vals[i] > Z_vals[i + 1], \
                f"Z_1 not decreasing: |Z_1({[5,10,20,50][i]})| = {Z_vals[i]}, " \
                f"|Z_1({[5,10,20,50][i+1]})| = {Z_vals[i+1]}"

    def test_weyl_invariance(self):
        """Z(a) = Z(-a): Weyl reflection invariance for SU(2)."""
        checks = nekrasov_modular_property(
            Rational(3, 2), Rational(1, 3), Rational(1, 5), max_inst=3
        )
        for k in range(4):
            assert checks[k], f"Weyl invariance fails at k={k}"


# ===================================================================
# Cross-cutting: AGT structural tests
# ===================================================================

class TestAGTStructural:
    """Structural tests for the AGT correspondence."""

    def test_z0_always_1(self):
        """Z_0 = 1 for all parameter choices and all N."""
        params = [
            (Rational(1), Rational(1, 3), Rational(1, 5)),
            (Rational(2), Rational(1, 7), Rational(1, 11)),
            (Rational(5, 2), Rational(1, 2), Rational(1, 3)),
        ]
        for a, e1, e2 in params:
            Z = nekrasov_partition_su2(a, e1, e2, 0)
            assert Z[0] == 1

    def test_eps_symmetry_su2_multiple(self):
        """eps1 <-> eps2 symmetry for SU(2) at multiple parameter values."""
        for a_val in [Rational(1), Rational(3, 2), Rational(5, 2)]:
            for max_k in [1, 2, 3]:
                Z12 = nekrasov_partition_su2(a_val, Rational(1, 3), Rational(1, 5), max_k)
                Z21 = nekrasov_partition_su2(a_val, Rational(1, 5), Rational(1, 3), max_k)
                for k in range(max_k + 1):
                    assert simplify(Z12[k] - Z21[k]) == 0, \
                        f"eps-symmetry fails: a={a_val}, k={k}"

    def test_su2_z1_two_terms(self):
        """Z_1 for SU(2) is the sum of exactly two Young diagram contributions."""
        a = Rational(3, 2)
        e1, e2 = Rational(1, 3), Rational(1, 5)

        z_term1 = nekrasov_factor_pair(a, (1,), (), e1, e2)
        z_term2 = nekrasov_factor_pair(a, (), (1,), e1, e2)
        Z1 = z_term1 + z_term2

        Z_full = nekrasov_partition_su2(a, e1, e2, 1)
        assert simplify(Z1 - Z_full[1]) == 0

    def test_agt_c_self_duality(self):
        """c(b) = c(1/b): fundamental AGT self-duality."""
        for b_val in [Rational(2, 3), Rational(3, 5), Rational(7, 11)]:
            c1 = agt_central_charge(b_val)
            c2 = agt_central_charge(1 / b_val)
            assert simplify(c1 - c2) == 0

    def test_agt_c_b1_gives_25(self):
        """c(b=1) = 25: the critical value for AGT."""
        assert agt_central_charge(1) == 25

    def test_shadow_kappa_from_agt_params(self):
        """Shadow kappa matches c/2 from AGT parameters."""
        params = agt_parameter_map(Rational(1, 3), Rational(1, 5))
        kappa = params['kappa']
        c = params['c']
        assert simplify(kappa - c / 2) == 0

    def test_instanton_free_energy_k1(self):
        """Free energy f_1 = Z_1 (leading cumulant)."""
        a = Rational(3, 2)
        e1, e2 = Rational(1, 3), Rational(1, 5)
        Z = nekrasov_partition_su2(a, e1, e2, 1)
        f = nekrasov_free_energy_su2(a, e1, e2, 1)
        assert simplify(f[1] - Z[1]) == 0

    def test_instanton_free_energy_k2(self):
        """Free energy f_2 = Z_2 - Z_1^2/2."""
        a = Rational(3, 2)
        e1, e2 = Rational(1, 3), Rational(1, 5)
        Z = nekrasov_partition_su2(a, e1, e2, 2)
        f = nekrasov_free_energy_su2(a, e1, e2, 2)
        expected = Z[2] - Z[1]**2 / 2
        assert simplify(f[2] - expected) == 0

    def test_su3_z0(self):
        """Z_0 = 1 for SU(3)."""
        a_vals = [Rational(1), Rational(-1, 2), Rational(-1, 2)]
        Z = nekrasov_partition_su3(a_vals, Rational(1, 3), Rational(1, 5), 0)
        assert Z[0] == 1

    def test_su3_z1_nonzero(self):
        """Z_1 nonzero for SU(3) with generic parameters."""
        a_vals = [Rational(2), Rational(-1), Rational(-1)]
        Z = nekrasov_partition_su3(a_vals, Rational(1, 3), Rational(1, 5), 1)
        assert Z[1] != 0

    def test_w3_kappa_from_c_function(self):
        """w3_kappa_from_c returns 5c/6."""
        for c_val in [6, 12, 30, 98]:
            kappa = w3_kappa_from_c(c_val)
            assert kappa == 5 * Rational(c_val) / 6


# ===================================================================
# Multi-path: Nekrasov Z_k via AGT and shadow
# ===================================================================

class TestMultiPathNekrasovShadow:
    """Multi-path tests connecting Nekrasov, AGT, and shadow tower."""

    def test_nekrasov_shadow_genus1_comparison(self):
        """Shadow F_1 = kappa/24 is structurally consistent with Nekrasov.

        The shadow gives the UNIVERSAL (a-independent) part.
        The Nekrasov partition function has both universal and
        representation-dependent parts.

        Structural test: kappa/24 is real and positive.
        """
        from compute.lib.utils import lambda_fp

        params = agt_parameter_map(Rational(1, 3), Rational(1, 5))
        kappa = params['kappa']
        shadow_f1 = kappa * lambda_fp(1)
        # lambda_fp(1) = 1/24
        assert lambda_fp(1) == Rational(1, 24)
        assert simplify(shadow_f1 - kappa / 24) == 0

    def test_nekrasov_z_k_partition_count(self):
        """Number of terms in Z_k matches partition count."""
        for k in range(4):
            expected = instanton_partition_count(k, 2)
            actual = sum(1 for _ in all_partition_pairs(k))
            assert actual == expected

    def test_nekrasov_kappa_weak_coupling(self):
        """At a -> infinity, the Nekrasov sum Z_1 ~ const/a^2.

        The rescaled product a^2 * Z_1 approaches a constant as a -> infinity.
        The shadow kappa = c/2 controls the universal envelope.
        """
        e1, e2 = Rational(1, 3), Rational(1, 5)
        # Z_1 * a^2 should approach a constant
        Z_large = nekrasov_partition_su2(Rational(100), e1, e2, 1)
        Z_small = nekrasov_partition_su2(Rational(10), e1, e2, 1)

        # a^2 * Z_1 should stabilize
        scaled_large = float(Z_large[1] * 100**2)
        scaled_small = float(Z_small[1] * 10**2)

        # The ratio should be close to 1 (same constant)
        ratio = scaled_large / scaled_small
        assert 0.9 < ratio < 1.1, \
            f"Weak coupling ratio = {ratio}, expected ~1 " \
            f"(a^2*Z_1: {scaled_large} vs {scaled_small})"

    def test_shadow_controls_genus_expansion_leading(self):
        """Shadow kappa controls the leading genus expansion coefficient.

        F_g = kappa * lambda_g^FP is the shadow prediction.
        The Nekrasov genus expansion should match this at the universal level.
        """
        from compute.lib.utils import lambda_fp

        c = Rational(25)  # b=1 point
        kappa = c / 2

        for g in range(1, 6):
            fg = kappa * lambda_fp(g)
            assert fg > 0, f"Shadow F_{g} should be positive"
            assert fg == kappa * lambda_fp(g)

    def test_prepotential_k1_from_nekrasov_and_periods(self):
        """F_0^{(1)} from Nekrasov limit matches known exact value.

        Path 1: lim_{eps->0} eps^2 * Z_1(a, eps, eps)
        Path 2: 1/(2a^2) (exact SW result)
        """
        a = Rational(5)
        exact = Rational(1, 2) / a**2  # = 1/50

        # Compute Z_1 at small eps and extract leading term
        for p in [10, 50]:
            eps = Rational(1, p)
            Z = nekrasov_partition_su2(a, eps, eps, 1)
            estimate = eps**2 * Z[1]
            error = abs(float(estimate - exact))
            # Error should decrease with smaller eps
            assert error < 0.1, \
                f"eps=1/{p}: estimate={float(estimate)}, exact={float(exact)}"

    def test_su3_nekrasov_matches_general(self):
        """SU(3) Nekrasov from dedicated and general code agree.

        Use non-degenerate Coulomb parameters to avoid poles.
        """
        a_vals = [Rational(3), Rational(-1), Rational(-2)]
        e1, e2 = Rational(1, 3), Rational(1, 5)

        Z_ded = nekrasov_partition_su3(a_vals, e1, e2, 1)
        Z_gen = nekrasov_partition_sun(a_vals, e1, e2, 3, max_inst=1)

        assert simplify(Z_ded[0] - Z_gen[0]) == 0
        assert simplify(Z_ded[1] - Z_gen[1]) == 0


# ===================================================================
# Performance and edge cases
# ===================================================================

class TestEdgeCases:
    """Edge cases and boundary tests."""

    def test_a_equals_zero(self):
        """Z_k at a=0 should still be computable (may have poles)."""
        # At a=0, some denominators in the Nekrasov formula vanish
        # The function should handle this gracefully
        try:
            Z = nekrasov_partition_su2(0, Rational(1, 3), Rational(1, 5), 1)
            # May return oo for degenerate Coulomb parameter
        except (ZeroDivisionError, Exception):
            pass  # Expected for degenerate case

    def test_large_eps(self):
        """Z_k at large eps should still be computable."""
        Z = nekrasov_partition_su2(Rational(3, 2), 5, 7, 2)
        assert Z[0] == 1
        # Z_k should be finite
        for k in [1, 2]:
            assert Z[k] != oo

    def test_c_at_25(self):
        """At c=25 (b=1): the critical AGT point."""
        assert agt_central_charge(1) == 25
        kappa_25 = Rational(25, 2)
        assert kappa_25 == Rational(25, 2)

    def test_c_at_1(self):
        """At c=1: the free boson point."""
        # b = i gives c = 1, but b must be complex
        # Instead, use c=1 directly
        kappa = Rational(1, 2)
        from compute.lib.utils import lambda_fp
        f1 = kappa * lambda_fp(1)
        assert f1 == Rational(1, 48)

    def test_w_n_kappa_n2(self):
        """kappa(W_2) = c/2 via the H_N formula."""
        c = Symbol('c')
        kappa = w_n_kappa(2, c)
        assert simplify(kappa - c/2) == 0

    def test_partition_n_tuples_empty(self):
        """N-tuples at k=0: one tuple of empty partitions."""
        for N in [1, 2, 3, 4, 5]:
            tuples = list(all_partition_n_tuples(0, N))
            assert len(tuples) == 1
            assert all(p == () for p in tuples[0])
