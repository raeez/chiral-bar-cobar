r"""Tests for the celestial shadow engine: bar complex of w_{1+\infty}.

Verifies:
1. W_N central charge formula at low N (cross-checked against known values)
2. OPE structure constants for TT, TW, WW at low spins
3. Channel-refined kappa = c * (H_N - 1) for W_N
4. kappa(W_2) = c/2 (Virasoro consistency)
5. Harmonic number divergence of kappa at large N
6. Bar complex construction at low arities
7. r-matrix pole orders (AP19: pole reduced by 1 from OPE)
8. r-matrix all-odd-poles property (bosonic algebra)
9. Shadow depth = class M for all N >= 2
10. Shadow kappa, cubic C, quartic Q on Virasoro channel
11. Shadow discriminant Delta = 40/(5c+22)
12. Soft graviton theorems at order 0, 1, 2 from shadow projections
13. Large-N scaling: kappa ~ c * ln(N)
14. Spin-1 sector = Kac-Moody (class L, depth 3)
15. MHV collinear factorization from bar differential
16. Gaberdiel-Gopakumar 't Hooft limit scaling
17. Cross-spin consistency checks
18. Channel vector completeness

Ground truth sources:
   - kappa(W_N) = c * (H_N - 1) (wn_channel_refined.py, concordance.tex)
   - c(W_N) = (N-1) - N(N^2-1)(k+N-1)^2/(k+N) (standard DS formula)
   - Q^contact_Vir = 10/[c(5c+22)] (higher_genus_modular_koszul.tex)
   - r-matrix pole = OPE pole - 1 (AP19)
   - Com^! = Lie, shadow depth G/L/C/M classification
   - Parke-Taylor: A_n^{MHV} = <ij>^4 / prod <k,k+1>

References:
   celestial_shadow_engine.py (compute/lib/)
   celestial_koszul_ope.py (compute/lib/)
   wn_channel_refined.py (compute/lib/)
   concordance.tex, higher_genus_modular_koszul.tex
"""

from fractions import Fraction

import pytest

from compute.lib.celestial_shadow_engine import (
    # Arithmetic helpers
    harmonic_number,
    # W_N data
    WNAlgebraData,
    wn_central_charge,
    make_wn,
    # w_{1+infty} truncation
    WInfinityTruncation,
    make_w_infinity_trunc,
    # OPE structure constants
    CelestialOPEStructureConstant,
    ope_self_coupling_coefficient,
    ope_tt_coefficients,
    ope_tw_coefficients,
    ope_ww_leading_coefficient,
    ope_general_self_leading,
    ope_conformal_weight_term,
    # Channel-refined kappa
    channel_kappa,
    kappa_wn,
    kappa_w_infinity_normalized,
    kappa_w_infinity_scaling,
    # Bar complex
    CelestialBarComplex,
    celestial_bar_complex,
    # r-matrix
    CelestialRMatrix,
    celestial_r_matrix,
    r_matrix_pole_orders_spin_s,
    verify_celestial_collinear_matching,
    # Shadow depth
    shadow_depth_wn,
    shadow_depth_w_infinity,
    verify_shadow_depth_class_m,
    # Shadow projections
    shadow_kappa,
    shadow_kappa_virasoro_channel,
    shadow_cubic_virasoro,
    shadow_quartic_contact_virasoro,
    shadow_discriminant_virasoro,
    shadow_tower_virasoro_channel,
    # Soft theorems
    SoftGravitonTheorem,
    soft_theorem_from_shadow,
    verify_soft_kappa_leading,
    verify_soft_cubic_subleading,
    verify_soft_quartic_subsubleading,
    # Large-N scaling
    large_n_kappa_scaling,
    large_n_channel_vector,
    # MHV
    parke_taylor_mhv_n,
    mhv_collinear_factorization,
    # Spin-1 sector
    spin1_sector_is_kac_moody,
    # Gaberdiel-Gopakumar
    gaberdiel_gopakumar_central_charge,
    gaberdiel_gopakumar_kappa,
    thooft_limit_kappa_scaling,
    # Full suite
    run_full_celestial_shadow_verification,
)
from compute.lib.wn_central_charge_canonical import c_wn_fl as canonical_c_wn_fl


# ============================================================================
# Section 1: Harmonic numbers (exact arithmetic)
# ============================================================================

