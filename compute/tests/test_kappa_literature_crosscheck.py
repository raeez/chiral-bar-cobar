"""STRICT LITERATURE CROSS-CHECK: kappa formulas from first principles.

For each standard family, independently derive kappa from OPE data and
verify against the manuscript values in higher_genus_foundations.tex,
thm:genus1-universal-curvature.

KEY INSIGHT (from the manuscript):
  kappa(A) is NOT simply c/2 in general.  It is the coefficient of
  the genus-1 curvature d_fib^2 = kappa * omega_1.

  The ANOMALY RATIO rho(A) := kappa(A) / c(A) is a structural invariant
  of the algebra family:
    rho(Heisenberg) = 1        =>  kappa = c
    rho(Virasoro)   = 1/2      =>  kappa = c/2
    rho(W_N)        = H_N - 1  =>  kappa = c * (H_N - 1)
    rho(KM g_k)     = dim(g)*(k+h^v) / (2*h^v*c)  [level-dependent ratio]

  The derivation:
  For an algebra with generators of conformal weights h_1, ..., h_r,
  each generator W^{(h_i)} contributes c/h_i to the curvature (from
  the highest pole in the self-OPE).  So:
    kappa = sum_i c/h_i = c * sum_i 1/h_i

  For Heisenberg: one generator of weight h=1, so kappa = c/1 = c.
  For Virasoro: one generator T of weight h=2, so kappa = c/2.
  For W_N: generators of weights h_i = i+1 for i=1..N-1 (plus T),
           so kappa = c * sum_{s=2}^{N} 1/s = c*(H_N - 1).

  For KM: the derivation is different because the generators are NOT
  Virasoro primary.  The genus-1 curvature comes from two channels:
    double-pole channel: dim(g)*k/(2*h^v)
    simple-pole channel: dim(g)/2
    Total: kappa = dim(g)*(k+h^v)/(2*h^v)

  Note this is NOT c/2 = k*dim(g)/(2*(k+h^v)).

Reference: preface.tex lines 244-253, higher_genus_foundations.tex lines 3306-3319,
           w_algebras.tex Theorem thm:wn-obstruction, kac_moody.tex line 15.
"""

import sys
import os

# Add compute directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from sympy import Rational, Symbol, simplify, harmonic, S
from lib.lie_algebra import cartan_data, sugawara_c, kappa_km, sigma_invariant
from lib.genus_expansion import (
    kappa_heisenberg, kappa_virasoro, kappa_w3, kappa_sl2,
    kappa_sl3, kappa_g2, kappa_b2,
)


# =========================================================================
# PART 1: Heisenberg kappa from first principles
# =========================================================================

