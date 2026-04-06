r"""Tests for cy_grand_atlas_k3e_engine.py -- Grand Unified Atlas for K3 x E.

Multi-path verification:
    Path A: Direct computation from defining formulas
    Path B: Alternative formula / independent algorithm
    Path C: Limiting/special cases (chi=0, c=6, d=3)
    Path D: Symmetry/duality (Hodge symmetry, Serre duality, complementarity)
    Path E: Cross-family consistency (additivity, Kunneth)
    Path F: Literature comparison (Yau-Zaslow, DVV, Eichler-Zagier)
    Path G: Dimensional/degree analysis
    Path H: Numerical evaluation at specific parameter values

Target: >= 120 tests covering all 17 sections of the engine,
including synthesis tests that cross-check between engines.
"""

import math
from fractions import Fraction

import pytest

from compute.lib.cy_grand_atlas_k3e_engine import (
    # Arithmetic helpers
    sigma_k,
    partition_count,
    bernoulli_number,
    faber_pandharipande,
    eta_product_coeffs,
    eta_power_coeffs,
    partition_generating_coeffs,
    eisenstein_coeffs,
    # Hodge diamond
    HodgeDiamond,
    product_hodge,
    k3_hodge,
    elliptic_hodge,
    k3xe_hodge,
    quintic_hodge,
    # K-theory
    K0_RANK_K3XE,
    MUKAI_RANK_K3,
    k0_rank_k3xe,
    mukai_lattice_k3,
    euler_form_k3xe,
    h_even_rank_k3xe,
    # Kappa
    kappa_k3_sigma,
    kappa_e_sigma,
    kappa_k3xe,
    kappa_gepner_k3,
    kappa_kummer_lattice,
    kappa_discrepancy_explanation,
    # Shadow tower
    shadow_F_g,
    shadow_metric_k3xe,
    shadow_depth_k3xe,
    shadow_connection_k3xe,
    # Amplitudes
    genus_g_amplitude_scalar,
    genus_g_ahat_gf,
    # DT and BPS
    dt_degree0_k3xe,
    macmahon_coeffs,
    macmahon_power_zero,
    yau_zaslow_coeffs,
    bps_count_k3_genus0,
    bekenstein_hawking_entropy,
    dvv_bps_asymptotic,
    # GV invariants
    gv_invariants_k3_genus0,
    verify_gv_integrality,
    # HH
    hh_dimensions_k3xe,
    hh_total_dim_k3xe,
    # Brauer group
    brauer_group_k3xe,
    autoequivalence_generators_k3xe,
    # Gluing
    gluing_construction_summary,
    # Chiral algebra
    chiral_algebra_k3xe,
    n4_ope_structure,
    koszul_dual_k3xe,
    # Holographic datum
    holographic_datum_k3xe,
    # Cross-checks
    cross_check_euler,
    cross_check_kappa,
    cross_check_dt_degree0,
    cross_check_bps_vs_entropy,
    cross_check_gv_integrality,
    cross_check_hodge_diamond,
    cross_check_k0_rank,
    cross_check_hh_vs_hodge,
    cross_check_f1_multi_path,
    cross_check_f2_multi_path,
    # Open problems
    open_problems,
    # Master table
    master_data_table,
    run_all_cross_checks,
    verify_all_consistent,
)

F = Fraction


# ============================================================================
# Section 0: Arithmetic helpers
# ============================================================================

