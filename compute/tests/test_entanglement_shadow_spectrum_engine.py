from __future__ import annotations

import math
from fractions import Fraction

import pytest

from compute.lib import entanglement_shadow_spectrum_engine as eng


ONE_THIRD = Fraction(1, 3)
# VERIFIED: [DC] c=1 gives S_EE=(1/3)log(L/eps); [LT] Calabrese-Cardy single-interval entropy.

TWO_THIRDS = Fraction(2, 3)
# VERIFIED: [DC] kappa_EE=2*kappa/3 at kappa=1; [LT] CLAUDE C1 gives kappa(H_1)=1.

THREE_HALVES = Fraction(3, 2)
# VERIFIED: [DC] sl_2 at k=1 has kappa=3(1+2)/4=9/4, then 2*kappa/3=3/2; [LT] CLAUDE C3 affine KM formula.

THIRTEEN_THIRDS = Fraction(13, 3)
# VERIFIED: [DC] c=13 gives kappa=13/2 and kappa_EE=13/3; [SY] c=13 is the Virasoro self-dual point.

TWENTY_SIX_THIRDS = Fraction(26, 3)
# VERIFIED: [DC] K_EE(Vir)=13/3+13/3=26/3; [SY] Vir duality c <-> 26-c fixes c=13.

NEGATIVE_SIX = Fraction(-6, 1)
# VERIFIED: [DC] c_BP(0)=2-24/3=-6; [LT] w_algebras_deep.tex BP central-charge formula.

NEGATIVE_ONE = Fraction(-1, 1)
# VERIFIED: [DC] kappa_BP(0)=c_BP(0)/6=-1; [LT] varrho_BP=1/6 and kappa=varrho*c in w_algebras_deep.tex.

NINETY_EIGHT_THIRDS = Fraction(98, 3)
# VERIFIED: [DC] 196/6=98/3 from BP conductor 196 and varrho_BP=1/6; [LT] CLAUDE C31.

ZERO = Fraction(0, 1)
# VERIFIED: [DC] additive identity; [SY] anti-symmetric duality gives exact cancellation.


BC_BG_CANCELLATION_CASES = [
    (Fraction(0), Fraction(-2), Fraction(2)),
    # VERIFIED: [DC] direct substitution at lambda=0; [SY] c_bg=-c_bc by polynomial identity.
    (Fraction(1, 2), Fraction(1), Fraction(-1)),
    # VERIFIED: [DC] lambda=1/2 gives c_bc=1 and c_bg=-1; [LC] free fermion / symplectic boson normalization.
    (Fraction(1), Fraction(-2), Fraction(2)),
    # VERIFIED: [DC] lambda=1 gives c_bc=-2 and c_bg=2; [SY] ghost complementarity.
    (Fraction(3, 2), Fraction(-11), Fraction(11)),
    # VERIFIED: [DC] lambda=3/2 gives c_bc=-11 and c_bg=11; [SY] exact cancellation.
    (Fraction(2), Fraction(-26), Fraction(26)),
    # VERIFIED: [DC] lambda=2 gives reparametrization-ghost values; [LT] standard bc/betagamma cancellation.
]


AFFINE_ZERO_LEVEL_CASES = [
    ("sl_2", Fraction(3, 2)),
    # VERIFIED: [DC] dim(sl_2)/2=3/2 at k=0; [LT] CLAUDE C3 zero-level check.
    ("sl_3", Fraction(4, 1)),
    # VERIFIED: [DC] dim(sl_3)/2=8/2=4; [LT] affine KM census formula.
    ("e_8", Fraction(124, 1)),
    # VERIFIED: [DC] dim(E_8)/2=248/2=124; [LT] E_8 adjoint dimension 248.
]


AFFINE_CRITICAL_CASES = [
    ("sl_2", Fraction(-2)),
    # VERIFIED: [DC] k=-h^v=-2 makes kappa=0; [LT] CLAUDE C3 critical-level check.
    ("sl_3", Fraction(-3)),
    # VERIFIED: [DC] k=-h^v=-3 makes kappa=0; [LT] affine KM census formula.
    ("e_8", Fraction(-30)),
    # VERIFIED: [DC] k=-h^v=-30 makes kappa=0; [LT] E_8 has h^v=30.
]


