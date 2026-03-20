"""Tests for the charge-graded master equation recursion.

Verifies:
  1. Rank-1 recovery: two-sector reduces to single-line results
  2. Rank-2 abelian: contact cascade to arity 6
  3. Cubic pump non-nilpotency: alpha!=0, Q!=0 gives infinite tower on charged
  4. Four-class persistence for 5 parameter combinations
  5. Charge conservation: no backflow from charged to neutral
  6. Symmetry factor accounting: j=k terms halved
  7. Explicit coefficient verification against hand computation

Ground truth:
  - thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
  - prop:independent-sum-factorization (higher_genus_modular_koszul.tex)
  - virasoro_shadow_tower.py (single-sector reference)
"""

import pytest
from sympy import (
    Rational, Symbol, simplify, factor, S, symbols, expand,
)

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from multi_stratum_shadow import (
    compute_two_sector_tower,
    compute_rank_n_abelian_tower,
    verify_four_class_persistence,
    tower_by_charge,
    shadow_depth,
    single_sector_recovery,
    _charge_decompositions,
    _available_charges_two_sector,
    _available_charges_rank_n,
)


kappa_sym = Symbol('kappa')
alpha_sym = Symbol('alpha')
Q_sym = Symbol('Q')
c = Symbol('c')


# =========================================================================
# I. Charge lattice utilities
# =========================================================================

class TestChargeLattice:
    """Tests for charge decomposition and available charge sets."""

    def test_two_sector_available(self):
        """Two-sector system has exactly charges 0 and 1."""
        avail = _available_charges_two_sector()
        assert avail == {(0,), (1,)}

    def test_rank2_available(self):
        """Rank-2 system has 4 available charges."""
        avail = _available_charges_rank_n(2)
        assert avail == {(0, 0), (0, 1), (1, 0), (1, 1)}

    def test_rank3_available(self):
        """Rank-3 system has 8 available charges."""
        avail = _available_charges_rank_n(3)
        assert len(avail) == 8

    def test_decompositions_neutral(self):
        """Charge (0,) decomposes as (0,)+(0,) only in two-sector."""
        avail = _available_charges_two_sector()
        decomps = _charge_decompositions((0,), avail)
        assert decomps == [((0,), (0,))]

    def test_decompositions_charged(self):
        """Charge (1,) decomposes as (0,)+(1,) and (1,)+(0,) in two-sector."""
        avail = _available_charges_two_sector()
        decomps = _charge_decompositions((1,), avail)
        assert set(map(tuple, decomps)) == {((0,), (1,)), ((1,), (0,))}

    def test_decompositions_rank2_mixed(self):
        """Charge (1,1) in rank-2 decomposes four ways."""
        avail = _available_charges_rank_n(2)
        decomps = _charge_decompositions((1, 1), avail)
        expected = {
            ((0, 0), (1, 1)),
            ((0, 1), (1, 0)),
            ((1, 0), (0, 1)),
            ((1, 1), (0, 0)),
        }
        assert set(map(tuple, decomps)) == expected


# =========================================================================
# II. Rank-1 recovery
# =========================================================================

