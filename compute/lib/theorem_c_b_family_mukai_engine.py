r"""K3 Mukai-lattice verification and B-row claim firewall.

The proved input is the integral Mukai lattice

    H~(X,Z) = H^0(X,Z) (+) H^2(X,Z) (+) H^4(X,Z)
             ~= U^4 (+) E8(-1)^2

for a complex K3 surface ``X``.  It has rank 24 and signature ``(4,20)``.
This module verifies that statement through three routes:

1. the K3 lattice ``H^2 ~= U^3 (+) E8(-1)^2`` plus the Mukai hyperbolic
   plane ``H^0 (+) H^4``;
2. the Betti number ``b2=22`` and Hirzebruch signature
   ``(c1^2-2c2)/3=-16``;
3. an explicit even unimodular Gram matrix of rank 24.

The arithmetic numbers

    c_+ = 4,  2c_+ = 8,  rank = 24,  2 rank = 48,
    c_+/rank = 1/6

therefore follow.  Their interpretation as chiral Koszul conductors requires
new mathematics: an open chiral chart attached to the indefinite Mukai
lattice, a proof of its quadratic comparison ``q_A``, a scalar-normalization
theorem, and the relevant modular/quantum bridges.

Two former citations supplied no such theorem.

* Bruinier (2002), Lemma 5.1, concerns cyclotomic fields of Fourier
  coefficients of vector-valued cusp forms.  In half-integral weight it uses
  ``lcm(N,8)``.  It does not compute an order-eight Humbert monodromy class.
* Lusztig's root-of-unity quantum groups depend on a chosen root order.  The
  cited work contains no construction selecting order eight from a K3 Mukai
  lattice.

Accordingly, the value eight remains a computed candidate under the complete
``H_B`` comparison package, while the claimed Bruinier--Mukai--Lusztig
equality is retracted as a theorem.  The Bershadsky--Polyakov lane supplies a
second firewall: its standard central-charge conductor is exactly ``50``,
whereas its modular characteristic is a status-only invariant pending a
genus-one curvature calculation.  The engine makes both epistemic
boundaries executable.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Mapping, Tuple

from sympy import Matrix, diag

try:
    from compute.lib.bp_koszul_conductor_engine import (
        BP_GENERATORS,
        BP_KAPPA_STATUS,
        KAPPA_COMPLEMENTARITY_EXACT,
        K_BP_EXACT,
        compute_varrho,
    )
except ModuleNotFoundError:  # direct execution from compute/lib
    from bp_koszul_conductor_engine import (
        BP_GENERATORS,
        BP_KAPPA_STATUS,
        KAPPA_COMPLEMENTARITY_EXACT,
        K_BP_EXACT,
        compute_varrho,
    )


B_FAMILY_PACKAGE_NAME = "H_B"


def hyperbolic_plane() -> Matrix:
    """Gram matrix of the even unimodular hyperbolic plane ``U``."""

    return Matrix([[0, 1], [1, 0]])


def e8_cartan_matrix() -> Matrix:
    """A positive-definite even Gram matrix for the ``E8`` root lattice."""

    matrix = 2 * Matrix.eye(8)
    for index in range(6):
        matrix[index, index + 1] = -1
        matrix[index + 1, index] = -1
    matrix[2, 7] = -1
    matrix[7, 2] = -1
    return matrix


def k3_h2_gram_matrix() -> Matrix:
    r"""Gram matrix of ``H^2(K3,Z) ~= U^3 (+) E8(-1)^2``."""

    u = hyperbolic_plane()
    e8_negative = -e8_cartan_matrix()
    return diag(u, u, u, e8_negative, e8_negative)


def mukai_gram_matrix() -> Matrix:
    r"""Gram matrix of ``H~(K3,Z) ~= U^4 (+) E8(-1)^2``."""

    return diag(hyperbolic_plane(), k3_h2_gram_matrix())


def mukai_signature_from_blocks() -> Tuple[int, int]:
    """Block-decomposition signature ``4(1,1)+2(0,8)=(4,20)``."""

    return (4, 20)


def k3_signature_from_hirzebruch() -> int:
    r"""Compute ``sigma(K3)=(c1^2-2c2)/3=-16``."""

    c1_squared = 0
    c2 = 24
    return (c1_squared - 2 * c2) // 3


def k3_h2_signature_from_betti() -> Tuple[int, int]:
    """Recover ``(b2+,b2-)=(3,19)`` from ``b2=22`` and ``sigma=-16``."""

    b2 = 22
    signature = k3_signature_from_hirzebruch()
    b2_plus = (b2 + signature) // 2
    b2_minus = (b2 - signature) // 2
    return (b2_plus, b2_minus)


def mukai_signature_from_hirzebruch() -> Tuple[int, int]:
    """Add the Mukai hyperbolic plane to the K3 intersection form."""

    positive, negative = k3_h2_signature_from_betti()
    return (positive + 1, negative + 1)


def k3_betti_numbers() -> Tuple[int, int, int, int, int]:
    """Integral Betti numbers ``(b0,...,b4)=(1,0,22,0,1)``."""

    return (1, 0, 22, 0, 1)


def k3_euler_characteristic() -> int:
    """Euler characteristic of K3, equal to 24."""

    return sum((-1) ** degree * value for degree, value in enumerate(k3_betti_numbers()))


def mukai_signature() -> Tuple[int, int]:
    """Canonical signature of the integral Mukai lattice."""

    by_blocks = mukai_signature_from_blocks()
    by_hirzebruch = mukai_signature_from_hirzebruch()
    if by_blocks != by_hirzebruch:
        raise AssertionError("the two Mukai-signature computations disagree")
    return by_blocks


def mukai_rank() -> int:
    """Rank of the Mukai lattice."""

    positive, negative = mukai_signature()
    return positive + negative


def mukai_c_plus() -> int:
    """Positive index of the Mukai pairing."""

    return mukai_signature()[0]


def mukai_c_minus() -> int:
    """Negative index of the Mukai pairing."""

    return mukai_signature()[1]


def verify_mukai_lattice() -> Dict[str, object]:
    """Return the three-path lattice certificate."""

    e8 = e8_cartan_matrix()
    mukai = mukai_gram_matrix()
    leading_minors = tuple(
        e8[:size, :size].det() for size in range(1, e8.rows + 1)
    )
    return {
        "status": "proved",
        "signature_by_blocks": mukai_signature_from_blocks(),
        "signature_by_hirzebruch": mukai_signature_from_hirzebruch(),
        "k3_h2_signature": k3_h2_signature_from_betti(),
        "hirzebruch_signature": k3_signature_from_hirzebruch(),
        "betti_numbers": k3_betti_numbers(),
        "euler_characteristic": k3_euler_characteristic(),
        "gram_rank": int(mukai.rank()),
        "gram_determinant": int(mukai.det()),
        "gram_symmetric": mukai == mukai.T,
        "gram_even": all(mukai[index, index] % 2 == 0 for index in range(mukai.rows)),
        "e8_positive_by_sylvester": all(value > 0 for value in leading_minors),
        "e8_determinant": int(e8.det()),
    }


@dataclass(frozen=True)
class ScalarCandidate:
    """An arithmetic expression with an explicit epistemic status."""

    name: str
    value: Fraction
    derivation: str
    status: str
    theorem_required: str


def mukai_scalar_candidates() -> Mapping[str, ScalarCandidate]:
    """Arithmetic candidates obtained from the proved lattice signature."""

    rank = Fraction(mukai_rank())
    positive = Fraction(mukai_c_plus())
    return {
        "positive_index": ScalarCandidate(
            name="c_+(Mukai(K3))",
            value=positive,
            derivation="positive index of signature (4,20)",
            status="proved-lattice-invariant",
            theorem_required="none",
        ),
        "pair_sum_candidate": ScalarCandidate(
            name="2 c_+(Mukai(K3))",
            value=2 * positive,
            derivation="arithmetic doubling of the positive index",
            status="computed-candidate",
            theorem_required=(
                "H_B supplies H_chart, H_KD, H_scalar, H_mod, and H_quantum; "
                "H_scalar identifies this number with kappa(A)+kappa(A^!)"
            ),
        ),
        "rank_double": ScalarCandidate(
            name="2 rank(Mukai(K3))",
            value=2 * rank,
            derivation="arithmetic doubling of rank 24",
            status="computed-lattice-number",
            theorem_required="H_CFT constructs a conformal theory with c=c^!=24",
        ),
        "signature_ratio": ScalarCandidate(
            name="c_+/rank",
            value=positive / rank,
            derivation="4/24",
            status="computed-lattice-ratio",
            theorem_required="H_anom identifies this ratio with a chiral anomaly coefficient",
        ),
    }


def candidate_bridge_report() -> Dict[str, object]:
    r"""Check the arithmetic identity ``(c_+/rank)(2rank)=2c_+``.

    The equality is tautological from the three definitions.  Its promotion to
    a theorem about chiral algebras requires the hypotheses recorded below.
    """

    candidates = mukai_scalar_candidates()
    ratio = candidates["signature_ratio"].value
    rank_double = candidates["rank_double"].value
    pair_sum = candidates["pair_sum_candidate"].value
    return {
        "left_side": ratio * rank_double,
        "right_side": pair_sum,
        "arithmetic_identity": ratio * rank_double == pair_sum,
        "epistemic_status": "tautological-lattice-arithmetic",
        "chiral_conductor_status": "conjectured",
        "hypothesis_package_name": B_FAMILY_PACKAGE_NAME,
        "missing_hypotheses": B_FAMILY_HYPOTHESES,
    }


BRUINIER_LEMMA_5_1 = {
    "source": "Bruinier, LNM 1780 (2002), Lemma 5.1",
    "actual_statement": (
        "S_{kappa,L} has a basis with Fourier coefficients in a cyclotomic "
        "integer ring; in half-integral weight the field uses N'=lcm(N,8)"
    ),
    "humbert_torsion_order_8": False,
    "supports_mukai_conductor": False,
}


LUSZTIG_ROOT_ORDER_SCOPE = {
    "source": (
        "Lusztig, Finite-dimensional Hopf algebras arising from quantized "
        "universal enveloping algebra, JAMS 3 (1990), 257--296"
    ),
    "actual_scope": "construction at a chosen admissible root-of-unity order",
    "selects_order_8_from_mukai_lattice": False,
    "supports_mukai_conductor": False,
}


def source_claim_audit() -> Dict[str, object]:
    """Return the citation audit for the former three-faces argument."""

    return {
        "bruinier": dict(BRUINIER_LEMMA_5_1),
        "lusztig": dict(LUSZTIG_ROOT_ORDER_SCOPE),
        "former_three_faces_claim": {
            "claim": "Bruinier order = Mukai doubling = Lusztig ell = 8",
            "status": "retracted",
            "reason": (
                "the cited sources provide neither the asserted order-eight "
                "Humbert class nor a functor selecting root order eight"
            ),
        },
        "hbar_identity": {
            "claim": "hbar^2 K = -1 with hbar^2=-1/8 and K=8",
            "status": "normalization-tautology",
            "chiral_status": "conjectured-under-H_B",
            "reason": (
                "substitution proves the scalar equality; H_B supplies the "
                "chart, Koszul, scalar, modular, and quantum bridges"
            ),
        },
    }


B_FAMILY_HYPOTHESES: Tuple[str, ...] = (
    "H_chart: construct an augmented chiral chart from the indefinite Mukai lattice",
    "H_KD: prove q_A:A^i->Bar_X(A) is an equivalence and identify A^!",
    "H_scalar: prove kappa(A)+kappa(A^!)=2c_+(Mukai(K3))",
    "H_mod: construct the claimed Humbert/Borcherds modular comparison",
    "H_quantum: construct a functor selecting root order eight",
)


def b_family_scope() -> Dict[str, object]:
    """Return the exact proof obligations for the proposed B-row."""

    return {
        "scope": "K3 Mukai-lattice candidate",
        "proved_input": "H~(K3,Z) has rank 24 and signature (4,20)",
        "candidate_value": Fraction(8),
        "candidate_status": "conjectured-as-chiral-conductor-under-H_B",
        "hypothesis_package_name": B_FAMILY_PACKAGE_NAME,
        "hypothesis_package": B_FAMILY_HYPOTHESES,
        "source_audit": source_claim_audit(),
    }


def theorem_c_certified_values() -> Tuple[Fraction, ...]:
    """Certified numerical scalar lanes in the current Theorem C census."""

    return (Fraction(0), Fraction(13), Fraction(250, 3))


def theorem_c_candidate_values() -> Tuple[Fraction, ...]:
    """Active numerical ledger: certified lanes plus the ``H_B`` candidate.

    The tuple itself is arithmetic.  The B-row value eight carries the status
    returned by ``b_family_scope``; object-level interpretations of the other
    family values retain their own theorem packages elsewhere.  The BP lane
    has no active number and therefore lies outside this tuple.
    """

    return tuple(sorted((*theorem_c_certified_values(), Fraction(8))))


def theorem_c_status_ledger() -> Dict[Fraction, str]:
    """Attach an epistemic status to every current scalar candidate."""

    return {
        Fraction(0): "computed scalar lane; object-level package family-dependent",
        Fraction(8): "conjectured B-row under H_B from Mukai lattice arithmetic",
        Fraction(13): "computed Virasoro scalar identity; duality theorem-scoped",
        Fraction(250, 3): "computed principal-W3 scalar identity; duality theorem-scoped",
    }


def bp_former_kappa_proposal() -> Dict[str, object]:
    """Return the retracted BP proposal as historical status data."""

    return {
        "value": Fraction(25, 3),
        "status": "former-conditional-proposal",
        "epistemic_status": "retracted-derivation",
        "invalidated_derivation": BP_KAPPA_STATUS.invalidated_derivation,
        "active_status": BP_KAPPA_STATUS.status,
        "resolution_obligation": BP_KAPPA_STATUS.resolution_obligation,
    }


def bp_scalar_scope() -> Dict[str, object]:
    """Expose exact BP data and the status-only modular-characteristic lane."""

    return {
        "central_charge_conductor": K_BP_EXACT,
        "central_charge_status": "proved-primary-source",
        "strong_generator_parities": tuple(
            (name, parity) for name, (_weight, parity) in BP_GENERATORS.items()
        ),
        "reciprocal_weight_diagnostic": compute_varrho(),
        "reciprocal_weight_status": "computed-parity-diagnostic-only",
        "kappa_value": None,
        "kappa_complementarity_value": KAPPA_COMPLEMENTARITY_EXACT,
        "kappa_status": BP_KAPPA_STATUS.status,
        "resolution_obligation": BP_KAPPA_STATUS.resolution_obligation,
        "former_conditional_proposal": bp_former_kappa_proposal(),
    }


def verify_engine() -> Dict[str, object]:
    """Run the lattice, source, and status checks."""

    lattice = verify_mukai_lattice()
    assert lattice["signature_by_blocks"] == (4, 20)
    assert lattice["signature_by_hirzebruch"] == (4, 20)
    assert lattice["gram_rank"] == 24
    assert abs(lattice["gram_determinant"]) == 1
    assert lattice["gram_even"] is True
    assert lattice["e8_positive_by_sylvester"] is True

    candidates = mukai_scalar_candidates()
    assert candidates["pair_sum_candidate"].value == 8
    bridge = candidate_bridge_report()
    assert bridge["arithmetic_identity"] is True
    assert bridge["chiral_conductor_status"] == "conjectured"
    assert bridge["hypothesis_package_name"] == B_FAMILY_PACKAGE_NAME

    audit = source_claim_audit()
    assert audit["former_three_faces_claim"]["status"] == "retracted"
    assert audit["bruinier"]["supports_mukai_conductor"] is False
    assert audit["lusztig"]["supports_mukai_conductor"] is False

    certified = theorem_c_certified_values()
    active = theorem_c_candidate_values()
    assert certified == (Fraction(0), Fraction(13), Fraction(250, 3))
    assert Fraction(8) in active and Fraction(8) not in certified
    assert Fraction(25, 3) not in active

    bp_scope = bp_scalar_scope()
    assert bp_scope["central_charge_conductor"] == Fraction(50)
    assert all(parity == 0 for _name, parity in bp_scope["strong_generator_parities"])
    assert bp_scope["reciprocal_weight_diagnostic"] == Fraction(17, 6)
    assert bp_scope["kappa_value"] is None
    assert bp_scope["kappa_complementarity_value"] is None
    assert bp_scope["kappa_status"] == "open-genus-one-computation"

    return {
        "status": "verified",
        "lattice": lattice,
        "candidates": candidates,
        "bridge": bridge,
        "source_audit": audit,
        "b_family": b_family_scope(),
        "theorem_c_candidates": active,
        "theorem_c_certified": certified,
        "theorem_c_status": theorem_c_status_ledger(),
        "bp_open_slot": bp_former_kappa_proposal(),
        "bp_scope": bp_scope,
    }


if __name__ == "__main__":
    report = verify_engine()
    print(f"Mukai lattice: {report['lattice']['signature_by_blocks']}")
    print(f"B-row candidate status: {report['b_family']['candidate_status']}")
    print(f"BP central-charge conductor: {report['bp_scope']['central_charge_conductor']}")
    print(f"BP kappa status: {report['bp_scope']['kappa_status']}")
    print(
        "Former Bruinier--Mukai--Lusztig claim: "
        f"{report['source_audit']['former_three_faces_claim']['status']}"
    )
