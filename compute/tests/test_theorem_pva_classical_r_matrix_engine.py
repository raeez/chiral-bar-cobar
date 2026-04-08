r"""Tests for PVA classical r-matrix extraction and KZ25 bridge.

THEOREM (KZ25 classical-quantum bridge):
The classical r-matrix extracted from the PVA lambda-bracket is the
genus-0 binary seed of the shadow obstruction tower:
    r^{cl}(z) = Res^{coll}_{0,2}(\Theta_A)|_{\hbar=0}

VERIFICATION PATHS (3+ per claim, per CLAUDE.md multi-path mandate):

    Path 1 (PVA extraction):    lambda-bracket -> OPE modes -> r-matrix poles
    Path 2 (AP19 cross-check):  OPE poles -> d-log shift -> collision poles
    Path 3 (rmatrix_landscape): compare with existing collision-residue engine
    Path 4 (CYBE):              classical Yang-Baxter from Jacobi identity
    Path 5 (kappa consistency): scalar trace of r-matrix matches kappa(A)

All formulas computed from first principles (AP1, AP3).
AP44 divided-power convention verified at every step.
Cross-family consistency verified (AP10).

References:
    AP19 (CLAUDE.md): r-matrix pole one below OPE
    AP44 (CLAUDE.md): divided-power convention lambda^{(n)} = lambda^n / n!
    rmatrix_landscape.py: collision-residue r-matrices
    collision_residue_identification.py: BinaryRMatrix
    w3_lambda_brackets.py: W_3 lambda-brackets
"""

import pytest
from fractions import Fraction

from compute.lib.theorem_pva_classical_r_matrix_engine import (
    # PVA data
    PVALambdaBracket,
    PVAClassicalRMatrix,
    # Family constructors
    heisenberg_pva,
    affine_sl2_pva,
    virasoro_pva,
    w3_pva,
    # AP44 verification
    verify_ap44_convention,
    # CYBE
    verify_cybe_heisenberg,
    verify_cybe_sl2,
    verify_cybe_virasoro,
    # Lambda-Jacobi
    verify_lambda_jacobi_heisenberg,
    verify_lambda_jacobi_sl2_scalar,
    verify_lambda_jacobi_virasoro_scalar,
    # Quantum corrections
    quantum_correction_class,
    # Cross-checks
    cross_check_with_rmatrix_landscape,
    kappa_from_pva,
    # Skew-symmetry and parity
    verify_skew_symmetry_scalar,
    verify_bosonic_parity,
    # KZ25 summary
    kz25_bridge_summary,
    # Internals
    _factorial,
)


# ========================================================================
# Section 1: PVA lambda-bracket extraction
# ========================================================================

class TestHeisenbergPVA:
    """Test Heisenberg PVA lambda-bracket and r-matrix."""

    def test_heisenberg_bracket_structure(self):
        """Heisenberg: {J_lambda J} = k*lambda has exactly one nonzero mode."""
        pva = heisenberg_pva(k=Fraction(3))
        bracket = pva.get_bracket("J", "J")
        assert 1 in bracket
        assert bracket[1] == Fraction(3)
        # c_0 should be absent (no constant term)
        assert bracket.get(0, Fraction(0)) == Fraction(0)

    def test_heisenberg_max_pole_order(self):
        """Heisenberg OPE: J(z)J(w) ~ k/(z-w)^2, so max pole = 2."""
        pva = heisenberg_pva(k=Fraction(1))
        assert pva.max_pole_order("J", "J") == 2

    def test_heisenberg_r_matrix_ope_poles(self):
        """Heisenberg PVA r-matrix: OPE pole at order 2 with coefficient k."""
        k = Fraction(5)
        pva = heisenberg_pva(k=k)
        rmat = PVAClassicalRMatrix(pva)
        ope_poles = rmat.ope_poles[("J", "J")]
        assert 2 in ope_poles
        assert ope_poles[2] == k  # OPE mode J_{(1)}J = 1! * k = k

    def test_heisenberg_collision_poles(self):
        """After AP19 d-log absorption: pole 2 -> pole 1."""
        k = Fraction(7)
        pva = heisenberg_pva(k=k)
        rmat = PVAClassicalRMatrix(pva)
        coll = rmat.coll_poles[("J", "J")]
        assert coll == {1: k}

    def test_heisenberg_ap19(self):
        """AP19: collision max pole = OPE max pole - 1."""
        pva = heisenberg_pva(k=Fraction(1))
        rmat = PVAClassicalRMatrix(pva)
        assert rmat.ope_max_pole("J", "J") == 2
        assert rmat.coll_max_pole("J", "J") == 1
        assert rmat.verify_ap19()[("J", "J")] is True


