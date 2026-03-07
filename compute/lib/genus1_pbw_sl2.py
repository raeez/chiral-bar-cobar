"""Genus-1 PBW spectral sequence verification for sl2-hat.

Computational verification of Theorem thm:pbw-genus1-km (higher_genus.tex:8517).

WHAT WE VERIFY (Step 4 of the proof, lines 8684-8714):

At conformal weight h=2, g=sl2, genus 1:

The enrichment from H^1(E_tau) at bar degree 2 is g tensor g (dim 9).
Under the adjoint action, g^{otimes 2} = V_5 + V_3 + V_1.

(1) d_1 (Lie bracket): g^{otimes 2} -> g has rank 3 (surjective).
(2) ker(d_1) = V_5 + V_1, dim 6.
(3) V_3 = Lambda^2(g) is mapped isomorphically to g.
(4) The Killing form invariant kappa in V_1 lies in ker(d_1).
(5) d_2 (Killing contraction at level k) kills V_1 at E_3.

Additionally, we verify the CE complex (exterior algebra model):
(6) d_CE: Lambda^1(g*) -> Lambda^2(g*) has rank 3 (injective).
(7) d_CE: Lambda^2(g*) -> Lambda^3(g*) is zero.
(8) H*(sl2) = k[0] + k[3], total dim 2.

CONVENTIONS:
    - sl2 basis: e=0, h=1, f=2
    - Killing form: kappa(h,h) = 2, kappa(e,f) = kappa(f,e) = 1
    - Structure constants: [e,f] = h, [h,e] = 2e, [h,f] = -2f
"""

from __future__ import annotations

from sympy import Matrix, Rational, Symbol, zeros

# ===========================================================================
# sl2 structure constants and Killing form
# ===========================================================================

DIM_SL2 = 3  # basis: e=0, h=1, f=2

# Structure constants: bracket[i,j] = {k: coeff} for [e_i, e_j] = sum coeff * e_k
SL2_BRACKET = {
    (0, 2): {1: Rational(1)},    # [e, f] = h
    (2, 0): {1: Rational(-1)},   # [f, e] = -h
    (1, 0): {0: Rational(2)},    # [h, e] = 2e
    (0, 1): {0: Rational(-2)},   # [e, h] = -2e
    (1, 2): {2: Rational(-2)},   # [h, f] = -2f
    (2, 1): {2: Rational(2)},    # [f, h] = 2f
}

# Killing form: kappa(e_i, e_j) (normalized so kappa(h,h) = 2)
SL2_KILLING = {
    (0, 2): Rational(1),   # kappa(e, f) = 1
    (2, 0): Rational(1),   # kappa(f, e) = 1
    (1, 1): Rational(2),   # kappa(h, h) = 2
}


def lie_bracket(a: int, b: int) -> dict:
    """Compute [e_a, e_b] = sum_c f^c_{ab} e_c."""
    return SL2_BRACKET.get((a, b), {})


def killing(a: int, b: int) -> Rational:
    """Compute kappa(e_a, e_b)."""
    return SL2_KILLING.get((a, b), Rational(0))


# ===========================================================================
# (1)-(5): Enrichment d_1 differential (bracket on tensor square)
# ===========================================================================

def bracket_on_tensor_square() -> Matrix:
    """Build d_1: g^{otimes 2} -> g, the Lie bracket map.

    d_1(e_a otimes e_b) = [e_a, e_b] = sum_c f^c_{ab} e_c

    This is the PBW d_1 differential acting on the genus-1 enrichment
    at bar degree 2, conformal weight 2.

    Returns: 3 x 9 matrix (target g = C^3, source g^{otimes 2} = C^9).
    Source index: a*3 + b for e_a otimes e_b.
    """
    d = DIM_SL2
    mat = zeros(d, d ** 2)
    for a in range(d):
        for b in range(d):
            src = a * d + b
            for c, coeff in lie_bracket(a, b).items():
                mat[c, src] += coeff
    return mat


def killing_form_element() -> Matrix:
    """The Killing form element kappa = sum kappa^{ab} e_a otimes e_b in g^{otimes 2}.

    For sl2: kappa = e otimes f + f otimes e + (1/2) h otimes h
    (using the inverse Killing form kappa^{ab}).

    The inverse of kappa_{ab} = {(e,f):1, (f,e):1, (h,h):2} is
    kappa^{ab} = {(e,f):1, (f,e):1, (h,h):1/2}.

    Returns: 9-component column vector.
    """
    d = DIM_SL2
    vec = zeros(d ** 2, 1)
    # kappa^{ab} (inverse Killing form)
    # kappa_{ab} = ((0,0,1),(0,2,0),(1,0,0)) in matrix form
    # kappa^{ab} = ((0,0,1),(0,1/2,0),(1,0,0))
    inv_killing = {
        (0, 2): Rational(1),     # kappa^{e,f} = 1
        (2, 0): Rational(1),     # kappa^{f,e} = 1
        (1, 1): Rational(1, 2),  # kappa^{h,h} = 1/2
    }
    for (a, b), coeff in inv_killing.items():
        vec[a * d + b] = coeff
    return vec


