"""Independent exact checks for universal-conductor type separation."""

from pathlib import Path

import sympy as sp

from compute.lib.universal_conductor_type_engine import (
    arity_two_deconcatenation_obstruction,
    concatenation_descends_to_coinvariants,
    reynolds_coinvariant_certificate,
    reynolds_lie_defect_certificate,
    reynolds_matrix,
)


ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapters" / "theory" / "universal_conductor_K_platonic.tex"


def test_reynolds_is_an_exact_idempotent() -> None:
    for dimension in (1, 2, 3):
        for arity in (0, 1, 2, 3):
            certificate = reynolds_coinvariant_certificate(dimension, arity)
            assert certificate.idempotent
            assert certificate.invariant_dimension == certificate.expected_symmetric_dimension


def test_quotient_after_reynolds_is_the_original_coinvariant_quotient() -> None:
    for dimension in (2, 3):
        for arity in (2, 3, 4):
            certificate = reynolds_coinvariant_certificate(dimension, arity)
            assert certificate.quotient_after_reynolds_equals_quotient


def test_reynolds_rank_has_two_independent_oracles() -> None:
    certificate = reynolds_coinvariant_certificate(3, 4)
    assert certificate.invariant_dimension == 15
    assert certificate.expected_symmetric_dimension == 15
    assert certificate.tensor_dimension == 81
    assert len(reynolds_matrix(3, 4).nullspace()) == 66


def test_raw_deconcatenation_kernel_is_not_a_coideal() -> None:
    certificate = arity_two_deconcatenation_obstruction()
    assert certificate.quotient_of_kernel_vector == sp.zeros(3, 1)
    assert certificate.reduced_deconcatenation_after_arity_one_quotients != sp.zeros(4, 1)
    assert not certificate.kernel_is_coideal


def test_equivariance_alone_does_not_make_reynolds_a_lie_morphism() -> None:
    certificate = reynolds_lie_defect_certificate()
    assert certificate.first_kernel_element == sp.Matrix([[0, 1], [0, 0]])
    assert certificate.second_kernel_element == sp.Matrix([[0, 0], [1, 0]])
    assert certificate.bracket == sp.diag(1, -1)
    assert certificate.averaged_bracket == sp.diag(1, -1)
    assert certificate.bracket_of_averages == sp.zeros(2)
    assert certificate.defect == sp.diag(1, -1)
    assert not certificate.reynolds_is_lie_morphism
    assert not certificate.kernel_is_lie_ideal


def test_equivariant_concatenation_descends_to_coinvariants() -> None:
    for dimension in (1, 2, 3):
        for left_arity, right_arity in ((1, 1), (1, 2), (2, 2)):
            assert concatenation_descends_to_coinvariants(
                dimension, left_arity, right_arity
            )


def test_manuscript_records_the_arity_two_coalgebra_firewall() -> None:
    source = CHAPTER.read_text(encoding="utf-8")
    assert r"q_n\circ\Av^{\mathrm{Rey}}_{\Sigma_n}=q_n" in source
    assert r"a=[v|w]-[w|v]" in source
    assert r"\bar\Delta_T(a)=v\otimes w-w\otimes v" in source
    assert "shuffle/factorization coproduct supplied by the hypothesis package" in source


def test_manuscript_types_the_reynolds_model_as_transported_structure() -> None:
    source = CHAPTER.read_text(encoding="utf-8")
    assert "fixed-point summand receives the\noperations transported from the quotient" in source
    assert r"[x,y]_{\mathrm{tr}}" in source
    assert r"=\mathrm{Re}_{m+n}[\widetilde x,\widetilde y]" in source
    assert "Reynolds-kernel criterion" in source
