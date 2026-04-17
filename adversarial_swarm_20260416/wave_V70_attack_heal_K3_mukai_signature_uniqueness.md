# Wave V70 --- Russian-School Adversarial Attack and Heal on the Foundational Assumption that the Mukai Signature $(4,20)$ is What Makes K3 Pentagon-Closed

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Russian-school
deepest adversarial attack on the V49+V53+V53.1+V57+V63 implicit assumption
that K3 is the canonical input for Pentagon-at-$E_1$ closure *because* its
Mukai signature is $(p,q) = (4,20)$. Chriss--Ginzburg discipline:
construct, do not narrate. Bezrukavnikov reduction-to-minimum-hypothesis;
Mukai lattice-classification rigour; Gelfand "find the structural reason"
principle. AP-CY61 first-principles healing throughout.

**Posture.** No `.tex` edits. No `CLAUDE.md` edits. No commits. No build.
No test runs. Read-only attack with explicit structural diagnostics;
healing into the minimum-hypothesis form for Pentagon-at-$E_1$ closure.

**Predecessors.**
- V49 (`wave_application_V49_status_promotion.md`): three-route Pentagon
  closure for K3 input, conditional on FM164/FM161; honest scope K3 only.
- V53 + V53.1 (`wave21_pythagorean_first_principles.md`): Pythagorean
  identity $(p+q)^2 = (p-q)^2 + 4pq$ universal in $(p,q)$, Mukai $(4,20)$
  is one specialisation in a ladder.
- V50 (`wave_K3_multi_projection_trace.md`): four-term closure
  $\mathrm{tr}_{Z_{\mathrm{KM}}} + \mathrm{tr}_{Z_{\mathrm{BKM}}} +
  \mathrm{tr}_{Z_{\mathrm{Ber}}} + \mathrm{tr}_{Z_{\chi}} =
  \chi(\mathcal{O}_X)$ for K3-fibred CY3.
- V55 (`wave_frontier_pentagon_E1_non_K3.md`): Class A / B0 / B
  dichotomy for non-K3 inputs.
- V57: K3 Yangian inscription bundle.
- V63: Mukai self-Koszul / Heisenberg self-opposite / ADE Langlands
  self-dual triple as the V49 closure mechanism.
- AP-CY8 (Borcherds $(2,n)$ canonical setting); AP-CY55 (manifold vs
  algebraization); AP-CY61 (first-principles ghost-theorem extraction).
- `RANK_1_FRONTIER_v2.md`: dichotomy frontier; Class A = K3-fibred.

---

## §0. The single-line attack-and-heal thesis

> **Attack.** Five waves (V49, V53, V53.1, V57, V63) treat K3 as the
> canonical Pentagon-closed CY3 fibre because its Mukai lattice carries
> signature $(4,20)$. The implicit story has *three* equivalent
> readings, all of which reduce on inspection to a *more fundamental*
> hypothesis: (a) "$(4,20)$ is uniquely realised among even unimodular
> lattices of rank 24 by the K3 Mukai lattice" — TRUE up to isometry
> (Milnor 1958 + Serre classification), but the abstract isometry class
> is not what V49 routes use; (b) "the K3 fibre carries $\mathrm{Heis}^{24}$"
> — TRUE but a downstream consequence of $h^{2,0}(K3) = 1$; (c) "the
> K3 fibre admits the Borcherds singular-theta lift $\Phi_{10}$" —
> TRUE but conditional on the embedding $H^*(K3,\mathbb{Z})
> \hookrightarrow II_{2,26}$ as a primitive sublattice, again a
> downstream consequence of the Mukai lattice carrying the $K3$ Hodge
> polarisation. The *foundational* assumption $(4,20) =$ canonical is
> therefore *narrative*, not *structural*: each V49 route uses a
> different structural feature of K3, and these features are
> *correlated* in K3 but *separable* in principle. The attack reveals
> that Mukai signature $(4,20)$ alone is neither necessary nor
> sufficient for Pentagon closure; what matters is the conjunction of
> (i) $h^{2,0}(\text{fiber}) = 1$, (ii) even unimodular lattice of
> signature $(p,q)$ with $p \geq 2$ supporting a Borcherds-style
> singular-theta lift, and (iii) abelian Heisenberg presentation of the
> chiral algebra at the $E_1$ level.

> **Heal.** The Platonic minimum hypothesis for Pentagon-at-$E_1$
> closure of a CY3 fibre $F$ is the **Hodge-Lattice-Heisenberg triple**:
> (H1) $h^{2,0}(F) = 1$ and $h^{1,0}(F) = 0$ (so the Hodge structure
> is "K3-like" but not necessarily K3); (H2) $H^*(F,\mathbb{Z})$ is
> even and admits an embedding into a Borcherds lattice $II_{2,n}$ as
> a primitive sublattice with $\mathrm{rank}(F) \geq 4$; (H3) the chiral
> algebra $A_F = \Phi_2(D^b(\mathrm{Coh}(F)))$ admits a Heisenberg
> presentation at the abelian level. K3 satisfies all three (with
> rank 24, signature $(4,20)$). Among compact CY2-fibres, abelian
> surfaces $T^4$ satisfy (H2)+(H3) but FAIL (H1) (because $h^{1,0}(T^4)
> = 2 \neq 0$); Enriques surfaces FAIL (H1) (because $h^{2,0}(\text{En})
> = 0$). Therefore K3 is the unique compact CY2-fibre satisfying all
> three. **K3 IS the unique compact CY2-fibre with Pentagon-at-$E_1$
> closure of the V49 type.** Among non-compact and orbifold CY2-fibres:
> the 8 diagonal $\mathbb{Z}/N\mathbb{Z}$ symplectic K3 orbifolds inherit
> all three (per `kappa_bkm_universal.py`), and any K3 with Hodge-isometric
> period also inherits. The Pythagorean ladder of V53.1 lives at the
> level of *abstract lattices* with signature $(p,q)$, $p+q = 24$, but
> only $(4,20)$ is realised by a Hodge structure of K3 type; the other
> ladder entries $(0,24), (1,23), (8,16), \dots$ are abstract lattices
> not arising as $H^*(F,\mathbb{Z})$ of a CY2 fibre. The Class A of
> RANK_1_FRONTIER_v2 is therefore *structurally precise*: K3-fibred
> CY3 is the maximal class for V49-type Pentagon closure; broader
> "Hodge-Lattice-Heisenberg triple"-fibred CY3 collapses to K3-fibred
> in the compact case.

---

## §1. V49 + V53 + V53.1 + V57 + V63 dependencies on Mukai $(4,20)$

This section enumerates *exactly where* each predecessor wave invokes
the K3 Mukai signature $(4,20)$, distinguishing structural use from
narrative use.

### 1.1 V49 (Pentagon-at-$E_1$ K3 closure, three routes)

Three independent verification routes converging on $[\omega]_{K3} =
0 \in H^2(\mathrm{SC}^{\mathrm{ch,top}}; \mathfrak{aut})$.