class TestHarmonicNumbers:
    """Verify harmonic number computation."""

    def test_h1(self):
        assert harmonic_number(1) == Fraction(1)

    def test_h2(self):
        assert harmonic_number(2) == Fraction(3, 2)

    def test_h3(self):
        assert harmonic_number(3) == Fraction(11, 6)

    def test_h4(self):
        assert harmonic_number(4) == Fraction(25, 12)

    def test_h5(self):
        assert harmonic_number(5) == Fraction(137, 60)

    def test_h0(self):
        assert harmonic_number(0) == Fraction(0)

    def test_h_negative_raises(self):
        with pytest.raises(ValueError):
            harmonic_number(-1)


# ============================================================================
# Section 2: W_N central charge
# ============================================================================

class TestWNCentralCharge:
    """Verify central charge formula: c = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)."""

    def test_matches_canonical_helper(self):
        """Delegates to the canonical Fateev-Lukyanov implementation."""
        samples = [
            (2, Fraction(1)),
            (3, Fraction(1)),
            (5, Fraction(7, 3)),
        ]
        for N, k in samples:
            assert wn_central_charge(N, k) == canonical_c_wn_fl(N, k)

    def test_virasoro_n2_k1(self):
        """Virasoro from sl_2 DS at k=1: c = 1 - 6*4/3 = -7."""
        c = wn_central_charge(2, Fraction(1))
        # c = 1 - 2*3*(1+2-1)^2/(1+2) = 1 - 6*4/3 = 1 - 8 = -7
        assert c == Fraction(-7)

    def test_virasoro_n2_k10(self):
        """Virasoro from sl_2 DS at k=10: c = 1 - 6*121/12."""
        c = wn_central_charge(2, Fraction(10))
        expected = Fraction(1) - Fraction(6) * Fraction(121) / Fraction(12)
        assert c == expected

    def test_critical_level_raises(self):
        """k = -N is critical: should raise ValueError."""
        with pytest.raises(ValueError):
            wn_central_charge(3, Fraction(-3))

    def test_w3_k1(self):
        """W_3 at k=1: c = 2 - 3*8*9/4 = 2 - 54 = -52."""
        # c = (3-1) - 3*(9-1)*(1+3-1)^2/(1+3) = 2 - 24*9/4 = 2 - 54 = -52
        # Let me recompute: N=3, k=1, N^2-1=8, k+N-1=3, (k+N-1)^2=9, k+N=4
        # c = 2 - 3*8*9/4 = 2 - 54 = -52
        c = wn_central_charge(3, Fraction(1))
        assert c == Fraction(-52)

    def test_make_wn_constructs(self):
        """make_wn returns correct data."""
        w = make_wn(3, Fraction(1))
        assert w.N == 3
        assert w.level == Fraction(1)
        assert w.num_generators == 2  # spins 2, 3
        assert w.generator_spins == [2, 3]


# ============================================================================
# Section 3: OPE structure constants
# ============================================================================

class TestOPEStructureConstants:
    """Verify OPE coefficients at low spins."""

    def test_self_coupling_spin2(self):
        """Self-coupling for spin 2: c/2."""
        c = Fraction(30)
        assert ope_self_coupling_coefficient(2, c) == Fraction(15)

    def test_self_coupling_spin3(self):
        """Self-coupling for spin 3: c/3."""
        c = Fraction(30)
        assert ope_self_coupling_coefficient(3, c) == Fraction(10)

    def test_self_coupling_spin1(self):
        """Self-coupling for spin 1: c/1 = c."""
        c = Fraction(30)
        assert ope_self_coupling_coefficient(1, c) == Fraction(30)

    def test_self_coupling_spin5(self):
        """Self-coupling for spin 5: c/5."""
        c = Fraction(30)
        assert ope_self_coupling_coefficient(5, c) == Fraction(6)

    def test_self_coupling_spin_invalid(self):
        with pytest.raises(ValueError):
            ope_self_coupling_coefficient(0, Fraction(30))

    def test_tt_ope_vacuum_coeff(self):
        """TT OPE vacuum channel: coefficient c/2."""
        c = Fraction(26)
        tt = ope_tt_coefficients(c)
        assert tt["vacuum"].coefficient == Fraction(13)

    def test_tt_ope_vacuum_pole(self):
        """TT OPE vacuum channel: pole order 4."""
        tt = ope_tt_coefficients(Fraction(26))
        assert tt["vacuum"].pole_order == 4

    def test_tt_ope_T_coeff(self):
        """TT OPE T channel: coefficient 2."""
        tt = ope_tt_coefficients(Fraction(26))
        assert tt["T"].coefficient == Fraction(2)

    def test_tt_ope_T_pole(self):
        """TT OPE T channel: pole order 2."""
        tt = ope_tt_coefficients(Fraction(26))
        assert tt["T"].pole_order == 2

    def test_tt_ope_dT_coeff(self):
        """TT OPE dT channel: coefficient 1."""
        tt = ope_tt_coefficients(Fraction(26))
        assert tt["dT"].coefficient == Fraction(1)

    def test_tt_ope_dT_pole(self):
        """TT OPE dT channel: pole order 1."""
        tt = ope_tt_coefficients(Fraction(26))
        assert tt["dT"].pole_order == 1

    def test_tw_ope_W_coeff(self):
        """TW OPE: coefficient = conformal weight 3."""
        tw = ope_tw_coefficients(Fraction(26))
        assert tw["W"].coefficient == Fraction(3)

    def test_tw_ope_W_pole(self):
        """TW OPE: pole order 2."""
        tw = ope_tw_coefficients(Fraction(26))
        assert tw["W"].pole_order == 2

    def test_ww_leading(self):
        """WW OPE leading coefficient = c/3."""
        c = Fraction(30)
        assert ope_ww_leading_coefficient(c) == Fraction(10)

    def test_general_self_leading_spin4(self):
        """Spin-4 self-OPE leading: c/4 at pole 8."""
        c = Fraction(24)
        ope = ope_general_self_leading(4, c)
        assert ope.coefficient == Fraction(6)
        assert ope.pole_order == 8

    def test_conformal_weight_term_spin4(self):
        """T(z) J^4(w): conformal weight = 4 at pole 2."""
        cw = ope_conformal_weight_term(2, 4)
        assert cw.coefficient == Fraction(4)
        assert cw.pole_order == 2

    def test_conformal_weight_term_wrong_spin_raises(self):
        """Conformal weight term only for s1=2."""
        with pytest.raises(ValueError):
            ope_conformal_weight_term(3, 4)


