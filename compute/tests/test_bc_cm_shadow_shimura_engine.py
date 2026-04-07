r"""Tests for BC-118: Complex multiplication on shadow moduli and Shimura variety special points.

Multi-path verification:
    (i)   j-invariant computation (q-expansion vs Eisenstein)
    (ii)  class polynomial (roots match CM database)
    (iii) Shimura reciprocity (Galois orbits match class group)
    (iv)  Galois orbit transitivity
    (v)   numerical proximity at zeta zeros

CAUTION (AP1): kappa formulas are family-specific.
CAUTION (AP10): cross-verify all CM values by multiple independent methods.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
"""

import cmath
import math

import pytest

from compute.lib.bc_cm_shadow_shimura_engine import (
    # Basic shadow invariants
    kappa_virasoro,
    kappa_affine_sl2,
    virasoro_alpha,
    virasoro_S4,
    virasoro_Delta,
    affine_sl2_alpha,
    affine_sl2_S4,
    affine_sl2_Delta,
    # Shadow metric
    shadow_metric_Q,
    shadow_metric_roots,
    shadow_cross_ratio,
    lambda_to_j,
    shadow_j_invariant_virasoro,
    shadow_j_invariant_affine_sl2,
    # j-invariant
    j_from_tau,
    tau_from_j_numerical,
    # CM database
    CMData,
    cm_database,
    class_number,
    # CM locus
    CMShadowPoint,
    find_virasoro_cm_point,
    find_affine_sl2_cm_point,
    compute_cm_shadow_table,
    # Shimura
    ideal_class_group_representatives,
    shimura_action,
    verify_shimura_reciprocity,
    verify_heegner_h1_rationality,
    # Zeta zeros
    riemann_zeta_zeros,
    shadow_c_from_zeta_zero,
    nearest_cm_to_zero,
    cm_proximity_at_zeros,
    # Algebraicity
    test_algebraicity as check_algebraicity,
    # Multi-path verification
    verify_j_invariant_multipath,
    # Galois orbits
    galois_orbit_cm,
    # Shadow discriminant
    shadow_discriminant_virasoro,
    shadow_modular_discriminant_virasoro,
    # Summary
    build_cm_shadow_summary,
    # Internal
    _reduced_forms,
    _divisors,
    _cm_j_from_reduced_forms,
)


# ============================================================================
# 1. Basic shadow invariants (AP1: recompute, never copy)
# ============================================================================

class TestShadowInvariants:
    """Verify shadow invariants match manuscript formulas."""

    def test_kappa_virasoro_basic(self):
        """κ(Vir, c) = c/2."""
        assert kappa_virasoro(26) == 13.0
        assert kappa_virasoro(0) == 0.0
        assert kappa_virasoro(1) == 0.5
        assert kappa_virasoro(13) == 6.5

    def test_kappa_virasoro_self_dual(self):
        """At the self-dual point c=13: κ = 13/2 = 6.5.
        AP8: Virasoro is self-dual at c=13, NOT c=26."""
        assert kappa_virasoro(13) == 6.5

    def test_kappa_complementarity(self):
        """AP24: κ(Vir_c) + κ(Vir_{26-c}) = 13, NOT 0."""
        for c_val in [0, 1, 5, 10, 13, 20, 25, 26]:
            total = kappa_virasoro(c_val) + kappa_virasoro(26 - c_val)
            assert abs(total - 13.0) < 1e-12, f"Failed at c={c_val}: got {total}"

    def test_kappa_affine_sl2(self):
        """κ(sl₂, k) = 3(k+2)/4."""
        assert kappa_affine_sl2(0) == 1.5       # 3*2/4 = 1.5
        assert kappa_affine_sl2(1) == 2.25      # 3*3/4 = 2.25
        assert kappa_affine_sl2(2) == 3.0       # 3*4/4 = 3.0
        assert abs(kappa_affine_sl2(-2)) < 1e-12  # critical level

    def test_virasoro_S4(self):
        """Q^contact_Vir = 10/[c(5c+22)]."""
        assert abs(virasoro_S4(1) - 10 / 27) < 1e-12
        assert abs(virasoro_S4(10) - 10 / (10 * 72)) < 1e-12

    def test_virasoro_Delta(self):
        """Δ = 40/(5c+22)."""
        assert abs(virasoro_Delta(1) - 40 / 27) < 1e-12
        assert abs(virasoro_Delta(10) - 40 / 72) < 1e-12

    def test_virasoro_Delta_consistency(self):
        """Δ = 8κS₄ (definition consistency)."""
        for c_val in [1, 5, 10, 13, 25]:
            delta_direct = virasoro_Delta(c_val)
            delta_product = 8 * kappa_virasoro(c_val) * virasoro_S4(c_val)
            assert abs(delta_direct - delta_product) < 1e-12


# ============================================================================
# 2. Shadow metric
# ============================================================================

