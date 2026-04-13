import mpmath as mp

from compute.lib.genus1_arithmetic_shadow import BETA_GAMMA, HEISENBERG, VIRASORO


mp.mp.dps = 50


def test_heisenberg_shadow_matches_exact_euler_product_at_u2():
    u = mp.mpf(2)
    expected = mp.zeta(u) * mp.zeta(u + 1)
    # VERIFIED: [DC] weights=[1] gives S_H(u)=zeta(u)zeta(u+1); [CF] genus-1 triangle docstring states the same exact factorization.
    assert abs(HEISENBERG.S(u) - expected) < mp.mpf("1e-30")
    assert abs(HEISENBERG.euler_defect(u) - mp.mpf(1)) < mp.mpf("1e-30")


def test_virasoro_defect_matches_one_minus_inverse_zeta():
    u = mp.mpf(3)
    expected = 1 - 1 / mp.zeta(u)
    # VERIFIED: [DC] weight multiset [2] subtracts H_1(u)=1 in the definition of S_A; [LC] the docstring records the Virasoro defect as 1-1/zeta(u).
    assert abs(VIRASORO.euler_defect(u) - expected) < mp.mpf("1e-30")
    assert not VIRASORO.is_euler_koszul()


def test_heisenberg_sewing_coefficients_start_with_divisor_sums():
    expected = [mp.mpf(1), mp.mpf(3) / 2, mp.mpf(4) / 3]
    # VERIFIED: [DC] for weights=[1], a_N=sigma_{-1}(N)=sum_{d|N} 1/d; [LC] N=1,2,3 give 1, 1+1/2, 1+1/3.
    assert HEISENBERG.sewing_coefficients(3) == expected


def test_xi_regularization_and_beta_gamma_exactness():
    expected_xi = mp.zeta(2)
    # VERIFIED: [DC] Xi_H(1)=zeta(2)*(u-1)zeta(u)|_{u=1}; [LC] lim_{u->1}(u-1)zeta(u)=1.
    assert abs(HEISENBERG.Xi(mp.mpf(1)) - expected_xi) < mp.mpf("1e-30")
    assert BETA_GAMMA.is_euler_koszul()
    assert abs(BETA_GAMMA.euler_defect(mp.mpf(2)) - mp.mpf(1)) < mp.mpf("1e-30")
