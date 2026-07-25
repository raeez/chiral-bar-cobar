r"""Exact theorem-scope certificates for bar--cobar reconstruction.

This module separates four maps which earlier versions of the computational
layer conflated.

``A``  The universal associative resolution

    epsilon_A : Omega Bar(A) -> A.

    In a pro-nilpotent stable symmetric-monoidal infinity-category this is an
    equivalence for every augmented associative algebra.  The relevant source
    is Francis--Gaitsgory, *Chiral Koszul duality* (2012), Proposition 4.1.2;
    their proof of Theorem 5.1.1 establishes pro-nilpotence for the chiral
    tensor category on ``D(Ran X)``.

``B``  The quadratic comparison

    q_A : A^i -> Bar(A).

    For a connected quadratic presentation this map is an equivalence exactly
    on the quadratic Koszul locus.  Equivalently, ``Omega(A^i) -> A`` is an
    equivalence and the left and right Koszul complexes are acyclic.  See
    Loday--Vallette (2012), Theorems 2.3.2 and 3.4.6.

``H``  The general completion theorem

    Heuts (2024), Theorem 2.1, identifies the unit of operadic Koszul duality
    with nilcompletion and the counit with conilcompletion.  It gives an
    equivalence between nilcomplete algebras and conilcomplete divided-power
    coalgebras.  This theorem supplies the correct boundary in a general
    ambient category; the Ran application already follows directly from the
    pro-nilpotent Francis--Gaitsgory theorem.

``V``  The Verdier object

    D_Ran Bar(A).

    Its identification with a chosen Koszul-dual algebra is a separate
    Verdier/finiteness statement.  None of the three preceding results supplies
    that identification by itself.

The executable part is deliberately finite.  It certifies hypotheses and map
signatures, and it checks the tensor-coalgebra combinatorics used in the first
worked examples.  It makes no family-wide claims about Virasoro, affine, W,
or minimal-model Koszulness.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb
from typing import Dict, Iterable, Optional, Tuple


FG_SOURCE = (
    "Francis--Gaitsgory (2012), Proposition 4.1.2 and proof of "
    "Theorem 5.1.1, arXiv:1103.5803"
)
HEUTS_SOURCE = "Heuts (2024), Theorem 2.1, arXiv:2408.06173"
LV_RESOLUTION_SOURCE = "Loday--Vallette (2012), Corollary 2.3.4"
LV_QUADRATIC_SOURCE = (
    "Loday--Vallette (2012), Theorems 2.3.2 and 3.4.6"
)
BL_SOURCE = "Booth--Lazarev, Global Koszul duality, arXiv:2304.08409"


@dataclass(frozen=True)
class AmbientSignature:
    """Hypotheses carried by an operadic ambient category."""

    name: str
    stable: bool
    presentable: bool
    symmetric_monoidal: bool
    tensor_preserves_colimits_separately: bool
    pro_nilpotent: bool

    @property
    def heuts_ready(self) -> bool:
        """Heuts' categorical hypotheses, independent of object completion."""

        return all(
            (
                self.stable,
                self.presentable,
                self.symmetric_monoidal,
                self.tensor_preserves_colimits_separately,
            )
        )

    @property
    def fg_ready(self) -> bool:
        """Francis--Gaitsgory's pro-nilpotent hypothesis package."""

        return self.heuts_ready and self.pro_nilpotent


RAN_CHIRAL_AMBIENT = AmbientSignature(
    name="(D(Ran X), tensor_ch)",
    stable=True,
    presentable=True,
    symmetric_monoidal=True,
    tensor_preserves_colimits_separately=True,
    pro_nilpotent=True,
)

ORDINARY_CHAIN_AMBIENT = AmbientSignature(
    name="(Ch_k, tensor)",
    stable=True,
    presentable=True,
    symmetric_monoidal=True,
    tensor_preserves_colimits_separately=True,
    pro_nilpotent=False,
)


@dataclass(frozen=True)
class MapCertificate:
    """A theorem claim together with its complete type signature."""

    theorem: str
    map_name: str
    domain: str
    codomain: str
    ambient: str
    hypotheses: Tuple[str, ...]
    status: str
    conclusion: str
    source: str

    @property
    def typed_map(self) -> str:
        return f"{self.map_name}: {self.domain} -> {self.codomain}"


