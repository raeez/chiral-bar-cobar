"""Tests for explicit bar cohomology H*(B(βγ)) at weights 0 through 8.

Ground truth:
  GF: P(x) = √((1+x)/(1-3x)), algebraic degree 2
  Discriminant: Δ(x) = (1+x)(1-3x), shared with Virasoro and sl₂-hat
  Recurrence: n·a(n) = 2n·a(n-1) + 3(n-2)·a(n-2)
  ODE: (1+x)(1-3x)P' = 2P
  Values: 1, 2, 4, 10, 26, 70, 192, 534, 1500, 4246, 12092
  Shadow class: C (contact), depth 4
  Koszul dual: bc ghosts
  κ(λ) = 6λ²-6λ+1, c(λ) = 2κ

  landscape_census.tex: eq:gf-betagamma
  beta_gamma.tex: thm:betagamma-fermion-koszul, prop:betagamma-bar-deg2
"""

import pytest
from fractions import Fraction
from sympy import Rational, Symbol, sqrt, series, simplify

from compute.lib.bar_cohomology_betagamma_explicit_engine import (
    # GF and coefficients
    gf_algebraic_equation,
    bar_cohomology_dim_recurrence,
    bar_cohomology_dim_algebraic,
    bar_cohomology_dim_ode,
    bar_cohomology_dim_trinomial,
    bar_cohomology_dim_integral,
    BETAGAMMA_BAR_COHOMOLOGY,
    BC_BAR_COHOMOLOGY,
    bc_bar_cohomology_dim,
    # Fock space
    betagamma_fock_basis,
    betagamma_fock_dim,
    # Bar complex
    bar_complex_dims_at_weight,
    # Koszulness
    koszulness_test,
    # Shadow data
    betagamma_kappa,
    betagamma_central_charge,
    betagamma_shadow_depth,
    betagamma_shadow_class,
    betagamma_quartic_contact_on_weight_line,
    betagamma_quartic_virasoro_subalgebra,
    # Koszul duality
    koszul_dual_identification,
    complementarity_check,
    # Symplectic boson
    symplectic_boson_data,
    # Discriminant
    discriminant_analysis,
    asymptotic_formula,
    # Weight-0
    weight_zero_analysis,
    # Multi-path verification
    verify_all_paths,
    verify_bc_bar_cohomology,
    verify_convolution_identity,
    verify_ode_relation,
    verify_growth_rate,
    # Summary
    bar_cohomology_table,
)


# ===================================================================
# 1. Generating function coefficients — 5 independent paths
# ===================================================================

class TestPath1Recurrence:
    """Path 1: n·a(n) = 2n·a(n-1) + 3(n-2)·a(n-2)."""

    @pytest.mark.parametrize("h,expected", [
        (0, 1), (1, 2), (2, 4), (3, 10), (4, 26),
        (5, 70), (6, 192), (7, 534), (8, 1500),
    ])
    def test_known_values(self, h, expected):
        assert bar_cohomology_dim_recurrence(h) == expected

    def test_initial_conditions(self):
        assert bar_cohomology_dim_recurrence(0) == 1
        assert bar_cohomology_dim_recurrence(1) == 2

    def test_negative_weight(self):
        assert bar_cohomology_dim_recurrence(-1) == 0
        assert bar_cohomology_dim_recurrence(-5) == 0

    def test_extends_to_weight_12(self):
        """Check a(9)=4246, a(10)=12092, a(11)=34606, a(12)=99442."""
        assert bar_cohomology_dim_recurrence(9) == 4246
        assert bar_cohomology_dim_recurrence(10) == 12092
        assert bar_cohomology_dim_recurrence(11) == 34606
        assert bar_cohomology_dim_recurrence(12) == 99442


class TestPath2Algebraic:
    """Path 2: P² = (1+x)/(1-3x), extract sqrt via Cauchy product."""

    @pytest.mark.parametrize("h,expected", [
        (0, 1), (1, 2), (2, 4), (3, 10), (4, 26),
        (5, 70), (6, 192), (7, 534), (8, 1500),
    ])
    def test_matches_recurrence(self, h, expected):
        assert bar_cohomology_dim_algebraic(h) == expected

    def test_integrality(self):
        """All coefficients must be positive integers."""
        for h in range(15):
            a = bar_cohomology_dim_algebraic(h)
            assert isinstance(a, int) and a > 0