class TestRank1Recovery:
    """Two-sector system reduces to known single-sector results."""

    def test_gaussian_class_neutral_only_kappa(self):
        """Class G: only kappa on neutral, nothing on charged."""
        tower = compute_two_sector_tower(
            kappa=kappa_sym, alpha=S.Zero, Q=S.Zero, max_arity=10
        )
        assert (2, (0,)) in tower
        assert tower[(2, (0,))] == kappa_sym
        # Nothing else
        assert len(tower) == 1

    def test_lie_class_cubic_on_neutral(self):
        """Class L: kappa and alpha on neutral, charged empty."""
        tower = compute_two_sector_tower(
            kappa=kappa_sym, alpha=alpha_sym, Q=S.Zero, max_arity=10
        )
        neutral = tower_by_charge(tower, (0,))
        charged = tower_by_charge(tower, (1,))
        assert neutral == {2: kappa_sym, 3: alpha_sym}
        assert charged == {}

    def test_contact_class_quartic_on_charged(self):
        """Class C: kappa on neutral, Q on charged, no mixing."""
        tower = compute_two_sector_tower(
            kappa=kappa_sym, alpha=S.Zero, Q=Q_sym, max_arity=10
        )
        neutral = tower_by_charge(tower, (0,))
        charged = tower_by_charge(tower, (1,))
        assert neutral == {2: kappa_sym}
        assert charged == {4: Q_sym}

    def test_virasoro_parameters_class_l(self):
        """Virasoro cubic alpha=2, kappa=c/2 in class L (Q=0)."""
        tower = compute_two_sector_tower(
            kappa=c / 2, alpha=Rational(2), Q=S.Zero, max_arity=8
        )
        neutral = tower_by_charge(tower, (0,))
        assert simplify(neutral[2] - c / 2) == 0
        assert simplify(neutral[3] - 2) == 0
        assert 4 not in neutral  # no quartic generated in class L

    def test_shadow_depth_function(self):
        """shadow_depth returns correct maximum arity per sector."""
        tower = compute_two_sector_tower(
            kappa=kappa_sym, alpha=alpha_sym, Q=Q_sym, max_arity=8
        )
        assert shadow_depth(tower, (0,)) == 3
        assert shadow_depth(tower, (1,)) == 8

    def test_single_sector_recovery_gaussian(self):
        """single_sector_recovery extracts neutral sub-tower."""
        tower = compute_two_sector_tower(
            kappa=kappa_sym, alpha=S.Zero, Q=S.Zero, max_arity=6
        )
        recovered = single_sector_recovery(tower)
        assert recovered == {2: kappa_sym}


# =========================================================================
# III. Rank-2 abelian: contact cascade
# =========================================================================

class TestRank2Abelian:
    """Rank-2 abelian system with quartic contacts on each fundamental sector."""

    def test_initial_data(self):
        """Initial data: kappa at (0,0), Q_i at fundamental charges."""
        Q1, Q2 = symbols('Q_1 Q_2')
        tower = compute_rank_n_abelian_tower(
            kappa=kappa_sym, Q_list=[Q1, Q2], max_arity=6, rank=2
        )
        assert tower[(2, (0, 0))] == kappa_sym
        assert tower[(4, (1, 0))] == Q1
        assert tower[(4, (0, 1))] == Q2

    def test_no_quartic_on_neutral(self):
        """No quartic shadow on neutral sector (abelian: no cubic to generate it)."""
        Q1, Q2 = symbols('Q_1 Q_2')
        tower = compute_rank_n_abelian_tower(
            kappa=kappa_sym, Q_list=[Q1, Q2], max_arity=8, rank=2
        )
        assert (4, (0, 0)) not in tower

    def test_cross_sector_sextic(self):
        """Arity 6 at charge (1,1): cross-sector sewing of Q_1 and Q_2.

        Hand computation:
          r=6, j=k=4, c_{44} = 1/2, jk = 16
          Charge decompositions: (1,0)+(0,1) and (0,1)+(1,0)
          obstruction = (1/2)*16*(Q_1*Q_2 + Q_2*Q_1) = 16*Q_1*Q_2
          S_6^{(1,1)} = -(2/(kappa*12)) * 16*Q_1*Q_2 = -8*Q_1*Q_2/(3*kappa)
        """
        Q1, Q2 = symbols('Q_1 Q_2')
        tower = compute_rank_n_abelian_tower(
            kappa=kappa_sym, Q_list=[Q1, Q2], max_arity=6, rank=2
        )
        expected = -8 * Q1 * Q2 / (3 * kappa_sym)
        assert simplify(tower[(6, (1, 1))] - expected) == 0

    def test_no_arity5(self):
        """No arity-5 entries in rank-2 abelian (no cubic to sew with quartic)."""
        Q1, Q2 = symbols('Q_1 Q_2')
        tower = compute_rank_n_abelian_tower(
            kappa=kappa_sym, Q_list=[Q1, Q2], max_arity=8, rank=2
        )
        for (r, q) in tower:
            assert r != 5, f"Unexpected arity-5 entry at charge {q}"

    def test_same_sector_no_sextic(self):
        """No arity-6 at charge (2,0) because charge 2 is unavailable.

        S_4^{(1,0)} * S_4^{(1,0)} would give charge (2,0), but (2,0)
        is not in the available set.
        """
        Q1, Q2 = symbols('Q_1 Q_2')
        tower = compute_rank_n_abelian_tower(
            kappa=kappa_sym, Q_list=[Q1, Q2], max_arity=8, rank=2
        )
        assert (6, (2, 0)) not in tower

    def test_rank2_total_entries(self):
        """Rank-2 abelian at max_arity=6 has exactly 4 entries."""
        Q1, Q2 = symbols('Q_1 Q_2')
        tower = compute_rank_n_abelian_tower(
            kappa=kappa_sym, Q_list=[Q1, Q2], max_arity=6, rank=2
        )
        assert len(tower) == 4

    def test_rank2_equal_Q(self):
        """When Q_1 = Q_2 = Q, the cross-sector sextic is -8Q^2/(3*kappa)."""
        tower = compute_rank_n_abelian_tower(
            kappa=kappa_sym, Q_list=[Q_sym, Q_sym], max_arity=6, rank=2
        )
        expected = -8 * Q_sym**2 / (3 * kappa_sym)
        assert simplify(tower[(6, (1, 1))] - expected) == 0

    def test_rank1_abelian_trivial(self):
        """Rank-1 abelian with Q: only kappa at (0,) and Q at (1,), nothing more.

        For rank-1 abelian, charge (1,)+(1,) = (2,) is not available.
        No cubic. Tower terminates at arity 4 on charged.
        """
        tower = compute_rank_n_abelian_tower(
            kappa=kappa_sym, Q_list=[Q_sym], max_arity=8, rank=1
        )
        assert len(tower) == 2
        assert tower[(2, (0,))] == kappa_sym
        assert tower[(4, (1,))] == Q_sym


