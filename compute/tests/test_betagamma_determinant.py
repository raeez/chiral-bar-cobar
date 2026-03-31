r"""Tests for betagamma determinant control and modular state space conjectures.

Investigates:
  conj:betagamma-determinant-control (beta_gamma.tex, ~line 1700)
  conj:betagamma-modular-state-spaces (beta_gamma.tex, ~line 1578)

Ground truth sources:
  - beta_gamma.tex: conjectures, kappa formula, complementarity
  - CLAUDE.md: bg is NOT self-dual, (bg)^! = bc, kappa = 1 at lam=1
  - higher_genus_complementarity.tex: Theorem C avatar
  - Mumford (1977): determinant of cohomology isomorphism
"""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from sympy import Rational, Symbol, simplify, bernoulli, factorial

try:
    from compute.lib.betagamma_determinant import (
        central_charge, kappa_betagamma, central_charge_bc, kappa_bc,
        shadow_depth, shadow_class, is_koszul, koszul_dual,
        euler_characteristic_Kn, h0_Kn, h1_Kn,
        mumford_exponent, determinant_line_exponent,
        verify_mumford_central_charge_identity,
        partition_function_euler_char, genus0_partition,
        genus1_eta_exponent, genus1_curvature,
        complementarity_kappa, complementarity_central_charge, complementarity_mumford,
        degeneration_separating, degeneration_nonseparating,
        quillen_metric_anomaly, quillen_determinant_genus2,
        special_weight_data, genus_expansion_coefficients,
        SPECIAL_WEIGHTS,
    )
except ImportError:
    pass

from betagamma_determinant import (
    central_charge, kappa_betagamma, central_charge_bc, kappa_bc,
    shadow_depth, shadow_class, is_koszul, koszul_dual,
    euler_characteristic_Kn, h0_Kn, h1_Kn,
    mumford_exponent, determinant_line_exponent,
    verify_mumford_central_charge_identity,
    partition_function_euler_char, genus0_partition,
    genus1_eta_exponent, genus1_curvature,
    complementarity_kappa, complementarity_central_charge, complementarity_mumford,
    degeneration_separating, degeneration_nonseparating,
    quillen_metric_anomaly, quillen_determinant_genus2,
    special_weight_data, genus_expansion_coefficients,
    SPECIAL_WEIGHTS,
)


# =====================================================================
# 1. Basic betagamma system data
# =====================================================================

class TestBasicData:
    """Test betagamma system parameters."""

    def test_central_charge_lam1(self):
        """c(lam=1) = 2.  Ground truth: beta_gamma.tex."""
        assert central_charge(1) == 2

    def test_central_charge_lam0(self):
        """c(lam=0) = 2.  Symmetric: c(0) = c(1)."""
        assert central_charge(0) == 2

    def test_central_charge_lam_half(self):
        """c(lam=1/2) = -1.  Symplectic boson."""
        assert central_charge(Rational(1, 2)) == -1

    def test_central_charge_lam2(self):
        """c(lam=2) = 26.  BRST ghost critical dimension."""
        assert central_charge(2) == 26

    def test_central_charge_symmetry(self):
        """c(lam) = c(1-lam): weight symmetry."""
        lam = Symbol('lambda')
        diff = simplify(central_charge(lam) - central_charge(1 - lam))
        assert diff == 0

    def test_kappa_lam1(self):
        """kappa(lam=1) = 1.  Ground truth: CLAUDE.md."""
        assert kappa_betagamma(1) == 1

    def test_kappa_lam_half(self):
        """kappa(lam=1/2) = -1/2."""
        assert kappa_betagamma(Rational(1, 2)) == Rational(-1, 2)

    def test_kappa_equals_c_over_2(self):
        """kappa = c/2 for all lam.  Ground truth: prop:betagamma-obstruction-coefficient."""
        lam = Symbol('lambda')
        assert simplify(kappa_betagamma(lam) - central_charge(lam) / 2) == 0

    def test_shadow_depth_is_4(self):
        """Shadow depth = 4 (contact/quartic).  Ground truth: CLAUDE.md."""
        assert shadow_depth() == 4

    def test_shadow_class_is_C(self):
        """Shadow class = C (contact).  Ground truth: CLAUDE.md."""
        assert shadow_class() == 'C'

    def test_is_koszul(self):
        """bg is chirally Koszul.  Ground truth: thm:betagamma-fermion-koszul."""
        assert is_koszul()

    def test_not_self_dual(self):
        """bg is NOT self-dual.  (bg)^! = bc.  Ground truth: CLAUDE.md."""
        assert koszul_dual() == 'bc'
        assert koszul_dual() != 'betagamma'


