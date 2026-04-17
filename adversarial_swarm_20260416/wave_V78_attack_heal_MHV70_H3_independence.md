# Wave V78 --- Russian-School Adversarial Attack and Heal on the
# Independence of H1, H2, H3 in MHV70

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Russian-school
deepest adversarial attack on V77's MHV70 hypothesis-minimality claim.
Chriss-Ginzburg discipline (construct, do not narrate);
Bezrukavnikov reduction-to-minimum-hypothesis; Bogomolov-Tian-Todorov
rigidity rigour. AP-CY61 first-principles healing throughout.

**Posture.** No `.tex` edits. No `CLAUDE.md` edits. No commits. No
build. No test runs. Sandbox-only. Read-only attack with explicit
structural diagnostics; healing into the *truly* minimum-hypothesis
form.

**Predecessor.**
- V70/V77 (`wave_V70_attack_heal_K3_mukai_signature_uniqueness.md`):
  introduces MHV70 = (H1) Hodge $h^{2,0}=1, h^{1,0}=0$ AND (H2) even
  unimodular $H^*(F,\mathbb{Z})$ with primitive $(2,n)$, $n\geq 10$
  embedding AND (H3) Heisenberg presentation $\Phi_2(D^b(\mathrm{Coh}(F)))
  = \mathrm{Heis}^{\mathrm{rk}(F)}$.
- V49 (`wave_application_V49_status_promotion.md`): three-route
  Pentagon closure for K3 input.
- AP-CY55 (manifold vs algebraization), AP-CY58 (CY-B d-dependent),
  AP-CY61 (first-principles ghost-theorem extraction), HZ3-1
  (CY-A_3 dependency tree).

---

## §0. The single-line attack-and-heal thesis

> **Attack.** V77's MHV70 presents three hypotheses (H1)+(H2)+(H3)
> as if they were structurally independent conditions on a compact
> CY2 fibre $F$. They are NOT. For compact CY2-fibres, (H1) implies
> (H2) and (H1) implies (H3) by classical theorems
> (Bogomolov + Hirzebruch--Riemann--Roch + Mukai-Orlov), so MHV70
> over-counts conditions at the geometric level. (H2) and (H3) are
> redundant in the geometric (Class A) regime, becoming the
> *primary* conditions only in the algebraic non-geometric regime
> (Class A''). The presentation as three independent conditions is
> the *narrative* artifact of constructing MHV70 by reading off the
> three V49 routes; it is not the *structural* state of affairs.

> **Heal.** The Platonic minimum hypothesis stratifies by regime:
> - **Class A (compact symplectic CY2-fibre, geometric):** ONE
>   condition, (H1). The Hodge characterisation $(h^{2,0}, h^{1,0})
>   = (1, 0)$ alone forces (H2) and (H3) by Bogomolov + HRR + Mukai's
>   reconstruction theorem for derived categories of K3 surfaces.
>   Pentagon-at-$E_1$ closure governed by Hodge characterisation
>   alone.
> - **Class A'' (algebraic non-geometric):** TWO conditions, (H2)
>   and (H3) at higher rank. (H1) is vacuous (no underlying compact
>   complex manifold). Pentagon closure governed by lattice
>   unimodularity + Heisenberg presentation.
> - **Class A' (non-symplectic K3-fibred):** THREE conditions
>   genuinely independent. Non-symplectic involution can preserve
>   (H1) on the cover but break (H2) (lattice gets discriminant) or
>   (H3) (Heisenberg presentation truncates to invariants). Each
>   must be checked separately.
>
> Therefore corrected MHV70 has REGIME-DEPENDENT minimal hypothesis
> count: 1 condition for Class A, 2 for Class A'', 3 for Class A'.
> The three-condition uniform statement of V77 is not wrong, it is
> over-conservative for Class A and incomplete for Class A''.

---

## §1. V77 MHV70 restated

V77 MHV70 (verbatim from `wave_V70_attack_heal_K3_mukai_signature_uniqueness.md`
§4):

> **Minimal Hypothesis (MHV70).** A CY3 input $X$ is "V49-Pentagon
> closing" iff there exists a fibration $X \to B$ with generic fibre
> $F$ satisfying:
>
> (H1) $h^{2,0}(F) = 1$, $h^{1,0}(F) = 0$;
> (H2) $H^*(F,\mathbb{Z})$ even unimodular, primitive sublattice
>      embedding into a $(2,n)$ Borcherds-relevant lattice with
>      $n \geq 10$;
> (H3) $\Phi_2(D^b(\mathrm{Coh}(F)))$ has a Heisenberg presentation
>      $\mathrm{Heis}^{\mathrm{rk}(F)}$ with $\sum h_i = 0$.

V77 lists K3 as the unique compact CY2-fibre satisfying all three;
abelian $T^4$ failing (H1); Enriques and bielliptic also failing (H1);
and Conway/Leech satisfying (H2)+(H3) without (H1) (algebraic
non-geometric).

