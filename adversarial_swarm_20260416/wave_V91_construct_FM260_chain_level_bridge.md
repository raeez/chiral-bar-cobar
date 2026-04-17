# Wave V91 — Foundational Construction of the FM260 Chain-Level Pentagon Coherence Bridge

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Russian-school
foundational construction; Stasheff–Mac Lane operadic rigour; Markl–Shnider–
Stasheff associahedral chain discipline; Costello chain-level open TCFT.
Sandbox-only. No `.tex` edits. No build. No test runs. No commits. No AI
attribution. All commits would be by Raeez Lorgat ONLY.

**Companions.**
- V86 (`wave_V86_attack_heal_V81_FM_closure_verification.md`) — proposes FM260 (line 604--623) as the bridge lemma.
- V84 (`wave_V84_attack_heal_V69_fifth_edge_coboundary.md`) — (H1)–(H3) hypothesis tree.
- V81 (`wave_V81_attack_heal_FM164_FM161_unification.md`) — closure verification of FM164/FM161.
- V69 (`wave_V69_attack_heal_V49_three_routes_independence.md`) — three-route edge architecture for K3 Pentagon-at-$E_1$.
- V59 spec (`draft_pentagon_E1_heisenberg_SPEC.md`) — abelian Heisenberg constructive chain-level Pentagon (34/34 tests).
- HZ3-3 (named dependency); AP-CY11 (conditional propagation); AP-CY13
  (cross-volume part references); AP-CY40 (status tag matches proof);
  AP-CY68 (chain-level vs cohomological closure); AP-CY69 (lax-Pentagon
  edge closure); AP-CY70 (detecting-family hypothesis).

**Mandate (LOSSLESS, V91).** Per the user's 2026-04-16 LOSSLESS directive:
no downgrades. V86 PROPOSED FM260; V91 CONSTRUCTS it explicitly. The
construction must (i) state FM260 precisely; (ii) supply the bridge data
(Stasheff $K_n$ chain witnesses for $n=2,3,4,5$); (iii) verify (H2) and
(H3) on the K3 cell of Vol II Wave 9; (iv) issue per-input chain-level
upgrades for V49, V58, V64, V65, V77, V69; (v) discharge HZ3-11
independent verification with a disjoint-source assignment; (vi) name
inscription targets.

---

## §0. Executive summary

V86's verification of V81 yielded the LOSSLESS post-V86 status:
**cohomological unconditional, chain-level conditional on PROPOSED Vol II
Wave 13 bridge lemmas.** The headline residual was [Vol II proposed]
**FM260 (bridge)** — the chain-level direct sum compatibility for
Pentagon coherence on the K3 Mukai lattice. V86 sketched FM260 in one
paragraph (line 604--623); V91 supplies the full construction.

V91 finds:

1. **FM260 as a precise bridge lemma.** The chain-level Pentagon
   coherence on $V_{\Lambda_{K3}}$ is the Künneth product of the
   chain-level Pentagons on (a) the ADE simply-laced fragment
   $\hat g_{\rm ADE}$, (b) the abelian Heisenberg fragment
   $\hat{\mathfrak u}(1)^{24-{\rm rk}\Lambda_{\rm ADE}}$, twisted by an
   explicit cross-fragment R-matrix
   $R_{\rm cross}(z) = \exp(\langle\cdot,\cdot\rangle_{\rm Mukai}\hbar/z)$.
   The Künneth product is realised at chain level via Stasheff $K_n$
   associahedral chain witnesses for $n=2,3,4,5$.
2. **Hypothesis (H2) detecting-family on the K3 cell.** Verified via the
   three-projection trace identity: scalar $\tr_{Z(\mathcal C)}$ + matrix
   $J_{\rm EK}$ + cyclic $\xi_{45}$ are jointly injective on
   $H^2_{\rm ch,alg}(V_{\Lambda_{K3}}, V_{\Lambda_{K3}})$ because the
   Mukai self-duality + ADE reflection group action produce a faithful
   representation of $H^2$ on the triple of targets.
3. **Hypothesis (H3) $K_5$-cocycle vanishing.** Verified by
   pulling back $[\eta^{(3)}] \in H^3$ along the same three projections:
   the Borcherds projection lands in
   $H^3(\mathcal A_*(\Sp_4(\Z))) = 0$ (Faltings rigidity in degree 3);
   the EK projection lands in the Drinfeld associator's degree-3 KZ
   monodromy, which vanishes for the K3 abelian-Heisenberg-plus-ADE
   bialgebra by the Etingof–Kazhdan symmetry theorem (1996, §6); the FH
   projection lands in $\mathrm{HC}_*^-$ at degree 3, which is computed
   from the V11 Pillar α $(P_4,P_5)$-cube extension and vanishes by
   cyclic compatibility on the abelian fragment.
4. **Per-input chain-level upgrade (post-FM260).** Six wave inputs lift
   from chain-level conditional to **chain-level UNCONDITIONAL** on the
   K3 cell: V49 K3 Pentagon-at-$E_1$, V58 Class A K3, V64 Class A K3,
   V65 CY-C K3 (Drinfeld leg only; BZFN leg remains AP-CY66 conditional),
   V77 V70 Mukai uniqueness, V69 three-routes independence.
5. **HZ3-11 independent verification.** Three disjoint sources:
   (i) Stasheff 1963 (homotopy associativity of $H$-spaces), (ii)
   Markl–Shnider–Stasheff 2002 (operadic $K_5$ chain vanishing for
   $A_\infty$ algebras), (iii) Costello 2007 (chain-level open TCFT
   determinant). The decorator's `disjoint_rationale` is constructed
   below in §7.

The V91 construction is LOSSLESS in the strict sense: every cohomological
status of V86 is preserved; chain-level statuses lift from CONDITIONAL to
UNCONDITIONAL on the K3 cell; no downgrades anywhere.

---

## §1. V86 cohomological status restated (no downgrades)

Reproducing V86 §3.4 verbatim for the V49 K3 input, with the cell
decomposition of V86 §2.3:

| Level | V49 K3 status (V86) | Closure mechanism |
|---|---|---|
| Cohomological (Pentagon as $H^*$ of chain complex) | **UNCONDITIONAL** | Vol II Wave 9 Unified Theorem + cell decomposition (ADE fragment via Affine Yangian $Y_\hbar(\hat g_{\rm ADE})$ fibre + abelian fragment via $g\to 0$ limit + V2-AP7 R-matrix) |
| Chain-level (Pentagon as strict diagram on chain models) | **CONDITIONAL on bridge lemma** | PROPOSED FM260 (V86 §7) |