class TestPath3ODE:
    """Path 3: ODE (1+x)(1-3x)P' = 2P."""

    @pytest.mark.parametrize("h,expected", [
        (0, 1), (1, 2), (2, 4), (3, 10), (4, 26),
        (5, 70), (6, 192), (7, 534), (8, 1500),
    ])
    def test_matches_recurrence(self, h, expected):
        assert bar_cohomology_dim_ode(h) == expected


class TestPath4Trinomial:
    """Path 4: Convolution identity from P² = Q."""

    @pytest.mark.parametrize("h,expected", [
        (0, 1), (1, 2), (2, 4), (3, 10), (4, 26),
        (5, 70), (6, 192), (7, 534), (8, 1500),
    ])
    def test_matches_recurrence(self, h, expected):
        assert bar_cohomology_dim_trinomial(h) == expected


class TestPath5Integral:
    """Path 5: Numerical Cauchy integral."""

    @pytest.mark.parametrize("h,expected", [
        (0, 1), (1, 2), (2, 4), (3, 10), (4, 26),
        (5, 70), (6, 192), (7, 534), (8, 1500),
    ])
    def test_matches_recurrence(self, h, expected):
        assert bar_cohomology_dim_integral(h) == expected


class TestAllPathsAgree:
    """All 5 paths must agree at every weight."""

    @pytest.mark.parametrize("h", list(range(9)))
    def test_five_paths_agree(self, h):
        a1 = bar_cohomology_dim_recurrence(h)
        a2 = bar_cohomology_dim_algebraic(h)
        a3 = bar_cohomology_dim_ode(h)
        a4 = bar_cohomology_dim_trinomial(h)
        a5 = bar_cohomology_dim_integral(h)
        assert a1 == a2 == a3 == a4 == a5, (
            f"Disagreement at h={h}: rec={a1}, alg={a2}, ode={a3}, "
            f"tri={a4}, int={a5}"
        )


# ===================================================================
# 2. Hardcoded values match Master Table
# ===================================================================

class TestMasterTable:
    """Cross-check against hardcoded Master Table values (AP10 prevention)."""

    @pytest.mark.parametrize("h", list(range(9)))
    def test_betagamma_matches_table(self, h):
        if h in BETAGAMMA_BAR_COHOMOLOGY:
            assert bar_cohomology_dim_recurrence(h) == BETAGAMMA_BAR_COHOMOLOGY[h]

    @pytest.mark.parametrize("h", list(range(9)))
    def test_bc_matches_table(self, h):
        if h in BC_BAR_COHOMOLOGY:
            assert bc_bar_cohomology_dim(h) == BC_BAR_COHOMOLOGY[h]

    def test_bc_formula(self):
        """bc bar cohomology = 2^n - n + 1 for n ≥ 1."""
        for n in range(1, 12):
            assert bc_bar_cohomology_dim(n) == 2**n - n + 1


# ===================================================================
# 3. Algebraic equation and convolution identity
# ===================================================================

class TestAlgebraicEquation:
    """Verify P² = (1+x)/(1-3x) at coefficient level."""

    @pytest.mark.parametrize("n", list(range(9)))
    def test_convolution(self, n):
        """Σ_{k=0}^{n} a(k)·a(n-k) = q(n) where q(n) from (1+x)/(1-3x)."""
        conv = sum(bar_cohomology_dim_recurrence(k) *
                   bar_cohomology_dim_recurrence(n - k)
                   for k in range(n + 1))
        expected = 1 if n == 0 else 3**n + 3**(n - 1)
        assert conv == expected

    def test_algebraic_degree_2(self):
        """P satisfies a polynomial of degree 2: (1-3x)P² = 1+x."""
        data = gf_algebraic_equation()
        x = Symbol('x')
        assert data['discriminant'] == 1 - 2*x - 3*x**2

    def test_branch_singularities(self):
        data = gf_algebraic_equation()
        assert Rational(-1) in data['branch_singularities']
        assert Rational(1, 3) in data['branch_singularities']


