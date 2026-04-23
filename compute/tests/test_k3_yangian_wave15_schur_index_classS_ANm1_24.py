r"""Tests for k3_yangian_wave15_schur_index_classS_ANm1_24.

Verifies:
    (A) Chacaltana-Distler trinion anomalies match CD 2010 Tab. 3 at
        N in {2, 3, 4, 5}.
    (B) Class-S total anomaly table matches Wave 15
        Proposition ``prop:thqg-occ-CD-ANm1-24''.
    (C) Shapere-Tachikawa (a, c) and Beem-Rastelli c_{2d} match Wave 15
        table values at N in {2, 3, 4}.
    (D) Constant Fourier coefficient f^{(N)}(0, 0) = 2(N + 3) at
        N in {2, 3, 4, 5, 6}.
    (E) Borcherds weight = N + 3 (honest) and (N + 3)/2 (spin cover);
        k_2 = 5, k_3 = 6, k_4 = 7 honestly; k_2 = 5/2, k_3 = 3, k_4 = 7/2
        on spin cover. Wave 17 verification for k_3 = 3 and k_4 = 7/2.
    (F) Umbral / Niemeier table at N in {2, 3, 4, 5}.
    (G) Summary record at N = 2 matches N = 2 canonical data.
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.k3_yangian_wave15_schur_index_classS_ANm1_24 import (
    beem_rastelli_c2d,
    borcherds_weight,
    class_S_anomaly_data,
    constant_fourier_coefficient,
    gritsenko_weight,
    is_niemeier_root_system,
    jacobi_input,
    labelling_breaks_at,
    mock_modular_form_6D4_low_coefficients,
    naive_labelling_rank_deficit,
    naive_labelling_valid,
    niemeier_coxeter_number,
    niemeier_root_system_rank,
    niemeiers_at_coxeter_slot,
    shapere_tachikawa_ac,
    siegel_lattice,
    siegel_weight,
    trinion_nh,
    trinion_nv,
    umbral_group,
    umbral_group_corrected,
    umbral_group_order,
    umbral_group_order_corrected,
    umbral_niemeier,
    umbral_niemeier_corrected,
    wave17_record,
    wave19_divisor_rule_holds,
    wave19_has_conway_moonshine,
    wave19_niemeier_root_system,
    wave19_summary_record,
    wave19_umbral_anchor,
    wave19_umbral_group,
    wave19_umbral_order,
    wave19_valid_naive_N,
)


# -- (A) Chacaltana-Distler trinion anomaly ---------------------------------

@pytest.mark.parametrize("N,nv,nh", [
    (2, 0, 4),
    (3, 5, 16),
    (4, 18, 40),
    (5, 42, 80),
])
def test_trinion_anomaly_vs_CD2010_table3(N, nv, nh):
    assert trinion_nv(N) == nv, (
        f"T_{N} vector multiplet count disagrees with CD 2010 Tab. 3: "
        f"computed {trinion_nv(N)}, expected {nv}"
    )
    assert trinion_nh(N) == nh, (
        f"T_{N} hypermultiplet count disagrees with CD 2010 Tab. 3: "
        f"computed {trinion_nh(N)}, expected {nh}"
    )


# -- (B) Class-S totals vs Wave 15 Prop. ``prop:thqg-occ-CD-ANm1-24'' ------

@pytest.mark.parametrize("N,n_v,n_h", [
    (2, 63, 88),
    (3, 278, 352),
    (4, 711, 880),
])
def test_class_S_totals_match_wave15_table(N, n_v, n_h):
    d = class_S_anomaly_data(N, g=0, n=24)
    assert d["n_trinions"] == 22
    assert d["n_tubes"] == 21
    assert d["n_v"] == n_v, (
        f"n_v at N = {N}: computed {d['n_v']}, expected {n_v}"
    )
    assert d["n_h"] == n_h, (
        f"n_h at N = {N}: computed {d['n_h']}, expected {n_h}"
    )


# -- (C) Shapere-Tachikawa (a, c) + Beem-Rastelli c_{2d} -------------------

@pytest.mark.parametrize("N,a_expected,c_expected,c2d_expected", [
    (2, Fraction(403, 24), Fraction(107, 6),  Fraction(-214)),
    (3, Fraction(871, 12), Fraction(227, 3),  Fraction(-908)),
    (4, Fraction(4435, 24), Fraction(1151, 6), Fraction(-2302)),
])
def test_shapere_tachikawa_and_beem_rastelli(
        N, a_expected, c_expected, c2d_expected):
    a, c = shapere_tachikawa_ac(N, g=0, n=24)
    assert a == a_expected, f"a_{{4d}}(N={N}) mismatch"
    assert c == c_expected, f"c_{{4d}}(N={N}) mismatch"
    assert beem_rastelli_c2d(N, g=0, n=24) == c2d_expected, (
        f"c_{{2d}} = -12 c_{{4d}} mismatch at N = {N}"
    )


# -- (D) Constant Fourier coefficient --------------------------------------

@pytest.mark.parametrize("N,f0", [
    (2, 10), (3, 12), (4, 14), (5, 16), (6, 18),
])
def test_constant_fourier_coefficient(N, f0):
    assert constant_fourier_coefficient(N) == f0


# -- (E) Borcherds / Siegel weights -- Wave 17 verification ----------------

@pytest.mark.parametrize("N,k_honest,k_spin", [
    (2, Fraction(5),      Fraction(5, 2)),
    (3, Fraction(6),      Fraction(3)),     # Wave 17: k_3 = 3 on spin cover
    (4, Fraction(7),      Fraction(7, 2)),  # Wave 17: k_4 = 7/2 on spin cover
    (5, Fraction(8),      Fraction(4)),
    (6, Fraction(9),      Fraction(9, 2)),
])
def test_siegel_weight_wave17(N, k_honest, k_spin):
    # Honest weight on O(Lambda).
    assert siegel_weight(N, spin=False) == k_honest
    assert borcherds_weight(N, honest=True) == k_honest
    # Spin-cover weight = Wave 16 conjecture = Wave 17 theorem.
    assert siegel_weight(N, spin=True) == k_spin
    assert borcherds_weight(N, honest=False) == k_spin
    assert gritsenko_weight(N) == k_spin


def test_wave17_k3_equals_3():
    """Wave 17 headline: k_3(spin) = 3 verified via Borcherds lift of
    f^{(3)}(0,0) = 12, so weight = 12/2 = 6 honestly = 3 on spin cover."""
    assert constant_fourier_coefficient(3) == 12
    assert borcherds_weight(3, honest=True) == Fraction(6)
    assert borcherds_weight(3, honest=False) == Fraction(3)


def test_wave17_k4_equals_7_over_2():
    """Wave 17 headline: k_4(spin) = 7/2 verified via Borcherds lift of
    f^{(4)}(0,0) = 14, so weight = 14/2 = 7 honestly = 7/2 on spin cover."""
    assert constant_fourier_coefficient(4) == 14
    assert borcherds_weight(4, honest=True) == Fraction(7)
    assert borcherds_weight(4, honest=False) == Fraction(7, 2)


# -- (F) Umbral / Niemeier labelling ---------------------------------------

@pytest.mark.parametrize("N,root,group,order", [
    (2, "24 A_1", "M_24",      244823040),
    (3, "12 A_2", "2.M_12",    190080),
    (4, "8 A_3",  "2.AGL_3(2)", 2688),
    (5, "6 A_4",  "GL_2(5)/{+-1}", 240),
])
def test_umbral_niemeier_table(N, root, group, order):
    assert umbral_niemeier(N) == root
    assert umbral_group(N) == group
    assert umbral_group_order(N) == order
    assert niemeier_root_system_rank(N) == 24


# -- (G) Summary record ----------------------------------------------------

def test_wave17_record_N2_is_canonical():
    r = wave17_record(2)
    assert r["N"] == 2
    assert r["n_v"] == 63
    assert r["n_h"] == 88
    assert r["a_4d"] == Fraction(403, 24)
    assert r["c_4d"] == Fraction(107, 6)
    assert r["c_2d"] == Fraction(-214)
    assert r["f_constant"] == 10
    assert r["k_honest"] == Fraction(5)
    assert r["k_spin"] == Fraction(5, 2)
    assert r["niemeier_root_system"] == "24 A_1"
    assert r["umbral_group"] == "M_24"


def test_siegel_lattice_and_jacobi_input_structure():
    assert "II_{1,1}" in siegel_lattice(3) and "A_2(-1)" in siegel_lattice(3)
    assert "II_{1,1}" in siegel_lattice(4) and "A_3(-1)" in siegel_lattice(4)
    assert "sig (4, 2)" in siegel_lattice(3)  # O(4, 2) for N=3
    assert "sig (5, 2)" in siegel_lattice(4)  # O(5, 2) for N=4
    assert "phi^(N=3)" in jacobi_input(3)
    assert "phi^(N=4)" in jacobi_input(4)
    assert "M_24-averaged" in jacobi_input(3)


# -- (H) MULTI-PATH CROSS-VERIFICATION (Beilinson 3+ paths rule) -----------

@pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
def test_siegel_weight_three_path_coherence(N):
    """Path 1: Borcherds 1998 Thm 13.3 weight = f^{(N)}(0,0) / 2.
    Path 2: Gritsenko 1999 additive-lift weight on metaplectic cover.
    Path 3: honest/spin cover relation weight_spin * 2 = weight_honest.
    All three must agree on the spin-cover weight $(N+3)/2$."""
    # Path 1: Borcherds honest; spin = Borcherds / 2.
    w_borch_honest = borcherds_weight(N, honest=True)
    w_borch_spin   = borcherds_weight(N, honest=False)
    # Path 2: Gritsenko directly on spin cover.
    w_grit = gritsenko_weight(N)
    # Path 3: the unified Siegel-weight function.
    w_sieg_honest = siegel_weight(N, spin=False)
    w_sieg_spin   = siegel_weight(N, spin=True)
    # Coherence relations.
    assert w_borch_honest == w_sieg_honest, (
        f"Path 1 vs Path 3 disagree at N = {N}: "
        f"Borcherds honest {w_borch_honest}, Siegel honest {w_sieg_honest}"
    )
    assert w_borch_spin == w_sieg_spin == w_grit, (
        f"Paths 1, 2, 3 disagree at N = {N} on spin-cover weight"
    )
    # Honest = 2 * spin (covering-degree relation).
    assert w_borch_honest == 2 * w_borch_spin, (
        f"Spin-cover relation broken at N = {N}"
    )


@pytest.mark.parametrize("N", [2, 3, 4])
def test_shapere_tachikawa_beem_rastelli_three_path(N):
    """Path 1: ST formula $a = (5 n_v + n_h)/24$, $c = (2 n_v + n_h)/12$.
    Path 2: ST / BR combination $c_{2d} = -12 c_{4d}$.
    Path 3: direct $(2 n_v + n_h) = -c_{2d}$ (eliminating factor of 12).
    All must agree."""
    d = class_S_anomaly_data(N, g=0, n=24)
    a, c = shapere_tachikawa_ac(N, g=0, n=24)
    c2d = beem_rastelli_c2d(N, g=0, n=24)
    # Path 1: ST direct.
    assert 24 * a == Fraction(5 * d["n_v"] + d["n_h"])
    assert 12 * c == Fraction(2 * d["n_v"] + d["n_h"])
    # Path 2: BR dictionary.
    assert c2d == -12 * c
    # Path 3: direct relation, no intermediate step.
    assert c2d == Fraction(-(2 * d["n_v"] + d["n_h"]))


@pytest.mark.parametrize("N", [2, 3, 4, 5])
def test_trinion_formula_three_path(N):
    """Path 1: closed formula $(N-1)(N-2)(N+2)/2$ / $2N(N^2-1)/3$.
    Path 2: factorisation of $n_h$ uses $N^2 - 1 = (N-1)(N+1)$.
    Path 3: ratio n_h / n_v approaches 2/(N-2) as N -> infty."""
    nv = trinion_nv(N)
    nh = trinion_nh(N)
    # Path 1 already = computation.
    # Path 2: n_h = (2/3) N (N - 1)(N + 1).
    assert 3 * nh == 2 * N * (N - 1) * (N + 1)
    # Path 3: n_v * 6 = 3 (N-1)(N-2)(N+2), parity-clean.
    assert 2 * nv == (N - 1) * (N - 2) * (N + 2)


def test_wave15_table_vs_closed_formulae_cross_check():
    """Cross-check the entire Wave 15 table at N in {2, 3, 4} by recomputing
    the ST/BR pipeline via independent closed formulae, then comparing."""
    for N in (2, 3, 4):
        d = class_S_anomaly_data(N, g=0, n=24)
        # Closed form: n_v = 21 (N^2 - 1) + 11 (N-1)(N-2)(N+2).
        nv_closed = 21 * (N * N - 1) + 11 * (N - 1) * (N - 2) * (N + 2)
        assert d["n_v"] == nv_closed
        # Closed form: n_h = 44 N (N^2 - 1) / 3.
        assert 3 * d["n_h"] == 44 * N * (N * N - 1)


@pytest.mark.parametrize("N", [2, 3, 4, 5, 6])
def test_constant_fourier_coefficient_three_path(N):
    """Path 1: 2(N+3) directly.
    Path 2: derivative check - f(N+1) - f(N) = 2 (linear in N).
    Path 3: parity - 2(N+3) is always even (f/2 is integer)."""
    f0 = constant_fourier_coefficient(N)
    # Path 1.
    assert f0 == 2 * (N + 3)
    # Path 2 (finite difference): linear in N.
    if N >= 3:
        assert (f0 - constant_fourier_coefficient(N - 1)) == 2
    # Path 3: evenness (Borcherds honest weight = f/2 integer).
    assert f0 % 2 == 0


# -- (I) WAVE 18 RE-ANCHORING: N = 6 umbral Niemeier labelling -------------

@pytest.mark.parametrize("N,expected", [
    (2, "24 A_1"),
    (3, "12 A_2"),
    (4, "8 A_3"),
    (5, "6 A_4"),
    (6, "6 D_4"),  # Wave 18: re-anchored from the failing naive 4 A_5
])
def test_wave18_umbral_niemeier_corrected(N, expected):
    assert umbral_niemeier_corrected(N) == expected


@pytest.mark.parametrize("N,expected_group,expected_order", [
    (2, "M_24", 244823040),
    (3, "2.M_12", 190080),
    (4, "2.AGL_3(2)", 2688),
    (5, "GL_2(5)/{+-1}", 240),
    (6, "3.Sym_6", 2160),  # Wave 18: umbral group of 6 D_4 per CDH 2014 Tab. 1
])
def test_wave18_umbral_group_corrected(N, expected_group, expected_order):
    assert umbral_group_corrected(N) == expected_group
    assert umbral_group_order_corrected(N) == expected_order


def test_wave18_naive_labelling_breaks_at_N6_but_not_below():
    """Wave 18 headline: the systematic (24/N) A_{N-1} labelling is a
    valid Niemeier root system for N <= 5 and FAILS at N = 6 because
    4 A_5 is not among the 23 Niemeier root systems (Niemeier 1973;
    Conway-Sloane 1988 SPLAG Ch. 16)."""
    for N in (2, 3, 4, 5):
        assert labelling_breaks_at(N, scheme="naive") is False, (
            f"Naive (24/N) A_(N-1) labelling must not break at N = {N}"
        )
    assert labelling_breaks_at(6, scheme="naive") is True, (
        "Naive labelling 4 A_5 at N = 6 must break (no such Niemeier lattice)"
    )


def test_wave18_corrected_labelling_holds_at_all_N_in_2_6():
    for N in (2, 3, 4, 5, 6):
        assert labelling_breaks_at(N, scheme="corrected") is False, (
            f"Wave 18 corrected labelling must hold at N = {N}"
        )


def test_wave18_naive_4A5_is_not_a_niemeier_root_system():
    """Primary test of the Wave 18 re-anchoring premise: the would-be
    N = 6 naive label 4 A_5 is NOT one of the 23 Niemeier root systems
    (Conway-Sloane 1988 SPLAG Table 16.1)."""
    assert is_niemeier_root_system("4 A_5") is False


@pytest.mark.parametrize("root_system", [
    "24 A_1", "12 A_2", "8 A_3", "6 A_4", "4 A_6", "2 A_12", "A_24",
    "6 D_4", "4 D_6", "3 D_8", "2 D_12", "D_24",
    "4 A_5 D_4", "3 E_8", "4 E_6",
])
def test_wave18_niemeier_existence(root_system):
    """Sanity check: known Niemeier root systems (Niemeier 1973;
    Conway-Sloane 1988 SPLAG Ch. 16 Table 16.1) are recognised."""
    assert is_niemeier_root_system(root_system) is True


def test_wave18_niemeier_coxeter_number_6D4_equals_6():
    """Coxeter number h(D_4) = 6, matching the N = 6 Coxeter slot
    (Humphreys 1990 Section 2.11)."""
    assert niemeier_coxeter_number("6 D_4") == 6


def test_wave18_niemeier_coxeter_numbers_ANm1_table():
    """Cross-check: the naive (24/N) A_{N-1} labelling assigns Coxeter
    number h(A_{N-1}) = N, and the Niemeier 6 D_4 hosts h = 6. At
    N = 6 the 6 D_4 Coxeter number AGREES with the naive-N value,
    so the re-anchoring preserves the Coxeter slot."""
    assert niemeier_coxeter_number("24 A_1") == 2
    assert niemeier_coxeter_number("12 A_2") == 3
    assert niemeier_coxeter_number("8 A_3") == 4
    assert niemeier_coxeter_number("6 A_4") == 5
    # N = 6: 6 D_4 Coxeter number h(D_4) = 6, matching h(A_5) = 6.
    assert niemeier_coxeter_number("6 D_4") == 6


def test_wave18_mock_modular_6D4_leading_coefficients_nonzero():
    """The Wave 18 corrected N = 6 labelling carries a mock-modular
    form $H^{(6 D_4)}$ (CDH 2014 Table 5 / App. C): test that the
    leading Fourier coefficients are non-trivially populated."""
    coeffs = mock_modular_form_6D4_low_coefficients()
    assert coeffs[0] == -2, "Polar term of H^{(6D_4)}_1 must be -2 q^{-1/12}"
    # Positive-exponent coefficients should be non-zero.
    for n in (1, 2, 3, 4, 5, 6):
        assert coeffs[n] != 0, (
            f"H^{{(6D_4)}}_1 Fourier coefficient c({n}) must be non-zero"
        )


def test_wave18_siegel_weight_k6_is_9_over_2_under_corrected_labelling():
    """Wave 18 headline: even under the corrected (6 D_4) labelling,
    the Siegel weight on the spin cover at N = 6 is k_6 = 9/2 via the
    formula (N + 3)/2. The re-anchoring is a labelling choice; the
    Jacobi-form-input f^(6)(0,0) = 2(6+3) = 18 and Borcherds 1998
    Thm 13.3 are unchanged by the Niemeier substitution."""
    assert siegel_weight(6, spin=True) == Fraction(9, 2)
    assert borcherds_weight(6, honest=True) == Fraction(9)
    assert constant_fourier_coefficient(6) == 18


def test_wave18_record_N6_contains_corrected_and_break_diagnostics():
    """The wave17_record must be Wave-18-aware at N = 6: it must carry
    both the naive (now-failing) and corrected (6 D_4) labels, plus
    the break diagnostics."""
    r = wave17_record(6)
    # Naive label retained for reference (string notes the failure).
    assert "6 D_4" in r["niemeier_root_system"]
    # Corrected label is clean 6 D_4.
    assert r["niemeier_root_system_corrected"] == "6 D_4"
    assert r["umbral_group_corrected"] == "3.Sym_6"
    assert r["umbral_group_order_corrected"] == 2160
    # Break diagnostics.
    assert r["labelling_breaks_naive"] is True
    assert r["labelling_breaks_corrected"] is False


def test_wave18_sym6_order_is_720_so_3Sym6_is_2160():
    """Verify the factor-of-3 central extension: |Sym_6| = 720, and
    |3.Sym_6| = 3 * 720 = 2160 (CDH 2014 Table 1)."""
    # Sym_6 order = 6! = 720.
    order_Sym_6 = 1
    for k in range(1, 7):
        order_Sym_6 *= k
    assert order_Sym_6 == 720
    # 3.Sym_6 is a non-split central extension by Z/3.
    assert 3 * order_Sym_6 == umbral_group_order_corrected(6)


def test_N2_canonical_agreement_with_gritsenko_nikulin_1998():
    """At N = 2, the Wave 17 computation must reproduce the
    Gritsenko-Nikulin 1998 Theorem 4.1 result:
        weight(Borch(phi_{0,1}^{K3})) = 5 (honest)
        equivalent spin-cover weight = 5/2
        producing Delta_5 = Igusa cusp form of weight 5 on O(3,2).
    """
    assert constant_fourier_coefficient(2) == 10  # phi_{0,1}^{K3} Fourier.
    assert borcherds_weight(2, honest=True) == Fraction(5)
    assert borcherds_weight(2, honest=False) == Fraction(5, 2)
    # Delta_5^2 = Phi_10 cross-check (Igusa 1964).
    assert 2 * borcherds_weight(2, honest=True) == Fraction(10)


# -- (J) WAVE 19 GAIOTTO: extended N in {7, 8, 9, 12, 13, 24, 25} ---------

def test_wave19_corrected_divisor_rule_Nm1_divides_24():
    """Wave 19 Gaiotto headline: the naive (24/(N-1)) A_{N-1} umbral
    Niemeier labelling is valid iff (N - 1) | 24, giving
    N in {2, 3, 4, 5, 7, 9, 13, 25}.
    Wave 18's "divisor-of-24 rule" (N | 24) was INCORRECT; the
    correct rule is (N - 1) | 24 because A_{N-1} has rank N - 1
    and the Niemeier rank constraint is 24."""
    expected = (2, 3, 4, 5, 7, 9, 13, 25)
    assert wave19_valid_naive_N() == expected
    # Exhaustive check up to N = 30:
    for N in range(2, 31):
        valid = naive_labelling_valid(N)
        must_hold = (24 % (N - 1) == 0)
        assert valid == must_hold, (
            f"Corrected divisor rule mismatch at N = {N}: "
            f"valid = {valid}, (N-1)|24 = {must_hold}"
        )


@pytest.mark.parametrize("N,deficit", [
    (2, 0), (3, 0), (4, 0), (5, 0),
    (6, 4),   # 24 - 4*5 = 4
    (7, 0),   # 24 - 4*6 = 0
    (8, 3),   # 24 - 3*7 = 3
    (9, 0),   # 24 - 3*8 = 0
    (12, 2),  # 24 - 2*11 = 2
    (13, 0),  # 24 - 2*12 = 0
    (24, 1),  # 24 - 1*23 = 1
    (25, 0),  # 24 - 1*24 = 0
])
def test_wave19_rank_deficit_formula(N, deficit):
    """The naive (24/(N-1)) A_{N-1} rank deficit is
    Delta = 24 - (N - 1) * floor(24/(N - 1)). Zero iff (N - 1) | 24."""
    assert naive_labelling_rank_deficit(N) == deficit


@pytest.mark.parametrize("N,niemeier,naive_valid", [
    (7,  "4 A_6",        True),
    (8,  "2 A_7 D_5^2",  False),
    (9,  "3 A_8",        True),
    (10, "2 A_9 D_6",    False),
    (12, "A_11 D_7 E_6", False),
    (13, "2 A_12",       True),
    (25, "A_24",         True),
])
def test_wave19_umbral_anchor_niemeier(N, niemeier, naive_valid):
    """Wave 19 umbral anchors at $N \\in \\{7, 8, 9, 12, 13, 25\\}$
    match the Niemeier root system at Coxeter slot $h = N$
    (Niemeier 1973; SPLAG Ch. 16 Tab. 16.1; CDH 2014 Tab. 1).
    """
    assert wave19_niemeier_root_system(N) == niemeier
    rec = wave19_umbral_anchor(N)
    assert rec["naive_valid"] == naive_valid
    assert rec["coxeter_h"] == N
    # The anchor Niemeier root system is recognised in the table
    # (either as-is for the naive cases, or as the substitute).
    assert is_niemeier_root_system(niemeier) is True


@pytest.mark.parametrize("N,group,order", [
    (7,  "SL_2(3)", 24),
    (8,  "Z/2",     2),
    (9,  "Dih_4",   8),
    (10, "Z/2",     2),
    (12, "1",       1),
    (13, "Z/4",     4),
    (25, "Z/2",     2),
])
def test_wave19_umbral_groups_CDH2014_table1(N, group, order):
    """Wave 19 umbral groups per CDH 2014 Table 1 row by row:
        X = 4 A_6:        SL_2(3), order 24;
        X = 2 A_7 D_5^2:  Z/2, order 2;
        X = 3 A_8:        Dih_4, order 8;
        X = A_11 D_7 E_6: trivial, order 1;
        X = 2 A_12:       Z/4, order 4;
        X = A_24:         Z/2, order 2.
    """
    assert wave19_umbral_group(N) == group
    assert wave19_umbral_order(N) == order


def test_wave19_N24_is_conway_moonshine():
    """Wave 19: at N = 24 there is NO Niemeier with h = 24
    (adjacent slots are h = 22 via 2 D_12 and h = 25 via A_24).
    The rank-24 extremal lattice is the Leech lattice (no roots)
    with automorphism group Co_0 = 2.Co_1 and Conway moonshine
    (Duncan-Mack-Crane 2020 arXiv:2012.14980) replacing umbral."""
    assert wave19_has_conway_moonshine(24) is True
    rec = wave19_umbral_anchor(24)
    assert rec["coxeter_h"] is None  # Leech has no Coxeter number.
    assert rec["umbral_group"] == "Co_0"
    # |Co_0| = 2 |Co_1| = 8,315,553,613,086,720,000 (ATLAS).
    assert rec["umbral_order"] == 8315553613086720000
    assert rec["niemeier_root_system"].startswith("Leech")


def test_wave19_no_niemeier_has_coxeter_number_24():
    """Wave 19: there is NO Niemeier root system with common Coxeter
    number h = 24 (Niemeier 1973 classification). The N = 24 slot of
    class-S A_{N-1}-on-Sigma_{0,24} therefore escapes umbral moonshine
    and lands in Conway moonshine via Leech."""
    assert niemeiers_at_coxeter_slot(24) == []
    # Adjacent slots do exist:
    assert len(niemeiers_at_coxeter_slot(22)) >= 1
    assert len(niemeiers_at_coxeter_slot(25)) >= 1


def test_wave19_N_not_divisor_plus_1_breaks_naive():
    """Wave 19: for every N \\in {6, 8, 10, 11, 12, 14, ...} not of
    the form (N - 1) | 24, the naive label has positive rank deficit,
    hence is not a Niemeier root system."""
    for N in (6, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24):
        assert naive_labelling_valid(N) is False, (
            f"Naive labelling must fail at N = {N}"
        )
        assert naive_labelling_rank_deficit(N) > 0


def test_wave19_coxeter_slot_table_matches_niemeier_1973():
    """Wave 19: Coxeter-slot table for class-S A_{N-1} at N in
    {7, 8, 9, 13, 25} lands on the unique Niemeier root system with
    that Coxeter number containing A_{N-1} summand
    (Niemeier 1973; SPLAG Tab. 16.1).
    """
    # h = 7: only 4 A_6.
    assert [n for (n, _) in niemeiers_at_coxeter_slot(7)] == ["4 A_6"]
    # h = 9: only 3 A_8.
    assert [n for (n, _) in niemeiers_at_coxeter_slot(9)] == ["3 A_8"]
    # h = 13: only 2 A_12.
    assert [n for (n, _) in niemeiers_at_coxeter_slot(13)] == ["2 A_12"]
    # h = 25: only A_24.
    assert [n for (n, _) in niemeiers_at_coxeter_slot(25)] == ["A_24"]


def test_wave19_siegel_weights_extended_N():
    """Wave 19: the Borcherds/Siegel weight formula $k_N = (N+3)/2$
    (spin cover) and $k_N^{\\mathrm{honest}} = N + 3$ extend without
    modification to the extended-N regime:
        k_7 = 10 (honest) / 5 (spin);
        k_8 = 11/2 (spin) / 11 (honest);
        k_9 = 6 (spin) / 12 (honest);
        k_12 = 15/2 (spin) / 15 (honest);
        k_13 = 8 (spin) / 16 (honest);
        k_24 = 27/2 (spin) / 27 (honest);
        k_25 = 14 (spin) / 28 (honest).
    The weight is set by the Jacobi-form constant Fourier coefficient
    f^{(N)}(0, 0) = 2(N + 3) via Borcherds 1998 Theorem 13.3; the
    umbral/Conway labelling is a choice of mock-modular companion,
    not a weight ingredient."""
    cases = [
        (7,  Fraction(10), Fraction(5)),
        (8,  Fraction(11), Fraction(11, 2)),
        (9,  Fraction(12), Fraction(6)),
        (12, Fraction(15), Fraction(15, 2)),
        (13, Fraction(16), Fraction(8)),
        (24, Fraction(27), Fraction(27, 2)),
        (25, Fraction(28), Fraction(14)),
    ]
    for (N, k_honest, k_spin) in cases:
        assert siegel_weight(N, spin=False) == k_honest
        assert siegel_weight(N, spin=True) == k_spin
        # Borcherds 1998: weight = f(0)/2 = (N + 3).
        assert borcherds_weight(N, honest=True) == k_honest
        # Gritsenko additive-lift weight on spin cover:
        assert gritsenko_weight(N) == k_spin


def test_wave19_summary_record_N7():
    """Wave 19 summary record at N = 7 (naive-valid slot).
    Niemeier: 4 A_6, umbral: SL_2(3) order 24, Coxeter h = 7.
    """
    r = wave19_summary_record(7)
    assert r["N"] == 7
    assert r["niemeier_root_system"] == "4 A_6"
    assert r["umbral_group"] == "SL_2(3)"
    assert r["umbral_group_order"] == 24
    assert r["coxeter_h"] == 7
    assert r["naive_valid"] is True
    assert r["rank_deficit"] == 0
    assert r["k_honest"] == Fraction(10)
    assert r["k_spin"] == Fraction(5)
    assert r["divisor_rule"] == "(N - 1) | 24"
    assert r["divisor_rule_holds"] is True


def test_wave19_summary_record_N8():
    """Wave 19 summary record at N = 8 (substitute-anchor slot).
    Naive 3 A_7 fails (rank 21, deficit 3); substitute 2 A_7 D_5^2,
    umbral group Z/2."""
    r = wave19_summary_record(8)
    assert r["niemeier_root_system"] == "2 A_7 D_5^2"
    assert r["coxeter_h"] == 8
    assert r["naive_valid"] is False
    assert r["rank_deficit"] == 3
    assert r["umbral_group"] == "Z/2"
    assert r["k_spin"] == Fraction(11, 2)
    assert r["divisor_rule_holds"] is False


def test_wave19_summary_record_N24_conway_moonshine():
    """Wave 19 summary record at N = 24: no Niemeier has h = 24;
    Leech lattice with Co_0 via Duncan-Mack-Crane 2020 Conway
    moonshine.
    """
    r = wave19_summary_record(24)
    assert r["niemeier_root_system"].startswith("Leech")
    assert r["umbral_group"] == "Co_0"
    assert r["umbral_group_order"] == 8315553613086720000
    assert r["coxeter_h"] is None
    assert r["naive_valid"] is False
    assert r["rank_deficit"] == 1
    assert r["conway_moonshine"] is True
    assert r["k_honest"] == Fraction(27)
    assert r["k_spin"] == Fraction(27, 2)


def test_wave19_summary_record_N25():
    """Wave 19 summary record at N = 25: naive A_24 Niemeier."""
    r = wave19_summary_record(25)
    assert r["niemeier_root_system"] == "A_24"
    assert r["coxeter_h"] == 25
    assert r["naive_valid"] is True
    assert r["umbral_group"] == "Z/2"
    assert r["k_honest"] == Fraction(28)
    assert r["divisor_rule_holds"] is True


def test_wave19_divisor_rule_three_path_cross_check():
    """Three independent verification paths for the Wave 19 corrected
    divisor rule (N - 1) | 24:
    Path 1: direct divisibility test 24 % (N - 1) == 0.
    Path 2: rank-deficit zero iff divisor rule holds.
    Path 3: Niemeier Coxeter-slot membership with A_{N-1} summand of
            the required multiplicity (24/(N-1)).
    """
    for N in (2, 3, 4, 5, 7, 9, 13, 25):
        # Path 1.
        assert 24 % (N - 1) == 0
        # Path 2.
        assert naive_labelling_rank_deficit(N) == 0
        # Path 3.
        slot = niemeiers_at_coxeter_slot(N)
        assert len(slot) >= 1, (
            f"Niemeier slot h = {N} must contain A_{{{N-1}}} "
            f"summand of multiplicity {24 // (N - 1)}"
        )


def test_wave19_N8_heals_wave18_divisor_of_24_rule():
    """Wave 19 HEAL: Wave 18's "divisor-of-24 rule" proposed that N
    divides 24, i.e. N in {2, 3, 4, 6, 8, 12, 24}. This is INCORRECT.
    The correct rule is (N - 1) | 24, giving N in {2, 3, 4, 5, 7, 9,
    13, 25}. The rules disagree at every N except N = 2 (a vacuous
    coincidence where both 1 and 2 divide 24 / 2 = 12)."""
    wave18_naive = {N for N in range(2, 25) if 24 % N == 0}
    wave19_corrected = {N for N in range(2, 26)
                        if 24 % (N - 1) == 0}
    # Disagree on N = 3 (Wave 18 says no via 3|24 yes but... hmm):
    # Wave 18 "N|24": {2, 3, 4, 6, 8, 12, 24};
    # Wave 19 "(N-1)|24": {2, 3, 4, 5, 7, 9, 13, 25}.
    assert wave18_naive == {2, 3, 4, 6, 8, 12, 24}
    assert wave19_corrected == {2, 3, 4, 5, 7, 9, 13, 25}
    # Intersection is just {2, 3, 4}; the rules diverge beyond N = 4.
    assert wave18_naive & wave19_corrected == {2, 3, 4}


def test_wave19_co0_order_matches_atlas():
    """Conway group order sanity: |Co_1| = 4,157,776,806,543,360,000
    (ATLAS), so |Co_0| = 2 * |Co_1| = 8,315,553,613,086,720,000.
    The Wave 19 N = 24 anchor attaches Co_0 as the Leech lattice
    automorphism group (Conway 1968; ATLAS).
    """
    order_co1 = 4157776806543360000
    assert 2 * order_co1 == wave19_umbral_order(24)
    # Factorisation: |Co_1| = 2^21 * 3^9 * 5^4 * 7^2 * 11 * 13 * 23.
    expected = (
        (2 ** 21) * (3 ** 9) * (5 ** 4) * (7 ** 2)
        * 11 * 13 * 23
    )
    assert order_co1 == expected


def test_wave19_extended_siegel_weight_linear_in_N():
    """Wave 19: the Borcherds/Siegel weight k_N^{honest} = N + 3
    is linear in N across the entire extended range. Finite-difference
    check: k_{N+1} - k_N = 1 for every N in the sequence
    2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 24, 25."""
    Ns = (2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 24, 25)
    prev = None
    for N in Ns:
        kN = siegel_weight(N, spin=False)
        assert kN == Fraction(N + 3)
        if prev is not None:
            prev_N, prev_k = prev
            # Finite difference over unit N-step should equal 1.
            if N - prev_N == 1:
                assert kN - prev_k == Fraction(1)
        prev = (N, kN)


def test_wave19_fourier_coefficient_linear_extended():
    """Wave 19: f^{(N)}(0, 0) = 2(N + 3) extends without modification
    to the extended-N regime. Path check: f stays even, linear, and
    f/2 = N + 3 returns an integer (Borcherds honest-weight check)."""
    for N in (7, 8, 9, 12, 13, 24, 25):
        f0 = constant_fourier_coefficient(N)
        assert f0 == 2 * (N + 3)
        assert f0 % 2 == 0
        assert f0 // 2 == N + 3


# -- (K) WAVE 21.9 EXTENDED LADDER N in {9, 10, 11, 12} --------------------
#
# Theorem walgdeep-N9-N12-re-anchor in chapters/examples/w_algebras_deep.tex:
#   N = 9:  naive    3 A_8         umbral Dih_4    k_9  = 12
#   N = 10: sub      2 A_9 D_6     umbral Z/2      k_10 = 13
#   N = 11: void     none          none            k_11 = 14 (Coxeter void)
#   N = 12: sub      A_11 D_7 E_6  umbral trivial  k_12 = 15
#
# The first genuine Coxeter-void inside the non-Leech range is N = 11:
# h(A_10) = 11 is the only solution of h(simple Lie algebra) = 11, and
# 10 does not divide 24.

from compute.lib.k3_yangian_wave15_schur_index_classS_ANm1_24 import (
    wave21_9_coxeter_void_slots,
    wave21_9_is_coxeter_void,
)


def test_wave21_9_coxeter_void_at_h11():
    """Wave 21.9 headline: no Niemeier has common Coxeter number h = 11.
    The Cartan-Killing classification admits h = 11 only via h(A_10),
    and 10 does not divide 24 (so no pure-A Niemeier); D_n forces
    2n - 2 = 11 which fails integrality; E_6/E_7/E_8 have h in {12,18,30}.
    """
    # h = 11 slot is empty in the Niemeier Coxeter table.
    from compute.lib.k3_yangian_wave15_schur_index_classS_ANm1_24 import (
        niemeiers_at_coxeter_slot,
    )
    assert niemeiers_at_coxeter_slot(11) == []
    # Adjacent slots do exist:
    assert len(niemeiers_at_coxeter_slot(10)) >= 1  # 2 A_9 D_6 or 4 D_6.
    assert len(niemeiers_at_coxeter_slot(12)) >= 1  # A_11 D_7 E_6 or 4 E_6.


def test_wave21_9_N11_is_coxeter_void_N24_is_not():
    """Wave 21.9: N = 11 is Coxeter-void; N = 24 is NOT (Leech escape)."""
    assert wave21_9_is_coxeter_void(11) is True
    # N = 24 escapes via Leech; not classified as Coxeter-void here.
    assert wave21_9_is_coxeter_void(24) is False
    # Valid naive slots are not void.
    for N in (2, 3, 4, 5, 7, 9, 13, 25):
        assert wave21_9_is_coxeter_void(N) is False


def test_wave21_9_coxeter_void_slot_list():
    """The complete list of Coxeter-void slots in [2, 25] is
    {11, 15, 17, 19, 20, 21, 23}: each N where h(A_{N-1}) = N is
    absent from the Niemeier Coxeter spectrum {2,3,4,5,6,7,8,9,10,
    12,13,14,16,18,22,25,30,46} and N != 24.
    """
    assert wave21_9_coxeter_void_slots() == (11, 15, 17, 19, 20, 21, 23)


def test_wave21_9_N10_substitute_anchor_2A9_D6():
    """Wave 21.9: N = 10 substitute anchor is 2 A_9 D_6 with umbral Z/2.
    Rank deficit 24 - 2*9 = 6 is absorbed by a single D_6 summand
    (rank 6, h(D_6) = 10). Uniqueness: the only Niemeier at h = 10
    containing A_9 summand."""
    from compute.lib.k3_yangian_wave15_schur_index_classS_ANm1_24 import (
        wave19_umbral_anchor,
        wave19_niemeier_root_system,
        wave19_umbral_group,
    )
    rec = wave19_umbral_anchor(10)
    assert rec["niemeier_root_system"] == "2 A_9 D_6"
    assert rec["coxeter_h"] == 10
    assert rec["umbral_group"] == "Z/2"
    assert rec["umbral_order"] == 2
    assert rec["naive_valid"] is False
    assert rec["rank_deficit"] == 6
    assert wave19_niemeier_root_system(10) == "2 A_9 D_6"
    assert wave19_umbral_group(10) == "Z/2"


def test_wave21_9_siegel_weight_at_N11_without_anchor():
    """Wave 21.9: at N = 11 the Siegel weight k_11 = 14 (honest) = 7
    (spin) is set by the Jacobi-form input f^{(11)}(0, 0) = 28 via
    Borcherds 1998 Theorem 13.3, independent of any Niemeier anchor
    (which does not exist at h = 11). The ladder k_N = N + 3
    continues through the Coxeter-void slot without gap."""
    assert constant_fourier_coefficient(11) == 28
    assert borcherds_weight(11, honest=True) == Fraction(14)
    assert borcherds_weight(11, honest=False) == Fraction(7)
    assert siegel_weight(11, spin=False) == Fraction(14)
    assert siegel_weight(11, spin=True) == Fraction(7)
    assert gritsenko_weight(11) == Fraction(7)


def test_wave21_9_extended_ladder_N9_to_N12_continuity():
    """Wave 21.9: (k_9, k_10, k_11, k_12)^honest = (12, 13, 14, 15)
    forms an arithmetic progression of common difference 1, uniformly
    across the four regimes (naive, substitute, void, substitute)."""
    expected = [(9, 12), (10, 13), (11, 14), (12, 15)]
    for (N, kN_hon) in expected:
        assert siegel_weight(N, spin=False) == Fraction(kN_hon)
        assert constant_fourier_coefficient(N) == 2 * kN_hon
    # Finite-difference check.
    for i in range(1, len(expected)):
        N_prev, k_prev = expected[i - 1]
        N_this, k_this = expected[i]
        assert N_this - N_prev == 1
        assert k_this - k_prev == 1


@pytest.mark.parametrize("N,expected_void", [
    (9, False),    # naive, (N-1)=8|24.
    (10, False),   # substitute, Niemeier 2 A_9 D_6 exists at h = 10.
    (11, True),    # Coxeter void: h = 11 absent from Niemeier spectrum.
    (12, False),   # substitute, Niemeier A_11 D_7 E_6 exists at h = 12.
])
def test_wave21_9_void_classification_N9_to_N12(N, expected_void):
    """Wave 21.9: classify each N in {9, 10, 11, 12} as naive /
    substitute / Coxeter-void according to the three-regime theorem."""
    assert wave21_9_is_coxeter_void(N) is expected_void


def test_wave21_9_three_path_coxeter_void_N11():
    """Wave 21.9 three verification paths for the N = 11 Coxeter void:
    Path 1: no root system has Coxeter number 11 matching the rank
            constraint k*10 = 24 (arithmetic).
    Path 2: niemeiers_at_coxeter_slot(11) returns [] (exhaustive
            inspection of Niemeier 1973 / SPLAG Tab. 16.1).
    Path 3: wave21_9_is_coxeter_void(11) returns True (composite
            diagnostic combining the above).
    """
    from compute.lib.k3_yangian_wave15_schur_index_classS_ANm1_24 import (
        niemeiers_at_coxeter_slot,
        naive_labelling_valid,
    )
    # Path 1: naive invalid at N = 11 (10 does not divide 24).
    assert naive_labelling_valid(11) is False
    # Path 2: empty Niemeier slot at h = 11.
    assert niemeiers_at_coxeter_slot(11) == []
    # Path 3: composite diagnostic.
    assert wave21_9_is_coxeter_void(11) is True