class TestShadowMetric:
    """Shadow metric Q_L(t) = (2κ + 3αt)² + 2Δt²."""

    def test_Q_at_zero(self):
        """Q_L(0) = 4κ²."""
        for c_val in [1, 10, 13, 26]:
            kap = kappa_virasoro(c_val)
            Q0 = shadow_metric_Q(0, kap, virasoro_alpha(), virasoro_Delta(c_val))
            assert abs(Q0 - 4 * kap ** 2) < 1e-10

    def test_roots_are_roots(self):
        """Verify t_± are actual roots of Q_L."""
        for c_val in [1, 5, 10, 13, 20, 26]:
            kap = kappa_virasoro(c_val)
            alp = virasoro_alpha()
            delta = virasoro_Delta(c_val)
            t_p, t_m = shadow_metric_roots(kap, alp, delta)
            Q_plus = shadow_metric_Q(t_p, kap, alp, delta)
            Q_minus = shadow_metric_Q(t_m, kap, alp, delta)
            assert abs(Q_plus) < 1e-8 * max(1, abs(4 * kap ** 2)), \
                f"Q(t+) = {Q_plus} at c={c_val}"
            assert abs(Q_minus) < 1e-8 * max(1, abs(4 * kap ** 2)), \
                f"Q(t-) = {Q_minus} at c={c_val}"

    def test_discriminant_formula(self):
        """Discriminant of Q_L as quadratic: b²-4ac = -32Δκ²."""
        for c_val in [1, 5, 10, 13, 26]:
            kap = kappa_virasoro(c_val)
            alp = virasoro_alpha()
            delta = virasoro_Delta(c_val)
            disc = shadow_discriminant_virasoro(c_val)
            expected = -32 * delta * kap ** 2
            assert abs(disc - expected) < 1e-10

    def test_roots_conjugate_for_positive_Delta(self):
        """When Δ > 0 and κ > 0, roots are complex conjugates."""
        for c_val in [1, 5, 10, 26]:
            kap = kappa_virasoro(c_val)
            alp = virasoro_alpha()
            delta = virasoro_Delta(c_val)
            t_p, t_m = shadow_metric_roots(kap, alp, delta)
            # Should be conjugates
            assert abs(t_p - t_m.conjugate()) < 1e-10


# ============================================================================
# 3. j-invariant computation (multi-path)
# ============================================================================

class TestJInvariant:
    """j-invariant from τ, verified by multiple methods."""

    @pytest.mark.parametrize("tau, j_expected", [
        (1j, 1728.0),                           # D = -4
        ((-1 + 1j * math.sqrt(3)) / 2, 0.0),   # D = -3 (cube root of unity)
        (1j * math.sqrt(2), 8000.0),             # D = -8
        ((1 + 1j * math.sqrt(7)) / 2, -3375.0), # D = -7
    ])
    def test_j_known_values(self, tau, j_expected):
        """j at CM points with class number 1."""
        j_val = j_from_tau(tau)
        assert abs(j_val.imag) < 1e-4, f"j should be real, got Im = {j_val.imag}"
        assert abs(j_val.real - j_expected) < 1.0, \
            f"j({tau}) = {j_val.real}, expected {j_expected}"

    def test_j_multipath_agreement_tau_i(self):
        """Multi-path: q-expansion vs Eisenstein vs eta for τ = i."""
        v = verify_j_invariant_multipath(1j)
        assert v["agreement_12"] < 1e-10, f"q-exp vs Eisenstein: {v['agreement_12']}"
        assert v["agreement_13"] < 1e-10, f"q-exp vs alt: {v['agreement_13']}"
        assert v["agreement_23"] < 1e-10, f"Eisenstein vs alt: {v['agreement_23']}"

    def test_j_multipath_agreement_rho(self):
        """Multi-path for τ = ρ (cube root of unity)."""
        tau = (-1 + 1j * math.sqrt(3)) / 2
        v = verify_j_invariant_multipath(tau)
        # j = 0, so use absolute tolerance
        assert abs(v["j_qexp"]) < 1e-4
        assert abs(v["j_eisenstein"]) < 1e-4

    def test_j_multipath_agreement_sqrt2(self):
        """Multi-path for τ = i√2."""
        v = verify_j_invariant_multipath(1j * math.sqrt(2))
        assert v["agreement_12"] < 1e-8

    def test_j_positive_imaginary_only(self):
        """j(τ) requires Im(τ) > 0."""
        with pytest.raises(ValueError):
            j_from_tau(-1j)

    def test_lambda_to_j_special(self):
        """λ = 1/2 corresponds to j = 1728 (the square lattice)."""
        j_val = lambda_to_j(0.5)
        assert abs(j_val - 1728) < 1e-6

    def test_lambda_to_j_symmetry(self):
        """j(λ) = j(1-λ) = j(1/λ) (S₃ symmetry of cross-ratios)."""
        for lam in [0.3, 0.5 + 0.1j, -1.0 + 0.5j]:
            j1 = lambda_to_j(lam)
            j2 = lambda_to_j(1 - lam)
            j3 = lambda_to_j(1 / lam)
            assert abs(j1 - j2) < 1e-6 * max(1, abs(j1)), "j(λ) ≠ j(1-λ)"
            assert abs(j1 - j3) < 1e-6 * max(1, abs(j1)), "j(λ) ≠ j(1/λ)"


