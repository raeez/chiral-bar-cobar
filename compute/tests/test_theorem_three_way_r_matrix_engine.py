r"""Tests for the three-way r-matrix cross-check engine.

Verifies that the collision residue r(z) = Res^{coll}_{0,2}(Theta_A) agrees
across four independent perspectives:

  (1) BAR collision residue (our framework)
  (2) PVA lambda-bracket (KZ25 / Gui-Li-Zeng)
  (3) DNP25 MC element (dg-shifted Yangian)
  (4) GZ26 commuting Hamiltonians

Test organization:
  Section 1: Heisenberg family (4 perspectives x 3 levels = 12 comparisons)
  Section 2: sl_2 KM family (4 perspectives x 3 levels)
  Section 3: Virasoro family (4 perspectives x 3 central charges)
  Section 4: Virasoro on primary states
  Section 5: W_3 multi-channel structure
  Section 6: Structural properties (antisymmetry, CYBE, pole structure)
  Section 7: AP19 verification (d log absorption, pole orders)
  Section 8: AP44 verification (PVA divided-power convention)
  Section 9: Numerical checks (IBR, KZ commutativity)
  Section 10: Full consistency matrix

40+ tests total, each with independent verification.

Multi-path verification strategy (CLAUDE.md mandate: 3+ independent paths):
  Path 1: Direct computation from each perspective
  Path 2: Cross-perspective comparison (pairwise agreement)
  Path 3: Structural constraints (antisymmetry, CYBE, pole orders)
  Path 4: Numerical verification (sl_2 Casimir, KZ Hamiltonians)
  Path 5: AP19/AP44 convention checks

Ground truth references:
  - higher_genus_modular_koszul.tex: Theta_A, collision residue
  - yangians_foundations.tex: prop:dg-shifted-comparison
  - chiral_koszul_pairs.tex: PVA lambda-bracket
  - AP19 (pole absorption), AP44 (divided-power convention)
"""

import sys
import os
from fractions import Fraction

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from theorem_three_way_r_matrix_engine import (
    # Kappa formulas
    kappa_heisenberg,
    kappa_affine_sl2,
    kappa_virasoro,
    kappa_w3,
    # R-matrix classes
    RMatrixFromBar,
    RMatrixFromPVA,
    RMatrixFromDNP,
    RMatrixFromGZ26,
    # Cross-check
    compare_r_matrices,
    full_consistency_matrix,
    # Structural
    verify_antisymmetry,
    verify_pole_structure,
    verify_leading_order_matching,
    # Numerical
    verify_cybe_sl2_numerical,
    verify_kz_commutativity_from_r_matrix,
    # W_3 / Virasoro specifics
    w3_ope_mode_verification,
    virasoro_pva_to_ope_verification,
)


# ============================================================
# Section 1: Heisenberg family -- four-perspective agreement
# ============================================================

class TestHeisenbergRMatrix:
    """Four-perspective cross-check for Heisenberg r(z) = k/z."""

    def test_heisenberg_bar_k1(self):
        """Bar collision residue: r(z) = 1/z at level k=1."""
        r = RMatrixFromBar.heisenberg(Fraction(1))
        assert r == {1: Fraction(1)}

    def test_heisenberg_pva_k1(self):
        """PVA lambda-bracket: r^{cl}(z) = 1/z at level k=1."""
        r = RMatrixFromPVA.heisenberg(Fraction(1))
        assert r == {1: Fraction(1)}

    def test_heisenberg_dnp_k1(self):
        """DNP MC element: r(z) = 1/z at level k=1."""
        r = RMatrixFromDNP.heisenberg(Fraction(1))
        assert r == {1: Fraction(1)}

    def test_heisenberg_gz26_k1(self):
        """GZ26 Hamiltonian: r(z) = 1/z at level k=1."""
        r = RMatrixFromGZ26.heisenberg(Fraction(1))
        assert r == {1: Fraction(1)}

    def test_heisenberg_all_agree_k1(self):
        """All four perspectives agree for Heisenberg at k=1."""
        result = compare_r_matrices('heisenberg', {'k': 1})
        assert result['all_agree']

    def test_heisenberg_all_agree_k2(self):
        """All four perspectives agree for Heisenberg at k=2."""
        result = compare_r_matrices('heisenberg', {'k': 2})
        assert result['all_agree']

    def test_heisenberg_all_agree_k_negative(self):
        """All four perspectives agree for Heisenberg at k=-1 (dual level)."""
        result = compare_r_matrices('heisenberg', {'k': -1})
        assert result['all_agree']

    def test_heisenberg_single_pole(self):
        """Heisenberg r-matrix has exactly one pole at z^{-1}."""
        r = RMatrixFromBar.heisenberg(Fraction(3))
        assert set(r.keys()) == {1}

    def test_heisenberg_coefficient_is_level(self):
        """The z^{-1} coefficient equals the level k."""
        for k in [1, 2, 3, -1, Fraction(1, 2)]:
            r = RMatrixFromBar.heisenberg(Fraction(k))
            assert r[1] == Fraction(k)