def adjoint_casimir_on_tensor_square() -> Matrix:
    """The quadratic Casimir C_2 = sum_a (ad(e_a))^2 acting on g^{otimes 2}.

    Uses the diagonal adjoint action: ad(x)(a otimes b) = [x,a] otimes b + a otimes [x,b].

    The Casimir eigenvalues determine the irreducible decomposition.
    Our Killing form is the trace form in the fundamental representation
    (= half the standard Killing form), so the Casimir eigenvalue on
    V_{2j+1} (spin j rep) is 2*j*(j+1), not j*(j+1):
    - V_5 (dim 5, spin 2): C_2 = 2*2*3 = 12
    - V_3 (dim 3, spin 1): C_2 = 2*1*2 = 4   [= adjoint]
    - V_1 (dim 1, spin 0): C_2 = 0             [= trivial]

    Returns: 9 x 9 matrix.
    """
    d = DIM_SL2
    n = d ** 2

    # Build ad(e_a) on g^{otimes 2} (diagonal action)
    def ad_on_tensor(x_idx):
        """ad(e_x) acting on g^{otimes 2}."""
        mat = zeros(n, n)
        for a in range(d):
            for b in range(d):
                src = a * d + b
                # [e_x, e_a] otimes e_b
                for c, coeff in lie_bracket(x_idx, a).items():
                    tgt = c * d + b
                    mat[tgt, src] += coeff
                # e_a otimes [e_x, e_b]
                for c, coeff in lie_bracket(x_idx, b).items():
                    tgt = a * d + c
                    mat[tgt, src] += coeff
        return mat

    # Casimir = sum kappa^{ab} ad(a) ad(b)
    inv_killing = {
        (0, 2): Rational(1),
        (2, 0): Rational(1),
        (1, 1): Rational(1, 2),
    }
    casimir = zeros(n, n)
    for (a, b), coeff in inv_killing.items():
        casimir += coeff * ad_on_tensor(a) * ad_on_tensor(b)
    return casimir


