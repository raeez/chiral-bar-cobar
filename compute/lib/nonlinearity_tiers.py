#!/usr/bin/env python3
r"""
nonlinearity_tiers.py — Three-tier classification of OPE nonlinearity and
the corrected finite/infinite depth criterion.

THE CORRECTED CLASSIFICATION:

The "depth-4 barrier for free theories" is WRONG. The correct picture is a
THREE-TIER HIERARCHY of OPE nonlinearity:

Tier 1 (ABELIAN): OPE output ∈ span{vacuum, ∂^k(inputs)}.
  No new fields created. Shadow depth ≤ 2.
  Examples: Heisenberg, free fermion.

Tier 2 (CONTROLLED): OPE creates new fields, but determined by bilinear data.
  The vertex operator OPE e^{iλ·X} · e^{iμ·X} ~ (z-w)^{λ·μ} e^{i(λ+μ)·X}
  creates the NEW field e^{i(λ+μ)·X}, but the structure is controlled by the
  inner product λ·μ.  Shadow depth finite but UNBOUNDED (grows with rank).
  Examples: Affine V_k(g) (depth 3), V_{E_8} (depth 3), V_{Leech} (depth 4),
  rank-48 lattice (depth 5), rank-72 (depth 6), ...

Tier 2' (CONTACT): OPE is abelian, but an external deformation parameter
  (the conformal weight λ) creates nontrivial shadow tower.
  Shadow depth ≤ 4.
  Example: βγ system (depth 4).

Tier 3 (SELF-REFERENTIAL): A generator appears in its OWN self-OPE.
  The defining condition: ∃ strong generator a such that a ∈ a_{(k)}a for some k.
  Shadow depth = ∞.
  Examples: Virasoro (T_{(1)}T = 2T), W_N (T_{(1)}T = 2T), Yangians.

THE FINITE/INFINITE CRITERION (corrected):

  depth(A) = ∞  ⟺  ∃ strong generator a with a ∈ a_{(k)}a
  depth(A) < ∞  ⟺  ∀ strong generators a: a ∉ a_{(k)}a

This is the DIRECT SELF-REFERENTIALITY criterion. INDIRECT loops
(a ∈ b_{(k)}b where b ≠ a, and b ∈ a_{(j)}c) do NOT force infinite depth.
The affine case has J ∈ E_{(0)}E^{-α} (indirect), but J ∉ J_{(k)}J (no direct
self-loop), so depth is finite (3).

THE SHADOW-L CORRESPONDENCE (corrected):

  For lattice VOAs:
    depth d = 1 + (# critical lines of ε^c_s)  [PROVED for 5 examples]

  For all VOAs:
    depth d = ∞ ⟺ self-referential OPE  [CRITERION]
    depth d < ∞ ⟺ no self-referential OPE, and d determined by
                    the modular form content of the partition function

  The cusp singularity theorem relates depth to cusp growth:
    Tier 1: polynomial growth y^{c/2} → depth 2
    Tier 2: polynomial growth y^k (from theta ∈ M_k) → depth = 1 + # critical lines
    Tier 2': exponential e^{πy/6} (from 1/η²) → depth 4
    Tier 3: exponential e^{πcy/12} (from vacuum character) → depth ∞
"""

import numpy as np


def classify_nonlinearity(ope_data):
    r"""
    Classify the nonlinearity tier of a vertex algebra from its OPE data.

    ope_data: dict with keys 'generators' (list of generator names) and
    'self_ope' (dict mapping generator a to the set of generators appearing
    in a_{(k)}a for all k).

    Returns the tier (1, 2, 2', or 3) and predicted depth range.
    """
    generators = ope_data.get('generators', [])
    self_ope = ope_data.get('self_ope', {})
    creates_new = ope_data.get('creates_new_fields', False)
    has_weight_deformation = ope_data.get('weight_deformation', False)

    # Check Tier 3: self-referential
    for a in generators:
        if a in self_ope.get(a, set()):
            return {
                'tier': 3,
                'name': 'Self-referential (Composite)',
                'self_referential_generator': a,
                'depth': float('inf'),
                'mechanism': f'{a} ∈ {a}_(k){a}: direct self-loop',
            }

    # Check Tier 2: controlled nonlinearity
    if creates_new:
        return {
            'tier': 2,
            'name': 'Controlled (Lattice/Lie)',
            'depth': 'finite, unbounded',
            'mechanism': 'OPE creates new fields but no self-loops',
        }

    # Check Tier 2': contact/deformation
    if has_weight_deformation:
        return {
            'tier': 2.5,
            'name': 'Contact (Deformation)',
            'depth': '≤ 4',
            'mechanism': 'Abelian OPE + weight deformation',
        }

    # Tier 1: abelian
    return {
        'tier': 1,
        'name': 'Abelian (Free)',
        'depth': '≤ 2',
        'mechanism': 'OPE output ∈ span{vacuum, derivatives of inputs}',
    }


# ============================================================
# Standard examples
# ============================================================

def heisenberg_ope():
    return {
        'generators': ['J'],
        'self_ope': {'J': set()},  # J_{(k)}J = κ·vac, no J in output
        'creates_new_fields': False,
        'weight_deformation': False,
    }


def affine_sl2_ope():
    return {
        'generators': ['J+', 'J-', 'J3'],
        'self_ope': {
            'J+': set(),        # J+_{(k)}J+ = 0 (regular)
            'J-': set(),        # J-_{(k)}J- = 0
            'J3': set(),        # J3_{(k)}J3 = k·vac
        },
        'creates_new_fields': True,  # J+_{(0)}J- = J3 (new generator appears)
        'weight_deformation': False,
    }


def e8_ope():
    return {
        'generators': ['J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8'] + ['E_alpha'] * 240,
        'self_ope': {f'J{i}': set() for i in range(1, 9)},  # J_i not in J_i · J_i
        # E^α not in E^α · E^α (since 2α is never a root)
        'creates_new_fields': True,  # E^α · E^β = ε E^{α+β} if α+β ∈ Δ
        'weight_deformation': False,
    }


def betagamma_ope():
    return {
        'generators': ['beta', 'gamma'],
        'self_ope': {
            'beta': set(),     # β_{(k)}β = 0
            'gamma': set(),    # γ_{(k)}γ = 0
        },
        'creates_new_fields': False,
        'weight_deformation': True,  # λ deformation
    }


def virasoro_ope():
    return {
        'generators': ['T'],
        'self_ope': {'T': {'T'}},  # T_{(1)}T = 2T: T IS in T·T output!
        'creates_new_fields': True,
        'weight_deformation': False,
    }


def w3_ope():
    return {
        'generators': ['T', 'W'],
        'self_ope': {
            'T': {'T'},   # T_{(1)}T = 2T
            'W': set(),   # W_{(k)}W = ... + Λ = :TT:, but W ∉ W·W directly
        },
        'creates_new_fields': True,
        'weight_deformation': False,
    }


def classify_all_standard():
    """Classify all standard examples."""
    examples = {
        'Heisenberg': heisenberg_ope(),
        'Affine sl_2': affine_sl2_ope(),
        'V_{E_8}': e8_ope(),
        'βγ': betagamma_ope(),
        'Virasoro': virasoro_ope(),
        'W_3': w3_ope(),
    }

    results = {}
    for name, ope in examples.items():
        results[name] = classify_nonlinearity(ope)
        results[name]['algebra'] = name

    return results
