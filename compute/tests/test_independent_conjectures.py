"""Tests for independent conjectures (not subsumed by MC1-MC5).

Three conjectures:
1. Virasoro c=26 self-duality — complementarity c+c'=26, special c=26 structure
2. Derived bc-betagamma equivalence — Koszul Hilbert series relation
3. Near-rationality Pade — W_3 and Virasoro bar GF near-rationality

Ground truth references:
  - comp:virasoro-curvature: c + c' = 26
  - thm:betagamma-fermion-koszul: bc^! = betagamma
  - conj:w3-bar-gf: W_3 rational GF conjecture
  - bar_gf_solver.py: Pade/algebraic GF machinery
"""

import pytest
from sympy import Rational, Symbol, simplify

from compute.lib.independent_conjectures import (
    virasoro_complementarity_sum,
    virasoro_ds_central_charge,
    virasoro_dual_central_charge,
    virasoro_curvature,
    virasoro_bar_at_c26,
    virasoro_self_duality_check,
    bc_central_charge,
    beta_gamma_central_charge,
    bc_betagamma_central_charge_sum,
    bc_bar_dimensions,
    beta_gamma_bar_dimensions,
    bc_betagamma_koszul_check,
    pade_approximant,
    pade_approximant_test,
    w3_pade_check,
    virasoro_pade_check,
    verify_virasoro_complementarity,
    verify_bc_betagamma_duality,
)


# ===========================================================================
# Conjecture 1: Virasoro c+c'=26
# ===========================================================================

class TestVirasoroComplementarity:
    """Virasoro central charge complementarity c + c' = 26."""

    def test_complementarity_sum(self):
        """c + c' = 26 (symbolic verification)."""
        assert virasoro_complementarity_sum() == 26

    def test_ds_at_k0(self):
        """c(k=0) = 1 - 6*1/2 = -2."""
        assert virasoro_ds_central_charge(0) == -2

    def test_ds_complementarity_k0(self):
        """c(0) + c(-4) = 26."""
        c0 = virasoro_ds_central_charge(0)
        c_dual = virasoro_ds_central_charge(-4)
        assert c0 + c_dual == 26

    def test_ds_complementarity_k1(self):
        """c(1) + c(-5) = 26."""
        c1 = virasoro_ds_central_charge(1)
        c_dual = virasoro_ds_central_charge(-5)
        assert c1 + c_dual == 26

    def test_ds_complementarity_symbolic(self):
        """c(k) + c(-k-4) = 26 for symbolic k."""
        k = Symbol('k')
        c_k = virasoro_ds_central_charge(k)
        c_dual = virasoro_ds_central_charge(-k - 4)
        assert simplify(c_k + c_dual) == 26

    def test_curvature_complementarity(self):
        """m_0(c) + m_0(26-c) = 13."""
        c = Symbol('c')
        m0 = virasoro_curvature(c)
        m0_dual = virasoro_curvature(26 - c)
        assert simplify(m0 + m0_dual) == 13

    def test_dual_central_charge(self):
        """c' = 26 - c."""
        assert virasoro_dual_central_charge(26) == 0
        assert virasoro_dual_central_charge(0) == 26
        assert virasoro_dual_central_charge(13) == 13

    def test_all_complementarity_checks(self):
        """All checks in verify_virasoro_complementarity pass."""
        for name, ok in verify_virasoro_complementarity().items():
            assert ok, f"Complementarity check failed: {name}"


class TestVirasoroC26:
    """Bar complex properties at c=26 (bosonic string critical dimension)."""

    def test_curvature_at_c26(self):
        """m_0 = 13 at c=26."""
        data = virasoro_bar_at_c26()
        assert data["curvature"] == 13

    def test_dual_curvature_at_c26(self):
        """m_0' = 0 at c'=0 (dual is uncurved)."""
        data = virasoro_bar_at_c26()
        assert data["dual_curvature"] == 0

    def test_dual_central_charge_at_c26(self):
        """c' = 0 at c=26."""
        data = virasoro_bar_at_c26()
        assert data["dual_central_charge"] == 0

    def test_bar_dims_c_independent(self):
        """Bar cohomology dims are c-independent (generically)."""
        data = virasoro_bar_at_c26()
        assert data["dims_are_c_independent"] is True

    def test_bar_dims_are_motzkin_diffs(self):
        """Bar dims at c=26 = Motzkin differences (same as any generic c)."""
        data = virasoro_bar_at_c26(6)
        dims = data["bar_cohomology_dims"]
        # Known Motzkin differences: 1, 2, 5, 12, 30, 76
        expected = {1: 1, 2: 2, 3: 5, 4: 12, 5: 30, 6: 76}
        for n, exp in expected.items():
            assert dims[n] == exp, f"H^{n} = {dims[n]}, expected {exp}"