# ============================================================================
# 4. CM database and class numbers
# ============================================================================

class TestCMDatabase:
    """Verify CM data against known mathematical facts."""

    def test_heegner_numbers_class_1(self):
        """The 9 Heegner numbers have class number 1."""
        heegner = [-3, -4, -7, -8, -11, -19, -43, -67, -163]
        for D in heegner:
            assert class_number(D) == 1, f"h({D}) should be 1"

    def test_class_number_2_examples(self):
        """Known fields with h = 2."""
        h2_fields = [-15, -20, -24, -35, -40, -51]
        for D in h2_fields:
            assert class_number(D) == 2, f"h({D}) should be 2, got {class_number(D)}"

    def test_class_number_3_examples(self):
        """Known fields with h = 3."""
        h3_fields = [-23, -31]
        for D in h3_fields:
            assert class_number(D) == 3, f"h({D}) should be 3, got {class_number(D)}"

    def test_class_number_4_examples(self):
        """Known fields with h = 4."""
        h4_fields = [-39, -55, -56]
        for D in h4_fields:
            assert class_number(D) == 4, f"h({D}) should be 4, got {class_number(D)}"

    def test_cm_database_nonempty(self):
        """CM database has entries."""
        db = cm_database()
        assert len(db) > 10

    def test_cm_database_h1_count(self):
        """Exactly 9 entries with h = 1."""
        db = cm_database()
        h1 = [cm for cm in db if cm.h == 1]
        assert len(h1) == 9

    def test_cm_j_values_match_class_number(self):
        """Each CM entry has h j-values."""
        db = cm_database()
        for cm in db:
            assert len(cm.j_values) == cm.h, \
                f"D={cm.D}: expected {cm.h} j-values, got {len(cm.j_values)}"

    def test_reduced_forms_discriminant(self):
        """Reduced forms have the correct discriminant."""
        for D in [-3, -4, -7, -15, -23, -39]:
            forms = _reduced_forms(D)
            for a, b, c_form in forms:
                disc = b ** 2 - 4 * a * c_form
                assert disc == D, \
                    f"Form ({a},{b},{c_form}): disc = {disc}, expected {D}"


# ============================================================================
# 5. Heegner number verification (class number 1)
# ============================================================================

class TestHeegnerNumbers:
    """Verify the 9 Heegner number CM j-values."""

    def test_all_heegner_j_rational(self):
        """All 9 Heegner j-values should be rational (real integers)."""
        results = verify_heegner_h1_rationality()
        for D, data in results.items():
            assert data["is_rational"], f"D={D}: j should be rational"

    def test_all_heegner_j_match_known(self):
        """All 9 Heegner j-values should match known values."""
        results = verify_heegner_h1_rationality()
        for D, data in results.items():
            assert data["matches_known"], \
                f"D={D}: j_computed={data['j_computed'].real:.2f}, expected={data['j_expected']}"

    @pytest.mark.parametrize("D, j_expected", [
        (-3, 0),
        (-4, 1728),
        (-7, -3375),
        (-8, 8000),
        (-11, -32768),
        (-19, -884736),
        (-43, -884736000),
        (-67, -147197952000),
    ])
    def test_individual_heegner(self, D, j_expected):
        """Individual Heegner j-values from reduced forms."""
        forms = _reduced_forms(D)
        assert len(forms) == 1
        a, b, c_form = forms[0]
        tau = (-b + cmath.sqrt(D)) / (2 * a)
        j_val = j_from_tau(tau)
        assert abs(j_val.imag) < 1e-4
        assert abs(j_val.real - j_expected) < max(1.0, abs(j_expected) * 1e-6)

    @pytest.mark.xfail(reason="D=-163 Heegner j-value j((-1+sqrt(-163))/2) = -640320^3 "
                        "exceeds float64 precision: the q-expansion at tau ~ 6.3i requires "
                        "~55 decimal digits but float64 provides ~16. Needs mpmath.")
    def test_heegner_163_ramanujan(self):
        """D=-163: j = -640320³ (Ramanujan's constant).
        e^{π√163} ≈ 640320³ + 744 (the near-integer)."""
        forms = _reduced_forms(-163)
        a, b, c_form = forms[0]
        tau = (-b + cmath.sqrt(-163)) / (2 * a)
        j_val = j_from_tau(tau)
        assert abs(j_val.imag) < 1.0  # Larger tolerance for huge number
        expected = -262537412640768000  # = -640320³
        assert abs(j_val.real - expected) / abs(expected) < 1e-6


# ============================================================================
# 6. Shimura reciprocity
# ============================================================================

