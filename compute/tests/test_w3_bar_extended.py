"""Generic W3 PBW and exact generator-OPE checks."""

import pytest
import sympy as sp

from compute.lib.w3_bar_extended import (
    OpenW3ExtendedBarError,
    VACUUM,
    W3VacuumModule,
    bar_chain_dim,
    chain_dimension_analysis,
    dim_vbar_gf,
    make_state,
    state_weight,
    verify_ds_central_charge,
    verify_mu_generators,
    verify_skew_symmetry,
    vbar_basis,
)


def test_pbw_basis_matches_independent_product_character():
    max_weight = 14
    basis = vbar_basis(max_weight)
    dimensions = dim_vbar_gf(max_weight)
    assert {weight: len(basis[weight]) for weight in range(max_weight + 1)} == dimensions
    assert make_state((2,), ()) in basis[2]
    assert make_state((), (3,)) in basis[3]
    assert state_weight(make_state((3, 2), (4,))) == 9


def test_generator_ope_packet_uses_32_16_and_skew_symmetry():
    assert all(verify_mu_generators(verbose=False).values())
    assert all(verify_skew_symmetry().values())


def test_finite_module_represents_exact_generator_nth_products():
    module = W3VacuumModule(8, c_val=sp.Integer(2))
    T = make_state((2,), ())
    W = make_state((), (3,))
    assert module.compute_nth_product(T, T, 3)[0] == 1
    ww1 = module.compute_nth_product(W, W, 1)
    assert ww1[module._state_to_idx[make_state((2, 2), ())]] == 1
    assert ww1[module._state_to_idx[make_state((4,), ())]] == 0
    assert module._L_on_state(0, W) == {W: 3}
    assert module._L_on_state(-2, VACUUM) == {T: 1}


def test_raw_top_form_chain_count_is_typed_as_chain_data():
    assert bar_chain_dim(0, 4) == 3
    packet = chain_dimension_analysis(3, 10)
    assert packet["ordered_bar_differential"].status == "open"
    assert packet["bar_cohomology"].status == "open"


def test_formal_central_reflection_is_not_categorical_duality():
    packet = verify_ds_central_charge()
    assert packet["formal_reflected_sum"] == 100
    assert packet["categorical_duality"].status == "open"


def test_residue_multiplication_and_composite_mode_actions_stop_at_boundary():
    module = W3VacuumModule(8, c_val=2)
    T = make_state((2,), ())
    with pytest.raises(OpenW3ExtendedBarError):
        module.compute_mu(T, T)
    with pytest.raises(OpenW3ExtendedBarError):
        module.compute_nth_product(T, make_state((2, 2), ()), 1)