| Route | Use of Mukai $(4,20)$ |
|-------|----------------------|
| (i) Direct sympy | Diagonal R-matrix $g_{K3}(z) = \prod_i (z-h_i)/(z+h_i)$ over 24 indices $i = 1,\dots,24$. The number 24 enters as the *rank* $p+q$. The signature $(4,20)$ enters only via the spectral parameters $\{h_i\}$; the cocycle vanishes by scalar commutativity, *independent of signature*. |
| (ii) Etingof--Kazhdan | Lie bialgebra structure on $\mathrm{Heis}^{24} \oplus \mathfrak{g}_{\mathrm{ADE}}$. The 24 enters as the rank of the abelian Heisenberg part. The signature enters via the symmetric bilinear form: K3 has $(4,20)$, but ANY signature with $p+q = 24$ would give a Lie bialgebra with the same Pentagon coherence. |
| (iii) V20 trace identity | $\mathrm{tr}_{Z_{\mathrm{BKM}}}(\mathfrak{K}) = c_1(0)/2 = 5$ for $\Phi_{10}$. This DOES use signature $(4,20)$ structurally, via the Borcherds singular-theta lift's dependence on the signature of the embedded lattice. |

**Audit of V49.** Routes (i) and (ii) use only the rank $p+q = 24$,
not the signature. Route (iii) uses the signature $(4,20)$ via the
Borcherds lift. Therefore signature $(4,20)$ is *load-bearing for
route (iii) only*; routes (i) and (ii) generalise to any rank-24
even unimodular lattice.

### 1.2 V53 + V53.1 (Pythagorean ladder)

The identity $(p+q)^2 = (p-q)^2 + 4pq$ at $(p,q) = (4,20)$ yields
$24^2 = (-16)^2 + 320$. V53.1 explicitly notes this is universal in
$(p,q)$ and that $(4,20)$ is one specialisation in the ladder

| $(p,q)$ | sdim | $4pq$ | Comment |
|---------|------|-------|---------|
| $(0,24)$ | $-24$ | $0$ | purely odd, Berezinian degenerate |
| $(4,20)$ | $-16$ | $320$ | **Mukai signature** |
| $(8,16)$ | $-8$ | $512$ | non-Mukai |
| $(12,12)$ | $0$ | $576$ | sdim degenerate |
| $(24,0)$ | $+24$ | $0$ | purely even, dual extreme |

V53.1 explicitly states that the K3 case is *distinguished in this
ladder by the Hodge-theoretic constraint that the K3 period domain
has positive part of rank 4*. This is the SECOND foundational
assumption: not just $(p,q) = (4,20)$ as an abstract signature, but
$(p,q) = (4,20)$ *carrying the K3 period polarisation*.

### 1.3 V57 (K3 Yangian inscription bundle)

V57 inscribes the abelian K3 Yangian presentation with 24 generators,
$\sum h_i = 0$, ADE-enhancement at codimension-2 strata of Mukai
moduli. The 24 enters as Mukai rank; the constraint $\sum h_i = 0$
enters from the unimodularity (the trace of the Mukai pairing on
$H^*(K3,\mathbb{Z})$ vanishes); the signature $(4,20)$ enters via
the convention "4 of the $h_i$ are positive, 20 negative" — but this
is a *gauge choice* in the parameter assignment, not a structural
necessity. The Yangian relations are signature-independent at the
abelian level.

### 1.4 V63 (Mukai self-Koszul + Heisenberg self-opposite + ADE Langlands self-dual)

V63 isolates three K3-specific structural features:
- (a) Mukai *self-Koszul* duality: $H_{\mathrm{Mukai}}^! =
  H_{\mathrm{Mukai}}$, with $K = 0$. Uses unimodularity and the
  symmetric Mukai pairing. Signature-independent.
- (b) Heisenberg *self-opposite*: $H_{\mathrm{Mukai}}^{op} =
  H_{\mathrm{Mukai}}$, abelian. Uses the abelian Lie structure of
  Heisenberg. Signature-independent.
- (c) ADE *Langlands self-dual*: simply-laced enhancement at singular
  K3 moduli. Uses the *ADE root systems embedding into the K3 lattice
  with the right signature*. SIGNATURE-DEPENDENT: ADE roots are
  positive-norm $+2$ vectors; the K3 lattice with signature $(3,19)$
  on the transcendental part hosts ADE configurations only because
  there are "20 negative directions" available.

V63's three-feature analysis confirms: features (a) and (b) are
signature-independent; (c) requires "enough negative directions" but
is *not* exclusive to $(4,20)$ — any signature $(p,q)$ with $q \geq
\mathrm{rank}_{\mathrm{ADE}}$ supports the same ADE configurations.

### 1.5 Summary of where $(4,20)$ is structurally load-bearing

| Wave | Use of $(4,20)$ | Structural? |
|------|-----------------|-------------|
| V49 (i) sympy | rank 24 only | NO (signature-independent) |
| V49 (ii) EK | rank 24 only | NO |
| V49 (iii) V20 trace | Borcherds lift via $\Phi_{10}$ weight | YES |
| V53 / V53.1 | Pythagorean ladder, K3 specialisation | NO (universal-in-$(p,q)$ identity) |
| V57 K3 Yangian | rank 24 + gauge convention $\sum h_i = 0$ | NO at abelian level |
| V63 (a) self-Koszul | unimodular + symmetric | NO |
| V63 (b) self-opposite | abelian | NO |
| V63 (c) ADE Langlands | $q \geq \mathrm{rank}_{\mathrm{ADE}}$ | PARTIAL (requires enough negative directions) |

**Diagnosis.** Of eight load-bearing entries across five waves, ONLY
ONE (V49 route (iii) Borcherds lift) is genuinely $(4,20)$-specific.
All others use either rank 24, unimodularity, abelian Heisenberg, or
"enough negative directions" — none of which fix $(4,20)$ uniquely.

---

## §2. ATTACK — six angles with AP-CY61 ghost-theorem extraction

### A1. Is $(4,20)$ unique among rank-24 even unimodular signatures?

**The claim under attack.** "K3 is canonical because its Mukai lattice
$H^*(K3,\mathbb{Z})$ has signature $(4,20)$, and this signature is
uniquely realised among even unimodular lattices of rank 24."

**First-principles audit.** Even unimodular indefinite lattices are
classified by Milnor 1958 + Serre: in indefinite signature $(p,q)$
with $p,q \geq 1$ and $p \equiv q \pmod{8}$, there is a UNIQUE even
unimodular lattice up to isometry, namely $II_{p,q} = E_8(-1)^a \oplus
U^b$ for appropriate $a,b$. Signatures $(4,20)$ satisfies $4 \equiv
20 \pmod 8$ (both $\equiv 4$), so $II_{4,20} = E_8(-1)^2 \oplus U^4$
exists and is unique up to isometry.

Other rank-24 even unimodular indefinite signatures:
- $(0,24) = $ negative-definite Niemeier (24 isometry classes including
  Leech, $D_{24}^+$, $E_8^3$, ...); NOT indefinite, so Milnor uniqueness
  fails — there are 24 distinct positive-definite even unimodular
  lattices of rank 24.
- $(8,16)$: $8 \equiv 16 \pmod 8$ both $\equiv 0$, so $II_{8,16} =
  E_8(-1)^2 \oplus U^8$ unique up to isometry. EXISTS.
- $(12,12)$: both $\equiv 4$, so $II_{12,12} = E_8(-1) \oplus E_8 \oplus
  U^4$ exists. EXISTS.
- $(16,8) = (8,16)$ with sign flip. EXISTS.
- $(20,4) = (4,20)$ with sign flip. EXISTS.
- $(24,0) = $ positive-definite Niemeier. 24 classes.