class TestArithmeticHelpers:
    """Tests for sigma_k, partition_count, Bernoulli, FP, eta, etc."""

    def test_sigma_1_small(self):
        """sigma_1(n) = sum of divisors."""
        assert sigma_k(1, 1) == 1
        assert sigma_k(2, 1) == 3
        assert sigma_k(3, 1) == 4
        assert sigma_k(6, 1) == 12
        assert sigma_k(12, 1) == 28

    def test_sigma_3_small(self):
        """sigma_3(n) for Eisenstein E_4."""
        assert sigma_k(1, 3) == 1
        assert sigma_k(2, 3) == 9
        assert sigma_k(3, 3) == 28
        assert sigma_k(4, 3) == 73

    def test_partition_count(self):
        """Partition numbers p(n)."""
        assert partition_count(0) == 1
        assert partition_count(1) == 1
        assert partition_count(2) == 2
        assert partition_count(3) == 3
        assert partition_count(4) == 5
        assert partition_count(5) == 7
        assert partition_count(10) == 42

    def test_bernoulli(self):
        """Bernoulli numbers B_n."""
        assert bernoulli_number(0) == F(1)
        assert bernoulli_number(1) == F(-1, 2)
        assert bernoulli_number(2) == F(1, 6)
        assert bernoulli_number(4) == F(-1, 30)
        assert bernoulli_number(6) == F(1, 42)
        assert bernoulli_number(3) == F(0)
        assert bernoulli_number(5) == F(0)

    def test_faber_pandharipande_g1(self):
        """lambda_1^FP = 1/24."""
        assert faber_pandharipande(1) == F(1, 24)

    def test_faber_pandharipande_g2(self):
        """lambda_2^FP = 7/5760."""
        assert faber_pandharipande(2) == F(7, 5760)

    def test_faber_pandharipande_g3(self):
        """lambda_3^FP = 31/967680."""
        assert faber_pandharipande(3) == F(31, 967680)

    def test_eta_product_leading(self):
        """prod(1-q^n) starts with 1, -1, -1, 0, 0, 1, 0, 1, ..."""
        c = eta_product_coeffs(10)
        assert c[0] == 1
        assert c[1] == -1
        assert c[2] == -1
        assert c[3] == 0
        assert c[4] == 0
        assert c[5] == 1
        assert c[7] == 1

    def test_partition_generating(self):
        """1/prod(1-q^n) = sum p(n) q^n."""
        c = partition_generating_coeffs(15)
        assert c[0] == 1
        assert c[1] == 1
        assert c[2] == 2
        assert c[3] == 3
        assert c[4] == 5
        assert c[5] == 7
        assert c[10] == 42

    def test_eta_inverse_is_partition(self):
        """eta^{-1} coefficients (without q^{-1/24}) = partition numbers."""
        c = eta_power_coeffs(15, -1)
        for n in range(15):
            assert c[n] == partition_count(n), f"Mismatch at n={n}"

    def test_eisenstein_e4_leading(self):
        """E_4 = 1 + 240*q + 2160*q^2 + ..."""
        c = eisenstein_coeffs(4, 5)
        assert c[0] == 1
        assert c[1] == 240
        assert c[2] == 2160
        assert c[3] == 6720

    def test_eisenstein_e6_leading(self):
        """E_6 = 1 - 504*q - 16632*q^2 - ..."""
        c = eisenstein_coeffs(6, 4)
        assert c[0] == 1
        assert c[1] == -504
        assert c[2] == -16632


# ============================================================================
# Section 1: Hodge diamond
# ============================================================================

class TestHodgeDiamond:
    """Tests for Hodge diamonds: K3, E, K3 x E, quintic."""

    def test_k3_euler(self):
        """chi(K3) = 24."""
        assert k3_hodge().euler == 24

    def test_elliptic_euler(self):
        """chi(E) = 0."""
        assert elliptic_hodge().euler == 0

    def test_k3xe_euler_kunneth(self):
        """chi(K3 x E) = chi(K3) * chi(E) = 24 * 0 = 0."""
        assert k3xe_hodge().euler == 0

    def test_k3xe_euler_direct(self):
        """chi from direct Hodge diamond summation."""
        hd = k3xe_hodge()
        chi = sum((-1) ** (p + q) * hd.h(p, q)
                  for p in range(4) for q in range(4))
        assert chi == 0

    def test_k3xe_euler_betti(self):
        """chi from alternating Betti sum."""
        hd = k3xe_hodge()
        bn = hd.betti_numbers
        chi = sum((-1) ** k * bn.get(k, 0) for k in range(7))
        assert chi == 0

    def test_k3xe_h21(self):
        """h^{2,1}(K3 x E) = 21."""
        assert k3xe_hodge().h(2, 1) == 21

    def test_k3xe_h11(self):
        """h^{1,1}(K3 x E) = 21."""
        assert k3xe_hodge().h(1, 1) == 21

    def test_k3xe_h30(self):
        """h^{3,0}(K3 x E) = 1 (CY3 condition)."""
        assert k3xe_hodge().h(3, 0) == 1

    def test_k3xe_h10(self):
        """h^{1,0}(K3 x E) = 1 (from E factor)."""
        assert k3xe_hodge().h(1, 0) == 1

    def test_k3xe_hodge_symmetry(self):
        """h^{p,q} = h^{q,p} (Hodge symmetry)."""
        hd = k3xe_hodge()
        for p in range(4):
            for q in range(4):
                assert hd.h(p, q) == hd.h(q, p), f"Hodge symmetry fails at ({p},{q})"

    def test_k3xe_serre_duality(self):
        """h^{p,q} = h^{3-p,3-q} (Serre duality for CY3)."""
        hd = k3xe_hodge()
        for p in range(4):
            for q in range(4):
                assert hd.h(p, q) == hd.h(3 - p, 3 - q), f"Serre fails at ({p},{q})"

    def test_k3xe_betti_numbers(self):
        """Betti numbers b_0=1, b_1=2, b_2=23, b_3=44, b_4=23, b_5=2, b_6=1."""
        bn = k3xe_hodge().betti_numbers
        assert bn[0] == 1
        assert bn[1] == 2
        assert bn[2] == 23
        assert bn[3] == 44
        assert bn[4] == 23
        assert bn[5] == 2
        assert bn[6] == 1

    def test_k3xe_chi_y_vanishes(self):
        """chi_y(K3 x E) = 0 (from chi_y(E) = 0)."""
        assert k3xe_hodge().chi_y_vanishes

    def test_k3_chi_y_nonzero(self):
        """chi_y(K3) != 0."""
        assert not k3_hodge().chi_y_vanishes

    def test_quintic_euler(self):
        """chi(quintic) = -200."""
        assert quintic_hodge().euler == -200

    def test_product_hodge_kunneth_entry(self):
        """Verify specific Kunneth product entries."""
        hd = k3xe_hodge()
        # h^{2,2}(K3xE) = sum h^{a,c}(K3)*h^{2-a,2-c}(E)
        # a=2,c=2: h^{2,2}(K3)*h^{0,0}(E) = 1*1 = 1
        # a=1,c=1: h^{1,1}(K3)*h^{1,1}(E) = 20*1 = 20
        # a=0,c=0: h^{0,0}(K3)*h^{2,2}(E) -- but h^{2,2}(E) = 0 (E is dim 1)
        # a=2,c=1: h^{2,1}(K3)*h^{0,1}(E) = 0*1 = 0
        # a=1,c=2: h^{1,2}(K3)*h^{1,0}(E) = 0*1 = 0
        # a=2,c=0: h^{2,0}(K3)*h^{0,2}(E) -- h^{0,2}(E) = 0
        # a=0,c=2: h^{0,2}(K3)*h^{2,0}(E) -- h^{2,0}(E) = 0
        # a=0,c=1: h^{0,1}(K3)*h^{2,1}(E) -- h^{2,1}(E) = 0
        # a=1,c=0: h^{1,0}(K3)*h^{1,2}(E) -- h^{1,2}(E) = 0
        # So h^{2,2} = 1 + 20 = 21
        assert hd.h(2, 2) == 21

    def test_total_hodge_sum(self):
        """Sum of all h^{p,q} = 96 for K3 x E."""
        hd = k3xe_hodge()
        total = sum(hd.h(p, q) for p in range(4) for q in range(4))
        assert total == 96