class TestVirasoroSelfDuality:
    """Self-duality diagnostics for Virasoro bar complex."""

    def test_not_self_dual_at_c26(self):
        """c=26 is NOT self-dual (c' = 0 != 26)."""
        sd = virasoro_self_duality_check(6)
        assert sd["c26_is_self_dual"] is False

    def test_self_dual_point_is_c13(self):
        """Self-duality requires c = c', giving c = 13."""
        sd = virasoro_self_duality_check(6)
        assert sd["self_dual_central_charge"] == 13

    def test_koszul_product_first_term(self):
        """H(t)*H(-t) has leading coefficient 1."""
        sd = virasoro_self_duality_check(6)
        assert sd["koszul_product"][0] == 1

    def test_virasoro_not_koszul_self_dual(self):
        """Virasoro is NOT Koszul self-dual (H(t)*H(-t) != 1)."""
        sd = virasoro_self_duality_check(6)
        # The product should have nonzero higher terms
        assert sd["is_koszul_self_dual"] is False

    def test_complementarity_sum_consistent(self):
        """Complementarity sum = 26 in self-duality check."""
        sd = virasoro_self_duality_check(6)
        assert sd["complementarity_sum"] == 26


# ===========================================================================
# Conjecture 2: bc-betagamma Koszul duality
# ===========================================================================

class TestBcBetaGammaCentralCharge:
    """Central charge formulas for bc and betagamma systems."""

    def test_bc_lambda1(self):
        """c_{bc}(1) = -2.
        # VERIFIED: [DC] 1 - 3*(2-1)^2 = 1-3 = -2. [CF] c_bc(1)+c_bg(1)=-2+2=0.
        """
        assert bc_central_charge(1) == -2

    def test_bg_lambda1(self):
        """c_{bg}(1) = 2.
        # VERIFIED: [DC] 2*(6-6+1) = 2. [CF] c_bc(1)+c_bg(1)=-2+2=0.
        """
        assert beta_gamma_central_charge(1) == 2

    def test_bc_lambda_half(self):
        """c_{bc}(1/2) = 1 (single Dirac fermion).
        # VERIFIED: [DC] 1 - 3*(0)^2 = 1. [LT] Polchinski eq. (2.5.12).
        """
        assert bc_central_charge(Rational(1, 2)) == 1

    def test_bg_lambda_half(self):
        """c_{bg}(1/2) = -1 (symplectic boson).
        # VERIFIED: [DC] 2*(3/2-3+1) = -1. [CF] c_bc(1/2)+c_bg(1/2)=1+(-1)=0.
        """
        assert beta_gamma_central_charge(Rational(1, 2)) == -1

    def test_bc_lambda2(self):
        """c_{bc}(2) = -26 (reparametrization ghosts).
        # VERIFIED: [DC] 1 - 3*(3)^2 = 1-27 = -26. [LT] Polchinski eq. (2.5.12).
        """
        assert bc_central_charge(2) == -26

    def test_bg_lambda2(self):
        """c_{bg}(2) = 26 (matter ghost, string ghost cancellation c_bg+c_bc=0).
        # VERIFIED: [DC] 2*(24-12+1) = 26. [CF] c_bc(2)+c_bg(2)=-26+26=0.
        """
        assert beta_gamma_central_charge(2) == 26

    @pytest.mark.parametrize("lam", [0, 1, 2, 3, -1])
    def test_central_charge_sum_vanishes(self, lam):
        """c_{bc}(lambda) + c_{bg}(lambda) = 0 for all lambda."""
        assert bc_betagamma_central_charge_sum(lam) == 0

    def test_central_charge_sum_symbolic(self):
        """c_{bc}(lambda) + c_{bg}(lambda) = 0 for symbolic lambda."""
        lam = Symbol('lambda')
        s = bc_betagamma_central_charge_sum(lam)
        assert simplify(s) == 0