AFFINE_CENTRAL_CHARGE_CASES = [
    ("sl_2", Fraction(1), Fraction(1)),
    # VERIFIED: [DC] 3*1/(1+2)=1; [LT] standard affine SU(2)_1 central charge.
    ("sl_3", Fraction(1), Fraction(2)),
    # VERIFIED: [DC] 8*1/(1+3)=2; [LT] standard affine SU(3)_1 central charge.
    ("e_8", Fraction(1), Fraction(8)),
    # VERIFIED: [DC] 248*1/(1+30)=8; [LT] E_8 level-1 central charge.
]


W_KAPPA_CASES = [
    (2, Fraction(1), Fraction(1, 2)),
    # VERIFIED: [DC] H_2-1=1/2; [CF] W_2 must match Virasoro.
    (3, Fraction(6), Fraction(5)),
    # VERIFIED: [DC] H_3-1=5/6 so 6*(5/6)=5; [LT] CLAUDE C4 N=3 check.
    (4, Fraction(12), Fraction(13)),
    # VERIFIED: [DC] H_4-1=13/12 so 12*(13/12)=13; [CF] harmonic-number formula.
]


UNIVERSAL_SHADOW_CASES = [
    ("heisenberg", {"k": Fraction(1)}),
    # VERIFIED: [DC] kappa=1 gives universal 2/3 coefficient; [LT] CLAUDE C1.
    ("virasoro", {"c": Fraction(1)}),
    # VERIFIED: [DC] kappa=c/2=1/2; [LT] CLAUDE C2.
    ("affine_km", {"lie_algebra": "sl_2", "k": Fraction(1)}),
    # VERIFIED: [DC] kappa=9/4 so S_shadow/kappa=2/3; [LT] CLAUDE C3.
    ("affine_km", {"lie_algebra": "sl_3", "k": Fraction(1)}),
    # VERIFIED: [DC] same ratio is parameter-independent; [LT] affine KM formula.
    ("w_n", {"N": 3, "c": Fraction(6)}),
    # VERIFIED: [DC] kappa=5 and S_shadow/kappa=2/3; [CF] W_N shadow formula.
    ("bc", {"lam": Fraction(2)}),
    # VERIFIED: [DC] kappa=-13 and S_shadow/kappa=2/3; [LT] bc ghost central charge.
    ("betagamma", {"lam": Fraction(2)}),
    # VERIFIED: [DC] kappa=13 and S_shadow/kappa=2/3; [SY] c_bg=-c_bc at lambda=2.
    ("bershadsky_polyakov", {"k": Fraction(0)}),
    # VERIFIED: [DC] kappa=-1 and S_shadow/kappa=2/3; [LT] BP kappa=c/6 on the live source.
]


def test_heisenberg_entropy_at_k_one_and_e_ratio() -> None:
    entropy = eng.entanglement_entropy(eng.heisenberg_central_charge(), math.e, 1.0)
    assert entropy == pytest.approx(float(ONE_THIRD))


def test_virasoro_entropy_at_c_one_and_e_ratio() -> None:
    entropy = eng.entanglement_entropy(eng.virasoro_central_charge(1), math.e, 1.0)
    assert entropy == pytest.approx(float(ONE_THIRD))


def test_virasoro_kappa_ee_at_c_thirteen() -> None:
    assert eng.entanglement_shadow_kappa(eng.virasoro_kappa(13)) == THIRTEEN_THIRDS


def test_heisenberg_kappa_ee_at_k_one() -> None:
    assert eng.entanglement_shadow_kappa(eng.heisenberg_kappa(1)) == TWO_THIRDS


def test_affine_sl2_kappa_ee_at_k_one() -> None:
    assert eng.entanglement_shadow_kappa(eng.affine_km_kappa("sl_2", 1)) == THREE_HALVES


def test_virasoro_entanglement_koszul_conductor() -> None:
    assert eng.virasoro_entanglement_koszul_conductor(7) == TWENTY_SIX_THIRDS


