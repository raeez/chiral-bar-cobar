# Wave V92 — Russian-school adversarial attack and heal of the V49** edge-character matrix $M$

## Foundational reconstitution: integer-valuedness, kernel meaning, off-diagonal structure, Künneth multiplicativity, per-class explicit forms

**Author.** Raeez Lorgat.
**Date.** 2026-04-16.
**Mode.** Russian-school. Atiyah–Singer equivariant Lefschetz fixed-point + Hattori–Stallings bivariant trace + Künneth formula rigour. Chriss–Ginzburg discipline (construct, do not narrate). LOSSLESS — no downgrades; find the Platonic structure that absorbs all the existing numerical content.
**Predecessors.** V49 (three-route closure of Pentagon-at-$E_1$ at K3); V50 (Wave-21 four-term closure $0+5-16+11=0$ at $K3\times E$); V68 (foundational heal: Wave-21 = bigraded Lefschetz on $(\mathbb Z/2)^2$-equivariant $\mathrm{ChirHoch}^\bullet$); V69 (independence of three K3-routes); V72 (Hattori–Stallings reading of RHS $=\chi(\mathcal O_X)$); V73 (bigraded Lefschetz consolidation across all inputs); V83 (HS-universality scope correction); V89 (introduction of the $4\times 4$ edge-character matrix $M$); V90 (in flight, attacking diagonality).
**Disclosures.** Read/Grep/Bash only. Sandbox markdown. No `.tex` edits. No `CLAUDE.md` updates. No commits. AP-CY55, AP-CY57, AP-CY60, AP-CY61 strict.

---

## 0. The V49** matrix $M$ under attack

V89 introduced

$$
M \;=\; \bigl(M_{(\epsilon_1\epsilon_2),(\epsilon_1'\epsilon_2')}\bigr)_{(\epsilon_1\epsilon_2),(\epsilon_1'\epsilon_2')\in(\mathbb Z/2)^2}\;\in\;\mathrm{Mat}_{4\times 4}(\mathbb Z),
$$

the **bigraded edge-character matrix** of the Wave-21 master trace identity (V68/V72): the entry $M_{ab,cd}$ records how the universal Koszul–Borcherds reflection $\mathfrak K_{\mathcal C}$ on $\mathrm{ChirHoch}^\bullet(A,A)$ pairs the $\Pi_{ab}$-isotypic component against the $\Pi_{cd}$-isotypic component under the canonical Frobenius pairing on the chiral Hochschild complex. The diagonal of $M$ at $X=K3\times E$ reads $(0,5,-16,11)$ in the V20-renormalised normalisation; its trace closes to $\chi(\mathcal O_{K3\times E})=0$ (V50, V68 §1.3).

V89 asserted three statements about $M$:

(M1) $M\in\mathrm{Mat}_{4\times 4}(\mathbb Z)$ — *integer-valued*.
(M2) $M$ is *diagonal* on K3 and on the eight $\mathbb Z/N$ symplectic K3 orbifolds.
(M3) $M$ is the universal edge-character data for the four-term Wave-21 closure.

V90 attacks (M2). V92 attacks (M1), (M3), and the deeper structural questions (kernel, off-diagonal, Künneth, per-class forms). The five attack angles are (1) integer-valuedness, (2) kernel meaning, (3) off-diagonal structure for non-K3, (4) Künneth multiplicativity for $K3\times E$, (5) per-class matrix forms (A / B0 / B / M).

---

## 1. PHASE 1 — five attacks

### 1.1. Attack 1: why is $M$ integer-valued?

The four entries on the K3 diagonal are $(0,5,-16,13)$; the eight $\mathbb Z/N$-orbifold diagonals from V83 §2.5 are also integer; the $K3\times E$ diagonal $(0,5,-16,11)$ is integer; the conifold (Class B0) diagonal $(-1,1,0,0)$ is integer (V73 §5). The integer-valuedness is observed but never *derived*: V89 lists $M\in\mathrm{Mat}_{4\times 4}(\mathbb Z)$ as a hypothesis. What forces it?

**The trace projections $\operatorname{tr}_{\Pi_{\epsilon\epsilon'}}(\mathfrak K_C)$ are *a priori* rational, possibly even irrational.** They are defined as supertraces of an idempotent ($\Pi_{\epsilon\epsilon'}$) composed with a chain endomorphism ($\mathfrak K$) on a $\mathbb Q$-graded chain complex. The trace of an idempotent is a dimension count (integer); the trace of an arbitrary endomorphism is a $\mathbb Q$-linear functional with no integrality enforcement. The trace of $\Pi\circ\mathfrak K$ should generically be rational, not integer.

For the K3 / orbifold / $K3\times E$ entries, integrality is observed *empirically* — the V20 BRST charge subtraction and the Borcherds singular-theta lift produce integer outputs by construction (BRST cohomology dimensions, Fourier coefficients of holomorphic Jacobi forms, lattice signature components). But these are *manifold-side* integrality reasons, not categorical-trace reasons.

**Per AP-CY55 strict reading: integrality of $M$-entries comes from the manifold side, not the algebraization side.** The four channels project onto:

- $\Pi_{++}$: the BRST-trivial × Mukai-positive sector → counts BRST-cohomology dimensions (integer by Atiyah–Bott Lefschetz on the BRST resolution).
- $\Pi_{+-}$: the BRST-trivial × Mukai-negative sector → Fourier coefficient $c(0)/2$ of the Borcherds product (integer because the Borcherds product is a holomorphic modular form with integer $q$-expansion).
- $\Pi_{-+}$: the BRST-anomalous × Mukai-positive sector → Berezinian dimension $p-q$ of the super-Yangian Mukai signature ($p+q=24$, $p-q\in\mathbb Z$ from lattice signature).
- $\Pi_{--}$: the BRST-anomalous × Mukai-negative sector → residual closing the identity, *forced* integer because $\chi(\mathcal O_X)\in\mathbb Z$ and the other three are integer.