# ============================================================================
# Section 2: K-theory and lattice data
# ============================================================================

class TestKTheory:
    """Tests for K_0 rank, Mukai lattice, Euler form."""

    def test_k0_rank(self):
        """K_0(K3 x E) = Z^48."""
        assert k0_rank_k3xe() == 48

    def test_k0_rank_product(self):
        """K_0 rank = K_0(K3) * K_0(E) = 24 * 2 = 48."""
        assert MUKAI_RANK_K3 * 2 == 48

    def test_mukai_lattice(self):
        """Mukai lattice rank 24, signature (4,20)."""
        ml = mukai_lattice_k3()
        assert ml["rank"] == 24
        assert ml["signature"] == (4, 20)

    def test_euler_form_antisymmetric(self):
        """Euler form on CY3 is antisymmetric."""
        ef = euler_form_k3xe()
        assert ef["symmetry"] == "antisymmetric"

    def test_h_even_rank(self):
        """H^{even} rank = b_0 + b_2 + b_4 + b_6 = 1+23+23+1 = 48."""
        assert h_even_rank_k3xe() == 48

    def test_k0_equals_h_even(self):
        """K_0 rank = H^{even} rank (Chern character isomorphism)."""
        assert k0_rank_k3xe() == h_even_rank_k3xe()

    def test_hpp_sum(self):
        """sum h^{p,p} = 44 for K3 x E (diagonal Hodge numbers).

        NOTE: sum h^{p,p} = 1+21+21+1 = 44 != 48 = rk K_0.
        The Chern character isomorphism K_0 tensor Q -> H^{even} uses
        BETTI numbers b_{2k} = sum_{p+q=2k} h^{p,q}, not just h^{p,p}.
        For K3 x E: b_2 = h^{2,0}+h^{1,1}+h^{0,2} = 1+21+1 = 23, not h^{1,1}=21.
        """
        hd = k3xe_hodge()
        hpp_sum = sum(hd.h(p, p) for p in range(4))
        assert hpp_sum == 44


# ============================================================================
# Section 3: Modular characteristics (kappa)
# ============================================================================

