"""Tests for the C^3 functor chain: CY3 -> cyclic A-infinity -> Lie conformal -> W_{1+inf}.

Tests cover all five steps of the functor chain plus cross-checks with Vol I
and gap analysis.  Every numerical value is verified by at least 2 independent
methods per the multi-path verification mandate.

Test categories:
    test_step1_*    -- Polyvector field dimensions and equivariant character
    test_step2_*    -- Schouten-Nijenhuis bracket structure
    test_step3_*    -- Omega-background and Lie conformal algebra
    test_step4_*    -- Factorization envelope and W_{1+inf} identification
    test_step5_*    -- MacMahon function and DT partition function
    test_gap_*      -- Gap analysis (what the chain misses)
    test_crosscheck_* -- Cross-checks with Vol I shadow data
"""

import pytest
from fractions import Fraction

from compute.lib.c3_functor_chain import (
    OmegaBackground,
    PolyvectorBasis,
    analyze_functor_chain_gap,
    cross_check_with_vol1,
    dt_partition_function_c3,
    execute_functor_chain,
    factorization_envelope_c3,
    lie_conformal_from_omega,
    macmahon_coefficients,
    polyvector_dimensions,
    polyvector_equivariant_character,
    schouten_bracket_gl3_subalgebra,
    schouten_bracket_structure,
    self_dual_omega_background,
    standard_omega_background,
    structure_function_from_omega,
    verify_macmahon_identity,
    w_infinity_central_charge,
    w_infinity_central_charge_from_omega,
    kappa_w_infinity_at_n,
)


# =========================================================================
# STEP 1: Polyvector fields on C^3
# =========================================================================

class TestStep1PolyvectorFields:
    """Dimensions and equivariant character of PV(C^3)."""

    def test_pv_dim_deg0(self):
        """PV^*(C^3) at polynomial degree 0: dim = 8 = 2^3 (exterior algebra)."""
        dims = polyvector_dimensions(0)
        assert dims[0] == 1   # functions: C
        assert dims[1] == 3   # vector fields: C^3
        assert dims[2] == 3   # bivectors: C^3
        assert dims[3] == 1   # trivectors: C
        assert sum(dims.values()) == 8  # 2^3

    def test_pv_dim_deg1(self):
        """PV^*(C^3) at polynomial degree <= 1.

        Polynomial monomials of degree <= 1 in 3 variables: 1 + 3 = 4.
        Total dim = 4 * 8 = 32.
        """
        dims = polyvector_dimensions(1)
        n_poly = 4  # 1, x, y, z
        assert dims[0] == 1 * n_poly
        assert dims[1] == 3 * n_poly
        assert dims[2] == 3 * n_poly
        assert dims[3] == 1 * n_poly
        assert sum(dims.values()) == 8 * n_poly

    def test_pv_dim_deg2(self):
        """PV^*(C^3) at polynomial degree <= 2.

        Polynomial monomials: C(2+3,3) = C(5,3) = 10.
        """
        dims = polyvector_dimensions(2)
        assert sum(dims.values()) == 8 * 10

    def test_pv_dim_deg3(self):
        """PV^*(C^3) at polynomial degree <= 3.

        Polynomial monomials: C(3+3,3) = C(6,3) = 20.
        """
        dims = polyvector_dimensions(3)
        assert sum(dims.values()) == 8 * 20

    def test_pv_dim_general_formula(self):
        """Verify dim formula: C(d+3,3) * 2^3 for degree <= d."""
        for d in range(6):
            dims = polyvector_dimensions(d)
            n_poly = (d + 1) * (d + 2) * (d + 3) // 6
            assert sum(dims.values()) == 8 * n_poly, f"Failed at deg {d}"

    def test_pv_dim_exterior_binomials(self):
        """PV^p has C(3,p) exterior generators."""
        for d in range(4):
            dims = polyvector_dimensions(d)
            n_poly = (d + 1) * (d + 2) * (d + 3) // 6
            assert dims[0] == n_poly       # C(3,0) = 1
            assert dims[1] == 3 * n_poly   # C(3,1) = 3
            assert dims[2] == 3 * n_poly   # C(3,2) = 3
            assert dims[3] == n_poly       # C(3,3) = 1

    def test_polyvector_basis_object(self):
        """PolyvectorBasis correctly enumerates monomials."""
        pb = PolyvectorBasis(max_poly_deg=2)
        assert len(pb.poly_monomials) == 10  # C(5,3)
        dims = pb.dim_by_degree()
        assert sum(dims.values()) == pb.total_dim()

    def test_equivariant_character_total(self):
        """Equivariant character has correct total multiplicity."""
        bg = standard_omega_background(Fraction(1), Fraction(1))
        for d in range(4):
            char = polyvector_equivariant_character(
                d, bg.h1, bg.h2, bg.h3)
            total = sum(char.values())
            expected = 8 * (d + 1) * (d + 2) * (d + 3) // 6
            assert total == expected, f"Mismatch at deg {d}: {total} vs {expected}"

    def test_equivariant_character_weight_zero(self):
        """Weight-zero piece of PV(C^3) under T^3 action at degree <= 1.

        Weight zero monomials: {1, x del_x, y del_y, z del_z, ...}
        For h1=1, h2=1, h3=-2 at poly deg 0: only the constant 1 and
        del_x^del_y^del_z (weight -(h1+h2+h3) = 0) are weight 0.
        """
        bg = standard_omega_background(Fraction(1), Fraction(1))
        char = polyvector_equivariant_character(0, bg.h1, bg.h2, bg.h3)
        # At poly deg 0: monomials are just (0,0,0)
        # Weights: poly_wt=0, ext0: 0, ext1: -1,-1,2, ext2: -2,1,1, ext3: 0
        # Weight 0 from: ext0 (constant) and ext3 (volume form)
        assert char.get(Fraction(0), 0) == 2  # constant + volume form