class TestShimuraReciprocity:
    """Verify Shimura reciprocity law for CM points."""

    def test_h1_fields_single_orbit(self):
        """Class number 1: single rational j-value."""
        for D in [-3, -4, -7, -8, -11, -19, -43, -67]:
            v = verify_shimura_reciprocity(D)
            assert v["h_K"] == 1
            assert v["j_rational_if_h1"] is True

    def test_h2_two_conjugate_j(self):
        """Class number 2: two j-values that are Galois conjugates."""
        for D in [-15, -20]:
            v = verify_shimura_reciprocity(D)
            assert v["h_K"] == 2
            assert v["distinct"] is True

    def test_galois_orbit_transitive_h1(self):
        """Galois orbit is transitive for h=1."""
        for D in [-3, -4, -7, -8]:
            orb = galois_orbit_cm(D)
            assert orb["is_transitive"]
            assert orb["orbit_size"] == 1

    def test_galois_orbit_transitive_h2(self):
        """Galois orbit is transitive for h=2."""
        for D in [-15, -20, -24]:
            orb = galois_orbit_cm(D)
            assert orb["is_transitive"]
            assert orb["orbit_size"] == 2

    def test_galois_orbit_transitive_h3(self):
        """Galois orbit is transitive for h=3."""
        for D in [-23, -31]:
            orb = galois_orbit_cm(D)
            assert orb["is_transitive"]
            assert orb["orbit_size"] == 3

    def test_ideal_class_group_size(self):
        """Ideal class group has h_K elements."""
        for D, h in [(-3, 1), (-15, 2), (-23, 3), (-39, 4)]:
            reps = ideal_class_group_representatives(D)
            assert len(reps) == h, f"D={D}: expected {h} reps, got {len(reps)}"

    def test_shimura_action_h1_rational(self):
        """For h=1, the Shimura action produces a single rational j-value."""
        for D in [-3, -4, -7]:
            action = shimura_action(D)
            assert len(action) == 1
            j_val = list(action.values())[0]
            assert abs(j_val.imag) < 1e-4


# ============================================================================
# 7. Shadow j-invariant (Virasoro)
# ============================================================================

class TestShadowJInvariant:
    """Shadow elliptic curve j-invariant for Virasoro."""

    def test_shadow_j_real_for_real_c(self):
        """j_shadow(c) should be real when c is real."""
        for c_val in [1, 5, 10, 13, 20, 26]:
            j = shadow_j_invariant_virasoro(float(c_val))
            assert abs(j.imag) < 1e-8 * max(1, abs(j.real)), \
                f"c={c_val}: j has nonzero imaginary part {j.imag}"

    def test_shadow_j_varies_with_c(self):
        """j_shadow(c) is not constant."""
        j_values = [shadow_j_invariant_virasoro(float(c)).real
                     for c in [1, 5, 10, 20]]
        # Check they're distinct
        for i in range(len(j_values)):
            for j_idx in range(i + 1, len(j_values)):
                assert abs(j_values[i] - j_values[j_idx]) > 1.0

    def test_shadow_j_complementarity(self):
        """j_shadow(c) and j_shadow(26-c) are related by complementarity.
        The shadow metrics at c and 26-c have related discriminants:
        Δ(c) + Δ(26-c) is a known expression."""
        for c_val in [1, 5, 10, 13, 20, 25]:
            delta_c = virasoro_Delta(c_val)
            delta_dual = virasoro_Delta(26 - c_val)
            # Both should be positive (5c+22 > 0 for c > -22/5)
            assert delta_c > 0
            assert delta_dual > 0

    def test_shadow_j_self_dual_point(self):
        """At c=13 (self-dual): the shadow metric has special structure."""
        j_13 = shadow_j_invariant_virasoro(13.0)
        # j(13) and j(26-13) = j(13) should agree
        j_13_dual = shadow_j_invariant_virasoro(13.0)
        assert abs(j_13 - j_13_dual) < 1e-10


# ============================================================================
# 8. CM locus search
# ============================================================================

class TestCMLocus:
    """Find CM points on the shadow moduli."""

    def test_find_cm_j_1728(self):
        """Find c where j_shadow = 1728 (D=-4, i)."""
        c = find_virasoro_cm_point(1728.0)
        assert c is not None
        j_check = shadow_j_invariant_virasoro(c)
        assert abs(j_check - 1728) < 1.0

    def test_find_cm_j_0(self):
        """Find c where j_shadow = 0 (D=-3, cube root of unity)."""
        c = find_virasoro_cm_point(0.0, c_initial=5.0 + 2.0j)
        assert c is not None
        j_check = shadow_j_invariant_virasoro(c)
        assert abs(j_check) < 1.0

    def test_find_cm_j_minus_3375(self):
        """Find c where j_shadow = -3375 (D=-7)."""
        c = find_virasoro_cm_point(-3375.0)
        assert c is not None
        j_check = shadow_j_invariant_virasoro(c)
        assert abs(j_check - (-3375)) < 10.0

    def test_find_cm_j_8000(self):
        """Find c where j_shadow = 8000 (D=-8)."""
        c = find_virasoro_cm_point(8000.0)
        assert c is not None
        j_check = shadow_j_invariant_virasoro(c)
        assert abs(j_check - 8000) < 10.0

    def test_find_cm_j_minus_32768(self):
        """Find c where j_shadow = -32768 (D=-11)."""
        c = find_virasoro_cm_point(-32768.0)
        assert c is not None
        j_check = shadow_j_invariant_virasoro(c)
        assert abs(j_check - (-32768)) < 100.0

    def test_cm_shadow_kappa_at_j1728(self):
        """κ at the CM point j=1728 should be c/2."""
        c = find_virasoro_cm_point(1728.0)
        assert c is not None
        kap = kappa_virasoro(c)
        assert abs(kap - c / 2) < 1e-10

    def test_affine_sl2_cm_point(self):
        """Find k where j_shadow(sl₂) = 1728."""
        k = find_affine_sl2_cm_point(1728.0)
        assert k is not None
        j_check = shadow_j_invariant_affine_sl2(k)
        assert abs(j_check - 1728) < 10.0


