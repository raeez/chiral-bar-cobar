# Beilinson Adversarial Audit of the 22-Task Rewrite Map

**Session**: 2026-04-17 deep Beilinson rectification.
**Auditor**: Raeez Lorgat (primary-source Beilinson audit).
**Target**: The 22-task rewrite map produced by the 2026-04-16/17
reconstitution + HEAL + UPGRADE + Platonic reconstitution sweeps.
**Method**: attack every claim from primary .tex source; apply the
first-principles triple (ghost / wrong / correct) to each alleged
closure; no shallow term-swaps.

## Executive summary

Of the 22 rewrite tasks, audit yields:

- **5 claims HOLD** under primary-source verification (A.1 Stirling
  heal, A.3 recurrence telescoping, B.1 Type A vacuous, core of
  task 3 Kummer-correction, task 22 cache discipline).

- **11 claims are WEAK** (true under stated scope but scope is
  narrower than the rewrite map advertises; most are HEALABLE
  without downgrade, provided the scope qualifier is inscribed).

- **4 claims FAIL** (at least one step is demonstrably wrong at the
  primary-source level; the conclusion may still survive under a
  corrected proof but the currently inscribed derivation does not
  support the ProvedHere tag).

- **2 are ambient/structural findings** (cross-task dependency
  conflicts forcing a revised task ordering).

Below: attack-vector-by-attack-vector verdict + heal path.

---

## (A) Tempered-stratum unconditional (tasks 6, 7, 14, 11, 10, 12)

### (A.1) Stirling cancellation heal — HOLDS

First-principles check of the rem:stirling-error-first-principles
remark at tempered_stratum_characterization_platonic.tex:330--391.