class TestKappa:
    """Tests for kappa values: multi-path verification."""

    def test_kappa_k3_sigma(self):
        """kappa(K3 sigma model) = 2 = dim_C(K3)."""
        assert kappa_k3_sigma() == 2

    def test_kappa_e_sigma(self):
        """kappa(E sigma model) = 1 = dim_C(E)."""
        assert kappa_e_sigma() == 1

    def test_kappa_k3xe_additivity(self):
        """kappa(K3xE) = kappa(K3) + kappa(E) = 2+1 = 3."""
        assert kappa_k3xe() == kappa_k3_sigma() + kappa_e_sigma()

    def test_kappa_k3xe_value(self):
        """kappa(K3xE) = 3 = dim_C(K3 x E)."""
        assert kappa_k3xe() == 3

    def test_kappa_gepner_orbifolded(self):
        """kappa(Gepner/K3) = 2 after orbifold."""
        assert kappa_gepner_k3() == F(2)

    def test_kappa_kummer_free_boson(self):
        """kappa(V_{T^4}) = 4 = rank (free boson, different from sigma model!)."""
        assert kappa_kummer_lattice() == 4

    def test_kappa_sigma_ne_lattice(self):
        """kappa(K3 sigma) != kappa(V_{T^4}): different algebras, AP48."""
        assert kappa_k3_sigma() != kappa_kummer_lattice()

    def test_kappa_from_F1(self):
        """kappa = 24 * F_1 = 24 * 1/8 = 3."""
        assert 24 * shadow_F_g(1) == F(kappa_k3xe())

    def test_kappa_discrepancy_doc(self):
        """Discrepancy explanation provides all 5 values."""
        ex = kappa_discrepancy_explanation()
        assert ex["k3_sigma_model"] == 2
        assert ex["gepner_unorbifolded"] == 3
        assert ex["free_boson_T4"] == 4
        assert ex["k3xe_value"] == 3


# ============================================================================
# Section 4: Shadow obstruction tower
# ============================================================================

class TestShadowTower:
    """Tests for shadow amplitudes, metric, depth, connection."""

    def test_F1_value(self):
        """F_1 = kappa/24 = 3/24 = 1/8."""
        assert shadow_F_g(1) == F(1, 8)

    def test_F2_value(self):
        """F_2 = kappa * 7/5760 = 21/5760 = 7/1920."""
        assert shadow_F_g(2) == F(7, 1920)

    def test_F3_value(self):
        """F_3 = kappa * 31/967680 = 93/967680 = 31/322560."""
        assert shadow_F_g(3) == F(31, 322560)

    def test_F1_from_bernoulli(self):
        """F_1 from Bernoulli: B_2=1/6, lambda_1 = 1/2 * 1/6 / 2 = 1/24."""
        B2 = bernoulli_number(2)
        lambda_1 = F(2 ** 1 - 1, 2 ** 1) * abs(B2) / math.factorial(2)
        assert lambda_1 == F(1, 24)
        assert F(3) * lambda_1 == F(1, 8)

    def test_F2_from_bernoulli(self):
        """F_2 from Bernoulli: B_4=-1/30, lambda_2 = 7/8 * 1/30 / 24 = 7/5760."""
        B4 = bernoulli_number(4)
        lambda_2 = F(2 ** 3 - 1, 2 ** 3) * abs(B4) / math.factorial(4)
        assert lambda_2 == F(7, 5760)
        assert F(3) * lambda_2 == F(7, 1920)

    def test_shadow_metric_at_zero(self):
        """Q_L(0) = (2*kappa)^2 = 36 for kappa=3."""
        assert shadow_metric_k3xe(F(0)) == F(36)

    def test_shadow_depth_class_M(self):
        """K3 x E has shadow depth class M (infinite)."""
        sd = shadow_depth_k3xe()
        assert sd["class"] == "M"
        assert sd["depth"] == float("inf")

    def test_shadow_connection_monodromy(self):
        """Shadow connection monodromy = -1 (Koszul sign)."""
        sc = shadow_connection_k3xe()
        assert sc["monodromy"] == -1
        assert sc["residue"] == F(1, 2)

    def test_Fg_positive_all_genera(self):
        """F_g > 0 for all g >= 1 (Bernoulli alternating signs give positive FP)."""
        for g in range(1, 6):
            assert shadow_F_g(g) > 0, f"F_{g} should be positive"

    def test_Fg_decreasing(self):
        """F_g / F_{g-1} decreases (roughly like 1/(2*pi)^2 per genus)."""
        for g in range(2, 5):
            ratio = float(shadow_F_g(g) / shadow_F_g(g - 1))
            assert ratio < 0.1, f"F_{g}/F_{g-1} = {ratio} not decreasing fast enough"

    def test_genus_g_scalar_matches_shadow(self):
        """genus_g_amplitude_scalar and shadow_F_g agree."""
        for g in range(1, 5):
            assert genus_g_amplitude_scalar(g) == shadow_F_g(g)


# ============================================================================
# Section 5: DT invariants and BPS counting
# ============================================================================

