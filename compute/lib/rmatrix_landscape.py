r"""r-matrix landscape: explicit collision residues for 8 standard families.

The r-matrix r(z) = Res^{coll}_{0,2}(\Theta_A) is the binary collision
residue of the universal MC element.  By AP19 (the bar kernel absorbs
a pole), the bar construction extracts residues along d\log(z_i - z_j),
which absorbs one power of (z-w) from each OPE pole:

    OPE pole z^{-n}  --->  r-matrix pole z^{-(n-1)}

In particular, z^{-1} in the OPE becomes z^0 = regular and DROPS.

Families computed
-----------------
1. Heisenberg at level k:       r(z) = k/z
2. Affine sl_2 at level k:      r(z) = k * Omega_{sl_2} / z
3. Affine sl_3 at level k:      r(z) = k * Omega_{sl_3} / z
4. Virasoro at central charge c: r(z) = (c/2)/z^3 + 2T/z
5. W_3 (TT channel):            same as Virasoro
6. W_3 (WW channel):            r(z) = (c/3)/z^5 + 2T/z^3 + dT/z^2 + ...
7. betagamma:                    r(z) = 0 (entirely regular)
8. Free fermion:                 r(z) = 0 (entirely regular for each pair)

Verification targets
--------------------
- AP19 pole orders:     pole_order(r) = pole_order(OPE) - 1
- CYBE:                 [r_{12}, r_{13}+r_{23}] + [r_{13}, r_{23}] = 0
- Skew-symmetry:        r_{12}(z) + r_{21}(-z) = 0
- Bosonic parity:       single bosonic generator => r-matrix has only odd poles
- kappa consistency:    scalar trace of r agrees with kappa(A)

Mathematical references
-----------------------
- AP19 in CLAUDE.md
- eq:virasoro-r-collision in spectral-braiding-core.tex
- prop:affine-r-mode in e1_modular_koszul.tex
- thm:mc2-bar-intrinsic in higher_genus_modular_koszul.tex
- collision_residue_identification.py (existing OPE/BinaryRMatrix engine)
- test_rmatrix_poles_comprehensive.py (existing pole-shift tests)

Conventions
-----------
- Cohomological grading (|d| = +1).
- Bar uses desuspension s^{-1}.
- Casimir tensor Omega = sum_a T^a tensor T_a with respect to the
  normalized Killing form (T^a, T_b) = delta^a_b.
- For sl_N: dim(sl_N) = N^2-1, h^vee = N, Killing form = trace form in
  the fundamental representation.
- kappa(KM) = dim(g)(k+h^vee)/(2h^vee).  kappa(Vir_c) = c/2.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

import numpy as np


# ========================================================================
# AP19 pole-shift engine
# ========================================================================

def ope_to_rmatrix_poles(ope_poles: Dict[int, Any]) -> Dict[int, Any]:
    """Apply the d log absorption rule: OPE pole z^{-n} -> r-matrix z^{-(n-1)}.

    Args:
        ope_poles: {pole_order: coefficient}. E.g. {4: c/2, 2: 2, 1: 1}
            for Virasoro T(z)T(w).

    Returns:
        {pole_order: coefficient} for the r-matrix.
        Order-0 terms (regular) are dropped.
    """
    result = {}
    for n, coeff in ope_poles.items():
        shifted = n - 1
        if shifted > 0 and coeff != 0:
            result[shifted] = coeff
    return result


def max_pole_order(poles: Dict[int, Any]) -> int:
    """Maximum pole order in the dictionary, or 0 if empty."""
    return max(poles.keys()) if poles else 0


# ========================================================================
# Family data: OPE poles and r-matrix for each family
# ========================================================================

class FamilyRMatrix:
    """Container for a chiral algebra family's OPE and r-matrix data.

    Stores:
      - name: human-readable name
      - channels: dict of channel_name -> {ope_poles, rmatrix_poles, description}
      - kappa: modular characteristic kappa(A)
      - generators: list of generator names with conformal weights
      - statistics: 'bosonic' or 'fermionic' per generator
    """

    def __init__(self, name: str):
        self.name = name
        self.channels: Dict[str, Dict] = {}
        self.kappa: Optional[Fraction] = None
        self.generators: List[Tuple[str, Fraction]] = []
        self.statistics: Dict[str, str] = {}

    def add_channel(self, channel_name: str, gen_i: str, gen_j: str,
                    ope_poles: Dict[int, Any], description: str = ""):
        """Add an OPE channel and compute its r-matrix poles."""
        rmatrix_poles = ope_to_rmatrix_poles(ope_poles)
        self.channels[channel_name] = {
            'gen_i': gen_i,
            'gen_j': gen_j,
            'ope_poles': ope_poles,
            'rmatrix_poles': rmatrix_poles,
            'ope_max_pole': max_pole_order(ope_poles),
            'rmatrix_max_pole': max_pole_order(rmatrix_poles),
            'description': description,
        }

    def verify_ap19(self) -> Dict[str, bool]:
        """Verify AP19 for all channels: r-matrix max pole = OPE max pole - 1.

        Returns {channel_name: passes} for each channel.
        """
        results = {}
        for name, ch in self.channels.items():
            ope_max = ch['ope_max_pole']
            r_max = ch['rmatrix_max_pole']
            # AP19: r-matrix max pole = OPE max pole - 1
            # Exception: if OPE max pole = 1 (simple pole only), r-matrix
            # is regular (max pole = 0), so the shift is also 1.
            if ope_max == 0:
                results[name] = (r_max == 0)
            else:
                results[name] = (r_max == ope_max - 1)
        return results

    def verify_bosonic_parity(self) -> Dict[str, bool]:
        """For same-statistics bosonic generators, r-matrix has only odd poles.

        Returns {channel_name: passes} for diagonal channels.
        """
        results = {}
        for name, ch in self.channels.items():
            gen_i, gen_j = ch['gen_i'], ch['gen_j']
            # Only check diagonal bosonic channels
            stat_i = self.statistics.get(gen_i, 'bosonic')
            stat_j = self.statistics.get(gen_j, 'bosonic')
            if stat_i == 'bosonic' and stat_j == 'bosonic' and gen_i == gen_j:
                all_odd = all(order % 2 == 1 for order in ch['rmatrix_poles'])
                results[name] = all_odd
        return results


# ========================================================================
# 1. Heisenberg at level k
# ========================================================================

def heisenberg_rmatrix(k: Fraction = Fraction(1)) -> FamilyRMatrix:
    r"""Heisenberg at level k.

    OPE:  J(z) J(w) ~ k / (z-w)^2
    r-matrix: r(z) = k/z  (single simple pole)

    The Heisenberg is abelian (no bracket), so the OPE has only
    the double pole from the bilinear form.  The d log absorption
    shifts this to a simple pole.

    kappa(H_k) = k.

    Properties:
    - CYBE trivially satisfied (abelian: all commutators vanish)
    - Skew-symmetry: k/z + k/(-z) = 0 (odd function)
    - Bosonic parity: z^{-1} is odd (h=1 generator)
    """
    fam = FamilyRMatrix("Heisenberg")
    fam.generators = [("J", Fraction(1))]
    fam.statistics = {"J": "bosonic"}
    fam.kappa = k

    fam.add_channel(
        "JJ", "J", "J",
        ope_poles={2: k},
        description=f"J(z)J(w) ~ {k}/(z-w)^2"
    )
    return fam


# ========================================================================
# 2. Affine sl_2 at level k
# ========================================================================

def affine_sl2_rmatrix(k: Fraction = Fraction(1)) -> FamilyRMatrix:
    r"""Affine sl_2 at level k.

    OPE:  J^a(z) J^b(w) ~ k delta^{ab} / (z-w)^2  +  f^{ab}_c J^c(w) / (z-w)

    For diagonal pairs (a=b):
        OPE poles: {2: k}
        r-matrix poles: {1: k}  (z^{-2} -> z^{-1})

    For off-diagonal pairs (a != b, f^{ab}_c != 0):
        OPE poles: {1: f^{ab}_c}
        r-matrix poles: {}  (z^{-1} -> z^0 = regular, DROPS)

    The full r-matrix is:
        r(z) = k * Omega_{sl_2} / z
    where Omega = sum_a T^a tensor T_a is the Casimir tensor.

    In the fundamental representation (V = C^2):
        r^{fund}(z) = k * P / z
    where P is the permutation operator (since Omega = P - I/2 up to
    normalization; more precisely Omega acts as P in the trace-form
    normalization).

    kappa(sl_2, k) = dim(sl_2)(k+h^vee)/(2h^vee) = 3(k+2)/4.

    Properties:
    - CYBE reduces to IBR: [Omega_{12}, Omega_{13}+Omega_{23}] = 0
    - Skew-symmetry: Omega is symmetric => r_{21}(-z) = -r_{12}(z)
    """
    if k + 2 == 0:
        raise ValueError("Critical level k = -h^vee = -2: Sugawara undefined")

    fam = FamilyRMatrix("Affine sl_2")
    fam.generators = [("J1", Fraction(1)), ("J2", Fraction(1)), ("J3", Fraction(1))]
    fam.statistics = {"J1": "bosonic", "J2": "bosonic", "J3": "bosonic"}
    fam.kappa = Fraction(3) * (k + 2) / Fraction(4)

    # Diagonal channels: double pole from Killing form
    for gen in ["J1", "J2", "J3"]:
        fam.add_channel(
            f"{gen}{gen}", gen, gen,
            ope_poles={2: k},
            description=f"{gen}(z){gen}(w) ~ k/(z-w)^2 + ..."
        )

    # Off-diagonal channels: simple pole from structure constants
    # [J1,J2] = J3, [J2,J3] = J1, [J3,J1] = J2 (using e,f,h ~ J1,J2,J3)
    for (gi, gj) in [("J1", "J2"), ("J2", "J3"), ("J3", "J1")]:
        fam.add_channel(
            f"{gi}{gj}", gi, gj,
            ope_poles={1: Fraction(1)},  # structure constant
            description=f"{gi}(z){gj}(w) ~ f^{{...}} J/(z-w)"
        )

    return fam


# ========================================================================
# 3. Affine sl_3 at level k
# ========================================================================

def affine_sl3_rmatrix(k: Fraction = Fraction(1)) -> FamilyRMatrix:
    r"""Affine sl_3 at level k.

    OPE: J^a(z) J^b(w) ~ k (T^a, T^b) / (z-w)^2 + f^{ab}_c J^c(w) / (z-w)

    Same pole structure as sl_2: diagonal double pole, off-diagonal simple pole.

    r-matrix: r(z) = k * Omega_{sl_3} / z
    where Omega = sum_{a=1}^8 T^a tensor T_a (8-dimensional Casimir).

    In the fundamental representation (V = C^3):
        Omega acts as the permutation operator P on V tensor V
        (up to normalization by the index of the fundamental: ell = 1/2).

    kappa(sl_3, k) = dim(sl_3)(k+h^vee)/(2h^vee) = 8(k+3)/6 = 4(k+3)/3.

    h^vee(sl_3) = 3.  dim(sl_3) = 8.
    """
    if k + 3 == 0:
        raise ValueError("Critical level k = -h^vee = -3: Sugawara undefined")

    fam = FamilyRMatrix("Affine sl_3")
    gen_names = ["H1", "H2", "E1", "E2", "E3", "F1", "F2", "F3"]
    fam.generators = [(g, Fraction(1)) for g in gen_names]
    fam.statistics = {g: "bosonic" for g in gen_names}
    fam.kappa = Fraction(4) * (k + 3) / Fraction(3)

    # Diagonal channels: double pole from Killing form
    # For Cartan generators H1, H2: (H_i, H_j) = A_{ij} (Cartan matrix entry)
    # For root generators: (E_i, F_i) = 1
    for gen in gen_names:
        fam.add_channel(
            f"{gen}{gen}", gen, gen,
            ope_poles={2: k},  # k * (T^a, T^a) with normalized basis
            description=f"Diagonal: {gen}(z){gen}(w) ~ k/(z-w)^2"
        )

    # Off-diagonal channels with nonzero structure constants: simple pole
    # The exact structure constants are in sl3_bar.py; here we record the
    # pole structure only.
    off_diag_pairs = [
        ("H1", "E1"), ("H1", "F1"), ("H2", "E2"), ("H2", "F2"),
        ("E1", "E2"), ("F1", "F2"), ("E1", "F1"), ("E2", "F2"), ("E3", "F3"),
    ]
    for (gi, gj) in off_diag_pairs:
        fam.add_channel(
            f"{gi}{gj}", gi, gj,
            ope_poles={1: Fraction(1)},  # structure constant (nonzero)
            description=f"{gi}(z){gj}(w) ~ f^{{...}} J/(z-w)"
        )

    return fam


# ========================================================================
# 4. Virasoro at central charge c
# ========================================================================

def virasoro_rmatrix(c: Fraction = Fraction(26)) -> FamilyRMatrix:
    r"""Virasoro algebra at central charge c.

    OPE:  T(z) T(w) ~ (c/2)/(z-w)^4  +  2T(w)/(z-w)^2  +  dT(w)/(z-w)

    OPE poles: {4: c/2, 2: 2, 1: 1}
    r-matrix poles: {3: c/2, 1: 2}

    The d log absorption shifts each pole by 1:
      z^{-4} -> z^{-3}:  leading pole, coefficient c/2
      z^{-2} -> z^{-1}:  subleading, coefficient 2 (from 2T)
      z^{-1} -> z^{0}:   REGULAR, drops (the dT term disappears)

    Result: r(z) = (c/2)/z^3 + 2T/z

    No z^{-2} pole: bosonic parity for a single generator of even weight h=2.
    The d log extraction sends even OPE poles z^{-2n} to odd r-matrix poles
    z^{-(2n-1)}, and the single odd OPE pole z^{-1} becomes regular.

    kappa(Vir_c) = c/2.

    Ground truth: eq:virasoro-r-collision in spectral-braiding-core.tex.

    Properties:
    - CYBE: satisfied (the Virasoro r-matrix is a solution of the
      generalized CYBE with the Virasoro algebra as the underlying
      Lie algebra; verified in Feigin-Fuchs / Belavin-Drinfeld).
    - Skew-symmetry: r(z) is an odd function of z (only odd poles).
    - Bosonic parity: poles at z^{-3} and z^{-1} only (both odd).
    """
    fam = FamilyRMatrix("Virasoro")
    fam.generators = [("T", Fraction(2))]
    fam.statistics = {"T": "bosonic"}
    fam.kappa = c / Fraction(2)

    fam.add_channel(
        "TT", "T", "T",
        ope_poles={4: c / 2, 2: Fraction(2), 1: Fraction(1)},
        description=f"T(z)T(w) ~ (c/2)/(z-w)^4 + 2T/(z-w)^2 + dT/(z-w)"
    )
    return fam


# ========================================================================
# 5. W_3 (TT channel) -- same as Virasoro
# ========================================================================

def w3_TT_rmatrix(c: Fraction = Fraction(4)) -> FamilyRMatrix:
    r"""W_3 algebra, TT channel.

    The T(z)T(w) OPE in the W_3 algebra is identical to the Virasoro OPE:
      T(z)T(w) ~ (c/2)/(z-w)^4 + 2T/(z-w)^2 + dT/(z-w)

    r-matrix (TT): r_{TT}(z) = (c/2)/z^3 + 2T/z

    kappa(W_3) = c * (H_3 - 1) = c * (1 + 1/2 + 1/3 - 1) = c * 5/6
    where H_3 = 1 + 1/2 + 1/3 = 11/6.
    WAIT: kappa(W_N) = c * (H_N - 1). For N=3: H_3 = 11/6, so H_3-1 = 5/6.
    But this is the MULTI-GENERATOR kappa. For the TT channel alone,
    the relevant quantity is the T two-point coefficient c/2.
    """
    fam = FamilyRMatrix("W_3 (TT channel)")
    fam.generators = [("T", Fraction(2)), ("W", Fraction(3))]
    fam.statistics = {"T": "bosonic", "W": "bosonic"}
    # kappa for W_3: c * (H_3 - 1) = c * 5/6
    fam.kappa = c * Fraction(5, 6)

    fam.add_channel(
        "TT", "T", "T",
        ope_poles={4: c / 2, 2: Fraction(2), 1: Fraction(1)},
        description="T(z)T(w) ~ (c/2)/(z-w)^4 + 2T/(z-w)^2 + dT/(z-w)"
    )
    return fam


# ========================================================================
# 6. W_3 (WW channel)
# ========================================================================

def w3_WW_rmatrix(c: Fraction = Fraction(4)) -> FamilyRMatrix:
    r"""W_3 algebra, WW channel.

    W(z)W(w) ~ (c/3)/(z-w)^6 + 2T/(z-w)^4 + dT/(z-w)^3
               + [(3/10)d^2T + beta*Lambda]/(z-w)^2 + [...]/(z-w)
    where beta = 16/(22 + 5c) and Lambda = (TT) - (3/10)d^2T is the
    quasi-primary composite at weight 4.

    OPE poles: {6: c/3, 4: 2, 3: 1, 2: composite, 1: composite}

    r-matrix poles (shifted by 1):
      z^{-6} -> z^{-5}: coefficient c/3
      z^{-4} -> z^{-3}: coefficient 2 (from 2T)
      z^{-3} -> z^{-2}: coefficient 1 (from dT)
      z^{-2} -> z^{-1}: composite (from d^2T + beta*Lambda)
      z^{-1} -> z^{0}: DROPS (regular)

    Result: r_{WW}(z) = (c/3)/z^5 + 2T/z^3 + dT/z^2 + composite/z

    Note: unlike the Virasoro (single bosonic generator), the WW r-matrix
    HAS even-order poles (z^{-2}).  This is because W has spin 3 (odd
    conformal weight), and the OPE W(z)W(w) has both even and odd poles.
    The bosonic parity constraint (only odd poles in r-matrix) applies
    to SAME-STATISTICS, SAME-GENERATOR pairings of EVEN-weight fields.
    For a weight-3 field, the OPE pole pattern is z^{-6}, z^{-4}, z^{-3},
    z^{-2}, z^{-1}, and after shift: z^{-5}, z^{-3}, z^{-2}, z^{-1}.

    kappa(W_3) = c * 5/6.
    """
    fam = FamilyRMatrix("W_3 (WW channel)")
    fam.generators = [("T", Fraction(2)), ("W", Fraction(3))]
    fam.statistics = {"T": "bosonic", "W": "bosonic"}
    fam.kappa = c * Fraction(5, 6)

    # For the numerical poles, use Fraction values for the known coefficients.
    # The z^{-2} and z^{-1} poles involve composite fields; mark symbolically.
    fam.add_channel(
        "WW", "W", "W",
        ope_poles={
            6: c / Fraction(3),
            4: Fraction(2),
            3: Fraction(1),
            2: Fraction(1),   # placeholder for composite coefficient
            1: Fraction(1),   # placeholder for composite coefficient
        },
        description=(
            "W(z)W(w) ~ (c/3)/(z-w)^6 + 2T/(z-w)^4 + dT/(z-w)^3 "
            "+ composite/(z-w)^2 + composite/(z-w)"
        ),
    )
    return fam


# ========================================================================
# 7. betagamma system
# ========================================================================

def betagamma_rmatrix(lam: Fraction = Fraction(1)) -> FamilyRMatrix:
    r"""betagamma system at weight lambda.

    OPE:
      beta(z) gamma(w) ~ 1/(z-w)         (simple pole, mixed propagator)
      gamma(z) beta(w) ~ 1/(z-w)         (simple pole)
      beta(z) beta(w) ~ 0                (regular)
      gamma(z) gamma(w) ~ 0              (regular)

    r-matrix:
      All channels are entirely regular (no poles in the r-matrix).
      The simple pole z^{-1} in the mixed propagator becomes z^0 = regular
      after d log absorption, and DROPS.

    r(z) = 0 for all channels.

    This is consistent with the betagamma system being shadow class C
    (contact, terminates at arity 4): the leading bar interaction is
    quartic, not binary.

    Central charge: c(betagamma, lambda) = 2(6lambda^2 - 6lambda + 1).
    Standard weight lambda=1: c = 2.
    kappa(betagamma) = c/2 = 6lambda^2 - 6lambda + 1.
    """
    c = Fraction(2) * (6 * lam * lam - 6 * lam + 1)

    fam = FamilyRMatrix("betagamma")
    fam.generators = [("beta", lam), ("gamma", Fraction(1) - lam)]
    fam.statistics = {"beta": "bosonic", "gamma": "bosonic"}
    fam.kappa = c / Fraction(2)

    # Mixed channels: simple pole only -> drops in r-matrix
    fam.add_channel(
        "beta_gamma", "beta", "gamma",
        ope_poles={1: Fraction(1)},
        description="beta(z)gamma(w) ~ 1/(z-w)"
    )
    fam.add_channel(
        "gamma_beta", "gamma", "beta",
        ope_poles={1: Fraction(1)},
        description="gamma(z)beta(w) ~ 1/(z-w)"
    )

    # Diagonal channels: no singular OPE
    fam.add_channel(
        "beta_beta", "beta", "beta",
        ope_poles={},
        description="beta(z)beta(w) ~ 0 (regular)"
    )
    fam.add_channel(
        "gamma_gamma", "gamma", "gamma",
        ope_poles={},
        description="gamma(z)gamma(w) ~ 0 (regular)"
    )

    return fam


# ========================================================================
# 8. Free fermion (two generators)
# ========================================================================

def free_fermion_rmatrix() -> FamilyRMatrix:
    r"""Free fermion F_2 (two generators psi_1, psi_2 of weight 1/2).

    OPE:
      psi_i(z) psi_j(w) ~ delta_{ij} / (z-w)    (simple pole for i=j)

    r-matrix:
      Diagonal (i=j): OPE has z^{-1} -> r-matrix z^0 = regular, DROPS.
      Off-diagonal (i!=j): no singular OPE.

    r(z) = 0 for all channels.

    The simple pole in the OPE is absorbed by d log(z-w), producing
    a regular (z^0) term that exits the collision residue.

    Like betagamma, the free fermion r-matrix is entirely regular.
    However, the mechanism is different: for betagamma, the mixed
    propagator produces the simple pole; for the free fermion, the
    diagonal (same-generator) propagator produces it.

    Note: psi_i are FERMIONIC (odd statistics, weight 1/2).
    The desuspension s^{-1}(psi_i) has degree |s^{-1}psi_i| = 0 (even),
    so B(F_2) = Sym^c(s^{-1}V_bar), a SYMMETRIC coalgebra.

    Central charge: c(F_2) = 1 (two real fermions = one complex fermion).
    kappa(F_2) = c/2 = 1/2.
    """
    fam = FamilyRMatrix("Free fermion")
    fam.generators = [("psi_1", Fraction(1, 2)), ("psi_2", Fraction(1, 2))]
    fam.statistics = {"psi_1": "fermionic", "psi_2": "fermionic"}
    fam.kappa = Fraction(1, 2)

    # Diagonal channels: simple pole from delta_{ij}/(z-w)
    fam.add_channel(
        "psi1_psi1", "psi_1", "psi_1",
        ope_poles={1: Fraction(1)},
        description="psi_1(z)psi_1(w) ~ 1/(z-w)"
    )
    fam.add_channel(
        "psi2_psi2", "psi_2", "psi_2",
        ope_poles={1: Fraction(1)},
        description="psi_2(z)psi_2(w) ~ 1/(z-w)"
    )

    # Off-diagonal channels: no singular OPE
    fam.add_channel(
        "psi1_psi2", "psi_1", "psi_2",
        ope_poles={},
        description="psi_1(z)psi_2(w) ~ 0 (regular)"
    )
    fam.add_channel(
        "psi2_psi1", "psi_2", "psi_1",
        ope_poles={},
        description="psi_2(z)psi_1(w) ~ 0 (regular)"
    )

    return fam


# ========================================================================
# Full landscape: all 8 families
# ========================================================================

def full_landscape(k: Fraction = Fraction(1),
                   c_vir: Fraction = Fraction(26),
                   c_w3: Fraction = Fraction(4),
                   lam_bg: Fraction = Fraction(1)) -> Dict[str, FamilyRMatrix]:
    """Build the full r-matrix landscape for all 8 families.

    Args:
        k: level for Heisenberg and affine KM families
        c_vir: central charge for Virasoro
        c_w3: central charge for W_3
        lam_bg: weight parameter for betagamma

    Returns:
        Dict mapping family name to FamilyRMatrix.
    """
    return {
        "heisenberg": heisenberg_rmatrix(k),
        "affine_sl2": affine_sl2_rmatrix(k),
        "affine_sl3": affine_sl3_rmatrix(k),
        "virasoro": virasoro_rmatrix(c_vir),
        "w3_TT": w3_TT_rmatrix(c_w3),
        "w3_WW": w3_WW_rmatrix(c_w3),
        "betagamma": betagamma_rmatrix(lam_bg),
        "free_fermion": free_fermion_rmatrix(),
    }


# ========================================================================
# Casimir tensor constructions (for CYBE verification)
# ========================================================================

def sl2_casimir_fund() -> np.ndarray:
    """Build the sl_2 Casimir tensor Omega in V tensor V, V = C^2.

    Omega = E tensor F + F tensor E + (1/2) H tensor H

    in the Chevalley basis {E, F, H} with
      E = [[0,1],[0,0]], F = [[0,0],[1,0]], H = [[1,0],[0,-1]]

    and the standard Killing form normalization
      (E,F) = 1, (H,H) = 2  =>  (H,H)/2 = 1

    so Omega = sum_{a} T^a tensor T_a with (T^a, T_b) = delta^a_b:
    the dual-basis Casimir.
    """
    E = np.array([[0, 1], [0, 0]], dtype=complex)
    F = np.array([[0, 0], [1, 0]], dtype=complex)
    H = np.array([[1, 0], [0, -1]], dtype=complex)

    return np.kron(E, F) + np.kron(F, E) + 0.5 * np.kron(H, H)


def sl3_casimir_fund() -> np.ndarray:
    """Build the sl_3 Casimir tensor Omega in V tensor V, V = C^3.

    Chevalley basis of sl_3:
      H1 = diag(1,-1,0), H2 = diag(0,1,-1)
      E1 = e_{12}, E2 = e_{23}, E3 = e_{13}
      F1 = e_{21}, F2 = e_{32}, F3 = e_{31}

    Killing form in the fundamental: (X,Y) = tr(XY).
    Cartan matrix: A = [[2,-1],[-1,2]].
    Inverse Cartan metric: K^{-1} = (1/3)[[2,1],[1,2]].

    Omega = sum_{i,j} (K^{-1})_{ij} H_i tensor H_j
          + sum_{alpha>0} (E_alpha tensor F_alpha + F_alpha tensor E_alpha)
    """
    H1 = np.diag([1, -1, 0]).astype(complex)
    H2 = np.diag([0, 1, -1]).astype(complex)
    E1 = np.zeros((3, 3), dtype=complex); E1[0, 1] = 1
    E2 = np.zeros((3, 3), dtype=complex); E2[1, 2] = 1
    E3 = np.zeros((3, 3), dtype=complex); E3[0, 2] = 1
    F1 = np.zeros((3, 3), dtype=complex); F1[1, 0] = 1
    F2 = np.zeros((3, 3), dtype=complex); F2[2, 1] = 1
    F3 = np.zeros((3, 3), dtype=complex); F3[2, 0] = 1

    K_inv = np.array([[2, 1], [1, 2]], dtype=complex) / 3.0
    H_gens = [H1, H2]

    Omega = np.zeros((9, 9), dtype=complex)
    for i in range(2):
        for j in range(2):
            Omega += K_inv[i, j] * np.kron(H_gens[i], H_gens[j])
    for Ep, Fp in [(E1, F1), (E2, F2), (E3, F3)]:
        Omega += np.kron(Ep, Fp) + np.kron(Fp, Ep)

    return Omega


def permutation_operator(n: int) -> np.ndarray:
    """Build the permutation operator P on C^n tensor C^n.

    P |i> tensor |j> = |j> tensor |i>.
    """
    P = np.zeros((n * n, n * n), dtype=complex)
    for i in range(n):
        for j in range(n):
            P[i * n + j, j * n + i] = 1
    return P


def casimir_triple(Omega: np.ndarray, n: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Build Omega_{12}, Omega_{13}, Omega_{23} in V^{tensor 3}, V = C^n.

    These are the three embeddings of the Casimir tensor into the
    triple tensor product, needed for the IBR/CYBE verification.

    Args:
        Omega: n^2 x n^2 Casimir tensor on V tensor V.
        n: dimension of V.

    Returns:
        (Omega_12, Omega_13, Omega_23) as n^3 x n^3 matrices.
    """
    I_n = np.eye(n, dtype=complex)

    # Omega_12 = Omega tensor I_n
    O12 = np.kron(Omega, I_n)

    # Omega_23 = I_n tensor Omega
    O23 = np.kron(I_n, Omega)

    # Omega_13: need to act on slots 1 and 3 of V^{tensor 3}.
    # Omega = sum_a T^a tensor T_a, so
    # Omega_13 = sum_a T^a tensor I tensor T_a.
    # We can compute this by extracting the rank-1 components, or
    # by using the permutation P_{23} to move slot 3 to slot 2:
    #   Omega_13 = (I tensor P_{23}) . (Omega tensor I) . (I tensor P_{23})
    P23 = np.kron(I_n, permutation_operator(n))
    O13 = P23 @ O12 @ P23

    return O12, O13, O23