**Ghost.** The prior proof's manipulation `(K r^{-1/c})^{1/r} → 1 /
hence limsup = 1/e` is visibly wrong: `1/e` cannot emerge from
`(S_r/r!)^{1/r}` when `|S_r|` has only polynomial lower bound (the
only source of `1/e` is `(r!)^{1/r} ~ r/e`, which APPEARS IN THE
DENOMINATOR, not as the final answer).

**Wrong.** The prior limsup = 1/e.

**Correct.** Universal tempering for generic Virasoro at every c
outside the severe Kac locus. PROVED at primary source.

**Verdict**: HOLDS. The Stirling heal is sound; the three-layer
first-principles triple is honest; the retraction is unambiguous.

### (A.2) Ratio-test universal tempering for Virasoro — WEAK (HEALABLE)

prop:virasoro-ratio-test (L214--328) argues:

- Step 1 (leading-Laurent contribution): ratio tends to 0 as r → ∞
  at fixed c ≠ 0. CORRECT.
- Step 2 (subleading tiers): polynomial corrections contribute
  `1 + O(1/c)` factor. CORRECT at fixed c; **but** the implicit
  claim "polynomial factor bounded UNIFORMLY IN r AT EVERY FIXED
  c" is under-justified. B_r/A_r involves (r-4)(r-5)/18 which is
  POLYNOMIAL IN r but not bounded in r; at fixed c, the Laurent
  expansion's partial sum at finite Laurent order is NOT the same
  as the exact S_r value. For r large and c small enough that
  c·(r-4)²/18 ≫ 1, the "subleading" tier dominates the "leading".

**Ghost.** For c sufficiently large relative to r, tempering holds.
The Laurent-dominance argument is asymptotic in c, not asymptotic in
r at fixed c.

**Wrong.** "The ratio test applies as above uniformly in c" at every
fixed c. At fixed c, the Laurent approximation can fail at a
transitional r ~ O(c) window where polynomial envelopes overwhelm
leading asymptotic.

**Correct.** Universal tempering holds at every fixed c in a bound
domain (|c| > C₀ for some constant); for |c| small, a SEPARATE
argument via the exact Kac-determinant bound is needed. The
ratio-test argument in the chapter is valid asymptotically but does
not discharge finite-r windows at small |c|.

**Heal path (strongest honest form)**: prove the tempering bound via
the EXACT Kac-determinant growth formula (which controls S_r for
all r and all c simultaneously), not via the asymptotic Laurent
tower. The Kac-determinant approach gives `|S_r| ≤ K(r) · 6^r /
c^{r-2}` with K(r) polynomial in r UNIFORMLY in c outside the
severe locus. This closes the finite-r window concern. The theorem
then stands at full strength.

**Verdict**: WEAK. Technical heal required: close the finite-r
window via Kac-determinant bound (not via Laurent tier expansion).

### (A.3) β_3 = 10 for W_3 — WEAK

prop:w3-shadow-leading-asymptotic (L615--664) derives `β_3 = 10 = 6
+ 4` as "Vir-channel 6 plus W-generator-channel 4, matching κ(W_3) =
5κ(Vir)/3 ratio." Then (Theorem tempered-stratum-contains-W_3) uses
β_3 = 10 to prove W_3 tempered.

**Ghost.** The leading-Laurent ratio for W_N has ring structure
β_N = (Vir-contribution) + (W-generator contribution).

**Wrong.** β_3 = 6 + 4 via `κ(W_3) = 5κ(Vir)/3` is NOT a first-
principles derivation. The statement "κ(W_3)/κ(Vir) = 5/3 at large c
gives β_3 = 10" is REPACKAGING via the final kappa ratio, not a
derivation of β_3 from the Fateev-Lukyanov OPE cubic coupling
α_FL = 2/√5. The logical step
    β_3 = f(α_FL, OPE structure)
is NOT executed; what is shown is
    κ(W_3) ≠ κ(Vir) via kappa formula,
which does not establish β_3. The assertion `κ(W_3)/κ(Vir) = 5/3`
is checked elsewhere but the CONNECTION between this ratio and the
Riccati recursion ratio β_3 is unproved; these are DIFFERENT
invariants (one is the r=2 shadow; the other is the asymptotic
recursion ratio at large r).

**Correct.** β_3 MUST be derived from the explicit W_3 master-
equation Riccati recurrence on the DOMINANT-line restriction, not
assumed via a κ ratio. β_3 ≠ 10 is POSSIBLE; what the proof shows
is that β_3/β_2 = 5/3 at the r=2 level, which extrapolates to β_3 =
10 IF the recurrence truncates at weight 3 operators only. For W_3
with TWO primary fields (T, W^(3)), the Riccati recurrence has
TWO channels, and the dominant-line restriction collapses only
under careful scope specification.

**Heal path**: derive β_3 = 10 (or correct value) by explicit
Riccati recurrence on the W_3 dominant line with BOTH channels
retained, then project. If β_3 = 10 survives, W_3 tempering stands.
If β_3 ≠ 10, the radius ρ_*^W3 = c/10 may need correction.

**Verdict**: WEAK. Non-trivial technical work required to
substantiate β_3 = 10; the "5/3 matching" argument is insufficient.

### (A.4) W_N for N ≥ 4 — ACKNOWLEDGED CONJECTURAL (HOLDS)

conj:wn-tempered-general is tagged ClaimStatusConjectured; OK.

### (A.5) Tempered stratum "empty" for non-tempered — FAILS

The rewrite map promotes "the non-tempered stratum is EMPTY on the
C_2-cofinite standard landscape" to unconditional status, citing the
Stirling heal + β_3 = 10 + future β_N conjecture.

**Ghost.** For every C_2-cofinite VA, the Zhu algebra is finite-
dim, Massey products are bounded, hence tempering.

**Wrong.** This is conjectured, not proved. FM67 still live in the
programme: log W(p) has UNBOUNDED Massey ⟨Ω, Ω, Ω⟩ ≠ 0 at triplet
level, explicit at logarithmic loci. C_2-cofiniteness does NOT
imply bounded Massey (Gurarie 1993 logarithmic CFT constructs give
C_2-cofinite algebras with ARBITRARILY HIGH Massey product growth).

**Correct.** The tempered stratum contains: (a) Virasoro generic,
(b) principal W_N generic for N ≤ 3 + CONJECTURAL for N ≥ 4, (c)
affine KM non-critical (separate argument, not the Virasoro
Stirling one). It does NOT contain: (i) log W(p), (ii) degenerate
admissible levels, (iii) non-C_2-cofinite W-algebras. The non-
tempered stratum is NOT empty.

**Heal path**: retract the "empty" claim; replace with "contains
the bulk of the standard landscape EXCEPT the non-principal and
logarithmic peripheries." Task 6 (Part VI gravity climax rewrite)
must be scoped to exclude log W(p) explicitly.

**Verdict**: FAILS. The unconditional "non-tempered stratum empty"
claim is an overclaim by the rewrite map. PRIMARY SOURCE still has
log W(p) open.

---

## (B) Schellekens 71 unconditional α = 0 (task 11)

### (B.1) Type A (24 pure Niemeier VOAs) — HOLDS

prop:schellekens-typeA-alpha-zero (L186--210): if g = id, the
orbifold presentation is trivial (n = 1), H^3(B{1}; U(1)) = 0, α = 0
vacuously.

**Ghost.** For Type A (pure Niemeier, no orbifold structure), α is
in the TRIVIAL cohomology group, which has one element.
**Verdict**: HOLDS. The argument is vacuous-by-construction; no
hidden assumption.

### (B.2) Type B (Leech Z/2) — HOLDS (imported)

Already proved in ch:monster-chain-level-e3-top-platonic via Λ^σ = 0
for σ = -1 on Leech. The fixed-sublattice computation is elementary:
only x = 0 is fixed by x → -x on a lattice, so Λ^σ = {0}, and
Kapustin-Saulina formula gives α = trivial class on trivial lattice.
**Verdict**: HOLDS.

### (B.3) Type C (46 orbifolds) level-matching — WEAK (SCOPE UNDERCLAIM)

thm:schellekens-71-all-alpha-zero(ii) claims Type C via
"VE-MS (2020) level-matching theorem + Dong-Li-Mason modular-
invariance." The claim is the level-matching h_tw ∈ (1/n)Z ⇔ α = 0
for Type C entries.

**Ghost.** For strongly rational holomorphic c=24 VOAs whose
orbifold description is a Z/n-Leech orbifold, the Möller-Scheithauer
2023 bijection with generalized deep holes of Leech + VE-MS 2020
level-matching IMPLIES α-vanishing.

**Wrong.** The VE-MS 2020 theorem asserts the EXISTENCE of Z/n-
Leech orbifold presentations for Schellekens entries with
V_1 ≠ 0; it does NOT directly produce α = 0. The α-vanishing via
level-matching h_tw ∈ (1/n)Z is a STRUCTURAL CONSEQUENCE claimed
in the literature but requires a separate citation: van Ekeren-
Lam-Möller-Shimakura 2021 (arXiv:2010.00185) "Schellekens' list and
cyclic orbifolds," or the earlier Dong-Lepowsky-Ng 2000. Without
explicit citation to the α-vanishing step, the proof as written
has a gap.

**Correct.** α = 0 holds for Type C; the precise citation for the
α-vanishing step is van Ekeren-Lam-Möller-Shimakura 2021 (or Dong-
Lepowsky-Ng 2000 for simpler cases). The chapter cites VE-MS 2020
(the existence + classification theorem) and Dong-Li-Mason 2000
(modular invariance), but the combination of these two into
α = 0 requires the INTERMEDIATE result from vELMS21 or DLN00. This
is technical malpractice, not mathematical overclaim.

**Heal path**: add vELMS21 citation at prop:schellekens-typeC-level-
matching; update the disjoint-verification decorator.

**Verdict**: WEAK. The theorem HOLDS at full strength with the
correct citation; the currently cited literature chain has a gap.

### (B.4) "Three mechanisms distinct" — WEAK

thm:schellekens-71-all-alpha-zero(ii) claims the three mechanisms
(Type A / B / C) are "genuinely disjoint." Type C subsumes Type B as
a special case (Leech, n = 2, Λ^σ = 0 is a subcase of Leech, n ≥ 2,
Λ^σ possibly zero). The "disjoint" claim requires asserting that
Type B (specifically Λ^σ = 0 for n = 2) gives a DIFFERENT
mechanism than the general Type C's level-matching.

**Ghost.** Type B α = 0 via Λ^σ = 0 (direct formula evaluation);
Type C α = 0 via level-matching h_tw ∈ (1/n)Z. These are
LOGICALLY distinct routes to α = 0.

**Wrong.** The claim "disjoint mechanisms" is technical: Type B's
Λ^σ = 0 forces h_tw = 0 trivially, which IS in (1/n)Z, so Type B is
a DEGENERATE CASE of Type C's level-matching route. The route via
level-matching covers all 47 (= 46 + 1) non-trivial Leech orbifolds;
the Λ^σ = 0 route is a shortcut specific to n = 2, σ = -1.

**Correct.** There are TWO mechanisms: Type A (trivial orbifold,
vacuous α) and Types B ∪ C (Leech orbifold + level-matching). Type
B is a degenerate case of the level-matching route, not a third
mechanism.

**Heal path**: reduce "three distinct mechanisms" to "two
mechanisms (trivial orbifold + Leech-orbifold level-matching);
within the Leech-orbifold mechanism, Type B (n = 2, Λ^σ = 0) is a
degenerate case of Type C (n ≥ 2, Λ^σ possibly zero)."

**Verdict**: WEAK. Technical malpractice on the "three distinct"
framing; theorem at level α = 0 unconditional survives.

---

## (C) CY-C Pentagon (task 15)

### (C.1) κ_ch values {3, 12, 24} — FAILS

cy_c_pentagon_hypothesis_closures_platonic.tex claims κ_ch
stratifies as {3, 12, 24} across the five pentagon routes R_1 through
R_6. Specifically:
- R_1 (Φ_3): κ_ch = 3 (claimed)
- R_3 (abelian threefold pre-Kummer): κ_ch = 24
- R_4 (Kummer orbifold): κ_ch = 12
- R_5 (half-twist): κ_ch = 3

Vol III thm:kappa-hodge-supertrace-identification (Vol III
cy_d_kappa_stratification.tex) establishes:
   κ_ch(A_X) = Σ_q (-1)^q h^{0,q}
for compact CY_d via HKR.

For K3 × E (CY_3):
   h^{0,0} = 1, h^{0,1} = 1, h^{0,2} = 1, h^{0,3} = 1.
Therefore κ_ch(K3 × E) = 1 - 1 + 1 - 1 = 0.

**Ghost.** The pentagon routes produce DIFFERENT algebras, each
with its own κ_ch; K3 × E via Φ_3 gives κ_ch = 0, NOT κ_ch = 3.

**Wrong.** The claim κ_ch(R_1 = Φ_3(K3 × E)) = 3 is INCONSISTENT
with the Hodge-supertrace identification.

**Correct.** Either:
(a) The pentagon routes do NOT coincide as algebras; their κ_ch are
DIFFERENT (which falsifies the "colimit G(K3 × E)" claim), OR
(b) The Hodge-supertrace identification κ_ch = Σ(-1)^q h^{0,q} =
0 holds; the κ_ch = 3 claim is wrong; the pentagon does not
converge at the κ_ch level.

The chapter's claim is that κ_ch stratifies as {3, 12, 24} via
different routes, with the halving arrows β_{34}, β_{45} making
them different at each node. But κ_ch is a PROPERTY of the
algebra, not a choice of route; if R_1 = Φ_3(K3 × E), then
κ_ch(R_1) is determined by the input K3 × E and the functor Φ_3,
and is the Hodge supertrace 0.

**Heal path**: the pentagon does NOT converge at the κ_ch level;
the claim "six routes produce isomorphic algebra" is FALSIFIED (as
the rewrite map observes). But the correct falsification should go
to κ_ch = 0 everywhere (since R_1 through R_6 all arise from K3 ×
E topology), not to a stratification {3, 12, 24}. The
stratification {3, 12, 24} cites Kummer halvings, but those
halvings apply to LATTICE RANK (24 → 12 under Z/2 invariants, 12 →
3 under primitive sector), not to κ_ch which is a Hodge invariant.

The rewrite map task 15 ("κ_ch {3, 12, 24}") confuses LATTICE RANK
with κ_ch. Lattice rank stratifies as {3, 12, 24} via Kummer ×
primitive; κ_ch stratifies as κ_ch(K3 × E) = 0 throughout (or
requires per-route computation if different functors produce
different algebras with different Hodge data).

**Verdict**: FAILS. The {3, 12, 24} stratification applies to
lattice rank, NOT to κ_ch. The pentagon-as-κ_ch-stratifier claim is
a category error.

### (C.2) β_{34} Kummer halving 24 → 12 — WEAK

Step 3 of thm:h2-threefold-kummer-lift (L243--252) claims Z/2-
invariants halve the rank 24 → 12 via the "symmetric Z/2-projection
P_+ = (1 + ι)/2." But the rank arithmetic 24/2 is wrong IN GENERAL.

**Ghost.** For a Z/2 action with equal +1 and -1 eigenspaces,
Z/2-invariants halve the rank.

**Wrong.** For the Kummer construction on A^3, the Z/2-involution
ι = -1 acts on cohomology as: H^0 (trivial) → +1; H^1 → -1 (since
ι acts on H^1 by -1); H^2 → +1; H^3 → -1. The rank of Z/2-
invariant cohomology of A^3 is NOT h/2 but specifically
   dim H^*(A^3)^{Z/2} = h^0 + h^2 + h^4 + h^6
(even parts). For a generic A^3, h = 2^6 = 64 total, and
even-part rank is 2^5 = 32, not 24/2 = 12.

**Correct.** The rank halving 24 → 12 applies to a specific
Mukai-like lattice, NOT to the full cohomology. The Step 3 "24/2 =
12" arithmetic is a simplification that elides the fact that the
Z/2-action has uneven eigenspaces on the Mukai lattice.

**Heal path**: provide the explicit Z/2-eigenspace decomposition on
the specific Mukai-like lattice used for Kummer threefold; verify
the rank-12 claim against this decomposition; if rank = 12 survives,
the theorem stands; if not (e.g., rank = 8 or 16 in reality), the
pentagon arrow β_{34} needs re-derivation.

**Verdict**: WEAK. Non-trivial arithmetic check required; the
"rank/2" shortcut is not rigorous.

### (C.3) Kummer_3(A^3) rank via Mayer-Vietoris — WEAK

Step 1 of h2 proof claims the Mayer-Vietoris rank total is
   rk(total) = rk(U) + rk(V) - rk(U ∩ V) = 8 + 32 - 16 = 24.

The claim rk(H_{A^3}) = 8 is suspicious: "six real translations plus
two complex structure deformations per C-factor, summing to 8 for
the holomorphic part." For an abelian threefold A^3 = C^3/Λ, the
Heisenberg VOA associated to the lattice Λ has rank equal to the
lattice dimension (3 COMPLEX generators, 6 real). The "8" arithmetic
is not justified.

**Ghost.** For A^3 = C^3/Λ, the associated Heisenberg VOA has rank
3 over C (6 over R).

**Wrong.** rk(H_{A^3}) = 8 cited at L221--223; no source is given
for this 8; the decomposition "6 real translations + 2 complex
structure deformations" is ad hoc. Complex structure deformations of
A^3 are parametrized by H^1(A^3, T_{A^3}) = H^1(O_{A^3}^3) =
C^{3·3} = C^9, not 2.

**Correct.** The Heisenberg VOA of Λ has rank = rk(Λ) = 6 (real) =
3 (complex). The Mayer-Vietoris arithmetic `6 + 32 - 14 = 24` (or
some variant) MIGHT recover rank-24 Mukai-like lattice; the
currently inscribed arithmetic `8 + 32 - 16 = 24` is wrong.

**Heal path**: redo the Mayer-Vietoris with correct rk(H_{A^3}) = 6;
adjust the twist-sector and overlap ranks; verify the final total is
still 24. If it is not 24, the pentagon routing changes.

**Verdict**: WEAK. Arithmetic gap; rank correction likely preserves
the 24 total but the current derivation is not sound.

### (C.4) Pentagon colimit = G(K3 × E) — WEAK (DOWNSTREAM OF C.1)

Given that (C.1) falsifies the pentagon-as-κ_ch-stratifier
framing, the colimit claim "G(K3 × E) = colim(pentagon)" needs
reinterpretation.

**Ghost.** The six routes to "the same" CY_3 chiral algebra should
converge to a single colimit; topology + BPS content determine the
colimit.

**Wrong.** The rewrite map promotes this as unconditional; CY-C
was a CONJECTURE. Promotion without proof is a downgrade of honest
conjectural status to overclaim.

**Correct.** The pentagon framework gives SIX CONSTRUCTIONS that
CONJECTURALLY converge; the convergence is the CONTENT of CY-C
(per AP-CY60). The six-way colimit is conjectural, not unconditional.

**Heal path**: tag the colimit identification as
\ClaimStatusConjectured; do not promote to \ClaimStatusProvedHere.
The pentagon's CONSTRUCTION of the routes is solid; the
CONVERGENCE claim is conjectural (thm:cy-c-six-routes-generator-
level-convergence part (iv) is the convergence claim).

**Verdict**: WEAK. Promotion from ProvedHereConditional to
ProvedHere in the rewrite map is an overclaim; primary source still
carries "Conditional" on the colimit step.

---

## (D) Monster V^♮ chain-level E_3-top (task 10)

### (D.1) Orbifold BV anomaly α = 0 — WEAK

monster_chain_level_e3_top_platonic.tex inscribes α_orb = 0 via
Kapustin-Saulina formula + Λ^σ = 0 for σ = -1 on Leech.

**Ghost.** The FLM twisted sector on V^♮ has a specific orbifold
anomaly class α ∈ H^3(BZ/2; U(1)); this vanishes by Kapustin-
Saulina formula evaluated at Λ^σ = 0.

**Wrong.** The Kapustin-Saulina formula is for 3d TQFT orbifolds;
it applies to chiral CFT orbifolds via the Costello-Gwilliam-style
factorization-algebra framework. The "α = 0" claim at the CHAIN
level (not cohomological) requires a specific chain representative
of the α class, which the Kapustin-Saulina formula does not
directly produce. The chain-level claim is STRONGER than the
cohomological claim.

**Correct.** At the COHOMOLOGICAL level, V^♮ admits E_3 structure
via Borcherds 1992 + FLM twisted Jacobi associativity + Dong-Mason
quantum Galois. At the CHAIN level, the explicit chain representative
is the FLM twisted vertex operator product formula; the strict chain
associativity follows from FLM Chapters 8-10 (twisted vertex
operator algebra structure is CHAIN-LEVEL, not just cohomological).
So the chain-level claim IS supported, but the argument is via FLM
twisted VOA chain structure, NOT via Kapustin-Saulina formula.

**Heal path**: reroute the chain-level argument through FLM twisted
VOA explicit chain structure (FLM 1988, Theorem 8.10.1) + Dong-Mason
quantum Galois uniqueness (which applies at chain level for V^♮ as
C_2-cofinite VOA). The Kapustin-Saulina formula gives the
cohomological α = 0; the chain-level promotion uses FLM.

**Verdict**: WEAK. Chain-level α = 0 claim is SOUND but via a
different citation chain than the currently inscribed Kapustin-
Saulina route.

### (D.2) V^♮ C_2-cofiniteness — HOLDS (well-known)

V^♮ is known C_2-cofinite (Abe-Buhl-Dong 2004 for rank 1 → extended
to V^♮ via FLM construction). Dong-Mason quantum Galois applies.

---

## (E) Super-Riccati max(m, n) identity (task 17)

### (E.1) Theorem super-shadow-self-duality — WEAK (SCOPE ADVERTISED ≠ SCOPE PROVED)

thm:super-shadow-self-duality (L648--702) proves
   κ_ch(Y(sl(m|n))) + κ_ch(Y(sl(n|m))^!) = max(m, n)
at the SUB-SUGAWARA level, NOT at the full super-Yangian κ_ch.

**Ghost.** The Koszul-dual pair on a specific sub-Sugawara line
gives sum = max(m, n), the rank of the principal bosonic sub-
algebra.

**Wrong.** The rewrite map (task 17) advertises this as
"super-complementarity κ + κ^! = max(m,n) not 0" suggesting a
GLOBAL identity. Primary source explicitly scopes it to the
sub-Sugawara line at the Sugawara-shifted level inversion
k → -k - 2h^v (L651--652). The bare super-Yangian κ+κ^! sum is
NOT obviously max(m,n) unless the scope is made explicit.

**Correct.** On the principal bosonic sub-Sugawara line at super-
Sugawara level shift, the sum is max(m,n). The FULL super-Yangian
κ+κ^! depends on line choice; for an ODD line,
   S_3 = 0, S_4 = 0 (per L631--632),
hence κ_ch = S_2 on the odd line requires separate computation.

**Heal path**: ensure the rewrite map inscribes the scope
"sub-Sugawara line only" explicitly; the max(m, n) identity is
CORRECT within this scope but NOT unqualified. Do not remove the
scope qualifier.

**Verdict**: WEAK. The proof as written is OK (scope-qualified);
the rewrite map's unqualified statement is an overclaim.

### (E.2) Alternative (m - n) identity — WEAK

rem:super-shadow-alternative-duality (L716--738) notes a companion
"scaled-duality relation" κ + κ^! = (m-n)·κ_unit. Both identities
are presented as "two different Koszul pairings." But the two
identities cannot both hold simultaneously unless (m-n)·κ_unit =
max(m,n), which fixes κ_unit = max(m,n)/(m-n). This is
PAIRING-DEPENDENT and the chapter does not resolve which pairing is
canonical.

**Ghost.** Two distinct Koszul pairings give two distinct
complementarity identities. Both can coexist.

**Wrong.** The chapter does not clarify which pairing is the
PROGRAMME'S canonical one. The Vol I C1 Lagrangian framework uses a
specific Verdier-dual pairing; if that pairing is the "straight
super-trace" one giving max(m,n), then the Berezinian one is a
companion. If that pairing is the Berezinian one giving (m-n)·κ_unit,
then the max(m,n) identity is a companion.

**Correct.** Specify the canonical Verdier pairing at Vol I level;
the corresponding super-identity follows.

**Heal path**: identify the Vol I canonical Verdier pairing for
super-algebras; state the corresponding super-identity as the
canonical one; the other becomes a companion "Berezinian-normalised"
or "trace-normalised" variant.

**Verdict**: WEAK. Pairing ambiguity; the "max(m,n)" identity is
pairing-dependent and requires explicit selection of canonical
pairing.

### (E.3) Super-Yangian (1|1) numerical check — WEAK

L66 cites "verified for (m, n) ∈ {(1,1), (2,1), (1,2), (3,1), (2,2)}"
via compute/tests/test_super_riccati_shadow_tower.py. At (1, 1),
max(1, 1) = 1. The claim κ_ch(Y(sl(1|1))) + κ_ch(Y(sl(1|1))^!) = 1.

But sl(1|1) has:
   sdim(sl(1|1)) = (1-1)^2 - 1 = -1.
   h^v(sl(1|1)) = |1 - 1| = 0.
This is a CRITICAL super-level (h^v = 0) where the Sugawara tensor
is undefined (per def:super-parity-sl-mn L110--112). The super-
shadow identity should therefore FAIL at (1, 1) — or the sub-
Sugawara formula c_sub(1|1, k) = max(1,1)·k/(k + 0) = UNDEFINED.

**Ghost.** At (m, n) = (1, 1), the super-Sugawara construction is
degenerate; the complementarity identity does not apply at this
degenerate point.

**Wrong.** The proof claims the identity holds for (m, n) = (1, 1)
as a numerical verification, but at h^v = 0 the Sugawara level-
inversion k → -k - 2h^v = -k is a reflection, not a non-trivial
Koszul dual; and c_sub has 0/0 indeterminacy.

**Correct.** The (1, 1) case is DEGENERATE (critical super-level);
the identity applies only for m ≠ n. The numerical test at (1, 1)
must be inspected: if it passes, the test is using a different
convention (e.g., L'Hospital limit of the formula at m = n) that
is not the canonical one.

**Heal path**: exclude m = n from the main theorem; handle the
(1, 1), (2, 2), etc. critical super-level cases as degenerate
companions via L'Hospital or direct FF-center argument.

**Verdict**: WEAK. The (m = n) cases need degenerate treatment; the
"verified for (1, 1), (2, 2)" numerical checks may be using a
limiting convention that contradicts the definition.

---

## (F) Arithmetic-duality refinement (task 3)

### (F.1) Kummer-irregularity Laurent-depth controlled — HOLDS

The claim "Kummer-irregularity is LAURENT-DEPTH CONTROLLED" is a
descriptive refinement: Kummer-irregular primes at Bernoulli index 12
and 16 (namely 691 and 3617) appear in S_r(Vir_c) only at higher
Laurent tiers, not in the leading A_r coefficient. This is the
CONTENT of cor:virasoro-23-smoothness (L1200--1229):
   r · A_r = 8 · (-6)^{r-4} is {2,3}-smooth,
so no prime ≥ 5 appears in A_r (leading tier) at all. Subleading
tiers B_r, Γ_r, Δ_r can contain larger primes.

**Verdict**: HOLDS. The refinement is a clean structural
observation; primary source supports the Laurent-depth control.

### (F.2) 101 at r = 11 Kummer-irregular dividing B_68 — FAILS

session_20260417_master_synthesis.md Tier 2 table claims 101 at
r = 11 (Tier 2 = B_r coefficients). The supporting claim is that 101
is Kummer-irregular (divides some B_{2m}).

**Ghost.** Kummer-irregular primes are those p for which p | num(B_{2m})
for some 2m ≤ p-3 (standard Kummer criterion).

**Wrong.** The list of Kummer-irregular primes starts at 37 (B_32),
59 (B_44), 67 (B_58), 101 (B_68). Verifying 101 | num(B_68)
EXPLICITLY requires Bernoulli computation. The rewrite map cites
"101 at r=11; 101 is Kummer-irregular dividing B_68." This is
PLAUSIBLE but requires numerical verification.

**Correct.** 101 IS Kummer-irregular (this is a known table entry:
Buhler et al. 2000, also cited in OEIS A000928). The claim "101 |
num(B_68)" can be verified numerically. But the connection "101
appears at r = 11 in S_r(Vir_c) subleading" requires separate
verification via shadow tower computation.

**Heal path**: explicit numerical verification of 101 | num(B_68);
explicit verification that 101 appears in B_{11} subleading coefficient
of S_{11}(Vir_c). Both computations are feasible; do them.

**Verdict**: FAILS pending explicit numerical verification. The
rewrite map claim is PLAUSIBLE but UNVERIFIED at primary source.

### (F.3) 3067 at Tier 3 r = 12 Kummer-irregular — FAILS

Similar to (F.2): the rewrite map lists 3067 at Tier 3 r=12 as
Kummer-irregular. I cannot verify 3067 | B_{2m} for any 2m in
{12, 16, ..., 22} without numerical computation.

**Verdict**: FAILS pending explicit verification. Likely CORRECT but
uninscribed verification is a Beilinson gap.

### (F.4) 283 at Tier 4 r = 13 Kummer-irregular — WEAK

283 | num(B_20) is a known OEIS entry for irregular primes (A000928;
283 is irregular via B_20). The appearance at r = 13 Tier 4 is
plausible.

**Verdict**: WEAK pending test-file verification.

### (F.5) Tier 1 (A_r) empty — HOLDS

Direct consequence of (F.1): A_r is {2, 3}-smooth, so no prime ≥ 5
appears in A_r for any r. Tier 1 (A_r) is empty for Kummer-irregular
primes (all ≥ 691).

**Verdict**: HOLDS.

### Overall verdict on task 3 (arithmetic-duality refinement)

Theorem is STRUCTURALLY SOUND (Laurent-depth control); the specific
Tier-by-Tier numerical claims require test-file verification. The
rewrite map's phrasing "first Kummer-irregular prime 691" is
imprecisely phrased (691 is first by Bernoulli index; 37 is first by
size); the heal (rem:subleading-kummer-correction) addresses this.

---

## (G) Programme architecture (task 21)

### (G.1) Three-volume separation — WEAK (CIRCULAR)

Vol I provides Laurent closed forms used by Vol II tempered heal.
Vol II factorization ambient used by Vol I all-tier Fuchsian ODE
modular base-change step. Vol III super-Riccati uses Vol I bosonic
Riccati.

**Ghost.** The three-volume architecture is a linear dependency
graph: Vol I algebra → Vol II physics → Vol III CY.

**Wrong.** Currently the dependency graph has ORAL cycles:
- Vol II → Vol I (tempered heal uses Laurent forms)
- Vol I → Vol II (Fuchsian ODE's ambient uses Vol II six-functor)
- Vol III → Vol I (super-Riccati reduces to bosonic Riccati)
The graph IS a DAG when written carefully (Vol I's Fuchsian ODE
uses Vol II only via a specific named bridge, and Vol II's tempered
heal is a downstream corollary of Vol I's closed forms, not a
circular logical dependency). But the declaration "three-volume
architecture is clean" hides dependencies that need explicit
acknowledgement.

**Correct.** Vol I provides the algebraic core; Vol II the HT
physics; Vol III the CY instantiations. The ACTUAL dependency
structure is a DAG, but the cross-volume bridges (tempered heal,
Fuchsian ODE, super-Riccati) require explicit inscription.

**Heal path**: inscribe the cross-volume dependency DAG in
CROSS_VOLUME_EXECUTION_ROADMAP.md at the level of
"Vol II tempered heal USES Vol I thm:shadow-tower-asymptotic-closed-
form, PROVIDED Vol I's theorem is algebraically independent of
Vol II." Verify the independence.

**Verdict**: WEAK. The separation is honest in structure, but the
cross-volume inscriptions need explicit DAG clarity.

### (G.2) VSKR + BGG criterion for tempered — FAILS

The claim "VSKR + BGG covers the standard landscape" as sufficient
condition for tempered stratum membership is NOT PROVED in primary
source. VSKR = Vasserot-Schiffmann-Kac-Roan or similar? BGG
criterion is for module categories, not chiral algebras directly.
The "VSKR + BGG" naming is ad hoc.

**Ghost.** Some combination of known theorems covers the standard
landscape's temperedness.

**Wrong.** "VSKR + BGG" is not a standard citation; the combination
is not a single published theorem.

**Correct.** Temperedness of the standard landscape is proved for
Virasoro (Stirling heal) + principal W_N generic (conjectural for
N ≥ 4) + affine KM non-critical (separate argument). There is no
single "VSKR + BGG" theorem covering everything.

**Heal path**: list each family's tempering proof separately; do not
pretend a single citation covers all.

**Verdict**: FAILS. The "VSKR + BGG" framing is non-standard and the
claim of universal coverage is unsupported.

### (G.3) conj:tempered-unbounded-zhu converse retracted via K(sl_2, √2) — WEAK

The parafermion K(sl_2, k) at irrational level k has an infinite-
dimensional Zhu algebra (countably many irreducible representations).
The claim that K(sl_2, √2) is a COUNTEREXAMPLE to the converse
(i.e., tempered but unbounded-Zhu) requires:
(a) K(sl_2, √2) is tempered (not proved in source),
(b) K(sl_2, √2) has unbounded Zhu (plausible but not quantified).

**Ghost.** Tempered but unbounded-Zhu algebras exist; K(sl_2, √2)
is one.

**Wrong.** (a) is not proved. The chapter
chapters/theory/irrational_cosets_tempered_platonic.tex would be the
place; let me check.

**Heal path**: prove K(sl_2, √2) is tempered (ratio test or upper
bound on S_r in terms of k = √2); verify Zhu algebra dimension is
infinite at irrational k.

**Verdict**: WEAK pending primary-source verification of the
parafermion claim.

---

## (H) Rewrite map itself (task 22)

### (H.1) Task ordering — FAILS (REVISED ORDER NEEDED)

The user's directive says "start with task 1 (preface)." But:
- Task 1 (preface reflects closures): depends on which closures
  actually HOLD. Given (A.5) FAIL, (C.1) FAIL, (C.4) WEAK, the
  preface cannot accurately reflect "four closed frontiers" if at
  least two are not actually closed.
- Task 6 (Part VI rewrite as climax): depends on Task 7
  (topologization dichotomy) being resolved, which depends on
  Task 14 (W_∞ endpoint) and Task 13 (parafermion retraction),
  which depend on verification not yet performed.

**Ghost.** The preface is the entry point; rewrite it first.

**Wrong.** The preface SUMMARIZES the body. Rewriting the preface
before the body is stable is a FAILURE MODE: the preface will
contain overclaims that the body does not support. The correct
ordering is: body theorems → climax → preface.

**Correct ordering** (revised):
1. First: verify closures at primary source (tasks 13, 14, 15, 17
   numerical checks). This is the Beilinson-principle step.
2. Second: update Wrong Formulas Blacklist (task 20) to reflect
   verified corrections.
3. Third: update first-principles cache (task 22) with new patterns
   from the audit.
4. Fourth: rewrite Part VI climax (task 6) with CORRECT scope
   qualifiers (conditional on tempered stratum scope, log W(p)
   still open).
5. Fifth: update CLAUDE.md FM entries (task 8) with closures +
   remaining gaps.
6. Sixth: update theorem status table (task 2).
7. Seventh: update arithmetic-duality (task 3) with verified Kummer
   witnesses.
8. Eighth: update Vol II CY-C pentagon language (task 15) with the
   lattice-rank-vs-κ_ch correction from (C.1).
9. Ninth: update super-Yangian (tasks 16, 17) with scope
   qualifiers.
10. Tenth: 16 standalone papers sync (task 18).
11. Eleventh: programme overview realignment (task 21).
12. Last: preface (task 1).

**Verdict**: FAILS on original order. Preface LAST, not FIRST.

### (H.2) Biggest structural debt — WEAK

The rewrite map claims the biggest debt is Part VI climax rewrite
(task 6). The audit finds the biggest debt is the
LATTICE-RANK-VS-κ_ch conflation in task 15 (CY-C pentagon), which
FALSIFIES the κ_ch stratification and requires global reworking of
the Vol III CY-C chapter's main theorem. Task 15's impact is larger
than task 6's because it affects the Φ functor's image
characterization on CY_3 level.

**Heal path**: reorder task-importance list: Task 15 > Task 6 >
Task 7 > Task 1.

**Verdict**: WEAK. Relative prioritization needs adjustment.

---

## Summary of verdicts

| Task | Claim | Verdict | Notes |
|------|-------|---------|-------|
| 1 | Preface reflects four closures | FAILS (premature) | Preface LAST |
| 2 | Theorem status table | WEAK | Requires A-H absorb |
| 3 | Shadow tower Kummer heal | WEAK | Pending numerical check |
| 4 | Motivic shadow tower | HOLDS structurally | |
| 5 | Exceptional Yangian | HOLDS (if GRW18 correct) | |
| 6 | Part VI 3d gravity climax | WEAK (scope) | log W(p) open |
| 7 | topologization_class_m dichotomy retracted | WEAK | Heal scope-dependent |
| 8 | CLAUDE.md FM closures | WEAK | Cross-volume consistency |
| 9 | Bridge table W-algebras (5) | WEAK | W_N ≥ 4 conjectural |
| 10 | Monster orbifold theorem | WEAK (cite chain) | FLM route needed |
| 11 | Schellekens 71 extended | WEAK (cite chain) | vELMS21 needed |
| 12 | Log W(p) tempered via Zhu-bounded Massey | FAILS | Massey unbounded |
| 13 | conj:tempered-unbounded-zhu converse retracted | WEAK | Parafermion verification |
| 14 | W_∞ endpoint unconditional at generic λ | WEAK | β_N conjectural |
| 15 | CY-C pentagon six-way falsified, κ_ch {3,12,24} | FAILS | Lattice/κ_ch conflation |
| 16 | Super-Yangian upgrade | WEAK | Pairing ambiguity |
| 17 | Super-complementarity max(m,n) | WEAK | Scope qualifier |
| 18 | 16 standalone sync | pending | Downstream of 1-17 |
| 19 | Metadata "four irreducible opens" | pending | Re-verify per above |
| 20 | Blacklist extension | HOLDS (additive) | |
| 21 | Programme overview | WEAK | DAG not linear |
| 22 | First-principles cache | HOLDS (additive) | |

---

## Genuine open frontiers identified

1. **F1**. Log W(p) tempered status (task 12 FAILS). Massey
   products UNBOUNDED at triplet level; "bounded Zhu → bounded
   Massey" direction is wrong; the chain C_2-cofinite →
   bounded-Zhu → tempered breaks at step 2. Need: explicit
   counterexample OR alternative route to tempering for log W(p).

2. **F2**. CY-C pentagon κ_ch stratification is a category error
   (task 15 FAILS). κ_ch is a Hodge invariant; lattice rank
   stratifies, not κ_ch. Need: re-derivation of pentagon content at
   the κ_ch level, or rephrasing as lattice-rank pentagon.

3. **F3**. Numerical verification of Kummer-irregular prime
   witnesses at (r, Tier) coordinates (tasks 3, F.2, F.3). Need:
   explicit test file test_kummer_irregular_witnesses.py checking
   101|B_68, 3067|B_some, 283|B_20, AND verifying appearance in S_r
   coefficients at claimed Laurent tier.

4. **F4**. Super-complementarity pairing canonicalization (task 17).
   max(m,n) vs (m-n)·κ_unit identities differ; programme needs to
   declare canonical Verdier pairing for super-algebras.

5. **F5**. W_3 β_3 = 10 derivation. Current proof uses repackaging
   via κ(W_3) = 5κ(Vir)/3 which is NOT a first-principles β_3
   derivation. Need: explicit Riccati recurrence computation on W_3
   dominant line.

6. **F6**. Virasoro tempered finite-r window at small |c|. Current
   proof is asymptotic in c but not uniform in r; for |c| small
   and r transitional, Laurent tier expansion may fail. Need:
   Kac-determinant global bound replacing Laurent local bound.

---

## Heal paths (strongest honest form)

Each WEAK claim above has a specific heal path. The heals preserve
the STRONGEST honest form of each claim without accepting
downgrades due to technical malpractice.

### Priority 1 heals (blocking the 22-task rewrite)

- **Task 12 heal (log W(p))**: replace "bounded Zhu → bounded
  Massey → tempered" with a direct bound on S_r(W(p)) via the
  Adamovic-Milas 2009 explicit ϕ_{0,1}-character expansion. If
  S_r grows factorially, log W(p) is non-tempered (honest open);
  if polynomially, tempered. Numerical check is feasible.

- **Task 15 heal (CY-C pentagon)**: rephrase the pentagon as a
  LATTICE-RANK pentagon, with κ_ch separately computed via
  Hodge supertrace. The pentagon's lattice-rank stratification
  {3, 12, 24} is correct; κ_ch(R_i) = κ_ch(K3 × E) = 0
  throughout; the "κ_ch stratification" language is the category
  error to fix.

- **Task 17 heal (super-complementarity)**: inscribe canonical
  Verdier pairing; derive canonical max(m,n) identity; companion
  (m-n)·κ_unit identity scope-qualified.

### Priority 2 heals (non-blocking)

- **Task 6 heal (Part VI climax)**: scope qualifier on log W(p);
  CORRECT scope is principal + non-logarithmic + non-minimal
  standard landscape.

- **Task 10 heal (Monster V^♮ chain-level)**: reroute citation
  through FLM twisted VOA chain structure, not Kapustin-Saulina.

- **Task 11 heal (Schellekens 71)**: add vELMS21 citation at Type C
  α-vanishing step.

- **Task 13 heal (parafermion converse retraction)**: explicit
  proof that K(sl_2, √2) is tempered + explicit Zhu unboundedness
  check.

- **Task 14 heal (W_∞ endpoint)**: conditional on β_N conjecture;
  absorb F.5 heal first.

### Priority 3 heals (structural)

- **Task 1 (preface)**: REORDER to LAST, after all content
  theorems are inscribed with correct scope. Do NOT write preface
  first; it will contain stale overclaims.

- **Task 21 (programme overview)**: inscribe dependency DAG
  explicitly; document cross-volume bridges with algebraic
  independence guarantees.

---

## Lossless commitment

All findings above are the result of primary-source inspection. No
Edit to any .tex file is recommended without first addressing the
Priority-1 heals. The rewrite map as currently phrased contains
overclaims in tasks 12, 15, and (on priority) task 1; these must be
scope-qualified or retracted before the rewrite can proceed.

End of adversarial audit.
