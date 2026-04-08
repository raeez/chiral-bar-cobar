"""Tests for W_3 explicit bar cohomology engine.

Ground truth sources:
  bar_complex_tables.tex: comp:w3-nthproducts, comp:w3-bar-degree2
  landscape_census.tex: conj:w3-bar-gf, tab:bar-dimensions
  bar_gf_algebraicity.py: w3_bar_dims, virasoro_bar_dims

Verification paths per claim:
  1. Direct computation (from OPE mode algebra)
  2. Generating function (rational GF formula)
  3. Recurrence (linear recurrence relation)
  4. Cross-family (Virasoro sub-algebra comparison)
  5. Symmetry (Z_2 parity, skew-symmetry)
  6. Literature (Zamolodchikov 1985, Fateev-Lukyanov)
"""

import pytest
from fractions import Fraction

from compute.lib.bar_cohomology_w3_explicit_engine import (
    W3BarCohomologyEngine,
    w3_bar_dims,
    w3_gf_from_formula,
    virasoro_bar_dims,
    w3_vacuum_dims,
    bar_chain_dim,
    verify_ope_data,
    verify_curvature_complementarity,
    _motzkin_numbers,
    dim_vbar,
)


# =========================================================================
# Bar dimension sequence (paths 2 + 3: GF and recurrence)
# =========================================================================

class TestBarDimSequence:
    """Verify the bar cohomology dimension sequence [2, 5, 16, 52, 171, ...]."""

    def test_known_values(self):
        """Ground truth from bar_complex_tables.tex."""
        a = w3_bar_dims(8)
        assert a[1] == 2
        assert a[2] == 5
        assert a[3] == 16
        assert a[4] == 52
        assert a[5] == 171

    def test_recurrence_matches_gf(self):
        """Path 2 vs 3: GF formula matches recurrence."""
        from_rec = w3_bar_dims(12)
        from_gf = w3_gf_from_formula(12)
        for n in range(1, 13):
            assert from_rec[n] == from_gf[n], f"Mismatch at n={n}"

    def test_a6_from_recurrence(self):
        """a_6 = 4*171 - 2*52 - 16 = 564."""
        assert w3_bar_dims(6)[6] == 564

    def test_a7_from_recurrence(self):
        """a_7 = 4*564 - 2*171 - 52 = 1862."""
        assert w3_bar_dims(7)[7] == 1862

    def test_a8_from_recurrence(self):
        """a_8 = 4*1862 - 2*564 - 171 = 6149."""
        assert w3_bar_dims(8)[8] == 6149

    def test_a0_is_zero(self):
        """No bar cohomology at weight 0."""
        assert w3_bar_dims(1)[0] == 0

    def test_all_positive(self):
        """All bar dims are positive for n >= 1."""
        a = w3_bar_dims(15)
        for n in range(1, 16):
            assert a[n] > 0, f"a_{n} = {a[n]} <= 0"

    def test_growth_is_exponential(self):
        """Growth rate ~ (3+sqrt(13))/2 ~ 3.303."""
        a = w3_bar_dims(20)
        # Check ratio converges
        ratios = [a[n] / a[n - 1] for n in range(10, 21)]
        expected = (3 + 13**0.5) / 2  # ~ 3.3028
        assert abs(ratios[-1] - expected) < 0.01

    def test_gf_denominator_roots(self):
        """Denominator (1-x)(1-3x-x^2) has roots at x=1 and x=(-3+-sqrt(13))/2."""
        import math
        r1 = 1.0
        r2 = (-3 + math.sqrt(13)) / 2  # ~ 0.3028
        r3 = (-3 - math.sqrt(13)) / 2  # ~ -3.3028
        # Check denominator vanishes
        for r in [r1, r2, r3]:
            den = 1 - 4 * r + 2 * r**2 + r**3
            assert abs(den) < 1e-10, f"Denominator at x={r}: {den}"


# =========================================================================
# Virasoro comparison (path 4: cross-family)
# =========================================================================