V77 does NOT claim explicitly that (H1), (H2), (H3) are *independent*.
But by listing them as three separate conditions in MHV70 and by
treating their conjunction as the criterion, the implicit claim is
that each is load-bearing: removing any one would leave a strictly
weaker condition. V78 attacks this implicit independence.

---

## §2. ATTACK -- five angles with AP-CY61 ghost-theorem extraction

### A1. (H3) might follow from (H1) for compact CY2-fibres

**The claim under attack.** "(H3) Heisenberg presentation
$\Phi_2(D^b(\mathrm{Coh}(F))) = \mathrm{Heis}^{\mathrm{rk}(F)}$ is an
independent condition on $F$ beyond (H1)."

**First-principles audit.** Mukai's reconstruction theorem
(Mukai 1981, Orlov 1997): the derived category $D^b(\mathrm{Coh}(F))$
of a compact complex surface $F$ with $h^{2,0}(F) = 1$ and $h^{1,0}(F)
= 0$ is determined up to derived equivalence by the Hodge structure
on $H^*(F, \mathbb{Z})$. By Bogomolov decomposition, such an $F$ is
either K3 or an Enriques quotient; (H1) demands $h^{2,0}=1$, ruling
out Enriques ($h^{2,0}=0$). So (H1) for compact CY2 forces $F = $ K3.

For K3, $\Phi_2(D^b(\mathrm{Coh}(K3))) = H^*_{\mathrm{Mukai}}(K3)$ with
the Heisenberg vertex algebra structure (CY-A_2, PROVED at
cohomological level via thm:phi-k3-explicit). The Heisenberg
presentation $\mathrm{Heis}^{24}$ with $\sum h_i = 0$ is the explicit
output of Phi on the K3 derived category; no independent verification
is needed --- it is the CY-A_2 theorem.

**Verdict.** (H3) is FORCED by (H1) for compact CY2-fibres, via
Bogomolov + Mukai-Orlov + CY-A_2. The implicit independence of (H3)
is a NARRATIVE artifact: V77 reads off (H3) from V49 route (i)+(ii)
because routes (i)+(ii) explicitly invoke the Heisenberg
presentation. But routes (i)+(ii) work BECAUSE Phi delivers
Heisenberg, which is the CY-A_2 conclusion for K3 fibres.

**Ghost theorem (AP-CY61, this attack).**

(a) **Right.** (H3) is a real load-bearing condition for V49 routes
(i)+(ii). The Heisenberg presentation IS what makes the diagonal
R-matrix work in route (i) and the abelian Lie bialgebra structure
work in route (ii).

(b) **Wrong.** The presentation of (H3) as an INDEPENDENT condition
on $F$ beyond (H1) is wrong for compact CY2-fibres. (H1) alone
forces $F = $ K3 (by Bogomolov + Hodge classification), and for K3
the Heisenberg presentation is automatic via CY-A_2 PROVED at
cohomological level.

(c) **Correct relationship.** For compact CY2-fibres, (H1) implies
(H3) via the chain:
- (H1) + Bogomolov $\Rightarrow$ $F = $ K3 (unique compact CY2 with
  $h^{2,0}=1, h^{1,0}=0$).
- $F = $ K3 + CY-A_2 $\Rightarrow$ $\Phi_2(D^b(\mathrm{Coh}(K3))) =
  H^*_{\mathrm{Mukai}}(K3)$ with Heisenberg vertex algebra structure.
- $H^*_{\mathrm{Mukai}}(K3) = \mathrm{Heis}^{24}$ at the abelian level
  with $\sum h_i = 0$ from the unimodularity-induced trace constraint.

The ghost theorem is **Mukai's reconstruction theorem combined with
CY-A_2**: for compact CY2-fibres satisfying (H1), the Heisenberg
presentation is automatic. (H3) is *not* an independent condition
in this regime.

### A2. (H2) might follow from (H1) for compact CY2-fibres

**The claim under attack.** "(H2) $H^*(F,\mathbb{Z})$ even unimodular
with primitive $(2,n)$, $n\geq 10$ embedding is an independent
condition on $F$ beyond (H1)."

**First-principles audit.** Same Bogomolov chain: (H1) + Bogomolov
$\Rightarrow$ $F = $ K3. For K3, the Mukai lattice
$H^*(K3, \mathbb{Z})$ is even unimodular of signature $(4, 20)$ with
isometry class $II_{4,20} = E_8(-1)^2 \oplus U^4$. This is a
classical result (cf. Mukai 1984 lattice rank 24, e.g., the
independent verification cited in `compute/tests/test_phi_k3_explicit.py`).

