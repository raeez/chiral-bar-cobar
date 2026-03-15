#!/usr/bin/env python3
"""Quick validation: sl₂ bar cohomology via chiral_bar_direct.

This should give Riordan R(n+3): 3, 6, 15, 36, 91.
"""
import sys
sys.path.insert(0, '/Users/raeez/chiral-bar-cobar/compute/scripts')
from chiral_bar_direct import sl2_structure_constants, compute_bar_cohomology

d, sc = sl2_structure_constants()
compute_bar_cohomology(d, sc, "sl_2", max_deg=5, expected=[3, 6, 15, 36, 91])