class TestBcBarDimensions:
    """Bar cohomology dimensions for bc ghost system."""

    def test_bc_formula(self):
        """dim H^n(B(bc)) = 2^n - n + 1."""
        dims = bc_bar_dimensions(1, 8)
        expected = {1: 2, 2: 3, 3: 6, 4: 13, 5: 28, 6: 59, 7: 122, 8: 249}
        for n, exp in expected.items():
            assert dims[n] == exp, f"bc H^{n} = {dims[n]}, expected {exp}"

    def test_bc_matches_known(self):
        """bc dims match KNOWN_BAR_DIMS['bc']."""
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        dims = bc_bar_dimensions(1, 8)
        for n in range(1, 9):
            assert dims[n] == KNOWN_BAR_DIMS["bc"][n]


class TestBetaGammaBarDimensions:
    """Bar cohomology dimensions for betagamma system."""

    def test_bg_known_values(self):
        """betagamma bar dims match known values."""
        dims = beta_gamma_bar_dimensions(1, 8)
        expected = {1: 2, 2: 4, 3: 10, 4: 26, 5: 70, 6: 192, 7: 534, 8: 1500}
        for n, exp in expected.items():
            assert dims[n] == exp, f"bg H^{n} = {dims[n]}, expected {exp}"

    def test_bg_matches_known(self):
        """betagamma dims match KNOWN_BAR_DIMS['beta_gamma']."""
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        dims = beta_gamma_bar_dimensions(1, 8)
        for n in range(1, 9):
            assert dims[n] == KNOWN_BAR_DIMS["beta_gamma"][n]


class TestBcBetaGammaKoszulCheck:
    """Koszul duality verification for bc/betagamma pair.

    NOTE: The classical Koszul relation H_A(t)*H_{A!}(-t) = 1 does NOT
    hold for chiral bar cohomology. Instead, we verify:
    (a) Central charge complementarity: c_bc + c_bg = 0
    (b) Algebraic GF for betagamma: P^2 = (1+x)/(1-3x)
    (c) Closed-form for bc: 2^n - n + 1
    """

    def test_koszul_dual_lam1(self):
        """bc and bg are verified Koszul dual at lambda=1, degree 5."""
        result = bc_betagamma_koszul_check(lam=1, max_degree=5)
        assert result["is_koszul_dual"], "bc-bg Koszul duality check failed"

    def test_koszul_dual_lam1_deg7(self):
        """bc and bg are verified Koszul dual at lambda=1, degree 7."""
        result = bc_betagamma_koszul_check(lam=1, max_degree=7)
        assert result["is_koszul_dual"], "bc-bg Koszul duality check failed at deg 7"

    def test_central_charge_complement(self):
        """c_bc + c_bg = 0 in the check output."""
        result = bc_betagamma_koszul_check(lam=1, max_degree=5)
        assert result["central_charge_complement"]

    def test_bg_algebraic_gf(self):
        """betagamma bar GF satisfies P^2 = (1+x)/(1-3x)."""
        result = bc_betagamma_koszul_check(lam=1, max_degree=7)
        assert result["bg_algebraic_gf_verified"]

    def test_bc_formula(self):
        """bc bar dims satisfy 2^n - n + 1."""
        result = bc_betagamma_koszul_check(lam=1, max_degree=7)
        assert result["bc_formula_verified"]

    def test_central_charge_sum_in_check(self):
        """Central charge sum is 0 in the check output."""
        result = bc_betagamma_koszul_check(lam=1, max_degree=3)
        assert result["c_sum"] == 0

    def test_all_duality_checks(self):
        """All checks in verify_bc_betagamma_duality pass."""
        for name, ok in verify_bc_betagamma_duality().items():
            assert ok, f"bc-bg duality check failed: {name}"


# ===========================================================================
# Conjecture 3: Near-rationality (Pade)
# ===========================================================================

