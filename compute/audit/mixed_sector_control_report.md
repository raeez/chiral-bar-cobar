# What the Mixed Sector of SC^{ch,top,!} Controls

## Summary

The mixed sector SC^!(ch^k, top^m; top) of the Koszul dual cooperad controls
the **bulk-to-boundary module structure**: how the chiral derived center
Z^der_ch(A) acts on the boundary algebra A via iterated brace evaluation.

It does NOT control delta_F_g^cross (Agent 16's falsification is correct).

## The Five Manifestations

### M1. Bulk-to-boundary map (PROVED, thm:thqg-swiss-cheese)

The genus-0, k-interior, m-boundary projection of Theta^oc gives the
universal bulk-to-boundary coupling:

    iota_{0,k,m} : Z^der(A)^{otimes k} -> Hom(A^{otimes m}, A)

This is the mixed projection of the open/closed MC element
(thm:thqg-oc-projection(iii)).  The universal open/closed pair
U(A) = (C^*_ch(A,A), A) is terminal among all Swiss-cheese pairs
over A; its mixed operations mu^univ_{p;q} are precisely the brace
evaluations of Hochschild cochains on algebra elements.

Dimension at (k,m): cooperad_dim(k,m) * gen_dim^{k+m+1}.

| (k,m) | Cooperad dim | Heis (r=1) | sl_2 (r=3) | W_3 (r=2) |
|-------|-------------|------------|------------|-----------|
| (1,1) | 2           | 2          | 54         | 16        |
| (1,2) | 3           | 3          | 243        | 48        |
| (2,1) | 3           | 3          | 243        | 48        |
| (2,2) | 6           | 6          | 1458       | 192       |

### M2. Brace relations (PROVED, thm:thqg-brace-dg-algebra)

The higher pre-Lie identities on C^*_ch(A,A) constrain how multiple
bulk operators compose when acting on boundary states.  The brace
f{g_1,...,g_r} encodes simultaneous insertion of r bulk operators
into a boundary computation.  The mixed MC equation ensures these
are compatible with the A-infinity structure.

The Gerstenhaber bracket [f, g] = f{g} - (-1)^{|f||g|} g{f}
descends to cohomology, giving the Gerstenhaber algebra structure
on Z^der_ch(A) = H^*(C^*_ch(A,A)).

### M3. Line-defect screening (STRUCTURAL consequence of M1)

When a bulk operator passes through a line defect with m boundary
insertions, it can be inserted at (m+1) positions.  This matches:

    SC^!(1, m; top) = C(1+m, m) = m+1

Verified for m = 1 through 8.  For k bulk operators screening
simultaneously, the factorization

    SC^!(k, m) = Lie(k) * C(k+m, m)

means the k bulk operators first compose via their OPE (Lie structure),
then the composite screens through the boundary (shuffle interleaving).

### M4. Annulus degeneration constraint (PROVED, prop:thqg-annulus-degeneration-kappa)

The annulus trace Tr_A in HH_0(A) is the genus-0 mixed-sector shadow.
The non-separating clutching sends it to kappa * lambda_1:

    Delta_ns(Tr_A) = kappa(A) * lambda_1

This is the first mixed-to-closed transfer: open-sector data (the trace)
determines closed-sector data (the genus-1 curvature) via the clutching
sector of the open/closed MC equation.

### M5. Derived center module dimension (COMPUTATIONAL)

For each standard family, the derived center action on A has dimensions
controlled by the mixed-sector convolution.

| Family     | gen_dim | Shadow | Mixed MC | Z^der action |
|-----------|---------|--------|----------|-------------|
| Heisenberg | 1       | G      | trivial  | scalar (k acts by multiplication) |
| aff sl_2   | 3       | L      | nontrivial | adjoint + corrections (dim 54 at (1,1)) |
| Virasoro   | 1       | M      | nontrivial | T self-interaction via T_{(1)}T = 2T |
| W_3        | 2       | M      | nontrivial | mixed T-W couplings (dim 16 at (1,1)) |


## What the Mixed Sector Does NOT Control

### F1. delta_F_g^cross (FALSIFIED by Agent 16)

The cross-channel correction delta_F_g^cross involves graphs on M-bar_{g,0}
(no boundary marked points) with mixed channel assignments.  These are
endomorphism decorations within the CLOSED sector, not sector changes.
The relevant moduli space has no boundary components.

Key distinction: channel assignments label which generator propagates
along each edge.  This is structure within End_A (the endomorphism
part of the convolution), not structure within SC^! (the cooperad part).

delta_F_g^cross = F_g - kappa * lambda_g^FP is entirely within g^mod_A
(the closed-sector convolution algebra).

### F2. Line-operator fusion (pure OPEN sector)

Line-operator fusion (tensor product of boundary modules) is controlled
by Ass^c(m), the associative cooperad in the open sector.  The mixed
sector controls bulk SCREENING of lines (a bulk operator passing through
a defect), not line-line fusion.

### F3. R-matrix (CLOSED sector collision residue)

The classical r-matrix r(z) = Res^coll_{0,2}(Theta_A) is a genus-0,
arity-2 closed-sector projection.  The open-sector braiding of modules
lives in the open sector.  Neither involves the mixed sector.


## The Mixed MC Equation

The full open/closed MC equation (thm:thqg-oc-mc-equation) decomposes:

    (a) Pure closed:   D(Theta^mod) + 1/2[Theta^mod, Theta^mod] = 0
    (b) Pure open:     sum mu_i o mu_j = 0
    (c) Mixed:         d(Theta^mix) + [Theta^mod, Theta^mix]
                       + 1/2[Theta^mix, Theta^mix] + [Theta^R, Theta^mix] = 0
    (d) Clutching:     hbar * Delta_clutch(Theta^oc) = 0

Equation (c) is the MIXED MC EQUATION.  Its three interaction terms:

- [Theta^mod, Theta^mix]: closed-sector constraints on bulk-boundary coupling
- [Theta^mix, Theta^mix]: self-interaction of bulk-boundary couplings
- [Theta^R, Theta^mix]: R-matrix constraints on bulk-boundary coupling

This equation is equivalent to the condition that A is an A-infinity
MODULE over Z^der_ch(A), with the module structure compatible with
the genus tower (from Theta^mod) and the braiding (from Theta^R).


## The W_3 Explicit Example

At (1,1) for W_3 (gen_dim = 2):

- Cooperad dimension: SC^!(1,1) = 2 (two orderings)
- Endomorphism dimension: 2^3 = 8 (bulk x bdry x output generator choices)
- Total convolution dimension: 16

The 8 endomorphism components per ordering:

| Bulk | Bdry | Out | Nonzero? | Value |
|------|------|-----|----------|-------|
| T    | T    | T   | Yes      | 2T (from T_{(1)}T = 2T) |
| T    | T    | W   | No       | -- |
| T    | W    | T   | No       | -- |
| T    | W    | W   | Yes      | 3W (conformal weight action) |
| W    | T    | T   | No       | -- |
| W    | T    | W   | Yes      | 3W (skew-symmetry) |
| W    | W    | T   | Yes      | 2*beta*T (W_3 structure constant) |
| W    | W    | W   | No       | -- |

4 nonzero components per ordering, 8 total nonzero couplings.
These encode the full T-W brace algebra structure at leading order.


## Compute Verification

Engine: `compute/lib/sc_mixed_sector_engine.py` (13 sections, ~600 lines)
Tests: `compute/tests/test_sc_mixed_sector_engine.py` (47 tests, all pass)

Test coverage:
- Cooperad dimensions (3-path verification per AP10)
- Bulk-to-boundary map dimensions for all standard families
- Line-defect screening SC^!(1,m) = m+1 for m = 1..8
- Brace algebra dimensional structure
- Mixed MC equation decomposition at gen_dim = 1, 2, 3
- Falsification recording (Agent 16)
- Explicit shuffle enumeration
- Module consistency checks
- W_3 explicit OPE component analysis


## Relation to Manuscript

The mixed-sector identification is implicit in Vol I at:
- thm:thqg-swiss-cheese (the universal open/closed pair)
- thm:thqg-oc-mc-equation, part (c) (the mixed MC equation)
- thm:thqg-oc-projection, part (iii) (the mixed projection)
- thm:thqg-brace-dg-algebra (the brace dg algebra)

The explicit statement "the mixed sector controls the bulk-to-boundary
module structure" appears in the proof of thm:thqg-oc-mc-equation:
"The terms with k >= 1 and |m| >= 1 encode the bulk-to-boundary
couplings: how closed-sector operators act on the boundary modules M_j."

The engine makes this implicit identification explicit and computable.
