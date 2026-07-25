"""Exact W3 checks and reconstruction-boundary guards."""

from dataclasses import FrozenInstanceError
from pathlib import Path

import pytest
import sympy as sp

from compute.lib.theorem_w3_bouwknegt_schoutens_engine import (
    lambda_zero_witness as bs_lambda_zero_witness,
    w3_level_one_null_curve as bs_level_one_null_curve,
    w3_ww_ope_modes as bs_ww_ope_modes,
)
from compute.lib.theorem_w3_holographic_datum_engine import (
    ClaimPacket,
    collision_kernel_packet,
    derived_center_packet,
    exact_local_packet,
    genus_graph_packet,
    hamiltonian_packet,
    holographic_datum,
    holographic_lift_packet,
    lambda_mode_commutator_coefficient,
    lambda_norm,
    lambda_virasoro_witness,
    lambda_zero,
    lambda_zero_packet,
    leading_ope_norms,
    level_one_gram_matrix,
    level_one_null_polynomial,
    level_one_packet,
    modular_kappa_packet,
    modular_rho_packet,
    presentation_coalgebra_packet,
    propagator_mixing_packet,
    reciprocal_weight_diagnostic,
    reflected_central_charge,
    reflected_central_packet,
    reflected_central_sum,
    reflected_level,
    scalar_conductor_packet,
    scalar_shadow_packet,
    verification_surface,
    w3_central_charge,
    ww_ope_packet,
)


ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters/examples/w3_holographic_datum.tex"
STANDALONE = ROOT / "standalone/w3_holographic_datum.tex"


def test_principal_central_charge_and_reflection_are_exact():
    k = sp.Symbol("k")
    expected = 2 - 24 * (k + 2) ** 2 / (k + 3)
    assert sp.simplify(w3_central_charge(k) - expected) == 0
    assert reflected_level(reflected_level(k)) == k
    assert reflected_central_sum(k) == 100
    assert sp.simplify(
        reflected_central_charge(k) - (100 - w3_central_charge(k))
    ) == 0


@pytest.mark.parametrize("k", [-2, -1, 0, 1, sp.Rational(7, 3)])
def test_reflected_central_sum_at_regular_levels(k):
    assert reflected_central_sum(k) == 100


def test_reflected_packet_is_typed_as_arithmetic():
    packet = reflected_central_packet(0)
    assert packet.status == "exact"
    assert packet.value["sum"] == 100
    assert packet.value["formal_midpoint"] == 50
    assert packet.value["mathematical_type"] == (
        "reflected principal central arithmetic"
    )


def test_principal_pole_is_guarded():
    with pytest.raises(ValueError):
        w3_central_charge(-3)


def test_complete_ww_packet_has_32_16_normalization():
    c = sp.Symbol("c")
    packet = ww_ope_packet(c)
    assert packet.status == "exact"
    data = packet.value
    assert sp.simplify(data["pole_2"]["Lambda"] - 32 / (5 * c + 22)) == 0
    assert sp.simplify(data["pole_1"]["dLambda"] - 16 / (5 * c + 22)) == 0
    assert data["pole_5"] == {}


def test_ww_packet_agrees_with_independent_bouwknegt_schoutens_engine():
    c = sp.Symbol("c")
    local = ww_ope_packet(c).value
    independent = bs_ww_ope_modes(c)
    assert sp.simplify(
        local["pole_2"]["Lambda"]
        - independent["mode_1"]["fields"]["Lambda"]
    ) == 0
    assert sp.simplify(
        local["pole_1"]["dLambda"]
        - independent["mode_0"]["fields"]["dLambda"]
    ) == 0


def test_mode_commutator_coefficient_uses_the_16_normalization():
    c, m, n = sp.symbols("c m n")
    expected = 16 * (m - n) / (5 * c + 22)
    assert sp.simplify(
        lambda_mode_commutator_coefficient(m, n, c) - expected
    ) == 0