# ============================================================================
# Section 4: Channel-refined modular characteristic
# ============================================================================

class TestChannelRefinedKappa:
    """Verify kappa(W_N) = c * (H_N - 1)."""

    def test_kappa_w2_is_c_over_2(self):
        """kappa(W_2) = c/2 = kappa(Virasoro)."""
        c = Fraction(26)
        assert kappa_wn(2, c) == Fraction(13)

    def test_kappa_w3_is_5c_over_6(self):
        """kappa(W_3) = c * (H_3 - 1) = c * 5/6."""
        c = Fraction(30)
        assert kappa_wn(3, c) == Fraction(25)

    def test_kappa_w4_is_13c_over_12(self):
        """kappa(W_4) = c * (H_4 - 1) = c * 13/12."""
        c = Fraction(12)
        assert kappa_wn(4, c) == Fraction(13)

    def test_kappa_w5(self):
        """kappa(W_5) = c * (H_5 - 1) = c * 77/60."""
        c = Fraction(60)
        # H_5 - 1 = 137/60 - 1 = 77/60
        assert kappa_wn(5, c) == Fraction(77)

    def test_channel_kappa_spin2(self):
        """Channel kappa at spin 2: c/2."""
        assert channel_kappa(2, Fraction(30)) == Fraction(15)

    def test_channel_kappa_spin3(self):
        """Channel kappa at spin 3: c/3."""
        assert channel_kappa(3, Fraction(30)) == Fraction(10)

    def test_channel_sum_equals_total(self):
        """Sum of channel contributions = total kappa."""
        c = Fraction(30)
        N = 5
        total = sum(channel_kappa(s, c) for s in range(2, N + 1))
        assert total == kappa_wn(N, c)

    def test_channel_kappa_spin_invalid(self):
        with pytest.raises(ValueError):
            channel_kappa(0, Fraction(30))

    def test_kappa_normalized(self):
        """Normalized kappa: kappa/c = H_N - 1."""
        for N in [2, 3, 5, 10]:
            assert kappa_w_infinity_normalized(N) == harmonic_number(N) - 1

    def test_kappa_monotone_increasing(self):
        """kappa(W_N) increases with N for c > 0."""
        c = Fraction(30)
        prev = kappa_wn(2, c)
        for N in range(3, 15):
            curr = kappa_wn(N, c)
            assert curr > prev, f"kappa(W_{N}) = {curr} <= kappa(W_{N-1}) = {prev}"
            prev = curr


# ============================================================================
# Section 5: Bar complex construction
# ============================================================================

