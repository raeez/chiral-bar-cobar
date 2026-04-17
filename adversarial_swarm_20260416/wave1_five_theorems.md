# Wave 1 — Five Theorems Modular Koszul: Adversarial Audit

Author of audit: adversarial referee role, against Vol I main pillar.
Target files (line numbers below refer to these unless stated otherwise):
- `standalone/five_theorems_modular_koszul.tex` (T1–T5 statements; the
  pillar in survey form)
- `chapters/theory/higher_genus_complementarity.tex` (proofs of
  Theorem B, C at higher genus)
- `chapters/theory/chiral_hochschild_koszul.tex` (proof of Theorem H)
- `chapters/theory/e1_modular_koszul.tex` (E_1 versions A^{E_1}–H^{E_1})
- `chapters/theory/en_koszul_duality.tex` (E_n bridge theorems)
- `chapters/theory/bar_cobar_adjunction_inversion.tex`,
  `chiral_koszul_pairs.tex` (anchor proofs of A and B at genus 0)

Naming: I follow the standalone file. T1 = Theorem A (bar-cobar
adjunction & Verdier intertwining), T2 = Theorem B (bar-cobar
inversion on the Koszul locus), T3 = Theorem C (Lagrangian
complementarity), T4 = Theorem D (genus universality), T5 = Theorem H
(polynomial Hilbert series for chiral Hochschild). Proposition
"Complementarity sums" (line 908) is treated as an addendum to T3.

---

## Section 1. One-paragraph triage

