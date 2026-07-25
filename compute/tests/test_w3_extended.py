"""Compatibility checks for the reconstructed generic W3 PBW surface."""

import pytest
import sympy as sp

from compute.lib.w3_bar_extended import (
    OpenW3ExtendedBarError,
    VACUUM,
    W3VacuumModule,
    dim_vbar,
    dim_vbar_gf,
    make_state,
    ordered_top_form_chain_dim,
    state_weight,
    vbar_basis,
)


def test_low_weight_generic_vacuum_dimensions():
    expected = {0: 0, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 8, 7: 10, 8: 17}
    assert {weight: dim_vbar(weight) for weight in expected} == expected
    assert dim_vbar_gf(8) == expected


def test_state_representation_and_basis_order():
    state = make_state((2, 4, 3), (3, 5))
    assert state == ((4, 3, 2), (5, 3))
    assert state_weight(state) == 17
    assert state in vbar_basis(17)[17]


def test_l0_and_vacuum_creation_actions_are_exact():
    module = W3VacuumModule(10, c_val=7)
    T = make_state((2,), ())
    W = make_state((), (3,))
    assert module._L_on_state(0, T) == {T: 2}
    assert module._L_on_state(0, W) == {W: 3}
    assert module._L_on_state(-2, VACUUM) == {T: 1}
    assert module._W_on_state(-3, VACUUM) == {W: 1}


def test_generator_nth_products_are_exact_at_c7():
    module = W3VacuumModule(10, c_val=7)
    T = make_state((2,), ())
    W = make_state((), (3,))
    assert module.compute_nth_product(T, T, 3)[0] == sp.Rational(7, 2)
    assert module.compute_nth_product(T, W, 1)[module._state_to_idx[W]] == 3
    assert module.compute_nth_product(W, T, 0)[module._state_to_idx[make_state((), (4,))]] == 2
    assert module.compute_nth_product(W, W, 5)[0] == sp.Rational(7, 3)


def test_raw_chain_counts_are_combinatorial_inputs():
    assert ordered_top_form_chain_dim(1, 2) == 1
    assert ordered_top_form_chain_dim(2, 4) == 1
    assert ordered_top_form_chain_dim(3, 6) == 2


def test_general_composite_mode_action_is_open():
    module = W3VacuumModule(10, c_val=7)
    with pytest.raises(OpenW3ExtendedBarError):
        module._L_on_state(-2, make_state((2,), ()))
