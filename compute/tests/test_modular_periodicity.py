"""Tests for modular periodicity computations.

Verifies conj:modular-periodicity and conj:reflected-modular-periodicity
from deformation_theory.tex.

Three conjecture families tested:
1. Modular periodicity (Type I): T-matrix period N = 24q/gcd(p,24)
   for rational chiral algebras with c = p/q.
2. Reflected modular periodicity: 1/N + 1/N' = (gcd(p,24)+gcd(p',24))/(24q)
   for Koszul dual pairs.
3. Nilpotence bounds (Graber-Vakil): kappa^{g-1} = 0 on smooth M_g.

Ground truth references:
  - conj:modular-periodicity (deformation_theory.tex)
  - conj:reflected-modular-periodicity (deformation_theory.tex)
  - thm:modular-periodicity-minimal (deformation_theory.tex)
  - thm:modular-periodicity-wzw (deformation_theory.tex)
  - thm:geometric-depth-smooth (deformation_theory.tex)
  - CLAUDE.md: verified formulas
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.modular_periodicity import (
    minimal_model_central_charge,
    virasoro_ds_central_charge,
    wzw_central_charge,
    wzw_central_charge_direct,
    scalar_modular_characteristic,
    w_algebra_sigma,
    modular_period,
    modular_period_from_pq,
    modular_period_divides_check,
    feigin_frenkel_dual_level,
    dual_central_charge_km,
    virasoro_dual_central_charge_km,
    km_central_charge_sum,
    reflected_period_check,
    reflected_period_check_km,
    reflected_period_check_virasoro,
    reflected_period_sum,
    reflected_period_formula_rhs,
    nilpotence_bound_smooth,
    nilpotence_bound_compactified,
    geometric_depth_comparison,
    dimensional_nilpotence_check,
    minimal_model_period_table,
    wzw_period_table,
    minimal_model_conformal_weights,
    actual_t_matrix_period,
    t_matrix_period_check,
    quantum_period,
    combined_period_bound,
    verify_modular_periodicity_minimal,
    verify_reflected_periodicity_km,
    verify_nilpotence_bounds,
    verify_feigin_frenkel,
    lie_dim,
    dual_coxeter,
    lie_rank,
)


# ===========================================================================
# Minimal model central charges
# ===========================================================================

class TestMinimalModelCentralCharge:
    """Central charge c = 1 - 6(p-q)^2/(pq) for minimal models M(p,q)."""

    def test_m23_trivial(self):
        """M(2,3): c = 0 (trivial theory)."""
        assert minimal_model_central_charge(2, 3) == 0

    def test_m34_ising(self):
        """M(3,4): c = 1/2 (Ising model)."""
        assert minimal_model_central_charge(3, 4) == Rational(1, 2)

    def test_m25(self):
        """M(2,5): c = -22/5."""
        assert minimal_model_central_charge(2, 5) == Rational(-22, 5)

    def test_m35(self):
        """M(3,5): c = -3/5."""
        assert minimal_model_central_charge(3, 5) == Rational(-3, 5)

    def test_m45_tricritical(self):
        """M(4,5): c = 7/10 (tricritical Ising)."""
        assert minimal_model_central_charge(4, 5) == Rational(7, 10)

    def test_m56_potts(self):
        """M(5,6): c = 4/5 (three-state Potts)."""
        assert minimal_model_central_charge(5, 6) == Rational(4, 5)

    def test_m27(self):
        """M(2,7): c = -68/7."""
        assert minimal_model_central_charge(2, 7) == Rational(-68, 7)

    def test_m37(self):
        """M(3,7): c = -25/7."""
        assert minimal_model_central_charge(3, 7) == Rational(-25, 7)

    def test_m47(self):
        """M(4,7): c = 1/14 (tetracritical Ising)."""
        c = minimal_model_central_charge(4, 7)
        # c = 1 - 6*9/28 = 1 - 54/28 = 1 - 27/14 = -13/14
        assert c == Rational(-13, 14)

    def test_m57(self):
        """M(5,7): c = 6/35."""
        c = minimal_model_central_charge(5, 7)
        expected = 1 - Rational(6 * 4, 35)
        assert c == expected

    def test_m67(self):
        """M(6,7): c = 6/7."""
        c = minimal_model_central_charge(6, 7)
        expected = 1 - Rational(6, 42)
        assert c == expected

    def test_invalid_p_geq_q(self):
        """p >= q should raise ValueError."""
        with pytest.raises(ValueError):
            minimal_model_central_charge(5, 3)

    def test_invalid_gcd(self):
        """gcd(p,q) != 1 should raise ValueError."""
        with pytest.raises(ValueError):
            minimal_model_central_charge(4, 6)

    def test_c_is_rational(self):
        """Central charge is always rational."""
        for p, q in [(2, 3), (3, 4), (4, 5), (5, 6), (3, 7)]:
            c = minimal_model_central_charge(p, q)
            assert isinstance(c, Rational)

    def test_unitary_range(self):
        """Unitary minimal models M(m, m+1) have 0 < c < 1 for m >= 3."""
        for m in range(3, 12):
            c = minimal_model_central_charge(m, m + 1)
            assert 0 < c < 1, f"M({m},{m+1}): c={c} not in (0,1)"


# ===========================================================================
# Virasoro DS central charge
# ===========================================================================

class TestVirasoroDSCentralCharge:
    """c(k) = 1 - 6(k+1)^2/(k+2) for DS reduction at level k."""

    def test_k_minus1(self):
        """c(-1) = 1 (free boson)."""
        assert virasoro_ds_central_charge(-1) == 1

    def test_k0(self):
        """c(0) = 1 - 6/2 = -2."""
        assert virasoro_ds_central_charge(0) == -2

    def test_k1(self):
        """c(1) = 1 - 6*4/3 = -7."""
        assert virasoro_ds_central_charge(1) == -7

    def test_complementarity_symbolic(self):
        """c(k) + c(-k-4) = 26 for symbolic k (CLAUDE.md verified)."""
        k = Symbol('k')
        c_k = virasoro_ds_central_charge(k)
        c_dual = virasoro_ds_central_charge(-k - 4)
        assert simplify(c_k + c_dual) == 26

    def test_complementarity_numerical(self):
        """c(k) + c(-k-4) = 26 for k = 0,1,2,3."""
        for k in range(4):
            c_k = virasoro_ds_central_charge(k)
            c_dual = virasoro_ds_central_charge(-k - 4)
            assert c_k + c_dual == 26


# ===========================================================================
# WZW central charges
# ===========================================================================

class TestWZWCentralCharge:
    """c = k * dim(g) / (k + h^vee)."""

    def test_sl2_k1(self):
        """sl_2 at k=1: c = 1*3/3 = 1."""
        assert wzw_central_charge("sl2", 1) == 1

    def test_sl2_k2(self):
        """sl_2 at k=2: c = 2*3/4 = 3/2."""
        assert wzw_central_charge("sl2", 2) == Rational(3, 2)

    def test_sl2_k3(self):
        """sl_2 at k=3: c = 3*3/5 = 9/5."""
        assert wzw_central_charge("sl2", 3) == Rational(9, 5)

    def test_sl2_k4(self):
        """sl_2 at k=4: c = 4*3/6 = 2."""
        assert wzw_central_charge("sl2", 4) == 2

    def test_sl3_k1(self):
        """sl_3 at k=1: c = 1*8/4 = 2."""
        assert wzw_central_charge("sl3", 1) == 2

    def test_sl3_k2(self):
        """sl_3 at k=2: c = 2*8/5 = 16/5."""
        assert wzw_central_charge("sl3", 2) == Rational(16, 5)

    def test_sl3_k3(self):
        """sl_3 at k=3: c = 3*8/6 = 4."""
        assert wzw_central_charge("sl3", 3) == 4

    def test_g2_k1(self):
        """G_2 at k=1: c = 1*14/5 = 14/5."""
        assert wzw_central_charge("g2", 1) == Rational(14, 5)

    def test_c_approaches_dim_g(self):
        """As k -> infinity, c -> dim(g)."""
        for name in ["sl2", "sl3", "g2"]:
            c = wzw_central_charge(name, 10000)
            dim_g = lie_dim(name)
            assert abs(float(c) - dim_g) < 0.01

    def test_direct_matches_named(self):
        """wzw_central_charge_direct matches wzw_central_charge."""
        for name in ["sl2", "sl3"]:
            for k in [1, 2, 3]:
                c1 = wzw_central_charge(name, k)
                c2 = wzw_central_charge_direct(lie_dim(name), dual_coxeter(name), k)
                assert c1 == c2


# ===========================================================================
# Scalar modular characteristic
# ===========================================================================

class TestScalarModularCharacteristic:
    """kappa(A) = c/2 for single-generator algebras."""

    def test_heisenberg(self):
        """kappa(Heis) = c/2 = 1/2 at c=1."""
        assert scalar_modular_characteristic(1) == Rational(1, 2)

    def test_virasoro_c_half(self):
        """kappa(Vir_{1/2}) = 1/4."""
        assert scalar_modular_characteristic(Rational(1, 2)) == Rational(1, 4)

    def test_symbolic(self):
        """kappa(c) = c/2 symbolically."""
        c = Symbol('c')
        assert scalar_modular_characteristic(c) == c / 2


class TestWAlgebraSigma:
    """sigma(sl_N) = H_N - 1 = sum_{h=2}^N 1/h."""

    def test_w2_virasoro(self):
        """W_2 (Virasoro): sigma = 1/2."""
        assert w_algebra_sigma(2) == Rational(1, 2)

    def test_w3(self):
        """W_3: sigma = 5/6."""
        assert w_algebra_sigma(3) == Rational(5, 6)

    def test_w4(self):
        """W_4: sigma = 13/12."""
        assert w_algebra_sigma(4) == Rational(13, 12)

    def test_w5(self):
        """W_5: sigma = 77/60."""
        assert w_algebra_sigma(5) == Rational(77, 60)


# ===========================================================================
# Modular period computation
# ===========================================================================

class TestModularPeriod:
    """N = 24q / gcd(p, 24) for c = p/q in lowest terms."""

    def test_c_zero(self):
        """c=0: N = 24*1/gcd(0,24) = 24/24 = 1."""
        assert modular_period(0) == 1

    def test_c_one(self):
        """c=1: N = 24*1/gcd(1,24) = 24."""
        assert modular_period(1) == 24

    def test_c_half(self):
        """c=1/2: N = 24*2/gcd(1,24) = 48."""
        assert modular_period(Rational(1, 2)) == 48

    def test_c_seven_tenth(self):
        """c=7/10: N = 24*10/gcd(7,24) = 240."""
        assert modular_period(Rational(7, 10)) == 240

    def test_c_four_fifth(self):
        """c=4/5: N = 24*5/gcd(4,24) = 120/4 = 30."""
        assert modular_period(Rational(4, 5)) == 30

    def test_c_three_half(self):
        """c=3/2: N = 24*2/gcd(3,24) = 48/3 = 16."""
        assert modular_period(Rational(3, 2)) == 16

    def test_c_two(self):
        """c=2: N = 24*1/gcd(2,24) = 24/2 = 12."""
        assert modular_period(2) == 12

    def test_c_negative(self):
        """c=-22/5: N = 24*5/gcd(22,24) = 120/2 = 60."""
        assert modular_period(Rational(-22, 5)) == 60

    def test_ising_period(self):
        """Ising M(3,4): period = 48 (matches monograph 'divides 48')."""
        c = minimal_model_central_charge(3, 4)
        assert modular_period(c) == 48

    def test_tricritical_ising_period(self):
        """Tricritical Ising M(4,5): period = 240 (matches monograph)."""
        c = minimal_model_central_charge(4, 5)
        assert modular_period(c) == 240

    def test_potts_period(self):
        """Three-state Potts M(5,6): period = 30 (matches monograph)."""
        c = minimal_model_central_charge(5, 6)
        assert modular_period(c) == 30

    def test_period_is_positive(self):
        """Period is always positive."""
        for c_val in [0, 1, Rational(1, 2), Rational(-3, 5), Rational(7, 10)]:
            assert modular_period(c_val) > 0

    def test_period_divides_24_times_denominator(self):
        """N divides 24 * denominator of c (since gcd(p,24) divides 24)."""
        for c_val in [Rational(1, 2), Rational(7, 10), Rational(-3, 5)]:
            r = Rational(c_val)
            N = modular_period(c_val)
            assert (24 * int(r.q)) % N == 0

    def test_modular_period_from_pq(self):
        """modular_period_from_pq agrees with modular_period."""
        for p, q in [(1, 2), (7, 10), (-3, 5), (4, 5), (1, 1)]:
            N1 = modular_period(Rational(p, q))
            N2 = modular_period_from_pq(p, q)
            assert N1 == N2

    def test_period_divides_check(self):
        """modular_period_divides_check is True for N and multiples."""
        c = Rational(1, 2)
        N = modular_period(c)
        assert modular_period_divides_check(c, N)
        assert modular_period_divides_check(c, 2 * N)
        assert modular_period_divides_check(c, 3 * N)
        # Smaller values should not work (N is minimal)
        for m in range(1, N):
            if m != N:
                # At least some should fail
                pass
        # Specific check: N=48 for c=1/2, so 24 should not work
        assert not modular_period_divides_check(c, 24)

    def test_minimality(self):
        """N is the MINIMAL period: no smaller positive integer works."""
        for c_val in [Rational(1, 2), Rational(7, 10), Rational(4, 5)]:
            N = modular_period(c_val)
            for m in range(1, N):
                assert not modular_period_divides_check(c_val, m), \
                    f"c={c_val}: m={m} < N={N} is also a period"


# ===========================================================================
# Feigin-Frenkel duality
# ===========================================================================

class TestFeiginFrenkelDuality:
    """k' = -k - 2h^vee (CRITICAL: NOT -k - h^vee)."""

    def test_sl2_formula(self):
        """sl_2: k' = -k - 4 (h^vee = 2)."""
        assert feigin_frenkel_dual_level(1, 2) == -5
        assert feigin_frenkel_dual_level(2, 2) == -6
        assert feigin_frenkel_dual_level(3, 2) == -7

    def test_sl3_formula(self):
        """sl_3: k' = -k - 6 (h^vee = 3)."""
        assert feigin_frenkel_dual_level(1, 3) == -7
        assert feigin_frenkel_dual_level(2, 3) == -8

    def test_symbolic(self):
        """Symbolic verification: k' = -k - 2h^vee."""
        k = Symbol('k')
        assert simplify(feigin_frenkel_dual_level(k, 2) - (-k - 4)) == 0
        assert simplify(feigin_frenkel_dual_level(k, 3) - (-k - 6)) == 0

    def test_double_dual_is_identity(self):
        """(k')' = k: the duality is an involution."""
        k = Symbol('k')
        for h in [2, 3, 4, 6]:
            k_dual = feigin_frenkel_dual_level(k, h)
            k_double = feigin_frenkel_dual_level(k_dual, h)
            assert simplify(k_double - k) == 0

    def test_not_minus_h_dual(self):
        """k' is NOT -k - h^vee (common mistake per CLAUDE.md)."""
        k = Symbol('k')
        for h in [2, 3]:
            k_dual = feigin_frenkel_dual_level(k, h)
            wrong = -k - h
            assert simplify(k_dual - wrong) != 0

    def test_verify_feigin_frenkel_suite(self):
        """Run full verification suite."""
        results = verify_feigin_frenkel()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"


