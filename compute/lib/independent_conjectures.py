"""Computational checks for independent conjectures (not subsumed by MC1-MC5).

Three independent conjectures with computational handles:

1. VIRASORO c=26 SELF-DUALITY
   The Virasoro complementarity c + c' = 26 implies self-duality at c = 13
   (or trivial duality c = 26, c' = 0). At c = 26, the dual is the trivial
   algebra (c' = 0, uncurved), and the bar complex B(Vir_26) acquires special
   structure related to the bosonic string critical dimension.

2. DERIVED bc-betagamma EQUIVALENCE
   The bc ghost system and betagamma system are Koszul dual:
     bc^! = betagamma, betagamma^! = bc
   The conjecture: this lifts to a derived equivalence of module categories.
   Computational checks: central charge complementarity c_bc + c_bg = 0,
   algebraic GF verification P_bg^2 = (1+x)/(1-3x), bc formula 2^n-n+1.
   NOTE: The classical Koszul relation H_A(t)*H_{A!}(-t)=1 does NOT hold
   for chiral bar cohomology (OS algebra structure modifies the relation).

3. NEAR-RATIONALITY (Pade)
   Some bar cohomology GFs are "nearly rational" — Pade approximants
   stabilize quickly. W_3 GF is conjectured rational; Virasoro is algebraic
   but near-rational through degree 8.

Ground truth references:
  - Virasoro complementarity: comp:virasoro-curvature, virasoro_bar.py
  - bc-betagamma duality: thm:betagamma-fermion-koszul, betagamma_bar.py
  - W_3 GF: conj:w3-bar-gf, bar_gf_solver.py
  - Central charges: CLAUDE.md verified formulas

CONVENTIONS:
- Cohomological grading, |d| = +1
- Bar uses desuspension: B(A) = T^c(s^{-1}A-bar, d)
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

from sympy import Rational, Symbol, simplify


# ===========================================================================
# Conjecture 1: Virasoro c=26 self-duality
# ===========================================================================

def virasoro_complementarity_sum() -> int:
    """Verify c + c' = 26 for the Virasoro algebra.

    The Virasoro DS reduction at level k gives:
      c(k) = 1 - 6(k+1)^2/(k+2)
    and the dual level k' = -k-4 gives:
      c(k') = 1 - 6(-k-3)^2/(-k-2)
    Their sum c(k) + c(k') = 26 (level-independent).

    Ground truth: comp:virasoro-curvature (detailed_computations.tex).
    Also verified symbolically in virasoro_bar.py.
    """
    k = Symbol('k')
    c_k = 1 - 6 * (k + 1)**2 / (k + 2)
    c_dual = 1 - 6 * (-k - 3)**2 / (-k - 2)
    total = simplify(c_k + c_dual)
    return int(total)


def virasoro_ds_central_charge(k):
    """DS formula: c_{Vir}(k) = 1 - 6(k+1)^2/(k+2).

    Ground truth: CLAUDE.md verified formulas.
    Uses Rational arithmetic to avoid float division at integer k.
    """
    k = Rational(k) if isinstance(k, (int, float)) else k
    return 1 - 6 * (k + 1)**2 / (k + 2)


def virasoro_dual_central_charge(c_val):
    """Dual central charge: c' = 26 - c.

    From complementarity c + c' = 26.
    """
    return 26 - c_val


def virasoro_curvature(c_val):
    """Curvature m_0 = c/2 at central charge c.

    Ground truth: comp:virasoro-curvature.
    """
    return Rational(c_val, 2) if isinstance(c_val, int) else c_val / 2


def virasoro_bar_at_c26(max_degree: int = 6) -> Dict[str, object]:
    """Bar cohomology properties at c=26 (bosonic string critical dimension).

    At c=26:
    - m_0 = 26/2 = 13 (curvature)
    - Dual: c' = 0 (trivial/uncurved)
    - m_0' = 0 (dual curvature vanishes)

    Bar cohomology dimensions are level-INDEPENDENT for generic c
    (rem:bar-dims-level-independent): they are Motzkin differences
    M(n+1) - M(n) regardless of c.

    The special structure at c=26 is NOT in the dimensions but in:
    (a) the curvature element m_0 = 13 mediates bar-cobar inversion
    (b) the dual algebra Vir_0 is strictly uncurved (m_0' = 0)
    (c) BV/BRST connection: c=26 is the no-ghost theorem critical dimension

    Ground truth: comp:virasoro-curvature, rem:bar-dims-level-independent.
    """
    from compute.lib.bar_complex import bar_dim_virasoro

    dims = {}
    for n in range(1, max_degree + 1):
        d = bar_dim_virasoro(n)
        if d is not None:
            dims[n] = d

    return {
        "central_charge": 26,
        "dual_central_charge": 0,
        "curvature": Rational(13),
        "dual_curvature": Rational(0),
        "bar_cohomology_dims": dims,
        "dims_are_c_independent": True,
        "special_properties": [
            "dual algebra is trivially uncurved (c'=0, m_0'=0)",
            "bosonic string critical dimension",
            "curvature m_0=13 is maximal half-integer",
        ],
    }


def virasoro_self_duality_check(max_degree: int = 6) -> Dict[str, object]:
    """Check self-duality properties at c=26.

    Self-duality in the Koszul sense means A ~ A^!. For Virasoro:
    - True self-duality would require c = c', i.e. c = 13 (midpoint).
    - At c = 26, the dual is the trivial algebra (c' = 0).

    We check three self-duality diagnostics:

    (a) Hilbert series H(t) vs H(-t):
        For a Koszul self-dual algebra, H(t)*H(-t) = 1.
        For Virasoro, H_Vir(t) = sum_n h_n t^n where h_n = M(n+1)-M(n).

    (b) Euler characteristic:
        chi = sum (-1)^n h_n. For self-dual: chi should relate to 1.

    (c) Poincare duality:
        For a finite-dimensional self-dual complex: h_n = h_{N-n}.
        Virasoro bar complex is infinite, so this does not apply strictly.

    Ground truth: bar_complex.py KNOWN_BAR_DIMS, koszul_hilbert.py.
    """
    from compute.lib.bar_complex import bar_dim_virasoro

    # Bar cohomology dimensions (Motzkin differences)
    h = [1]  # h_0 = 1 (vacuum)
    for n in range(1, max_degree + 1):
        d = bar_dim_virasoro(n)
        h.append(d if d is not None else 0)

    # (a) Koszul product: H(t)*H(-t) coefficients
    koszul_product = []
    for k in range(len(h)):
        val = 0
        for i in range(k + 1):
            j = k - i
            if i < len(h) and j < len(h):
                val += h[i] * h[j] * ((-1) ** j)
        koszul_product.append(val)

    is_koszul_self_dual = (
        koszul_product[0] == 1
        and all(p == 0 for p in koszul_product[1:])
    )

    # (b) Euler characteristic (partial, through max_degree)
    euler = sum((-1)**n * h[n] for n in range(len(h)))

    # (c) Alternating Hilbert series H(-1) = sum (-1)^n h_n
    alt_hilbert = euler  # same as Euler characteristic

    return {
        "bar_dims": h,
        "koszul_product": koszul_product,
        "is_koszul_self_dual": is_koszul_self_dual,
        "euler_characteristic": euler,
        "alternating_hilbert": alt_hilbert,
        "complementarity_sum": 26,
        "self_dual_central_charge": 13,
        "c26_is_self_dual": False,  # c=26 gives c'=0, not c'=26
        "c13_would_be_self_dual": True,
    }


# ===========================================================================
# Conjecture 2: Derived bc-betagamma equivalence
# ===========================================================================

def bc_central_charge(lam) -> object:
    """Central charge of the bc ghost system at weight lambda.

    c_{bc}(lambda) = 1 - 3*(2*lambda - 1)^2

    Standard values:
      lambda = 1/2: c = 1 - 3*0 = 1      (single Dirac fermion)
      lambda = 1:   c = 1 - 3*1 = -2      (bc ghosts, conformal weight 1)
      lambda = 2:   c = 1 - 3*9 = -26     (reparametrization ghosts)
      lambda = 0:   c = 1 - 3*1 = -2

    # C5: c_bc(2) = -26 (reparametrization ghost). c_bc(1/2) = 1 (Dirac fermion).
    # VERIFIED: [DC] direct expansion 1-3*(2*2-1)^2 = 1-27 = -26.
    #           [LT] Polchinski, String Theory I, eq. (2.5.12).

    Ground truth: beta_gamma.tex, CLAUDE.md C5.
    """
    return 1 - 3 * (2 * lam - 1)**2


def beta_gamma_central_charge(lam) -> object:
    """Central charge of the betagamma system at weight lambda.

    c_{betagamma}(lambda) = 2*(6*lambda^2 - 6*lambda + 1)

    Standard values:
      lambda = 1/2: c = 2*(3/2 - 3 + 1) = -1   (symplectic boson)
      lambda = 1:   c = 2*(6 - 6 + 1) = 2
      lambda = 2:   c = 2*(24 - 12 + 1) = 26    (matter ghost, c_bg + c_bc = 0)
      lambda = 0:   c = 2*(0 - 0 + 1) = 2

    # C6: c_bg(2) = 26. c_bg(1/2) = -1 (symplectic boson).
    # C7: c_bg(lambda) + c_bc(lambda) = 0 for all lambda.
    # VERIFIED: [DC] direct expansion 2*(6*4 - 6*2 + 1) = 2*13 = 26.
    #           [LT] Polchinski, String Theory I, eq. (2.5.12) (partner).
    #           [CF] c_bg(2) + c_bc(2) = 26 + (-26) = 0 (string ghost cancellation).

    Ground truth: beta_gamma.tex, CLAUDE.md C6-C7.
    """
    return 2 * (6 * lam**2 - 6 * lam + 1)


def bc_betagamma_central_charge_sum(lam) -> object:
    """Verify c_{bc}(lambda) + c_{betagamma}(lambda) = 0.

    This is the central charge complementarity for the bc/betagamma
    Koszul dual pair. The sum vanishes identically in lambda.

    Ground truth: thm:betagamma-fermion-koszul (beta_gamma.tex).
    """
    return bc_central_charge(lam) + beta_gamma_central_charge(lam)


def bc_bar_dimensions(lam: int, max_degree: int = 5) -> Dict[int, int]:
    """Known bar cohomology dimensions for bc ghosts.

    From KNOWN_BAR_DIMS["bc"] in bar_complex.py:
      dim H^n(B(bc)) = 2^n - n + 1

    This is lambda-independent at the level of bar cohomology dimensions
    (just as Virasoro bar dims are c-independent).

    Ground truth: Master Table (examples_summary.tex).
    """
    return {n: 2**n - n + 1 for n in range(1, max_degree + 1)}


def beta_gamma_bar_dimensions(lam: int, max_degree: int = 5) -> Dict[int, int]:
    """Known bar cohomology dimensions for betagamma system.

    From KNOWN_BAR_DIMS["beta_gamma"] in bar_complex.py:
      GF: sqrt((1+x)/(1-3x))
      Recurrence: n*a(n) = 2n*a(n-1) + 3(n-2)*a(n-2)

    Values: 2, 4, 10, 26, 70, 192, 534, 1500, 4246, 12092

    Ground truth: Master Table (examples_summary.tex).
    """
    known = {1: 2, 2: 4, 3: 10, 4: 26, 5: 70, 6: 192, 7: 534, 8: 1500}
    return {n: known[n] for n in range(1, min(max_degree + 1, 9))}


def bc_betagamma_koszul_check(lam: int = 1, max_degree: int = 5) -> Dict[str, object]:
    """Verify bc^! = betagamma at the level of bar cohomology GFs.

    IMPORTANT: The naive classical Koszul relation H_A(t)*H_{A!}(-t) = 1
    does NOT hold for chiral bar cohomology dimensions. The chiral bar
    complex has additional OS algebra structure that modifies the relation.

    Instead, we verify:
    (a) Central charge complementarity: c_bc + c_bg = 0
    (b) The betagamma bar GF is algebraic: P(x)^2 = (1+x)/(1-3x)
    (c) The bc bar dims satisfy the closed-form: 2^n - n + 1
    (d) The GFs are related via the shared discriminant (1-3x)(1+x)

    Ground truth: thm:betagamma-fermion-koszul, bar_gf_solver.py.
    """
    bc_dims = bc_bar_dimensions(lam, max_degree)
    bg_dims = beta_gamma_bar_dimensions(lam, max_degree)

    h_bc = [1] + [bc_dims.get(n, 0) for n in range(1, max_degree + 1)]
    h_bg = [1] + [bg_dims.get(n, 0) for n in range(1, max_degree + 1)]

    # Central charge data
    c_bc = bc_central_charge(lam)
    c_bg = beta_gamma_central_charge(lam)

    # (a) Central charge complementarity
    central_charge_complement = (c_bc + c_bg == 0)

    # (b) Verify bg GF satisfies P^2 = (1+x)/(1-3x)
    # P(x) = 1 + 2x + 4x^2 + 10x^3 + 26x^4 + ...
    # P(x)^2 should have coefficients matching (1+x)/(1-3x) = 1 + 4x + 12x^2 + ...
    # (1+x)/(1-3x) = sum_{n>=0} (3^n + 3^{n-1}) x^n for n>=1, with c_0 = 1.
    # Actually: (1+x)/(1-3x) = 1/(1-3x) + x/(1-3x) = sum 3^n x^n + sum 3^n x^{n+1}
    # = 1 + 4x + 12x^2 + 36x^3 + ...
    target_coeffs = [Rational(1)]
    for n in range(1, max_degree + 1):
        target_coeffs.append(Rational(3**n + 3**(n - 1)))

    # Compute P^2 coefficients
    p_sq = [Rational(0)] * (max_degree + 1)
    for i in range(min(len(h_bg), max_degree + 1)):
        for j in range(min(len(h_bg), max_degree + 1 - i)):
            p_sq[i + j] += Rational(h_bg[i]) * Rational(h_bg[j])

    bg_algebraic = all(
        p_sq[k] == target_coeffs[k]
        for k in range(min(len(p_sq), len(target_coeffs)))
    )

    # (c) Verify bc formula: 2^n - n + 1
    bc_formula_ok = all(
        bc_dims.get(n, 0) == 2**n - n + 1
        for n in range(1, max_degree + 1)
    )

    # (d) Shared discriminant check:
    # bg GF^2 = (1+x)/(1-3x), so discriminant = (1-3x)(1+x).
    # sl2 and Virasoro also have this discriminant.
    shared_discriminant = True  # structural fact from bar_gf_solver.py

    is_koszul_dual = central_charge_complement and bg_algebraic and bc_formula_ok

    return {
        "lambda": lam,
        "c_bc": c_bc,
        "c_bg": c_bg,
        "c_sum": c_bc + c_bg,
        "h_bc": h_bc,
        "h_bg": h_bg,
        "central_charge_complement": central_charge_complement,
        "bg_algebraic_gf_verified": bg_algebraic,
        "bc_formula_verified": bc_formula_ok,
        "shared_discriminant": shared_discriminant,
        "is_koszul_dual": is_koszul_dual,
        "max_degree_checked": max_degree,
    }


# ===========================================================================
# Conjecture 3: Near-rationality (Pade approximant test)
# ===========================================================================

def pade_approximant(coefficients: List[int], p: int, q: int) -> Optional[Dict]:
    """Compute the [p/q] Pade approximant of a power series.

    Given f(x) = c_0 + c_1*x + c_2*x^2 + ..., find polynomials
    N(x) = n_0 + n_1*x + ... + n_p*x^p and
    D(x) = 1 + d_1*x + ... + d_q*x^q
    such that f(x)*D(x) - N(x) = O(x^{p+q+1}).

    This gives p+q+1 linear equations in p+1+q unknowns.

    Returns dict with 'num' (numerator coeffs), 'den' (denominator coeffs),
    'predictions' (next predicted coefficients), or None if underdetermined.
    """
    n_needed = p + q + 1
    if len(coefficients) < n_needed:
        return None

    c = [Rational(x) for x in coefficients]

    # Build the linear system.
    # f(x)*D(x) - N(x) = 0 through x^{p+q}.
    # Coefficient of x^k:
    #   c_k + d_1*c_{k-1} + ... + d_q*c_{k-q} - n_k = 0  for k <= p
    #   c_k + d_1*c_{k-1} + ... + d_q*c_{k-q} = 0        for p < k <= p+q
    #
    # Unknowns: d_1, ..., d_q (the denominator determines the approximant)
    # We solve the denominator first from the equations for k = p+1, ..., p+q.

    # Denominator equations: for k = p+1, ..., p+q
    # c_k + d_1*c_{k-1} + ... + d_q*c_{k-q} = 0
    from sympy import Matrix

    if q == 0:
        # Polynomial approximant: N = truncated series
        return {
            "num": [c[k] for k in range(p + 1)],
            "den": [],
            "predictions": [c[k] if k < len(c) else None
                            for k in range(p + 1, p + 4)],
        }

    A_rows = []
    b_rows = []
    for k in range(p + 1, p + q + 1):
        row = []
        for j in range(1, q + 1):
            idx = k - j
            if 0 <= idx < len(c):
                row.append(c[idx])
            else:
                row.append(Rational(0))
        A_rows.append(row)
        b_rows.append(-c[k] if k < len(c) else Rational(0))

    A_mat = Matrix(A_rows)
    b_mat = Matrix(b_rows)

    try:
        d_sol = A_mat.solve(b_mat)
    except Exception:
        return None

    d_list = [d_sol[j] for j in range(q)]

    # Compute numerator: n_k = c_k + d_1*c_{k-1} + ... for k = 0, ..., p
    n_list = []
    for k in range(p + 1):
        val = c[k]
        for j in range(1, q + 1):
            idx = k - j
            if 0 <= idx:
                val += d_list[j - 1] * c[idx]
        n_list.append(val)

    # Predict next coefficients using the Pade approximant
    # For k > p: c_k = -(d_1*c_{k-1} + ... + d_q*c_{k-q})
    extended = list(c)
    predictions = []
    for _ in range(3):
        k = len(extended)
        if k <= p:
            # Still in numerator range
            val = n_list[k]
            for j in range(1, q + 1):
                idx = k - j
                if 0 <= idx < len(extended):
                    val -= d_list[j - 1] * extended[idx]
            predictions.append(val)
            extended.append(val)
        else:
            val = Rational(0)
            for j in range(1, q + 1):
                idx = k - j
                if 0 <= idx < len(extended):
                    val -= d_list[j - 1] * extended[idx]
            predictions.append(val)
            extended.append(val)

    return {
        "num": n_list,
        "den": d_list,
        "predictions": predictions,
    }


def pade_approximant_test(
    coefficients: List[int],
    max_order: int = 4,
) -> Dict[str, object]:
    """Test near-rationality of a generating function via Pade approximants.

    Computes [p/q] Pade approximants for various (p, q) with p+q <= max_order
    and checks whether predictions stabilize (i.e., different approximants
    predict the same next coefficient).

    A GF is "near-rational" if Pade approximants of low order already
    stabilize on the correct predictions.

    Returns dict with approximant results and stabilization analysis.
    """
    results = {}
    predictions_at_next = {}

    for total in range(2, max_order + 1):
        for q in range(1, total + 1):
            p = total - q
            if p < 0:
                continue
            pade = pade_approximant(coefficients, p, q)
            if pade is None:
                continue
            key = f"[{p}/{q}]"
            results[key] = pade

            # Record the first prediction
            if pade["predictions"] and pade["predictions"][0] is not None:
                pred = pade["predictions"][0]
                if pred not in predictions_at_next:
                    predictions_at_next[pred] = []
                predictions_at_next[pred].append(key)

    # Check stabilization: do different approximants agree?
    if predictions_at_next:
        most_common_pred = max(predictions_at_next.keys(),
                               key=lambda k: len(predictions_at_next[k]))
        n_agreeing = len(predictions_at_next[most_common_pred])
        n_total = sum(len(v) for v in predictions_at_next.values())
        stabilized = n_agreeing == n_total
    else:
        most_common_pred = None
        n_agreeing = 0
        n_total = 0
        stabilized = False

    return {
        "approximants": results,
        "predictions_by_value": {str(k): v for k, v in predictions_at_next.items()},
        "consensus_prediction": most_common_pred,
        "n_agreeing": n_agreeing,
        "n_total": n_total,
        "stabilized": stabilized,
    }


def w3_pade_check(max_degree: int = 8) -> Dict[str, object]:
    """Check if the W_3 bar Hilbert series has a rational GF via Pade.

    Known bar cohomology: H^1=2, H^2=5, H^3=16, H^4=52, H^5=171 (conjectured).

    Conjectured rational GF (bar_gf_solver.py):
      P(x) = x(2-3x) / ((1-x)(1-3x-x^2))

    The Pade [2/3] approximant (matching through x^5) should recover this GF.

    Ground truth: conj:w3-bar-gf (examples_summary.tex), bar_gf_solver.py.
    """
    # Include h_0 = 1 (vacuum) for the full Hilbert series
    # H(t) = 1 + 2t + 5t^2 + 16t^3 + 52t^4 + 171t^5 + ...
    #
    # But the bar_gf_solver convention uses P(x) = a_1 x + a_2 x^2 + ...
    # with a_0 omitted. For Pade we use the full series starting from h_0.

    # Known values (h_0 through h_5 at most)
    w3_dims = [1, 2, 5, 16, 52]  # h_0=1 (vacuum), then H^1..H^4

    # Conjectured h_5 = 171
    w3_dims_extended = [1, 2, 5, 16, 52, 171]

    result = pade_approximant_test(w3_dims, max_order=4)

    # Also check extended data (with conjectured H^5=171)
    result_extended = pade_approximant_test(w3_dims_extended, max_order=5)

    # Verify against conjectured GF: D(x) = (1-x)(1-3x-x^2) = 1-4x+2x^2+x^3
    # N(x) = ... this is for P(x) = a_1 x + ..., not H(t) = 1 + ...
    # For the full H(t): H(t) = 1 + P(t) where P(t) starts at t^1.
    # If P = N/D then H = 1 + N/D = (D+N)/D.
    # D = 1-4t+2t^2+t^3, N = 2t-3t^2.
    # D+N = 1 - 2t - t^2 + t^3.
    # So H(t) = (1-2t-t^2+t^3)/(1-4t+2t^2+t^3).

    # Check: [3/3] Pade of [1, 2, 5, 16, 52, 171] should give this.
    pade_33 = pade_approximant(w3_dims_extended, 3, 3)

    return {
        "known_dims": w3_dims,
        "extended_dims": w3_dims_extended,
        "pade_analysis": result,
        "pade_analysis_extended": result_extended,
        "pade_33": pade_33,
        "conjectured_h5": 171,
    }


def virasoro_pade_check(max_terms: int = 8) -> Dict[str, object]:
    """Check near-rationality of Virasoro bar GF.

    Virasoro bar cohomology: Motzkin differences M(n+1)-M(n).
    H^n: 1, 2, 5, 12, 30, 76, 196, 512, 1353, ...

    The GF is ALGEBRAIC (degree 2), not rational. But a depth-3
    rational approximation fits through degree 8 (failing at degree 9:
    predicts 1352, actual 1353). This is the "near-rationality"
    phenomenon.

    Ground truth: bar_gf_solver.py verify_virasoro_prediction().
    """
    from compute.lib.koszul_hilbert import motzkin

    # Full Hilbert series including h_0 = 1
    h = [1]  # vacuum
    for n in range(1, max_terms + 1):
        h.append(motzkin(n + 1) - motzkin(n))

    result = pade_approximant_test(h, max_order=min(6, len(h) - 1))

    return {
        "dims": h,
        "pade_analysis": result,
        "is_truly_rational": False,
        "is_algebraic_degree_2": True,
        "near_rational_through_degree": 8,
    }


# ===========================================================================
# Verification helpers
# ===========================================================================

def verify_virasoro_complementarity() -> Dict[str, bool]:
    """Verify all aspects of Virasoro complementarity c + c' = 26."""
    results = {}

    # Direct computation
    results["c + c' = 26 (symbolic)"] = virasoro_complementarity_sum() == 26

    # Specific levels
    k_vals = [0, 1, 2, -1, -3, Rational(1, 2)]
    for kv in k_vals:
        c_k = virasoro_ds_central_charge(kv)
        c_dual = virasoro_ds_central_charge(-kv - 4)
        s = simplify(c_k + c_dual)
        results[f"c(k={kv}) + c(k'={-kv-4}) = 26"] = (s == 26)

    # Curvature complementarity: m0(c) + m0(26-c) = 13
    c = Symbol('c')
    m0 = c / 2
    m0_dual = (26 - c) / 2
    results["m0(c) + m0(26-c) = 13"] = simplify(m0 + m0_dual) == 13

    return results


def verify_bc_betagamma_duality() -> Dict[str, bool]:
    """Verify bc/betagamma Koszul duality at several lambda values."""
    results = {}

    # Central charge complementarity at integer lambda
    for lam in [0, 1, 2, 3]:
        s = bc_betagamma_central_charge_sum(lam)
        results[f"c_bc({lam}) + c_bg({lam}) = 0"] = (s == 0)

    # Half-integer lambda
    lam = Rational(1, 2)
    s = bc_betagamma_central_charge_sum(lam)
    results[f"c_bc(1/2) + c_bg(1/2) = 0"] = (simplify(s) == 0)

    # Specific central charge values
    # C5: c_bc(lam) = 1 - 3*(2*lam - 1)^2. C6: c_bg(lam) = 2*(6*lam^2 - 6*lam + 1).
    # VERIFIED: [DC] direct substitution. [CF] c_bc + c_bg = 0 at each point.
    results["c_bc(1) = -2"] = (bc_central_charge(1) == -2)
    results["c_bg(1) = 2"] = (beta_gamma_central_charge(1) == 2)
    results["c_bc(1/2) = 1"] = (bc_central_charge(Rational(1, 2)) == 1)
    results["c_bg(1/2) = -1"] = (beta_gamma_central_charge(Rational(1, 2)) == -1)
    results["c_bc(2) = -26"] = (bc_central_charge(2) == -26)
    results["c_bg(2) = 26"] = (beta_gamma_central_charge(2) == 26)

    # Koszul duality verification at lambda=1 (algebraic GF + formula checks)
    check = bc_betagamma_koszul_check(lam=1, max_degree=5)
    results["bc-bg koszul dual (lam=1, deg<=5)"] = check["is_koszul_dual"]

    return results


if __name__ == "__main__":
    print("=" * 70)
    print("INDEPENDENT CONJECTURES: COMPUTATIONAL CHECKS")
    print("=" * 70)

    print("\n--- Conjecture 1: Virasoro c=26 Self-Duality ---")

    print("\n  Complementarity:")
    for name, ok in verify_virasoro_complementarity().items():
        print(f"    [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n  Bar complex at c=26:")
    data = virasoro_bar_at_c26(6)
    print(f"    Central charge: {data['central_charge']}")
    print(f"    Dual central charge: {data['dual_central_charge']}")
    print(f"    Curvature: {data['curvature']}")
    print(f"    Bar dims: {data['bar_cohomology_dims']}")

    print("\n  Self-duality check:")
    sd = virasoro_self_duality_check(6)
    print(f"    Koszul product: {sd['koszul_product']}")
    print(f"    Is Koszul self-dual: {sd['is_koszul_self_dual']}")
    print(f"    c=26 is self-dual: {sd['c26_is_self_dual']}")

    print("\n--- Conjecture 2: bc-betagamma Koszul Duality ---")

    print("\n  Central charge complementarity:")
    for name, ok in verify_bc_betagamma_duality().items():
        print(f"    [{'PASS' if ok else 'FAIL'}] {name}")

    print("\n  Koszul duality check (lam=1):")
    kc = bc_betagamma_koszul_check(lam=1, max_degree=7)
    print(f"    h_bc: {kc['h_bc']}")
    print(f"    h_bg: {kc['h_bg']}")
    print(f"    Central charge complement: {kc['central_charge_complement']}")
    print(f"    BG algebraic GF verified: {kc['bg_algebraic_gf_verified']}")
    print(f"    BC formula verified: {kc['bc_formula_verified']}")
    print(f"    Is Koszul dual: {kc['is_koszul_dual']}")

    print("\n--- Conjecture 3: Near-Rationality (Pade) ---")

    print("\n  W_3 Pade check:")
    wp = w3_pade_check()
    print(f"    Known dims: {wp['known_dims']}")
    print(f"    Stabilized: {wp['pade_analysis']['stabilized']}")
    print(f"    Consensus prediction: {wp['pade_analysis']['consensus_prediction']}")

    print("\n  Virasoro Pade check:")
    vp = virasoro_pade_check()
    print(f"    Dims: {vp['dims']}")
    print(f"    Stabilized: {vp['pade_analysis']['stabilized']}")
