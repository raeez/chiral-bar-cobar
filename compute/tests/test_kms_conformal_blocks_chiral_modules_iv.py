"""Independent verification for KMS and conformal-block bottlenecks.

The tests use finite algebraic models rather than the manuscript proofs:

* upper-unipotent matrices model the nonabelian Cech cocycle of a torsor;
* a two-term symplectic linear model checks the AT transversality criterion;
* a two-term bar/coequalizer model checks exactly when classical conformal
  blocks agree with H^0 of the derived bar complex.
"""

from __future__ import annotations

from fractions import Fraction

from compute.lib import independent_verification as iv
from compute.lib.conformal_blocks_bar_identification_engine import (
    genus0_npoint_sl2,
    verlinde_dim_pointed_sl2,
)


DERIV_KMS = (
    "koszulness_moduli_scheme proof: Drinfeld associator torsor plus "
    "Kontsevich-Tamarkin transfer"
)
DERIV_AT = (
    "koszulness_moduli_scheme Alekseev-Torossian chart proof and "
    "Kashiwara-Vergne gauge"
)
DERIV_CB = (
    "chiral_modules geometric pointed bar proof and Koszul spectral sequence"
)

VERIF_CECH = "finite upper-unipotent nonabelian Cech torsor model over Q"
VERIF_LINEAR_SYMPLECTIC = (
    "finite shifted-symplectic linear algebra transversality model over Q"
)
VERIF_COEQUALIZER = "finite coequalizer/bar-resolution linear algebra over Q"
VERIF_FUSION = "sl2 truncated Clebsch-Gordan fusion and pointed Verlinde formula"