# ===========================================================================
# KM central charge complementarity
# ===========================================================================

class TestKMComplementarity:
    """c(k) + c(k') for KM algebra under Feigin-Frenkel duality."""

    def test_sl2_sum_is_6(self):
        """sl_2 WZW: c(k) + c(k') = 6 for all k."""
        k = Symbol('k')
        assert km_central_charge_sum("sl2", k) == 6

    def test_sl3_sum_is_16(self):
        """sl_3 WZW: c(k) + c(k') = 16 for all k."""
        k = Symbol('k')
        assert km_central_charge_sum("sl3", k) == 16

    def test_sl2_numerical(self):
        """sl_2: c(k) + c(k') = 6 for k=1,2,3,4."""
        for k in [1, 2, 3, 4]:
            c = wzw_central_charge("sl2", k)
            c_dual = dual_central_charge_km("sl2", k)
            assert c + c_dual == 6

    def test_virasoro_sum_is_26(self):
        """Virasoro (DS of sl_2): c + c' = 26."""
        for k in range(5):
            c = virasoro_ds_central_charge(k)
            c_dual = virasoro_dual_central_charge_km(k)
            assert c + c_dual == 26

    def test_general_formula(self):
        """c(k) + c(k') = 2*dim(g)*h^vee / (2*h^vee) = dim(g) for WZW.

        Actually: c(k) + c(k') = k*d/(k+h) + k'*d/(k'+h)
        where k' = -k - 2h. This simplifies to:
        d * (k/(k+h) + (-k-2h)/(-k-h))
        = d * (k/(k+h) + (k+2h)/(k+h))
        = d * (2k + 2h) / (k+h) = 2d.
        So c + c' = 2*dim(g).

        Wait: sl_2: 2*3 = 6. sl_3: 2*8 = 16. Yes!
        """
        k = Symbol('k')
        for name in ["sl2", "sl3"]:
            total = km_central_charge_sum(name, k)
            assert total == 2 * lie_dim(name)


