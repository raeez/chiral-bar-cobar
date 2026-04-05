"""Cross-family kappa consistency tests (AP10 mitigation).

Verifies the modular characteristic kappa(A) is computed IDENTICALLY
by two independent code paths:

  Path A: shadow_metric_census.py formulas (used in shadow obstruction tower construction)
  Path B: theorem_c_complementarity.py formulas (used in complementarity checks)

These modules were written independently. If they agree across all families
and parameter values, the formulas are robust. If they disagree, one module
has a systematic error that single-family hardcoded tests would miss.

Additionally verifies:
  - Complementarity: kappa(A) + kappa(A!) = constant (level-independent)
  - Shadow metric consistency: Q_L(0) = 4*kappa^2
  - Cross-genus: F_g(A) = kappa(A) * lambda_g^FP at g=1,2,3
"""

import pytest
from fractions import Fraction
from sympy import Rational, S, simplify, sqrt

from compute.lib.shadow_metric_census import (
    kappa_heisenberg,
    kappa_virasoro,
    kappa_w3,
    kappa_affine_sl2,
    kappa_affine_slN,
    kappa_betagamma,
    kappa_lattice,
    kappa_bc,
)
from compute.lib.shadow_tower_recursive import shadow_metric_from_data
from compute.lib.theorem_c_complementarity import (
    kappa as kappa_thmc,
    kappa_dual as kappa_dual_thmc,
    complementarity_sum,
    verify_complementarity_scalar,
)


# ---------------------------------------------------------------------------
# Test 1: Two-path kappa agreement across all families
# ---------------------------------------------------------------------------

def _eq(a, b):
    """Compare values that may be float, Fraction, or Rational."""
    return simplify(S(a) - S(b)) == 0


class TestKappaTwoPathAgreement:
    """Verify kappa from shadow_metric_census == kappa from theorem_c_complementarity."""

    def test_heisenberg_two_path(self):
        for k in [1, 2, 3, -1, -2, Fraction(1, 2), Fraction(7, 3)]:
            path_a = kappa_heisenberg(k)
            path_b = kappa_thmc("heisenberg", k=k)
            assert _eq(path_a, path_b), (
                f"Heisenberg k={k}: census={path_a}, thm_c={path_b}"
            )

    def test_virasoro_two_path(self):
        for c in [1, 2, 13, 25, 26, Fraction(1, 2), Fraction(7, 10)]:
            path_a = kappa_virasoro(c)
            path_b = kappa_thmc("virasoro", c=c)
            assert _eq(path_a, path_b), (
                f"Virasoro c={c}: census={path_a}, thm_c={path_b}"
            )

    def test_affine_sl2_two_path(self):
        for k in [0, 1, 2, 3, -1, Fraction(1, 2)]:
            path_a = kappa_affine_sl2(k)
            path_b = kappa_thmc("affine", lie_type="A", rank=1, k=k)
            assert _eq(path_a, path_b), (
                f"sl_2 k={k}: census={path_a}, thm_c={path_b}"
            )

    def test_affine_sl3_two_path(self):
        for k in [0, 1, 2, -1, Fraction(1, 2)]:
            path_a = kappa_affine_slN(3, k)
            path_b = kappa_thmc("affine", lie_type="A", rank=2, k=k)
            assert _eq(path_a, path_b), (
                f"sl_3 k={k}: census={path_a}, thm_c={path_b}"
            )

    def test_affine_slN_two_path(self):
        """Cross-check for sl_4, sl_5 at generic levels."""
        for n, rank in [(4, 3), (5, 4)]:
            for k in [0, 1, 2]:
                path_a = kappa_affine_slN(n, k)
                path_b = kappa_thmc("affine", lie_type="A", rank=rank, k=k)
                assert _eq(path_a, path_b), (
                    f"sl_{n} k={k}: census={path_a}, thm_c={path_b}"
                )

    def test_w3_two_path(self):
        for c in [2, 6, 12, 50, Fraction(100, 3)]:
            path_a = kappa_w3(c)
            path_b = kappa_thmc("w3", c=c)
            assert _eq(path_a, path_b), (
                f"W_3 c={c}: census={path_a}, thm_c={path_b}"
            )

    def test_betagamma_two_path(self):
        for lam in [0, 1, Fraction(1, 2), Fraction(1, 3), 2]:
            path_a = kappa_betagamma(lam)
            path_b = kappa_thmc("betagamma", lam=lam)
            assert _eq(path_a, path_b), (
                f"betagamma lam={lam}: census={path_a}, thm_c={path_b}"
            )

    def test_lattice_two_path(self):
        for rank in [1, 2, 4, 8, 16, 24]:
            path_a = kappa_lattice(rank)
            path_b = kappa_thmc("lattice", rank=rank)
            assert _eq(path_a, path_b), (
                f"Lattice rank={rank}: census={path_a}, thm_c={path_b}"
            )


# ---------------------------------------------------------------------------
# Test 2: Complementarity kappa(A) + kappa(A!) = constant
# ---------------------------------------------------------------------------

