# conj:w-orbit-duality -- Frontier Assessment

## Location

w_algebras.tex, line 471. Label: conj:w-orbit-duality.
Status: ClaimStatusConjectured. Cross-referenced in 18 files across Vol I.

## Statement

For non-principal nilpotent f in g and simply-laced g:

    W^k(g, f)^! = W^{k'}(g, f^D)

where f^D is the Barbasch-Vogan dual nilpotent (whose orbit has the same
component group A(O) as O_f) and k' is determined by the Feigin-Frenkel
involution shifted by the difference in Dynkin gradings. For non-simply-laced
g, the duality involves the Langlands dual g^v and the Spaltenstein dual of f.

## Proved corridor

- **Principal nilpotent** (f = f_prin): PROVED for all simple g.
  This is Feigin-Frenkel duality: W^k(g)^! = W^{-k-2h^v}(g).
  (thm:w-algebra-koszul-main)

- **Hook-type in type A**: CONDITIONAL on DS-bar compatibility.
  Transport-closure theorem (thm:hook-transport-corridor): if bar-cobar
  intertwines with reduction/inverse-reduction along the hook network,
  then W^k(sl_N, f_eta)^! = W^{-k-2N}(sl_N, f_{eta^t}) for every hook
  partition eta = (N-r, 1^r). Transport propagation lemma
  (prop:transport-propagation) PROVED: if the duality works on hook
  vertices and intertwines every edge, it extends to the transport-closure.
  Computationally verified for N = 2, ..., 7.

- **sl_3 Bershadsky-Polyakov (minimal orbit)**: CONJECTURED (conj:bp-duality).
  (B^k)^! = B^{-k-6} with c + c' = 196 (k-independent). Evidence: central
  charge transforms correctly, curvature data compatible, explicit bar
  computation done (comp:bp-bar). The minimal orbit (2,1) is self-transpose
  so orbit type is preserved. Missing: actual non-principal DS/bar comparison.

- **sl_2 admissible levels**: Koszul at all admissible levels (structural
  argument from single-weight null vector).

## Relationship to conj:ds-kd-arbitrary-nilpotent

These are two distinct conjectures that address different layers of the
same problem. Their relationship is:

### conj:ds-kd-arbitrary-nilpotent (w_algebras_deep.tex, line 1969)

**Statement**: The comparison map B(W^k(g,f)) --> H^0_{DS,f}(B(V_k(g)))
is a quasi-isomorphism for every nilpotent f at generic level.
Equivalently: bar-cobar/Koszul duality COMMUTES with DS reduction.

**Nature**: This is a FUNCTOR COMMUTATIVITY statement. It says bar and DS
commute as functors, regardless of what the resulting dual algebra turns
out to be.

### conj:w-orbit-duality (w_algebras.tex, line 471)

**Statement**: The Koszul dual W^k(g,f)^! is identified as W^{k'}(g,f^D)
for the Barbasch-Vogan dual nilpotent.

**Nature**: This is an IDENTIFICATION statement. It identifies the OUTPUT
of Koszul duality with a specific known algebra.

### Logical relationship

The two conjectures factor the full problem into two independent pieces:

    conj:ds-kd-arbitrary-nilpotent = "bar commutes with DS"
    conj:w-orbit-duality = "the dual is W^{k'}(g, f^D)"

Neither implies the other. Specifically:

1. **ds-kd-arbitrary-nilpotent does NOT imply w-orbit-duality.**
   Even if bar commutes with DS, one still needs to identify:
   (a) which nilpotent orbit appears on the dual side (the BV dual f^D),
   (b) what the level transform k' = k'(k,f) is.
   The functor commutativity gives W^k(g,f)^! = DS_f(V_k(g)^!) = DS_f(V_{-k-2h^v}(g)),
   but one must then show DS_f(V_{-k-2h^v}(g)) = W^{k'}(g, f^D). This
   requires proving that DS at the dual level, applied to the Feigin-Frenkel
   dual affine algebra, produces the W-algebra for the BV dual orbit --
   a non-trivial identification involving the geometry of nilpotent orbits.

2. **w-orbit-duality does NOT imply ds-kd-arbitrary-nilpotent.**
   One could in principle identify W^k(g,f)^! = W^{k'}(g,f^D) by direct
   bar cohomology computation, without establishing the functor commutativity.
   (This is conceptually possible but computationally much harder.)

3. **Together they give the full picture.** The combination says:
   bar-cobar duality commutes with DS, AND the result is the W-algebra
   for the BV dual orbit at the shifted level. The concordance
   (line 9630-9654) reformulates ds-kd-arbitrary-nilpotent in the
   Theta^oc language: DS_f should induce a morphism of open-closed
   convolution algebras preserving the MC element. This is STRONGER than
   mere functor commutativity.

### Which is harder?

**conj:ds-kd-arbitrary-nilpotent is the harder analytic problem.**
The obstruction is precisely identified: E_1-degeneration of the BRST
spectral sequence for non-abelian n_+ (the Kazhdan filtration argument
breaks when [n_+, n_+] != 0). The first genuine test case is the (3,2)
partition in sl_5 (BRST order 4, 6 commutator landings, non-abelian n_+).

**conj:w-orbit-duality is the harder algebraic-combinatorial problem.**
Even granted functor commutativity, the orbit identification requires:
(a) understanding Barbasch-Vogan duality for all orbits (known classically),
(b) determining the level transform k' for each orbit (known only for
principal and hook-type in type A),
(c) verifying compatibility with the Slodowy slice geometry.

### The proving strategy

The manuscript's approach decomposes the full W-duality problem into
three layers (w_algebras_deep.tex, rem:ds-kd-scope-map):

    Layer 1: DS-bar commutation (conj:ds-kd-arbitrary-nilpotent)
    Layer 2: Orbit identification under BV duality (part of conj:w-orbit-duality)
    Layer 3: Level transform k' = k'(k,f) (part of conj:w-orbit-duality)

The hook-type transport corridor (thm:hook-transport-corridor) bypasses
Layer 1 by using the transport propagation mechanism: start from the
principal (where all three layers are proved) and propagate along edges
of the reduction network. This does not require proving DS-bar commutation
at each node individually.

The type-A transport-to-transpose conjecture (conj:type-a-transport-to-transpose)
extends this: if hook vertices suffice as seeds and every edge of Gamma_N
is compatible, then duality extends to all partitions in Par(N). This is
the type-A specialization of conj:w-orbit-duality, with transport replacing
the global BV identification.

## Status assessment

**Proved cases**: Principal (all simple g). Hook-type in type A (conditional
on DS-bar compatibility). sl_3 Bershadsky-Polyakov (conjectural, with
strong evidence).

**First open case**: The (3,2) partition in sl_5 -- the first non-abelian
n_+ case. A direct BRST spectral sequence computation would advance both
conjectures simultaneously.

**Structural dividing line**: Abelianity of n_+ = bigoplus_{j>0} g_j.
When n_+ is abelian, the Kazhdan filtration gives E_1-degeneration and
the functor commutativity follows (prop:ds-bar-formality). When n_+ is
non-abelian, ghost-ghost corrections in the BRST charge introduce genuine
obstructions.

**Beyond type A**: For non-simply-laced g, the duality involves the
Langlands dual g^v and the Spaltenstein dual (not the BV dual). The
B_n <-> C_n orbit exchange adds a layer of complexity not present in
type A.

## Difficulty

MODERATE-to-HARD. The abelian-n_+ corridor is settled. The non-abelian
case requires controlling ghost-ghost corrections to the Kazhdan filtration
spectral sequence -- a genuine new input. The orbit/level identification
is a separate combinatorial problem that requires orbit-by-orbit analysis.

## Recommended next steps

1. Explicit BRST spectral sequence computation for (3,2) in sl_5.
   This is a finite computation (6 commutator landings, BRST order 4)
   that tests both conjectures at their first non-trivial instance.

2. Tabulate BV dual orbits and candidate level transforms for sl_4
   and sl_5 (all orbits, not just hook-type). Compare with the
   transport-closure predictions.

3. For non-simply-laced: compute the Spaltenstein dual orbits for
   B_2, C_2, G_2 and compare with the existing non-simply-laced
   Koszul data (all class L by the extremal swarm computation).