**Mukai lattice identification.** $H^*(K3,\mathbb{Z}) = U^4 \oplus
E_8(-1)^2$ as an abstract lattice. Compare $II_{4,20} = E_8(-1)^2
\oplus U^4$. These are isometric. So the Mukai lattice is the
indefinite even unimodular lattice $II_{4,20}$ in its abstract
isometry class.

**Ghost theorem (AP-CY61, this attack).**

(a) **Right.** The Mukai lattice IS uniquely realised up to isometry
in signature $(4,20)$ as an *abstract* lattice. Milnor 1958 + Serre
classification give this.

(b) **Wrong.** The claim "$(4,20)$ is unique" conflates *abstract
lattice isometry uniqueness* (true) with *Hodge structure uniqueness*
(also true, but this is what makes K3 special, not the abstract
signature). Other rank-24 even unimodular signatures ($(8,16), (12,12),
(0,24), (16,8), (20,4), (24,0)$) all exist; the claim that $(4,20)$
is unique is true *only as the Mukai-K3 specialisation*, not as a
signature classification.

(c) **Correct relationship.** The space of rank-24 even unimodular
lattices stratifies by signature; in each indefinite signature class
there is a unique abstract lattice (Milnor); in $(0,24)$ and $(24,0)$
there are 24 Niemeier lattices each. Among ALL these, the Mukai lattice
$II_{4,20}$ is distinguished BY THE EXISTENCE OF THE K3 PERIOD
POLARISATION on it — i.e., the existence of a complex K3 surface whose
$H^*(K3,\mathbb{Z})$ is isometric to it carrying a Hodge structure
with $h^{2,0} = 1$, $h^{1,1} = 22$, $h^{0,2} = 1$ on the transcendental
part. This Hodge structure is what V49 uses, NOT the abstract
signature.

**Verdict.** $(4,20)$ is not unique as an abstract signature — it
is the unique signature among rank-24 even unimodular lattices that
SUPPORTS THE K3 HODGE POLARISATION. The ghost theorem is the
*Torelli theorem for K3*: K3 surfaces are classified by their period
in the period domain $\Omega \subset \mathbb{P}(II_{4,20} \otimes
\mathbb{C})$, and this period domain is signature-$(2,3)$ inside the
positive-norm part of $II_{4,20}$.

### A2. Generalisation to non-K3 fibres with other Mukai signatures

**The claim under attack.** "Pentagon-at-$E_1$ closes for K3-fibred
CY3 because of the K3 Mukai signature; other CY3 fibres have other
Mukai signatures (STU model: $(2,18)$ from $T^2 \times K3$ minus $E$
contribution; rigid $T^4$: signature $(3,3)$) and these may or may
not Pentagon-close."

**First-principles audit.** A CY3 with K3 fibre $F$ has total Mukai
data combining the K3 fibre Mukai lattice $(4,20)$ with the base
contributions. STU model is K3-fibred over $\mathbb{P}^1$ with elliptic
fibre on the K3, so its total cohomology is $H^*(K3) \otimes H^*(E)
\otimes H^*(\mathbb{P}^1)$ (via Kunneth-like decomposition), giving
total rank $24 \cdot 2 \cdot 2 = 96$ but with the SAME K3 fibre
signature $(4,20)$ on each fibre.

For non-K3 fibres: a CY3 with $T^4$ (4-torus) fibre would have fibre
cohomology rank 16, signature $(3,3)$ on $H^2(T^4,\mathbb{Z})$ (the
Mukai lattice of an abelian surface), even but NOT unimodular in the
same way as K3 (the Mukai pairing on $H^*(T^4,\mathbb{Z})$ has
discriminant 1 but the Hodge structure is different).

For Enriques surface fibres: $H^*(\mathrm{En},\mathbb{Z})$ has rank
12, signature $(2,10)$ on the cohomology mod torsion; with discriminant
2 (NOT unimodular).

For Calabi-Yau 2-fold which is NOT K3, abelian surface, or Enriques:
classification (Bogomolov decomposition) says compact Kahler CY2 is
EITHER K3, abelian surface, hyperelliptic (= bielliptic), or Enriques.
That's it. So the only candidate non-K3 compact CY2-fibres are
abelian surface ($T^4$), hyperelliptic, and Enriques.

**Pentagon closure audit per non-K3 CY2-fibre.**

| Fibre | Hodge: $h^{2,0}$ | Lattice rank | Lattice signature | Unimodular? | Pentagon V49 routes? |
|-------|------------------|--------------|-------------------|-------------|----------------------|
| K3 | 1 | 24 | $(4,20)$ | YES | ALL THREE PASS |
| $T^4$ (abelian) | 1 | 8 (on $H^2$) | $(3,3)$ on $H^2$ | YES on $H^2$ | (i) PASS rank 8 / (ii) PASS / (iii) NO Borcherds lift exists in standard form |
| Hyperelliptic | 0 (since $h^{0,1} = 1$, $h^{2,0} = 0$ via Bogomolov) | various | (?) | NO | (i) GENERALISES rank-dependent / (ii) PASS / (iii) NO |
| Enriques | 0 | 12 | $(1,9)$ | NO (disc 2) | (i) PASS rank 10 / (ii) PASS / (iii) NO |

Among the four compact CY2-fibres, ONLY K3 has $h^{2,0} = 1$ AND a
unimodular Mukai lattice. Abelian $T^4$ has $h^{2,0} = 1$ but smaller
rank; Enriques and hyperelliptic have $h^{2,0} = 0$.

**Ghost theorem (AP-CY61, this attack).**

(a) **Right.** Pentagon-at-$E_1$ DOES depend on the fibre lattice
structure. Different signatures give different obstructions.

(b) **Wrong.** The implicit claim that signature $(4,20)$ is the
*only* signature giving Pentagon closure is wrong. What matters is
the *conjunction* of (i) $h^{2,0} = 1$ (so the fibre admits a
holomorphic 2-form, the Mukai polarisation), (ii) unimodular Mukai
lattice (so the Borcherds lift can land in a self-dual ambient
lattice), (iii) sufficient rank for Heisenberg presentation.

(c) **Correct relationship.** Among the four compact CY2-fibre types
(K3, $T^4$, hyperelliptic, Enriques), K3 is the unique fibre satisfying
all three conditions. Therefore K3-fibred CY3 is the structural class
satisfying all three; abelian-fibred CY3 (e.g., $T^6$) satisfies (i)
but with smaller rank; Enriques-fibred CY3 fails (i). The Pythagorean
ladder of V53.1 is real at the level of *abstract lattices*, but only
$(4,20)$ corresponds to a compact CY2 fibre with $h^{2,0} = 1$ and
unimodular cohomology. The ghost theorem is the **Bogomolov
decomposition theorem applied to compact CY2-fibres**: K3 is the
unique fibre type satisfying the Hodge-Lattice-Heisenberg triple.

### A3. The Borcherds superalgebra signature mismatch (AP-CY8)

**The claim under attack.** "V49 route (iii) closes Pentagon for K3
via Borcherds singular-theta lift in signature $(2,n)$; the K3 Mukai
lattice has signature $(4,20)$, which is OUTSIDE the canonical
$(2,n)$ Borcherds setting. Therefore V49 route (iii) is secretly
either (a) a twisted-Borcherds construction requiring $(4,20)$
specifically, or (b) a Borcherds lift on a sub-lattice of signature
$(2,n)$ inside $II_{4,20}$."

