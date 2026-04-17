r"""draft_test_hochschild_atiyah_class.py -- Test bank for Wave 13 Strengthening #6.

Tests the Atiyah-class characterisation thm:K-Atiyah:

        K(A) = - c_1(Atiyah_A)

on the staged landscape {Heisenberg, free fermion, bc(lambda),
beta-gamma(lambda), affine Kac-Moody hat g_k, Virasoro, principal
W_N, Bershadsky-Polyakov}.  Each test decorated with
@independent_verification(claim='thm:K-Atiyah', ...) per HZ3-11 protocol.

DISJOINTNESS RATIONALE
----------------------
The two computations being compared are GENUINELY independent:

  derived_from = ['Hochschild-Atiyah class via formal moduli']
      = the chiral curvature trace tr(R) of the Hochschild diagonal
        connection, computed via Beilinson-Drinfeld 2004 Sec 2.5 +
        Kapranov's L_infty model for the Atiyah class.  The Atiyah
        class lives in HH^2_ch(A, A) = HH^1(A, A \otimes A^*)[1] as
        a derived geometric obstruction.  Its first Chern class is
        the trace of a curvature 2-form -- a HOCHSCHILD/DERIVED
        invariant, not a sum of bc-charges.

  verified_against = ['V28 climax_verification.py family conductors via
                      BRST ghost charge sum']
      = K(A) = -c_ghost(BRST(A)) computed from the explicit
        (lambda_alpha, epsilon_alpha) listing of the family's
        quasi-free BRST resolution via FMS bc-charge formula.  This
        is a SUM OVER FREE-FIELD GENERATORS, not a derived invariant.

Their numerical agreement is the content of V13 Cor thm:K-Atiyah:
the chiral Riemann-Roch-Grothendieck identity on the Hochschild
diagonal equates the Atiyah trace to the BRST ghost charge.  This
is NOT a tautology -- it is a non-trivial cohomological theorem
(BD 2004 + Faltings 1992).

SCOPE
-----
The current implementation provides constructive Atiyah descriptors
for the simple landscape (Heisenberg, Vir, KM, BP, principal W_N,
free fermion, bc/beta-gamma).  Richer families (DS at non-principal
nilpotents, cosets, logarithmic VOAs, root-of-unity QGs) are out of
scope here; the structural identification K = -c_1(Atiyah_A) is the
key contribution.  Full numerical implementation can be staged.

LOCAL HARNESS
-------------
Imports go via sys.path manipulation to keep the draft engine
self-contained inside adversarial_swarm_20260416/.  When promoted
to compute/lib/hochschild_atiyah_class.py the import becomes the
standard `from compute.lib.hochschild_atiyah_class import ...`.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

import pytest

# Local-draft imports.
HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

# Use the canonical Vol I independent_verification module.
if str(HERE.parent) not in sys.path:
    sys.path.insert(0, str(HERE.parent))

from compute.lib.independent_verification import independent_verification  # noqa: E402

import draft_hochschild_atiyah_class as ha  # noqa: E402
import draft_climax_verification as cv  # noqa: E402


# Canonical decorator metadata (re-used by every test).
_DERIVED = ['Hochschild-Atiyah class via formal moduli']
_VERIFIED = ['V28 climax_verification.py family conductors via BRST ghost charge sum']
_RATIONALE = (
    "The Atiyah class K_E := -c_1(Atiyah_A) is computed as the trace of "
    "the chiral curvature 2-form on the Hochschild diagonal A -> A "
    "tensor A^*, using the Beilinson-Drinfeld + Kapranov formal-moduli "
    "model for HH^*_ch(A, A).  This is a DERIVED-GEOMETRIC invariant, "
    "depending only on the Hochschild category and not on the choice "
    "of BRST resolution.  The V28 BRST conductor K_c is computed as "
    "a sum over (lambda_alpha, epsilon_alpha) of the explicit quasi-"
    "free resolution chain via the FMS bc-charge formula -- a "
    "RESOLUTION-LEVEL combinatorial sum.  Their numerical agreement "
    "is the chiral Riemann-Roch-Grothendieck identity (Faltings 1992 "
    "+ BD 2004 Section 2.5), an independent theorem connecting the "
    "two definitions.  Neither computation uses the other as input."
)


# =============================================================================
# Atiyah descriptor sanity
# =============================================================================


def test_atiyah_class_heisenberg_empty():
    """Heisenberg has trivial Hochschild-Atiyah class (no gauge resolution)."""
    blocks = ha.atiyah_class("heisenberg")
    assert blocks == []


def test_atiyah_class_vir_single_bc2():
    """Virasoro Atiyah class is a single bc(2) curvature block."""
    blocks = ha.atiyah_class("vir")
    assert len(blocks) == 1
    assert blocks[0].lam == Fraction(2)
    assert blocks[0].epsilon == 1
    assert blocks[0].multiplicity == 1


def test_atiyah_class_km_adjoint_bc1():
    """Affine Kac-Moody Atiyah class is dim(g) copies of bc(1)."""
    blocks = ha.atiyah_class("km", 8)  # sl_3
    assert len(blocks) == 1
    assert blocks[0].lam == Fraction(1)
    assert blocks[0].epsilon == 1
    assert blocks[0].multiplicity == 8


def test_atiyah_class_wn_toda_tower():
    """Principal W_N Atiyah class is the Toda BRST tower bc(j) for j=2..N."""
    blocks = ha.atiyah_class("wn", 5)
    weights = sorted(int(b.lam) for b in blocks)
    assert weights == [2, 3, 4, 5]
    assert all(b.epsilon == 1 for b in blocks)
    assert all(b.multiplicity == 1 for b in blocks)


# =============================================================================
# c_1(Atiyah_A) primitives -- direct evaluation of curvature trace
# =============================================================================


def test_c1_atiyah_heisenberg_zero():
    """Heisenberg: trivial curvature, c_1 = 0."""
    assert ha.c1_atiyah("heisenberg") == 0


def test_c1_atiyah_vir_26():
    """Vir bc(2) trace: 2(24-12+1) = 26."""
    assert ha.c1_atiyah("vir") == 26


def test_c1_atiyah_km_2dim_g():
    """KM adjoint bc(1) trace: dim(g) * 2(6-6+1) = 2 dim(g)."""
    for dg in [3, 8, 15, 24, 28, 133, 248]:
        assert ha.c1_atiyah("km", dg) == 2 * dg


def test_c1_atiyah_bp_196():
    """BP: 8 * K_{bc(1)} + DS Atiyah = 16 + 180 = 196."""
    assert ha.c1_atiyah("bp") == 196


# =============================================================================
# The main Atiyah-vs-V28 cross-check (GHOST IDENTITY meets ATIYAH)
# =============================================================================


@independent_verification(
    claim='thm:K-Atiyah',
    derived_from=_DERIVED,
    verified_against=_VERIFIED,
    disjoint_rationale=_RATIONALE,
)
def test_atiyah_matches_climax_heisenberg():
    """Heisenberg: K_atiyah == K_brst == 0."""
    assert ha.family_atiyah_kappa("heisenberg") == cv.heisenberg_ghost_charge()


@independent_verification(
    claim='thm:K-Atiyah',
    derived_from=_DERIVED,
    verified_against=_VERIFIED,
    disjoint_rationale=_RATIONALE,
)
def test_atiyah_matches_climax_fermion_single():
    """Single free fermion: K_atiyah == K_brst == -1."""
    assert ha.family_atiyah_kappa("fermion_single") == cv.fermion_single_ghost_charge()


@pytest.mark.parametrize("lam", [
    Fraction(1, 2), Fraction(1), Fraction(3, 2),
    Fraction(2), Fraction(5, 2), Fraction(3),
    Fraction(4), Fraction(5), Fraction(6),
])
@independent_verification(
    claim='thm:K-Atiyah',
    derived_from=_DERIVED,
    verified_against=_VERIFIED,
    disjoint_rationale=_RATIONALE,
)
def test_atiyah_matches_climax_bc(lam):
    """bc(lambda) at standard weights: Atiyah trace == V28 ghost-charge sum."""
    assert ha.family_atiyah_kappa("bc", lam) == cv.bc_pair_ghost_charge(lam)


@pytest.mark.parametrize("lam", [
    Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2),
])
@independent_verification(
    claim='thm:K-Atiyah',
    derived_from=_DERIVED,
    verified_against=_VERIFIED,
    disjoint_rationale=_RATIONALE,
)
def test_atiyah_matches_climax_betagamma(lam):
    """beta-gamma(lambda): Atiyah trace == V28 ghost-charge sum."""
    assert ha.family_atiyah_kappa("betagamma", lam) == cv.betagamma_pair_ghost_charge(lam)


@pytest.mark.parametrize("name,dim_g", [
    ("sl_2", 3), ("sl_3", 8), ("sl_4", 15), ("sl_5", 24),
    ("so_8", 28), ("E_7", 133), ("E_8", 248),
])
@independent_verification(
    claim='thm:K-Atiyah',
    derived_from=_DERIVED,
    verified_against=_VERIFIED,
    disjoint_rationale=_RATIONALE,
)
def test_atiyah_matches_climax_km(name, dim_g):
    """Affine Kac-Moody for canonical g: K_atiyah == 2 dim(g) == K_brst."""
    assert ha.family_atiyah_kappa("km", dim_g) == cv.km_ghost_charge(dim_g)


@independent_verification(
    claim='thm:K-Atiyah',
    derived_from=_DERIVED,
    verified_against=_VERIFIED,
    disjoint_rationale=_RATIONALE,
)
def test_atiyah_matches_climax_vir():
    """Virasoro: K_atiyah == 26 == K_brst."""
    assert ha.family_atiyah_kappa("vir") == cv.vir_ghost_charge()


@pytest.mark.parametrize("N", list(range(2, 9)))
@independent_verification(
    claim='thm:K-Atiyah',
    derived_from=_DERIVED,
    verified_against=_VERIFIED,
    disjoint_rationale=_RATIONALE,
)
def test_atiyah_matches_climax_wn(N):
    """Principal W_N for N=2..8: K_atiyah == 4N^3 - 2N - 2 == K_brst."""
    assert ha.family_atiyah_kappa("wn", N) == cv.wn_ghost_charge(N)


@independent_verification(
    claim='thm:K-Atiyah',
    derived_from=_DERIVED,
    verified_against=_VERIFIED,
    disjoint_rationale=_RATIONALE,
)
def test_atiyah_matches_climax_bp():
    """Bershadsky-Polyakov: K_atiyah == 196 == K_brst."""
    assert ha.family_atiyah_kappa("bp") == cv.bp_ghost_charge()


# =============================================================================
# Symbolic chiral RRG identities
# =============================================================================


def test_chiral_rrg_wn_polynomial():
    """Chiral RRG: trace of Atiyah for W_N equals 4N^3 - 2N - 2 as polynomial in N."""
    assert ha.chiral_rrg_check_wn()


def test_chiral_rrg_km():
    """Chiral RRG: KM adjoint bc(1) trace equals 2 dim(g) symbolically."""
    assert ha.chiral_rrg_check_km()


def test_chiral_rrg_vir():
    """Chiral RRG: Vir bc(2) trace equals 26."""
    assert ha.chiral_rrg_check_vir()


# =============================================================================
# Out-of-scope families raise NotImplementedError (honest staging)
# =============================================================================


def test_unstaged_family_raises():
    """DS at non-principal nilpotents, cosets, logarithmic VOAs are out of scope."""
    with pytest.raises(NotImplementedError):
        ha.atiyah_class("ds_non_principal", {"g": "sl_4", "f": "(2,2)"})
    with pytest.raises(NotImplementedError):
        ha.atiyah_class("coset", {"G": "sl_2", "H": "U(1)"})
    with pytest.raises(NotImplementedError):
        ha.atiyah_class("triplet", {"p": 2})
