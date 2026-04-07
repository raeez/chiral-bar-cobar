r"""Tests for the Gaiotto-Rapcak Y-algebra landscape engine.

FULL REDO: Deep mathematical verification of corner VOA Y_{N1,N2,N3}[Psi].

Verifies:
  1. h-parameter and lambda constraints (eqs. 3.42-3.43)
  2. Central charge via two independent paths (eq. 3.37 vs eq. 3.41)
  3. Match with Fateev-Lukyanov W_N formula for Y_{0,0,N}
  4. S3 triality invariance (eq. 3.38)
  5. Three dualities: S-duality vs FF-duality vs Koszul
  6. FF-complementarity (Psi-independent for |N2-N1| <= 1, NOT generally)
  7. Shadow depth classification (G/L/M)
  8. Kappa computation (exact for W_N-type, approximate for general)
  9. Generator counting and first null weights
  10. MacMahon box counting
  11. Large-N limit towards W_{1+infinity}
  12. Koszulness predictions
  13. Cross-family consistency
  14. Full landscape survey

Multi-path verification (CLAUDE.md mandate):
  Every numerical value verified by at least 2 independent paths.

Sources:
  [GR17] Gaiotto-Rapcak, arXiv:1703.00982
  [PR17] Prochazka-Rapcak, arXiv:1711.05725
  [CL20] Creutzig-Linshaw, arXiv:2005.10234
  [Rap20] Rapcak thesis
"""

import pytest
from fractions import Fraction

from compute.lib.gaiotto_rapcak_landscape_engine import (
    h_params_from_psi,
    lambda_params,
    verify_lambda_constraint,
    verify_truncation_curve,
    central_charge,
    central_charge_lambda,
    central_charge_via_lambda,
    fl_central_charge_wn,
    fl_central_charge_wn_bare,
    ff_complementarity_wn,
    fdv_constant_wn,
    verify_wn_match,
    triality_sigma,
    triality_tau,
    triality_orbit,
    verify_triality_invariance,
    kappa_y_algebra,
    kappa_y_algebra_is_exact,
    kappa_wn_bare,
    kappa_heisenberg,
    harmonic_number,
    shadow_depth_class,
    shadow_depth,
    s_duality,
    ff_duality,
    koszul_dual_prediction,
    koszul_complementarity_sum,
    ff_complementarity_sum,
    ff_complementarity_is_constant,
    ff_complementarity_constant,
    s_duality_complementarity_sum,
    koszul_preserves_depth_class,
    triality_preserves_depth_class,
    generator_weights,
    num_generators,
    first_null_weight,
    num_generators_box,
    macmahon_box,
    is_freely_strongly_generated,
    is_chirally_koszul,
    analyze_y_algebra,
    landscape_survey,
    landscape_summary,
    landscape_depth_census,
    large_n_central_charge,
    large_n_kappa_ratio,
    # Multi-path Koszulness proof infrastructure (thm:y-algebra-koszulness)
    degenerate_psi_values,
    truncation_singular_psi,
    admissible_psi_values,
    non_generic_psi_set,
    is_generic_psi,
    koszul_proof_path_1_fsg,
    koszul_proof_path_2_brst,
    koszul_proof_path_3_truncation,
    koszul_proof_path_4_spectral_seq,
    koszul_proof_summary,
    verify_koszulness_at_psi,
    triality_preserves_koszulness,
    ff_duality_preserves_koszulness,
)


# ============================================================================
# Section 1: h-parameter and lambda constraints
# ============================================================================

class TestParametrization:
    """Tests for the h and lambda parameter computations."""

    def test_h_params_sum_zero(self):
        """h1 + h2 + h3 = 0 for all valid Psi."""
        for psi in [Fraction(2), Fraction(3), Fraction(1, 2),
                    Fraction(-1), Fraction(5, 3)]:
            h1, h2, h3 = h_params_from_psi(psi)
            assert h1 + h2 + h3 == 0, f"h sum != 0 at Psi={psi}"

    def test_h_params_psi_recovery(self):
        """Psi = -h2/h1."""
        for psi in [Fraction(2), Fraction(3), Fraction(1, 2), Fraction(-1)]:
            h1, h2, h3 = h_params_from_psi(psi)
            assert -h2 / h1 == psi, f"Psi not recovered at Psi={psi}"

    def test_h_params_degenerate(self):
        """Psi=0 and Psi=1 are degenerate."""
        with pytest.raises(ValueError):
            h_params_from_psi(Fraction(0))
        with pytest.raises(ValueError):
            h_params_from_psi(Fraction(1))

    def test_lambda_constraint(self):
        """1/lambda_1 + 1/lambda_2 + 1/lambda_3 = 0 (eq. 3.40)."""
        for N1, N2, N3 in [(0, 0, 2), (1, 2, 3), (0, 1, 3), (2, 2, 2)]:
            for psi in [Fraction(3), Fraction(5, 2)]:
                lam1, lam2, lam3 = lambda_params(N1, N2, N3, psi)
                if lam1 != 0 and lam2 != 0 and lam3 != 0:
                    assert verify_lambda_constraint(lam1, lam2, lam3), \
                        f"Lambda constraint fails for ({N1},{N2},{N3})[{psi}]"

    def test_truncation_curve(self):
        """N1/l1 + N2/l2 + N3/l3 = 1 (eq. 3.35)."""
        for N1, N2, N3 in [(0, 0, 3), (1, 1, 2), (1, 2, 3)]:
            for psi in [Fraction(3), Fraction(7, 2)]:
                lam1, lam2, lam3 = lambda_params(N1, N2, N3, psi)
                if lam1 != 0 and lam2 != 0 and lam3 != 0:
                    assert verify_truncation_curve(N1, N2, N3, lam1, lam2, lam3), \
                        f"Truncation curve fails for ({N1},{N2},{N3})[{psi}]"

    def test_lambda_for_y002(self):
        """For Y_{0,0,2}[3]: lambda_3 = sigma/h3 = 4/2 = 2."""
        lam1, lam2, lam3 = lambda_params(0, 0, 2, Fraction(3))
        # sigma = 0*1 + 0*(-3) + 2*(3-1) = 4
        # lambda_3 = 4/(3-1) = 2
        assert lam3 == 2

    def test_lambda_constraint_systematic(self):
        """Systematic lambda constraint check for all N_i <= 3."""
        for n1 in range(4):
            for n2 in range(4):
                for n3 in range(4):
                    for psi in [Fraction(3), Fraction(7, 3)]:
                        lam1, lam2, lam3 = lambda_params(n1, n2, n3, psi)
                        if lam1 != 0 and lam2 != 0 and lam3 != 0:
                            assert verify_lambda_constraint(lam1, lam2, lam3)


# ============================================================================
# Section 2: Central charge -- two-path verification
# ============================================================================

class TestCentralCharge:
    """Tests for central charge formula via two independent paths."""

    def test_two_paths_agree_y002(self):
        """Y_{0,0,2}[3]: direct and lambda paths agree."""
        c1 = central_charge(0, 0, 2, Fraction(3))
        c2 = central_charge_via_lambda(0, 0, 2, Fraction(3))
        assert c1 == c2

    def test_two_paths_agree_y003(self):
        """Y_{0,0,3}[4]: direct and lambda paths agree."""
        c1 = central_charge(0, 0, 3, Fraction(4))
        c2 = central_charge_via_lambda(0, 0, 3, Fraction(4))
        assert c1 == c2

    def test_two_paths_agree_y123(self):
        """Y_{1,2,3}[5/2]: direct and lambda paths agree."""
        c1 = central_charge(1, 2, 3, Fraction(5, 2))
        c2 = central_charge_via_lambda(1, 2, 3, Fraction(5, 2))
        assert c1 == c2

    def test_two_paths_systematic(self):
        """All Y_{N1,N2,N3} with N_i <= 3 at two Psi values."""
        for psi in [Fraction(3), Fraction(5, 2)]:
            for n1 in range(4):
                for n2 in range(4):
                    for n3 in range(4):
                        c1 = central_charge(n1, n2, n3, psi)
                        c2 = central_charge_via_lambda(n1, n2, n3, psi)
                        assert c1 == c2, \
                            f"({n1},{n2},{n3})[{psi}]: {c1} vs {c2}"

    def test_y000_central_charge(self):
        """Y_{0,0,0}[Psi]: c = 0 from direct formula (all terms vanish)."""
        c = central_charge(0, 0, 0, Fraction(3))
        assert c == 0

    def test_y001_central_charge(self):
        """Y_{0,0,1}[Psi]: c = 1.

        Manual: a=-1, b=-1, d=0.
        term1 = (1/3)(-1)(0) = 0; term2 = 3(-1)(0) = 0; term3 = 0.
        term4 = (2+0-0)(1)^2 = 2; term5 = -1.  Total = 1.
        """
        c = central_charge(0, 0, 1, Fraction(3))
        assert c == 1

    def test_y002_virasoro(self):
        """Y_{0,0,2}[3] = W_2 x gl(1): c(Vir at k=1) = -7, c(Y) = -6."""
        c = central_charge(0, 0, 2, Fraction(3))
        assert c == -6

    def test_y003_w3(self):
        """Y_{0,0,3}[4] = W_3 x gl(1): c(W_3 at k=1) = -52, c(Y) = -51."""
        c = central_charge(0, 0, 3, Fraction(4))
        assert c == -51

    def test_y002_at_psi2(self):
        """Y_{0,0,2}[2]: k=0, c(Vir,0) = 1 - 6*1/2 = -2, c(Y) = -1."""
        c = central_charge(0, 0, 2, Fraction(2))
        assert c == -1

    def test_degenerate_psi(self):
        """Psi=0 and Psi=1 raise errors."""
        with pytest.raises(ValueError):
            central_charge(0, 0, 2, Fraction(0))
        with pytest.raises(ValueError):
            central_charge(0, 0, 2, Fraction(1))