# =========================================================================
# IV. Cubic pump and non-nilpotency
# =========================================================================

class TestCubicPump:
    """The cubic pump: alpha on neutral feeds the charged sector indefinitely."""

    def test_arity5_charged_nonzero(self):
        """S_5^{(1)} != 0 when alpha != 0 and Q != 0."""
        tower = compute_two_sector_tower(
            kappa=kappa_sym, alpha=alpha_sym, Q=Q_sym, max_arity=6
        )
        assert (5, (1,)) in tower
        S5 = tower[(5, (1,))]
        assert simplify(S5) != 0

    def test_arity5_charged_formula(self):
        """S_5^{(1)} = -12*alpha*Q/(5*kappa).

        Hand computation:
          r=5, j+k=7, (j,k)=(3,4), c_{34}=1.
          Charge decomps of (1,): (0,)+(1,) gives alpha*Q; (1,)+(0,) gives 0.
          obstruction = 1 * 3 * 4 * alpha * Q = 12*alpha*Q
          S_5 = -(2/(kappa*10)) * 12*alpha*Q = -12*alpha*Q/(5*kappa)
        """
        tower = compute_two_sector_tower(
            kappa=kappa_sym, alpha=alpha_sym, Q=Q_sym, max_arity=6
        )
        expected = -12 * alpha_sym * Q_sym / (5 * kappa_sym)
        assert simplify(tower[(5, (1,))] - expected) == 0

    def test_arity6_charged_formula(self):
        """S_6^{(1)} from sewing S_3^{(0)} with S_5^{(1)}.

        r=6, j+k=8. Options: (3,5) and (4,4).
          (3,5): c_{35}=1, charge (0,)+(1,): alpha * S_5^{(1)}.
                 charge (1,)+(0,): S_3^{(1,)}=0.
                 contrib = 3*5*alpha*(-12*alpha*Q/(5*kappa)) = -36*alpha^2*Q/kappa
          (4,4): c_{44}=1/2, charge (0,)+(1,): S_4^{(0,)}=0.
                 charge (1,)+(0,): Q * S_4^{(0,)}=0.
                 No contribution.
          obstruction = -36*alpha^2*Q/kappa
          S_6 = -(2/(kappa*12)) * (-36*alpha^2*Q/kappa) = 6*alpha^2*Q/kappa^2
        """
        tower = compute_two_sector_tower(
            kappa=kappa_sym, alpha=alpha_sym, Q=Q_sym, max_arity=6
        )
        expected = 6 * alpha_sym**2 * Q_sym / kappa_sym**2
        assert simplify(tower[(6, (1,))] - expected) == 0

    def test_arity7_charged_formula(self):
        """S_7^{(1)} from sewing S_3^{(0)} with S_6^{(1)}.

        r=7, j+k=9. Options: (3,6), (4,5).
          (3,6): 3*6*alpha*S_6^{(1)} = 18*alpha*(6*alpha^2*Q/kappa^2)
                 = 108*alpha^3*Q/kappa^2
          (4,5): 4*5*Q*S_5^{(0)}. But S_5^{(0)}=0.
                 Also 4*5*S_4^{(0)}*S_5^{(1)}: S_4^{(0)}=0.
          obstruction = 108*alpha^3*Q/kappa^2
          S_7 = -(2/(kappa*14)) * 108*alpha^3*Q/kappa^2
              = -108*alpha^3*Q/(7*kappa^3)
        """
        tower = compute_two_sector_tower(
            kappa=kappa_sym, alpha=alpha_sym, Q=Q_sym, max_arity=7
        )
        expected = -108 * alpha_sym**3 * Q_sym / (7 * kappa_sym**3)
        assert simplify(tower[(7, (1,))] - expected) == 0

    def test_charged_tower_infinite(self):
        """Charged sector reaches all arities up to max_arity in class M."""
        tower = compute_two_sector_tower(
            kappa=kappa_sym, alpha=alpha_sym, Q=Q_sym, max_arity=10
        )
        for r in range(5, 11):
            assert (r, (1,)) in tower, f"Missing S_{r}^{{(1,)}} in charged sector"

    def test_neutral_tower_finite_in_class_m(self):
        """Neutral sector stays at arity 3 in class M (charge conservation)."""
        tower = compute_two_sector_tower(
            kappa=kappa_sym, alpha=alpha_sym, Q=Q_sym, max_arity=10
        )
        neutral = tower_by_charge(tower, (0,))
        assert set(neutral.keys()) == {2, 3}

    def test_geometric_progression(self):
        """Charged sector shadow coefficients form a geometric-like sequence.

        S_r^{(1)} / S_{r-1}^{(1)} should be proportional to alpha/kappa
        up to a rational factor depending on r.
        """
        tower = compute_two_sector_tower(
            kappa=kappa_sym, alpha=alpha_sym, Q=Q_sym, max_arity=8
        )
        for r in range(6, 9):
            ratio = simplify(
                tower[(r, (1,))] * kappa_sym / (tower[(r - 1, (1,))] * alpha_sym)
            )
            # ratio should be a rational number (no symbolic dependence)
            assert ratio.is_Rational, (
                f"S_{r}/S_{r-1} * kappa/alpha = {ratio}, expected rational"
            )


