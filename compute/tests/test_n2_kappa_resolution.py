"""Tests for N=2 superconformal kappa resolution.

Verifies that kappa(N=2) = (6-c)/(2(3-c)) = (k+4)/4 (coset formula)
and NOT 7c/6 (naive Zamolodchikov sum).

30+ tests covering:
  - Coset decomposition consistency (6 tests)
  - Complementarity sum = 1 (6 tests)
  - Additive duality c + c' = 6 (4 tests)
  - Discrepancy analysis (4 tests)
  - sl(2) naive failure (4 tests)
  - F_1 values (5 tests)
  - Anomaly ratio (3 tests)
  - Self-consistency (2 tests)
"""

import pytest
from sympy import Rational, simplify, Symbol

from compute.lib.n2_kappa_resolution import (
    F1_values,
    coset_decomposition,
    complementarity_sum,
    discrepancy,
    discrepancy_symbolic,
    k_from_c,
    kappa_n2_correct,
    kappa_n2_from_k,
    kappa_n2_wrong,
    kappa_sl2,
    kappa_fermion_pair,
    kappa_u1_denominator,
    n2_central_charge,
    n2_koszul_dual_c,
    n2_koszul_dual_level,
    sigma_n2,
    sl2_naive_vs_correct,
    verify_resolution,
    wrong_duality_check,
)


# =========================================================================
# Coset decomposition consistency
# =========================================================================

class TestCosetDecomposition:
    """Verify kappa = kappa(sl2) + kappa(ferm) - kappa(U1)."""

    @pytest.mark.parametrize("k_val", [1, 2, 4, 10, 100])
    def test_coset_matches_k_formula(self, k_val):
        d = coset_decomposition(k_val)
        assert d['coset_matches_k'], f"Coset sum disagrees with (k+4)/4 at k={k_val}"

    @pytest.mark.parametrize("k_val", [1, 2, 4, 10, 100])
    def test_coset_matches_c_formula(self, k_val):
        d = coset_decomposition(k_val)
        assert d['coset_matches_c'], f"Coset sum disagrees with (6-c)/(2(3-c)) at k={k_val}"

    def test_naive_disagrees(self):
        """The naive formula 7c/6 disagrees with the coset formula at k=1."""
        d = coset_decomposition(1)
        assert not d['naive_agrees'], "Naive formula should NOT agree with coset"

    def test_constituent_kappas(self):
        """Verify each constituent kappa independently."""
        # sl(2) at k=2: kappa = 3*4/4 = 3
        assert kappa_sl2(2) == Rational(3)
        # Fermion pair: kappa = 1/2
        assert kappa_fermion_pair() == Rational(1, 2)
        # U(1) at k=2: level = 2/2+1 = 2, kappa = 2
        assert kappa_u1_denominator(2) == Rational(2)
        # Total: 3 + 1/2 - 2 = 3/2. And (2+4)/4 = 3/2.
        total = kappa_sl2(2) + kappa_fermion_pair() - kappa_u1_denominator(2)
        assert total == Rational(3, 2)

    def test_central_charge(self):
        """c = 3k/(k+2) at specific values."""
        assert n2_central_charge(1) == Rational(1)
        assert n2_central_charge(2) == Rational(3, 2)
        assert n2_central_charge(10) == Rational(5, 2)

    def test_k_from_c_inverse(self):
        """k = 2c/(3-c) is inverse of c = 3k/(k+2)."""
        for kv in [1, 2, 5, 10]:
            c_v = n2_central_charge(kv)
            k_back = k_from_c(c_v)
            assert simplify(k_back - kv) == 0


# =========================================================================
# Complementarity sum
# =========================================================================

