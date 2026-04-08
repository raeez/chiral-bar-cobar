# DS-KD Intertwining for Arbitrary Nilpotent: Assessment

## The Conjecture

**conj:ds-kd-arbitrary-nilpotent** (w_algebras_deep.tex, line 1969):
For every nilpotent f in g at generic level, the comparison map

    B(W^k(g,f)) --> H^0_{DS,f}(B(V_k(g)))

is a quasi-isomorphism of dg coalgebras.  Equivalently, bar-cobar/Koszul
duality commutes with Drinfeld-Sokolov reduction for arbitrary nilpotent f.

**conj:DS-arbitrary-nilpotent** (ordered_associative_chiral_kd.tex, line 7594):
The ordered-bar variant: Q_DS(A^!) = Q_DS(A)^! for arbitrary nilpotent,
conditional on (a) Q_DS exact on filtered complexes, (b) Q_DS preserves
PBW filtrations, (c) the BRST differential lifts to the ordered bar coalgebra.

## Proved Corridor

- **Principal nilpotent**: proved for all simple g (Feigin-Frenkel,
  thm:w-algebra-koszul-main).
- **Subregular and minimal in sl_3**: proved (explicit computation).
- **Hook-type in type A**: proved corridor
  (thm:hook-transport-corridor, prop:transport-propagation).
  Transport-closure in type A verified computationally for N=2,...,7
  (thm:transport-closure-type-a).
- **sl_2 admissible levels**: Koszul at all admissible levels
  (structural argument from single-weight null vector).

## What Specifically Fails Beyond Hook-Type

The structural dividing line is the **abelianity of n_+**
(rem:abelian-nonabelian-nilradical):

### Abelian n_+ regime (where the proof works):

When n_+ = bigoplus_{j>0} g_j is abelian (i.e., [n_+, n_+] = 0), the BRST
charge decomposes as Q_DS = Q_st + Q_gh with Q_gh = 0 (no ghost-ghost term).
The Kazhdan filtration on V_k(g) tensor F_{n_+} gives E_1-degeneration at
generic k, and the resulting E_1-page is the W-algebra with no higher
corrections.  This is the content of prop:ds-bar-formality.

Hook-type partitions in type A have abelian n_+ (verified case-by-case).
The proof extends to any partition with abelian n_+.

### Non-abelian n_+ regime (where the proof breaks):

When [n_+, n_+] != 0, the BRST charge acquires ghost-ghost terms of order
<= max{j : g_j != 0}.  The first non-abelian case is the **(3,2) partition
in sl_5**, with BRST order 4 and 6 commutator landings.

**Specifically, what fails:**

1. **Q_gh != 0**: The ghost-ghost piece is quadratic in ghosts, encoding
   the Lie bracket [n_+, n_+].  The BRST complex is no longer a Koszul
   complex on the n_+-action; it has genuine higher-order terms.

2. **E_1 degeneration is not automatic**: The Kazhdan filtration spectral
   sequence may have nontrivial higher differentials d_r for r >= 2.
   At generic k, the expectation is still E_1-degeneration (because the
   associated graded is still Sym_partial(g) with trivial n_+-action),
   but the proof requires controlling the ghost-ghost corrections to
   the filtration.

3. **At rational k (admissible/critical levels)**: Even for abelian n_+,
   E_1-degeneration can fail because vacuum null vectors produce genuine
   higher differentials.  For non-abelian n_+, this is worse: the
   ghost-ghost terms interact with null vectors.

4. **The manuscript's internal inconsistency**: The current summaries of the
   type-A abelian-n_+ locus are "not yet internally harmonized"
   (rem:abelian-nonabelian-nilradical, line 2079), so even the abelian
   hook-wide extension is used with care.

## Does the E_1 Primacy Thesis Help?

**Partially, yes.** The ordered bar framework (ordered_associative_chiral_kd.tex)
provides new structural leverage in three ways:

### What the ordered bar adds:

1. **The BRST complex is naturally E_1**.  The DS reduction acts on the
   ordered bar coalgebra B^ord(V_k(g)), and the BRST differential
   Q_DS lifts to an endomorphism of B^ord.  The ordered structure
   (deconcatenation coproduct, not coshuffle) is the natural home for
   the BRST complex because the ghost system has an ordering
   (the Dynkin grading provides a canonical filtration on n_+).

2. **PBW compatibility is automatic for the ordered bar**.  The strong
   filtration axiom (mu_r(F^{i_1},...,F^{i_r}) subset F^{i_1+...+i_r})
   that controls the completion tower (thm:completed-bar-cobar-strong)
   is compatible with the Kazhdan filtration.  This means the ordered
   bar construction preserves filtered limits, which is step (b) of
   conj:DS-arbitrary-nilpotent.

3. **The ordered bar captures the R-matrix data**.  For DS-KD
   intertwining of the full modular Koszul triple (algebra + dual + r-matrix),
   the r-matrix transfer requires both DS-bar commutation AND filtration
   formality (prop:ds-bar-formality; rem:ds-triple-nonprincipal).
   The ordered bar is the natural setting for the r-matrix because
   deconcatenation encodes the ordered collision data.

### What the ordered bar does NOT resolve:

1. **The core difficulty remains**: step (c) of conj:DS-arbitrary-nilpotent
   requires that the BRST differential lifts to the ordered bar coalgebra
   BEYOND the abelian-n_+ regime.  When Q_gh != 0, the ghost-ghost terms
   introduce higher-order corrections that may not respect the coalgebra
   structure.  The ordered bar framework identifies this as the precise
   obstruction but does not solve it.

2. **E_1 degeneration for non-abelian BRST**: The Kazhdan filtration
   argument works because the associated graded has trivial n_+-action.
   For the ordered bar, the analogous statement is that the E_1 page
   of the ordered-bar spectral sequence should be the ordered bar of
   the W-algebra.  This is proved for abelian n_+ (where E_1 degeneration
   of the BRST complex gives it directly) but not for non-abelian n_+.

## The Obstruction Hierarchy

From the concordance (line 9655) and the Theta^oc reformulation:

1. **Algebraic level**: DS_f must induce a morphism of open-closed
   convolution algebras DS_f^oc: g^oc_{V_k} --> g^oc_{W_k(g,f)}
   satisfying DS_f^oc(Theta^oc_{V_k}) = Theta^oc_{W_k(g,f)}.
   This is STRONGER than functor commutativity.

2. **The (3,2) in sl_5 is the first genuine test case**: BRST order 4,
   6 commutator landings, non-abelian n_+.  An explicit computation
   of the BRST spectral sequence for this case would either prove or
   refute the conjecture at the first non-trivial instance.

3. **Beyond type A**: the BV orbit identification (rem:bv-orbit-identification)
   extends the duality to all simple g via Barbasch-Vogan/Spaltenstein,
   but the filtration-formality proof does not automatically transfer.

## Assessment Summary

**Status**: OPEN.  The conjecture is well-formulated and the obstruction
is precisely identified: E_1-degeneration of the BRST spectral sequence
for non-abelian n_+.

**Difficulty**: MODERATE-to-HARD.  The abelian case is settled by existing
methods.  The non-abelian case requires genuine new input (controlling
ghost-ghost corrections to the Kazhdan filtration).  The (3,2) in sl_5
is a concrete, computationally accessible test case.

**E_1 primacy leverage**: The ordered bar framework correctly identifies
the obstruction as a coalgebra-level lifting problem and provides the
right categorical setting.  It does not by itself resolve the spectral
sequence degeneration question, but it clarifies what must be proved.

**Recommended next step**: Explicit computation of the BRST spectral
sequence for the (3,2) nilpotent in sl_5, checking whether E_1-degeneration
holds at generic level.  This is a finite-dimensional computation
(6 commutator landings, BRST order 4) that can be carried out
computationally.  If E_1 degeneration holds, the pattern suggests a
proof via filtration formality for all nilpotents at generic level.
If it fails, the conjecture must be restricted or reformulated.