class TestAffineSl2PVA:
    """Test affine sl_2 PVA lambda-bracket and r-matrix."""

    def test_sl2_ef_bracket(self):
        """{e_lambda f} = h + k*lambda: c_0 = h, c_1 = k."""
        k = Fraction(3)
        pva = affine_sl2_pva(k=k)
        bracket = pva.get_bracket("e", "f")
        # c_0 is field-valued (h)
        assert bracket[0] == (Fraction(1), "h")
        # c_1 is the level k
        assert bracket[1] == k

    def test_sl2_hh_bracket(self):
        """{h_lambda h} = 2k*lambda: c_1 = 2k."""
        k = Fraction(4)
        pva = affine_sl2_pva(k=k)
        bracket = pva.get_bracket("h", "h")
        assert bracket[1] == 2 * k

    def test_sl2_he_bracket(self):
        """{h_lambda e} = 2e: c_0 = 2e."""
        pva = affine_sl2_pva(k=Fraction(1))
        bracket = pva.get_bracket("h", "e")
        assert bracket[0] == (Fraction(2), "e")

    def test_sl2_ee_vanishes(self):
        """{e_lambda e} = 0."""
        pva = affine_sl2_pva(k=Fraction(1))
        bracket = pva.get_bracket("e", "e")
        assert bracket == {}

    def test_sl2_max_pole_orders(self):
        """sl_2: diagonal channels pole 2, off-diagonal pole 1."""
        pva = affine_sl2_pva(k=Fraction(1))
        # hh channel: {h_lambda h} = 2k*lambda -> c_1 nonzero -> max mode 1 -> pole 2
        assert pva.max_pole_order("h", "h") == 2
        # ef channel: {e_lambda f} = h + k*lambda -> c_1 nonzero -> pole 2
        assert pva.max_pole_order("e", "f") == 2
        # he channel: {h_lambda e} = 2e -> c_0 nonzero -> pole 1
        assert pva.max_pole_order("h", "e") == 1

    def test_sl2_off_diagonal_drops_after_dlog(self):
        """Off-diagonal simple pole (order 1) -> order 0 -> drops after d-log."""
        pva = affine_sl2_pva(k=Fraction(1))
        rmat = PVAClassicalRMatrix(pva)
        # he channel: OPE max pole = 1, collision max pole = 0
        assert rmat.coll_max_pole("h", "e") == 0

    def test_sl2_ap19_all_channels(self):
        """AP19 verified for all sl_2 channels."""
        pva = affine_sl2_pva(k=Fraction(1))
        rmat = PVAClassicalRMatrix(pva)
        ap19 = rmat.verify_ap19()
        for pair, passed in ap19.items():
            assert passed, f"AP19 failed for channel {pair}"

    def test_sl2_critical_level_raises(self):
        """Critical level k = -2 should raise ValueError."""
        with pytest.raises(ValueError, match="Critical level"):
            affine_sl2_pva(k=Fraction(-2))


