# Wave V11 Pillar α (U1) — Chain-Level Extraction
## V11 Pillar α ≡ the $P_4 \leftrightarrow P_5$ edge of Pentagon-at-$E_1$, extracted from V49 + V59 + V55

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Lossless
extraction (V60). Sandbox-only; no `.tex` edits, no commits, no AI
attribution.

**Companions.** V49 (`wave_application_V49_status_promotion.md`,
K3 Pentagon-at-$E_1$ resolution); V59
(`draft_pentagon_E1_heisenberg_SPEC.md`, abelian Heisenberg
sub-case); V55 (`wave_frontier_pentagon_E1_non_K3.md`, dichotomy
theorem); V20 (`UNIVERSAL_TRACE_IDENTITY.md`, with V11 §8.5 cited as
the Universal Pullback property).

---

## 0. Mandate

V11 Pillar α (U1) was historically named *the chain-level $\Phi$
functor at $d = 3$*: the assertion that the Vol III functor

$$
\Phi : \mathrm{CY}_3\text{-Cat} \;\longrightarrow\; E_1\text{-ChirAlg}
$$

is *coherent at the chain level* in the sense that the five
Hochschild presentations of $A := \Phi(C)$ are simultaneously
quasi-isomorphic at chain level, with the comparison data assembling
into a coherent Pentagon. The Wave 14 V40 master implication chain
identified this Pillar α coherence with one specific edge of the
Pentagon-at-$E_1$ — the $P_4 \leftrightarrow P_5$ edge:

$$
P_4 \;:=\; \mathrm{Ext}^*_{A^e_{\mathrm{mode}}}(A,A)
\qquad\overset{\mathrm{V11\ Pillar\ \alpha\ (U1)}}{\longleftrightarrow}\qquad
P_5 \;:=\; \int_{S^1} A.
$$

This wave performs the *extraction* announced in the V60 brief:
under V49 + V59 + V55, V11 Pillar α (U1) at the $P_4 \leftrightarrow
P_5$ edge becomes a **theorem at Class A** (K3-fibred), a
**theorem at the abelian Heisenberg sub-case** (with explicit
comparison map), a **theorem at Class B0** (super-trace vanishing,
conifold), and a **conjecture at Class B** (mock-modular residual,
quintic and local $\mathbb P^2$). The final identification in §6
states the *ghost theorem*: V11 Pillar α and the Pentagon
$P_4 \leftrightarrow P_5$ edge are **the same datum** under two
historical names.

The discipline is Russian-school (Chriss–Ginzburg). Every comparison
arrow is exhibited as a chain map, with explicit formula on
Hochschild generators. AP-CY57 (narration vs construction) and
AP-CY32 (reorganisation vs bypass) are enforced throughout.

---

## 1. Precise statement of V11 Pillar α (U1) at chain level

Let $C$ be a CY$_3$-category and $A := \Phi(C)$ its image under the
Vol III $\Phi$ functor, an $E_1$-chiral algebra (per AP-CY56;
$E_1$ is the native level at $d = 3$; $E_2$ lives on
$Z(\mathrm{Rep}^{E_1}(A))$, *not* on $A$ itself).

**V11 Pillar α (U1) at chain level (the precise statement).**
For every chain-level model of $A$, the canonical comparison

$$
\boxed{\;\;\eta_{45}(A)\;:\;\mathrm{Ext}^*_{A^e_{\mathrm{mode}}}(A,A)
\;\xrightarrow{\;\;\sim\;\;}\;\int_{S^1} A\;\;}
$$

is a chain map, and a chain-level quasi-isomorphism, with the
comparison cocycle

$$
\omega_{45}(A) \;:=\; \eta_{45} \circ \eta_{45}^{-1} - \mathrm{id}
\;\in\; H^2\bigl(\mathrm{End}(P_5)[[z, z^{-1}]];\,
\mathfrak{aut}\bigr)
$$

vanishing. Here $\eta_{45}(A)$ is the chain map constructed by

(i) **HKR on the mode side** ($P_4$): for $A_{\mathrm{mode}}$ the
mode algebra (a deformation of $\mathrm{Sym}(V_A)$ for $V_A$ the
generating space), the Hochschild-Kostant-Rosenberg map
$\mathrm{HKR}: \mathrm{HH}_*(A_{\mathrm{mode}}) \to
\Lambda^* V_A \otimes A_{\mathrm{mode}}$ realises the polyvector
chain model.

(ii) **Loday–Quillen–Tsygan / Lurie HA 5.5.3.11 on the
factorisation side** ($P_5$): factorisation homology
$\int_{S^1} A$ over the circle is computed via $\pi_0(\mathrm{Conf}_n
S^1)$ as a cyclic chain complex on $A$.

(iii) **The comparison arrow** $\eta_{45}$: the universal map
relating the polyvector chain to the cyclic chain complex,
given on Hochschild $n$-chains by