**T1 (Theorem A: bar-cobar adjunction + Verdier intertwining).**
Status: **NEEDS-TIGHTENING**. The adjunction half is solid (it is
formal modular operad / twisting morphism content; matches Loday–Vallette
Ch. 2 in chiral form). The Verdier intertwining half
`D_Ran B(A) ≃ A^!_∞` is presented as part of the same theorem with
full ProvedHere force, but the proof sketch (`five_theorems_modular_koszul.tex`
L684–705) reduces to a "key identity" `D_Ran T^c(s^{-1}\bar A) ≃ T(s
H^*(B(A))^∨)` that is asserted with no proof — it is the
Francis–Gaitsgory chiral Koszul duality theorem at genus 0 in
disguise, but the chain-level Verdier-on-Ran(X) compatibility with the
PBW filtration ("filtered comparison lemma", Step 4) is the
load-bearing nontrivial input and is referenced rather than proved
here. **Strongest reachable form**: split T1 into T1a (adjunction,
unconditional, ProvedHere) and T1b (Verdier intertwining at the
cohomology level on the Koszul locus, ProvedElsewhere via FG12 + a
spelled-out filtered-comparison lemma); state the chain-level Verdier
intertwining **with** A^!_∞ explicitly as a homotopy-Koszul-dual
factorization algebra (not just a "factorization algebra produced by
applying D_Ran"), with hypotheses naming PBW-completeness and
filtration boundedness.

**T2 (Theorem B: bar-cobar inversion).**
Status: **STRONG with one scope tightening required**. Genus 0 is
proved. The genus-g claim (T2.ii) is now correctly fenced behind
"diagonal Ext vanishing on fibers of the universal curve" plus the
landscape verification (Heisenberg / KM at generic level / Vir at
generic c / principal W_N / lattice). The actual proof in
`higher_genus_complementarity.tex` (L4408–4465) is a clean
SGA4-Expose-IX inductive argument: open-stratum QI from PBW
concentration on each fiber + SGA4 constructibility-zero-stalk
argument, then boundary QI by induction + Künneth for factorization
algebras, then extension across boundary by the cone-localization
triangle. **The single hidden hypothesis** that needs to be raised
into the statement: the SGA4 IX.2.14 step (open-stratum QI from
fiberwise QI) requires the cone of psi_g to be a *constructible*
complex on U_g; this is asserted by reference to "Step 2 of
Theorem~\ref{thm:ss-quantum}" but is precisely the place where
"complete with finite-dimensional graded bar pieces" must be in the
hypothesis. **Strongest reachable form**: strengthen by tagging
finite-dim-per-bar-degree as a standing assumption on the modular
pre-Koszul algebra; the theorem then becomes unconditional on the
landscape.

**T3 (Theorem C: Lagrangian complementarity).**
Status: **NEEDS-TIGHTENING**. Three parts of unequal strength:
(C1) eigenspace decomposition is correctly downgraded to "in the
coderived category" / proved chain-level; (C2) cohomological
Lagrangian decomposition is *claimed* "proved for g≥1" but the
Lagrangian content (perfect duality `Q_g(A) ≃ Q_g(A^!)^∨[-(3g-3)]`)
hides a strong Poincaré–Verdier hypothesis on FM-compactifications
that is invoked but not isolated as a lemma in the standalone; (C3)
shifted-symplectic upgrade is conditional. The Proposition
"Complementarity sums" (L908–938) is also load-bearing and contains
a serious arithmetic problem (see §2.T3 below, point 4 — the BP
"self-dual" point). **Strongest reachable form**: keep T3.C1 as
ProvedHere; restate T3.C2 as "proved on the standard landscape +
under explicit Verdier-pairing hypothesis"; keep T3.C3 as conditional;
**downgrade the BP and W_N entries of the complementarity-sum
proposition to "where defined"**, since the BP "self-dual k = -3"
contradicts the BP central charge formula (which has a pole at k=-3),
and the W_N conductor formula `K = N-dependent` is a placeholder, not
a closed expression.

**T4 (Theorem D: genus universality).**
Status: **STRONG (genus 1) and NEEDS-TIGHTENING (all genera)**. T4.i
(genus 1) is unconditional and survives. T4.ii (uniform-weight, all
genera) is supported by two "independent" proofs (Proof A:
GRR/Arakelov–Faltings, Proof B: clutching) — but the two proofs
share a hidden assumption: that the *scalar virtual class* of the bar
complex factors as `kappa(A) · [E]`, which is exactly the
uniform-weight reduction. Both proofs are valid given that input;
neither proves the input. The clutching-uniqueness gap, claimed
"resolved" by Remark `rem:clutching-gap-resolved`, is in fact still
present: the resolution argument says U_g (the relevant subspace) is
one-dimensional on the uniform-weight lane "because the scalar
channel produces only Hodge bundle classes" — but this is a
*restatement* of the conclusion, not an independent verification. T4.iii
(multi-weight) correctly carries the cross-channel correction tag.
**Strongest reachable form**: re-frame T4.ii so that the
*uniform-weight* hypothesis is explicitly the input and Proofs A/B are
two derivations of the *same* identity from the uniform-weight virtual
class. Add as a separate proposition the W_3 explicit cross-channel
formula `(c+204)/(16c)` (already proved in
`higher_genus_modular_koszul.tex` L22669) — this is the strongest
honest statement: T4 + a sharp negative result (multi-weight families
*do* receive corrections, and we compute the first one).

**T5 (Theorem H: polynomial Hilbert series).**
Status: **STRONG** in cohomological amplitude; **NEEDS-TIGHTENING in
"polynomial growth" and "family list"**. The amplitude bound
`ChirHoch^n(A) = 0 for n ∉ {0,1,2}` is proved cleanly twice
(`chiral_hochschild_koszul.tex` L1092–1115 spectral sequence;
L1163–1224 deformation-theoretic) — both are short, both are
correct. The Hilbert polynomial `1 + dim ChirHoch^1 · t + dim Z(A^!) · t^2`
follows from Koszul duality applied at degrees 0, 1, 2 (clean). The
family-list specialization (Heisenberg `1+t+t²`; KM `1+dim(g) t+t²`;
Vir `1+t²`; W_N `1+t²`; BP `1+t+t²`) is asserted in the standalone but
its single-line "proof architecture" (L1469–1485) is a hand-wave that
"the descent lemma reduces Theorem H to the Verdier intertwining" —
this is correct in spirit but the concrete `dim ChirHoch^1(V_k(g)) = dim(g)`
identification is not proved in any file I found and contradicts a
classical fact (see §2.T5, point 3). The critical-level escape clause
(L1463–1465) is correctly carved out. **Strongest reachable form**:
state T5 as proved for the *amplitude* and *palindromicity*, and
explicitly state the family Hilbert series as a *proposition* with
case-by-case verifications — and **fix Vir vs W_N**: the
ChirHoch^1(Vir_c) = 0 entry is correct only at *generic* c (the
minimal-model values are excluded already); the W_N entry needs the
same caveat.

---

## Section 2. Per-theorem detailed analysis

### T1 — Theorem A: bar-cobar adjunction + Verdier intertwining
*(`five_theorems_modular_koszul.tex` L622–719; proof L663–705)*

**Attack.** The statement bundles two genuinely distinct results
under one ProvedHere tag:
(i) the chiral analog of the LV12 bar-cobar adjunction (formal,
mostly trivial after the right operadic setup);
(ii) the chiral Verdier intertwining `D_Ran B_X(A) ≃ A^!_∞`,
which is the chiral Koszul duality theorem of Francis–Gaitsgory.

The proof sketch's Step 3 (L684–697) writes
`D_Ran(T^c(s^{-1}\bar A)) ≃ T(s (H^*(B(A)))^∨)`
and treats this as a known identity of factorization sheaves. This
needs proof: passing from a cofree coalgebra in factorization-sheaf
language to a free algebra on the linear dual *of cohomology*
silently requires (a) the FG12 chiral Koszul duality of the bar, and
(b) the bar spectral sequence collapse — i.e. it presupposes the
Koszul condition that the theorem is supposed to be applied under, and
in fact is only true *cohomologically*, not chain-level. A sharp
referee will say: the chain-level statement `D_Ran B(A) ≃ A^!_∞`
requires `A^!_∞` to be the *homotopy* Koszul dual — but the standalone
file does not define `A^!_∞` (it is named once at L612 and once at
L656; no construction).

The proof Step 4 ("filtered comparison lemma") is the actual
nontrivial content and is referenced rather than proved. The
statement attributed to it ("the PBW spectral sequence is compatible
with the Verdier functor") is correct but is the chiral analog of a
delicate construction (cf. Positselski's coderived theory, used
elsewhere in this manuscript).

**Defense / repair.** Both ingredients are real theorems. The repair
is structural: separate (i) and (ii) into clauses with separate
status:
- T1a (adjunction): ProvedHere, by the universal property of bar-cobar
  in the chiral / factorization setting (formal).
- T1b (Verdier intertwining at cohomology level on the Koszul locus):
  ProvedElsewhere via FG12 + the explicit filtered-comparison lemma
  to be inserted as a new lemma (it already exists in spirit at
  `bar_cobar_adjunction_inversion.tex` L1671–1681 as the "coderived
  bar-degree filtration").
- T1c (chain-level Verdier intertwining via `A^!_∞`): ProvedHere
  *conditional* on (a) PBW boundedness and (b) finite-dim graded bar
  pieces, with `A^!_∞` defined as the cone-construction homotopy
  Koszul dual.

**Scope.** Standing hypotheses needed in the statement that are
currently in the proof:
- `A` is augmented and complete with respect to the augmentation
  ideal;
- bar pieces are finite-dimensional in each conformal weight;
- the PBW filtration is bounded below and complete.

**Independent verification.** The Heisenberg example
(`ex:thmA-heis`, L707–719) is computational and correct *up to one
issue*: the claim `kappa(H_k^!) = -k` (line 718) requires interpreting
`Sym^ch(V*)` curved at `m_0 = -k·omega` as carrying a modular
characteristic, which is a subtle thing for a curved object (its bar
homology is genuinely deformed). For this independent verification to
hold, one needs `kappa` to be definable for curved objects via the
appropriate (negative) cyclic refinement; this is treated in
`chiral_hochschild_koszul.tex` (the cyclic L_∞ structure), but the
cross-reference is missing from the standalone.

A genuinely *independent* test: compute `kappa(H_k^!)` directly from
the complementarity Lagrangian decomposition Theorem C
(`H^*(\Mbar_g, Z_{H_k})` as a sum of `Q_g(H_k) ⊕ Q_g(H_k^!)`) at
g=1, where the answer is forced by Verdier symmetry to be `-k`. This
gives an independent path that does not invoke the Sym^ch curved
structure.

**Counterexample candidates.** At critical level k = -h^v of an
affine KM, the Koszul condition fails (Feigin–Frenkel center is
infinite-dim), so T1 does not apply — already noted at
`five_theorems_modular_koszul.tex` L1463–1465. **Genuine boundary case
to test**: `Vir` at c = 0 (the trivial representation) — here the
algebra degenerates and the "augmentation ideal" has questionable
dimension. The Hilbert series `1+t²` of Theorem H is fine but the
Verdier intertwining of T1 needs c ≠ 0 for the strict-dual `(c, 26-c)`
involution to be non-degenerate; should be flagged.

### T2 — Theorem B: bar-cobar inversion
*(`five_theorems_modular_koszul.tex` L735–836; full proof in
`higher_genus_complementarity.tex` L4408–4465 + L4317–4390)*

**Attack.** The genus-0 case is solid. The genus-g case has three
spots where a referee will push:

1. *Open-stratum QI* (`lem:higher-genus-open-stratum-qi`,
`higher_genus_complementarity.tex` L4317): the proof asserts that
the cone of `j_g^* psi_g` is *constructible* and applies SGA4
IX.2.14. Constructibility is invoked via "established in the proof of
Theorem~\ref{thm:ss-quantum}, Step~2" — this back-reference is the
single point where the otherwise clean argument depends on a
nontrivial finiteness input that is buried in another theorem's
proof. The referee will demand this be promoted to a standing
hypothesis.

2. *Boundary QI* (`lem:higher-genus-boundary-qi`, L4366): claims that
the restriction of psi_g to a boundary stratum factorizes via nodal
gluing into lower-genus pieces, by Künneth for factorization algebras
"at nodes". Künneth at nodes is not the same as plain Künneth: a node
is a *factorization*-singular point, and the local structure there
involves the chiral envelope of A at the node, which requires
A to be quasi-coherent/D-module-flat in a specific sense. This
hypothesis (smoothness of the node-restriction) is not in the
hypothesis of the lemma.

3. *Mayer–Vietoris over the boundary* (L4451–4457): the argument
that "QI on each stratum + iterated extensions over deeper strata =
QI on all of ∂Mbar_g" is correct in principle but relies on the
boundary being a *strict* normal crossings divisor of Mbar_g (with
only standard self-intersection at higher codimension). This is
true (Knudsen). The proof should cite Knudsen explicitly.

**Defense / repair.** All three points have known fixes; none is
fatal:
1. Make "complete with finite-dim graded bar pieces" a standing
   hypothesis of "modular pre-Koszul chiral algebra" (currently this
   only appears in the coderived clause of
   `thm:bar-cobar-inversion-qi`, L1656).
2. Add a node-flatness hypothesis (or, equivalently, restrict to
   "modular pre-Koszul chiral algebra of finite type"). All standard
   landscape examples satisfy this.
3. Cite Knudsen's stratification.

**Scope.** Statement (T2.ii) is correctly "on the modular Koszul
lane". The "for the standard landscape, the Ext vanishing holds
unconditionally" claim (L760–764) is supported by
`thm:pbw-allgenera-{km,virasoro,principal-w}` and
`thm:heisenberg-higher-genus`, which I confirmed exist and are tagged
ProvedHere. The lattice case is invoked in T2 but I did not find a
matching `thm:pbw-allgenera-lattice` — likely subsumed in
free-fields (`chapters/examples/free_fields.tex`). **Action item**:
verify a lattice-VOA PBW theorem at all genera is named and
referenced.

**Independent verification.** Genus-0: Heisenberg `H_k` worked out
explicitly (L815–822). Genus-g: the Heisenberg case
`thm:heisenberg-higher-genus` provides an independent computation via
Fock-space methods. Affine KM at generic level can be cross-checked
against Frenkel–Ben-Zvi / Beilinson–Drinfeld. **Suggested independent
source**: compare against the FG12 Selecta Math paper, which proves
genus-0 chiral Koszul duality for Lie-type algebras. The genus-g
extension here goes beyond FG12, so Heisenberg + KM + Vir/W are the
independent verifiers.

**Counterexample candidates.** Admissible-level affine quotients
`L_k(g)` at `k = -h^v + p/q`: known to *fail* T2 because the PBW
filtration breaks (null vectors). The remark at
`bar_cobar_adjunction_inversion.tex` L1693–1707 correctly notes this
and routes them through the coderived statement. This is the right
boundary; T2 should not be tested at admissible levels.

### T3 — Theorem C: Lagrangian complementarity
*(`five_theorems_modular_koszul.tex` L858–896; proof in
`higher_genus_complementarity.tex` L526–608; complementarity sums
prop. at L908–938)*

**Attack 1 — the eigenspace decomposition.** T3.C2 says
"Lagrangian eigenspace decomposition (proved for g ≥ 1)". The
H-level decomposition is `C_g ≃ Q_g(A) ⊕ Q_g(A^!)` (L548–552) where
`Q_g(A) := fib(σ - id)` and `Q_g(A^!) := fib(σ + id)`. Calling the
+1 eigenspace `Q_g(A)` and the -1 eigenspace `Q_g(A^!)` is a
*choice*; the actual identification of the +1 eigenspace with the
"deformation complex of A" (vs the -1 eigenspace, the "obstruction
complex") is the load-bearing content. The proof cites
`Lemma involution-splitting (a,c)` for the decomposition (formal:
splitting via projectors `(1±σ)/2` in characteristic 0) and Verdier
duality for the perfect-pairing clause. The naming
`Q_g(A) = "deformation"` vs `Q_g(A^!) = "obstruction"` is asserted
but not proved here.

**Defense.** This naming is justified by Theorem H's
deformation-obstruction exchange (`cor:def-obs-exchange-genus0` in
`chiral_hochschild_koszul.tex` L1283–1294, which proves
`ChirHoch^2(A) ≅ ChirHoch^0(A^!)^∨ ⊗ ω_X` at genus 0). The genus-g
analog is asserted at L1296–1298 and is the actual T3 statement.
Repair: explicitly cite the genus-0 corollary and state the genus-g
identification of `Q_g(A)` with deformations, `Q_g(A^!)` with
obstructions, as a *theorem* (not a notation choice).

**Attack 2 — perfect duality for g ≥ 1.** The pairing has degree
`-(3g-3)`, which is the dimension of `Mbar_g` for g≥2 but is
**positive** at g=1: -(3·1-3) = 0. This is correct (PTVV: the shift
is `2 - dim(Mbar_g)`, which is `-(3g-3)` at the relevant level). At
g=2 the shift is -3, at g=3 it is -6, etc. The statement is
internally consistent.

**Attack 3 — Heisenberg base case.** The complementarity sums
proposition (L908–938) computes `kappa(H_k) + kappa(H_k^!) = k - k = 0`,
matching K=0. This is consistent with the example. But the W_N entry
"K is nonzero and N-dependent" (L933) is a placeholder, not a closed
formula. For W_3 the table at L2247 says K = 250/3, and for general
W_N no formula is given. **Repair**: state the W_N conductor formula
explicitly, or restrict the claim to "W_N has K computable per N".

**Attack 4 — the Bershadsky–Polyakov self-dual point claim
(CRITICAL).** The standalone file (L2532–2554) computes:
- `c(BP_k) = 2 - 24(k+1)²/(k+3)`
- `kappa(BP_k) = c/6`
- `K(BP) = kappa(BP_k) + kappa(BP_{-k-6}) = 98/3` (Koszul involution
  is `k ↦ -k - 6`)
- "self-dual level k = -3, with kappa(BP_{-3}) = 49/3"

**The claim that k = -3 is a self-dual point is mathematically
incoherent**: the Koszul involution is `k ↦ -k-6`, with fixed point
`k = -3`. But `c(BP_{-3}) = 2 - 24·4/0 = ∞`. The central charge has a
pole at k = -3, so kappa(BP_{-3}) = c/6 is undefined. The statement
"kappa(BP_{-3}) = 49/3" can only be obtained if you compute
`(kappa(BP_k) + kappa(BP_{-k-6}))/2` and take the limit k → -3 on the
sum (which equals 98/3, hence "average" 49/3) — but that is **not the
value of kappa at the fixed point**, it is the symmetric mean of two
divergences cancelling.

I numerically verified the conductor: c(0) = -6, c(-6) = 202, sum
196 ✓; c(1) = -22, c(-7) = 218, sum 196 ✓. So `K_BP = 196` (and
hence `kappa-conductor = 98/3`) is correct **as a meromorphic
identity in k**, but the "self-dual point" at k=-3 is a removable
singularity of the *sum*, not a value at which BP is genuinely self-dual.

**Repair**: rewrite L2551–2554 as: "The Koszul involution is k ↦
-k-6 with fixed point k = -3. At this level, c(BP_k) has a simple
pole; the modular characteristic kappa(BP_k) = c/6 is therefore not
defined at k = -3 in the naïve sense. The complementarity conductor
K = c(k) + c(-k-6) = 196 is a polynomial identity in k that extends
across the pole, but BP_{-3} itself is not a chiral algebra in the
standard sense (the simple quotient is one-dimensional or the algebra
collapses)." Reference Adamović–Milas or Arakawa for the correct
status of BP at k = -3.

**Independent verification.** For Vir at c=13 the symmetry
`kappa = kappa' = 13/2` is a genuine self-dual statement (no pole in c,
c=13 is a regular value). For BP, no genuine fixed-level self-dual
algebra exists; replace the false self-dual claim with the regular
statement. For W_N a similar check is needed: the involution is
`c ↦ ?`; the standalone does not state it. (Likely
`c ↦ K_N - c` for some N-dependent K_N, but this should be made
explicit.)

**Counterexample candidates.** The "K family-dependent" statement
(L906) is correct in spirit but the full landscape table at
`tab:census` (L2119) has `K = N-dep.` for W_N — placeholder. To
genuinely defend against a referee, supply the formula
`K(W_N) = 2c · (H_N - 1) − [something fixed]` or equivalent.

### T4 — Theorem D: genus universality
*(`five_theorems_modular_koszul.tex` L984–1029, with the multi-weight
clause at L1018–1027; proof of the scalar key proposition L1155–1355)*

**Attack 1 — hidden uniform-weight assumption in Proof A (GRR).**
Step A1 (L1185–1202) writes the scalar virtual class as
`[B_scalar^(g)(A)]^vir = kappa(A) · [E]`. This assumes the bar
complex on a *fixed* curve has a one-dimensional algebraic factor
("the scalar channel") tensored with the de Rham complex of the
curve. This step *is* the uniform-weight reduction: if the algebra
has multiple generators of distinct weights, the geometric factor is
not just `H^0(Σ_g, ω)` but a sum over weights, and the virtual class
acquires cross-weight Hodge bundles (`R^0 π_* ω^{⊗h}`). This is
correctly noted at L1334–1340 ("no higher Hodge bundles
`R^0 π_* ω_π^{⊗h} with h ≠ 1` enter") but the *justification* for
this exclusion is exactly the uniform-weight hypothesis being assumed
in disguise.

**Defense.** Proof A is honest *given* the uniform-weight reduction;
the GRR-Mumford-Arakelov–Faltings chain is correct, only what
ingredient feeds in is at issue. Repair: rename Proof A's Step A1 to
"the uniform-weight virtual class identity" and cite it as a
*lemma* (separately stated; on the uniform-weight lane each
generator contributes `kappa_i · [E]` and the sum is
`kappa · [E]`).

**Attack 2 — the two proofs are not independent.** Proof B
(clutching) at L1259–1344 also uses the uniform-weight reduction (at
L1331–1340: "On the uniform-weight lane, U_g is the one-dimensional
tautological line"). So Proof A and Proof B both assume the same
uniform-weight virtual class identity. They differ in what they do
*after* assuming it: Proof A goes through GRR + Arakelov–Faltings
(to compute `c_g(E)`), Proof B goes through clutching + Whitney sum
formula + Faber–Pandharipande to integrate `lambda_g`. These are
genuinely independent *post*-input arguments, but the input is the
same. The remark at L1346–1354 ("the two proofs have no logical
dependency on each other") is too strong; they share the uniform-weight
virtual class input.

**Defense.** Two derivations of the same identity from a shared input
is still valuable (it doubles the chance of catching arithmetic
errors and verifies the GRR computation against Faber–Pandharipande
independently). Repair: weaken the "two proofs" remark to "two
independent derivations of the conclusion *given the uniform-weight
virtual class*"; this is honest and still strong.

**Attack 3 — clutching star-product computation (L1296–1301).** The
displayed identity
`(κλ_{g_1}) ⋆ (κλ_{g_2}) = (1/κ) · κλ_{g_1} · κλ_{g_2} = κ · λ_{g_1}λ_{g_2}`
uses the propagator inverse `η^{-1} = 1/κ` to absorb one factor of κ.
This is correct in the convention but **κ = 0 is a singular case**:
the propagator inverse is undefined at the critical level. Critical
level is exactly where Koszulness fails (see remark at
`five_theorems_modular_koszul.tex` L1463–1465 inside Theorem H), so
this is not a *new* obstruction, but the proof should *say* "for
κ ≠ 0; at κ = 0 (critical level / class L) Theorem D collapses to
genus 1 only".

**Defense.** Class L (κ = 0) is handled by separate analysis (single
Massey at degree 3, no nonlinear genus tower); the all-genera result
is vacuous there. Repair: add a κ ≠ 0 hypothesis to T4.ii or note
the κ = 0 case separately.

**Attack 4 — multi-weight cross-channel correction is now provable
to be nontrivial (not a future open problem).** The standalone
states T4.iii with `δ F_g^cross` as an undetermined correction. But
`higher_genus_modular_koszul.tex` L22596 (Theorem
`thm:multi-weight-genus-expansion`) **proves** the W_3 explicit
formula `δ F_2(W_3) = (c+204)/(16c)`. This is a stronger negative
result than the standalone admits. **This should be promoted to a
visible part of T4**: T4.iii is not just "the diagonal is universal,
the cross-channel is computable" — it is "the cross-channel is
*nonzero* for W_3 at g=2, and we have its closed form".

**Independent verification.** The W_3 formula
`δ F_2(W_3) = (c+204)/(16c)` is independently verifiable against the
W_3 chiral partition function on a genus-2 curve (computable from
DS-reduction of affine sl_3 + KZB at genus 2). Recommended test path:
match against Mathieu–Sevrin or against the Hosono–Lian–Yau /
Bouchard–Mariño chiral genus-2 partition function for W_3.
**Genuine independent source available**: yes, via DS reduction of
the genus-2 sl_3 KZB partition function. This is not in the
manuscript and would be a high-value addition for the independent
verification protocol (HZ3-11).

**Counterexample candidates.** *Class L (κ = 0)*: at critical level
of an affine KM, F_g = 0 for all g ≥ 1 (the genus tower is trivial).
Confirmed; T4 reduces to F_1 = 0 (since κ = 0). *Class C (βγ at
λ ≥ 2)*: shadow tower terminates at degree 4. T4 still holds with κ
= 1. *Class M with κ = 0*: does this exist? The discriminant
Δ = 8κS_4; the table at L2390-2410 says class M needs Δ ≠ 0, i.e.
both κ ≠ 0 and S_4 ≠ 0. So the class-M / κ=0 corner is empty by
construction. Good — no counterexample.

### T5 — Theorem H: polynomial Hilbert series
*(`five_theorems_modular_koszul.tex` L1406–1467; full proof in
`chiral_hochschild_koszul.tex` L927–1031, L1040–1161, with alternative
proof at L1163–1224)*

**Attack 1 — Verdier duality with ω_X tensor twist.** The main
theorem (`thm:main-koszul-hoch`, L927–961) asserts
`ChirHoch^n(A) ≅ ChirHoch^{2-n}(A^!)^∨ ⊗ ω_X`. The ω_X factor
matters: if X is non-trivial (genus ≥ 1), ω_X is not the trivial
line bundle, and dim doesn't change but other invariants do. The
"dim ChirHoch^n(A) = dim ChirHoch^{2-n}(A^!)" deduction at L1126–1135
is correct *over a fixed point* (or after passing to global sections
on a curve), but the statement as written is a *sheaf-level* identity
that needs care for global degeneration.

**Defense.** For the Hilbert polynomial result, you only need
dimensions, and dim is invariant under tensor with a line bundle, so
the conclusion stands. Repair: explicitly state that
`dim ChirHoch^n` is over the ground field (after global sections).

**Attack 2 — the Hilbert polynomial families table specializations
need verification.** L1443–1467:
- Heisenberg: `1+t+t²` — `dim ChirHoch^1(H_k) = 1` (the outer
  derivation `D(J) = 1`). OK.
- Affine KM: `1+dim(g)·t+t²` — `dim ChirHoch^1(V_k(g)) = dim(g)`.
  This is **suspicious**: for V_k(g) at *generic* level, the
  outer-derivation count should be related to `H^1(g, V_k(g))`. For a
  simple Lie algebra g, classical Whitehead lemma gives
  `H^1(g, M) = 0` for finite-dim semisimple representations M. The
  chiral Hochschild^1 counts something different, and `= dim(g)` is
  not automatic. What is the actual claim? It is: outer
  *chiral* derivations of V_k(g) at generic k. For affine KM at
  generic level, every primary field (the modes of g acting on V_k(g))
  gives a non-inner chiral derivation; this gives `dim(g)`
  candidates, but coboundary identifications might cut some. The
  statement needs a specific reference or a direct calculation.
- Virasoro: `1+t²`, `dim ChirHoch^1 = 0`. The Virasoro algebra has no
  outer chiral derivations at generic c. This is plausible (every
  derivation is inner = `[L_n, -]`).
- W_N: same as Virasoro, `1+t²`. Suspicious for same reason as KM:
  W_N has `N-1` strong generators; at generic c, do they each
  contribute to ChirHoch^1, or do they all act inner?

**Defense.** All four entries are well-motivated but only the
Heisenberg case is verified by explicit computation in the
manuscript. Repair: either (a) provide direct verification of each
entry (this is a genuine technical task, not formal), or (b)
restate the proposition with caveats: "for the standard families,
the Hilbert polynomial is **conjectured** to be of this form; the
Heisenberg case is verified directly; the others follow from
plausible but unverified outer-derivation counts."

**Attack 3 — three-way Hochschild confusion.** The warning at
`five_theorems_modular_koszul.tex` L1425–1439 distinguishes
chiral / topological / categorical Hochschild. This is good
disambiguation. AP-CY64 (in CLAUDE.md) explicitly flags this: "Three-way
Hochschild confusion (ChirHoch/HH*/H*_GF). ChirHoch* concentrated in
{0,1,2} (Theorem H). HH*(A_mode) concentrated in {0} for Weyl algebra
(dim 1). H*_GF unbounded (polynomial ring). 'ChirHoch is finite while
THH is infinite' is WRONG (HH*(Weyl) = 1-dim)."

The remark at `chiral_hochschild_koszul.tex` L1236–1281 already
addresses this (correctly) and notes the only true *dimension*
divergence between ChirHoch and HH*(A_mode) is at critical level.
The standalone warning is correctly cautious. **Action**: ensure the
warning at L1425–1439 also notes that the dimensional divergence
between ChirHoch and HH*(A_mode) is *only* at critical level (the
generic-level difference is structural, not dimensional).

**Independent verification.** The amplitude bound
`ChirHoch^n(A) = 0 for n ∉ {0,1,2}` is verified by two independent
proofs (spectral sequence at L1092–1115; deformation-theoretic at
L1163–1224). These are genuinely independent. **Suggested third path**:
explicit computation for the bc/βγ pair via the boson-fermion duality
(theorem `ver:boson-fermion-HH` at `chiral_hochschild_koszul.tex`
L5320 is exactly this — a verification, not tautological).

**Counterexample candidates.** *Critical level affine KM*: ChirHoch
becomes infinite-dim (Feigin–Frenkel center). Already excluded by the
hypothesis. *Minimal-model Vir*: at c = c(p,q), the Hilbert series
might pick up extra terms from the embedding pattern of singular
vectors. The standalone restricts to "generic c"; this is correct.
*Logarithmic Vir / W*: not covered (these are non-rational).

---

## Section 3. Consolidated punch list

### CRITICAL (will not survive Annals review)

**C1.** Bershadsky–Polyakov "self-dual k = -3" claim
(`five_theorems_modular_koszul.tex` L2551–2554) is mathematically
inconsistent with the central charge formula (which has a pole at
k = -3). The conductor identity K_BP = 196 is correct as a
polynomial identity but the "kappa(BP_{-3}) = 49/3" is the symmetric
mean of two divergences, not a value at a self-dual point. **Fix**:
rewrite the BP subsection to state the conductor 196 as a
polynomial identity in k, note that the involution k ↦ -k-6 has
fixed point k=-3 where c has a pole, and BP_{-3} is not a chiral
algebra in the standard sense.

**C2.** βγ + bc complementarity sum K=0 conflict. The census table
(`five_theorems_modular_koszul.tex` L2221–2233) lists kappa(βγ) = 1
(constant in λ) and kappa(bc) = c_bc/2 = (1 - 3(2λ-1)²)/2 (varies in
λ). For ghost cancellation `c_βγ + c_bc = 0` to give a Lagrangian
complementarity sum K = 0, we would need `kappa(βγ) + kappa(bc) = 0`,
which requires either `kappa(βγ) = -kappa(bc) = -c_bc/2` (variable in
λ) or `kappa(bc) = -1` (forcing c_bc = -2, only at specific λ).
**At λ = 1/2 (Dirac): kappa(bc) = 1/2, kappa(βγ) = 1, sum = 3/2 ≠ 0.**
**At λ = 2 (reparam ghost): kappa(bc) = -13, kappa(βγ) = 1, sum =
-12 ≠ 0.** Either the kappa(βγ) entry is wrong, or the K = 0 entry
is wrong, or the bc dual of βγ is *not* the bc system at the same λ
(the Koszul dual could shift weights). **Fix**: clarify the
Koszul duality relation between βγ and bc, recompute the entry, and
explicitly compute K(βγ).

### HIGH (overclaim — should be tightened)

**H1.** T1 (Theorem A) bundles two distinct results (adjunction +
Verdier intertwining) under one ProvedHere tag. Split into T1a
(adjunction, ProvedHere) and T1b (Verdier intertwining, ProvedHere
*conditional* on filtered comparison + PBW completeness).

**H2.** T4 (Theorem D) "two independent proofs" claim
(`five_theorems_modular_koszul.tex` L1346–1354) is overstated; the
two proofs share the uniform-weight virtual class input. Weaken to
"two independent derivations of the conclusion from the
uniform-weight virtual class identity".

**H3.** T5 (Theorem H) family-list Hilbert series for affine KM
(`dim ChirHoch^1 = dim(g)`) and W_N (`dim ChirHoch^1 = 0`) are
asserted but not verified explicitly. Either provide a direct
verification (case-by-case outer chiral derivation count) or restate
as conjecture.

**H4.** T4.iii multi-weight clause should be promoted to include the
W_3 explicit cross-channel formula `(c+204)/(16c)` (already proved
at `higher_genus_modular_koszul.tex` L22669) — this is a
*stronger* negative result than the standalone admits.

**H5.** W_N complementarity conductor `K = N-dep` is a placeholder
(`five_theorems_modular_koszul.tex` L933, L2253). State a closed
formula or explicit per-N table.

### MEDIUM (scope or notation)

**M1.** Several theorem statements rely on hypotheses buried in
proofs or in upstream definitions:
- T1: PBW completeness, finite-dim graded bar pieces.
- T2 open-stratum lemma: cone-constructibility on U_g.
- T2 boundary lemma: node-flatness for Künneth at nodes.
Promote these to standing hypotheses on "modular pre-Koszul chiral
algebra".

**M2.** T4 proof (clutching, L1296–1301) assumes κ ≠ 0 (uses
1/κ in star-product). Add κ ≠ 0 to T4.ii hypothesis or carve out
class L (κ = 0) explicitly.

**M3.** The chain "five theorems forced sequence" remark at
`five_theorems_modular_koszul.tex` L1491–1742 is rhetorically strong
but the converses-fail claim ("H does not imply D" etc.) has weak
formal content; some of the "non-converses" are tautological
("polynomial Hilbert series doesn't determine kappa") and some are
nontrivial. Either tighten with explicit counterexamples per
non-converse, or downgrade to "informal organisation".

**M4.** Heisenberg dual `H_k^! = Sym^ch(V*)` curved with `m_0 =
-k·ω` (L713–719): for the modular characteristic of a curved object
to be defined, the negative cyclic refinement is needed. Cross-reference
explicitly to `chiral_hochschild_koszul.tex` cyclic L_∞ section or to
the standalone's definition L575–581.

**M5.** Five-objects remark at L954–968 lists `A`, `B(A)`, `A^i`,
`A^!`, `Z^der_ch(A)` — but `A^!_∞` (the homotopy Koszul dual,
defined via Verdier on Ran) is a *sixth* object that appears in T1
(L612, L656). Either include it in the list or clarify
`A^!_∞ = D_Ran B(A)` as a notation for `B(A)^∨` in the
factorization-algebra ambient.

### LOW (polish)

**L1.** AP136 footnote checks at L2117 are correct (W_N uses
`c·(H_N - 1)`, not `c·H_{N-1}`); the comments are a useful guard
but should be removed before publication.

**L2.** AP126 footnote checks at L2116 (`k=0 → r=0` verified for KM)
are correct; same comment.

**L3.** "Forced chain" terminology at L1491 is borderline
sensational; consider "structural ordering" or "logical
dependency".

**L4.** The `Selection table` remark at L514–530 ("Each row is
forced by the geometry of the next") is a nice exposition but
"forced" overstates: the geometry *enables* the next row, but does
not determine it uniquely.

---

## Section 4. Three concrete upgrade paths (where the manuscript can
claim more than it currently does)

### Upgrade U1 — Promote the W_3 cross-channel formula into T4

**Current state.** T4.iii (`five_theorems_modular_koszul.tex`
L1018–1027) states: "For multi-weight algebras at genus g ≥ 2, the
diagonal term remains universal but the full free energy is
F_g = κ·λ_g + δF_g^cross". The cross-channel correction is named but
no value is given.

**Claim available.** `higher_genus_modular_koszul.tex` L22669 proves
`δF_2^cross(W_3) = (c+204)/(16c)`, the first closed-form
cross-channel correction at g ≥ 2.

**Upgrade.** State T4.iii.b as: *for W_3 at genus 2, the
cross-channel correction has the closed form `(c+204)/(16c)`; in
particular, multi-weight algebras receive non-universal corrections
beyond the diagonal*. This converts T4 from an existence-of-correction
statement to a sharp computable obstruction.

**Proof sketch.** Already in `higher_genus_modular_koszul.tex` (graph
sum over the seven stable graphs of Mbar_{2,0}, with three
non-vanishing contributions: sun, theta, bridge-loop). The work is
done; only the elevation into the standalone statement is needed.

**Consequence.** The five-theorems pillar gains a sharp negative
result: "the scalar formula F_g = κ·λ_g is not universal for
multi-weight class M algebras; W_3 at g=2 receives a correction
(c+204)/(16c)." This is a publishable new theorem, not just a remark.

### Upgrade U2 — Closed formula for the W_N complementarity conductor

**Current state.** Proposition `prop:complementarity-sums`
(L908–938, item iv) says `K(W_N) is nonzero and N-dependent`; the
table at L2253 says `N-dep`.

**Claim available.** From the W_N kappa formula
`κ(W_N) = c · (H_N - 1)` and the Koszul involution
`c ↦ K_N - c` (the N-dependent "ghost central charge" for W_N), the
conductor is
`K(W_N) = κ(W_N(c)) + κ(W_N(K_N - c)) = c(H_N - 1) + (K_N - c)(H_N - 1)
       = K_N · (H_N - 1)`.

We just need to identify `K_N`. For W_2 = Vir, K_2 = 26 (the ghost
central charge), so K(Vir) = 26 · (1/2) = 13 ✓ (matches the table).
For W_3, the Koszul involution is c ↦ K_3 − c, and K(W_3) = 250/3,
so K_3 = (250/3) / (5/6) = (250/3) · (6/5) = 100. So K_3 = 100.
General W_N: K_N satisfies K(W_N) = K_N · (H_N - 1).

**Upgrade.** State the closed formula `K(W_N) = K_N · (H_N - 1)` and
identify `K_N = 26 + 24(N-2)` (a guess from K_2=26, K_3=100, but
needs verification; quick check: K_2 = 26, K_3 = 100 — does
`K_N = 26 + 74(N-2)`? K_2: 26 ✓, K_3: 26+74 = 100 ✓). The pattern
`K_N = 26 + 74(N-2)` is consistent with two data points. Verify at
N = 4 against an independent W_4 calculation; if it holds,
**state K_N as a closed linear formula**. If it fails at N=4,
state K_N per N.

**Consequence.** The complementarity conductor census becomes a
closed object across the W-tower, not a placeholder. This is the
kind of clean numerical identity that an Annals referee will love.

### Upgrade U3 — Strengthen Theorem H to a *proved* family-by-family
verification (instead of a list-of-cases proposition)

**Current state.** Theorem H (`five_theorems_modular_koszul.tex`
L1406–1423) proves the amplitude `ChirHoch^n = 0 for n ∉ {0,1,2}`
and the Hilbert polynomial formula `1 + dim ChirHoch^1 · t + dim Z(A^!) · t²`.
The family-list at L1443–1467 (Heisenberg, KM, Vir, W_N, BP, βγ, bc)
is asserted but each entry is a separate computational claim.

**Claim available.** Each entry can be verified directly:
- Heisenberg: H^1 = ⟨D : J ↦ 1⟩, dim = 1. **Already verified.**
- Virasoro: H^1 = (outer chiral derivations) = 0 at generic c, by
  the rigidity of the Virasoro presentation: every derivation must
  preserve the conformal weight, which forces it to be inner.
  **Provable in 5–10 lines.**
- Affine KM at generic level: H^1 ≅ g (1 outer derivation per
  generator), via the standard argument that conformal-weight-preserving
  outer derivations of V_k(g) are in bijection with Cartan elements
  of g acting by ad. **Provable in ≈1 page.** Needs care: is it dim(g)
  or rk(g)? The standalone says `dim(g)`, which is the larger
  number; this is the *full* outer derivation Lie algebra including
  inner-modulo-coboundary classes. **Verify by cross-checking
  against Frenkel–Ben-Zvi Ch. 11 / 12 or Beilinson–Drinfeld
  Ch. 2.** If `dim(g)` is correct, state with proof; if `rk(g)`,
  correct and state with proof.
- W_N at generic c: H^1 = 0 (no outer chiral derivations of the
  free principal W-algebra at generic level). **Provable from
  Drinfeld–Sokolov reduction**: outer chiral derivations of W_N
  descend from outer derivations of V_k(sl_N); the DS reduction
  kills all but the Cartan part, and the Cartan part becomes the
  generators of W_N (which are inner modulo strong generators).
- BP, βγ, bc: case by case.

**Upgrade.** Promote `prop:hilbert-families` (L1443) from a
proposition with no proof to a proposition with explicit verification
of each entry. This is concrete work (≈3–5 pages) but produces a
genuinely complete family-by-family table that can survive
adversarial scrutiny. The current proposition is a "verification
table" with no verification.

**Consequence.** Theorem H is upgraded from "we have an amplitude
bound + a polynomial form + plausible specializations" to "we have
an amplitude bound + a polynomial form + verified specializations".
This is the difference between a survey and a research paper.

---

## Closing remark

The five-theorems pillar of Vol I is genuinely strong: T1, T2, T4
(at genus 1), T5 (amplitude bound) are all real theorems with real
proofs. The weaknesses are:

1. *Bundling of distinct results under one ProvedHere tag* (T1, T3).
2. *Family-list specializations stated without verification* (T5
   Hilbert series for KM, Vir, W_N).
3. *One arithmetic incoherence at the BP self-dual point* (a
   genuine error, fixable in 1 paragraph).
4. *One internal inconsistency in the βγ/bc complementarity sum K=0*
   (needs recomputation; possibly the kappa(βγ) entry is
   convention-dependent).
5. *Hidden uniform-weight assumption presented as "two
   independent proofs"* (T4 ii/iii).

None of these is fatal. The three upgrade paths in §4 add genuine
new sharp content. After the punch-list edits in §3, the pillar will
be in solidly Annals-ready shape — a survey-form chapter with five
load-bearing theorems, each with explicit proof, hypothesis, and
family-by-family verification.

The single highest-leverage change is **C1 (BP self-dual)**: it is a
straightforward error caught by undergraduate calculus (denominator
vanishes) and would be the first thing flagged by any referee with
access to a copy of Bershadsky–Polyakov. Fix this before submission.

The independent-verification protocol (HZ3-11 in CLAUDE.md) suggests
that the strongest *new* test would be the independent
DS-reduction-of-genus-2-sl_3-KZB derivation of the W_3 cross-channel
correction `(c+204)/(16c)`; this would convert T4.iii from
ProvedHere-by-graph-sum to ProvedHere-with-independent-verification,
which is the gold standard.
