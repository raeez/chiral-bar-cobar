r"""Tests for the N=2 SCA chiral bar complex analysis.

30+ tests verifying:
  1. OPE data consistency (3 paths)
  2. Generator weights and parities
  3. CE differential computation
  4. Chiral bar H^2 analysis
  5. Koszulness evidence assessment
  6. Cross-checks with n2_superconformal_shadow.py

References:
    n2_sca_chiral_bar_engine.py
    n2_superconformal_shadow.py
    Manuscript: chiral_koszul_pairs.tex
"""

import pytest
import unittest

from sympy import Rational, Symbol

from compute.lib.n2_sca_chiral_bar_engine import (
    GENERATORS,
    GEN_WEIGHT,
    GEN_PARITY,
    n2_ope_data,
    max_pole_order,
    bar_basis_at_weight,
    bar_dim_at_weight,
    ce_h2_at_weight,
    chiral_bar_h2_numerical,
    n2_sca_koszulness_analysis,
    koszulness_evidence_summary,
    _compute_h2_at_weight_simplified,
)

c = Symbol('c')


# =========================================================================
# 1. Generator data (3 paths)
# =========================================================================

class TestGeneratorData(unittest.TestCase):
    """Generator weights and parities for the N=2 SCA."""

    def test_four_generators(self):
        """Path 1: exactly 4 generators."""
        self.assertEqual(len(GENERATORS), 4)

    def test_generator_names(self):
        """Path 2: correct generator names."""
        self.assertEqual(set(GENERATORS), {'T', 'J', 'G+', 'G-'})

    def test_weights(self):
        """Path 3: correct conformal weights."""
        self.assertEqual(GEN_WEIGHT['T'], 2)
        self.assertEqual(GEN_WEIGHT['J'], 1)
        self.assertEqual(GEN_WEIGHT['G+'], Rational(3, 2))
        self.assertEqual(GEN_WEIGHT['G-'], Rational(3, 2))

    def test_parities(self):
        """Correct statistics: T, J bosonic; G+, G- fermionic."""
        self.assertEqual(GEN_PARITY['T'], 0)
        self.assertEqual(GEN_PARITY['J'], 0)
        self.assertEqual(GEN_PARITY['G+'], 1)
        self.assertEqual(GEN_PARITY['G-'], 1)

    def test_total_weight(self):
        """Total weight of generators: 2 + 1 + 3/2 + 3/2 = 6."""
        total = sum(GEN_WEIGHT[g] for g in GENERATORS)
        self.assertEqual(total, 6)


# =========================================================================
# 2. OPE data consistency (3 paths)
# =========================================================================

class TestOPEData(unittest.TestCase):
    """OPE n-th product data for the N=2 SCA."""

    def test_tt_central_charge(self):
        """Path 1: T_{(3)}T = c/2 (standard Virasoro)."""
        ope = n2_ope_data()
        self.assertEqual(ope[('T', 'T')][3]['1'], c / 2)

    def test_jj_level(self):
        """Path 2: J_{(1)}J = c/3 (U(1) level)."""
        ope = n2_ope_data()
        self.assertEqual(ope[('J', 'J')][1]['1'], c / 3)

    def test_gpgm_cubic_pole(self):
        """Path 3: G+_{(2)}G- = c/3 (SUSY central term)."""
        ope = n2_ope_data()
        self.assertEqual(ope[('G+', 'G-')][2]['1'], c / 3)

    def test_gpgm_susy(self):
        """G+_{(0)}G- contains T (SUSY relation)."""
        ope = n2_ope_data()
        self.assertIn('T', ope[('G+', 'G-')][0])
        self.assertEqual(ope[('G+', 'G-')][0]['T'], 1)

    def test_gpgp_vanishes(self):
        """G+G+ OPE vanishes (fermionic self-OPE)."""
        ope = n2_ope_data()
        self.assertEqual(ope[('G+', 'G+')], {})

    def test_gmgm_vanishes(self):
        """G-G- OPE vanishes."""
        ope = n2_ope_data()
        self.assertEqual(ope[('G-', 'G-')], {})

    def test_jgp_charge(self):
        """J_{(0)}G+ = G+ (charge +1)."""
        ope = n2_ope_data()
        self.assertEqual(ope[('J', 'G+')][0]['G+'], 1)

    def test_jgm_charge(self):
        """J_{(0)}G- = -G- (charge -1)."""
        ope = n2_ope_data()
        self.assertEqual(ope[('J', 'G-')][0]['G-'], -1)