class TestDTAndBPS:
    """Tests for DT_0, MacMahon, Yau-Zaslow, BPS, entropy."""

    def test_dt_degree0(self):
        """DT_0 = 1 for chi = 0."""
        assert dt_degree0_k3xe() == 1

    def test_macmahon_power_zero(self):
        """M(-q)^0 = 1."""
        assert macmahon_power_zero() == 1

    def test_macmahon_leading(self):
        """M(q) = 1 + q + 3*q^2 + 6*q^3 + 13*q^4 + ..."""
        c = macmahon_coeffs(8)
        assert c[0] == 1
        assert c[1] == 1
        assert c[2] == 3
        assert c[3] == 6

    def test_yau_zaslow_n0(self):
        """n^0_0 = 1 (Yau-Zaslow)."""
        assert bps_count_k3_genus0(0) == 1

    def test_yau_zaslow_n1(self):
        """n^0_1 = 24 (Yau-Zaslow)."""
        assert bps_count_k3_genus0(1) == 24

    def test_yau_zaslow_n2(self):
        """n^0_2 = 324 (Yau-Zaslow)."""
        assert bps_count_k3_genus0(2) == 324

    def test_yau_zaslow_n3(self):
        """n^0_3 = 3200 (Yau-Zaslow, literature value)."""
        assert bps_count_k3_genus0(3) == 3200

    def test_yau_zaslow_n4(self):
        """n^0_4 = 25650 (Yau-Zaslow)."""
        assert bps_count_k3_genus0(4) == 25650

    def test_yau_zaslow_integrality(self):
        """All n^0_d are integers for d = 0,...,8."""
        for d in range(9):
            n = bps_count_k3_genus0(d)
            assert isinstance(n, int), f"n^0_{d} = {n} not integer"
            assert n > 0, f"n^0_{d} should be positive"

    def test_yau_zaslow_is_eta_inverse_24(self):
        """n^0_d = coefficient of q^d in 1/eta^{24} (without q-shift).

        Precisely: sum n^0_d q^{d-1} = 1/Delta(q) = q^{-1} / prod(1-q^n)^{24}.
        So n^0_d = partition_like coefficient of 1/prod(1-q^n)^{24} at index d.
        """
        nmax = 10
        c = eta_power_coeffs(nmax, -24)
        for d in range(min(6, nmax)):
            assert bps_count_k3_genus0(d) == c[d], f"Mismatch at d={d}"

    def test_entropy_formula(self):
        """S_BH = 4*pi*sqrt(Delta)."""
        assert bekenstein_hawking_entropy(1) == pytest.approx(4 * math.pi)
        assert bekenstein_hawking_entropy(4) == pytest.approx(8 * math.pi)
        assert bekenstein_hawking_entropy(0) == 0.0

    def test_entropy_negative_delta(self):
        """S_BH = 0 for Delta < 0 (no black hole)."""
        assert bekenstein_hawking_entropy(-1) == 0.0

    def test_bps_entropy_consistency(self):
        """log(d(Delta)) ~ S_BH for large Delta (leading order)."""
        for Delta in [25, 36, 49]:
            s_bh = bekenstein_hawking_entropy(Delta)
            d_asymp = dvv_bps_asymptotic(Delta)
            log_d = math.log(d_asymp)
            # Leading term should match within 50% for these moderate Delta
            assert abs(log_d - s_bh) / s_bh < 0.5, (
                f"Delta={Delta}: log d = {log_d:.2f}, S_BH = {s_bh:.2f}"
            )


# ============================================================================
# Section 6: Gopakumar-Vafa invariants
# ============================================================================

class TestGVInvariants:
    """Tests for GV integrality and values."""

    def test_gv_integrality(self):
        """GV invariants n^0_d are integers for d=0,...,10."""
        assert verify_gv_integrality(10)

    def test_gv_dictionary(self):
        """gv_invariants_k3_genus0 returns correct dictionary."""
        gv = gv_invariants_k3_genus0(4)
        assert gv[0] == 1
        assert gv[1] == 24
        assert gv[2] == 324
        assert gv[3] == 3200
        assert gv[4] == 25650

    def test_gv_positive(self):
        """All genus-0 GV invariants are positive."""
        gv = gv_invariants_k3_genus0(8)
        for d, n in gv.items():
            assert n > 0, f"n^0_{d} = {n} not positive"


# ============================================================================
# Section 7: Hochschild cohomology
# ============================================================================

class TestHochschild:
    """Tests for HH^n(K3 x E) via HKR."""

    def test_hh2_dimension(self):
        """HH^2(K3 x E) = 23 (deformation space dimension).

        HH^2 = h^{3,2} + h^{2,1} + h^{1,0} = 1 + 21 + 1 = 23.
        """
        hh = hh_dimensions_k3xe()
        assert hh[2] == 23

    def test_hh0_dimension(self):
        """HH^0(K3 x E) = h^{3,0} = 1."""
        hh = hh_dimensions_k3xe()
        assert hh[0] == 1

    def test_hh1_dimension(self):
        """HH^1(K3 x E) = h^{3,1} + h^{2,0} = 1 + 1 = 2."""
        hh = hh_dimensions_k3xe()
        assert hh[1] == 2

    def test_hh3_dimension(self):
        """HH^3(K3 x E) = h^{3,3} + h^{2,2} + h^{1,1} + h^{0,0} = 1+21+21+1 = 44."""
        hh = hh_dimensions_k3xe()
        assert hh[3] == 44

    def test_hh_serre_symmetry(self):
        """HH^n = HH^{d-n} for CY d-fold (n=3): HH^n = HH^{3-n} by Serre."""
        hh = hh_dimensions_k3xe()
        # For CY3, HH^n and HH^{6-n} are Serre dual
        # But by HKR, HH^n = sum h^{3-p,q} for p+q=n
        # The duality is HH^n ~ (HH^{6-n})^*, so dim HH^n = dim HH^{6-n}
        for n in range(7):
            if n in hh and (6 - n) in hh:
                assert hh[n] == hh[6 - n], f"HH^{n} != HH^{6-n}"

    def test_hh_total(self):
        """Total HH dimension = sum of Hodge numbers h^{3-p,q}."""
        hh = hh_dimensions_k3xe()
        total = sum(hh.values())
        assert total == hh_total_dim_k3xe()