class TestBarComplex:
    """Verify bar complex of w_{1+infty}."""

    def test_bar_deg1_dim_with_spin1(self):
        """Bar degree 1 dim = N_max (spins 1, ..., N_max)."""
        bar = celestial_bar_complex(5, Fraction(30), include_spin_1=True)
        assert bar.bar_degree_dims[1] == 5

    def test_bar_deg1_dim_without_spin1(self):
        """Bar degree 1 dim = N_max - 1 (spins 2, ..., N_max)."""
        bar = celestial_bar_complex(5, Fraction(30), include_spin_1=False)
        assert bar.bar_degree_dims[1] == 4

    def test_bar_deg2_dim(self):
        """Bar degree 2 dim = C(num_gen, 2)."""
        bar = celestial_bar_complex(5, Fraction(30), include_spin_1=True)
        from math import comb
        assert bar.bar_degree_dims[2] == comb(5, 2)

    def test_bar_deg3_dim(self):
        """Bar degree 3 dim = C(num_gen, 3)."""
        bar = celestial_bar_complex(4, Fraction(30), include_spin_1=True)
        from math import comb
        assert bar.bar_degree_dims[3] == comb(4, 3)

    def test_bar_shadow_depth_class_M(self):
        """Shadow depth class = M for all N >= 2."""
        for N in [2, 3, 5, 10]:
            bar = celestial_bar_complex(N, Fraction(30))
            assert bar.shadow_depth_class == "M"


# ============================================================================
# Section 6: r-matrix and AP19 pole reduction
# ============================================================================

class TestRMatrix:
    """Verify celestial r-matrix (collision residue)."""

    def test_spin2_pole_orders(self):
        """Spin-2 r-matrix: poles at 3 and 1 (from OPE poles 4, 2, 1)."""
        poles = r_matrix_pole_orders_spin_s(2)
        assert poles == (3, 1)

    def test_spin3_pole_orders(self):
        """Spin-3 r-matrix: poles at 5, 3, 1."""
        poles = r_matrix_pole_orders_spin_s(3)
        assert poles == (5, 3, 1)

    def test_spin4_pole_orders(self):
        """Spin-4 r-matrix: poles at 7, 5, 3, 1."""
        poles = r_matrix_pole_orders_spin_s(4)
        assert poles == (7, 5, 3, 1)

    def test_spin1_pole_orders(self):
        """Spin-1 r-matrix: pole at 1 (from OPE pole 2)."""
        poles = r_matrix_pole_orders_spin_s(1)
        assert poles == (1,)

    def test_all_poles_odd(self):
        """All r-matrix poles are odd (bosonic algebra, d log extraction)."""
        for s in range(1, 10):
            poles = r_matrix_pole_orders_spin_s(s)
            assert all(p % 2 == 1 for p in poles), \
                f"Spin {s}: even pole found in {poles}"

    def test_leading_pole_is_2s_minus_1(self):
        """Leading r-matrix pole for spin s is 2s-1."""
        for s in range(1, 10):
            poles = r_matrix_pole_orders_spin_s(s)
            assert poles[0] == 2 * s - 1

    def test_r_matrix_leading_coeff_spin2(self):
        """Leading r-matrix coefficient at spin 2: c/2."""
        c = Fraction(26)
        r = celestial_r_matrix(5, c)
        assert r.leading_coefficients_by_spin[2] == Fraction(13)

    def test_r_matrix_leading_coeff_spin3(self):
        """Leading r-matrix coefficient at spin 3: c/3."""
        c = Fraction(30)
        r = celestial_r_matrix(5, c)
        assert r.leading_coefficients_by_spin[3] == Fraction(10)

    def test_r_matrix_satisfies_cybe(self):
        """r-matrix satisfies CYBE (from MC equation + Arnold relations)."""
        r = celestial_r_matrix(10, Fraction(30))
        assert r.satisfies_cybe is True

    def test_collinear_matching_spin2(self):
        """Bar propagator d log(z-w) matches celestial collinear for spin 2."""
        result = verify_celestial_collinear_matching(2, Fraction(26))
        assert result["pole_reduction_by_1"] is True
        assert result["coefficients_match"] is True
        assert result["all_r_poles_odd"] is True

    def test_collinear_matching_spin3(self):
        """Bar propagator d log(z-w) matches celestial collinear for spin 3."""
        result = verify_celestial_collinear_matching(3, Fraction(30))
        assert result["pole_reduction_by_1"] is True
        assert result["coefficients_match"] is True

    def test_collinear_matching_spin5(self):
        """Bar propagator d log(z-w) matches celestial collinear for spin 5."""
        result = verify_celestial_collinear_matching(5, Fraction(30))
        assert result["pole_reduction_by_1"] is True
        assert result["all_r_poles_odd"] is True

    def test_ap19_pole_order_reduction(self):
        """AP19: r-matrix pole = OPE pole - 1 at every spin."""
        for s in range(1, 8):
            ope_pole = 2 * s
            r_pole = r_matrix_pole_orders_spin_s(s)[0]
            assert r_pole == ope_pole - 1, \
                f"Spin {s}: r-matrix pole {r_pole} != OPE pole {ope_pole} - 1"