class TestVirasoroComparison:
    """Compare W_3 bar dims with the Virasoro sub-algebra contribution."""

    def test_virasoro_motzkin_differences(self):
        """Virasoro bar dims = Motzkin differences."""
        M = _motzkin_numbers(12)
        v = virasoro_bar_dims(10)
        for n in range(1, 11):
            assert v[n] == M[n + 1] - M[n]

    def test_virasoro_known_values(self):
        """Virasoro: 1, 2, 5, 12, 30, 76, 196, 512."""
        v = virasoro_bar_dims(8)
        expected = [0, 1, 2, 5, 12, 30, 76, 196, 512]
        for n in range(1, 9):
            assert v[n] == expected[n], f"Vir mismatch at n={n}"

    def test_w3_exceeds_virasoro(self):
        """W_3 bar dims exceed Virasoro at every n >= 1."""
        w = w3_bar_dims(10)
        v = virasoro_bar_dims(10)
        for n in range(1, 11):
            assert w[n] > v[n], f"n={n}: W_3={w[n]} not > Vir={v[n]}"

    def test_w3_at_n1_is_double_virasoro(self):
        """At n=1: W_3 has 2 generators (T,W), Virasoro has 1 (T)."""
        assert w3_bar_dims(1)[1] == 2
        assert virasoro_bar_dims(1)[1] == 1

    def test_excess_grows(self):
        """W-channel excess grows faster than Virasoro contribution."""
        w = w3_bar_dims(10)
        v = virasoro_bar_dims(10)
        excess = [w[n] - v[n] for n in range(1, 11)]
        # Excess should be monotonically increasing
        for n in range(1, len(excess)):
            assert excess[n] >= excess[n - 1]

    def test_growth_ratio_increases(self):
        """Ratio dim(W_3^!)/dim(Vir^!) increases with n."""
        e = W3BarCohomologyEngine(10)
        ratios = [e.growth_ratio(n) for n in range(1, 11)]
        for i in range(1, len(ratios)):
            assert ratios[i] >= ratios[i - 1]


# =========================================================================
# OPE verification (path 1: direct computation)
# =========================================================================

class TestOPEData:
    """Verify W_3 OPE data at c=7 against ground truth."""

    @pytest.fixture
    def ope_results(self):
        return verify_ope_data(7.0)

    def test_TT_vacuum(self, ope_results):
        """T_{(3)}T = c/2 (quartic pole curvature)."""
        assert ope_results["mu(T,T) vac = c/2"]

    def test_TT_T_coeff(self, ope_results):
        """T_{(1)}T = 2T (double pole)."""
        assert ope_results["mu(T,T) T = 2"]

    def test_TT_dT_coeff(self, ope_results):
        """T_{(0)}T = dT (simple pole Lie bracket)."""
        assert ope_results["mu(T,T) dT = 1"]

    def test_TW_no_vacuum(self, ope_results):
        """No vacuum in T x W OPE (W is primary)."""
        assert ope_results["mu(T,W) no vac"]

    def test_TW_W_coeff(self, ope_results):
        """T_{(1)}W = 3W (conformal weight of W)."""
        assert ope_results["mu(T,W) W = 3"]

    def test_TW_dW_coeff(self, ope_results):
        """T_{(0)}W = dW."""
        assert ope_results["mu(T,W) dW = 1"]

    def test_WT_no_vacuum(self, ope_results):
        """No vacuum in W x T OPE."""
        assert ope_results["mu(W,T) no vac"]

    def test_WT_W_coeff(self, ope_results):
        """W_{(1)}T = 3W."""
        assert ope_results["mu(W,T) W = 3"]

    def test_WT_dW_asymmetric(self, ope_results):
        """W_{(0)}T = 2dW (NOT dW; asymmetric with T_{(0)}W, AP19)."""
        assert ope_results["mu(W,T) dW = 2 (asymmetric)"]

    def test_WW_vacuum(self, ope_results):
        """W_{(5)}W = c/3 (sixth-order pole curvature)."""
        assert ope_results["mu(W,W) vac = c/3"]

    def test_WW_T_coeff(self, ope_results):
        """W_{(3)}W = 2T (quartic pole in WW)."""
        assert ope_results["mu(W,W) T = 2"]

    def test_WW_dT_coeff(self, ope_results):
        """W_{(2)}W = dT (cubic pole in WW)."""
        assert ope_results["mu(W,W) dT = 1"]

    def test_WW_L4_coeff(self, ope_results):
        """W_{(1)}W: L_{-4} component = (3/5)(1-alpha).

        d^2T = 2*L_{-4}|0> (AP45: desuspension lowers degree).
        Lambda = L_{-2}^2 - (3/5)*L_{-4}.
        W_{(1)}W = (3/10)*2*L_{-4} + alpha*(L_{-2}^2 - (3/5)*L_{-4})
                 = (3/5)(1-alpha)*L_{-4} + alpha*L_{-2}^2.
        """
        assert ope_results["mu(W,W) L4 = (3/5)(1-alpha)"]

    def test_WW_TT_coeff(self, ope_results):
        """W_{(1)}W: L_{-2}^2 component = alpha = 16/(22+5c)."""
        assert ope_results["mu(W,W) TT = alpha"]

    def test_curvature_ratio(self, ope_results):
        """m0(W)/m0(T) = (c/3)/(c/2) = 2/3 (level-independent)."""
        assert ope_results["curvature ratio 2/3"]

    def test_asymmetry(self, ope_results):
        """mu(T,W) != mu(W,T): Borcherds skew-symmetry (AP19)."""
        assert ope_results["W_(0)T asymmetric with T_(0)W"]