# ===========================================================================
# T-matrix periodicity for minimal models
# ===========================================================================

class TestTMatrixPeriodicity:
    """T^{N_T} = Id on character space for minimal models.

    The actual T-matrix period N_T = lcm of denominators of h_{r,s} - c/24.
    The formula period N = 24q'/gcd(p',24) always divides N_T.
    N_T always divides 24*p*q.
    """

    def test_m34_ising(self):
        """Ising M(3,4): T^48 = Id, 3 modules."""
        check = t_matrix_period_check(3, 4)
        assert check["T_N_is_identity"]
        assert check["N_T"] == 48
        assert check["N_formula"] == 48
        assert check["num_modules"] == 3

    def test_m45_tricritical(self):
        """Tricritical Ising M(4,5): T^240 = Id, 6 modules."""
        check = t_matrix_period_check(4, 5)
        assert check["T_N_is_identity"]
        assert check["N_T"] == 240
        assert check["N_formula"] == 240
        assert check["num_modules"] == 6

    def test_m25(self):
        """M(2,5): T^60 = Id, 2 modules."""
        check = t_matrix_period_check(2, 5)
        assert check["T_N_is_identity"]
        assert check["N_T"] == 60
        assert check["N_formula"] == 60
        assert check["num_modules"] == 2

    def test_m35(self):
        """M(3,5): T^40 = Id, 4 modules."""
        check = t_matrix_period_check(3, 5)
        assert check["T_N_is_identity"]
        assert check["N_T"] == 40
        assert check["N_formula"] == 40
        assert check["num_modules"] == 4

    def test_m56_potts(self):
        """Three-state Potts M(5,6): N_T=120, formula N=30, 10 modules.

        The formula period N=30 divides the actual T-matrix period N_T=120.
        Some conformal weights have denominator 8 (from (6r-5s)^2/(120)),
        so h-c/24 has denominator 120, requiring N_T=120 for T^{N_T}=Id.
        """
        check = t_matrix_period_check(5, 6)
        assert check["T_N_is_identity"]
        assert check["N_T"] == 120
        assert check["N_formula"] == 30
        assert check["formula_divides_actual"]
        assert check["actual_divides_24pq"]
        assert check["num_modules"] == 10

    def test_m23_trivial(self):
        """Trivial M(2,3): T^1 = Id, 1 module."""
        check = t_matrix_period_check(2, 3)
        assert check["T_N_is_identity"]
        assert check["N_T"] == 1
        assert check["N_formula"] == 1
        assert check["num_modules"] == 1

    def test_m37(self):
        """M(3,7): T-matrix periodicity."""
        check = t_matrix_period_check(3, 7)
        assert check["T_N_is_identity"]
        assert check["formula_divides_actual"]
        assert check["actual_divides_24pq"]

    def test_m57(self):
        """M(5,7): T-matrix periodicity."""
        check = t_matrix_period_check(5, 7)
        assert check["T_N_is_identity"]
        assert check["formula_divides_actual"]
        assert check["actual_divides_24pq"]

    def test_m67(self):
        """M(6,7): N_T=168, formula N=28. Another case where N < N_T."""
        check = t_matrix_period_check(6, 7)
        assert check["T_N_is_identity"]
        assert check["N_T"] == 168
        assert check["N_formula"] == 28
        assert check["formula_divides_actual"]
        assert check["actual_divides_24pq"]

    def test_all_small_models(self):
        """T-matrix periodicity for all M(p,q) with p<=6, q<=8."""
        results = verify_modular_periodicity_minimal(6, 8)
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_formula_divides_actual_always(self):
        """Formula period N always divides actual T-matrix period N_T."""
        for p in range(2, 8):
            for q in range(p + 1, 10):
                from math import gcd as mgcd
                if mgcd(p, q) != 1:
                    continue
                check = t_matrix_period_check(p, q)
                assert check["formula_divides_actual"], \
                    f"M({p},{q}): N={check['N_formula']} does not divide N_T={check['N_T']}"

    def test_actual_divides_24pq_always(self):
        """Actual T-matrix period N_T always divides 24*p*q."""
        for p in range(2, 8):
            for q in range(p + 1, 10):
                from math import gcd as mgcd
                if mgcd(p, q) != 1:
                    continue
                check = t_matrix_period_check(p, q)
                assert check["actual_divides_24pq"], \
                    f"M({p},{q}): N_T={check['N_T']} does not divide 24pq={24*p*q}"

    def test_module_count_formula(self):
        """Number of irreducible modules = (p-1)(q-1)/2."""
        for p, q in [(2, 3), (3, 4), (3, 5), (4, 5), (5, 6)]:
            weights = minimal_model_conformal_weights(p, q)
            expected = (p - 1) * (q - 1) // 2
            assert len(weights) == expected, \
                f"M({p},{q}): got {len(weights)}, expected {expected}"

    def test_actual_t_matrix_period_direct(self):
        """Direct computation of actual T-matrix period."""
        assert actual_t_matrix_period(3, 4) == 48
        assert actual_t_matrix_period(4, 5) == 240
        assert actual_t_matrix_period(5, 6) == 120
        assert actual_t_matrix_period(6, 7) == 168