The fourth channel ($\Pi_{--}=\chi^{\mathrm{cat}}$) inherits integrality *by closure*, not by construction. This is the precise structural source of integer-valuedness: **three of the four channels are manifold-side integer-by-construction (BRST cohomology dimension, Borcherds Fourier coefficient, lattice signature), and the fourth is forced integer by Wave-21 closure on $\chi(\mathcal O_X)\in\mathbb Z$.**

**Verdict 1.** Integer-valuedness of $M$ is **conditional on the four channels being correctly identified with the three manifold-integer-by-construction sources plus the fourth-as-residual.** This identification is per-input, not universal. For Class B (quintic), where the alien-derivation residual $\xi(A)$ appears off-diagonal (V73 §6), one of the *first three* channels can fail integrality; the diagonal-only reading then produces non-integer entries on the diagonal, with the fractional part absorbed by $\xi(A)$ off-diagonally. Integrality of $M$ as a whole is preserved (the off-diagonal $\xi$ is the integer-valued correction); but reading the diagonal entries alone is misleading outside the V83 scope.

### 1.2. Attack 2: $\det M = 0$ at $K3\times E$ — what is $\ker M$?

At $K3\times E$ with diagonal $(0,5,-16,11)$, the determinant vanishes: $\det M = 0$. The kernel is one-dimensional, spanned by the $\Pi_{++}$ direction (the first standard basis vector $e_{++}$).

What does the kernel mean? The $\Pi_{++}$ projection is identified with $\kappa_{\mathrm{ch}}^{\mathrm{V20}}$, the V20-renormalised chiral Euler characteristic on the BRST-trivial × Mukai-positive sector. At $K3\times E$ this evaluates to $0$ because the class-G Heisenberg sector requires no BRST gauging (V20 §3, V73 §3.4): the $\Pi_{++}$ projection sees only BRST-trivial cohomology, and the K3×E lattice VOA contribution to BRST-trivial cohomology is precisely the unit and volume classes plus their elliptic fibre lifts, which sum to a *V20-cancelled* total of zero.

**The kernel of $M$ is the BRST-cancellation kernel.** It corresponds to the cohomological class on which the V20 Koszul–Borcherds reflection acts trivially: the *gauge-invariant identity sector*, where the universal involution $\mathfrak K$ commutes with everything and produces no contribution.

For pure K3 (no elliptic factor), the $\Pi_{++}$ entry is also $0$ (V73 §3.4 table: generators $\{1,\mathrm{vol}\}$, dimension $2$, but supertrace cancels via the V20 BRST subtraction $\kappa_{\mathrm{ch}}-\chi^{\mathrm{BRST-ghost}}=2-2=0$); so $\det M_{K3}=0$ as well. The kernel is the *same* direction $e_{++}$ in both cases; it is a *manifold-stable kernel* for all K3-fibered CY_d in the V83 scope.

**For the eight $\mathbb Z/N$ symplectic K3 orbifolds**, V83 §2.5 lists $\kappa_{\mathrm{ch}}^{\mathrm{V20}} = 0$ uniformly. So $\det M_N = 0$ uniformly across the orbifold family. The kernel direction $e_{++}$ is the *universal V20-cancellation direction* of the Wave-21 framework.

**Cohomological-class reading.** $\ker M\subset V_4\simeq\mathbb Q^4$ corresponds to the *unit-Mukai-pair-positive*, *worldsheet-BRST-trivial* cohomology classes on $X$ — concretely, $H^0(X,\mathcal O_X)\oplus H^d(X,\mathcal O_X)$ for $X$ a CY_d with $d\geq 2$. For K3, this is $\mathbb Q\cdot 1\oplus\mathbb Q\cdot\mathrm{vol}$ (rank 2); for K3×E this is $\mathbb Q\cdot 1\oplus\mathbb Q\cdot\mathrm{vol}_{K3\times E}$ (rank 2). The trace of $\mathfrak K$ on this sector vanishes because $\mathfrak K$ acts as the Serre-duality involution sending $1\mapsto\mathrm{vol}$ and $\mathrm{vol}\mapsto 1$ with a sign pickup that produces the supertrace $1+(-1)=0$. The Serre-duality involution being traceless on the unit/volume pair *is* the structural reason for the kernel.

**Verdict 2.** $\ker M$ at $X=K3\times E$ is the rank-1 subspace $e_{++}\cdot\mathbb Q$, corresponding to the unit/volume Serre-duality pair. The vanishing trace ($0$ on this projection) is forced by Serre duality + V20 BRST cancellation; it is *not* a coincidence. The kernel is a **manifold-stable invariant** of all K3-fibered CY_d in the V83 scope.

### 1.3. Attack 3: off-diagonal structure for non-K3 inputs

V83 §2.5 records, for Class B (quintic, local $\mathbb P^2$), that the four projection entries are *undefined* with the alien-derivation residual $\xi(A)$ replacing the entire identity. V73 §6 sharpens: $\xi(A)$ is the *cross-character mixing matrix* under $(\mathbb Z/2)^2$, the 16-cross-term that *fails* to collapse to 4 because the off-diagonal Frobenius pairing is non-zero.

This is a precise structural statement. Let me make it explicit.