# ============================================================
# Section 2: sl_2 KM family -- four-perspective agreement
# ============================================================

class TestSl2KMRMatrix:
    """Four-perspective cross-check for sl_2 r(z) = Omega/((k+2)z)."""

    def test_sl2_bar_k1(self):
        """Bar collision residue at level k=1: prefactor = 1/(1+2) = 1/3."""
        r = RMatrixFromBar.affine_sl2(Fraction(1))
        assert r == {1: Fraction(1, 3)}

    def test_sl2_pva_k1(self):
        """PVA lambda-bracket at level k=1: prefactor = 1/3."""
        r = RMatrixFromPVA.affine_sl2(Fraction(1))
        assert r == {1: Fraction(1, 3)}

    def test_sl2_dnp_k1(self):
        """DNP MC element at level k=1: prefactor = 1/3."""
        r = RMatrixFromDNP.affine_sl2(Fraction(1))
        assert r == {1: Fraction(1, 3)}

    def test_sl2_gz26_k1(self):
        """GZ26 Hamiltonian at level k=1: prefactor = 1/3."""
        r = RMatrixFromGZ26.affine_sl2(Fraction(1))
        assert r == {1: Fraction(1, 3)}

    def test_sl2_all_agree_k1(self):
        """All four perspectives agree for sl_2 at k=1."""
        result = compare_r_matrices('sl2', {'k': 1})
        assert result['all_agree']

    def test_sl2_all_agree_k2(self):
        """All four perspectives agree for sl_2 at k=2."""
        result = compare_r_matrices('sl2', {'k': 2})
        assert result['all_agree']

    def test_sl2_all_agree_k3(self):
        """All four perspectives agree for sl_2 at k=3."""
        result = compare_r_matrices('sl2', {'k': 3})
        assert result['all_agree']

    def test_sl2_prefactor_formula(self):
        """Verify prefactor = 1/(k + h^v) = 1/(k + 2) for sl_2."""
        for k in [1, 2, 3, 5, 10]:
            r = RMatrixFromBar.affine_sl2(Fraction(k))
            expected = Fraction(1, k + 2)
            assert r[1] == expected, f"Failed at k={k}: got {r[1]}, expected {expected}"

    def test_sl2_single_pole(self):
        """sl_2 r-matrix has exactly one pole at z^{-1} (AP19)."""
        r = RMatrixFromBar.affine_sl2(Fraction(1))
        assert set(r.keys()) == {1}


# ============================================================
# Section 3: Virasoro family -- four-perspective agreement
# ============================================================

class TestVirasoroRMatrix:
    """Four-perspective cross-check for Virasoro r(z) = (c/2)/z^3 + 2T/z."""

    def test_virasoro_bar_c1(self):
        """Bar collision residue at c=1: (1/2)/z^3 + 2T/z."""
        r = RMatrixFromBar.virasoro(Fraction(1))
        assert r[3] == Fraction(1, 2)
        assert r[1] == '2T'

    def test_virasoro_pva_c1(self):
        """PVA extraction at c=1: same pole structure."""
        r = RMatrixFromPVA.virasoro(Fraction(1))
        assert r[3] == Fraction(1, 2)
        assert r[1] == '2T'

    def test_virasoro_dnp_c1(self):
        """DNP MC element at c=1: same pole structure."""
        r = RMatrixFromDNP.virasoro(Fraction(1))
        assert r[3] == Fraction(1, 2)
        assert r[1] == '2T'

    def test_virasoro_gz26_c1(self):
        """GZ26 Hamiltonian at c=1: same pole structure."""
        r = RMatrixFromGZ26.virasoro(Fraction(1))
        assert r[3] == Fraction(1, 2)
        assert r[1] == '2T'

    def test_virasoro_all_agree_c1(self):
        """All four perspectives agree for Virasoro at c=1."""
        result = compare_r_matrices('virasoro', {'c': 1})
        assert result['all_agree']

    def test_virasoro_all_agree_c26(self):
        """All four perspectives agree at c=26 (critical dimension)."""
        result = compare_r_matrices('virasoro', {'c': 26})
        assert result['all_agree']

    def test_virasoro_all_agree_c13(self):
        """All four perspectives agree at c=13 (self-dual point)."""
        result = compare_r_matrices('virasoro', {'c': 13})
        assert result['all_agree']

    def test_virasoro_no_z_minus_2(self):
        """AP19: Virasoro r-matrix has NO z^{-2} pole."""
        r = RMatrixFromBar.virasoro(Fraction(1))
        assert 2 not in r, "Virasoro r-matrix must not have z^{-2} pole (AP19)"

    def test_virasoro_central_coefficient(self):
        """The z^{-3} coefficient is c/2 (central term)."""
        for c in [1, 2, 13, 26, Fraction(1, 2)]:
            r = RMatrixFromBar.virasoro(Fraction(c))
            assert r[3] == Fraction(c, 2), f"z^{{-3}} coeff should be c/2={Fraction(c,2)}, got {r[3]}"

    def test_virasoro_max_pole_order(self):
        """Max pole order of Virasoro r-matrix is 3 (OPE max 4, minus 1 by AP19)."""
        assert RMatrixFromBar.max_pole_order('virasoro') == 3


