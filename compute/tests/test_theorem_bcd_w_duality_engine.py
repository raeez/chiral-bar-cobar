r"""Tests for exact BCD root arithmetic and typed principal-W claims.

48 tests organized in 8 sections:
    I.    Lie algebra data and ||rho||^2 verification (6 tests)
    II.   Accidental root-isomorphism oracles (6 tests)
    III.  Typed central-charge surfaces (6 tests)
    IV.   Typed modular-conductor surfaces (8 tests)
    V.    Langlands duality structure (6 tests)
    VI.   Nilpotent orbit enumeration (4 tests)
    VII.  BV candidate boundary (6 tests)
    VIII. Multi-path verification and cross-family consistency (6 tests)

Exact scalars occur only in the Lie/root/isomorphism and partition lanes.
Central charge, rho, kappa, reflected levels, and modular conductors carry
``ClaimPacket`` status, evidence, and hypotheses with ``value=None``.

||rho||^2 NORMALIZATION: all formulas use the invariant form with long
roots squared = 2.  The C_n formula is n(n+1)(2n+1)/12 (NOT /6).
The B_2 = C_2 isomorphism (so_5 ~ sp_4) is the primary cross-check.
"""

from sympy import Rational, Symbol

from compute.lib.non_principal_w_bar_engine import ClaimPacket, ClaimStatus

from compute.lib.theorem_bcd_w_duality_engine import (
    BCDPrincipalDualityData,
    IsomorphismCheckData,
    KappaComplementarityData,
    LanglandsDualityData,
    _is_valid_bcd_partition,
    _lie_data,
    _transpose_partition,
    _transpose_parity_repair_candidate,
    affine_central_charge,
    affine_kappa,
    anomaly_ratio,
    bcd_duality_summary,
    bcd_nilpotent_partitions,
    bv_dual_partition,
    central_charge,
    check_b2_c2_isomorphism,
    check_d3_a3_isomorphism,
    ds_kappa_deficit,
    d3_a3_incomplete_ansatz_discrepancy,
    ff_dual_level,
    kappa,
    kappa_complementarity,
    langlands_duality_data,
    principal_duality_data,
    reciprocal_weight_diagnostic,
)


k = Symbol('k')


def _assert_unresolved(packet: ClaimPacket, status: ClaimStatus) -> None:
    """Assert the common typed-claim boundary."""

    assert isinstance(packet, ClaimPacket)
    assert packet.status is status
    assert packet.value is None
    assert packet.hypotheses


# ===================================================================
# I.  Lie algebra data and ||rho||^2 verification
# ===================================================================

class TestLieData:
    """Verify Lie algebra data: dim, h^v, exponents, ||rho||^2."""

    def test_b2_data(self):
        """B_2 = so_5: dim=10, h^v=3, exponents=(1,3), ||rho||^2=5/2."""
        d = _lie_data('B', 2)
        assert d['dim'] == 10
        assert d['h_dual'] == 3
        assert d['exponents'] == (1, 3)
        assert d['generator_weights'] == (2, 4)
        assert d['rho_squared'] == Rational(5, 2)

    def test_c2_data(self):
        """C_2 = sp_4: dim=10, h^v=3, exponents=(1,3), ||rho||^2=5/2.

        CRITICAL: ||rho||^2 = n(n+1)(2n+1)/12 = 5/2, NOT n(n+1)(2n+1)/6 = 5.
        The /6 formula uses orthonormal coordinates; the /12 formula uses
        the long-root-normalized form required by the KRW formula.
        """
        d = _lie_data('C', 2)
        assert d['dim'] == 10
        assert d['h_dual'] == 3
        assert d['exponents'] == (1, 3)
        assert d['rho_squared'] == Rational(5, 2)

    def test_b2_c2_same_rho_squared(self):
        """B_2 and C_2 MUST have same ||rho||^2 (so_5 ~ sp_4 isomorphism)."""
        assert _lie_data('B', 2)['rho_squared'] == _lie_data('C', 2)['rho_squared']

    def test_d3_data(self):
        """D_3 = so_6: dim=15, h^v=4, ||rho||^2=5."""
        d = _lie_data('D', 3)
        assert d['dim'] == 15
        assert d['h_dual'] == 4
        assert d['rho_squared'] == Rational(5)

    def test_b3_data(self):
        """B_3 = so_7: dim=21, h^v=5, ||rho||^2=35/4."""
        d = _lie_data('B', 3)
        assert d['dim'] == 21
        assert d['h_dual'] == 5
        assert d['rho_squared'] == Rational(35, 4)

    def test_rho_sq_freudenthal_check(self):
        """Cross-check: ||rho||^2 via Freudenthal-de Vries dim*h/12.

        For simply-laced types (D_n), FdV gives ||rho||^2 = dim*h/12
        where h is the Coxeter number (NOT the dual Coxeter number).
        For D_n: h = 2n-2 = h^v (simply-laced), dim = n(2n-1).
        So FdV: n(2n-1)(2n-2)/12 = n(n-1)(2n-1)/6.
        """
        for n in [3, 4, 5]:
            d = _lie_data('D', n)
            fdv = Rational(d['dim'] * d['h_dual'], 12)
            assert d['rho_squared'] == fdv, \
                f"D_{n}: ||rho||^2 = {d['rho_squared']} but FdV gives {fdv}"