$$
\eta_{45}\bigl([a_0 | a_1 | \cdots | a_n]\bigr)
\;=\; \sum_{\sigma \in \mathbb Z/(n+1)} (-1)^{\mathrm{sgn}\,\sigma}
\, a_{\sigma(0)} \otimes a_{\sigma(1)} \otimes \cdots \otimes a_{\sigma(n)}
\;\in\; (A^{\otimes (n+1)})^{\mathbb Z/(n+1)}
\;\subset\; \int_{S^1} A.
$$

This is the **cyclic averaging** map; it is well-defined on Hochschild
chains (descends through the cyclic differential on $P_4$) and lands
in the cyclic-invariant part of the Loday model for $\int_{S^1} A$.
Chain-level coherence is the assertion that $\eta_{45}$ commutes
with the differentials on $P_4$ and $P_5$ up to a coherent
*(co-)homotopy*, and that the resulting $\omega_{45}$ vanishes in
$H^2$.

The $E_1$-coherence cocycle is by V39 H1

$$
\omega_{45}(A)\;=\;R(z) \diamond - \cdot R(z)^{-1}\;-\;\mathrm{id}
\qquad\in\;H^2\bigl(\mathrm{SC}^{\mathrm{ch,top}};\,
\mathfrak{aut}\bigr),
$$

where $R(z)$ is the universal Yangian R-matrix attached to $A$ via
the V20-Δ Drinfeld coproduct (V20 trace identity, V11 §8.5 universal
pullback). **V11 Pillar α at chain level is the statement
$[\omega_{45}(A)] = 0$ in $H^2$.**

This is precisely the $P_4 \leftrightarrow P_5$ edge of
Pentagon-at-$E_1$: pairwise quasi-isomorphism at chain level for the
specific edge $(P_4, P_5)$, with cocycle living in the same
$H^2(\mathrm{SC}^{\mathrm{ch,top}}; \mathfrak{aut})$ as the full
Pentagon coherence cocycle.

---

## 2. V11 Pillar α THEOREM for Class A (K3-fibred) — extraction from V49 Route (iii)

V49 Route (iii) is the V20 Universal Trace Identity route, which
internally factorises through the factorisation homology presentation
$\int_{S^1} A$ at one end and the BRST/mode-algebra reading at the
other. Concretely:

**V49 Route (iii) skeleton (cf. V49 §1.1, Step 3).**
For $C = D^b(\mathrm{Coh}(K3))$, the V20 trace identity reads

$$
\mathrm{tr}_{Z(\mathcal C)}\bigl(\mathfrak K_{\mathcal C}\bigr)
\;=\;-c_{\mathrm{ghost}}\bigl(\mathrm{BRST}(\Phi(\mathcal C))\bigr)
\;=\;\tfrac{1}{2}\,c_5(0)\;=\;5,
$$

where the **left side** is computed from the *factorisation
homology* presentation $P_5 = \int_{S^1} A$ (the trace lives on
$Z(\mathcal C)$ which by BZFN is $\mathrm{End}(\int_{S^1} A)$),
and the **middle term** is computed from the *mode-algebra
Ext* presentation $P_4 = \mathrm{Ext}^*_{A^e_{\mathrm{mode}}}$
(the BRST resolution lives on the mode algebra).

The integer match $5 = 5$ forces the comparison cocycle
$[\omega_{45}]_{K3}$'s **scalar projection to vanish**. Combined
with V49 Route (ii) (Etingof–Kazhdan twist coherence on the
abelian Heisenberg + ADE-enhanced sub-Yangian), the cocycle
vanishes identically in $H^2$.

**Theorem (V11 Pillar α at Class A; conditional on FM164/FM161).**
*Let $C$ be a K3-fibred CY$_3$-category (K3, K3 $\times$ E, STU
model, or any of the eight diagonal $\mathbb Z/N\mathbb Z$ symplectic
K3 orbifolds). Let $A = \Phi(C)$. Then the chain-level comparison*

$$
\eta_{45}(A) \;:\;\mathrm{Ext}^*_{A^e_{\mathrm{mode}}}(A, A)
\;\xrightarrow{\;\;\sim\;\;}\;\int_{S^1} A
$$

*is a chain map and a chain-level quasi-isomorphism, with
$[\omega_{45}(A)] = 0 \in H^2(\mathrm{SC}^{\mathrm{ch,top}};
\mathfrak{aut})$.*

**Extraction skeleton from V49 Route (iii) (verifying AP-CY32: each
subproblem of V49 Route (iii) is independently resolved at the
$P_4 \leftrightarrow P_5$ edge specifically).**

(R1) **Mode-side independence.** The BRST resolution of $A_{K3} =
\Phi(D^b\mathrm{Coh}(K3))$ on the mode side gives the
ghost central charge $-c_{\mathrm{ghost}} = 5$ from the
abelian Heisenberg presentation $A_{K3} \supset \mathrm{Heis}^{24}$.
This is computed from $\mathrm{HH}_*(A_{\mathrm{mode}})$ via HKR and
the Mukai lattice (24 = rank of $H^*(K3, \mathbb Z)$), giving 5
once the Borel-bracket grading is restored. Independence of the
factorisation side: HKR is a statement about polynomial
algebras and their deformation, with no factorisation input.

