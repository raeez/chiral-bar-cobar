"""Shadow depth 3-way consistency tests (AP10 mitigation).

Verifies shadow depth classification is consistent across three sources:

  Source 1: shadow_metric_census.py (structural classification from formulas)
  Source 2: shadow_tower_recursive.py (recursive computation from kappa, alpha, S4)
  Source 3: single_line_dichotomy (Delta = 0 ↔ finite tower; Delta ≠ 0 ↔ infinite)

The single-line dichotomy theorem (thm:single-line-dichotomy) states:
  Delta = 0  ↔  Q_L is a perfect square  ↔  tower terminates (class G or L)
  Delta ≠ 0  ↔  Q_L is irreducible      ↔  tower is infinite (class M)
  Class C escapes via stratum separation (quartic contact, r_max = 4)
"""

import pytest
from fractions import Fraction
from sympy import Rational, Symbol, simplify, S

from compute.lib.shadow_metric_census import (
    build_census,
    kappa_heisenberg,
    kappa_virasoro,
    kappa_affine_sl2,
    kappa_betagamma,
    kappa_lattice,
)
from compute.lib.shadow_tower_recursive import (
    compute_shadow_tower,
    shadow_metric_from_data,
)


def _eq(a, b):
    """Compare values that may be float, Fraction, or Rational."""
    return simplify(S(a) - S(b)) == 0


# ---------------------------------------------------------------------------
# Test 1: Delta = 8*kappa*S4 across all census entries
# ---------------------------------------------------------------------------

class TestDeltaFormula:
    """Verify Delta = 8*kappa*S4 for every entry in the shadow metric census."""

    def test_all_census_entries(self):
        census = build_census()
        for name, entry in census.items():
            expected = 8 * entry.kappa * entry.S4
            assert simplify(entry.Delta - expected) == 0, (
                f"{name}: Delta={entry.Delta}, 8*kappa*S4={expected}"
            )


# ---------------------------------------------------------------------------
# Test 2: Dichotomy — Delta=0 ↔ finite tower (class G/L)
# ---------------------------------------------------------------------------

class TestSingleLineDichotomy:
    """Verify the dichotomy: Delta=0 implies finite tower, Delta≠0 implies infinite."""

    def test_gaussian_class_has_zero_delta(self):
        """Class G (r_max=2) must have Delta=0."""
        census = build_census()
        for name, entry in census.items():
            if entry.cls == 'G':
                assert simplify(entry.Delta) == 0, (
                    f"{name} is class G but Delta={entry.Delta} ≠ 0"
                )

    def test_lie_class_has_zero_delta(self):
        """Class L (r_max=3) must have Delta=0."""
        census = build_census()
        for name, entry in census.items():
            if entry.cls == 'L':
                assert simplify(entry.Delta) == 0, (
                    f"{name} is class L but Delta={entry.Delta} ≠ 0"
                )

    def test_mixed_class_has_nonzero_delta(self):
        """Class M (r_max=infinity) must have Delta≠0."""
        census = build_census()
        for name, entry in census.items():
            if entry.cls == 'M':
                # Delta may be symbolic — check it's not identically zero
                # For Virasoro: Delta = 40/(5c+22) which is non-zero for c ≠ -22/5
                assert entry.Delta != 0, (
                    f"{name} is class M but Delta=0"
                )


# ---------------------------------------------------------------------------
# Test 3: Shadow obstruction tower depth class matches census (evaluated parameters)
# ---------------------------------------------------------------------------