class TestVirasoroPVA:
    """Test Virasoro PVA lambda-bracket and r-matrix."""

    def test_virasoro_bracket_structure(self):
        """{T_lambda T} = dT + 2T*lambda + (c/12)*lambda^3."""
        c = Fraction(26)
        pva = virasoro_pva(c=c)
        bracket = pva.get_bracket("T", "T")
        # c_0 = dT (field-valued)
        assert bracket[0] == (Fraction(1), "dT")
        # c_1 = 2T
        assert bracket[1] == (Fraction(2), "T")
        # c_3 = c/12
        assert bracket[3] == c / 12
        # c_2 absent (no lambda^2 term)
        assert 2 not in bracket

    def test_virasoro_max_pole_order(self):
        """Virasoro OPE has max pole order 4 (from T_{(3)}T = c/2)."""
        pva = virasoro_pva(c=Fraction(1))
        assert pva.max_pole_order("T", "T") == 4

    def test_virasoro_ope_poles(self):
        """Virasoro OPE poles: {4: c/2, 2: 2T, 1: dT}."""
        c = Fraction(12)
        pva = virasoro_pva(c=c)
        rmat = PVAClassicalRMatrix(pva)
        ope = rmat.ope_poles[("T", "T")]
        # Pole order 4: from c_3 = c/12.  OPE mode = 3! * c/12 = 6 * c/12 = c/2
        assert ope[4] == c / 2
        # Pole order 2: from c_1 = 2T.  OPE mode = 1! * 2 = 2
        assert ope[2] == (Fraction(2), "T")
        # Pole order 1: from c_0 = dT.  OPE mode = 0! * 1 = 1
        assert ope[1] == (Fraction(1), "dT")

    def test_virasoro_collision_poles(self):
        """After AP19: poles {4,2,1} -> {3,1,0}. Order 0 drops."""
        c = Fraction(24)
        pva = virasoro_pva(c=c)
        rmat = PVAClassicalRMatrix(pva)
        coll = rmat.coll_poles[("T", "T")]
        # Pole 3: from OPE pole 4 (c/2)
        assert 3 in coll
        assert coll[3] == c / 2
        # Pole 1: from OPE pole 2 (2T)
        assert 1 in coll
        assert coll[1] == (Fraction(2), "T")
        # Pole 0 (from OPE pole 1, dT) should be ABSENT (drops)
        assert 0 not in coll

    def test_virasoro_ap19(self):
        """AP19: collision max pole 3 = OPE max pole 4 - 1."""
        pva = virasoro_pva(c=Fraction(1))
        rmat = PVAClassicalRMatrix(pva)
        assert rmat.ope_max_pole("T", "T") == 4
        assert rmat.coll_max_pole("T", "T") == 3
        assert rmat.verify_ap19()[("T", "T")] is True

    def test_virasoro_bosonic_parity(self):
        """Virasoro collision poles are all odd: {3, 1}."""
        pva = virasoro_pva(c=Fraction(1))
        result = verify_bosonic_parity(pva, "T")
        assert result['all_odd'] is True
        assert set(result['odd_poles']) == {1, 3}
        assert result['even_poles'] == []


class TestW3PVA:
    """Test W_3 PVA lambda-bracket and r-matrix."""

    def test_w3_tt_bracket_matches_virasoro(self):
        """W_3 TT bracket is identical to Virasoro TT bracket."""
        c = Fraction(50)
        vir = virasoro_pva(c=c)
        w3 = w3_pva(c=c)
        assert vir.get_bracket("T", "T") == w3.get_bracket("T", "T")

    def test_w3_tw_bracket_primary(self):
        """{T_lambda W} = dW + 3W*lambda (W is primary of weight 3)."""
        w3 = w3_pva(c=Fraction(1))
        bracket = w3.get_bracket("T", "W")
        assert bracket[0] == (Fraction(1), "dW")
        assert bracket[1] == (Fraction(3), "W")

    def test_w3_ww_scalar_coefficient(self):
        """WW bracket scalar: c_5 = c/360 (AP44: W_{(5)}W/5! = (c/3)/120)."""
        c = Fraction(360)
        w3 = w3_pva(c=c)
        bracket = w3.get_bracket("W", "W")
        assert bracket[5] == c / 360
        assert bracket[5] == Fraction(1)  # 360/360 = 1

    def test_w3_ww_max_pole_order(self):
        """W_3 WW OPE: max pole order = 6 (from mode W_{(5)}W)."""
        w3 = w3_pva(c=Fraction(1))
        assert w3.max_pole_order("W", "W") == 6

    def test_w3_ww_collision_max_pole(self):
        """After AP19: WW collision max pole = 6 - 1 = 5."""
        w3 = w3_pva(c=Fraction(1))
        rmat = PVAClassicalRMatrix(w3)
        assert rmat.coll_max_pole("W", "W") == 5

    def test_w3_tw_ope_max_pole(self):
        """TW OPE: max pole order = 2 (from T_{(1)}W = 3W)."""
        w3 = w3_pva(c=Fraction(1))
        assert w3.max_pole_order("T", "W") == 2


# ========================================================================
# Section 2: AP44 divided-power convention
# ========================================================================

