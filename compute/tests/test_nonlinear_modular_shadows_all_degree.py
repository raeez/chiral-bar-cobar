"""Independent verification for the all-degree NMS master equation."""

from __future__ import annotations

from sympy import Rational, simplify

from compute.lib.independent_verification import independent_verification
from compute.lib.nonlinear_modular_shadows_all_degree import (
    bracket_output_degree,
    c,
    linear_pair_coefficient,
    obstruction_is_future_free,
    obstruction_pair_coefficients,
    ordered_degree_pairs,
    scalar_master_residual,
    virasoro_generating_function_tower,
    virasoro_master_tower,
)


@independent_verification(
    claim="thm:nms-all-degree-master-equation",
    derived_from=[
        "appendices/nonlinear_modular_shadows.tex proof of the all-degree master equation",
        "Definition def:nms-degree-r-obstruction and its c_{p,q} coefficients",
    ],
    verified_against=[
        "Ordered finite-degree pair enumeration in one half of the Hamiltonian bracket",
        "Automorphism count of one-edge two-vertex graphs: two ordered flags off diagonal and one on the diagonal",
    ],
    disjoint_rationale=(
        "The manuscript states the collected degree-r formula. This test "
        "reconstructs the coefficient 1 or 1/2 from the ordered finite "
        "pair expansion and graph automorphism count, without reading the "
        "definition's coefficient table."
    ),
)
def test_ordered_pair_collection_gives_exact_obstruction_coefficients():
    """The coefficient c_{p,q} is forced by ordered-pair collection."""
    for r in range(3, 22):
        ordered = ordered_degree_pairs(r)
        assert ordered
        assert all(bracket_output_degree(p, q) == r for p, q in ordered)

        linear = linear_pair_coefficient(r)
        assert linear.p == 2 and linear.q == r
        assert linear.ordered_count == 2
        assert linear.coefficient == 1

        for item in obstruction_pair_coefficients(r):
            assert item.p >= 3
            assert item.p + item.q == r + 2
            if item.p == item.q:
                assert item.ordered_count == 1
                assert item.coefficient == Rational(1, 2)
            else:
                assert item.ordered_count == 2
                assert item.coefficient == 1


@independent_verification(
    claim="thm:nms-all-degree-master-equation",
    derived_from=[
        "appendices/nonlinear_modular_shadows.tex proof of degree-r closure",
        "Quintic and sextic examples displayed in Definition def:nms-degree-r-obstruction",
    ],
    verified_against=[
        "Finite future-free dependency check for every obstruction pair through degree 40",
        "Direct degree equation p+q-2=r for single-edge contraction",
    ],
    disjoint_rationale=(
        "The proof argues abstractly in the completed filtration. The test "
        "checks the finite dependency graph: after the linear (2,r) term is "
        "removed, every obstruction at degree r only sees lower degrees."
    ),
)
def test_obstruction_part_uses_only_lower_shadow_degrees():
    """The nonlinear obstruction never depends on the unknown Sh_r."""
    for r in range(3, 41):
        assert obstruction_is_future_free(r)
        for item in obstruction_pair_coefficients(r):
            assert item.p < r
            assert item.q < r
            assert bracket_output_degree(item.p, item.q) == r


@independent_verification(
    claim="thm:nms-all-degree-master-equation",
    derived_from=[
        "appendices/nonlinear_modular_shadows.tex all-degree master equation",
        "Local NMS theorem proof using homogeneous degree projection",
    ],
    verified_against=[
        "Virasoro shadow metric square-root identity H(t)^2=t^4 Q_L(t)",
        "Coefficient comparison for Q_L(t)=c^2+12ct+((180c+872)/(5c+22))t^2",
        "Exact residual computation of the scalar master recurrence through arity 16",
    ],
    disjoint_rationale=(
        "The theorem proof is a formal MC-degree argument. The check compares "
        "the recurrence it implies on the Virasoro scalar line with an "
        "independent generating-function coefficient extraction from the "
        "quadratic shadow metric."
    ),
)
def test_virasoro_master_recurrence_matches_square_root_metric():
    """Virasoro coefficients from the master equation equal the metric route."""
    master = virasoro_master_tower(max_r=16)
    metric = virasoro_generating_function_tower(max_r=16)

    for r in range(2, 17):
        assert simplify(master[r] - metric[r]) == 0

    for r in range(5, 17):
        assert scalar_master_residual(r, master, Rational(2) / c) == 0


@independent_verification(
    claim="thm:nms-all-degree-master-equation",
    derived_from=[
        "appendices/nonlinear_modular_shadows.tex recurrence statement",
        "compute/lib/virasoro_quintic_shadow.py quintic-only calculation",
    ],
    verified_against=[
        "Exact all-degree recurrence specialized at c=13 and c=26",
        "Independent rational values extracted from the square-root metric path",
    ],
    disjoint_rationale=(
        "The test does not reuse the quintic-only engine. It solves the "
        "all-degree recurrence and checks low-degree rational witnesses "
        "against values obtained from the metric coefficient route."
    ),
)
def test_virasoro_low_degree_rational_witnesses():
    """Exact rational witnesses at the self-dual and critical central charges."""
    tower = virasoro_master_tower(max_r=7)

    assert simplify(tower[5].subs(c, 13) - Rational(-16, 4901)) == 0
    assert simplify(tower[6].subs(c, 13) - Rational(62240, 49887279)) == 0
    assert simplify(tower[7].subs(c, 13) - Rational(-81920, 168138607)) == 0

    assert simplify(tower[5].subs(c, 26) - Rational(-3, 6422)) == 0
    assert simplify(tower[6].subs(c, 26) - Rational(6815, 76139232)) == 0
    assert simplify(tower[7].subs(c, 26) - Rational(-20295, 1154778352)) == 0
