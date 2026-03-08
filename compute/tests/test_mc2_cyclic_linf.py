"""Tests for the MC2 cyclic L-infinity compute scaffold."""

from sympy import Rational, simplify

from compute.lib.mc2_cyclic_linf import (
    build_mc2_coderivation_dg_lie_model,
    build_mc2_cyclic_linf_model,
    build_mc2_sl2_coderivation_seed,
    build_mc2_sl2_cyclic_linf_seed,
    mc_residual_single_parameter,
    solve_mc_single_parameter,
    verify_mc2_cyclic_linf_scaffold,
    verify_mc2_sl2_seed_from_bar,
)


class TestMC2CoderivationDGLie:
    def test_d_squared_zero(self):
        model = build_mc2_coderivation_dg_lie_model()
        assert model.verify_d_squared_zero()

    def test_jacobi(self):
        model = build_mc2_coderivation_dg_lie_model()
        assert model.verify_jacobi_identity()

    def test_leibniz(self):
        model = build_mc2_coderivation_dg_lie_model()
        assert model.verify_d_leibniz()


class TestMC2CyclicLInfinity:
    def test_residual_formula(self):
        model = build_mc2_cyclic_linf_model()
        t, residual = mc_residual_single_parameter(model)
        # residual is (t^2 - t^3) * omega
        assert residual.keys() == {"omega"}
        assert simplify(residual["omega"] - (t**2 - t**3)) == 0

    def test_mc_solver(self):
        model = build_mc2_cyclic_linf_model()
        solved = solve_mc_single_parameter(model)
        assert set(solved["solutions"]) == {Rational(0), Rational(1)}

    def test_solver_residual_vanishes_at_solutions(self):
        model = build_mc2_cyclic_linf_model()
        solved = solve_mc_single_parameter(model)
        t = solved["parameter"]
        residual = solved["residual"]["omega"]
        for value in solved["solutions"]:
            assert residual.subs({t: value}) == 0

    def test_cyclic_pairing_compatibility(self):
        model = build_mc2_cyclic_linf_model()
        left_l2 = model.pairing_vectors(model.l2_basis("theta", "theta"), {"theta": 1})
        right_l2 = model.pairing_vectors({"theta": 1}, model.l2_basis("theta", "theta"))
        assert simplify(left_l2 - right_l2) == 0

        left_l3 = model.pairing_vectors(
            model.l3_basis("theta", "theta", "theta"),
            {"theta": 1},
        )
        right_l3 = model.pairing_vectors(
            {"theta": 1},
            model.l3_basis("theta", "theta", "theta"),
        )
        assert simplify(left_l3 - right_l3) == 0


class TestMC2ScaffoldBundle:
    def test_verify_bundle(self):
        checks = verify_mc2_cyclic_linf_scaffold()
        assert all(checks.values()), checks


class TestMC2Sl2Seed:
    def test_dg_lie_identities(self):
        model = build_mc2_sl2_coderivation_seed()
        assert model.verify_d_squared_zero()
        assert model.verify_jacobi_identity()
        assert model.verify_d_leibniz()

    def test_expected_brackets(self):
        model = build_mc2_sl2_coderivation_seed()
        assert model.bracket_basis("e", "f") == {"h": Rational(1)}
        assert model.bracket_basis("h", "e") == {"e": Rational(2)}
        assert model.bracket_basis("h", "f") == {"f": Rational(-2)}

    def test_normalized_pairing(self):
        model = build_mc2_sl2_cyclic_linf_seed()
        assert simplify(model.pairing_basis("e", "f") - 1) == 0
        assert simplify(model.pairing_basis("f", "e") - 1) == 0
        assert simplify(model.pairing_basis("h", "h") - 2) == 0

    def test_verify_sl2_seed_bundle(self):
        checks = verify_mc2_sl2_seed_from_bar()
        assert all(checks.values()), checks