# ============================================================
# Section 4: Virasoro on primary states
# ============================================================

class TestVirasoroPrimaryRMatrix:
    """Cross-check r(z) evaluated on primary states of weight h."""

    def test_primary_all_agree_c1_h_half(self):
        """All agree on primary with c=1, h=1/2."""
        result = compare_r_matrices('virasoro_primary', {'c': 1, 'h': Fraction(1, 2)})
        assert result['all_agree']

    def test_primary_all_agree_c26_h1(self):
        """All agree on primary with c=26, h=1."""
        result = compare_r_matrices('virasoro_primary', {'c': 26, 'h': 1})
        assert result['all_agree']

    def test_primary_scalar_coefficients(self):
        """On primaries, both coefficients are numerical (no field labels)."""
        r = RMatrixFromBar.virasoro_on_primary(Fraction(1), Fraction(1, 2))
        assert isinstance(r[3], Fraction)
        assert isinstance(r[1], Fraction)
        assert r[3] == Fraction(1, 2)
        assert r[1] == Fraction(1)  # 2 * 1/2 = 1

    def test_primary_z_minus_1_is_2h(self):
        """The z^{-1} coefficient on a primary is 2h."""
        for h in [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3, 4)]:
            r = RMatrixFromBar.virasoro_on_primary(Fraction(1), h)
            assert r[1] == 2 * h, f"z^{{-1}} on primary of weight {h} should be {2*h}, got {r[1]}"


# ============================================================
# Section 5: W_3 multi-channel structure
# ============================================================

class TestW3RMatrix:
    """Cross-check for W_3 multi-channel r-matrix."""

    def test_w3_all_agree(self):
        """All four perspectives agree for W_3 at c=2."""
        result = compare_r_matrices('w3', {'c': 2})
        assert result['all_agree']

    def test_w3_k_max(self):
        """W_3 r-matrix has k_max = 5 (OPE max pole 6, minus 1 by AP19)."""
        r = RMatrixFromBar.w3(Fraction(2))
        assert r['k_max'] == 5

    def test_w3_max_pole_order(self):
        """Max pole order of W_3 r-matrix is 5."""
        assert RMatrixFromBar.max_pole_order('w3') == 5

    def test_w3_TT_channel_matches_virasoro(self):
        """The T-T channel of W_3 is identical to the Virasoro r-matrix."""
        c = Fraction(2)
        r_w3_TT = RMatrixFromBar.w3(c)['TT']
        r_vir = RMatrixFromBar.virasoro(c)
        assert r_w3_TT == r_vir

    def test_w3_WW_leading_pole(self):
        """W-W channel leading pole: z^{-5} with coefficient c/3."""
        c = Fraction(2)
        r_ww = RMatrixFromBar.w3(c)['WW']
        assert r_ww[5] == Fraction(c, 3)

    def test_w3_WW_has_even_pole(self):
        """W-W channel has a z^{-2} pole (from dT mode), unlike Virasoro."""
        c = Fraction(2)
        r_ww = RMatrixFromBar.w3(c)['WW']
        assert 2 in r_ww, "W-W channel should have z^{-2} pole from W_{(2)}W = (1/3)dT"

    def test_w3_TW_single_pole(self):
        """T-W channel has a single pole at z^{-1}."""
        c = Fraction(2)
        r_tw = RMatrixFromBar.w3(c)['TW']
        assert set(r_tw.keys()) == {1}

    def test_w3_ope_mode_extraction(self):
        """Verify W_3 OPE mode extraction from lambda-bracket (AP44 check)."""
        result = w3_ope_mode_verification(2)
        assert result['lambda_5']['match'], "W_{(5)}W should be c/3"
        assert result['lambda_3']['match'], "W_{(3)}W should be 2T"
        assert result['lambda_2']['match'], "W_{(2)}W should be (1/3)dT"