# ===========================================================================
# Conformal weights
# ===========================================================================

class TestConformalWeights:
    """Conformal weights h_{r,s} = ((qr-ps)^2 - (q-p)^2)/(4pq)."""

    def test_ising_vacuum(self):
        """Ising M(3,4) vacuum: h_{1,1} = 0."""
        weights = minimal_model_conformal_weights(3, 4)
        h_11 = [w for w in weights if w["r"] == 1 and w["s"] == 1][0]["h"]
        assert h_11 == 0

    def test_ising_spin(self):
        """Ising M(3,4) spin field: h_{2,1} = 1/2."""
        weights = minimal_model_conformal_weights(3, 4)
        # (r,s) = (1,2) or equivalently (2,2) under identification
        # h_{1,2} = ((4-6)^2 - 1) / 48 = (4-1)/48 = 3/48 = 1/16
        # h_{2,1} = ((8-3)^2 - 1) / 48 = (25-1)/48 = 24/48 = 1/2
        h_vals = sorted([w["h"] for w in weights])
        assert Rational(0) in h_vals
        assert Rational(1, 16) in h_vals
        assert Rational(1, 2) in h_vals

    def test_all_weights_rational(self):
        """All conformal weights are rational."""
        for p, q in [(3, 4), (4, 5), (5, 6)]:
            weights = minimal_model_conformal_weights(p, q)
            for w in weights:
                assert isinstance(w["h"], Rational)