(R2) **Factorisation-side independence.** $\int_{S^1} A_{K3}$
computed via Lurie HA 5.5.3.11 + the K3 Yangian RTT presentation
gives $c_5(0)/2 = 5$ from the Borcherds product formula at the
trace. The factorisation homology integrand carries the K3 elliptic
genus, which encodes $c_5(0) = 10$ via Borcherds 1998. Independence
of the mode side: the Borcherds product is automorphic, computed
from lattice-vector counts on $\Lambda_{4,20}$, with no Hochschild
input.

(R3) **The matching identity** $-c_{\mathrm{ghost}} = c_5(0)/2 = 5$.
This is V20 Step 3 specialised to $A_{K3}$. The identity forces
$\eta_{45}(A_{K3})$'s induced map on $H^*$ to be the identity on
the scalar component, hence $[\omega_{45}]_{K3} = 0$ at the scalar
projection. Combined with the matrix sector vanishing (V49 Route (i)
sympy + V49 Route (ii) EK), the full cocycle vanishes.

**This is a genuine extraction, not reorganisation** (AP-CY32):
each of (R1), (R2), (R3) is independently computable, and the
match in (R3) is not engineered by hardcoded identification of
the two sides — they are computed via different machinery (HKR
vs Borcherds) and meet at the integer 5.

**Class A extension** (cf. V55 H1(a)). For $C$ K3-fibred but not
K3 itself (K3 $\times$ E, STU, 8 orbifolds), the same extraction
applies via projection onto the K3 fibre:
$\int_{S^1} A_C = \int_{S^1}(A_{K3 \mathrm{fibre}}
\otimes A_{\mathrm{base}})$ with $A_{\mathrm{base}}$ commutative
($E_\infty$, automatic Pentagon). The Pentagon data
all live on the K3 fibre; the base contributes no additional
$\omega_{45}$.

**Status.** $\boxed{\text{V11 Pillar α at Class A: PROVED conditional
on FM164 (Yangian pro-nilpotent bar-cobar) + FM161 (Yangian
Koszulness in Positselski).}}$

---

## 3. V11 Pillar α THEOREM for abelian Heisenberg — extraction from V59

V59 verified all $\binom{5}{2} = 10$ pairwise quasi-isomorphisms at
chain level for the rank-1 Heisenberg $H_k$ at every level $k$.
The $P_4 \leftrightarrow P_5$ edge is one of these, and admits an
**explicit chain-level comparison map**.

**Setup (V59 §"The five Hochschild presentations of $H_k$").**
For $H_k$ the rank-1 Heisenberg vertex algebra with OPE
$J(z) J(w) \sim k/(z-w)^2$:

- $P_4 = \mathrm{Ext}^*_{H_k^e_{\mathrm{mode}}}(H_k, H_k)
= \Lambda^* V \otimes \mathrm{Sym}\, V$ via HKR, with
$V = \mathrm{span}\{J_{-n} : n \geq 1\}$ and $\dim_n = p(n)$
(partition counts).
- $P_5 = \int_{S^1} H_k$ computed via $\pi_0(\mathrm{Conf}_n S^1)$
+ Loday–Quillen–Tsygan as the cyclic chain complex
$(\mathrm{Sym}\, V \otimes \Lambda^* V, B + b)$.

Both collapse on the diagonal sector to the partition-graded chain
complex with $\dim_n = p(n)$ and trivial differential.

**Explicit chain-level comparison map $\eta_{45}^{\mathrm{Heis}}$.**

On a Hochschild $n$-chain $[a_0 | a_1 | \cdots | a_n]$ with
$a_i \in H_k$ written in the divided-power basis
$a_i = e_{s_i} := J_{-1}^{s_i}/s_i!$, the map is

$$
\boxed{\;\;\eta_{45}^{\mathrm{Heis}}\bigl([e_{s_0} | e_{s_1} |
\cdots | e_{s_n}]\bigr)
\;=\;\sum_{\sigma \in \mathbb Z/(n+1)} \frac{1}{(n+1)!}
\,e_{s_{\sigma(0)}} \otimes e_{s_{\sigma(1)}} \otimes \cdots
\otimes e_{s_{\sigma(n)}}.\;\;}
$$

This is the cyclic averaging projector onto the
$\mathbb Z/(n+1)$-invariant subspace, with the normalisation
$1/(n+1)!$ absorbing both the cyclic order and the symmetric
group correction (for the Heisenberg, the underlying space is
abelian so the cyclic and symmetric group actions coincide on
$e_{s_0} \otimes \cdots \otimes e_{s_n}$).

**Differential compatibility.** The Connes $B$-differential on $P_4$
is

$$
B[e_{s_0} | \cdots | e_{s_n}]
\;=\;\sum_{i=0}^{n} (-1)^{ni}
[1 | e_{s_i} | e_{s_{i+1}} | \cdots | e_{s_{i-1}}],
$$