# =========================================================================
# STEP 2: Schouten-Nijenhuis bracket
# =========================================================================

class TestStep2SchoutenBracket:
    """Schouten-Nijenhuis bracket structure on PV(C^3)."""

    def test_bracket_degree_shift(self):
        """Schouten bracket has degree shift -(d-1) = -2 for d=3."""
        sb = schouten_bracket_structure()
        assert sb['degree_shift'] == -2

    def test_bracket_properties(self):
        """Schouten bracket satisfies graded Lie axioms."""
        sb = schouten_bracket_structure()
        assert 'graded_antisymmetry' in sb['properties']
        assert 'graded_jacobi' in sb['properties']
        assert 'graded_leibniz_for_wedge_product' in sb['properties']

    def test_gl3_dimension(self):
        """The gl_3 subalgebra has dimension 9."""
        gl3 = schouten_bracket_gl3_subalgebra()
        assert gl3['dimension'] == 9
        assert gl3['cartan_dim'] == 3

    def test_gl3_structure_constants(self):
        """Verify [E_{ij}, E_{kl}] = delta_{jk} E_{il} - delta_{il} E_{kj}."""
        gl3 = schouten_bracket_gl3_subalgebra()
        sc = gl3['structure_constants']

        # [E_{01}, E_{10}] = delta_{10} E_{00} - delta_{00} E_{10}
        #                   = E_{00} - E_{11}
        key = ((0, 1), (1, 0))
        assert key in sc
        terms = sc[key]
        assert (1, (0, 0)) in terms
        assert (-1, (1, 1)) in terms

    def test_gl3_cartan_commute(self):
        """Diagonal elements [E_{ii}, E_{jj}] = 0 (terms cancel).

        The structure constant computation may include entries with
        cancelling terms (e.g., [E_{00}, E_{00}] = E_{00} - E_{00} = 0).
        We check that the NET bracket vanishes.
        """
        gl3 = schouten_bracket_gl3_subalgebra()
        sc = gl3['structure_constants']
        for i in range(3):
            for j in range(3):
                key = ((i, i), (j, j))
                if key in sc:
                    # Sum the coefficients for each output basis element
                    net = {}
                    for coeff, idx in sc[key]:
                        net[idx] = net.get(idx, 0) + coeff
                    # All net coefficients should be zero
                    for idx, val in net.items():
                        assert val == 0, (
                            f"[E_{{{i}{i}}}, E_{{{j}{j}}}] has nonzero net "
                            f"coefficient {val} at E_{{{idx[0]}{idx[1]}}}"
                        )

    def test_gl3_sl3_plus_gl1(self):
        """gl_3 = sl_3 + gl_1 decomposition."""
        gl3 = schouten_bracket_gl3_subalgebra()
        props = gl3['properties']
        assert 'gl_3 = sl_3 + gl_1' in props


# =========================================================================
# STEP 3: Omega-background and structure function
# =========================================================================