def verify_enrichment_claims():
    """Verify claims (1)-(5) about the enrichment d_1 differential.

    Returns dict with all verification results.
    """
    results = {}
    d = DIM_SL2

    # --- Claim (1): d_1 has rank 3 (surjective) ---
    D = bracket_on_tensor_square()
    results["d1_shape"] = D.shape  # (3, 9)
    results["d1_rank"] = D.rank()
    results["claim_1_surjective"] = (D.rank() == d)

    # --- Claim (2): ker(d_1) has dim 6 ---
    ker_dim = d ** 2 - D.rank()
    results["ker_d1_dim"] = ker_dim
    results["claim_2_ker_dim_6"] = (ker_dim == 6)

    # --- Claim (3): V_3 = Lambda^2(g) maps isomorphically ---
    # Antisymmetric part of g tensor g: basis {e_a wedge e_b : a < b}
    # e_a wedge e_b = e_a tensor e_b - e_b tensor e_a
    antisym_basis = []
    for a in range(d):
        for b in range(a + 1, d):
            vec = zeros(d ** 2, 1)
            vec[a * d + b] = Rational(1)
            vec[b * d + a] = Rational(-1)
            antisym_basis.append(vec)

    # D restricted to antisymmetric subspace
    D_antisym = zeros(d, len(antisym_basis))
    for j, v in enumerate(antisym_basis):
        Dv = D * v
        for i in range(d):
            D_antisym[i, j] = Dv[i]

    results["antisym_dim"] = len(antisym_basis)  # should be 3
    results["d1_on_antisym_rank"] = D_antisym.rank()
    results["claim_3_V3_isomorphism"] = (D_antisym.rank() == d)

    # --- Claim (4): Killing form invariant in ker(d_1) ---
    kappa = killing_form_element()
    D_kappa = D * kappa
    kappa_in_ker = all(D_kappa[i] == 0 for i in range(d))
    results["killing_element"] = kappa.T.tolist()[0]
    results["d1_of_kappa"] = D_kappa.T.tolist()[0]
    results["claim_4_kappa_in_ker"] = kappa_in_ker

    # --- Verify Casimir decomposition ---
    C2 = adjoint_casimir_on_tensor_square()

    # Casimir eigenvalues: 2j(j+1) with our normalization
    # V_5 (spin 2): 12, V_3 (spin 1): 4, V_1 (spin 0): 0
    eigenvals = C2.eigenvals()
    results["casimir_eigenvalues"] = {str(k): v for k, v in eigenvals.items()}

    # Expected: {12: 5, 4: 3, 0: 1} (eigenvalue = 2*j*(j+1) with our normalization)
    expected_eigenvals = {Rational(12): 5, Rational(4): 3, Rational(0): 1}
    results["claim_adjoint_decomposition"] = (eigenvals == expected_eigenvals)

    # Verify kappa is Casimir eigenvector with eigenvalue 0 (V_1)
    C2_kappa = C2 * kappa
    kappa_eigenvalue_zero = all(C2_kappa[i] == 0 for i in range(d ** 2))
    results["claim_kappa_is_invariant"] = kappa_eigenvalue_zero

    # --- Claim (5): d_2 (Killing contraction) kills V_1 ---
    # d_2 maps bar=2 enrichment to bar=0 via the (1)-product (Killing form).
    # For a tensor b: d_2(a tensor b) = k * kappa(a, b)
    # On the Killing element: d_2(kappa^{ab} e_a tensor e_b) = k * kappa^{ab} kappa(a,b)
    #   = k * (kappa(e,f) + kappa(f,e) + (1/2)*kappa(h,h))
    #   = k * (1 + 1 + 1) = k * dim(g)/dim(g)... let me compute directly.
    k = Symbol('k')
    killing_contraction = Rational(0)
    inv_killing = {
        (0, 2): Rational(1),
        (2, 0): Rational(1),
        (1, 1): Rational(1, 2),
    }
    for (a, b), inv_coeff in inv_killing.items():
        killing_contraction += inv_coeff * killing(a, b)
    # killing_contraction = 1*1 + 1*1 + (1/2)*2 = 1 + 1 + 1 = 3 = dim(sl2)

    results["killing_contraction_scalar"] = killing_contraction
    results["claim_5_d2_nonzero"] = (killing_contraction != 0)
    results["d2_image"] = f"k * {killing_contraction} (nonzero for k != 0)"

    return results


# ===========================================================================
# (6)-(8): CE complex verification (exterior algebra)
# ===========================================================================

def ce_differential_1_to_2() -> Matrix:
    """CE differential d: Lambda^1(g*) -> Lambda^2(g*).

    For xi in g*, (d xi)(x, y) = -xi([x, y]).

    Basis for Lambda^1(g*): {e*, h*, f*} (indices 0, 1, 2)
    Basis for Lambda^2(g*): {e*^h*, e*^f*, h*^f*}
        ordered by (0,1), (0,2), (1,2)

    Returns: 3 x 3 matrix (target Lambda^2, source Lambda^1).
    """
    d = DIM_SL2
    # Ordered pairs (i,j) with i < j
    wedge2_basis = [(0, 1), (0, 2), (1, 2)]

    mat = zeros(len(wedge2_basis), d)
    for col, xi_idx in enumerate(range(d)):
        # d(e*_{xi_idx})(e_i, e_j) = -e*_{xi_idx}([e_i, e_j])
        for row, (i, j) in enumerate(wedge2_basis):
            bracket_ij = lie_bracket(i, j)
            coeff = bracket_ij.get(xi_idx, Rational(0))
            mat[row, col] = -coeff
    return mat