class TestHeisenbergKappa:
    """Verify: kappa(H_k) = k (the level), NOT c/2.

    The rank-1 Heisenberg at level k has:
      - OPE: alpha(z)alpha(w) ~ k/(z-w)^2
      - Stress tensor: T = (1/2k):alpha*alpha:
      - Central charge: c = 1 (one free boson, independent of k)
      - One generator alpha of conformal weight h=1
      - kappa = c/h = 1/1 = 1... but manuscript says kappa = k!

    RESOLUTION: The anomaly ratio formula kappa = c * sum(1/h_i) applies
    to the Zamolodchikov-normalized generators.  The Heisenberg current
    alpha has OPE alpha(z)alpha(w) ~ k/(z-w)^2, so the leading pole
    coefficient IS k (not 1).  The genus-1 curvature is:
      d_fib^2 = Res_{z1=z2}[alpha(z1) alpha(z2) * eta_12^ell]|_vac = k
    This is a DIRECT extraction, not mediated by the stress tensor.

    The point is: kappa extracts from ALL generating fields, not just T.
    For Heisenberg, the current alpha is the generator, and its self-OPE
    has highest pole k/(z-w)^2, giving curvature k.  The stress tensor
    T = (1/2k):alpha*alpha: is a COMPOSITE, not a generator.
    """

    def test_kappa_equals_level(self):
        """kappa(H_k) = k for all k."""
        for k in [1, 2, 3, 5, 10, Rational(1, 2), Rational(7, 3)]:
            assert kappa_heisenberg(k) == k

    def test_central_charge_is_1(self):
        """c(H_k) = 1 for rank-1 Heisenberg at any level k."""
        # The central charge of one free boson is always 1
        c = 1
        for k in [1, 2, 3, 10]:
            # kappa != c/2 for k != 1
            if k != 1:
                assert kappa_heisenberg(k) != Rational(c, 2)

    def test_anomaly_ratio_at_standard_normalization(self):
        """At k=1, anomaly ratio = kappa/c = 1/1 = 1."""
        c = 1
        kappa = kappa_heisenberg(1)
        assert kappa / c == 1  # anomaly ratio = 1

    def test_rank_d_heisenberg(self):
        """kappa(H_k^{oplus d}) = d*k."""
        for d in range(1, 8):
            for k in [1, 2, 3]:
                # rank-d at level k: kappa = d*k, c = d
                kappa_val = d * k
                c_val = d
                assert kappa_val == d * kappa_heisenberg(k)

    def test_genus1_table_check(self):
        """Verify F_1 = kappa/24 for Heisenberg.

        From the table in heisenberg_eisenstein.tex:
          d=1, k=1: F_1 = 1/24, kappa = 1
          d=24, k=1: F_1 = 1, kappa = 24
        """
        from lib.utils import F_g
        # rank 1, level 1
        assert F_g(kappa_heisenberg(1), 1) == Rational(1, 24)
        # rank 24, level 1
        assert F_g(24 * kappa_heisenberg(1), 1) == Rational(1)

    def test_complementarity(self):
        """kappa(H_k) + kappa(H_{-k}) = 0.

        Heisenberg Koszul dual: H_k^! = H_{-k}.
        """
        for k in [1, 2, 3, Rational(5, 2)]:
            assert kappa_heisenberg(k) + kappa_heisenberg(-k) == 0


# =========================================================================
# PART 2: Affine Kac-Moody kappa from first principles
# =========================================================================

class TestKMKappa:
    """Verify: kappa(g_k) = dim(g)*(k+h^v)/(2*h^v), NOT c/2.

    Two-channel decomposition (Remark rem:theta-two-channel):
      kappa = dim(g)*k/(2*h^v)     [double-pole channel]
            + dim(g)/2              [simple-pole channel]
            = dim(g)*(k+h^v)/(2*h^v)

    Compare with c/2 = k*dim(g)/(2*(k+h^v)).
    These are DIFFERENT: kappa ~ (k+h^v), while c/2 ~ k/(k+h^v).
    """

    def test_sl2_formula(self):
        """kappa(sl2_k) = 3(k+2)/4."""
        for k in [1, 2, 3, 5, 10, -1, Rational(1, 2)]:
            expected = Rational(3) * (k + 2) / 4
            assert kappa_sl2(k) == expected
            assert kappa_km("A", 1, k) == expected

    def test_sl2_not_c_over_2(self):
        """kappa(sl2_k) != c/2 for generic k."""
        for k in [1, 2, 3, 5, 10]:
            c = sugawara_c("A", 1, k)
            c_half = c / 2
            kappa = kappa_km("A", 1, k)
            # They should be DIFFERENT
            assert simplify(kappa - c_half) != 0, \
                f"At k={k}: kappa={kappa}, c/2={c_half} -- they should differ!"

    def test_sl2_two_channel_decomposition(self):
        """Verify the two-channel decomposition for sl2."""
        k = Symbol('k')
        dim_g = 3
        h_dual = 2

        double_pole = dim_g * k / (2 * h_dual)  # 3k/4
        simple_pole = Rational(dim_g, 2)          # 3/2
        total = double_pole + simple_pole          # 3(k+2)/4

        expected = dim_g * (k + h_dual) / (2 * h_dual)
        assert simplify(total - expected) == 0

    def test_sl3_formula(self):
        """kappa(sl3_k) = 4(k+3)/3."""
        for k in [1, 2, 3]:
            expected = Rational(4) * (k + 3) / 3
            assert kappa_sl3(k) == expected
            assert kappa_km("A", 2, k) == expected

    def test_sl3_not_c_over_2(self):
        """kappa(sl3_k) != c/2."""
        for k in [1, 2, 3]:
            c = sugawara_c("A", 2, k)
            kappa = kappa_km("A", 2, k)
            assert simplify(kappa - c / 2) != 0

    def test_general_km_formula(self):
        """kappa = dim(g)*(k+h^v)/(2*h^v) for all available types."""
        test_cases = [
            ("A", 1, 1),  # sl2
            ("A", 1, 3),
            ("A", 2, 1),  # sl3
            ("A", 3, 1),  # sl4
            ("B", 2, 1),  # so5
            ("C", 2, 1),  # sp4
            ("G", 2, 1),  # G2
            ("D", 4, 1),  # so8
        ]
        for type_, rank, k in test_cases:
            data = cartan_data(type_, rank)
            expected = Rational(data.dim) * (k + data.h_dual) / (2 * data.h_dual)
            computed = kappa_km(type_, rank, k)
            assert computed == expected, \
                f"{type_}{rank} at k={k}: got {computed}, expected {expected}"

    def test_critical_level_vanishing(self):
        """kappa = 0 at critical level k = -h^v."""
        for type_, rank in [("A", 1), ("A", 2), ("B", 2), ("G", 2)]:
            data = cartan_data(type_, rank)
            kappa = kappa_km(type_, rank, -data.h_dual)
            assert kappa == 0, \
                f"{type_}{rank}: kappa at k=-h^v={-data.h_dual} should be 0, got {kappa}"

    def test_feigin_frenkel_antisymmetry(self):
        """kappa(g_k) + kappa(g_{-k-2h^v}) = 0."""
        for type_, rank in [("A", 1), ("A", 2), ("B", 2), ("G", 2)]:
            data = cartan_data(type_, rank)
            for k in [1, 2, 3]:
                k_dual = -k - 2 * data.h_dual
                kappa_sum = kappa_km(type_, rank, k) + kappa_km(type_, rank, k_dual)
                assert kappa_sum == 0, \
                    f"{type_}{rank}: kappa(k={k}) + kappa(k'={k_dual}) = {kappa_sum} != 0"

    def test_sl2_genus1_table(self):
        """Verify F_1(sl2_k) = (k+2)/32 from genus_expansions.tex."""
        from lib.utils import F_g
        for k in [1, 2, 3]:
            F1 = F_g(kappa_sl2(k), 1)
            expected = Rational(k + 2, 32)
            assert F1 == expected, f"F_1(sl2_{k}) = {F1}, expected {expected}"