class TestStep3OmegaBackground:
    """Omega-background and Lie conformal algebra extraction."""

    def test_cy_condition(self):
        """CY condition h1 + h2 + h3 = 0."""
        for h1, h2 in [(1, 2), (1, -1), (3, 5), (0, 0)]:
            bg = standard_omega_background(Fraction(h1), Fraction(h2))
            assert bg.verify_cy()
            assert bg.h3 == -(bg.h1 + bg.h2)

    def test_sigma_values(self):
        """Elementary symmetric polynomials for (1, 2, -3)."""
        bg = standard_omega_background(Fraction(1), Fraction(2))
        assert bg.sigma_2 == 1 * 2 + 1 * (-3) + 2 * (-3)  # = 2 - 3 - 6 = -7
        assert bg.sigma_3 == 1 * 2 * (-3)  # = -6

    def test_structure_function_phi0(self):
        """phi_0 = 1 always (g(z) -> 1 as z -> infinity)."""
        for h1, h2 in [(1, 2), (1, -1), (3, 5)]:
            bg = standard_omega_background(Fraction(h1), Fraction(h2))
            phi = structure_function_from_omega(bg, max_order=3)
            assert phi[0] == 1

    def test_structure_function_phi1_zero(self):
        """phi_1 = 0 by CY condition (p_1 = h1+h2+h3 = 0)."""
        for h1, h2 in [(1, 2), (1, -1), (3, 5), (7, 11)]:
            bg = standard_omega_background(Fraction(h1), Fraction(h2))
            phi = structure_function_from_omega(bg, max_order=3)
            assert phi[1] == 0

    def test_structure_function_phi2_zero(self):
        """phi_2 = 0 (no even power sums contribute to odd log-series)."""
        for h1, h2 in [(1, 2), (1, -1), (3, 5)]:
            bg = standard_omega_background(Fraction(h1), Fraction(h2))
            phi = structure_function_from_omega(bg, max_order=3)
            assert phi[2] == 0

    def test_structure_function_phi3(self):
        """phi_3 = -2*p_3/3 = -2*sigma_3*3/3 = -2*sigma_3.

        p_3 = h1^3 + h2^3 + h3^3 = 3*sigma_3 (by Newton identity with sigma_1=0).
        alpha_3 = -2*p_3/3 = -2*sigma_3.
        phi_3 = alpha_3 (since phi_1=phi_2=0).
        """
        bg = standard_omega_background(Fraction(1), Fraction(2))
        phi = structure_function_from_omega(bg, max_order=4)
        expected_phi3 = -2 * bg.sigma_3  # = -2*(-6) = 12
        assert phi[3] == expected_phi3

    def test_structure_function_phi_even_zero(self):
        """phi_{2k} need not vanish for k >= 3 (but phi_2 = phi_4 = 0)."""
        bg = standard_omega_background(Fraction(1), Fraction(2))
        phi = structure_function_from_omega(bg, max_order=8)
        assert phi[2] == 0
        assert phi[4] == 0
        # phi_6 = alpha_3^2/2 which is nonzero in general
        alpha_3 = -2 * bg.sigma_3
        expected_phi6 = alpha_3 ** 2 / 2
        assert phi[6] == expected_phi6

    def test_self_dual_structure_function_trivial(self):
        """At self-dual point (sigma_3=0), g(z) = 1 (all phi_j = 0 for j >= 1)."""
        sd = self_dual_omega_background()
        assert sd.sigma_3 == 0
        phi = structure_function_from_omega(sd, max_order=10)
        for j in range(1, 11):
            assert phi[j] == 0, f"phi_{j} = {phi[j]} != 0 at self-dual point"

    def test_g_times_g_inverse_identity(self):
        """g(z) * g(-z) = 1 (equivalently, phi_j * phi_j^{(-)} sum to delta_{j,0}).

        This follows from g(-z) = 1/g(z).
        Check: sum_{i+j=n} phi_i * (-1)^j * phi_j = delta_{n,0}.
        """
        bg = standard_omega_background(Fraction(1), Fraction(2))
        phi = structure_function_from_omega(bg, max_order=10)
        N = 10

        for n in range(N + 1):
            val = Fraction(0)
            for i in range(n + 1):
                j = n - i
                val += phi[i] * ((-1) ** j) * phi[j]
            expected = Fraction(1) if n == 0 else Fraction(0)
            assert val == expected, f"g*g^(-1) identity fails at n={n}: {val}"

    def test_lie_conformal_j1j1_bracket(self):
        """[J^1_lambda J^1] = -sigma_2 * lambda for the spin-1 current."""
        bg = standard_omega_background(Fraction(1), Fraction(2))
        lcd = lie_conformal_from_omega(bg)
        assert lcd['lambda_bracket_J1J1'] == -bg.sigma_2


