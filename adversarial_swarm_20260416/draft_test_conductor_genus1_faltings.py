r"""draft_test_conductor_genus1_faltings.py -- Tests for the third leg of K-trinity.

Verifies the V13 thm:K-trinity statement K_E = K_c = K_g where:

  K_E (V32 hochschild_atiyah_class.py):  Atiyah class first Chern class
  K_c (V28 climax_verification.py):      BRST ghost-charge sum (FMS)
  K_g (THIS engine):                     24 * kappa_{g=1} / rho via Faltings GRR

Each test decorated with @independent_verification(claim='thm:K-trinity', ...)
per HZ3-11 protocol.

DISJOINTNESS RATIONALE
----------------------
For each family the THREE definitions are GENUINELY independent:

  derived_from = ['Faltings 1992 chiral RRG genus-1 Quillen anomaly on M_{1,1}',
                  'BRST ghost-anomaly density rho = sum 1/lambda_alpha']
      = the genus-1 Quillen anomaly is a degree of a determinant line
        bundle on the moduli stack M_{1,1} of elliptic curves; rho
        measures the harmonic weighting of the BRST tower by inverse
        spins.  Both inputs are GEOMETRIC / HARMONIC, not c-anomaly.

  verified_against = ['V28 climax_verification BRST ghost-charge sum (FMS)',
                      'V32 hochschild_atiyah_class first Chern class']
      = V28 sums Friedan-Martinec-Shenker bc-charges over (lambda, eps)
        descriptors; V32 reads c_1 of the Hochschild-Atiyah class via
        Beilinson-Drinfeld 2.5 + Kapranov L-infinity model.  Neither
        invokes Faltings GRR or rho.

The agreement K_E = K_c = K_g is the V13 thm:K-trinity, NOT a
tautology.  Each side is the trace of a different mathematical object
(curvature trace, central-charge sum, Quillen anomaly), and the
identification is the trinity content.

LOCAL HARNESS NOTE
------------------
Imports go via sys.path manipulation to keep the draft tests self-
contained inside adversarial_swarm_20260416/.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

import pytest
import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

VOL_I_LIB = HERE.parent / "compute" / "lib"
if str(VOL_I_LIB.parent.parent) not in sys.path:
    sys.path.insert(0, str(VOL_I_LIB.parent.parent))

from compute.lib.independent_verification import independent_verification  # noqa: E402

import draft_conductor_genus1_faltings as cg  # noqa: E402


CLAIM = "thm:K-trinity"
DERIVED_FROM = [
    "Faltings 1992 chiral RRG genus-1 Quillen anomaly on M_{1,1}",
    "BRST ghost-anomaly density rho = sum 1/lambda_alpha",
]
VERIFIED_AGAINST = [
    "V28 climax_verification BRST ghost-charge sum (FMS)",
    "V32 hochschild_atiyah_class first Chern class",
]
RATIONALE = (
    "K_g is computed from the Faltings GRR identity 24*kappa_{g=1} = K*rho "
    "on M_{1,1}: kappa_{g=1} is a Quillen anomaly degree, rho a harmonic "
    "inverse-spin sum.  K_c (V28) is the FMS bc-charge sum over (lambda, eps) "
    "descriptors; K_E (V32) is the first Chern class of the chiral diagonal "
    "Atiyah curvature.  All three derivations use disjoint mathematical "
    "machinery (Quillen anomaly vs FMS central charge vs HH^2_ch curvature "
    "trace).  Their numerical agreement is the V13 K-trinity theorem."
)


def _trinity_check(family, params=None):
    """Helper: assert all three legs agree for one family."""
    row = cg.family_K_trinity(family, params)
    assert row.K_E == row.K_c, f"{family}: K_E={row.K_E} != K_c={row.K_c}"
    assert row.K_c == row.K_g, f"{family}: K_c={row.K_c} != K_g={row.K_g}"
    assert row.K_E == row.K_g, f"{family}: K_E={row.K_E} != K_g={row.K_g}"
    return row


# -----------------------------------------------------------------------------
# Section 1: Trinity agreement per family
# -----------------------------------------------------------------------------

@independent_verification(
    claim=CLAIM,
    derived_from=DERIVED_FROM,
    verified_against=VERIFIED_AGAINST,
    disjoint_rationale=RATIONALE,
)
def test_trinity_heisenberg():
    row = _trinity_check("heisenberg")
    assert row.K_g == Fraction(0)


@independent_verification(
    claim=CLAIM,
    derived_from=DERIVED_FROM,
    verified_against=VERIFIED_AGAINST,
    disjoint_rationale=RATIONALE,
)
def test_trinity_fermion_single():
    row = _trinity_check("fermion_single")
    assert row.K_g == Fraction(-1)


@pytest.mark.parametrize("lam", [Fraction(1, 2), Fraction(1), Fraction(3, 2),
                                  Fraction(2), Fraction(5, 2), Fraction(3),
                                  Fraction(4), Fraction(5), Fraction(6)])
@independent_verification(
    claim=CLAIM,
    derived_from=DERIVED_FROM,
    verified_against=VERIFIED_AGAINST,
    disjoint_rationale=RATIONALE,
)
def test_trinity_bc(lam):
    row = _trinity_check("bc", lam)
    expected = 2 * (6 * lam * lam - 6 * lam + 1)
    assert row.K_g == expected


@pytest.mark.parametrize("lam", [Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2)])
@independent_verification(
    claim=CLAIM,
    derived_from=DERIVED_FROM,
    verified_against=VERIFIED_AGAINST,
    disjoint_rationale=RATIONALE,
)
def test_trinity_betagamma(lam):
    row = _trinity_check("betagamma", lam)
    expected = -2 * (6 * lam * lam - 6 * lam + 1)
    assert row.K_g == expected


@pytest.mark.parametrize("name,dim_g", [("sl_2", 3), ("sl_3", 8), ("sl_4", 15),
                                          ("sl_5", 24), ("so_8", 28),
                                          ("E_7", 133), ("E_8", 248)])
@independent_verification(
    claim=CLAIM,
    derived_from=DERIVED_FROM,
    verified_against=VERIFIED_AGAINST,
    disjoint_rationale=RATIONALE,
)
def test_trinity_km(name, dim_g):
    row = _trinity_check("km", dim_g)
    assert row.K_g == Fraction(2 * dim_g)


@independent_verification(
    claim=CLAIM,
    derived_from=DERIVED_FROM,
    verified_against=VERIFIED_AGAINST,
    disjoint_rationale=RATIONALE,
)
def test_trinity_vir():
    row = _trinity_check("vir")
    assert row.K_g == Fraction(26)


@pytest.mark.parametrize("N", list(range(2, 9)))
@independent_verification(
    claim=CLAIM,
    derived_from=DERIVED_FROM,
    verified_against=VERIFIED_AGAINST,
    disjoint_rationale=RATIONALE,
)
def test_trinity_wn(N):
    row = _trinity_check("wn", N)
    assert row.K_g == Fraction(4 * N ** 3 - 2 * N - 2)


@independent_verification(
    claim=CLAIM,
    derived_from=DERIVED_FROM,
    verified_against=VERIFIED_AGAINST,
    disjoint_rationale=RATIONALE,
)
def test_trinity_bp():
    row = _trinity_check("bp")
    assert row.K_g == Fraction(196)


# -----------------------------------------------------------------------------
# Section 2: Faltings GRR identity 24*kappa_{g=1} = K*rho per family
# -----------------------------------------------------------------------------

def test_faltings_identity_vir():
    K = cg.K_brst_charge("vir")
    r = cg.rho("vir")
    kg1 = cg.kappa_genus1("vir")
    assert 24 * kg1 == K * r
    assert K == 26
    assert r == Fraction(1, 2)
    assert kg1 == Fraction(13, 24)


@pytest.mark.parametrize("dim_g", [3, 8, 15, 248])
def test_faltings_identity_km(dim_g):
    K = cg.K_brst_charge("km", dim_g)
    r = cg.rho("km", dim_g)
    kg1 = cg.kappa_genus1("km", dim_g)
    assert 24 * kg1 == K * r
    assert K == 2 * dim_g
    assert r == dim_g
    assert kg1 == Fraction(2 * dim_g * dim_g, 24)


@pytest.mark.parametrize("N", list(range(2, 9)))
def test_faltings_identity_wn(N):
    K = cg.K_brst_charge("wn", N)
    r = cg.rho("wn", N)
    kg1 = cg.kappa_genus1("wn", N)
    assert 24 * kg1 == K * r
    # Closed form: K = 4N^3 - 2N - 2; rho = H_N - 1.
    assert K == 4 * N ** 3 - 2 * N - 2
    expected_rho = sum((Fraction(1, j) for j in range(2, N + 1)), Fraction(0))
    assert r == expected_rho


def test_faltings_identity_bp():
    K = cg.K_brst_charge("bp")
    r = cg.rho("bp")
    kg1 = cg.kappa_genus1("bp")
    assert 24 * kg1 == K * r
    assert K == 196
    assert r == Fraction(9)


# -----------------------------------------------------------------------------
# Section 3: Symbolic Faltings RRG identities
# -----------------------------------------------------------------------------

def test_faltings_grr_wn_symbolic():
    assert cg.faltings_grr_wn_check()


def test_faltings_grr_vir_symbolic():
    assert cg.faltings_grr_vir_check()


def test_faltings_grr_km_symbolic():
    assert cg.faltings_grr_km_check()


# -----------------------------------------------------------------------------
# Section 4: Inversion K_g = 24 kappa_{g=1} / rho recovers K_brst on every family
# -----------------------------------------------------------------------------

@pytest.mark.parametrize("family,params", [
    ("fermion_single", None),
    ("bc", Fraction(1, 2)),
    ("bc", Fraction(2)),
    ("betagamma", Fraction(2)),
    ("km", 8),
    ("vir", None),
    ("wn", 4),
    ("bp", None),
])
def test_inversion_recovers_K_brst(family, params):
    K_brst = cg.K_brst_charge(family, params)
    K_g = cg.K_genus1(family, params)
    assert K_g == K_brst, f"{family}: K_g={K_g} != K_brst={K_brst}"


# -----------------------------------------------------------------------------
# Section 5: Heisenberg edge case (rho convention)
# -----------------------------------------------------------------------------

def test_heisenberg_faltings_vacuous():
    """Heisenberg has K=0; Faltings identity holds trivially with rho=1."""
    K = cg.K_brst_charge("heisenberg")
    r = cg.rho("heisenberg")
    kg1 = cg.kappa_genus1("heisenberg")
    assert K == 0
    assert kg1 == 0
    assert 24 * kg1 == K * r  # 0 = 0


# -----------------------------------------------------------------------------
# Section 6: report() executes without error
# -----------------------------------------------------------------------------

def test_report_executes():
    text = cg.report()
    assert "trinity?" in text
    assert "OK" in text
    assert "FAIL" not in text  # all rows must agree