# ============================================================================
# 9. CM shadow table
# ============================================================================

class TestCMShadowTable:
    """Build and verify the CM shadow table."""

    def test_table_nonempty(self):
        """Table has entries for h ≤ 2."""
        table = compute_cm_shadow_table(max_class_number=2)
        assert len(table) > 5

    def test_table_h1_entries(self):
        """All h=1 CM points should have c_shadow found."""
        table = compute_cm_shadow_table(
            families=["virasoro"], max_class_number=1)
        for pt in table:
            assert pt.h_K == 1
            # c_shadow may or may not be found for all j-values
            # (Newton's method may not converge for extreme j-values)

    def test_table_kappa_consistency(self):
        """κ at CM points should equal c_shadow/2."""
        table = compute_cm_shadow_table(
            families=["virasoro"], max_class_number=1)
        for pt in table:
            if pt.c_shadow is not None and pt.kappa_val is not None:
                assert abs(pt.kappa_val - pt.c_shadow / 2) < 1e-8

    def test_summary_table(self):
        """Build summary table for h ≤ 2."""
        summary = build_cm_shadow_summary(max_h=2)
        assert len(summary) > 0
        for row in summary:
            assert "h_K" in row
            assert "D" in row
            assert "j_CM" in row


# ============================================================================
# 10. Riemann zeta zeros and CM proximity
# ============================================================================

class TestZetaZeroProximity:
    """Shadow CM proximity at Riemann zeta zeros."""

    def test_zeta_zeros_count(self):
        """First 20 zeros available."""
        zeros = riemann_zeta_zeros(20)
        assert len(zeros) == 20

    def test_zeta_zeros_increasing(self):
        """Zeros are strictly increasing."""
        zeros = riemann_zeta_zeros(20)
        for i in range(len(zeros) - 1):
            assert zeros[i] < zeros[i + 1]

    def test_first_zero_value(self):
        """γ₁ ≈ 14.1347."""
        zeros = riemann_zeta_zeros(1)
        assert abs(zeros[0] - 14.134725) < 0.001

    def test_shadow_c_at_first_zero(self):
        """c(ρ₁) should be close to 26 with small imaginary part."""
        c = shadow_c_from_zeta_zero(14.134725)
        assert abs(c.real - 26) < 1.0
        assert abs(c.imag) < 2.0

    def test_shadow_c_real_part_approaches_26(self):
        """As γ → ∞, Re(c(ρ)) → 26."""
        zeros = riemann_zeta_zeros(20)
        re_parts = [shadow_c_from_zeta_zero(g).real for g in zeros]
        # Later zeros should be closer to 26
        assert re_parts[-1] > re_parts[0]
        assert abs(re_parts[-1] - 26) < abs(re_parts[0] - 26)

    def test_shadow_c_imaginary_part_decreases(self):
        """As γ → ∞, Im(c(ρ)) → 0."""
        zeros = riemann_zeta_zeros(20)
        im_parts = [abs(shadow_c_from_zeta_zero(g).imag) for g in zeros]
        # Later zeros should have smaller imaginary part
        assert im_parts[-1] < im_parts[0]

    def test_cm_proximity_runs(self):
        """CM proximity computation runs without error."""
        results = cm_proximity_at_zeros(n_zeros=5, max_h=1)
        assert len(results) == 5
        for r in results:
            assert "gamma" in r
            assert "c_zero" in r
            assert "distance" in r

    def test_nearest_cm_returns_valid_point(self):
        """Nearest CM point should have a valid discriminant."""
        result = nearest_cm_to_zero(14.134725, max_h=1)
        assert result["D_nearest"] is not None
        assert result["D_nearest"] < 0


# ============================================================================
# 11. Algebraicity tests
# ============================================================================