def test_zamolodchikov_pole_is_guarded():
    with pytest.raises(ValueError):
        ww_ope_packet(sp.Rational(-22, 5))


def test_lambda_norm_from_the_level_four_virasoro_gram_block():
    c = sp.Symbol("c")
    packet = lambda_virasoro_witness(c)
    gram = packet.value["gram"]
    coefficient = sp.Rational(-3, 5)
    direct = (
        gram["L_-2^2,L_-2^2"]
        + 2 * coefficient * gram["L_-4,L_-2^2"]
        + coefficient**2 * gram["L_-4,L_-4"]
    )
    assert sp.factor(direct - c * (5 * c + 22) / 10) == 0
    assert sp.factor(packet.value["norm"] - lambda_norm(c)) == 0


def test_lambda_zero_mode_includes_the_normal_ordering_term():
    h = sp.Symbol("h")
    packet = lambda_zero_packet(h)
    assert packet.value["normal_ordered_TT_zero"] == h**2 + 2 * h
    assert packet.value["d2T_zero"] == 6 * h
    assert sp.factor(lambda_zero(h) - (h**2 + h / 5)) == 0
    assert sp.factor(
        lambda_zero(h) - bs_lambda_zero_witness(h)["lambda_zero"]
    ) == 0


def test_level_one_gram_determinant_is_the_null_curve():
    c, h, w = sp.symbols("c h w")
    matrix = level_one_gram_matrix(c, h, w)
    polynomial = level_one_null_polynomial(c, h, w)
    assert sp.simplify((5 * c + 22) * matrix.det() + polynomial) == 0
    expected = 9 * w**2 * (5 * c + 22) - 2 * h**2 * (32 * h + 2 - c)
    assert sp.expand(polynomial - expected) == 0


def test_level_one_curve_agrees_with_independent_engine():
    c, h, w = sp.symbols("c h w")
    assert sp.expand(
        level_one_null_polynomial(c, h, w)
        - bs_level_one_null_curve(c, h, w)
    ) == 0


def test_level_one_kernel_at_an_exact_point():
    c = sp.Integer(2)
    h = sp.Integer(1)
    w = sp.sqrt(2) / 3
    matrix = level_one_gram_matrix(c, h, w)
    vector = sp.Matrix([-3 * w / (2 * h), 1])
    assert level_one_null_polynomial(c, h, w) == 0
    assert all(sp.simplify(entry) == 0 for entry in matrix * vector)
    assert level_one_packet(c, h, w).value["determinant_identity"] == 0


def test_local_norms_and_reciprocal_weights_remain_distinct_types():
    c = sp.Symbol("c")
    norms = leading_ope_norms(c)
    diagnostic = reciprocal_weight_diagnostic()
    assert norms.value["T"] == c / 2
    assert norms.value["W"] == c / 3
    assert norms.value["mathematical_type"] == "leading self-OPE norms"
    assert diagnostic.value["value"] == sp.Rational(5, 6)
    assert diagnostic.value["mathematical_type"] == (
        "reciprocal strong-generator weights"
    )


def test_presentation_modular_and_scalar_conductor_packets_are_open():
    packets = (
        presentation_coalgebra_packet(),
        modular_kappa_packet(),
        modular_rho_packet(),
        scalar_conductor_packet(),
        genus_graph_packet(2),
        genus_graph_packet(3),
        scalar_shadow_packet("T"),
        scalar_shadow_packet("W"),
        scalar_shadow_packet("mixed"),
        propagator_mixing_packet(),
        holographic_lift_packet(),
    )
    for packet in packets:
        assert packet.status == "open"
        assert packet.value is None
        assert packet.hypotheses
        assert packet.type_signature


def test_derived_center_and_physical_comparison_keep_their_packages():
    packet = derived_center_packet()
    assert packet.status == "conditional"
    assert packet.hypotheses
    assert packet.value["formal_target"] == "Z_ch^der(W3)=C_ch^bullet(W3,W3)"
    comparison = packet.value["comparison"]
    assert comparison.status == "open"
    assert comparison.hypotheses