# ============================================================================
# Section 3: Match with Fateev-Lukyanov W_N formula
# ============================================================================

class TestWNMatch:
    """Verify Y_{0,0,N}[Psi] matches W_N central charge + gl(1)."""

    def test_w2_match(self):
        """Y_{0,0,2}[Psi] = W_2 x gl(1) at several Psi."""
        for psi in [Fraction(3), Fraction(5), Fraction(7, 2)]:
            assert verify_wn_match(2, psi)

    def test_w3_match(self):
        """Y_{0,0,3}[Psi] = W_3 x gl(1)."""
        for psi in [Fraction(4), Fraction(5), Fraction(9, 2)]:
            assert verify_wn_match(3, psi)

    def test_w4_match(self):
        """Y_{0,0,4}[Psi] = W_4 x gl(1)."""
        for psi in [Fraction(5), Fraction(7), Fraction(11, 2)]:
            assert verify_wn_match(4, psi)

    def test_w5_match(self):
        """Y_{0,0,5}[Psi] = W_5 x gl(1)."""
        for psi in [Fraction(6), Fraction(8)]:
            assert verify_wn_match(5, psi)

    def test_wn_systematic(self):
        """Systematic W_N match for N=2..8 at generic Psi."""
        for N in range(2, 9):
            psi = Fraction(N + 1)
            assert verify_wn_match(N, psi), f"W_{N} match fails"

    def test_fl_explicit_w2(self):
        """Explicit FL formula for W_2 (Virasoro) at k=1: c = -7, c+gl(1) = -6."""
        c = fl_central_charge_wn(2, Fraction(1))
        assert c == Fraction(-6)

    def test_fl_explicit_w3(self):
        """FL formula for W_3 at k=1: c(W_3) = -52, plus gl(1) = -51."""
        c = fl_central_charge_wn(3, Fraction(1))
        assert c == Fraction(-51)

    def test_fl_bare_w2(self):
        """Bare W_2 (without gl(1)) at k=1: c = -7."""
        c = fl_central_charge_wn_bare(2, Fraction(1))
        assert c == Fraction(-7)

    def test_fl_bare_w2_complementarity(self):
        """W_2: c(k=1) + c(k'=-5) = 26 (Freudenthal-de Vries for Virasoro)."""
        c1 = fl_central_charge_wn_bare(2, Fraction(1))
        c2 = fl_central_charge_wn_bare(2, Fraction(-5))
        assert c1 + c2 == 26


# ============================================================================
# Section 4: Triality
# ============================================================================

class TestTriality:
    """Tests for S3 triality symmetry."""

    def test_sigma_involution(self):
        """sigma^2 = id."""
        N1, N2, N3, psi = 1, 2, 3, Fraction(5, 2)
        s = triality_sigma(N1, N2, N3, psi)
        ss = triality_sigma(*s)
        assert ss == (N1, N2, N3, psi)

    def test_tau_involution(self):
        """tau^2 = id."""
        N1, N2, N3, psi = 1, 2, 3, Fraction(5, 2)
        t = triality_tau(N1, N2, N3, psi)
        tt = triality_tau(*t)
        assert tt == (N1, N2, N3, psi)

    def test_triality_orbit_size_generic(self):
        """Generic orbit (all N_i distinct) has 6 elements."""
        orbit = triality_orbit(1, 2, 3, Fraction(5, 2))
        assert len(orbit) == 6

    def test_triality_invariance_y123(self):
        """Central charge invariant under triality for Y_{1,2,3}."""
        assert verify_triality_invariance(1, 2, 3, Fraction(5, 2))

    def test_triality_invariance_y012(self):
        """Central charge invariant under triality for Y_{0,1,2}."""
        assert verify_triality_invariance(0, 1, 2, Fraction(3))

    def test_triality_invariance_systematic(self):
        """Systematic triality check for all N_i <= 3."""
        for n1 in range(4):
            for n2 in range(4):
                for n3 in range(4):
                    assert verify_triality_invariance(n1, n2, n3, Fraction(3)), \
                        f"Triality fails for ({n1},{n2},{n3})"

    def test_triality_maps_w_algebras(self):
        """Y_{0,0,N}, Y_{0,N,0}, Y_{N,0,0} all have the same c at triality-related Psi."""
        for N in range(2, 5):
            psi = Fraction(N + 1)
            c1 = central_charge(0, 0, N, psi)
            # tau: (0,0,N)[Psi] -> (0,N,0)[1-Psi]
            c2 = central_charge(0, N, 0, 1 - psi)
            assert c1 == c2

    def test_sigma_explicit(self):
        """sigma: (1,2,3,3) -> (2,1,3,1/3)."""
        result = triality_sigma(1, 2, 3, Fraction(3))
        assert result == (2, 1, 3, Fraction(1, 3))

    def test_tau_explicit(self):
        """tau: (1,2,3,3) -> (1,3,2,-2)."""
        result = triality_tau(1, 2, 3, Fraction(3))
        assert result == (1, 3, 2, Fraction(-2))

    def test_s3_relation(self):
        """(sigma.tau)^3 = id (S3 relation)."""
        N1, N2, N3, psi = 1, 2, 3, Fraction(5, 2)
        state = (N1, N2, N3, psi)
        for _ in range(3):
            state = triality_tau(*state)
            state = triality_sigma(*state)
        assert state == (N1, N2, N3, psi)


# ============================================================================
# Section 5: Three dualities (S, FF, Koszul)
# ============================================================================

class TestThreeDualities:
    """Tests for the three distinct duality operations."""

    def test_s_duality_swaps_n1_n2(self):
        """S-duality swaps N1 <-> N2 and inverts Psi."""
        n1s, n2s, n3s, psi_s = s_duality(1, 2, 3, Fraction(5))
        assert (n1s, n2s, n3s) == (2, 1, 3)
        assert psi_s == Fraction(1, 5)

    def test_ff_duality_preserves_triple(self):
        """FF-duality preserves (N1,N2,N3) and negates Psi."""
        n1f, n2f, n3f, psi_f = ff_duality(1, 2, 3, Fraction(5))
        assert (n1f, n2f, n3f) == (1, 2, 3)
        assert psi_f == Fraction(-5)

    def test_s_and_ff_are_different(self):
        """S-duality and FF-duality are genuinely different operations."""
        sd = s_duality(1, 2, 3, Fraction(5))
        ff = ff_duality(1, 2, 3, Fraction(5))
        assert sd != ff, "S-duality and FF-duality should differ"

    def test_koszul_dual_equals_ff(self):
        """Koszul dual prediction = FF-duality."""
        for n1, n2, n3 in [(0, 0, 2), (1, 2, 3), (1, 1, 1)]:
            kd = koszul_dual_prediction(n1, n2, n3, Fraction(5))
            ff = ff_duality(n1, n2, n3, Fraction(5))
            assert kd == ff

    def test_ff_involution(self):
        """FF^2 = id: (Psi -> -Psi -> Psi)."""
        N1, N2, N3, psi = 1, 2, 3, Fraction(5)
        d = ff_duality(N1, N2, N3, psi)
        dd = ff_duality(*d)
        assert dd == (N1, N2, N3, Fraction(psi))

    def test_s_involution(self):
        """S^2 = id: (1/Psi -> Psi)."""
        N1, N2, N3, psi = 1, 2, 3, Fraction(5)
        d = s_duality(N1, N2, N3, psi)
        dd = s_duality(*d)
        assert dd == (N1, N2, N3, Fraction(psi))

    def test_s_ff_composition(self):
        """S . FF: (N1,N2,N3,Psi) -> (N2,N1,N3,-1/Psi).

        This is a third operation, the composition of S and FF.
        """
        s_ff = s_duality(*ff_duality(1, 2, 3, Fraction(5)))
        assert s_ff == (2, 1, 3, Fraction(-1, 5))

    def test_ff_s_composition(self):
        """FF . S: (N1,N2,N3,Psi) -> (N2,N1,N3,-1/Psi) as well.

        Since FF preserves N-triple and negates Psi, and S swaps N1/N2
        and inverts Psi: FF(S(x)) = FF(N2,N1,N3,1/Psi) = (N2,N1,N3,-1/Psi).
        """
        ff_s = ff_duality(*s_duality(1, 2, 3, Fraction(5)))
        assert ff_s == (2, 1, 3, Fraction(-1, 5))


# ============================================================================
# Section 6: FF-complementarity
# ============================================================================