# ============================================================
# Section 6: Structural properties
# ============================================================

class TestStructuralProperties:
    """Structural properties: antisymmetry, CYBE, strictness."""

    def test_antisymmetry_heisenberg(self):
        """Heisenberg r-matrix is antisymmetric."""
        result = verify_antisymmetry('heisenberg', {'k': 1})
        assert result['verified']

    def test_antisymmetry_virasoro_primary(self):
        """Virasoro r-matrix on primaries is antisymmetric (no even poles)."""
        result = verify_antisymmetry('virasoro_primary', {'c': 1, 'h': Fraction(1, 2)})
        assert result['verified']

    def test_heisenberg_is_strict(self):
        """Heisenberg dg-shifted Yangian is strict (m_k = 0 for k >= 3)."""
        assert RMatrixFromDNP.is_strict('heisenberg')

    def test_sl2_is_strict(self):
        """sl_2 dg-shifted Yangian is strict."""
        assert RMatrixFromDNP.is_strict('sl2')

    def test_virasoro_is_not_strict(self):
        """Virasoro dg-shifted Yangian is NOT strict (class M, infinite shadow depth)."""
        assert not RMatrixFromDNP.is_strict('virasoro')

    def test_w3_is_not_strict(self):
        """W_3 dg-shifted Yangian is NOT strict."""
        assert not RMatrixFromDNP.is_strict('w3')

    def test_cybe_scalar_heisenberg(self):
        """CYBE trivially holds for scalar (abelian) Heisenberg r-matrix."""
        r = RMatrixFromBar.heisenberg(Fraction(1))
        assert RMatrixFromDNP.verify_cybe_scalar(r)

    def test_cybe_sl2_casimir(self):
        """CYBE holds for sl_2 Casimir r-matrix (verified via IBR)."""
        assert RMatrixFromDNP.verify_cybe_sl2_casimir(k=1)

    def test_cybe_sl2_casimir_level_2(self):
        """CYBE holds at level k=2."""
        assert RMatrixFromDNP.verify_cybe_sl2_casimir(k=2)


# ============================================================
# Section 7: AP19 verification (pole structure)
# ============================================================

class TestAP19PoleStructure:
    """Verify AP19: d log absorption shifts pole orders by 1."""

    def test_heisenberg_pole_structure(self):
        """Heisenberg: OPE pole 2, r-matrix pole 1."""
        result = verify_pole_structure('heisenberg')
        assert result['ope_max_pole'] == 2
        assert result['r_matrix_max_pole'] == 1
        assert result['ap19_satisfied']

    def test_sl2_pole_structure(self):
        """sl_2: OPE pole 2, r-matrix pole 1."""
        result = verify_pole_structure('sl2')
        assert result['ope_max_pole'] == 2
        assert result['r_matrix_max_pole'] == 1
        assert result['ap19_satisfied']

    def test_virasoro_pole_structure(self):
        """Virasoro: OPE pole 4, r-matrix pole 3, no z^{-2}."""
        result = verify_pole_structure('virasoro')
        assert result['ope_max_pole'] == 4
        assert result['r_matrix_max_pole'] == 3
        assert result['ap19_satisfied']
        assert result['no_z_minus_2']
        assert 3 in result['poles_present']
        assert 1 in result['poles_present']
        assert 2 in result['poles_absent']

    def test_w3_pole_structure(self):
        """W_3: OPE pole 6 (W-W channel), r-matrix pole 5."""
        result = verify_pole_structure('w3')
        assert result['ope_max_pole'] == 6
        assert result['r_matrix_max_pole'] == 5
        assert result['ap19_satisfied']

    def test_wn_general_pole_orders(self):
        """W_N: OPE max pole = 2N, r-matrix max pole = 2N - 1."""
        for N in [2, 3, 4, 5]:
            family = f'w{N}'
            max_pole = RMatrixFromBar.max_pole_order(family)
            assert max_pole == 2 * N - 1, f"W_{N} should have max pole {2*N-1}, got {max_pole}"


# ============================================================
# Section 8: AP44 verification (PVA divided-power convention)
# ============================================================