class TestAP44Convention:
    """Verify the AP44 divided-power convention: c_n = a_{(n)}b / n!."""

    def test_ap44_heisenberg_mode1(self):
        """Heisenberg: J_{(1)}J = k. Lambda coeff c_1 = k/1! = k."""
        k = Fraction(5)
        pva = heisenberg_pva(k=k)
        result = verify_ap44_convention(
            pva, "J", "J", n=1,
            expected_ope_mode=k,
            expected_lambda_coeff=k,
        )
        assert result['convention_correct'] is True

    def test_ap44_virasoro_mode3(self):
        """Virasoro: T_{(3)}T = c/2. Lambda coeff c_3 = (c/2)/3! = c/12."""
        c = Fraction(24)
        pva = virasoro_pva(c=c)
        result = verify_ap44_convention(
            pva, "T", "T", n=3,
            expected_ope_mode=c / 2,           # T_{(3)}T = c/2
            expected_lambda_coeff=c / 12,       # c_3 = (c/2)/6 = c/12
        )
        assert result['convention_correct'] is True

    def test_ap44_virasoro_mode1(self):
        """Virasoro: T_{(1)}T = 2T. Lambda coeff c_1 = 2T/1! = 2T."""
        pva = virasoro_pva(c=Fraction(1))
        result = verify_ap44_convention(
            pva, "T", "T", n=1,
            expected_ope_mode=(Fraction(2), "T"),
            expected_lambda_coeff=(Fraction(2), "T"),
        )
        # For n=1, 1! = 1, so OPE mode = lambda coeff
        assert result['convention_correct'] is True

    def test_ap44_w3_ww_mode5(self):
        """W_3: W_{(5)}W = c/3. Lambda coeff c_5 = (c/3)/5! = c/360."""
        c = Fraction(720)
        pva = w3_pva(c=c)
        result = verify_ap44_convention(
            pva, "W", "W", n=5,
            expected_ope_mode=c / 3,            # W_{(5)}W = c/3
            expected_lambda_coeff=c / 360,       # c_5 = (c/3)/120 = c/360
        )
        assert result['convention_correct'] is True

    def test_ap44_factorial_values(self):
        """Verify factorial computation: 0!=1, 1!=1, 3!=6, 5!=120."""
        assert _factorial(0) == Fraction(1)
        assert _factorial(1) == Fraction(1)
        assert _factorial(3) == Fraction(6)
        assert _factorial(5) == Fraction(120)


# ========================================================================
# Section 3: CYBE verification
# ========================================================================

class TestCYBE:
    """Verify classical Yang-Baxter equation for standard families."""

    def test_cybe_heisenberg(self):
        """Heisenberg: CYBE trivially satisfied (abelian)."""
        result = verify_cybe_heisenberg(k=Fraction(1))
        assert result['cybe_satisfied'] is True
        assert result['shadow_class'] == 'G (Gaussian)'

    def test_cybe_sl2_numerical(self):
        """sl_2: CYBE verified numerically in fundamental representation.

        The CYBE for r(z) = Omega/z decomposes into two conditions:
          (A) [O12, O23] + [O13, O23] = 0
          (B) [O12, O13] - [O13, O23] = 0
        Both must vanish independently.
        """
        result = verify_cybe_sl2(k=Fraction(1))
        assert result['cybe_satisfied'] is True
        assert result['condition_A_norm'] < 1e-12
        assert result['condition_B_norm'] < 1e-12

    def test_cybe_sl2_various_levels(self):
        """sl_2 CYBE holds at various levels k.

        The CYBE conditions are ALGEBRAIC (independent of k), since
        r(z) = k*Omega/z and the commutators scale as k^2 on both sides.
        """
        for k_val in [1, 2, 5, 10, -1]:
            result = verify_cybe_sl2(k=Fraction(k_val))
            assert result['cybe_satisfied'] is True, f"CYBE failed at k={k_val}"

    def test_cybe_virasoro(self):
        """Virasoro: CYBE from lambda-Jacobi identity."""
        result = verify_cybe_virasoro(c=Fraction(26))
        assert result['cybe_satisfied'] is True
        assert result['shadow_class'] == 'M (mixed, r_max = infinity)'
        assert result['quantum_corrections'] is True


# ========================================================================
# Section 4: Lambda-Jacobi identity
# ========================================================================