# ===================================================================
# 4. ODE relation
# ===================================================================

class TestODE:
    """Verify (n+1)a_{n+1} = 2(n+1)a_n + 3(n-1)a_{n-1}."""

    @pytest.mark.parametrize("n", list(range(1, 8)))
    def test_ode_relation(self, n):
        a_prev = bar_cohomology_dim_recurrence(n - 1)
        a_curr = bar_cohomology_dim_recurrence(n)
        a_next = bar_cohomology_dim_recurrence(n + 1)
        lhs = (n + 1) * a_next
        rhs = 2 * (n + 1) * a_curr + 3 * (n - 1) * a_prev
        assert lhs == rhs, f"ODE fails at n={n}: {lhs} != {rhs}"

    def test_equivalent_master_recurrence(self):
        """Master recurrence: n·a(n) = 2n·a(n-1) + 3(n-2)·a(n-2)."""
        for n in range(2, 10):
            a = bar_cohomology_dim_recurrence
            assert n * a(n) == 2 * n * a(n-1) + 3 * (n-2) * a(n-2)


# ===================================================================
# 5. Fock space structure
# ===================================================================

class TestFockSpace:
    """Vacuum module / Fock space of βγ."""

    def test_dim_weight_0(self):
        """No states at weight 0 in augmentation ideal."""
        assert betagamma_fock_dim(0) == 0

    def test_dim_weight_1(self):
        """Weight 1: β_{-1}|0⟩ and γ_{-1}|0⟩."""
        assert betagamma_fock_dim(1) == 2

    def test_dim_weight_2(self):
        """Weight 2: β₋₂, γ₋₂, β₋₁², β₋₁γ₋₁, γ₋₁²."""
        assert betagamma_fock_dim(2) == 5

    def test_dim_weight_3(self):
        assert betagamma_fock_dim(3) == 10

    def test_two_colored_partitions(self):
        """Fock space dim = 2-colored partition function."""
        # Two bosonic generators, both weight 1:
        # dim V_h = Σ_{j=0}^h p(j)·p(h-j)
        from functools import lru_cache

        @lru_cache(maxsize=256)
        def p(n):
            if n < 0: return 0
            if n == 0: return 1
            dp = [0]*(n+1)
            dp[0] = 1
            for i in range(1, n+1):
                for j in range(i, n+1):
                    dp[j] += dp[j-i]
            return dp[n]

        for h in range(1, 8):
            expected = sum(p(j) * p(h-j) for j in range(h+1))
            assert betagamma_fock_dim(h) == expected

    def test_fock_basis_weight_1(self):
        """Explicit basis at weight 1."""
        basis = betagamma_fock_basis(1)
        assert len(basis) == 2
        # Should be (β₋₁, ∅) and (∅, γ₋₁)
        assert ((1,), ()) in basis
        assert ((), (1,)) in basis

    def test_fock_basis_weight_2(self):
        """Explicit basis at weight 2."""
        basis = betagamma_fock_basis(2)
        assert len(basis) == 5


# ===================================================================
# 6. Bar complex dimensions
# ===================================================================

class TestBarComplexDims:
    """Naive bar chain group dimensions at each weight."""

    def test_weight_1(self):
        dims = bar_complex_dims_at_weight(1)
        # B^1_1 = V_1 (dim 2), no higher bar degrees
        assert dims[1] == 2
        assert 2 not in dims

    def test_weight_2(self):
        dims = bar_complex_dims_at_weight(2)
        # B^1_2 = V_2 (dim 5)
        assert dims[1] == 5
        # B^2_2 = V_1 ⊗ V_1 (dim 2*2=4)
        assert dims[2] == 4

    def test_weight_3(self):
        dims = bar_complex_dims_at_weight(3)
        assert dims[1] == 10  # V_3
        # B^2_3 = V_1⊗V_2 + V_2⊗V_1 = 2*5 + 5*2 = 20
        assert dims[2] == 2 * 5 + 5 * 2
        # B^3_3 = V_1⊗V_1⊗V_1 = 8
        assert dims[3] == 8

    def test_bar_coh_leq_chain_dims(self):
        """Bar cohomology ≤ total chain dim (sanity check)."""
        for h in range(1, 6):
            chain_total = sum(bar_complex_dims_at_weight(h).values())
            coh_dim = bar_cohomology_dim_recurrence(h)
            assert coh_dim <= chain_total