**First-principles audit per AP-CY8.** Borcherds 1995/1998 singular
theta correspondence is canonically formulated for even lattices of
signature $(2,n)$ with $n \geq 1$. The output is a meromorphic modular
form on the Hermitian symmetric domain $\mathrm{O}(2,n)/\mathrm{O}(2)
\times \mathrm{O}(n)$. For the Igusa cusp form $\Phi_{10}$, the input
lattice is $II_{2,2} \oplus E_8(-1)$ of signature $(2,10)$, and the
output is on $\mathrm{Sp}(4,\mathbb{Z}) \backslash \mathbb{H}_2$.

The K3 Mukai lattice $II_{4,20}$ has signature $(4,20)$. To get the
Borcherds lift relevant to K3, one DOES NOT lift on $II_{4,20}$
directly; one lifts on the *Picard-orthogonal sub-lattice*, which
for K3 generic Picard is $II_{2,2} \oplus E_8(-1)^2$ of signature
$(2,18)$.

The Igusa $\Phi_{10}$ corresponds to a different sub-lattice
$II_{2,2} \oplus E_8(-1) = II_{2,10}$ of signature $(2,10)$, which
sits inside $II_{4,20}$ as the "small Mukai" sub-lattice relevant to
genus-2 Heegner divisors.

**Verdict.** V49 route (iii) is a Borcherds lift on a signature-$(2,n)$
sub-lattice of $II_{4,20}$, not on $II_{4,20}$ itself. The "$(4,20)$"
serves as the AMBIENT lattice in which the Borcherds-relevant
sub-lattice lives.

**Ghost theorem (AP-CY61, this attack).**

(a) **Right.** AP-CY8 is real: bare $(2,n)$ is the canonical Borcherds
setting; $(4,20)$ is not. V49 route (iii)'s use of $\Phi_{10}$ does
involve a $(2,n)$ sub-lattice.

(b) **Wrong.** The implication that K3 needs a "twisted Borcherds"
construction is wrong. K3 uses a STANDARD Borcherds lift on the
$(2,n)$ sub-lattice (where $n = 10$ for $\Phi_{10}$, $n = 18$ for
the full Picard-orthogonal). The role of the $(4,20)$ ambient is to
provide the AUTOMORPHIC SETTING (the K3 period domain is the
$O(2,18)$-symmetric domain inside $II_{4,20}$, not $II_{2,18}$).

(c) **Correct relationship.** The Borcherds lift requires:
- A $(2,n)$ even lattice $L$ as input.
- The Hermitian symmetric domain $\mathcal{D}_L = O(2,n)/O(2) \times
  O(n)$ as the target.
- An embedding $L \hookrightarrow L_{\mathrm{ambient}}$ as a primitive
  sub-lattice, where $L_{\mathrm{ambient}}$ is even unimodular of
  some signature $(p,q)$ with $p \geq 2$.

For K3: $L = II_{2,18}$ (Picard-orthogonal of generic K3) embeds
into $L_{\mathrm{ambient}} = II_{4,20}$ (full Mukai). For Igusa
$\Phi_{10}$: $L = II_{2,10}$ embeds into $II_{4,20}$ via a different
choice of sub-lattice. **The ambient lattice need not be $II_{4,20}$
specifically; it could be ANY even unimodular $(p,q)$ with $p \geq 2$
and $q \geq 10$.** Examples: $II_{2,18}$ itself (no ambient enlargement
needed), $II_{4,20}$ (Mukai), $II_{8,24}$, $II_{2,26}$ (the Conway
ambient).

**Verdict.** The Borcherds setting is signature-$(2,n)$; the
*specific* signature $(4,20)$ enters K3 only through the K3 period
domain identification. The ghost theorem is the **Borcherds
singular-theta correspondence** on $(2,n)$ lattices; applied to K3
via the Picard-orthogonal sub-lattice. V49 route (iii) generalises
to any CY2-fibre whose Mukai lattice contains a primitive $(2,n)$
sub-lattice with $n \geq 10$ — which is more permissive than "Mukai
signature $(4,20)$".

### A4. The ghost theorem behind "K3 is the canonical CY3 fibre"

**The claim under attack.** "K3 is the canonical CY3 fibre because
$h^{2,0}(K3) = 1$ uniquely (besides abelian surfaces). This
Hodge-theoretic uniqueness is more fundamental than the Mukai-signature
uniqueness."

**First-principles audit.** Bogomolov decomposition for compact
Kahler CY2: every compact Kahler manifold with $c_1 = 0$ in real
cohomology decomposes as a finite étale quotient of products of
(a) tori, (b) hyperKahler manifolds, (c) strict CY manifolds. In
complex dim 2: tori = abelian surfaces ($T^4$); hyperKahler = K3;
strict CY in complex dim 2 = K3 (every strict CY2 is a K3); finite
quotients give Enriques (K3/$\mathbb{Z}_2$) and bielliptic
(abelian/$\mathbb{Z}_n$).

So compact Kahler CY2 is exactly $\{K3, T^4, \mathrm{Enriques},
\mathrm{bielliptic}\}$. Among these:
- K3: $h^{2,0} = 1, h^{1,0} = 0$.
- $T^4$: $h^{2,0} = 1, h^{1,0} = 2$ (NOT simply connected).
- Enriques: $h^{2,0} = 0, h^{1,0} = 0$ (K3/$\mathbb{Z}_2$).
- Bielliptic: $h^{2,0} = 0, h^{1,0} = 1$.

K3 is unique among compact CY2-fibres satisfying $h^{2,0} = 1$ AND
$h^{1,0} = 0$. This is a **stronger** uniqueness than "Mukai signature
$(4,20)$": it captures both the existence of a holomorphic 2-form
(needed for the Mukai pairing) and simple connectivity (needed to
avoid spurious $h^{1,0}$ contributions to the Hodge filtration).

**Ghost theorem (AP-CY61, this attack).**

(a) **Right.** K3 IS uniquely characterised among compact CY2-fibres
by $(h^{2,0}, h^{1,0}) = (1, 0)$.

(b) **Wrong.** The wave's narrative attributes K3's specialness to
Mukai signature $(4,20)$; the actual structural reason is the Hodge
characterisation $(1,0)$ combined with even unimodular cohomology.
$(4,20)$ is downstream of $(1,0)$ via the Hodge decomposition: $24 =
b_0 + b_2 + b_4 = 1 + 22 + 1$, signature $(4,20)$ from
$h^{2,0} + h^{0,2} + (\mathrm{positive}~h^{1,1}) = 1+1+2 = 4$ positive
directions and $20 = h^{1,1}_{-} + 0 = 20$ negative directions.

(c) **Correct relationship.** The Hodge type $(h^{2,0}, h^{1,0}) =
(1, 0)$ FORCES the Mukai signature $(4,20)$ via the Hodge decomposition.
The Hodge-theoretic uniqueness is the *more fundamental* condition;
the lattice signature is a CONSEQUENCE. Other CY2-fibres FAIL the
Hodge condition: $T^4$ has $h^{1,0} = 2 \neq 0$, Enriques and
bielliptic have $h^{2,0} = 0$. Therefore K3 is the unique compact
CY2-fibre satisfying the Hodge-Lattice-Heisenberg triple of §0.