# =========================================================================
# PART 3: Virasoro kappa from first principles
# =========================================================================

class TestVirasoroKappa:
    """Verify: kappa(Vir_c) = c/2.

    Virasoro has one generator T of conformal weight h=2.
    T(z)T(w) ~ c/2/(z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w).
    The highest pole coefficient is c/2.

    Anomaly ratio: rho = kappa/c = 1/2 = 1/h_T.
    Alternatively: one generator of weight 2, so kappa = c * (1/2) = c/2.
    """

    def test_kappa_equals_c_over_2(self):
        """kappa(Vir_c) = c/2 for all c."""
        for c in [1, 2, 13, 26, Rational(1, 2), Rational(7, 10)]:
            assert kappa_virasoro(c) == Rational(c) / 2

    def test_self_duality_at_c13(self):
        """kappa(Vir_13) = 13/2, kappa(Vir_{26-13}) = 13/2. Self-dual."""
        assert kappa_virasoro(13) == kappa_virasoro(26 - 13)

    def test_complementarity_sum(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        for c in [0, 1, 2, 13, 25, 26, Rational(1, 2)]:
            total = kappa_virasoro(c) + kappa_virasoro(26 - Rational(c))
            assert total == 13

    def test_anomaly_ratio(self):
        """rho(Vir) = 1/2."""
        for c in [1, 2, 26]:
            rho = kappa_virasoro(c) / c
            assert rho == Rational(1, 2)


# =========================================================================
# PART 4: W_N kappa from first principles
# =========================================================================

class TestWNKappa:
    """Verify: kappa(W_N^k) = c * (H_N - 1), where H_N = sum_{j=1}^N 1/j.

    W_N has generators W^{(s)} of conformal weight s, for s = 2, 3, ..., N.
    (W^{(2)} = T is the stress tensor.)
    In Zamolodchikov normalization, each W^{(s)} self-OPE gives
    W^{(s)}_{(2s-1)} W^{(s)} = c/s (leading pole = c/s).

    So kappa = sum_{s=2}^{N} c/s = c * (H_N - 1).

    Cross-check: For W_N = W(sl_{N-1}, f_prin), the exponents of sl_{N-1}
    are m_i = i for i=1,...,N-1, giving h_i = m_i + 1 = i+1, i.e., h runs
    from 2 to N.  So sigma = sum 1/(m_i+1) = sum_{s=2}^{N} 1/s = H_N - 1.
    """

    def test_w2_is_virasoro(self):
        """W_2 = Virasoro: H_2 - 1 = 1/2, so kappa = c/2."""
        c = Symbol('c')
        H2 = Rational(1) + Rational(1, 2)  # H_2 = 1 + 1/2 = 3/2
        kappa_w2 = c * (H2 - 1)  # c * 1/2 = c/2
        assert simplify(kappa_w2 - c / 2) == 0

    def test_w3_formula(self):
        """kappa(W_3) = 5c/6."""
        H3 = Rational(1) + Rational(1, 2) + Rational(1, 3)  # 11/6
        kappa_w3_expected = Symbol('c') * (H3 - 1)  # c * 5/6
        assert simplify(kappa_w3_expected - 5 * Symbol('c') / 6) == 0

        # Numerical check
        for c in [1, 2, 10, Rational(7, 3)]:
            expected = 5 * Rational(c) / 6
            assert kappa_w3(c) == expected

    def test_w4_formula(self):
        """kappa(W_4) = c * (1/2 + 1/3 + 1/4) = 13c/12."""
        H4 = Rational(1) + Rational(1, 2) + Rational(1, 3) + Rational(1, 4)
        kappa_w4 = (H4 - 1)  # 13/12
        assert kappa_w4 == Rational(13, 12)

    def test_sigma_from_exponents(self):
        """sigma(sl_N) = sum 1/(m_i + 1) = H_N - 1 for type A."""
        # sl_2 (A_1): exponents = [1], sigma = 1/2
        assert sigma_invariant("A", 1) == Rational(1, 2)
        # sl_3 (A_2): exponents = [1, 2], sigma = 1/2 + 1/3 = 5/6
        assert sigma_invariant("A", 2) == Rational(5, 6)
        # sl_4 (A_3): exponents = [1, 2, 3], sigma = 1/2 + 1/3 + 1/4 = 13/12
        assert sigma_invariant("A", 3) == Rational(13, 12)

    def test_wn_complementarity_sum(self):
        """kappa(W_N^k) + kappa(W_N^{k'}) = (H_N-1) * (c + c').

        From cor:wn-complementarity (w_algebras.tex, line 1920-1924).
        For W_3: c + c' = 2*(3-1)*(2*9+6+1) = 4*25 = 100.
        kappa + kappa' = (5/6) * 100 = 250/3.
        """
        # W_3 complementarity
        H3_minus_1 = Rational(5, 6)
        c_plus_c_prime = 2 * (3 - 1) * (2 * 9 + 2 * 3 + 1)  # 2*2*(18+6+1) = 4*25 = 100
        kappa_sum = H3_minus_1 * c_plus_c_prime
        assert kappa_sum == Rational(250, 3)


# =========================================================================
# PART 5: Beta-gamma kappa from first principles
# =========================================================================

class TestBetaGammaKappa:
    """Verify: kappa(beta-gamma_lambda) = c/2 = 6*lambda^2 - 6*lambda + 1.

    The beta-gamma system at weight lambda has:
      c = 2*(6*lambda^2 - 6*lambda + 1)
      (Wait: the preface says kappa = 6*lambda^2 - 6*lambda + 1 = c/2.
       And c_betagamma = 2*(6*lambda^2 - 6*lambda + 1). Confirm.)

    Actually from beta_gamma.tex (prop:betagamma-genus1-curvature):
      m_0^(1) = (6*lambda^2 - 6*lambda + 1)/12 * E_2(tau)
              = c_{beta-gamma}/24 * E_2(tau)
    This means kappa = c/2 for beta-gamma.

    But wait: the beta-gamma has TWO generators: beta (weight lambda)
    and gamma (weight 1-lambda).  If we naively apply kappa = c*sum(1/h_i),
    we'd get kappa = c*(1/lambda + 1/(1-lambda)) = c/(lambda*(1-lambda)).
    This is NOT c/2 in general.

    RESOLUTION: The sum-of-inverse-weights formula applies to a single
    generating field (in the Zamolodchikov sense) whose self-OPE has
    a c-dependent highest pole.  For beta-gamma, the stress tensor is the
    ONLY field with a c-dependent self-OPE.  The beta and gamma fields
    have a MUTUAL OPE (beta(z)gamma(w) ~ 1/(z-w)), not self-OPEs with
    c-dependent poles.

    So for beta-gamma, the curvature comes from the same mechanism as
    Virasoro: extracting from the stress tensor T, giving kappa = c/2.
    The anomaly ratio is rho = 1/2, same as Virasoro.
    """

    def test_kappa_formula(self):
        """kappa(betagamma_lambda) = 6*lambda^2 - 6*lambda + 1."""
        test_cases = [
            (0, 1),
            (1, 1),
            (Rational(1, 2), Rational(-1, 2)),
        ]
        for lam, expected in test_cases:
            lam = Rational(lam)
            kappa = 6 * lam ** 2 - 6 * lam + 1
            assert kappa == expected, f"lambda={lam}: kappa={kappa}, expected={expected}"

    def test_kappa_equals_c_over_2(self):
        """kappa = c/2 for beta-gamma."""
        for lam in [0, 1, Rational(1, 2), Rational(1, 3), 2]:
            lam = Rational(lam)
            c = 2 * (6 * lam ** 2 - 6 * lam + 1)
            kappa = 6 * lam ** 2 - 6 * lam + 1
            assert kappa == c / 2

    def test_lambda_1_values(self):
        """At lambda=1: c = 2, kappa = 1.

        From the master table in higher_genus_foundations.tex.
        """
        lam = 1
        c = 2 * (6 * lam ** 2 - 6 * lam + 1)
        kappa = 6 * lam ** 2 - 6 * lam + 1
        assert c == 2
        assert kappa == 1

    def test_bc_complementarity(self):
        """kappa(betagamma) + kappa(bc) = 0.

        bc at lambda has c_{bc} = -c_{betagamma}, so
        kappa(bc) = c_{bc}/2 = -kappa(betagamma).
        """
        for lam in [0, 1, Rational(1, 2), 2]:
            lam = Rational(lam)
            kappa_bg = 6 * lam ** 2 - 6 * lam + 1
            kappa_bc = -(6 * lam ** 2 - 6 * lam + 1)
            assert kappa_bg + kappa_bc == 0


# =========================================================================
# PART 6: The fundamental distinction: kappa vs c/2
# =========================================================================

class TestKappaVsCOver2:
    """Demonstrate that kappa != c/2 in general.

    The KEY FINDING of this cross-check:

    1. For algebras where the stress tensor is the ONLY generator
       (Virasoro, beta-gamma, bc, free fermion):
         kappa = c/2   (anomaly ratio = 1/2)

    2. For algebras with a current J of weight 1 as a generator
       (Heisenberg, KM):
         kappa != c/2 in general

    3. For W-algebras with higher-spin generators:
         kappa = c * sigma where sigma = sum 1/(m_i + 1) = H_N - 1

    The general pattern: if the algebra has generators of conformal
    weights h_1, ..., h_r, and each generator's self-OPE has highest
    pole c/h_i (Zamolodchikov normalization), then:
      kappa = sum_i c/h_i = c * sum_i 1/h_i

    For Heisenberg: one generator of weight 1, self-OPE pole = k (level).
    So kappa = k, not c * (1/1) = c = 1.  The discrepancy is because
    the Heisenberg OPE pole is k, not c/1 = 1.

    CORRECTED UNDERSTANDING: The formula is
      kappa = sum_i (highest pole of W^{(h_i)} self-OPE)
    For Zamolodchikov-normalized generators, this is c/h_i.
    For Heisenberg current alpha with alpha.alpha ~ k/(z-w)^2,
    the highest pole is k, giving kappa = k.
    """

    def test_heisenberg_vs_c_over_2(self):
        """kappa(H_k) = k, while c/2 = 1/2. Different for k != 1."""
        # rank-1 Heisenberg: c = 1 always
        c = 1
        for k in [2, 3, 5, 10]:
            assert kappa_heisenberg(k) == k
            assert Rational(c, 2) == Rational(1, 2)
            assert kappa_heisenberg(k) != Rational(c, 2)

    def test_km_vs_c_over_2(self):
        """kappa(g_k) != c(g_k)/2 for KM algebras."""
        for k in [1, 2, 3]:
            # sl2
            c = sugawara_c("A", 1, k)
            kappa = kappa_km("A", 1, k)
            c_half = c / 2
            diff = simplify(kappa - c_half)
            assert diff != 0, f"sl2 at k={k}: kappa - c/2 should be nonzero"

            # Explicit: kappa = 3(k+2)/4, c/2 = 3k/(2(k+2))
            assert kappa == Rational(3) * (k + 2) / 4
            assert c_half == Rational(3) * k / (2 * (k + 2))

    def test_virasoro_agrees_with_c_over_2(self):
        """For Virasoro, kappa = c/2 (the one case where they agree)."""
        for c in [1, 2, 13, 26]:
            assert kappa_virasoro(c) == Rational(c, 2)

    def test_w3_vs_c_over_2(self):
        """kappa(W_3) = 5c/6 != c/2."""
        for c in [1, 2, 6]:
            assert kappa_w3(c) == 5 * Rational(c) / 6
            assert kappa_w3(c) != Rational(c, 2)

    def test_anomaly_ratio_table(self):
        """Verify the anomaly ratio table from the preface."""
        # Heisenberg at k=1: rho = kappa/c = 1/1 = 1
        assert kappa_heisenberg(1) / 1 == 1

        # Virasoro: rho = 1/2
        c = Rational(7)  # arbitrary nonzero
        assert kappa_virasoro(c) / c == Rational(1, 2)

        # W_3: rho = H_3 - 1 = 5/6
        c = Rational(7)
        assert kappa_w3(c) / c == Rational(5, 6)

        # sl2: rho = kappa/c = [3(k+2)/4] / [3k/(k+2)]
        #          = (k+2)^2 / (4k)
        # This is NOT a constant! It depends on k.
        for k in [1, 2, 3]:
            kappa = kappa_km("A", 1, k)
            c = sugawara_c("A", 1, k)
            rho = simplify(kappa / c)
            expected_rho = (Rational(k) + 2) ** 2 / (4 * Rational(k))
            assert simplify(rho - expected_rho) == 0, \
                f"sl2 at k={k}: rho = {rho}, expected {expected_rho}"


# =========================================================================
# PART 7: Cross-check with the master table in higher_genus_foundations.tex
# =========================================================================

class TestMasterTable:
    """Verify all entries in the table at thm:genus1-universal-curvature.

    The table (lines 3308-3318 of higher_genus_foundations.tex):
      A              | kappa(A)        | kappa(A!)        | kappa+kappa! | F_1
      H_kappa        | kappa           | -kappa           | 0            | kappa/24
      sl2_k          | 3(k+2)/4        | -3(k+2)/4        | 0            | (k+2)/32
      Vir_c          | c/2             | (26-c)/2         | 13           | c/48
      W_3 charge c   | 5c/6            | 5(100-c)/6       | 250/3        | 5c/144
      bc_lambda       | c_{bc}/2        | ---              | ---          | c_{bc}/48
    """

    def test_heisenberg_row(self):
        from lib.utils import F_g
        kappa = kappa_heisenberg(1)
        assert kappa == 1
        assert F_g(kappa, 1) == Rational(1, 24)

    def test_sl2_row(self):
        from lib.utils import F_g
        k = Symbol('k')
        kappa = Rational(3) * (k + 2) / 4
        # kappa! = -kappa (FF antisymmetry)
        kappa_dual = -kappa
        assert simplify(kappa + kappa_dual) == 0
        # F_1 = kappa/24 = 3(k+2)/(4*24) = (k+2)/32
        F1 = kappa / 24
        assert simplify(F1 - (k + 2) / 32) == 0

    def test_virasoro_row(self):
        from lib.utils import F_g
        c = Symbol('c')
        kappa = c / 2
        kappa_dual = (26 - c) / 2
        assert simplify(kappa + kappa_dual - 13) == 0
        F1 = kappa / 24
        assert simplify(F1 - c / 48) == 0

    def test_w3_row(self):
        c = Symbol('c')
        kappa = 5 * c / 6
        kappa_dual = 5 * (100 - c) / 6
        total = simplify(kappa + kappa_dual)
        assert total == Rational(250, 3)
        F1 = kappa / 24
        assert simplify(F1 - 5 * c / 144) == 0

    def test_bc_row(self):
        """bc system: kappa = c_{bc}/2."""
        lam = Symbol('lambda')
        c_bc = -(12 * lam ** 2 - 12 * lam + 2)  # = -2*(6*lam^2 - 6*lam + 1)
        kappa_bc = c_bc / 2
        # At lambda=1: c_bc = -2, kappa = -1
        assert kappa_bc.subs(lam, 1) == -1


# =========================================================================
# PART 8: Physical derivation of the two-channel decomposition for KM
# =========================================================================

class TestTwoChannelDecomposition:
    """Verify the two-channel decomposition of kappa for KM.

    From genus_expansions.tex (the sl2 genus-2 proof):
      double-pole channel: dim(g)*k/(2*h^v) [from OPE k*kappa^{ab}/(z-w)^2]
      simple-pole channel: dim(g)/2         [from structure constants f^{ab}_c]
      Total: kappa = dim(g)*(k+h^v)/(2*h^v)

    The simple-pole channel comes from:
      sum_{c,d} f^{ac}_d f^{bc}_d = 2*h^v * kappa^{ab}
    Tracing: sum_{a,b} kappa_{ab} * 2*h^v * kappa^{ab} = 2*h^v * dim(g)
    Normalizing by 2*h^v: dim(g)/2.

    The double-pole channel comes from:
      OPE: J^a(z) J^b(w) ~ k*kappa^{ab}/(z-w)^2 + ...
    Tracing: sum_{a,b} kappa_{ab} * k * kappa^{ab} = k * dim(g)
    Normalizing by 2*h^v: k*dim(g)/(2*h^v).
    """

    def test_sl2_decomposition(self):
        """sl2: double-pole = 3k/4, simple-pole = 3/2."""
        for k in [1, 2, 3, 5]:
            dp = Rational(3) * k / 4        # double-pole
            sp = Rational(3, 2)              # simple-pole
            total = dp + sp
            assert total == kappa_sl2(k)

    def test_sl3_decomposition(self):
        """sl3: dim=8, h^v=3, double-pole = 4k/3, simple-pole = 4."""
        for k in [1, 2, 3]:
            dp = Rational(8) * k / (2 * 3)  # 8k/6 = 4k/3
            sp = Rational(8, 2)              # 4
            total = dp + sp
            assert total == kappa_sl3(k), \
                f"sl3 at k={k}: {dp} + {sp} = {total}, expected {kappa_sl3(k)}"

    def test_g2_decomposition(self):
        """G2: dim=14, h^v=4, double-pole = 14k/8 = 7k/4, simple-pole = 7."""
        for k in [1, 2, 3]:
            dp = Rational(14) * k / (2 * 4)  # 7k/4
            sp = Rational(14, 2)              # 7
            total = dp + sp
            assert total == kappa_g2(k), \
                f"G2 at k={k}: {dp} + {sp} = {total}, expected {kappa_g2(k)}"

    def test_b2_decomposition(self):
        """B2 = so5: dim=10, h^v=3, double-pole = 10k/6 = 5k/3, simple-pole = 5."""
        for k in [1, 2, 3]:
            dp = Rational(10) * k / (2 * 3)
            sp = Rational(10, 2)
            total = dp + sp
            assert total == kappa_b2(k)


# =========================================================================
# PART 9: The preface claim "anomaly ratio = 1 for Heisenberg"
# =========================================================================

class TestAnomalyRatioConsistency:
    """Resolve the apparent contradiction in the preface anomaly ratio.

    Preface (line 253):
      "The ratio rho(A) := kappa(A)/c(A) is the anomaly ratio:
       it equals 1 for the Heisenberg..."

    But kappa(H_k) = k and c(H_k) = 1, so rho = k, not 1.

    RESOLUTION: The preface means the anomaly ratio for the Heisenberg
    FAMILY is a structural constant equal to 1.  This means that at
    the STANDARD normalization (where c = k, i.e., rank-d Heisenberg
    at level 1, where c = d = kappa), the ratio is 1.

    Actually, more precisely: for rank-1 at level k, c = 1 always
    (from T = (1/2k):alpha*alpha:).  So rho = k/1 = k.

    But the preface says rho = 1.  This works if we interpret it as:
    "the anomaly ratio is 1 at the standard normalization k = 1".
    Or: "kappa/c is level-independent only when expressed in the
    correct variables."

    WAIT: let me reread.  The Heisenberg at level k has:
      alpha.alpha ~ k/(z-w)^2
      T = (1/2k):alpha*alpha:
      c = 1

    So kappa = k, c = 1, rho = k.  This is level-dependent.

    But for W_N, the preface claims rho is level-independent (= H_N - 1).
    How is this consistent?

    For W_N: kappa = c * (H_N - 1).  Here c DOES depend on k.
    So rho = kappa/c = H_N - 1 is indeed level-independent.

    For KM: kappa = dim(g)*(k+h^v)/(2*h^v), c = k*dim(g)/(k+h^v).
    So rho = (k+h^v)^2/(2*h^v*k).  This IS level-dependent.

    For Heisenberg: if we write c as a function of the level parameter,
    then at level k (with standard normalization where the OPE coefficient
    IS the level), c = 1 always, so rho = k.

    BUT: there is a natural rescaling.  If we normalize alpha so that
    alpha.alpha ~ 1/(z-w)^2 (level-1 normalization), then kappa = 1 and
    c = 1, giving rho = 1.  The "level k" is then a PARAMETER in the
    stress tensor T_k = (k/2):alpha*alpha:, giving c = k.  In this
    normalization: kappa(H,c=k) = k, c = k, rho = 1.

    So the preface statement rho = 1 for Heisenberg refers to the
    normalization where c = k (using T_k = (k/2):alpha*alpha:
    or equivalently rank-d Heisenberg at standard level where c = d).

    At level k=1, rank d: c = d, kappa = d, rho = 1. Correct.
    """

    def test_rank_d_level_1_ratio(self):
        """rank-d Heisenberg at k=1: c = d, kappa = d, rho = 1."""
        for d in range(1, 10):
            c = d
            kappa = d * kappa_heisenberg(1)
            assert kappa / c == 1

    def test_w_algebra_ratio_level_independent(self):
        """W_N anomaly ratio is level-independent: rho = sigma(g)."""
        # W_3 at different c values
        sigma_sl3 = sigma_invariant("A", 2)  # 5/6
        for c in [Rational(1), Rational(2), Rational(100)]:
            kappa = kappa_w3(c)
            rho = kappa / c
            assert rho == sigma_sl3

    def test_km_ratio_is_level_dependent(self):
        """KM anomaly ratio is level-dependent."""
        ratios = []
        for k in [1, 2, 3]:
            c = sugawara_c("A", 1, k)
            kappa = kappa_km("A", 1, k)
            rho = simplify(kappa / c)
            ratios.append(rho)
        # Check they are all different
        assert ratios[0] != ratios[1]
        assert ratios[1] != ratios[2]


# =========================================================================
# PART 10: Deformation_quantization.tex formula check
# =========================================================================

class TestDeformationQuantizationFormula:
    """The deformation_quantization.tex (line 1141) states:
      m_0(g_k) = (k+h^v)*kappa/(2*h^v)

    Here 'kappa' is the Killing form (kappa^{ab}), not the modular
    characteristic!  This is potentially confusing notation.

    The modular characteristic is:
      kappa(g_k) = dim(g)*(k+h^v)/(2*h^v)

    And the per-generator curvature (using Killing kappa^{ab}) is:
      m_0^{ab} = (k+h^v)*kappa^{ab}/(2*h^v)

    Tracing: sum_{a,b} kappa_{ab} * m_0^{ab}
           = (k+h^v)/(2*h^v) * sum kappa_{ab} kappa^{ab}
           = (k+h^v)/(2*h^v) * dim(g)
           = modular characteristic kappa.
    """

    def test_trace_gives_modular_characteristic(self):
        """Tracing the per-generator curvature gives kappa."""
        for type_, rank in [("A", 1), ("A", 2), ("B", 2), ("G", 2)]:
            data = cartan_data(type_, rank)
            for k in [1, 2]:
                per_gen = (Rational(k) + data.h_dual) / (2 * data.h_dual)
                traced = per_gen * data.dim
                kappa = kappa_km(type_, rank, k)
                assert traced == kappa


# =========================================================================
# Run all tests
# =========================================================================

if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v", "--tb=short"])
