"""BV-BRST formalism and its connection to bar-cobar duality.

Ground truth from the manuscript (bv_brst.tex, feynman_diagrams.tex):
  - QME: hbar*Delta*S + (1/2){S,S} = 0 (factor 1/2!)
  - HCS action: Tr(A-bar wedge dbar A + (2/3)A-bar^3) — coefficient 2/3
  - BRST differential Q = {S, -}
  - BV antibracket {F,G} = delta F/delta phi * delta G/delta phi^+ - (same switched)
  - Ghost number grading: fields (0), antifields (+1), ghosts (-1)
  - Bar complex as BV: B(A) encodes classical BV data
  - Curvature = failure of classical master equation (obstruction to d^2=0)

CONVENTIONS:
- Cohomological grading (ghost number = degree)
- QME has factor 1/2 on antibracket (NOT 1)
- HCS has factor 2/3 (NOT 1/3)
"""

from __future__ import annotations

from typing import Dict

from sympy import Rational, Symbol


# ---------------------------------------------------------------------------
# BV data
# ---------------------------------------------------------------------------

def qme_coefficients() -> Dict[str, object]:
    """Quantum master equation coefficients.

    hbar*Delta*S + (1/2){S,S} = 0

    Ground truth: CLAUDE.md.
    """
    return {
        "delta_coeff": Symbol('hbar'),
        "antibracket_coeff": Rational(1, 2),
        "equation": "hbar*Delta*S + (1/2){S,S} = 0",
    }


def hcs_coefficients() -> Dict[str, object]:
    """Holomorphic Chern-Simons action coefficients.

    S = Tr(A-bar wedge dbar A + (2/3) A-bar^3)

    Ground truth: CLAUDE.md.
    """
    return {
        "kinetic_coeff": Rational(1),
        "cubic_coeff": Rational(2, 3),
        "action": "Tr(A-bar ^ dbar A + (2/3) A-bar ^ [A-bar, A-bar])",
    }


# ---------------------------------------------------------------------------
# Ghost number / grading
# ---------------------------------------------------------------------------

def ghost_number_table() -> Dict[str, int]:
    """Ghost number assignments in BV formalism."""
    return {
        "fields": 0,
        "antifields": 1,  # cohomological convention
        "ghosts": -1,
        "antighosts": -2,
        "BRST_operator": 1,  # |Q| = 1
        "antibracket": -1,   # |{,}| = -1
        "Delta": -1,         # |Delta| = -1
    }


# ---------------------------------------------------------------------------
# Bar complex as BV
# ---------------------------------------------------------------------------

def bar_as_bv() -> Dict[str, str]:
    """Interpretation of bar complex in BV language.

    The bar construction B(A) encodes the BV data:
    - Bar generators = fields + ghosts
    - Bar differential = BRST operator Q
    - Curvature m_0 = failure of classical master equation
    - d^2 = 0 in bar = QME satisfied
    """
    return {
        "bar_generators": "fields + ghost tower",
        "bar_differential": "BRST operator Q = {S, -}",
        "curvature": "obstruction to d^2 = 0 (classical anomaly)",
        "d_squared_zero": "equivalent to QME being satisfied",
        "koszul_dual": "antifield complex (BV dual)",
    }


def bar_curvature_as_anomaly(algebra: str) -> Dict[str, object]:
    """Bar curvature interpreted as BV anomaly.

    Curvature m_0 != 0 means the classical master equation fails.
    This is the classical anomaly / obstruction.
    """
    anomaly_data = {
        "Virasoro": {
            "m0": "c/2",
            "anomaly": "Conformal anomaly (central charge)",
            "anomaly_free_at": "c = 0",
            "dual_anomaly_free_at": "c = 26 (bosonic string)",
        },
        "W3": {
            "m0": "5c/6",
            "anomaly": "W-algebra anomaly",
            "anomaly_free_at": "c = 0",
            "dual_anomaly_free_at": "c = 100 (W_3 string?)",
        },
        "sl2": {
            "m0": "3(k+2)/4 * kappa",
            "anomaly": "Level anomaly",
            "anomaly_free_at": "k = -2 (critical level)",
        },
    }
    return anomaly_data.get(algebra, {"m0": "unknown"})


# ---------------------------------------------------------------------------
# Feynman diagram interpretation
# ---------------------------------------------------------------------------

def feynman_bar_correspondence() -> Dict[str, str]:
    """Correspondence between Feynman diagrams and bar complex.

    Ground truth: feynman_diagrams.tex, feynman_connection.tex.
    """
    return {
        "propagator": "log form omega_{ij} on FM_n",
        "vertex": "OPE n-th product a_{(n)}b",
        "loop": "genus-g contribution (modular operad)",
        "tree_level": "genus-0 bar-cobar (classical Koszul duality)",
        "1_loop": "genus-1 correction F_1(A)",
        "divergence": "curvature / central extension",
        "renormalization": "Arnold cancellation kills divergences",
    }


# ---------------------------------------------------------------------------
# Verification
# ---------------------------------------------------------------------------

def verify_bv_brst():
    results = {}

    # QME coefficients
    qme = qme_coefficients()
    results["QME: antibracket = 1/2"] = qme["antibracket_coeff"] == Rational(1, 2)

    # HCS coefficients
    hcs = hcs_coefficients()
    results["HCS: cubic = 2/3"] = hcs["cubic_coeff"] == Rational(2, 3)

    # Ghost numbers
    gn = ghost_number_table()
    results["fields: ghost# = 0"] = gn["fields"] == 0
    results["BRST: ghost# = 1"] = gn["BRST_operator"] == 1

    # Bar as BV
    bv = bar_as_bv()
    results["bar diff = BRST"] = "BRST" in bv["bar_differential"]

    # Anomalies
    vir_anom = bar_curvature_as_anomaly("Virasoro")
    results["Vir anomaly-free at c=0"] = "c = 0" in vir_anom["anomaly_free_at"]
    results["Vir dual at c=26"] = "c = 26" in vir_anom["dual_anomaly_free_at"]

    return results


if __name__ == "__main__":
    print("=" * 60)
    print("BV-BRST FORMALISM: VERIFICATION")
    print("=" * 60)

    for name, ok in verify_bv_brst().items():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