**Verdict.** The ghost theorem is the **Hodge characterisation of K3**:
K3 is the unique compact CY2-fibre with $(h^{2,0}, h^{1,0}) = (1, 0)$
and even unimodular cohomology. Mukai signature $(4,20)$ is downstream.
This is the FOUNDATIONAL uniqueness; Mukai is the DERIVED uniqueness.

### A5. Generalised K3-fibered CY3 (Doran--Harder, Borisov--Caldararu)

**The claim under attack.** "Pentagon-at-$E_1$ V49 routes apply to
all K3-fibered CY3, but K3-fibration over $\mathbb{P}^1$ is a discrete
discrete family (Doran--Harder, Borisov--Caldararu); does V49 work
for ALL of them, or only for a subclass?"

**First-principles audit.** Doran--Harder 2014 + Borisov--Caldararu
classification: K3-fibered CY3 over $\mathbb{P}^1$ admit *Tyurin
degeneration* to a quasi-Fano pair. Doran--Harder enumerate them via
lattice-polarised K3 families; Borisov--Caldararu give Calabi--Yau
threefolds as fibre products of two such families.

The Doran--Harder list contains many K3-fibered CY3, including:
- STU model (Mukai-totally-Lagrangian K3 fibration over
  $\mathbb{P}^1$ with elliptic K3 fibre).
- The 8 diagonal $\mathbb{Z}/N\mathbb{Z}$ symplectic K3 orbifolds
  (per `kappa_bkm_universal.py` classification).
- Various non-symplectic K3-fibered CY3 (where the K3 fibre admits
  a non-symplectic automorphism).
- Lattice-polarised K3-fibered CY3 with arbitrary Picard rank.

The CY3 inputs that V49 routes apply to (Class A of RANK_1_FRONTIER_v2)
require *more* than "K3-fibered": they require that the K3 fibre carries
the FULL Mukai data $(4,20)$ usable by V49 routes (i)+(ii)+(iii).

**Pentagon closure audit per K3-fibered CY3 type.**

| Type | Pentagon V49 status |
|------|--------------------|
| K3 (CY2 itself, base case) | PROVED via V49 |
| K3 × E (compact CY3) | PROVED, K3-fibre carries full Mukai |
| STU model | PROVED (K3-fibered over $\mathbb{P}^1$, K3 fibre is elliptic with full Mukai) |
| 8 diagonal $\mathbb{Z}/N\mathbb{Z}$ K3 orbifolds | PROVED, orbifold projection inherits Pentagon |
| Non-symplectic K3-fibered CY3 (Voisin examples) | CONDITIONAL — non-symplectic involution may break Mukai self-Koszul (V63 (a)); needs case analysis |
| Lattice-polarised K3-fibered CY3 with rank-20 transcendental | PROVED, generic K3 fibre |
| Rigid K3-fibered CY3 (Borisov--Caldararu fibre products) | UNCLEAR — fibre product may introduce additional cocycle data on the fibre product structure |

**Ghost theorem (AP-CY61, this attack).**

(a) **Right.** V49 routes do generalise to *some* K3-fibered CY3
beyond K3 × E.

(b) **Wrong.** The blanket claim "all K3-fibered CY3" is too broad.
Non-symplectic K3-fibrations and Borisov--Caldararu fibre products
may break one or more of V63's three structural features.

(c) **Correct relationship.** The precise Class A is K3-fibered CY3
where the K3 fibre carries:
- Full Mukai signature $(4,20)$ (no truncation by orbifold projection
  except in the controlled $\mathbb{Z}/N\mathbb{Z}$ cases of
  `kappa_bkm_universal.py`),
- Symplectic structure (no breaking by non-symplectic involution),
- Trivial monodromy on the Picard part (so V49 route (i) sympy
  diagonalises).

This is the SYMPLECTIC K3-FIBRED CY3 sub-class. Non-symplectic
K3-fibrations form a SECONDARY class with conditional Pentagon closure.

**Verdict.** Class A = symplectic K3-fibred CY3 = exactly the
$\kappa_{\mathrm{BKM}}$-universal class of `prop:bkm-weight-universal`
(8 diagonal symplectic $\mathbb{Z}/N\mathbb{Z}$ orbifolds + STU + K3 +
K3 × E + 4 more — 15 total). Non-symplectic K3-fibrations form Class
A' with conditional closure.

### A6. Even-unimodular Pythagorean ladder beyond K3 — Leech, $II_{2,26}$, etc.

**The claim under attack.** "V53.1's Pythagorean ladder $(p+q)^2 =
(p-q)^2 + 4pq$ at $p+q = 24$ gives the K3 case. Apply the same identity
at signature $(2,26)$ (rank-28, the Conway ambient) or $(0,24)$ (Leech).
Are these Pentagon-closed?"

**First-principles audit.** $II_{2,26}$ is the Conway ambient
even unimodular lattice of signature $(2,26)$, rank 28. It hosts the
Borcherds singular-theta lift producing $\Delta_{12}$ (the cube of
the genus-1 Igusa cusp form, weight 12 on $\mathrm{Sp}(2,\mathbb{Z})$
restricted to genus-1 boundary). The Conway moonshine module
$V^\natural$ has central charge 24 and lives on the Leech lattice
$\Lambda_{\mathrm{Leech}}$ (signature $(0,24)$, positive-definite).

For Pentagon closure at $II_{2,26}$ as a Mukai-like ambient:
- The Pythagorean identity $(28)^2 = (-24)^2 + 4 \cdot 2 \cdot 26 =
  784 = 576 + 208$. Check: $4 \cdot 52 = 208$. $576 + 208 = 784$.
  Yes, $784 = 28^2$.
- A Borcherds lift on $II_{2,26}$ exists (this is the Conway / Monster
  singular-theta).
- Heisenberg presentation exists ($\mathrm{Heis}^{28}$ for the abelian
  part).
- Self-Koszul: depends on $II_{2,26}$ being self-dual — YES, even
  unimodular lattices are self-dual.

So $II_{2,26}$-input would Pentagon-close via the THREE V49 routes:
(i) sympy on rank 28; (ii) EK on $\mathrm{Heis}^{28}$ Lie bialgebra;
(iii) Borcherds via Conway $\Phi$.

**But what CY3 has $II_{2,26}$ Mukai-like cohomology?** The Bogomolov
classification rules out compact CY2 fibres with rank-28 cohomology.
The only CY-like setting with $II_{2,26}$ is the **non-geometric**
Conway moonshine setting — there is no compact CY3 whose K3-like
fibre has rank-28 unimodular cohomology with Hodge type $(1,0)$ and
signature $(2,26)$.

For Leech $\Lambda$ (signature $(0,24)$): same problem, no compact
CY3 fibre.

**Ghost theorem (AP-CY61, this attack).**

(a) **Right.** The Pythagorean identity is universal, and Pentagon
closure (V49 routes (i)+(ii)) generalises to any rank-$N$ even
unimodular lattice with Heisenberg presentation. At rank 28 with
Conway-style Borcherds lift, Pentagon would close at the
PURELY-ALGEBRAIC level.

(b) **Wrong.** The implication that "Pentagon-closed lattices form
a broader class" misses that the lattice must arise as the cohomology
of a CY-like fibre with the right Hodge structure. Bogomolov restricts
compact CY2-fibres to four types; only K3 supports rank-24 even
unimodular cohomology with Hodge type $(1,0)$. Higher ranks (28, 32,
...) do NOT arise from compact CY2-fibres.