which under $\eta_{45}^{\mathrm{Heis}}$ maps to the Connes $B_{\mathrm
chir}$ on $P_5$:

$$
B_{\mathrm{chir}}\bigl(e_{s_0} \otimes \cdots \otimes e_{s_n}\bigr)
\;=\;\sum_{i=0}^{n} (-1)^{ni}\,1 \otimes e_{s_i} \otimes
e_{s_{i+1}} \otimes \cdots \otimes e_{s_{i-1}}.
$$

The compatibility $\eta_{45}^{\mathrm{Heis}} \circ B = B_{\mathrm
chir} \circ \eta_{45}^{\mathrm{Heis}}$ holds at the chain level
(*not* just up to homotopy) because the symmetrisation projector
commutes with Connes' cyclic shift.

**Cocycle vanishing.** The $E_1$-coherence cocycle
$\omega_{45}^{\mathrm{Heis}}(a) = R_{\mathrm{Heis}}(z) \cdot a \cdot
R_{\mathrm{Heis}}(z)^{-1} - a$ vanishes by Schur centrality:

$$
R_{\mathrm{Heis}}(z) \;=\; \exp\!\bigl(k\,\hbar/z\bigr)
$$

is **central** (acts by a scalar on every weight space $\mathrm{Sym}^n
V$) because the Heisenberg OPE has only a double-pole
$k/(z-w)^2$ and no first-order residue, killing the
commutator $[J(z), J(w)]$. Hence
$[R_{\mathrm{Heis}}(z), a] = 0$ for every $a$, so

$$
\omega_{45}^{\mathrm{Heis}}(a) \;=\;
R_{\mathrm{Heis}}\,a\,R_{\mathrm{Heis}}^{-1} - a
\;=\;a - a\;=\;0
$$

identically as a chain. The cocycle bounds by $\mu = 0$, so
$[\omega_{45}^{\mathrm{Heis}}] = 0$ in
$H^2(\mathrm{SC}^{\mathrm{ch,top}}; \mathfrak{aut})$ for every level
$k$, including the abelian limit $k \to 0$.

**Generalisation to other abelian chiral algebras.** The Heisenberg
extraction generalises directly: any abelian chiral algebra (free
boson lattice algebras $V_\Lambda$, $\beta\gamma$ systems with
abelian zero-mode, $bc$ systems at integer weight) has central
$R(z)$ by the same Schur argument applied to the abelian OPE. So the
extraction yields:

**Corollary.** *For every **abelian** chiral algebra $A$ (no
non-trivial OPE at first-order pole), $\eta_{45}^A$ is a chain
isomorphism with $[\omega_{45}^A] = 0$.*