# =========================================================================
# V. Four-class persistence
# =========================================================================

class TestFourClassPersistence:
    """Verify the four shadow depth classes in the multi-stratum setting."""

    def test_class_g(self):
        """Class G (Gaussian): alpha=0, Q=0 => tower terminates at arity 2."""
        results = verify_four_class_persistence(max_arity=10)
        assert results['G']['class_correct']
        assert results['G']['max_r_neutral'] == 2
        assert results['G']['max_r_charged'] == 0

    def test_class_l(self):
        """Class L (Lie/tree): alpha!=0, Q=0 => neutral at 3, charged at 0."""
        results = verify_four_class_persistence(max_arity=10)
        assert results['L']['class_correct']
        assert results['L']['max_r_neutral'] == 3
        assert results['L']['max_r_charged'] == 0

    def test_class_c(self):
        """Class C (contact): alpha=0, Q!=0 => neutral at 2, charged at 4."""
        results = verify_four_class_persistence(max_arity=10)
        assert results['C']['class_correct']
        assert results['C']['max_r_neutral'] == 2
        assert results['C']['max_r_charged'] == 4

    def test_class_m(self):
        """Class M (mixed): alpha!=0, Q!=0 => neutral at 3, charged infinite."""
        results = verify_four_class_persistence(max_arity=10)
        assert results['M']['class_correct']
        assert results['M']['max_r_neutral'] == 3
        assert results['M']['max_r_charged'] >= 10

    def test_class_g_numeric(self):
        """Class G with numeric kappa=1."""
        tower = compute_two_sector_tower(
            kappa=Rational(1), alpha=S.Zero, Q=S.Zero, max_arity=8
        )
        assert len(tower) == 1
        assert tower[(2, (0,))] == 1

    def test_class_l_numeric(self):
        """Class L with numeric kappa=1, alpha=3."""
        tower = compute_two_sector_tower(
            kappa=Rational(1), alpha=Rational(3), Q=S.Zero, max_arity=8
        )
        neutral = tower_by_charge(tower, (0,))
        assert set(neutral.keys()) == {2, 3}
        assert neutral[2] == 1
        assert neutral[3] == 3

    def test_class_c_numeric(self):
        """Class C with numeric kappa=2, Q=5."""
        tower = compute_two_sector_tower(
            kappa=Rational(2), alpha=S.Zero, Q=Rational(5), max_arity=8
        )
        neutral = tower_by_charge(tower, (0,))
        charged = tower_by_charge(tower, (1,))
        assert set(neutral.keys()) == {2}
        assert set(charged.keys()) == {4}
        assert neutral[2] == 2
        assert charged[4] == 5

    def test_class_m_numeric_arity5(self):
        """Class M with numeric values: S_5 on charged."""
        tower = compute_two_sector_tower(
            kappa=Rational(1), alpha=Rational(1), Q=Rational(1), max_arity=8
        )
        # S_5^{(1)} = -12*1*1/(5*1) = -12/5
        assert tower[(5, (1,))] == Rational(-12, 5)

    def test_class_m_numeric_arity6(self):
        """Class M with numeric values: S_6 on charged."""
        tower = compute_two_sector_tower(
            kappa=Rational(1), alpha=Rational(1), Q=Rational(1), max_arity=8
        )
        # S_6^{(1)} = 6*1*1/1 = 6
        assert tower[(6, (1,))] == Rational(6)