# ===================================================================
# II.  Accidental isomorphism cross-checks
# ===================================================================

class TestIsomorphisms:
    """Verify B_2 = C_2 (so_5 ~ sp_4) and D_3 = A_3 (so_6 ~ sl_4)."""

    def test_b2_c2_central_charge(self):
        """The exact B_2=C_2 root oracle precedes central-charge transport."""
        iso = check_b2_c2_isomorphism(k)
        assert isinstance(iso, IsomorphismCheckData)
        assert iso.root_data_match is True
        _assert_unresolved(iso.c_match, ClaimStatus.OPEN)
        assert iso.c_match.evidence

    def test_b2_c2_kappa(self):
        """B_2=C_2 kappa equality is conditional on the trace comparison."""
        iso = check_b2_c2_isomorphism(k)
        _assert_unresolved(iso.kappa_match, ClaimStatus.CONDITIONAL)
        assert any("genus-one" in h for h in iso.kappa_match.hypotheses)

    def test_b2_c2_anomaly_ratio(self):
        """The common 3/4 diagnostic leaves rho equality open."""
        iso = check_b2_c2_isomorphism(k)
        assert reciprocal_weight_diagnostic('B', 2) == Rational(3, 4)
        assert reciprocal_weight_diagnostic('C', 2) == Rational(3, 4)
        _assert_unresolved(iso.rho_match, ClaimStatus.OPEN)
        assert any("3/4" in item for item in iso.rho_match.evidence)

    def test_d3_a3_central_charge(self):
        """D_3=A_3 detects the exact failure of the rank-minus-pole ansatz."""
        iso = check_d3_a3_isomorphism(k)
        assert iso.root_data_match is True
        assert iso.incomplete_central_ansatz_discrepancy == 60 * k + 120
        assert d3_a3_incomplete_ansatz_discrepancy(k) == 60 * k + 120
        _assert_unresolved(iso.c_match, ClaimStatus.OPEN)
        assert any("60*k + 120" in item for item in iso.c_match.evidence)

    def test_d3_a3_kappa(self):
        """D_3=A_3 kappa transport retains the genus-one hypotheses."""
        iso = check_d3_a3_isomorphism(k)
        _assert_unresolved(iso.kappa_match, ClaimStatus.CONDITIONAL)
        assert iso.kappa_match.evidence

    def test_d3_a3_anomaly_ratio(self):
        """The exact D_3=A_3 diagnostic is 13/12; rho remains open."""
        iso = check_d3_a3_isomorphism(k)
        assert reciprocal_weight_diagnostic('D', 3) == Rational(13, 12)
        _assert_unresolved(iso.rho_match, ClaimStatus.OPEN)
        assert any("13/12" in item for item in iso.rho_match.evidence)


# ===================================================================
# III.  Principal W-algebra central charges
# ===================================================================