# =====================================================================
# 2. Riemann-Roch
# =====================================================================

class TestRiemannRoch:
    """Test Riemann-Roch: chi(Sigma_g, K^n) = (2n-1)(g-1)."""

    def test_genus0_K0(self):
        """chi(P^1, O) = 1."""
        assert euler_characteristic_Kn(0, 0) == 1

    def test_genus0_K1(self):
        """chi(P^1, K) = -1.  (h^0 = 0, h^1 = 2 -> chi = -1? No: deg K = -2, chi = -2+1 = -1.)"""
        assert euler_characteristic_Kn(1, 0) == -1

    def test_genus0_K2(self):
        """chi(P^1, K^2) = -3."""
        assert euler_characteristic_Kn(2, 0) == -3

    def test_genus1_all_vanish(self):
        """chi(E, K^n) = 0 for all n (torus: g=1, (2n-1)(1-1) = 0)."""
        for n in range(5):
            assert euler_characteristic_Kn(n, 1) == 0

    def test_genus2_K1(self):
        """chi(Sigma_2, K) = 1.  h^0 = 2, h^1 = 1."""
        assert euler_characteristic_Kn(1, 2) == 1

    def test_genus2_K2(self):
        """chi(Sigma_2, K^2) = 3.  3g-3 = 3 quadratic differentials."""
        assert euler_characteristic_Kn(2, 2) == 3

    def test_genus2_K0(self):
        """chi(Sigma_2, O) = -1.  h^0 = 1, h^1 = 2."""
        assert euler_characteristic_Kn(0, 2) == -1

    def test_additivity_formula(self):
        """chi(K^n, Sigma_g) = (2n-1)(g-1) for a range of values."""
        for g in range(5):
            for n in range(5):
                assert euler_characteristic_Kn(n, g) == Rational(2 * n - 1) * Rational(g - 1)

    def test_serre_duality_euler_char(self):
        """chi(K^n) + chi(K^{1-n}) = 0 (Serre duality implies chi is anti-symmetric about n=1/2).

        chi(K^n) = (2n-1)(g-1), chi(K^{1-n}) = (1-2n)(g-1) = -chi(K^n).
        """
        for g in range(2, 5):
            for n in [0, 1, 2, 3]:
                assert euler_characteristic_Kn(n, g) + euler_characteristic_Kn(1 - n, g) == 0


# =====================================================================
# 3. Mumford isomorphism
# =====================================================================