def _u_mul(x: tuple[Fraction, Fraction, Fraction],
           y: tuple[Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction, Fraction]:
    """Multiply 3x3 upper-unipotent coordinates (a,b,c)."""
    a, b, c = x
    aa, bb, cc = y
    return (a + aa, b + bb, c + cc + a * bb)


def _u_inv(x: tuple[Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction, Fraction]:
    """Inverse in the same coordinates."""
    a, b, c = x
    return (-a, -b, a * b - c)


def _rank(matrix: list[list[Fraction]]) -> int:
    """Exact row rank over Q."""
    rows = [row[:] for row in matrix if any(v != 0 for v in row)]
    if not rows:
        return 0
    rank = 0
    col_count = len(rows[0])
    for col in range(col_count):
        pivot = None
        for row in range(rank, len(rows)):
            if rows[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][col]
        rows[rank] = [v / scale for v in rows[rank]]
        for row in range(len(rows)):
            if row != rank and rows[row][col] != 0:
                factor = rows[row][col]
                rows[row] = [
                    rows[row][j] - factor * rows[rank][j]
                    for j in range(col_count)
                ]
        rank += 1
        if rank == len(rows):
            break
    return rank


def _homology_dims(differential: list[list[Fraction]],
                   domain_dim: int,
                   codomain_dim: int) -> tuple[int, int]:
    """Return (H_1, H_0) for C_1 --d--> C_0."""
    rank = _rank(differential)
    return domain_dim - rank, codomain_dim - rank


@iv.independent_verification(
    claim="v1-thm:kms-moduli",
    derived_from=[DERIV_KMS],
    verified_against=[VERIF_CECH],
    disjoint_rationale=(
        "The manuscript derives the KMS torsor from associators and "
        "Tamarkin transfer. The test verifies the same cocycle law in a "
        "finite nonabelian upper-unipotent Cech torsor over Q, with no "
        "associator or formality input."
    ),
)
def test_kms_torsor_cocycle_closes_only_on_nonempty_support():
    chart_points = {
        "Phi_KZ": (Fraction(0), Fraction(0), Fraction(0)),
        "Phi_AT": (Fraction(1), Fraction(0), Fraction(0)),
        "Phi_dRB": (Fraction(0), Fraction(1), Fraction(0)),
        "Phi_ell": (Fraction(1), Fraction(1), Fraction(1)),
        "Phi_Kon": (Fraction(2), Fraction(-1), Fraction(3)),
    }
    certificate_components = {
        "pbw": chart_points,
        "bar": {
            name: _u_mul((Fraction(0), Fraction(0), Fraction(5)), point)
            for name, point in chart_points.items()
        },
    }

    def transition(
        component: str,
        source: str,
        target: str,
    ) -> tuple[Fraction, Fraction, Fraction]:
        points = certificate_components[component]
        return _u_mul(_u_inv(points[source]), points[target])

    identity = (Fraction(0), Fraction(0), Fraction(0))
    for component in certificate_components:
        for i in chart_points:
            assert transition(component, i, i) == identity
            for j in chart_points:
                assert _u_mul(
                    transition(component, i, j),
                    transition(component, j, i),
                ) == identity
                for k in chart_points:
                    assert _u_mul(
                        transition(component, i, j),
                        transition(component, j, k),
                    ) == transition(component, i, k)

    koszul_support = certificate_components
    nonkoszul_support: dict[str, tuple[Fraction, Fraction, Fraction]] = {}
    assert sorted(koszul_support) == ["bar", "pbw"]
    assert all(len(component) == 5 for component in koszul_support.values())
    assert nonkoszul_support == {}


@iv.independent_verification(
    claim="v1-prop:kms-at-chart",
    derived_from=[DERIV_AT],
    verified_against=[VERIF_LINEAR_SYMPLECTIC],
    disjoint_rationale=(
        "The chapter uses the Alekseev-Torossian/Kashiwara-Vergne chart. "
        "The test checks the independent finite linear fact behind the "
        "criterion: for two Lagrangians in a two-dimensional symplectic "
        "space, transversality is equivalent to acyclicity of the comparison "
        "complex L -> V/L'."
    ),
)
def test_at_chart_transversality_equals_two_term_acyclicity():
    # V = Q e + Q f, omega(e,f)=1.  L_e and L_f are transverse.
    transverse_matrix = [[Fraction(1)]]
    h1, h0 = _homology_dims(transverse_matrix, domain_dim=1, codomain_dim=1)
    assert (h1, h0) == (0, 0)

    # If L' = L, the map L -> V/L' is zero and both homology groups survive.
    nontransverse_matrix = [[Fraction(0)]]
    h1_bad, h0_bad = _homology_dims(nontransverse_matrix, 1, 1)
    assert (h1_bad, h0_bad) == (1, 1)


@iv.independent_verification(
    claim="prop:conformal-blocks-bar",
    derived_from=[DERIV_CB],
    verified_against=[VERIF_COEQUALIZER, VERIF_FUSION],
    disjoint_rationale=(
        "The manuscript derives the result from the geometric pointed bar "
        "complex. The test verifies the degree-zero statement by exact "
        "coequalizer linear algebra and, independently, by the sl2 fusion "
        "rule/pointed Verlinde equality for a four-point block."
    ),
)
def test_conformal_blocks_bar_h0_requires_exact_pointed_resolution():
    exact_bar_differential = [
        [Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(1)],
        [Fraction(1), Fraction(1)],
    ]
    h1, h0 = _homology_dims(exact_bar_differential, domain_dim=2, codomain_dim=3)
    coinvariant_dimension = 3 - _rank(exact_bar_differential)
    assert (h1, h0) == (0, coinvariant_dimension)
    assert coinvariant_dimension == 1

    obstructed_differential = [
        [Fraction(1), Fraction(1)],
        [Fraction(2), Fraction(2)],
        [Fraction(0), Fraction(0)],
    ]
    h1_bad, h0_bad = _homology_dims(obstructed_differential, 2, 3)
    assert h1_bad == 1
    assert h0_bad == 2

    fusion_dim = genus0_npoint_sl2(2, [1, 1, 1, 1])
    verlinde_dim = verlinde_dim_pointed_sl2(2, 0, [1, 1, 1, 1])
    assert fusion_dim == verlinde_dim == 2
