"""Genus-1 and genus-2 free energies for the full standard landscape.

The genus-g free energy of a modular Koszul algebra A is

    F_g(A) = kappa(A) * lambda_g^FP

where lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!
is the Faber-Pandharipande intersection number.

At genus 1:  F_1 = kappa / 24       (lambda_1^FP = 1/24)
At genus 2:  F_2 = 7 * kappa / 5760 (lambda_2^FP = 7/5760)

This module computes F_1 and F_2 for all 15+ standard families in the
monograph landscape, using the authoritative kappa formulas from
shadow_metric_census.py and genus_expansion.py.

Mathematical references:
    - thm:universal-generating-function in higher_genus_modular_koszul.tex
    - tab:master-invariants in landscape_census.tex
    - The genus-1 formula F_1 = kappa/24 is UNCONDITIONAL for all modular
      Koszul algebras (proved at genus 1 for all families, including
      multi-generator).

CAUTION (AP1): Each kappa formula is FAMILY-SPECIFIC:
    kappa(H_k) = k                              (Heisenberg)
    kappa(V_Lambda) = rank(Lambda)              (lattice VOA)
    kappa(ff) = 1/4                             (free fermion, c = 1/2)
    kappa(bg, lambda) = 6*lambda^2 - 6*lambda + 1  (betagamma)
    kappa(bc, j) = -(6j^2 - 6j + 1)            (bc ghosts)
    kappa(Vir_c) = c/2                          (Virasoro)
    kappa(g_k) = dim(g) * (k + h^v) / (2 * h^v)  (affine Kac-Moody)
    kappa(W_N, c) = (H_N - 1) * c               (W-algebras)
These are DISTINCT formulas. NEVER copy between families (AP1).
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, NamedTuple, Optional

from sympy import Rational


# =========================================================================
# Faber-Pandharipande numbers (exact rational)
# =========================================================================

LAMBDA_FP_1 = Rational(1, 24)
LAMBDA_FP_2 = Rational(7, 5760)


# =========================================================================
# Family data
# =========================================================================

class FamilyData(NamedTuple):
    """Data for a single algebra family at specific parameter values."""
    name: str
    kappa: Rational
    central_charge: Rational
    description: str


def _R(n, d=1):
    """Shorthand for Rational(n, d)."""
    return Rational(n, d)


# =========================================================================
# Kappa formulas (from first principles, not copied)
# =========================================================================

def kappa_heisenberg(level):
    """kappa(H_k) = k."""
    return Rational(level)


def kappa_free_fermion():
    """kappa(free fermion) = 1/4.

    The free fermion has c = 1/2. kappa = c/2 = 1/4.
    """
    return _R(1, 4)


def kappa_betagamma(weight):
    """kappa(betagamma, lambda) = 6*lambda^2 - 6*lambda + 1.

    At lambda = 0 or 1: kappa = 1.
    At lambda = 1/2: kappa = -1/2 (symplectic).
    """
    w = Rational(weight)
    return 6 * w**2 - 6 * w + 1


def kappa_bc(spin):
    """kappa(bc, j) = -(6j^2 - 6j + 1).

    Opposite sign from betagamma. At j = 0: kappa = -1.
    """
    j = Rational(spin)
    return -(6 * j**2 - 6 * j + 1)


def kappa_virasoro(c):
    """kappa(Vir_c) = c/2."""
    return Rational(c) / 2


def kappa_affine(dim_g, h_dual, level):
    """kappa(g_k) = dim(g) * (k + h^v) / (2 * h^v).

    General formula for affine Kac-Moody algebras.

    Args:
        dim_g: dimension of the finite-dimensional Lie algebra g
        h_dual: dual Coxeter number h^v
        level: affine level k
    """
    return Rational(dim_g) * (Rational(level) + Rational(h_dual)) / (2 * Rational(h_dual))


def kappa_wN(N, c):
    """kappa(W_N, c) = (H_N - 1) * c.

    H_N = 1 + 1/2 + ... + 1/N is the N-th harmonic number.
    (H_N - 1) = 1/2 + 1/3 + ... + 1/N.

    For Virasoro (N = 2): H_2 - 1 = 1/2, so kappa = c/2.
    For W_3 (N = 3): H_3 - 1 = 1/2 + 1/3 = 5/6, so kappa = 5c/6.
    """
    rho = sum(Rational(1, i) for i in range(2, N + 1))
    return rho * Rational(c)


def kappa_lattice(rank):
    """kappa(V_Lambda) = rank(Lambda).

    For even self-dual lattice VOAs: kappa equals the rank.
    D_4: rank 4, E_8: rank 8, Leech: rank 24.
    """
    return Rational(rank)


# =========================================================================
# The 15+ standard families (specific parameter values)
# =========================================================================

# Lie algebra data: (type, dim, h_dual)
LIE_DATA = {
    'sl2': (3, 2),
    'sl3': (8, 3),
    'G2': (14, 4),
    'E8': (248, 30),
}


def build_landscape():
    """Build the full landscape of 15+ standard families.

    Returns a list of FamilyData tuples with kappa computed from first
    principles for each family.
    """
    families = []

    # 1. Heisenberg H_1
    families.append(FamilyData(
        name='Heisenberg H_1',
        kappa=kappa_heisenberg(1),
        central_charge=_R(1),
        description='Single free boson at level k=1',
    ))

    # 2. Free fermion
    families.append(FamilyData(
        name='Free fermion',
        kappa=kappa_free_fermion(),
        central_charge=_R(1, 2),
        description='Single real fermion, c = 1/2',
    ))

    # 3. betagamma at lambda = 1
    families.append(FamilyData(
        name='betagamma (lambda=1)',
        kappa=kappa_betagamma(1),
        central_charge=_R(2),
        description='Standard betagamma at conformal weight lambda = 1, c = 2',
    ))

    # 4. bc at spin j = 0 (equivalently lambda = 0)
    families.append(FamilyData(
        name='bc (j=0)',
        kappa=kappa_bc(0),
        central_charge=_R(-2),
        description='bc ghosts at spin j = 0, c = -2',
    ))

    # 5. Affine sl_2 at k = 1
    dim_sl2, h_sl2 = LIE_DATA['sl2']
    families.append(FamilyData(
        name='Affine sl_2 (k=1)',
        kappa=kappa_affine(dim_sl2, h_sl2, 1),
        central_charge=Rational(dim_sl2) * 1 / (1 + h_sl2),
        description='sl_2 at level 1: dim=3, h*=2, kappa = 3*3/4 = 9/4',
    ))

    # 6. Affine sl_3 at k = 1
    dim_sl3, h_sl3 = LIE_DATA['sl3']
    families.append(FamilyData(
        name='Affine sl_3 (k=1)',
        kappa=kappa_affine(dim_sl3, h_sl3, 1),
        central_charge=Rational(dim_sl3) * 1 / (1 + h_sl3),
        description='sl_3 at level 1: dim=8, h*=3, kappa = 8*4/6 = 16/3',
    ))

    # 7. Affine G_2 at k = 1
    dim_G2, h_G2 = LIE_DATA['G2']
    families.append(FamilyData(
        name='Affine G_2 (k=1)',
        kappa=kappa_affine(dim_G2, h_G2, 1),
        central_charge=Rational(dim_G2) * 1 / (1 + h_G2),
        description='G_2 at level 1: dim=14, h*=4, kappa = 14*5/8 = 35/4',
    ))

    # 8. Virasoro at c = 1/2
    families.append(FamilyData(
        name='Virasoro (c=1/2)',
        kappa=kappa_virasoro(_R(1, 2)),
        central_charge=_R(1, 2),
        description='Virasoro at c = 1/2 (Ising model)',
    ))

    # 9. Virasoro at c = 25
    families.append(FamilyData(
        name='Virasoro (c=25)',
        kappa=kappa_virasoro(25),
        central_charge=_R(25),
        description='Virasoro at c = 25 (Koszul dual of c = 1)',
    ))

    # 10. W_3 at c = 2
    families.append(FamilyData(
        name='W_3 (c=2)',
        kappa=kappa_wN(3, 2),
        central_charge=_R(2),
        description='W_3 algebra at c = 2, kappa = 5*2/6 = 5/3',
    ))

    # 11. W_3 at c = 50 (self-dual)
    families.append(FamilyData(
        name='W_3 (c=50, self-dual)',
        kappa=kappa_wN(3, 50),
        central_charge=_R(50),
        description='W_3 at self-dual c = 50, kappa = 5*50/6 = 125/3',
    ))

    # 12. D_4 lattice VOA
    families.append(FamilyData(
        name='D_4 lattice',
        kappa=kappa_lattice(4),
        central_charge=_R(4),
        description='Even self-dual D_4 lattice VOA, rank 4',
    ))

    # 13. E_8 lattice VOA
    families.append(FamilyData(
        name='E_8 lattice',
        kappa=kappa_lattice(8),
        central_charge=_R(8),
        description='Even self-dual E_8 lattice VOA, rank 8',
    ))

    # 14. Leech lattice VOA
    families.append(FamilyData(
        name='Leech lattice',
        kappa=kappa_lattice(24),
        central_charge=_R(24),
        description='Leech lattice VOA, rank 24',
    ))

    # 15. Affine E_8 at k = 1
    dim_E8, h_E8 = LIE_DATA['E8']
    families.append(FamilyData(
        name='Affine E_8 (k=1)',
        kappa=kappa_affine(dim_E8, h_E8, 1),
        central_charge=Rational(dim_E8) * 1 / (1 + h_E8),
        description='E_8 at level 1: dim=248, h*=30, kappa = 248*31/60 = 1922/15',
    ))

    return families


# =========================================================================
# Free energy computations
# =========================================================================

def F1(kappa):
    """Genus-1 free energy: F_1 = kappa / 24."""
    return kappa * LAMBDA_FP_1


def F2(kappa):
    """Genus-2 free energy: F_2 = 7 * kappa / 5760."""
    return kappa * LAMBDA_FP_2


def Fg(kappa, g):
    """Genus-g free energy: F_g = kappa * lambda_g^FP.

    Uses the Faber-Pandharipande intersection number:
        lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!
    """
    from sympy import bernoulli, factorial
    B_2g = bernoulli(2 * g)
    numerator = (2 ** (2 * g - 1) - 1) * abs(B_2g)
    denominator = 2 ** (2 * g - 1) * factorial(2 * g)
    lam = Rational(numerator, denominator)
    return kappa * lam


def landscape_F1():
    """Compute F_1 for all 15 standard families.

    Returns a list of dicts with keys: name, kappa, F1, F1_simplified.
    """
    results = []
    for family in build_landscape():
        f1 = F1(family.kappa)
        results.append({
            'name': family.name,
            'kappa': family.kappa,
            'c': family.central_charge,
            'F1': f1,
            'description': family.description,
        })
    return results


def landscape_F2():
    """Compute F_2 for all 15 standard families.

    Returns a list of dicts with keys: name, kappa, F2.
    """
    results = []
    for family in build_landscape():
        f2 = F2(family.kappa)
        results.append({
            'name': family.name,
            'kappa': family.kappa,
            'c': family.central_charge,
            'F2': f2,
            'description': family.description,
        })
    return results


def landscape_table(max_genus=2):
    """Full landscape table with F_g for g = 1, ..., max_genus.

    Returns a list of dicts with keys: name, kappa, c, F_1, F_2, ..., F_{max_genus}.
    """
    results = []
    for family in build_landscape():
        row = {
            'name': family.name,
            'kappa': family.kappa,
            'c': family.central_charge,
        }
        for g in range(1, max_genus + 1):
            row[f'F_{g}'] = Fg(family.kappa, g)
        results.append(row)
    return results


# =========================================================================
# Expected values (independently computed, for cross-checking)
# =========================================================================

# F_1 = kappa / 24 for each family
EXPECTED_F1 = {
    'Heisenberg H_1':          _R(1, 24),
    'Free fermion':            _R(1, 96),
    'betagamma (lambda=1)':    _R(1, 24),
    'bc (j=0)':                _R(-1, 24),
    'Affine sl_2 (k=1)':      _R(3, 32),     # 9/4 / 24 = 9/96 = 3/32
    'Affine sl_3 (k=1)':      _R(2, 9),      # 16/3 / 24 = 16/72 = 2/9
    'Affine G_2 (k=1)':       _R(35, 96),    # 35/4 / 24 = 35/96
    'Virasoro (c=1/2)':        _R(1, 96),
    'Virasoro (c=25)':         _R(25, 48),
    'W_3 (c=2)':               _R(5, 72),     # 5/3 / 24 = 5/72
    'W_3 (c=50, self-dual)':   _R(125, 72),   # 125/3 / 24 = 125/72
    'D_4 lattice':             _R(1, 6),      # 4/24 = 1/6
    'E_8 lattice':             _R(1, 3),      # 8/24 = 1/3
    'Leech lattice':           _R(1),         # 24/24 = 1
    'Affine E_8 (k=1)':       _R(961, 180),  # 1922/15 / 24 = 1922/360 = 961/180
}

# kappa values (for cross-checking)
EXPECTED_KAPPA = {
    'Heisenberg H_1':          _R(1),
    'Free fermion':            _R(1, 4),
    'betagamma (lambda=1)':    _R(1),
    'bc (j=0)':                _R(-1),
    'Affine sl_2 (k=1)':      _R(9, 4),
    'Affine sl_3 (k=1)':      _R(16, 3),
    'Affine G_2 (k=1)':       _R(35, 4),
    'Virasoro (c=1/2)':        _R(1, 4),
    'Virasoro (c=25)':         _R(25, 2),
    'W_3 (c=2)':               _R(5, 3),
    'W_3 (c=50, self-dual)':   _R(125, 3),
    'D_4 lattice':             _R(4),
    'E_8 lattice':             _R(8),
    'Leech lattice':           _R(24),
    'Affine E_8 (k=1)':       _R(1922, 15),
}


# =========================================================================
# Main
# =========================================================================

if __name__ == '__main__':
    print("=" * 80)
    print("GENUS-1 AND GENUS-2 FREE ENERGIES: FULL STANDARD LANDSCAPE")
    print("F_g(A) = kappa(A) * lambda_g^FP")
    print(f"lambda_1^FP = {LAMBDA_FP_1},  lambda_2^FP = {LAMBDA_FP_2}")
    print("=" * 80)

    for row in landscape_table(max_genus=2):
        print(f"\n  {row['name']}")
        print(f"    c = {row['c']},  kappa = {row['kappa']}")
        print(f"    F_1 = {row['F_1']}")
        print(f"    F_2 = {row['F_2']}")

    # Verification
    print("\n" + "=" * 80)
    print("CROSS-CHECK: F_1 = kappa / 24")
    all_ok = True
    for family in build_landscape():
        computed = F1(family.kappa)
        expected = EXPECTED_F1[family.name]
        match = (computed == expected)
        status = "OK" if match else "FAIL"
        if not match:
            all_ok = False
        print(f"  [{status}] {family.name}: F_1 = {computed} (expected {expected})")
    print(f"\nAll checks passed: {all_ok}")