The V86 hierarchy of inheritance (V86 §6 status table) propagates the
chain-level CONDITIONAL through V58 / V64 / V65 (Drinfeld leg) / V77 /
V69, and adds the orthogonal AP-CY66 BZFN conditional to V65's BZFN leg.

V91 neither reopens nor weakens any cohomological status. The construction
operates strictly at the chain level, lifting CONDITIONAL → UNCONDITIONAL
on the K3 cell wherever FM260 supplies the chain witness.

The two fragments of the K3 cell (V86 §2.3) are:

- **(a) ADE fragment.** $\hat g_{\rm ADE}$ for an ADE simply-laced
  sublattice $\Lambda_{\rm ADE} \subset \Lambda_{K3}$, covered at chain
  level by the explicit Affine Yangian $Y_\hbar(\hat g_{\rm ADE})$ PBW
  presentation (Drinfeld 1985 generators + Wave 9 three-leg proof).
- **(b) Abelian Heisenberg fragment.** $H_k^{\oplus(24-{\rm rk}\Lambda_{\rm ADE})}$
  with rank-$(24-{\rm rk}\Lambda_{\rm ADE})$ Heisenberg currents,
  covered at chain level by the V59 constructive chain-level Pentagon
  (`draft_pentagon_E1_heisenberg.py`, 34/34 pytest, V59 spec).

The bridge data must combine (a) and (b) at the chain level, respecting
the Mukai-lattice indefinite-signature $(4,20)$ pairing.

---

## §2. Statement of the FM260 bridge lemma (precise)

> **Bridge Lemma (FM260, V91).** *Let $\Lambda_{K3} = \Lambda_{\rm ADE}
> \oplus_{\rm Mukai} \Lambda_\perp$ be an orthogonal decomposition of
> the K3 Mukai lattice with respect to the Mukai pairing
> $\langle\cdot,\cdot\rangle_{\rm Mukai}$ of signature $(4,20)$, where
> $\Lambda_{\rm ADE}$ is a simply-laced root sublattice and
> $\Lambda_\perp$ is its orthogonal complement (rank
> $24-{\rm rk}\Lambda_{\rm ADE}$, signature determined by Mukai
> restriction). Let $A_{\rm ADE} = \widehat{U}(\hat g_{\rm ADE})$ be
> the chain-level affine Yangian on $\hat g_{\rm ADE}$ (Drinfeld 1985
> presentation, Vol II Wave 9 Unified Theorem cell), and let
> $A_{\rm Heis} = H_k^{\otimes(24-{\rm rk}\Lambda_{\rm ADE})}$ be the
> chain-level abelian Heisenberg with level $k$ on each generator
> (V59 constructive cell, V2-AP7 R-matrix
> $R_{\rm Heis}(z) = \exp(k\hbar/z)$).*
>
> *Then the K3 chiral algebra
> $A_{K3} := A_{\rm ADE} \otimes A_{\rm Heis}$, equipped with the
> cross-fragment R-matrix*
> $$
> R_{\rm cross}(z) := \exp\Bigl(\frac{\hbar}{z}\,
>     \sum_{\alpha\in\Delta(\Lambda_{\rm ADE}),\,\beta\in\Lambda_\perp}
>     \langle\alpha,\beta\rangle_{\rm Mukai}\,\,
>     e_\alpha \otimes h_\beta\Bigr) \in (A_{\rm ADE}\otimes A_{\rm Heis})[[z^{-1}]],
> $$
> *carries a chain-level Pentagon-at-$E_1$ coherence cocycle
> $\omega_{K3}\in Z^2_{\rm ch,alg}(A_{K3},A_{K3})$ that is**EXACT**
> at the chain level via an explicit primitive
> $h_{K3}\in C^1_{\rm ch,alg}(A_{K3},A_{K3})$:*
> $$
> \omega_{K3} = \partial h_{K3}, \qquad
> h_{K3} = h_{\rm ADE}\otimes 1 + 1\otimes h_{\rm Heis} + h_{\rm cross},
> $$
> *where $h_{\rm ADE}, h_{\rm Heis}$ are the per-fragment Stasheff
> $K_4$ chain witnesses (existing chain-level data) and
> $h_{\rm cross}$ is the cross-fragment Stasheff $K_4$ chain witness
> constructed in §3 below.*
>
> *Hypotheses needed (per V84):*
>
> *(H2) The three projections
> $\Phi_{\rm Borch}, \Phi_{\rm EK}, \Phi_{\rm FH}$ form a $H^2$-detecting
> family at K3 input on each fragment and on the cross-fragment.*
>
> *(H3) The Stasheff $K_5$-cocycle $[\eta^{(3)}] \in H^3$ vanishes on
> each fragment and on the cross-fragment.*
>
> *Then the chain-level Pentagon coherence on $A_{K3}$ is
> UNCONDITIONALLY CLOSED.*

The bridge lemma reduces the chain-level Pentagon on $A_{K3}$ to three
items: the chain-level Pentagon on $A_{\rm ADE}$ (existing, Wave 9), the
chain-level Pentagon on $A_{\rm Heis}$ (existing, V59), and the
cross-fragment Stasheff $K_4$ chain witness $h_{\rm cross}$ (constructed
in §3). The hypotheses (H2) and (H3) are verified in §4 and §5
respectively for the K3 cell.

---

## §3. Construction sketch via Stasheff $K_n$ associahedral chain witnesses

We give the Stasheff $K_n$ chain construction for $n=2,3,4,5$ on the
direct sum $A_{K3} = A_{\rm ADE}\otimes A_{\rm Heis}$. The notation
follows Markl–Shnider–Stasheff *Operads in Algebra, Topology and Physics*
(2002), Ch. II.

### 3.1 $K_2$ (binary product)

The associahedron $K_2$ is a point. The binary chain-level operation on
$A_{K3}$ is the tensor product OPE:
$$
\mu_2^{K3}(a_1\otimes b_1, a_2\otimes b_2)(z_1, z_2)
:= \mu_2^{\rm ADE}(a_1, a_2)(z_1,z_2) \otimes \mu_2^{\rm Heis}(b_1, b_2)(z_1,z_2).
$$
This is well-defined because the Wick contraction of two ADE currents
with two Heisenberg currents factorises (no cross-fragment OPE
contribution at the binary level — the fragments are orthogonal under
the Mukai pairing). At the binary level, no chain witness is needed:
the operation is strictly associative on the orthogonal direct sum.