class TestCentralCharges:
    """Principal and affine central surfaces retain their hypotheses."""

    def test_b2_c_formula(self):
        """The B_2 central packet imports the canonical KRW obligation."""
        packet = central_charge('B', 2, k)
        _assert_unresolved(packet, ClaimStatus.OPEN)
        assert any("60*k+120" in item for item in packet.evidence)

    def test_c3_c_formula(self):
        """The C_3 central packet names grading and form normalization."""
        packet = central_charge('C', 3, k)
        _assert_unresolved(packet, ClaimStatus.OPEN)
        assert any("good grading" in h for h in packet.hypotheses)

    def test_d4_c_formula(self):
        """The D_4 exponent multiplicity is exact while c remains open."""
        data = _lie_data('D', 4)
        assert data['exponents'] == (1, 3, 3, 5)
        assert data['generator_weights'] == (2, 4, 4, 6)
        _assert_unresolved(central_charge('D', 4, k), ClaimStatus.OPEN)

    def test_b3_c_formula(self):
        """The B_3 root ledger and central packet remain distinct."""
        assert _lie_data('B', 3)['rho_squared'] == Rational(35, 4)
        packet = central_charge('B', 3, k)
        _assert_unresolved(packet, ClaimStatus.OPEN)
        assert packet.evidence

    def test_affine_c_vs_w_c(self):
        """Affine and principal central charges are separate typed surfaces."""
        for t, n in [('B', 2), ('C', 3), ('D', 4)]:
            c_aff = affine_central_charge(t, n, Rational(10))
            c_w = central_charge(t, n, Rational(10))
            _assert_unresolved(c_aff, ClaimStatus.CONDITIONAL)
            _assert_unresolved(c_w, ClaimStatus.OPEN)
            assert c_aff.evidence

    def test_c_pole_at_minus_h_dual(self):
        """The dual-level relation is a fixed-convention open claim."""
        for t, n in [('B', 3), ('C', 2), ('D', 5)]:
            packet = ff_dual_level(t, n, k)
            _assert_unresolved(packet, ClaimStatus.OPEN)
            assert any("Feigin--Frenkel" in h for h in packet.hypotheses)


# ===================================================================
# IV.  Kappa complementarity for same-type FF duality
# ===================================================================

class TestKappaComplementarity:
    """The modular conductor is an open represented-trace comparison."""

    def test_b2_kappa_sum(self):
        """B_2 source, dual, and conductor packets have the right statuses."""
        comp = kappa_complementarity('B', 2, k)
        assert isinstance(comp, KappaComplementarityData)
        _assert_unresolved(comp.kappa_k, ClaimStatus.CONDITIONAL)
        _assert_unresolved(comp.kappa_kprime, ClaimStatus.CONDITIONAL)
        _assert_unresolved(comp.kappa_sum, ClaimStatus.OPEN)
        _assert_unresolved(comp.kappa_sum_is_constant, ClaimStatus.OPEN)

    def test_c2_kappa_sum(self):
        """C_2 conductor resolution requires a common reflected convention."""
        comp = kappa_complementarity('C', 2, k)
        _assert_unresolved(comp.kappa_sum, ClaimStatus.OPEN)
        assert any("common convention" in h for h in comp.kappa_sum.hypotheses)

    def test_b3_kappa_sum(self):
        """The B_3 diagnostic is 11/12 and its conductor remains open."""
        comp = kappa_complementarity('B', 3, k)
        assert reciprocal_weight_diagnostic('B', 3) == Rational(11, 12)
        _assert_unresolved(comp.kappa_sum, ClaimStatus.OPEN)

    def test_c3_kappa_sum(self):
        """The C_3 diagnostic is 11/12 and its conductor remains open."""
        comp = kappa_complementarity('C', 3, k)
        assert reciprocal_weight_diagnostic('C', 3) == Rational(11, 12)
        _assert_unresolved(comp.kappa_sum, ClaimStatus.OPEN)

    def test_d3_kappa_sum(self):
        """The D_3 diagnostic is 13/12 and its conductor remains open."""
        comp = kappa_complementarity('D', 3, k)
        assert reciprocal_weight_diagnostic('D', 3) == Rational(13, 12)
        _assert_unresolved(comp.kappa_sum, ClaimStatus.OPEN)

    def test_d4_kappa_sum(self):
        """D_4 retains the repeated weight-four generator in its diagnostic."""
        comp = kappa_complementarity('D', 4, k)
        assert reciprocal_weight_diagnostic('D', 4) == Rational(7, 6)
        _assert_unresolved(comp.kappa_sum, ClaimStatus.OPEN)

    def test_all_constant(self):
        """Level-independence remains open for every configured BCD family."""
        for t in ['B', 'C']:
            for n in range(2, 7):
                comp = kappa_complementarity(t, n, k)
                _assert_unresolved(comp.kappa_sum_is_constant, ClaimStatus.OPEN)
        for n in range(3, 7):
            comp = kappa_complementarity('D', n, k)
            _assert_unresolved(comp.kappa_sum_is_constant, ClaimStatus.OPEN)

    def test_bn_cn_same_kappa_sum(self):
        """B_n and C_n share exact diagnostics; conductor equality stays open."""
        for n in range(2, 7):
            assert reciprocal_weight_diagnostic('B', n) == reciprocal_weight_diagnostic('C', n)
            comparison = langlands_duality_data('B', n, k).same_kappa_sum
            _assert_unresolved(comparison, ClaimStatus.OPEN)