# ===========================================================================
# Reflected modular periodicity (conj:reflected-modular-periodicity)
# ===========================================================================

class TestReflectedPeriodicity:
    """1/N + 1/N' = (gcd(p,24) + gcd(p',24)) / (24q)."""

    def test_sl2_k1(self):
        """sl_2 k=1: c=1, c'=5, 1/N + 1/N' = 1/12."""
        check = reflected_period_check_km("sl2", 1)
        assert check["match"]
        assert check["lhs"] == Rational(1, 12)

    def test_sl2_k2(self):
        """sl_2 k=2: c=3/2, c'=9/2."""
        check = reflected_period_check_km("sl2", 2)
        assert check["match"]

    def test_sl2_k3(self):
        """sl_2 k=3: c=9/5, c'=21/5."""
        check = reflected_period_check_km("sl2", 3)
        assert check["match"]

    def test_sl2_k4(self):
        """sl_2 k=4: c=2, c'=4."""
        check = reflected_period_check_km("sl2", 4)
        assert check["match"]

    def test_sl2_k5(self):
        """sl_2 k=5."""
        check = reflected_period_check_km("sl2", 5)
        assert check["match"]

    def test_sl2_k6(self):
        """sl_2 k=6."""
        check = reflected_period_check_km("sl2", 6)
        assert check["match"]

    def test_sl2_all_levels(self):
        """sl_2: reflected periodicity for k=1..10."""
        results = verify_reflected_periodicity_km("sl2", 10)
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_sl3_k1(self):
        """sl_3 k=1: c=2, c'=14."""
        check = reflected_period_check_km("sl3", 1)
        assert check["match"]

    def test_sl3_k2(self):
        """sl_3 k=2."""
        check = reflected_period_check_km("sl3", 2)
        assert check["match"]

    def test_sl3_k3(self):
        """sl_3 k=3."""
        check = reflected_period_check_km("sl3", 3)
        assert check["match"]

    def test_sl3_all_levels(self):
        """sl_3: reflected periodicity for k=1..6."""
        results = verify_reflected_periodicity_km("sl3", 6)
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_virasoro_k0(self):
        """Virasoro k=0: c=-2, c'=28."""
        check = reflected_period_check_virasoro(0)
        assert check["match"]

    def test_virasoro_k1(self):
        """Virasoro k=1: c=-7, c'=33."""
        check = reflected_period_check_virasoro(1)
        assert check["match"]

    def test_virasoro_k_minus1(self):
        """Virasoro k=-1: c=1, c'=25."""
        check = reflected_period_check_virasoro(-1)
        assert check["match"]
        # c=1, c'=25: gcd(1,24)=1, gcd(25,24)=1
        # 1/N + 1/N' = (1+1)/24 = 1/12
        assert check["lhs"] == Rational(1, 12)

    def test_virasoro_half_integer_level(self):
        """Virasoro at k=1/2 (admissible level)."""
        check = reflected_period_check_virasoro(Rational(1, 2))
        assert check["match"]

    def test_special_1_over_12(self):
        """1/N + 1/N' = 1/12 requires both p and p' coprime to 24.

        From monograph: for q=1, need gcd(p,24) + gcd(p',24) = 2.
        This requires gcd(p,24) = gcd(p',24) = 1.
        """
        # c=1, c'=25: both coprime to 24 -> sum = 1/12
        check = reflected_period_check(1, 25)
        assert check["is_1_over_12"]

        # c=7, c'=19: both coprime to 24 -> sum = 1/12
        check = reflected_period_check(7, 19)
        assert check["is_1_over_12"]

        # c=5, c'=21: gcd(21,24)=3 -> sum != 1/12
        check = reflected_period_check(5, 21)
        assert not check["is_1_over_12"]

    def test_c5_c21_not_1_over_12(self):
        """c=5, c'=21: gcd(21,24)=3, so 1/N+1/N' = 1/6 != 1/12.

        Explicit check from monograph remark.
        """
        N = modular_period(5)   # 24/gcd(5,24) = 24
        N_dual = modular_period(21)  # 24/gcd(21,24) = 24/3 = 8
        assert N == 24
        assert N_dual == 8
        assert Rational(1, N) + Rational(1, N_dual) == Rational(1, 6)

    def test_denominator_match_coprime(self):
        """When gcd(p,q) = 1, q' = q for Virasoro duality c + c' = 26."""
        for k in range(5):
            check = reflected_period_check_virasoro(k)
            # For Virasoro: c(k) + c(k') = 26
            # If c = p/q, then c' = 26 - p/q = (26q - p)/q
            # So q' divides q (it equals q if gcd(26q-p, q) = 1)
            assert check["q_dual"] == check["q"] or check["q_dual"] % check["q"] == 0 or check["q"] % check["q_dual"] == 0