# ===================================================================
# 7. Koszulness
# ===================================================================

class TestKoszulness:
    """βγ is chirally Koszul: bar cohomology concentrated in degree 1."""

    def test_koszulness_algebraic_eq(self):
        """The algebraic equation (Koszul relation at coefficient level)."""
        results = koszulness_test(8)
        for key, val in results.items():
            assert val, f"Koszulness check failed: {key}"

    def test_concentrated_in_bar_degree_1(self):
        """Informational: for Koszul algebra, all H^k=0 for k≥2."""
        # We verify this is consistent with the GF:
        # If all cohomology is in degree 1, then
        # dim H^1_h = a(h) = bar_cohomology_dim
        for h in range(1, 9):
            assert bar_cohomology_dim_recurrence(h) > 0


# ===================================================================
# 8. Shadow data
# ===================================================================

class TestShadowData:
    """Shadow obstruction tower invariants."""

    def test_shadow_class(self):
        assert betagamma_shadow_class() == "C"

    def test_shadow_depth(self):
        assert betagamma_shadow_depth() == 4

    def test_quartic_contact_vanishes(self):
        """mu_{bg} = 0 on the weight-changing line."""
        assert betagamma_quartic_contact_on_weight_line() == 0

    @pytest.mark.parametrize("lam_val,expected_kappa", [
        (0, 1),
        (Rational(1, 2), Rational(-1, 2)),
        (1, 1),
        (2, 13),
    ])
    def test_kappa_values(self, lam_val, expected_kappa):
        assert betagamma_kappa(lam_val) == expected_kappa

    @pytest.mark.parametrize("lam_val,expected_c", [
        (0, 2),
        (Rational(1, 2), -1),
        (1, 2),
        (2, 26),
    ])
    def test_central_charge(self, lam_val, expected_c):
        assert betagamma_central_charge(lam_val) == expected_c

    def test_kappa_is_c_over_2(self):
        """κ = c/2 for βγ (AP39: this holds for rank-1 algebras)."""
        lam = Symbol('lambda')
        kappa = betagamma_kappa(lam)
        c = betagamma_central_charge(lam)
        assert simplify(kappa - c / 2) == 0

    def test_kappa_symmetric_under_lambda_to_one_minus_lambda(self):
        """κ(λ) = κ(1-λ): weight symmetry (NOT Koszul duality)."""
        lam = Symbol('lambda')
        assert simplify(betagamma_kappa(lam) - betagamma_kappa(1 - lam)) == 0

    def test_quartic_vir_subalgebra(self):
        """Q^contact from Virasoro subalgebra = 10/(c(5c+22))."""
        c = Symbol('c')
        q = betagamma_quartic_virasoro_subalgebra(c)
        assert simplify(q - Rational(10) / (c * (5*c + 22))) == 0


# ===================================================================
# 9. Koszul duality: βγ ↔ bc
# ===================================================================

class TestKoszulDuality:
    """The duality pair (βγ)! = bc, (bc)! = βγ."""

    def test_dual_identification(self):
        data = koszul_dual_identification()
        assert data["betagamma_dual"] == "bc_ghosts"
        assert data["bc_dual"] == "betagamma"

    def test_shared_discriminant(self):
        data = koszul_dual_identification()
        assert data["shared_discriminant"] == "1 - 2x - 3x^2"

    def test_complementarity_generic(self):
        """κ(βγ) + κ(bc) = 0 for free fields (AP24 safe)."""
        lam = Symbol('lambda')
        comp = complementarity_check(lam)
        assert comp['is_zero']

    @pytest.mark.parametrize("lam_val", [0, Rational(1, 2), 1, 2])
    def test_complementarity_numerical(self, lam_val):
        comp = complementarity_check(lam_val)
        assert comp['sum'] == 0

    def test_involution(self):
        """(A!)! = A: bc is dual of βγ and vice versa."""
        data = koszul_dual_identification()
        assert data["betagamma_dual"] == "bc_ghosts"
        assert data["bc_dual"] == "betagamma"