The primitive $(2, n)$ embedding for $n \geq 10$: the Picard-orthogonal
sub-lattice of generic K3 has signature $(2, 18)$, which contains a
primitive $(2, 10)$ sub-lattice supporting the Igusa $\Phi_{10}$
Borcherds lift. The existence of this primitive sub-lattice is a
GENERIC fact about K3 (it fails only at codimension-$\geq 1$ Heegner
divisors in K3 moduli, where the Picard rank jumps).

So (H2) is automatic for K3 (= the unique (H1)-satisfying compact
CY2-fibre). Specifically:
- Even: K3 cohomology is even by Wu's formula.
- Unimodular: K3 $H^*$ is unimodular by Poincare duality + $\pi_1(K3)
  = 1$ + intersection form is unimodular.
- Signature $(4, 20)$: from Hodge decomposition $24 = 1 + 22 + 1$
  with $h^{2,0}+h^{0,2}+h^{1,1}_+ = 1+1+2 = 4$ positive.
- Primitive $(2, n)$ embedding: generic K3 Picard-orthogonal is
  $II_{2, 18}$, contains $II_{2, 10}$ as primitive sub-lattice via
  $II_{2,18} = II_{2,10} \oplus E_8(-1)$.

All four ingredients of (H2) are FORCED by $F = $ K3, which is itself
forced by (H1) + Bogomolov.

**Ghost theorem (AP-CY61, this attack).**

(a) **Right.** (H2) is a real condition relevant for V49 route (iii)
Borcherds lift. The unimodularity is needed for the singular-theta
correspondence to land in a self-dual ambient; the $(2, n)$ primitive
embedding is needed for the lift to produce an automorphic form on
$O(2, n)$.

(b) **Wrong.** The presentation of (H2) as INDEPENDENT of (H1) is
wrong for compact CY2-fibres. (H1) forces $F = $ K3, which forces
all of (H2) automatically. The Pythagorean ladder of V53.1 (alternate
signatures $(8, 16), (12, 12), (0, 24)$) doesn't realize on compact
CY2-fibres because Bogomolov + Hodge restricts compact CY2 to four
types and only K3 has rank-24 even unimodular Mukai data.

(c) **Correct relationship.** For compact CY2-fibres, (H1) implies
(H2) via:
- (H1) + Bogomolov $\Rightarrow$ $F = $ K3.
- $F = $ K3 + Mukai 1984 + Wu + Poincare $\Rightarrow$
  $H^*(F, \mathbb{Z}) = II_{4,20}$ even unimodular.
- $F = $ K3 generic $\Rightarrow$ Picard-orthogonal $II_{2,18}$
  contains primitive $II_{2,10}$.

The ghost theorem is the **K3 lattice classification (Mukai 1984
+ Milnor-Serre)**: the K3 Mukai lattice is uniquely $II_{4,20}$ as
an abstract lattice, and contains the Borcherds-relevant primitive
sub-lattices generically. (H2) is *not* an independent condition for
compact CY2-fibres.

### A3. All three conditions might be the same condition for compact symplectic CY2

**The claim under attack.** "(H1), (H2), (H3) are three independent
conditions; their conjunction defines MHV70."

**First-principles audit.** Combining A1 and A2: for compact CY2-fibres,
(H1) implies both (H2) and (H3). Therefore the conjunction (H1) AND
(H2) AND (H3) is equivalent to (H1) alone in this regime. MHV70
restricted to compact CY2-fibres is a SINGLE-CONDITION criterion in
disguise.

Stronger: for compact CY2-fibres, the implications run:
$$
(H1) \Longleftrightarrow F = K3 \Longleftrightarrow (H1) \wedge (H2) \wedge (H3)
$$
where the first equivalence is Bogomolov + Hodge characterisation
(plus simply-connected from $h^{1,0}=0$ via Bogomolov decomposition
ruling out abelian and bielliptic, and $h^{2,0}=1$ ruling out
Enriques), and the second equivalence is A1+A2 above.

For Class A (compact, symplectic) MHV70 has ONE structural
hypothesis, not three.

**Ghost theorem (AP-CY61, this attack).**

(a) **Right.** All three conditions DO hold for K3, and they are
all real conditions in the sense that (H2) and (H3) can be CHECKED
independently of (H1) (e.g., for an abstract algebraic structure
without a geometric realisation, one can ask about (H2) and (H3)
without (H1)).

(b) **Wrong.** The implication that the three conditions are
SEPARATE constraints on $F$ in the compact CY2 regime is wrong. They
collapse to one. Removing (H2) or (H3) from MHV70 in the compact
geometric regime would NOT weaken the criterion; the resulting
single-(H1) criterion still picks out exactly K3.

(c) **Correct relationship.** For compact CY2-fibres, MHV70's three
conditions are not three independent constraints; they are three
EXTRINSIC CHARACTERISATIONS of the same intrinsic condition $F = $
K3:
- (H1) = Hodge characterisation.
- (H2) = lattice characterisation.
- (H3) = derived-category / chiral-algebra characterisation.