# ============================================================================
# Section 7: Shadow depth classification
# ============================================================================

class TestShadowDepth:
    """Verify shadow depth classification."""

    def test_heisenberg_class_g(self):
        """Spin-1 only (Heisenberg): class G."""
        assert shadow_depth_wn(1) == "G"

    def test_virasoro_class_m(self):
        """N=2 (Virasoro): class M."""
        assert shadow_depth_wn(2) == "M"

    def test_w3_class_m(self):
        """N=3 (W_3): class M."""
        assert shadow_depth_wn(3) == "M"

    def test_w_infinity_class_m(self):
        """w_{1+infty}: class M."""
        assert shadow_depth_w_infinity() == "M"

    def test_all_n_ge_2_class_m(self):
        """All W_N for N >= 2 are class M."""
        for N in range(2, 20):
            assert shadow_depth_wn(N) == "M"

    def test_verify_class_m(self):
        """Verification function returns correct data for N=3."""
        result = verify_shadow_depth_class_m(3)
        assert result["is_class_M"] is True
        assert result["infinite_tower"] is True
        assert result["contains_virasoro"] is True


# ============================================================================
# Section 8: Shadow projections (kappa, C, Q) on Virasoro channel
# ============================================================================

class TestShadowProjections:
    """Verify shadow kappa, cubic, quartic on the Virasoro channel."""

    def test_shadow_kappa_w5(self):
        """Shadow kappa for W_5: c * (H_5 - 1)."""
        c = Fraction(60)
        assert shadow_kappa(5, c) == Fraction(77)

    def test_shadow_kappa_virasoro_channel(self):
        """Virasoro channel of kappa: c/2."""
        assert shadow_kappa_virasoro_channel(Fraction(26)) == Fraction(13)

    def test_cubic_shadow_virasoro(self):
        """Cubic shadow S_3 = 2 for Virasoro (c-independent)."""
        assert shadow_cubic_virasoro(Fraction(1)) == Fraction(2)
        assert shadow_cubic_virasoro(Fraction(26)) == Fraction(2)
        assert shadow_cubic_virasoro(Fraction(100)) == Fraction(2)

    def test_quartic_contact_virasoro_c26(self):
        """Q^contact at c=26: 10/(26*152) = 10/3952 = 5/1976."""
        Q = shadow_quartic_contact_virasoro(Fraction(26))
        expected = Fraction(10) / (Fraction(26) * Fraction(152))
        assert Q == expected

    def test_quartic_contact_virasoro_c2(self):
        """Q^contact at c=2: 10/(2*32) = 10/64 = 5/32."""
        Q = shadow_quartic_contact_virasoro(Fraction(2))
        assert Q == Fraction(5, 32)

    def test_quartic_contact_singular_c0(self):
        """Q^contact singular at c=0."""
        with pytest.raises(ValueError):
            shadow_quartic_contact_virasoro(Fraction(0))

    def test_discriminant_virasoro_c26(self):
        """Delta = 40/(5*26+22) = 40/152 = 5/19."""
        delta = shadow_discriminant_virasoro(Fraction(26))
        assert delta == Fraction(5, 19)

    def test_discriminant_virasoro_c2(self):
        """Delta = 40/(10+22) = 40/32 = 5/4."""
        delta = shadow_discriminant_virasoro(Fraction(2))
        assert delta == Fraction(5, 4)

    def test_discriminant_nonzero_class_m(self):
        """Discriminant nonzero for generic c confirms class M."""
        for c_val in [Fraction(1), Fraction(10), Fraction(26), Fraction(100)]:
            delta = shadow_discriminant_virasoro(c_val)
            assert delta != 0, f"Discriminant zero at c = {c_val}"

    def test_shadow_tower_s2(self):
        """Shadow tower S_2 = kappa = c/2 on Virasoro channel."""
        c = Fraction(26)
        tower = shadow_tower_virasoro_channel(c)
        assert tower[2] == Fraction(13)

    def test_shadow_tower_s3(self):
        """Shadow tower S_3 = 2 on Virasoro channel (alpha/3 * r/r = 2)."""
        c = Fraction(26)
        tower = shadow_tower_virasoro_channel(c)
        assert tower[3] == Fraction(2)

    def test_shadow_tower_monotone_decrease_magnitude(self):
        """For large c (convergent tower), |S_r| should decrease."""
        c = Fraction(100)
        tower = shadow_tower_virasoro_channel(c, max_arity=8)
        # At c = 100, rho < 1, so tower should converge
        for r in range(3, 8):
            assert abs(tower[r]) <= abs(tower[r - 1]) + Fraction(1, 10), \
                f"|S_{r}| = {abs(tower[r])} unexpectedly large"