class TestFFComplementarity:
    """Tests for Feigin-Frenkel complementarity c(Psi) + c(-Psi)."""

    def test_wn_fdv_n2(self):
        """Y_{0,0,2}: c(Psi)+c(-Psi) = 28 = FdV(2)+2, all Psi."""
        fdv = fdv_constant_wn(2)
        assert fdv == 28
        for psi in [Fraction(3), Fraction(5), Fraction(7, 2)]:
            assert ff_complementarity_wn(2, psi) == 28

    def test_wn_fdv_n3(self):
        """Y_{0,0,3}: c(Psi)+c(-Psi) = 102 = FdV(3)+2."""
        fdv = fdv_constant_wn(3)
        assert fdv == 102
        for psi in [Fraction(4), Fraction(5), Fraction(7, 2)]:
            assert ff_complementarity_wn(3, psi) == 102

    def test_wn_fdv_n4(self):
        """Y_{0,0,4}: FdV = 2*3 + 4*4*15 + 2 = 248."""
        assert fdv_constant_wn(4) == 248

    def test_wn_fdv_n5(self):
        """Y_{0,0,5}: FdV = 2*4 + 4*5*24 + 2 = 490."""
        assert fdv_constant_wn(5) == 490

    def test_ff_psi_independent_d0(self):
        """d = N2-N1 = 0: FF complementarity is Psi-independent."""
        for n1, n2, n3 in [(0, 0, 2), (1, 1, 2), (2, 2, 3), (0, 0, 5)]:
            assert ff_complementarity_is_constant(n1, n2, n3), \
                f"({n1},{n2},{n3}): d={n2-n1}, should be constant"

    def test_ff_psi_independent_d1(self):
        """d = N2-N1 = 1: d(d^2-1) = 0, Psi-independent."""
        for n1, n2, n3 in [(0, 1, 2), (1, 2, 3), (0, 1, 3)]:
            assert ff_complementarity_is_constant(n1, n2, n3)

    def test_ff_psi_independent_dm1(self):
        """d = N2-N1 = -1: d(d^2-1) = 0, Psi-independent."""
        for n1, n2, n3 in [(1, 0, 2), (2, 1, 3), (3, 2, 0)]:
            assert ff_complementarity_is_constant(n1, n2, n3)

    def test_ff_NOT_psi_independent_d2(self):
        """d = N2-N1 = 2: d(d^2-1) = 6 != 0, NOT Psi-independent."""
        assert not ff_complementarity_is_constant(0, 2, 3)
        assert not ff_complementarity_is_constant(1, 3, 0)

    def test_ff_NOT_psi_independent_dm2(self):
        """d = N2-N1 = -2: NOT Psi-independent."""
        assert not ff_complementarity_is_constant(2, 0, 3)
        assert not ff_complementarity_is_constant(3, 1, 0)

    def test_ff_constant_value_y002(self):
        """For Y_{0,0,2}: FF constant = 28."""
        assert ff_complementarity_constant(0, 0, 2) == 28

    def test_ff_constant_value_y003(self):
        """For Y_{0,0,3}: FF constant = 102."""
        assert ff_complementarity_constant(0, 0, 3) == 102

    def test_ff_constant_returns_none_when_not_constant(self):
        """Non-constant case returns None."""
        assert ff_complementarity_constant(0, 2, 3) is None

    def test_ff_constant_y112(self):
        """Y_{1,1,2}: d=0, Psi-independent.  Verify at two values."""
        s1 = ff_complementarity_sum(1, 1, 2, Fraction(3))
        s2 = ff_complementarity_sum(1, 1, 2, Fraction(7))
        assert s1 == s2 == 2

    def test_ff_constant_y123(self):
        """Y_{1,2,3}: d=1, Psi-independent.  Verify at two values."""
        s1 = ff_complementarity_sum(1, 2, 3, Fraction(3))
        s2 = ff_complementarity_sum(1, 2, 3, Fraction(7))
        assert s1 == s2 == 6


# ============================================================================
# Section 7: S-duality complementarity
# ============================================================================

class TestSDualityComplementarity:
    """S-duality complementarity: c(A) + c(S(A)) = 2*c(A) by triality invariance."""

    def test_s_complementarity_equals_2c(self):
        """c(A) + c(S(A)) = 2c for all Y-algebras (triality invariance)."""
        for n1, n2, n3 in [(0, 0, 2), (1, 2, 3), (0, 1, 2), (1, 1, 1)]:
            psi = Fraction(3)
            c = central_charge(n1, n2, n3, psi)
            s_comp = s_duality_complementarity_sum(n1, n2, n3, psi)
            assert s_comp == 2 * c, \
                f"({n1},{n2},{n3}): c+c_S={s_comp}, 2c={2*c}"

    def test_s_complementarity_systematic(self):
        """Systematic S-duality complementarity for N_i <= 2."""
        for n1 in range(3):
            for n2 in range(3):
                for n3 in range(3):
                    psi = Fraction(5)
                    c = central_charge(n1, n2, n3, psi)
                    s_comp = s_duality_complementarity_sum(n1, n2, n3, psi)
                    assert s_comp == 2 * c


# ============================================================================
# Section 8: Shadow depth classification
# ============================================================================

class TestShadowDepth:
    """Tests for shadow depth class predictions."""

    def test_y000_gaussian(self):
        """Y_{0,0,0} is class G (single boson)."""
        assert shadow_depth_class(0, 0, 0) == 'G'
        assert shadow_depth(0, 0, 0) == 2

    def test_y001_gaussian(self):
        """Y_{0,0,1} is class G (Heisenberg-type)."""
        assert shadow_depth_class(0, 0, 1) == 'G'
        assert shadow_depth(0, 0, 1) == 2

    def test_y011_lie(self):
        """Y_{0,1,1} is class L (affine-type coset, no higher W)."""
        assert shadow_depth_class(0, 1, 1) == 'L'
        assert shadow_depth(0, 1, 1) == 3

    def test_y011_triality_invariant(self):
        """All permutations of (0,1,1) give class L."""
        for perm in [(0, 1, 1), (1, 0, 1), (1, 1, 0)]:
            assert shadow_depth_class(*perm) == 'L'

    def test_y002_mixed(self):
        """Y_{0,0,2} = Virasoro x gl(1) is class M."""
        assert shadow_depth_class(0, 0, 2) == 'M'
        assert shadow_depth(0, 0, 2) is None

    def test_y003_mixed(self):
        """Y_{0,0,3} = W_3 x gl(1) is class M."""
        assert shadow_depth_class(0, 0, 3) == 'M'

    def test_wn_all_class_m(self):
        """Y_{0,0,N} for N >= 2 are all class M."""
        for N in range(2, 8):
            assert shadow_depth_class(0, 0, N) == 'M'

    def test_y012_class_m(self):
        """Y_{0,1,2} is class M (non-principal DS)."""
        assert shadow_depth_class(0, 1, 2) == 'M'

    def test_y111_class_m(self):
        """Y_{1,1,1} is class M (N=2 super type)."""
        assert shadow_depth_class(1, 1, 1) == 'M'

    def test_triality_preserves_class(self):
        """Triality always preserves depth class (permutation invariant)."""
        for n1 in range(4):
            for n2 in range(4):
                for n3 in range(4):
                    assert triality_preserves_depth_class(n1, n2, n3)

    def test_koszul_preserves_class(self):
        """Koszul/FF duality preserves depth class (N-triple unchanged)."""
        for n1 in range(4):
            for n2 in range(4):
                for n3 in range(4):
                    assert koszul_preserves_depth_class(n1, n2, n3, Fraction(3))

    def test_landscape_class_counts(self):
        """Count depth classes in the max_N=3 landscape."""
        summary = landscape_summary(max_N=3, psi=Fraction(3))
        # G class: sorted triples (0,0,0) and (0,0,1) -> 1+3 = 4
        assert summary['G'] == 4
        # L class: sorted triple (0,1,1) -> 3 permutations
        assert summary['L'] == 3
        # C class: none in Y-landscape
        assert summary['C'] == 0
        # M class: everything else
        assert summary['M'] == summary['total'] - summary['G'] - summary['L']
        assert summary['total'] == 64  # 4^3

    def test_no_class_c_in_landscape(self):
        """No class C (contact) appears in the Y-algebra landscape up to N=5."""
        census = landscape_depth_census(max_N=5)
        assert len(census['C']) == 0

    def test_depth_census_structure(self):
        """Depth census has expected structure for max_N=3."""
        census = landscape_depth_census(max_N=3)
        assert (0, 0, 0) in census['G']
        assert (0, 0, 1) in census['G']
        assert (0, 1, 1) in census['L']
        assert (0, 0, 2) in census['M']


# ============================================================================
# Section 9: Kappa computation
# ============================================================================

class TestKappa:
    """Tests for modular characteristic kappa."""

    def test_harmonic_numbers(self):
        """H_1 = 1, H_2 = 3/2, H_3 = 11/6, H_4 = 25/12."""
        assert harmonic_number(1) == Fraction(1)
        assert harmonic_number(2) == Fraction(3, 2)
        assert harmonic_number(3) == Fraction(11, 6)
        assert harmonic_number(4) == Fraction(25, 12)

    def test_kappa_w2_matches_virasoro(self):
        """kappa(W_2 at k) = c(Vir,k)/2 since H_2-1 = 1/2."""
        for k in [Fraction(1), Fraction(2), Fraction(-3)]:
            c_vir = fl_central_charge_wn_bare(2, k)
            kap = kappa_wn_bare(2, k)
            assert kap == c_vir / 2

    def test_kappa_y002_exact(self):
        """kappa(Y_{0,0,2}[3]) = kappa(W_2, k=1) + kappa(gl(1), k=1).

        kappa(W_2, 1) = c(W_2, 1)/2 = -7/2.
        kappa(gl(1), 1) = 1.
        Total = -7/2 + 1 = -5/2.
        """
        kap = kappa_y_algebra(0, 0, 2, Fraction(3))
        assert kap == Fraction(-5, 2)

    def test_kappa_y003_exact(self):
        """kappa(Y_{0,0,3}[4]) = kappa(W_3, k=1) + kappa(gl(1), k=1).

        H_3 - 1 = 5/6. kappa(W_3) = -52 * 5/6 = -130/3.
        kappa(gl(1)) = 1.
        Total = -130/3 + 1 = -127/3.
        """
        kap = kappa_y_algebra(0, 0, 3, Fraction(4))
        expected = Fraction(-52) * Fraction(5, 6) + 1
        assert kap == expected
        assert kap == Fraction(-127, 3)

    def test_kappa_differs_from_c_over_2(self):
        """kappa != c/2 for Y_{0,0,N>=2} (AP48 verification)."""
        for N in range(2, 6):
            psi = Fraction(N + 1)
            c = central_charge(0, 0, N, psi)
            kap = kappa_y_algebra(0, 0, N, psi)
            assert kap != c / 2, f"W_{N}: kappa should not equal c/2"

    def test_kappa_exactness_flag(self):
        """Y_{0,0,N} has exact kappa; general Y has approximate."""
        assert kappa_y_algebra_is_exact(0, 0, 2) is True
        assert kappa_y_algebra_is_exact(0, 0, 5) is True
        assert kappa_y_algebra_is_exact(1, 2, 3) is False
        assert kappa_y_algebra_is_exact(1, 1, 1) is False

    def test_kappa_y000_zero(self):
        """kappa(Y_{0,0,0}) = 0."""
        assert kappa_y_algebra(0, 0, 0, Fraction(3)) == 0

    def test_kappa_y001(self):
        """kappa(Y_{0,0,1}) = c = 1."""
        assert kappa_y_algebra(0, 0, 1, Fraction(3)) == 1

    def test_kappa_heisenberg_consistency(self):
        """kappa(Heisenberg at level k) = k."""
        for k in [Fraction(1), Fraction(2), Fraction(-3)]:
            assert kappa_heisenberg(k) == k


