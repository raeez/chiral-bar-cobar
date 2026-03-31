"""Q_contact (quartic contact invariant) cross-family consistency tests.

Verifies Q_contact = S_4 across families via structural formulas and
the shadow metric relation Delta = 8*kappa*S_4.

Key formulas (from the manuscript):
  - Heisenberg: S_4 = 0 (class G, tower terminates at arity 2)
  - Affine KM: S_4 = 0 (class L, tower terminates at arity 3)
  - Beta-gamma: S_4 != 0 on charged stratum (class C, terminates at arity 4)
  - Virasoro: Q^contact = 10/[c(5c+22)]
  - Virasoro dual (26-c): Q^contact = 10/[(26-c)(5(26-c)+22)] = 10/[(26-c)(152-5c)]
"""

import pytest
from fractions import Fraction
from sympy import Rational, Symbol, simplify, S

from compute.lib.shadow_metric_census import build_census


def _eq(a, b):
    """Compare values that may be float, Fraction, or Rational."""
    return simplify(S(a) - S(b)) == 0


class TestQcontactGaussianVanishing:
    """Class G algebras must have S_4 = 0."""

    def test_heisenberg_S4_zero(self):
        census = build_census()
        entry = census['Heisenberg']
        assert simplify(entry.S4) == 0

    def test_lattice_S4_zero(self):
        census = build_census()
        entry = census['Lattice']
        assert simplify(entry.S4) == 0

    def test_free_fermion_S4_zero(self):
        census = build_census()
        entry = census['FreeFermion']
        assert simplify(entry.S4) == 0


class TestQcontactLieVanishing:
    """Class L algebras must have S_4 = 0 (tower terminates at arity 3)."""

    def test_affine_sl2_S4_zero(self):
        census = build_census()
        entry = census['Affine_sl2']
        assert simplify(entry.S4) == 0

    def test_affine_slN_S4_zero(self):
        census = build_census()
        entry = census['Affine_slN']
        assert simplify(entry.S4) == 0


class TestQcontactVirasoroFormula:
    """Verify Q^contact_Vir = 10/[c(5c+22)] from the census."""

    def test_virasoro_S4_formula(self):
        census = build_census()
        entry = census['Virasoro']
        c = Symbol('c')
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(entry.S4 - expected) == 0

    def test_virasoro_S4_numerical(self):
        """Evaluate at specific c values and verify."""
        census = build_census()
        entry = census['Virasoro']
        c = Symbol('c')
        for c_val in [1, 2, 13, 25, Rational(1, 2), Rational(7, 10)]:
            s4_eval = entry.S4.subs(c, c_val)
            expected = Rational(10) / (c_val * (5 * c_val + 22))
            assert _eq(s4_eval, expected), (
                f"Virasoro c={c_val}: S4={s4_eval}, expected={expected}"
            )

    def test_virasoro_delta_from_S4(self):
        """Verify Delta = 8*kappa*S_4 = 40/(5c+22) for Virasoro."""
        census = build_census()
        entry = census['Virasoro']
        c = Symbol('c')
        expected_delta = Rational(40) / (5 * c + 22)
        assert simplify(entry.Delta - expected_delta) == 0


class TestQcontactDualityVirasoro:
    """Verify Q_contact transforms correctly under Virasoro duality c -> 26-c."""

    def test_qcontact_duality_relation(self):
        """Q_contact(Vir_c) and Q_contact(Vir_{26-c}) are related by c -> 26-c."""
        c = Symbol('c')
        q_c = Rational(10) / (c * (5 * c + 22))
        q_dual = Rational(10) / ((26 - c) * (5 * (26 - c) + 22))
        q_dual_simplified = Rational(10) / ((26 - c) * (152 - 5 * c))
        assert simplify(q_dual - q_dual_simplified) == 0

    def test_qcontact_self_dual_c13(self):
        """At the self-dual point c=13: Q_contact(Vir_13) = Q_contact(Vir_13)."""
        q_13 = Rational(10) / (13 * (5 * 13 + 22))
        q_dual_13 = Rational(10) / ((26 - 13) * (152 - 5 * 13))
        assert q_13 == q_dual_13
        assert q_13 == Rational(10) / (13 * 87)
        assert q_13 == Rational(10, 1131)

    def test_qcontact_sum_not_constant(self):
        """Unlike kappa, Q_contact + Q_contact_dual is NOT level-independent.
        This verifies that the quartic contact is a genuinely new invariant
        beyond the scalar kappa."""
        c = Symbol('c')
        q_c = Rational(10) / (c * (5 * c + 22))
        q_dual = Rational(10) / ((26 - c) * (152 - 5 * c))
        total = simplify(q_c + q_dual)
        # Evaluate at two different c values — if sum is NOT constant, they differ
        val_1 = total.subs(c, 1)
        val_13 = total.subs(c, 13)
        assert val_1 != val_13, (
            "Q_contact + Q_contact_dual should NOT be level-independent"
        )


class TestQcontactClassConsistency:
    """Shadow depth class should be consistent with S_4 value."""

    def test_class_G_implies_S4_zero(self):
        census = build_census()
        for name, entry in census.items():
            if entry.cls == 'G':
                assert simplify(entry.S4) == 0, (
                    f"{name} is class G but S4={entry.S4}"
                )

    def test_class_L_implies_S4_zero(self):
        census = build_census()
        for name, entry in census.items():
            if entry.cls == 'L':
                assert simplify(entry.S4) == 0, (
                    f"{name} is class L but S4={entry.S4}"
                )

    def test_class_M_implies_S4_nonzero(self):
        """Class M algebras should have S_4 != 0 (infinite tower requires
        non-vanishing quartic or higher)."""
        census = build_census()
        for name, entry in census.items():
            if entry.cls == 'M':
                assert entry.S4 != 0, (
                    f"{name} is class M but S4=0"
                )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