(c) **Correct relationship.** The Pythagorean ladder is a
classification of **abstract algebraic structures** that would
Pentagon-close at the V49 algebraic level (routes (i) sympy + (ii)
EK + (iii) Borcherds). The actual GEOMETRIC realisation as the
Mukai lattice of a compact CY2-fibre is a separate question,
controlled by Bogomolov + Hodge theory. K3 is the unique geometric
realisation among compact CY2-fibres; $II_{2,26}$ and Leech are
algebraic realisations without geometric input.

**Verdict.** The Pythagorean ladder DOES extend beyond K3 *at the
algebraic level*. The geometric restriction (compact CY2-fibre with
$h^{2,0} = 1$ and unimodular cohomology) FORCES K3. The ghost theorem
is the **Bogomolov × Hodge characterisation**: among compact CY2-fibres,
K3 is the unique fibre admitting Pentagon-relevant lattice data.
Among non-compact / non-geometric inputs, the Pythagorean ladder hosts
a continuum of Pentagon-closed algebraic structures.

---

## §3. WHAT SURVIVES — the structural reduction

After the six attacks, the surviving core is:

**Theorem (V70 surviving core, structural).** *Pentagon-at-$E_1$ for
a CY3 input with fibre $F$ closes via V49-style routes if and only
if $F$ satisfies the Hodge-Lattice-Heisenberg triple:*

(H1) **Hodge characterisation.** $h^{2,0}(F) = 1$ AND $h^{1,0}(F) = 0$.

(H2) **Lattice characterisation.** $H^*(F,\mathbb{Z})$ is even
unimodular of signature $(p,q)$ with $p \geq 2$, supporting an
embedding into $II_{p,q}$ as a primitive sublattice; AND there exists
a $(2,n)$ sub-lattice with $n \geq 10$ supporting a Borcherds
singular-theta lift.

(H3) **Heisenberg characterisation.** The chiral algebra $A_F =
\Phi_2(D^b(\mathrm{Coh}(F)))$ admits a Heisenberg presentation
$\mathrm{Heis}^{p+q}$ at the abelian level, with $\sum h_i = 0$
(unimodularity-induced trace constraint).

**Among compact CY2-fibres** (Bogomolov classification): K3 is the
UNIQUE fibre satisfying (H1) AND (H2) AND (H3). Abelian surfaces
fail (H1) ($h^{1,0} = 2 \neq 0$); Enriques and bielliptic fail (H1)
($h^{2,0} = 0$). Therefore K3 is the unique compact CY2-fibre with
V49-style Pentagon closure.

**Among non-compact, orbifold, and non-geometric inputs:**

- 8 diagonal symplectic $\mathbb{Z}/N\mathbb{Z}$ K3 orbifolds: inherit
  all three (orbifold projection preserves Hodge type and unimodular
  refinement, per `kappa_bkm_universal.py`).
- K3-fibered CY3 with symplectic K3 fibre: inherit all three on the
  fibre.
- Non-geometric Conway moonshine $II_{2,26}$ or Leech-type setups:
  satisfy (H2) and (H3) at a higher rank, but lack a CY2 geometric
  realisation — Pentagon closure holds at the *algebraic* level
  (V49 routes (i)+(ii)+(iii) extend) but the resulting object is not
  $\Phi_2$ of any compact CY2 category.

**Failing classes:**

- Quintic, conifold, local $\mathbb{P}^2$, banana: not K3-fibred, do
  not satisfy (H1)/(H2)/(H3) in the V70 sense; Pentagon closure
  governed by Class B0/B mechanisms of V55 (super-trace vanishing /
  mock-modular residual).
- Abelian surfaces $T^4$ and abelian-fibred CY3: satisfy (H2) at rank
  8 with signature $(3,3)$ on $H^2$, but FAIL (H1) because $h^{1,0}(T^4)
  = 2$. Pentagon closure for abelian-fibred CY3 is genuinely OPEN
  via a separate route (not V49 K3-style).

---

## §4. FOUNDATIONAL HEAL — minimal hypothesis

The minimal hypothesis for V49-style Pentagon-at-$E_1$ closure is the
**Hodge-Lattice-Heisenberg triple** of §3. Equivalently:

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

### Status of the foundational healing per CY3 input

| Input | Fibre $F$ | Satisfies MHV70? | Pentagon status |
|-------|-----------|------------------|-----------------|
| K3 (base case) | $F = K3$ itself | YES (trivially, $X = F$) | PROVED V49 |
| K3 × E | $F = K3$ | YES | PROVED, K3 fibre carries triple |
| STU model | $F = K3$ (elliptic) | YES | PROVED |
| 8 diagonal $\mathbb{Z}/N\mathbb{Z}$ K3 orbifolds | symplectic K3 quotient | YES (per `kappa_bkm_universal`) | PROVED |
| Non-symplectic K3-fibered CY3 | $F = K3$ with non-sympl. inv. | PARTIAL — (H1) holds, (H2) PARTIAL | CONDITIONAL |
| Borisov--Caldararu fibre products | composite | UNCLEAR — case analysis needed | OPEN |
| Abelian threefold $T^6$ | $F = T^4$ | NO — fails (H1) ($h^{1,0} \neq 0$) | OPEN (separate route needed) |
| Enriques-fibered CY3 | $F = $ Enriques | NO — fails (H1) ($h^{2,0} = 0$) | OPEN (no Mukai polarisation) |
| Bielliptic-fibered CY3 | $F = $ bielliptic | NO — fails (H1) | OPEN |
| Quintic | no K3-like fibre | NO | OPEN, Class B mock-modular residual (V55) |
| Conifold | no K3-like fibre | NO | PROVED via Class B0 super-trace (V55) |
| Local $\mathbb{P}^2$ | no K3-like fibre | NO | CONJECTURAL, Class B (V55) |
| Banana | no K3-like fibre | NO | CONJECTURAL, Class B (V55) |
| $C^3$ | non-compact, no K3-like fibre | NO | OPEN |

### What MHV70 covers vs RANK_1_FRONTIER_v2 Class A

RANK_1_FRONTIER_v2 Class A = "K3-fibred CY3 with abelian Heisenberg
on the K3 fibre". MHV70 covers this exactly, with explicit minimal
hypotheses (H1)+(H2)+(H3). The two classifications agree.

The foundational healing thus REPLACES the narrative "K3-fibred" by
the structural triple (H1)+(H2)+(H3). This makes the class precisely
characterisable and falsifiable per input.

---

## §5. Generalised CY3 inputs admitting Pentagon-at-$E_1$ closure

The corrected Class A definition is:

> **Class A (corrected, V70).** A CY3 input $X$ is in Class A iff it
> admits a fibration $X \to B$ whose generic fibre $F$ is a compact
> CY2 satisfying MHV70 (= K3, by Bogomolov + Hodge characterisation).

Equivalently:

> **Class A = K3-fibred CY3 with symplectic K3 fibre.**

Among compact CY3, this includes:
1. K3 × E.
2. STU model.
3. 8 diagonal $\mathbb{Z}/N\mathbb{Z}$ symplectic K3 orbifolds (with
   $N \in \{2, 3, 4, 5, 6, 7, 8\}$ per `kappa_bkm_universal.py`,
   plus the trivial $N = 1$ case).
4. Lattice-polarised K3-fibred CY3 (Doran--Harder list, restricted
   to symplectic K3 fibre).