# ============================================================================
# Section 8: Brauer group and autoequivalences
# ============================================================================

class TestBrauerAndAut:
    """Tests for Brauer group structure and autoequivalence data."""

    def test_brauer_rho1(self):
        """Br(K3 x E) contains (Q/Z)^22 for rho = 1."""
        br = brauer_group_k3xe(picard_rank_k3=1)
        assert br["torsion_rank"] == 22

    def test_brauer_rho0(self):
        """Br(K3 x E) contains (Q/Z)^23 for generic rho = 0."""
        br = brauer_group_k3xe(picard_rank_k3=0)
        assert br["torsion_rank"] == 23

    def test_brauer_mixed_zero(self):
        """Mixed term H^1(K3, Pic^0(E)) = 0."""
        br = brauer_group_k3xe()
        assert br["mixed"] == 0

    def test_no_exceptional_objects(self):
        """K3 x E (CY3) has no exceptional objects."""
        ae = autoequivalence_generators_k3xe()
        assert ae["no_exceptional_objects"] is True


# ============================================================================
# Section 9: Chiral algebra and OPE
# ============================================================================

class TestChiralAlgebra:
    """Tests for chiral algebra structure, OPE, bar complex."""

    def test_total_generators(self):
        """9 primary generators: T + 4G + 3J + j_E."""
        ca = chiral_algebra_k3xe()
        assert ca["total_generators"] == 9

    def test_central_charge(self):
        """c = 6 + 1 = 7."""
        ca = chiral_algebra_k3xe()
        assert ca["central_charge"] == 7

    def test_bar_degree_1(self):
        """Bar degree 1 has 9 generators (one per primary)."""
        ca = chiral_algebra_k3xe()
        assert ca["bar_degree_1_dim"] == 9

    def test_kappa_in_chiral(self):
        """kappa from chiral algebra data = 3."""
        ca = chiral_algebra_k3xe()
        assert ca["kappa"] == 3

    def test_expected_koszul(self):
        """K3 x E chiral algebra expected to be Koszul."""
        ca = chiral_algebra_k3xe()
        assert ca["koszul_expected"] is True

    def test_shadow_class_M(self):
        """Shadow class = M (infinite) from chiral algebra data."""
        ca = chiral_algebra_k3xe()
        assert ca["shadow_class"] == "M"

    def test_ope_tt_pole_4(self):
        """T(z)T(w) has maximal pole order 4 (c/2 coefficient)."""
        ope = n4_ope_structure()
        assert 4 in ope["TT"]["ope_poles"]

    def test_rmatrix_pole_shift(self):
        """AP19: r-matrix poles one less than OPE poles."""
        ope = n4_ope_structure()
        for channel, data in ope.items():
            max_ope = max(data["ope_poles"])
            max_r = max(data["rmatrix_poles"])
            assert max_r == max_ope - 1, (
                f"{channel}: max OPE pole = {max_ope}, max r-matrix pole = {max_r}"
            )


# ============================================================================
# Section 10: Koszul dual
# ============================================================================

class TestKoszulDual:
    """Tests for Koszul dual of K3 x E chiral algebra."""

    def test_kappa_dual_complementarity(self):
        """kappa(A^!) = -kappa(A) = -3 (complementarity)."""
        kd = koszul_dual_k3xe()
        assert kd["kappa_dual"] == -3

    def test_kappa_sum_zero(self):
        """kappa + kappa' = 0 (for free-field sectors)."""
        assert kappa_k3xe() + koszul_dual_k3xe()["kappa_dual"] == 0


# ============================================================================
# Section 11: Holographic datum
# ============================================================================