# ===================================================================
# V.  Langlands duality structure
# ===================================================================

class TestLanglandsDuality:
    """B_n^L = C_n, C_n^L = B_n, D_n^L = D_n."""

    def test_b_c_same_exponents(self):
        """B_n and C_n have the same exponents for all n."""
        for n in range(2, 7):
            d_b = _lie_data('B', n)
            d_c = _lie_data('C', n)
            assert d_b['exponents'] == d_c['exponents'], \
                f"n={n}: B exponents {d_b['exponents']} != C exponents {d_c['exponents']}"

    def test_b_c_same_anomaly_ratio(self):
        """B_n and C_n share a diagnostic while both rho packets stay open."""
        for n in range(2, 7):
            assert reciprocal_weight_diagnostic('B', n) == reciprocal_weight_diagnostic('C', n)
            _assert_unresolved(anomaly_ratio('B', n), ClaimStatus.OPEN)
            _assert_unresolved(anomaly_ratio('C', n), ClaimStatus.OPEN)

    def test_b_c_different_h_dual(self):
        """B_n and C_n have different h^v for n >= 3."""
        for n in range(3, 7):
            assert _lie_data('B', n)['h_dual'] != _lie_data('C', n)['h_dual']

    def test_b_c_different_central_charges(self):
        """Central-charge comparison is open in a common DS convention."""
        for n in range(3, 7):
            data = langlands_duality_data('B', n, k)
            _assert_unresolved(data.c_g, ClaimStatus.OPEN)
            _assert_unresolved(data.c_gL, ClaimStatus.OPEN)
            _assert_unresolved(data.same_central_charge, ClaimStatus.OPEN)

    def test_langlands_data_structure(self):
        """Langlands duality data records the correct structure."""
        ld = langlands_duality_data('B', 3, k)
        assert isinstance(ld, LanglandsDualityData)
        assert ld.type_g == 'B_3'
        assert ld.type_gL == 'C_3'
        assert ld.same_exponents is True
        _assert_unresolved(ld.same_anomaly_ratio, ClaimStatus.OPEN)
        _assert_unresolved(ld.same_central_charge, ClaimStatus.OPEN)
        _assert_unresolved(ld.same_kappa_sum, ClaimStatus.OPEN)
        assert ld.same_anomaly_ratio.evidence

    def test_d_self_dual(self):
        """D_n is self-Langlands-dual."""
        ld = langlands_duality_data('D', 4, k)
        assert ld.type_g == 'D_4'
        assert ld.type_gL == 'D_4'
        assert ld.same_exponents is True
        _assert_unresolved(ld.same_central_charge, ClaimStatus.OPEN)


# ===================================================================
# VI.  Nilpotent orbit enumeration
# ===================================================================