# ============================================================================
# Section 9: Soft graviton theorems from shadow projections
# ============================================================================

class TestSoftGravitonTheorems:
    """Verify soft theorem <-> shadow projection correspondence."""

    def test_soft_leading_order_0(self):
        """S^{(0)} from kappa (arity 2)."""
        soft = soft_theorem_from_shadow(0)
        assert soft.order == 0
        assert soft.shadow_arity == 2
        assert "kappa" in soft.shadow_name

    def test_soft_subleading_order_1(self):
        """S^{(1)} from cubic shadow (arity 3)."""
        soft = soft_theorem_from_shadow(1)
        assert soft.order == 1
        assert soft.shadow_arity == 3
        assert "cubic" in soft.shadow_name.lower() or "C" in soft.shadow_name

    def test_soft_subsubleading_order_2(self):
        """S^{(2)} from quartic shadow (arity 4)."""
        soft = soft_theorem_from_shadow(2)
        assert soft.order == 2
        assert soft.shadow_arity == 4
        assert "quartic" in soft.shadow_name.lower() or "Q" in soft.shadow_name

    def test_soft_arity_is_order_plus_2(self):
        """Shadow arity = soft order + 2."""
        for n in range(6):
            soft = soft_theorem_from_shadow(n)
            assert soft.shadow_arity == n + 2

    def test_soft_negative_order_raises(self):
        with pytest.raises(ValueError):
            soft_theorem_from_shadow(-1)

    def test_soft_kappa_leading_nonzero(self):
        """Leading soft theorem has nonzero kappa."""
        result = verify_soft_kappa_leading(5, Fraction(30))
        assert result["kappa_nonzero"] is True
        assert result["soft_order"] == 0

    def test_soft_cubic_subleading_nonzero(self):
        """Subleading soft theorem has nonzero cubic shadow."""
        result = verify_soft_cubic_subleading(Fraction(26))
        assert result["S3_nonzero"] is True

    def test_soft_quartic_subsubleading_nonzero(self):
        """Sub-subleading soft theorem has nonzero Q^contact."""
        result = verify_soft_quartic_subsubleading(Fraction(26))
        assert result["Q_contact_nonzero"] is True

    def test_soft_symmetry_bms(self):
        """S^{(0)} symmetry is BMS."""
        soft = soft_theorem_from_shadow(0)
        assert "BMS" in soft.symmetry

    def test_soft_symmetry_virasoro(self):
        """S^{(1)} symmetry is Virasoro/superrotation."""
        soft = soft_theorem_from_shadow(1)
        assert "Virasoro" in soft.symmetry or "superrotation" in soft.symmetry

    def test_soft_symmetry_w_infinity(self):
        """S^{(2)} symmetry is w_{1+inf}."""
        soft = soft_theorem_from_shadow(2)
        assert "w_{1+infinity}" in soft.symmetry or "w_" in soft.symmetry


# ============================================================================
# Section 10: Large-N scaling
# ============================================================================

class TestLargeNScaling:
    """Verify large-N scaling of shadow invariants."""

    def test_harmonic_divergence(self):
        """kappa/c = H_N - 1 diverges logarithmically.

        H_N - 1 ~ ln(N) + gamma - 1 where gamma ~ 0.577.
        So H_N - 1 ~ ln(N) - 0.423.
        The ratio (H_N - 1) / ln(N) approaches 1 from below.
        At N=10: ratio ~ 0.84.  At N=1000: ratio ~ 0.94.
        """
        import math
        for N in [10, 100, 1000]:
            h_tail = float(harmonic_number(N) - 1)
            ln_n = math.log(N)
            ratio = h_tail / ln_n
            # Ratio should be between 0.7 and 1.1 for N >= 10
            assert 0.7 < ratio < 1.1, \
                f"N={N}: ratio {ratio} not in expected range"
        # Also verify the ratio increases toward 1 as N grows
        ratios = []
        for N in [10, 100, 1000]:
            h_tail = float(harmonic_number(N) - 1)
            ratios.append(h_tail / math.log(N))
        assert ratios[1] > ratios[0], "Ratio should increase with N"
        assert ratios[2] > ratios[1], "Ratio should increase with N"

    def test_scaling_data_structure(self):
        """large_n_kappa_scaling returns correct structure."""
        data = large_n_kappa_scaling(Fraction(30), [5, 10, 20])
        assert len(data) == 3
        assert all("N" in d and "kappa" in d for d in data)

    def test_kappa_increases_with_N(self):
        """kappa(W_N) increases with N at fixed c."""
        c = Fraction(30)
        data = large_n_kappa_scaling(c, [3, 5, 10, 20, 50])
        kappas = [d["kappa"] for d in data]
        for i in range(1, len(kappas)):
            assert kappas[i] > kappas[i - 1]

    def test_channel_vector_completeness(self):
        """Channel vector has entries for all spins 2, ..., N."""
        c = Fraction(30)
        vec = large_n_channel_vector(10, c)
        assert set(vec.keys()) == set(range(2, 11))

    def test_channel_vector_sum_is_kappa(self):
        """Sum of channel vector = kappa(W_N)."""
        c = Fraction(30)
        for N in [3, 5, 10]:
            vec = large_n_channel_vector(N, c)
            assert sum(vec.values()) == kappa_wn(N, c)