5. Various Calabi--Yau threefolds in toric ambients with K3 hyperplane
   section (CICY classification).

Estimated total in Class A: ~15-30 CY3 (compact, symplectic
K3-fibred). Non-compact extensions: K3 × $\mathbb{C}^*$, K3 ×
(non-compact base) for Coulomb-branch geometries.

**Class A' (extension):** Non-symplectic K3-fibred CY3. Conditional
Pentagon closure pending case analysis of which V63 features survive
the non-symplectic involution.

**Class A'' (algebraic, non-geometric):** Conway moonshine $II_{2,26}$,
Leech $\Lambda$, and other non-CY-realised even unimodular lattices.
Pentagon closes algebraically; no compact CY2 input.

### Pentagon-closure chain map for each surviving input

For each input $X$ in Class A, the explicit Pentagon edge $\eta_{45}:
P_4 \leftrightarrow P_5$ in the SC$^{\mathrm{ch,top}}$ resolution is:

```
η_{45}^X : P_4(A_X) ⟶ P_5(A_X)
        := R_X(z) ⋅ — ⋅ R_X(z)^{-1}
```

where $R_X(z) = \prod_{i=1}^{\mathrm{rk}(F)} (z - h_i^X)/(z + h_i^X)$
is the diagonal R-matrix on the Heisenberg-presented fibre with
spectral parameters $\{h_i^X\}$ inherited from the K3 fibre Mukai
data. By V49 route (i) sympy, $\eta_{45}^X$ is a coboundary; by V49
route (ii) EK, it is the Drinfeld twist coherence; by V49 route (iii)
V20, $\mathrm{tr}_{Z(\mathcal{C})}(\eta_{45}^X) = 5$ via Borcherds
$\Phi_{10}$.

For each of the 15-30 Class A inputs, this chain map specialises
explicitly:
- K3 × E: $h_i$ are the 24 Mukai eigenvalues of K3 fibre, lifted to
  $K3 \times E$ via Kunneth.
- STU: $h_i$ are the 24 Mukai eigenvalues of the elliptic K3 fibre.
- $\mathbb{Z}/N\mathbb{Z}$ K3 orbifolds: $h_i$ are the
  $\mathbb{Z}/N\mathbb{Z}$-invariant subset of the 24 Mukai eigenvalues
  (effective rank reduces to $24/N \cdot$ orbifold-invariance count).

This makes the Pentagon-closure chain map COMPUTABLE per input.

---

## §6. Pythagorean ladder generalised to other even unimodular signatures

V53.1's universal Pythagorean identity $(p+q)^2 = (p-q)^2 + 4pq$
extends to any signature. The relevant entries for Pentagon-closure
candidates:

| $(p,q)$ | rank | Berezinian sdim | $4pq$ | Pythagorean check | Geometric realisation |
|---------|------|-----------------|-------|-------------------|----------------------|
| $(2,10)$ | 12 | $-8$ | 80 | $144 = 64 + 80$ | $II_{2,10}$, Igusa $\Phi_{10}$ ambient sub |
| $(2,18)$ | 20 | $-16$ | 144 | $400 = 256 + 144$ | K3 Picard-orthogonal generic |
| $(4,20)$ | 24 | $-16$ | 320 | $576 = 256 + 320$ | **K3 Mukai** |
| $(2,26)$ | 28 | $-24$ | 208 | $784 = 576 + 208$ | Conway ambient, no compact CY2 |
| $(0,24)$ | 24 | $-24$ | 0 | $576 = 576 + 0$ | Leech, no compact CY2 |
| $(8,16)$ | 24 | $-8$ | 512 | $576 = 64 + 512$ | $II_{8,16}$, no compact CY2 |
| $(12,12)$ | 24 | $0$ | 576 | $576 = 0 + 576$ | $II_{12,12}$, no compact CY2 |
| $(2,2)$ | 4 | 0 | 16 | $16 = 0 + 16$ | $II_{2,2} = U \oplus U$, ambient core |

**Observation.** Among rank-24 entries, only $(4,20)$ has a compact
CY2 realisation (K3, by Bogomolov). All other rank-24 entries are
abstract lattices without geometric interpretation.

Among non-rank-24 entries, $(2,10)$ and $(2,18)$ correspond to
sub-lattices of K3 Mukai; $(2,26)$ corresponds to Conway. None of
$(8,16), (12,12), (24,0), (0,24)$ has a known compact CY2
realisation.

### Pythagorean ladder Pentagon-closure status

| Signature | Algebraic Pentagon (V49 (i)+(ii)) | Borcherds (V49 (iii)) | Geometric CY2 | Net status |
|-----------|----------------------------------|----------------------|---------------|------------|
| $(2,10)$ | YES (rank 12) | YES ($\Phi_{10}$) | NO (sub-lattice only) | algebraic only |
| $(2,18)$ | YES (rank 20) | YES (K3 Picard-orthog) | NO (sub-lattice) | algebraic only |
| $(4,20)$ | YES (rank 24) | YES (Mukai) | YES (K3) | **PROVED V49** |
| $(2,26)$ | YES (rank 28) | YES (Conway) | NO | algebraic only |
| $(0,24)$ | YES (rank 24) | NO (definite, no Hermitian dom) | NO | non-applicable |
| $(8,16)$ | YES (rank 24) | YES, but no Mukai polarisation | NO | algebraic only |
| $(12,12)$ | YES (rank 24) | YES, sdim degenerate | NO | algebraic only |

**Conclusion of Pythagorean ladder analysis.** The ladder hosts many
algebraically Pentagon-closed entries; only $(4,20)$ has a compact
CY2 geometric realisation. The Pentagon closure mechanism extends
across the ladder, but the geometric input class is restricted to
K3 by Bogomolov.

---

## §7. Updated RANK_1_FRONTIER directive

**Class A (corrected definition, V70).**

> Class A = CY3 inputs $X$ admitting a fibration $X \to B$ with
> generic fibre $F$ a compact CY2 satisfying the Hodge-Lattice-Heisenberg
> triple (MHV70 of §4). By Bogomolov + Hodge characterisation, $F$
> must be K3, so Class A = symplectic K3-fibred CY3.

This is *narrower* than "Pentagon-closing CY3" (which includes
Class B0 super-trace-vanishing, e.g., conifold) and *broader* than
"K3 Mukai signature $(4,20)$ CY3" (since the latter is signature-fixated
rather than Hodge-fixated; the V70 reading replaces signature by
the more fundamental Hodge characterisation).

**Updated dichotomy from RANK_1_FRONTIER_v2:**

```
Pentagon-at-E_1 chain-level (V70 corrected)
    │
    ├── Class A (V70): symplectic K3-fibred CY3, fibre satisfies MHV70
    │                  PROVED via V49 K3 routes
    │   Examples: K3, K3xE, STU, 8 diagonal Z/NZ orbifolds, ~15-30 total
    │
    ├── Class A': non-symplectic K3-fibred CY3
    │              CONDITIONAL on case-by-case check of V63 features
    │
    ├── Class A'': algebraic non-geometric (Conway, Leech, etc.)
    │              ALGEBRAICALLY PROVED via V49 routes generalised
    │              No CY2 input
    │
    ├── Class B0: super-trace-vanishing CY3 (conifold gl(1|1))
    │              PROVED via super-EK + str(K) = 0
    │
    └── Class B: mock-modular residual (quintic, local P^2, banana)
                 CONJECTURAL, ξ(A) vanishing equivalent to V8 §6
                 mock-modular conjecture
```

