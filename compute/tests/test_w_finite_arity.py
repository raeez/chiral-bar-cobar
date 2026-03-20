"""Tests for compute/lib/w_finite_arity.py — conj:w-finite-arity-WN.

Finite-arity principle for principal W_N: the higher-spin envelope
satisfies ell_n = 0 for n > N.

Ground truth:
  N=2 (Virasoro): PROVED (thm:w-finite-arity-polynomial-pva, d=1)
  N=3: PROVED (cor:w-semistrictity-classical-w3, d=2)
  N>=4: CONJECTURED (conj:w-finite-arity-WN)

Structure:
  1. PVA generator-degree analysis (explicit for N=2,3)
  2. Miura transform degree bounds (all N)
  3. L-infinity bracket vanishing (all N)
  4. Hessian/cubic/kappa data (all N)
  5. Shadow depth classification
  6. Subregular comparison
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.w_finite_arity import (
    PVAGenerator,
    PVAMonomial,
    WN_Linfty,
    MiuraTransform,
    virasoro_pva,
    w3_pva,
    w4_pva,
    w5_pva,
    wN_pva,
    max_generator_degree_from_brackets,
    arity_bound_from_brackets,
    miura_ope_max_composite_degree,
    miura_arity_bound,
    bv_differential_degree_bound,
    ell_n_vanishing_range,
    wn_hessian,
    wn_cubic_invariant,
    wn_kappa,
    wn_central_charge,
    wn_complementarity_partner,
    wn_shadow_depth,
    wn_shadow_archetype,
    subregular_arity,
    verify_finite_arity_principle,
    verify_all_small_N,
    ope_degree_table,
    highest_arity_source,
)


# =========================================================================
# 1. PVA structure and generator-degree analysis
# =========================================================================

class TestPVAStructure:
    """Test PVA generator-degree analysis for explicit small cases."""

    def test_virasoro_generators(self):
        """W_2 = Virasoro has one generator T of spin 2."""
        pva = virasoro_pva()
        assert pva["N"] == 2
        assert len(pva["generators"]) == 1
        assert pva["generators"][0].name == "T"
        assert pva["generators"][0].spin == 2

    def test_virasoro_max_gen_degree(self):
        """Virasoro: all lambda-bracket monomials have gen-degree <= 1.

        {T_lambda T} = c/2 lambda^3 + 2T lambda + dT
        The only monomials are: vacuum (deg 0), T (deg 1), dT (deg 1).
        Max gen-degree = 1.
        """
        pva = virasoro_pva()
        d = max_generator_degree_from_brackets(pva)
        assert d == 1

    def test_virasoro_arity_bound(self):
        """Virasoro: arity bound = d+1 = 2. Bulk is 2-strict."""
        pva = virasoro_pva()
        assert arity_bound_from_brackets(pva) == 2
        assert pva["arity_bound"] == 2

    def test_w3_generators(self):
        """W_3 has generators T (spin 2) and W (spin 3)."""
        pva = w3_pva()
        assert pva["N"] == 3
        assert len(pva["generators"]) == 2
        spins = sorted([g.spin for g in pva["generators"]])
        assert spins == [2, 3]

    def test_w3_max_gen_degree(self):
        """W_3: the T^2 and T*dT terms in {W_lambda W} give gen-degree 2.

        cor:w-semistrictity-classical-w3: max gen-degree = 2.
        """
        pva = w3_pva()
        d = max_generator_degree_from_brackets(pva)
        assert d == 2

    def test_w3_arity_bound(self):
        """W_3: arity bound = d+1 = 3. Bulk is 3-strict (semistrict).

        cor:w-semistrictity-classical-w3: ell_n = 0 for n >= 4.
        """
        pva = w3_pva()
        assert arity_bound_from_brackets(pva) == 3
        assert pva["arity_bound"] == 3

    def test_w3_ww_bracket_has_T_squared(self):
        """The {W_lambda W} bracket contains T^2 (gen-degree 2)."""
        pva = w3_pva()
        ww_brackets = pva["brackets"][("W", "W")]
        # Check lambda^1 coefficient for T^2 term
        pole_1_terms = ww_brackets[1]
        gen_degrees = [t[1].generator_degree for t in pole_1_terms]
        assert 2 in gen_degrees, "T^2 term missing from {W_lambda W}"

    def test_w4_max_gen_degree(self):
        """W_4: max gen-degree = 3 (T^3 type terms from e_2^3 contributions)."""
        pva = w4_pva()
        assert pva["max_gen_degree"] == 3
        assert pva["arity_bound"] == 4

    def test_w5_max_gen_degree(self):
        """W_5: max gen-degree = 4."""
        pva = w5_pva()
        assert pva["max_gen_degree"] == 4
        assert pva["arity_bound"] == 5


class TestPVAMonomial:
    """Test PVAMonomial generator-degree computation."""

    def test_vacuum_degree(self):
        """Vacuum monomial has generator-degree 0."""
        m = PVAMonomial(())
        assert m.generator_degree == 0

    def test_single_generator(self):
        """Single generator has degree 1."""
        m = PVAMonomial((("T", 0),))
        assert m.generator_degree == 1

    def test_derivative_generator(self):
        """Derivative of a generator still has degree 1."""
        m = PVAMonomial((("T", 2),))
        assert m.generator_degree == 1

    def test_quadratic(self):
        """T^2 has generator-degree 2."""
        m = PVAMonomial((("T", 0), ("T", 0)))
        assert m.generator_degree == 2

    def test_mixed_quadratic(self):
        """T * dT has generator-degree 2."""
        m = PVAMonomial((("T", 0), ("T", 1)))
        assert m.generator_degree == 2


# =========================================================================
# 2. Miura transform degree bounds
# =========================================================================

class TestMiuraTransform:
    """Test Miura transform degree analysis for general W_N."""

    def test_miura_virasoro(self):
        """W_2 Miura: max composite degree = 2*2-1 = 3, gen-degree = 1."""
        assert miura_ope_max_composite_degree(2) == 1

    def test_miura_w3(self):
        """W_3 Miura: max composite degree from e_3*e_3 = 5, gen-degree = 2."""
        assert miura_ope_max_composite_degree(3) == 2

    def test_miura_w4(self):
        """W_4 Miura: max composite degree from e_4*e_4 = 7, gen-degree = 3."""
        assert miura_ope_max_composite_degree(4) == 3

    def test_miura_arity_bound_equals_N(self):
        """The Miura arity bound d+1 equals N for all N = 2,...,20."""
        for N in range(2, 21):
            assert miura_arity_bound(N) == N, f"Failed at N={N}"

    def test_miura_transform_object(self):
        """MiuraTransform.arity_bound() == N for N = 2,...,10."""
        for N in range(2, 11):
            mt = MiuraTransform(N)
            assert mt.arity_bound() == N
            assert mt.arity_sharp()

    def test_miura_max_from_top_ope(self):
        """The maximal gen-degree always includes the W^{(N)} x W^{(N)} pair.

        For small N the maximum may be achieved by multiple pairs (ties).
        The essential point is that W^{(N)} x W^{(N)} always achieves the
        global maximum gen-degree = N-1.
        """
        for N in range(2, 11):
            mt = MiuraTransform(N)
            top_deg = mt.max_generator_degree_in_ope(N, N)
            global_deg = mt.global_max_generator_degree()
            assert top_deg == global_deg, (
                f"N={N}: top OPE gen-degree {top_deg} != global {global_deg}"
            )

    def test_miura_generator_degrees(self):
        """Each W^{(s)} has current-degree s in the free-field realization."""
        mt = MiuraTransform(5)
        degs = mt.generator_current_degrees()
        assert degs == {"W2": 2, "W3": 3, "W4": 4, "W5": 5}

    def test_miura_num_bosons(self):
        """W_N Miura uses N-1 free bosons (rank of sl_N)."""
        for N in range(2, 11):
            mt = MiuraTransform(N)
            assert mt.num_bosons == N - 1


# =========================================================================
# 3. L-infinity bracket vanishing
# =========================================================================

class TestLinftyBrackets:
    """Test L-infinity bracket structure from the finite-arity principle."""

    def test_virasoro_ell3_vanishes(self):
        """Virasoro: ell_3 = 0 (bulk is strictly quadratic)."""
        linf = WN_Linfty(2)
        assert linf.ell_n_is_zero(3)
        assert linf.ell_n_is_zero(4)
        assert linf.ell_n_is_zero(100)

    def test_virasoro_ell1_ell2_nonzero(self):
        """Virasoro: ell_1 and ell_2 are the only nonzero brackets."""
        linf = WN_Linfty(2)
        assert not linf.ell_n_is_zero(1)
        assert not linf.ell_n_is_zero(2)
        assert linf.nonzero_brackets() == [1, 2]

    def test_w3_semistrict(self):
        """W_3: ell_1, ell_2, ell_3 nonzero; ell_n = 0 for n >= 4.

        cor:w-semistrictity-classical-w3.
        """
        linf = WN_Linfty(3)
        assert not linf.ell_n_is_zero(1)
        assert not linf.ell_n_is_zero(2)
        assert not linf.ell_n_is_zero(3)
        assert linf.ell_n_is_zero(4)
        assert linf.nonzero_brackets() == [1, 2, 3]

    def test_w4_4_strict(self):
        """W_4: ell_1,...,ell_4 nonzero; ell_n = 0 for n >= 5.

        conj:w-finite-arity-WN for N=4.
        """
        linf = WN_Linfty(4)
        assert not linf.ell_n_is_zero(4)
        assert linf.ell_n_is_zero(5)
        assert linf.bracket_count() == 4

    def test_wN_bracket_count(self):
        """W_N has exactly N possibly nonzero L-infinity brackets."""
        for N in range(2, 15):
            linf = WN_Linfty(N)
            assert linf.bracket_count() == N

    def test_bv_degree_bound(self):
        """BV differential degree bound: max degree = d+1."""
        assert bv_differential_degree_bound(1) == 2  # Virasoro
        assert bv_differential_degree_bound(2) == 3  # W_3
        assert bv_differential_degree_bound(3) == 4  # W_4

    def test_ell_n_vanishing_range(self):
        """ell_n_vanishing_range returns arity_bound = N."""
        for N in range(2, 11):
            bound, _ = ell_n_vanishing_range(N)
            assert bound == N

    def test_w3_weight_recursion_terms(self):
        """W_3 weight recursion has quadratic + cubic contributions.

        thm:w-cubic-weight-recursion: the MC equation involves
        ell_1(alpha_w) + quadratic terms + cubic terms = 0.
        At weight w, quadratic terms come from 2-compositions of w
        (there are w-1 of them), cubic from 3-compositions (C(w-1,2)).
        """
        linf = WN_Linfty(3)
        # Weight 3: 2-compositions = {(1,2),(2,1)} = 2, 3-compositions = {(1,1,1)} = 1
        assert linf.weight_recursion_terms(3) == 2 + 1
        # Weight 4: 2-comp = 3, 3-comp = 3
        assert linf.weight_recursion_terms(4) == 3 + 3


# =========================================================================
# 4. Hessian, cubic, kappa data
# =========================================================================

class TestShadowData:
    """Test Hessian, cubic, and kappa data for principal W_N."""

    def test_wn_hessian_diagonal(self):
        """Hessian is diagonal: H_s = c/s for each spin s.

        thm:w-principal-wn-hessian-cubic, eq:w-principal-wn-hessian.
        """
        c = Symbol('c')
        for N in [2, 3, 4, 5]:
            H = wn_hessian(N)
            assert len(H) == N - 1
            for s in range(2, N + 1):
                assert simplify(H[f"x{s}"] - c / s) == 0

    def test_wn_cubic_has_x2_cubed(self):
        """Cubic invariant always has 2*x_2^3 term.

        eq:w-principal-wn-cubic.
        """
        for N in [2, 3, 4, 5]:
            C = wn_cubic_invariant(N)
            assert "2*x2^3" in C

    def test_wn_central_charge_virasoro(self):
        """W_2 central charge: c = 1 - 6/(k+2).

        DS formula for Virasoro from sl_2.
        """
        k = Symbol('k')
        c = wn_central_charge(2, k)
        # c = 1 - 6/(k+2)
        assert simplify(c - (1 - Rational(6) / (k + 2))) == 0

    def test_wn_central_charge_w3(self):
        """W_3 central charge: c = 2 - 24/(k+3).

        DS formula for W_3 from sl_3.
        """
        k = Symbol('k')
        c = wn_central_charge(3, k)
        # c = 2 - 24/(k+3)
        assert simplify(c - (2 - Rational(24) / (k + 3))) == 0

    def test_wn_central_charge_w4(self):
        """W_4 central charge: c = 3 - 60/(k+4).

        DS formula for W_4 from sl_4.
        """
        k = Symbol('k')
        c = wn_central_charge(4, k)
        # c = 3 - 60/(k+4)
        assert simplify(c - (3 - Rational(60) / (k + 4))) == 0

    def test_complementarity_partner(self):
        """Complementarity constant C_N = N^2 - 1.

        For N=2: C = 3 (wrong: should be 26 for full Virasoro).
        Wait, this is the slab-reduction value.
        For N=2: one (2,-1) betagamma pair gives c = 3.
        For N=3: pairs (2,-1) + (3,-2) give 3 + 5 = 8 = 9-1.
        For N=4: 3 + 5 + 7 = 15 = 16-1.
        """
        assert wn_complementarity_partner(2) == 3
        assert wn_complementarity_partner(3) == 8
        assert wn_complementarity_partner(4) == 15
        assert wn_complementarity_partner(5) == 24


# =========================================================================
# 5. Shadow depth and archetype classification
# =========================================================================

class TestShadowClassification:
    """Test shadow depth and archetype for principal W_N."""

    def test_all_wn_mixed_archetype(self):
        """All principal W_N have infinite shadow tower (class M).

        rem:w-semistrict-archetype-connection: finite bulk arity does NOT
        imply finite shadow depth.  The shadow tower is always infinite
        for N >= 2.
        """
        for N in range(2, 11):
            assert wn_shadow_depth(N) == "M"
            assert wn_shadow_archetype(N) == "Mixed"

    def test_shadow_depth_vs_arity_separation(self):
        """Shadow depth != bulk arity: both are infinite but for different reasons.

        The bulk arity = N (the finite-arity principle).
        The shadow depth = infinity (from iterated contraction of trivalent graphs).
        These are DISTINCT invariants.
        """
        for N in range(2, 11):
            linf = WN_Linfty(N)
            # Bulk arity is finite = N
            assert linf.bracket_count() == N
            # Shadow depth is infinite
            assert wn_shadow_depth(N) == "M"


# =========================================================================
# 6. Subregular comparison
# =========================================================================

class TestSubregularComparison:
    """Compare principal W_N arity with subregular W_n^{(2)} arity."""

    def test_subregular_arity_staircase(self):
        """Subregular arity staircase: W_n^{(2)} has arity n-1.

        cor:w-subregular-arity-staircase.
        """
        assert subregular_arity(3) == 2  # BP is strict
        assert subregular_arity(4) == 3
        assert subregular_arity(5) == 4
        assert subregular_arity(6) == 5

    def test_principal_vs_subregular(self):
        """Principal W_N has arity N, subregular W_n^{(2)} has arity n-1.

        For n = N: principal arity = N, subregular arity = N-1.
        The principal algebra is always one step more nonlinear.
        """
        for N in range(3, 11):
            principal_arity = miura_arity_bound(N)
            sub_arity = subregular_arity(N)
            assert principal_arity == N
            assert sub_arity == N - 1
            assert principal_arity == sub_arity + 1


# =========================================================================
# 7. Comprehensive verification
# =========================================================================

class TestVerification:
    """Comprehensive verification of conj:w-finite-arity-WN."""

    def test_verify_n2(self):
        """Full verification for N=2 (Virasoro)."""
        result = verify_finite_arity_principle(2)
        assert result["N"] == 2
        assert result["max_gen_degree"] == 1
        assert result["arity_bound"] == 2
        assert result["conjectured_bound"] == 2
        assert result["match"] is True
        assert result["status"] == "PROVED"

    def test_verify_n3(self):
        """Full verification for N=3."""
        result = verify_finite_arity_principle(3)
        assert result["N"] == 3
        assert result["max_gen_degree"] == 2
        assert result["arity_bound"] == 3
        assert result["conjectured_bound"] == 3
        assert result["match"] is True
        assert result["status"] == "PROVED"

    def test_verify_n4(self):
        """Full verification for N=4 (conjectured)."""
        result = verify_finite_arity_principle(4)
        assert result["match"] is True
        assert result["status"] == "CONJECTURED"
        assert result["arity_bound"] == 4

    def test_verify_n5(self):
        """Full verification for N=5 (conjectured)."""
        result = verify_finite_arity_principle(5)
        assert result["match"] is True
        assert result["arity_bound"] == 5

    def test_verify_all_small(self):
        """Verify for N = 2,...,10: arity bound always equals N."""
        results = verify_all_small_N(10)
        for r in results:
            assert r["match"] is True, f"Failed at N={r['N']}"

    def test_ope_degree_table_w4(self):
        """OPE degree table for W_4."""
        table = ope_degree_table(4)
        # Pairs: (2,2), (2,3), (2,4), (3,3), (3,4), (4,4)
        assert len(table) == 6
        # The (4,4) entry should have the highest gen-degree = 3
        w4w4 = [row for row in table if row["s1"] == 4 and row["s2"] == 4][0]
        assert w4w4["gen_degree"] == 3
        assert w4w4["contributes_to_arity"] == 4

    def test_ope_degree_table_max_achievable(self):
        """The top OPE pair (N,N) always achieves the maximal gen-degree.

        There may be ties with other pairs, but (N,N) is always among
        the maximizers.
        """
        for N in [3, 4, 5, 6, 7]:
            table = ope_degree_table(N)
            max_deg = max(row["gen_degree"] for row in table)
            top_row = [row for row in table if row["s1"] == N and row["s2"] == N][0]
            assert top_row["gen_degree"] == max_deg, (
                f"N={N}: (N,N) gen-degree {top_row['gen_degree']} != max {max_deg}"
            )

    def test_wN_general_formula(self):
        """Test the general W_N factory for N = 2,...,15."""
        for N in range(2, 16):
            pva = wN_pva(N)
            assert pva["N"] == N
            assert pva["max_gen_degree"] == N - 1
            assert pva["arity_bound"] == N
            assert len(pva["generators"]) == N - 1

    def test_arity_grows_linearly(self):
        """The arity bound grows linearly with N: arity = N.

        This is the content of the conjecture: the rough Miura bound
        is sharp. The arity is determined by the rank of the underlying
        Lie algebra sl_N.
        """
        for N in range(2, 21):
            assert miura_arity_bound(N) == N

    def test_generator_count_is_rank(self):
        """W_N has N-1 generators (= rank of sl_N)."""
        for N in range(2, 11):
            pva = wN_pva(N)
            assert pva["N"] - 1 == len(pva["generators"])

    def test_highest_spin_determines_arity(self):
        """The highest-spin generator W^{(N)} determines the arity.

        Its self-OPE has composites of gen-degree N-1, which is the global
        maximum.
        """
        for N in range(2, 11):
            mt = MiuraTransform(N)
            # Self-OPE of W^{(N)}: current-degree 2N-1, gen-degree = N-1
            self_deg = mt.max_generator_degree_in_ope(N, N)
            global_deg = mt.global_max_generator_degree()
            assert self_deg == global_deg == N - 1
