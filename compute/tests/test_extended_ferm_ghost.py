"""Tests for extended fermion-ghost duality (conj:extended-ferm-ghost).

Verifies computational aspects of the conjecture that a derived fermionic
system F^bullet is Koszul dual to the derived betagamma-bc system.

PROVED BASE CASES:
  thm:betagamma-bc-koszul — bc^! = betagamma (two-generator, dim V=2)
  thm:single-fermion-boson-duality — F^! = Sym^ch(gamma) (single-generator, dim V=1)

CONJECTURED EXTENSION:
  conj:extended-ferm-ghost — derived fermionic system Koszul dual to derived bg-bc

Ground truth references:
  - Central charges: beta_gamma.tex, CLAUDE.md
  - Orthogonality: prop:bc-betagamma-orthogonality
  - Bar cohomology: Master Table (examples_summary.tex)
  - Koszul pairing: conj:extended-ferm-ghost evidence Step 3
  - BRST: def:derived-bg-bc, evidence Step 4

CONVENTIONS:
- Cohomological grading, |d| = +1
- Bar uses desuspension: B(A) = T^c(s^{-1}A-bar, d)
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.extended_ferm_ghost import (
    # Central charges
    bc_central_charge_single,
    betagamma_central_charge_single,
    bc_central_charge,
    betagamma_central_charge,
    central_charge_complementarity,
    # OPE
    derived_fermion_ope,
    derived_fermion_all_products,
    derived_fermion_generator_count,
    derived_fermion_weights,
    # Derived bg-bc
    derived_bg_bc_generator_count,
    derived_bg_bc_generators,
    # Pairing
    koszul_pairing_matrix,
    koszul_pairing_rank,
    # BRST
    brst_differential,
    brst_squares_to_zero,
    # Bar complex
    bc_bar_chain_dim,
    betagamma_bar_chain_dim,
    bc_bar_cohomology,
    betagamma_bar_cohomology,
    BC_BAR_COHOMOLOGY_D1,
    BETAGAMMA_BAR_COHOMOLOGY_D1,
    # Hilbert series
    bc_hilbert_series,
    betagamma_hilbert_series,
    koszul_hilbert_product,
    verify_classical_koszul_relation,
    verify_bg_algebraic_gf,
    # Quadratic duality
    orthogonality_check,
    # Parity and coalgebra
    desuspension_parity_bc,
    desuspension_parity_betagamma,
    coalgebra_type_bc,
    coalgebra_type_betagamma,
    # Characters
    bc_character,
    betagamma_character,
    character_duality_check,
    # Bosonization
    bosonization_vs_koszul,
    # Derived structures
    derived_bg_bc_brst_complex,
    derived_fermion_brst_complex,
    # Summary
    extended_duality_summary,
    # Verification
    verify_central_charges,
    verify_orthogonality,
    verify_derived_fermion_ope,
    verify_pairing_matrix,
)


# ===========================================================================
# Central charge: single pair
# ===========================================================================

class TestSinglePairCentralCharge:
    """Central charge formulas for a single bc or betagamma pair."""

    def test_bc_lambda1(self):
        """c_{bc}(1) = -1 (standard bc ghosts)."""
        assert bc_central_charge_single(1) == -1

    def test_bc_lambda_half(self):
        """c_{bc}(1/2) = -1/2."""
        assert bc_central_charge_single(Rational(1, 2)) == Rational(-1, 2)

    def test_bc_lambda2(self):
        """c_{bc}(2) = -5 (reparametrization ghosts)."""
        assert bc_central_charge_single(2) == -5

    def test_bc_lambda0(self):
        """c_{bc}(0) = -1."""
        assert bc_central_charge_single(0) == -1

    def test_bg_lambda1(self):
        """c_{bg}(1) = 1."""
        assert betagamma_central_charge_single(1) == 1

    def test_bg_lambda_half(self):
        """c_{bg}(1/2) = 1/2."""
        assert betagamma_central_charge_single(Rational(1, 2)) == Rational(1, 2)

    def test_bg_lambda2(self):
        """c_{bg}(2) = 5."""
        assert betagamma_central_charge_single(2) == 5

    def test_bg_lambda0(self):
        """c_{bg}(0) = 1."""
        assert betagamma_central_charge_single(0) == 1

    def test_single_pair_sum_lambda1(self):
        """c_{bc}(1) + c_{bg}(1) = 0."""
        assert bc_central_charge_single(1) + betagamma_central_charge_single(1) == 0

    def test_single_pair_sum_symbolic(self):
        """c_{bc}(lam) + c_{bg}(lam) = 0 for symbolic lambda."""
        lam = Symbol("lambda")
        s = bc_central_charge_single(lam) + betagamma_central_charge_single(lam)
        assert simplify(s) == 0


# ===========================================================================
# Central charge: multi-generator (dim V = d)
# ===========================================================================

class TestMultiGeneratorCentralCharge:
    """Central charges for bc(V) and betagamma(V) at dim V = d."""

    def test_bc_d1_lambda1(self):
        """c_{bc}(d=1, lambda=1) = -1."""
        assert bc_central_charge(1, 1) == -1

    def test_bc_d2_lambda1(self):
        """c_{bc}(d=2, lambda=1) = -2."""
        assert bc_central_charge(2, 1) == -2

    def test_bc_d3_lambda1(self):
        """c_{bc}(d=3, lambda=1) = -3."""
        assert bc_central_charge(3, 1) == -3

    def test_bg_d1_lambda1(self):
        """c_{bg}(d=1, lambda=1) = 1."""
        assert betagamma_central_charge(1, 1) == 1

    def test_bg_d2_lambda1(self):
        """c_{bg}(d=2, lambda=1) = 2."""
        assert betagamma_central_charge(2, 1) == 2

    def test_bg_d3_lambda1(self):
        """c_{bg}(d=3, lambda=1) = 3."""
        assert betagamma_central_charge(3, 1) == 3

    @pytest.mark.parametrize("d", [1, 2, 3, 4, 5])
    def test_complementarity_integer_lambda(self, d):
        """c_{bc}(d, 1) + c_{bg}(d, 1) = 0 for d = 1, ..., 5."""
        assert central_charge_complementarity(d, 1) == 0

    @pytest.mark.parametrize("d", [1, 2, 3])
    def test_complementarity_half_lambda(self, d):
        """c_{bc}(d, 1/2) + c_{bg}(d, 1/2) = 0."""
        assert simplify(central_charge_complementarity(d, Rational(1, 2))) == 0

    @pytest.mark.parametrize("d", [1, 2, 3])
    def test_complementarity_symbolic(self, d):
        """c_{bc}(d, lam) + c_{bg}(d, lam) = 0 for symbolic lambda."""
        lam = Symbol("lambda")
        assert simplify(central_charge_complementarity(d, lam)) == 0

    @pytest.mark.parametrize("d,lam", [(1, 2), (2, 2), (3, 2)])
    def test_complementarity_lambda2(self, d, lam):
        """c_{bc}(d, 2) + c_{bg}(d, 2) = 0."""
        assert central_charge_complementarity(d, lam) == 0

    def test_all_central_charge_checks(self):
        """All checks in verify_central_charges pass."""
        for name, ok in verify_central_charges().items():
            assert ok, f"Central charge check failed: {name}"


# ===========================================================================
# Derived fermion OPE
# ===========================================================================

class TestDerivedFermionOPE:
    """OPE structure of the derived fermionic system (conj:extended-ferm-ghost)."""

    def test_psi0_psi0(self):
        """psi^(0)_{(0)} psi^(0) = |0> (standard fermion self-pairing)."""
        result = derived_fermion_ope(0, 0, 0)
        assert result.get("vac") == 1

    def test_psi1_psim1(self):
        """psi^(1)_{(0)} psi^(-1) = |0>."""
        result = derived_fermion_ope(1, -1, 0)
        assert result.get("vac") == 1

    def test_psim1_psi1(self):
        """psi^(-1)_{(0)} psi^(1) = |0>."""
        result = derived_fermion_ope(-1, 1, 0)
        assert result.get("vac") == 1

    def test_psi0_psi1_vanishes(self):
        """psi^(0)_{(0)} psi^(1) = 0 (i+j = 1 != 0)."""
        assert len(derived_fermion_ope(0, 1, 0)) == 0

    def test_psi0_psim1_vanishes(self):
        """psi^(0)_{(0)} psi^(-1) = 0 (i+j = -1 != 0)."""
        assert len(derived_fermion_ope(0, -1, 0)) == 0

    def test_psi1_psi1_vanishes(self):
        """psi^(1)_{(0)} psi^(1) = 0 (i+j = 2 != 0)."""
        assert len(derived_fermion_ope(1, 1, 0)) == 0

    def test_psim1_psim1_vanishes(self):
        """psi^(-1)_{(0)} psi^(-1) = 0 (i+j = -2 != 0)."""
        assert len(derived_fermion_ope(-1, -1, 0)) == 0

    def test_psi1_psi0_vanishes(self):
        """psi^(1)_{(0)} psi^(0) = 0 (i+j = 1 != 0)."""
        assert len(derived_fermion_ope(1, 0, 0)) == 0

    def test_psim1_psi0_vanishes(self):
        """psi^(-1)_{(0)} psi^(0) = 0 (i+j = -1 != 0)."""
        assert len(derived_fermion_ope(-1, 0, 0)) == 0

    def test_no_higher_poles(self):
        """No singular products at n >= 1 (simple pole only)."""
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for n in [1, 2, 3]:
                    assert len(derived_fermion_ope(i, j, n)) == 0, (
                        f"psi^({i})_({n}) psi^({j}) should be zero"
                    )

    def test_all_products_consistent(self):
        """All products dictionary is consistent with individual calls."""
        products = derived_fermion_all_products()
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i + j == 0:
                    assert (i, j) in products
                    assert 0 in products[(i, j)]
                    assert products[(i, j)][0].get("vac") == 1
                else:
                    assert products[(i, j)] == {}

    def test_all_ope_checks(self):
        """All checks in verify_derived_fermion_ope pass."""
        for name, ok in verify_derived_fermion_ope().items():
            assert ok, f"OPE check failed: {name}"


# ===========================================================================
# Generator counts and weights
# ===========================================================================

class TestGeneratorStructure:
    """Generator counts and conformal weights."""

    def test_derived_fermion_has_3_generators(self):
        """Derived fermionic system has 3 generators."""
        assert derived_fermion_generator_count() == 3

    def test_derived_bg_bc_has_4_generators(self):
        """Derived betagamma-bc system has 4 generators."""
        assert derived_bg_bc_generator_count() == 4

    def test_derived_bg_bc_generator_names(self):
        """Generators are beta, gamma, b, c."""
        gens = derived_bg_bc_generators()
        assert set(gens) == {"beta", "gamma", "b", "c"}

    def test_psi0_weight(self):
        """psi^(0) has weight h = 1/2."""
        weights = derived_fermion_weights()
        assert weights[0] == Rational(1, 2)

    def test_psi1_weight(self):
        """psi^(1) has weight h = 3/2."""
        weights = derived_fermion_weights()
        assert weights[1] == Rational(3, 2)

    def test_psim1_weight(self):
        """psi^(-1) has weight h = -1/2."""
        weights = derived_fermion_weights()
        assert weights[-1] == Rational(-1, 2)

    def test_weight_spacing(self):
        """Weights are evenly spaced by 1."""
        weights = derived_fermion_weights()
        assert weights[1] - weights[0] == 1
        assert weights[0] - weights[-1] == 1


# ===========================================================================
# Koszul pairing matrix
# ===========================================================================

class TestKoszulPairingMatrix:
    """Koszul pairing matrix from evidence Step 3."""

    def test_psi0_gamma(self):
        """<psi^(0), gamma> = 1."""
        pairing = koszul_pairing_matrix()
        assert pairing[(0, "gamma")] == 1

    def test_psi1_c(self):
        """<psi^(1), c> = 1."""
        pairing = koszul_pairing_matrix()
        assert pairing[(1, "c")] == 1

    def test_psim1_b(self):
        """<psi^(-1), b> = 1."""
        pairing = koszul_pairing_matrix()
        assert pairing[(-1, "b")] == 1

    def test_psi0_beta_zero(self):
        """<psi^(0), beta> = 0."""
        pairing = koszul_pairing_matrix()
        assert pairing[(0, "beta")] == 0

    def test_psi0_b_zero(self):
        """<psi^(0), b> = 0."""
        pairing = koszul_pairing_matrix()
        assert pairing[(0, "b")] == 0

    def test_psi0_c_zero(self):
        """<psi^(0), c> = 0."""
        pairing = koszul_pairing_matrix()
        assert pairing[(0, "c")] == 0

    def test_psi1_beta_zero(self):
        """<psi^(1), beta> = 0."""
        pairing = koszul_pairing_matrix()
        assert pairing[(1, "beta")] == 0

    def test_psi1_gamma_zero(self):
        """<psi^(1), gamma> = 0."""
        pairing = koszul_pairing_matrix()
        assert pairing[(1, "gamma")] == 0

    def test_psi1_b_zero(self):
        """<psi^(1), b> = 0."""
        pairing = koszul_pairing_matrix()
        assert pairing[(1, "b")] == 0

    def test_psim1_beta_zero(self):
        """<psi^(-1), beta> = 0."""
        pairing = koszul_pairing_matrix()
        assert pairing[(-1, "beta")] == 0

    def test_psim1_gamma_zero(self):
        """<psi^(-1), gamma> = 0."""
        pairing = koszul_pairing_matrix()
        assert pairing[(-1, "gamma")] == 0

    def test_psim1_c_zero(self):
        """<psi^(-1), c> = 0."""
        pairing = koszul_pairing_matrix()
        assert pairing[(-1, "c")] == 0

    def test_rank(self):
        """Pairing matrix has rank 3 (full row rank)."""
        assert koszul_pairing_rank() == 3

    def test_exactly_3_nonzero_entries(self):
        """Exactly 3 nonzero entries in the pairing matrix."""
        pairing = koszul_pairing_matrix()
        nonzero = sum(1 for v in pairing.values() if v != 0)
        assert nonzero == 3

    def test_each_fermion_pairs_uniquely(self):
        """Each fermionic generator pairs with exactly one bg-bc generator."""
        pairing = koszul_pairing_matrix()
        for i in [-1, 0, 1]:
            partners = [g for g in ["beta", "gamma", "b", "c"]
                        if pairing[(i, g)] != 0]
            assert len(partners) == 1, f"psi^({i}) pairs with {partners}"

    def test_all_pairing_checks(self):
        """All checks in verify_pairing_matrix pass."""
        for name, ok in verify_pairing_matrix().items():
            assert ok, f"Pairing check failed: {name}"


# ===========================================================================
# BRST differential
# ===========================================================================

class TestBRSTDifferential:
    """BRST differential on the derived fermionic system."""

    def test_Q_psim1_is_zero(self):
        """Q psi^(-1) = 0 (coefficient = 0)."""
        result = brst_differential(-1)
        assert result["is_zero"] is True
        assert result["coefficient"] == 0

    def test_Q_psi0_is_psi1(self):
        """Q psi^(0) = psi^(1) (coefficient = 1)."""
        result = brst_differential(0)
        assert result["is_zero"] is False
        assert result["coefficient"] == 1
        assert result["target"] == 1

    def test_Q_psi1_is_zero(self):
        """Q psi^(1) = 0 (truncation: psi^(2) not in system)."""
        result = brst_differential(1)
        assert result["is_zero"] is True

    def test_Q_squared_is_zero(self):
        """Q^2 = 0 on the derived fermionic system."""
        assert brst_squares_to_zero() is True

    def test_differential_is_chain_complex(self):
        """The BRST differential gives a (degenerate) chain complex."""
        # psi^(-1) --Q=0--> X --Q=id--> psi^(1) --Q=0--> X
        d_m1 = brst_differential(-1)
        d_0 = brst_differential(0)
        d_1 = brst_differential(1)

        # Q psi^(-1) = 0
        assert d_m1["is_zero"]
        # Q psi^(0) = psi^(1), Q psi^(1) = 0, so Q^2 psi^(0) = 0
        assert d_0["target"] == 1
        assert d_1["is_zero"]


# ===========================================================================
# Bar complex chain dimensions
# ===========================================================================

class TestBarChainDimensions:
    """Bar complex chain space dimensions for bc(V) and betagamma(V)."""

    def test_bc_d1_n1(self):
        """bc(d=1) bar degree 1: chain dim = 2."""
        assert bc_bar_chain_dim(1, 1) == 2

    def test_bc_d1_n2(self):
        """bc(d=1) bar degree 2: chain dim = 6."""
        assert bc_bar_chain_dim(1, 2) == 6

    def test_bc_d1_n3(self):
        """bc(d=1) bar degree 3: chain dim = 18."""
        assert bc_bar_chain_dim(1, 3) == 18

    def test_bc_d1_formula(self):
        """bc(d=1) chain dim = 2*3^{n-1} for n = 1,...,5."""
        for n in range(1, 6):
            assert bc_bar_chain_dim(1, n) == 2 * 3**(n - 1)

    def test_bg_d1_equals_bc_d1(self):
        """betagamma(d=1) chain dims equal bc(d=1) chain dims."""
        for n in range(1, 6):
            assert betagamma_bar_chain_dim(1, n) == bc_bar_chain_dim(1, n)

    def test_bc_d2_n1(self):
        """bc(d=2) bar degree 1: chain dim = 4."""
        assert bc_bar_chain_dim(2, 1) == 4

    def test_bc_d2_n2(self):
        """bc(d=2) bar degree 2: chain dim = 20."""
        assert bc_bar_chain_dim(2, 2) == 20

    def test_bc_d3_n1(self):
        """bc(d=3) bar degree 1: chain dim = 6."""
        assert bc_bar_chain_dim(3, 1) == 6

    def test_chain_dim_zero_at_n0(self):
        """Chain dim is 0 at bar degree 0 (by convention)."""
        for d in [1, 2, 3]:
            assert bc_bar_chain_dim(d, 0) == 0


# ===========================================================================
# Bar cohomology (proved for d=1)
# ===========================================================================

class TestBarCohomologyD1:
    """Bar cohomology at dim V = 1 (proved case)."""

    def test_bc_formula(self):
        """bc bar cohomology: H^n = 2^n - n + 1 for n = 1,...,8."""
        for n in range(1, 9):
            assert bc_bar_cohomology(1, n) == 2**n - n + 1

    def test_bc_known_values(self):
        """bc bar cohomology matches known table."""
        expected = {1: 2, 2: 3, 3: 6, 4: 13, 5: 28, 6: 59, 7: 122, 8: 249}
        for n, exp in expected.items():
            assert bc_bar_cohomology(1, n) == exp

    def test_bg_known_values(self):
        """betagamma bar cohomology matches known table."""
        expected = {1: 2, 2: 4, 3: 10, 4: 26, 5: 70, 6: 192, 7: 534, 8: 1500}
        for n, exp in expected.items():
            assert betagamma_bar_cohomology(1, n) == exp

    def test_bc_matches_stored_data(self):
        """bc bar cohomology matches BC_BAR_COHOMOLOGY_D1."""
        for n, exp in BC_BAR_COHOMOLOGY_D1.items():
            assert bc_bar_cohomology(1, n) == exp

    def test_bg_matches_stored_data(self):
        """betagamma bar cohomology matches BETAGAMMA_BAR_COHOMOLOGY_D1."""
        for n, exp in BETAGAMMA_BAR_COHOMOLOGY_D1.items():
            assert betagamma_bar_cohomology(1, n) == exp

    def test_bc_d2_is_none(self):
        """bc bar cohomology at d=2 returns None (not yet computed)."""
        assert bc_bar_cohomology(2, 1) is None

    def test_bg_d2_is_none(self):
        """betagamma bar cohomology at d=2 returns None (not yet computed)."""
        assert betagamma_bar_cohomology(2, 1) is None


# ===========================================================================
# Hilbert series and Koszul relation
# ===========================================================================

class TestHilbertSeries:
    """Hilbert series and Koszul duality relations."""

    def test_bc_hilbert_starts_with_1(self):
        """bc Hilbert series starts with h_0 = 1."""
        h = bc_hilbert_series(5)
        assert h[0] == 1

    def test_bc_hilbert_correct_values(self):
        """bc Hilbert series: [1, 2, 3, 6, 13, 28]."""
        h = bc_hilbert_series(5)
        assert h == [1, 2, 3, 6, 13, 28]

    def test_bg_hilbert_starts_with_1(self):
        """betagamma Hilbert series starts with h_0 = 1."""
        h = betagamma_hilbert_series(5)
        assert h[0] == 1

    def test_bg_hilbert_correct_values(self):
        """betagamma Hilbert series: [1, 2, 4, 10, 26, 70]."""
        h = betagamma_hilbert_series(5)
        assert h == [1, 2, 4, 10, 26, 70]

    def test_classical_koszul_relation_fails(self):
        """Classical Koszul relation H_bc(t)*H_bg(-t) = 1 does NOT hold.

        This is expected: chiral bar cohomology has OS algebra structure
        that modifies the classical Koszul relation.
        """
        result = verify_classical_koszul_relation(6)
        assert result["is_classical_koszul"] is False

    def test_classical_koszul_product_leading_term(self):
        """Leading term of H_bc(t)*H_bg(-t) is 1."""
        result = verify_classical_koszul_relation(6)
        assert result["product"][0] == 1

    def test_classical_koszul_product_subleading_nonzero(self):
        """Subleading terms of H_bc(t)*H_bg(-t) are nonzero."""
        result = verify_classical_koszul_relation(6)
        # At least one higher coefficient should be nonzero
        assert any(result["product"][k] != 0 for k in range(1, len(result["product"])))


class TestAlgebraicGF:
    """Algebraic generating function verification for betagamma."""

    def test_bg_gf_is_algebraic(self):
        """betagamma bar GF satisfies P^2 = (1+x)/(1-3x)."""
        result = verify_bg_algebraic_gf(7)
        assert result["matches"]

    def test_bg_p_squared_at_degree0(self):
        """P^2 coefficient at degree 0 is 1."""
        result = verify_bg_algebraic_gf(5)
        assert result["p_squared"][0] == 1

    def test_bg_p_squared_at_degree1(self):
        """P^2 coefficient at degree 1 is 4 = 3 + 1."""
        result = verify_bg_algebraic_gf(5)
        assert result["p_squared"][1] == 4

    def test_bg_p_squared_at_degree2(self):
        """P^2 coefficient at degree 2 is 12 = 9 + 3."""
        result = verify_bg_algebraic_gf(5)
        assert result["p_squared"][2] == 12

    def test_bg_target_formula(self):
        """Target coefficients: (1+x)/(1-3x) = 1 + 4x + 12x^2 + 36x^3 + ..."""
        result = verify_bg_algebraic_gf(5)
        expected_target = [1, 4, 12, 36, 108, 324]
        assert result["target"][:6] == expected_target


# ===========================================================================
# Quadratic relation orthogonality
# ===========================================================================

class TestQuadraticOrthogonality:
    """Quadratic relation orthogonality R_bc perp R_bg."""

    @pytest.mark.parametrize("d", [1, 2, 3, 4, 5])
    def test_orthogonality(self, d):
        """R_bc perp R_bg at dim V = d."""
        check = orthogonality_check(d)
        assert check["orthogonal"]

    def test_per_pair_inner_product_is_zero(self):
        """Each pair contributes 0 to the inner product."""
        check = orthogonality_check(1)
        assert check["per_pair_inner_product"] == 0

    def test_d1_proved(self):
        """Orthogonality at d=1 is proved (prop:bc-betagamma-orthogonality)."""
        check = orthogonality_check(1)
        assert check["proved_for_d1"] is True

    def test_d2_conjectured(self):
        """Orthogonality at d=2 is conjectured (extends beyond proved case)."""
        check = orthogonality_check(2)
        assert check["conjectured_for_d_geq_2"] is True

    def test_total_inner_product_is_zero(self):
        """Total inner product is 0 for all d."""
        for d in range(1, 10):
            check = orthogonality_check(d)
            assert check["total_inner_product"] == 0

    def test_all_orthogonality_checks(self):
        """All checks in verify_orthogonality pass."""
        for name, ok in verify_orthogonality().items():
            assert ok, f"Orthogonality check failed: {name}"


# ===========================================================================
# Desuspension parity and coalgebra type
# ===========================================================================

class TestParityAndCoalgebra:
    """Desuspension parity and bar coalgebra type."""

    def test_bc_desuspension_even(self):
        """bc generators desuspend to EVEN parity."""
        assert desuspension_parity_bc() == "even"

    def test_bg_desuspension_odd(self):
        """betagamma generators desuspend to ODD parity."""
        assert desuspension_parity_betagamma() == "odd"

    def test_bc_coalgebra_symmetric(self):
        """B(bc) is a SYMMETRIC coalgebra (even desuspension -> symmetric)."""
        assert coalgebra_type_bc() == "symmetric"

    def test_bg_coalgebra_exterior(self):
        """B(betagamma) is an EXTERIOR coalgebra (odd desuspension -> exterior)."""
        assert coalgebra_type_betagamma() == "exterior"

    def test_statistics_exchange(self):
        """Koszul duality exchanges statistics: symmetric <-> exterior."""
        # bc (fermionic) -> symmetric coalgebra -> cobar gives commuting gens -> betagamma
        # betagamma (bosonic) -> exterior coalgebra -> cobar gives anticommuting gens -> bc
        assert coalgebra_type_bc() == "symmetric"  # -> bosonic dual
        assert coalgebra_type_betagamma() == "exterior"  # -> fermionic dual


# ===========================================================================
# Character-level verification
# ===========================================================================

class TestCharacters:
    """Character (graded dimension) computations."""

    def test_bc_d1_level0(self):
        """bc(d=1) Fock space: dim at level 0 is 1 (vacuum)."""
        ch = bc_character(1, 5)
        assert ch[0] == 1

    def test_bc_d1_level1(self):
        """bc(d=1) Fock space: dim at level 1 is 2."""
        ch = bc_character(1, 5)
        assert ch[1] == 2

    def test_bc_d1_level2(self):
        """bc(d=1) Fock space: dim at level 2 is 3."""
        ch = bc_character(1, 5)
        assert ch[2] == 3

    def test_bg_d1_level0(self):
        """betagamma(d=1) Fock space: dim at level 0 is 1."""
        ch = betagamma_character(1, 5)
        assert ch[0] == 1

    def test_bg_d1_level1(self):
        """betagamma(d=1) Fock space: dim at level 1 is 2."""
        ch = betagamma_character(1, 5)
        assert ch[1] == 2

    def test_bg_d1_level2(self):
        """betagamma(d=1) Fock space: dim at level 2 is 5."""
        ch = betagamma_character(1, 5)
        # (1 + q + q^2 + ...)^2 = 1 + 2q + 3q^2 + 4q^3 + 5q^4 + ...
        # But 1/(1-q)^2 = sum (n+1)q^n, and we need product over n >= 1.
        # 1/(1-q)^2 * 1/(1-q^2)^2 * ... => level 2: partitions of 2 into parts
        # with multiplicity <= 2 ... Actually this is prod_{n>=1} 1/(1-q^n)^2.
        # Level 2: 2 from q+q, 1 from q^2, plus cross terms -> 5.
        assert ch[2] == 5

    def test_bc_d2_grows_faster(self):
        """bc(d=2) Fock dims grow faster than bc(d=1)."""
        ch1 = bc_character(1, 4)
        ch2 = bc_character(2, 4)
        # At higher levels, d=2 should have more states
        assert ch2[2] > ch1[2]

    def test_bg_d2_grows_faster(self):
        """betagamma(d=2) Fock dims grow faster than betagamma(d=1)."""
        ch1 = betagamma_character(1, 4)
        ch2 = betagamma_character(2, 4)
        assert ch2[2] > ch1[2]

    def test_character_duality_check_runs(self):
        """Character duality check executes without error."""
        result = character_duality_check(1, 4)
        assert "ch_bc" in result
        assert "ch_bg" in result
        assert "product" in result


# ===========================================================================
# Bosonization vs Koszul duality
# ===========================================================================

class TestBosonizationDistinction:
    """Bosonization != Koszul duality (CLAUDE.md critical pitfall)."""

    def test_bosonization_changes_generators(self):
        """Bosonization: bc (2 gens) -> Heisenberg (1 gen)."""
        bvk = bosonization_vs_koszul()
        assert bvk["bosonization"]["preserves_generators"] is False

    def test_koszul_preserves_generators(self):
        """Koszul duality: bc (2 gens) -> betagamma (2 gens)."""
        bvk = bosonization_vs_koszul()
        assert bvk["koszul_duality"]["preserves_generators"] is True

    def test_bosonization_not_koszul(self):
        """Bosonization is NOT Koszul duality."""
        bvk = bosonization_vs_koszul()
        assert bvk["bosonization"]["is_koszul_duality"] is False

    def test_koszul_is_koszul(self):
        """bc-betagamma IS Koszul duality."""
        bvk = bosonization_vs_koszul()
        assert bvk["koszul_duality"]["is_koszul_duality"] is True

    def test_different_targets(self):
        """Bosonization and Koszul duality have different targets."""
        bvk = bosonization_vs_koszul()
        assert bvk["bosonization"]["target"] != bvk["koszul_duality"]["target"]

    def test_summary_statement(self):
        """Summary correctly states bosonization != Koszul duality."""
        bvk = bosonization_vs_koszul()
        assert "!=" in bvk["summary"]


# ===========================================================================
# Derived structure
# ===========================================================================

class TestDerivedStructure:
    """Derived betagamma-bc and fermionic BRST complexes."""

    def test_bg_bc_complex_structure(self):
        """Derived bg-bc complex has correct ghost number assignments."""
        cx = derived_bg_bc_brst_complex()
        assert cx["ghost_0"] == "betagamma"
        assert cx["ghost_1"] == "bc"

    def test_bg_bc_statistics_alternation(self):
        """Statistics alternate: bosonic, fermionic, bosonic."""
        cx = derived_bg_bc_brst_complex()
        assert cx["statistics_pattern"] == ["bosonic", "fermionic", "bosonic"]

    def test_bg_bc_total_generators_at_truncation(self):
        """Truncated derived bg-bc has 4 generators."""
        cx = derived_bg_bc_brst_complex()
        assert cx["total_generators_at_truncation_1"] == 4

    def test_fermion_complex_weights(self):
        """Derived fermion complex has correct weights."""
        fc = derived_fermion_brst_complex()
        assert fc["weights"][-1] == Rational(-1, 2)
        assert fc["weights"][0] == Rational(1, 2)
        assert fc["weights"][1] == Rational(3, 2)

    def test_fermion_complex_differential_coefficients(self):
        """Differential coefficients: Q psi^(k) has coefficient k+1."""
        fc = derived_fermion_brst_complex()
        assert fc["differential_coefficients"][-1] == 0
        assert fc["differential_coefficients"][0] == 1
        assert fc["differential_coefficients"][1] == 2

    def test_generator_count_mismatch(self):
        """3 fermionic gens vs 4 bg-bc gens (rank 3 pairing)."""
        assert derived_fermion_generator_count() == 3
        assert derived_bg_bc_generator_count() == 4
        assert koszul_pairing_rank() == 3


# ===========================================================================
# Extended duality summary
# ===========================================================================

class TestExtendedDualitySummary:
    """Summary of proved vs conjectured statements."""

    def test_has_proved_items(self):
        """Summary lists proved items."""
        s = extended_duality_summary()
        assert len(s["proved"]) >= 4

    def test_has_conjectured_items(self):
        """Summary lists conjectured items."""
        s = extended_duality_summary()
        assert len(s["conjectured"]) >= 3

    def test_correct_conjecture_label(self):
        """Summary references correct conjecture label."""
        s = extended_duality_summary()
        assert s["conjecture_label"] == "conj:extended-ferm-ghost"

    def test_scope_remark(self):
        """Summary references correct scope remark."""
        s = extended_duality_summary()
        assert s["scope_remark"] == "rem:extended-ferm-ghost-scope"

    def test_category(self):
        """Conjecture is in derived/super extension flank."""
        s = extended_duality_summary()
        assert "derived" in s["category"]


# ===========================================================================
# Cross-module consistency
# ===========================================================================

class TestCrossModuleConsistency:
    """Cross-checks with existing compute modules."""

    def test_bc_dims_match_betagamma_bar(self):
        """bc bar cohomology matches BC_BAR_COHOMOLOGY in betagamma_bar.py."""
        from compute.lib.betagamma_bar import BC_BAR_COHOMOLOGY
        for n in range(1, 9):
            assert bc_bar_cohomology(1, n) == BC_BAR_COHOMOLOGY[n], (
                f"bc H^{n}: extended_ferm_ghost={bc_bar_cohomology(1, n)}, "
                f"betagamma_bar={BC_BAR_COHOMOLOGY[n]}"
            )

    def test_bg_dims_match_betagamma_bar(self):
        """betagamma bar cohomology matches BETAGAMMA_BAR_COHOMOLOGY."""
        from compute.lib.betagamma_bar import BETAGAMMA_BAR_COHOMOLOGY
        for n in range(1, 9):
            assert betagamma_bar_cohomology(1, n) == BETAGAMMA_BAR_COHOMOLOGY[n], (
                f"bg H^{n}: extended_ferm_ghost={betagamma_bar_cohomology(1, n)}, "
                f"betagamma_bar={BETAGAMMA_BAR_COHOMOLOGY[n]}"
            )

    def test_bc_dims_match_bar_complex(self):
        """bc bar cohomology matches KNOWN_BAR_DIMS in bar_complex.py."""
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        for n in range(1, 9):
            assert bc_bar_cohomology(1, n) == KNOWN_BAR_DIMS["bc"][n]

    def test_bg_dims_match_bar_complex(self):
        """betagamma bar cohomology matches KNOWN_BAR_DIMS in bar_complex.py."""
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        for n in range(1, 9):
            assert betagamma_bar_cohomology(1, n) == KNOWN_BAR_DIMS["beta_gamma"][n]

    def test_bc_chain_dim_d1_matches_betagamma_bar(self):
        """bc chain dim at d=1 matches betagamma_bar.betagamma_chain_type_count."""
        from compute.lib.betagamma_bar import betagamma_chain_type_count
        for n in range(1, 6):
            assert bc_bar_chain_dim(1, n) == betagamma_chain_type_count(n)

    def test_central_charge_matches_independent_conjectures(self):
        """Central charges match independent_conjectures.py."""
        from compute.lib.independent_conjectures import (
            bc_central_charge as ic_bc,
            beta_gamma_central_charge as ic_bg,
        )
        for lam in [0, 1, 2]:
            assert bc_central_charge_single(lam) == ic_bc(lam), (
                f"bc c({lam}): ours={bc_central_charge_single(lam)}, ic={ic_bc(lam)}"
            )
            assert betagamma_central_charge_single(lam) == ic_bg(lam), (
                f"bg c({lam}): ours={betagamma_central_charge_single(lam)}, ic={ic_bg(lam)}"
            )

    def test_koszul_pair_involution(self):
        """bc^! = betagamma and betagamma^! = bc (from koszul_pairs.py)."""
        from compute.lib.koszul_pairs import KOSZUL_PAIRS
        pair = KOSZUL_PAIRS["beta_gamma_bc"]
        assert pair["involution"] is True
        assert pair["A"] == "beta_gamma"
        assert pair["A_dual"] == "bc_ghosts"

    def test_bosonization_flagged_as_error(self):
        """Bosonization != Koszul is correctly flagged in koszul_pairs.py."""
        from compute.lib.koszul_pairs import COMMON_ERRORS
        assert "bosonization_is_koszul" in COMMON_ERRORS
        assert "WRONG" in COMMON_ERRORS["bosonization_is_koszul"]["truth"]