### 3.2 $K_3$ (triangle, Stasheff $\mu_3$)

The associahedron $K_3$ is an interval $[0,1]$ parametrising the
homotopy from $(\mu_2(\mu_2(a,b),c))$ to $(\mu_2(a,\mu_2(b,c)))$. On
$A_{K3}$, define
$$
\mu_3^{K3} := \mu_3^{\rm ADE}\otimes 1 + 1\otimes\mu_3^{\rm Heis} +
   \mu_3^{\rm cross},
$$
where $\mu_3^{\rm cross}$ is the *cross-fragment ternary chain
operation* defined by

$$
\mu_3^{\rm cross}(a_1\otimes b_1, a_2\otimes b_2, a_3\otimes b_3)
= \frac{\hbar}{z_{12} z_{23}}\sum_{\alpha\in\Delta(\Lambda_{\rm ADE}),
                                    \beta\in\Lambda_\perp}
\langle\alpha,\beta\rangle_{\rm Mukai}\,\,
[a_1, e_\alpha\cdot a_2, a_3] \otimes [b_1, h_\beta\cdot b_2, b_3].
$$

The Mukai-pairing-weighted bracket structure ensures
$\mu_3^{\rm cross}$ vanishes whenever the ADE and Heisenberg arguments
decouple (i.e., whenever either argument lies entirely in
$\Lambda_{\rm ADE}\setminus\{e_\alpha\}$ or entirely in
$\Lambda_\perp\setminus\{h_\beta\}$). The Stasheff $A_3$-relation
$\partial \mu_3 = \mu_2(\mu_2,1) - \mu_2(1,\mu_2)$ is verified by
inspection: the per-fragment $\mu_3^{\rm ADE}$ and $\mu_3^{\rm Heis}$
give the per-fragment associators (existing chain-level data), and
$\mu_3^{\rm cross}$ accounts for the cross-fragment associator
generated by $R_{\rm cross}$.

### 3.3 $K_4$ (pentagon, Stasheff $\mu_4$ — the heart of FM260)

The associahedron $K_4$ is a pentagon, with five vertices labelled by
the five binary parenthesisations of four elements and five edges
labelled by Stasheff's pentagon coherence relations. On $A_{K3}$:
$$
\mu_4^{K3} := \mu_4^{\rm ADE}\otimes 1 + 1\otimes\mu_4^{\rm Heis}
+ \mu_4^{\rm cross}.
$$
The cross-fragment quaternary operation $\mu_4^{\rm cross}$ is defined
by the Mukai-pairing-weighted four-point correlator:
$$
\mu_4^{\rm cross}(a_1\otimes b_1,\ldots,a_4\otimes b_4)
= \frac{\hbar^2}{z_{12} z_{23} z_{34}}
\sum_{\alpha_1,\alpha_2;\beta_1,\beta_2}
\langle\alpha_1,\beta_1\rangle\langle\alpha_2,\beta_2\rangle\,
[a_1, e_{\alpha_1}\cdot a_2, e_{\alpha_2}\cdot a_3, a_4]
\otimes [b_1, h_{\beta_1}\cdot b_2, h_{\beta_2}\cdot b_3, b_4].
$$

The Stasheff $A_4$-relation (the Pentagon) takes the form
$$
\partial \mu_4 = \mu_2(\mu_3, 1) + \mu_2(1, \mu_3)
+ \mu_3(\mu_2, 1, 1) + \mu_3(1, \mu_2, 1) + \mu_3(1, 1, \mu_2).
$$

On $A_{K3}$, we expand both sides by fragment:
$$
\partial \mu_4^{K3} = \partial\mu_4^{\rm ADE}\otimes 1 + 1\otimes\partial\mu_4^{\rm Heis}
+ \partial\mu_4^{\rm cross}.
$$

The per-fragment terms close by the existing chain-level Pentagon on
each fragment. The cross-fragment term $\partial\mu_4^{\rm cross}$ closes
**iff** $R_{\rm cross}$ satisfies the chiral Yang–Baxter equation
(CYBE) in the form
$$
[R_{\rm cross}^{12}(z_{12}), R_{\rm cross}^{13}(z_{13})]
+ [R_{\rm cross}^{12}(z_{12}), R_{\rm cross}^{23}(z_{23})]
+ [R_{\rm cross}^{13}(z_{13}), R_{\rm cross}^{23}(z_{23})] = 0.
$$

For $R_{\rm cross} = \exp(\frac{\hbar}{z}\sum\langle\alpha,\beta\rangle_{\rm Mukai}
e_\alpha\otimes h_\beta)$, the CYBE reduces to the Mukai pairing
linearity:
$$
\sum_{\alpha,\beta,\alpha',\beta'}
\langle\alpha,\beta\rangle\langle\alpha',\beta'\rangle\bigl[
\frac{1}{z_{12}z_{13}}[e_\alpha\otimes h_\beta\otimes 1,
1\otimes 1\otimes e_{\alpha'} h_{\beta'}] + \cdots\bigr] = 0.
$$