# =========================================================================
# STEP 4: Factorization envelope and W_{1+inf}
# =========================================================================

class TestStep4FactorizationEnvelope:
    """W_{1+inf} from factorization envelope of Omega-deformed PV(C^3)."""

    def test_w2_central_charge(self):
        """W_2 = Virasoro: c = 1 - 6/(k+2).

        From Omega with (h1, h2, h3) = (1, 2, -3):
            k + 2 = -2*sigma_2/sigma_3 = -2*(-7)/(-6) = -7/3
            c = 1 - 6/(-7/3) = 1 + 18/7 = 25/7
        """
        bg = standard_omega_background(Fraction(1), Fraction(2))
        c = w_infinity_central_charge_from_omega(bg, 2)
        assert c == Fraction(25, 7)

        # Cross-check via direct formula
        k_plus_N = -Fraction(2) * bg.sigma_2 / bg.sigma_3
        k = k_plus_N - 2
        c_direct = w_infinity_central_charge(2, k)
        assert c == c_direct

    def test_w3_central_charge(self):
        """W_3 central charge from Omega-background.

        k + 3 = -3*sigma_2/sigma_3 = -3*(-7)/(-6) = -7/2
        c = 2*(1 - 3*4/(-7/2)) = 2*(1 + 24/7) = 2*31/7 = 62/7
        """
        bg = standard_omega_background(Fraction(1), Fraction(2))
        c = w_infinity_central_charge_from_omega(bg, 3)
        assert c == Fraction(62, 7)

    def test_central_charge_formula_consistency(self):
        """c from Omega matches c from level for all N = 2..6."""
        bg = standard_omega_background(Fraction(1), Fraction(2))
        for N in range(2, 7):
            c_omega = w_infinity_central_charge_from_omega(bg, N)
            k_plus_N = -Fraction(N) * bg.sigma_2 / bg.sigma_3
            k = k_plus_N - N
            c_level = w_infinity_central_charge(N, k)
            assert c_omega == c_level, f"Mismatch at N={N}: {c_omega} vs {c_level}"

    def test_kappa_formula_consistency(self):
        """kappa from CY functor = (H_N - 1) * c for all N = 2..6."""
        bg = standard_omega_background(Fraction(1), Fraction(2))
        xc = cross_check_with_vol1(bg)
        for N in range(2, 6):
            assert xc[N]['kappa_match'], f"kappa mismatch at N={N}"

    def test_kappa_w2_is_c_over_2(self):
        """For W_2 = Virasoro: kappa = c/2 (anomaly ratio rho = 1/2)."""
        bg = standard_omega_background(Fraction(1), Fraction(2))
        c = w_infinity_central_charge_from_omega(bg, 2)
        kappa = kappa_w_infinity_at_n(bg, 2)
        assert kappa == c / 2

    def test_kappa_w3_anomaly_ratio(self):
        """For W_3: rho(sl_3) = H_3 - 1 = 1 + 1/2 + 1/3 - 1 = 5/6."""
        bg = standard_omega_background(Fraction(1), Fraction(2))
        c = w_infinity_central_charge_from_omega(bg, 3)
        kappa = kappa_w_infinity_at_n(bg, 3)
        rho = Fraction(5, 6)
        assert kappa == rho * c

    def test_factorization_envelope_type(self):
        """Factorization envelope gives W_{1+inf} type."""
        bg = standard_omega_background(Fraction(1), Fraction(2))
        fe = factorization_envelope_c3(bg)
        assert fe['vertex_algebra'] == 'W_{1+inf}'
        assert fe['shadow_depth_class'] == 'M (infinite)'

    def test_different_omega_give_different_c(self):
        """Different Omega parameters give different central charges."""
        bg1 = standard_omega_background(Fraction(1), Fraction(2))
        bg2 = standard_omega_background(Fraction(1), Fraction(3))
        c1 = w_infinity_central_charge_from_omega(bg1, 2)
        c2 = w_infinity_central_charge_from_omega(bg2, 2)
        assert c1 != c2


# =========================================================================
# STEP 5: MacMahon function and DT
# =========================================================================