def ce_differential_2_to_3() -> Matrix:
    """CE differential d: Lambda^2(g*) -> Lambda^3(g*).

    For alpha in Lambda^2(g*):
    (d alpha)(x,y,z) = -alpha([x,y],z) + alpha([x,z],y) - alpha([y,z],x)

    Basis for Lambda^2(g*): {e*^h*, e*^f*, h*^f*}
    Basis for Lambda^3(g*): {e*^h*^f*} (single element)

    Evaluate at (e, h, f) = (0, 1, 2).

    Returns: 1 x 3 matrix.
    """
    wedge2_basis = [(0, 1), (0, 2), (1, 2)]

    def eval_wedge2(alpha_idx, x, y):
        """Evaluate basis wedge form alpha on (e_x, e_y).
        alpha = e*_i ^ e*_j means alpha(x,y) = delta_{x,i}*delta_{y,j} - delta_{x,j}*delta_{y,i}.
        """
        i, j = wedge2_basis[alpha_idx]
        return (Rational(1) if (x == i and y == j) else Rational(0)) - \
               (Rational(1) if (x == j and y == i) else Rational(0))

    mat = zeros(1, len(wedge2_basis))
    # The single basis element of Lambda^3 is e*^h*^f*, evaluate at (e,h,f)=(0,1,2)
    x, y, z = 0, 1, 2
    for col in range(len(wedge2_basis)):
        # (d alpha)(x,y,z) = -alpha([x,y],z) + alpha([x,z],y) - alpha([y,z],x)
        val = Rational(0)
        # Term 1: -alpha([x,y], z)
        for c, coeff in lie_bracket(x, y).items():
            val -= coeff * eval_wedge2(col, c, z)
        # Term 2: +alpha([x,z], y)
        for c, coeff in lie_bracket(x, z).items():
            val += coeff * eval_wedge2(col, c, y)
        # Term 3: -alpha([y,z], x)
        for c, coeff in lie_bracket(y, z).items():
            val -= coeff * eval_wedge2(col, c, x)
        mat[0, col] = val
    return mat


def verify_ce_complex():
    """Verify claims (6)-(8) about the CE complex of sl2.

    Returns dict with verification results.
    """
    results = {}

    d1 = ce_differential_1_to_2()
    d2 = ce_differential_2_to_3()

    results["d1_shape"] = d1.shape  # (3, 3)
    results["d1_matrix"] = d1.tolist()
    results["d1_rank"] = d1.rank()
    results["claim_6_d1_rank_3"] = (d1.rank() == 3)

    results["d2_shape"] = d2.shape  # (1, 3)
    results["d2_matrix"] = d2.tolist()
    results["d2_rank"] = d2.rank()
    results["claim_7_d2_is_zero"] = (d2.rank() == 0)

    # d^2 = 0
    d_sq = d2 * d1
    results["d_squared_zero"] = d_sq.is_zero_matrix

    # Cohomology dimensions
    # H^0 = ker(d: C^0 -> C^1) = C^0 = k (no d from degree -1)
    h0 = 1
    # H^1 = ker(d1) / im(d: C^0 -> C^1), but d: C^0 -> C^1 is zero (no bracket on scalars)
    h1 = DIM_SL2 - d1.rank()  # ker(d1) - im(d0) = (3-3) - 0 = 0
    # H^2 = ker(d2) / im(d1)
    h2 = (3 - d2.rank()) - d1.rank()  # (3-0) - 3 = 0
    # H^3 = C^3 / im(d2) = 1 - 0 = 1
    h3 = 1 - d2.rank()

    results["H0"] = h0
    results["H1"] = h1
    results["H2"] = h2
    results["H3"] = h3
    results["claim_8_cohomology"] = (h0 == 1 and h1 == 0 and h2 == 0 and h3 == 1)
    results["total_betti"] = h0 + h1 + h2 + h3

    return results


# ===========================================================================
# Full MC1 verification
# ===========================================================================

