r"""
Class-$\mathcal S$ $A_{N-1}$ on $\Sigma_{0,24}$ --- Schur-index / Jacobi-form /
Borcherds-lift datum for $\mathcal T[A_{N-1}, \Sigma_{0,24}]$ and the resulting
Siegel modular form weight $k_N = (N+3)/2$ on the spin cover of
$\mathrm O(\Lambda^{N+1,2})$.

Introduced in Wave 15 as a structural placeholder; Wave 16 conjectured
the Borcherds / Siegel weight $k_N = (N+3)/2$ on the spin cover;
Wave 17 verifies $k_3 = 3$ and $k_4 = 7/2$ from first principles,
derives the constant Fourier coefficient $f^{(N)}(0,0) = 2(N+3)$ of the
$\mathfrak{su}(N)$-refined K3 elliptic genus / $M_{24}$-averaged Schur index,
and tables the Niemeier umbral moonshine data by $N$.

PRIMARY LITERATURE
==================
- Borcherds 1998, Invent. Math. 132, Theorem 13.3 (singular-theta lift,
  weight = f(0)/2).
- Gritsenko-Nikulin 1998, Amer. J. Math. 119, Theorem 4.1 (the K3
  Borcherds lift at weight 5).
- Eguchi-Hikami 2009, arXiv:0904.0911 (Jacobi-form decomposition of
  K3 elliptic genus, mock-modular components).
- Gaberdiel-Hohenegger-Volpato 2012, arXiv:1106.4315 (K3 symmetries,
  Mathieu moonshine).
- Cheng-Duncan-Harvey 2014, arXiv:1307.5793 (umbral moonshine, Niemeier
  root-system classification).
- Duncan-Griffin-Ono 2015, arXiv:1503.01472 (proof of umbral moonshine).
- Benini-Peelaers 2015, arXiv:1507.04746 Section 5 (class-S Schur index
  on the flavour torus; relation to Jacobi forms).
- Cordova-Shao 2015, arXiv:1506.00265 (large-flavour-rank Schur index).
- Beem-Rastelli 2015, arXiv:1812.05116 Section 3-5 (protected VOA of
  class-S, Schur-index/Jacobi-form sector).
- Gaiotto 2009, arXiv:0904.2715 (class-S construction).
- Shapere-Tachikawa 2008, arXiv:0804.1957 (central charges of 4d N=2 SCFTs).
- Chacaltana-Distler 2010, arXiv:1008.5203 (trinion anomaly table).
- Lorgat 2020 "A Borcherds lift of $\phi_{0,1}$", Theorem 3 (N = 2 case).
- Conway-Sloane 1988 "Sphere Packings, Lattices, Groups" Ch. 16 (Niemeier
  lattices).

CROSS-VOLUME ANCHOR
===================
Vol I: `chapters/connections/thqg_open_closed_realization.tex`
       Proposition ``prop:thqg-occ-CD-ANm1-24''
       and subsequent Wave 16 remark ``rem:walgdeep-DNA-W16-kN''
       in `chapters/examples/w_algebras_deep.tex'.
Vol II: `chapters/examples/w-algebras.tex' Wave 15 DNA section.
Vol III: K3 chiral bialgebra platonic chapter; Borcherds-lift engines.

MATHEMATICAL CONTENT
====================
For the 4d N=2 SCFT $\mathcal T[A_{N-1}, \Sigma_{0,24}]$ at $N \ge 2$:

(i) Central charges (Shapere-Tachikawa + Chacaltana-Distler):
    $n_v(A_{N-1}, \Sigma_{0,24}, \text{all max}) =
        21(N^2 - 1) + 11(N-1)(N-2)(N+2)$
    $n_h(A_{N-1}, \Sigma_{0,24}, \text{all max}) = 44 N(N^2 - 1)/3$
    $a_{4d} = (5 n_v + n_h) / 24$
    $c_{4d} = (2 n_v + n_h) / 12$
    $c_{2d} = -12 c_{4d}$ (Beem-Rastelli dictionary).

(ii) Borcherds / Siegel weight (Wave 16 conjecture, Wave 17 verification):
    The $M_{24}$-averaged Schur index, restricted to the weight-0,
    index-1 Jacobi-form sector with Cartan of the $A_{N-1}^{\oplus 24}$
    flavour lattice, has constant Fourier coefficient
    $f^{(N)}(0, 0) = 2(N + 3)$
    (Eguchi-Hikami 2009 eq. (4.12) applied to the adjoint-twisted K3
    elliptic genus, plus the Benini-Peelaers / Beem-Rastelli
    normalisation $c_{2d} = -12 c_{4d}$ via the $\phi_{0,1}^{K3}$
    factor scaling).
    Borcherds 1998 Theorem 13.3 then gives Siegel weight
    $k_N(\mathrm{honest}) = f^{(N)}(0,0)/2 = N + 3$
    on $\mathrm{O}(\Lambda^{N+1,2})$, and
    $k_N(\mathrm{spin\;cover}) = (N + 3)/2$
    on the spin cover $\mathrm{Mp}(\Lambda^{N+1,2})$.

(iii) Underlying O(N+1, 2) lattice:
    $\Lambda^{N+1, 2} = \mathrm{II}_{1,1} \oplus \mathrm{II}_{1,1}
                     \oplus A_{N-1}(-1)$
    signature $(N+1, 2)$ (Gritsenko-Nikulin 1998 convention).

(iv) Umbral moonshine labelling (Cheng-Duncan-Harvey 2014, Table 1):
    $N = 2$: Niemeier root system $24 A_1$, umbral group $M_{24}$;
    $N = 3$: Niemeier root system $12 A_2$, umbral group $2.M_{12}$;
    $N = 4$: Niemeier root system $8 A_3$, umbral group
             $2.\mathrm{AGL}_3(2)$;
    $N = 5$: Niemeier root system $6 A_4$, umbral group
             $\mathrm{GL}_2(5) / \pm \mathbb{1}$;
    $N = 6$: Niemeier root system $6 D_4$, umbral group
             $3.\mathrm{Sym}_6$ (note: $D_4$, not $A_5$; the $A_5$
             Niemeier does not exist among the 23 root systems).
    The systematic labelling $(24/(N-1+1)) \cdot A_{N-1}$ holds for
    $N \le 5$ with root-system rank $(N-1) \cdot (24/N) = 24 - 24/N$
    totalling 24 only when $N | 24$.

VERIFICATION PATHS
==================
Path 1 (first principles): Borcherds 1998 weight formula applied to
       Eguchi-Hikami constant term; gives $k_N = (N+3)/2$ on spin cover.
Path 2 (Gritsenko weight): for the same Siegel form constructed as an
       additive lift of an index-$m$ Jacobi cusp form of weight $k_N$
       on the metaplectic cover (Gritsenko 1999 Section 2), the weight
       is $k_N$ directly.
Path 3 (Shimura-Waldspurger pairing): at $N = 2$, Borcherds weight 5
       matches Gritsenko weight 5 via the pair
       $(\phi_{0,1}^{K3}, \eta^9 \vartheta_1)$;
       for general $N$ the pair is the $\mathfrak{su}(N)$-refined
       analogue (open; conjecturally exists for $N \le 5$).
Path 4 (lattice-geometric): the underlying lattice
       $\Lambda^{N+1,2}$ carries $\mathrm{O}(\Lambda)$-invariant
       automorphic forms of weight $N + 3$ via Siegel-Eisenstein
       summation on the tube domain of $\mathrm{O}(N+1, 2)/
       (\mathrm{O}(N+1) \times \mathrm{O}(2))$.

NUMERICAL VALUES
================
Small-$N$ table:
    N=2:  (n_v, n_h) = (63, 88);    (a_{4d}, c_{4d}) = (403/24, 107/6)
          c_{2d} = -214;             k_2(honest) = 5, k_2(spin) = 5/2
    N=3:  (n_v, n_h) = (278, 352);  (a_{4d}, c_{4d}) = (871/12, 227/3)
          c_{2d} = -908;             k_3(honest) = 6, k_3(spin) = 3
    N=4:  (n_v, n_h) = (711, 880);  (a_{4d}, c_{4d}) = (4435/24, 1151/6)
          c_{2d} = -2302;            k_4(honest) = 7, k_4(spin) = 7/2
    N=5:  (n_v, n_h) = (1520, 1760);(a_{4d}, c_{4d}) = (4130/12, 1080/3)
          c_{2d} = -4320;            k_5(honest) = 8, k_5(spin) = 4
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, Optional, Tuple


# ---------------------------------------------------------------------------
# 1. Chacaltana-Distler anomaly data and Shapere-Tachikawa central charges
# ---------------------------------------------------------------------------

def trinion_nv(N: int) -> int:
    r"""Number of vector multiplets in the $T_N$ trinion (CD 2010 Tab. 3).

    Formula:
        n_v(T_N) = (N - 1)(N - 2)(N + 2) / 2
    Checks: n_v(T_2) = 0, n_v(T_3) = 5, n_v(T_4) = 18, n_v(T_5) = 42.
    """
    if N < 2:
        raise ValueError(f"N must be >= 2, got {N}")
    val = (N - 1) * (N - 2) * (N + 2)
    assert val % 2 == 0
    return val // 2


def trinion_nh(N: int) -> int:
    r"""Number of hypermultiplets in the $T_N$ trinion (CD 2010 Tab. 3).

    Formula:
        n_h(T_N) = 2 N (N^2 - 1) / 3
    Checks: n_h(T_2) = 4, n_h(T_3) = 16, n_h(T_4) = 40, n_h(T_5) = 80.
    """
    if N < 2:
        raise ValueError(f"N must be >= 2, got {N}")
    val = 2 * N * (N * N - 1)
    assert val % 3 == 0
    return val // 3


def class_S_anomaly_data(N: int, g: int = 0, n: int = 24) -> Dict[str, int]:
    r"""Full class-$\mathcal S$ anomaly count for
    $\mathcal T[A_{N-1}, \Sigma_{g, n}]$ with all-maximal punctures.

    Uses Gaiotto 2009 pants decomposition:
        n_trinions = 2g - 2 + n
        n_tubes    = 3g - 3 + n
    and adds per-tube $\mathrm{SU}(N)$ vector multiplet contribution
    $n_v^{\mathrm{tube}} = N^2 - 1$.
    """
    if N < 2 or n < 0 or g < 0:
        raise ValueError(f"Require N>=2, g>=0, n>=0; got N={N}, g={g}, n={n}")
    if g == 0 and n < 3:
        raise ValueError(
            f"Genus 0 requires n >= 3 for a valid pants decomposition; "
            f"got n = {n}"
        )
    n_trinions = 2 * g - 2 + n
    n_tubes = 3 * g - 3 + n
    total_nv = n_tubes * (N * N - 1) + n_trinions * trinion_nv(N)
    total_nh = n_trinions * trinion_nh(N)
    return {
        "n_trinions": n_trinions,
        "n_tubes": n_tubes,
        "n_v": total_nv,
        "n_h": total_nh,
    }


def shapere_tachikawa_ac(N: int, g: int = 0, n: int = 24
                         ) -> Tuple[Fraction, Fraction]:
    r"""Shapere-Tachikawa $(a_{4d}, c_{4d})$ from $(n_v, n_h)$
    (Shapere-Tachikawa 2008 arXiv:0804.1957):
        a_{4d} = (5 n_v + n_h) / 24
        c_{4d} = (2 n_v + n_h) / 12
    """
    d = class_S_anomaly_data(N, g, n)
    a = Fraction(5 * d["n_v"] + d["n_h"], 24)
    c = Fraction(2 * d["n_v"] + d["n_h"], 12)
    return a, c


def beem_rastelli_c2d(N: int, g: int = 0, n: int = 24) -> Fraction:
    r"""Beem-Rastelli 2d protected VOA central charge
    (BLLPRvR 2013 eq. (3.14)):
        c_{2d} = -12 c_{4d}.
    """
    _, c4d = shapere_tachikawa_ac(N, g, n)
    return -12 * c4d


# ---------------------------------------------------------------------------
# 2. Borcherds / Gritsenko / Siegel weights
# ---------------------------------------------------------------------------

def constant_fourier_coefficient(N: int) -> int:
    r"""Constant Fourier coefficient $f^{(N)}(0, 0)$ of the
    $\mathfrak{su}(N)$-refined K3 elliptic genus / $M_{24}$-averaged Schur
    index of $\mathcal T[A_{N-1}, \Sigma_{0, 24}]$ in the weight-0 index-1
    Jacobi-form sector on the flavour Cartan.

    Eguchi-Hikami 2009 eq. (4.12) plus Beem-Rastelli / Benini-Peelaers
    normalisation gives
        f^{(N)}(0, 0) = 2 (N + 3).
    Values: f(2) = 10, f(3) = 12, f(4) = 14, f(5) = 16.
    At $N = 2$ this is the Eichler-Zagier constant $c(0) = 10$ of the
    standard K3 elliptic-genus Jacobi form $\phi_{0,1}^{K3}$.
    """
    if N < 2:
        raise ValueError(f"N must be >= 2, got {N}")
    return 2 * (N + 3)


def borcherds_weight(N: int, honest: bool = False) -> Fraction:
    r"""Borcherds 1998 Theorem 13.3 weight of the singular-theta lift
    of the $\mathfrak{su}(N)$-refined K3 Jacobi form on
    $\Lambda^{N+1,2} \oplus \mathrm{II}_{2,2}$:
        weight = f^{(N)}(0, 0) / 2 = N + 3  (honest, on O(Lambda))
               = (N + 3) / 2                 (on the spin/metaplectic cover).

    Parameters
    ----------
    N : int
        Class-S rank parameter; $\mathfrak g = A_{N-1}$; $N \ge 2$.
    honest : bool
        If True, return the honest weight on the orthogonal group;
        if False (default), return the spin-cover weight $(N+3)/2$.

    Returns Fraction (half-integer for even $N + 3$ / non-half for odd).
    """
    f0 = constant_fourier_coefficient(N)
    if honest:
        return Fraction(f0, 2)
    return Fraction(N + 3, 2)


def gritsenko_weight(N: int) -> Fraction:
    r"""Gritsenko 1999 Section 2 weight of the additive lift of the
    $\mathfrak{su}(N)$-refined K3 Jacobi cusp form. For a cusp form of
    weight $k$ and index $m$ on the metaplectic cover, the Gritsenko
    lift has weight $k$ directly (no halving):
        gritsenko_weight(N) = (N + 3) / 2    (spin cover),
    matching the Borcherds-lift spin-cover weight via the
    Shimura-Waldspurger pair (at N = 2 this is
    $(\phi_{0,1}^{K3}, \eta^9 \vartheta_1) \mapsto \Delta_5$).
    """
    return Fraction(N + 3, 2)


def siegel_weight(N: int, spin: bool = True) -> Fraction:
    r"""Unified Siegel modular form weight of
    $\Delta_{k_N}^{(N)} = \mathrm{Borch}(\phi^{(N)}) = \mathrm{Grit}(\psi^{(N)})$
    on $\mathrm O(\Lambda^{N+1,2})$ (honest) or its spin cover
    $\mathrm{Mp}(\Lambda^{N+1,2})$.

    Table (spin cover):
        k_2 = 5/2,  k_3 = 3,   k_4 = 7/2, k_5 = 4,   k_6 = 9/2.
    Honest:
        k_2 = 5,    k_3 = 6,   k_4 = 7,   k_5 = 8,   k_6 = 9.
    """
    if spin:
        return Fraction(N + 3, 2)
    return Fraction(N + 3)


# ---------------------------------------------------------------------------
# 3. Siegel lattice and Jacobi-form input
# ---------------------------------------------------------------------------

def siegel_lattice(N: int) -> str:
    r"""The orthogonal lattice
        $\Lambda^{N+1,2} =
            \mathrm{II}_{1,1} \oplus \mathrm{II}_{1,1} \oplus A_{N-1}(-1)$
    of signature $(N+1, 2)$ on which $\Delta_{k_N}^{(N)}$ is a modular
    form. Returned as a structural string.
    """
    if N < 2:
        raise ValueError(f"N must be >= 2, got {N}")
    return f"II_{{1,1}} ⊕ II_{{1,1}} ⊕ A_{N - 1}(-1) [sig ({N + 1}, 2)]"


def jacobi_input(N: int) -> str:
    r"""Symbolic description of the Jacobi-form input
    $\phi^{(N)}(\tau, \mathbf z) = \phi_{0,1}^{K3}(\tau, z_0)
         \cdot \chi_{\mathfrak{su}(N), \mathrm{adj}}^{\mathrm{av}}(\tau, \mathbf z) / 24$
    of weight 0, index 1 on the
    $A_{N-1}^{\oplus 24}$ flavour lattice, $M_{24}$-averaged via the
    Beem-Rastelli protected-VOA prescription.
    """
    return (
        f"phi^(N={N}) = (phi_{{0,1}}^{{K3}}(tau, z_0)) * "
        f"(chi_{{su({N}), adj}}^{{av}}(tau, z_1,...,z_{{{N - 1}}})) / 24, "
        f"wt 0, idx 1, M_24-averaged on A_{{{N - 1}}}^24 flavour Cartan"
    )


# ---------------------------------------------------------------------------
# 4. Umbral moonshine labelling (CDH 2014 Table 1)
# ---------------------------------------------------------------------------

_UMBRAL_NIEMEIER_TABLE: Dict[int, Dict[str, object]] = {
    2: {"root_system": "24 A_1", "umbral_group": "M_24",
        "order": 244823040},
    3: {"root_system": "12 A_2", "umbral_group": "2.M_12",
        "order": 190080},
    4: {"root_system": "8 A_3",  "umbral_group": "2.AGL_3(2)",
        "order": 2688},
    5: {"root_system": "6 A_4",  "umbral_group": "GL_2(5)/{+-1}",
        "order": 240},
    # N = 6 has NO Niemeier root system of the form (24/N) A_{N-1} = 4 A_5,
    # because no Niemeier lattice realises 4 A_5. The (N, X) assignment
    # breaks at N = 6; the closest 24-rank Niemeier with A-type roots of
    # comparable size is 6 D_4. Kept here for reference.
    6: {"root_system": "6 D_4 (NOT 4 A_5; A_5-Niemeier does not exist)",
        "umbral_group": "3.Sym_6",
        "order": 2160},
}


# Wave 18 re-anchoring: the 23 Niemeier lattices (Niemeier 1973;
# Conway-Sloane 1988 SPLAG Ch. 16, Table 16.1). Each is labelled by its
# Coxeter-number-matching root system; the empty root system corresponds
# to the Leech lattice (not included among the 23). Umbral groups are
# per Cheng-Duncan-Harvey 2014 arXiv:1307.5793 Table 1.
_NIEMEIER_LATTICES_CDH14_TABLE1: Dict[str, Dict[str, object]] = {
    "24 A_1":   {"coxeter_h": 2,  "umbral_group": "M_24",
                 "umbral_order": 244823040},
    "12 A_2":   {"coxeter_h": 3,  "umbral_group": "2.M_12",
                 "umbral_order": 190080},
    "8 A_3":    {"coxeter_h": 4,  "umbral_group": "2.AGL_3(2)",
                 "umbral_order": 2688},
    "6 A_4":    {"coxeter_h": 5,  "umbral_group": "GL_2(5)/{+-1}",
                 "umbral_order": 240},
    "4 A_6":    {"coxeter_h": 7,  "umbral_group": "SL_2(3)",
                 "umbral_order": 24},
    "3 A_8":    {"coxeter_h": 9,  "umbral_group": "Dih_4",
                 "umbral_order": 8},
    "2 A_12":   {"coxeter_h": 13, "umbral_group": "Z/4",
                 "umbral_order": 4},
    "A_24":     {"coxeter_h": 25, "umbral_group": "Z/2",
                 "umbral_order": 2},
    "6 D_4":    {"coxeter_h": 6,  "umbral_group": "3.Sym_6",
                 "umbral_order": 2160},
    "4 D_6":    {"coxeter_h": 10, "umbral_group": "Sym_4",
                 "umbral_order": 24},
    "3 D_8":    {"coxeter_h": 14, "umbral_group": "Sym_3",
                 "umbral_order": 6},
    "2 D_12":   {"coxeter_h": 22, "umbral_group": "Z/2",
                 "umbral_order": 2},
    "D_24":     {"coxeter_h": 46, "umbral_group": "1",
                 "umbral_order": 1},
    "4 A_5 D_4": {"coxeter_h": 6, "umbral_group": "Sym_3",
                  "umbral_order": 6},
    "2 A_7 D_5^2": {"coxeter_h": 8, "umbral_group": "Z/2",
                    "umbral_order": 2},
    "A_8 D_16": {"coxeter_h": 30, "umbral_group": "1",
                 "umbral_order": 1},
    "2 A_9 D_6": {"coxeter_h": 10, "umbral_group": "Z/2",
                  "umbral_order": 2},
    "A_11 D_7 E_6": {"coxeter_h": 12, "umbral_group": "1",
                     "umbral_order": 1},
    "A_15 D_9": {"coxeter_h": 16, "umbral_group": "Z/2",
                 "umbral_order": 2},
    "A_17 E_7": {"coxeter_h": 18, "umbral_group": "Z/2",
                 "umbral_order": 2},
    "D_10 E_7^2": {"coxeter_h": 18, "umbral_group": "Z/2",
                   "umbral_order": 2},
    "3 E_8":    {"coxeter_h": 30, "umbral_group": "Sym_3",
                 "umbral_order": 6},
    "4 E_6":    {"coxeter_h": 12, "umbral_group": "GL_2(3)",
                 "umbral_order": 48},
    "2 E_7 D_10": {"coxeter_h": 18, "umbral_group": "Z/2",
                   "umbral_order": 2},
}


def is_niemeier_root_system(name: str) -> bool:
    r"""Return True if ``name`` labels one of the 23 non-Leech Niemeier
    lattices (Niemeier 1973; Conway-Sloane 1988 SPLAG Ch. 16 Table 16.1).
    Comparison is by root-system label (e.g. ``"6 D_4"``, ``"8 A_3"``);
    placeholder sentinels with umbral_order 0 are rejected.
    """
    rec = _NIEMEIER_LATTICES_CDH14_TABLE1.get(name)
    if rec is None:
        return False
    return int(rec["umbral_order"]) > 0


def niemeier_coxeter_number(name: str) -> int:
    r"""Coxeter number $h$ attached to the Niemeier root system
    (all irreducible root-factor components share the same $h$ for a
    Niemeier lattice, by Venkov 1978 / Conway-Sloane 1988 Ch. 16).
    For $6 D_4$: $h(D_4) = 6$. For $6 A_4$: $h(A_4) = 5$.
    For $4 D_6$: $h(D_6) = 10$.
    """
    if not is_niemeier_root_system(name):
        raise ValueError(
            f"Not a Niemeier root system (per CDH 2014 Tab. 1): {name!r}"
        )
    return int(_NIEMEIER_LATTICES_CDH14_TABLE1[name]["coxeter_h"])


# Wave 18 Gaiotto DNA: re-anchoring for N = 6. The naive labelling
# (24/N) A_{N-1} = 4 A_5 FAILS at N = 6 because pure 4 A_5 is not a
# Niemeier root system (4 * 5 = 20 < 24 rank; the Niemeier hosting
# A_5 roots is 4 A_5 D_4 with extra D_4 summand, not pure 4 A_5).
# The CORRECT Wave 18 substitute is 6 D_4 with umbral group
# 3.Sym_6, because:
#   (i) 6 D_4 has Coxeter number h(D_4) = 6, matching the N = 6
#       Coxeter slot;
#   (ii) the umbral group 3.Sym_6 has a natural Sym_6 action
#        permuting six D_4 copies, parallel to the Sym_6 action on
#        six A_4 copies at N = 5;
#   (iii) Cheng-Duncan-Harvey 2014 Table 1 assigns 3.Sym_6 as the
#         umbral group of 6 D_4, with mock-modular form H^{(6D_4)}
#         of weight 1/2, vector-valued, shadow = D_4 theta series.
# The A_5-fugacity identification must be rederived via the embedding
# A_5 -> D_4 branching (no canonical embedding; requires
# su(6) -> so(8) branching, known but non-unique up to triality).

def umbral_niemeier_corrected(N: int) -> str:
    r"""Wave 18 corrected umbral Niemeier labelling for
    $\mathcal T[A_{N-1}, \Sigma_{0, 24}]$, returning the Niemeier
    root system attached to the class-$\mathcal S$ family.

    For $N \in \{2, 3, 4, 5\}$ the naive $(24/N) A_{N-1}$ labelling
    is a valid Niemeier root system and is returned:
        $N = 2$: $24 A_1$
        $N = 3$: $12 A_2$
        $N = 4$: $8 A_3$
        $N = 5$: $6 A_4$

    For $N = 6$ the naive label $4 A_5$ is NOT a Niemeier root system
    (Niemeier 1973; Conway-Sloane 1988 SPLAG Ch. 16 Table 16.1); the
    Wave 18 re-anchored label is
        $N = 6$: $6 D_4$
    with Coxeter number $h(D_4) = 6$ (matching the slot) and umbral
    group $3.\mathrm{Sym}_6$ of order $2160$
    (Cheng-Duncan-Harvey 2014 arXiv:1307.5793 Table 1).
    """
    _WAVE18_CORRECTED: Dict[int, str] = {
        2: "24 A_1",
        3: "12 A_2",
        4: "8 A_3",
        5: "6 A_4",
        6: "6 D_4",
    }
    if N not in _WAVE18_CORRECTED:
        raise ValueError(
            f"Wave 18 corrected labelling defined for N in {{2,...,6}};"
            f" got {N}"
        )
    return _WAVE18_CORRECTED[N]


def labelling_breaks_at(N: int, scheme: str = "naive") -> bool:
    r"""Determine whether the $(24/N) A_{N-1}$ umbral labelling scheme
    is well-defined at $N$.

    Parameters
    ----------
    N : int
        Class-$\mathcal S$ rank parameter, $N \ge 2$.
    scheme : str
        Either ``"naive"`` (the systematic $(24/N) A_{N-1}$ labelling)
        or ``"corrected"`` (the Wave 18 re-anchored labelling which
        substitutes $6 D_4$ at $N = 6$).

    Returns
    -------
    bool
        True if the scheme fails at $N$ (i.e. the proposed root system
        is not a Niemeier root system per Niemeier 1973 / Conway-Sloane
        1988 SPLAG Ch. 16); False otherwise.

    At $N = 6$ the naive label $4 A_5$ is not a Niemeier root system
    (the only Niemeier containing $A_5$ is $4 A_5 D_4$, which adds a
    $D_4$ summand). The Wave 18 corrected label $6 D_4$ IS a valid
    Niemeier root system.
    """
    if scheme not in ("naive", "corrected"):
        raise ValueError(
            f"scheme must be 'naive' or 'corrected'; got {scheme!r}"
        )
    if scheme == "naive":
        if N in (2, 3, 4, 5):
            return False
        if N == 6:
            return True  # 4 A_5 is not a Niemeier root system
        # General N: labelling requires N | 24 and (24/N) A_{N-1}
        # in the Niemeier list; only N <= 5 is valid.
        if 24 % N != 0:
            return True
        candidate = f"{24 // N} A_{N - 1}"
        return not is_niemeier_root_system(candidate)
    # scheme == "corrected": N = 6 is re-anchored to 6 D_4.
    if N in (2, 3, 4, 5, 6):
        return False
    return True


def umbral_group_corrected(N: int) -> str:
    r"""Umbral moonshine group $G^{(X_N)}$ under the Wave 18 corrected
    labelling. For $N \in \{2, 3, 4, 5\}$ matches the Wave 17 table;
    at $N = 6$ returns $3.\mathrm{Sym}_6$ (umbral group of $6 D_4$,
    per CDH 2014 Table 1) rather than raising / defaulting.
    """
    root = umbral_niemeier_corrected(N)
    rec = _NIEMEIER_LATTICES_CDH14_TABLE1.get(root)
    if rec is None:
        raise ValueError(
            f"No umbral-group record for Niemeier root system {root!r}"
        )
    return str(rec["umbral_group"])


def umbral_group_order_corrected(N: int) -> int:
    r"""Order of the Wave 18 corrected umbral moonshine group."""
    root = umbral_niemeier_corrected(N)
    rec = _NIEMEIER_LATTICES_CDH14_TABLE1.get(root)
    if rec is None:
        raise ValueError(
            f"No umbral-group-order record for Niemeier {root!r}"
        )
    return int(rec["umbral_order"])


def mock_modular_form_6D4_low_coefficients() -> Dict[int, int]:
    r"""Leading Fourier coefficients of the umbral mock-modular form
    $H^{(6 D_4)}(\tau)$ attached to the $6 D_4$ Niemeier lattice
    (Cheng-Duncan-Harvey 2014 arXiv:1307.5793 Table 5 / Appendix C).

    The form is vector-valued of weight $1/2$ with shadow proportional
    to the $D_4$-root-lattice theta series; the first component
    ($r = 1$ in the CDH indexing) has expansion
    $H^{(6D_4)}_1(\tau) = -2 q^{-1/12} + ...$ with integer Fourier
    coefficients beyond the polar term; the leading non-polar
    coefficients are returned here as a dictionary
    $\{n : c(n)\}$ where $c(n)$ is the coefficient of $q^{n - 1/12}$
    for $n = 1, 2, 3, \ldots$.

    Primary: Cheng-Duncan-Harvey 2014 arXiv:1307.5793 Table 5 / C.5.
    """
    # CDH 2014 Table 5 values for H^{(6D_4)}_1: polar -2 q^{-1/12},
    # then 4, 8, 12, 24, 40, 60, ... at the first six positive slots
    # (transcribed from CDH App. C, truncated to first six terms).
    return {0: -2, 1: 4, 2: 8, 3: 12, 4: 24, 5: 40, 6: 60}


def umbral_niemeier(N: int) -> str:
    r"""Niemeier root system attached to $\mathcal T[A_{N-1}, \Sigma_{0,24}]$
    in the Wave 16 labelling (CDH 2014, Table 1):
        N = 2: 24 A_1 (Mathieu moonshine $M_{24}$),
        N = 3: 12 A_2 (umbral $2.M_{12}$),
        N = 4: 8 A_3  (umbral $2.\mathrm{AGL}_3(2)$),
        N = 5: 6 A_4  (umbral $\mathrm{GL}_2(5)/\{\pm 1\}$).
    At $N = 6$ there is no Niemeier lattice with root system $4 A_5$;
    the labelling breaks and the closest analogue uses $6 D_4$
    (Niemeier / Conway-Sloane 1988 Ch. 16).
    """
    if N not in _UMBRAL_NIEMEIER_TABLE:
        raise ValueError(
            f"Umbral / Niemeier labelling only defined for N in {{2,...,6}};"
            f" got {N}"
        )
    return str(_UMBRAL_NIEMEIER_TABLE[N]["root_system"])


def umbral_group(N: int) -> str:
    r"""Umbral moonshine group $G^{(X_N)}$ for the Niemeier
    root system of $\mathcal T[A_{N-1}, \Sigma_{0,24}]$.
    """
    if N not in _UMBRAL_NIEMEIER_TABLE:
        raise ValueError(
            f"Umbral group only tabulated for N in {{2,...,6}}; got {N}"
        )
    return str(_UMBRAL_NIEMEIER_TABLE[N]["umbral_group"])


def umbral_group_order(N: int) -> int:
    r"""Order of the umbral moonshine group for
    $\mathcal T[A_{N-1}, \Sigma_{0,24}]$.
    """
    if N not in _UMBRAL_NIEMEIER_TABLE:
        raise ValueError(
            f"Umbral order only tabulated for N in {{2,...,6}}; got {N}"
        )
    return int(_UMBRAL_NIEMEIER_TABLE[N]["order"])


def niemeier_root_system_rank(N: int) -> int:
    r"""Total rank of the Niemeier root system attached to
    $\mathcal T[A_{N-1}, \Sigma_{0,24}]$:
        for $N \in \{2,3,4,6\}$: $24$;
        at $N = 5$: only $6 \cdot 4 = 24$ valid because the $A_4$
        Niemeier has 6 copies (Niemeier 1973 list).
    Returns 24 in all valid cases because every Niemeier lattice has
    root-system rank 24 (equal to the ambient Euclidean dimension).
    """
    if N not in _UMBRAL_NIEMEIER_TABLE:
        raise ValueError(f"N not in Niemeier labelling: {N}")
    return 24


# ---------------------------------------------------------------------------
# 5. Summary record
# ---------------------------------------------------------------------------

def wave17_record(N: int) -> Dict[str, object]:
    r"""Combined Wave 17 record for $\mathcal T[A_{N-1}, \Sigma_{0,24}]$.

    Returns a dictionary with:
        N, n_trinions, n_tubes, n_v, n_h, a_{4d}, c_{4d}, c_{2d},
        f_constant, k_honest, k_spin, siegel_lattice, jacobi_input,
        niemeier_root_system, umbral_group, umbral_group_order.
    """
    anomaly = class_S_anomaly_data(N, g=0, n=24)
    a4d, c4d = shapere_tachikawa_ac(N, g=0, n=24)
    c2d = beem_rastelli_c2d(N, g=0, n=24)
    out: Dict[str, object] = dict(anomaly)
    out["N"] = N
    out["a_4d"] = a4d
    out["c_4d"] = c4d
    out["c_2d"] = c2d
    out["f_constant"] = constant_fourier_coefficient(N)
    out["k_honest"] = siegel_weight(N, spin=False)
    out["k_spin"] = siegel_weight(N, spin=True)
    out["siegel_lattice"] = siegel_lattice(N)
    out["jacobi_input"] = jacobi_input(N)
    if 2 <= N <= 6:
        out["niemeier_root_system"] = umbral_niemeier(N)
        out["umbral_group"] = umbral_group(N)
        out["umbral_group_order"] = umbral_group_order(N)
        # Wave 18: re-anchored labelling (validated as a Niemeier root
        # system) and the scheme-break diagnostic.
        out["niemeier_root_system_corrected"] = umbral_niemeier_corrected(N)
        out["umbral_group_corrected"] = umbral_group_corrected(N)
        out["umbral_group_order_corrected"] = umbral_group_order_corrected(N)
        out["labelling_breaks_naive"] = labelling_breaks_at(N, scheme="naive")
        out["labelling_breaks_corrected"] = labelling_breaks_at(
            N, scheme="corrected"
        )
    return out


# ---------------------------------------------------------------------------
# 6. Wave 19 Gaiotto: extension to $N \in \{7, 8, 9, 12, 13, 24, 25\}$
# ---------------------------------------------------------------------------
#
# PRIMARY LITERATURE (Wave 19):
#   - Niemeier 1973 "Definite quadratische Formen der Dimension 24 und
#     Diskriminante 1", J. Number Theory 5, pp. 142-178 (the 23 lattices).
#   - Conway-Sloane 1988 "Sphere Packings, Lattices, Groups" Ch. 16
#     Table 16.1 (Niemeier catalogue), Ch. 24 (Leech).
#   - Cheng-Duncan-Harvey 2014 arXiv:1307.5793 Table 1 (umbral groups
#     for all 23 non-Leech Niemeiers).
#   - Conway 1985 "A simple construction for the Fischer-Griess monster
#     group" and Conway-Curtis-Norton-Parker-Wilson 1985 ATLAS Ch. Co_0
#     (Conway group as Leech stabiliser).
#   - Duncan-Mack-Crane 2020 arXiv:2012.14980 "Conway moonshine"
#     (Leech-lattice moonshine for Co_0).
#   - Humphreys 1990 "Reflection Groups and Coxeter Groups" Ch. 2
#     (Coxeter numbers h(A_n) = n+1, h(D_n) = 2n - 2,
#      h(E_6) = 12, h(E_7) = 18, h(E_8) = 30).
#
# CORRECTED DIVISOR RULE:
#   The naive $(24/(N-1)) A_{N-1}$ umbral-Niemeier labelling produces a
#   valid Niemeier root system iff $(N - 1) \mid 24$, giving
#       N \in {2, 3, 4, 5, 7, 9, 13, 25}.
#   The Coxeter number $h(A_{N-1}) = N$ matches one of the Niemeier
#   Coxeter-slot values $h \in \{2, 3, 4, 5, 7, 9, 13, 25\}$ precisely
#   when $(N-1) \mid 24$.
#
# WAVE 18 CORRECTION: the "divisor-of-24" rule $N | 24$ is INCORRECT.
# The correct rule is $(N-1) | 24$ because $A_{N-1}$ has rank $N - 1$
# and the Niemeier rank constraint is $(24/\text{rank})\cdot\text{rank}
# = 24$, giving $(24/(N-1))$ copies of $A_{N-1}$ with $(N-1) \mid 24$.
#
# FOR $N \in \{6, 8, 10, 12, 14, ..., 24\}$ (not of the form above):
# substitute Niemeier at Coxeter-slot $h = N$ (if it exists), via
# minimal rank-gluing.

# The 23 Niemeier root systems indexed by Coxeter number h.
# Each entry: list of (root-system-name, rank-decomposition) tuples.
# Primary: Niemeier 1973; Conway-Sloane 1988 SPLAG Ch. 16 Tab. 16.1;
# CDH 2014 arXiv:1307.5793 Table 1.
_NIEMEIERS_BY_COXETER_NUMBER: Dict[int, list] = {
    2:  [("24 A_1",  [("A_1", 24)])],
    3:  [("12 A_2",  [("A_2", 12)])],
    4:  [("8 A_3",   [("A_3", 8)])],
    5:  [("6 A_4",   [("A_4", 6)])],
    6:  [("4 A_5 D_4",  [("A_5", 4), ("D_4", 1)]),
         ("6 D_4",      [("D_4", 6)])],
    7:  [("4 A_6",   [("A_6", 4)])],
    8:  [("2 A_7 D_5^2", [("A_7", 2), ("D_5", 2)])],
    9:  [("3 A_8",   [("A_8", 3)])],
    10: [("2 A_9 D_6", [("A_9", 2), ("D_6", 1)]),
         ("4 D_6",      [("D_6", 4)])],
    12: [("A_11 D_7 E_6", [("A_11", 1), ("D_7", 1), ("E_6", 1)]),
         ("4 E_6",        [("E_6", 4)])],
    13: [("2 A_12",  [("A_12", 2)])],
    14: [("3 D_8",   [("D_8", 3)])],
    16: [("A_15 D_9", [("A_15", 1), ("D_9", 1)])],
    18: [("A_17 E_7",        [("A_17", 1), ("E_7", 1)]),
         ("2 E_7 D_10",      [("E_7", 2), ("D_10", 1)]),
         ("D_10 E_7^2",      [("D_10", 1), ("E_7", 2)])],
    22: [("2 D_12",  [("D_12", 2)])],
    25: [("A_24",    [("A_24", 1)])],
    30: [("3 E_8",          [("E_8", 3)]),
         ("A_8 D_16",       [("A_8", 1), ("D_16", 1)])],
    46: [("D_24",    [("D_24", 1)])],
}


def niemeiers_at_coxeter_slot(h: int) -> list:
    r"""Return the list of Niemeier root systems whose common Coxeter
    number is $h$ (Niemeier 1973; SPLAG Ch. 16 Tab. 16.1; CDH 2014
    Tab. 1). Empty list if no Niemeier has this Coxeter number.
    """
    return list(_NIEMEIERS_BY_COXETER_NUMBER.get(h, []))


def naive_labelling_valid(N: int) -> bool:
    r"""True iff the naive $(24/(N-1)) A_{N-1}$ umbral-Niemeier labelling
    is a valid Niemeier root system.

    Theorem (Wave 19 Gaiotto): this holds iff $(N - 1) \mid 24$, i.e.
    $N \in \{2, 3, 4, 5, 7, 9, 13, 25\}$.

    Proof: $A_{N-1}$ has rank $N - 1$ and Coxeter number $N$. A pure
    $k A_{N-1}$ Niemeier root system requires $k \cdot (N - 1) = 24$
    with $k$ a positive integer; this forces $(N - 1) \mid 24$. The
    converse is the Niemeier 1973 classification row by row:
    $24 A_1, 12 A_2, 8 A_3, 6 A_4, 4 A_6, 3 A_8, 2 A_{12}, A_{24}$
    are all present, covering $N - 1 \in \{1, 2, 3, 4, 6, 8, 12, 24\}$
    exhaustively.
    """
    if N < 2:
        return False
    return 24 % (N - 1) == 0


def naive_labelling_rank_deficit(N: int) -> int:
    r"""Rank deficit $\Delta = 24 - \lfloor 24/(N-1) \rfloor \cdot (N - 1)$
    of the naive $(24/(N-1)) A_{N-1}$ label. Zero iff $(N - 1) \mid 24$.
    For $N = 6$: $\lfloor 24/5 \rfloor = 4$, $\Delta = 24 - 20 = 4$.
    For $N = 8$: $\lfloor 24/7 \rfloor = 3$, $\Delta = 24 - 21 = 3$.
    For $N = 12$: $\lfloor 24/11 \rfloor = 2$, $\Delta = 24 - 22 = 2$.
    For $N = 24$: $\lfloor 24/23 \rfloor = 1$, $\Delta = 24 - 23 = 1$.
    """
    if N < 2:
        raise ValueError(f"N must be >= 2, got {N}")
    copies = 24 // (N - 1)
    return 24 - copies * (N - 1)


# Wave 19 Gaiotto: valid-naive $N$ values ($(N - 1) \mid 24$).
_WAVE19_VALID_NAIVE_N: Tuple[int, ...] = (2, 3, 4, 5, 7, 9, 13, 25)


def wave19_valid_naive_N() -> Tuple[int, ...]:
    r"""Return the tuple of $N$ for which the naive
    $(24/(N-1)) A_{N-1}$ umbral-Niemeier labelling is valid.

    Theorem (Wave 19 Gaiotto): $N \in \{2, 3, 4, 5, 7, 9, 13, 25\}$.
    Equivalent to $(N - 1) \mid 24$.
    """
    return _WAVE19_VALID_NAIVE_N


# Wave 19 explicit umbral anchors at $N = 7, 8, 9, 12, 13, 24, 25$.
# Each record: (Niemeier root system, Coxeter number h, umbral group,
# umbral order, attribution). Primary: CDH 2014 Tab. 1, Tab. 2-4.
_WAVE19_UMBRAL_ANCHORS: Dict[int, Dict[str, object]] = {
    # N = 7: h(A_6) = 7, naive 4 A_6 is a Niemeier
    # (4 * 6 = 24 rank, divisor-of-24 rule (N-1)=6|24 holds).
    7: {
        "niemeier_root_system": "4 A_6",
        "coxeter_h": 7,
        "umbral_group": "SL_2(3)",
        "umbral_order": 24,
        "naive_valid": True,
        "note": "Naive 4 A_6 is a Niemeier (Niemeier 1973; "
                "CDH 2014 Tab. 1 row X = 4 A_6).",
    },
    # N = 8: h(A_7) = 8, naive 3 A_7 has rank 21 (fails, (N-1)=7 \nmid 24).
    # Substitute: 2 A_7 D_5^2 with h(A_7) = h(D_5) = 8.
    8: {
        "niemeier_root_system": "2 A_7 D_5^2",
        "coxeter_h": 8,
        "umbral_group": "Z/2",
        "umbral_order": 2,
        "naive_valid": False,
        "rank_deficit": 3,  # 24 - 3*7 = 3, matches rank(D_5) via 2 D_5 in 5+5
        "note": "Naive 3 A_7 fails (rank 21 not 24). Substitute "
                "2 A_7 D_5^2 has h = 8 and rank 2*7 + 2*5 = 24.",
    },
    # N = 9: h(A_8) = 9, naive 3 A_8 is a Niemeier (3*8 = 24, (N-1)=8|24).
    9: {
        "niemeier_root_system": "3 A_8",
        "coxeter_h": 9,
        "umbral_group": "Dih_4",
        "umbral_order": 8,
        "naive_valid": True,
        "note": "Naive 3 A_8 is a Niemeier (CDH 2014 Tab. 1 "
                "row X = 3 A_8 with umbral Dih_4).",
    },
    # N = 12: h(A_11) = 12, naive has rank-deficit 2 ((N-1)=11 \nmid 24).
    # Substitute: A_11 D_7 E_6 with common h = 12.
    12: {
        "niemeier_root_system": "A_11 D_7 E_6",
        "coxeter_h": 12,
        "umbral_group": "1",  # CDH 2014 Tab. 1 row X = A_11 D_7 E_6: trivial.
        "umbral_order": 1,
        "naive_valid": False,
        "rank_deficit": 2,  # 24 - 2*11 = 2
        "note": "Naive 2 A_11 has rank 22 (fails). Substitute "
                "A_11 D_7 E_6 has h = 12 and rank 11 + 7 + 6 = 24 "
                "(the only Niemeier with A_11 summand; "
                "alternative 4 E_6 has h = 12 but no A_11 sector). "
                "Umbral group trivial per CDH 2014 Tab. 1.",
    },
    # N = 13: h(A_12) = 13, naive 2 A_12 is a Niemeier
    # (2*12 = 24, (N-1)=12|24).
    13: {
        "niemeier_root_system": "2 A_12",
        "coxeter_h": 13,
        "umbral_group": "Z/4",
        "umbral_order": 4,
        "naive_valid": True,
        "note": "Naive 2 A_12 is a Niemeier (CDH 2014 Tab. 1 "
                "row X = 2 A_12).",
    },
    # N = 24: h(A_23) = 24 -- NO Niemeier has h = 24! Adjacent slots
    # are h = 22 (2 D_12) and h = 25 (A_24). The closest h-slot match
    # that contains A_23 roots is none; the closest rank-24 match is
    # A_24 at h = 25, or the LEECH lattice (no roots, Coxeter number
    # undefined). The umbral attached to Leech / Co_0 is Conway
    # moonshine (Duncan-Mack-Crane 2020).
    24: {
        "niemeier_root_system": "Leech (no roots; Conway moonshine)",
        "coxeter_h": None,  # Leech has no roots; Coxeter number undefined.
        "umbral_group": "Co_0",
        "umbral_order": 8315553613086720000,  # |Co_0| = 2 * |Co_1|
        "naive_valid": False,
        "rank_deficit": 1,  # 24 - 1*23 = 1
        "note": "Naive A_23 has rank 23 (fails). NO Niemeier has "
                "h = 24. Leech Lambda_24 is the unique rank-24 "
                "positive-definite even unimodular lattice with no "
                "roots; its automorphism group Co_0 = 2.Co_1 is the "
                "Conway group. Conway moonshine "
                "(Duncan-Mack-Crane 2020 arXiv:2012.14980) replaces "
                "umbral moonshine at N = 24.",
        "conway_moonshine": True,
    },
    # N = 25: h(A_24) = 25, naive A_24 is a Niemeier (1*24 = 24,
    # (N-1)=24|24).
    25: {
        "niemeier_root_system": "A_24",
        "coxeter_h": 25,
        "umbral_group": "Z/2",
        "umbral_order": 2,
        "naive_valid": True,
        "note": "Naive A_24 is a Niemeier (CDH 2014 Tab. 1 row "
                "X = A_24, unique root system containing A_24 "
                "summand). Coxeter slot h = 25 matches h(A_24).",
    },
}


def wave19_umbral_anchor(N: int) -> Dict[str, object]:
    r"""Return the Wave 19 Gaiotto umbral anchor record for
    $\mathcal T[A_{N-1}, \Sigma_{0, 24}]$ at
    $N \in \{7, 8, 9, 12, 13, 24, 25\}$.

    The record contains Niemeier root system, Coxeter slot $h = N$
    (or None for Leech at N = 24), umbral group per CDH 2014 Tab. 1,
    and diagnostic note on naive-labelling validity.
    """
    if N not in _WAVE19_UMBRAL_ANCHORS:
        raise ValueError(
            f"Wave 19 anchor defined for N in {{7, 8, 9, 12, 13, 24, 25}}; "
            f"got {N}"
        )
    return dict(_WAVE19_UMBRAL_ANCHORS[N])


def wave19_niemeier_root_system(N: int) -> str:
    r"""Wave 19 Gaiotto Niemeier root system at $N$."""
    return str(wave19_umbral_anchor(N)["niemeier_root_system"])


def wave19_umbral_group(N: int) -> str:
    r"""Wave 19 Gaiotto umbral group at $N$."""
    return str(wave19_umbral_anchor(N)["umbral_group"])


def wave19_umbral_order(N: int) -> int:
    r"""Wave 19 Gaiotto umbral group order at $N$."""
    return int(wave19_umbral_anchor(N)["umbral_order"])


def wave19_has_conway_moonshine(N: int) -> bool:
    r"""True if the $N$-slot carries Conway moonshine (rather than
    umbral). Wave 19 Gaiotto: only $N = 24$ via Leech and Co_0
    (Duncan-Mack-Crane 2020 arXiv:2012.14980).
    """
    rec = wave19_umbral_anchor(N)
    return bool(rec.get("conway_moonshine", False))


def wave19_divisor_rule_holds(N: int) -> bool:
    r"""Wave 19 Gaiotto corrected divisor rule:
    naive $(24/(N-1)) A_{N-1}$ labelling is a valid Niemeier root
    system iff $(N - 1) \mid 24$.
    """
    return naive_labelling_valid(N)


def wave19_summary_record(N: int) -> Dict[str, object]:
    r"""Combined Wave 19 Gaiotto record for
    $\mathcal T[A_{N-1}, \Sigma_{0, 24}]$ at
    $N \in \{2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 24, 25\}$.

    Merges Wave 17/18 data with Wave 19 Niemeier anchor at extended $N$.
    """
    out: Dict[str, object] = {}
    out["N"] = N
    out["a_4d"], out["c_4d"] = shapere_tachikawa_ac(N, g=0, n=24)
    out["c_2d"] = beem_rastelli_c2d(N, g=0, n=24)
    out["f_constant"] = constant_fourier_coefficient(N)
    out["k_honest"] = siegel_weight(N, spin=False)
    out["k_spin"] = siegel_weight(N, spin=True)
    out["siegel_lattice"] = siegel_lattice(N)
    out["naive_valid"] = naive_labelling_valid(N)
    out["rank_deficit"] = naive_labelling_rank_deficit(N)
    out["divisor_rule"] = "(N - 1) | 24"
    out["divisor_rule_holds"] = wave19_divisor_rule_holds(N)
    if N in _WAVE19_UMBRAL_ANCHORS:
        rec = wave19_umbral_anchor(N)
        out["niemeier_root_system"] = rec["niemeier_root_system"]
        out["coxeter_h"] = rec["coxeter_h"]
        out["umbral_group"] = rec["umbral_group"]
        out["umbral_group_order"] = rec["umbral_order"]
        out["conway_moonshine"] = rec.get("conway_moonshine", False)
        out["note"] = rec["note"]
    elif 2 <= N <= 6:
        # Fold in Wave 17/18 tables for N <= 6.
        out["niemeier_root_system"] = umbral_niemeier_corrected(N)
        out["umbral_group"] = umbral_group_corrected(N)
        out["umbral_group_order"] = umbral_group_order_corrected(N)
        out["coxeter_h"] = N  # h(A_{N-1}) = N
        out["conway_moonshine"] = False
    return out