# ============================================================================
# Section 11: Spin-1 sector = Kac-Moody
# ============================================================================

class TestSpin1Sector:
    """Verify spin-1 sector is Kac-Moody (class L)."""

    def test_km_depth_class_L(self):
        """Spin-1 sector (Kac-Moody) is class L, depth 3."""
        result = spin1_sector_is_kac_moody(8, Fraction(1))  # sl_3: dim=8
        assert result["depth_class"] == "L"
        assert result["shadow_depth"] == 3

    def test_km_kappa_at_level_0(self):
        """kappa(KM at k=0) = dim/2."""
        result = spin1_sector_is_kac_moody(3, Fraction(0))  # dim=3 (sl_2)
        assert result["kappa_at_level_0"] == Fraction(3, 2)

    def test_km_kappa_sl3_level_0(self):
        """kappa(V_0(sl_3)) = 8/2 = 4."""
        result = spin1_sector_is_kac_moody(8, Fraction(0))
        assert result["kappa_at_level_0"] == Fraction(4)


# ============================================================================
# Section 12: MHV amplitudes and collinear factorization
# ============================================================================

class TestMHVAmplitudes:
    """Verify MHV / Parke-Taylor structure."""

    def test_parke_taylor_4pt(self):
        """4-point MHV amplitude string."""
        pt = parke_taylor_mhv_n(4)
        assert "ij" in pt and "4" in pt

    def test_collinear_factorization_structure(self):
        """Collinear factorization of n-point MHV."""
        fact = mhv_collinear_factorization(5)
        assert "Split" in fact["collinear_limit"]
        assert fact["pole_order"] == "1"

    def test_collinear_from_bar(self):
        """Collinear splitting comes from bar differential."""
        fact = mhv_collinear_factorization(6)
        assert "bar" in fact["bar_differential_origin"].lower()


# ============================================================================
# Section 13: Gaberdiel-Gopakumar 't Hooft limit
# ============================================================================

class TestGaberdielGopakumar:
    """Verify Gaberdiel-Gopakumar duality scaling."""

    def test_gg_central_charge(self):
        """GG central charge matches wn_central_charge."""
        for N in [2, 3, 5]:
            k = Fraction(1)
            assert gaberdiel_gopakumar_central_charge(N, k) == wn_central_charge(N, k)

    def test_gg_kappa_equals_c_times_h_tail(self):
        """GG kappa = c * (H_N - 1)."""
        N, k = 4, Fraction(3)
        c = wn_central_charge(N, k)
        kap = gaberdiel_gopakumar_kappa(N, k)
        assert kap == c * (harmonic_number(N) - 1)

    def test_thooft_limit_structure(self):
        """'t Hooft limit returns correct structure."""
        data = thooft_limit_kappa_scaling(5, Fraction(5))
        assert "N" in data
        assert "thooft_coupling" in data
        assert "kappa" in data

    def test_thooft_coupling_correct(self):
        """lambda = N/(k+N)."""
        N, k = 5, Fraction(5)
        data = thooft_limit_kappa_scaling(N, k)
        expected_lam = Fraction(N) / (k + N)
        assert data["thooft_coupling"] == expected_lam


# ============================================================================
# Section 14: w_{1+infty} truncation
# ============================================================================

class TestWInfinityTruncation:
    """Verify truncated w_{1+infty} construction."""

    def test_spins_with_spin1(self):
        """With spin 1: generators at spins 1, 2, ..., N_max."""
        w = make_w_infinity_trunc(5, Fraction(30), include_spin_1=True)
        assert w.generator_spins == [1, 2, 3, 4, 5]
        assert w.num_generators == 5

    def test_spins_without_spin1(self):
        """Without spin 1: generators at spins 2, ..., N_max."""
        w = make_w_infinity_trunc(5, Fraction(30), include_spin_1=False)
        assert w.generator_spins == [2, 3, 4, 5]
        assert w.num_generators == 4

    def test_central_charge_stored(self):
        """Central charge is correctly stored."""
        w = make_w_infinity_trunc(10, Fraction(42))
        assert w.central_charge == Fraction(42)