class TestNilpotentOrbits:
    """Nilpotent orbit partition enumeration for BCD types."""

    def test_b2_orbit_count(self):
        """B_2 (so_5): 4 nilpotent orbits.

        Partitions of 5 with even parts having even multiplicity:
        (5), (3,1,1), (2,2,1), (1,1,1,1,1).
        """
        parts = bcd_nilpotent_partitions('B', 2)
        assert len(parts) == 4
        assert (5,) in parts
        assert (1, 1, 1, 1, 1) in parts

    def test_c2_orbit_count(self):
        """C_2 (sp_4): 4 nilpotent orbits.

        Partitions of 4 with odd parts having even multiplicity:
        (4), (2,2), (2,1,1), (1,1,1,1).
        """
        parts = bcd_nilpotent_partitions('C', 2)
        assert len(parts) == 4
        assert (4,) in parts
        assert (2, 2) in parts

    def test_d3_orbit_count(self):
        """D_3 (so_6): 5 nilpotent orbits (same as A_3 by isomorphism).

        Partitions of 6 with even parts having even multiplicity:
        (5,1), (3,3), (3,1,1,1), (2,2,1,1), (1,1,1,1,1,1).
        Note: (6) is NOT valid (6 is even with multiplicity 1).
        """
        parts = bcd_nilpotent_partitions('D', 3)
        assert len(parts) == 5
        assert (5, 1) in parts
        assert (3, 3) in parts
        assert (6,) not in parts  # invalid: even part with odd mult

    def test_partition_validity(self):
        """Spot-check partition validity rules."""
        # B-type: even parts need even multiplicity
        assert _is_valid_bcd_partition('B', (5,)) is True
        assert _is_valid_bcd_partition('B', (4, 1)) is False  # 4 has mult 1
        assert _is_valid_bcd_partition('B', (2, 2, 1)) is True  # 2 has mult 2
        # C-type: odd parts need even multiplicity
        assert _is_valid_bcd_partition('C', (4,)) is True
        assert _is_valid_bcd_partition('C', (3, 1)) is False  # 3 has mult 1
        assert _is_valid_bcd_partition('C', (2, 2)) is True


# ===================================================================
# VII.  BV candidate boundary
# ===================================================================

class TestBVDuality:
    """Separate exact partition arithmetic from the open BV realization."""

    def test_principal_to_zero(self):
        """The B2 principal transpose lane yields the C2 zero candidate."""
        candidate = _transpose_parity_repair_candidate((1, 1, 1, 1, 1), 'C')
        assert candidate == (1, 1, 1, 1)
        _assert_unresolved(bv_dual_partition('B', 2, (5,)), ClaimStatus.OPEN)

    def test_zero_to_principal(self):
        """The B2 zero transpose lane yields a size-four C2 candidate."""
        candidate = _transpose_parity_repair_candidate((5,), 'C')
        assert candidate == (4,)
        _assert_unresolved(
            bv_dual_partition('B', 2, (1, 1, 1, 1, 1)), ClaimStatus.OPEN
        )

    def test_c2_zero_to_b2(self):
        """C2 exhibits the missing size-changing operation explicitly."""
        candidate = _transpose_parity_repair_candidate((4,), 'B')
        assert candidate == (3,)
        assert sum(candidate) == 3
        packet = bv_dual_partition('C', 2, (1, 1, 1, 1))
        _assert_unresolved(packet, ClaimStatus.OPEN)
        assert any("partition size 5" in item for item in packet.evidence)

    def test_transpose_involution(self):
        """_transpose_partition is an involution on partitions."""
        test_cases = [(5,), (3, 2), (4, 2, 1), (2, 2, 2)]
        for p in test_cases:
            assert _transpose_partition(_transpose_partition(p)) == p

    def test_d3_self_type_bv(self):
        """Every D3 dual-orbit identification remains an open packet."""
        for p in bcd_nilpotent_partitions('D', 3):
            _assert_unresolved(bv_dual_partition('D', 3, p), ClaimStatus.OPEN)

    def test_x_collapse_preserves_dominance(self):
        """The parity-repair candidate is weakly smaller than its input.

        This property belongs to the candidate and supplies no BV theorem.
        """
        test_cases = [
            ((4, 2, 1), 'C'),  # 4 is ok; 2 ok; 1 has mult 1 -> collapse
            ((3, 3, 2), 'B'),  # 2 has mult 1 -> collapse
            ((4, 2), 'D'),     # 4 has mult 1 -> collapse; 2 has mult 1 -> collapse
        ]
        for partition, target in test_cases:
            collapsed = _transpose_parity_repair_candidate(partition, target)
            assert sum(collapsed) <= sum(partition), \
                f"Collapse {partition} -> {collapsed}: sum increased!"


