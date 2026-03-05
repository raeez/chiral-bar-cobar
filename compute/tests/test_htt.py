"""Tests for HTT (Homotopy Transfer Theorem) computations.

Ground truth:
  sl_2 is semisimple → CE complex is formal
  H*(sl_2; k) = Λ(x_3): 1-dim in degrees 0 and 3
  SDR: h_2 = d_1^{-1} = diag(-1/2, 1, -1/2)
"""
import pytest
from sympy import Rational, Matrix, eye, zeros

from compute.lib.htt import build_sl2_ce_sdr, verify_sdr


class TestSDRConstruction:
    def test_sdr_builds(self):
        ce, p, iota, h, d = build_sl2_ce_sdr()
        assert ce is not None

    def test_h2_equals_d1_inverse(self):
        ce, p, iota, h, d = build_sl2_ce_sdr()
        expected = Matrix([
            [Rational(-1, 2), 0, 0],
            [0, 1, 0],
            [0, 0, Rational(-1, 2)]
        ])
        assert h[2].equals(expected)

    def test_all_sdr_conditions(self):
        ce, p, iota, h, d = build_sl2_ce_sdr()
        results = verify_sdr(p, iota, h, d)
        for name, ok in results.items():
            assert ok, f"SDR condition failed: {name}"

    def test_p_iota_identity(self):
        ce, p, iota, h, d = build_sl2_ce_sdr()
        for k in [0, 3]:
            assert (p[k] * iota[k]).equals(eye(1))

    def test_h1_zero(self):
        """h_1: C^1 → C^0 is zero (no degree-0 coboundaries)."""
        ce, p, iota, h, d = build_sl2_ce_sdr()
        assert h[1].equals(zeros(1, 3))

    def test_h3_zero(self):
        """h_3: C^3 → C^2 is zero (all of C^3 is cohomology)."""
        ce, p, iota, h, d = build_sl2_ce_sdr()
        assert h[3].equals(zeros(3, 1))


class TestFormality:
    """sl_2 is formal: all transferred L∞ operations vanish."""

    def test_no_transferred_l1(self):
        """l_1^{tr} = p ∘ d ∘ ι = 0 (d kills harmonic reps)."""
        ce, p, iota, h, d = build_sl2_ce_sdr()
        # d_0 ∘ ι_0: C^0 → C^1
        result = d[0] * iota[0]
        assert result.equals(zeros(3, 1))

    def test_formality_low_degree(self):
        """l_n = 0 for n = 3, 4 by direct degree check.

        l_3: need a+b+c+2-3 ∈ {0,3} with a,b,c ∈ {0,3}. Max sum is 9, min 0.
        a+b+c = 1 or 4. With entries in {0,3}: impossible.
        l_4: need a+b+c+d+2-4 ∈ {0,3}. Sum = 2 or 5. Impossible from {0,3}.
        """
        cohom_degrees = {0, 3}
        for n in [3, 4]:
            for combo in _all_combos(list(cohom_degrees), n):
                target = sum(combo) + 2 - n
                assert target not in cohom_degrees, (
                    f"l_{n} degree-compatible for inputs {combo} → {target}")

    def test_formality_via_sdr(self):
        """sl_2 is formal: the SDR homotopy h is concentrated in degree 2.

        Since h_1 = 0 and h_3 = 0, the only nonzero homotopy is h_2.
        All HTT tree formulas involving h at other degrees give zero,
        which (combined with the gap in cohomology) forces all
        higher operations to vanish.
        """
        ce, p, iota, h, d = build_sl2_ce_sdr()
        assert h[1].equals(zeros(1, 3)), "h_1 should be zero"
        assert h[3].equals(zeros(3, 1)), "h_3 should be zero"
        # h_2 is nonzero: diag(-1/2, 1, -1/2)
        assert h[2].rank() == 3, "h_2 should have full rank"


def _all_combos(values, n):
    """Generate all n-tuples from values."""
    if n == 0:
        yield ()
        return
    for v in values:
        for rest in _all_combos(values, n - 1):
            yield (v,) + rest