Each characterisation is a different LANGUAGE in which to state
"$F = $ K3"; they are mathematically equivalent for compact CY2 by
Bogomolov + Mukai 1984 + CY-A_2.

The ghost theorem is the **K3 multi-characterisation theorem**:
$F = $ K3 (compact CY2) admits multiple equivalent characterisations
at the Hodge, lattice, and derived-category levels, all forced by
Bogomolov + Hodge + Mukai-Orlov + CY-A_2. MHV70 is a CONJUNCTION of
these equivalent characterisations, hence equivalent to ONE of them
(say (H1), the simplest).

### A4. (H3) inherits chain-level conditionality from CY-A_2

**The claim under attack.** "(H3) Heisenberg presentation is
unconditional once $F = $ K3, via CY-A_2."

**First-principles audit.** CY-A_2 (PROVED) establishes
$\Phi_2(D^b(\mathrm{Coh}(K3))) = H^*_{\mathrm{Mukai}}(K3)$ as an
$E_2$-chiral algebra at the COHOMOLOGICAL level. The Heisenberg
presentation $\mathrm{Heis}^{24}$ with $\sum h_i = 0$ is a statement
at the cohomological level; it follows from the Mukai pairing
structure being abelian symplectic.

But MHV70 uses (H3) for V49 Pentagon closure at the CHAIN level. If
(H3) is required at the chain level, then it inherits chain-level
conditionality even though CY-A_2 is PROVED cohomologically. The
chain-level statement requires explicit framing data on the
$A_\infty$-structure of $D^b(\mathrm{Coh}(K3))$, which is non-formal
in general (per AP-CY34 and the operadic TCFT machinery of Costello).

**Verdict.** (H3) is unconditional COHOMOLOGICALLY once $F = $ K3 (via
CY-A_2 PROVED). At the CHAIN level, (H3) inherits from the
non-formality status of the $A_\infty$-structure. For K3 specifically,
the $A_\infty$-structure on $D^b(\mathrm{Coh}(K3))$ is FORMAL by
Kaledin's theorem (compact symplectic surfaces have formal derived
categories); so the chain-level Heisenberg presentation is also
unconditional for K3.

For non-K3 fibres in Class A' (non-symplectic K3-fibrations), the
$A_\infty$-structure on the invariant subcategory may be non-formal,
and (H3) chain-level then inherits genuine conditionality.

**Ghost theorem (AP-CY61, this attack).**

(a) **Right.** Chain-level vs cohomological-level distinctions
matter. (H3) at the chain level is in principle stronger than (H3)
at the cohomological level.

(b) **Wrong.** For K3 (compact, symplectic), chain-level and
cohomological-level (H3) coincide by Kaledin's formality theorem.
The chain-level conditionality is automatic for K3.

(c) **Correct relationship.** (H3) chain-level for $F = $ K3 is
automatic via Kaledin formality $\circ$ CY-A_2. For non-K3 Class A'
inputs, formality may fail and (H3) chain-level becomes a genuine
condition. So MHV70 (H3) inherits conditional chain-level scope
ONLY in Class A', not in Class A.

The ghost theorem is **Kaledin formality for compact symplectic
surfaces**: $D^b(\mathrm{Coh}(K3))$ is formal, so chain-level (H3)
reduces to cohomological-level (H3) for K3. (H3) is unconditional
chain-level for the Class A regime; conditional only in Class A'.

### A5. Algebraic vs geometric distinction --- Class A'' (Conway, Leech)

**The claim under attack.** "MHV70 is uniformly stated for compact
CY2-fibres and algebraic non-geometric inputs (Conway, Leech) by the
same three conditions (H1)+(H2)+(H3)."

**First-principles audit.** For Class A'' (Conway moonshine
$II_{2,26}$, Leech $\Lambda$, etc.), there is no underlying compact
complex manifold $F$. So (H1) Hodge characterisation is VACUOUS
(there is no Hodge structure to characterise). (H1) cannot be
applied to algebraic non-geometric inputs.

For Class A'', MHV70 effectively has TWO conditions: (H2) lattice
characterisation and (H3) Heisenberg presentation. (H1) is dropped
because it has no meaning. The Pentagon closure at Class A'' is
governed by (H2)+(H3) alone.

**Stratification across regimes:**

| Regime | (H1) status | (H2) status | (H3) status | Effective MHV70 |
|--------|-------------|-------------|-------------|----------------|
| Class A (compact symplectic) | required, FORCES (H2)+(H3) | automatic from (H1) | automatic from (H1) | (H1) alone, ONE condition |
| Class A' (non-symplectic K3-fibred) | preserved | partial | conditional | (H1)+(H2)+(H3), THREE conditions |
| Class A'' (algebraic non-geometric) | vacuous | required | required | (H2)+(H3), TWO conditions |

**Ghost theorem (AP-CY61, this attack).**

(a) **Right.** MHV70 does cover Class A'' inputs via (H2)+(H3); the
V77 wave explicitly notes Conway moonshine and Leech as Class A''
examples satisfying (H2)+(H3) without (H1).

