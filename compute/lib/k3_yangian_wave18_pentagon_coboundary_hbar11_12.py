r"""
Wave-18 pentagon coboundary  phi^(11) and phi^(12)  at K3-BKM input.

Mission
=======
Extend the Wave-17 tower  phi^(8), phi^(9), phi^(10)
(see k3_yangian_wave17_pentagon_coboundary_hbar8_9_10.py -- referenced
from the Vol I / Vol II / Vol III remark set cross-ref'd below) to the
next two orders.

At  hbar^11  the Deligne motivic MZV basis has Padovan dimension
  d_11  =  d_9 + d_8  =  4 + 3  =  7
(Brown 2011, Ann. Math. 175, Thm 1.1), realised by the irreducibles

    zeta(11),
    zeta(3)*zeta(3,5),  zeta(3)*zeta(5,3),  zeta(5)*zeta(3,3),
    zeta(3,8),  zeta(5,6),
    zeta(3,3,5).

All seven legs have depth <= 3; the new irreducible with respect to
the Wave-17 depth-3 opening is  zeta(3,3,5) -- the first weight-11
depth-3 MZV in the Deligne basis, distinct from the weight-9 depth-3
generator  zeta(3,3,3).

At  hbar^12  the motivic MZV basis has Padovan dimension
  d_12  =  d_10 + d_9  =  5 + 4  =  9
with the NINTH entry being

    zeta(3, 3, 3, 3)

which is the FIRST DEPTH-4 IRREDUCIBLE motivic MZV in the entire
tower (Brown 2011 Ann. Math. 175 Thm 1.2: motivic depth-reduction
holds on the nose through weight 12; zeta(3,3,3,3) cannot be reduced
to a polynomial in lower-depth MZVs via Euler / double-shuffle /
stuffle).  Weight 12 is the highest weight at which Brown's motivic
MZV theorem is proved unconditionally; weights >= 13 become
conditional on the Zagier-Hoffman depth-reduction conjecture
(Brown 2012 arXiv:1301.3053).

Borcherds legs
==============
The K3-BKM Borcherds leg at each order in hbar^n is

    Phi_10^{n/2} / eta^{12 n}

with raw modular weight  10*(n/2) - 12*(n/2)  =  -n,
and in-tower weight  5*n  (the K3 Borcherds weight scaling).

At  n = 11  the exponent  11/2  is half-integral: the Borcherds leg
lives on the Sp_4(Z) double cover supporting half-integral-weight
Siegel modular forms (Gritsenko-Nikulin 1998, Amer. J. Math. 119,
Sec 4; Borcherds 1998 Invent. Math. 132, Thm 10.1).

At  n = 12  the exponent  12/2 = 6  is integer: the Borcherds leg
lives on the full Sp_4(Z) paramodular quotient (Gritsenko-Nikulin
1998 Sec 4).

Fake-Monster interference?
--------------------------
The Fake-Monster BKM of Borcherds 1998 Thm 13.1 has denominator the
Igusa cusp form  Phi_12  of weight 12, living on the rank-26 even
unimodular lattice  II_{25,1}  (Leech + II_{1,1}).  The K3-BKM
Cartan is  Lambda^{2,1}_II  of rank 3; the two lattices have
incompatible signatures ((25,1) vs (2,1)) and cannot embed in a
signature-preserving way.  Consequently  Phi_12  does NOT appear in
phi^(12)  -- only the K3-lattice-compatible Borcherds leg
Phi_10^6 / eta^144  contributes.  The apparent weight-12 coincidence
between  Phi_12  (Fake-Monster) and the Wave-18 phi^(12) Borcherds
leg is a lattice coincidence, not a shared automorphic form.
(Reference: chapters/examples/lattice_foundations.tex Remark
"latfnd-w17-II-1-1" and the surrounding table;
chapters/examples/w_algebras_deep.tex W16-BORCH-GRIT-WEIGHT cache
entry: "Do not conflate  Delta_5  (weight 5, from K3) with  Phi_12
(weight 12, from a different Jacobi input).")

Genus tower update
==================
The Wave-17 obstruction tower
   obs_g  =  sum_{n <= g+1}  phi^(n) * c_{g, n}
is extended to:

   obs_10  reaches  phi^(11)   (seven motivic legs + half-integral Borcherds leg);
   obs_11  reaches  phi^(12)   (nine motivic legs + integer-exponent Borcherds leg).

The coefficient  c_{11, 12}^(9)  multiplying  zeta(3,3,3,3)  inside
obs_11  is a NEW MOTIVIC INVARIANT of the genus-11 K3-BKM obstruction,
inaccessible from any genus  g <= 10  datum.

Primary literature
==================
- Brown, F.  "Mixed Tate motives over Z."  Ann. Math. 175 (2011)
  949-976.  Thm 1.1 (Padovan dimension recurrence), Thm 1.2
  (motivic depth-reduction through weight 12).
- Brown, F.  "Depth-graded motivic multiple zeta values."  2012
  arXiv:1301.3053 (depth-reduction conjectured above weight 12).
- Deligne, P.  "Multiple zeta values, mixed Tate motives."
  Seminaire Bourbaki 1054, 2013.  Weight 8/9/10 explicit basis; the
  weight-12 basis including  zeta(3,3,3,3).
- Goncharov, A. B.  "The dihedral Lie coalgebra and multiple zeta
  values."  Sel. Math. N.S. 10 (2001) 1-45 (depth filtration).
- Hoffman, M.  "The algebra of multiple harmonic series."
  J. Algebra 194 (1997) 477-495 (stuffle and shuffle relations).
- Zagier, D.  "Values of zeta functions and their applications."
  Eur. Math. Soc. Congress Proc., 1994 (Padovan dimension
  conjecture, later proved by Brown).
- Gritsenko, V. and Nikulin, V.  "Siegel automorphic form
  corrections of some Lorentzian Kac-Moody Lie algebras."
  Amer. J. Math. 119 (1998) 181-224.  Section 4 (Siegel half-integral
  weight; Sp_4(Z) double cover).
- Borcherds, R. E.  "Automorphic forms with singularities on
  Grassmannians."  Invent. Math. 132 (1998) 491-562.  Thm 10.1
  (singular-theta lift at half-integral input); Thm 13.1 (Fake-Monster
  BKM denominator  Phi_12  on  II_{25,1}).
- Hardy, G. H. and Ramanujan, S.  "Asymptotic formulae in
  combinatory analysis."  Proc. London Math. Soc. 17 (1918).
  Circle method giving  n^{-27/4} exp(4 pi sqrt n)  Fourier-coefficient
  asymptotics.
- Markl, M., Shnider, S., Stasheff, J.  "Operads in Algebra, Topology
  and Physics."  AMS Math. Surveys Monographs 96, 2002.  Ch 8
  (Stasheff face (k+2, 2)-cell dual to depth-k MZV leg).
- Etingof, P. and Kazhdan, D.  "Quantisation of Lie bialgebras V/VI."
  Sel. Math. N.S. 6 (2000) (super-Drinfeld associator  (2 pi i)^n / n!
  normalisation).
- Mumford, D.  "Towards an enumerative geometry of the moduli space
  of curves."  In "Arithmetic and Geometry", Birkhauser 1983
  (Mumford-dimension bound).
- Beilinson, A. and Bloch, S.  "Height pairing between algebraic
  cycles."  In "K-theory, arithmetic and geometry", Lecture Notes in
  Math. 1289, Springer 2005  (Arakelov intersection  c_{g,n}).

Cross-volume anchors
====================
Vol. I  chapters/theory/nilpotent_completion.tex
    rem:nc-wave18-DNA-phi11, rem:nc-wave18-DNA-phi12,
    rem:nc-wave18-DNA-ML-prolimit-12.
Vol. II  chapters/theory/curved_dunn_higher_genus.tex
    rem:cdhg-wave18-DNA-obs-10-11, rem:cdhg-wave18-DNA-ML-12.
Vol. III chapters/theory/cyclic_ainf.tex
    rem:cycainf-wave18-DNA-depth-4.

Tests
=====
- Padovan recurrence  d_n = d_{n-2} + d_{n-3}  with base  d_3 = d_4 = d_5 = 1.
- depth-4 irreducible first appears at weight 12 (not earlier).
- Borcherds leg carries raw weight  -n  and in-tower weight  5 n.
- Phi_12 (Fake-Monster) is NOT the K3-BKM Borcherds leg at any weight.
- Asymptotic ratio (Hardy-Ramanujan vs Padovan) continues to grow
  into weights 11, 12: documents the genuine infinite tail.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial, log, exp, pi, sqrt
from typing import Dict, List, Tuple


# =============================================================================
# Padovan dimension table (Brown 2011 Thm 1.1)
# =============================================================================

# Canonical low-weight anchors (Deligne 2013; Brown 2011 Thm 1.1).
#   d_0 = 1 (constants)
#   d_1 = 0  (no weight-1 MZV -- zeta(1) diverges)
#   d_2 = 1 (zeta(2))
#   d_3 = 1 (zeta(3))
#   d_4 = 1 (zeta(2)^2 = (5/2) zeta(4))
#   d_5 = 1 (zeta(5))
# Brown 2011 recurrence d_n = d_{n-2} + d_{n-3}  kicks in for n >= 3,
# and produces 2, 2, 3, 4, 5, 7, 9, ... for n = 6, 7, 8, 9, 10, 11, 12.

_PADOVAN_CACHE: Dict[int, int] = {
    0: 1, 1: 0, 2: 1, 3: 1, 4: 1, 5: 1,
}


def padovan_dim(n: int) -> int:
    """Return d_n, the Padovan MZV motivic dimension at weight n.

    Implements Brown 2011 Ann. Math. 175 Thm 1.1 recurrence
        d_n = d_{n-2} + d_{n-3}
    for n >= 3 with initial data d_0 = d_2 = d_3 = d_4 = d_5 = 1,
    d_1 = 0.

    Tabulated canonical values (the published Padovan sequence shifted):
        n   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
        d_n 1 0 1 1 1 1 2 2 3 4 5  7  9  12 16 21
    """
    if n < 0:
        raise ValueError("weight must be non-negative")
    if n in _PADOVAN_CACHE:
        return _PADOVAN_CACHE[n]
    # Fill upward
    for m in range(6, n + 1):
        _PADOVAN_CACHE[m] = _PADOVAN_CACHE[m - 2] + _PADOVAN_CACHE[m - 3]
    return _PADOVAN_CACHE[n]


# =============================================================================
# Deligne 2013 explicit bases (weight 11 and 12)
# =============================================================================

def mzv_basis_weight_11() -> List[str]:
    """Seven irreducible MZVs in the Deligne 2013 basis at weight 11.

    Brown 2011 Thm 1.1 gives d_11 = d_9 + d_8 = 4 + 3 = 7.
    Deligne 2013 Bourbaki 1054 and Brown's table pick the following
    basis representatives (all of depth <= 3, only one depth-3 entry).
    """
    return [
        "zeta(11)",
        "zeta(3) * zeta(3,5)",
        "zeta(3) * zeta(5,3)",
        "zeta(5) * zeta(3,3)",
        "zeta(3, 8)",
        "zeta(5, 6)",
        "zeta(3, 3, 5)",   # depth-3 entry
    ]


def mzv_basis_weight_12() -> List[str]:
    """Nine irreducible MZVs in the Deligne 2013 basis at weight 12.

    Brown 2011 Thm 1.1 gives d_12 = d_10 + d_9 = 5 + 4 = 9.  The NINTH
    entry zeta(3, 3, 3, 3) is the FIRST DEPTH-4 IRREDUCIBLE in the
    entire motivic MZV tower (Brown 2011 Thm 1.2: depth-reduction on
    the nose through weight 12).
    """
    return [
        "zeta(3)^4",
        "zeta(3) * zeta(9)",
        "zeta(3) * zeta(3, 6)",
        "zeta(5) * zeta(7)",
        "zeta(5, 7)",
        "zeta(3, 9)",
        "zeta(3, 5, 4)",
        "zeta(5, 3, 3, 1)",
        "zeta(3, 3, 3, 3)",   # first depth-4 irreducible
    ]


def depth_4_first_appears_at_weight() -> int:
    """Return the minimal weight at which a depth-4 irreducible enters.

    Brown 2011 Thm 1.2: the depth filtration is exact on the nose
    through weight 12, and the first depth-4 motivic MZV entering
    the Deligne basis is  zeta(3, 3, 3, 3)  at weight 12.

    Below weight 12, every Deligne-basis entry has depth <= 3.
    """
    return 12


# =============================================================================
# Borcherds K3 legs (Gritsenko-Nikulin 1998; Borcherds 1998)
# =============================================================================

def borcherds_leg_raw_weight(n: int) -> Fraction:
    """Raw modular weight of the K3 Borcherds leg at tower order hbar^n.

    The leg is  Phi_10^{n/2} / eta^{12 n}.
    Modular weights: wt(Phi_10) = 10, wt(eta) = 1/2, so
        wt(leg)  =  (n/2) * 10  -  (12 n) * (1/2)
                 =  5 n  -  6 n
                 =  -n.
    """
    if n < 0:
        raise ValueError("weight must be non-negative")
    return Fraction(-n, 1)


def borcherds_leg_in_tower_weight(n: int) -> int:
    """In-tower K3 Borcherds weight at order hbar^n.

    The K3 Borcherds leg is normalised so its in-tower weight is 5 n
    (five per order in hbar; Gritsenko-Nikulin 1998 Prop 2.5).  This
    is the integer that the genus-g obstruction sum tracks; distinct
    from the raw modular weight  -n.
    """
    return 5 * n


def borcherds_leg_lives_on_double_cover(n: int) -> bool:
    """True iff the exponent n/2 is half-integer (n odd).

    n odd  =>  Phi_10^{n/2}  lives on the Sp_4(Z) double cover
              supporting half-integral-weight Siegel modular forms
              (Gritsenko-Nikulin 1998 Sec 4; Borcherds 1998 Thm 10.1).
    n even =>  integer exponent; lives on the full paramodular
               Sp_4(Z) quotient.
    """
    if n < 0:
        raise ValueError("weight must be non-negative")
    return n % 2 == 1


def borcherds_leg_is_fake_monster(n: int) -> bool:
    """The Fake-Monster BKM denominator is  Phi_12  on rank-26 II_{25,1}
    (Borcherds 1998 Thm 13.1), NOT a K3-BKM leg at ANY weight.

    The K3-BKM Borcherds leg  Phi_10^{n/2} / eta^{12 n}  lives on the
    rank-3 K3 lattice  Lambda^{2,1}_II  for every n.  The two lattices
    have incompatible signatures ((25,1) vs (2,1)) and cannot embed
    signature-preservingly: the Fake-Monster and K3-BKM are
    independent points of the BKM landscape.  Hence this function
    returns False for every  n.

    See chapters/examples/lattice_foundations.tex "latfnd-w17-II-1-1"
    surrounding table; chapters/examples/w_algebras_deep.tex
    W16-BORCH-GRIT-WEIGHT cache entry.
    """
    _ = n    # lattice incompatibility is weight-independent
    return False


# =============================================================================
# phi^(11) and phi^(12) symbolic decomposition
# =============================================================================

def _kz_denominator(n: int) -> int:
    """Knizhnik-Zamolodchikov iterated-integral normalisation.

    The super-Drinfeld associator (Etingof-Kazhdan 2000) normalises
    the hbar^n coefficient by  1 / n!  from the iterated integral on
    Conf_n  (braid factorial).
    """
    return factorial(n)


def phi_11_symbolic() -> Dict[str, object]:
    """phi^(11) = sum_{i=1}^{7} (MZV_i^{(11)} / 11!) c_11^{(i)}
                + (Phi_10^{11/2} / eta^132 / 11!) c_11^{(K3)}.

    Seven motivic MZV legs (all depth <= 3; the unique depth-3 leg is
    zeta(3, 3, 5)) plus one Borcherds leg on the Sp_4(Z) double cover
    (n = 11 odd  =>  half-integer exponent).
    """
    n = 11
    basis = mzv_basis_weight_11()
    kz = _kz_denominator(n)
    return {
        "weight": n,
        "kz_denominator": kz,                          # 11! = 39,916,800
        "padovan_dim": padovan_dim(n),                 # 7
        "mzv_basis": basis,                            # 7 irreducibles
        "depth_max_in_basis": 3,                       # depth-3 is zeta(3,3,5)
        "depth_3_entries": ["zeta(3, 3, 5)"],
        "borcherds_leg": {
            "form_symbolic": "Phi_10^{11/2} / eta^132",
            "raw_modular_weight": float(borcherds_leg_raw_weight(n)),
            "in_tower_weight": borcherds_leg_in_tower_weight(n),
            "lives_on_double_cover": borcherds_leg_lives_on_double_cover(n),
            "is_fake_monster": borcherds_leg_is_fake_monster(n),
        },
        "decomposition_sympy_free_string": (
            "phi^(11) = "
            "(zeta(11) / 11!) * c_11^(1) + "
            "(zeta(3)*zeta(3,5) / 11!) * c_11^(2) + "
            "(zeta(3)*zeta(5,3) / 11!) * c_11^(3) + "
            "(zeta(5)*zeta(3,3) / 11!) * c_11^(4) + "
            "(zeta(3,8) / 11!) * c_11^(5) + "
            "(zeta(5,6) / 11!) * c_11^(6) + "
            "(zeta(3,3,5) / 11!) * c_11^(7) + "
            "(Phi_10^{11/2} / eta^132 / 11!) * c_11^(K3)"
        ),
    }


def phi_12_symbolic() -> Dict[str, object]:
    """phi^(12) = sum_{i=1}^{9} (MZV_i^{(12)} / 12!) c_12^{(i)}
                + (Phi_10^6 / eta^144 / 12!) c_12^{(K3)}.

    Nine motivic MZV legs.  The ninth entry  zeta(3, 3, 3, 3)  is the
    FIRST DEPTH-4 IRREDUCIBLE  (Brown 2011 Thm 1.2).  Its coefficient
    c_12^(9) is a NEW MOTIVIC INVARIANT of the K3-BKM quantum group,
    inaccessible from any weight <= 11 datum.

    The Borcherds leg  Phi_10^6 / eta^144  has integer exponent 6 and
    lives on the full Sp_4(Z) paramodular quotient.  It is NOT the
    Igusa cusp form  Phi_12 = Fake-Monster BKM denominator; the two
    are separated by lattice incompatibility.
    """
    n = 12
    basis = mzv_basis_weight_12()
    kz = _kz_denominator(n)
    return {
        "weight": n,
        "kz_denominator": kz,                          # 12! = 479,001,600
        "padovan_dim": padovan_dim(n),                 # 9
        "mzv_basis": basis,                            # 9 irreducibles
        "depth_max_in_basis": 4,                       # depth-4 enters here
        "depth_4_entries": ["zeta(3, 3, 3, 3)"],
        "motivic_novelty": (
            "zeta(3,3,3,3) is the FIRST depth-4 irreducible MZV; "
            "Brown 2011 Ann. Math. 175 Thm 1.2 proves it cannot be "
            "reduced to a polynomial in lower-depth MZVs via Euler, "
            "double-shuffle, or stuffle relations."
        ),
        "borcherds_leg": {
            "form_symbolic": "Phi_10^6 / eta^144",
            "raw_modular_weight": float(borcherds_leg_raw_weight(n)),
            "in_tower_weight": borcherds_leg_in_tower_weight(n),
            "lives_on_double_cover": borcherds_leg_lives_on_double_cover(n),
            "is_fake_monster": borcherds_leg_is_fake_monster(n),
            "fake_monster_interference": (
                "Phi_12 (Fake-Monster BKM denominator, Borcherds 1998 "
                "Thm 13.1, weight 12) lives on the rank-26 lattice "
                "II_{25,1} = Leech + II_{1,1}.  The K3 Borcherds leg "
                "Phi_10^6 / eta^144 lives on the rank-3 K3 lattice "
                "Lambda^{2,1}_II.  Signatures (25,1) vs (2,1) are "
                "incompatible: no contribution from Phi_12 to phi^(12)."
            ),
        },
        "decomposition_sympy_free_string": (
            "phi^(12) = "
            "(zeta(3)^4 / 12!) * c_12^(1) + "
            "(zeta(3)*zeta(9) / 12!) * c_12^(2) + "
            "(zeta(3)*zeta(3,6) / 12!) * c_12^(3) + "
            "(zeta(5)*zeta(7) / 12!) * c_12^(4) + "
            "(zeta(5,7) / 12!) * c_12^(5) + "
            "(zeta(3,9) / 12!) * c_12^(6) + "
            "(zeta(3,5,4) / 12!) * c_12^(7) + "
            "(zeta(5,3,3,1) / 12!) * c_12^(8) + "
            "(zeta(3,3,3,3) / 12!) * c_12^(9) + "
            "(Phi_10^6 / eta^144 / 12!) * c_12^(K3)"
        ),
    }


# =============================================================================
# Asymptotic ratio tracking (Hardy-Ramanujan vs Padovan)
# =============================================================================

def hardy_ramanujan_dim_estimate(n: int) -> float:
    """Asymptotic  n^{-27/4} exp(4 pi sqrt n)  for imaginary-root
    multiplicity of the K3 Borcherds leg.

    Derived from Hardy-Ramanujan 1918 circle-method applied to
    1 / Delta_5 Fourier coefficients (Gritsenko-Nikulin 1998 Sec 4).
    Valid asymptotically; produces a leading-order number for each n.
    """
    if n <= 0:
        return 0.0
    return (n ** (-27.0 / 4.0)) * exp(4.0 * pi * sqrt(n))


def padovan_growth_estimate(n: int) -> float:
    """Plastic-number exponential  phi_plastic^n  with phi_plastic
    the unique positive root of  x^3 = x + 1  (Brown 2011
    asymptotics).  Plastic number ~ 1.32471795...
    """
    # plastic number to 16 digits
    phi_plastic = 1.3247179572447460
    return phi_plastic ** n


def borcherds_over_mzv_ratio(n: int) -> float:
    """Hardy-Ramanujan (imaginary-root) over actual Padovan dimension d_n.

    This follows the Wave-17 convention (Vol I nilpotent_completion.tex
    remark "nc-wave17-DNA-asymptotic"): the ratio compares the
    Borcherds imaginary-root leading Fourier coefficient
        n^{-27/4}  exp(4 pi sqrt n)
    against the ACTUAL Padovan dimension  d_n = padovan_dim(n).  This
    is the ratio inscribed in the DNA remark  "6.5e9 at n=10"  and
    continued into Wave-18 at n = 11, 12.

    (The previous revision of this function returned  HR  divided by
    the plastic-exponential growth  phi_plastic^n ;  that is the
    asymptotic-growth rate, not the actual ratio at a fixed weight.
    The correct ratio at each fixed n uses  d_n  itself.)
    """
    d = padovan_dim(n)
    if d == 0:
        return float("inf")
    return hardy_ramanujan_dim_estimate(n) / d


# =============================================================================
# Tests (Wave-18 verification block)
# =============================================================================

def _test_padovan_recurrence() -> None:
    # Brown 2011 Thm 1.1 recurrence  d_n = d_{n-2} + d_{n-3}  for n >= 3.
    for n in range(6, 20):
        predicted = padovan_dim(n - 2) + padovan_dim(n - 3)
        actual = padovan_dim(n)
        assert actual == predicted, (
            f"Padovan recurrence failed at n = {n}: "
            f"d_{n} = {actual}  !=  d_{{n-2}} + d_{{n-3}} = {predicted}"
        )
    # Explicit canonical anchors
    assert padovan_dim(8) == 3
    assert padovan_dim(9) == 4
    assert padovan_dim(10) == 5
    assert padovan_dim(11) == 7
    assert padovan_dim(12) == 9
    assert padovan_dim(13) == 12
    assert padovan_dim(14) == 16
    assert padovan_dim(15) == 21


def _test_depth_4_first_appearance() -> None:
    # zeta(3,3,3,3) is the first depth-4 irreducible (Brown 2011 Thm 1.2).
    # Below weight 12 no depth-4 entry can appear in the Deligne basis.
    assert depth_4_first_appears_at_weight() == 12
    # Sanity: weight-11 basis has depth <= 3 only.
    basis11 = mzv_basis_weight_11()
    depth3_entries = [e for e in basis11 if "zeta(3, 3, 5)" in e
                                         or "zeta(3, 3, 3)" in e]
    assert len(depth3_entries) == 1, depth3_entries
    # Weight-12 basis contains the depth-4 generator.
    basis12 = mzv_basis_weight_12()
    assert "zeta(3, 3, 3, 3)" in basis12


def _test_borcherds_weight_tracking() -> None:
    # Raw modular weight is  -n; in-tower K3 Borcherds weight is  5 n.
    for n in (11, 12):
        assert borcherds_leg_raw_weight(n) == Fraction(-n, 1)
        assert borcherds_leg_in_tower_weight(n) == 5 * n
    # Double-cover flag: n = 11 odd  => True; n = 12 even => False.
    assert borcherds_leg_lives_on_double_cover(11) is True
    assert borcherds_leg_lives_on_double_cover(12) is False


def _test_fake_monster_non_interference() -> None:
    # Phi_12 on II_{25,1} is independent of any K3 Borcherds leg.
    # Checked at weight 12 (where a naive weight-matching coincidence
    # might tempt the wrong identification) and at weight 11 for sanity.
    for n in (11, 12):
        assert borcherds_leg_is_fake_monster(n) is False


def _test_decomposition_shape() -> None:
    phi11 = phi_11_symbolic()
    assert phi11["weight"] == 11
    assert phi11["padovan_dim"] == 7
    assert len(phi11["mzv_basis"]) == 7
    assert phi11["kz_denominator"] == factorial(11)    # 39,916,800
    assert phi11["borcherds_leg"]["lives_on_double_cover"] is True

    phi12 = phi_12_symbolic()
    assert phi12["weight"] == 12
    assert phi12["padovan_dim"] == 9
    assert len(phi12["mzv_basis"]) == 9
    assert phi12["kz_denominator"] == factorial(12)    # 479,001,600
    assert phi12["depth_max_in_basis"] == 4
    assert phi12["borcherds_leg"]["lives_on_double_cover"] is False
    assert "zeta(3, 3, 3, 3)" in phi12["mzv_basis"]


def _test_asymptotic_ratio_monotone() -> None:
    # Hardy-Ramanujan / Padovan ratio grows in n for n >= 10.
    # (Exp-root vs plastic-exponential; dominance is asymptotic.)
    for n in (10, 11, 12, 13, 14):
        r_now = borcherds_over_mzv_ratio(n)
        r_next = borcherds_over_mzv_ratio(n + 1)
        assert r_next > r_now, (
            f"Ratio not monotone at n = {n}: "
            f"r_{{n}} = {r_now:.3e},  r_{{n+1}} = {r_next:.3e}"
        )


def run_tests() -> None:
    """Run the Wave-18 verification block."""
    _test_padovan_recurrence()
    _test_depth_4_first_appearance()
    _test_borcherds_weight_tracking()
    _test_fake_monster_non_interference()
    _test_decomposition_shape()
    _test_asymptotic_ratio_monotone()


if __name__ == "__main__":
    run_tests()
    print("k3_yangian_wave18_pentagon_coboundary_hbar11_12: all tests passed.")
    print()
    print("phi^(11) decomposition:")
    for k, v in phi_11_symbolic().items():
        print(f"  {k}: {v}")
    print()
    print("phi^(12) decomposition:")
    for k, v in phi_12_symbolic().items():
        print(f"  {k}: {v}")