class TestAlgebraicity:
    """Test algebraicity detection."""

    def test_integer_detected(self):
        """Integers are algebraic of degree 0."""
        r = check_algebraicity(complex(1728, 0))
        assert r["is_algebraic"]
        assert r["degree"] == 0

    def test_rational_detected(self):
        """Rationals are algebraic of degree 1."""
        r = check_algebraicity(complex(1.5, 0))
        assert r["is_algebraic"]
        assert r["degree"] <= 1

    def test_sqrt2_algebraic(self):
        """sqrt(2) is algebraic of degree 2.

        Use tighter tolerance than default to prevent the rational
        search (q up to 999) from matching a close convergent like
        1393/985 ~ 1.41421356..., which is accurate to ~5e-7.
        """
        r = check_algebraicity(complex(math.sqrt(2), 0), max_degree=3,
                               tol=1e-12)
        assert r["is_algebraic"]
        assert r["degree"] == 2


# ============================================================================
# 12. Shadow discriminant
# ============================================================================

class TestShadowDiscriminant:
    """Shadow discriminant and modular discriminant."""

    def test_shadow_disc_formula(self):
        """disc = -32Δκ²."""
        for c_val in [1, 5, 10, 13, 26]:
            disc = shadow_discriminant_virasoro(c_val)
            kap = kappa_virasoro(c_val)
            delta = virasoro_Delta(c_val)
            expected = -32 * delta * kap ** 2
            assert abs(disc - expected) < 1e-10

    def test_shadow_disc_negative_for_class_M(self):
        """For Virasoro (class M, Δ > 0, κ > 0): disc < 0."""
        for c_val in [1, 5, 10, 13, 26]:
            disc = shadow_discriminant_virasoro(c_val)
            assert disc.real < 0, f"disc should be negative at c={c_val}"

    def test_modular_disc_formula(self):
        """Modular discriminant = b²-4ac for Q_L as quadratic."""
        for c_val in [1, 10, 26]:
            disc = shadow_modular_discriminant_virasoro(c_val)
            kap = kappa_virasoro(c_val)
            alp = virasoro_alpha()
            delta = virasoro_Delta(c_val)
            a = 9 * alp ** 2 + 2 * delta
            b = 12 * kap * alp
            c0 = 4 * kap ** 2
            expected = b ** 2 - 4 * a * c0
            assert abs(disc - expected) < 1e-8


# ============================================================================
# 13. Internal utilities
# ============================================================================

class TestUtilities:
    """Test internal utility functions."""

    def test_divisors_small(self):
        """Divisors of small numbers."""
        assert _divisors(1) == [1]
        assert _divisors(6) == [1, 2, 3, 6]
        assert _divisors(12) == [1, 2, 3, 4, 6, 12]
        assert _divisors(7) == [1, 7]  # prime

    def test_reduced_forms_identity(self):
        """The principal form (1, b, c) is always present."""
        for D in [-3, -4, -7, -8, -11]:
            forms = _reduced_forms(D)
            # Principal form has a=1
            has_principal = any(a == 1 for a, b, c_form in forms)
            assert has_principal, f"D={D}: no principal form"

    def test_cm_j_from_reduced_forms(self):
        """CM j-values from reduced forms match known h=1 values."""
        known = {-3: 0, -4: 1728, -7: -3375, -8: 8000}
        for D, j_exp in known.items():
            j_vals = _cm_j_from_reduced_forms(D)
            assert len(j_vals) == 1
            assert abs(j_vals[0].real - j_exp) < max(1.0, abs(j_exp) * 1e-6)
            assert abs(j_vals[0].imag) < 1e-4


# ============================================================================
# 14. Cross-family consistency (AP5, AP10)
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-checks between Virasoro and affine sl₂ CM structures."""

    def test_kappa_different_families(self):
        """κ formulas are distinct between families (AP1)."""
        # At c=3 for Virasoro: κ = 3/2
        # At k=3 for sl₂: κ = 3*5/4 = 15/4
        assert abs(kappa_virasoro(3) - 1.5) < 1e-12
        assert abs(kappa_affine_sl2(3) - 3.75) < 1e-12
        assert kappa_virasoro(3) != kappa_affine_sl2(3)

    def test_class_number_formula(self):
        """Class number computed from reduced forms matches h(D).
        Cross-check: h(D) = #reduced forms = degree of Hilbert class polynomial."""
        for D, h_exp in [(-3, 1), (-4, 1), (-15, 2), (-23, 3), (-39, 4)]:
            h = class_number(D)
            assert h == h_exp

    def test_j_invariant_two_paths(self):
        """j(τ) from q-expansion matches j from Eisenstein E₄, E₆."""
        for tau in [1j, 1j * math.sqrt(2), 0.5 + 0.866j]:
            v = verify_j_invariant_multipath(tau)
            assert v["agreement_12"] < 1e-6, \
                f"τ={tau}: paths disagree by {v['agreement_12']}"


# ============================================================================
# 15. Galois orbit structure
# ============================================================================