class TestComplementarity:
    """Verify kappa(c) + kappa(6-c) = 1."""

    @pytest.mark.parametrize("k_val", [1, 2, 5, 10, -1, -3])
    def test_complementarity_from_k(self, k_val):
        comp = complementarity_sum(k_val=k_val)
        assert comp['sum'] == 1, f"kappa + kappa' != 1 at k={k_val}: got {comp['sum']}"

    @pytest.mark.parametrize("c_val", [1, 2, Rational(3, 2), Rational(5, 2), 5])
    def test_complementarity_from_c(self, c_val):
        comp = complementarity_sum(c_val=c_val)
        assert comp['sum'] == 1, f"kappa + kappa' != 1 at c={c_val}: got {comp['sum']}"

    def test_complementarity_symbolic(self):
        """Symbolic proof that kappa + kappa' = 1."""
        comp = complementarity_sum()
        assert comp['sum'] == 1

    def test_wrong_duality_different_constant(self):
        """c' = 9/c with correct kappa gives sum = 3/2, not 1.

        The correct duality c' = 6-c gives kappa + kappa' = 1.
        The wrong duality c' = 9/c gives kappa + kappa' = 3/2.
        Both are constant, but only the sl(2) duality (sum=1) is correct.
        """
        s_wrong = wrong_duality_check(c_val=1)['sum']
        assert s_wrong == Rational(3, 2), f"Wrong duality sum should be 3/2, got {s_wrong}"
        # Contrast with correct duality:
        s_correct = complementarity_sum(c_val=1)['sum']
        assert s_correct == 1, f"Correct duality sum should be 1, got {s_correct}"
        assert s_wrong != s_correct


# =========================================================================
# Additive duality c + c' = 6
# =========================================================================

class TestDuality:
    """Verify the correct Koszul duality is c' = 6-c."""

    @pytest.mark.parametrize("k_val", [1, 2, 10, -1])
    def test_additive_duality(self, k_val):
        c_v = n2_central_charge(k_val)
        c_dual = n2_koszul_dual_c(c_v)
        assert simplify(c_v + c_dual - 6) == 0

    def test_dual_level(self):
        """k' = -k-4 at specific values."""
        assert n2_koszul_dual_level(1) == Rational(-5)
        assert n2_koszul_dual_level(2) == Rational(-6)
        assert n2_koszul_dual_level(-4) == Rational(0)

    def test_dual_c_at_k1(self):
        """At k=1: c=1, c'=5. Check c' = 6-1 = 5."""
        c_v = n2_central_charge(1)
        c_dual = n2_koszul_dual_c(c_v)
        assert c_dual == 5

    def test_critical_level_kappa_zero(self):
        """At k=-4 (critical level of sl(2)): kappa = 0."""
        assert kappa_n2_from_k(-4) == 0


# =========================================================================
# Discrepancy analysis
# =========================================================================

class TestDiscrepancy:
    """Verify that 7c/6 disagrees with (6-c)/(2(3-c)) at all c != 0."""

    def test_discrepancy_at_c1(self):
        d = discrepancy(1)
        assert d['kappa_correct'] == Rational(5, 4)
        assert d['kappa_wrong'] == Rational(7, 6)
        assert d['difference'] != 0

    def test_discrepancy_at_c3_2(self):
        d = discrepancy(Rational(3, 2))
        assert d['kappa_correct'] == Rational(3, 2)
        assert d['kappa_wrong'] == Rational(7, 4)
        assert d['difference'] == Rational(3, 2) - Rational(7, 4)

    def test_discrepancy_at_c5_2(self):
        d = discrepancy(Rational(5, 2))
        assert d['kappa_correct'] == Rational(7, 2)
        assert d['kappa_wrong'] == Rational(35, 12)

    def test_discrepancy_symbolic(self):
        d = discrepancy_symbolic()
        # difference = (6-c)/(2(3-c)) - 7c/6 should be nonzero symbolically
        # Evaluated at c=1: (5/4 - 7/6) = (15-14)/12 = 1/12
        diff_at_1 = d['difference'].subs(Symbol('c'), 1)
        assert simplify(diff_at_1) == Rational(1, 12)


# =========================================================================
# sl(2) naive formula failure
# =========================================================================