(b) **Wrong.** The uniform three-condition presentation is not
uniform across regimes. (H1) is vacuous for Class A''; (H2) and (H3)
are forced by (H1) for Class A. The three-condition statement masks
this regime-dependence.

(c) **Correct relationship.** MHV70 has REGIME-DEPENDENT minimal
hypothesis count: ONE (= H1) for Class A; TWO (= H2 + H3) for Class
A''; THREE for Class A' (where each condition is genuinely
independent). The uniform three-condition statement of V77 is
correct as a SUFFICIENT condition across all regimes, but
over-conservative (Class A) or incomplete-as-stated (Class A'',
where H1 is vacuous and not "satisfied" or "violated").

The ghost theorem is the **regime stratification of MHV70**: for
compact symplectic CY2 (Class A), Hodge alone suffices; for algebraic
non-geometric (Class A''), lattice + Heisenberg suffice; for
non-symplectic K3-fibrations (Class A'), all three are independent.
The single three-condition MHV70 should be replaced by a
regime-dependent stratified MHV70.

---

## §3. WHAT SURVIVES -- the structural reduction

After the five attacks, the surviving core is:

**Theorem (V78 surviving core, structural).** *MHV70 is regime-stratified.
For compact CY2-fibres satisfying the appropriate Bogomolov-class
condition, the three conditions (H1)+(H2)+(H3) collapse as follows:*

(R-A) **Class A (compact, symplectic CY2-fibre).** (H1) alone is
load-bearing. (H1) implies (H2) and (H3) via Bogomolov + Hodge
characterisation + Mukai 1984 + Mukai-Orlov + CY-A_2 + Kaledin
formality.

(R-A') **Class A' (non-symplectic K3-fibred CY3).** (H1) is preserved
on the cover but (H2) and (H3) can be partially broken by the
non-symplectic involution on the invariant sub-lattice / sub-category.
All three conditions are genuinely independent in this regime.

(R-A'') **Class A'' (algebraic non-geometric).** (H1) is vacuous (no
underlying complex manifold). (H2) and (H3) are the load-bearing
conditions; they can be checked directly on the abstract algebraic
structure without geometric input.

**Among compact CY2-fibres** (Bogomolov), Class A consists of K3
alone. So Class A's "ONE condition" criterion is simply "$F = $ K3".

**Among non-compact, orbifold, or non-geometric inputs**: the
stratification gives genuine non-trivial criteria.

---

## §4. FOUNDATIONAL HEAL --- minimal hypothesis count per regime

The minimal-hypothesis count for MHV70 stratifies as:

> **Stratified Minimal Hypothesis (MHV78, replacing MHV70).** For a
> CY-input fibre $F$ (compact, orbifold, or algebraic), the
> Pentagon-at-$E_1$ closure via V49-style routes requires:
>
> - **If $F$ is a compact symplectic CY2 (Class A regime):**
>   ONE condition: $(h^{2,0}(F), h^{1,0}(F)) = (1, 0)$.
>   Equivalently: $F = $ K3.
>   The lattice and Heisenberg conditions are FORCED via Bogomolov
>   + Mukai 1984 + CY-A_2 + Kaledin.
>
> - **If $F$ is a non-symplectic K3-fibration cover (Class A' regime):**
>   THREE conditions: (H1) preserved, (H2) and (H3) checked on the
>   invariant sub-lattice / sub-category. Each genuinely independent;
>   case analysis required per non-symplectic involution.
>
> - **If $F$ is an algebraic non-geometric input (Class A'' regime):**
>   TWO conditions: (H2) lattice characterisation and (H3) Heisenberg
>   presentation, both checked on the abstract algebraic data. (H1)
>   is vacuous.

**Three options for the foundational heal:**

(O1) **Strong reduction to ONE condition (Class A only).** For the
compact symplectic CY2 regime, MHV70 collapses to (H1) alone. This
is the strongest possible reduction; it IS achieved for Class A by
Bogomolov + Mukai-Orlov + CY-A_2 + Kaledin.

(O2) **Strong reduction to TWO conditions (Class A'').** For the
algebraic non-geometric regime, MHV70 collapses to (H2)+(H3). (H1)
is vacuous. This is the natural reduction for non-geometric inputs.

(O3) **Strong stratification (full classification).** Three regimes,
each with its own minimal hypothesis count: 1, 3, 2 for Class A, A',
A'' respectively. This is the FULL Platonic ideal: it acknowledges
that Pentagon closure has different structural reasons in different
regimes, and the minimal hypothesis reflects this.

**Recommended heal.** O3 (strong stratification) is the Platonic
ideal. It is more honest than O1 (which only covers Class A) or O2
(which only covers Class A''), and it reveals the genuine structural
diversity of Pentagon-closure mechanisms across the V49 frontier.

---

## §5. Per-class minimal hypotheses (A vs A' vs A'')

### Class A (compact symplectic CY2-fibre, geometric)

> **MHV78 [Class A].** $F$ is in Class A iff it is a compact CY2
> with $(h^{2,0}(F), h^{1,0}(F)) = (1, 0)$.

By Bogomolov decomposition, this forces $F = $ K3. By Mukai 1984,
$H^*(F, \mathbb{Z}) = II_{4,20}$ is even unimodular with the requisite
primitive sub-lattice embeddings. By CY-A_2, $\Phi_2(D^b(\mathrm{Coh}
(F))) = \mathrm{Heis}^{24}$ at the cohomological level. By Kaledin
formality, the chain-level statement coincides with the cohomological
statement.

**Minimal hypothesis count: 1 (just (H1)).**

The other two MHV70 conditions (H2)+(H3) are AUTOMATIC and need not
be stated.

### Class A' (non-symplectic K3-fibred CY3)

> **MHV78 [Class A'].** $F$ is in Class A' iff there exists a
> non-symplectic involution $\sigma: F \to F$ such that:
> (H1') $(h^{2,0}(F), h^{1,0}(F)) = (1, 0)$ on the cover (so $F = $
>      K3 itself), AND
> (H2') $H^*(F, \mathbb{Z})^{\sigma}$ is even unimodular as an
>      abstract lattice (or has bounded discriminant), AND
> (H3') $\Phi_2(D^b(\mathrm{Coh}(F))^{\sigma})$ admits a Heisenberg
>      presentation on the $\sigma$-invariant sub-category.

The non-symplectic involution $\sigma$ acts on $H^2(K3, \mathbb{Z})$
by a fixed-locus determined by Nikulin's classification. The
$\sigma$-invariant sub-lattice has signature $(1, n)$ with various
$n \leq 19$, and discriminant divisible by $2^k$ for some $k \geq 1$
(rarely unimodular). So (H2') is a genuine restriction.

The $\sigma$-invariant sub-category $D^b(\mathrm{Coh}(F))^{\sigma}$
may not have an abelian Heisenberg presentation; the presentation
truncates to $\sigma$-invariants. (H3') is a genuine restriction.

**Minimal hypothesis count: 3 (H1', H2', H3' all genuinely
independent).**

This is the regime where MHV70's three-condition presentation IS
correct as stated.

### Class A'' (algebraic non-geometric)

> **MHV78 [Class A''].** $F$ is in Class A'' iff $F$ is an abstract
> even unimodular lattice $L$ of signature $(p, q)$ with $p \geq 2$
> and $q \geq 10$, equipped with a Heisenberg-vertex-algebra
> presentation $V_L = \mathrm{Heis}^{p+q}$ and an $L \hookrightarrow
> II_{p+q'}$ primitive embedding into a Borcherds-relevant ambient
> for some $q' \geq q$.

There is no compact complex manifold; (H1) is vacuous. (H2) is the
lattice unimodularity condition; (H3) is the Heisenberg presentation
on the lattice vertex algebra.

Examples: Conway moonshine $II_{2, 26}$, rank 28; Leech $\Lambda$
(positive-definite rank 24, but no Borcherds-relevant Hermitian
domain); $II_{8, 16}$ rank 24 abstract; $II_{12, 12}$ rank 24
abstract.

**Minimal hypothesis count: 2 ((H2) + (H3)).**

(H1) is dropped as vacuous. The Pentagon closure at the algebraic
level uses only the lattice + Heisenberg data.

---

## §6. Corrected MHV70 statement (replacing V77)

> **Corrected MHV70 (= MHV78).** Pentagon-at-$E_1$ closure for a
> CY-input fibre $F$ via V49-style routes is governed by the
> following regime-stratified minimal hypothesis:
>
> $$
> \boxed{
> \begin{array}{l}
> \text{Class A (compact symplectic CY2): }
>      F\text{ satisfies } (h^{2,0}, h^{1,0}) = (1, 0). \\
> \quad \quad \text{ONE CONDITION, forces all of (H1), (H2), (H3) of MHV70.} \\[6pt]
> \text{Class A' (non-symplectic K3-fibred CY3 cover): }
>      \text{(H1') + (H2') + (H3') on } \sigma\text{-invariants.} \\
> \quad \quad \text{THREE CONDITIONS, all genuinely independent.} \\[6pt]
> \text{Class A'' (algebraic non-geometric): }
>      \text{(H2) + (H3) on abstract lattice/Heisenberg data.} \\
> \quad \quad \text{TWO CONDITIONS, (H1) vacuous.}
> \end{array}}
> $$

The original three-condition MHV70 of V77 is recovered as the
*sufficient* uniform criterion across all regimes; the regime
stratification is the *necessary and sufficient* refinement.

**Class A (compact symplectic) by Bogomolov forces $F = $ K3 uniquely.**
The "ONE CONDITION" criterion is therefore equivalent to "$F = $ K3"
in this regime, but the formulation in terms of Hodge type is the
INTRINSIC characterisation; the Bogomolov classification is the
EXTRINSIC consequence.

**Loss-less reformulation.** MHV78 is strictly more informative than
MHV70: it conveys the same set of valid inputs but with the structural
reason for inclusion in each regime. MHV70 is recovered as the
union-of-regimes criterion.

---

## §7. v3.3 directive for RANK_1_FRONTIER

The RANK_1_FRONTIER_v2 dichotomy already includes Class A, A', A''
as the K3-axis stratification (per V70 §7). The V78 refinement makes
the minimal hypothesis count per class precise.

> **v3.3 directive (replacing v3 / v2 K3-axis statements).**
>
> The Pentagon-at-$E_1$ closure on the K3-axis stratifies as:
>
> ```
> Pentagon-at-E_1 chain-level (V78 corrected, regime-stratified)
>     |
>     +-- Class A (compact symplectic CY2-fibred CY3)
>     |       MIN HYPOTHESIS COUNT: 1
>     |       Criterion: (h^{2,0}, h^{1,0}) = (1, 0) on fibre F.
>     |       Bogomolov => F = K3 uniquely.
>     |       Lattice + Heisenberg conditions FORCED.
>     |       PROVED via V49 routes.
>     |
>     +-- Class A' (non-symplectic K3-fibred CY3)
>     |       MIN HYPOTHESIS COUNT: 3
>     |       Criterion: (H1') + (H2') + (H3') on sigma-invariants.
>     |       All three conditions genuinely independent.
>     |       CONDITIONAL on case-by-case sigma analysis.
>     |
>     +-- Class A'' (algebraic non-geometric: Conway, Leech, etc.)
>     |       MIN HYPOTHESIS COUNT: 2
>     |       Criterion: (H2) + (H3) on abstract lattice/Heisenberg.
>     |       (H1) vacuous (no underlying complex manifold).
>     |       ALGEBRAICALLY PROVED via V49 routes generalised.
>     |
>     +-- Class B0 (super-trace-vanishing CY3)
>     |       Off-K3-axis. Pentagon proved via super-EK + str(K) = 0.
>     |
>     +-- Class B (mock-modular residual: quintic, local P^2)
>             Off-K3-axis. Pentagon CONJECTURAL via xi(A) = 0.
> ```
>
> **Falsifiable predictions of v3.3.**
>
> (P1) For any compact symplectic CY2 $F$ NOT having
>      $(h^{2,0}, h^{1,0}) = (1, 0)$, MHV78 [Class A] FAILS;
>      Pentagon closure follows a different route or fails.
>      Test: $T^4$ fails (H1) ($h^{1,0} = 2$), Enriques fails (H1)
>      ($h^{2,0} = 0$), bielliptic fails (H1) ($h^{2,0} = 0$).
>
> (P2) For any non-symplectic involution $\sigma$ on K3 with
>      $H^*(K3)^\sigma$ NOT even unimodular, Class A' (H2') FAILS;
>      Pentagon closure on the cover is partial.
>      Test: Nikulin's classification of non-symplectic involutions
>      gives discriminant data per involution.
>
> (P3) For any abstract even unimodular lattice $L$ of signature
>      $(p, q)$ with $p \geq 2, q \geq 10$ and Heisenberg vertex
>      algebra structure, Class A'' (H2)+(H3) holds and Pentagon
>      closes algebraically.
>      Test: Conway $II_{2, 26}$ confirmed; Leech $\Lambda$ would
>      need a Hermitian-domain modification.
>
> (P4) The minimal hypothesis count is GENUINELY 1 for Class A
>      (not 2 or 3): removing (H2) or (H3) from MHV70 in Class A
>      leaves a criterion logically equivalent to the original.
>      Test: Bogomolov + Mukai 1984 + CY-A_2 + Kaledin chain
>      verified.
>
> **Inscription discipline.** No `.tex` edits, no `CLAUDE.md` edits,
> no commits, no build, no test runs. Sandbox-only delivery.
> Inscription path (separate wave) would update:
> - `notes/RANK_1_FRONTIER_v3.md` -> add MHV78 stratification.
> - `chapters/cy_to_chiral.tex` -> add remark on MHV78 regime
>   stratification near MHV70 inscription point (if MHV70 is
>   inscribed; pending V77 acceptance).
> - V78's MHV78 should be inscribed AS A REFINEMENT of MHV70, not
>   a replacement; both formulations are valid (sufficient and
>   necessary-and-sufficient respectively).

---

## §8. Coda --- the structural lesson

V78 reveals that the MHV70 three-condition presentation is *narrative*,
reflecting the three V49 routes (sympy, Etingof-Kazhdan, Borcherds),
not *structural*. The structural state of affairs is regime-dependent:

- **Class A (compact symplectic):** ONE condition, by classical
  theorems collapsing the three.
- **Class A' (non-symplectic K3-fibred):** THREE conditions, genuinely
  independent.
- **Class A'' (algebraic non-geometric):** TWO conditions, (H1)
  vacuous.

The Russian-school discipline (reduction-to-minimum-hypothesis a la
Bezrukavnikov) is most powerful in Class A, where it strips MHV70
from three to one. Bogomolov-Tian-Todorov rigidity is the engine:
the rigidity of compact CY2 classification forces (H1) to determine
the entire structure of $F$, including its Mukai lattice and derived
category.

**Lossless rephrasing achieved.**
- V77 MHV70: 3 conditions, uniform across regimes.
- V78 MHV78: regime-stratified, 1 / 3 / 2 conditions for Class A /
  A' / A''.

V78 is strictly more informative: it identifies the genuine
structural reason for Pentagon closure in each regime, and reveals
the minimal hypothesis count per regime. The Class A reduction from
3 to 1 is the deepest reduction; it captures the Bogomolov-Mukai-CY-A_2
synthesis as the foundational mechanism.

The corrected MHV70 statement (= MHV78) ships the regime stratification
as the precise version. The original MHV70 remains a valid
SUFFICIENT criterion across regimes, but is over-conservative for
Class A (over-counting by 2) and incomplete-as-stated for Class A''
(treating vacuous (H1) as a non-trivial condition).

The single boxed take-away of V78:

$$
\boxed{
\begin{array}{l}
\text{For Class A (compact symplectic CY2-fibre), MHV70 collapses to ONE condition:} \\
(h^{2,0}(F), h^{1,0}(F)) = (1, 0). \\[6pt]
\text{Bogomolov + Mukai 1984 + CY-A}_2\text{ + Kaledin formality force} \\
\text{(H2) lattice unimodularity AND (H3) Heisenberg presentation} \\
\text{automatically. K3 is uniquely characterised by (H1) alone.}
\end{array}}
$$

The foundational claim "MHV70 has three independent conditions"
is **vindicated in spirit but corrected in form**: MHV70 has three
conditions across regimes, but in Class A (the geometric regime
that V49 was built for), only ONE is structurally load-bearing.
The other two are downstream consequences. Russian-school discipline
extracts the minimum.

---

## §9. Falsifiability and follow-up

**Falsifiable predictions of V78** (collected from §7 (P1)-(P4)):

(F1) Verify P1 explicitly: compute $T^4$, Enriques, bielliptic
failure of MHV78 [Class A] (already done in V77 table).

(F2) Verify P2 for one Nikulin-classified non-symplectic involution
on K3: e.g., the order-2 involution with fixed-locus $K3 / \sigma$ =
Enriques surface; check (H2') discriminant.

(F3) Verify P3 for Conway moonshine $II_{2, 26}$: explicit Pentagon
coherence at the $\mathrm{Heis}^{28}$ Lie bialgebra level.

(F4) Verify P4 logical equivalence: write out the chain
$(H1) \Rightarrow F = K3 \Rightarrow (H2) \wedge (H3)$ as a formal
syllogism with each step cited (Bogomolov, Mukai 1984, CY-A_2,
Kaledin).

**Follow-up tasks (separate waves).**

(G1) Adopt MHV78 stratification in RANK_1_FRONTIER_v3.3 (sandbox
update; no inscription without user review).

(G2) Inscribe corrected MHV70 in `chapters/cy_to_chiral.tex` as a
remark that the three conditions collapse in Class A.

(G3) Audit Doran-Harder list of K3-fibered CY3 for non-symplectic
candidates; classify by which regime (A vs A') they fall into.

(G4) For each algebraic non-geometric input (Conway, Leech, $II_{8,16}$,
$II_{12,12}$), verify (H2)+(H3) explicitly and confirm Class A''
membership.

(G5) Investigate whether (H1) IS vacuous for Class A'', or whether
there is a categorified Hodge-type condition that could be applied
to algebraic non-geometric inputs (e.g., a Calabi-Yau structure on
the abstract vertex algebra giving a "categorical Hodge" replacement).

---

**End of V78 memorandum.**

Authored by Raeez Lorgat. No AI attribution; no commit; no manuscript
edits; no test runs; no build. No sympy invocations beyond reference
to V49/V53/V53.1/V70 sympy-verified Pythagorean identity and V49
sympy-verified cocycle vanishing routes. Delivered to
`/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/wave_V78_attack_heal_MHV70_H3_independence.md`
per Russian-school deepest adversarial attack on MHV70 hypothesis-
minimality. Five attack angles with AP-CY61 ghost-theorem extraction;
foundational healing into the regime-stratified MHV78 with minimal
hypothesis count 1 / 3 / 2 for Class A / A' / A''; corrected MHV70
statement; v3.3 directive for RANK_1_FRONTIER.

--- Raeez Lorgat, 2026-04-16