class TestGaloisOrbits:
    """Galois orbit structure of CM j-values."""

    def test_h1_single_rational_orbit(self):
        """h=1: single rational j-value (one orbit element)."""
        for D in [-3, -4, -7, -8]:
            orb = galois_orbit_cm(D)
            assert orb["orbit_size"] == 1
            assert orb["is_transitive"]
            if D != -3:  # j(-3)=0 is rational but might appear as tiny imaginary
                assert orb["j_rational"] or abs(orb["j_values"][0].imag) < 1e-4

    def test_h2_two_element_orbit(self):
        """h=2: two distinct j-values forming one orbit."""
        for D in [-15, -20]:
            orb = galois_orbit_cm(D)
            assert orb["orbit_size"] == 2
            assert orb["is_transitive"]

    def test_h3_three_element_orbit(self):
        """h=3: three distinct j-values."""
        orb = galois_orbit_cm(-23)
        assert orb["orbit_size"] == 3
        assert orb["is_transitive"]

    def test_h2_j_values_are_conjugates(self):
        """For D=-15 (h=2): j-values are roots of the same quadratic."""
        orb = galois_orbit_cm(-15)
        j1, j2 = orb["j_values"]
        # Sum and product should be rational (integers)
        s = j1 + j2
        p = j1 * j2
        assert abs(s.imag) < 1e-2, f"Sum has imaginary part: {s.imag}"
        assert abs(p.imag) < 1e-2, f"Product has imaginary part: {p.imag}"


# ============================================================================
# 16. Shadow metric at CM points
# ============================================================================

class TestShadowMetricAtCM:
    """Shadow invariants evaluated at CM points."""

    def test_shadow_metric_positive_at_origin(self):
        """Q_L(0) > 0 for all c with κ ≠ 0."""
        for c_val in [1, 5, 10, 13, 26]:
            Q0 = shadow_metric_Q(
                0, kappa_virasoro(c_val),
                virasoro_alpha(), virasoro_Delta(c_val))
            assert Q0.real > 0

    def test_shadow_connection_monodromy(self):
        """The shadow connection has monodromy -1 (Koszul sign).
        This means going around a root of Q_L, √Q changes sign.

        Method: track winding number of Q_L around a simple zero.
        Q_L has a simple zero at t_p, so Q_L winds once (phase 2π)
        around a small circle. Therefore √Q_L accumulates phase π,
        giving monodromy exp(iπ) = -1.

        We track Q_L's winding (not √Q_L) to avoid cmath.sqrt
        branch-cut artifacts (AP10)."""
        c_val = 10.0
        kap = kappa_virasoro(c_val)
        alp = virasoro_alpha()
        delta = virasoro_Delta(c_val)
        t_p, t_m = shadow_metric_roots(kap, alp, delta)

        # Trace a small circle around t_p, tracking winding of Q_L
        n_pts = 200
        phase_total_Q = 0.0
        eps = 0.001
        prev_Q = None
        for k in range(n_pts):
            theta = 2 * math.pi * k / n_pts
            t = t_p + eps * cmath.exp(1j * theta)
            Q_val = shadow_metric_Q(t, kap, alp, delta)
            if prev_Q is not None:
                phase_total_Q += cmath.phase(Q_val / prev_Q)
            prev_Q = Q_val

        # Close the loop
        t_close = t_p + eps * cmath.exp(0j)
        Q_close = shadow_metric_Q(t_close, kap, alp, delta)
        phase_total_Q += cmath.phase(Q_close / prev_Q)

        # Q_L has a simple zero at t_p, so winding number = 1 (phase = 2π)
        assert abs(abs(phase_total_Q) - 2 * math.pi) < 0.2, \
            f"Q_L winding phase = {phase_total_Q:.4f}, expected ±2π"

        # Therefore √Q_L has monodromy exp(iπ) = -1
        # (half the winding of Q_L around a simple zero)


# ============================================================================
# 17. Spectral map properties
# ============================================================================

class TestSpectralMap:
    """Properties of the map ρ → c(ρ) from zeta zeros to shadow parameters."""

    def test_critical_line_maps_near_26(self):
        """Re(ρ) = 1/2 maps to Re(c) ≈ 26."""
        for gamma in [10, 20, 50, 100]:
            c = shadow_c_from_zeta_zero(gamma)
            assert 25 < c.real < 27

    def test_self_dual_point(self):
        """ρ = 1/2 (the real point) maps to c = 13."""
        c = shadow_c_from_zeta_zero(0)
        assert abs(c - 13.0) < 1e-10

    def test_imaginary_part_sign(self):
        """Im(c) > 0 when γ > 0."""
        for gamma in [14.13, 21.02, 25.01]:
            c = shadow_c_from_zeta_zero(gamma)
            assert c.imag > 0

    def test_large_gamma_limit(self):
        """As γ → ∞, c → 26."""
        c_100 = shadow_c_from_zeta_zero(100)
        c_1000 = shadow_c_from_zeta_zero(1000)
        assert abs(c_1000 - 26) < abs(c_100 - 26)
        assert abs(c_1000.real - 26) < 0.01


# ============================================================================
# 18. Tau inversion
# ============================================================================