class TestSl2NaiveFailure:
    """The naive sum of OPE coefficients fails even for sl(2)_k."""

    @pytest.mark.parametrize("k_val,expected_kappa", [
        (1, Rational(9, 4)),   # 3*(1+2)/4
        (4, Rational(9, 2)),   # 3*(4+2)/4
        (10, Rational(9)),     # 3*(10+2)/4
    ])
    def test_sl2_correct_kappa(self, k_val, expected_kappa):
        assert kappa_sl2(k_val) == expected_kappa

    @pytest.mark.parametrize("k_val", [1, 4, 10])
    def test_sl2_naive_wrong(self, k_val):
        result = sl2_naive_vs_correct(k_val)
        assert not result['agree'], f"Naive should fail at k={k_val}"

    def test_sl2_naive_agrees_at_k2_coincidence(self):
        """At k=2 = h^v(sl_2), the naive formula accidentally agrees."""
        result = sl2_naive_vs_correct(2)
        assert result['agree'], "At k=h^v, naive formula happens to agree"

    def test_quantum_correction(self):
        """Quantum correction = 3(2-k)/4."""
        for kv in [1, 3, 5]:
            result = sl2_naive_vs_correct(kv)
            expected = Rational(3) * (2 - kv) / 4
            assert result['quantum_correction'] == expected


# =========================================================================
# F_1 values
# =========================================================================

class TestF1:
    """F_1 = kappa/24 at physically important central charges."""

    def test_f1_c1(self):
        """c=1: F_1 = 5/96."""
        vals = F1_values()
        assert vals['c=1 (k=1)']['F_1_correct'] == Rational(5, 96)

    def test_f1_c3_2(self):
        """c=3/2: F_1 = 1/16."""
        vals = F1_values()
        assert vals['c=3/2 (k=2)']['F_1_correct'] == Rational(1, 16)

    def test_f1_c5_2(self):
        """c=5/2: F_1 = 7/48."""
        vals = F1_values()
        assert vals['c=5/2 (k=10)']['F_1_correct'] == Rational(7, 48)

    def test_f1_dual_pair_c1_c5(self):
        """F_1(c=1) + F_1(c=5) = 1/24 (from kappa + kappa' = 1)."""
        vals = F1_values()
        f1_c1 = vals['c=1 (k=1)']['F_1_correct']
        f1_c5 = vals['c=5 (dual of c=1)']['F_1_correct']
        assert f1_c1 + f1_c5 == Rational(1, 24)

    def test_f1_critical(self):
        """At critical c=6: kappa = 0, F_1 = 0."""
        vals = F1_values()
        assert vals['c=6 (critical)']['F_1_correct'] == 0


# =========================================================================
# Anomaly ratio
# =========================================================================

class TestAnomalyRatio:
    """sigma = kappa/c is NOT constant for the N=2 SCA."""

    def test_sigma_c1(self):
        assert sigma_n2(1) == Rational(5, 4)

    def test_sigma_c3_2(self):
        assert sigma_n2(Rational(3, 2)) == Rational(1)

    def test_sigma_not_constant(self):
        """sigma varies with c (coset, not principal W-algebra)."""
        s1 = sigma_n2(1)
        s2 = sigma_n2(2)
        assert s1 != s2


# =========================================================================
# Self-consistency
# =========================================================================

class TestSelfConsistency:
    """Run the full verification suite."""

    def test_all_checks_pass(self):
        results = verify_resolution()
        for name, passed in results.items():
            assert passed, f"Check failed: {name}"

    def test_kappa_correct_vs_free_field_module(self):
        """Cross-check against n2_free_field_shadow.py kappa formula."""
        from compute.lib.n2_free_field_shadow import kappa_n2 as kappa_ff
        for c_v in [1, Rational(3, 2), Rational(5, 2), 5]:
            assert kappa_n2_correct(c_v) == kappa_ff(c_v), \
                f"Resolution disagrees with free-field module at c={c_v}"