class TestHolographicDatum:
    """Tests for the holographic modular Koszul datum assembly."""

    def test_datum_has_six_components(self):
        """H(K3xE) has components A, A^!, C, r(z), Theta_A, nabla^hol."""
        hd = holographic_datum_k3xe()
        assert "A" in hd
        assert "A_dual" in hd
        assert "C" in hd
        assert "r_matrix" in hd
        assert "Theta_A" in hd
        assert "nabla_hol" in hd

    def test_derived_center_dimensions(self):
        """Derived center HH^* has correct dimensions."""
        hd = holographic_datum_k3xe()
        hh = hd["C"]["hh_dimensions"]
        assert hh[2] == 23  # HH^2 = deformation space

    def test_theta_kappa(self):
        """Theta_A arity-2 projection = kappa = 3."""
        hd = holographic_datum_k3xe()
        assert hd["Theta_A"]["arity_2"] == f"kappa = {kappa_k3xe()}"


# ============================================================================
# Section 12: Cross-consistency checks
# ============================================================================

class TestCrossChecks:
    """Tests for all cross-consistency checks (multi-path verification)."""

    def test_euler_3_paths(self):
        """chi = 0 by 3 independent paths."""
        result = cross_check_euler()
        assert result["consistent"]
        assert result["path_a_kunneth"] == 0
        assert result["path_b_hodge"] == 0
        assert result["path_c_betti"] == 0

    def test_kappa_3_paths(self):
        """kappa = 3 by 3 independent paths."""
        result = cross_check_kappa()
        assert result["consistent"]
        assert result["path_a_cy_dim"] == 3
        assert result["path_b_additivity"] == 3

    def test_dt_degree0_3_paths(self):
        """DT_0 = 1 by 3 independent paths."""
        result = cross_check_dt_degree0()
        assert result["consistent"]
        assert result["path_a_mnop"] == 1

    def test_hodge_diamond_3_paths(self):
        """Hodge diamond consistent by 3 paths (Kunneth, direct, symmetry)."""
        result = cross_check_hodge_diamond()
        assert result["consistent"]
        assert result["path_c_hodge_symmetry"]
        assert result["path_c_serre_symmetry"]

    def test_k0_rank_3_paths(self):
        """K_0 rank = 48 by 3 independent paths."""
        result = cross_check_k0_rank()
        assert result["consistent"]
        assert result["path_a_mukai_tensor"] == 48
        assert result["path_b_h_even"] == 48
        assert result["path_c_h_even_betti"] == 48

    def test_hh_vs_hodge(self):
        """HH^n matches HKR prediction from Hodge numbers."""
        result = cross_check_hh_vs_hodge()
        assert result["consistent"]
        assert result["hh2"] == 23

    def test_f1_3_paths(self):
        """F_1 = 1/8 by 3 independent paths."""
        result = cross_check_f1_multi_path()
        assert result["all_equal"]
        assert result["value"] == F(1, 8)

    def test_f2_3_paths(self):
        """F_2 = 7/1920 by 3 independent paths."""
        result = cross_check_f2_multi_path()
        assert result["all_equal"]

    def test_gv_integrality_cross_check(self):
        """GV invariants integral through d=10."""
        result = cross_check_gv_integrality()
        for d in range(min(11, len(result))):
            assert result[d], f"GV n^0_{d} not integral"


# ============================================================================
# Section 13: Master data table
# ============================================================================

class TestMasterTable:
    """Tests for the master data table assembly."""

    def test_table_has_all_sections(self):
        """Master table has geometry, kappa, shadow, DT, BPS, chiral, etc."""
        t = master_data_table()
        assert "geometry" in t
        assert "modular_characteristics" in t
        assert "shadow_tower" in t
        assert "dt_invariants" in t
        assert "bps" in t
        assert "chiral_algebra" in t
        assert "brauer_group" in t
        assert "hh_dimensions" in t

    def test_geometry_section(self):
        """Geometry section has correct invariants."""
        g = master_data_table()["geometry"]
        assert g["dim_C"] == 3
        assert g["chi"] == 0
        assert g["h21"] == 21
        assert g["h11"] == 21
        assert g["K0_rank"] == 48
        assert g["chi_y_vanishes"] is True

    def test_kappa_section(self):
        """Kappa section has all variants."""
        k = master_data_table()["modular_characteristics"]
        assert k["kappa_k3xe"] == 3
        assert k["kappa_k3"] == 2
        assert k["kappa_e"] == 1

    def test_shadow_section(self):
        """Shadow tower section has F_1, F_2, F_3."""
        s = master_data_table()["shadow_tower"]
        assert s["class"] == "M"
        assert s["F_1"] == "1/8"

    def test_dt_section(self):
        """DT section has DT_0 = 1."""
        d = master_data_table()["dt_invariants"]
        assert d["DT_0"] == 1
        assert d["chi_for_macmahon"] == 0

    def test_bps_section(self):
        """BPS section has Yau-Zaslow values."""
        b = master_data_table()["bps"]
        assert b["n0_0"] == 1
        assert b["n0_1"] == 24
        assert b["n0_2"] == 324


# ============================================================================
# Section 14: Open problems
# ============================================================================