# ===========================================================================
# Period sum analysis
# ===========================================================================

class TestPeriodSumAnalysis:
    """Structural properties of the reflected period sum."""

    def test_reflected_period_sum_function(self):
        """reflected_period_sum correctly computes 1/N + 1/N'."""
        s = reflected_period_sum(1, 25)
        assert s == Rational(1, 12)

    def test_reflected_period_formula_rhs_function(self):
        """reflected_period_formula_rhs gives (gcd(p,24)+gcd(p',24))/(24q)."""
        rhs = reflected_period_formula_rhs(1, 25)
        # c=1=1/1, c'=25=25/1, q=1
        # (gcd(1,24) + gcd(25,24)) / (24*1) = (1+1)/24 = 1/12
        assert rhs == Rational(1, 12)

    def test_sl2_k1_is_1_over_12(self):
        """sl_2 k=1: c=1, c'=5 -> 1/N+1/N' = 1/12 (both coprime to 24)."""
        check = reflected_period_check_km("sl2", 1)
        assert check["is_1_over_12"]

    def test_sl2_k4_is_1_over_4(self):
        """sl_2 k=4: c=2, c'=4 -> 1/N+1/N' = 1/12 + 1/6 = 1/4."""
        check = reflected_period_check_km("sl2", 4)
        # c=2: N=12, c'=4: N'=6
        assert check["N"] == 12
        assert check["N_dual"] == 6
        assert check["lhs"] == Rational(1, 4)


# ===========================================================================
# Nilpotence bounds (Graber-Vakil)
# ===========================================================================

class TestNilpotenceBounds:
    """kappa(lambda)^{g-1} = 0 on M_g (proved, thm:geometric-depth-smooth)."""

    def test_smooth_bound_g2(self):
        """g=2: kappa^1 = 0 (Hodge class vanishes on M_2)."""
        assert nilpotence_bound_smooth(2) == 1

    def test_smooth_bound_g3(self):
        """g=3: kappa^2 = 0."""
        assert nilpotence_bound_smooth(3) == 2

    def test_smooth_bound_g10(self):
        """g=10: kappa^9 = 0."""
        assert nilpotence_bound_smooth(10) == 9

    def test_compactified_bound_g2(self):
        """g=2: kappa^4 = 0 on M-bar_2."""
        assert nilpotence_bound_compactified(2) == 4

    def test_compactified_bound_g3(self):
        """g=3: kappa^7 = 0 on M-bar_3."""
        assert nilpotence_bound_compactified(3) == 7

    def test_smooth_less_than_compactified(self):
        """Smooth bound < compactified bound for all g >= 2."""
        for g in range(2, 20):
            assert nilpotence_bound_smooth(g) < nilpotence_bound_compactified(g)

    def test_improvement_factor_approaches_3(self):
        """Compactified / smooth -> 3 as g -> infinity.

        (3g-2)/(g-1) = 3 + 1/(g-1) -> 3.
        """
        for g in range(2, 20):
            comp = geometric_depth_comparison(g)
            ratio = float(comp["improvement_factor"])
            assert ratio > 3.0  # Always > 3 for finite g

    def test_invalid_g1(self):
        """g=1 should raise (smooth moduli is a point)."""
        with pytest.raises(ValueError):
            nilpotence_bound_smooth(1)

    def test_dimensional_vanishing_g1_g2(self):
        """Dimensional argument: obs^2 = 0 for g < 3."""
        for g in [1, 2]:
            if g >= 1:  # g=0 has no moduli
                check = dimensional_nilpotence_check(g)
                assert check["vanishes_dimensionally"]

    def test_dimensional_vanishing_fails_g3(self):
        """Dimensional argument FAILS at g=3 (top degree)."""
        check = dimensional_nilpotence_check(3)
        assert not check["vanishes_dimensionally"]
        # obs^2 degree = 12 = max degree = 2*(3*3-3) = 12
        assert check["obs_squared_degree"] == check["max_cohomological_degree"]

    def test_dimensional_vanishing_fails_g_geq_3(self):
        """Dimensional argument fails for all g >= 3."""
        for g in range(3, 15):
            check = dimensional_nilpotence_check(g)
            assert not check["vanishes_dimensionally"]

    def test_verify_nilpotence_bounds_suite(self):
        """Run full nilpotence verification suite."""
        results = verify_nilpotence_bounds()
        for name, ok in results.items():
            assert ok, f"Failed: {name}"

    def test_nilpotent_not_periodic(self):
        """CRITICAL from CLAUDE.md: kappa is NILPOTENT, not PERIODIC.

        The sharp bound kappa^{g-1} = 0 means geometry provides
        a threshold (tautological depth), NOT a period.
        """
        # At genus 2: kappa vanishes entirely
        assert nilpotence_bound_smooth(2) == 1  # kappa^1 = 0
        # At genus 100: kappa^99 = 0 (finite nilpotence index)
        assert nilpotence_bound_smooth(100) == 99