def test_affine_entanglement_koszul_conductor() -> None:
    assert eng.affine_km_entanglement_koszul_conductor("sl_2", 1) == ZERO


def test_heisenberg_entanglement_koszul_conductor() -> None:
    assert eng.heisenberg_entanglement_koszul_conductor(1) == ZERO


def test_w2_kappa_matches_virasoro() -> None:
    assert eng.w_algebra_kappa(2, 13) == eng.virasoro_kappa(13)


@pytest.mark.parametrize(("lam", "expected_bc", "expected_bg"), BC_BG_CANCELLATION_CASES)
def test_bc_and_betagamma_central_charges_cancel(
    lam: Fraction,
    expected_bc: Fraction,
    expected_bg: Fraction,
) -> None:
    assert eng.bc_central_charge(lam) == expected_bc
    assert eng.betagamma_central_charge(lam) == expected_bg
    assert eng.bc_central_charge(lam) + eng.betagamma_central_charge(lam) == ZERO


@pytest.mark.parametrize(("lie_algebra", "expected"), AFFINE_ZERO_LEVEL_CASES)
def test_affine_kappa_at_zero_level_is_dim_over_two(
    lie_algebra: str,
    expected: Fraction,
) -> None:
    assert eng.affine_km_kappa(lie_algebra, 0) == expected


@pytest.mark.parametrize(("lie_algebra", "critical_level"), AFFINE_CRITICAL_CASES)
def test_affine_kappa_at_critical_level_is_zero(
    lie_algebra: str,
    critical_level: Fraction,
) -> None:
    assert eng.affine_km_kappa(lie_algebra, critical_level) == ZERO


@pytest.mark.parametrize(("lie_algebra", "level", "expected"), AFFINE_CENTRAL_CHARGE_CASES)
def test_affine_central_charge_samples(
    lie_algebra: str,
    level: Fraction,
    expected: Fraction,
) -> None:
    assert eng.affine_km_central_charge(lie_algebra, level) == expected


@pytest.mark.parametrize(("N", "central_charge", "expected"), W_KAPPA_CASES)
def test_w_algebra_kappa_samples(
    N: int,
    central_charge: Fraction,
    expected: Fraction,
) -> None:
    assert eng.w_algebra_kappa(N, central_charge) == expected


def test_harmonic_number_for_w2_case() -> None:
    assert eng.harmonic_number(2) == Fraction(3, 2)


def test_harmonic_number_for_w3_case() -> None:
    assert eng.harmonic_number(3) == Fraction(11, 6)


def test_heisenberg_central_charge_is_one() -> None:
    assert eng.heisenberg_central_charge() == Fraction(1)


def test_bc_kappa_is_half_the_central_charge() -> None:
    lam = Fraction(2)
    assert eng.bc_kappa(lam) == eng.bc_central_charge(lam) / 2


def test_betagamma_kappa_is_half_the_central_charge() -> None:
    lam = Fraction(2)
    assert eng.betagamma_kappa(lam) == eng.betagamma_central_charge(lam) / 2


def test_bershadsky_polyakov_central_charge_at_zero() -> None:
    assert eng.bershadsky_polyakov_central_charge(0) == NEGATIVE_SIX


def test_bershadsky_polyakov_kappa_at_zero() -> None:
    assert eng.bershadsky_polyakov_kappa(0) == NEGATIVE_ONE


def test_bershadsky_polyakov_kappa_complementarity_sum_at_zero() -> None:
    left = eng.bershadsky_polyakov_kappa(0)
    right = eng.bershadsky_polyakov_kappa(-6)
    assert left + right == NINETY_EIGHT_THIRDS


def test_bershadsky_polyakov_central_charge_pole_at_minus_three() -> None:
    with pytest.raises(ValueError):
        eng.bershadsky_polyakov_central_charge(-3)


def test_affine_central_charge_pole_at_critical_level() -> None:
    with pytest.raises(ValueError):
        eng.affine_km_central_charge("sl_2", -2)