def test_collision_and_hamiltonian_packets_are_conditional():
    c = sp.Symbol("c")
    collision = collision_kernel_packet(c)
    hamiltonian = hamiltonian_packet()
    assert collision.status == "conditional"
    assert collision.value["WW"]["poles"] == (5, 3, 2, 1)
    assert sp.simplify(
        collision.value["WW"]["coefficients"]["z^-1*Lambda"]
        - 32 / (5 * c + 22)
    ) == 0
    assert hamiltonian.status == "conditional"
    assert hamiltonian.value["candidate_order_bound"] == 4


def test_seven_entries_keep_exact_and_reconstruction_statuses():
    datum = holographic_datum(0)
    assert tuple(datum) == (
        "A",
        "A_i",
        "A_dual",
        "C",
        "K_coll",
        "Theta",
        "nabla",
    )
    assert datum["A"].status == "exact"
    assert datum["A_i"].status == "open"
    assert datum["A_dual"].status == "conditional"
    assert datum["C"].status == "conditional"
    assert datum["K_coll"].status == "conditional"
    assert datum["Theta"].status == "conditional"
    assert datum["nabla"].status == "conditional"


def test_full_verification_surface_has_values_only_on_exact_or_conditional_rows():
    surface = verification_surface(0, 1, 0)
    assert set(surface["exact_local"]) == {
        "central",
        "ope",
        "lambda",
        "lambda_zero",
        "level_one",
    }
    assert all(
        packet.status == "exact"
        for packet in surface["exact_local"].values()
    )
    assert surface["modular"]["kappa"].value is None
    assert surface["modular"]["rho"].value is None
    assert surface["modular"]["K_kappa"].value is None
    assert surface["holographic_lift"].status == "open"


def test_packets_are_immutable():
    packet = modular_kappa_packet()
    assert isinstance(packet, ClaimPacket)
    with pytest.raises(FrozenInstanceError):
        packet.status = "exact"


def test_chapter_preserves_external_labels_and_exact_formula_packet():
    text = CHAPTER.read_text(encoding="utf-8")
    required = (
        r"\label{thm:w3hol-conductor}",
        r"\label{thm:w3hol-r-channels}",
        r"\label{prop:w3hol-lambda-on-primaries}",
        r"\label{cor:w3hol-lambda-roots}",
        r"\label{thm:w3hol-kappa-formula}",
        r"\label{thm:w3hol-kappa-sum}",
        r"\label{thm:w3hol-deltaF2}",
        r"\label{prop:w3hol-deltaF3-finite-window}",
        r"\label{thm:w3hol-propagator-variance}",
        r"\label{thm:w3hol-Q-T}",
        r"\label{thm:w3hol-Q-W}",
        r"\label{thm:w3hol-discriminants}",
        r"\label{thm:w3hol-commuting-differentials}",
        r"c(k)=2-\frac{24(k+2)^2}{k+3}",
        r"\frac{32}{D(c)}\Lambda(w)",
        r"\frac{16}{D(c)}\partial\Lambda(w)",
        r"N_\Lambda",
        r"9w^2(5c+22)=2h^2(32h+2-c)",
    )
    for fragment in required:
        assert fragment in text


def test_chapter_retires_unconstructed_scalar_values():
    text = CHAPTER.read_text(encoding="utf-8")
    retired = (
        r"\frac{5c}{6}",
        "250/3",
        r"\frac{c+204}{16c}",
        "25c^2 + 100c - 428",
        "1280",
        r"C_{\Walg_3}^{W\text{-line}} = 12",
        r"C_{\mathcal{A}} = 6",
    )
    for fragment in retired:
        assert fragment not in text


def test_standalone_uses_the_canonical_chapter_source():
    text = STANDALONE.read_text(encoding="utf-8")
    assert r"\input{chapters/examples/w3_holographic_datum}" in text
    assert "exact local algebra" in text
    assert "named reconstruction packages" in text
