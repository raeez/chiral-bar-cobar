r"""Tests for the K3 Mukai-lattice and B-row claim firewall."""

from fractions import Fraction
from pathlib import Path

from sympy import Matrix

from compute.lib.bp_koszul_conductor_engine import (
    KAPPA_COMPLEMENTARITY_EXACT,
    K_BP_EXACT,
)
from compute.lib.theorem_c_b_family_mukai_engine import (
    B_FAMILY_PACKAGE_NAME,
    B_FAMILY_HYPOTHESES,
    BRUINIER_LEMMA_5_1,
    LUSZTIG_ROOT_ORDER_SCOPE,
    b_family_scope,
    bp_former_kappa_proposal,
    bp_scalar_scope,
    candidate_bridge_report,
    e8_cartan_matrix,
    hyperbolic_plane,
    k3_betti_numbers,
    k3_euler_characteristic,
    k3_h2_gram_matrix,
    k3_h2_signature_from_betti,
    k3_signature_from_hirzebruch,
    mukai_c_minus,
    mukai_c_plus,
    mukai_gram_matrix,
    mukai_rank,
    mukai_scalar_candidates,
    mukai_signature,
    mukai_signature_from_blocks,
    mukai_signature_from_hirzebruch,
    source_claim_audit,
    theorem_c_candidate_values,
    theorem_c_certified_values,
    theorem_c_status_ledger,
    verify_engine,
    verify_mukai_lattice,
)


ENGINE = Path("compute/lib/theorem_c_b_family_mukai_engine.py")


def fkr_standard_central_charge(level: int | Fraction) -> Fraction:
    """FKR21, Eq. (2.2), evaluated independently of the engine."""

    k = Fraction(level)
    return -((2 * k + 3) * (3 * k + 1)) / (k + 3)


class TestIntegralLattices:
    def test_hyperbolic_plane(self):
        u = hyperbolic_plane()
        assert u == Matrix([[0, 1], [1, 0]])
        assert u.det() == -1
        assert u.rank() == 2

    def test_e8_cartan_is_even_unimodular(self):
        e8 = e8_cartan_matrix()
        assert e8 == e8.T
        assert e8.det() == 1
        assert all(e8[index, index] == 2 for index in range(8))

    def test_e8_positive_by_sylvester(self):
        e8 = e8_cartan_matrix()
        leading_minors = [e8[:size, :size].det() for size in range(1, 9)]
        assert leading_minors == [2, 3, 4, 5, 6, 7, 8, 1]
        assert all(value > 0 for value in leading_minors)

    def test_k3_h2_gram(self):
        gram = k3_h2_gram_matrix()
        assert gram.shape == (22, 22)
        assert gram.rank() == 22
        assert abs(gram.det()) == 1
        assert gram == gram.T

    def test_mukai_gram(self):
        gram = mukai_gram_matrix()
        assert gram.shape == (24, 24)
        assert gram.rank() == 24
        assert gram.det() == 1
        assert gram == gram.T
        assert all(gram[index, index] % 2 == 0 for index in range(24))


class TestThreeSignaturePaths:
    def test_block_decomposition(self):
        assert mukai_signature_from_blocks() == (4, 20)

    def test_hirzebruch_signature(self):
        assert k3_signature_from_hirzebruch() == -16
        assert k3_h2_signature_from_betti() == (3, 19)
        assert mukai_signature_from_hirzebruch() == (4, 20)

    def test_betti_and_euler_path(self):
        assert k3_betti_numbers() == (1, 0, 22, 0, 1)
        assert k3_euler_characteristic() == 24

    def test_paths_agree(self):
        assert mukai_signature_from_blocks() == mukai_signature_from_hirzebruch()
        assert mukai_signature() == (4, 20)

    def test_rank_and_indices(self):
        assert mukai_rank() == 24
        assert mukai_c_plus() == 4
        assert mukai_c_minus() == 20

    def test_full_lattice_certificate(self):
        certificate = verify_mukai_lattice()
        assert certificate["status"] == "proved"
        assert certificate["signature_by_blocks"] == (4, 20)
        assert certificate["signature_by_hirzebruch"] == (4, 20)
        assert certificate["gram_rank"] == 24
        assert certificate["gram_determinant"] == 1
        assert certificate["gram_even"] is True
        assert certificate["e8_positive_by_sylvester"] is True


