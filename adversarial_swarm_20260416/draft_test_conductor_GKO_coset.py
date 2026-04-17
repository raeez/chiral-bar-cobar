r"""draft_test_conductor_GKO_coset.py -- Test bank for draft_conductor_GKO_coset.

Tests the V28 follow-up prediction (Wave 13 §11):

        K(GKO coset (sl_2)_k x (sl_2)_1 / (sl_2)_{k+1})  =  20.

DISJOINTNESS RATIONALE (HZ3-11)
-------------------------------
  derived_from = ['V13/V14 GHOST IDENTITY ghost-additive coset rule
                   K(coset) = K(parent_in_cohomology) - K(embed)']
      = the conductor of the GKO coset is computed as the difference
        of the Virasoro conductor (parent in cohomology) and the affine
        Kac-Moody conductor of the gauged diagonal sl_2.  This is a
        CHAIN-LEVEL ghost-bookkeeping computation.  No CFT identity is
        invoked; only the additivity of the BRST ghost sum.

  verified_against = [
      'Polyakov 1981 critical bosonic-string ghost charge (c_ghost = -26)',
      'Goddard-Olive 1986 g-gauge ghost charge (c_ghost = -2 dim(g))',
      'BPZ 1984 Sugawara minimal-model central charge formula
       c = 1 - 6/((k+2)(k+3)), derived from Sugawara construction',
  ]
      = three independent CFT computations.  Polyakov's bc(2) charge
        comes from gauging worldsheet diffeomorphisms in the bosonic
        string.  Goddard-Olive's gauge ghost charge comes from
        gauging an internal Lie algebra symmetry.  BPZ's central
        charge comes from the Sugawara construction on (sl_2)_k.
        None of these uses BRST ghost-charge sums for cosets.

The agreement K(GKO) = 26 - 6 = 20 is therefore a substantive
prediction, not a tautology.

LOCAL HARNESS NOTE
------------------
Sibling-import pattern matches draft_test_climax_verification.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

# Local-draft sibling imports.
HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

# Vol I canonical independent-verification module.
VOL_I_ROOT = HERE.parent
if str(VOL_I_ROOT) not in sys.path:
    sys.path.insert(0, str(VOL_I_ROOT))

from compute.lib.independent_verification import independent_verification  # noqa: E402

import draft_conductor_GKO_coset as gk  # noqa: E402


_DERIVED = [
    'V13/V14 GHOST IDENTITY ghost-additive coset rule '
    'K(coset) = K(parent_in_cohomology) - K(embed)'
]
_VERIFIED = [
    'Polyakov 1981 critical bosonic-string ghost charge (c_ghost = -26)',
    'Goddard-Olive 1986 g-gauge ghost charge (c_ghost = -2 dim(g))',
    'BPZ 1984 Sugawara minimal-model central charge formula '
    'c = 1 - 6/((k+2)(k+3))',
]
_RATIONALE = (
    "K(GKO coset) = 20 is computed by ghost-additivity from K(Vir) and "
    "K(hat sl_2_1).  K(Vir) = 26 is the Polyakov 1981 reparametrisation "
    "ghost charge derived from worldsheet diffeomorphism gauging.  K(hat "
    "sl_2_1) = 6 is the Goddard-Olive 1986 g-gauge ghost charge derived "
    "from internal-symmetry gauging.  The BPZ Sugawara central charge "
    "c = 1 - 6/((k+2)(k+3)) confirms the cohomology IS Virasoro at minimal-"
    "model values.  None of these CFT inputs uses ghost-additive coset "
    "bookkeeping; their concurrence with K(GKO) = 26 - 6 = 20 is the "
    "Wave 13 §11 prediction."
)


# =============================================================================
# Headline test: K(GKO coset) = 20
# =============================================================================

@independent_verification(
    claim='conj:gko-coset-conductor-20',
    derived_from=_DERIVED,
    verified_against=_VERIFIED,
    disjoint_rationale=_RATIONALE,
)
def test_GKO_predicts_20():
    """The Vol I V6 prediction: K(GKO coset (sl_2)_1 x (sl_2)_1 / (sl_2)_2) = 20."""
    assert gk.gko_coset_kappa('sl_2', 1, 'sl_2', 2) == 20


@independent_verification(
    claim='conj:gko-coset-conductor-20',
    derived_from=_DERIVED,
    verified_against=_VERIFIED,
    disjoint_rationale=_RATIONALE,
)
def test_vir_minimal_via_gko_returns_20():
    """vir_minimal_via_gko() returns 20 at default k=1."""
    assert gk.vir_minimal_via_gko() == 20


@independent_verification(
    claim='conj:gko-coset-conductor-20',
    derived_from=_DERIVED,
    verified_against=_VERIFIED,
    disjoint_rationale=_RATIONALE,
)
def test_GKO_level_independence():
    """K(GKO coset) = 20 is independent of the level k.

    Both K(Vir) = 26 and K(hat sl_2_k) = 6 are level-independent in the
    ghost convention, so their difference is also level-independent.
    """
    for k in [1, 2, 3, 5, 10]:
        assert gk.vir_minimal_via_gko(k) == 20, k


# =============================================================================
# Decomposition test: 20 = 26 - 6
# =============================================================================

@independent_verification(
    claim='conj:gko-coset-conductor-20',
    derived_from=_DERIVED,
    verified_against=_VERIFIED,
    disjoint_rationale=_RATIONALE,
)
def test_decomposition_26_minus_6():
    """The 20 factorises as K(Vir) - K(KM_1(sl_2)) = 26 - 6 = 20."""
    K_Vir = gk.K_virasoro()
    K_KM = gk.K_affine_KM('sl_2')
    assert K_Vir == 26
    assert K_KM == 6
    assert K_Vir - K_KM == 20
    assert gk.gko_coset_kappa('sl_2', 1, 'sl_2', 2) == K_Vir - K_KM


@independent_verification(
    claim='conj:gko-coset-conductor-20',
    derived_from=_DERIVED,
    verified_against=_VERIFIED,
    disjoint_rationale=_RATIONALE,
)
def test_KM_ghost_charge_per_dim():
    """K(hat g_k) = 2 dim(g) for the standard simple algebras (Goddard-Olive 1986)."""
    expected = {
        'sl_2':   6,
        'sl_3':  16,
        'sl_4':  30,
        'so_8':  56,
        'g_2':   28,
        'e_6':  156,
        'e_8':  496,
    }
    for g, K in expected.items():
        assert gk.K_affine_KM(g) == K, (g, K)


# =============================================================================
# BPZ central charge cross-check
# =============================================================================

@independent_verification(
    claim='conj:gko-coset-conductor-20',
    derived_from=_DERIVED,
    verified_against=_VERIFIED,
    disjoint_rationale=_RATIONALE,
)
def test_BPZ_minimal_model_central_charges():
    """The GKO coset central charge matches BPZ minimal-model values:
        k=1 -> c = 1/2 (Ising, M(3,4))
        k=2 -> c = 7/10 (tricritical Ising, M(4,5))
        k=3 -> c = 4/5 (3-state Potts, M(5,6))
    """
    expected = {1: Fraction(1, 2), 2: Fraction(7, 10), 3: Fraction(4, 5)}
    for k, c in expected.items():
        assert gk.gko_central_charge(k) == c, (k, c)


# =============================================================================
# Standard tabulated cosets
# =============================================================================

@independent_verification(
    claim='conj:gko-coset-conductor-20',
    derived_from=_DERIVED,
    verified_against=_VERIFIED,
    disjoint_rationale=_RATIONALE,
)
def test_all_standard_cosets_have_K_20():
    """Every tabulated GKO coset has the same K = 20 (level-independence)."""
    table = gk.all_standard_coset_conductors()
    assert table, "no standard cosets tabulated"
    for name, K in table.items():
        assert K == 20, (name, K)


# =============================================================================
# Defensive checks
# =============================================================================

def test_dim_lookup_unknown_raises():
    """Unknown Lie algebras raise KeyError (defensive against typos)."""
    import pytest
    with pytest.raises(KeyError):
        gk.dim_g('sl_42')


def test_non_diagonal_embedding_raises():
    """Mismatched parent/embed raises ValueError (the GKO ghost-additive
    formula is for diagonal embeddings only; off-diagonal cosets require
    the more general Wave 13 §11 formula K(G/H) = K(G) - K(H) + K_BRST)."""
    import pytest
    with pytest.raises(ValueError):
        gk.gko_coset_kappa('sl_3', 1, 'sl_2', 2)


def test_report_smoke():
    """Smoke test for the human-readable report."""
    text = gk.report()
    assert "K(GKO coset)" in text
    assert "20" in text
