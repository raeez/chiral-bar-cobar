"""Independent bar-side C^res extraction and comparison with C^DS.

This test module provides the FIRST independent bar-side verification
of the DS-KD intertwining theorem (thm:ds-koszul-intertwine).

The key idea:
  C^res_{s,t;u;0,n}(N) = primary coefficient of W^(u) at pole order n
                          in the W^(s)(z) W^(t)(w) OPE.
  C^DS_{s,t;u;0,n}(N) = same coefficient extracted from the DS reduction
                          of the KM bar complex.
  thm:ds-koszul-intertwine says C^res = C^DS.

This module extracts C^res directly from the W_3 OPE (w3_bar.py)
and compares with C^DS from the seed packet (w4_stage4_coefficients.py).
The two code paths are completely independent.

Ground truth:
  prop:winfty-ds-stage3-explicit-packet (bar_cobar_construction.tex:6856)
  Stage-3 packet I_3: 15 entries, 3 nonzero, 12 zeros.

Conventions (CLAUDE.md):
  - Vertex algebra OPE: a(z)b(w) ~ sum_{n>=0} a_{(n)}b / (z-w)^{n+1}
  - So mode index n corresponds to pole order n+1.
  - Cohomological grading: |d| = +1
"""

from __future__ import annotations

import pytest
from sympy import Rational, Symbol

from compute.lib.w3_bar import w3_nth_products
from compute.lib.w4_stage4_coefficients import (
    seed_set,
    stage3_ds_coefficients,
)


# Generator spin -> name in w3_bar.py
SPIN_TO_GEN = {2: "T", 3: "W"}

# Primary generators (not descendants, not composites)
PRIMARY_GENS = {"T": 2, "W": 3}


def extract_c_res_stage3() -> dict:
    """Extract C^res from the W_3 OPE for all tuples in I_3.

    For each (s, t, u, n_pole) in I_3:
      - Look up the (s, t) OPE pair
      - Find the mode index = n_pole - 1 (since pole order P = mode + 1)
      - Extract the coefficient of the primary generator of spin u
    """
    products = w3_nth_products()
    seeds = seed_set(3)
    c_res = {}

    for s, t, u, n_pole in seeds:
        gen_s = SPIN_TO_GEN[s]
        gen_t = SPIN_TO_GEN[t]
        target = SPIN_TO_GEN[u]
        pair = (gen_s, gen_t)
        mode_index = n_pole - 1  # pole order P = mode + 1

        if pair in products and mode_index in products[pair]:
            coeff = products[pair][mode_index].get(target, 0)
        else:
            coeff = 0

        c_res[(s, t, u, n_pole)] = coeff

    return c_res


class TestBarSideExtraction:
    """Verify C^res = C^DS on the stage-3 seed packet I_3."""

    def test_seed_set_size(self):
        """I_3 has exactly 15 elements."""
        assert len(seed_set(3)) == 15

    def test_c_res_matches_c_ds_full_packet(self):
        """All 15 entries of C^res match C^DS."""
        c_res = extract_c_res_stage3()
        c_ds = stage3_ds_coefficients()
        for seed in seed_set(3):
            assert c_res[seed] == c_ds[seed], (
                f"Mismatch at {seed}: C^res={c_res[seed]}, C^DS={c_ds[seed]}"
            )

    def test_three_nonzero_entries(self):
        """Exactly three entries are nonzero."""
        c_res = extract_c_res_stage3()
        nonzero = {k: v for k, v in c_res.items() if v != 0}
        assert len(nonzero) == 3

    def test_c_res_222_02(self):
        """C^res_{2,2;2;0,2}(3) = 2 (T x T -> T at pole 2)."""
        c_res = extract_c_res_stage3()
        assert c_res[(2, 2, 2, 2)] == 2

    def test_c_res_232_02(self):
        """C^res_{2,3;3;0,2}(3) = 3 (T x W -> W at pole 2)."""
        c_res = extract_c_res_stage3()
        assert c_res[(2, 3, 3, 2)] == 3

    def test_c_res_332_04(self):
        """C^res_{3,3;2;0,4}(3) = 2 (W x W -> T at pole 4)."""
        c_res = extract_c_res_stage3()
        assert c_res[(3, 3, 2, 4)] == 2

    def test_twelve_zeros(self):
        """Exactly twelve entries are zero."""
        c_res = extract_c_res_stage3()
        zeros = {k: v for k, v in c_res.items() if v == 0}
        assert len(zeros) == 12

    def test_no_spin3_target_in_TT(self):
        """T x T OPE has no primary spin-3 target (W does not appear)."""
        c_res = extract_c_res_stage3()
        assert c_res[(2, 2, 3, 1)] == 0

    def test_no_spin2_target_in_TW(self):
        """T x W OPE has no primary spin-2 target at any pole order."""
        c_res = extract_c_res_stage3()
        for n_pole in [1, 2, 3]:
            assert c_res.get((2, 3, 2, n_pole), 0) == 0

    def test_ww_spin3_target_absent(self):
        """W x W OPE has no primary W target (only T and composites)."""
        c_res = extract_c_res_stage3()
        for n_pole in [1, 2, 3]:
            assert c_res.get((3, 3, 3, n_pole), 0) == 0


class TestPoleOrderConvention:
    """Verify the pole-order-to-mode-index convention is correct."""

    def test_tt_quartic_pole(self):
        """T_{(3)}T = c/2 is at pole order 4 (quartic), mode index 3."""
        products = w3_nth_products()
        c = Symbol("c")
        # Mode 3 gives pole order 4
        assert products[("T", "T")][3]["vac"] == c / 2

    def test_tt_double_pole(self):
        """T_{(1)}T = 2T is at pole order 2 (double), mode index 1."""
        products = w3_nth_products()
        assert products[("T", "T")][1]["T"] == 2

    def test_ww_sixth_pole(self):
        """W_{(5)}W = c/3 is at pole order 6, mode index 5."""
        products = w3_nth_products()
        c = Symbol("c")
        assert products[("W", "W")][5]["vac"] == c / 3

    def test_tw_weight_action(self):
        """T_{(1)}W = 3W: the conformal weight of W."""
        products = w3_nth_products()
        assert products[("T", "W")][1]["W"] == 3