# =========================================================================
# VI. Explicit coefficient verification
# =========================================================================

class TestExplicitCoefficients:
    """Hand-computed coefficient checks."""

    def test_propagator_factor(self):
        """P = 2/kappa enters as -(P/(2r)) = -1/(r*kappa) in the recursion."""
        tower = compute_two_sector_tower(
            kappa=kappa_sym, alpha=alpha_sym, Q=Q_sym, max_arity=5
        )
        S5 = tower[(5, (1,))]
        # S_5 = -(2/(kappa*10)) * 12*alpha*Q = -12*alpha*Q/(5*kappa)
        # The 1/(5*kappa) = P/(2*5) = 1/(r*kappa) pattern
        assert simplify(S5 + 12 * alpha_sym * Q_sym / (5 * kappa_sym)) == 0

    def test_symmetry_factor_j_neq_k(self):
        """For j != k, the symmetry factor c_{jk} = 1."""
        # At arity 5: (j,k) = (3,4), c_{34} = 1
        tower = compute_two_sector_tower(
            kappa=Rational(1), alpha=Rational(1), Q=Rational(1), max_arity=5
        )
        # obstruction = 1 * 3 * 4 * 1 * 1 = 12
        # S_5 = -(1/5) * 12 = -12/5
        assert tower[(5, (1,))] == Rational(-12, 5)

    def test_symmetry_factor_j_eq_k(self):
        """For j = k, the symmetry factor c_{jk} = 1/2.

        Rank-2 abelian: S_6^{(1,1)} from j=k=4.
        obstruction = (1/2)*16*(Q1*Q2 + Q2*Q1) = 16*Q1*Q2
        (the 1/2 from c_{44} times the 2 from both charge orderings).
        """
        Q1, Q2 = symbols('Q_1 Q_2')
        tower = compute_rank_n_abelian_tower(
            kappa=Rational(1), Q_list=[Rational(1), Rational(1)],
            max_arity=6, rank=2
        )
        # S_6^{(1,1)} = -(1/6) * 16 = -8/3
        assert tower[(6, (1, 1))] == Rational(-8, 3)

    def test_alternating_signs(self):
        """Sign alternation in the charged tower: -, +, -, +, ..."""
        tower = compute_two_sector_tower(
            kappa=Rational(1), alpha=Rational(1), Q=Rational(1), max_arity=10
        )
        signs = []
        for r in range(4, 11):
            if (r, (1,)) in tower:
                val = tower[(r, (1,))]
                signs.append(1 if val > 0 else -1)
        # Q at arity 4 is positive, then alternating from arity 5
        # r=4: Q=+1, r=5: -12/5, r=6: +6, r=7: -108/7, r=8: +81/2
        assert signs == [1, -1, 1, -1, 1, -1, 1]