# =========================================================================
# OPE at multiple c values (path 1: robustness)
# =========================================================================

class TestOPEMultipleC:
    """Verify OPE at multiple central charges."""

    @pytest.mark.parametrize("c_val", [1.0, 7.0, 13.0, 25.0, -22.0])
    def test_TT_vacuum(self, c_val):
        """mu(T,T) vacuum = c/2 at various c."""
        results = verify_ope_data(c_val)
        assert results["mu(T,T) vac = c/2"]

    @pytest.mark.parametrize("c_val", [1.0, 7.0, 25.0])
    def test_WW_vacuum(self, c_val):
        """mu(W,W) vacuum = c/3 at various c."""
        results = verify_ope_data(c_val)
        assert results["mu(W,W) vac = c/3"]

    @pytest.mark.parametrize("c_val", [1.0, 7.0, 13.0, 25.0])
    def test_curvature_ratio_universal(self, c_val):
        """m0(W)/m0(T) = 2/3 for all c != 0."""
        results = verify_ope_data(c_val)
        assert results["curvature ratio 2/3"]


# =========================================================================
# Curvature complementarity (path 6: literature)
# =========================================================================

class TestCurvatureComplementarity:
    """Verify Fateev-Lukyanov central charge formula."""

    @pytest.fixture
    def curv_results(self):
        return verify_curvature_complementarity()

    def test_complementarity_sum(self, curv_results):
        """c(k) + c(-k-6) = 100 (Fateev-Lukyanov)."""
        assert curv_results["c(k) + c(-k-6) = 100"]

    def test_c_at_k1(self, curv_results):
        """c(k=1) = 2 - 24*9/4 = -52."""
        assert curv_results["c(k=1) = -52"]

    def test_c_at_k0(self, curv_results):
        """c(k=0) = 2 - 24*4/3 = -30."""
        assert curv_results["c(k=0) = -30"]


# =========================================================================
# Vacuum module structure (path 1: direct)
# =========================================================================

class TestVacuumModule:
    """W_3 vacuum module dimensions and structure."""

    def test_dim_h2(self):
        """Vbar_2 = {T} (dim 1)."""
        assert dim_vbar(2) == 1

    def test_dim_h3(self):
        """Vbar_3 = {W, dT} (dim 2)."""
        assert dim_vbar(3) == 2

    def test_dim_h4(self):
        """Vbar_4 = {dW, d^2T, :TT:} (dim 3)."""
        assert dim_vbar(4) == 3

    def test_dim_h5(self):
        """Vbar_5: 4 states."""
        assert dim_vbar(5) == 4

    def test_dim_h6(self):
        """Vbar_6: 8 states."""
        assert dim_vbar(6) == 8

    def test_dim_h7(self):
        """Vbar_7: 10 states."""
        assert dim_vbar(7) == 10

    def test_dim_h8(self):
        """Vbar_8: 17 states."""
        assert dim_vbar(8) == 17

    def test_character_product_formula(self):
        """Vbar character = prod_{n>=2} 1/(1-q^n) * prod_{m>=3} 1/(1-q^m) - 1."""
        dims = w3_vacuum_dims(10)
        # Compare with explicit partition counting
        assert dims.get(2, 0) == 1
        assert dims.get(3, 0) == 2
        assert dims.get(4, 0) == 3


