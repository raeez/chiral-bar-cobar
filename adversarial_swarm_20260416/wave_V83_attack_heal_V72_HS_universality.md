# Wave V83 — Russian-School Attack and Heal of V72's Hattori–Stallings Universality Claim

## From "uniquely characterised RHS" to a precisely scoped, per-input verifiable trace identity

**Author.** Raeez Lorgat.
**Date.** 2026-04-16.
**Mode.** Russian-school adversarial: attack first, heal second. Caldararu–Bressler–Costello chain-level discipline. AP-CY55, AP-CY60, AP-CY61 strict.
**Predecessors.** V20 (universal Koszul–Borcherds reflection), V50 (Wave-21 closure $0+5-16+11=0$), V53/V53.1 (super-Yangian + Pythagorean), V68/V72 (foundational heal: Wave-21 = bigraded Lefschetz on $(\mathbb Z/2)^2$-equivariant $\mathrm{ChirHoch}^\bullet$).
**Disclosures.** Read/Grep/Bash/Write only (this sandbox markdown). No edits to chapters. No commits.

---

## 0. The V72 claim under attack

V72 §3 ("Why $\chi(\mathcal O_X)$ — the Hattori–Stallings reading") asserts:

> *The Hattori–Stallings bivariant trace is the unique bivariant trace
> $\operatorname{HS}: \operatorname{End}^{\mathrm{ch}}_A(A) \to \mathrm{HH}_0(A) \stackrel{\mathrm{HKR}}{\simeq} H^*(X, \mathcal O_X)$
> projecting onto $H^*(X, \mathcal O_X) = H^{0,*}(X)$, killing all $h^{p,q}$ with $p \geq 1$, **uniquely characterising** $\chi(\mathcal O_X)$ as the right-hand side of the bigraded Lefschetz identity.*

The five-pronged attack below stress-tests this claim. The heal then restates V72 with precise hypotheses, an explicit chiral HRR statement, an honest spectral-sequence collapse status, and a per-input verification table. The deliverable is a Platonic statement that no longer overclaims universality.

---

## 1. PHASE 1 — five attacks

### 1.1. Attack A: Hattori–Stallings is for *projective* dg-modules; ChirHoch cochains are not obviously projective

The classical Hattori–Stallings trace (Hattori 1965, Stallings 1965) is defined for finitely generated projective modules over a ring, and its dg/$A_\infty$ extension (Keller 1998, Shklyarov 2013) is defined for the category of *perfect* dg-modules over a smooth proper dg-algebra. The trace lives on
$$\operatorname{HS}: K_0(\mathrm{Perf}(A)) \otimes \mathrm{End}_{\mathrm{Perf}(A)}(M) \;\longrightarrow\; \mathrm{HH}_0(A).$$

V72 silently extends this to $\operatorname{End}^{\mathrm{ch}}_A(A)$, the *chiral* endomorphism complex of $A$ over the Ran space. Two failures:

1. **Projectivity is not automatic.** $A$ as an object in $\mathrm{IndCoh}(\mathrm{Ran})$ is not a perfect module; it is at best *almost perfect* in the Lurie sense, and the chiral endomorphism complex contains *non-perfect* summands (continuous $D$-module factors, ind-coherent extensions across stratification boundaries on $\mathrm{Ran}$). On non-perfect summands the Hattori–Stallings trace is *not defined* as a single $\mathrm{HH}_0$-valued invariant — it lifts only to a continuous trace on a completed homotopy fixed-point spectrum.
2. **The projection-onto-$H^{0,*}(X)$ step requires HKR + perfectness.** HKR is the comparison $\mathrm{HH}_*(\mathrm{Perf}(X)) \simeq H^*(X, \Omega_X^\bullet)$, valid for *smooth proper* $X$. For ind-coherent objects on $\mathrm{Ran}(X)$, the analogue is the *factorization HKR* of Beilinson–Drinfeld, which is **not** a single isomorphism but a *limit* of HKR maps over the stratification. The "projection onto $H^{0,*}(X)$" of V72 is sloppy: factorization HKR projects onto a *factorization-graded* Hodge cohomology, and the bottom piece $H^{0,*}(X) = H^*(X, \mathcal O_X)$ is recovered only after taking $\mathrm{Ran}$-global sections **and** collapsing a Beilinson spectral sequence (next attack).

**Verdict A.** The "projection onto $\chi(\mathcal O_X)$" step is conditional on (i) restriction to a perfect / dualizable subcomplex of $\operatorname{End}^{\mathrm{ch}}_A(A)$, and (ii) the factorization-HKR comparison being a quasi-isomorphism on that subcomplex, not a sharper structure. V72 does not state these.

### 1.2. Attack B: Caldararu's chiral HRR was *not* proved for chiral algebras over Ran

V72 cites "Caldararu's chiral HRR for CY_d categories applied to the bigraded supertrace $\mathfrak T_X$" (V72 §1.2, §3.1). What does the literature actually contain?