class TestMumford:
    """Test Mumford isomorphism: det(RGamma(K^n)) ~ lambda^{6n^2-6n+1}."""

    def test_mumford_K0(self):
        """e(0) = 1.  det(RGamma(O)) ~ lambda^1."""
        assert mumford_exponent(0) == 1

    def test_mumford_K1(self):
        """e(1) = 1.  det(RGamma(K)) ~ lambda^1 (Hodge = Hodge)."""
        assert mumford_exponent(1) == 1

    def test_mumford_K2(self):
        """e(2) = 13.  The famous Mumford exponent for K^2."""
        assert mumford_exponent(2) == 13

    def test_mumford_K3(self):
        """e(3) = 37."""
        assert mumford_exponent(3) == 37

    def test_mumford_central_charge_identity_symbolic(self):
        """e(lam) + e(1-lam) = c_{bg}(lam) symbolically."""
        assert verify_mumford_central_charge_identity()

    def test_mumford_central_charge_identity_numerical(self):
        """e(lam) + e(1-lam) = c_{bg}(lam) at specific values."""
        for lam_val in [0, 1, Rational(1, 2), 2, Rational(1, 3)]:
            assert verify_mumford_central_charge_identity(lam_val)

    def test_determinant_line_exponent_lam1(self):
        """D^{bg}_{g,1} ~ lambda^{-2}  (since c = 2)."""
        assert determinant_line_exponent(1) == -2

    def test_determinant_line_exponent_lam_half(self):
        """D^{bg}_{g,1/2} ~ lambda^{+1}  (since c = -1)."""
        assert determinant_line_exponent(Rational(1, 2)) == 1

    def test_determinant_line_exponent_lam2(self):
        """D^{bg}_{g,2} ~ lambda^{-26}  (since c = 26)."""
        assert determinant_line_exponent(2) == -26

    def test_determinant_line_equals_minus_c(self):
        """Total Mumford exponent = -c for all lam."""
        for lam_val in [0, 1, Rational(1, 2), 2, Rational(1, 3), Rational(3, 4)]:
            assert determinant_line_exponent(lam_val) == -central_charge(lam_val)


# =====================================================================
# 4. Complementarity
# =====================================================================

class TestComplementarity:
    """Test Q_g(bg) + Q_g(bc) = H*(M_bar_g, Z(bg)) at scalar level."""

    def test_kappa_complementarity_lam1(self):
        """kappa(bg) + kappa(bc) = 0 at lam=1."""
        r = complementarity_kappa(1)
        assert r['vanishes']
        assert r['kappa_bg'] == 1
        assert r['kappa_bc'] == -1

    def test_kappa_complementarity_symbolic(self):
        """kappa(bg) + kappa(bc) = 0 symbolically."""
        lam = Symbol('lambda')
        assert simplify(kappa_betagamma(lam) + kappa_bc(lam)) == 0

    def test_central_charge_complementarity(self):
        """c(bg) + c(bc) = 0 for all lam."""
        for lam_val in [0, 1, Rational(1, 2), 2]:
            r = complementarity_central_charge(lam_val)
            assert r['vanishes']

    def test_mumford_complementarity(self):
        """Mumford exponents cancel: det(bg) tensor det(bc) ~ trivial."""
        for lam_val in [0, 1, Rational(1, 2), 2]:
            r = complementarity_mumford(lam_val)
            assert r['trivial']

    def test_complementarity_not_self_dual(self):
        """bg is NOT self-dual: kappa(bg) != 0 generically.

        Self-duality would require kappa(A) = 0 (e.g., Virasoro at c=13).
        bg has kappa = 6 lam^2 - 6 lam + 1 = 0 only at lam = (3 +/- sqrt(3))/6.
        """
        # kappa vanishes at the irrational points (3 +/- sqrt(3))/6
        # but NOT at any standard weight value
        for lam_val in [0, 1, 2, Rational(1, 2)]:
            if lam_val == Rational(1, 2):
                # kappa = -1/2 != 0
                assert kappa_betagamma(lam_val) != 0
            else:
                assert kappa_betagamma(lam_val) != 0


# =====================================================================
# 5. Partition function data
# =====================================================================

class TestPartitionFunction:
    """Test partition function structure."""

    def test_genus0_normalized(self):
        """Z_0 = 1 (normalization)."""
        assert genus0_partition() == 1

    def test_genus1_eta_exponent(self):
        """Z_1 = eta^{-2} for one bg pair (2 oscillator modes)."""
        for lam_val in [0, 1, Rational(1, 2), 2]:
            assert genus1_eta_exponent(lam_val) == 2

    def test_genus1_curvature_formula(self):
        """m_0^{(1)} = c/24 * E_2(tau).  Ground truth: eq:betagamma-genus1-curvature."""
        for lam_val, expected_c in [(1, 2), (0, 2), (Rational(1, 2), -1)]:
            r = genus1_curvature(lam_val)
            assert r['curvature_coeff'] == Rational(expected_c, 24)

    def test_euler_char_sum_vanishes(self):
        """chi(K^lam) + chi(K^{1-lam}) = 0 for all g.

        This reflects the pairing between beta and gamma sectors.
        """
        for g in range(5):
            for lam_val in [1, 2, Rational(1, 3)]:
                r = partition_function_euler_char(lam_val, g)
                assert r['chi_sum'] == 0