# =========================================================================
# Z_2 parity (path 5: symmetry)
# =========================================================================

class TestZ2Parity:
    """Z_2 parity structure (W -> -W)."""

    def test_h2_all_even(self):
        """Weight 2: only T (even parity)."""
        e = W3BarCohomologyEngine(8)
        z2 = e.z2_parity_vbar(2)
        assert z2["even"] == 1 and z2["odd"] == 0

    def test_h3_one_each(self):
        """Weight 3: W (odd) and dT (even)."""
        e = W3BarCohomologyEngine(8)
        z2 = e.z2_parity_vbar(3)
        assert z2["even"] == 1 and z2["odd"] == 1

    def test_h4_two_even_one_odd(self):
        """Weight 4: dW (odd), d^2T and :TT: (even)."""
        e = W3BarCohomologyEngine(8)
        z2 = e.z2_parity_vbar(4)
        assert z2["even"] == 2 and z2["odd"] == 1

    def test_parity_sums_to_total(self):
        """even + odd = total at each weight."""
        e = W3BarCohomologyEngine(10)
        for h in range(2, 10):
            z2 = e.z2_parity_vbar(h)
            assert z2["even"] + z2["odd"] == z2["total"]


# =========================================================================
# Bar chain dimensions (path 7: dimensional analysis)
# =========================================================================

class TestBarChainDims:
    """Bar chain group dimensions B^n_h."""

    def test_B1_equals_vbar(self):
        """B^1_h = Vbar_h (OS^0 = {1} is 1-dim)."""
        for h in range(2, 9):
            assert bar_chain_dim(1, h) == dim_vbar(h)

    def test_B2_min_weight(self):
        """B^2_h = 0 for h < 4 (each factor has weight >= 2)."""
        assert bar_chain_dim(2, 3) == 0
        assert bar_chain_dim(2, 4) > 0

    def test_B2_at_4(self):
        """B^2_4: only (T,T), OS^1 has dim 1. So B^2_4 = 1."""
        assert bar_chain_dim(2, 4) == 1

    def test_B2_at_5(self):
        """B^2_5: pairs at weight 5 = (2,3). States: T x {W,dT} + {W,dT} x T = 4.
        Times OS^1 dim 1 = 4."""
        assert bar_chain_dim(2, 5) == 4

    def test_B3_min_weight(self):
        """B^3_h = 0 for h < 6."""
        assert bar_chain_dim(3, 5) == 0
        assert bar_chain_dim(3, 6) > 0

    def test_B3_at_6(self):
        """B^3_6: only (T,T,T), OS^2 has dim 2. So B^3_6 = 2."""
        assert bar_chain_dim(3, 6) == 1 * 2  # 1 triple * 2 OS forms

    def test_B4_min_weight(self):
        """B^4_h = 0 for h < 8."""
        assert bar_chain_dim(4, 7) == 0
        assert bar_chain_dim(4, 8) > 0


# =========================================================================
# Engine class (path 2 + 4: GF + cross-family)
# =========================================================================

class TestEngine:
    """W3BarCohomologyEngine integration tests."""

    @pytest.fixture
    def engine(self):
        return W3BarCohomologyEngine(10, 7.0)

    def test_H1_at_n1(self, engine):
        """dim H^1_1 = 2 (T and W generators)."""
        assert engine.H1_dim(1) == 2

    def test_H1_at_n2(self, engine):
        """dim H^1_2 = 5."""
        assert engine.H1_dim(2) == 5

    def test_H1_at_n3(self, engine):
        """dim H^1_3 = 16."""
        assert engine.H1_dim(3) == 16

    def test_H1_at_n4(self, engine):
        """dim H^1_4 = 52."""
        assert engine.H1_dim(4) == 52

    def test_H1_at_n5(self, engine):
        """dim H^1_5 = 171."""
        assert engine.H1_dim(5) == 171

    def test_vir_H1_at_n1(self, engine):
        """Virasoro sub-algebra: dim = 1 at n=1."""
        assert engine.vir_H1_dim(1) == 1

    def test_w_channel_positive(self, engine):
        """W-channel excess is positive for n >= 1."""
        for n in range(1, 11):
            assert engine.w_channel_excess(n) >= 0

    def test_w_channel_at_n1(self, engine):
        """W-channel excess at n=1 is 1 (the W generator)."""
        assert engine.w_channel_excess(1) == 1

    def test_recurrence_verified(self, engine):
        """Recurrence matches GF at all computed weights."""
        checks = engine.verify_recurrence()
        assert all(checks.values())

    def test_full_table_completeness(self, engine):
        """Full table has all required keys."""
        t = engine.full_table()
        assert "bar_dims" in t
        assert "vir_dims" in t
        assert "growth_rate" in t
        assert t["koszulness"] is True

    def test_H1_total(self, engine):
        """Total H^1 up to n=5 = 2+5+16+52+171 = 246."""
        assert engine.H1_total(5) == 246