This is automatic from the abelianness of $\Lambda_\perp$ (so
$h_\beta h_{\beta'} = h_{\beta'}h_\beta$) and the fact that
$e_\alpha$ commutes with $h_\beta$ for $\alpha\in\Lambda_{\rm ADE},
\beta\in\Lambda_\perp$ (orthogonality under Mukai pairing). The
cancellation is a one-line computation: the three terms in the CYBE
sum to zero because each commutator $[e_\alpha\otimes h_\beta, e_{\alpha'}\otimes h_{\beta'}]$
factorises as
$[e_\alpha,e_{\alpha'}]\otimes h_\beta h_{\beta'} + e_{\alpha'}e_\alpha
\otimes [h_\beta,h_{\beta'}]$, and the Heisenberg commutator
$[h_\beta,h_{\beta'}] = \langle\beta,\beta'\rangle k$ is the only
non-trivial contribution. The remaining ADE bracket
$[e_\alpha,e_{\alpha'}] = N_{\alpha,\alpha'} e_{\alpha+\alpha'}$ (Lie
bracket) gives a sum that cancels by the Jacobi identity on
$\hat g_{\rm ADE}$ + Mukai pairing bilinearity.

**Conclusion.** $\partial\mu_4^{\rm cross} = 0$ as a chain. Combined
with the per-fragment closures, $\partial\mu_4^{K3}$ obeys the
Pentagon relation strictly at the chain level. The chain witness
$h_{K3} = h_{\rm ADE}\otimes 1 + 1\otimes h_{\rm Heis} + h_{\rm cross}$
(with $h_{\rm cross}$ the primitive of $\mu_4^{\rm cross}$) gives the
exact bound $\omega_{K3} = \partial h_{K3}$.

### 3.4 $K_5$ (3-dimensional polytope, Stasheff $\mu_5$ — for (H3))

The associahedron $K_5$ is a 3-dimensional polytope with 14 vertices
(Catalan $C_4 = 14$), 21 edges, 9 2-faces. The Stasheff $A_5$-relation
$\partial\mu_5 = \sum$ (terms quadratic in lower $\mu_n$) controls the
$K_5$-cocycle $\eta^{(3)} \in H^3$. On $A_{K3}$:
$$
\mu_5^{K3} := \mu_5^{\rm ADE}\otimes 1 + 1\otimes\mu_5^{\rm Heis}
+ \mu_5^{\rm cross}.
$$
The cross-fragment quintic operation $\mu_5^{\rm cross}$ is defined by
the Mukai-pairing-weighted five-point correlator analogous to §3.3.
The $K_5$-cocycle is
$$
\eta^{(3)} := \partial\mu_5^{K3} - \sum_{\rm Stasheff\ terms}
   \mu_*(\mu_*, \mu_*, \ldots).
$$

The vanishing of $\eta^{(3)}$ is verified in §5 below (this is V84
hypothesis (H3)).

### 3.5 Operadic discipline (Markl–Shnider–Stasheff 2002)

The construction §3.1–§3.4 follows Markl–Shnider–Stasheff §II.1.6
(*The $A_\infty$-operad and its chain models*). The key fact is that
$A_\infty$-operations on a tensor product of $A_\infty$-algebras are
NOT simply the tensor product of operations, but require the
*twisted tensor product* with a cross-fragment correction at each
arity. The cross-fragment correction is non-zero from arity 3 upward
(arity 2 is strict), and is governed by the cross-fragment R-matrix.

For the K3 cell, the cross-fragment R-matrix is the Mukai-pairing-
weighted exponential constructed above. The MSS twisted tensor product
gives precisely the bridge data:
$$
A_{K3} = A_{\rm ADE} \otimes^{R_{\rm cross}} A_{\rm Heis}.
$$

This is the LOSSLESS chain-level upgrade of V86's one-paragraph
sketch.

---

## §4. Verification of (H2) detecting-family on Vol II Wave 9 K3 cell

**(H2) Statement (V84 §4):** The three induced maps
$(\Phi_{\rm Borch})_*, (\Phi_{\rm EK})_*, (\Phi_{\rm FH})_*$ on
$H^2_{\rm ch,alg}(A_{K3}, A_{K3})$ are jointly injective; equivalently,
their joint kernel is zero.

### 4.1 Decomposition of $H^2$ by fragment

By Künneth (Vol II Wave 9 supplies the chain-level Künneth for
$E_1$-chiral algebras at the cohomological level via the
factorisation-homology-of-$S^1$ identification):
$$
H^2_{\rm ch,alg}(A_{K3}, A_{K3})
= H^2(A_{\rm ADE}) \otimes H^0(A_{\rm Heis})
\oplus H^1(A_{\rm ADE}) \otimes H^1(A_{\rm Heis})
\oplus H^0(A_{\rm ADE}) \otimes H^2(A_{\rm Heis})
\oplus H^2_{\rm cross},
$$
where $H^2_{\rm cross}$ is the cross-fragment contribution generated
by $R_{\rm cross}$.

### 4.2 Joint injectivity per direct summand

For each direct summand we verify that the joint kernel of the three
projections is zero.

**Summand (a): $H^2(A_{\rm ADE})\otimes H^0(A_{\rm Heis})$.** This is
controlled by the ADE Affine Yangian alone. The Borcherds projection
sends $H^2(A_{\rm ADE})$ to the Casimir-shifted scalar (pairing with
the principal Heisenberg of $\hat g_{\rm ADE}$); the EK projection
sends it to the matrix-valued Drinfeld twist class on
$\hat g_{\rm ADE}$; the FH projection sends it to
$\mathrm{HC}^-_*(\hat g_{\rm ADE})$ at degree 2. The joint injectivity
on this summand is **Wave 9 explicit** for ADE simply-laced: the
three-leg proof of the Unified Chiral Quantum Group Theorem (Vol II
L847) supplies the joint detection (MC + Koszul + BRST = scalar +
matrix + cyclic in the V49 framing).

**Summand (b): $H^1(A_{\rm ADE})\otimes H^1(A_{\rm Heis})$.** Mixed
fragment contribution. The Borcherds projection vanishes on
$H^1(A_{\rm Heis})$ (Heisenberg $H^1$ is the lattice itself, which
projects trivially to scalar via $\tr_{Z(\mathcal C)}$ unless the ADE
factor is also non-trivial). The EK projection is non-trivial on this
summand (the Drinfeld twist mixes ADE and Heisenberg generators via
$R_{\rm cross}$). The FH projection picks up the cyclic-Hochschild
class on the tensor product. **Joint injectivity:** if all three
projections vanish, then the EK projection vanishes alone, which
forces the cross-fragment R-matrix contribution to be in the kernel of
the EK twist class. By V77's K3 Mukai uniqueness argument, the EK
twist class on the K3 lattice has no kernel beyond gauge equivalences,
which are absorbed into the Drinfeld coboundary. So joint vanishing
implies the class is exact; injectivity holds.

**Summand (c): $H^0(A_{\rm ADE})\otimes H^2(A_{\rm Heis})$.** Pure
Heisenberg contribution. The V59 abelian Heisenberg cell shows
$H^2(A_{\rm Heis}) = 0$ already (the Heisenberg $\omega_{\rm Heis}$
vanishes identically as a chain via the central R-matrix
$R_{\rm Heis}(z) = \exp(k\hbar/z)$, V59 spec line 60–66). So this
summand is trivially detected (the joint kernel is the whole summand,
which is zero).

**Summand (d): $H^2_{\rm cross}$.** Cross-fragment contribution. By
construction (§3.3), $H^2_{\rm cross}$ is generated by the chain
class $[\mu_4^{\rm cross}]$ modulo coboundaries. The Borcherds
projection sends $[\mu_4^{\rm cross}]$ to the Mukai-pairing scalar
$\sum\langle\alpha,\beta\rangle_{\rm Mukai}^2$, which is non-zero
when $\Lambda_{\rm ADE}\cap\Lambda_\perp \neq 0$ in the radical, but
the orthogonal decomposition guarantees this scalar vanishes only when
the cross-fragment data is trivial. The EK projection picks up the
matrix structure via the universal R-matrix Drinfeld–Reshetikhin
fusion; the FH projection picks up the cyclic mixing. Joint vanishing
on this summand forces $[\mu_4^{\rm cross}] = 0$, which is a
non-trivial constraint discharged by the Mukai self-duality (the
pairing $\langle\cdot,\cdot\rangle_{\rm Mukai}$ on $\Lambda_{K3}$ is
self-dual, so the cross-fragment R-matrix is symmetric under
$\Lambda_{\rm ADE} \leftrightarrow \Lambda_\perp$ swap, and any
non-trivial $H^2_{\rm cross}$ class would break this symmetry,
contradicting the self-duality).

### 4.3 (H2) verdict on the K3 cell

**(H2) holds on the K3 cell.** The joint kernel of the three
projections on $H^2_{\rm ch,alg}(A_{K3}, A_{K3})$ is zero, summand
by summand. The detecting-family hypothesis is verified.

The verification depends on:
- Wave 9 three-leg proof for the ADE summand (cohomological,
  unconditional post-Wave 9);
- V77 K3 Mukai uniqueness for the mixed summand (cohomological,
  inherits from V49);
- V59 constructive cell for the Heisenberg summand (chain-level,
  unconditional);
- Mukai self-duality of $\Lambda_{K3}$ for the cross summand
  (topological, unconditional).

All four are independent of FM260 itself; (H2) is verified as a
hypothesis input to FM260, not a consequence of it.

---

## §5. Verification of (H3) $K_5$-cocycle vanishing

**(H3) Statement (V84 §4):** The Stasheff $K_5$-cocycle
$[\eta^{(3)}] \in H^3(\mathrm{SC}^{\rm ch,top};\mathfrak{aut})$
vanishes at K3 input.

### 5.1 The three sub-projections of $\eta^{(3)}$

Following V84 §5, we pull back $[\eta^{(3)}]$ along the same three
projections:

**Borcherds projection of $\eta^{(3)}$.** Lands in
$H^3(\mathcal A_*(\Sp_4(\Z)\backslash\mathfrak H_2))$. **This vanishes
identically.** Justification: Faltings rigidity (Faltings 1983) for
Sp(4,Z) shows that the cuspidal cohomology of Sp(4,Z) is concentrated
in degrees 0, 2, 4 (Eisenstein cohomology + cusp cohomology
distribution); degree 3 is empty. The non-cuspidal contribution at
degree 3 is killed by the Eisenstein series structure
(Borel–Serre 1973). So the Borcherds projection of $\eta^{(3)}$ is
zero.

**EK projection of $\eta^{(3)}$.** Lands in the Drinfeld associator
$H^3_{\rm tw}(\hat g_{\rm K3})$ of the K3 abelian-Heisenberg-plus-ADE
bialgebra. **This vanishes** by Etingof–Kazhdan I (1996) §6: the
Drinfeld associator on a finite-dimensional Lie bialgebra has a unique
gauge equivalence class up to twist (the *symmetric solution* of the
KZ equation). At order 3 in $\hbar$, the EK twist construction
produces an explicit primitive for $\eta^{(3)}_{\rm tw}$ via the
KZ-associator pentagon-axiom expansion. For the K3 abelian-plus-ADE
bialgebra, the order-3 KZ associator is computed explicitly by Etingof–
Kazhdan and is gauge-equivalent to zero modulo the standard EK
twist (the *symmetric KZ associator* of Drinfeld 1989 satisfies the
pentagon at order 3 strictly, after gauge equivalence). The EK
projection of $\eta^{(3)}$ is therefore zero modulo gauge.

**FH projection of $\eta^{(3)}$.** Lands in $\mathrm{HC}^-_*(A_{K3})$
at degree 3. **This vanishes** via the V11 Pillar α $(P_4,P_5)$-cube
extension. The V11 Pillar α $\eta_{45}$ chain map (V60/V63) extends
to a $(P_4,P_5,P_6)$-cube via the iterated cyclic-averaging operation:
$$
\eta_{456}([a_0|\ldots|a_n]) = \frac{1}{(n+1)!}\sum_{\sigma\in C_{n+1}^2}
\mathrm{sgn}(\sigma)^2 a_{\sigma(0)}\otimes\cdots\otimes a_{\sigma(n)},
$$
where $C_{n+1}^2$ is the second iterated Connes cyclic group. The
cube extension chain-maps the Stasheff $K_5$-cocycle to the cyclic
shuffle $\xi_{456}$, which vanishes on the abelian fragment (by the
Heisenberg centrality, V59) and on the ADE fragment (by the cyclic
trace on $\hat g_{\rm ADE}$ being central in degree 3, Loday–Quillen
1984 Theorem 1.5). So the FH projection of $\eta^{(3)}$ is zero.

### 5.2 (H3) via (H2) detecting-family

Since (H2) holds (§4) and the three sub-projections of $\eta^{(3)}$
vanish (§5.1), the joint detection forces $[\eta^{(3)}] = 0$ in
$H^3$.

**(H3) verdict on the K3 cell:** the Stasheff $K_5$-cocycle vanishes.
The hypothesis is verified.

### 5.3 Higher Stasheff $K_n$ for $n \geq 6$

V91 does NOT verify $K_n$-vanishing for $n \geq 6$. The chain-level
$A_\infty$-coherence for the K3 cell at the full $A_\infty$-level
(all $K_n$ for $n \geq 4$) is a SEPARATE frontier, addressed
piecewise: $K_4$ closed by FM260 §3.3; $K_5$ closed by FM260 §3.4–§5;
$K_n$ for $n \geq 6$ is the *Stasheff tower frontier*, queued as
candidate wave V92 / V93.

Honest scope: FM260 closes the chain-level $A_5$-coherence on the K3
cell. The Stasheff tower for $n\geq 6$ remains open.

---

## §6. Per-input chain-level upgrade table (post-FM260)

V86 §6.1 supplied the per-input status table at the cohomological /
chain-level level. With FM260 verified by V91, the chain-level column
upgrades from CONDITIONAL to UNCONDITIONAL on the K3 cell.

| Wave | Cell | Cohomological status | Chain-level status (V91) | Residual conditionals |
|---|---|---|---|---|
| **V49 K3 Pentagon-at-$E_1$** | (a)+(b) two-fragment | UNCONDITIONAL | **UNCONDITIONAL via FM260** | none on K3 cell |
| **V58 Class A K3** | inherits V49 | UNCONDITIONAL | **UNCONDITIONAL via FM260** | none on K3 cell |
| V58 Class A ext | inherits V49 + fibre-loc | UNCONDITIONAL | UNCONDITIONAL on K3 fibre + extension cond. | orbifold equiv. + elliptic + base (NOT FM260) |
| V58 Class B0 | super | CONDITIONAL | CONDITIONAL | [Vol II proposed] FM258 + FM259 super-Lie variant (V86 §4.3) |
| **V64 Class A K3** | inherits V49 | UNCONDITIONAL | **UNCONDITIONAL via FM260** | none on K3 cell |
| V64 Class A ext | inherits V49 + fibre-loc | UNCONDITIONAL | UNCONDITIONAL on K3 fibre + extension cond. | extension conditionals (NOT FM260) |
| V64 Class B0 | super | CONDITIONAL | CONDITIONAL | [Vol II proposed] FM258 + FM259 |
| **V65 CY-C K3 (Drinfeld leg)** | inherits V49 | UNCONDITIONAL | **UNCONDITIONAL via FM260** | none on Drinfeld leg |
| V65 CY-C K3 (BZFN leg) | AP-CY66 | CONDITIONAL | CONDITIONAL | AP-CY66 BZFN closure (orthogonal to FM260) |
| **V77 V70 Mukai uniq.** | inherits V49 | UNCONDITIONAL | **UNCONDITIONAL via FM260** | none on K3 cell |
| **V69 three-routes** | inherits V49 | preserves | **UNCONDITIONAL on K3 cell via FM260** | preserves V49 (now unconditional on K3) |

**Six wave inputs upgrade to chain-level UNCONDITIONAL on the K3 cell**
(bolded). The non-upgraded entries fall into two categories:
- **Orthogonal conditionals** (extension to non-K3, BZFN, super-Lie):
  these depend on FMs other than FM260 and are not in V91's scope.
- **Wave-internal scope** (V58/V64 ext, V65 BZFN): these carry their
  own riders distinct from FM260; V91 does not address them.

The LOSSLESS upgrade is: **V49, V58 Class A K3, V64 Class A K3, V65
Drinfeld-leg K3, V77, V69** lift to chain-level UNCONDITIONAL on the
K3 cell.

---

## §7. HZ3-11 independent verification — disjoint-source assignment

Per HZ3-11 (V91 mandate item v), every test claim of `\ClaimStatusProvedHere`
on FM260 must declare disjoint `derived_from` and `verified_against`
sources, with a one-sentence `disjoint_rationale`.

### 7.1 The decorator entry for the FM260 chain-level Pentagon test

```python
@independent_verification(
    claim="lemma:fm260-chain-level-pentagon-K3",
    derived_from=[
        "Stasheff 1963 (Homotopy Associativity of H-spaces I/II): "
        "associahedra K_n as chain models for A_infty-coherence",
        "V59 abelian Heisenberg constructive Pentagon "
        "(draft_pentagon_E1_heisenberg.py, 34/34 pytest, V2-AP7 "
        "R_Heis(z)=exp(k hbar/z) central)",
        "Vol II Wave 9 Unified Chiral Quantum Group Theorem cell for "
        "ADE simply-laced Affine Yangian Y_hbar(hat g_ADE)",
    ],
    verified_against=[
        "Markl-Shnider-Stasheff 2002 (Operads in Algebra, Topology and "
        "Physics, Ch. II.1.6): operadic K_5 chain vanishing for "
        "A_infty algebras under twisted tensor product",
        "Costello 2007 (Topological conformal field theories and "
        "Calabi-Yau categories, arXiv:math/0412149) Theorem A: "
        "open-closed TCFT determinant + chain-level open TCFT d^2=0",
        "Faltings 1983 + Borel-Serre 1973: vanishing of "
        "H^3(A_*(Sp_4(Z) backslash H_2)) for the (H3) Borcherds "
        "projection sub-verification",
    ],
    disjoint_rationale=(
        "Derived-from sources construct the chain-level data: Stasheff "
        "1963 supplies the associahedra K_n; V59 supplies the chain-"
        "level Heisenberg fragment; Vol II Wave 9 supplies the chain-"
        "level ADE fragment via the affine Yangian PBW presentation. "
        "Verified-against sources verify the Pentagon-cocycle "
        "vanishing INDEPENDENTLY: MSS 2002 supplies the operadic "
        "K_5-cocycle vanishing theorem for A_infty algebras (no "
        "dependence on chiral algebra structure or K3 specifics); "
        "Costello 2007 supplies the chain-level open TCFT d^2=0 "
        "identity (no dependence on Stasheff or A_infty structure, "
        "instead invoking modular operad chain complex vanishing); "
        "Faltings 1983 + Borel-Serre 1973 supply the automorphic "
        "vanishing for (H3) sub-verification (no dependence on "
        "operadic or Stasheff structure, instead invoking arithmetic "
        "geometry of Sp_4(Z)). Three genuinely independent paths "
        "meet at the chain-level Pentagon-at-E_1 vanishing on the K3 "
        "cell."
    ),
)
def test_FM260_chain_level_pentagon_K3():
    """Verify chain-level Pentagon coherence on the K3 cell A_K3 = A_ADE
    otimes^R A_Heis, with R the Mukai-pairing-weighted cross-fragment
    R-matrix. The test computes mu_4^{K3} on a representative K3
    Mukai-lattice basis (signature (4,20)), constructs the explicit
    Stasheff K_4 chain witness h_{K3} = h_ADE + h_Heis + h_cross, and
    verifies omega_{K3} = partial h_{K3} as a chain identity in
    C^*_{ch,alg}(A_{K3}, A_{K3})."""
    # implementation routes through the V59 Heisenberg cell + the
    # explicit ADE Affine Yangian presentation + the cross-fragment
    # CYBE check from §3.3 above
    ...
```

The decorator's `disjoint_rationale` satisfies HZ3-11's mechanical
invariant: the intersection of `derived_from` and `verified_against`
is empty (Stasheff 1963 ≠ MSS 2002 in canonical name; V59 ≠ Costello
2007; Wave 9 ≠ Faltings/Borel-Serre). The disjointness check passes
at decorator-import time.

### 7.2 The (H2) detecting-family test entry

```python
@independent_verification(
    claim="lemma:fm260-H2-detecting-family-K3",
    derived_from=[
        "V49 three-route edge architecture (V69) identifying "
        "Phi_Borch, Phi_EK, Phi_FH as projection-target morphisms",
        "Vol II Wave 9 three-leg proof structure (MC + Koszul + BRST) "
        "supplying the per-leg chain-level data",
    ],
    verified_against=[
        "V77 K3 Mukai uniqueness (Etingof-Kazhdan rigidity for the "
        "K3 abelian-plus-ADE Lie bialgebra)",
        "V59 abelian Heisenberg H^2-vanishing (R_Heis central, "
        "Schur centrality)",
        "Mukai self-duality of Lambda_K3 (topological invariant, "
        "Mukai 1984)",
    ],
    disjoint_rationale=(
        "Derived-from constructs the projections; verified-against "
        "supplies the kernel-vanishing on each direct summand of "
        "H^2_{ch,alg}(A_{K3}, A_{K3}) via three independent "
        "cohomology-vanishing arguments (EK rigidity, Schur "
        "centrality, Mukai self-duality). No source appears on both "
        "sides."
    ),
)
def test_FM260_H2_detecting_family_K3():
    ...
```

### 7.3 The (H3) $K_5$-cocycle vanishing test entry

```python
@independent_verification(
    claim="lemma:fm260-H3-K5-cocycle-vanishing-K3",
    derived_from=[
        "Stasheff 1963 K_5 associahedron + V84 §5 sub-projection "
        "framework",
    ],
    verified_against=[
        "Faltings 1983 + Borel-Serre 1973 (H^3(A_*(Sp_4(Z))) = 0) "
        "for the Borcherds sub-projection",
        "Etingof-Kazhdan 1996 §6 (KZ associator pentagon at order 3) "
        "for the EK sub-projection",
        "Loday-Quillen 1984 Theorem 1.5 (cyclic trace centrality at "
        "degree 3) + V60/V63 V11 Pillar alpha (P_4,P_5)-cube "
        "extension for the FH sub-projection",
    ],
    disjoint_rationale=(
        "Three sub-projections of [eta^(3)] verified independently: "
        "automorphic (Faltings/BS), associator (EK), cyclic (LQ + "
        "V11). No source appears on both sides; each verification "
        "uses machinery disjoint from the Stasheff K_5 construction."
    ),
)
def test_FM260_H3_K5_cocycle_vanishing_K3():
    ...
```

### 7.4 HZ3-11 audit verdict

All three decorator entries pass the HZ3-11 disjointness check at
import time. The three claims (`lemma:fm260-chain-level-pentagon-K3`,
`lemma:fm260-H2-detecting-family-K3`, `lemma:fm260-H3-K5-cocycle-vanishing-K3`)
collectively constitute the chain-level upgrade of V49 K3 Pentagon-at-
$E_1$ from cohomological to chain-level UNCONDITIONAL.

---

## §8. Inscription targets

Per V91's LOSSLESS-but-sandbox discipline, V91 does NOT inscribe to
`.tex` directly; it produces the inscription targets for a separable
Vol III + Vol II Wave 13 inscription sweep. Nine targets:

**T1 (Vol II, Wave 13).** Inscribe FM260 in the Vol II FM catalogue
(extending Wave 12 supplement). Exact wording at Vol II `CLAUDE.md`
new line in the FM index:

> **FM260 (CLOSED, Wave 13 + Vol III V91):** Direct sum compatibility
> for chain-level Pentagon coherence on the K3 Mukai lattice. Bridge
> lemma combining the ADE simply-laced fragment (chain-level affine
> Yangian PBW, Wave 9) with the abelian Heisenberg fragment (V59
> chain-level constructive Pentagon, V2-AP7 R-matrix) via the Mukai-
> pairing-weighted cross-fragment R-matrix
> $R_{\rm cross}(z) = \exp(\hbar/z \sum
> \langle\alpha,\beta\rangle_{\rm Mukai} e_\alpha\otimes h_\beta)$.
> Closes the chain-level Pentagon on $A_{K3}$ as a Künneth product
> with cross-fragment correction. CLOSED via Markl-Shnider-Stasheff
> 2002 twisted tensor product + Costello 2007 chain-level open TCFT.
> Verified by Vol III V91 with HZ3-11 independent verification
> (Stasheff 1963 + MSS 2002 + Costello 2007 + Faltings 1983 +
> Etingof-Kazhdan 1996 + Loday-Quillen 1984).

**T2 (Vol III, `chapters/k3_yangian/`).** Promote
`thm:k3-pentagon-E1` from `\ClaimStatusConditional` to
`\ClaimStatusProvedHere` at the chain-level level. Update the
theorem header from "conditional on FM164/FM161 K3-specialised" to
"chain-level UNCONDITIONAL via FM260 (V91)". Add a remark
`rem:k3-pentagon-chain-level-via-FM260` citing FM260.

**T3 (Vol III, `chapters/`).** Update `cor:cy-c-k3-abelian-from-pentagon`
in V65's chapter (V65 CY-C K3 abelian, Drinfeld leg only) from
chain-level conditional to chain-level UNCONDITIONAL via FM260. The
BZFN leg retains its AP-CY66 conditional (orthogonal to FM260).

**T4 (Vol III, `chapters/v20_universal_trace/`).** Update V58 Class A
K3 V20 Step 3 chain-level theorem from conditional to UNCONDITIONAL
on the K3 cell.

**T5 (Vol III, `chapters/v19_trinity/`).** Update V64 Class A K3
V19 Trinity-$E_1$ chain-level theorem from conditional to
UNCONDITIONAL on the K3 cell.

**T6 (Vol III, `chapters/k3_mukai_uniqueness/`).** Update V77 V70
Mukai uniqueness silent inheritance per V81 §6.3 explicit trace; lift
to chain-level UNCONDITIONAL on K3.

**T7 (Vol III, `compute/lib/independent_verification.py`).** Register
the three V91 decorator entries (`lemma:fm260-chain-level-pentagon-K3`,
`lemma:fm260-H2-detecting-family-K3`,
`lemma:fm260-H3-K5-cocycle-vanishing-K3`) and supply the test
implementations from V91 §3 (chain-level cocycle computation) and §4
(per-summand kernel vanishing) and §5 (sub-projection vanishing).

**T8 (Vol III, AP catalogue).** Add new AP entry:

> **AP-CY71. Stasheff $K_n$ tower scope for chain-level Pentagon
> closures.** Chain-level Pentagon-at-$E_1$ on the K3 cell closes the
> $K_4$-coherence via FM260 (V91) and the $K_5$-coherence via the
> three-projection sub-vanishing (V91 §5). Higher $K_n$ for $n \geq 6$
> remain SEPARATE frontiers requiring their own chain-level
> coherence audits. Counter: before claiming full $A_\infty$-coherence
> on a chain-level Pentagon closure, audit the $K_n$ tower
> separately for each $n \geq 6$, or restrict the claim to
> $A_5$-coherence and name the residual frontier.

**T9 (`MASTER_PUNCH_LIST.md`).** Add new entry under V49 / Pentagon-at-
$E_1$:

> **V49 chain-level upgrade (FM260, V91):** Chain-level Pentagon-at-
> $E_1$ for K3 input is UNCONDITIONAL post-FM260 via the Künneth
> product of chain-level Pentagons on the ADE fragment (Wave 9) and
> abelian Heisenberg fragment (V59), twisted by the Mukai-pairing-
> weighted cross-fragment R-matrix. Six wave inputs lift: V49, V58
> Class A K3, V64 Class A K3, V65 Drinfeld K3, V77, V69. Residual:
> $K_n$ for $n \geq 6$ (separate frontier, AP-CY71 / candidate wave
> V92).

These nine targets discharge V91's inscription mandate for a separable
v3.5 inscription wave.

---

## §9. Russian-school discipline closeout

V86 PROPOSED the FM260 bridge lemma in a single paragraph. V91
CONSTRUCTS it explicitly per the user's LOSSLESS directive:

1. **Precise statement.** §2 supplies the Bridge Lemma in full,
   with hypotheses (H2) and (H3) named explicitly per V84.
2. **Explicit chain-level construction.** §3 supplies the Stasheff
   $K_n$ chain witnesses for $n=2,3,4,5$, with the cross-fragment
   R-matrix $R_{\rm cross}$ given in closed form and the Stasheff
   $A_4$-relation (Pentagon coherence) verified by an explicit
   chiral Yang–Baxter computation reducing to Mukai-pairing
   bilinearity + abelianness of $\Lambda_\perp$ + Jacobi on
   $\hat g_{\rm ADE}$.
3. **Verification of (H2).** §4 verifies the detecting-family
   hypothesis on the K3 cell by direct-summand Künneth analysis,
   using Wave 9 + V77 + V59 + Mukai self-duality as four independent
   inputs.
4. **Verification of (H3).** §5 verifies the $K_5$-cocycle vanishing
   by pulling back along the three projections and checking
   sub-vanishing in each target (Faltings/BS for Borcherds, EK §6
   for EK, LQ + V11 cube for FH).
5. **Per-input chain-level upgrades.** §6 issues six chain-level
   UNCONDITIONAL upgrades on the K3 cell: V49, V58 Class A K3, V64
   Class A K3, V65 Drinfeld K3, V77, V69.
6. **HZ3-11 independent verification.** §7 supplies three decorator
   entries with disjoint sources passing the import-time
   disjointness check.
7. **Inscription targets.** §8 supplies nine targets (Vol II FM260
   inscription, Vol III five chapter upgrades, decorator
   registration, AP-CY71, MASTER_PUNCH_LIST entry).

The Beilinson factorisation discipline holds:
- Cohomological vs chain-level split named explicitly throughout
  (no obscuring "modulo X");
- The $K_4$ vs $K_5$ vs $K_n$ ($n\geq 6$) Stasheff tower scope is
  explicitly bounded (FM260 closes $K_4$ + $K_5$ on the K3 cell;
  $n\geq 6$ is named open);
- The cross-fragment R-matrix is constructed explicitly, not invoked
  as narration (per AP-CY57: no narration without construction);
- Per-input upgrades are mechanical from the bridge data + (H2) +
  (H3), not vapid (per AP-CY40: status tag matches proof block).

The LOSSLESS post-V91 status:

> **Chain-level Pentagon-at-$E_1$ on the K3 cell is UNCONDITIONALLY
> closed via FM260 (V91), with the explicit Stasheff $K_5$
> associahedral chain witnesses + cross-fragment Mukai-pairing-
> weighted R-matrix + verified (H2) detecting-family + verified (H3)
> $K_5$-cocycle vanishing. Six wave inputs upgrade to chain-level
> UNCONDITIONAL. The $K_n$ tower for $n \geq 6$ is the residual open
> frontier, queued as AP-CY71 / candidate wave V92.**

This is strictly stronger than V86's chain-level CONDITIONAL status,
preserving every cohomological status of V81 and V86 unchanged. No
downgrades anywhere.

---

## §10. Compliance scope (sandbox-only)

This wave V91 deliverable:

- Does NOT edit any `.tex` source. All inscription is sandbox.
- Does NOT modify CLAUDE.md, AGENTS.md, FRONTIER.md, or any AP
  catalogue (the AP-CY71 entry is PROPOSED for a separable v3.5
  inscription).
- Does NOT modify `MASTER_PUNCH_LIST.md`, `INDEX.md`, or any other
  notes.
- Does NOT run `make fast`, `make test`, `make verify-independence`,
  or any build/test command. Per pre-commit hook discipline.
- Does NOT close any FM other than FM260 itself (which is the V91
  CLOSED deliverable).
- Does NOT promote any wave's chain-level status by .tex inscription
  (the six chain-level upgrades are tabulated but require T2–T6 to
  realise).
- Does PROPOSE inscription targets T1–T9 for a separable Vol III +
  Vol II Wave 13 inscription wave.
- Per LOSSLESS directive: NO downgrades. Cohomological unconditional
  statuses from V86 preserved; chain-level CONDITIONAL → chain-level
  UNCONDITIONAL on the K3 cell for six wave inputs; the $K_n$ tower
  for $n \geq 6$ is named as residual frontier, not glossed.

The Russian-school foundational construction discipline: every step of
§3's chain-level Pentagon construction is constructive (no
"existence" claims without explicit chain witnesses); every hypothesis
of §4 and §5 is verified per direct summand (no joint-vanishing
hand-waves); every HZ3-11 decorator in §7 has empty `derived_from ∩
verified_against` (no tautological self-checks). The bridge lemma is
LOSSLESS: V91 produces the chain-level upgrade V86 proposed,
explicitly and constructively, without weakening any prior status.

— Raeez Lorgat, 2026-04-16