class TestLambdaJacobi:
    """Verify lambda-Jacobi identity for standard PVAs."""

    def test_jacobi_heisenberg(self):
        """Heisenberg: Jacobi trivially satisfied (all terms vanish)."""
        result = verify_lambda_jacobi_heisenberg(k=Fraction(1))
        assert result['jacobi_satisfied'] is True

    def test_jacobi_sl2_efh(self):
        """sl_2: Jacobi on efh channel gives 2k(lambda+mu) = 2k(lambda+mu)."""
        result = verify_lambda_jacobi_sl2_scalar(k=Fraction(3))
        assert result['jacobi_satisfied'] is True
        assert result['lhs_numerical'] == result['rhs_numerical']

    def test_jacobi_sl2_multiple_levels(self):
        """sl_2 Jacobi holds at various levels."""
        for k_val in [1, 2, 7, Fraction(1, 2)]:
            result = verify_lambda_jacobi_sl2_scalar(k=Fraction(k_val))
            assert result['jacobi_satisfied'] is True

    def test_jacobi_virasoro_scalar(self):
        """Virasoro: scalar Jacobi check passes."""
        result = verify_lambda_jacobi_virasoro_scalar(c=Fraction(26))
        assert result['jacobi_satisfied'] is True


# ========================================================================
# Section 5: Quantum correction classification
# ========================================================================

class TestQuantumCorrections:
    """Verify quantum correction structure by shadow class."""

    def test_heisenberg_class_g(self):
        """Heisenberg is class G: no quantum corrections."""
        pva = heisenberg_pva(k=Fraction(1))
        qc = quantum_correction_class(pva)
        assert qc['class'] == 'G'
        assert qc['shadow_depth'] == 2
        assert qc['quantum_corrections'] is False

    def test_sl2_class_l(self):
        """Affine sl_2 is class L: no corrections at tree level."""
        pva = affine_sl2_pva(k=Fraction(1))
        qc = quantum_correction_class(pva)
        assert qc['class'] == 'L'
        assert qc['shadow_depth'] == 3
        assert qc['quantum_corrections_tree'] is False

    def test_virasoro_class_m(self):
        """Virasoro is class M: quantum corrections present."""
        pva = virasoro_pva(c=Fraction(1))
        qc = quantum_correction_class(pva)
        assert qc['class'] == 'M'
        assert qc['shadow_depth'] == float('inf')
        assert qc['quantum_corrections'] is True

    def test_w3_class_m(self):
        """W_3 is class M: quantum corrections present."""
        pva = w3_pva(c=Fraction(1))
        qc = quantum_correction_class(pva)
        assert qc['class'] == 'M'
        assert qc['quantum_corrections'] is True


# ========================================================================
# Section 6: Kappa consistency
# ========================================================================