# =========================================================================
# VII. Charge conservation tests
# =========================================================================

class TestChargeConservation:
    """The charge lattice structure prevents certain flows."""

    def test_no_charge2_entry(self):
        """Charge (2,) is never generated (not in available set)."""
        tower = compute_two_sector_tower(
            kappa=kappa_sym, alpha=alpha_sym, Q=Q_sym, max_arity=10
        )
        for (r, q) in tower:
            assert q != (2,), f"Unexpected charge (2,) at arity {r}"

    def test_neutral_isolated_in_class_m(self):
        """Neutral sector q=(0,) cannot receive contributions from charged.

        In the two-sector system, the only charge decomposition of (0,)
        is (0,)+(0,). Since the charged sector doesn't feed back, the
        neutral sector sees only its own data.
        """
        tower = compute_two_sector_tower(
            kappa=kappa_sym, alpha=alpha_sym, Q=Q_sym, max_arity=10
        )
        neutral = tower_by_charge(tower, (0,))
        for r, val in neutral.items():
            # val should depend only on kappa and alpha, NOT on Q
            assert not val.has(Q_sym), (
                f"S_{r}^{{(0,)}} = {val} depends on Q (backflow!)"
            )

    def test_charged_depends_on_all(self):
        """Charged sector depends on both alpha and Q."""
        tower = compute_two_sector_tower(
            kappa=kappa_sym, alpha=alpha_sym, Q=Q_sym, max_arity=6
        )
        S5 = tower[(5, (1,))]
        assert S5.has(alpha_sym) and S5.has(Q_sym)


# =========================================================================
# VIII. Rank-2 cascade to arity 6
# =========================================================================

class TestRank2Cascade:
    """Detailed verification of the rank-2 abelian contact cascade."""

    def test_cascade_stops_at_6(self):
        """Rank-2 abelian tower has entries only at arities 2, 4, 6."""
        Q1, Q2 = symbols('Q_1 Q_2')
        tower = compute_rank_n_abelian_tower(
            kappa=kappa_sym, Q_list=[Q1, Q2], max_arity=10, rank=2
        )
        arities = set(r for (r, q) in tower)
        assert arities == {2, 4, 6}

    def test_cascade_charges(self):
        """The charge sectors that appear are (0,0), (1,0), (0,1), (1,1)."""
        Q1, Q2 = symbols('Q_1 Q_2')
        tower = compute_rank_n_abelian_tower(
            kappa=kappa_sym, Q_list=[Q1, Q2], max_arity=10, rank=2
        )
        charges = set(q for (r, q) in tower)
        assert charges == {(0, 0), (1, 0), (0, 1), (1, 1)}

    def test_no_arity8_cascade(self):
        """No arity-8 entries in rank-2 abelian.

        Would need j+k=10, j,k>=3. Options: (4,6), (5,5).
        (4,6): need S_4^{q1}*S_6^{q2}. S_6 only at (1,1).
               S_4 at (1,0) or (0,1). So charge = (1,0)+(1,1)=(2,1) or
               (0,1)+(1,1)=(1,2): both unavailable.
               Also (0,0)+(1,1): S_4^{(0,0)}=0.
        (5,5): S_5 = 0 everywhere.
        """
        Q1, Q2 = symbols('Q_1 Q_2')
        tower = compute_rank_n_abelian_tower(
            kappa=kappa_sym, Q_list=[Q1, Q2], max_arity=10, rank=2
        )
        for (r, q) in tower:
            assert r <= 6, f"Unexpected entry at arity {r}"

    def test_numeric_cascade(self):
        """Numeric rank-2: kappa=1, Q_1=2, Q_2=3."""
        tower = compute_rank_n_abelian_tower(
            kappa=Rational(1), Q_list=[Rational(2), Rational(3)],
            max_arity=6, rank=2
        )
        assert tower[(2, (0, 0))] == 1
        assert tower[(4, (1, 0))] == 2
        assert tower[(4, (0, 1))] == 3
        # S_6^{(1,1)} = -8*2*3/(3*1) = -16
        assert tower[(6, (1, 1))] == Rational(-16)

    def test_rank3_abelian_sextic_count(self):
        """Rank-3 abelian: sextic at charge (1,1,0), (1,0,1), (0,1,1).

        Each pair of distinct fundamental charges generates a cross-sector sextic.
        """
        Q1, Q2, Q3 = symbols('Q_1 Q_2 Q_3')
        tower = compute_rank_n_abelian_tower(
            kappa=kappa_sym, Q_list=[Q1, Q2, Q3], max_arity=6, rank=3
        )
        sextic_charges = [q for (r, q) in tower if r == 6]
        assert len(sextic_charges) == 3
        assert (1, 1, 0) in sextic_charges
        assert (1, 0, 1) in sextic_charges
        assert (0, 1, 1) in sextic_charges