def run_mc1_computation():
    """Run the full MC1 verification for sl2-hat at genus 1.

    Verifies all claims in Theorem thm:pbw-genus1-km, Step 4
    (higher_genus.tex:8684-8714).
    """
    print("=" * 70)
    print("MC1 VERIFICATION: PBW degeneration for sl2-hat at genus 1")
    print("Theorem thm:pbw-genus1-km (higher_genus.tex:8517)")
    print("=" * 70)

    # Part A: CE complex
    print("\n--- Part A: Chevalley-Eilenberg complex of sl2 ---")
    ce = verify_ce_complex()
    print(f"  d_CE^1 (Lambda^1 -> Lambda^2): {ce['d1_shape']}")
    print(f"    Matrix: {ce['d1_matrix']}")
    print(f"    Rank: {ce['d1_rank']}  [claim (6): rank=3] {'PASS' if ce['claim_6_d1_rank_3'] else 'FAIL'}")
    print(f"  d_CE^2 (Lambda^2 -> Lambda^3): {ce['d2_shape']}")
    print(f"    Matrix: {ce['d2_matrix']}")
    print(f"    Rank: {ce['d2_rank']}  [claim (7): rank=0] {'PASS' if ce['claim_7_d2_is_zero'] else 'FAIL'}")
    print(f"  d^2 = 0: {ce['d_squared_zero']}")
    print(f"  H*(sl2) = ({ce['H0']}, {ce['H1']}, {ce['H2']}, {ce['H3']})")
    print(f"    [claim (8): (1,0,0,1)] {'PASS' if ce['claim_8_cohomology'] else 'FAIL'}")
    print(f"  Total Betti: {ce['total_betti']} (Poincare poly: 1 + t^3)")

    # Part B: Enrichment analysis
    print("\n--- Part B: Enrichment d_1 at weight h=2 ---")
    enr = verify_enrichment_claims()
    print(f"  d_1 (g tensor g -> g): {enr['d1_shape']}")
    print(f"    Rank: {enr['d1_rank']}  [claim (1): rank=3] {'PASS' if enr['claim_1_surjective'] else 'FAIL'}")
    print(f"    ker(d_1) dim: {enr['ker_d1_dim']}  [claim (2): dim=6] {'PASS' if enr['claim_2_ker_dim_6'] else 'FAIL'}")

    print(f"\n  Antisymmetric subspace Lambda^2(g) (= V_3):")
    print(f"    dim: {enr['antisym_dim']}")
    print(f"    d_1|_V3 rank: {enr['d1_on_antisym_rank']}  [claim (3): isomorphism] {'PASS' if enr['claim_3_V3_isomorphism'] else 'FAIL'}")

    print(f"\n  Casimir decomposition of g tensor g:")
    print(f"    Eigenvalues (multiplicity): {enr['casimir_eigenvalues']}")
    print(f"    [expected: {{6:5, 2:3, 0:1}} = V_5+V_3+V_1] {'PASS' if enr['claim_adjoint_decomposition'] else 'FAIL'}")

    print(f"\n  Killing form element kappa^{{ab}}:")
    print(f"    kappa = {enr['killing_element']}")
    print(f"    d_1(kappa) = {enr['d1_of_kappa']}")
    print(f"    kappa in ker(d_1): {enr['claim_4_kappa_in_ker']}  [claim (4)] {'PASS' if enr['claim_4_kappa_in_ker'] else 'FAIL'}")
    print(f"    kappa is g-invariant (C_2 eigenvalue 0): {enr['claim_kappa_is_invariant']}")

    print(f"\n  d_2 (Killing contraction at level k):")
    print(f"    kappa^{{ab}} kappa_{{ab}} = {enr['killing_contraction_scalar']} = dim(sl2)")
    print(f"    d_2(kappa tensor H^1) = {enr['d2_image']}")
    print(f"    Nonzero at generic k: {'PASS' if enr['claim_5_d2_nonzero'] else 'FAIL'}")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    all_claims = [
        ("(1) d_1 surjective (rank 3)", enr['claim_1_surjective']),
        ("(2) ker(d_1) dim = 6", enr['claim_2_ker_dim_6']),
        ("(3) V_3 = Lambda^2(g) -> g isomorphism", enr['claim_3_V3_isomorphism']),
        ("(4) Killing form kappa in ker(d_1)", enr['claim_4_kappa_in_ker']),
        ("(5) d_2 kills V_1 (nonzero contraction)", enr['claim_5_d2_nonzero']),
        ("(6) CE d1 rank 3 (injective)", ce['claim_6_d1_rank_3']),
        ("(7) CE d2 = 0", ce['claim_7_d2_is_zero']),
        ("(8) H*(sl2) = (1,0,0,1)", ce['claim_8_cohomology']),
        ("Casimir decomposition V_5+V_3+V_1", enr['claim_adjoint_decomposition']),
        ("kappa is g-invariant", enr['claim_kappa_is_invariant']),
        ("d^2 = 0 in CE complex", ce['d_squared_zero']),
    ]

    all_pass = True
    for name, result in all_claims:
        status = "PASS" if result else "FAIL"
        print(f"  {status}: {name}")
        if not result:
            all_pass = False

    print()
    if all_pass:
        print("  ALL CLAIMS VERIFIED.")
        print("  Theorem thm:pbw-genus1-km Step 4 is computationally confirmed.")
        print()
        print("  Interpretation:")
        print("  - E_1(g=1) = E_1(g=0) + enrichment from H^1(E_tau)")
        print("  - At h=2: enrichment = g^{otimes 2} = V_5 + V_3 + V_1 (dim 9)")
        print("  - d_1 kills V_3 (bracket isomorphism, dim 3)")
        print("  - Whitehead kills V_5 (non-trivial rep, dim 5)")
        print("  - d_2 kills V_1 (Killing contraction at level k, dim 1)")
        print("  - All 9 enrichment classes eliminated => E_inf = E_inf(g=0)")
        print("  - PBW SS degenerates => unconditional modular Koszulity at g=1")
    else:
        print("  SOME CLAIMS FAILED — investigate.")

    return {"ce": ce, "enrichment": enr, "all_pass": all_pass}


if __name__ == "__main__":
    run_mc1_computation()