def universal_resolution_certificate(
    ambient: AmbientSignature = RAN_CHIRAL_AMBIENT,
) -> MapCertificate:
    r"""Certify the universal map ``Omega Bar(A) -> A``.

    The result concerns the full bar coalgebra.  Quadratic presentation data
    and diagonal bar homology play no role in its type signature.
    """

    status = "proved-by-FG" if ambient.fg_ready else "hypothesis-open"
    conclusion = (
        "equivalence for every augmented associative algebra A"
        if ambient.fg_ready
        else "application awaits pro-nilpotence of the ambient category"
    )
    return MapCertificate(
        theorem="Theorem A: enhanced associative bar--cobar reconstruction",
        map_name="epsilon_A",
        domain="Omega_X Bar_X(A)",
        codomain="A",
        ambient=ambient.name,
        hypotheses=(
            "stable presentable symmetric-monoidal ambient",
            "tensor product preserves colimits separately",
            "pro-nilpotent ambient",
            "augmented associative algebra A",
        ),
        status=status,
        conclusion=conclusion,
        source=FG_SOURCE,
    )


def coalgebra_resolution_certificate(
    ambient: AmbientSignature = RAN_CHIRAL_AMBIENT,
) -> MapCertificate:
    r"""Certify the companion universal map ``C -> Bar Omega(C)``."""

    status = "proved-by-FG" if ambient.fg_ready else "hypothesis-open"
    conclusion = (
        "equivalence for every coalgebra in the enhanced FG target"
        if ambient.fg_ready
        else "application awaits pro-nilpotence of the ambient category"
    )
    return MapCertificate(
        theorem="Theorem A: enhanced associative bar--cobar reconstruction",
        map_name="eta_C",
        domain="C",
        codomain="Bar_X Omega_X(C)",
        ambient=ambient.name,
        hypotheses=(
            "stable presentable symmetric-monoidal ambient",
            "tensor product preserves colimits separately",
            "pro-nilpotent ambient",
            "coalgebra C in the enhanced bar target",
        ),
        status=status,
        conclusion=conclusion,
        source=FG_SOURCE,
    )


@dataclass(frozen=True)
class QuadraticPresentation:
    """Input data for the quadratic recognition theorem."""

    name: str
    connected: bool
    positive_weight: bool
    relation_degrees: Tuple[int, ...]
    filtered_realization_converges: bool
    q_quasi_isomorphism_verified: Optional[bool] = None

    @property
    def quadratic(self) -> bool:
        """A free presentation has ``R=0`` and is therefore quadratic."""

        return all(degree == 2 for degree in self.relation_degrees)

    @property
    def recognition_hypotheses(self) -> bool:
        return all(
            (
                self.connected,
                self.positive_weight,
                self.quadratic,
                self.filtered_realization_converges,
            )
        )


FREE_TENSOR_PRESENTATION = QuadraticPresentation(
    name="T(V)",
    connected=True,
    positive_weight=True,
    relation_degrees=(),
    filtered_realization_converges=True,
    q_quasi_isomorphism_verified=True,
)

DUAL_NUMBERS_PRESENTATION = QuadraticPresentation(
    name="k[e]/(e^2)",
    connected=True,
    positive_weight=True,
    relation_degrees=(2,),
    filtered_realization_converges=True,
    q_quasi_isomorphism_verified=True,
)

TRUNCATED_CUBIC_PRESENTATION = QuadraticPresentation(
    name="k[x]/(x^3)",
    connected=True,
    positive_weight=True,
    relation_degrees=(3,),
    filtered_realization_converges=True,
    q_quasi_isomorphism_verified=None,
)


def quadratic_comparison_certificate(
    presentation: QuadraticPresentation,
) -> MapCertificate:
    r"""Certify the scope of ``q_A: A^i -> Bar(A)``.

    ``q_quasi_isomorphism_verified`` records a supplied proof or computation;
    the engine never promotes a family to the Koszul locus from its name.
    """

    if not presentation.recognition_hypotheses:
        status = "outside-quadratic-signature"
        conclusion = (
            "the quadratic comparison requires connected positive-weight "
            "quadratic presentation data and convergent realization"
        )
    elif presentation.q_quasi_isomorphism_verified is True:
        status = "proved-koszul"
        conclusion = (
            "q_A, Omega(A^i)->A, and both Koszul-complex acyclicity "
            "conditions are equivalent and hold"
        )
    elif presentation.q_quasi_isomorphism_verified is False:
        status = "computed-off-koszul-locus"
        conclusion = "the supplied computation detects a nonzero cone of q_A"
    else:
        status = "criterion-open"
        conclusion = "the cone of q_A is the remaining proof obligation"

    return MapCertificate(
        theorem="Theorem B: quadratic Koszul recognition",
        map_name="q_A",
        domain="A^i",
        codomain="Bar_X(A)",
        ambient="connected positive-weight quadratic chiral presentation",
        hypotheses=(
            "A=T_X(V)/(R) with R in V tensor V",
            "connected positive-weight filtration",
            "convergent filtered realization",
        ),
        status=status,
        conclusion=conclusion,
        source=LV_QUADRATIC_SOURCE,
    )