def verify_ibr(Omega: np.ndarray, n: int, atol: float = 1e-10) -> Dict[str, float]:
    """Verify the infinitesimal braid relation (IBR) for a Casimir tensor.

    IBR: [Omega_{ij}, Omega_{ik} + Omega_{jk}] = 0 for all (i,j,k).

    This is equivalent to the CYBE for r(z) = Omega/z with spectral parameter.

    Args:
        Omega: n^2 x n^2 Casimir tensor.
        n: dimension of V.
        atol: absolute tolerance for the norm check.

    Returns:
        Dict with norms of each IBR commutator.
    """
    O12, O13, O23 = casimir_triple(Omega, n)
    comm = lambda A, B: A @ B - B @ A

    norms = {
        "[O12, O13+O23]": float(np.max(np.abs(comm(O12, O13 + O23)))),
        "[O13, O12+O23]": float(np.max(np.abs(comm(O13, O12 + O23)))),
        "[O23, O12+O13]": float(np.max(np.abs(comm(O23, O12 + O13)))),
    }
    return norms


def verify_casimir_symmetry(Omega: np.ndarray, n: int,
                            atol: float = 1e-12) -> float:
    """Verify that the Casimir is symmetric: P . Omega . P = Omega.

    This is a prerequisite for skew-symmetry of r(z) = Omega/z:
      r_{12}(z) + r_{21}(-z) = Omega/z + P.Omega.P/(-z) = 0
    requires P.Omega.P = Omega.

    Returns the max-norm of Omega - P.Omega.P.
    """
    P = permutation_operator(n)
    return float(np.max(np.abs(Omega - P @ Omega @ P)))