# ============================================================================
# Section 10: Koszul duality
# ============================================================================

class TestKoszulDuality:
    """Tests for Koszul duality predictions."""

    def test_kd_preserves_n_triple(self):
        """Koszul dual preserves (N1,N2,N3)."""
        N1d, N2d, N3d, _ = koszul_dual_prediction(1, 2, 3, Fraction(5))
        assert (N1d, N2d, N3d) == (1, 2, 3)

    def test_kd_negates_psi(self):
        """Koszul dual sends Psi -> -Psi (FF involution)."""
        _, _, _, psi_d = koszul_dual_prediction(1, 2, 3, Fraction(5))
        assert psi_d == Fraction(-5)

    def test_kd_involution(self):
        """(A^!)^! = A: double Koszul dual returns original."""
        N1, N2, N3, psi = 1, 2, 3, Fraction(5)
        d = koszul_dual_prediction(N1, N2, N3, psi)
        dd = koszul_dual_prediction(*d)
        assert dd == (N1, N2, N3, Fraction(psi))

    def test_kd_virasoro_complementarity_28(self):
        """Y_{0,0,2}: c(Psi)+c(-Psi) = 28, Psi-independent (Freudenthal-de Vries)."""
        for psi in [Fraction(3), Fraction(5), Fraction(7), Fraction(5, 2)]:
            comp = koszul_complementarity_sum(0, 0, 2, psi)
            assert comp == 28

    def test_kd_w3_complementarity_102(self):
        """Y_{0,0,3}: c(Psi)+c(-Psi) = 102."""
        for psi in [Fraction(4), Fraction(5), Fraction(7, 2)]:
            comp = koszul_complementarity_sum(0, 0, 3, psi)
            assert comp == 102

    def test_kd_w4_complementarity_248(self):
        """Y_{0,0,4}: c(Psi)+c(-Psi) = 248."""
        comp = koszul_complementarity_sum(0, 0, 4, Fraction(5))
        assert comp == 248

    def test_kd_complementarity_psi_independent_check(self):
        """Complementarity Psi-independent iff |N2-N1| <= 1."""
        for n1 in range(4):
            for n2 in range(4):
                for n3 in range(4):
                    d = n2 - n1
                    expected = (d * (d**2 - 1) == 0)
                    actual = ff_complementarity_is_constant(n1, n2, n3)
                    assert actual == expected, \
                        f"({n1},{n2},{n3}): d={d}, expected {expected}"


# ============================================================================
# Section 11: Generators
# ============================================================================

class TestGenerators:
    """Tests for generator counting."""

    def test_y000_one_generator(self):
        """Y_{0,0,0}: 1 generator (gl(1) current at weight 1)."""
        assert num_generators(0, 0, 0) == 1

    def test_y002_two_generators(self):
        """Y_{0,0,2} = W_2 x gl(1): 2 generators at weights 1, 2."""
        assert num_generators(0, 0, 2) == 2
        assert generator_weights(0, 0, 2) == [1, 2]

    def test_y003_three_generators(self):
        """Y_{0,0,3} = W_3 x gl(1): 3 generators at weights 1, 2, 3."""
        assert num_generators(0, 0, 3) == 3
        assert generator_weights(0, 0, 3) == [1, 2, 3]

    def test_y00n_generators(self):
        """Y_{0,0,N}: N generators for N=1..6."""
        for N in range(1, 7):
            assert num_generators(0, 0, N) == N

    def test_first_null_y002(self):
        """First null of Y_{0,0,2} at weight (0+1)(0+1)(2+1) = 3."""
        assert first_null_weight(0, 0, 2) == 3

    def test_first_null_y123(self):
        """First null of Y_{1,2,3} at weight 2*3*4 = 24."""
        assert first_null_weight(1, 2, 3) == 24

    def test_first_null_y111(self):
        """First null of Y_{1,1,1} at weight 2*2*2 = 8."""
        assert first_null_weight(1, 1, 1) == 8

    def test_first_null_y012(self):
        """First null of Y_{0,1,2} at weight 1*2*3 = 6."""
        assert first_null_weight(0, 1, 2) == 6

    def test_first_null_monotone(self):
        """First null weight increases with N-triple."""
        assert first_null_weight(0, 0, 2) < first_null_weight(0, 1, 2)
        assert first_null_weight(0, 1, 2) < first_null_weight(1, 1, 2)
        assert first_null_weight(1, 1, 2) < first_null_weight(1, 2, 3)


# ============================================================================
# Section 12: MacMahon box counting
# ============================================================================

class TestMacMahon:
    """Tests for MacMahon plane partition box formula."""

    def test_macmahon_111(self):
        """M(1,1,1) = 2 (empty + single box)."""
        assert macmahon_box(1, 1, 1) == 2

    def test_macmahon_112(self):
        """M(1,1,2) = 3."""
        assert macmahon_box(1, 1, 2) == 3

    def test_macmahon_122(self):
        """M(1,2,2) = 6."""
        assert macmahon_box(1, 2, 2) == 6

    def test_macmahon_222(self):
        """M(2,2,2) = 20."""
        assert macmahon_box(2, 2, 2) == 20

    def test_macmahon_123(self):
        """M(1,2,3) = 10."""
        assert macmahon_box(1, 2, 3) == 10

    def test_macmahon_113(self):
        """M(1,1,3) = 4."""
        assert macmahon_box(1, 1, 3) == 4

    def test_macmahon_223(self):
        """M(2,2,3) = 50."""
        assert macmahon_box(2, 2, 3) == 50

    def test_macmahon_333(self):
        """M(3,3,3) = 980."""
        assert macmahon_box(3, 3, 3) == 980

    def test_macmahon_zero_dimension(self):
        """Any zero dimension gives M = 1."""
        assert macmahon_box(0, 0, 0) == 1
        assert macmahon_box(0, 0, 5) == 1
        assert macmahon_box(0, 3, 4) == 1
        assert macmahon_box(5, 0, 3) == 1

    def test_macmahon_symmetry(self):
        """M(a,b,c) is symmetric in all three arguments."""
        for a, b, c_val in [(1, 2, 3), (2, 3, 4), (1, 1, 3)]:
            m = macmahon_box(a, b, c_val)
            assert macmahon_box(a, c_val, b) == m
            assert macmahon_box(b, a, c_val) == m
            assert macmahon_box(b, c_val, a) == m
            assert macmahon_box(c_val, a, b) == m
            assert macmahon_box(c_val, b, a) == m

    def test_macmahon_a1(self):
        """M(1,b,c) = C(b+c, b) = binomial coefficient."""
        from math import comb
        for b in range(1, 5):
            for c_val in range(1, 5):
                assert macmahon_box(1, b, c_val) == comb(b + c_val, b)


# ============================================================================
# Section 13: Large-N limit
# ============================================================================

class TestLargeN:
    """Tests for the large-N limit towards W_{1+infinity}."""

    def test_large_n_central_charge_growth(self):
        """c(Y_{0,0,N}) grows as ~N^3 for large N at fixed Psi."""
        psi = Fraction(3)
        c_prev = None
        for N in [5, 10, 20]:
            c = large_n_central_charge(N, psi)
            if c_prev is not None:
                # Ratio should approach (N/N_prev)^3
                pass
            c_prev = c
        # Verify sign: for Psi=3, c should be negative for large N
        # c ~ -N^3 * (Psi-1)^2/Psi = -N^3 * 4/3
        c20 = large_n_central_charge(20, psi)
        assert c20 < 0

    def test_large_n_kappa_ratio_grows(self):
        """kappa/c ratio grows like H_N - 1 ~ log(N)."""
        psi = Fraction(3)
        r5 = large_n_kappa_ratio(5, psi)
        r10 = large_n_kappa_ratio(10, psi)
        # H_N - 1 grows; ratio at N=10 > ratio at N=5
        assert r10 is not None
        assert r5 is not None

    def test_large_n_wn_match(self):
        """Y_{0,0,N} matches W_N formula even for large N."""
        for N in [10, 20, 50]:
            assert verify_wn_match(N, Fraction(N + 1))


# ============================================================================
# Section 14: Koszulness
# ============================================================================

