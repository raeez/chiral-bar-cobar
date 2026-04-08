# Restricted DK-4 on Evaluation Modules: Feasibility Assessment

## The Target

**DK-4** (conj:dk4-formal-moduli): Identify the tangent Lie algebra
g_A = T_* F_A of the factorization formal moduli problem with the
dg-shifted Yangian Y^dg_A, as filtered complete dg Lie algebras.

**Restricted DK-4**: The same identification restricted to the
evaluation-generated sector. Two of three ingredients for the
restricted DK-5 triple bridge (conj:restricted-dk5) are proved:
- Thick generation at all simple types (cor:dk2-thick-generation-all-types)
- Categorical CG closure at all types (thm:categorical-cg-all-types)

The missing piece is DK-4 restricted to the generated sector.

## What DK-4 Reduces To (Type A)

Proposition prop:yangian-dk4-typea-frontier achieves an extraordinary
reduction chain for standard type A. The live input reduces to:

### Step 1: Boundary-strip identities
    Delta_{a,0}(N) = K^line_{a,0}(N) - K^RTT_{a,0}(N) = 0

### Step 2: Auxiliary-kernel identity (on fundamental evaluation line)
    L_a(u) = R_{0a}(u - a)

### Step 3: Residue formula (under symmetry + normalization)
    Res_{u=a} L_a(u) = -hbar * P

### Step 4: Mixed-tensor check (single computation)
    Xi_a(e_1 tensor e_2) = -hbar * (e_2 tensor e_1)

### Step 5: Scalar coefficient (after degree-2 normalization)
    The scalar coefficient of the permutation operator = -1,
    which is forced by the fundamental Casimir insertion.

**Key result**: Corollary cor:factorization-fundamental-casimir-identity
proves that the factorization side ALREADY satisfies this identity.
Proposition prop:dg-shifted-factorization-shared-seed shows any
dg-shifted realization with the same ordered bar seed inherits the
same coefficient.

**Status**: The reduction chain is COMPLETE. The live input is not a new
coefficient computation, but the REALIZATION of the dg-shifted target
with the shared bar seed. This is an algebraic construction problem,
not a numerical verification problem.

## What Specifically Needs To Be Computed

The computation has two layers:

### Layer 1: Finite-dimensional (tractable)

At each evaluation point a in C, the tangent complex T_* F_A restricted
to evaluation modules V_{omega_i}(a) is a finite-dimensional complex:

    T_* F_A |_{V_omega(a)} = RHom_{FAlg}(A tensor R, A tensor R)|_{V_omega(a)}

For the Yangian E_1-chiral algebra A = Y(sl_N):
- V_omega(a) is the evaluation module: an (N choose i)-dimensional
  representation of sl_N with spectral parameter a.
- The tangent complex at this point is controlled by the
  endomorphism algebra End_Y(V_omega(a)).

**Dimension of relevant Ext groups**:

For evaluation modules V_n(a), V_m(b) of Y(sl_2):
- Ext^0_Y(V_n(a), V_m(b)) = Hom(V_n(a), V_m(b))
  - dim = delta_{n,m} * delta_{a,b}  (Schur's lemma for generic a,b)
  - dim = (n+1)  when a = b, n = m (endomorphisms)
- Ext^1_Y(V_n(a), V_m(b)):
  - For a != b: dim = delta_{n,m} (one-dimensional extension space
    from the R-matrix pole at u = a - b)
  - For a = b: dim = n (deformation theory of the evaluation structure)
- Ext^k for k >= 2:
  - Controlled by the bar spectral sequence. For Koszul Y(sl_N):
    Ext^k = 0 for k >= 2 on evaluation modules (bar concentration).

**For sl_2 fundamental (V_1)**:
- dim V_1 = 2.
- End_Y(V_1(a)) = C (scalar endomorphisms).
- Ext^1_Y(V_1(a), V_1(b)) = C for a - b generic (one R-matrix pole).
- The tangent complex is concentrated in degrees 0 and 1:
  a TWO-TERM complex of dimension 1 + 1 = 2.

**For sl_N fundamental (V_omega_1)**:
- dim V_omega_1 = N.
- End_Y(V_omega_1(a)) = C.
- Ext^1_Y(V_omega_1(a), V_omega_1(b)) = C for generic a - b.
- Tangent complex: two-term, dimension 1 + 1 = 2.

These are small, explicitly computable objects.

### Layer 2: Algebraic identification (the real content)

The finite-dimensional Ext data at Layer 1 gives the MODULE-LEVEL
comparison. The DK-4 content is the ALGEBRA-LEVEL identification:
the tangent dg Lie algebra g_A (derivations of the factorization
bar coalgebra) must be identified with the dg-shifted Yangian Y^dg_A.

This requires:
1. **Structure constants**: The Lie bracket on g_A restricted to
   evaluation generators is determined by the R-matrix via
   [g_a, g_b] = r(a-b) * (g_a tensor g_b). This is PROVED (the
   R-matrix IS the degree-2 part of the twisting morphism).

2. **Filtration comparison**: The RTT-adapted filtration on Y^dg
   must match the canonical filtration on g_A by order of the
   formal parameter. This is the content of conj:dk4-formal-moduli(b).

3. **Higher operations**: The L-infinity structure on g_A may have
   nontrivial higher brackets l_k for k >= 3. On the evaluation
   core, these are controlled by the Drinfeld associator Phi_KZ,
   which lives in ker(av) (the kernel of the averaging map
   B^ord -> B). The E1 primacy theorem (thm:e1-primacy) proves
   that this kernel is nontrivial at arity 3.

## Dimension Summary

| Object | Dimension | Computable? |
|--------|-----------|-------------|
| V_omega_1(a) for sl_N | N | Yes |
| End_Y(V_omega_1(a)) | 1 | Yes |
| Ext^1_Y(V_1(a), V_1(b)) | 1 | Yes |
| Tangent complex T_*F at eval point | 2-term, dim 1+1 | Yes |
| R-matrix r(u) for sl_N | N^2 x N^2 matrix | Yes (Yang R-matrix) |
| Drinfeld associator Phi_KZ at arity 3 | In ker(av_3) | Computed (47 tests) |
| RTT boundary strip defects | Verified = 0 for N=2,...,8 | Yes |

## Is This a Tractable Computation?

### YES for the restricted (evaluation-core) problem

The evaluation-core DK-4 reduces to a FINITE computation at each
evaluation point:

1. The RTT boundary-strip identities Delta_{a,0}(N) = 0 are VERIFIED
   numerically for N = 2, ..., 8 by the existing dk_compact_generation
   engine (test_dk_compact_generation.py).

2. The residue formula Res_{u=a} L_a(u) = -hbar * P is VERIFIED
   on the theorematic standard RTT tower (prop:dg-shifted-rtt-standard-
   typea-local-packet).

3. The factorization side satisfies the Casimir identity
   (cor:factorization-fundamental-casimir-identity).

4. The shared-seed proposition (prop:dg-shifted-factorization-shared-seed)
   transports the coefficient from the factorization side to any
   dg-shifted realization with the same bar seed.

**What remains**: The algebraic construction of the dg-shifted Yangian
Y^dg_A as a specific dg Lie algebra (not just its evaluation-module
data). The evaluation-module data is completely determined; what is
missing is the GLOBAL algebraic object that extends this data.

### NO for the full DK-4

The full DK-4 requires:
- Extension beyond evaluation modules to all highest-weight modules
  (category O). This is the B1 sub-target.
- The Mittag-Leffler condition for the completed inverse limit
  (B2, partially proved: thm:rtt-mittag-leffler).
- Comparison with Latyntsev's spectral quantum group (B4, open).

## The Genuine Gap

The reduction chain in prop:yangian-dk4-typea-frontier is remarkably
complete: it reduces DK-4 to a single mixed-tensor coefficient that
is ALREADY verified on both sides. The genuine gap is:

**REALIZATION**: Construct a dg Lie algebra g with the following properties:
1. Filtered complete, with the RTT-adapted filtration.
2. Its finite quotients g/F^{N+1} recover the theorematic RTT stages.
3. Its completed bar/cobar data is compatible with the standard RTT tower.
4. Its degree-2 twisting morphism matches the ordered bar seed on the
   fundamental evaluation line.

Properties (1)-(3) are formal consequences of the strong completion
tower theorem (thm:completed-bar-cobar-strong). Property (4) is
verified numerically. The gap is the ALGEBRAIC IDENTIFICATION: proving
that the abstract tangent Lie algebra g_A (which exists by Lurie's
theorem) satisfies (1)-(4).

This is a problem in HIGHER ALGEBRA, not in linear algebra or
numerical computation. The finite-dimensional Ext computations at
evaluation points are all tractable (and many are already done). The
missing step is the passage from pointwise data to global structure.

## Assessment

### Feasibility: HIGH for pointwise verification, MEDIUM for algebraic identification

- **Pointwise data**: Completely determined and verified. Ext groups
  at evaluation points are 0-or-1-dimensional. R-matrix coefficients
  match. Boundary strip defects vanish. All existing tests pass.

- **Algebraic identification**: Requires constructing Y^dg_A as a
  specific filtered complete dg Lie algebra and proving it equals g_A.
  The abstract existence (Lurie) is proved. The finite-quotient
  compatibility (MC4 strong completion) is proved. The remaining
  step is the identification of the canonical formal-moduli filtration
  with the RTT-adapted filtration in the basis of RTT generators.

### Most productive next step

Extend the existing dk_compact_generation and yangian_residue engines
to compute:

1. **Ext^*(V_omega(a), V_omega(b)) for sl_3**: Verify the tangent
   complex dimension at all fundamental evaluation points. The sl_2
   case is covered; sl_3 (the first rank-2 case) is the test.

2. **RTT boundary strip for non-simply-laced types**: The boundary
   strip Delta_{a,0}(N) = 0 is verified for sl_N. Extend to B_N,
   C_N, D_N (the R-matrices are different: Zamolodchikov-type).

3. **Degree-2 seed comparison at sl_3**: Verify that the degree-2
   twisting morphism tau|_{deg 2} on the sl_3 fundamental evaluation
   line matches the known sl_3 R-matrix. This is the type-A DK-4
   benchmark at the first non-trivial rank.

These are all finite-dimensional linear algebra computations, each
requiring O(N^4) operations (N^2 x N^2 R-matrix, N = rank+1).
Completely tractable.