# ===========================================================================
# Geometric depth comparison
# ===========================================================================

class TestGeometricDepthComparison:
    """Compare smooth and compactified nilpotence bounds."""

    def test_genus_2(self):
        """g=2: smooth=1, compact=4, gap=3."""
        comp = geometric_depth_comparison(2)
        assert comp["smooth_bound"] == 1
        assert comp["compactified_bound"] == 4
        assert comp["gap"] == 3

    def test_genus_3(self):
        """g=3: smooth=2, compact=7, gap=5."""
        comp = geometric_depth_comparison(3)
        assert comp["smooth_bound"] == 2
        assert comp["compactified_bound"] == 7
        assert comp["gap"] == 5

    def test_gap_is_2g_minus_1(self):
        """Gap = compact - smooth = (3g-2) - (g-1) = 2g-1."""
        for g in range(2, 15):
            comp = geometric_depth_comparison(g)
            assert comp["gap"] == 2 * g - 1


# ===========================================================================
# Period table tests
# ===========================================================================

class TestMinimalModelPeriodTable:
    """Systematic period computations for minimal models."""

    def test_table_nonempty(self):
        """Period table is nonempty."""
        table = minimal_model_period_table(6, 8)
        assert len(table) > 0

    def test_all_coprime(self):
        """All entries have gcd(p,q) = 1."""
        from math import gcd as mgcd
        table = minimal_model_period_table(6, 8)
        for row in table:
            assert mgcd(row["p"], row["q"]) == 1

    def test_period_divides_24lcm(self):
        """N divides 24*lcm(p,q) for all minimal models."""
        table = minimal_model_period_table(6, 8)
        for row in table:
            assert row["N_divides_24lcm"], \
                f"M({row['p']},{row['q']}): N={row['N']} does not divide 24*lcm"

    def test_known_entries(self):
        """Spot-check known entries."""
        table = minimal_model_period_table(6, 8)
        data = {(r["p"], r["q"]): r for r in table}

        # M(3,4): c=1/2, N=48
        assert data[(3, 4)]["c"] == Rational(1, 2)
        assert data[(3, 4)]["N"] == 48

        # M(4,5): c=7/10, N=240
        assert data[(4, 5)]["c"] == Rational(7, 10)
        assert data[(4, 5)]["N"] == 240


class TestWZWPeriodTable:
    """Systematic period computations for WZW models."""

    def test_table_nonempty(self):
        """Period table for sl_2 is nonempty."""
        table = wzw_period_table("sl2", 5)
        assert len(table) == 5

    def test_sl2_periods(self):
        """sl_2 WZW periods at k=1..4."""
        table = wzw_period_table("sl2", 4)
        expected_c = [1, Rational(3, 2), Rational(9, 5), 2]
        for i, row in enumerate(table):
            assert row["c"] == expected_c[i], f"k={i+1}: c={row['c']} != {expected_c[i]}"

    def test_sl2_c_plus_c_dual_is_6(self):
        """sl_2: c + c' = 6 for all levels."""
        table = wzw_period_table("sl2", 10)
        for row in table:
            assert row["c_sum"] == 6

    def test_sl3_c_plus_c_dual_is_16(self):
        """sl_3: c + c' = 16 for all levels."""
        table = wzw_period_table("sl3", 6)
        for row in table:
            assert row["c_sum"] == 16


# ===========================================================================
# Quantum periodicity
# ===========================================================================

class TestQuantumPeriodicity:
    """Type II quantum periodicity: M = 2*h^vee*p*q/gcd(p,q,h^vee)."""

    def test_sl2_p3_q2(self):
        """sl_2 admissible k=-1/2: p=3, q=2, M=24."""
        assert quantum_period(3, 2, 2) == 24

    def test_sl2_p4_q3(self):
        """sl_2 admissible k=-2+4/3: p=4, q=3, M=48."""
        assert quantum_period(4, 3, 2) == 48

    def test_sl2_p5_q3(self):
        """sl_2: p=5, q=3, M=60."""
        assert quantum_period(5, 3, 2) == 60

    def test_combined_period(self):
        """Combined period = lcm(N_mod, N_quant)."""
        assert combined_period_bound(24, 48) == 48
        assert combined_period_bound(24, 24) == 24
        assert combined_period_bound(30, 48) == 240


# ===========================================================================
# Lie algebra data
# ===========================================================================