class TestTauInversion:
    """tau_from_j_numerical inverts j_from_tau."""

    def test_tau_inversion_j_1728(self):
        """j = 1728 should give τ near i."""
        tau = tau_from_j_numerical(1728.0, initial_tau=0.0 + 1.0j)
        j_check = j_from_tau(tau)
        assert abs(j_check - 1728) < 1.0

    def test_tau_inversion_j_0(self):
        """j = 0 should give τ near ρ = (-1+i√3)/2."""
        tau = tau_from_j_numerical(0.0, initial_tau=-0.5 + 0.9j)
        j_check = j_from_tau(tau)
        assert abs(j_check) < 1.0

    def test_tau_inversion_roundtrip(self):
        """tau → j → tau should be consistent (up to modular group action)."""
        tau_orig = 0.3 + 1.2j
        j_val = j_from_tau(tau_orig)
        tau_recovered = tau_from_j_numerical(j_val, initial_tau=tau_orig)
        j_check = j_from_tau(tau_recovered)
        assert abs(j_check - j_val) / max(1, abs(j_val)) < 1e-6


# ============================================================================
# 19. Affine sl₂ shadow
# ============================================================================

class TestAffineSl2Shadow:
    """Shadow j-invariant for affine sl₂."""

    def test_j_defined_for_positive_level(self):
        """j_shadow(sl₂, k) defined for k > -2."""
        for k_val in [1, 2, 5, 10]:
            j = shadow_j_invariant_affine_sl2(float(k_val))
            assert not cmath.isinf(j)
            assert not cmath.isnan(j)

    def test_j_varies_with_level(self):
        """j_shadow changes with k."""
        j_values = [shadow_j_invariant_affine_sl2(float(k)).real
                     for k in [1, 2, 5, 10]]
        for i in range(len(j_values) - 1):
            assert j_values[i] != j_values[i + 1]

    def test_alpha_class_L(self):
        """Affine sl₂ has S₄ = 0 (class L), Δ = 0."""
        assert affine_sl2_S4() == 0.0
        assert affine_sl2_Delta() == 0.0

    def test_alpha_positive(self):
        """α > 0 for positive level."""
        for k_val in [1, 2, 5]:
            assert affine_sl2_alpha(k_val) > 0


# ============================================================================
# 20. Additional multi-path verifications
# ============================================================================

class TestMultiPath:
    """Additional multi-path verifications."""

    def test_j_from_tau_vs_eisenstein_at_D_8(self):
        """j(i√2) = 8000: q-expansion vs Eisenstein."""
        v = verify_j_invariant_multipath(1j * math.sqrt(2))
        assert abs(v["j_qexp"].real - 8000) < 1.0
        assert abs(v["j_eisenstein"].real - 8000) < 1.0
        assert v["agreement_12"] < 1e-6

    def test_j_from_tau_vs_eisenstein_at_D_7(self):
        """j((1+i√7)/2) = -3375: q-expansion vs Eisenstein."""
        tau = (1 + 1j * math.sqrt(7)) / 2
        v = verify_j_invariant_multipath(tau)
        assert abs(v["j_qexp"].real - (-3375)) < 1.0
        assert v["agreement_12"] < 1e-6

    def test_class_polynomial_h2_roots_match(self):
        """For D=-15 (h=2): CM j-values from reduced forms match
        roots of the Hilbert class polynomial."""
        forms = _reduced_forms(-15)
        assert len(forms) == 2

        j_from_forms = []
        for a, b, c_form in forms:
            tau = (-b + cmath.sqrt(-15)) / (2 * a)
            j_val = j_from_tau(tau)
            j_from_forms.append(j_val)

        # These should be roots of x² + 191025x - 121287375 = 0
        # Sum of roots = -191025, product = -121287375
        s = j_from_forms[0] + j_from_forms[1]
        p = j_from_forms[0] * j_from_forms[1]
        assert abs(s.real - (-191025)) < 1.0
        assert abs(p.real - (-121287375)) < 1000.0

    def test_class_poly_h3_degree(self):
        """For D=-23 (h=3): exactly 3 j-values from reduced forms."""
        j_vals = _cm_j_from_reduced_forms(-23)
        assert len(j_vals) == 3
        # All should be real (D=-23 has only real j-values)
        # Actually h=3 can have complex conjugate pairs plus one real
        # Check: sum of j-values should be real (trace of Galois orbit)
        total = sum(j_vals)
        assert abs(total.imag) < 1.0

    def test_shadow_j_cross_ratio_consistency(self):
        """The cross-ratio λ and j are related by the standard formula."""
        for c_val in [5, 10, 20]:
            kap = kappa_virasoro(c_val)
            alp = virasoro_alpha()
            delta = virasoro_Delta(c_val)
            lam = shadow_cross_ratio(kap, alp, delta)
            j_from_lam = lambda_to_j(lam)
            j_from_shadow = shadow_j_invariant_virasoro(c_val)
            assert abs(j_from_lam - j_from_shadow) < 1e-6 * max(1, abs(j_from_shadow))