# =========================================================================
# 3. Pole orders (AP19)
# =========================================================================

class TestPoleOrders(unittest.TestCase):
    """Maximum OPE pole orders."""

    def test_tt_pole_4(self):
        """TT has quartic pole (standard Virasoro)."""
        self.assertEqual(max_pole_order('T', 'T'), 4)

    def test_jj_pole_2(self):
        """JJ has double pole (abelian current)."""
        self.assertEqual(max_pole_order('J', 'J'), 2)

    def test_gpgm_pole_3(self):
        """G+G- has cubic pole (N=2 SUSY)."""
        self.assertEqual(max_pole_order('G+', 'G-'), 3)

    def test_jg_pole_1(self):
        """JG+ has simple pole."""
        self.assertEqual(max_pole_order('J', 'G+'), 1)

    def test_gpgp_pole_0(self):
        """G+G+ has no pole (vanishing OPE)."""
        self.assertEqual(max_pole_order('G+', 'G+'), 0)


# =========================================================================
# 4. Bar basis enumeration
# =========================================================================

class TestBarBasis(unittest.TestCase):
    """Bar chain group basis enumeration."""

    def test_b1_weight_2(self):
        """B^1 at weight 2: just T."""
        basis = bar_basis_at_weight(1, 2)
        self.assertEqual(len(basis), 1)
        self.assertEqual(basis[0], ('T',))

    def test_b1_weight_1(self):
        """B^1 at weight 1: just J."""
        basis = bar_basis_at_weight(1, 1)
        self.assertEqual(len(basis), 1)
        self.assertEqual(basis[0], ('J',))

    def test_b2_weight_3(self):
        """B^2 at weight 3: pairs summing to 3.
        (T,J): 2+1=3. (J,T): 1+2=3.
        (G+,G+): 3/2+3/2=3. (G+,G-): 3/2+3/2=3.
        (G-,G+): 3/2+3/2=3. (G-,G-): 3/2+3/2=3.
        Total: 6 pairs (including fermionic self-pairs).
        """
        basis = bar_basis_at_weight(2, 3)
        self.assertEqual(len(basis), 6)

    def test_b2_weight_2(self):
        """B^2 at weight 2: pairs summing to 2.
        (J,J): 1+1=2.
        Total: 1 pair.
        """
        basis = bar_basis_at_weight(2, 2)
        self.assertEqual(len(basis), 1)

    def test_b2_weight_4(self):
        """B^2 at weight 4: pairs summing to 4.
        (T,T): 2+2=4.
        (J, G+): 1+3/2=5/2 != 4. No.
        (G+,G+): 3 != 4. No.
        Total: 1 pair.
        Wait: also need half-integer sums.
        (J, ?): J has weight 1, need partner at weight 3. No generator at 3.
        (G+, G-): 3/2+3/2=3 != 4. No.
        Just (T,T).
        """
        basis = bar_basis_at_weight(2, 4)
        self.assertEqual(len(basis), 1)


# =========================================================================
# 5. CE H^2 analysis
# =========================================================================