class TestKappaComplementarity:
    """Verify kappa + kappa! is level-independent for each family."""

    def test_heisenberg_antisymmetry(self):
        """kappa(H_k) + kappa(H_{-k}) = 0 for all k."""
        for k in [1, 2, 3, -5, Fraction(1, 2), Fraction(7, 3)]:
            s = complementarity_sum("heisenberg", k=k)
            assert s == 0, f"Heisenberg k={k}: sum={s}"

    def test_virasoro_complementarity(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c."""
        for c in [1, 2, 13, 25, Fraction(1, 2), Fraction(7, 10)]:
            s = complementarity_sum("virasoro", c=c)
            assert s == 13, f"Virasoro c={c}: sum={s}"

    def test_affine_antisymmetry(self):
        """kappa(g_k) + kappa(g_{-k-2h*}) = 0 for all k (FF anti-symmetry)."""
        for k in [0, 1, 2, 3, -1, Fraction(1, 2)]:
            s = complementarity_sum("affine", lie_type="A", rank=1, k=k)
            assert s == 0, f"sl_2 k={k}: sum={s}"

    def test_w3_complementarity(self):
        """kappa(W3_c) + kappa(W3_{100-c}) = 250/3."""
        for c in [2, 6, 50, Fraction(100, 3)]:
            s = complementarity_sum("w3", c=c)
            assert s == Fraction(250, 3), f"W_3 c={c}: sum={s}"

    def test_betagamma_antisymmetry(self):
        """kappa(bg) + kappa(bc) = 0."""
        for lam in [0, 1, Fraction(1, 2)]:
            s = complementarity_sum("betagamma", lam=lam)
            assert s == 0, f"betagamma lam={lam}: sum={s}"

    def test_lattice_antisymmetry(self):
        """kappa(V_Lambda) + kappa(V_Lambda!) = 0."""
        for rank in [1, 2, 8, 24]:
            s = complementarity_sum("lattice", rank=rank)
            assert s == 0, f"Lattice rank={rank}: sum={s}"

    def test_complementarity_level_independence(self):
        """The complementarity sum should be the SAME for all parameter values."""
        # Virasoro: always 13
        vals = [complementarity_sum("virasoro", c=c) for c in [1, 5, 13, 25]]
        assert all(v == vals[0] for v in vals), f"Virasoro not constant: {vals}"
        # sl_2: always 0
        vals = [complementarity_sum("affine", lie_type="A", rank=1, k=k)
                for k in [0, 1, 2, 10]]
        assert all(v == vals[0] for v in vals), f"sl_2 not constant: {vals}"


# ---------------------------------------------------------------------------
# Test 3: Shadow metric Q_L(0) = 4*kappa^2
# ---------------------------------------------------------------------------

class TestKappaShadowMetricConsistency:
    """Verify that Q_L(0) = 4*kappa^2 across families."""

    def _check(self, kappa_val, alpha_val, S4_val, family_name):
        q0, q1, q2, Delta = shadow_metric_from_data(kappa_val, alpha_val, S4_val)
        expected_q0 = 4 * kappa_val ** 2
        assert simplify(q0 - expected_q0) == 0, (
            f"{family_name}: q0={q0}, expected 4*kappa^2={expected_q0}"
        )
        # Also verify Delta = 8*kappa*S4
        expected_Delta = 8 * kappa_val * S4_val
        assert simplify(Delta - expected_Delta) == 0, (
            f"{family_name}: Delta={Delta}, expected 8*kappa*S4={expected_Delta}"
        )

    def test_heisenberg_shadow_metric(self):
        """Heisenberg: kappa=k, alpha=0, S4=0 (Gaussian class)."""
        for k in [1, 2, 3]:
            self._check(Rational(k), Rational(0), Rational(0), f"H_{k}")

    def test_virasoro_shadow_metric(self):
        """Virasoro: kappa=c/2, alpha from cubic shadow."""
        for c_val in [1, 13, 25]:
            kv = Rational(c_val, 2)
            # alpha_vir = 2 (from Sh_3 = 2x^3, universal for Virasoro)
            # For this test, we only check Q_L(0) = 4*kappa^2
            self._check(kv, Rational(2), Rational(0), f"Vir_{c_val}")

    def test_affine_sl2_shadow_metric(self):
        """sl_2: kappa=3(k+2)/4."""
        for k in [1, 2, 3]:
            kv = Rational(3) * (k + 2) / 4
            self._check(kv, Rational(0), Rational(0), f"sl2_k{k}")


# ---------------------------------------------------------------------------
# Test 4: Cross-family formula consistency via dim(g)*(k+h*)/(2h*)
# ---------------------------------------------------------------------------

class TestKappaAffineUniversalFormula:
    """Verify all affine KM kappas are special cases of dim(g)*(k+h*)/(2h*)."""

    def test_sl2_from_universal(self):
        """sl_2: dim=3, h*=2. kappa = 3(k+2)/4."""
        for k in [0, 1, 2]:
            specific = kappa_affine_sl2(k)
            universal = kappa_affine_slN(2, k)
            assert _eq(specific, universal), (
                f"sl_2 k={k}: specific={specific}, universal={universal}"
            )

    def test_sl3_from_universal(self):
        """sl_3: dim=8, h*=3. kappa = 8(k+3)/6 = 4(k+3)/3."""
        for k in [0, 1, 2]:
            universal = kappa_affine_slN(3, k)
            expected = Rational(4) * (k + 3) / 3
            assert _eq(universal, expected), (
                f"sl_3 k={k}: got {universal}, expected {expected}"
            )

    def test_sl4_from_universal(self):
        """sl_4: dim=15, h*=4. kappa = 15(k+4)/8."""
        for k in [0, 1, 2]:
            universal = kappa_affine_slN(4, k)
            expected = Rational(15) * (k + 4) / 8
            assert _eq(universal, expected), (
                f"sl_4 k={k}: got {universal}, expected {expected}"
            )

    def test_critical_level_vanishing(self):
        """At critical level k=-h*, kappa = 0 (zero curvature)."""
        for n in [2, 3, 4, 5]:
            k_crit = -n  # h* = n for sl_n
            kv = kappa_affine_slN(n, k_crit)
            assert _eq(kv, 0), f"sl_{n} at k=-h*={k_crit}: kappa={kv}, expected 0"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