def test_log_ratio_uses_natural_log() -> None:
    assert eng.log_ratio(math.e, 1.0) == pytest.approx(1.0)


def test_universal_shadow_ratio_at_e() -> None:
    assert eng.universal_shadow_ratio(math.e, 1.0) == pytest.approx(float(TWO_THIRDS))


@pytest.mark.parametrize(("family", "params"), UNIVERSAL_SHADOW_CASES)
def test_shadow_spectrum_ratio_is_universal(
    family: str,
    params: dict[str, Fraction | str | int],
) -> None:
    record = eng.build_family_record(family, L=math.e, eps=1.0, **params)
    assert record["shadow_spectrum_ratio"] == pytest.approx(float(TWO_THIRDS))


def test_build_family_record_contains_physical_and_shadow_data() -> None:
    record = eng.build_family_record("heisenberg", k=1, L=math.e, eps=1.0)
    assert record["entanglement_entropy"] == pytest.approx(float(ONE_THIRD))
    assert record["shadow_entropy"] == pytest.approx(float(TWO_THIRDS))


def test_build_family_record_contains_virasoro_duality_data() -> None:
    record = eng.build_family_record("virasoro", c=13, L=math.e, eps=1.0)
    assert record["dual_params"] == {"c": Fraction(13)}
    assert record["kappa_ee_dual"] == THIRTEEN_THIRDS
    assert record["entanglement_koszul_conductor"] == TWENTY_SIX_THIRDS


def test_build_family_record_contains_affine_duality_data() -> None:
    record = eng.build_family_record("affine_km", lie_algebra="sl_2", k=1, L=math.e, eps=1.0)
    assert record["dual_params"] == {"lie_algebra": "sl_2", "k": Fraction(-5)}
    assert record["entanglement_koszul_conductor"] == ZERO


def test_build_family_record_contains_heisenberg_duality_data() -> None:
    record = eng.build_family_record("heisenberg", k=1, L=math.e, eps=1.0)
    assert record["dual_params"] == {"k": Fraction(-1)}
    assert record["entanglement_koszul_conductor"] == ZERO


def test_generate_census_table_returns_all_standard_families() -> None:
    table = eng.generate_census_table(L=math.e, eps=1.0)
    assert set(table) == {
        "heisenberg",
        "virasoro",
        "affine_km",
        "w_n",
        "bc",
        "betagamma",
        "bershadsky_polyakov",
    }


def test_generate_census_table_records_kappa_ee_values() -> None:
    table = eng.generate_census_table(L=math.e, eps=1.0)
    assert table["heisenberg"]["k=1"]["kappa_ee"] == TWO_THIRDS
    assert table["virasoro"]["c=13"]["kappa_ee"] == THIRTEEN_THIRDS


def test_generate_census_table_uses_dict_of_dicts_shape() -> None:
    table = eng.generate_census_table(L=math.e, eps=1.0)
    assert isinstance(table["affine_km"], dict)
    assert "k=1,lie_algebra=sl_2" in table["affine_km"]
    assert "k=1,lie_algebra=sl_3" in table["affine_km"]


def test_generate_census_table_uses_sorted_parameter_keys() -> None:
    table = eng.generate_census_table(
        L=math.e,
        eps=1.0,
        sweeps={"affine_km": ({"lie_algebra": "sl_2", "k": Fraction(1)},)},
    )
    assert list(table["affine_km"]) == ["k=1,lie_algebra=sl_2"]


def test_w2_record_matches_virasoro_shadow_data() -> None:
    w_record = eng.build_family_record("w_n", N=2, c=13, L=math.e, eps=1.0)
    vir_record = eng.build_family_record("virasoro", c=13, L=math.e, eps=1.0)
    assert w_record["kappa"] == vir_record["kappa"]
    assert w_record["kappa_ee"] == vir_record["kappa_ee"]


def test_bershadsky_polyakov_record_has_no_duality_slot() -> None:
    record = eng.build_family_record("bershadsky_polyakov", k=0, L=math.e, eps=1.0)
    assert record["dual_params"] is None
    assert record["entanglement_koszul_conductor"] is None