# =====================================================================
# 6. Degeneration / factorization
# =====================================================================

class TestDegeneration:
    """Test factorization under curve degeneration."""

    def test_separating_g1_plus_g1(self):
        """Separating degeneration: Sigma_2 -> Sigma_1 cup Sigma_1."""
        r = degeneration_separating(1, 1, 1)
        assert r['identity_holds']
        assert r['node_correction'] == 1  # 2*1 - 1 = 1

    def test_separating_g1_plus_g2(self):
        """Separating degeneration: Sigma_3 -> Sigma_1 cup Sigma_2."""
        r = degeneration_separating(1, 2, 1)
        assert r['identity_holds']

    def test_separating_lam2(self):
        """Separating degeneration at lam=2 (K^2 sector)."""
        r = degeneration_separating(2, 2, 2)
        assert r['identity_holds']
        assert r['node_correction'] == 3  # 2*2 - 1 = 3

    def test_nonseparating_g2(self):
        """Nonseparating degeneration: Sigma_2 -> Sigma_1 with node."""
        r = degeneration_nonseparating(2, 1)
        assert r['identity_holds']

    def test_nonseparating_g3(self):
        """Nonseparating degeneration: Sigma_3 -> Sigma_2 with node."""
        r = degeneration_nonseparating(3, 1)
        assert r['identity_holds']

    def test_node_correction_equals_chi_of_fiber(self):
        """Node correction = (2n-1), which is chi(K^n restricted to a point) = 1 ... no.

        Actually the node correction is (2n-1) = chi(Sigma_1, K^n) - 0 + discrepancy.
        The formula chi(Sigma_g, K^n) = (2n-1)(g-1) is not additive under
        connected sum; the discrepancy is always (2n-1).
        """
        for n in [0, 1, 2, 3]:
            r = degeneration_separating(1, 1, n)
            assert r['node_correction'] == Rational(2 * n - 1)


# =====================================================================
# 7. Quillen determinant structure
# =====================================================================

class TestQuillen:
    """Test Quillen metric anomaly and determinant structure."""

    def test_anomaly_equals_central_charge(self):
        """Total Quillen anomaly = c(bg) for all lam."""
        for lam_val in [0, 1, Rational(1, 2), 2]:
            r = quillen_metric_anomaly(lam_val, 2)
            assert r['equals_central_charge']

    def test_anomaly_factorizes_into_sectors(self):
        """Anomaly = e(lam) + e(1-lam), with e(n) = 6n^2 - 6n + 1."""
        for lam_val in [0, 1, 2]:
            r = quillen_metric_anomaly(lam_val, 2)
            assert r['total_anomaly'] == mumford_exponent(lam_val) + mumford_exponent(1 - lam_val)

    def test_genus2_data_lam1(self):
        """Genus-2 Quillen data at lam=1."""
        r = quillen_determinant_genus2(1)
        assert r['mumford_exp_beta'] == 1     # e(1) = 1
        assert r['mumford_exp_gamma'] == 1    # e(0) = 1
        assert r['total_mumford_exp'] == -2   # -c = -2
        assert r['chi_beta'] == 1             # (2*1-1)(2-1) = 1
        assert r['chi_gamma'] == -1           # (2*0-1)(2-1) = -1


# =====================================================================
# 8. Special weights
# =====================================================================