class TestPadeApproximant:
    """Pade approximant computation."""

    def test_pade_11_geometric(self):
        """[1/1] Pade of 1/(1-x) = 1 + x + x^2 + ... gives N=1, D=1-x."""
        coeffs = [1, 1, 1, 1, 1]
        pade = pade_approximant(coeffs, 1, 1)
        assert pade is not None
        # N(x) = 1 (just constant), D(x) = 1 - x
        # f(x)*D(x) - N(x) = (1+x+...)(1-x) - 1 = 1 - 1 = 0 + O(x^3)
        assert pade["num"][0] == Rational(1)  # n_0 = 1
        assert pade["den"] == [Rational(-1)]  # d_1 = -1

    def test_pade_01_constant(self):
        """[0/1] Pade of 1/(1-x) gives correct recurrence."""
        coeffs = [1, 1, 1]
        pade = pade_approximant(coeffs, 0, 1)
        assert pade is not None
        assert pade["num"][0] == 1

    def test_pade_predictions(self):
        """Pade approximant predicts correct next terms for geometric series."""
        coeffs = [1, 1, 1, 1, 1]
        pade = pade_approximant(coeffs, 1, 1)
        assert pade is not None
        # D = 1-x, so c_k = c_{k-1} for k > 1. Predictions should all be 1.
        for p in pade["predictions"]:
            assert p == 1

    def test_pade_polynomial(self):
        """[3/0] Pade of a polynomial is the polynomial itself."""
        coeffs = [1, 2, 3, 0, 0, 0]
        pade = pade_approximant(coeffs, 3, 0)
        assert pade is not None
        assert pade["num"] == [Rational(1), Rational(2), Rational(3), Rational(0)]


class TestW3Pade:
    """W_3 near-rationality via Pade approximants and rational GF solver."""

    def test_w3_pade_runs(self):
        """W_3 Pade check executes without error."""
        result = w3_pade_check()
        assert "known_dims" in result
        assert result["known_dims"] == [1, 2, 5, 16, 52]

    def test_w3_conjectured_h5(self):
        """Conjectured H^5(W_3) = 171 from recurrence."""
        # The depth-2+constant recurrence: a(n) = 3*a(n-1) + a(n-2) - 1
        a = [0, 2, 5, 16, 52]
        a5 = 3 * a[4] + a[3] - 1
        assert a5 == 171

    def test_w3_rational_gf_via_solver(self):
        """Conjectured W_3 rational GF verified by bar_gf_solver.

        With 5 data points [2,5,16,52,171] (P(x) convention from bar_gf_solver),
        the rational GF P(x) = x(2-3x)/((1-x)(1-3x-x^2)) is recovered.
        D(x) = 1 - 4x + 2x^2 + x^3, N(x) = 2x - 3x^2.
        """
        from compute.lib.bar_gf_solver import verify_conjectured_gf
        result = verify_conjectured_gf(
            [2, 5, 16, 52, 171],
            num_coeffs=[2, -3],
            den_coeffs=[-4, 2, 1],
            n_predict=2,
        )
        assert result["matches"], "W3 conjectured GF fails verification"
        assert result["predictions"][0] == 564

    def test_w3_pade_with_6_terms(self):
        """Pade [2/3] of full Hilbert series [1,2,5,16,52,171] gives rational GF.

        NOTE: The [2/3] Pade of the H(t) = 1 + ... series does NOT give the
        conjectured GF because the H(t) numerator has degree 3 (not 2).
        The bar_gf_solver uses the P(x) = a_1*x + ... convention instead.
        This test verifies the bar_gf_solver finds the rational GF.
        """
        from compute.lib.bar_gf_solver import find_rational_gf
        # bar_gf_solver convention: coeffs = [a_1, a_2, ...] of P(x)
        result = find_rational_gf([2, 5, 16, 52, 171], max_q=3, max_p=3)
        assert result is not None, "No rational GF found for W3 with 5 terms"
        assert result["den_coeffs"] == [Rational(-4), Rational(2), Rational(1)]
        assert result["num_coeffs"] == [Rational(2), Rational(-3)]