# ========================================================================
# Explicit r-matrix formulas (operator-valued)
# ========================================================================

def heisenberg_r_explicit(k: Fraction, z: complex) -> complex:
    """r(z) = k/z for the Heisenberg at level k."""
    return complex(k) / z


def virasoro_r_explicit(c: Fraction, z: complex,
                        T_eigenvalue: complex = 0.0) -> complex:
    """r(z) = (c/2)/z^3 + 2T/z for the Virasoro at central charge c.

    Args:
        c: central charge
        z: spectral parameter
        T_eigenvalue: the eigenvalue of T (the L_0 weight of the state).
            For the vacuum: T = 0.  For a primary of weight h: T = h.

    Returns:
        The scalar value of r(z) on the given state.
    """
    return complex(c) / (2 * z**3) + 2 * T_eigenvalue / z


def affine_r_explicit_fund(k: Fraction, Omega: np.ndarray,
                           z: complex) -> np.ndarray:
    """r(z) = k * Omega / z for affine algebras in the fundamental representation.

    Args:
        k: level
        Omega: Casimir tensor in V tensor V
        z: spectral parameter

    Returns:
        n^2 x n^2 matrix r(z) = k * Omega / z.
    """
    return complex(k) * Omega / z


# ========================================================================
# Summary report
# ========================================================================