class TestKappaConsistency:
    """Verify kappa(A) extracted from PVA matches known values."""

    def test_kappa_heisenberg(self):
        """kappa(H_k) = k."""
        for k_val in [1, 3, 7, Fraction(1, 2)]:
            pva = heisenberg_pva(k=Fraction(k_val))
            assert kappa_from_pva(pva) == Fraction(k_val)

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2."""
        for c_val in [1, 12, 26, Fraction(1, 2)]:
            pva = virasoro_pva(c=Fraction(c_val))
            assert kappa_from_pva(pva) == Fraction(c_val) / 2

    def test_kappa_sl2(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        for k_val in [1, 2, 5]:
            k = Fraction(k_val)
            pva = affine_sl2_pva(k=k)
            expected = Fraction(3) * (k + 2) / Fraction(4)
            assert kappa_from_pva(pva) == expected

    def test_kappa_w3(self):
        """kappa(W_3) = c/2 (same as Virasoro, from TT bracket)."""
        c = Fraction(50)
        pva = w3_pva(c=c)
        assert kappa_from_pva(pva) == c / 2


# ========================================================================
# Section 7: Cross-checks with existing engines
# ========================================================================

class TestCrossChecks:
    """Cross-check PVA r-matrix with rmatrix_landscape.py data."""

    def test_heisenberg_cross_check(self):
        """Heisenberg collision poles match rmatrix_landscape: {1: k}."""
        k = Fraction(3)
        pva = heisenberg_pva(k=k)
        result = cross_check_with_rmatrix_landscape(pva, k_value=k)
        assert result['ap19_verified'] is True
        check = result['cross_checks'][("J", "J")]
        assert check['match'] is True

    def test_virasoro_scalar_cross_check(self):
        """Virasoro scalar collision pole matches: {3: c/2}."""
        c = Fraction(26)
        pva = virasoro_pva(c=c)
        result = cross_check_with_rmatrix_landscape(pva, c_value=c)
        assert result['ap19_verified'] is True
        check = result['cross_checks'][("T", "T")]
        assert check['match'] is True

    def test_ap19_across_all_families(self):
        """AP19 holds for all four standard families."""
        families = [
            heisenberg_pva(k=Fraction(1)),
            affine_sl2_pva(k=Fraction(1)),
            virasoro_pva(c=Fraction(1)),
            w3_pva(c=Fraction(1)),
        ]
        for pva in families:
            rmat = PVAClassicalRMatrix(pva)
            for pair, passed in rmat.verify_ap19().items():
                assert passed, f"AP19 failed for {pva.name} channel {pair}"


# ========================================================================
# Section 8: Skew-symmetry and bosonic parity
# ========================================================================

class TestSkewSymmetryParity:
    """Verify skew-symmetry and bosonic parity of r-matrices."""

    def test_heisenberg_skew_symmetry(self):
        """Heisenberg r(z) = k/z: odd function, skew-symmetric."""
        pva = heisenberg_pva(k=Fraction(3))
        result = verify_skew_symmetry_scalar(pva, "J", "J")
        assert result['skew_symmetric'] is True

    def test_heisenberg_bosonic_parity(self):
        """Heisenberg collision poles: {1} (all odd)."""
        pva = heisenberg_pva(k=Fraction(1))
        result = verify_bosonic_parity(pva, "J")
        assert result['all_odd'] is True

    def test_virasoro_bosonic_parity(self):
        """Virasoro collision poles: {3, 1} (all odd)."""
        pva = virasoro_pva(c=Fraction(1))
        result = verify_bosonic_parity(pva, "T")
        assert result['all_odd'] is True
        assert sorted(result['odd_poles']) == [1, 3]


# ========================================================================
# Section 9: KZ25 bridge summary
# ========================================================================

class TestKZ25Bridge:
    """Test the full KZ25 deformation-quantization bridge summary."""

    def test_kz25_heisenberg(self):
        """KZ25 bridge for Heisenberg: class G, kappa = k, no corrections."""
        k = Fraction(5)
        pva = heisenberg_pva(k=k)
        summary = kz25_bridge_summary(pva, k_value=k)
        assert summary['algebra'] == 'Heisenberg'
        assert summary['kappa'] == k
        assert summary['shadow_class'] == 'G'
        assert summary['quantum_corrections'] is False
        assert summary['ap19_all_pass'] is True

    def test_kz25_virasoro(self):
        """KZ25 bridge for Virasoro: class M, kappa = c/2, corrections present."""
        c = Fraction(26)
        pva = virasoro_pva(c=c)
        summary = kz25_bridge_summary(pva, c_value=c)
        assert summary['algebra'] == 'Virasoro'
        assert summary['kappa'] == c / 2
        assert summary['shadow_class'] == 'M'
        assert summary['quantum_corrections'] is True
        assert summary['ap19_all_pass'] is True

    def test_kz25_sl2(self):
        """KZ25 bridge for sl_2: class L, kappa = 3(k+2)/4."""
        k = Fraction(1)
        pva = affine_sl2_pva(k=k)
        summary = kz25_bridge_summary(pva, k_value=k)
        assert summary['algebra'] == 'Affine sl_2'
        assert summary['kappa'] == Fraction(3) * (k + 2) / Fraction(4)
        assert summary['shadow_class'] == 'L'
        assert summary['ap19_all_pass'] is True

    def test_kz25_w3(self):
        """KZ25 bridge for W_3: class M, kappa = c/2."""
        c = Fraction(100)
        pva = w3_pva(c=c)
        summary = kz25_bridge_summary(pva, c_value=c)
        assert summary['algebra'] == 'W_3'
        assert summary['kappa'] == c / 2
        assert summary['shadow_class'] == 'M'
        assert summary['quantum_corrections'] is True


# ========================================================================
# Section 10: Multi-path verification — comprehensive consistency
# ========================================================================

class TestMultiPathVerification:
    """Multi-path consistency checks across all families."""

    def test_heisenberg_three_paths(self):
        """Heisenberg r-matrix verified via 3 independent paths.

        Path 1: PVA lambda-bracket -> c_1 = k -> OPE mode k -> pole {2: k}
        Path 2: AP19 shift -> collision pole {1: k}
        Path 3: kappa consistency -> kappa(H_k) = k = scalar trace
        """
        k = Fraction(7)
        pva = heisenberg_pva(k=k)
        rmat = PVAClassicalRMatrix(pva)

        # Path 1: PVA extraction
        bracket = pva.get_bracket("J", "J")
        assert bracket[1] == k

        # Path 2: AP19 shift
        assert rmat.coll_poles[("J", "J")] == {1: k}

        # Path 3: kappa consistency
        assert kappa_from_pva(pva) == k

    def test_virasoro_three_paths(self):
        """Virasoro r-matrix verified via 3 independent paths.

        Path 1: PVA lambda-bracket -> c_3 = c/12 -> OPE mode c/2 -> pole {4: c/2}
        Path 2: AP19 shift -> collision pole {3: c/2}
        Path 3: kappa = c/2 from the scalar leading pole coefficient
        """
        c = Fraction(12)
        pva = virasoro_pva(c=c)
        rmat = PVAClassicalRMatrix(pva)

        # Path 1: PVA extraction
        bracket = pva.get_bracket("T", "T")
        c_3 = bracket[3]
        assert c_3 == c / 12  # AP44 divided power
        ope_mode_3 = _factorial(3) * c_3  # = 6 * c/12 = c/2
        assert ope_mode_3 == c / 2

        # Path 2: AP19 shift gives pole 3 with coeff c/2
        scalar_coll = rmat.scalar_coll_poles("T", "T")
        assert scalar_coll[3] == c / 2

        # Path 3: kappa
        assert kappa_from_pva(pva) == c / 2

    def test_sl2_three_paths(self):
        """sl_2 r-matrix verified via 3 independent paths.

        Path 1: PVA bracket -> {h_lambda h} = 2k*lambda -> diagonal pole
        Path 2: AP19 -> diagonal collision pole {1: 2k}
        Path 3: kappa = 3(k+2)/4 from formula
        """
        k = Fraction(3)
        pva = affine_sl2_pva(k=k)
        rmat = PVAClassicalRMatrix(pva)

        # Path 1: bracket coefficient
        hh_bracket = pva.get_bracket("h", "h")
        assert hh_bracket[1] == 2 * k

        # Path 2: collision pole
        hh_coll = rmat.scalar_coll_poles("h", "h")
        assert hh_coll == {1: 2 * k}

        # Path 3: kappa
        expected_kappa = Fraction(3) * (k + 2) / Fraction(4)
        assert kappa_from_pva(pva) == expected_kappa

    def test_ap44_across_families(self):
        """AP44 divided-power convention holds across all families.

        For each family, verify: OPE mode = n! * lambda-bracket coefficient.
        """
        # Heisenberg: J_{(1)}J = k = 1! * k
        k = Fraction(5)
        pva_h = heisenberg_pva(k=k)
        ope_h = pva_h.ope_mode("J", "J", 1)
        assert ope_h == k  # 1! * k = k

        # Virasoro: T_{(3)}T = c/2 = 3! * (c/12)
        c = Fraction(48)
        pva_v = virasoro_pva(c=c)
        ope_v = pva_v.ope_mode("T", "T", 3)
        assert ope_v == c / 2  # 6 * c/12 = c/2

        # W_3: W_{(5)}W = c/3 = 5! * (c/360)
        pva_w = w3_pva(c=c)
        ope_w = pva_w.ope_mode("W", "W", 5)
        assert ope_w == c / 3  # 120 * c/360 = c/3

    def test_shadow_class_determines_corrections(self):
        """Shadow class determines quantum correction structure:
        G -> none, L -> none at tree, M -> nonzero."""
        families = {
            'Heisenberg': (heisenberg_pva(Fraction(1)), False),
            'sl_2': (affine_sl2_pva(Fraction(1)), False),
            'Virasoro': (virasoro_pva(Fraction(1)), True),
            'W_3': (w3_pva(Fraction(1)), True),
        }
        for name, (pva, has_corrections) in families.items():
            qc = quantum_correction_class(pva)
            if name in ('Heisenberg',):
                assert qc['quantum_corrections'] is False, f"{name} should have no corrections"
            elif name in ('sl_2',):
                assert qc['quantum_corrections_tree'] is False, f"{name} should have no tree corrections"
            else:
                assert qc['quantum_corrections'] is True, f"{name} should have corrections"