class TestCEH2(unittest.TestCase):
    """CE cohomology H^2 analysis at the generator level."""

    def test_ce_h2_weight_3(self):
        """CE H^2 at weight 3 (the critical weight)."""
        r = ce_h2_at_weight(3, c_val=1.0)
        self.assertIsNotNone(r)
        # At weight 3: B^2 has 6 elements (including fermionic self-pairs)
        self.assertEqual(r['dim_B2'], 6)

    def test_ce_h2_weight_2(self):
        """CE H^2 at weight 2."""
        r = ce_h2_at_weight(2, c_val=1.0)
        self.assertEqual(r['dim_B2'], 1)


# =========================================================================
# 6. Chiral bar H^2 computation
# =========================================================================

class TestChiralBarH2(unittest.TestCase):
    """Chiral bar H^2 computation for the N=2 SCA."""

    def test_weight_3_computation(self):
        """H^2 at weight 3 (generator level)."""
        r = _compute_h2_at_weight_simplified(3, c_val=1.0)
        self.assertIn('dim_B2', r)
        self.assertIn('ker_d', r)

    def test_weight_3_b2_dim_6(self):
        """B^2 at weight 3 has 6 elements (including fermionic self-pairs)."""
        r = _compute_h2_at_weight_simplified(3, c_val=1.0)
        self.assertEqual(r['dim_B2'], 6)

    def test_generic_c_analysis(self):
        """Analysis runs for generic c."""
        result = n2_sca_koszulness_analysis(c_val=1.0)
        self.assertIn('per_weight', result)

    def test_analysis_c_equals_3(self):
        """Analysis at the free-field point c=3."""
        result = n2_sca_koszulness_analysis(c_val=3.0)
        self.assertIn('full_conclusion', result)


# =========================================================================
# 7. Koszulness evidence
# =========================================================================

class TestKoszulnessEvidence(unittest.TestCase):
    """Evidence summary for N=2 SCA Koszulness."""

    def test_status_open(self):
        """Status is OPEN."""
        summary = koszulness_evidence_summary()
        self.assertEqual(summary['status'], 'OPEN')

    def test_has_evidence_for(self):
        """Evidence FOR Koszulness exists."""
        summary = koszulness_evidence_summary()
        self.assertGreater(len(summary['evidence_for']), 0)

    def test_has_evidence_against(self):
        """Evidence AGAINST Koszulness exists."""
        summary = koszulness_evidence_summary()
        self.assertGreater(len(summary['evidence_against']), 0)

    def test_lean_towards_koszul(self):
        """Evidence leans towards Koszul."""
        summary = koszulness_evidence_summary()
        self.assertIn('KOSZUL', summary['lean'].upper())

    def test_definitive_test_described(self):
        """Definitive test is described."""
        summary = koszulness_evidence_summary()
        self.assertIn('chiral bar', summary['definitive_test'])


# =========================================================================
# 8. Cross-checks with n2_superconformal_shadow.py
# =========================================================================

class TestCrossCheck(unittest.TestCase):
    """Cross-checks with the existing N=2 shadow engine."""

    def test_central_charge_consistency(self):
        """Central charge formula matches n2_superconformal_shadow."""
        try:
            from compute.lib.n2_superconformal_shadow import n2_central_charge
            for k_val in [1, 2, 3, 5, 10]:
                c_shadow = n2_central_charge(k_val)
                c_expected = Rational(3 * k_val, k_val + 2)
                self.assertEqual(c_shadow, c_expected)
        except ImportError:
            self.skipTest("n2_superconformal_shadow not available")

    def test_ope_tt_matches(self):
        """TT OPE matches between engines."""
        try:
            from compute.lib.n2_superconformal_shadow import n2_nth_products
            ope_shadow = n2_nth_products()
            ope_bar = n2_ope_data()
            # TT mode 3 (quartic pole): c/2 in both
            self.assertEqual(ope_shadow[('T', 'T')][3]['vac'],
                             ope_bar[('T', 'T')][3]['1'])
        except ImportError:
            self.skipTest("n2_superconformal_shadow not available")


if __name__ == '__main__':
    unittest.main()