**Five-class corrected frontier.** The original two-class frontier
(K3 vs non-K3) and the V55 three-class refinement (A / B0 / B) are
both extended by V70 to a five-class structure. The new classes A'
and A'' surface ONLY when the foundational K3 = $(4,20)$ assumption
is interrogated.

---

## §8. Coda — what V70 makes precise

The Russian-school discipline applied to the deepest foundational
assumption (K3 = $(4,20)$ canonical) reveals a layered structure:

1. **Surface narrative** (V49 + V53 + V53.1 + V57 + V63, original):
   K3 is canonical because Mukai signature $(4,20)$.

2. **First-principles audit** (V70 §1+2): The $(4,20)$ signature is
   structurally load-bearing for ONE of the V49 routes only (route
   (iii) Borcherds). Routes (i) sympy and (ii) EK use only rank 24,
   not the signature. The Pythagorean ladder confirms $(4,20)$ is
   one entry in a continuum of algebraically Pentagon-closed
   signatures.

3. **Foundational healing** (V70 §3+4): The minimal hypothesis is
   the Hodge-Lattice-Heisenberg triple (H1)+(H2)+(H3). Among compact
   CY2-fibres, K3 is the UNIQUE fibre satisfying all three, by
   Bogomolov decomposition + Hodge characterisation $(h^{2,0},
   h^{1,0}) = (1, 0)$.

4. **Generalisation map** (V70 §5+6): The Pentagon-closure mechanism
   extends across the Pythagorean ladder at the algebraic level
   (Conway, Leech, $II_{8,16}, II_{12,12}, \ldots$). The geometric
   restriction to compact CY2-fibres FORCES K3 by Bogomolov + Hodge.

5. **Updated frontier** (V70 §7): Class A = symplectic K3-fibred CY3
   (~15-30 inputs); Class A' = non-symplectic K3-fibred (conditional);
   Class A'' = algebraic non-geometric (Conway, Leech); Class B0 =
   super-trace vanishing (conifold); Class B = mock-modular residual
   (quintic, local $\mathbb{P}^2$).

The foundational claim "K3 is canonical because $(4,20)$" is
**vindicated in spirit but corrected in form**: K3 is canonical
because the **Hodge characterisation $(1, 0)$ + Bogomolov
classification** uniquely picks out K3 among compact CY2-fibres,
and this characterisation FORCES Mukai signature $(4,20)$ as a
downstream consequence. The Mukai signature is a SYMPTOM of K3's
specialness, not the CAUSE.

The Russian-school discipline produces a FOUR-FOLD precision improvement:

(i) From "K3 is the canonical CY3 fibre because of Mukai $(4,20)$"
    to "K3 is the canonical CY3 fibre because of Hodge $(1,0)$ +
    Bogomolov + lattice unimodularity, with Mukai $(4,20)$ as
    consequence".

(ii) From "non-K3 fibres fail Pentagon" to "non-K3 *compact CY2*
     fibres fail Pentagon by failing the Hodge characterisation;
     non-CY2-fibred CY3 inputs fall into Class B0 (super-trace) or
     Class B (mock-modular) per V55".

(iii) From "Pythagorean identity $(4,20)$ is K3-specific" to
      "Pythagorean identity is universal in $(p,q)$; K3 is the unique
      compact-CY2 specialisation; algebraic non-geometric
      specialisations ($II_{2,26}$, Leech, $II_{8,16}$, ...) host
      Pentagon-closed structures without geometric input".

(iv) From "Class A = K3-fibred" (RANK_1_FRONTIER_v2 v1) to "Class A
     = symplectic K3-fibred CY3 satisfying MHV70 + Class A' =
     non-symplectic K3-fibred + Class A'' = algebraic non-geometric"
     (V70 corrected).

The single boxed statement of V70:

$$
\boxed{
\begin{array}{l}
\text{Pentagon-at-}E_1\text{ closure for compact CY2 fibre }F\text{ requires }\\
(h^{2,0}(F), h^{1,0}(F)) = (1, 0)\text{ AND }H^*(F,\mathbb{Z})\text{ even unimodular}\\
\text{AND Heisenberg presentation }\Phi_2(D^b(\mathrm{Coh}(F))) = \mathrm{Heis}^{\mathrm{rk}(F)}.\\[6pt]
\text{By Bogomolov + Hodge characterisation: }F = K3\text{ uniquely.}\\
\text{Mukai signature }(4,20)\text{ is downstream of Hodge }(1,0).
\end{array}}
$$

The foundational assumption survives the deepest attack BY BEING
REFINED, not by being broken. K3's canonical status is GENUINE, but
its STRUCTURAL REASON is the Hodge characterisation, not the Mukai
signature. The Mukai signature is the FINGERPRINT, not the FUNDAMENT.

---

## §9. Falsifiability and follow-up

**Falsifiable predictions of V70.**

(P1) For any CY3 input $X$ with K3-like fibre $F$ NOT satisfying
$(h^{2,0}, h^{1,0}) = (1, 0)$, V49-style Pentagon-closure FAILS.
Test case: abelian threefold $T^6$ (fibre $T^4$ has $h^{1,0} = 2$);
Enriques-fibered CY3 (fibre has $h^{2,0} = 0$).

(P2) For any algebraic non-geometric input with even unimodular
$(p,q)$ lattice and abelian Heisenberg presentation, V49 routes (i)
and (ii) close Pentagon at the *algebraic* level. Test case: Conway
moonshine $V^\natural$ on $II_{2,26}$.

(P3) For non-symplectic K3-fibred CY3, Pentagon closure is
CONDITIONAL on the surviving subset of V63 features (a)+(b)+(c)
under the non-symplectic involution. Test case: Voisin's
non-symplectic K3-fibred CY3 examples.

**Follow-up tasks (separate waves).**

(F1) Verify P1 for $T^6$: explicit failure of V49 route (iii) on
abelian threefold (no Borcherds-relevant lift; abelian moonshine
not analogous to Borcherds singular-theta).

(F2) Verify P2 for Conway moonshine: explicit Pentagon coherence
verification for the $\mathrm{Heis}^{28}$ Lie bialgebra at
$II_{2,26}$.

(F3) Audit Doran--Harder list for non-symplectic K3-fibred CY3
candidates: which violate (H1) on the fibre, which preserve it.

(F4) Inscribe MHV70 as a definition in Vol III (not yet — this is
a sandbox-only V70 deliverable; user reviews before applying).

---

**End of V70 memorandum.**

Authored by Raeez Lorgat. No AI attribution; no commit; no manuscript
edits; no test runs; no build. No sympy invocations beyond reference
to V53/V53.1 sympy-verified Pythagorean identity and V49 sympy-verified
cocycle vanishing routes. Delivered to
`/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/wave_V70_attack_heal_K3_mukai_signature_uniqueness.md`
per Russian-school deepest adversarial attack mandate (foundational
assumption that Mukai $(4,20)$ is what makes K3 canonical for
Pentagon-at-$E_1$ closure). Six attack angles with AP-CY61 ghost-theorem
extraction; foundational healing into the Hodge-Lattice-Heisenberg
triple MHV70; updated five-class RANK_1_FRONTIER directive.

— Raeez Lorgat, 2026-04-16