def heuts_completion_certificate(
    ambient: AmbientSignature,
    *,
    algebra_nilcomplete: Optional[bool],
    coalgebra_conilcomplete: Optional[bool],
) -> Dict[str, object]:
    """Apply Heuts' Theorem 2.1 without inferring object completeness.

    The theorem identifies the unit and counit with completion maps.  A full
    equivalence for a specified pair therefore carries two explicit object
    hypotheses.
    """

    categorical_scope = "proved-by-Heuts" if ambient.heuts_ready else "ambient-open"
    pair_in_equivalence = (
        ambient.heuts_ready
        and algebra_nilcomplete is True
        and coalgebra_conilcomplete is True
    )
    return {
        "source": HEUTS_SOURCE,
        "ambient": ambient.name,
        "categorical_scope": categorical_scope,
        "algebra_unit": "A -> prim_BO indec_O(A) = nilcompletion(A)",
        "coalgebra_counit": (
            "indec_O prim_BO(C) -> C = conilcompletion counit"
        ),
        "algebra_nilcomplete": algebra_nilcomplete,
        "coalgebra_conilcomplete": coalgebra_conilcomplete,
        "pair_in_equivalence": pair_in_equivalence,
        "largest_complete_subcategories": ambient.heuts_ready,
    }


def verdier_comparison_certificate() -> MapCertificate:
    """Record the Verdier comparison as a separately hypothesized map."""

    return MapCertificate(
        theorem="Verdier--bar comparison",
        map_name="v_A",
        domain="D_Ran Bar_X(A)",
        codomain="A^!",
        ambient="Verdier-dualizable Ran objects",
        hypotheses=(
            "H_VD: Verdier dualizability and finite-type exchange",
            "a chosen algebra model A^! for the dual coalgebra",
        ),
        status="conditional-H_VD",
        conclusion="comparison is an equivalence when H_VD is discharged",
        source="manuscript Verdier hypothesis package H_VD",
    )


def booth_lazarev_transfer_certificate() -> Dict[str, object]:
    """Separate the abstract curved result from its Ran transfer problem."""

    return {
        "source": BL_SOURCE,
        "abstract_chain_complex_result": "proved",
        "abstract_result": (
            "extended curved bar--cobar is a Quillen equivalence for the "
            "model structures constructed by Booth--Lazarev"
        ),
        "ran_factorization_transfer": "open-hypothesis-package",
        "required_transfer_data": (
            "model structures on the chosen Ran/factorization categories",
            "compatibility of chiral tensor and weak equivalences",
            "curvature and completion compatibility",
        ),
    }


def comparison_table() -> Dict[str, MapCertificate]:
    """Return the four distinct manuscript claim surfaces."""

    return {
        "universal_algebra_resolution": universal_resolution_certificate(),
        "universal_coalgebra_resolution": coalgebra_resolution_certificate(),
        "quadratic_comparison": quadratic_comparison_certificate(
            FREE_TENSOR_PRESENTATION
        ),
        "verdier_comparison": verdier_comparison_certificate(),
    }


def bar_word_dimension(generator_dimension: int, bar_length: int) -> int:
    """Dimension of ``V^tensor bar_length`` for ``dim(V)=d``."""

    if generator_dimension < 0 or bar_length < 0:
        raise ValueError("dimensions and bar lengths are nonnegative")
    return generator_dimension**bar_length