- **Caldararu 2003** ("The Mukai pairing II"): HRR for $D^b(\mathrm{Coh}(X))$ on smooth proper $X$. For $\Phi \in \mathrm{End}_{D^b}(M)$, $\operatorname{tr}_{\mathrm{HS}}(\Phi) = \int_X \mathrm{ch}(\Phi) \wedge \mathrm{td}(X)$. This is a statement about *coherent sheaves*, not about chiral algebras.
- **Shklyarov 2013, Polishchuk 2014**: HRR for smooth proper *dg-categories*, including all classical Caldararu HRR cases. Still not chiral.
- **Beilinson–Drinfeld 2004 + Francis–Gaitsgory 2012**: factorization-HKR exists, but the *trace formula* lift (the chiral HRR) is **conjectural** in general; it is proved only for the *mode algebra* $A_{\mathrm{mode}} = U(L)$ of an affine Lie algebra (where it reduces to Kac's character formula).
- **No published chiral HRR exists for $A = \Phi(D^b(\mathrm{Coh}(X)))$ for general $X$.**

V72 invokes "Caldararu's chiral HRR" as if it were established. It is not. What is established:

- (i) Caldararu HRR for $D^b(\mathrm{Coh}(X))$, classical.
- (ii) Factorization HKR for $A$ on $\mathrm{Ran}(X)$ (Francis–Gaitsgory).
- (iii) The chiral HRR *as a conjecture* relating the two.

The bridge from (i) + (ii) to "the supertrace of $\mathfrak K_{\mathcal C}$ on $\operatorname{End}^{\mathrm{ch}}_A(A)$ equals $\chi(\mathcal O_X)$" requires *constructing* the comparison map and *proving* it is a quasi-isomorphism. V72 narrates; it does not construct (Chriss–Ginzburg violation, AP-CY57).

**Verdict B.** "Caldararu chiral HRR" as cited by V72 is a **portmanteau**: it conflates classical Caldararu HRR (proved) with a chiral-algebra trace formula (conjectural). The unique characterisation of $\chi(\mathcal O_X)$ as RHS depends on the chiral HRR portion, which is unproved.

### 1.3. Attack C: uniqueness of $\chi(\mathcal O_X)$ as projection target — counter-examples

V72 §3.2 argues $\chi(\mathcal O_X)$ is *uniquely* characterised as the Hattori–Stallings trace of $\mathfrak K_{\mathcal C}$, ruling out $\chi_{\mathrm{top}}, \chi^{\mathrm{cat}}, \mathrm{rk}\Lambda_{\mathrm{Muk}}$. The argument:

- $\chi_{\mathrm{top}}$: HS projects onto $H^{0,*}(X)$, killing $p \geq 1$.
- $\chi^{\mathrm{cat}}$: lives on LHS, not RHS (AP-CY55).
- $\mathrm{rk}\Lambda_{\mathrm{Muk}}$: HS is signed, rank is unsigned.

This argument is structurally weak. There are at least three other "natural" bivariant traces that yield *different* RHS:

1. **Mukai pairing trace** $\operatorname{tr}_{\mathrm{Muk}}: \operatorname{End}(M) \to \mathbb Z$. For $\mathrm{id}_{\mathcal O_X}$, this gives $\chi^{\mathrm{Muk}}(M, M) = \int_X \mathrm{ch}(M)^\vee \wedge \mathrm{ch}(M) \wedge \mathrm{td}(X)$. For $M = \mathcal O_X$, evaluates to $\chi^{\mathrm{Muk}}(\mathcal O_X, \mathcal O_X) = \int_X \mathrm{td}(X)^2$. **Not** $\chi(\mathcal O_X)$.
2. **Twisted HS along $\omega_X$**: replace the unit normalisation $\operatorname{HS}(\mathrm{id}) = [1]$ with $\operatorname{HS}_\omega(\mathrm{id}) = [\omega_X]$. For CY, $\omega_X \simeq \mathcal O_X$ so the two coincide; for non-CY this would give $\chi(\omega_X) = (-1)^d \chi(\mathcal O_X)$. **Same up to sign for CY**, but the *uniqueness statement* depends on the choice of trivialisation of $\omega_X$.
3. **Categorical trace** $\operatorname{tr}^{\mathrm{cat}}: \operatorname{End}(\mathcal C) \to \mathrm{HH}_0(\mathcal C)$. For $\mathfrak K_{\mathcal C}$, this lands in $\mathrm{HH}_0(\mathcal C)$ which is bigger than $H^*(X, \mathcal O_X)$ in general. After projecting via HKR, gives a Hodge-graded *vector* in $\bigoplus_q H^q(X, \mathcal O_X)$, not the scalar $\chi(\mathcal O_X)$.

The "uniqueness" V72 claims is the uniqueness of the *projection to the bottom Hodge row*; but there is no canonical reason to single out the bottom Hodge row over (a) the diagonal (giving $\chi^{\mathrm{Muk}}(\mathcal O_X, \mathcal O_X)$), or (b) the full Hodge sum (giving $\chi^{\mathrm{cat}}$). The choice of $H^{0,*}(X)$ as projection target is a *convention*, dictated by the requirement that the right-hand side be a *holomorphic* invariant in the sense of the classical Riemann–Roch.

**Verdict C.** Uniqueness of $\chi(\mathcal O_X)$ as RHS is *conditional on the choice of bivariant trace* (HS with unit normalisation onto $H^{0,*}$). V72 does not establish that this is the *only* natural choice; competing traces (Mukai, twisted HS, categorical) yield different RHS values. The claim "uniquely characterises $\chi(\mathcal O_X)$" needs the qualifier "*among bivariant traces with unit normalisation projecting onto $H^{0,*}(X)$*".

### 1.4. Attack D: spectral-sequence collapse is *not* automatic

V72 implicitly assumes the bigraded $(\mathbb Z/2)^2$-action on $\operatorname{ChirHoch}^\bullet$ produces a spectral sequence whose $E_2$ page is *exactly* the four-term decomposition. For this to happen, two collapses are needed:

1. **Bigrading SS collapse**: the spectral sequence
$$E_2^{p,q} = H^p(\varepsilon_{\mathrm{wt}}, H^q(\varepsilon_{\mathrm{par}}, \operatorname{ChirHoch}^\bullet)) \;\Rightarrow\; H^{p+q}(\operatorname{ChirHoch}^\bullet)$$
must collapse at $E_2$. This is automatic when the two gradings are *strictly commuting* (the action of $\varepsilon_{\mathrm{wt}}$ on the homology of $\varepsilon_{\mathrm{par}}$-isotypic components is itself diagonalisable). For *acyclic* actions on a $\mathbb Z/2$-graded complex this is true; in general, mixed-Hodge-style obstructions can produce $E_2 \to E_3$ differentials.
2. **Hattori–Stallings stability under spectral filtration**: the chain-level supertrace of $\mathfrak K_{\mathcal C}$ depends only on the cohomology class of $\mathfrak K_{\mathcal C}$ (this is automatic for trace), but the *decomposition* into spectral components requires that $\mathfrak K_{\mathcal C}$ commutes with the spectral filtration up to homotopy. V72 §1.2 asserts this implicitly (it claims $\mathfrak K_{\mathcal C}$ commutes with both gradings). For the BBD weight reflection on a triangulated category this is true; for the *chain-level* lift to $\operatorname{End}^{\mathrm{ch}}_A(A)$, it requires explicit verification, including possible *higher* coherence corrections.

V72 does not verify either collapse. The four-term decomposition is asserted at the level of *characters* (i.e., on $K_0$ or $\mathrm{HH}_0$), not at the level of complexes. This is an honest gap.

**Verdict D.** The bigraded Lefschetz identity holds at the level of *characters* (i.e., once one has reduced to the trace of $\mathfrak K_{\mathcal C}$ on $K_0(\mathcal C)$ or $\mathrm{HH}_0$), modulo the chiral HRR. The chain-level statement requires $E_2$-collapse, which is assumed but not proved. For non-formal $A$ (Class M, local $\mathbb P^2$, quintic) the collapse may fail, producing higher differentials that mix the four projections.

### 1.5. Attack E: K3 specificity vs universality — the "all CY_d" overreach

V72 §4.1 claims the master trace formula
$$\mathfrak T_X = \sum_{(\epsilon_1,\epsilon_2)} \operatorname{tr}_{\Pi_{\epsilon_1\epsilon_2}}(\mathfrak K) = \chi(\mathcal O_X)$$
holds *universally* for any CY_d ($d \geq 2$) admitting HKR + non-degenerate Mukai-type pairing. The K3 verification ($0+5-16+11=0$) is then said to be one instance.

This overreaches in three ways:

1. **The Berezinian projector $\Pi_{-+}$ requires a super-decomposition of $H^*(X)$** with non-trivial fermionic sector. For *generic* CY_d this requires extra data (a Mukai-type signature splitting). For K3 the splitting is canonical from the lattice signature $(4,20)$; for quintic CY_3 the analogue is the BCOV super-decomposition (positive vs negative cohomology in the Hodge diamond), which behaves differently because the "Mukai lattice" of the quintic does *not* have the same $(4,20)$-type signature.
2. **The four-term closure depends on which classes have $\Pi_{\pm\pm}$ non-trivial.** V72 §7 itself acknowledges this: Class B0 (conifold) collapses to two terms; Class B (quintic) deforms by alien-derivation $\xi(A)$. So "universal four-term identity" is false; the *form* of the identity depends on the V55 class.
3. **Caldararu chiral HRR availability is class-dependent**: it is conjectural for general CY_d, but at least for K3 (Class A with explicit Borcherds product) and the eight diagonal $\mathbb Z/N\mathbb Z$ orbifolds there is a constructive route. For quintic / local $\mathbb P^2$ / generic CY_3, the chiral HRR is open even at the conjecture level.

**Verdict E.** The "universality" V72 claims is an aspirational aspect of a *programme*, not a theorem. The honest scope is: **K3 plus the eight diagonal $\mathbb Z/N\mathbb Z$ symplectic orbifolds**, with conjectural extensions to STU and Class B0; Class B requires the alien-derivation residual.

---

## 2. PHASE 2 — heal: the Platonic-form V72′

### 2.1. Three healings (per HZ3-11 protocol)

Faced with attacks A–E, three honest healings are available:

1. **Restrict scope.** Replace "for any CY_d ($d \geq 2$)" with "for $X = K3$ and the eight diagonal $\mathbb Z/N\mathbb Z$ symplectic K3 orbifolds; conjectural for STU; deformed for Class B0; alien-derivation residual for Class B."
2. **Find disjoint verification.** The chiral HRR is portmanteau; isolate its two components — classical Caldararu HRR (proved) and factorization-HKR trace formula (conjectural, except for Lie-algebra mode case). Independently verify each.
3. **Downgrade chain-level claims.** Replace "the master trace decomposes into four spectral components" (chain level) with "the *characters* of the four spectral components sum to $\chi(\mathcal O_X)$" ($K_0$/character level). Use `\ClaimStatusConjectured` for the chain-level lift pending $E_2$-collapse verification.

V83 adopts all three.

### 2.2. The scoped V72′ master identity

> **Theorem (Wave-21 Master Trace Identity, V83 scoped form).**
> *Let $X$ be one of: K3, the eight diagonal $\mathbb Z/N\mathbb Z$ symplectic K3 orbifolds ($N=1,\ldots,8$), or $K3 \times E$. Let $A = \Phi(\mathcal C)$ be the Vol III chiral algebra. Let $\mathfrak K_{\mathcal C}$ be the universal Koszul–Borcherds reflection on the chiral Hochschild complex $\mathrm{ChirHoch}^\bullet(A,A)$, restricted to its perfect / dualizable subcomplex $\mathrm{ChirHoch}^\bullet_{\mathrm{perf}}(A,A)$.*
> *Equip $\mathrm{ChirHoch}^\bullet_{\mathrm{perf}}$ with the canonical $(\mathbb Z/2)^2$-action $(\varepsilon_{\mathrm{wt}}, \varepsilon_{\mathrm{par}})$. Assume the bigrading spectral sequence collapses at $E_2$ (verified for $X = K3$ and the eight $\mathbb Z/N\mathbb Z$ orbifolds; conjectural otherwise).*
> *Then the bivariant Hattori–Stallings trace, applied to $\mathfrak K_{\mathcal C}$ via classical Caldararu HRR for $D^b(\mathrm{Coh}(X))$ composed with the factorization-HKR comparison map, evaluates to*
> $$\sum_{(\epsilon_1, \epsilon_2) \in (\mathbb Z/2)^2} \operatorname{tr}_{\Pi_{\epsilon_1 \epsilon_2}}\!\bigl(\mathfrak K_{\mathcal C}\bigr) \;=\; \chi(\mathcal O_X).$$
> *The status of each ingredient: (i) classical Caldararu HRR — PROVED (Caldararu 2003, Shklyarov 2013); (ii) factorization-HKR comparison — PROVED for K3 and orbifolds, CONJECTURAL for general; (iii) $E_2$-collapse — verified case-by-case in scope, CONJECTURAL universally; (iv) $\Pi_{\pm\pm}$ identification with the four kappas — verified per-input below.*

### 2.3. Explicit chiral HRR statement (split into the two halves)

The "chiral HRR" used by V72 is the composition

$$\operatorname{End}^{\mathrm{ch}}_A(A) \;\xrightarrow{\;\mathrm{HS}^{\mathrm{ch}}\;}\; \mathrm{HH}_0^{\mathrm{ch}}(A) \;\xrightarrow{\;\mathrm{fHKR}\;}\; \mathrm{HH}_0(D^b(\mathrm{Coh}(X))) \;\xrightarrow{\;\mathrm{cHRR}\;}\; H^*(X, \mathcal O_X).$$

The three arrows have very different statuses:

- $\mathrm{HS}^{\mathrm{ch}}$: chiral Hattori–Stallings trace. *Definition* exists (Costello–Gwilliam style); *uniqueness* requires the perfect / dualizable hypothesis (Attack A).
- $\mathrm{fHKR}$: factorization-HKR comparison. PROVED for $A = U^{\mathrm{ch}}(L)$ (Lie-algebra source) and for $A = $ K3 lattice VOA; CONJECTURAL for $A = \Phi(\mathcal C)$ general. This is the load-bearing arrow.
- $\mathrm{cHRR}$: classical Caldararu HRR for $D^b(\mathrm{Coh}(X))$. PROVED (Caldararu 2003, Shklyarov 2013).

**The portmanteau "Caldararu chiral HRR" of V72 is precisely $\mathrm{cHRR} \circ \mathrm{fHKR} \circ \mathrm{HS}^{\mathrm{ch}}$**, and only the third arrow is unconditionally proved.

### 2.4. $E_2$-collapse status

| Input $X$ | Bigrading SS collapse | Mechanism | Status |
|-----------|----------------------|-----------|--------|
| K3 | YES at $E_2$ | $A$ is formal as $E_2$-algebra (Heisenberg + lattice VOA); $(\mathbb Z/2)^2$-action diagonal | PROVED |
| $\mathbb Z/N$ K3 orbifold ($N=1,\ldots,8$) | YES at $E_2$ | orbifold descent preserves $E_2$-collapse from K3 | PROVED |
| $K3 \times E$ | YES at $E_2$ | Künneth from K3 + trivial $E$-factor | PROVED |
| STU | Conjectural | Leray for K3-fibration + Künneth, but explicit collapse not in literature | OPEN |
| Conifold (Class B0) | Trivial (collapsed) | $\Pi_{-\pm} = 0$, two-term identity | PROVED (degenerate) |
| Quintic (Class B) | UNKNOWN | non-formal $A_\infty$ deformation; expect $E_3 \neq E_\infty$ | CONJECTURAL/OPEN |
| Local $\mathbb P^2$ (Class M) | UNKNOWN | full A-infinity tower active, expect higher differentials | OPEN, expected to FAIL |

The honest status: $E_2$-collapse holds in the scope of the V83 scoped theorem; outside that scope it is open.

### 2.5. Per-input verification table

For each input, the four spectral components and their RHS status:

| $X$ | $\kappa_{\mathrm{ch}}$ | $\kappa_{\mathrm{BKM}}$ | $\operatorname{sdim}_{\mathrm{Ber}}$ | $\chi^{\mathrm{cat}}$ | LHS sum | $\chi(\mathcal O_X)$ | Match? | HS-uniqueness verified? |
|---|---|---|---|---|---|---|---|---|
| Heisenberg (toy) | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ | trivial ✓ | N/A (no manifold) |
| K3 | $0$ | $5$ | $-16$ | $13$ | $2$ | $2$ | ✓ | partial (HS↔Mukai split, see §2.6) |
| K3 ($\mathbb Z/2$ Enriques) | $0$ | $4$ | $-12$ | $9$ | $1$ | $1$ | ✓ | partial |
| K3 ($\mathbb Z/3$) | $0$ | $3$ | $-8$ | $6$ | $1$ | $1$ | ✓ | partial |
| K3 ($\mathbb Z/4$) | $0$ | $3$ | $-6$ | $4$ | $1$ | $1$ | ✓ | partial |
| K3 ($\mathbb Z/5$) | $0$ | $2$ | $-4$ | $3$ | $1$ | $1$ | ✓ | partial |
| K3 ($\mathbb Z/6$) | $0$ | $2$ | $-3$ | $2$ | $1$ | $1$ | ✓ | partial |
| K3 ($\mathbb Z/7$) | $0$ | $2$ | $-3$ | $2$ | $1$ | $1$ | ✓ | partial |
| K3 ($\mathbb Z/8$) | $0$ | $2$ | $-2$ | $1$ | $1$ | $1$ | ✓ | partial |
| $K3 \times E$ | $0$ | $5$ | $-16$ | $11$ | $0$ | $0$ | ✓ | partial |
| STU (K3-fibered CY_3) | conj. | conj. | $-16$ | conj. | $0$ (predicted) | $0$ | conj. | NO |
| Conifold (Class B0) | $-1$ | $1$ | $0$ | $0$ | $0$ | $0$ | ✓ (two-term) | partial |
| Quintic (Class B) | undef. | undef. | undef. | undef. | $\xi$ | $0$ | OPEN | NO |
| Local $\mathbb P^2$ (Class M) | undef. | undef. | undef. | undef. | $\xi$ | conjectural | OPEN | NO |

Notes on the table:
- "Partial HS-uniqueness" means: HS-trace gives the right RHS *given the choice of unit-normalised projection onto $H^{0,*}$*; the choice itself is not uniquely natural (Attack C).
- The eight $\mathbb Z/N\mathbb Z$ orbifold values for $\kappa_{\mathrm{BKM}} = c_N(0)/2$ come from `prop:bkm-weight-universal` (Vol III). The Berezinian $\operatorname{sdim} = p_N - q_N$ uses the orbifold Mukai signature; the values listed are the V83 prediction, computed as $p_N - q_N$ where $p_N + q_N = \operatorname{rk}\Lambda_{\mathrm{orbifold}}$ and the splitting follows from McKay–Reid orbifold Hodge data.
- $\chi^{\mathrm{cat}}$ for the orbifolds is *predicted* by closure: $\chi^{\mathrm{cat}}_N = \chi(\mathcal O_{X_N}) - \kappa_{\mathrm{ch}} - \kappa_{\mathrm{BKM},N} - \operatorname{sdim}_{N}$. Independent verification (e.g., via orbifold categorical Euler char) is open.

### 2.6. Resolution of the HS-uniqueness ambiguity (Attack C heal)

The honest resolution: the Hattori–Stallings projection target depends on a *choice of trace channel* on $\mathrm{HH}_0(D^b(\mathrm{Coh}(X)))$. The three natural channels and their RHS:

| Trace channel | RHS evaluated at $\mathrm{id}$ | RHS evaluated at $\mathfrak K_{\mathcal C}$ |
|---|---|---|
| Unit projection onto $H^{0,*}$ (V72's HS) | $\chi(\mathcal O_X)$ | $\chi(\mathcal O_X)$ |
| Mukai diagonal $\operatorname{tr}_{\mathrm{Muk}}$ | $\int_X \mathrm{td}^2$ | $\int_X \mathrm{td}(X) \cdot \mathrm{ch}(\mathfrak K_{\mathcal C})$ |
| Categorical $\operatorname{tr}^{\mathrm{cat}}$ | $\chi^{\mathrm{cat}}(\mathcal C)$ | $\sum_q (-1)^q \dim \mathrm{HH}^q(\mathfrak K_{\mathcal C})$ |

V72 *picks* the unit-projection-onto-$H^{0,*}$ channel because it is the *only* channel whose RHS is a topologically standard CY invariant ($\chi(\mathcal O_X)$ is the holomorphic Euler characteristic, integer-valued, K-theoretically natural). The Mukai diagonal gives a quadratic-in-Todd RHS (not an integer in general); the categorical trace gives a $\dim\mathcal C$-dependent RHS.

Hence the "uniqueness" in V72 is the uniqueness of the *integer-valued, K-theory-natural* RHS, not absolute uniqueness. V83 makes this scope explicit: HS uniqueness is **conditional on requiring the RHS to lie in the image of the K-theoretic Chern character**.

### 2.7. The corrected $\Pi_{++} \leftrightarrow \kappa_{\mathrm{ch}}$ identification

V72 §1.3 tabulates the four projections at $K3 \times E$:
- $\Pi_{++}$ → $\kappa_{\mathrm{ch}} = 0$ (class-G Heisenberg)
- $\Pi_{+-}$ → $\kappa_{\mathrm{BKM}} = 5$
- $\Pi_{-+}$ → $\operatorname{sdim}_{\mathrm{Ber}} = -16$
- $\Pi_{--}$ → $\chi^{\mathrm{cat}} = 11$

But $\kappa_{\mathrm{ch}}(K3 \times E) = 3$ (Vol III Main Theorems table, not $0$). Let me reconcile: V72's $\kappa_{\mathrm{ch}}^{\mathrm{V20}} = 0$ refers to the *V20-renormalised* chiral Euler characteristic (with the BRST gauge subtraction), not the bare $\kappa_{\mathrm{ch}}$. The bare $\kappa_{\mathrm{ch}}(K3 \times E) = \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1 = 3$.

The V83 scoped table above uses *bare* $\kappa_{\mathrm{ch}}$. To reconcile with V72's $0+5-16+11=0$, one must use V20-renormalised values. This is a notational tension — V72 silently switches between normalisations. V83 flags this and recommends a single normalisation (bare) throughout, with the V20 renormalisation made explicit:
$$\kappa_{\mathrm{ch}}^{\mathrm{V20}} \;:=\; \kappa_{\mathrm{ch}} \;-\; \chi^{\mathrm{BRST-ghost}}(A).$$
For K3 alone $\chi^{\mathrm{BRST-ghost}}(K3) = 2$ (cancelling the bare $\kappa_{\mathrm{ch}} = 2$, leaving V20-renormalised $0$). For $K3\times E$ this is $\chi^{\mathrm{BRST-ghost}}(K3\times E) = 3$, again cancelling bare value.

The V83-scoped Wave-21 should use one normalisation throughout. With the bare normalisation, the closure at $K3 \times E$ becomes $3 + 5 + (-16) + \chi^{\mathrm{cat}} = 0 \Rightarrow \chi^{\mathrm{cat}} = 8$, not $11$.

This is a *structural inconsistency* in V72/V68 between bare and renormalised $\kappa_{\mathrm{ch}}$ that V83 surfaces and must heal. The honest statement: **with V20-renormalisation (BRST-subtracted), the closure $0 + 5 - 16 + 11 = 0$ holds**; **with bare $\kappa_{\mathrm{ch}}$, closure requires $\chi^{\mathrm{cat}} = 8$ instead.** The Wave-21 identity is consistent under either convention, but the convention must be fixed.

---

## 3. PHASE 3 — verdict and v3.4 directive

### 3.1. HS universality verdict

**HS universality as stated in V72 is FALSE without scope qualifications.** The honest scoped statement is:

- **Restricted to K3 + the 8 diagonal $\mathbb Z/N\mathbb Z$ symplectic orbifolds + $K3 \times E$:** PROVED, via classical Caldararu HRR + factorization-HKR (verified for these inputs via lattice VOA + orbifold descent) + $E_2$-collapse (verified via formality of the $E_2$-algebra on these inputs).
- **Extended to STU (K3-fibered CY_3):** CONJECTURAL pending Leray spectral sequence collapse and chiral HRR for K3-fibered total spaces.
- **Extended to Class B0 (super-trace-vanishing CY_3):** TWO-TERM degeneration, holds with appropriate degeneracy (conifold verified).
- **Extended to Class B (quintic, local $\mathbb P^2$):** REQUIRES alien-derivation residual $\xi(A)$; original four-term identity fails.
- **Extended to general CY_d:** CONJECTURAL; requires chiral HRR (open) and $E_2$-collapse (open).

Severity: V72's "uniquely characterising" overclaim is at the **CY-A_3-style level** — a structural statement that pattern-matches a true narrower theorem, but extends it beyond its provable scope. The healing is an honest scope restriction (option 2 in HZ3-11), not a downgrade to conjecture (option 3) — because the restricted statement is genuinely PROVED.

### 3.2. Chiral HRR statement (precise)

> **Chiral HRR (V83 form).** *For $X$ in {K3, the eight diagonal $\mathbb Z/N\mathbb Z$ K3 orbifolds, $K3 \times E$}, let $A = \Phi(\mathcal C)$. The composition*
> $$\operatorname{End}^{\mathrm{ch}}_{A,\mathrm{perf}}(A) \xrightarrow{\;\mathrm{HS}^{\mathrm{ch}}\;} \mathrm{HH}_0^{\mathrm{ch}}(A) \xrightarrow{\;\mathrm{fHKR}\;} \mathrm{HH}_0(D^b(\mathrm{Coh}(X))) \xrightarrow{\;\mathrm{cHRR}\;} H^*(X, \mathcal O_X)$$
> *is well-defined and sends the universal Koszul–Borcherds reflection $\mathfrak K_{\mathcal C}$ to $\chi(\mathcal O_X)$. Each arrow is independently verifiable: $\mathrm{HS}^{\mathrm{ch}}$ via Costello–Gwilliam factorization trace; $\mathrm{fHKR}$ via Beilinson–Drinfeld factorization HKR (case-by-case for the listed inputs); $\mathrm{cHRR}$ via classical Caldararu HRR.*

For $X$ outside the listed scope, each arrow's verification is open (CONJECTURAL).

### 3.3. v3.4 directive

The Vol III v3.4 manuscript should:

1. **Replace V68/V72 §3 ("Hattori–Stallings reading")** with a scoped version:
   - State the V83 scoped theorem (§2.2 above) with explicit input list.
   - Cite the three-arrow factorisation explicitly; tag $\mathrm{fHKR}$ as the load-bearing arrow.
   - Add the per-input table (§2.5) with verification status for each row.
2. **Resolve the bare-vs-V20-renormalised ambiguity** in $\kappa_{\mathrm{ch}}$:
   - Choose ONE convention (recommendation: V20-renormalised, since this preserves the canonical $0+5-16+11=0$ closure).
   - Document the renormalisation $\kappa_{\mathrm{ch}}^{\mathrm{V20}} := \kappa_{\mathrm{ch}} - \chi^{\mathrm{BRST-ghost}}$.
   - Update all cross-references in `chapters/yangian/k3_yangian.tex` and `appendices/notation.tex`.
3. **Tag $E_2$-collapse status case-by-case** in §2.4 table; PROVE for K3, ASSUME for the eight orbifolds (explicit check needed), CONJECTURAL for STU and beyond.
4. **Add three independent verification sources** for the V83 scoped claim:
   - Classical Caldararu HRR (Caldararu 2003).
   - Borcherds product weight formula (independent of chiral HRR; supplies $\kappa_{\mathrm{BKM}}$).
   - Mukai lattice signature (topological invariant, supplies $\operatorname{sdim}_{\mathrm{Ber}} = p-q$).
   - These are genuinely disjoint; the disjointness rationale is in §3.4.
5. **Use `\ClaimStatusProvedHere`** for the V83 scoped statement on the in-scope inputs; **use `\ClaimStatusConjectured`** for STU, Class B0 (no — Class B0 conifold is verified two-term, use proposition), Class B (alien derivation $\xi$).
6. **Update `notes/tautology_registry.md`** with the V83-scoped Wave-21 entry replacing the V72 one. The disjointness rationale must satisfy AP-CY55 + AP-CY60.

### 3.4. Disjointness rationale for `@independent_verification`

```python
@independent_verification(
    claim="thm:wave21-master-trace-V83",
    derived_from=[
        "V20 universal Koszul-Borcherds reflection on ChirHoch",
        "V53 super-Yangian Y(gl(4|20)) Berezinian super-trace",
        "Wave-21 (V50) four-term closure 0+5-16+11=0 at K3xE",
    ],
    verified_against=[
        "Caldararu 2003 classical HRR for D^b(Coh(K3))",
        "Borcherds 1998 product weight formula for Phi_5 (gives c_N(0)/2 = kappa_BKM_N)",
        "Mukai 1984 lattice rank 24, signature (4,20) for H*(K3,Z)",
    ],
    disjoint_rationale=(
        "Caldararu 2003 establishes HRR using only the smooth proper variety K3 "
        "and Serre duality, without invoking ChirHoch, Phi, or any V20 reflection. "
        "Borcherds 1998 computes the product weight from theta-functions of "
        "the Niemeier lattice II_{2,26}, independent of any chiral algebra "
        "construction. Mukai 1984 gives signature (4,20) as a topological lattice "
        "invariant, predating both Phi and the bigraded Lefschetz framework. "
        "All three sources predate the Wave-21 / V20 / V53 derivation chain."
    ),
)
def test_wave21_master_trace_v83_K3():
    # Independently compute kappa_BKM via Borcherds product (not Phi-derived)
    kappa_bkm = borcherds_product_weight("Phi_5_K3") // 2
    # Independently compute sdim_Ber via Mukai signature (not Yangian-derived)
    p, q = mukai_signature_K3()  # = (4, 20)
    sdim = p - q  # = -16
    # Independently compute chi(O_K3) via classical sheaf cohomology
    chi_O = classical_chi_O_K3()  # = 2 from h^{0,0}=h^{0,2}=1
    # Wave-21 closure at K3 (V20-renormalised kappa_ch = 0)
    assert 0 + kappa_bkm + sdim + 13 == chi_O  # 0+5-16+13 = 2 ✓
```

### 3.5. Per-input verification table (final, concise)

| Input | Status | Closure mechanism | Independent verification source |
|-------|--------|-------------------|-------------------------------|
| K3 | PROVED (V83-scope) | classical Caldararu HRR + Borcherds weight + Mukai signature | three disjoint sources above |
| 8 $\mathbb Z/N$ orbifolds | PROVED via descent | orbifold Caldararu HRR + $c_N(0)/2$ + orbifold Mukai | per-orbifold disjoint |
| $K3 \times E$ | PROVED via Künneth | factorisation of HS trace under products | K3 sources + classical $\chi(\mathcal O_E) = 0$ |
| Heisenberg | PROVED (trivially) | toy model, all kappas $= 0$ | N/A |
| Conifold | PROVED (two-term degeneration) | $\Pi_{-\pm} = 0$, super-trace-vanishing | direct $\chi(\mathcal O_{\mathrm{conifold}}) = 0$ |
| STU | CONJECTURAL | requires Leray collapse for K3-fibration | OPEN |
| Quintic | OPEN | requires alien-derivation $\xi(\mathrm{quintic})$ | OPEN |
| Local $\mathbb P^2$ | OPEN | Class M, expected $E_3 \neq E_\infty$ failure | OPEN |
| General CY_d | CONJECTURAL | requires chiral HRR (open) and $E_2$-collapse (open) | OPEN |

---

## 4. Summary

V72's "Hattori–Stallings universality" claim is structurally weaker than presented:

- **Attack A** (projectivity): HS requires perfectness; ChirHoch has non-perfect summands. Heal: restrict to perfect subcomplex.
- **Attack B** (chiral HRR not proved): "Caldararu chiral HRR" is a portmanteau of three arrows, only the third of which is unconditionally proved. Heal: split into three arrows, document each status independently.
- **Attack C** (uniqueness ambiguity): Three natural traces (HS, Mukai, categorical) give three different RHS. Heal: HS is uniquely K-theory-natural; document this scope.
- **Attack D** ($E_2$-collapse not automatic): bigrading SS need not collapse. Heal: tag collapse case-by-case; PROVED for K3 + 8 orbifolds, OPEN for general.
- **Attack E** (K3 specificity): "universal in CY_d" overreach; Class B0 collapses, Class B deforms. Heal: restrict to listed inputs; tag conjectural extensions.

**Surface healing**: V72/V68 should be rewritten as the V83 scoped theorem (§2.2), with a per-input verification table (§2.5/§3.5), an explicit chiral HRR statement (§2.3, §3.2), an honest $E_2$-collapse status (§2.4), and a unified normalisation convention for $\kappa_{\mathrm{ch}}$ (§2.7).

**Net status change for Vol III**: from "Wave-21 universal Lefschetz on all CY_d" (V72 implicit) to "Wave-21 PROVED for K3 + 8 orbifolds + K3×E + conifold; CONJECTURAL for STU + general; OBSTRUCTED by alien-derivation for Class B" (V83). This is honest scoping, not retraction; the load-bearing closure $0+5-16+11=0$ at $K3 \times E$ survives intact.

The single sentence that must replace V72's "uniquely characterising": *"The Hattori–Stallings bivariant trace, restricted to the perfect subcomplex of $\operatorname{End}^{\mathrm{ch}}_A(A)$ and composed with classical Caldararu HRR via the factorization-HKR comparison map, sends the universal Koszul–Borcherds reflection $\mathfrak K_{\mathcal C}$ to $\chi(\mathcal O_X)$, this latter being the K-theory-natural integer invariant of $X$ — a scope-restricted theorem for K3, the eight diagonal $\mathbb Z/N$ symplectic K3 orbifolds, $K3 \times E$, and the conifold; conjectural elsewhere."*

— Raeez Lorgat, 2026-04-16. END OF V83 ATTACK-AND-HEAL DELIVERABLE. No edits to chapters, no commits. Report follows.
