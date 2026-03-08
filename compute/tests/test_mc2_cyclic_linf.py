"""Tests for the MC2 cyclic L-infinity compute scaffold."""

from sympy import Rational, simplify

from compute.lib.mc2_cyclic_linf import (
    boundary_clutching_series_via_l2,
    build_mc2_coderivation_dg_lie_model,
    build_cyclic_l3_marker_extension_from_seed,
    build_mc2_cyclic_linf_model,
    build_mc2_sl2_coderivation_seed,
    build_mc2_sl2_cyclic_linf_seed,
    build_mc2_sl2_cyclic_linf_l3_seed,
    build_mc2_sl2_shifted_cyclic_linf_l3_seed,
    build_mc2_sl3_shifted_cyclic_linf_l3_seed,
    build_mc2_sp4_shifted_cyclic_linf_l3_seed,
    completed_pairing_series,
    completed_mc_obstruction_term_at_genus,
    completed_tensor_product_surrogate,
    cyclic_ce_profile_from_cyclic_seed,
    mc2_shifted_seed_one_channel_normalization_profiles,
    shifted_seed_eta_channel_scaling_profile,
    shifted_seed_obstruction_polynomial_profile,
    mc_residual_completed_truncated,
    mc_residual_single_parameter,
    mc_residual_three_parameter,
    solve_completed_mc_basis_family_recursive,
    solve_completed_mc_basis_family_truncated,
    solve_completed_mc_single_basis_recursive,
    solve_completed_mc_single_basis_truncated,
    solve_mc_single_parameter,
    verify_boundary_clutching_compatibility,
    verify_completed_cyclic_l2,
    verify_completed_cyclic_l3,
    verify_genus_stratified_obstruction_identity,
    verify_mc2_completion_clutching_scaffold,
    verify_mc2_cyclic_linf_scaffold,
    verify_mc2_sl2_seed_from_bar,
    verify_mc2_sl2_l3_seed,
    verify_mc2_sl2_shifted_seed_nontrivial_mc,
    verify_mc2_sl3_shifted_seed_nontrivial_mc,
    verify_mc2_sp4_shifted_seed_nontrivial_mc,
    verify_mc2_shifted_seed_eta_scaling_law,
    verify_mc2_shifted_seed_obstruction_polynomial_law,
    verify_mc2_shifted_seed_one_channel_normalization,
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


class TestMC2Sl2L3Seed:
    def test_l3_channel_is_nontrivial(self):
        model = build_mc2_sl2_cyclic_linf_l3_seed()
        assert model.l3_basis("e", "h", "f").get("eta", 0) != 0

    def test_three_parameter_residual_has_eta_channel(self):
        model = build_mc2_sl2_cyclic_linf_l3_seed()
        (x, y, z), residual = mc_residual_three_parameter(model)
        assert set(residual.keys()) == {"eta"}
        eta = simplify(residual["eta"])
        assert eta != 0
        assert simplify(eta.subs({x: 1, y: 1, z: 1})) != 0
        assert simplify(eta.subs({x: 0})) == 0
        assert simplify(eta.subs({y: 0})) == 0
        assert simplify(eta.subs({z: 0})) == 0

    def test_verify_l3_seed_bundle(self):
        checks = verify_mc2_sl2_l3_seed()
        assert all(checks.values()), checks


class TestMC2Sl2ShiftedL3Seed:
    def test_shifted_residual_eta_channel(self):
        model = build_mc2_sl2_shifted_cyclic_linf_l3_seed()
        (x, y, z), residual = mc_residual_three_parameter(model)
        assert set(residual.keys()) == {"eta"}
        eta = simplify(residual["eta"])
        assert simplify(eta.subs({x: 1, y: 1, z: 1}) + 2) == 0
        assert simplify(eta.subs({x: 0})) == 0
        assert simplify(eta.subs({y: 0})) == 0
        assert simplify(eta.subs({z: 0})) == 0

    def test_shifted_obstruction_terms(self):
        model = build_mc2_sl2_shifted_cyclic_linf_l3_seed()
        alpha = {1: {"e": Rational(1), "h": Rational(1), "f": Rational(1)}}
        obstruction_g2 = completed_mc_obstruction_term_at_genus(
            model=model,
            alpha_series=alpha,
            genus=2,
            require_zero_genus=True,
        )
        obstruction_g3 = completed_mc_obstruction_term_at_genus(
            model=model,
            alpha_series=alpha,
            genus=3,
            require_zero_genus=True,
        )
        assert obstruction_g2 == {"e": Rational(-2), "h": Rational(1), "f": Rational(-2)}
        assert obstruction_g3 == {"eta": Rational(-2)}

    def test_verify_shifted_seed_bundle(self):
        checks = verify_mc2_sl2_shifted_seed_nontrivial_mc()
        assert all(checks.values()), checks


class TestMC2Sl3ShiftedL3Seed:
    def test_shifted_residual_eta_channel(self):
        model = build_mc2_sl3_shifted_cyclic_linf_l3_seed()
        (x, y, z), residual = mc_residual_three_parameter(
            model,
            basis_elements=("e1", "e2", "f12"),
        )
        assert set(residual.keys()) == {"eta"}
        eta = simplify(residual["eta"])
        assert simplify(eta.subs({x: 1, y: 1, z: 1}) - 1) == 0
        assert simplify(eta.subs({x: 0})) == 0
        assert simplify(eta.subs({y: 0})) == 0
        assert simplify(eta.subs({z: 0})) == 0

    def test_shifted_obstruction_terms(self):
        model = build_mc2_sl3_shifted_cyclic_linf_l3_seed()
        alpha = {1: {"e1": Rational(1), "e2": Rational(1), "f12": Rational(1)}}
        obstruction_g2 = completed_mc_obstruction_term_at_genus(
            model=model,
            alpha_series=alpha,
            genus=2,
            require_zero_genus=True,
        )
        obstruction_g3 = completed_mc_obstruction_term_at_genus(
            model=model,
            alpha_series=alpha,
            genus=3,
            require_zero_genus=True,
        )
        assert obstruction_g2 == {"e12": Rational(1), "f1": Rational(1), "f2": Rational(-1)}
        assert obstruction_g3 == {"eta": Rational(1)}

    def test_verify_shifted_seed_bundle(self):
        checks = verify_mc2_sl3_shifted_seed_nontrivial_mc()
        assert all(checks.values()), checks


class TestMC2Sp4ShiftedL3Seed:
    def test_shifted_residual_eta_channel(self):
        model = build_mc2_sp4_shifted_cyclic_linf_l3_seed()
        (x, y, z), residual = mc_residual_three_parameter(
            model,
            basis_elements=("e1", "e2", "f12"),
        )
        assert set(residual.keys()) == {"eta"}
        eta = simplify(residual["eta"])
        assert simplify(eta.subs({x: 1, y: 1, z: 1}) - 2) == 0
        assert simplify(eta.subs({x: 0})) == 0
        assert simplify(eta.subs({y: 0})) == 0
        assert simplify(eta.subs({z: 0})) == 0

    def test_shifted_obstruction_terms(self):
        model = build_mc2_sp4_shifted_cyclic_linf_l3_seed()
        alpha = {1: {"e1": Rational(1), "e2": Rational(1), "f12": Rational(1)}}
        obstruction_g2 = completed_mc_obstruction_term_at_genus(
            model=model,
            alpha_series=alpha,
            genus=2,
            require_zero_genus=True,
        )
        obstruction_g3 = completed_mc_obstruction_term_at_genus(
            model=model,
            alpha_series=alpha,
            genus=3,
            require_zero_genus=True,
        )
        assert obstruction_g2 == {"e12": Rational(1), "f1": Rational(1), "f2": Rational(-2)}
        assert obstruction_g3 == {"eta": Rational(2)}

    def test_verify_shifted_seed_bundle(self):
        checks = verify_mc2_sp4_shifted_seed_nontrivial_mc()
        assert all(checks.values()), checks


class TestMC2ShiftedOneChannelNormalization:
    def test_profiles_match_expected_eta_channels(self):
        profiles = mc2_shifted_seed_one_channel_normalization_profiles()
        expected = {"sl2": Rational(-2), "sl3": Rational(1), "sp4": Rational(2)}
        for key, expected_eta in expected.items():
            assert simplify(profiles[key]["eta_residual_at_111"] - expected_eta) == 0
            assert simplify(profiles[key]["obstruction_eta"] - expected_eta) == 0
            assert profiles[key]["residual_support"] == ("eta",)
            assert profiles[key]["obstruction_support"] == ("eta",)
            assert simplify(profiles[key]["normalization_ratio"] - 1) == 0

    def test_verify_shifted_one_channel_bundle(self):
        checks = verify_mc2_shifted_seed_one_channel_normalization()
        assert all(checks.values()), checks


class TestMC2ShiftedEtaScalingLaw:
    def test_sl2_scaling_profile(self):
        profile = shifted_seed_eta_channel_scaling_profile(
            build_mc2_sl2_shifted_cyclic_linf_l3_seed(),
            basis_elements=("e", "h", "f"),
            alpha_basis=("e", "h", "f"),
        )
        t = profile["parameter"]
        assert simplify(profile["eta_residual_at_111"] + 2) == 0
        assert simplify(profile["obstruction_g2"]["e"] + 2 * t**2) == 0
        assert simplify(profile["obstruction_g2"]["h"] - t**2) == 0
        assert simplify(profile["obstruction_g2"]["f"] + 2 * t**2) == 0
        assert simplify(profile["obstruction_g3"]["eta"] + 2 * t**3) == 0

    def test_sl3_scaling_profile(self):
        profile = shifted_seed_eta_channel_scaling_profile(
            build_mc2_sl3_shifted_cyclic_linf_l3_seed(),
            basis_elements=("e1", "e2", "f12"),
            alpha_basis=("e1", "e2", "f12"),
        )
        t = profile["parameter"]
        assert simplify(profile["eta_residual_at_111"] - 1) == 0
        assert simplify(profile["obstruction_g2"]["e12"] - t**2) == 0
        assert simplify(profile["obstruction_g2"]["f1"] - t**2) == 0
        assert simplify(profile["obstruction_g2"]["f2"] + t**2) == 0
        assert simplify(profile["obstruction_g3"]["eta"] - t**3) == 0

    def test_sp4_scaling_profile(self):
        profile = shifted_seed_eta_channel_scaling_profile(
            build_mc2_sp4_shifted_cyclic_linf_l3_seed(),
            basis_elements=("e1", "e2", "f12"),
            alpha_basis=("e1", "e2", "f12"),
        )
        t = profile["parameter"]
        assert simplify(profile["eta_residual_at_111"] - 2) == 0
        assert simplify(profile["obstruction_g2"]["e12"] - t**2) == 0
        assert simplify(profile["obstruction_g2"]["f1"] - t**2) == 0
        assert simplify(profile["obstruction_g2"]["f2"] + 2 * t**2) == 0
        assert simplify(profile["obstruction_g3"]["eta"] - 2 * t**3) == 0

    def test_verify_shifted_eta_scaling_bundle(self):
        checks = verify_mc2_shifted_seed_eta_scaling_law()
        assert all(checks.values()), checks


class TestMC2ShiftedObstructionPolynomialLaw:
    def test_sl2_polynomial_profile_identities(self):
        profile = shifted_seed_obstruction_polynomial_profile(
            build_mc2_sl2_shifted_cyclic_linf_l3_seed(),
            basis_elements=("e", "h", "f"),
        )
        x, y, z = profile["parameters"]
        assert simplify(profile["eta_residual"] + 2 * x * y * z) == 0
        assert profile["obstruction_g2"] == profile["half_l2_alpha1_alpha1"]
        assert profile["obstruction_g3"] == profile["one_sixth_l3_alpha1_alpha1_alpha1"]
        assert simplify(profile["obstruction_g3"]["eta"] - profile["eta_residual"]) == 0

    def test_sl3_polynomial_profile_identities(self):
        profile = shifted_seed_obstruction_polynomial_profile(
            build_mc2_sl3_shifted_cyclic_linf_l3_seed(),
            basis_elements=("e1", "e2", "f12"),
        )
        x, y, z = profile["parameters"]
        assert simplify(profile["eta_residual"] - x * y * z) == 0
        assert profile["obstruction_g2"] == profile["half_l2_alpha1_alpha1"]
        assert profile["obstruction_g3"] == profile["one_sixth_l3_alpha1_alpha1_alpha1"]
        assert simplify(profile["obstruction_g3"]["eta"] - profile["eta_residual"]) == 0

    def test_sp4_polynomial_profile_identities(self):
        profile = shifted_seed_obstruction_polynomial_profile(
            build_mc2_sp4_shifted_cyclic_linf_l3_seed(),
            basis_elements=("e1", "e2", "f12"),
        )
        x, y, z = profile["parameters"]
        assert simplify(profile["eta_residual"] - 2 * x * y * z) == 0
        assert profile["obstruction_g2"] == profile["half_l2_alpha1_alpha1"]
        assert profile["obstruction_g3"] == profile["one_sixth_l3_alpha1_alpha1_alpha1"]
        assert simplify(profile["obstruction_g3"]["eta"] - profile["eta_residual"]) == 0

    def test_verify_shifted_obstruction_polynomial_bundle(self):
        checks = verify_mc2_shifted_seed_obstruction_polynomial_law()
        assert all(checks.values()), checks


class TestMC2SeedTransferLayer:
    """Generic seed transfer: generator-level l_2/pairing -> first l_3 channel."""

    def test_sl2_generic_l3_lift_matches_specialized_seed(self):
        base = build_mc2_sl2_cyclic_linf_seed()
        lifted = build_cyclic_l3_marker_extension_from_seed(base)
        specialized = build_mc2_sl2_cyclic_linf_l3_seed()
        assert lifted.l3_table == specialized.l3_table
        assert lifted.basis == specialized.basis
        assert lifted.degrees == specialized.degrees

    def test_sl2_seed_ce_profile_has_unique_h2_direction(self):
        profile = cyclic_ce_profile_from_cyclic_seed(build_mc2_sl2_cyclic_linf_seed())
        assert profile["dims"][0] == 0
        assert profile["dims"][1] == 0
        assert profile["dims"][2] == 1
        assert profile["dims"][3] == 0
        assert profile["killing_3form_value"] != 0


class TestMC2CompletionClutching:
    def test_completed_tensor_surrogate(self):
        left = {0: {"theta": Rational(1)}, 1: {"theta": Rational(2)}}
        right = {0: {"theta": Rational(3)}, 1: {"theta": Rational(5)}}
        tensor_series = completed_tensor_product_surrogate(left, right, max_genus=2)
        assert tensor_series[0] == {("theta", "theta"): Rational(3)}
        assert tensor_series[1] == {("theta", "theta"): Rational(11)}
        assert tensor_series[2] == {("theta", "theta"): Rational(10)}

    def test_boundary_clutching_via_l2(self):
        model = build_mc2_cyclic_linf_model()
        left = {0: {"theta": Rational(1)}, 1: {"theta": Rational(2)}}
        right = {0: {"theta": Rational(3)}, 1: {"theta": Rational(5)}}
        boundary = boundary_clutching_series_via_l2(model, left, right, max_genus=2)
        assert boundary[0] == {"omega": Rational(6)}
        assert boundary[1] == {"omega": Rational(22)}
        assert boundary[2] == {"omega": Rational(20)}

    def test_verify_boundary_clutching(self):
        model = build_mc2_cyclic_linf_model()
        left = {0: {"theta": Rational(1)}, 1: {"theta": Rational(2)}}
        right = {0: {"theta": Rational(3)}, 1: {"theta": Rational(5)}}
        expected = {
            0: {"omega": Rational(6)},
            1: {"omega": Rational(22)},
            2: {"omega": Rational(20)},
        }
        assert verify_boundary_clutching_compatibility(
            model=model,
            boundary_series=expected,
            left=left,
            right=right,
            max_genus=2,
        )
        broken = dict(expected)
        broken[2] = {"omega": Rational(21)}
        assert not verify_boundary_clutching_compatibility(
            model=model,
            boundary_series=broken,
            left=left,
            right=right,
            max_genus=2,
        )

    def test_completed_mc_residual(self):
        model = build_mc2_cyclic_linf_model()
        alpha = {0: {"theta": Rational(1)}, 1: {"theta": Rational(1)}}
        residual = mc_residual_completed_truncated(model, alpha_series=alpha, max_genus=2)
        assert 0 not in residual
        assert residual[1] == {"omega": Rational(-1)}
        assert residual[2] == {"omega": Rational(-2)}

    def test_completed_pairing_series(self):
        model = build_mc2_cyclic_linf_model()
        left = {0: {"theta": Rational(1)}, 1: {"theta": Rational(1)}}
        right = {0: {"omega": Rational(1)}, 1: {"omega": Rational(2)}}
        paired = completed_pairing_series(model, left, right, max_genus=2)
        assert paired[0] == Rational(1)
        assert paired[1] == Rational(3)
        assert paired[2] == Rational(2)

    def test_completed_cyclic_l2(self):
        model = build_mc2_cyclic_linf_model()
        u = {0: {"theta": Rational(1)}, 1: {"theta": Rational(2)}}
        v = {0: {"theta": Rational(3)}, 1: {"theta": Rational(5)}}
        w = {0: {"theta": Rational(7)}}
        assert verify_completed_cyclic_l2(model, u, v, w, max_genus=2)

    def test_completed_cyclic_l3(self):
        model = build_mc2_cyclic_linf_model()
        u = {0: {"theta": Rational(1)}, 1: {"theta": Rational(2)}}
        v = {0: {"theta": Rational(3)}, 1: {"theta": Rational(5)}}
        w = {0: {"theta": Rational(7)}}
        x = {0: {"theta": Rational(11)}}
        assert verify_completed_cyclic_l3(model, u, v, w, x, max_genus=2)

    def test_completed_mc_solver_branch_a0_eq_1(self):
        model = build_mc2_cyclic_linf_model()
        solved = solve_completed_mc_single_basis_truncated(
            model,
            basis_element="theta",
            max_genus=2,
            fixed_coefficients={0: Rational(1)},
        )
        assert len(solved["solutions"]) >= 1
        free = solved["free_parameters"]
        assert len(free) == 2
        for sol in solved["solutions"]:
            assert simplify(sol[free[0]]) == 0
            assert simplify(sol[free[1]]) == 0

    def test_completed_mc_inconsistent_branch_detected(self):
        model = build_mc2_cyclic_linf_model()
        solved = solve_completed_mc_single_basis_truncated(
            model,
            basis_element="theta",
            max_genus=2,
            fixed_coefficients={0: Rational(2)},
        )
        assert solved["solutions"] == []

    def test_completed_mc_recursive_solver_branch_a0_eq_1(self):
        model = build_mc2_cyclic_linf_model()
        solved = solve_completed_mc_single_basis_recursive(
            model,
            basis_element="theta",
            max_genus=4,
            fixed_coefficients={0: Rational(1)},
        )
        assert solved["branch_count"] == 1
        branch = solved["branches"][0]
        assert simplify(branch[0] - 1) == 0
        assert simplify(branch[1]) == 0
        assert simplify(branch[2]) == 0
        assert simplify(branch[3]) == 0
        assert simplify(branch[4]) == 0

    def test_completed_mc_multi_basis_solver_theta_a0_eq_1(self):
        model = build_mc2_cyclic_linf_model()
        solved = solve_completed_mc_basis_family_truncated(
            model,
            basis_elements=("theta", "omega"),
            max_genus=1,
            fixed_coefficients={(0, "theta"): Rational(1)},
        )
        assert len(solved["solutions"]) >= 1
        theta_g1 = solved["parameter_by_slot"][(1, "theta")]
        omega_g0 = solved["parameter_by_slot"][(0, "omega")]
        omega_g1 = solved["parameter_by_slot"][(1, "omega")]
        for sol in solved["solutions"]:
            assert simplify(sol[theta_g1]) == 0
            assert simplify(sol[omega_g0] - omega_g0) == 0
            assert simplify(sol[omega_g1] - omega_g1) == 0

    def test_completed_mc_multi_basis_solver_genus0_branch_split(self):
        model = build_mc2_cyclic_linf_model()
        solved = solve_completed_mc_basis_family_truncated(
            model,
            basis_elements=("theta", "omega"),
            max_genus=0,
        )
        theta_g0 = solved["parameter_by_slot"][(0, "theta")]
        roots = {simplify(sol[theta_g0]) for sol in solved["solutions"]}
        assert roots == {Rational(0), Rational(1)}

    def test_completed_mc_multi_basis_inconsistent_theta_a0_eq_2(self):
        model = build_mc2_cyclic_linf_model()
        solved = solve_completed_mc_basis_family_truncated(
            model,
            basis_elements=("theta", "omega"),
            max_genus=1,
            fixed_coefficients={(0, "theta"): Rational(2)},
        )
        assert solved["solutions"] == []

    def test_completed_mc_multi_basis_recursive_theta_a0_eq_1(self):
        model = build_mc2_cyclic_linf_model()
        solved = solve_completed_mc_basis_family_recursive(
            model,
            basis_elements=("theta", "omega"),
            max_genus=3,
            fixed_coefficients={(0, "theta"): Rational(1)},
        )
        assert solved["branch_count"] == 1
        branch = solved["branches_by_slot"][0]
        assert simplify(branch[(0, "theta")] - 1) == 0
        assert simplify(branch[(1, "theta")]) == 0
        assert simplify(branch[(2, "theta")]) == 0
        assert simplify(branch[(3, "theta")]) == 0
        for genus in range(4):
            omega_coeff = simplify(branch[(genus, "omega")])
            assert omega_coeff.free_symbols

    def test_genus_stratified_obstruction_identity(self):
        model = build_mc2_cyclic_linf_model()
        alpha = {
            1: {"theta": Rational(1)},
            2: {"theta": Rational(1)},
            3: {"theta": Rational(2)},
        }
        assert verify_genus_stratified_obstruction_identity(
            model=model,
            alpha_series=alpha,
            max_genus=3,
        )
        obstruction_g3 = completed_mc_obstruction_term_at_genus(
            model=model,
            alpha_series=alpha,
            genus=3,
            require_zero_genus=True,
        )
        assert obstruction_g3 == {"omega": Rational(1)}

    def test_genus_stratified_obstruction_requires_zero_genus(self):
        model = build_mc2_cyclic_linf_model()
        bad_alpha = {0: {"theta": Rational(1)}, 1: {"theta": Rational(1)}}
        assert not verify_genus_stratified_obstruction_identity(
            model=model,
            alpha_series=bad_alpha,
            max_genus=1,
        )

    def test_verify_completion_clutching_bundle(self):
        checks = verify_mc2_completion_clutching_scaffold()
        assert all(checks.values()), checks


# ===================================================================
# MC2 Step 3: Kappa extraction from cyclic L-infinity seed
# ===================================================================

from sympy import Matrix, Symbol, eye

from compute.lib.mc2_cyclic_linf import (
    adjoint_casimir_matrix,
    adjoint_casimir_eigenvalue,
    dual_coxeter_from_seed,
    kappa_from_seed,
    kappa_two_channel,
    verify_linf_arity4_identity,
    verify_cyclic_l2_full,
    verify_cyclic_l3_full,
    verify_mc2_kappa_extraction,
    verify_mc2_linf_identities,
)


class TestMC2AdjointCasimir:
    """Verify the adjoint Casimir operator from the sl_2 seed."""

    def test_casimir_matrix_is_3x3(self):
        model = build_mc2_sl2_cyclic_linf_seed()
        mat = adjoint_casimir_matrix(model)
        assert mat.shape == (3, 3)

    def test_casimir_is_scalar_multiple_of_identity(self):
        model = build_mc2_sl2_cyclic_linf_seed()
        mat = adjoint_casimir_matrix(model)
        eigenval = simplify(mat[0, 0])
        assert simplify(mat - eigenval * eye(3)) == Matrix.zeros(3, 3)

    def test_casimir_eigenvalue_is_4(self):
        """C_2 on adjoint sl_2 = 2*h^vee * id = 4 * id."""
        model = build_mc2_sl2_cyclic_linf_seed()
        eigenval = adjoint_casimir_eigenvalue(model)
        assert simplify(eigenval - 4) == 0

    def test_casimir_on_each_generator(self):
        """C_2(e) = 4e, C_2(h) = 4h, C_2(f) = 4f."""
        model = build_mc2_sl2_cyclic_linf_seed()
        mat = adjoint_casimir_matrix(model)
        # Column 0 = C_2(e), column 1 = C_2(h), column 2 = C_2(f)
        assert simplify(mat[0, 0] - 4) == 0  # C_2(e) has coefficient 4 on e
        assert simplify(mat[1, 0]) == 0       # no h component
        assert simplify(mat[2, 0]) == 0       # no f component
        assert simplify(mat[1, 1] - 4) == 0   # C_2(h) = 4h
        assert simplify(mat[2, 2] - 4) == 0   # C_2(f) = 4f


class TestMC2DualCoxeterExtraction:
    """Verify h^vee extraction from the cyclic seed."""

    def test_h_dual_equals_2(self):
        model = build_mc2_sl2_cyclic_linf_seed()
        h_dual = dual_coxeter_from_seed(model)
        assert simplify(h_dual - 2) == 0

    def test_h_dual_from_casimir(self):
        """h^vee = C_2_eigenvalue / 2."""
        model = build_mc2_sl2_cyclic_linf_seed()
        eigenval = adjoint_casimir_eigenvalue(model)
        h_dual = dual_coxeter_from_seed(model)
        assert simplify(eigenval - 2 * h_dual) == 0


class TestMC2KappaExtraction:
    """Core MC2 Step-3 test: kappa from L-infinity seed matches manuscript."""

    def test_kappa_symbolic(self):
        """kappa = 3(k+2)/4 for sl_2 at level k."""
        k = Symbol("k")
        model = build_mc2_sl2_cyclic_linf_seed()
        kappa = kappa_from_seed(model, level=k)
        expected = Rational(3) * (k + 2) / 4
        assert simplify(kappa - expected) == 0

    def test_kappa_at_k_1(self):
        """kappa(sl_2, k=1) = 3*3/4 = 9/4."""
        model = build_mc2_sl2_cyclic_linf_seed()
        kappa = kappa_from_seed(model, level=1)
        assert simplify(kappa - Rational(9, 4)) == 0

    def test_kappa_at_critical_level(self):
        """kappa(sl_2, k=-h^vee=-2) = 0 (critical level)."""
        model = build_mc2_sl2_cyclic_linf_seed()
        kappa = kappa_from_seed(model, level=-2)
        assert simplify(kappa) == 0

    def test_kappa_complementarity(self):
        """kappa(k) + kappa(-k-4) = 0 (Feigin-Frenkel involution)."""
        k = Symbol("k")
        model = build_mc2_sl2_cyclic_linf_seed()
        kappa_k = kappa_from_seed(model, level=k)
        kappa_dual = kappa_from_seed(model, level=-k - 4)
        assert simplify(kappa_k + kappa_dual) == 0

    def test_two_channel_decomposition(self):
        """Verify the double-pole and simple-pole channels."""
        k = Symbol("k")
        model = build_mc2_sl2_cyclic_linf_seed()
        channels = kappa_two_channel(model, level=k)
        # Double pole: 3k/4
        assert simplify(channels["double_pole"] - 3 * k / 4) == 0
        # Simple pole: 3/2
        assert simplify(channels["simple_pole"] - Rational(3, 2)) == 0
        # Total = double + simple
        assert simplify(channels["total"] - channels["double_pole"] - channels["simple_pole"]) == 0

    def test_two_channel_sum_matches_kappa(self):
        k = Symbol("k")
        model = build_mc2_sl2_cyclic_linf_seed()
        kappa = kappa_from_seed(model, level=k)
        channels = kappa_two_channel(model, level=k)
        assert simplify(kappa - channels["total"]) == 0

    def test_verify_kappa_extraction_bundle(self):
        """Run the full kappa extraction verification bundle."""
        checks = verify_mc2_kappa_extraction()
        assert checks["casimir_is_scalar"]
        assert checks["casimir_equals_2h_dual"]
        assert checks["h_dual_equals_2"]
        assert checks["kappa_matches_formula"]
        assert checks["double_pole_matches"]
        assert checks["simple_pole_matches"]
        assert checks["complementarity_zero"]
        assert checks["critical_level_zero"]


class TestMC2LinfArity4:
    """Verify the L-infinity arity-4 homotopy Jacobi identity."""

    def test_arity4_on_l3_seed(self):
        model = build_mc2_sl2_cyclic_linf_l3_seed()
        assert verify_linf_arity4_identity(model)

    def test_arity4_on_generator_seed(self):
        """On the seed without l_3, the identity reduces to Jacobi for l_2."""
        model = build_mc2_sl2_cyclic_linf_seed()
        assert verify_linf_arity4_identity(model)


class TestMC2CyclicSymmetry:
    """Verify full cyclic symmetry of l_2 and l_3."""

    def test_cyclic_l2_on_generator_seed(self):
        model = build_mc2_sl2_cyclic_linf_seed()
        assert verify_cyclic_l2_full(model)

    def test_cyclic_l2_on_l3_seed(self):
        model = build_mc2_sl2_cyclic_linf_l3_seed()
        assert verify_cyclic_l2_full(model)

    def test_cyclic_l3_on_l3_seed(self):
        model = build_mc2_sl2_cyclic_linf_l3_seed()
        assert verify_cyclic_l3_full(model)

    def test_verify_linf_identities_bundle(self):
        checks = verify_mc2_linf_identities()
        assert all(checks.values()), checks


# ===================================================================
# MC2 sl_3 extension: rank-2 universality
# ===================================================================

from compute.lib.mc2_cyclic_linf import (
    build_mc2_sl3_coderivation_seed,
    build_mc2_sl3_cyclic_linf_seed,
    build_mc2_sl3_cyclic_linf_l3_seed,
    verify_mc2_sl3_seed,
    verify_mc2_sl3_kappa_extraction,
)


class TestMC2Sl3Seed:
    """Verify the sl_3 cyclic L-infinity seed structural properties."""

    def test_dg_lie_identities(self):
        model = build_mc2_sl3_coderivation_seed()
        assert model.verify_d_squared_zero()
        assert model.verify_jacobi_identity()
        assert model.verify_d_leibniz()

    def test_expected_brackets(self):
        model = build_mc2_sl3_coderivation_seed()
        assert model.bracket_basis("e1", "f1") == {"h1": Rational(1)}
        assert model.bracket_basis("e2", "f2") == {"h2": Rational(1)}
        assert model.bracket_basis("e1", "e2") == {"e12": Rational(1)}
        assert model.bracket_basis("h1", "e1") == {"e1": Rational(2)}
        assert model.bracket_basis("h1", "e2") == {"e2": Rational(-1)}
        assert model.bracket_basis("f1", "f2") == {"f12": Rational(-1)}

    def test_cartan_brackets(self):
        """[h1, h2] = 0 (Cartan subalgebra is abelian)."""
        model = build_mc2_sl3_coderivation_seed()
        assert model.bracket_basis("h1", "h2") == {}

    def test_normalized_pairing(self):
        model = build_mc2_sl3_cyclic_linf_seed()
        assert simplify(model.pairing_basis("e1", "f1") - 1) == 0
        assert simplify(model.pairing_basis("e2", "f2") - 1) == 0
        assert simplify(model.pairing_basis("e12", "f12") - 1) == 0
        assert simplify(model.pairing_basis("h1", "h1") - 2) == 0
        assert simplify(model.pairing_basis("h2", "h2") - 2) == 0
        assert simplify(model.pairing_basis("h1", "h2") + 1) == 0

    def test_verify_sl3_seed_bundle(self):
        checks = verify_mc2_sl3_seed()
        assert all(checks.values()), checks


class TestMC2Sl3AdjointCasimir:
    """Verify the adjoint Casimir operator from the sl_3 seed."""

    def test_casimir_matrix_is_8x8(self):
        model = build_mc2_sl3_cyclic_linf_seed()
        mat = adjoint_casimir_matrix(model)
        assert mat.shape == (8, 8)

    def test_casimir_is_scalar_multiple_of_identity(self):
        model = build_mc2_sl3_cyclic_linf_seed()
        mat = adjoint_casimir_matrix(model)
        eigenval = simplify(mat[0, 0])
        assert simplify(mat - eigenval * eye(8)) == Matrix.zeros(8, 8)

    def test_casimir_eigenvalue_is_6(self):
        """C_2 on adjoint sl_3 = 2*h^vee * id = 6 * id."""
        model = build_mc2_sl3_cyclic_linf_seed()
        eigenval = adjoint_casimir_eigenvalue(model)
        assert simplify(eigenval - 6) == 0


class TestMC2Sl3DualCoxeterExtraction:
    """Verify h^vee extraction from the sl_3 cyclic seed."""

    def test_h_dual_equals_3(self):
        model = build_mc2_sl3_cyclic_linf_seed()
        h_dual = dual_coxeter_from_seed(model)
        assert simplify(h_dual - 3) == 0


class TestMC2Sl3KappaExtraction:
    """Core universality test: kappa from sl_3 L-infinity seed matches formula."""

    def test_kappa_symbolic(self):
        """kappa = 4(k+3)/3 for sl_3 at level k."""
        k = Symbol("k")
        model = build_mc2_sl3_cyclic_linf_seed()
        kappa = kappa_from_seed(model, level=k)
        expected = Rational(4) * (k + 3) / 3
        assert simplify(kappa - expected) == 0

    def test_kappa_at_k_1(self):
        """kappa(sl_3, k=1) = 4*4/3 = 16/3."""
        model = build_mc2_sl3_cyclic_linf_seed()
        kappa = kappa_from_seed(model, level=1)
        assert simplify(kappa - Rational(16, 3)) == 0

    def test_kappa_at_critical_level(self):
        """kappa(sl_3, k=-h^vee=-3) = 0 (critical level)."""
        model = build_mc2_sl3_cyclic_linf_seed()
        kappa = kappa_from_seed(model, level=-3)
        assert simplify(kappa) == 0

    def test_kappa_complementarity(self):
        """kappa(k) + kappa(-k-6) = 0 (Feigin-Frenkel involution for sl_3)."""
        k = Symbol("k")
        model = build_mc2_sl3_cyclic_linf_seed()
        kappa_k = kappa_from_seed(model, level=k)
        kappa_dual = kappa_from_seed(model, level=-k - 6)
        assert simplify(kappa_k + kappa_dual) == 0

    def test_two_channel_decomposition(self):
        """Verify the double-pole and simple-pole channels for sl_3."""
        k = Symbol("k")
        model = build_mc2_sl3_cyclic_linf_seed()
        channels = kappa_two_channel(model, level=k)
        # Double pole: 4k/3
        assert simplify(channels["double_pole"] - 4 * k / 3) == 0
        # Simple pole: 4
        assert simplify(channels["simple_pole"] - 4) == 0
        # Total = double + simple
        assert simplify(channels["total"] - channels["double_pole"] - channels["simple_pole"]) == 0

    def test_two_channel_sum_matches_kappa(self):
        k = Symbol("k")
        model = build_mc2_sl3_cyclic_linf_seed()
        kappa = kappa_from_seed(model, level=k)
        channels = kappa_two_channel(model, level=k)
        assert simplify(kappa - channels["total"]) == 0

    def test_verify_sl3_kappa_extraction_bundle(self):
        """Run the full sl_3 kappa extraction verification bundle."""
        checks = verify_mc2_sl3_kappa_extraction()
        assert checks["casimir_is_scalar"]
        assert checks["casimir_equals_2h_dual"]
        assert checks["h_dual_equals_3"]
        assert checks["kappa_matches_formula"]
        assert checks["double_pole_matches"]
        assert checks["simple_pole_matches"]
        assert checks["complementarity_zero"]
        assert checks["critical_level_zero"]


class TestMC2Sl3LinfIdentities:
    """Verify L-infinity structural identities for the sl_3 seed."""

    def test_cyclic_l2_on_generator_seed(self):
        model = build_mc2_sl3_cyclic_linf_seed()
        assert verify_cyclic_l2_full(model)

    def test_cyclic_l2_on_l3_seed(self):
        model = build_mc2_sl3_cyclic_linf_l3_seed()
        assert verify_cyclic_l2_full(model)

    def test_cyclic_l3_on_l3_seed(self):
        model = build_mc2_sl3_cyclic_linf_l3_seed()
        assert verify_cyclic_l3_full(model)

    def test_arity4_on_l3_seed(self):
        model = build_mc2_sl3_cyclic_linf_l3_seed()
        assert verify_linf_arity4_identity(model)

    def test_arity4_on_generator_seed(self):
        model = build_mc2_sl3_cyclic_linf_seed()
        assert verify_linf_arity4_identity(model)


class TestMC2Sl3L3Seed:
    """Verify the sl_3 l_3 Killing cocycle seed."""

    def test_generic_l3_lift_matches_specialized_seed(self):
        base = build_mc2_sl3_cyclic_linf_seed()
        lifted = build_cyclic_l3_marker_extension_from_seed(base)
        specialized = build_mc2_sl3_cyclic_linf_l3_seed()
        assert lifted.l3_table == specialized.l3_table
        assert lifted.basis == specialized.basis
        assert lifted.degrees == specialized.degrees

    def test_l3_channel_is_nontrivial(self):
        model = build_mc2_sl3_cyclic_linf_l3_seed()
        # phi(e1, e2, f12) = kap([e1,e2], f12) = kap(e12, f12) = 1
        assert model.l3_basis("e1", "e2", "f12").get("eta", 0) != 0

    def test_l3_killing_cocycle_value(self):
        """phi(e1, e2, f12) = 1 (from kap(e12, f12) = 1)."""
        model = build_mc2_sl3_cyclic_linf_l3_seed()
        assert simplify(model.l3_basis("e1", "e2", "f12").get("eta", 0) - 1) == 0

    def test_l3_antisymmetry_sample(self):
        """phi(a,b,c) = -phi(b,a,c) on sample triples."""
        model = build_mc2_sl3_cyclic_linf_l3_seed()
        for a, b, c in [("e1", "e2", "f12"), ("h1", "e1", "f1"), ("e1", "f1", "h1")]:
            abc = simplify(model.l3_basis(a, b, c).get("eta", 0))
            bac = simplify(model.l3_basis(b, a, c).get("eta", 0))
            assert simplify(abc + bac) == 0


class TestMC2KappaUniversality:
    """Cross-rank universality: the kappa formula works for both sl_2 and sl_3."""

    def test_kappa_formula_matches_across_ranks(self):
        """kappa = dim(g) * (k + h^vee) / (2 * h^vee) for both algebras."""
        k = Symbol("k")

        model_sl2 = build_mc2_sl2_cyclic_linf_seed()
        kappa_sl2 = kappa_from_seed(model_sl2, level=k)
        expected_sl2 = Rational(3) * (k + 2) / 4
        assert simplify(kappa_sl2 - expected_sl2) == 0

        model_sl3 = build_mc2_sl3_cyclic_linf_seed()
        kappa_sl3 = kappa_from_seed(model_sl3, level=k)
        expected_sl3 = Rational(4) * (k + 3) / 3
        assert simplify(kappa_sl3 - expected_sl3) == 0

    def test_simple_pole_is_half_dim(self):
        """Simple-pole channel = dim(g)/2 for both algebras."""
        k = Symbol("k")

        ch_sl2 = kappa_two_channel(build_mc2_sl2_cyclic_linf_seed(), level=k)
        assert simplify(ch_sl2["simple_pole"] - Rational(3, 2)) == 0

        ch_sl3 = kappa_two_channel(build_mc2_sl3_cyclic_linf_seed(), level=k)
        assert simplify(ch_sl3["simple_pole"] - 4) == 0

    def test_critical_level_universally_zero(self):
        """kappa(-h^vee) = 0 for both algebras."""
        assert simplify(kappa_from_seed(build_mc2_sl2_cyclic_linf_seed(), level=-2)) == 0
        assert simplify(kappa_from_seed(build_mc2_sl3_cyclic_linf_seed(), level=-3)) == 0


# ===================================================================
# MC2 sp_4 extension: non-simply-laced universality
# ===================================================================

from compute.lib.mc2_cyclic_linf import (
    build_mc2_sp4_coderivation_seed,
    build_mc2_sp4_cyclic_linf_seed,
    build_mc2_sp4_cyclic_linf_l3_seed,
    verify_mc2_sp4_seed,
    verify_mc2_sp4_kappa_extraction,
)


class TestMC2Sp4Seed:
    """Verify the sp_4 cyclic L-infinity seed structural properties."""

    def test_dg_lie_identities(self):
        model = build_mc2_sp4_coderivation_seed()
        assert model.verify_d_squared_zero()
        assert model.verify_jacobi_identity()
        assert model.verify_d_leibniz()

    def test_expected_brackets(self):
        model = build_mc2_sp4_coderivation_seed()
        assert model.bracket_basis("e1", "f1") == {"h1": Rational(1)}
        assert model.bracket_basis("e2", "f2") == {"h2": Rational(1)}
        assert model.bracket_basis("e1", "e2") == {"e12": Rational(1)}
        assert model.bracket_basis("e1", "e12") == {"e22": Rational(2)}
        assert model.bracket_basis("h1", "e1") == {"e1": Rational(2)}
        assert model.bracket_basis("h1", "e2") == {"e2": Rational(-2)}
        assert model.bracket_basis("f1", "f2") == {"f12": Rational(-1)}

    def test_cartan_brackets(self):
        """[h1, h2] = 0 (Cartan subalgebra is abelian)."""
        model = build_mc2_sp4_coderivation_seed()
        assert model.bracket_basis("h1", "h2") == {}

    def test_non_simply_laced_pairing(self):
        """Short roots pair to 2, long roots pair to 1."""
        model = build_mc2_sp4_cyclic_linf_seed()
        # Short roots
        assert simplify(model.pairing_basis("e1", "f1") - 2) == 0
        assert simplify(model.pairing_basis("e12", "f12") - 2) == 0
        # Long roots
        assert simplify(model.pairing_basis("e2", "f2") - 1) == 0
        assert simplify(model.pairing_basis("e22", "f22") - 1) == 0
        # Cartan
        assert simplify(model.pairing_basis("h1", "h1") - 4) == 0
        assert simplify(model.pairing_basis("h1", "h2") + 2) == 0
        assert simplify(model.pairing_basis("h2", "h2") - 2) == 0

    def test_verify_sp4_seed_bundle(self):
        checks = verify_mc2_sp4_seed()
        assert all(checks.values()), checks


class TestMC2Sp4AdjointCasimir:
    """Verify the adjoint Casimir operator from the sp_4 seed."""

    def test_casimir_matrix_is_10x10(self):
        model = build_mc2_sp4_cyclic_linf_seed()
        mat = adjoint_casimir_matrix(model)
        assert mat.shape == (10, 10)

    def test_casimir_is_scalar_multiple_of_identity(self):
        model = build_mc2_sp4_cyclic_linf_seed()
        mat = adjoint_casimir_matrix(model)
        eigenval = simplify(mat[0, 0])
        assert simplify(mat - eigenval * eye(10)) == Matrix.zeros(10, 10)

    def test_casimir_eigenvalue_is_6(self):
        """C_2 on adjoint sp_4 = 2*h^vee * id = 6 * id."""
        model = build_mc2_sp4_cyclic_linf_seed()
        eigenval = adjoint_casimir_eigenvalue(model)
        assert simplify(eigenval - 6) == 0


class TestMC2Sp4DualCoxeterExtraction:
    """Verify h^vee extraction from the sp_4 cyclic seed."""

    def test_h_dual_equals_3(self):
        """h^vee(sp_4) = 3 (NOT h = 4, the Coxeter number)."""
        model = build_mc2_sp4_cyclic_linf_seed()
        h_dual = dual_coxeter_from_seed(model)
        assert simplify(h_dual - 3) == 0


class TestMC2Sp4KappaExtraction:
    """Core non-simply-laced universality test: kappa from sp_4 seed."""

    def test_kappa_symbolic(self):
        """kappa = 5(k+3)/3 for sp_4 at level k."""
        k = Symbol("k")
        model = build_mc2_sp4_cyclic_linf_seed()
        kappa = kappa_from_seed(model, level=k)
        expected = Rational(5) * (k + 3) / 3
        assert simplify(kappa - expected) == 0

    def test_kappa_at_k_1(self):
        """kappa(sp_4, k=1) = 5*4/3 = 20/3."""
        model = build_mc2_sp4_cyclic_linf_seed()
        kappa = kappa_from_seed(model, level=1)
        assert simplify(kappa - Rational(20, 3)) == 0

    def test_kappa_at_critical_level(self):
        """kappa(sp_4, k=-h^vee=-3) = 0 (critical level)."""
        model = build_mc2_sp4_cyclic_linf_seed()
        kappa = kappa_from_seed(model, level=-3)
        assert simplify(kappa) == 0

    def test_kappa_complementarity(self):
        """kappa(k) + kappa(-k-6) = 0 (Feigin-Frenkel involution for sp_4)."""
        k = Symbol("k")
        model = build_mc2_sp4_cyclic_linf_seed()
        kappa_k = kappa_from_seed(model, level=k)
        kappa_dual = kappa_from_seed(model, level=-k - 6)
        assert simplify(kappa_k + kappa_dual) == 0

    def test_two_channel_decomposition(self):
        """Verify the double-pole and simple-pole channels for sp_4."""
        k = Symbol("k")
        model = build_mc2_sp4_cyclic_linf_seed()
        channels = kappa_two_channel(model, level=k)
        # Double pole: 5k/3
        assert simplify(channels["double_pole"] - 5 * k / 3) == 0
        # Simple pole: 5
        assert simplify(channels["simple_pole"] - 5) == 0
        # Total = double + simple
        assert simplify(channels["total"] - channels["double_pole"] - channels["simple_pole"]) == 0

    def test_two_channel_sum_matches_kappa(self):
        k = Symbol("k")
        model = build_mc2_sp4_cyclic_linf_seed()
        kappa = kappa_from_seed(model, level=k)
        channels = kappa_two_channel(model, level=k)
        assert simplify(kappa - channels["total"]) == 0

    def test_verify_sp4_kappa_extraction_bundle(self):
        """Run the full sp_4 kappa extraction verification bundle."""
        checks = verify_mc2_sp4_kappa_extraction()
        assert checks["casimir_is_scalar"]
        assert checks["casimir_equals_2h_dual"]
        assert checks["h_dual_equals_3"]
        assert checks["kappa_matches_formula"]
        assert checks["double_pole_matches"]
        assert checks["simple_pole_matches"]
        assert checks["complementarity_zero"]
        assert checks["critical_level_zero"]


class TestMC2Sp4LinfIdentities:
    """Verify L-infinity structural identities for the sp_4 seed."""

    def test_cyclic_l2_on_generator_seed(self):
        model = build_mc2_sp4_cyclic_linf_seed()
        assert verify_cyclic_l2_full(model)

    def test_cyclic_l2_on_l3_seed(self):
        model = build_mc2_sp4_cyclic_linf_l3_seed()
        assert verify_cyclic_l2_full(model)

    def test_cyclic_l3_on_l3_seed(self):
        model = build_mc2_sp4_cyclic_linf_l3_seed()
        assert verify_cyclic_l3_full(model)

    def test_arity4_on_generator_seed(self):
        model = build_mc2_sp4_cyclic_linf_seed()
        assert verify_linf_arity4_identity(model)


class TestMC2Sp4L3Seed:
    """Verify the sp_4 l_3 Killing cocycle seed."""

    def test_generic_l3_lift_matches_specialized_seed(self):
        base = build_mc2_sp4_cyclic_linf_seed()
        lifted = build_cyclic_l3_marker_extension_from_seed(base)
        specialized = build_mc2_sp4_cyclic_linf_l3_seed()
        assert lifted.l3_table == specialized.l3_table
        assert lifted.basis == specialized.basis
        assert lifted.degrees == specialized.degrees

    def test_l3_channel_is_nontrivial(self):
        model = build_mc2_sp4_cyclic_linf_l3_seed()
        # phi(e1, e2, f12) = kap([e1,e2], f12) = kap(e12, f12) = 2
        assert model.l3_basis("e1", "e2", "f12").get("eta", 0) != 0

    def test_l3_killing_cocycle_value(self):
        """phi(e1, e2, f12) = 2 (non-simply-laced: kap(e12, f12) = 2)."""
        model = build_mc2_sp4_cyclic_linf_l3_seed()
        assert simplify(model.l3_basis("e1", "e2", "f12").get("eta", 0) - 2) == 0

    def test_l3_antisymmetry_sample(self):
        model = build_mc2_sp4_cyclic_linf_l3_seed()
        for a, b, c in [("e1", "e2", "f12"), ("h1", "e1", "f1"), ("e1", "f1", "h1")]:
            abc = simplify(model.l3_basis(a, b, c).get("eta", 0))
            bac = simplify(model.l3_basis(b, a, c).get("eta", 0))
            assert simplify(abc + bac) == 0


class TestMC2KappaTripleUniversality:
    """Cross-rank AND cross-type universality: sl_2, sl_3, sp_4."""

    def test_kappa_formula_matches_all_three(self):
        """kappa = dim(g) * (k + h^vee) / (2 * h^vee) for all three algebras."""
        k = Symbol("k")

        model_sl2 = build_mc2_sl2_cyclic_linf_seed()
        kappa_sl2 = kappa_from_seed(model_sl2, level=k)
        expected_sl2 = Rational(3) * (k + 2) / 4
        assert simplify(kappa_sl2 - expected_sl2) == 0

        model_sl3 = build_mc2_sl3_cyclic_linf_seed()
        kappa_sl3 = kappa_from_seed(model_sl3, level=k)
        expected_sl3 = Rational(4) * (k + 3) / 3
        assert simplify(kappa_sl3 - expected_sl3) == 0

        model_sp4 = build_mc2_sp4_cyclic_linf_seed()
        kappa_sp4 = kappa_from_seed(model_sp4, level=k)
        expected_sp4 = Rational(5) * (k + 3) / 3
        assert simplify(kappa_sp4 - expected_sp4) == 0

    def test_simple_pole_is_half_dim(self):
        """Simple-pole channel = dim(g)/2 for all three algebras."""
        k = Symbol("k")

        ch_sl2 = kappa_two_channel(build_mc2_sl2_cyclic_linf_seed(), level=k)
        assert simplify(ch_sl2["simple_pole"] - Rational(3, 2)) == 0

        ch_sl3 = kappa_two_channel(build_mc2_sl3_cyclic_linf_seed(), level=k)
        assert simplify(ch_sl3["simple_pole"] - 4) == 0

        ch_sp4 = kappa_two_channel(build_mc2_sp4_cyclic_linf_seed(), level=k)
        assert simplify(ch_sp4["simple_pole"] - 5) == 0

    def test_critical_level_universally_zero(self):
        """kappa(-h^vee) = 0 for all three algebras."""
        assert simplify(kappa_from_seed(build_mc2_sl2_cyclic_linf_seed(), level=-2)) == 0
        assert simplify(kappa_from_seed(build_mc2_sl3_cyclic_linf_seed(), level=-3)) == 0
        assert simplify(kappa_from_seed(build_mc2_sp4_cyclic_linf_seed(), level=-3)) == 0

    def test_h_dual_distinguishes_sp4(self):
        """sp_4 has h^vee = 3 (= h^vee for sl_3) but h = 4 != h(sl_3) = 3.
        The kappa formula uses h^vee, not h."""
        model_sp4 = build_mc2_sp4_cyclic_linf_seed()
        model_sl3 = build_mc2_sl3_cyclic_linf_seed()
        h_dual_sp4 = dual_coxeter_from_seed(model_sp4)
        h_dual_sl3 = dual_coxeter_from_seed(model_sl3)
        # Both have h^vee = 3
        assert simplify(h_dual_sp4 - 3) == 0
        assert simplify(h_dual_sl3 - 3) == 0
        # But dim(sp4) = 10 != dim(sl3) = 8, so kappa differs
        k = Symbol("k")
        kappa_sp4 = kappa_from_seed(model_sp4, level=k)
        kappa_sl3 = kappa_from_seed(model_sl3, level=k)
        assert simplify(kappa_sp4 - kappa_sl3) != 0


# ===================================================================
# MC2 G_2 extension: exceptional universality
# ===================================================================

from compute.lib.mc2_cyclic_linf import (
    build_mc2_g2_coderivation_seed,
    build_mc2_g2_cyclic_linf_seed,
    build_mc2_g2_cyclic_linf_l3_seed,
    verify_mc2_g2_seed,
    verify_mc2_g2_kappa_extraction,
)


class TestMC2G2Seed:
    """Verify the G_2 cyclic L-infinity seed structural properties."""

    def test_dg_lie_identities(self):
        model = build_mc2_g2_coderivation_seed()
        assert model.verify_d_squared_zero()
        assert model.verify_jacobi_identity()
        assert model.verify_d_leibniz()

    def test_expected_brackets(self):
        model = build_mc2_g2_coderivation_seed()
        assert model.bracket_basis("e1", "f1") == {"h1": Rational(1)}
        assert model.bracket_basis("e2", "f2") == {"h2": Rational(1)}
        assert model.bracket_basis("e1", "e2") == {"e12": Rational(1)}
        assert model.bracket_basis("e1", "e12") == {"e112": Rational(2)}
        assert model.bracket_basis("e12", "e112") == {"e11122": Rational(-3)}
        assert model.bracket_basis("h1", "e2") == {"e2": Rational(-3)}

    def test_normalized_pairing(self):
        model = build_mc2_g2_cyclic_linf_seed()
        assert simplify(model.pairing_basis("e1", "f1") - 3) == 0
        assert simplify(model.pairing_basis("e2", "f2") - 1) == 0
        assert simplify(model.pairing_basis("e12", "f12") - 3) == 0
        assert simplify(model.pairing_basis("h1", "h1") - 6) == 0
        assert simplify(model.pairing_basis("h1", "h2") + 3) == 0
        assert simplify(model.pairing_basis("h2", "h2") - 2) == 0

    def test_verify_g2_seed_bundle(self):
        checks = verify_mc2_g2_seed()
        assert all(checks.values()), checks


class TestMC2G2AdjointCasimir:
    """Verify the adjoint Casimir operator from the G_2 seed."""

    def test_casimir_matrix_is_14x14(self):
        model = build_mc2_g2_cyclic_linf_seed()
        mat = adjoint_casimir_matrix(model)
        assert mat.shape == (14, 14)

    def test_casimir_is_scalar_multiple_of_identity(self):
        model = build_mc2_g2_cyclic_linf_seed()
        mat = adjoint_casimir_matrix(model)
        eigenval = simplify(mat[0, 0])
        assert simplify(mat - eigenval * eye(14)) == Matrix.zeros(14, 14)

    def test_casimir_eigenvalue_is_8(self):
        model = build_mc2_g2_cyclic_linf_seed()
        eigenval = adjoint_casimir_eigenvalue(model)
        assert simplify(eigenval - 8) == 0


class TestMC2G2DualCoxeterExtraction:
    """Verify h^vee extraction from the G_2 cyclic seed."""

    def test_h_dual_equals_4(self):
        model = build_mc2_g2_cyclic_linf_seed()
        h_dual = dual_coxeter_from_seed(model)
        assert simplify(h_dual - 4) == 0


class TestMC2G2KappaExtraction:
    """Exceptional-rank universality test: kappa from G_2 seed."""

    def test_kappa_symbolic(self):
        k = Symbol("k")
        model = build_mc2_g2_cyclic_linf_seed()
        kappa = kappa_from_seed(model, level=k)
        expected = Rational(7) * (k + 4) / 4
        assert simplify(kappa - expected) == 0

    def test_kappa_at_critical_level(self):
        model = build_mc2_g2_cyclic_linf_seed()
        assert simplify(kappa_from_seed(model, level=-4)) == 0

    def test_kappa_complementarity(self):
        k = Symbol("k")
        model = build_mc2_g2_cyclic_linf_seed()
        kappa_k = kappa_from_seed(model, level=k)
        kappa_dual = kappa_from_seed(model, level=-k - 8)
        assert simplify(kappa_k + kappa_dual) == 0

    def test_two_channel_decomposition(self):
        k = Symbol("k")
        model = build_mc2_g2_cyclic_linf_seed()
        channels = kappa_two_channel(model, level=k)
        assert simplify(channels["double_pole"] - 7 * k / 4) == 0
        assert simplify(channels["simple_pole"] - 7) == 0
        assert simplify(channels["total"] - channels["double_pole"] - channels["simple_pole"]) == 0

    def test_verify_g2_kappa_extraction_bundle(self):
        checks = verify_mc2_g2_kappa_extraction()
        assert checks["casimir_is_scalar"]
        assert checks["casimir_equals_2h_dual"]
        assert checks["h_dual_equals_4"]
        assert checks["kappa_matches_formula"]
        assert checks["double_pole_matches"]
        assert checks["simple_pole_matches"]
        assert checks["complementarity_zero"]
        assert checks["critical_level_zero"]


class TestMC2G2LinfIdentities:
    """Verify L-infinity structural identities for the G_2 seed."""

    def test_cyclic_l2_on_generator_seed(self):
        model = build_mc2_g2_cyclic_linf_seed()
        assert verify_cyclic_l2_full(model)

    def test_cyclic_l2_on_l3_seed(self):
        model = build_mc2_g2_cyclic_linf_l3_seed()
        assert verify_cyclic_l2_full(model)

    def test_cyclic_l3_on_l3_seed(self):
        model = build_mc2_g2_cyclic_linf_l3_seed()
        assert verify_cyclic_l3_full(model)

    def test_arity4_on_l3_seed(self):
        model = build_mc2_g2_cyclic_linf_l3_seed()
        assert verify_linf_arity4_identity(model)


class TestMC2G2L3Seed:
    """Verify the G_2 l_3 Killing cocycle seed."""

    def test_generic_l3_lift_matches_specialized_seed(self):
        base = build_mc2_g2_cyclic_linf_seed()
        lifted = build_cyclic_l3_marker_extension_from_seed(base)
        specialized = build_mc2_g2_cyclic_linf_l3_seed()
        assert lifted.l3_table == specialized.l3_table
        assert lifted.basis == specialized.basis
        assert lifted.degrees == specialized.degrees

    def test_l3_channel_is_nontrivial(self):
        model = build_mc2_g2_cyclic_linf_l3_seed()
        assert model.l3_basis("e1", "e2", "f12").get("eta", 0) != 0

    def test_l3_killing_cocycle_value(self):
        model = build_mc2_g2_cyclic_linf_l3_seed()
        assert simplify(model.l3_basis("e1", "e2", "f12").get("eta", 0) - 3) == 0


class TestMC2G2SeedCEBridge:
    """Cross-check the G_2 cyclic seed against the CE uniqueness profile."""

    def test_cyclic_ce_profile_matches_expected(self):
        profile = cyclic_ce_profile_from_cyclic_seed(build_mc2_g2_cyclic_linf_seed())
        assert profile["dims"] == {0: 0, 1: 0, 2: 1, 3: 0}