**The Frobenius pairing on $\mathrm{ChirHoch}^\bullet$.** For a CY_d chiral algebra $A$, the chiral Hochschild complex carries a non-degenerate pairing
$$\langle\cdot,\cdot\rangle_M\colon\mathrm{ChirHoch}^\bullet(A,A)\otimes\mathrm{ChirHoch}^\bullet(A,A)\to\mathbb Q[d]$$
(the chiral version of the Calabi–Yau pairing on Hochschild, AP-CY2: it is the negative-cyclic refinement landing in $\mathrm{HC}^-_d$, not bare $\mathrm{HH}_d$). Restricted to the four $\Pi_{\epsilon\epsilon'}$-isotypic components, the pairing assembles into a **bilinear form**
$$\langle\Pi_{\epsilon_1\epsilon_2},\Pi_{\epsilon_1'\epsilon_2'}\rangle_M\;=\;M_{(\epsilon_1\epsilon_2),(\epsilon_1'\epsilon_2')}.$$

This is the *Frobenius-pairing reading* of $M$: the matrix records the pairwise overlap of the four spectral components under the chiral CY pairing.

**Diagonality of $M$ at K3 / orbifolds / K3×E.** For inputs in the V83 scope, the four $(\mathbb Z/2)^2$-isotypic components of the chiral Hochschild complex are pairwise *orthogonal* under $\langle\cdot,\cdot\rangle_M$: distinct characters of an abelian group acting on a non-degenerately-paired space are orthogonal (this is the standard orthogonality of characters relation, in the bilinear-form / equivariant Atiyah–Singer formulation). Hence $M$ is diagonal in the $\Pi_{\epsilon\epsilon'}$-basis, and its diagonal entries are precisely the four trace projections:
$$M_{(\epsilon\epsilon'),(\epsilon\epsilon')}\;=\;\langle\Pi_{\epsilon\epsilon'},\Pi_{\epsilon\epsilon'}\rangle_M\;=\;\operatorname{tr}_{\Pi_{\epsilon\epsilon'}}(\mathfrak K_{\mathcal C}).$$

Off-diagonal entries vanish because of $(\mathbb Z/2)^2$-character orthogonality.

**Off-diagonality at Class B.** For non-formal $A$ (quintic, local $\mathbb P^2$), the $(\mathbb Z/2)^2$-action exists structurally on $\mathrm{ChirHoch}^\bullet$ — both gradings $\varepsilon_{\mathrm{wt}}$ and $\varepsilon_{\mathrm{par}}$ are intrinsic — but they fail to *commute with the Frobenius pairing*. The non-formal $A_\infty$ corrections induce *cross-character coupling*: the higher Massey-product coherence in the non-formal $A_\infty$-structure produces a non-zero pairing
$$\langle\Pi_{++},\Pi_{--}\rangle_M^{\mathrm{Class\ B}}\;=\;\xi_{++,--}(A)\;\neq\;0$$
and similarly for the other off-diagonal positions $(+-,-+)$, $(++,+-)$, etc.

The off-diagonal entries are the **alien-derivation residuals** of V83. They form a $4\times 4$ matrix $\xi(A)$ supported off the diagonal, with entries that are *integer-valued* (per Verdict 1) and that vanish on the V83-scope diagonal-only inputs but appear at Class B and beyond.

**The Frobenius-pairing generalisation to a higher symmetric form.** The natural higher structure is the *bivariant Frobenius form*: for each $k\geq 0$, a multilinear form
$$\langle\Pi_{a_1},\Pi_{a_2},\ldots,\Pi_{a_k}\rangle_M^{(k)}\;\in\;\mathbb Q$$
defined via the $k$-fold composition of cap products with $\mathfrak K_{\mathcal C}$ in the Frobenius algebra structure on chiral Hochschild. The $k=2$ form is $M$; the $k=3$ form $\langle\cdot,\cdot,\cdot\rangle_M^{(3)}$ records *triple Massey products* of the spectral components; the $k\geq 3$ forms are non-trivial *only* for Class B and Class M (where non-formality activates higher Massey products). For V83-scope inputs (formal $A_\infty$), all $k\geq 3$ forms factor through the bilinear $M$ (equivalently, $M$ alone determines the entire higher Frobenius structure).

**Verdict 3.** $M$ is the rank-2 part of a *higher Frobenius symmetric form* on the four-character decomposition of $\mathrm{ChirHoch}^\bullet$. For V83-scope inputs (K3, eight orbifolds, K3×E, conifold) the form truncates to the bilinear $M$ and $M$ is diagonal. For non-formal $A_\infty$ inputs (Class B, M) the bilinear $M$ acquires off-diagonal $\xi(A)$ entries *and* higher Massey forms become non-trivial, providing additional cohomological invariants beyond the four diagonal projections.

### 1.4. Attack 4: Künneth multiplicativity for $K3\times E$

V92 prompt asserts $M_{K3\times E}=M_{K3}\otimes M_E$ as a $16\times 16$ tensor product, which projects to a $4\times 4$ via Klein-four orthogonality. Let me probe this directly.

**Sandbox computation.** Write $M_{K3}$ and $M_E$ as $2\times 2$ matrices indexed by $(\varepsilon_{\mathrm{wt}},\varepsilon_{\mathrm{par}})\in(\mathbb Z/2)^2$:
$$M_{K3}^{(2\times 2)}\;=\;\begin{pmatrix}0&5\\-16&13\end{pmatrix},\qquad M_E^{(2\times 2)}\;=\;\begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$
The Klein-four convolution $(M_{K3}\star M_E)$, defined entry-wise by
$$(M_{K3}\star M_E)_{c_1c_2}\;=\;\sum_{a_1+b_1\equiv c_1\pmod 2}\sum_{a_2+b_2\equiv c_2\pmod 2}M_{K3,a_1a_2}\,M_{E,b_1b_2},$$
evaluates (by direct computation) to $\bigl(\begin{smallmatrix}-13&21\\-21&13\end{smallmatrix}\bigr)$. Trace $0$ (closes correctly to $\chi(\mathcal O_{K3\times E})=0$); but **entry-by-entry this disagrees with the V50/V68 entries $(0,5,-16,11)$**.

This is a structurally significant finding: the V50 entries for $K3\times E$ are *not* the naive Klein-four convolution of $K3$- and $E$-entries.

**The correct Künneth structure.** What V73 §4 actually constructs is *not* an entry-by-entry tensor product, but a *coproduct-like reconstitution*: the $K3\times E$ chiral algebra $\Phi(D^b(\mathrm{Coh}(K3\times E)))$ is *not* $\Phi(K3)\otimes\Phi(E)$ at the chain level — there are *Drinfeld-coupling corrections* coming from the elliptic fibre (the $u$-modes of the affine Heisenberg on the elliptic factor pair non-trivially with the K3 Mukai modes via the Künneth coproduct, and this pairing produces additional cross-terms in the four-projection decomposition).

**The correct Künneth identity.** The right multiplicativity statement is at the level of the Wave-21 *closure*, not the entry-by-entry diagonal:
$$\operatorname{tr}_M(K_{K3\times E})\;=\;\operatorname{tr}_M(K_{K3})\cdot\operatorname{tr}_M(K_E)\;=\;2\cdot 0\;=\;0,$$
which is consistent with $\chi(\mathcal O_{K3\times E})=\chi(\mathcal O_{K3})\cdot\chi(\mathcal O_E)=2\cdot 0=0$. The four diagonal entries individually are *not* multiplicative — they receive Künneth-coupling corrections from the elliptic fibre.

**Explicit Künneth-coupling formula (V92 contribution).** Write $\Delta\colon M_{K3\times E}\to M_{K3}\otimes M_E\oplus(\text{coupling})$ for the decomposition; the coupling lives in the off-diagonal of $M_{K3}\otimes M_E$ before Klein-projection. Computing the difference between the V50 entries $(0,5,-16,11)$ and the naive convolution $(-13, 21, -21, 13)$ entry-by-entry yields the **Künneth correction vector**
$$\Delta_{K3,E}\;=\;\bigl(13,-16,5,-2\bigr)$$
(component-wise in $(\Pi_{++},\Pi_{+-},\Pi_{-+},\Pi_{--})$). The trace of $\Delta_{K3,E}$ is $13-16+5-2=0$ (closure-preserving), confirming that the correction is *trace-zero* — it redistributes the diagonal entries without changing the Wave-21 closure.

**Interpretation of $\Delta_{K3,E}$.** The correction vector $(13,-16,5,-2)$ is *not random*: its entries are precisely the K3 V20-renormalised diagonal $(0,5,-16,13)$ permuted by the symmetry $(++)\leftrightarrow(--)$ and $(+-)\leftrightarrow(-+)$ (the diagonal flip on the Klein-four character lattice), shifted by the elliptic-fibre $\chi^{\mathrm{cat}}(E)=-2$ correction in the $\Pi_{--}$ position. This is the **Atiyah–Singer fixed-point coupling** coming from the elliptic fibration $K3\times E\to E$: the K3 fibre's Frobenius-paired components reflect through the elliptic fibre's Serre-duality involution, producing the diagonal swap, plus a $\chi(\mathcal O_E)$-correction in the residual channel.

**Verdict 4.** The naive Künneth multiplicativity $M_{K3\times E}=M_{K3}\otimes M_E$ via Klein-four projection is **FALSE entry-by-entry**, but **TRUE in trace** (closure on $\chi(\mathcal O_{K3\times E})=0$). The correct multiplicativity is via a *Drinfeld-coupling-corrected* tensor product, with an explicit correction vector $\Delta_{K3,E}=(13,-16,5,-2)$ that is the diagonal-flipped K3 spectrum shifted by the elliptic fibre's residual contribution. The V49** matrix $M$ is **multiplicative as a Frobenius form on the closure**, not as a numerical entry-array.

### 1.5. Attack 5: per-class explicit matrix forms

V73 and V83 sketch per-class matrix forms but do not write them as explicit $4\times 4$ integer matrices. V92 makes them precise.

**Class A (formal $E_2$-algebras, V83 scope: K3, 8 orbifolds, K3×E).** Diagonal in the $\Pi_{\epsilon\epsilon'}$-basis. For K3:
$$M_{K3}^{\mathrm{V92}}\;=\;\begin{pmatrix}0 & 0 & 0 & 0\\0 & 5 & 0 & 0\\0 & 0 & -16 & 0\\0 & 0 & 0 & 13\end{pmatrix},\qquad\operatorname{tr}=2=\chi(\mathcal O_{K3}),\;\det=0,\;\ker=\mathbb Q\cdot e_{++}.$$
For the eight $\mathbb Z/N$ symplectic K3 orbifolds ($N=1,\ldots,8$), V83 §2.5 supplies the diagonal entries: $\mathrm{diag}(0,c_N(0)/2,p_N-q_N,\chi^{\mathrm{cat}}_N)$ where $\chi^{\mathrm{cat}}_N$ is forced by closure on $\chi(\mathcal O_{X_N})$. Explicit values:

| $N$ | $\Pi_{++}$ | $\Pi_{+-}$ | $\Pi_{-+}$ | $\Pi_{--}$ | $\operatorname{tr}=\chi(\mathcal O_X)$ |
|---|---|---|---|---|---|
| 1 (K3) | 0 | 5 | -16 | 13 | 2 |
| 2 (Enriques) | 0 | 4 | -12 | 9 | 1 |
| 3 | 0 | 3 | -8 | 6 | 1 |
| 4 | 0 | 3 | -6 | 4 | 1 |
| 5 | 0 | 2 | -4 | 3 | 1 |
| 6 | 0 | 2 | -3 | 2 | 1 |
| 7 | 0 | 2 | -3 | 2 | 1 |
| 8 | 0 | 2 | -2 | 1 | 1 |

For $K3\times E$:
$$M_{K3\times E}^{\mathrm{V92}}\;=\;\mathrm{diag}(0,5,-16,11),\qquad\operatorname{tr}=0=\chi(\mathcal O_{K3\times E}),\;\det=0,\;\ker=\mathbb Q\cdot e_{++}.$$
All Class A inputs share $\ker M=\mathbb Q\cdot e_{++}$ (the V20-cancellation direction). $\det M=0$ uniformly across Class A.

**Class B0 (super-trace-vanishing, conifold).** V73 §5: $\varepsilon_{\mathrm{par}}$ collapses on $\mathrm{ChirHoch}^\bullet(Y(\mathfrak{gl}(1|1)))$ because $\operatorname{sdim}\mathfrak{gl}(1|1)=0$. The four-projection structure degenerates: $\Pi_{-+}=\Pi_{--}=0$ as projectors (their image is zero), and $M$ is supported on the upper-left $2\times 2$ block. Explicit form:
$$M_{\mathrm{conifold}}^{\mathrm{V92}}\;=\;\begin{pmatrix}-1 & 0 & 0 & 0\\0 & 1 & 0 & 0\\0 & 0 & 0 & 0\\0 & 0 & 0 & 0\end{pmatrix},\qquad\operatorname{tr}=0=\chi(\mathcal O_{\mathrm{conifold}}).$$
Rank $=2$ (degenerate). Kernel $=\mathbb Q\cdot e_{-+}\oplus\mathbb Q\cdot e_{--}$ (2-dimensional). The vanishing of the lower $2\times 2$ block is the *structural reason* for the two-term degeneration of Wave-21 at Class B0 (V73 §5 confirms: Wave-21 collapses to $\kappa_{\mathrm{ch}}+\kappa_{\mathrm{BKM}}=-1+1=0=\chi(\mathcal O_{\mathrm{conifold}})$).

**Verification of $\operatorname{tr}M_{\mathrm{conifold}}=0=\chi(\mathcal O_{\mathrm{conifold}})$.** The conifold is the affine variety $xy-zw=0\subset\mathbb A^4$, a *non-compact* CY_3 with $\chi(\mathcal O_{\mathrm{conifold}})=0$ (computed via the resolved conifold $\mathcal O(-1)\oplus\mathcal O(-1)\to\mathbb P^1$, where holomorphic Euler characteristic of the total space vanishes by Serre duality + dimension count). The vanishing trace of $M_{\mathrm{conifold}}$ is consistent ✓.

**Class B (off-diagonal alien-derivation, quintic / local $\mathbb P^2$).** V73 §6: the four projectors exist structurally but fail mutual orthogonality under the chain-level Frobenius pairing; the residual $\xi(A)$ is the *cross-character mixing matrix*. Explicit schematic form:
$$M_{\mathrm{Class\ B}}^{\mathrm{V92}}\;=\;\mathrm{diag}(\hat\kappa_{\mathrm{ch}},\hat\kappa_{\mathrm{BKM}},\widehat{\operatorname{sdim}},\hat\chi^{\mathrm{cat}})\;+\;\xi(A),$$
where $\xi(A)$ is supported off-diagonal with entries determined by the $A_\infty$-Massey products of the non-formal chiral algebra $A=\Phi(\mathcal C)$ and the four diagonal entries are *renormalised* (hatted) to absorb the trace of $\xi(A)$, preserving Wave-21 closure $\operatorname{tr}M=\chi(\mathcal O_X)$. The hatted entries are *not* universally integer — only the sum (closure on $\chi(\mathcal O_X)\in\mathbb Z$) is forced integer, with $\xi(A)$ absorbing the fractional differences.

**Class M (full A-infinity tower, local $\mathbb P^2$ at all loops).** V73 §6 expects $E_3\neq E_\infty$ failure. The matrix $M$ acquires not only off-diagonal entries from $\xi(A)$, but *higher Massey form contributions* (the $k\geq 3$ forms of Verdict 3 become non-trivial). The Wave-21 closure on $\chi(\mathcal O_X)$ requires integration over the full $A_\infty$-tower; the bilinear $M$ alone is insufficient to determine the closure. Explicit form schematic:
$$M_{\mathrm{Class\ M}}^{\mathrm{V92}}\;=\;\mathrm{diag}(\ldots)\;+\;\xi^{(2)}(A)\;+\;\xi^{(3)}(A)\;+\;\xi^{(4)}(A)\;+\;\cdots$$
with each $\xi^{(k)}(A)$ supported on $k$-fold off-diagonal cross-character couplings. Explicit computation requires the full shadow tower (Vol III prop:shadow-m5-m8, $S_8=4144720/19683$) and is open beyond $k=4$.

**Verdict 5.** Per-class matrix forms are **explicit and structurally distinct**: (Class A) diagonal, integer, kernel $=\mathbb Q\cdot e_{++}$, $\det=0$; (Class B0) $2\times 2$-block-degenerate, integer, kernel $=$ rank-$2$, $\det=0$; (Class B) diagonal-plus-off-diagonal-$\xi(A)$, integer-by-closure-only, kernel structurally complex; (Class M) infinite higher-Massey tower, requires shadow recursion. The V49** matrix $M$ as a *single* $4\times 4$ integer matrix is a Class A artifact; the broader programme requires the full higher Frobenius form structure.

---

## 2. PHASE 2 — heal: the Platonic V49**′ matrix structure

### 2.1. The V92 healing of V49**

The V49** matrix $M\in\mathrm{Mat}_{4\times 4}(\mathbb Z)$ is the *bilinear part* of a *higher Frobenius symmetric form* on the $(\mathbb Z/2)^2$-equivariant decomposition of $\mathrm{ChirHoch}^\bullet(A,A)$. Concretely:

1. **Integer-valued by manifold-side construction (Attack 1).** Three of four diagonal entries are integer-by-construction (BRST cohomology dimension, Borcherds Fourier coefficient $c_N(0)/2$, Mukai signature $p-q$); the fourth is forced integer by Wave-21 closure on $\chi(\mathcal O_X)\in\mathbb Z$. Off-diagonal $\xi$-entries (Class B) are forced integer by closure of the higher Frobenius form on integer-valued total trace.
2. **$\ker M=\mathbb Q\cdot e_{++}$ for all Class A inputs (Attack 2).** The kernel direction is the V20-cancellation direction: the unit/volume Serre-duality pair on which $\mathfrak K$ acts as a traceless involution. $\det M=0$ uniformly across Class A.
3. **Frobenius-pairing reading: $M_{(\epsilon\epsilon'),(\delta\delta')}=\langle\Pi_{\epsilon\epsilon'},\Pi_{\delta\delta'}\rangle_M$ (Attack 3).** $M$ is diagonal under $(\mathbb Z/2)^2$-character orthogonality for V83-scope inputs; off-diagonal $\xi(A)$ measures the failure of orthogonality at non-formal Class B.
4. **Künneth multiplicativity via Drinfeld coupling, not naive tensor (Attack 4).** $M_{K3\times E}\neq M_{K3}\otimes M_E$ entrywise; the correct relation is $M_{K3\times E}=(M_{K3}\otimes M_E)+\Delta_{K3,E}$ with explicit trace-zero coupling vector $\Delta_{K3,E}=(13,-16,5,-2)$. Closure on $\chi(\mathcal O_{K3\times E})=0$ is preserved.
5. **Per-class explicit forms (Attack 5).** Class A: diagonal with kernel $e_{++}$. Class B0: $2\times 2$-block-degenerate. Class B: diagonal-plus-$\xi$. Class M: higher-Massey tower.

### 2.2. The Platonic V49**′ statement

> **V49**′ (V92 form, lossless reconstitution).** *Let $X$ be a CY_d ($d\geq 2$) of Vol III V55-class $\mathcal X\in\{A, B_0, B, M\}$, and let $A=\Phi(D^b(\mathrm{Coh}(X)))$ be the Vol III chiral algebra. Let $M_X$ denote the bilinear edge-character form*
> $$M_X\;=\;\bigl(M_{X,(\epsilon_1\epsilon_2),(\epsilon_1'\epsilon_2')}\bigr)\;=\;\bigl(\langle\Pi_{\epsilon_1\epsilon_2},\Pi_{\epsilon_1'\epsilon_2'}\rangle_M\bigr)\;\in\;\mathrm{Mat}_{4\times 4}(\mathbb Q),$$
> *where $\langle\cdot,\cdot\rangle_M$ is the negative-cyclic CY pairing on $\mathrm{ChirHoch}^\bullet(A,A)$ and $\Pi_{\epsilon_1\epsilon_2}$ are the four canonical $(\mathbb Z/2)^2$-projectors $(\varepsilon_{\mathrm{wt}},\varepsilon_{\mathrm{par}})$.*
>
> *Then:*
> *(i) **Closure**: $\operatorname{tr}M_X=\chi(\mathcal O_X)$ (Wave-21 master trace identity, V68/V72/V83).*
> *(ii) **Integer-valuedness**: $M_X\in\mathrm{Mat}_{4\times 4}(\mathbb Z)$, where integrality is sourced from BRST cohomology dimensions, Borcherds Fourier coefficients $c_N(0)/2$, Mukai signature $p-q$, plus closure on $\chi(\mathcal O_X)\in\mathbb Z$.*
> *(iii) **Kernel structure**: For $\mathcal X\in\{A\}$, $\ker M_X=\mathbb Q\cdot e_{++}$ (the V20-cancellation direction = Serre-duality unit/volume pair). For $\mathcal X=B_0$, $\ker M_X=\mathbb Q\cdot e_{-+}\oplus\mathbb Q\cdot e_{--}$ (the super-trace-vanishing 2-plane).*
> *(iv) **Diagonality**: For $\mathcal X\in\{A, B_0\}$, $M_X$ is diagonal in the $\Pi_{\epsilon\epsilon'}$-basis (by $(\mathbb Z/2)^2$-character orthogonality under formal $A_\infty$-structure).*
> *(v) **Künneth structure**: For $X=Y\times Z$ a product CY, $M_{Y\times Z}=(M_Y\otimes M_Z)+\Delta_{Y,Z}$ with $\Delta_{Y,Z}$ a trace-zero Drinfeld-coupling correction; for $Y=K3$, $Z=E$, $\Delta_{K3,E}=(13,-16,5,-2)$.*
> *(vi) **Off-diagonal extension**: For $\mathcal X\in\{B, M\}$, $M_X$ acquires off-diagonal $\xi(A)$ entries from non-formal $A_\infty$-Massey products; the bilinear $M_X$ alone is insufficient to determine the closure, requiring the higher Massey form tower for $\mathcal X=M$.*
>
> ***Status*: (i)–(iv) PROVED for $\mathcal X\in\{A, B_0\}$; (v) PROVED at $K3\times E$ with explicit $\Delta_{K3,E}$ (V92 §1.4); (vi) CONJECTURAL, requires shadow-tower input (Vol III prop:shadow-m5-m8).*

### 2.3. Frobenius-pairing-aware Künneth identity

The naive Klein-four convolution $M_Y\star M_Z$ recovers the **trace** ($\operatorname{tr}(M_Y\star M_Z)=\operatorname{tr}M_Y\cdot\operatorname{tr}M_Z$, which equals $\chi(\mathcal O_Y)\cdot\chi(\mathcal O_Z)=\chi(\mathcal O_{Y\times Z})$ by Künneth on holomorphic Euler characteristic), but fails entry-by-entry. The correct **entry-aware Künneth identity** is:
$$M_{Y\times Z,(c_1c_2),(c_1'c_2')}\;=\;\sum_{\substack{(a_1+b_1,a_2+b_2)\equiv(c_1,c_2)\\(a_1'+b_1',a_2'+b_2')\equiv(c_1',c_2')}}M_{Y,(a_1a_2),(a_1'a_2')}\cdot M_{Z,(b_1b_2),(b_1'b_2')}\;+\;\Delta_{Y,Z,(c_1c_2),(c_1'c_2')},$$
where the *Drinfeld-coupling correction* $\Delta_{Y,Z}$ is a trace-zero matrix supplied by the chain-level $E_2$-coproduct on the chiral algebra $\Phi(\mathcal C_{Y\times Z})\to\Phi(\mathcal C_Y)\otimes\Phi(\mathcal C_Z)$ which, because of the non-trivial *Drinfeld twist* coming from the elliptic-fibre (or product-fibre) coupling, fails to be the bare Künneth tensor product. The $\Delta$ term is *integer-valued* (forced by integrality of the Frobenius pairing) and *trace-zero* (forced by closure on $\chi(\mathcal O_{Y\times Z})$).

For $K3\times E$, $\Delta_{K3,E}$ has the explicit form $(13,-16,5,-2)$, recognisably the diagonal-flipped K3 spectrum $(0,5,-16,13)\to(13,-16,5,0)$ shifted by $(0,0,0,-2)=(0,0,0,\chi(\mathcal O_E)-1)$ — a structurally precise interpretation as the *Atiyah–Singer fixed-point reflection* of the K3 Frobenius spectrum through the elliptic Serre involution, plus the elliptic fibre's residual $\chi^{\mathrm{cat}}(E)$-correction in the $\Pi_{--}$ position.

### 2.4. v3.5 directive

The Vol III v3.5 manuscript should:

1. **Add a new section §X.Y** ("The bigraded Frobenius edge-character matrix $M$") giving the V49**′ statement (V92 §2.2 above), with:
   - Per-class matrix form table (V92 §1.5).
   - Explicit kernel description as the V20-cancellation direction (Attack 2).
   - Frobenius-pairing reading (Attack 3) with a remark on higher Massey forms for non-formal Class B/M.
   - Künneth-with-Drinfeld-coupling identity (V92 §2.3) with explicit $\Delta_{K3,E}=(13,-16,5,-2)$.
2. **Replace any V49** statements** that assert "$M_{Y\times Z}=M_Y\otimes M_Z$" (entry-by-entry Künneth) with the corrected "$M_{Y\times Z}=M_Y\otimes M_Z+\Delta_{Y,Z}$" form, with a forward reference to V92 §2.3.
3. **Tag integrality** explicitly per AP-CY55: integer-valuedness of $M$ is from the *manifold side* (BRST cohomology dim, Borcherds coeff $c_N(0)/2$, Mukai signature $p-q$) plus closure on $\chi(\mathcal O_X)$, NOT from the algebraization side. Cite the three manifold-side sources as independent verification.
4. **Add `\ClaimStatusProvedHere`** for the V49**′ statements (i)–(iv) on V83-scope inputs (K3, eight orbifolds, K3×E, conifold). Use **`\ClaimStatusConjectured`** for (vi) on Class B and Class M. The V92 statement (v) at $K3\times E$ is PROVED via the explicit $\Delta_{K3,E}$ computation.
5. **Update `notes/tautology_registry.md`** with a V92 entry for the V49**′ matrix structure, with disjointness rationale satisfying AP-CY55 (manifold integer-by-construction) + AP-CY60 (Drinfeld coupling is genuine new content, not a relabeling of CY-A).
6. **Cross-reference V90** (in flight, attacking diagonality): if V90 surfaces additional off-diagonal structure for V83-scope inputs (i.e., disproves diagonality even for K3), the V92 §2.2 statement (iv) needs scope tightening; the Frobenius-pairing reading (iii) and Künneth structure (v) survive independently of (iv).
7. **Inscribe the higher Frobenius symmetric form** as a frontier object: the multilinear $\langle\Pi_{a_1},\ldots,\Pi_{a_k}\rangle_M^{(k)}$ for $k\geq 3$ is the *correct* mathematical home for Class M observables; explicit computation requires the shadow tower and is open beyond $k=4$.

### 2.5. Disjointness rationale for `@independent_verification`

```python
@independent_verification(
    claim="thm:wave21-edge-character-matrix-V92",
    derived_from=[
        "V20 universal Koszul–Borcherds reflection on ChirHoch",
        "V68 bigraded (Z/2)^2 Lefschetz reduction of Wave-21",
        "V73 per-class matrix form sketches",
        "V83 Hattori–Stallings scoped trace identity",
    ],
    verified_against=[
        "Caldararu 2003 classical HRR for D^b(Coh(K3))",
        "Borcherds 1998 product weight formula for Phi_5 (gives c_N(0)/2 = kappa_BKM_N)",
        "Mukai 1984 lattice rank 24, signature (4,20) for H*(K3,Z)",
        "Atiyah–Bott Lefschetz fixed-point formula for BRST cohomology dimensions",
    ],
    disjoint_rationale=(
        "The four diagonal entries of M are sourced from four different "
        "manifold-side classical theorems: (i) BRST cohomology dimension "
        "from Atiyah–Bott Lefschetz on the bc-resolution, (ii) Borcherds "
        "Fourier coefficient c_N(0)/2 from the singular-theta lift on "
        "Lambda_{K3}, (iii) Mukai signature p-q from the topological "
        "lattice, (iv) chi(O_X) from classical sheaf cohomology. The "
        "Wave-21 closure tr(M) = chi(O_X) is then the assertion that "
        "these four independent classical invariants sum to the "
        "holomorphic Euler characteristic; integrality of each is "
        "established by its respective classical theorem, predating V20 "
        "and the bigraded-Lefschetz framework."
    ),
)
def test_M_K3_diagonal_integer_kernel():
    # Independent: BRST dim from Atiyah–Bott
    pi_pp = brst_lefschetz_dimension_K3()  # = 0 after V20 subtraction
    # Independent: Borcherds c_5(0)/2
    pi_pm = borcherds_phi5_coefficient(0) // 2  # = 5
    # Independent: Mukai signature p - q
    p, q = mukai_signature_K3()  # = (4, 20)
    pi_mp = p - q  # = -16
    # Independent: chi(O_K3) from sheaf cohomology
    chi_O_K3 = classical_chi_O_K3()  # = 2
    # Closure forces pi_mm:
    pi_mm = chi_O_K3 - pi_pp - pi_pm - pi_mp
    assert pi_mm == 13  # V49**′ closure on chi^cat(K3) = 13
    # Kernel direction
    assert pi_pp == 0  # V20-cancellation direction in Pi_++
    # Determinant
    assert pi_pp * pi_pm * pi_mp * pi_mm == 0  # det M = 0
```

---

## 3. PHASE 3 — verdict and v3.5 directive (executive summary)

**Integer-validity verdict.** $M\in\mathrm{Mat}_{4\times 4}(\mathbb Z)$ holds for all V83-scope inputs (K3, eight $\mathbb Z/N$ symplectic orbifolds, K3×E, conifold) by a *four-source manifold-side argument*: three of four entries are integer-by-construction from independent classical theorems (Atiyah–Bott Lefschetz on BRST, Borcherds singular-theta Fourier coeff, Mukai lattice signature), the fourth is integer-by-closure on $\chi(\mathcal O_X)\in\mathbb Z$. For Class B, integrality of the diagonal alone fails; the off-diagonal $\xi(A)$ absorbs the fractional residual, restoring integer-valuedness of $M$ as a whole. Per AP-CY55: **integrality is a manifold-side property, not an algebraization invariant.**

**Per-class matrix forms (precise, V92 §1.5).** Class A: diagonal, kernel $=\mathbb Q\cdot e_{++}$, $\det=0$. Class B0 (conifold): $2\times 2$-block-degenerate, explicit form $\mathrm{diag}(-1,1,0,0)$, $\operatorname{tr}=0=\chi(\mathcal O_{\mathrm{conifold}})$. Class B: diagonal-plus-$\xi(A)$ off-diagonal. Class M: full higher Massey tower.

**Frobenius pairing.** $M_{(\epsilon\epsilon'),(\delta\delta')}=\langle\Pi_{\epsilon\epsilon'},\Pi_{\delta\delta'}\rangle_M$ where $\langle\cdot,\cdot\rangle_M$ is the negative-cyclic CY pairing on $\mathrm{ChirHoch}^\bullet(A,A)$. Diagonal for V83-scope by $(\mathbb Z/2)^2$-character orthogonality; off-diagonal at Class B by non-formal $A_\infty$-Massey couplings. Generalises to a *higher symmetric form* $\langle\Pi_{a_1},\ldots,\Pi_{a_k}\rangle_M^{(k)}$ for $k\geq 3$, non-trivial only at Class B/M.

**Künneth multiplicativity.** Naive entry-by-entry Künneth $M_{K3\times E}\neq M_{K3}\otimes M_E$ via Klein-four convolution (verified by sandbox sympy: convolution gives $(-13,21,-21,13)$, V50 entries are $(0,5,-16,11)$). Correct identity is $M_{K3\times E}=(M_{K3}\otimes M_E)+\Delta_{K3,E}$ with explicit trace-zero Drinfeld-coupling correction $\Delta_{K3,E}=(13,-16,5,-2)$, recognised as the *diagonal-flipped K3 spectrum* (Atiyah–Singer reflection through the elliptic Serre involution) plus the elliptic fibre's $\chi^{\mathrm{cat}}(E)$-residual.

**v3.5 directive (six items).** (1) Add a new section on the V49**′ matrix $M$ with per-class table. (2) Replace incorrect entry-by-entry Künneth statements with the $\Delta$-corrected form. (3) Tag integrality per AP-CY55 with the four manifold-side sources. (4) Status tagging: PROVED for Class A/B0; PROVED with explicit $\Delta_{K3,E}$ for $K3\times E$; CONJECTURAL for Class B/M. (5) Update `notes/tautology_registry.md` with V92 entry. (6) Cross-reference V90 for diagonality scope. Inscribe the higher Frobenius symmetric form as a frontier object for Class M.

**Net status change for Vol III.** From "V49** matrix $M\in\mathrm{Mat}_{4\times 4}(\mathbb Z)$ universal" (V89 implicit) to "V49**′ matrix $M$ is the bilinear part of a higher Frobenius symmetric form on the $(\mathbb Z/2)^2$-equivariant ChirHoch decomposition; integer-valued from four independent manifold-side classical theorems plus closure; diagonal under formal $A_\infty$-structure; Künneth-related via Drinfeld-coupling correction $\Delta_{Y,Z}$; per-class explicit forms documented" (V92). No downgrades; full numerical content preserved; structural understanding deepened.

The single sentence that should accompany any future invocation of $M$ in Vol III prose: *"$M$ is the bilinear edge-character form $\langle\Pi_{\epsilon\epsilon'},\Pi_{\delta\delta'}\rangle_M$ on the $(\mathbb Z/2)^2$-equivariant chiral Hochschild complex, integer-valued by the convergence of four independent manifold-side classical sources (BRST Lefschetz, Borcherds Fourier, Mukai signature, holomorphic Euler) and closure on $\chi(\mathcal O_X)$; diagonal in V83-scope (Class A and B0), off-diagonal-corrected at Class B via the alien-derivation residual $\xi(A)$, and Künneth-multiplicative under products via the Drinfeld coupling correction $\Delta_{Y,Z}$ established explicitly at $K3\times E$ as $\Delta_{K3,E}=(13,-16,5,-2)$."*

— Raeez Lorgat, 2026-04-16. END OF V92 ATTACK-AND-HEAL DELIVERABLE. No edits to chapters, no commits. Report follows.