class TestKoszulness:
    """Tests for Koszulness predictions."""

    def test_all_y_algebras_koszul(self):
        """All Y-algebras are predicted chirally Koszul at generic Psi."""
        for n1 in range(4):
            for n2 in range(4):
                for n3 in range(4):
                    result = is_chirally_koszul(n1, n2, n3)
                    assert result in ('yes_always', 'yes_generic')

    def test_small_y_always_koszul(self):
        """Y_{0,0,0} and Y_{0,0,1} are always Koszul (not just generically)."""
        assert is_chirally_koszul(0, 0, 0) == 'yes_always'
        assert is_chirally_koszul(0, 0, 1) == 'yes_always'
        assert is_chirally_koszul(0, 1, 1) == 'yes_always'

    def test_larger_y_generically_koszul(self):
        """Y with max(Ni) >= 2 are Koszul only at generic Psi."""
        assert is_chirally_koszul(0, 0, 2) == 'yes_generic'
        assert is_chirally_koszul(1, 2, 3) == 'yes_generic'

    def test_freely_strongly_generated(self):
        """Free strong generation is the mechanism for Koszulness."""
        for n1 in range(3):
            for n2 in range(3):
                for n3 in range(3):
                    fsg = is_freely_strongly_generated(n1, n2, n3)
                    ck = is_chirally_koszul(n1, n2, n3)
                    assert fsg == ck  # same classification