class TestScalarCandidates:
    def test_arithmetic_values(self):
        candidates = mukai_scalar_candidates()
        assert candidates["positive_index"].value == Fraction(4)
        assert candidates["pair_sum_candidate"].value == Fraction(8)
        assert candidates["rank_double"].value == Fraction(48)
        assert candidates["signature_ratio"].value == Fraction(1, 6)

    def test_only_positive_index_is_proved_invariant(self):
        candidates = mukai_scalar_candidates()
        assert candidates["positive_index"].status == "proved-lattice-invariant"
        assert candidates["pair_sum_candidate"].status == "computed-candidate"
        assert "H_B" in candidates["pair_sum_candidate"].theorem_required
        assert "H_scalar" in candidates["pair_sum_candidate"].theorem_required
        assert "H_CFT" in candidates["rank_double"].theorem_required
        assert "H_anom" in candidates["signature_ratio"].theorem_required

    def test_bridge_is_arithmetic_tautology(self):
        report = candidate_bridge_report()
        assert report["left_side"] == Fraction(8)
        assert report["right_side"] == Fraction(8)
        assert report["arithmetic_identity"] is True
        assert report["epistemic_status"] == "tautological-lattice-arithmetic"
        assert report["chiral_conductor_status"] == "conjectured"
        assert report["hypothesis_package_name"] == B_FAMILY_PACKAGE_NAME
        assert report["missing_hypotheses"] == B_FAMILY_HYPOTHESES


class TestPrimarySourceAudit:
    def test_bruinier_actual_lemma(self):
        assert BRUINIER_LEMMA_5_1["source"].endswith("Lemma 5.1")
        assert "cyclotomic" in BRUINIER_LEMMA_5_1["actual_statement"]
        assert "lcm(N,8)" in BRUINIER_LEMMA_5_1["actual_statement"]
        assert BRUINIER_LEMMA_5_1["humbert_torsion_order_8"] is False
        assert BRUINIER_LEMMA_5_1["supports_mukai_conductor"] is False

    def test_lusztig_scope(self):
        assert "chosen" in LUSZTIG_ROOT_ORDER_SCOPE["actual_scope"]
        assert LUSZTIG_ROOT_ORDER_SCOPE["selects_order_8_from_mukai_lattice"] is False
        assert LUSZTIG_ROOT_ORDER_SCOPE["supports_mukai_conductor"] is False

    def test_three_faces_claim_is_retracted(self):
        audit = source_claim_audit()
        claim = audit["former_three_faces_claim"]
        assert claim["status"] == "retracted"
        assert "neither" in claim["reason"]

    def test_hbar_equality_is_normalization_only(self):
        audit = source_claim_audit()
        assert audit["hbar_identity"]["status"] == "normalization-tautology"
        assert audit["hbar_identity"]["chiral_status"] == "conjectured-under-H_B"
        assert "H_B supplies" in audit["hbar_identity"]["reason"]


class TestBFamilyProofObligations:
    def test_scope_is_candidate(self):
        scope = b_family_scope()
        assert scope["scope"] == "K3 Mukai-lattice candidate"
        assert scope["proved_input"] == (
            "H~(K3,Z) has rank 24 and signature (4,20)"
        )
        assert scope["candidate_value"] == Fraction(8)
        assert scope["candidate_status"] == "conjectured-as-chiral-conductor-under-H_B"
        assert scope["hypothesis_package_name"] == B_FAMILY_PACKAGE_NAME == "H_B"

    def test_five_named_hypotheses(self):
        scope = b_family_scope()
        hypotheses = scope["hypothesis_package"]
        assert hypotheses == B_FAMILY_HYPOTHESES
        assert len(hypotheses) == 5
        assert hypotheses[0].startswith("H_chart")
        assert hypotheses[1].startswith("H_KD")
        assert hypotheses[2].startswith("H_scalar")
        assert hypotheses[3].startswith("H_mod")
        assert hypotheses[4].startswith("H_quantum")