class TestAP44DividedPower:
    """Verify AP44: PVA -> OPE mode conversion uses factorial factors."""

    def test_virasoro_pva_conversion(self):
        """Virasoro PVA -> OPE: (c/12)*3! = c/2 for the lambda^3 term."""
        result = virasoro_pva_to_ope_verification(1)
        assert result['T_3_T']['match']
        assert result['T_1_T']['match']
        assert result['T_0_T']['match']

    def test_virasoro_pva_conversion_c26(self):
        """Same check at c=26."""
        result = virasoro_pva_to_ope_verification(26)
        assert result['T_3_T']['ope_mode'] == Fraction(13)  # 26/2

    def test_w3_pva_conversion(self):
        """W_3 PVA -> OPE: (c/360)*5! = c/3 for the lambda^5 term."""
        result = w3_ope_mode_verification(2)
        assert result['lambda_5']['match']
        assert result['lambda_5']['ope_mode'] == Fraction(2, 3)  # c/3 at c=2

    def test_w3_pva_lambda3(self):
        """W_3 lambda^3 term: (1/3)*3! = 2 (factor of T)."""
        result = w3_ope_mode_verification(2)
        assert result['lambda_3']['match']

    def test_w3_pva_lambda2(self):
        """W_3 lambda^2 term: (1/6)*2! = 1/3 (factor of dT)."""
        result = w3_ope_mode_verification(2)
        assert result['lambda_2']['match']


# ============================================================
# Section 9: Numerical checks (IBR and KZ commutativity)
# ============================================================

class TestNumericalChecks:
    """Numerical verification of CYBE and KZ commutativity."""

    def test_cybe_sl2_spin_half(self):
        """CYBE for sl_2 Casimir in spin-1/2 representation."""
        result = verify_cybe_sl2_numerical(k=1, rep_dim=2)
        assert result['ibr_holds']
        assert result['cybe_holds']

    def test_cybe_sl2_spin_1(self):
        """CYBE for sl_2 Casimir in spin-1 representation."""
        result = verify_cybe_sl2_numerical(k=1, rep_dim=3)
        assert result['ibr_holds']
        assert result['cybe_holds']

    def test_cybe_sl2_spin_3half(self):
        """CYBE for sl_2 Casimir in spin-3/2 representation."""
        result = verify_cybe_sl2_numerical(k=1, rep_dim=4)
        assert result['ibr_holds']
        assert result['cybe_holds']

    def test_kz_commutativity_3pt_k1(self):
        """KZ Hamiltonians commute at 3 points, k=1."""
        result = verify_kz_commutativity_from_r_matrix(k=1, n_points=3)
        assert result['all_commute']

    def test_kz_commutativity_4pt_k1(self):
        """KZ Hamiltonians commute at 4 points, k=1."""
        result = verify_kz_commutativity_from_r_matrix(k=1, n_points=4)
        assert result['all_commute']

    def test_kz_commutativity_3pt_k2(self):
        """KZ Hamiltonians commute at 3 points, k=2."""
        result = verify_kz_commutativity_from_r_matrix(k=2, n_points=3)
        assert result['all_commute']

    def test_kz_commutativity_4pt_k3(self):
        """KZ Hamiltonians commute at 4 points, k=3."""
        result = verify_kz_commutativity_from_r_matrix(k=3, n_points=4)
        assert result['all_commute']


# ============================================================
# Section 10: Full consistency matrix and leading-order matching
# ============================================================

class TestConsistencyMatrix:
    """Full consistency matrix across all families and perspectives."""

    def test_full_consistency_matrix(self):
        """All families agree across all four perspectives."""
        result = full_consistency_matrix()
        assert result['all_consistent'], (
            f"Consistency failures: {result['n_agree']}/{result['n_families']} agree"
        )

    def test_leading_order_heisenberg(self):
        """Leading-order matching for Heisenberg: bar = PVA."""
        result = verify_leading_order_matching('heisenberg', {'k': 1})
        assert result['match']

    def test_leading_order_sl2(self):
        """Leading-order matching for sl_2: bar = PVA."""
        result = verify_leading_order_matching('sl2', {'k': 1})
        assert result['match']

    def test_leading_order_virasoro(self):
        """Leading-order matching for Virasoro: bar = PVA."""
        result = verify_leading_order_matching('virasoro', {'c': 1})
        assert result['match']

    def test_kappa_heisenberg_consistency(self):
        """kappa(H_k) = k: the r-matrix coefficient equals kappa for Heisenberg."""
        for k in [1, 2, 3]:
            r = RMatrixFromBar.heisenberg(Fraction(k))
            assert r[1] == kappa_heisenberg(Fraction(k))

    def test_kappa_virasoro_consistency(self):
        """The z^{-3} coefficient of Virasoro r-matrix is kappa = c/2."""
        for c in [1, 2, 13, 26]:
            r = RMatrixFromBar.virasoro(Fraction(c))
            assert r[3] == kappa_virasoro(Fraction(c))