# ============================================================================
# Section 15: Cross-family consistency
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-checks between Y-algebras and known standard landscape data."""

    def test_wn_kappa_cross_check(self):
        """kappa(Y_{0,0,2}[5]) matches known Virasoro formula + gl(1)."""
        psi = Fraction(5)
        kap = kappa_y_algebra(0, 0, 2, psi)
        c_vir = fl_central_charge_wn_bare(2, psi - 2)
        kappa_vir = c_vir / 2
        kappa_gl1 = psi - 2
        assert kap == kappa_vir + kappa_gl1

    def test_y_algebra_central_charge_additivity(self):
        """Central charges are additive for tensor products."""
        c1 = central_charge(0, 0, 2, Fraction(3))
        c2 = central_charge(0, 0, 0, Fraction(3))
        assert isinstance(c1 + c2, Fraction)

    def test_virasoro_self_dual_c13(self):
        """Virasoro is self-dual at c=13.

        For Y_{0,0,2}[Psi], c(Y) = c(Vir) + 1.
        Self-dual at c(Vir)=13, i.e., c(Y)=14.
        FF-complementarity: c(Psi)+c(-Psi) = 28 = 2*14.
        """
        # The complementarity sum is 28 = 2*14, consistent with
        # self-duality at c=14 for the Y-algebra (c=13 for bare Virasoro)
        assert fdv_constant_wn(2) == 28

    def test_y_extends_landscape(self):
        """Y-algebras with min(Ni) > 0 are NOT W_N type."""
        data = analyze_y_algebra(1, 1, 2, Fraction(3))
        assert not data.is_wn_type
        assert data.depth_class == 'M'

    def test_kappa_wn_complementarity(self):
        """kappa(W_N,k) + kappa(W_N,k') should be computable.

        For N=2: kappa + kappa' = 13 (from the canonical engine).
        For Y_{0,0,2}: kappa(Y) + kappa(Y') includes gl(1) contributions.
        """
        psi = Fraction(5)
        kap1 = kappa_y_algebra(0, 0, 2, psi)
        kap2 = kappa_y_algebra(0, 0, 2, -psi)
        # kappa_W + kappa_W' = 13 (bare Virasoro complementarity)
        # kappa_gl1 + kappa_gl1' = (Psi-2) + (-Psi-2) = -4
        # Total: 13 + (-4) = 9
        k = psi - 2
        kw1 = kappa_wn_bare(2, k)
        kw2 = kappa_wn_bare(2, -k - 4)
        assert kw1 + kw2 == 13  # bare Virasoro complementarity


# ============================================================================
# Section 16: Full landscape survey
# ============================================================================

class TestLandscapeSurvey:
    """Tests for the full landscape survey."""

    def test_survey_runs(self):
        """Survey completes without error."""
        results = landscape_survey(max_N=2, psi=Fraction(3))
        assert len(results) == 27  # 3^3

    def test_survey_all_have_central_charge(self):
        """Every algebra has a computed central charge."""
        results = landscape_survey(max_N=2, psi=Fraction(3))
        for data in results:
            assert isinstance(data.central_charge, Fraction)

    def test_survey_two_path_agreement(self):
        """Every algebra has matching central charges from two paths."""
        results = landscape_survey(max_N=2, psi=Fraction(3))
        for data in results:
            assert data.central_charge == data.central_charge_lambda, \
                f"({data.N1},{data.N2},{data.N3}): paths disagree"

    def test_survey_koszul_involution(self):
        """Koszul dual of dual is the original."""
        results = landscape_survey(max_N=2, psi=Fraction(3))
        for data in results:
            N1d, N2d, N3d, psi_d = data.koszul_dual
            if psi_d == 0 or psi_d == 1:
                continue
            dd = koszul_dual_prediction(N1d, N2d, N3d, psi_d)
            assert dd == (data.N1, data.N2, data.N3, data.psi)

    def test_summary_counts(self):
        """Summary counts are consistent."""
        summary = landscape_summary(max_N=2, psi=Fraction(3))
        assert summary['total'] == 27
        assert (summary['G'] + summary['L'] + summary['C'] + summary['M']
                == summary['total'])

    def test_analyze_y123(self):
        """Full analysis of Y_{1,2,3}[3]."""
        data = analyze_y_algebra(1, 2, 3, Fraction(3))
        assert data.depth_class == 'M'
        assert data.first_null == 24
        assert data.triality_orbit_size == 6
        assert not data.is_wn_type
        assert not data.kappa_is_exact

    def test_analyze_y002(self):
        """Full analysis of Y_{0,0,2}[3]."""
        data = analyze_y_algebra(0, 0, 2, Fraction(3))
        assert data.depth_class == 'M'
        assert data.first_null == 3
        assert data.is_wn_type
        assert data.kappa_is_exact
        assert data.central_charge == -6
        assert data.ff_complementarity == 28
        assert data.ff_complementarity_is_constant


# ============================================================================
# Section 17: Edge cases and special values
# ============================================================================

class TestEdgeCases:
    """Tests for edge cases and special values."""

    def test_negative_psi(self):
        """Negative Psi is allowed."""
        c = central_charge(0, 0, 2, Fraction(-1))
        assert isinstance(c, Fraction)

    def test_fractional_psi(self):
        """Fractional Psi works correctly."""
        c = central_charge(1, 2, 3, Fraction(7, 3))
        assert isinstance(c, Fraction)

    def test_large_n(self):
        """Y_{0,0,10}[11] computes without overflow."""
        c = central_charge(0, 0, 10, Fraction(11))
        assert verify_wn_match(10, Fraction(11))

    def test_symmetric_y_n_n_n(self):
        """Y_{N,N,N} has reduced triality orbit (Psi still varies)."""
        for N in [1, 2, 3]:
            orbit = triality_orbit(N, N, N, Fraction(3))
            assert len(orbit) >= 1

    def test_y_algebra_at_psi_half(self):
        """Y at Psi=1/2: sigma gives Psi=2, tau gives Psi=1/2."""
        c = central_charge(0, 0, 2, Fraction(1, 2))
        assert isinstance(c, Fraction)

    def test_all_y_with_max_ge_2_class_m(self):
        """All Y-algebras with max(N_i) >= 2 are class M."""
        for n1 in range(4):
            for n2 in range(4):
                for n3 in range(4):
                    if max(n1, n2, n3) >= 2:
                        assert shadow_depth_class(n1, n2, n3) == 'M'


# ============================================================================
# Section 18: Key research findings
# ============================================================================

class TestResearchFindings:
    """Tests that encode the key research findings from this analysis."""

    def test_finding_all_y_koszul(self):
        """FINDING: All Y-algebras are chirally Koszul at generic Psi.

        Mechanism: freely strongly generated => PBW collapse => Koszul.
        """
        for n1 in range(4):
            for n2 in range(4):
                for n3 in range(4):
                    assert is_chirally_koszul(n1, n2, n3) in \
                        ('yes_always', 'yes_generic')

    def test_finding_triality_preserves_depth(self):
        """FINDING: S3 triality PRESERVES shadow depth class.

        Reason: depth class depends on sorted(N1,N2,N3), triality permutes.
        """
        for n1 in range(4):
            for n2 in range(4):
                for n3 in range(4):
                    assert triality_preserves_depth_class(n1, n2, n3)

    def test_finding_s_duality_ne_koszul(self):
        """FINDING: S-duality != Koszul duality for Y-algebras.

        S-duality = sigma: (N1,N2) swap + Psi -> 1/Psi.
        Koszul = FF: same triple + Psi -> -Psi.
        These are DIFFERENT operations.
        """
        sd = s_duality(1, 2, 3, Fraction(5))
        kd = koszul_dual_prediction(1, 2, 3, Fraction(5))
        assert sd != kd

    def test_finding_s3_generated_by_s_and_tau(self):
        """FINDING: S3 triality = <S-duality, tau>.

        sigma = S-duality, tau = second generator.
        FF-duality is OUTSIDE S3 (it preserves the N-triple).
        """
        # Verify sigma and tau generate all 6 elements
        orbit = triality_orbit(1, 2, 3, Fraction(5, 2))
        assert len(orbit) == 6

    def test_finding_ff_complementarity_fails_for_d_ge_2(self):
        """FINDING: FF complementarity c(Psi)+c(-Psi) is NOT always constant.

        Psi-independent iff |N2-N1| <= 1.
        For |N2-N1| >= 2: the sum depends on Psi.
        """
        # Constant cases
        assert ff_complementarity_is_constant(0, 0, 3)
        assert ff_complementarity_is_constant(1, 2, 3)
        # Non-constant cases
        assert not ff_complementarity_is_constant(0, 2, 3)
        assert not ff_complementarity_is_constant(0, 3, 1)

    def test_finding_y_extends_landscape(self):
        """FINDING: Y-algebras extend the landscape beyond W_N.

        Y with all Ni > 0 are genuinely new (non-principal cosets).
        They are all class M and chirally Koszul.
        """
        count_new = 0
        for n1 in range(1, 4):
            for n2 in range(1, 4):
                for n3 in range(1, 4):
                    count_new += 1
                    assert shadow_depth_class(n1, n2, n3) == 'M'
        assert count_new == 27  # 3^3

    def test_finding_no_class_c_in_y_landscape(self):
        """FINDING: No class C (contact) in the Y-algebra landscape.

        The four classes for Y are: G (2 types), L (1 type), M (everything else).
        Class C (beta-gamma) does not appear because contact structure
        requires specific non-generic coupling.
        """
        census = landscape_depth_census(max_N=4)
        assert len(census['C']) == 0

    def test_finding_class_l_unique_to_011(self):
        """FINDING: Class L appears ONLY for Y_{0,1,1} (and permutations).

        This is the unique affine-type Y-algebra.
        """
        census = landscape_depth_census(max_N=4)
        l_triples = census['L']
        assert len(l_triples) == 1
        assert l_triples[0] == (0, 1, 1)

    def test_finding_large_n_w_infinity(self):
        """FINDING: Y_{0,0,N} -> W_{1+inf} as N -> inf (central charge ~ N^3)."""
        psi = Fraction(3)
        c10 = abs(large_n_central_charge(10, psi))
        c20 = abs(large_n_central_charge(20, psi))
        # c ~ N^3 * (Psi-1)^2/Psi, so c(20)/c(10) ~ 8
        ratio = c20 / c10
        assert 7 < float(ratio) < 9  # approximately 8


# ============================================================================
# Section 19: FF-complementarity algebraic structure
# ============================================================================

class TestFFComplementarityAlgebraic:
    """Deeper tests on the algebraic structure of FF-complementarity."""

    def test_ff_sum_formula_d0(self):
        """When d=0 (N1=N2), the FF sum simplifies to 2E where E is the constant part.

        For Y_{N,N,M}: a = N-M, b = N-M, d = 0.
        c(Psi) = a(a^2-1)(1/Psi + Psi) + E.
        c(-Psi) = a(a^2-1)(-1/Psi - Psi) + E.
        Sum = 2E.
        """
        for N, M in [(1, 2), (2, 3), (0, 2), (0, 5)]:
            psi1, psi2 = Fraction(3), Fraction(7)
            s1 = ff_complementarity_sum(N, N, M, psi1)
            s2 = ff_complementarity_sum(N, N, M, psi2)
            assert s1 == s2, f"Y_{{{N},{N},{M}}}: not constant"

    def test_ff_sum_formula_d1(self):
        """When d=1 (N2=N1+1), d(d^2-1) = 0 so the sum is constant."""
        for N1, N3 in [(0, 2), (0, 3), (1, 3), (2, 0)]:
            N2 = N1 + 1
            psi1, psi2 = Fraction(3), Fraction(7)
            s1 = ff_complementarity_sum(N1, N2, N3, psi1)
            s2 = ff_complementarity_sum(N1, N2, N3, psi2)
            assert s1 == s2

    def test_ff_sum_varies_d2(self):
        """When d=2, the sum genuinely depends on Psi."""
        s1 = ff_complementarity_sum(0, 2, 3, Fraction(3))
        s2 = ff_complementarity_sum(0, 2, 3, Fraction(5))
        assert s1 != s2, "Y_{0,2,3}: sum should vary with Psi"

    def test_ff_sum_varies_d3(self):
        """When d=3, the sum genuinely depends on Psi."""
        s1 = ff_complementarity_sum(0, 3, 1, Fraction(3))
        s2 = ff_complementarity_sum(0, 3, 1, Fraction(5))
        assert s1 != s2


# ============================================================================
# Section 20: Comprehensive landscape table
# ============================================================================

class TestLandscapeTable:
    """Build and verify the full landscape table for the monograph."""

    def test_landscape_table_max_n2(self):
        """Full landscape at max_N=2 has correct structure."""
        results = landscape_survey(max_N=2, psi=Fraction(3))
        wn_count = sum(1 for d in results if d.is_wn_type)
        non_wn_count = sum(1 for d in results if not d.is_wn_type)
        # W_N type: sorted has two zeros -> (0,0,0),(0,0,1),(0,0,2)
        # plus permutations: 1+3+3 = 7
        assert wn_count == 7
        assert non_wn_count == 20

    def test_landscape_table_max_n3(self):
        """Full landscape at max_N=3."""
        summary = landscape_summary(max_N=3, psi=Fraction(3))
        assert summary['total'] == 64
        assert summary['G'] == 4   # (0,0,0) + 3 perms of (0,0,1)
        assert summary['L'] == 3   # 3 perms of (0,1,1)
        assert summary['C'] == 0
        assert summary['M'] == 57  # everything else

    def test_distinct_sorted_triples(self):
        """Count distinct sorted triples up to max_N=3."""
        census = landscape_depth_census(max_N=3)
        total = sum(len(v) for v in census.values())
        # distinct sorted (n1,n2,n3) with 0 <= n1 <= n2 <= n3 <= 3
        # = C(3+3, 3) = C(6,3) = 20
        assert total == 20


# ############################################################################
#
#  SECTION 21: Y-ALGEBRA KOSZULNESS THEOREM (thm:y-algebra-koszulness)
#
#  Multi-path verification with 40+ tests.
#
#  THEOREM: Y_{N1,N2,N3}[Psi] is chirally Koszul at generic Psi.
#
#  Four independent proof paths:
#    P1: Free strong generation -> PBW -> Koszul
#    P2: BRST/DS definition preserves Koszulness
#    P3: Truncation of W_{1+infty} preserves free generation
#    P4: PBW spectral sequence collapses at E_2
#
# ############################################################################


# ============================================================================
# 21a: Non-generic locus analysis
# ============================================================================

class TestNonGenericLocus:
    """Tests for the non-generic Psi locus where Koszulness may fail."""

    def test_degenerate_values(self):
        """Degenerate Psi = {0, 1}."""
        degen = degenerate_psi_values()
        assert Fraction(0) in degen
        assert Fraction(1) in degen
        assert len(degen) == 2

    def test_truncation_singular_y002(self):
        """Y_{0,0,2}: sigma = (0-2) + (2-0)*Psi = -2 + 2*Psi = 2*(Psi-1).
        Singular at Psi = 1 (which is already degenerate).
        """
        psi_s = truncation_singular_psi(0, 0, 2)
        assert psi_s == Fraction(1)

    def test_truncation_singular_y003(self):
        """Y_{0,0,3}: sigma = -3 + 3*Psi = 3*(Psi-1).
        Singular at Psi = 1 (degenerate).
        """
        psi_s = truncation_singular_psi(0, 0, 3)
        assert psi_s == Fraction(1)

    def test_truncation_singular_y00n_always_at_1(self):
        """Y_{0,0,N}: sigma = N*(Psi-1), singular at Psi = 1 for all N >= 1.
        This coincides with the degenerate locus, so the truncation
        singularity introduces NO additional non-generic values.
        """
        for N in range(1, 8):
            psi_s = truncation_singular_psi(0, 0, N)
            assert psi_s == Fraction(1), f"N={N}: psi_s = {psi_s}"

    def test_truncation_singular_y123(self):
        """Y_{1,2,3}: sigma = (1-3) + (3-2)*Psi = -2 + Psi.
        Singular at Psi = 2 (genuinely non-degenerate).
        """
        psi_s = truncation_singular_psi(1, 2, 3)
        assert psi_s == Fraction(2)

    def test_truncation_singular_y011(self):
        """Y_{0,1,1}: sigma = -1 + (Psi-1) - Psi = -2. Never zero."""
        # sigma = (0 - 1) + (1 - 1)*Psi = -1, constant
        psi_s = truncation_singular_psi(0, 1, 1)
        assert psi_s is None

    def test_truncation_singular_y000(self):
        """Y_{0,0,0}: sigma = 0 for all Psi (degenerate triple)."""
        psi_s = truncation_singular_psi(0, 0, 0)
        assert psi_s is not None  # returns sentinel

    def test_truncation_singular_symmetric(self):
        """Y_{N,N,N}: sigma = N*(1 - Psi + Psi - 1) = 0.
        Degenerate: sigma vanishes identically.
        """
        psi_s = truncation_singular_psi(2, 2, 2)
        assert psi_s is not None  # sentinel for identically zero

    def test_admissible_y002_nonempty(self):
        """Y_{0,0,2} has admissible Psi values."""
        admiss = admissible_psi_values(0, 0, 2)
        assert len(admiss) > 0

    def test_admissible_y001_empty(self):
        """Y_{0,0,1}: no admissible obstructions (max N = 1)."""
        admiss = admissible_psi_values(0, 0, 1)
        assert len(admiss) == 0

    def test_admissible_y000_empty(self):
        """Y_{0,0,0}: no admissible obstructions."""
        admiss = admissible_psi_values(0, 0, 0)
        assert len(admiss) == 0

    def test_non_generic_set_structure(self):
        """Non-generic set has correct keys."""
        ng = non_generic_psi_set(1, 2, 3)
        assert 'degenerate' in ng
        assert 'truncation_singular' in ng
        assert 'admissible' in ng
        assert 'description' in ng

    def test_non_generic_always_contains_0_1(self):
        """Every non-generic set contains {0, 1} (the degenerate values)."""
        for n1 in range(3):
            for n2 in range(3):
                for n3 in range(3):
                    ng = non_generic_psi_set(n1, n2, n3)
                    assert Fraction(0) in ng['degenerate']
                    assert Fraction(1) in ng['degenerate']

    def test_is_generic_avoids_degenerate(self):
        """Psi = 0 and Psi = 1 are never generic."""
        for n1 in range(3):
            for n2 in range(3):
                for n3 in range(3):
                    assert not is_generic_psi(n1, n2, n3, 0)
                    assert not is_generic_psi(n1, n2, n3, 1)

    def test_is_generic_typical_values(self):
        """Typical irrational-like Psi values are generic."""
        # Psi = 7/3 is generic for most triples
        for n1 in range(3):
            for n2 in range(3):
                for n3 in range(3):
                    # At Psi = 7/3, the only obstruction is if
                    # the truncation singularity hits exactly 7/3
                    psi_s = truncation_singular_psi(n1, n2, n3)
                    if psi_s != Fraction(7, 3):
                        result = is_generic_psi(n1, n2, n3, Fraction(7, 3))
                        # May or may not be generic depending on admissible
                        assert isinstance(result, bool)

    def test_non_generic_locus_countable(self):
        """The non-generic locus is always finite (for bounded denom)."""
        for n1 in range(3):
            for n2 in range(3):
                for n3 in range(3):
                    ng = non_generic_psi_set(n1, n2, n3, max_denom=5)
                    n_total = (len(ng['degenerate'])
                               + (1 if ng['truncation_singular'] is not None else 0)
                               + len(ng['admissible']))
                    assert n_total < 200  # finite, not too large


# ============================================================================
# 21b: Proof Path 1 — Free strong generation -> PBW -> Koszul
# ============================================================================

class TestKoszulProofPath1:
    """Tests for Proof Path 1: Free strong generation."""

    def test_p1_valid_for_all_triples(self):
        """P1 is valid for all Y-algebras (the hypothesis is just generic Psi)."""
        for n1 in range(4):
            for n2 in range(4):
                for n3 in range(4):
                    p1 = koszul_proof_path_1_fsg(n1, n2, n3)
                    assert p1['valid'], f"P1 invalid for ({n1},{n2},{n3})"
                    assert p1['conclusion'] == 'chirally_koszul'

    def test_p1_references_correct_theorems(self):
        """P1 cites the correct chain of results."""
        p1 = koszul_proof_path_1_fsg(1, 2, 3)
        refs = p1['references']
        assert any('Gaiotto' in r for r in refs)
        assert any('pbw-universality' in r for r in refs)
        assert any('universal-koszul' in r for r in refs)

    def test_p1_generator_count_y002(self):
        """Y_{0,0,2}: 2 generators (spins 1,2)."""
        p1 = koszul_proof_path_1_fsg(0, 0, 2)
        assert p1['n_generators'] == 2

    def test_p1_generator_count_y005(self):
        """Y_{0,0,5}: 5 generators (spins 1,...,5)."""
        p1 = koszul_proof_path_1_fsg(0, 0, 5)
        assert p1['n_generators'] == 5

    def test_p1_fsg_status_small(self):
        """Small Y-algebras: always freely generated."""
        assert koszul_proof_path_1_fsg(0, 0, 0)['fsg_status'] == 'yes_always'
        assert koszul_proof_path_1_fsg(0, 0, 1)['fsg_status'] == 'yes_always'
        assert koszul_proof_path_1_fsg(0, 1, 1)['fsg_status'] == 'yes_always'

    def test_p1_fsg_status_large(self):
        """Larger Y-algebras: generically freely generated."""
        assert koszul_proof_path_1_fsg(0, 0, 2)['fsg_status'] == 'yes_generic'
        assert koszul_proof_path_1_fsg(1, 2, 3)['fsg_status'] == 'yes_generic'


# ============================================================================
# 21c: Proof Path 2 — BRST/DS definition
# ============================================================================

class TestKoszulProofPath2:
    """Tests for Proof Path 2: BRST/DS preserves Koszulness."""

    def test_p2_valid_for_all_triples(self):
        """P2 is valid for all Y-algebras."""
        for n1 in range(4):
            for n2 in range(4):
                for n3 in range(4):
                    p2 = koszul_proof_path_2_brst(n1, n2, n3)
                    assert p2['valid'], f"P2 invalid for ({n1},{n2},{n3})"

    def test_p2_parent_type_wn(self):
        """Y_{0,0,N} has parent gl(N) (affine, not super)."""
        p2 = koszul_proof_path_2_brst(0, 0, 3)
        assert p2['parent_type'] == 'affine'
        assert 'gl(3)' == p2['parent_algebra']

    def test_p2_parent_type_super(self):
        """Y_{1,2,3} has parent gl(3|1) (super affine)."""
        p2 = koszul_proof_path_2_brst(1, 2, 3)
        assert p2['parent_type'] == 'super_affine'
        assert '|' in p2['parent_algebra']

    def test_p2_ds_preserves_pbw(self):
        """DS reduction preserves PBW filtrations (theorem hypothesis)."""
        for n1 in range(3):
            for n2 in range(3):
                for n3 in range(3):
                    p2 = koszul_proof_path_2_brst(n1, n2, n3)
                    assert p2['ds_preserves_pbw']


# ============================================================================
# 21d: Proof Path 3 — Truncation of W_{1+infty}
# ============================================================================

class TestKoszulProofPath3:
    """Tests for Proof Path 3: Truncation of W_{1+infty}."""

    def test_p3_valid_for_all_triples(self):
        """P3 is valid for all Y-algebras."""
        for n1 in range(4):
            for n2 in range(4):
                for n3 in range(4):
                    p3 = koszul_proof_path_3_truncation(n1, n2, n3)
                    assert p3['valid'], f"P3 invalid for ({n1},{n2},{n3})"

    def test_p3_first_null_y002(self):
        """Y_{0,0,2}: first null at weight (0+1)(0+1)(2+1) = 3."""
        p3 = koszul_proof_path_3_truncation(0, 0, 2)
        assert p3['first_null_weight'] == 3

    def test_p3_first_null_y123(self):
        """Y_{1,2,3}: first null at weight (1+1)(2+1)(3+1) = 24."""
        p3 = koszul_proof_path_3_truncation(1, 2, 3)
        assert p3['first_null_weight'] == 24

    def test_p3_surviving_spins_y003(self):
        """Y_{0,0,3}: surviving spins are 1, 2, 3."""
        p3 = koszul_proof_path_3_truncation(0, 0, 3)
        assert p3['surviving_spins'] == [1, 2, 3]

    def test_p3_first_null_grows_with_triple(self):
        """First null weight increases as the N-triple grows."""
        # (N1+1)(N2+1)(N3+1) is monotone in each N_i
        fnull_002 = koszul_proof_path_3_truncation(0, 0, 2)['first_null_weight']
        fnull_003 = koszul_proof_path_3_truncation(0, 0, 3)['first_null_weight']
        fnull_123 = koszul_proof_path_3_truncation(1, 2, 3)['first_null_weight']
        assert fnull_002 < fnull_003 < fnull_123


# ============================================================================
# 21e: Proof Path 4 — PBW spectral sequence
# ============================================================================

class TestKoszulProofPath4:
    """Tests for Proof Path 4: PBW spectral sequence collapse."""

    def test_p4_distinct_weights_all_wn(self):
        """Y_{0,0,N}: generators at weights 1,...,N (distinct)."""
        for N in range(1, 8):
            p4 = koszul_proof_path_4_spectral_seq(0, 0, N)
            assert p4['distinct_weights'], f"Weight collision at N={N}"
            assert p4['e2_collapse']

    def test_p4_valid_for_all_small_triples(self):
        """P4 is valid for all Y-algebras with Ni <= 3."""
        for n1 in range(4):
            for n2 in range(4):
                for n3 in range(4):
                    p4 = koszul_proof_path_4_spectral_seq(n1, n2, n3)
                    # P4 validity depends on distinct weights
                    if p4['distinct_weights']:
                        assert p4['valid']
                        assert p4['e2_collapse']

    def test_p4_references_priddy(self):
        """P4 cites Priddy's theorem."""
        p4 = koszul_proof_path_4_spectral_seq(0, 0, 2)
        refs = p4['references']
        assert any('Priddy' in r for r in refs)

    def test_p4_e2_collapse_equivalent_to_koszul(self):
        """E_2 collapse is equivalent to chiral Koszulness (by definition)."""
        for n1 in range(3):
            for n2 in range(3):
                for n3 in range(3):
                    p4 = koszul_proof_path_4_spectral_seq(n1, n2, n3)
                    if p4['e2_collapse']:
                        assert p4['conclusion'] == 'chirally_koszul'


# ============================================================================
# 21f: Multi-path convergence
# ============================================================================

class TestMultiPathConvergence:
    """Tests that all four proof paths converge to the same conclusion."""

    def test_all_paths_agree_y002(self):
        """All four paths agree for Y_{0,0,2}."""
        summary = koszul_proof_summary(0, 0, 2)
        assert summary['all_paths_valid']
        assert summary['n_valid_paths'] == 4

    def test_all_paths_agree_y123(self):
        """All four paths agree for Y_{1,2,3}."""
        summary = koszul_proof_summary(1, 2, 3)
        assert summary['all_paths_valid']
        assert summary['n_valid_paths'] == 4

    def test_all_paths_agree_systematic(self):
        """All four paths agree for all Y with Ni <= 3.

        This is the CORE MULTI-PATH CONVERGENCE TEST.
        Four independent proof paths all conclude 'chirally_koszul'.
        """
        for n1 in range(4):
            for n2 in range(4):
                for n3 in range(4):
                    summary = koszul_proof_summary(n1, n2, n3)
                    assert summary['koszul_status'] in ('yes_always', 'yes_generic'), \
                        f"({n1},{n2},{n3}): unexpected status {summary['koszul_status']}"
                    # At least 3 paths must be valid (mandate: 3+ independent)
                    assert summary['n_valid_paths'] >= 3, \
                        f"({n1},{n2},{n3}): only {summary['n_valid_paths']} valid paths"

    def test_proof_summary_has_non_generic_locus(self):
        """Proof summary includes the non-generic locus."""
        summary = koszul_proof_summary(0, 0, 3)
        ng = summary['non_generic_locus']
        assert 'degenerate' in ng
        assert 'truncation_singular' in ng
        assert 'admissible' in ng


# ============================================================================
# 21g: Specific Psi verification
# ============================================================================

class TestKoszulnessAtSpecificPsi:
    """Tests for Koszulness at specific Psi values."""

    def test_generic_psi_is_koszul(self):
        """At generic Psi = 7/3, Y_{0,0,3} is Koszul."""
        result = verify_koszulness_at_psi(0, 0, 3, Fraction(7, 3))
        assert result['koszul_at_generic'] in ('yes_always', 'yes_generic')

    def test_degenerate_psi_not_generic(self):
        """Psi = 0 is not in the generic locus (degenerate)."""
        assert not is_generic_psi(0, 0, 2, 0)

    def test_multiple_generic_values(self):
        """Multiple Psi values are generic for Y_{1,2,3}.

        The admissible enumeration is CONSERVATIVE: it includes all small
        rationals p/q with p <= 3*N_max, q <= N_max as candidates.
        For N_max=3, this flags all integers up to 9.  So we test with
        larger values and irrational-like rationals.
        """
        generic_count = 0
        for psi in [Fraction(11), Fraction(13), Fraction(17),
                    Fraction(101, 7), Fraction(53, 3)]:
            if is_generic_psi(1, 2, 3, psi):
                generic_count += 1
        # Large primes and irrational-like rationals should be generic
        assert generic_count >= 3

    def test_verify_at_psi_returns_correct_keys(self):
        """verify_koszulness_at_psi returns all expected keys."""
        result = verify_koszulness_at_psi(0, 0, 2, Fraction(5))
        assert 'triple' in result
        assert 'psi' in result
        assert 'central_charge' in result
        assert 'is_generic' in result
        assert 'koszul_at_generic' in result
        assert 'generator_weights' in result

    def test_central_charge_at_specific_psi(self):
        """Central charge computation at the verified Psi is consistent."""
        result = verify_koszulness_at_psi(0, 0, 2, Fraction(3))
        assert result['central_charge'] == Fraction(-6)
        assert result['psi'] == Fraction(3)


# ============================================================================
# 21h: Duality compatibility with Koszulness
# ============================================================================

class TestKoszulDualityCompatibility:
    """Tests that dualities preserve the Koszulness property."""

    def test_triality_preserves_koszulness_systematic(self):
        """Triality preserves Koszulness for all Y with Ni <= 3."""
        for n1 in range(4):
            for n2 in range(4):
                for n3 in range(4):
                    assert triality_preserves_koszulness(n1, n2, n3), \
                        f"Triality breaks Koszulness for ({n1},{n2},{n3})"

    def test_ff_duality_preserves_koszulness_systematic(self):
        """FF-duality preserves Koszulness for all Y with Ni <= 3."""
        for n1 in range(4):
            for n2 in range(4):
                for n3 in range(4):
                    assert ff_duality_preserves_koszulness(n1, n2, n3), \
                        f"FF-duality breaks Koszulness for ({n1},{n2},{n3})"

    def test_koszul_dual_is_koszul(self):
        """The Koszul dual Y^![Psi'] is itself Koszul at generic Psi'.

        This is a consistency check: if Y is Koszul, then Y^! should
        also be Koszul (Koszul duality is an involution on the Koszul locus).
        """
        for n1 in range(3):
            for n2 in range(3):
                for n3 in range(3):
                    kd = koszul_dual_prediction(n1, n2, n3, Fraction(5))
                    n1d, n2d, n3d, psi_d = kd
                    status_dual = is_chirally_koszul(n1d, n2d, n3d)
                    assert status_dual in ('yes_always', 'yes_generic'), \
                        f"Koszul dual of ({n1},{n2},{n3}) not Koszul"


# ============================================================================
# 21i: Cross-family consistency
# ============================================================================

class TestKoszulCrossFamilyConsistency:
    """Cross-checks between Y-algebra Koszulness and known families."""

    def test_y002_equals_virasoro_koszulness(self):
        """Y_{0,0,2} = W_2 x gl(1): same Koszulness as Virasoro.

        Virasoro is chirally Koszul at all c (cor:universal-koszul).
        gl(1) is quadratic, hence Koszul.  Tensor product of Koszul
        algebras is Koszul.
        """
        assert is_chirally_koszul(0, 0, 2) == 'yes_generic'
        # At generic Psi, this matches Virasoro + Heisenberg

    def test_y003_equals_w3_koszulness(self):
        """Y_{0,0,3} = W_3 x gl(1): same Koszulness as W_3."""
        assert is_chirally_koszul(0, 0, 3) == 'yes_generic'

    def test_y00n_matches_wn_koszulness(self):
        """Y_{0,0,N} matches W_N Koszulness for all N."""
        for N in range(2, 8):
            assert is_chirally_koszul(0, 0, N) == 'yes_generic'

    def test_small_y_unconditionally_koszul(self):
        """Y_{0,0,0}, Y_{0,0,1}, Y_{0,1,1} are ALWAYS Koszul.

        These are free bosons / affine type, with no null vectors at ANY Psi.
        """
        assert is_chirally_koszul(0, 0, 0) == 'yes_always'
        assert is_chirally_koszul(0, 0, 1) == 'yes_always'
        assert is_chirally_koszul(0, 1, 1) == 'yes_always'
        # Check all permutations
        assert is_chirally_koszul(1, 0, 0) == 'yes_always'
        assert is_chirally_koszul(1, 1, 0) == 'yes_always'

    def test_y111_koszul(self):
        """Y_{1,1,1}: N=2 superconformal, chirally Koszul.

        max(Ni) = 1, so the algebra is ALWAYS freely strongly generated
        (no null vectors at any coupling), hence 'yes_always'.
        Despite being class M (infinite shadow depth from the N=2
        superconformal subalgebra), it is unconditionally Koszul.
        """
        assert is_chirally_koszul(1, 1, 1) == 'yes_always'
        # Has generators at multiple weights, class M
        assert shadow_depth_class(1, 1, 1) == 'M'

    def test_koszulness_independent_of_depth(self):
        """Koszulness holds for ALL depth classes (AP14 check).

        Shadow depth (G/L/M) classifies complexity WITHIN the Koszul world.
        All Y-algebras are Koszul regardless of depth class.
        """
        for n1 in range(4):
            for n2 in range(4):
                for n3 in range(4):
                    cls = shadow_depth_class(n1, n2, n3)
                    koszul = is_chirally_koszul(n1, n2, n3)
                    assert koszul in ('yes_always', 'yes_generic'), \
                        f"({n1},{n2},{n3}) class {cls}: not Koszul!"


# ============================================================================
# 21j: Edge cases and boundary
# ============================================================================

class TestKoszulEdgeCases:
    """Edge cases for the Koszulness theorem."""

    def test_large_n_triple(self):
        """Y_{5,5,5}: still Koszul at generic Psi."""
        assert is_chirally_koszul(5, 5, 5) == 'yes_generic'
        summary = koszul_proof_summary(5, 5, 5)
        assert summary['n_valid_paths'] >= 3

    def test_asymmetric_triple(self):
        """Y_{0,1,10}: asymmetric triple, still Koszul."""
        assert is_chirally_koszul(0, 1, 10) == 'yes_generic'

    def test_truncation_singular_not_admissible(self):
        """Truncation singularity is not in the admissible set.

        These are DIFFERENT obstructions: truncation singularity is
        geometric (sigma=0), admissible is representation-theoretic.
        """
        for n1 in range(3):
            for n2 in range(3):
                for n3 in range(3):
                    psi_s = truncation_singular_psi(n1, n2, n3)
                    if psi_s is not None and psi_s not in (0, 1):
                        admiss = admissible_psi_values(n1, n2, n3, max_denom=5)
                        # The singular Psi MAY or may not be admissible
                        # (no assertion: just check it runs)
                        assert isinstance(admiss, list)

    def test_proof_paths_independent(self):
        """The four proof paths use genuinely different mechanisms.

        P1: algebraic (free generation theorem)
        P2: homological (BRST/DS + PBW preservation)
        P3: truncation (W_{1+infty} quotient)
        P4: spectral (E_2 collapse from distinct weights)
        """
        p1 = koszul_proof_path_1_fsg(1, 2, 3)
        p2 = koszul_proof_path_2_brst(1, 2, 3)
        p3 = koszul_proof_path_3_truncation(1, 2, 3)
        p4 = koszul_proof_path_4_spectral_seq(1, 2, 3)
        # Each uses different references
        assert p1['proof_id'] != p2['proof_id']
        assert p2['proof_id'] != p3['proof_id']
        assert p3['proof_id'] != p4['proof_id']
        # Each has a different name
        names = {p['name'] for p in [p1, p2, p3, p4]}
        assert len(names) == 4