class TestTheoremCCandidateSurface:
    def test_bp_open_slot_stays_outside_numerical_ledger(self):
        values = set(theorem_c_candidate_values())
        assert Fraction(25, 3) not in values
        assert Fraction(98, 3) not in values

        bp_slot = bp_former_kappa_proposal()
        assert bp_slot["value"] == Fraction(25, 3)
        assert bp_slot["status"] == "former-conditional-proposal"
        assert bp_slot["epistemic_status"] == "retracted-derivation"
        assert "odd-parity" in bp_slot["invalidated_derivation"]
        assert bp_slot["active_status"] == "open-genus-one-computation"
        assert "genus-one curvature" in bp_slot["resolution_obligation"]

    def test_bp_source_packet_separates_exact_and_open_lanes(self):
        packet = bp_scalar_scope()

        # Independent FKR Eq. (2.2) samples and the k -> -k-6 symmetry.
        for level in (0, 1, -1, 2, -4):
            companion = -Fraction(level) - 6
            assert (
                fkr_standard_central_charge(level)
                + fkr_standard_central_charge(companion)
                == Fraction(50)
            )

        assert K_BP_EXACT == Fraction(50)
        assert packet["central_charge_conductor"] == Fraction(50)
        assert packet["central_charge_status"] == "proved-primary-source"
        assert packet["strong_generator_parities"] == (
            ("J", 0),
            ("G+", 0),
            ("G-", 0),
            ("T", 0),
        )
        assert packet["reciprocal_weight_diagnostic"] == (
            Fraction(1) + Fraction(2, 3) + Fraction(2, 3) + Fraction(1, 2)
        ) == Fraction(17, 6)
        assert packet["kappa_value"] is None
        assert KAPPA_COMPLEMENTARITY_EXACT is None
        assert packet["kappa_complementarity_value"] is None
        assert packet["kappa_status"] == "open-genus-one-computation"

    def test_candidate_set(self):
        assert set(theorem_c_candidate_values()) == {
            Fraction(0),
            Fraction(8),
            Fraction(13),
            Fraction(250, 3),
        }

    def test_certified_set_excludes_both_open_lanes(self):
        certified = set(theorem_c_certified_values())
        assert certified == {Fraction(0), Fraction(13), Fraction(250, 3)}
        assert Fraction(8) not in certified
        assert Fraction(25, 3) not in certified

    def test_every_value_has_status(self):
        ledger = theorem_c_status_ledger()
        assert set(ledger) == set(theorem_c_candidate_values())
        assert "conjectured B-row under H_B" in ledger[Fraction(8)]
        assert Fraction(25, 3) not in ledger
        assert "theorem-scoped" in ledger[Fraction(13)]


class TestEngine:
    def test_master_verification(self):
        report = verify_engine()
        assert report["status"] == "verified"
        assert report["source_audit"]["former_three_faces_claim"]["status"] == "retracted"
        assert (
            report["b_family"]["candidate_status"]
            == "conjectured-as-chiral-conductor-under-H_B"
        )
        assert report["theorem_c_certified"] == (
            Fraction(0),
            Fraction(13),
            Fraction(250, 3),
        )
        assert report["bp_open_slot"]["active_status"] == "open-genus-one-computation"
        assert report["bp_scope"]["central_charge_conductor"] == Fraction(50)
        assert report["bp_scope"]["kappa_complementarity_value"] is None

    def test_fabricated_apis_are_absent(self):
        source = ENGINE.read_text()
        assert "bruinier_heegner_h1_order" not in source
        assert "lusztig_root_of_unity_length" not in source
        assert "mukai_heisenberg_koszul_conductor" not in source
        assert "Humbert-H_1 reciprocity" not in source
        assert "universal B-family identity" not in source