class TestOpenProblems:
    """Tests for open problem documentation."""

    def test_eight_problems(self):
        """8 open problems documented."""
        assert len(open_problems()) == 8

    def test_each_problem_has_fields(self):
        """Each problem has id, title, computed, remains, tools."""
        for p in open_problems():
            assert "id" in p
            assert "title" in p
            assert "computed" in p
            assert "remains" in p
            assert "tools" in p


# ============================================================================
# Section 15: Full cross-check suite
# ============================================================================

class TestFullSuite:
    """Integration tests: run all checks together."""

    def test_all_cross_checks_pass(self):
        """All cross-consistency checks pass."""
        assert verify_all_consistent()

    def test_run_all_returns_dict(self):
        """run_all_cross_checks returns a dictionary with all check names."""
        results = run_all_cross_checks()
        assert "euler" in results
        assert "kappa" in results
        assert "dt_degree0" in results
        assert "f1" in results
        assert "f2" in results


# ============================================================================
# Section 16: Synthesis tests (cross-engine consistency)
# ============================================================================

class TestSynthesis:
    """Cross-engine synthesis tests verifying internal consistency."""

    def test_chi_times_chi_equals_zero(self):
        """chi(K3) * chi(E) = 24 * 0 = 0 = chi(K3xE)."""
        assert k3_hodge().euler * elliptic_hodge().euler == k3xe_hodge().euler

    def test_kappa_additivity_matches_dim(self):
        """kappa = dim_C for CY manifolds."""
        assert kappa_k3xe() == k3xe_hodge().dim

    def test_dt0_from_chi(self):
        """DT_0 = 1 because chi = 0."""
        chi = k3xe_hodge().euler
        assert chi == 0
        assert dt_degree0_k3xe() == 1

    def test_f1_from_kappa(self):
        """F_1 = kappa/24 = 3/24 = 1/8."""
        assert shadow_F_g(1) == F(kappa_k3xe(), 24)

    def test_k0_from_mukai_and_e(self):
        """K_0 rank from Mukai x K_0(E) = 24 x 2 = 48 = H^{even} rank."""
        assert MUKAI_RANK_K3 * 2 == h_even_rank_k3xe()

    def test_hh2_equals_deformations(self):
        """HH^2 = 23 = h^{2,1} + h^{1,0} + h^{3,2} = 21+1+1 (deformations)."""
        hd = k3xe_hodge()
        hh2_from_hodge = hd.h(3, 2) + hd.h(2, 1) + hd.h(1, 0)
        assert hh2_from_hodge == 23
        assert hh_dimensions_k3xe()[2] == 23

    def test_yau_zaslow_matches_eta24(self):
        """Yau-Zaslow n^0_d = coefficients of 1/prod(1-q^n)^{24}."""
        nmax = 8
        yz = yau_zaslow_coeffs(nmax)
        e24inv = eta_power_coeffs(nmax, -24)
        for d in range(nmax):
            assert yz[d] == e24inv[d], f"Mismatch at d={d}: YZ={yz[d]}, eta^-24={e24inv[d]}"

    def test_entropy_matches_cardy(self):
        """Bekenstein-Hawking entropy S = 4*pi*sqrt(Delta) is the Cardy formula."""
        # For Delta = n^2: S = 4*pi*n
        for n in range(1, 5):
            s = bekenstein_hawking_entropy(n ** 2)
            assert abs(s - 4 * math.pi * n) < 1e-10

    def test_shadow_connection_consistent_with_depth(self):
        """Class M => 2 singular points in shadow connection."""
        sd = shadow_depth_k3xe()
        sc = shadow_connection_k3xe()
        assert sd["class"] == "M"
        assert sc["singular_points"] == 2

    def test_bar_generators_match_chiral(self):
        """Bar degree 1 = number of primary generators = 9."""
        ca = chiral_algebra_k3xe()
        assert ca["bar_degree_1_dim"] == ca["total_generators"]

    def test_complementarity_kappa(self):
        """kappa(A) + kappa(A^!) = 0."""
        assert kappa_k3xe() + koszul_dual_k3xe()["kappa_dual"] == 0

    def test_no_exceptional_from_chi(self):
        """chi = 0 on CY3 => no exceptional objects in D^b."""
        assert k3xe_hodge().euler == 0
        ae = autoequivalence_generators_k3xe()
        assert ae["no_exceptional_objects"] is True

    def test_gluing_k0_matches(self):
        """Glued K_0 rank = actual K_0 rank = 48."""
        gs = gluing_construction_summary()
        assert gs["k0_rank_expected"] == gs["k0_rank_glued"] == 48

    def test_holographic_datum_complete(self):
        """Holographic datum has all 6 components with consistent data."""
        hd = holographic_datum_k3xe()
        assert hd["A"]["kappa"] == 3
        assert hd["A_dual"]["kappa_dual"] == -3
        assert hd["nabla_hol"]["monodromy"] == -1
        assert hd["C"]["hh_dimensions"][2] == 23