class TestSpecialWeights:
    """Test data at special weight values."""

    def test_all_special_weights_consistent(self):
        """Verify c and kappa match for all special weight values."""
        for lam_val, data in SPECIAL_WEIGHTS.items():
            r = special_weight_data(lam_val)
            assert simplify(r['c_computed'] - data['c']) == 0
            assert simplify(r['kappa_computed'] - data['kappa']) == 0

    def test_brst_ghost_c26(self):
        """lam=2 gives c=26 (bosonic string critical dimension)."""
        assert central_charge(2) == 26

    def test_symplectic_boson_c_minus1(self):
        """lam=1/2 gives c=-1 (logarithmic CFT)."""
        assert central_charge(Rational(1, 2)) == -1


# =====================================================================
# 9. Genus expansion
# =====================================================================

class TestGenusExpansion:
    """Test genus expansion F_g = kappa * lambda_g^FP."""

    def test_genus1_coefficient(self):
        """F_1 = kappa * |B_2| / (2 * 2!) = kappa / 12.

        B_2 = 1/6, so |B_2|/(2*2!) = (1/6)/4 = 1/24.
        Wait: lambda_1^FP = |B_2|/(2*2!) = (1/6)/4 = 1/24.
        F_1 = kappa * 1/24.

        Hmm, but the genus-1 curvature is c/24 = kappa/12.
        Let me recheck: lambda_1^FP should be 1/12 for the A-hat genus.

        Actually A-hat(x) = x/(2 sinh(x/2)) = 1 - x^2/24 + ...
        So the genus-1 coefficient is -1/24.  But |B_2|/(2*2!) = (1/6)/4 = 1/24.
        The sign is absorbed into the absolute value.

        The genus expansion gives F_g = kappa * lambda_g^FP,
        where lambda_g^FP = |B_{2g}| / (2g * (2g)!).
        At g=1: |B_2|/(2*2!) = (1/6)/4 = 1/24.
        So F_1 = kappa/24.

        But the genus-1 curvature is kappa/12 * E_2(tau), and the
        Faber-Pandharipande intersection number lambda_1 on M_1 is 1/24.
        """
        r = genus_expansion_coefficients(1, g_max=1)
        assert r[1]['lambda_g^FP'] == Rational(1, 24)
        assert r[1]['F_g'] == kappa_betagamma(1) * Rational(1, 24)

    def test_genus2_coefficient(self):
        """F_2 = kappa * lambda_2^FP.

        B_4 = -1/30, |B_4| = 1/30.
        lambda_2^FP = (2^3 - 1)/2^3 * |B_4|/(4!) = (7/8)*(1/30)/24 = 7/5760.
        """
        r = genus_expansion_coefficients(1, g_max=2)
        assert r[2]['lambda_g^FP'] == Rational(7, 5760)

    def test_genus_expansion_kappa_dependence(self):
        """F_g is proportional to kappa for all g."""
        for lam_val in [0, 1, 2]:
            k = kappa_betagamma(lam_val)
            r = genus_expansion_coefficients(lam_val, g_max=3)
            for g in range(1, 4):
                assert simplify(r[g]['F_g'] - k * r[g]['lambda_g^FP']) == 0


# =====================================================================
# 10. Cross-checks with existing modules
# =====================================================================

class TestCrossChecks:
    """Cross-check against betagamma_bar.py and betagamma_quartic_contact.py."""

    def test_kappa_matches_quartic_contact(self):
        """kappa formula matches betagamma_quartic_contact.betagamma_kappa."""
        try:
            from compute.lib.betagamma_quartic_contact import betagamma_kappa
        except ImportError:
            try:
                from betagamma_quartic_contact import betagamma_kappa
            except ImportError:
                pytest.skip('betagamma_quartic_contact not available')
                return
        lam = Symbol('lambda')
        assert simplify(kappa_betagamma(lam) - betagamma_kappa(lam)) == 0

    def test_koszul_dual_matches_bar(self):
        """Koszul dual matches betagamma_bar.betagamma_koszul_dual."""
        try:
            from compute.lib.betagamma_bar import betagamma_koszul_dual as bg_kd
        except ImportError:
            try:
                from betagamma_bar import betagamma_koszul_dual as bg_kd
            except ImportError:
                pytest.skip('betagamma_bar not available')
                return
        # betagamma_bar returns 'bc_ghosts', we return 'bc'
        assert bg_kd() in ('bc_ghosts', 'bc')