class TestVirasoroPade:
    """Virasoro near-rationality diagnostics."""

    def test_virasoro_pade_runs(self):
        """Virasoro Pade check executes without error."""
        result = virasoro_pade_check(6)
        assert "dims" in result
        assert result["is_truly_rational"] is False
        assert result["is_algebraic_degree_2"] is True

    def test_virasoro_known_dims(self):
        """Virasoro bar dims are correct Motzkin differences."""
        result = virasoro_pade_check(6)
        dims = result["dims"]
        expected = [1, 1, 2, 5, 12, 30, 76]
        assert dims == expected

    def test_virasoro_near_rational(self):
        """Virasoro is near-rational (Pade gives integer predictions)."""
        # Through degree 8, a rational approximation works
        from compute.lib.koszul_hilbert import motzkin
        h = [1]
        for n in range(1, 9):
            h.append(motzkin(n + 1) - motzkin(n))
        # [3/3] Pade through 7 terms
        pade = pade_approximant(h[:7], 3, 3)
        assert pade is not None
        # Should predict h[7] correctly (near-rationality)
        pred = pade["predictions"][0]
        assert pred == h[7], f"Pade predicts {pred}, actual {h[7]}"

    def test_virasoro_near_rationality_breaks(self):
        """Virasoro near-rationality fails at degree 9.

        The depth-3 rational recurrence predicts 1352 but actual is 1353.
        """
        from compute.lib.koszul_hilbert import motzkin
        h = [1]
        for n in range(1, 10):
            h.append(motzkin(n + 1) - motzkin(n))
        # h = [1, 1, 2, 5, 12, 30, 76, 196, 512, 1353]
        assert h[9] == 1353

        # A [3/3] Pade fit to h[:7] predicts h[9]
        pade = pade_approximant(h[:7], 3, 3)
        assert pade is not None

        # Get predictions up to index 9
        # First prediction = h[7], second = h[8], third = h[9]
        # The third prediction (h[9]) should be 1352 (wrong), not 1353
        preds = pade["predictions"]
        # preds[0] = predicted h[7]
        # We need more predictions; extend manually
        extended = list(h[:7])
        d = pade["den"]
        n_num = pade["num"]
        for step in range(4):
            k = len(extended)
            # For k > p: c_k = -(d_1*c_{k-1} + ... + d_q*c_{k-q})
            val = Rational(0)
            for j in range(1, len(d) + 1):
                idx = k - j
                if 0 <= idx < len(extended):
                    val -= d[j - 1] * extended[idx]
            extended.append(val)

        # extended[9] should be 1352 (rational approximation), actual is 1353
        assert extended[9] == 1352, f"Rational prediction at deg 9 = {extended[9]}"
        assert extended[9] != h[9], "Near-rationality should BREAK at degree 9"


# ===========================================================================
# Integration tests
# ===========================================================================

class TestIntegration:
    """Cross-module consistency checks."""

    def test_virasoro_complementarity_matches_virasoro_bar(self):
        """Our complementarity matches virasoro_bar.py."""
        from compute.lib.virasoro_bar import virasoro_complementarity_sum as vcs_orig
        assert virasoro_complementarity_sum() == vcs_orig()

    def test_bc_dims_match_bar_complex(self):
        """bc bar dims match KNOWN_BAR_DIMS."""
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        our_dims = bc_bar_dimensions(1, 10)
        for n in range(1, min(11, max(KNOWN_BAR_DIMS["bc"].keys()) + 1)):
            assert our_dims[n] == KNOWN_BAR_DIMS["bc"][n], (
                f"bc H^{n}: ours={our_dims[n]}, registry={KNOWN_BAR_DIMS['bc'][n]}"
            )

    def test_bg_dims_match_bar_complex(self):
        """betagamma bar dims match KNOWN_BAR_DIMS."""
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        our_dims = beta_gamma_bar_dimensions(1, 8)
        for n in range(1, 9):
            assert our_dims[n] == KNOWN_BAR_DIMS["beta_gamma"][n], (
                f"bg H^{n}: ours={our_dims[n]}, registry={KNOWN_BAR_DIMS['beta_gamma'][n]}"
            )

    def test_w3_gf_solver_predicts_171(self):
        """W_3 bar_gf_solver predicts H^5 = 171."""
        from compute.lib.bar_gf_solver import predict_w3_degree5
        gf_result = predict_w3_degree5()
        assert gf_result["conjectured_gf_verified"]
        preds = gf_result["predictions"]
        assert preds[0] == 171, f"GF solver predicts H^5 = {preds[0]}"