def landscape_summary() -> str:
    """Generate a human-readable summary of the r-matrix landscape."""
    landscape = full_landscape()
    lines = ["=" * 72]
    lines.append("r-MATRIX LANDSCAPE: COLLISION RESIDUES FOR 8 STANDARD FAMILIES")
    lines.append("r(z) = Res^{coll}_{0,2}(Theta_A)")
    lines.append("AP19: pole orders = OPE poles - 1 (d log absorption)")
    lines.append("=" * 72)

    for family_key, fam in landscape.items():
        lines.append(f"\n--- {fam.name} ---")
        lines.append(f"  Generators: {fam.generators}")
        lines.append(f"  kappa(A) = {fam.kappa}")
        for ch_name, ch in fam.channels.items():
            ope_str = str(ch['ope_poles']) if ch['ope_poles'] else "{} (regular)"
            r_str = str(ch['rmatrix_poles']) if ch['rmatrix_poles'] else "{} (entirely regular)"
            lines.append(f"  Channel {ch_name}:")
            lines.append(f"    OPE poles: {ope_str}")
            lines.append(f"    r-matrix poles: {r_str}")
            lines.append(f"    AP19 shift: max pole {ch['ope_max_pole']} -> {ch['rmatrix_max_pole']}")

        # AP19 verification
        ap19 = fam.verify_ap19()
        all_pass = all(ap19.values())
        lines.append(f"  AP19 verification: {'PASS' if all_pass else 'FAIL'}")

        # Bosonic parity
        bp = fam.verify_bosonic_parity()
        if bp:
            all_bp = all(bp.values())
            lines.append(f"  Bosonic parity: {'PASS' if all_bp else 'FAIL'}")

    lines.append("\n" + "=" * 72)
    return "\n".join(lines)