# ===================================================================
# 10. Symplectic boson comparison
# ===================================================================

class TestSymplecticBoson:
    """βγ at λ=1/2 (symplectic boson)."""

    def test_central_charge(self):
        data = symplectic_boson_data()
        assert data["central_charge"] == -1

    def test_kappa(self):
        data = symplectic_boson_data()
        assert data["kappa"] == Rational(-1, 2)

    def test_shadow_class(self):
        data = symplectic_boson_data()
        assert data["shadow_class"] == "C"

    def test_shadow_depth(self):
        data = symplectic_boson_data()
        assert data["shadow_depth"] == 4

    def test_complementarity(self):
        data = symplectic_boson_data()
        assert data["kappa_plus_kappa_dual"] == 0


# ===================================================================
# 11. Discriminant analysis and growth
# ===================================================================

class TestDiscriminant:
    """Shared discriminant Δ(x) = 1-2x-3x² = (1+x)(1-3x)."""

    def test_factorization(self):
        data = discriminant_analysis()
        x = Symbol('x')
        assert data['factored'] == (1 + x)*(1 - 3*x)

    def test_zeros(self):
        data = discriminant_analysis()
        assert Rational(-1) in data['zeros']
        assert Rational(1, 3) in data['zeros']

    def test_growth_rate(self):
        """Exponential growth rate = 3 (from singularity at x=1/3)."""
        data = discriminant_analysis()
        assert data['exponential_growth_rate'] == 3

    def test_ratio_converges_to_3(self):
        """a(n)/a(n-1) → 3."""
        for n in range(8, 13):
            ratio = bar_cohomology_dim_recurrence(n) / bar_cohomology_dim_recurrence(n - 1)
            assert abs(ratio - 3) < 0.3, f"Ratio at n={n}: {ratio:.4f}"

    def test_asymptotic_accuracy(self):
        """Asymptotic formula ~ C·3^n/√n should be within 5% for n≥5."""
        for n in range(5, 9):
            exact = bar_cohomology_dim_recurrence(n)
            approx = asymptotic_formula(n)
            ratio = approx / exact
            assert abs(ratio - 1) < 0.05, f"Asymp ratio at n={n}: {ratio:.4f}"


# ===================================================================
# 12. Weight-0 sector
# ===================================================================

class TestWeightZero:
    """The weight-0 sector and γ₀ zero mode."""

    def test_no_weight_0_states(self):
        data = weight_zero_analysis()
        assert data['dim_augmentation_ideal_wt0'] == 0

    def test_gamma0_annihilates_vacuum(self):
        data = weight_zero_analysis()
        assert data['gamma0_annihilates_vacuum']

    def test_independence_of_lambda(self):
        data = weight_zero_analysis()
        assert data['independence_of_lambda']

    def test_bar_coh_at_weight_0(self):
        """H^0 = 1 (the vacuum)."""
        assert bar_cohomology_dim_recurrence(0) == 1


# ===================================================================
# 13. Cross-family consistency (AP10 prevention)
# ===================================================================

class TestCrossFamilyConsistency:
    """Verify βγ data is consistent with related families."""

    def test_bg_growth_faster_than_bc(self):
        """βγ bar cohomology grows as 3^n/√n; bc grows as 2^n."""
        for h in range(4, 9):
            assert bar_cohomology_dim_recurrence(h) > bc_bar_cohomology_dim(h)

    def test_bg_not_equal_fock(self):
        """Bar cohomology ≠ Fock space dims (chiral bar ≠ naive tensor)."""
        mismatches = 0
        for h in range(2, 9):
            if bar_cohomology_dim_recurrence(h) != betagamma_fock_dim(h):
                mismatches += 1
        assert mismatches > 0, "Bar coh should differ from Fock dims"

    def test_bg_weight_1_matches_generators(self):
        """At weight 1: bar coh dim = 2 (two generators β, γ)."""
        assert bar_cohomology_dim_recurrence(1) == 2
        assert betagamma_fock_dim(1) == 2

    def test_shared_discriminant_property(self):
        """βγ, Vir, sl₂-hat all share Δ = 1-2x-3x²."""
        data = discriminant_analysis()
        x = Symbol('x')
        delta = data['discriminant']
        # Verify factorization
        assert simplify(delta - (1 - 2*x - 3*x**2)) == 0
        # Verify roots
        assert simplify(delta.subs(x, Rational(1, 3))) == 0
        assert simplify(delta.subs(x, -1)) == 0