# ============================================================================
# Section 15: Cross-consistency checks
# ============================================================================

class TestCrossConsistency:
    """Cross-check consistency between different computations."""

    def test_virasoro_channel_is_total_at_n2(self):
        """At N=2, the Virasoro channel IS the total kappa."""
        c = Fraction(30)
        assert shadow_kappa_virasoro_channel(c) == kappa_wn(2, c)

    def test_virasoro_channel_lt_total_at_n3(self):
        """At N >= 3, the Virasoro channel < total kappa."""
        c = Fraction(30)
        assert shadow_kappa_virasoro_channel(c) < kappa_wn(3, c)

    def test_r_matrix_matches_ope_self_coupling(self):
        """r-matrix leading coefficient = OPE self-coupling coefficient."""
        c = Fraction(30)
        r = celestial_r_matrix(5, c)
        for s in range(1, 6):
            ope_coeff = ope_self_coupling_coefficient(s, c)
            r_coeff = r.leading_coefficients_by_spin[s]
            assert ope_coeff == r_coeff, \
                f"Spin {s}: OPE coeff {ope_coeff} != r-matrix coeff {r_coeff}"

    def test_shadow_tower_s2_equals_kappa(self):
        """Shadow tower S_2 = kappa(Virasoro) = c/2."""
        c = Fraction(30)
        tower = shadow_tower_virasoro_channel(c)
        assert tower[2] == c / 2

    def test_shadow_s4_matches_quartic_contact(self):
        """Shadow tower S_4 matches Q^contact formula."""
        c = Fraction(26)
        tower = shadow_tower_virasoro_channel(c)
        q_contact = shadow_quartic_contact_virasoro(c)
        # S_4 from the tower should match the direct formula
        # S_4 = a_2 / 4 where a_2 = (q2 - a1^2) / (2*a0)
        # This is the same as Q^contact when properly normalized.
        # Let me check: kappa=13, alpha=2, S4 = Q^contact.
        # a0 = 2*13 = 26, a1 = 12*13*2/(2*26) = 312/52 = 6
        # q2 = 9*4 + 16*13*Q = 36 + 208*Q
        # a2 = (36 + 208*Q - 36)/(52) = 208*Q/52 = 4*Q
        # S_4 = a2/4 = Q
        assert tower[4] == q_contact

    def test_discriminant_from_kappa_and_s4(self):
        """Delta = 8 * kappa * S_4 cross-check."""
        c = Fraction(26)
        kap = c / 2
        s4 = shadow_quartic_contact_virasoro(c)
        delta_direct = shadow_discriminant_virasoro(c)
        delta_cross = 8 * kap * s4
        assert delta_direct == delta_cross


# ============================================================================
# Section 16: Full verification suite
# ============================================================================

class TestFullSuite:
    """Run the full verification suite."""

    def test_full_suite_runs(self):
        """Full suite completes without error."""
        results = run_full_celestial_shadow_verification(N_max=5, c=Fraction(30))
        assert isinstance(results, dict)
        assert len(results) > 0

    def test_full_suite_class_M(self):
        """Full suite confirms class M."""
        results = run_full_celestial_shadow_verification(N_max=5, c=Fraction(30))
        assert results["is_class_M"] is True

    def test_full_suite_cybe(self):
        """Full suite confirms CYBE."""
        results = run_full_celestial_shadow_verification(N_max=5, c=Fraction(30))
        assert results["r_matrix_cybe"] is True

    def test_full_suite_kappa_w2(self):
        """Full suite: kappa(W_2) = c/2."""
        results = run_full_celestial_shadow_verification(N_max=5, c=Fraction(30))
        assert results["kappa_W2_equals_c_over_2"] is True

    def test_full_suite_tt_vacuum(self):
        """Full suite: TT vacuum coefficient = c/2."""
        c = Fraction(30)
        results = run_full_celestial_shadow_verification(N_max=5, c=c)
        assert results["tt_vacuum_coeff"] == c / 2

    def test_full_suite_spin2_poles(self):
        """Full suite: spin-2 r-matrix poles are (3, 1)."""
        results = run_full_celestial_shadow_verification(N_max=5, c=Fraction(30))
        assert results["r_matrix_spin2_poles"] == (3, 1)