# =========================================================================
# IX. Five parameter combinations for four-class persistence
# =========================================================================

class TestFiveParameterCombinations:
    """Verify four-class persistence for 5 specific parameter choices."""

    @pytest.mark.parametrize("kappa_val,alpha_val,Q_val,expected_class", [
        (Rational(1), S.Zero, S.Zero, 'G'),
        (Rational(2), Rational(3), S.Zero, 'L'),
        (Rational(1, 2), S.Zero, Rational(7), 'C'),
        (Rational(1), Rational(1), Rational(1), 'M'),
        (Rational(5), Rational(2), Rational(3), 'M'),
    ])
    def test_parameter_combination(self, kappa_val, alpha_val, Q_val, expected_class):
        tower = compute_two_sector_tower(
            kappa=kappa_val, alpha=alpha_val, Q=Q_val, max_arity=10
        )
        neutral_depth = shadow_depth(tower, (0,))
        charged_depth = shadow_depth(tower, (1,))

        if expected_class == 'G':
            assert neutral_depth == 2 and charged_depth == 0
        elif expected_class == 'L':
            assert neutral_depth == 3 and charged_depth == 0
        elif expected_class == 'C':
            assert neutral_depth == 2 and charged_depth == 4
        elif expected_class == 'M':
            assert neutral_depth == 3 and charged_depth >= 10

    def test_large_kappa_class_m(self):
        """Class M with large kappa: tower still infinite on charged."""
        tower = compute_two_sector_tower(
            kappa=Rational(100), alpha=Rational(1, 100), Q=Rational(1, 100),
            max_arity=10
        )
        assert shadow_depth(tower, (1,)) >= 10

    def test_fractional_parameters_class_m(self):
        """Class M with fractional parameters."""
        tower = compute_two_sector_tower(
            kappa=Rational(1, 3), alpha=Rational(2, 7), Q=Rational(5, 11),
            max_arity=8
        )
        # Verify S_5 by hand: -12*(2/7)*(5/11) / (5*(1/3))
        # = -12*10/(77) / (5/3) = -120/(77*5/3) = -120*3/(77*5) = -360/385 = -72/77
        assert tower[(5, (1,))] == Rational(-72, 77)
        assert shadow_depth(tower, (1,)) >= 8


# =========================================================================
# X. Edge cases
# =========================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_max_arity_2(self):
        """max_arity=2 returns only kappa on neutral."""
        tower = compute_two_sector_tower(
            kappa=kappa_sym, alpha=alpha_sym, Q=Q_sym, max_arity=2
        )
        assert len(tower) == 1
        assert tower[(2, (0,))] == kappa_sym

    def test_max_arity_4(self):
        """max_arity=4 returns initial data only (recursion starts at 5)."""
        tower = compute_two_sector_tower(
            kappa=kappa_sym, alpha=alpha_sym, Q=Q_sym, max_arity=4
        )
        assert set(tower.keys()) == {(2, (0,)), (3, (0,)), (4, (1,))}

    def test_zero_Q_list_entry(self):
        """Rank-2 with Q_1=0: no quartic on first fundamental sector."""
        Q2 = Symbol('Q_2')
        tower = compute_rank_n_abelian_tower(
            kappa=kappa_sym, Q_list=[S.Zero, Q2], max_arity=6, rank=2
        )
        assert (4, (1, 0)) not in tower
        assert (4, (0, 1)) in tower
        # No sextic at (1,1) because Q_1=0
        assert (6, (1, 1)) not in tower