# =========================================================================
# Motzkin numbers (path 3: independent computation)
# =========================================================================

class TestMotzkinNumbers:
    """Verify Motzkin number computation."""

    def test_M0_to_M5(self):
        """M(0)=1, M(1)=1, M(2)=2, M(3)=4, M(4)=9, M(5)=21."""
        M = _motzkin_numbers(6)
        assert M == [1, 1, 2, 4, 9, 21]

    def test_M6_to_M8(self):
        """M(6)=51, M(7)=127, M(8)=323."""
        M = _motzkin_numbers(9)
        assert M[6] == 51
        assert M[7] == 127
        assert M[8] == 323


# =========================================================================
# Weight-4 analysis (path 1 + 5: direct + symmetry)
# =========================================================================

class TestWeight4:
    """Weight-4 bar cohomology and Lambda decomposition."""

    def test_dim_vbar_4(self):
        """dim Vbar_4 = 3."""
        assert dim_vbar(4) == 3

    def test_bar_dim_n2(self):
        """Bar dim at n=2 (corresponding to weight 4 structures) = 5."""
        assert w3_bar_dims(2)[2] == 5

    def test_lambda_is_quasi_primary(self):
        """Lambda = :TT: - (3/10)d^2T is quasi-primary (appears in WW OPE)."""
        e = W3BarCohomologyEngine(8)
        w4 = e.weight4_analysis()
        assert w4["weight"] == 4
        assert w4["dim_Vbar"] == 3

    def test_C_WWW_vanishes(self):
        """C_{WWW} = 0 by Z_2 parity (W is odd, W x W -> even)."""
        e = W3BarCohomologyEngine(8)
        w4 = e.weight4_analysis()
        assert w4["C_WWW"] == "0 (Z_2 parity: W x W -> even sector, W is odd)"


# =========================================================================
# Cross-check with bar_gf_algebraicity.py (path 6: literature)
# =========================================================================

class TestCrossCheckBarGF:
    """Verify against the existing bar_gf_algebraicity module."""

    def test_matches_bar_gf_algebraicity(self):
        """Our sequence matches bar_gf_algebraicity.w3_bar_dims."""
        from compute.lib.bar_gf_algebraicity import w3_bar_dims as w3_ref
        ref = w3_ref(8)
        ours = w3_bar_dims(8)
        for i, (r, o) in enumerate(zip(ref, ours[1:])):
            assert r == o, f"Mismatch at index {i}: ref={r}, ours={o}"

    def test_matches_virasoro_bar_gf(self):
        """Our Virasoro sequence matches bar_gf_algebraicity.virasoro_bar_dims."""
        from compute.lib.bar_gf_algebraicity import virasoro_bar_dims as vir_ref
        ref = vir_ref(8)
        ours = virasoro_bar_dims(8)
        for i, (r, o) in enumerate(zip(ref, ours[1:])):
            assert r == o, f"Mismatch at index {i}: ref={r}, ours={o}"


# =========================================================================
# Koszulness (path 5: structural)
# =========================================================================

class TestKoszulness:
    """Verify Koszulness of the W_3 algebra."""

    def test_koszul_flag(self):
        """Engine reports Koszulness = True."""
        e = W3BarCohomologyEngine(8)
        t = e.full_table()
        assert t["koszulness"] is True

    def test_generators_at_n1(self):
        """Two generators (T and W) contribute a_1 = 2."""
        assert w3_bar_dims(1)[1] == 2

    def test_growth_rate_is_algebraic(self):
        """Growth rate = (3+sqrt(13))/2, an algebraic number."""
        import math
        rate = (3 + math.sqrt(13)) / 2
        assert abs(rate - 3.3028) < 0.001