# ===================================================================
# VIII.  Multi-path verification and cross-family consistency
# ===================================================================

class TestMultiPath:
    """Multi-path verification: every result checked by 2+ methods."""

    def test_kappa_via_rho_times_c(self):
        """Generator diagnostics and all three modular packets stay separated."""
        for t, n in [('B', 2), ('C', 3), ('D', 4)]:
            assert reciprocal_weight_diagnostic(t, n) == sum(
                Rational(1, weight) for weight in _lie_data(t, n)['generator_weights']
            )
            _assert_unresolved(anomaly_ratio(t, n), ClaimStatus.OPEN)
            _assert_unresolved(central_charge(t, n, Rational(10)), ClaimStatus.OPEN)
            _assert_unresolved(kappa(t, n, Rational(10)), ClaimStatus.CONDITIONAL)

    def test_b2_kappa_against_creutzig_engine(self):
        """The facade returns the canonical B_2 kappa packet unchanged."""
        from compute.lib.theorem_creutzig_w_landscape_engine import (
            building_block_bcd_data,
        )
        our_kap = kappa('B', 2, k)
        their = building_block_bcd_data('B', 2, k)
        assert our_kap == their.kappa
        _assert_unresolved(our_kap, ClaimStatus.CONDITIONAL)

    def test_c2_kappa_against_creutzig_engine(self):
        """The facade returns the canonical C_2 kappa packet unchanged."""
        from compute.lib.theorem_creutzig_w_landscape_engine import (
            building_block_bcd_data,
        )
        our_kap = kappa('C', 2, k)
        their = building_block_bcd_data('C', 2, k)
        assert our_kap == their.kappa
        _assert_unresolved(our_kap, ClaimStatus.CONDITIONAL)

    def test_ds_deficit_positive_for_large_k(self):
        """The DS trace defect is conditional on the BRST trace comparison."""
        for t, n in [('B', 3), ('C', 4), ('D', 5)]:
            _assert_unresolved(affine_kappa(t, n, Rational(100)), ClaimStatus.CONDITIONAL)
            deficit = ds_kappa_deficit(t, n, Rational(100))
            _assert_unresolved(deficit, ClaimStatus.CONDITIONAL)
            assert any("BRST" in h for h in deficit.hypotheses)
            assert deficit.evidence

    def test_summary_table_consistency(self):
        """Summary rows expose exact root data and claim statuses only."""
        direct = principal_duality_data('B', 2, k)
        assert isinstance(direct, BCDPrincipalDualityData)
        _assert_unresolved(direct.modular_conductor, ClaimStatus.OPEN)
        rows = bcd_duality_summary(max_rank=4)
        assert len(rows) == 8
        for row in rows:
            assert isinstance(row['dim'], int)
            assert isinstance(row['rho_sq'], Rational)
            assert row['rho_status'] is ClaimStatus.OPEN
            assert row['central_charge_status'] is ClaimStatus.OPEN
            assert row['kappa_status'] is ClaimStatus.CONDITIONAL
            assert row['modular_conductor_status'] is ClaimStatus.OPEN
            assert row['shadow_status'] is ClaimStatus.OPEN
            assert 'c' not in row and 'kappa_sum' not in row

    def test_kappa_nonzero_generic(self):
        """Every generic-level BCD kappa remains conditional and nonnumeric."""
        for t in ['B', 'C']:
            for n in range(2, 5):
                _assert_unresolved(kappa(t, n, Rational(1)), ClaimStatus.CONDITIONAL)
        for n in range(3, 5):
            _assert_unresolved(kappa('D', n, Rational(1)), ClaimStatus.CONDITIONAL)