def reduced_deconcatenation_summands(word_length: int, iterations: int) -> int:
    r"""Count summands in the iterated reduced coproduct of one word.

    ``iterations=r`` asks for ``r`` cuts and hence ``r+1`` nonempty blocks.
    The count is ``binomial(n-1,r)``.  In particular it vanishes for
    ``r >= n``, which is the elementwise conilpotence certificate for the
    direct-sum tensor coalgebra ``T^c(V)``.
    """

    if word_length < 0 or iterations < 0:
        raise ValueError("word lengths and iteration counts are nonnegative")
    if word_length == 0:
        return 0
    if iterations > word_length - 1:
        return 0
    return comb(word_length - 1, iterations)


def conilpotence_index(word_length: int) -> int:
    """First reduced-coproduct iterate vanishing on a word of length ``n``."""

    if word_length < 0:
        raise ValueError("word length is nonnegative")
    return word_length


def completed_tensor_element_is_conilpotent(
    nonzero_bar_lengths: Iterable[int],
) -> bool:
    """Test bounded bar-length support for a completed tensor element.

    A direct-sum tensor-coalgebra element has finite support automatically.
    A completed element represented by an unbounded stream of nonzero lengths
    has no finite elementwise conilpotence bound.  The caller supplies a finite
    sample here; an empty sample and every finite sample are bounded.  Infinite
    streams are handled by ``completed_support_certificate`` below.
    """

    lengths = tuple(nonzero_bar_lengths)
    if any(length < 0 for length in lengths):
        raise ValueError("bar lengths are nonnegative")
    return True


def completed_support_certificate(*, bounded_support: bool) -> Dict[str, object]:
    """Expose the direct-sum/completed-product distinction explicitly."""

    return {
        "bounded_bar_length_support": bounded_support,
        "elementwise_conilpotent": bounded_support,
        "completion_requires_separate_argument": True,
    }


def worked_case_packet() -> Dict[str, object]:
    """Return the first concrete cases before the general theorem table."""

    return {
        "free_tensor": {
            "presentation": FREE_TENSOR_PRESENTATION,
            "theorem_a": universal_resolution_certificate(),
            "theorem_b": quadratic_comparison_certificate(
                FREE_TENSOR_PRESENTATION
            ),
        },
        "dual_numbers": {
            "presentation": DUAL_NUMBERS_PRESENTATION,
            "theorem_a": universal_resolution_certificate(),
            "theorem_b": quadratic_comparison_certificate(
                DUAL_NUMBERS_PRESENTATION
            ),
        },
        "truncated_cubic": {
            "presentation": TRUNCATED_CUBIC_PRESENTATION,
            "theorem_a": universal_resolution_certificate(),
            "theorem_b": quadratic_comparison_certificate(
                TRUNCATED_CUBIC_PRESENTATION
            ),
        },
        "square_zero_bar_dimensions_d2": tuple(
            bar_word_dimension(2, length) for length in range(6)
        ),
    }


def verify_scope_engine() -> Dict[str, object]:
    """Run deterministic consistency checks and return a theorem ledger."""

    maps = comparison_table()
    typed_maps = {certificate.typed_map for certificate in maps.values()}
    assert len(typed_maps) == len(maps)

    theorem_a = maps["universal_algebra_resolution"]
    theorem_b = maps["quadratic_comparison"]
    assert theorem_a.map_name == "epsilon_A"
    assert theorem_b.map_name == "q_A"
    assert theorem_a.status == "proved-by-FG"
    assert theorem_b.status == "proved-koszul"

    for length in range(1, 9):
        assert reduced_deconcatenation_summands(length, length) == 0
        if length > 1:
            assert reduced_deconcatenation_summands(length, length - 1) == 1

    heuts_general = heuts_completion_certificate(
        ORDINARY_CHAIN_AMBIENT,
        algebra_nilcomplete=None,
        coalgebra_conilcomplete=None,
    )
    assert heuts_general["pair_in_equivalence"] is False

    return {
        "status": "verified",
        "maps": maps,
        "worked_cases": worked_case_packet(),
        "heuts_general": heuts_general,
        "booth_lazarev": booth_lazarev_transfer_certificate(),
        "scope_statement": (
            "Theorem A reconstructs the full bar object universally in the "
            "pro-nilpotent Ran ambient; Theorem B recognizes when the "
            "quadratic subcoalgebra already computes that full bar object."
        ),
    }


if __name__ == "__main__":
    report = verify_scope_engine()
    print(report["scope_statement"])
    for key, certificate in report["maps"].items():
        print(f"{key}: {certificate.typed_map} [{certificate.status}]")