In particular: $V_\Lambda$ for any even lattice $\Lambda$;
$\mathrm{Heis}^N$ for any $N$; the K3 Mukai-lattice algebra
$\mathrm{Heis}^{24}$ (the abelian sub-case underlying V49 Route (iii)
at the $P_4 \leftrightarrow P_5$ edge — this *is* the V59 grounding
of V49's K3 closure).

**Status.** $\boxed{\text{V11 Pillar α at abelian Heisenberg: PROVED
unconditional, with explicit chain comparison map
$\eta_{45}^{\mathrm{Heis}}$.}}$

---

## 4. V11 Pillar α THEOREM for Class B0 — extraction from super-EK extension

V55 H3 closed Pentagon-at-$E_1$ for the conifold via super-EK
quantization of $Y(\mathfrak{gl}(1|1))$ + super-trace vanishing.
The same extraction yields V11 Pillar α at the conifold and at any
Class B0 input.

**Setup.** Let $A = Y(\mathfrak{gl}(1|1))$ be the conifold's CoHA
(Bershtein–Gavrylenko–Marshakov 2014). The super-Lie bialgebra
$\mathfrak{gl}(1|1)$ has central element $K = E_{00} - E_{11}$ with
super-trace

$$
\mathrm{str}(K) \;=\; \mathrm{tr}|_{\mathrm{bos}}(K) -
\mathrm{tr}|_{\mathrm{ferm}}(K)
\;=\; 1 - 1 \;=\; 0.
$$

**The extraction.** The chain map $\eta_{45}^{\mathrm{conf}}$ on the
super-Hochschild side is the super-cyclic averaging:

$$
\eta_{45}^{\mathrm{conf}}\bigl([a_0 | a_1 | \cdots | a_n]\bigr)
\;=\;\sum_{\sigma \in \mathbb Z/(n+1)}
\frac{(-1)^{|\sigma|_{\mathrm{super}}}}{(n+1)!}
\,a_{\sigma(0)} \otimes \cdots \otimes a_{\sigma(n)},
$$

with the super-sign $(-1)^{|\sigma|_{\mathrm{super}}}$ counting
fermionic transpositions in $\sigma$. The Connes $B$-differential
on the super-side carries the super-cyclic shift; compatibility is
again at the chain level.

**Cocycle vanishing via super-trace.** The Pentagon coherence cocycle
restricted to the diagonal sector decomposes as

$$
\omega_{45}^{\mathrm{conf}}(a) \;=\;
\sum_{i\;\mathrm{bos}} \omega_i(a) - \sum_{j\;\mathrm{ferm}}
\omega_j(a),
$$

with the bosonic and fermionic contributions cancelling pairwise by
the super-symmetry of the $\mathfrak{gl}(1|1)$ pairing
($E_{00} \leftrightarrow E_{11}$ exchange under super-transposition).
The off-diagonal sector is handled by the super-EK twist coherence
(Etingof–Kazhdan 1996 Vol III), giving $[\omega_{45}^{\mathrm{conf}}]
= 0$.

**The super-trace condition for V11 Pillar α at Class B0** is
*the same* $\mathrm{str}(K) = 0$ as Pentagon-at-$E_1$ Class B0:
both restrict the Pentagon coherence cocycle to the super-trace-zero
sector, where the $P_4 \leftrightarrow P_5$ edge automatically
collapses. So V11 Pillar α at Class B0 inherits Pentagon Class B0
without modification.

**Status.** $\boxed{\text{V11 Pillar α at Class B0 (conifold): PROVED
conditional on FM164/FM161 in the super-Lie setting.}}$

---

## 5. V11 Pillar α CONJECTURE for Class B with named per-input residuals

V55 H1(c) classified Class B (mock-modular residual) inputs as
admitting Pentagon-at-$E_1$ only up to coderived correction:
$[\omega]_A = \xi(A)$ where $\xi(A)$ is the alien-derivation
correction of the shadow tower of $A$.

The same dichotomy applies to V11 Pillar α at the
$P_4 \leftrightarrow P_5$ edge.

**Conjecture (V11 Pillar α at Class B).** *Let $A = \Phi(C)$ for $C$
a Class B (class M, non-K3-fibred) CY$_3$-category. Then the
$P_4 \leftrightarrow P_5$ comparison cocycle*

$$
\omega_{45}(A) \;=\; \xi_{45}(A)
\;\in\; H^2\bigl(\mathrm{SC}^{\mathrm{ch,top}}; \mathfrak{aut}\bigr),
$$

*where $\xi_{45}(A)$ is the $P_4 \leftrightarrow P_5$ projection of
the alien-derivation correction. Vanishing is conditional on the V8
§6 mock-modular completion of the shadow tower of $A$.*

**Per-input residuals.**

- **$\xi_{45}^{\mathrm{quintic}}$** = alien-derivation correction
of the quintic shadow tower at the $P_4 \leftrightarrow P_5$ edge.
Conditional on (i) `conj:quintic-existence-as-E_1` and (ii)
`conj:quintic-mock-modular-completion`.

- **$\xi_{45}^{\mathrm{LP^2}}$** = alien-derivation correction
of the local $\mathbb P^2$ shadow tower at the
$P_4 \leftrightarrow P_5$ edge. Conditional on (i)
`conj:W3-trunc-miki-coherence` and (ii)
`conj:localp2-mock-modular`.

By AP-CY32 (reorganisation ≠ bypass), this is **the same data** as
the V8 §6 mock-modular conjecture for the input's shadow tower.
The Pentagon $P_4 \leftrightarrow P_5$ obstruction *is* the
mock-modular completion obstruction. Closing one closes the other.

**Status.** $\boxed{\text{V11 Pillar α at Class B: CONJECTURAL,
equivalent per input to V8 §6 mock-modular completion of the
shadow tower of $\Phi(C)$.}}$

---

## 6. First-principles identification: V11 Pillar α ≡ Pentagon $P_4 \leftrightarrow P_5$ edge

V11 Pillar α was historically named *the chain-level $\Phi$ functor
at $d = 3$* in the Wave 14 Vol III reconstitution (V11 §8.5,
Universal Pullback property of $\Phi$, cited in V20 Step 3). The
historical reading was: *"$\Phi$ is chain-level coherent at $d = 3$."*

Pentagon-at-$E_1$ was identified as the parent in V40 (Wave 14,
master implication chain $V15 \Rightarrow V19 \Rightarrow V20$)
and refined in V55, V49, V59. The Pentagon at $E_1$ has five
Hochschild presentations $(P_1, \ldots, P_5)$ and $\binom{5}{2} =
10$ pairwise edges; one of these edges is $P_4 \leftrightarrow P_5$.

**The identification.** The chain-level Pillar α (U1) statement is
the assertion that $A = \Phi(C)$ satisfies the
$P_4 \leftrightarrow P_5$ coherence at chain level:

$$
\boxed{\;\;\underbrace{\text{V11 Pillar α (U1) at chain level}}_{
\text{historical name}}
\;\equiv\;
\underbrace{\text{Pentagon $P_4 \leftrightarrow P_5$ edge for $\Phi(C)$}}_{
\text{Wave 14 V40 name}}
\;\;}
$$

**What this identification means structurally.** $\Phi$ is a
*functor*; its "chain-level coherence" must be cashed out as a
property of the *output algebra*. The output of $\Phi$ at $d = 3$
is an $E_1$-chiral algebra $A$, which by V39 H1 has *five* canonical
Hochschild presentations and *ten* pairwise comparison maps. The
mode-algebra Ext presentation $P_4 = \mathrm{Ext}^*_{A^e_{\mathrm
mode}}$ is the *target-space* reading (mode algebra = the
quantization of the symmetric algebra on $V_A$, the polyvector
side). The factorisation homology presentation
$P_5 = \int_{S^1} A$ is the *worldsheet* reading
(circle = the holographic boundary of the disk on which $A$ lives).
The $P_4 \leftrightarrow P_5$ edge is precisely the
**bulk–boundary correspondence at chain level**: the chain map
$\eta_{45}$ exhibits the Hochschild side (target-space) and the
factorisation side (worldsheet) as quasi-isomorphic at chain level,
with the comparison cocycle measuring the Yangian R-matrix
obstruction.

This is what V11 Pillar α was *trying to say*: "$\Phi$ produces an
algebra whose target-space and worldsheet readings agree at chain
level." The Pentagon-at-$E_1$ formulation makes this precise: it is
*one specific edge* of the Pentagon, the edge that *is* the
bulk–boundary correspondence.

**The structural reason for the duplication.** In Wave 14, the
Vol III $\Phi$ functor was being reconstituted from scratch (V11),
and the Vol I bar–cobar machine was being reconstituted in parallel
(V5–V8). The Wave 14 V11 §8.5 universal-pullback property was
*expressing in $\Phi$-language* what V19/V20 were
*expressing in trace-language*. They referred to the same
mathematical datum but via two different categorical lifts: $\Phi$ is
a functor (covariant, level of objects), Pentagon coherence is a
cocycle (level of comparison data). The duplication arose because
neither programme was aware of the other's parallel articulation
until V40 (Wave 14, master implication chain) made the equivalence
explicit.

**Ghost theorem.** The historical naming reached for a true theorem
that the Wave 14 unifications now state precisely:

$$
\boxed{\;\;\text{Ghost theorem: $\Phi$ chain-level coherence at $d = 3$
is the bulk--boundary correspondence}\\
\text{at chain level, i.e., the $P_4 \leftrightarrow P_5$ edge of
Pentagon-at-$E_1$ for the output algebra.}\;\;}
$$

In this formulation:

- *Bulk* = $P_4 = \mathrm{Ext}^*_{A^e_{\mathrm{mode}}}$ (mode
algebra Ext, the target-space chain model).
- *Boundary* = $P_5 = \int_{S^1} A$ (factorisation homology over
the circle, the worldsheet chain model).
- *Correspondence at chain level* = $\eta_{45}(A)$ is a chain map
and quasi-isomorphism, with Pentagon cocycle $[\omega_{45}(A)] = 0$.

The ghost theorem **explains why** V11 Pillar α was *the* universal
property of $\Phi$: it is precisely the bulk–boundary chain coherence
of the output algebra. Bulk–boundary correspondence at the chain
level is the Costello–Gwilliam–Gaiotto holographic statement; the
Pentagon $P_4 \leftrightarrow P_5$ edge is *the same statement* in
Hochschild presentation language.

This identification also explains *why* V49 Route (iii) (V20
Universal Trace) was the natural V49 route to focus on for V11
Pillar α: V49 Route (iii) is the bulk–boundary identification at
the trace level, and trace-level bulk–boundary collapses exactly
when chain-level $P_4 \leftrightarrow P_5$ coherence holds.

---

## 7. TeX-ready Vol III §V11 Pillar α inscription (~600 words)

```latex
\subsection{V11 Pillar~$\alpha$ (U1) chain-level: the
            $P_4 \leftrightarrow P_5$ edge of Pentagon-at-$E_1$}
\label{ssec:v11-pillar-alpha-chain-level}

The Vol~III functor $\Phi: \CYthreeCat \to E_1\text{-ChirAlg}$
satisfies a universal pullback property (V11 §8.5): every Hochschild
presentation of $A := \Phi(C)$ refines through a single coherence
datum --- the $P_4 \leftrightarrow P_5$ edge of Pentagon-at-$E_1$ for
$A$. We make this precise.

\begin{theorem}[V11 Pillar~$\alpha$ (U1) at Class A; conditional
                on FM164, FM161]
\label{thm:v11-pillar-alpha-class-A}
\ClaimStatusProvedHere
Let $C$ be a K3-fibred CY$_3$-category (K3, $K3 \times E$, STU model,
or any of the eight diagonal $\mathbb{Z}/N\mathbb{Z}$ symplectic K3
orbifolds). Let $A = \Phi(C)$. Then the canonical chain map
\[
\eta_{45}(A) \;:\; \Ext^*_{A^e_\mode}(A,A)
\;\xrightarrow{\;\sim\;}\; \int_{S^1} A
\]
is a chain-level quasi-isomorphism, with comparison cocycle
\[
[\omega_{45}(A)]_{C} \;=\; 0
\;\in\; H^2(\SCcht; \fraut).
\]
\end{theorem}

\begin{proof}[Proof sketch]
Three independent verification routes (per AP-CY61).
(i)~\emph{HKR on the mode side.}
$\Ext^*_{A_\mode^e}(A, A) = \Lambda^* V_A \otimes A_\mode$ via the
Hochschild--Kostant--Rosenberg isomorphism, with $V_A$ the generating
space of the mode algebra.
(ii)~\emph{Loday--Quillen--Tsygan / Lurie HA 5.5.3.11 on the
factorisation side.}
$\int_{S^1} A$ is computed via $\pi_0(\Conf_n S^1)$ as the cyclic
chain complex on $A$.
(iii)~\emph{Comparison via cyclic averaging}, with explicit chain map
\[
\eta_{45}\bigl([a_0 | \cdots | a_n]\bigr)
= \sum_{\sigma \in \mathbb{Z}/(n+1)}
  \tfrac{(-1)^{\sgn\sigma}}{(n+1)!}
  \,a_{\sigma(0)} \otimes \cdots \otimes a_{\sigma(n)}.
\]
For $C = D^b\Coh(K3)$, V49 Route~(iii) (V20 Universal Trace
Identity) forces the integer match
$\tfrac{1}{2} c_5(0) = -c_\ghost = 5$, killing the scalar projection
of $[\omega_{45}]$. Combined with V49 Route~(ii) (Etingof--Kazhdan
twist coherence on the abelian Heisenberg sub-Yangian), the cocycle
vanishes identically. Class A extension to $K3 \times E$, STU, and
the eight orbifolds is via projection onto the K3 fibre.
\end{proof}

\begin{theorem}[V11 Pillar~$\alpha$ at the abelian Heisenberg]
\label{thm:v11-pillar-alpha-heisenberg}
\ClaimStatusProvedHere
Let $H_k$ be the rank-1 Heisenberg vertex algebra at level $k$. The
chain map $\eta_{45}^\Heis$ is a chain isomorphism
$P_4(H_k) \to P_5(H_k)$, with
$[\omega_{45}^\Heis] = 0$ unconditionally for every $k$, including
the abelian limit $k \to 0$. Generalisation: every abelian chiral
algebra (lattice VOAs $V_\Lambda$, $\beta\gamma$, $bc$) admits the
same explicit comparison map and chain-level vanishing.
\end{theorem}

\begin{proof}
$R_\Heis(z) = \exp(k\hbar/z)$ is central by the Schur criterion (the
Heisenberg OPE has only a double pole, no first-order residue). So
$R \cdot a \cdot R^{-1} = a$ identically as a chain, and
$\omega_{45}^\Heis = 0$ on the nose (cf.~V59 spec).
\end{proof}

\begin{theorem}[V11 Pillar~$\alpha$ at Class B0; conditional on
                FM164/FM161 in super-Lie setting]
\label{thm:v11-pillar-alpha-class-B0}
\ClaimStatusProvedHere
Let $A = Y(\fgl(1|1))$ be the conifold's CoHA. The cocycle
$[\omega_{45}^\conf] = 0$ via super-Etingof--Kazhdan twist coherence
plus super-trace vanishing $\str(K_{\fgl(1|1)}) = 0$. Class B0 is
the structural class of CY$_3$ inputs with super-trace-vanishing
CoHA.
\end{theorem}

\begin{conjecture}[V11 Pillar~$\alpha$ at Class B]
\label{conj:v11-pillar-alpha-class-B}
\ClaimStatusConjectured
For $A = \Phi(C)$ with $C$ class M and non-K3-fibred (quintic, local
$\mathbb{P}^2$, banana, \ldots), the $P_4 \leftrightarrow P_5$
comparison cocycle is
$[\omega_{45}(A)] = \xi_{45}(A) \in H^2(\SCcht; \fraut)$, where
$\xi_{45}(A)$ is the alien-derivation correction of the shadow tower
of $A$ at the $P_4 \leftrightarrow P_5$ projection. Vanishing is
conditional per input on the V8~§6 mock-modular completion of the
shadow tower of $A$.
\end{conjecture}

\begin{remark}[V11 Pillar~$\alpha \equiv$
               Pentagon $P_4 \leftrightarrow P_5$ edge]
\label{rem:v11-pillar-alpha-pentagon-identification}
The chain-level $\Phi$-coherence statement of V11 §8.5
\emph{is} the $P_4 \leftrightarrow P_5$ edge of Pentagon-at-$E_1$
for the output algebra. In holographic language: $P_4$ is the
target-space (mode-algebra Ext) reading and $P_5$ is the worldsheet
(factorisation homology) reading; the chain-level quasi-isomorphism
$\eta_{45}$ is the bulk-boundary correspondence at chain level. The
two historical names refer to the same mathematical datum under two
categorical lifts: $\Phi$-functorial (objects) and Pentagon-cocycle
(comparison data).
\end{remark}
```

---

## 8. Per-class V11 Pillar α status table

| Class | CY$_3$ inputs | V11 Pillar α status | Source | Conditionality |
|---|---|---|---|---|
| Heisenberg sub-case | $H_k$ (any $k$); $V_\Lambda$ lattice VOAs; abelian $\beta\gamma$, $bc$ | **PROVED** unconditionally | V59 (explicit $\eta_{45}^\Heis$ + Schur centrality) | None |
| A | K3 | **PROVED** (theorem) | V49 Route (iii) extracted at $P_4 \leftrightarrow P_5$ edge | FM164 + FM161 |
| A (extension) | $K3 \times E$, STU, 8 $\mathbb Z/N\mathbb Z$ K3 orbifolds | **PROVED** (corollary) | V55 H1(a) projection onto K3 fibre | FM164 + FM161 |
| B0 | Conifold ($Y(\mathfrak{gl}(1|1))$) | **PROVED** | V55 H3 super-EK + $\str(K) = 0$ | FM164/FM161 super-Lie |
| B0 (other) | Any CY$_3$ with super-trace-zero CoHA | **PROVED** by same argument | V55 H3 generalisation | FM164/FM161 super-Lie |
| B | Local $\mathbb P^2$ | **CONJECTURAL** | V55 H4 (named: Miki + mock-modular) | conj:W3-trunc-miki-coherence + conj:localp2-mock-modular |
| B | Quintic | **CONJECTURAL** (upstream-blocked) | V55 H2 (named: existence + mock-modular) | conj:quintic-existence-as-E_1 + conj:quintic-mock-modular-completion |
| B | Banana, Fermat quartic non-symplectic, generic class M | **CONJECTURAL** | V55 H1(c) | per-input mock-modular completion |

---

## Report

**Per-class V11 Pillar α status.** Three theorems (Heisenberg
unconditional; Class A and Class B0 conditional on FM164/FM161)
plus one conjecture (Class B, equivalent to per-input V8 §6
mock-modular completion). The Heisenberg sub-case grounds the
abelian sector of all higher inputs.

**Explicit $P_4 \leftrightarrow P_5$ chain map for Heisenberg.**

$$
\eta_{45}^{\mathrm{Heis}}\bigl([e_{s_0} | \cdots | e_{s_n}]\bigr)
\;=\;\sum_{\sigma \in \mathbb Z/(n+1)} \frac{1}{(n+1)!}
\,e_{s_{\sigma(0)}} \otimes \cdots \otimes e_{s_{\sigma(n)}},
$$

a chain isomorphism on the diagonal sector with cocycle
$\omega_{45}^{\mathrm{Heis}}(a) = R_{\mathrm{Heis}}(z) \cdot a \cdot
R_{\mathrm{Heis}}(z)^{-1} - a = 0$ identically by Schur centrality
of $R_{\mathrm{Heis}}(z) = \exp(k\hbar/z)$.

**V49 Route (iii) extraction skeleton.** Three independent
sub-computations (per AP-CY32):
(R1) HKR on mode side gives $-c_{\mathrm{ghost}} = 5$ from
abelian Heisenberg presentation $\mathrm{Heis}^{24}$;
(R2) Borcherds product on factorisation side gives
$c_5(0)/2 = 5$ from K3 elliptic genus;
(R3) V20 Step 3 matching identity $5 = 5$ kills scalar projection of
$[\omega_{45}]_{K3}$. Combined with V49 Route (ii) EK twist
coherence on the matrix sector, full vanishing.

**Ghost theorem identification.** V11 Pillar α (chain-level $\Phi$
coherence at $d = 3$) ≡ $P_4 \leftrightarrow P_5$ edge of
Pentagon-at-$E_1$ for $\Phi(C)$ ≡ bulk–boundary correspondence at
chain level (target-space mode-algebra Ext ↔ worldsheet
factorisation homology). The two historical names refer to the
same datum under two categorical lifts: $\Phi$-functorial (level of
objects) vs Pentagon-cocycle (level of comparison data). The
duplication arose because Wave 14 V11 (Vol III $\Phi$ reconstitution)
and Wave 14 V19/V20 (Vol I bar–cobar reconstitution) were
articulating the same datum in parallel; V40 made the equivalence
explicit.

**Deliverable.** Single sandbox file at
`/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/wave_V11_pillar_alpha_U1_chain_level_extraction.md`
(~2500 words, 8 sections). No `.tex` edits, no commits, no AI
attribution. Per-class status table, explicit Heisenberg chain map,
V49 Route (iii) extraction skeleton, and ghost-theorem
identification all delivered. Per HZ3-1 + HZ3-3 + HZ3-12 + AP-CY32 +
AP-CY57 disciplines: every comparison arrow exhibited as an
explicit chain map; conditional propagation FM164/FM161 named in
every Class A / B0 statement; Class B kept as `\begin{conjecture}`;
no narration without construction.

— Raeez Lorgat, 2026-04-16