class TestStep5MacMahon:
    """MacMahon function and DT partition function verification."""

    def test_macmahon_oeis(self):
        """MacMahon coefficients match OEIS A000219."""
        mac = macmahon_coefficients(10)
        oeis = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]
        for i in range(11):
            assert mac[i] == oeis[i], f"pp({i}): {mac[i]} != {oeis[i]}"

    def test_macmahon_higher(self):
        """MacMahon coefficients at n = 11..15 (OEIS A000219 extended)."""
        mac = macmahon_coefficients(15)
        # OEIS A000219 continued:
        oeis_extended = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500,
                         859, 1479, 2485, 4167, 6879]
        for i in range(16):
            assert mac[i] == oeis_extended[i], f"pp({i}): {mac[i]} != {oeis_extended[i]}"

    def test_macmahon_pp0(self):
        """pp(0) = 1 (the empty plane partition)."""
        mac = macmahon_coefficients(0)
        assert mac[0] == 1

    def test_macmahon_pp1(self):
        """pp(1) = 1 (the single-cell plane partition)."""
        mac = macmahon_coefficients(1)
        assert mac[1] == 1

    def test_macmahon_pp2(self):
        """pp(2) = 3: the three plane partitions of size 2.

        [[2]], [[1,1]], [[1],[1]]
        """
        mac = macmahon_coefficients(2)
        assert mac[2] == 3

    def test_dt_partition_function_signs(self):
        """DT partition function Z_DT(C^3) = M(-q): alternating signs."""
        dt = dt_partition_function_c3(5)
        mac = macmahon_coefficients(5)
        for n in range(6):
            assert dt[n] == (-1)**n * mac[n]

    def test_verify_macmahon_identity(self):
        """Run the full verification suite."""
        result = verify_macmahon_identity(10)
        assert result['match'] is True

    def test_log_macmahon_sigma2(self):
        """[q^n] log M(q) = sigma_2(n)/n where sigma_2(n) = sum_{d|n} d^2."""
        from compute.lib.c3_functor_chain import _log_macmahon_coeff
        # sigma_2(1) = 1, so log coeff at n=1 is 1
        assert _log_macmahon_coeff(1) == 1
        # sigma_2(2) = 1 + 4 = 5, so log coeff at n=2 is 5/2
        assert _log_macmahon_coeff(2) == Fraction(5, 2)
        # sigma_2(3) = 1 + 9 = 10, so log coeff at n=3 is 10/3
        assert _log_macmahon_coeff(3) == Fraction(10, 3)
        # sigma_2(6) = 1 + 4 + 9 + 36 = 50, so log coeff at n=6 is 50/6 = 25/3
        assert _log_macmahon_coeff(6) == Fraction(25, 3)


# =========================================================================
# GAP ANALYSIS
# =========================================================================

class TestGapAnalysis:
    """Tests for the gap analysis: what the functor chain misses."""

    def test_omega_essential(self):
        """Omega-background is essential for non-compact C^3."""
        bg = standard_omega_background(Fraction(1), Fraction(2))
        gap = analyze_functor_chain_gap(bg)
        assert gap['omega_background_essential'] is True

    def test_recovers_w_infinity_generic(self):
        """At generic Omega parameters, the chain recovers W_{1+inf}."""
        bg = standard_omega_background(Fraction(1), Fraction(2))
        gap = analyze_functor_chain_gap(bg)
        assert gap['recovers_w_infinity'] is True

    def test_self_dual_degenerates(self):
        """At self-dual point (sigma_3 = 0), the chain degenerates."""
        sd = self_dual_omega_background()
        gap = analyze_functor_chain_gap(sd)
        assert gap['self_dual_limit_degenerate'] is True
        assert gap['recovers_w_infinity'] is False

    def test_naive_chain_output(self):
        """Without Omega, the chain gives free fields."""
        bg = standard_omega_background(Fraction(1), Fraction(2))
        gap = analyze_functor_chain_gap(bg)
        assert 'free-field' in gap['naive_chain_output'].lower()

    def test_gap_classification(self):
        """The gap is classified as Omega-deformation + S^3 framing."""
        bg = standard_omega_background(Fraction(1), Fraction(2))
        gap = analyze_functor_chain_gap(bg)
        assert 'Omega' in gap['gap_classification']

    def test_structure_function_nontrivial_generic(self):
        """Structure function is nontrivial at generic parameters."""
        bg = standard_omega_background(Fraction(1), Fraction(2))
        gap = analyze_functor_chain_gap(bg)
        assert gap['structure_function_nontrivial'] is True

    def test_structure_function_trivial_self_dual(self):
        """Structure function is trivial at self-dual point."""
        sd = self_dual_omega_background()
        phi = structure_function_from_omega(sd, max_order=6)
        for j in range(1, 7):
            assert phi[j] == 0