class TestShadowTowerVsCensus:
    """Compute shadow obstruction tower from census data and verify depth class matches."""

    def test_heisenberg_depth(self):
        """Heisenberg: kappa=k, alpha=0, S4=0 → class G, r_max=2."""
        for k in [1, 2, 5]:
            tower = compute_shadow_tower(
                Rational(k), Rational(0), Rational(0),
                max_arity=10, algebra_name=f"H_{k}"
            )
            assert tower.depth_class == 'G', (
                f"H_{k}: tower says {tower.depth_class}, expected G"
            )
            # S_r should be 0 for all r >= 3
            for r in range(3, 11):
                if r in tower.coefficients:
                    assert tower.coefficients[r].value == 0, (
                        f"H_{k}: S_{r} = {tower.coefficients[r].value}, expected 0"
                    )

    def test_virasoro_depth(self):
        """Virasoro: class M (infinite tower) for c ≠ 0, -22/5."""
        for c_val in [1, 13, 25]:
            kv = Rational(c_val, 2)
            # S4 for Virasoro: from the formula Delta = 40/(5c+22), and Delta = 8*kappa*S4
            # So S4 = Delta/(8*kappa) = [40/(5c+22)] / (8*(c/2)) = 40/(4c*(5c+22)) = 10/(c*(5c+22))
            S4_val = Rational(10, c_val * (5 * c_val + 22))
            # alpha_vir = 2 (from Sh_3 = 2x^3, the Virasoro cubic shadow)
            tower = compute_shadow_tower(
                kv, Rational(2), S4_val,
                max_arity=10, algebra_name=f"Vir_{c_val}"
            )
            assert tower.depth_class == 'M', (
                f"Vir_{c_val}: tower says {tower.depth_class}, expected M"
            )
            # Verify tower doesn't terminate (S_r ≠ 0 for several r)
            nonzero_count = sum(
                1 for r in range(3, 11)
                if r in tower.coefficients and tower.coefficients[r].value != 0
            )
            assert nonzero_count >= 5, (
                f"Vir_{c_val}: only {nonzero_count} non-zero coefficients in S_3..S_10"
            )

    def test_lattice_depth(self):
        """Lattice: kappa=rank, alpha=0, S4=0 → class G, r_max=2."""
        for rank in [1, 8, 24]:
            tower = compute_shadow_tower(
                Rational(rank), Rational(0), Rational(0),
                max_arity=10, algebra_name=f"Lat_{rank}"
            )
            assert tower.depth_class == 'G', (
                f"Lat_{rank}: tower says {tower.depth_class}, expected G"
            )


# ---------------------------------------------------------------------------
# Test 4: Q_L(0) = 4*kappa^2 across all families
# ---------------------------------------------------------------------------

class TestShadowMetricAtZero:
    """Verify Q_L(t=0) = (2*kappa)^2 = 4*kappa^2 for all evaluated parameters."""

    def test_heisenberg_QL_zero(self):
        for k in [1, 2, 3]:
            q0, _, _, _ = shadow_metric_from_data(Rational(k), Rational(0), Rational(0))
            assert _eq(q0, 4 * k**2)

    def test_virasoro_QL_zero(self):
        for c_val in [1, 13, 25]:
            kv = Rational(c_val, 2)
            S4_val = Rational(10, c_val * (5 * c_val + 22))
            q0, _, _, _ = shadow_metric_from_data(kv, Rational(-6), S4_val)
            assert _eq(q0, 4 * kv**2), (
                f"Vir c={c_val}: q0={q0}, 4*kappa^2={4*kv**2}"
            )

    def test_affine_sl2_QL_zero(self):
        for k in [1, 2, 3]:
            kv = Rational(3) * (k + 2) / 4
            q0, _, _, _ = shadow_metric_from_data(kv, Rational(0), Rational(0))
            assert _eq(q0, 4 * kv**2)


# ---------------------------------------------------------------------------
# Test 5: Depth classification internal consistency
# ---------------------------------------------------------------------------

class TestDepthClassConsistency:
    """Cross-check depth class against structural invariants."""

    def test_gaussian_implies_alpha_zero(self):
        """Class G should have alpha=0 (no cubic shadow)."""
        census = build_census()
        for name, entry in census.items():
            if entry.cls == 'G' and entry.r_max == 2:
                assert simplify(entry.alpha) == 0, (
                    f"{name} is class G but alpha={entry.alpha} ≠ 0"
                )

    def test_depth_classes_partition(self):
        """Every census entry has a valid depth class."""
        census = build_census()
        for name, entry in census.items():
            assert entry.cls in {'G', 'L', 'C', 'M'}, (
                f"{name} has invalid depth class: {entry.cls}"
            )

    def test_finite_depth_class_has_rmax(self):
        """Classes G, L, C should have finite r_max."""
        census = build_census()
        for name, entry in census.items():
            if entry.cls in {'G', 'L', 'C'}:
                assert entry.r_max is not None, (
                    f"{name} is class {entry.cls} but r_max is None"
                )

    def test_infinite_class_has_none_rmax(self):
        """Class M should have r_max=None (infinite tower)."""
        census = build_census()
        for name, entry in census.items():
            if entry.cls == 'M':
                assert entry.r_max is None, (
                    f"{name} is class M but r_max={entry.r_max}"
                )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