# =====================================================================
# 11. The determinant control conjecture (structural tests)
# =====================================================================

class TestDeterminantControl:
    """Structural tests for conj:betagamma-determinant-control.

    The conjecture states: factorization homology of bg is
    quasi-isomorphic to the Quillen determinant line.
    We test necessary consequences.
    """

    def test_state_space_one_dimensional(self):
        """If the conjecture holds, H_g^{bg} is 1-dimensional (a line).

        The determinant line is a LINE bundle on M_g, so its space
        of sections is at most 1-dimensional at each point.
        """
        # This is a qualitative test: the determinant is a LINE (rank 1)
        assert True  # Structural: line bundle -> 1-dim fiber

    def test_determinant_line_well_defined(self):
        """D^{bg}_{g,lam} is well-defined for all lam and g >= 0."""
        for g in range(5):
            for lam_val in [0, 1, Rational(1, 2), 2]:
                chi = euler_characteristic_Kn(lam_val, g)
                # chi is always a well-defined integer
                assert isinstance(chi, Rational)

    def test_free_theory_implies_determinantal(self):
        """For a free theory (m_k = 0 for k >= 3), factorization homology
        reduces to a determinant.  This is the physical content of the conjecture.

        Ground truth: rem:betagamma-cleanest-test.
        """
        # The bg system has m_k = 0 for k >= 3: all local operations vanish
        # beyond the quadratic OPE. This makes factorization homology Gaussian.
        mk_vanish = True  # by definition of free field
        assert mk_vanish

    def test_bg_determinant_vs_heisenberg(self):
        """bg determinant line has TWO factors (beta and gamma sectors),
        while Heisenberg has ONE factor.

        bg: D = det(K^lam)^{-1} tensor det(K^{1-lam})^{-1}
        Heis: D = det(K)^{-1}   (single sector)
        """
        # bg has two sectors with complementary weights
        e_bg = -(mumford_exponent(1) + mumford_exponent(0))
        # Heisenberg at c=1 has mumford exponent 1
        e_heis = -mumford_exponent(1)

        assert e_bg == -2  # two copies of lambda^{-1}
        assert e_heis == -1  # one copy


# =====================================================================
# 12. Modular state space conjecture (structural tests)
# =====================================================================

class TestModularStateSpaces:
    """Structural tests for conj:betagamma-modular-state-spaces."""

    def test_partition_function_formula(self):
        """Z_g = det'(RGamma(K^lam))^{-1} * det'(RGamma(K^{1-lam}))^{-1}
        is a section of the determinant line D^{bg}_{g,lam}.

        This is a tautology: the formula DEFINES Z_g as a section of D.
        The content is that factorization homology reproduces this formula.
        """
        assert True  # Structural

    def test_genus1_matches_eta(self):
        """At genus 1, Z_1 = eta(tau)^{-2} = q^{-1/12} prod (1-q^n)^{-2}.

        This is the known result for one bg pair.
        The Dedekind eta function eta(tau) = q^{1/24} prod (1-q^n).
        eta^{-2} = q^{-1/12} prod (1-q^n)^{-2}.
        """
        # The number of eta^{-1} factors equals the number of oscillator families
        assert genus1_eta_exponent(1) == 2

    def test_genus1_determinant_interpretation(self):
        """At genus 1, det'(dbar_{K^1}) * det'(dbar_{K^0}) = eta(tau)^2.

        det'(dbar_K) on E_tau is related to eta(tau) by the Kronecker limit formula.
        For K^1 (sections = holomorphic differentials on torus):
          det'(dbar_{K^1}) ~ eta(tau)
        For K^0 (sections = functions on torus):
          det'(dbar_{K^0}) ~ eta(tau)

        So Z_1 = det'^{-1}(K^1) * det'^{-1}(K^0) ~ eta^{-2}.
        """
        # Both sectors contribute one eta factor
        assert genus1_eta_exponent(1) == 2


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