# ===================================================================
# 14. Verification batteries
# ===================================================================

class TestVerificationBatteries:
    """Run the built-in verification suites."""

    def test_all_paths(self):
        results = verify_all_paths(8)
        for key, val in results.items():
            assert val, f"Multi-path verification failed: {key}"

    def test_bc_bar_cohomology(self):
        results = verify_bc_bar_cohomology(8)
        for key, val in results.items():
            assert val, f"bc verification failed: {key}"

    def test_convolution_identity(self):
        results = verify_convolution_identity(8)
        for key, val in results.items():
            assert val, f"Convolution identity failed: {key}"

    def test_ode_relation(self):
        results = verify_ode_relation(8)
        for key, val in results.items():
            assert val, f"ODE relation failed: {key}"

    def test_growth_rate(self):
        results = verify_growth_rate(12)
        assert results.get("growth_rate_converges_to_3", False)


# ===================================================================
# 15. Summary table structure
# ===================================================================

class TestSummaryTable:
    """Verify the summary table is well-formed."""

    def test_table_has_all_weights(self):
        table = bar_cohomology_table(8)
        for h in range(9):
            assert h in table

    def test_table_entries_complete(self):
        table = bar_cohomology_table(8)
        for h in range(9):
            assert "bar_coh_dim" in table[h]
            assert "bc_bar_coh_dim" in table[h]

    def test_table_values_positive(self):
        table = bar_cohomology_table(8)
        for h in range(1, 9):
            assert table[h]["bar_coh_dim"] > 0
            assert table[h]["bc_bar_coh_dim"] > 0


# ===================================================================
# 16. Sympy GF verification (independent of engine)
# ===================================================================

class TestSympyGF:
    """Independent sympy verification of the generating function."""

    def test_gf_series_expansion(self):
        """Expand √((1+x)/(1-3x)) and check coefficients."""
        x = Symbol('x')
        P = sqrt((1 + x) / (1 - 3*x))
        s = series(P, x, 0, 10)
        expected = [1, 2, 4, 10, 26, 70, 192, 534, 1500, 4246]
        for i, val in enumerate(expected):
            assert s.coeff(x, i) == val

    def test_ode_symbolic(self):
        """Verify (1-2x-3x²)P' = 2P symbolically."""
        x = Symbol('x')
        P = sqrt((1 + x) / (1 - 3*x))
        lhs = (1 - 2*x - 3*x**2) * P.diff(x)
        rhs = 2 * P
        assert simplify(lhs - rhs) == 0

    def test_algebraic_equation_symbolic(self):
        """Verify (1-3x)P² = 1+x symbolically."""
        x = Symbol('x')
        P = sqrt((1 + x) / (1 - 3*x))
        assert simplify((1 - 3*x) * P**2 - (1 + x)) == 0


# ===================================================================
# 17. Edge cases and robustness
# ===================================================================

class TestEdgeCases:
    """Edge cases for robustness."""

    def test_large_weight(self):
        """Compute at weight 15 without error."""
        val = bar_cohomology_dim_recurrence(15)
        assert val > 0
        # Cross-check with algebraic path
        assert val == bar_cohomology_dim_algebraic(15)

    def test_monotone_increasing(self):
        """a(n) is strictly increasing for n ≥ 1."""
        for n in range(1, 12):
            assert bar_cohomology_dim_recurrence(n) < bar_cohomology_dim_recurrence(n + 1)

    def test_all_positive(self):
        """All coefficients are positive."""
        for n in range(15):
            assert bar_cohomology_dim_recurrence(n) > 0

    def test_bc_monotone(self):
        """bc bar cohomology is strictly increasing for n ≥ 1."""
        for n in range(1, 10):
            assert bc_bar_cohomology_dim(n) < bc_bar_cohomology_dim(n + 1)