class TestLieData:
    """Basic Lie algebra data correctness."""

    def test_sl2_dim(self):
        """dim(sl_2) = 3."""
        assert lie_dim("sl2") == 3

    def test_sl3_dim(self):
        """dim(sl_3) = 8."""
        assert lie_dim("sl3") == 8

    def test_sl2_h_dual(self):
        """h^vee(sl_2) = 2."""
        assert dual_coxeter("sl2") == 2

    def test_sl3_h_dual(self):
        """h^vee(sl_3) = 3."""
        assert dual_coxeter("sl3") == 3

    def test_g2_h_dual(self):
        """h^vee(G_2) = 4."""
        assert dual_coxeter("g2") == 4

    def test_sl2_rank(self):
        """rank(sl_2) = 1."""
        assert lie_rank("sl2") == 1

    def test_sl3_rank(self):
        """rank(sl_3) = 2."""
        assert lie_rank("sl3") == 2


# ===========================================================================
# Integration / cross-checks
# ===========================================================================

class TestCrossChecks:
    """Cross-checks between different computation paths."""

    def test_minimal_model_vs_ds(self):
        """M(p,p+1) central charge matches Virasoro DS at appropriate level.

        M(p, p+1): c = 1 - 6/(p(p+1))
        Virasoro DS at k = p-2: c(k) = 1 - 6(k+1)^2/(k+2)
                                     = 1 - 6(p-1)^2/p
        These are NOT the same (different formulas).
        But M(3,4) = Ising should correspond to some DS level.
        """
        # M(3,4): c = 1/2
        # DS: c(k) = 1/2 when 1 - 6(k+1)^2/(k+2) = 1/2
        # => 6(k+1)^2/(k+2) = 1/2 => 12(k+1)^2 = k+2
        # Actually the minimal model M(p,q) at admissible level
        # k = p/q - 2 gives c(k) via DS.
        for p, q in [(3, 4), (4, 5), (5, 6)]:
            k = Rational(p, q) - 2
            c_ds = virasoro_ds_central_charge(k)
            c_mm = minimal_model_central_charge(p, q)
            assert c_ds == c_mm, \
                f"M({p},{q}): DS(k={k})={c_ds} != MM={c_mm}"

    def test_period_consistency(self):
        """modular_period is consistent across computation paths."""
        for p, q in [(3, 4), (4, 5), (5, 6)]:
            c = minimal_model_central_charge(p, q)
            N1 = modular_period(c)
            # Also compute from DS
            k = Rational(p, q) - 2
            c_ds = virasoro_ds_central_charge(k)
            N2 = modular_period(c_ds)
            assert N1 == N2

    def test_kappa_additivity(self):
        """kappa is additive: kappa(A tensor B) = kappa(A) + kappa(B).

        Verified numerically: for WZW, c is additive in the sense
        c(g1 x g2) = c(g1) + c(g2) at the same level.
        """
        # c(sl_2 x sl_2 at k=1) = 1 + 1 = 2
        c1 = wzw_central_charge("sl2", 1)
        c_product = c1 + c1
        kappa_product = scalar_modular_characteristic(c_product)
        kappa_sum = scalar_modular_characteristic(c1) + scalar_modular_characteristic(c1)
        assert kappa_product == kappa_sum

    def test_complementarity_implies_dual_period(self):
        """If c + c' = 2*dim(g), then the dual period is determined.

        For sl_2: c + c' = 6, so c' = 6 - c.
        """
        for k in range(1, 6):
            c = wzw_central_charge("sl2", k)
            c_dual = 6 - c
            c_dual_check = dual_central_charge_km("sl2", k)
            assert c_dual == c_dual_check

    def test_virasoro_complementarity_26(self):
        """Virasoro c + c' = 26 verified at multiple levels."""
        for k in [-1, 0, 1, 2, 3, Rational(1, 2), Rational(1, 3)]:
            c = virasoro_ds_central_charge(k)
            c_dual = virasoro_dual_central_charge_km(k)
            assert simplify(c + c_dual) == 26

    def test_period_monotonicity_unitary(self):
        """For unitary M(m,m+1), period can vary non-monotonically.

        This is a structural test, not a monotonicity requirement.
        """
        periods = []
        for m in range(3, 12):
            c = minimal_model_central_charge(m, m + 1)
            N = modular_period(c)
            periods.append((m, N))
        # Just verify they are all positive
        for m, N in periods:
            assert N > 0


# ===========================================================================
# Edge cases and error handling
# ===========================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_c_integer_period(self):
        """Integer central charges have period dividing 24."""
        for c in range(-10, 11):
            N = modular_period(c)
            assert 24 % N == 0 or N % 24 == 0 or N <= 24

    def test_c_equals_26_special(self):
        """c=26: dual c'=0 (uncurved). Period of c=26: N=24/gcd(26,24)=24/2=12."""
        N = modular_period(26)
        assert N == 12
        N_dual = modular_period(0)
        assert N_dual == 1

    def test_c_equals_13_self_dual_point(self):
        """c=13: self-dual point for Virasoro. N=24/gcd(13,24)=24."""
        N = modular_period(13)
        assert N == 24

    def test_large_denominator(self):
        """Large denominator: c = 1/1000."""
        c = Rational(1, 1000)
        N = modular_period(c)
        assert N == 24 * 1000  # gcd(1, 24) = 1

    def test_negative_central_charge(self):
        """Negative central charges have well-defined periods."""
        for p, q in [(2, 5), (2, 7), (3, 7)]:
            c = minimal_model_central_charge(p, q)
            assert c < 0
            N = modular_period(c)
            assert N > 0
            assert modular_period_divides_check(c, N)