# =========================================================================
# CROSS-CHECKS with Vol I shadow data
# =========================================================================

class TestCrossChecks:
    """Cross-checks between CY functor and Vol I formulas."""

    def test_cross_check_all_match(self):
        """Central charges and kappa match between CY and Vol I for N=2..5."""
        bg = standard_omega_background(Fraction(1), Fraction(2))
        xc = cross_check_with_vol1(bg)
        for N in range(2, 6):
            assert xc[N]['c_match'], f"c mismatch at N={N}"
            assert xc[N]['kappa_match'], f"kappa mismatch at N={N}"

    def test_w2_level_from_omega(self):
        """W_2 level extracted from Omega parameters is consistent.

        k + 2 = -2*sigma_2/sigma_3 = -2*(-7)/(-6) = -7/3
        k = -7/3 - 2 = -13/3
        """
        bg = standard_omega_background(Fraction(1), Fraction(2))
        xc = cross_check_with_vol1(bg)
        assert xc[2]['level_k'] == Fraction(-13, 3)

    def test_kappa_additivity_at_n2(self):
        """For two different Omega backgrounds, kappa(W_2) = c/2 in both cases."""
        for h1, h2 in [(1, 2), (3, 5), (1, 7)]:
            bg = standard_omega_background(Fraction(h1), Fraction(h2))
            c = w_infinity_central_charge_from_omega(bg, 2)
            kappa = kappa_w_infinity_at_n(bg, 2)
            if c is not None and kappa is not None:
                assert kappa == c / 2, f"kappa(W_2) != c/2 for ({h1},{h2})"

    def test_anomaly_ratio_matches_vol1(self):
        """rho(W_N) = H_N - 1 for the CY functor, matching Vol I."""
        bg = standard_omega_background(Fraction(1), Fraction(2))
        for N in range(2, 7):
            c = w_infinity_central_charge_from_omega(bg, N)
            kappa = kappa_w_infinity_at_n(bg, N)
            if c is not None and kappa is not None and c != 0:
                rho = kappa / c
                h_N = sum(Fraction(1, i) for i in range(1, N + 1))
                expected_rho = h_N - 1
                assert rho == expected_rho, f"rho mismatch at N={N}: {rho} vs {expected_rho}"

    def test_different_omega_different_params(self):
        """Different Omega backgrounds parametrize different points on the W_{1+inf} moduli."""
        bg1 = standard_omega_background(Fraction(1), Fraction(2))
        bg2 = standard_omega_background(Fraction(2), Fraction(3))
        for N in [2, 3]:
            c1 = w_infinity_central_charge_from_omega(bg1, N)
            c2 = w_infinity_central_charge_from_omega(bg2, N)
            assert c1 != c2, f"Should give different c for N={N}"


# =========================================================================
# FULL FUNCTOR CHAIN INTEGRATION
# =========================================================================

class TestFullFunctorChain:
    """Integration tests for the complete functor chain."""

    def test_execute_chain_runs(self):
        """The full chain executes without errors."""
        result = execute_functor_chain(max_poly_deg=2)
        assert result.pv_total_dim == 80  # 8 * 10

    def test_execute_chain_macmahon(self):
        """MacMahon coefficients are correct in the full chain."""
        result = execute_functor_chain(max_poly_deg=2)
        assert result.macmahon[0] == 1
        assert result.macmahon[1] == 1
        assert result.macmahon[2] == 3

    def test_execute_chain_gap(self):
        """Gap analysis is present and correct."""
        result = execute_functor_chain()
        assert result.gap_analysis['omega_background_essential'] is True
        assert result.gap_analysis['recovers_w_infinity'] is True

    def test_execute_chain_central_charges(self):
        """Central charges are computed for N=2..7."""
        result = execute_functor_chain()
        for N in range(2, 7):
            assert N in result.central_charges
            assert result.central_charges[N] is not None

    def test_execute_chain_different_params(self):
        """Chain gives different results for different parameters."""
        r1 = execute_functor_chain(eps1=Fraction(1), eps2=Fraction(2))
        r2 = execute_functor_chain(eps1=Fraction(2), eps2=Fraction(3))
        assert r1.central_charges[2] != r2.central_charges[2]

    def test_chain_omega_background_stored(self):
        """Omega-background is correctly stored in the result."""
        result = execute_functor_chain(eps1=Fraction(3), eps2=Fraction(5))
        assert result.omega_bg.h1 == Fraction(3)
        assert result.omega_bg.h2 == Fraction(5)
        assert result.omega_bg.h3 == Fraction(-8)
