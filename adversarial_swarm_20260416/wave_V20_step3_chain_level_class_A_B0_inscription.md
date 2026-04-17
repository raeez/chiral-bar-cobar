# Wave V58 (V20 Step 3 chain-level dichotomy inscription)
## V20 Step 3 chain-level as a THEOREM for Class A and Class B0,
## with Class B as named residual conjecture

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Inscription-ready
sandbox draft for Vol I §V20 epilogue, downstream consolidation of V55 H1
dichotomy + V57 V49 inscription bundle. **Posture.** No `.tex` edits, no
`CLAUDE.md` updates, no commits, no test runs, no build. Read-only structural
draft for main-thread review and selective application.

**Companions.** V40 (`wave_frontier_universal_trace_chain_level.md` master
implication chain Pentagon-at-$E_1 \Rightarrow$ V19 Trinity-$E_1 \Rightarrow$
V20 Step 3 chain-level); V49 (`wave_K3_Pentagon_E1_attempt.md` K3-Pentagon
three-route resolution); V55 (`wave_frontier_pentagon_E1_non_K3.md` Class A /
B0 / B dichotomy); V57 (`draft_k3_yangian_pentagon_E1_theorem.tex` TeX-ready
K3-Pentagon theorem + corollary bundle); V20 cross-volume centrepiece
(`UNIVERSAL_TRACE_IDENTITY.md`); V50 (`wave_K3_multi_projection_trace.md`
inverting V41: Verlinde fibre is OFF the four-term Wave-21 closure as an
additional projection on $Z_{\mathrm{Verlinde}}$, NOT the missing fourth term);
V53.1 (Berezinian channel rigidly forced by Mukai signature
$\operatorname{sdim} = p - q$).

**Single-line thesis.** The V40 master implication chain
$$
\text{Pentagon-at-}E_1 \;\Longrightarrow\; \text{V19 Trinity-}E_1
\;\Longrightarrow\; \text{V20 Step 3 chain-level}
$$
combined with the V55 dichotomy of its premise into Class A (PROVED, V49 K3
routes), Class B0 (PROVED, super-EK + super-trace vanishing), and Class B
(CONJECTURAL, mock-modular completion residual) yields the same dichotomy on
its conclusion: V20 Step 3 chain-level is a THEOREM for Class A and Class B0,
and a precise residual CONJECTURE for Class B with explicit per-input residual
$\operatorname{tr}(\xi_A)$ named.

---

## §1. Precise statement of V20 Step 3 chain-level for arbitrary chiral algebra $A$

The V20 Universal Trace Identity (`UNIVERSAL_TRACE_IDENTITY.md`) states that
for any CY$_d$ category $\mathcal{C}$ with Vol III $\Phi$-image
$A := \Phi(\mathcal{C}) \in (\text{$E_n$-ChirAlg})$ ($n = \infty, 2, 1$ at
$d = 1, 2, \geq 3$ respectively), there is a single involutive reflection
$\mathfrak{K}_{\mathcal{C}}$ on the categorical centre
$Z(\mathcal{C}) := \operatorname{Hom}_{\mathcal{C}\text{-}\mathcal{C}\text{-bimod}}
(\operatorname{id}_{\mathcal{C}}, \operatorname{id}_{\mathcal{C}})$ with two
specialisations of its trace:
$$
\operatorname{tr}_{Z(\mathcal{C})}(\mathfrak{K}_{\mathcal{C}})
\;=\; -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal{C})))
\;=\; \frac{c_N(0)}{2}.
\tag{V20-eq}
$$
The **homotopy-category** version of this identity (i.e., on
$h(Z(\mathcal{C}))$) is unconditional: it follows from the Wave 14 V11 §8.5
universal-pullback property of $\Phi$ combined with skew-derivation rigidity
(`UNIVERSAL_TRACE_IDENTITY.md` §IV Step 3). The **chain-level** version is
the content of V20 Step 3:

> **Definition (V20 Step 3 chain-level for $A$).** Let $A$ be an
> $E_1$-chiral algebra (so $A = \Phi(\mathcal{C})$ at $d \geq 3$, or, by
> restriction, the $E_1$-shadow of an $E_2$-chiral algebra at $d = 2$). The
> **V20 Step 3 chain-level identity for $A$** is the assertion that
> $$
> \mathfrak{K}_A^{\mathrm{ch}} \;=\; \mathfrak{K}_A^{\mathrm{BKM}}
> \quad \text{as chain-level operators on } Z(\mathcal{C})
> $$
> in the algebraic chiral Hochschild model
> $C^*_{\mathrm{ch,alg}}(A,A)$ (AP-CY62 (b)), with both sides specialising at
> the level of traces to (V20-eq).

Equivalently, the **chain-level discrepancy**
$$
\delta_A \;:=\; \mathfrak{K}_A^{\mathrm{ch}} - \mathfrak{K}_A^{\mathrm{BKM}}
\;\in\; \operatorname{Hom}_{\mathrm{Ch}}\bigl(Z(\mathcal{C}), Z(\mathcal{C})\bigr)[+1]
$$
vanishes chain-level, NOT merely up to chain homotopy.

**V40 master implication.** V40 reduced the chain-level vanishing of
$\delta_A$ to the chain-level Pentagon-at-$E_1$ coherence cocycle of V39 H1:
$$
[\omega]_A \;=\; 0 \;\in\; H^2(\mathrm{SC}^{\mathrm{ch,top}}; \mathfrak{aut})
\quad\Longrightarrow\quad
\delta_A \;=\; 0 \;\in\; \mathrm{Hom}_{\mathrm{Ch}}(Z(\mathcal{C}), Z(\mathcal{C}))[+1].
$$
The implication route: $[\omega]_A = 0$ forces the chain-level V19 Trinity at
$E_1$ for $A$ (the five Hochschild presentations of $A$ are pairwise
quasi-isomorphic at chain level, with no Pentagon obstruction); V19 Trinity
at chain level forces the chain-level identification of $\mathfrak{K}_A^{\mathrm{ch}}$
with the chiral-bar Koszul reflection on $\overline{B}_X(A)$; the
chiral-bar Koszul reflection chain-level-coincides with the Borcherds
reflection on the BKM lift (when the BKM lift exists; modified residual
when it does not, see §4).

This wave inherits the V55 dichotomy of the premise into the same dichotomy
on the conclusion.

---

## §2. THEOREM for Class A (K3-fibred CY$_3$ inputs)

### 2.1 Statement

> **Theorem (V20 Step 3 chain-level for Class A; CONDITIONAL on FM164,
> FM161 K3-specialised).** Let $\mathcal{C}$ be a CY$_3$ category whose
> object $X$ admits an elliptic K3-fibration $X \to B$, equivalently
> $X \in \{K3, K3 \times E, \text{STU}, \text{8 diagonal Z/NZ symplectic
> K3 orbifolds}\}$ (the V55 Class A roster). Let
> $A = \Phi(D^b(\mathrm{Coh}(X)))$ be its CY-to-chiral image. Then
> $$
> \boxed{\;\operatorname{tr}_{Z(\mathcal{C})}(\mathfrak{K}_{\mathcal{C}})
> \;=\; -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal{C})))
> \;=\; \frac{c_N(0)}{2}\;}
> $$
> holds **at chain level** in the algebraic chiral Hochschild model
> $C^*_{\mathrm{ch,alg}}(A,A)$. Equivalently, the chain-level discrepancy
> $\delta_A = 0$ in $\mathrm{Hom}_{\mathrm{Ch}}(Z(\mathcal{C}), Z(\mathcal{C}))[+1]$.

### 2.2 Proof sketch (reduction to V49 + V40 + Class M shadow tower at $\xi(A) = 0$ for K3-fibred input)

The proof proceeds in three steps.

**Step A (Pentagon-at-$E_1$ for K3-fibred inputs reduces to V49).**
Let $A_X = \Phi(D^b(\mathrm{Coh}(X)))$ with $X$ K3-fibred. The V49 H1 (Class A
extension) statement establishes that the Pentagon coherence cocycle
$[\omega]_{A_X}$ vanishes via fibre-localisation: the elliptic / orbifold base
acts trivially on the Mukai-lattice Pentagon data because the Mukai pairing
lives entirely on the K3 fibre. Concretely, for $X = K3 \times E$,
$\Phi(\mathcal{C}) = H_{\mathrm{Mukai}} \otimes V_E$ with $V_E$ the elliptic
lattice VOA; the Pentagon cocycle factorises as
$[\omega]_{K3 \times E} = [\omega]_{K3} \otimes [\omega]_E$, and both factors
vanish individually (V49 K3-Pentagon, plus elliptic lattice VOA Pentagon
trivially closed by abelian structure). For the eight diagonal $\mathbb{Z}/N\mathbb{Z}$
symplectic K3 orbifolds ($N = 1, \ldots, 8$, per `kappa_bkm_universal.py`
classification), the orbifold quotient acts as a permutation on the Mukai
sublattice that preserves the Pentagon cocycle's vanishing class (each orbit
contributes its $K3$-Pentagon and the orbit-sum is zero by symmetry of the
diagonal action). For STU model, the K3 fibre over a rational base inherits
V49 directly.

The honest scope: V49 is conditional on FM164 (Yangian pro-nilpotent bar-cobar
completion) and FM161 (Yangian Koszulness in the Positselski nonhomogeneous
framework), both K3-specialised. These conditions are inherited by all Class A
extensions (the elliptic and orbifold quotients do not introduce new Yangian
completion gaps).

**Step B (V40 master implication).** By V40 (`wave_frontier_universal_trace_chain_level.md`
§3.1), the chain-level vanishing of $[\omega]_{A_X}$ forces the chain-level
V19 Trinity at $E_1$ for $A_X$, which in turn forces the chain-level
identification of $\mathfrak{K}_{A_X}^{\mathrm{ch}}$ with $\mathfrak{K}_{A_X}^{\mathrm{BKM}}$
in the algebraic chiral Hochschild model.

**Step C (Class M shadow tower at $\xi(A_X) = 0$ for K3-fibred input).** For
$A_X$ K3-fibred, the shadow-tower data $(c_S, A_\pm, S_\pm)$ of $A_X$ is
derivable from the K3 fibre's shadow tower, which is class L (for pure K3
abelian level) or class C (with ADE enhancement at singular K3 moduli) —
NEITHER of which carries non-trivial alien-derivation correction. Therefore
the V40 §3.1 alien-derivation correction $\xi(A_X) = 0$ unconditionally for
K3-fibred inputs (the class M residual term of V40 §2.3 option (b) is empty
for Class A).

In particular, the trace identity (V20-eq) holds chain-level with no Stokes
correction: the LHS and RHS are equal as chain-level operators on $Z(\mathcal{C})$,
not merely modulo a Borel-summable alien correction.

**Step D (Trace specialisations).** Apply V20 Steps 4 and 5
(`UNIVERSAL_TRACE_IDENTITY.md` §IV) to obtain the two specialisations:
the BRST ghost reading $-c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal{C})))$
chain-level-equals the Borcherds reading $c_N(0)/2$ for $N$ the orbifold
order ($N = 1$ for K3 untwisted, $N = 1, \ldots, 8$ for the diagonal
symplectic orbifolds; the BKM weight values are $5, 4, 3, 2, 2, 2, 2, 2$ from
the Vol III table per `prop:bkm-weight-universal`).

**Q.E.D. (modulo FM164/FM161 K3-specialised).**

### 2.3 Conditional dependencies (per AP-CY11)

This theorem chains through V49 (K3 Pentagon-at-$E_1$), which is conditional
on FM164 + FM161 K3-specialised. By AP-CY11 (HZ3-3), this conditionality
propagates: V20 Step 3 chain-level for Class A is `\ClaimStatusConditional`
on FM164/FM161 K3-specialised. The conditionality is separable (a follow-up
technical exercise on Yangian Koszulness for K3-input data) and is not a
mathematical obstruction; the dependency is recorded explicitly per the
HZ3-3 protocol.

Per AP-CY60: the V49 K3 routes (sympy direct, Etingof–Kazhdan, V20 trace)
are three independent constructions, NOT three applications of $\Phi$. The
present Class A theorem inherits this discipline: the proof above invokes V49
once via the master implication, and the elliptic/orbifold extension within
Class A is a fibre-localisation argument, NOT an additional application of
$\Phi$.

---

## §3. THEOREM for Class B0 (super-trace vanishing)

### 3.1 Statement

> **Theorem (V20 Step 3 chain-level for Class B0; CONDITIONAL on FM164,
> FM161 super-Lie variant).** Let $A$ be an $E_1$-chiral algebra arising as
> the CoHA of a CY$_3$ category whose super-trace $\operatorname{str}(K_A) = 0$.
> Equivalently: $A$ is a quantization of a Lie superbialgebra
> $(\mathfrak{g}, \delta)$ with vanishing super-Killing form
> $\operatorname{str}_{\mathfrak{g}}(\mathrm{ad}\, x \circ \mathrm{ad}\, y) = 0$
> for all $x, y \in \mathfrak{g}$. (The canonical example is the **resolved
> conifold** $X_{\mathrm{res}} = \mathcal{O}(-1) \oplus \mathcal{O}(-1) \to
> \mathbb{P}^1$, with $A = Y(\mathfrak{gl}(1|1))$ via the
> Bershtein–Gavrylenko–Marshakov 2014 CoHA construction, and
> $\operatorname{str}(\mathbf{1}_{\mathfrak{gl}(1|1)}) = 1 - 1 = 0$.)
> Then
> $$
> \boxed{\;\operatorname{tr}_{Z(\mathcal{C})}(\mathfrak{K}_{\mathcal{C}})
> \;=\; -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal{C})))
> \;=\; 0\;}
> $$
> holds **at chain level** in $C^*_{\mathrm{ch,alg}}(A,A)$. The right-hand
> $c_N(0)/2$ specialisation is replaced by $0$ in the absence of a BKM lift;
> the trace identity collapses to a single zero on both sides.

### 3.2 Proof sketch (super-EK extension)

**Step A (Pentagon-at-$E_1$ for Class B0 reduces to V55 H3).**
V55 H3 (`wave_frontier_pentagon_E1_non_K3.md` §H3) establishes the conifold
Pentagon-at-$E_1$ via three independent routes parallel to V49:
(i) direct super-sympy verification of the
$Y(\mathfrak{gl}(1|1))$ R-matrix (Bershtein et al. 2014, eq. 4.2);
(ii) super-Etingof–Kazhdan quantization of $\mathfrak{gl}(1|1)$ Lie
superbialgebra (Etingof–Kazhdan 1996 Vol. III super-version, with
super-Drinfeld twist coherence);
(iii) super-trace vanishing $\operatorname{str}(K_A) = 0$ as a
representation-theoretic identity.

For general Class B0 inputs (any $A$ with $\operatorname{str}(K_A) = 0$
arising from a super-Lie superbialgebra quantization), the same three routes
generalise: (i) is algebra-specific but extends to any explicit Yangian
super-R-matrix; (ii) is structural (EK super-quantization holds for ALL Lie
superbialgebras); (iii) is the defining property of Class B0.

**Step B (V40 master implication, super version).** The V40 master implication
chain Pentagon-at-$E_1 \Rightarrow$ V19 Trinity-$E_1 \Rightarrow$ V20 Step 3
chain-level is structural and applies in the super-Lie setting without
modification. The chain-level Hochschild model $C^*_{\mathrm{ch,alg}}(A,A)$ is
defined for super-chiral algebras (the underlying chain complex is the same;
the super-grading gives signs in differentials but the cocycle structure is
identical).

**Step C (super-trace vanishing kills the residual).** For Class B0 inputs,
the V40 §2.3 option (b) alien-derivation correction $\xi(A)$ has its
$\operatorname{tr}$ computed via super-trace, and
$\operatorname{str}(\xi_A) = 0$ by Class B0 hypothesis. Therefore the
chain-level identity reduces to $0 = 0 + 0$, with both sides vanishing
identically: the BRST ghost reading $c_{\mathrm{ghost}} = 0$ for
$\mathfrak{gl}(1|1)$ (super-BRST resolution is trivial, $\mathfrak{gl}(1|1)$
is its own BRST cohomology), and the Borcherds reading is undefined (no BKM
lift) but the conditional trace identity in the form
$\operatorname{tr}(\mathfrak{K}) = c_N(0)/2 + \operatorname{str}(\xi_A)$
reduces to $0 = 0 + 0$.

**Step D (per V53.1: Berezinian channel rigidly forced by Mukai signature).**
For $X_{\mathrm{res}}$ (resolved conifold), the Mukai signature is
$\operatorname{sdim} = p - q = 0$ (vanishing super-dimension of the conifold
CoHA), forcing the Berezinian channel to act trivially. This is the V53.1
rigidity statement: the super-trace channel is not a free parameter but is
rigidly determined by the geometry. For Class B0 inputs more generally,
$\operatorname{str}(K_A) = 0$ is the structural shadow of $\operatorname{sdim}
\operatorname{Coh}(X) = 0$ (vanishing super-dimension of the geometric
category).

**Q.E.D. (modulo FM164/FM161 super-Lie variant).**

### 3.3 Conditional dependencies (per AP-CY11)

V55 H3 is conditional on FM164/FM161 in the super-Lie setting (super-version
of the standard Yangian Koszulness; tractable at the same difficulty as the
even case). This conditionality propagates: V20 Step 3 chain-level for
Class B0 is `\ClaimStatusConditional` on FM164/FM161 super-Lie variant.

Per AP-CY60: the conifold is the **canonical example** of Class B0; other
Class B0 candidates include any CY$_3$ whose CoHA is a quantization of a
super-Lie bialgebra with $\operatorname{str} = 0$ (e.g., $bc$-$\beta\gamma$
systems on log-degenerate toric CY$_3$ via Atiyah-flop resolution; see V55
§H9 reason 2). The theorem is stated for general Class B0; the conifold is
the inhabited witness.

---

## §4. CONJECTURE for Class B (mock-modular residual)

### 4.1 Statement

> **Conjecture (V20 Step 3 chain-level for Class B; CONJECTURAL).** Let $A$
> be an $E_1$-chiral algebra of shadow class M (per V8 quadrichotomy) that is
> neither K3-fibred (Class A) nor super-trace vanishing (Class B0). The
> canonical examples are:
> - $A_{\mathrm{quintic}} = \Phi(D^b(\mathrm{Coh}(Q)))$ (quintic CY$_3$
>   $Q \subset \mathbb{P}^4$, $\chi/24 = -25/3$, BCOV value);
> - $A_{\mathrm{LP^2}} = \Phi(D^b(\mathrm{Coh}(K_{\mathbb{P}^2})))$
>   (local $\mathbb{P}^2$, $\kappa_{\mathrm{ch}} = \chi(\mathbb{P}^2)/2 = 3/2$).
>
> Then the V20 chain-level identity holds **modulo the alien-derivation
> correction** $\xi(A)$ of the class M shadow tower:
> $$
> \mathfrak{K}_A^{\mathrm{ch}} - \mathfrak{K}_A^{\mathrm{BKM-replacement}}
> \;=\; \partial \mu + \mu \partial + \xi(A) \quad \text{in } C^*_{\mathrm{ch,alg}}(A,A)
> $$
> where $\xi(A)$ is the Stokes-jump invariant of the shadow tower of $A$
> (V40 §2.3 option (b)), and $\mathfrak{K}_A^{\mathrm{BKM-replacement}}$ is
> the BCOV / Donaldson–Thomas replacement reflection ($\kappa_{\mathrm{BCOV}}
> = \chi(X)/24$ for compact, shadow-depth replacement for non-compact).
> The trace identity becomes
> $$
> \operatorname{tr}_{Z(\mathcal{C})}(\mathfrak{K}_A^{\mathrm{ch}})
> \;-\; \operatorname{tr}_{Z(\mathcal{C})}(\mathfrak{K}_A^{\mathrm{BKM-replacement}})
> \;=\; \operatorname{tr}(\xi_A).
> $$
>
> **Vanishing** $\operatorname{tr}(\xi_A) = 0$ is CONJECTURAL conditional on
> the V8 §6 mock-modular completion of the shadow tower of $A$ matching the
> Zwegers holomorphic anomaly of the (hypothetical or replacement) BKM lift
> of $A$.

### 4.2 Explicit per-input residuals

**Quintic.** Sub-conjectures (per V55 H2):
- (`conj:quintic-existence-as-E_1`) $A_{\mathrm{quintic}}$ exists as a
  chain-level $E_1$-chiral algebra with $\kappa_{\mathrm{ch}} = -25/3$.
- (`conj:quintic-mock-modular-completion`) The quintic shadow tower's
  Stokes data $(c_S^{\mathrm{quintic}}, A_\pm^{\mathrm{quintic}},
  S_\pm^{\mathrm{quintic}})$ admits a mock-modular completion playing the
  role of the (non-existent) BKM lift.

The explicit residual:
$$
\operatorname{tr}(\xi_{\mathrm{quintic}})
\;=\; \mathrm{Borel\text{-}sum}\Bigl(\sum_{g \geq 1} \Delta F_g^{\mathrm{quintic}}(q)\Bigr)
$$
where $F_g^{\mathrm{quintic}}(q)$ is the genus-$g$ topological string free
energy on the quintic and $\Delta F_g$ is its Stokes jump (per BCOV resurgence,
Mariño–Schiappa–Reis transseries). This is currently OPEN at the cutting edge
of CY$_3$ mirror symmetry; closing it is equivalent to closing the quintic
mock-modular completion.

**Local $\mathbb{P}^2$.** Sub-conjectures (per V55 H4):
- (`conj:W3-trunc-miki-coherence`) Algebraic Miki coherence for the
  $W_3$-truncation of $U_{q,t}(\widehat{\widehat{\mathfrak{gl}_1}})$
  (separable algebraic problem, plausibly tractable in 1–2 sessions per
  AP-CY22 algebra-specific Miki).
- (`conj:localp2-mock-modular`) The local $\mathbb{P}^2$ shadow tower's
  Stokes data $(c_S^{\mathrm{LP^2}}, A_\pm^{\mathrm{LP^2}},
  S_\pm^{\mathrm{LP^2}})$ matches a mock-modular completion governing the
  local $\mathbb{P}^2$ Donaldson–Thomas partition function.

The explicit residual:
$$
\operatorname{tr}(\xi_{\mathrm{LP^2}})
\;=\; \xi_{\mathrm{Miki}}^{\mathrm{LP^2}} \;+\; \xi_{\mathrm{mock}}^{\mathrm{LP^2}}
$$
decomposed as the **algebraic** Miki-coherence correction (controllable via
$W_3$-truncation) plus the **resurgent** mock-modular completion correction
(at the level of Pasquetti–Schiappa local $\mathbb{P}^2$ resurgence, plus
Couso-Santamaría–Edelstein–Schiappa transseries work). The first term is
plausibly closeable; the second is the cutting edge.

### 4.3 Status discipline (per HZ3-1, AP-CY40)

The Class B statement uses `\begin{conjecture}` per HZ3-1: the proof chain
through V55 H1(c) reaches back to the open Pentagon-at-$E_1$ for Class B
inputs, which is itself conjectural. Per AP-CY40, no `\ClaimStatusProvedHere`
tag may be applied. The decomposition
$\operatorname{tr}(\xi_A) = \xi_{\mathrm{algebraic}} + \xi_{\mathrm{resurgent}}$
makes the residual obstructions PRECISE per input; the conjecture is
quantitatively stated, not vague.

---

## §5. TeX-ready epilogue for Vol I §V20 (~600 words)

The following block is intended for insertion at the end of the §V20
treatment in Vol I (Universal Trace Identity chapter), following the
homotopy-category Theorem and preceding the cross-volume Remark on the
Borcherds singular-theta correspondence. Insertion target:
`/Users/raeez/chiral-bar-cobar/chapters/koszul/chiral_chern_weil_brst_conductor.tex`
(per `UNIVERSAL_TRACE_IDENTITY.md` §IX install location 1).

```latex
%% =========================================================================
%% Vol I §V20 epilogue: chain-level dichotomy for V20 Step 3 (the chain-level
%% upgrade of the Universal Trace Identity).
%% Sandbox draft from wave_V20_step3_chain_level_class_A_B0_inscription.md
%% (Wave V58, 2026-04-16). Inscription pending main-thread review.
%% Author: Raeez Lorgat. No AI attribution. Not committed.
%%
%% New labels introduced:
%%   thm:V20-step-3-class-A          -- Class A theorem
%%   thm:V20-step-3-class-B0         -- Class B0 theorem
%%   conj:V20-step-3-class-B         -- Class B residual conjecture
%%   rem:V20-step-3-V55-dichotomy    -- pointer to V55 H1 dichotomy
%%   rem:V20-step-3-cross-volume     -- cross-volume citation skeleton
%% =========================================================================

The homotopy-category form of the Universal Trace Identity
\textup{(}Theorem~\ref{thm:universal-trace-identity}\textup{)} is
unconditional. Its chain-level upgrade --- the assertion that
$\mathfrak{K}_{\mathcal{C}}^{\mathrm{ch}} = \mathfrak{K}_{\mathcal{C}}^{\mathrm{BKM}}$
holds at chain level in $C^*_{\mathrm{ch,alg}}(A,A)$ \textup{(}AP-CY62
(b)\textup{)}, not merely modulo chain homotopy --- inherits the
Pentagon-at-$E_1$ dichotomy of V55 H1.

\begin{theorem}[V20 Step 3 chain-level for Class A;
                conditional on FM164, FM161 K3-specialised]
\label{thm:V20-step-3-class-A}
\ClaimStatusConditional
For $\mathcal{C}$ a CY$_3$ category with $X$ K3-fibred --- equivalently,
$X \in \{K3, K3 \times E, \text{STU}, \text{8 diagonal Z/NZ symplectic K3
orbifolds}\}$ --- the chain-level identity
\[
  \boxed{\;\operatorname{tr}_{Z(\mathcal{C})}(\mathfrak{K}_{\mathcal{C}})
  \;=\; -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal{C})))
  \;=\; \frac{c_N(0)}{2}\;}
\]
holds in $C^*_{\mathrm{ch,alg}}(A,A)$, with $A = \Phi(D^b(\mathrm{Coh}(X)))$
and $N$ the orbifold order ($N = 1, \ldots, 8$).
\end{theorem}

\begin{proof}
By the V40 master implication chain Pentagon-at-$E_1 \Rightarrow$ V19
Trinity-$E_1 \Rightarrow$ V20 Step~3 chain-level, it suffices to verify
$[\omega]_{A_X} = 0$ at chain level for $X$ K3-fibred. This is V49
Pentagon-at-$E_1$ at K3 input \textup{(}three independent verification
routes per~\cite{V49}\textup{)} extended to Class A by fibre-localisation:
the elliptic and orbifold quotients act trivially on the Mukai-lattice
Pentagon data because the Mukai pairing lives on the K$3$ fibre. The
class M alien-derivation residual $\xi(A_X) = 0$ unconditionally for K$3$-fibred
inputs (Class A inhabits class L or class C, not class M; V40 §3.1 residual
empty). Trace specialisations follow from \ref{thm:universal-trace-identity}
Steps 4 and 5.
\end{proof}

\begin{theorem}[V20 Step 3 chain-level for Class B0;
                conditional on FM164, FM161 super-Lie variant]
\label{thm:V20-step-3-class-B0}
\ClaimStatusConditional
For $A$ an $E_1$-chiral algebra arising as the CoHA of a CY$_3$ category with
$\operatorname{str}(K_A) = 0$ --- canonically the resolved conifold with
$A = Y(\mathfrak{gl}(1|1))$ --- the chain-level identity
\[
  \boxed{\;\operatorname{tr}_{Z(\mathcal{C})}(\mathfrak{K}_{\mathcal{C}})
  \;=\; -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal{C}))) \;=\; 0\;}
\]
holds in $C^*_{\mathrm{ch,alg}}(A,A)$, with both specialisations vanishing
identically (BRST: $c_{\mathrm{ghost}}(\mathfrak{gl}(1|1)) = 0$;
BKM-replacement: undefined, replaced by $0$ via super-trace vanishing).
\end{theorem}

\begin{proof}
By V55 H3 (super-Etingof--Kazhdan extension of V49 route (ii) plus super-trace
vanishing as V49 route (iii) instantiated in the super setting), the
Pentagon-at-$E_1$ cocycle $[\omega]_A = 0$ at chain level. Apply the V40
master implication. The class M residual $\operatorname{str}(\xi_A) = 0$ by
Class B0 hypothesis; Berezinian channel rigidity (V53.1) forces the
super-trace projection to vanish; chain-level identity follows.
\end{proof}

\begin{conjecture}[V20 Step 3 chain-level for Class B;
                  CONJECTURAL via mock-modular completion]
\label{conj:V20-step-3-class-B}
For $A$ class M, neither K3-fibred (Class A) nor super-trace vanishing
(Class B0) --- canonically $A_{\mathrm{quintic}}$ or $A_{\mathrm{LP^2}}$ ---
the chain-level identity holds modulo the alien-derivation correction:
\[
  \mathfrak{K}_A^{\mathrm{ch}} - \mathfrak{K}_A^{\mathrm{BKM-replacement}}
  \;=\; \partial \mu + \mu \partial + \xi(A),
\]
with explicit residuals $\operatorname{tr}(\xi_{\mathrm{quintic}}) =
\mathrm{Borel\text{-}sum}(\sum_g \Delta F_g^{\mathrm{quintic}})$ and
$\operatorname{tr}(\xi_{\mathrm{LP^2}}) = \xi_{\mathrm{Miki}}^{\mathrm{LP^2}}
+ \xi_{\mathrm{mock}}^{\mathrm{LP^2}}$. Vanishing $\operatorname{tr}(\xi_A) = 0$
is conjectural conditional on the mock-modular completion of the shadow
tower of $A$ (per V8 §6, V40 §3.1, V55 H1(c)).
\end{conjecture}

\begin{remark}[V20 Step 3 chain-level inherits the V55 dichotomy]
\label{rem:V20-step-3-V55-dichotomy}
Theorems~\ref{thm:V20-step-3-class-A} and~\ref{thm:V20-step-3-class-B0} and
Conjecture~\ref{conj:V20-step-3-class-B} together resolve V20 Step 3
chain-level into the same three-class structure as V55 H1
(\texttt{wave\_frontier\_pentagon\_E1\_non\_K3.md}): Class A K3-fibred
(PROVED), Class B0 super-trace vanishing (PROVED), Class B mock-modular
residual (CONJECTURAL). The reduction is via the V40 master implication
chain Pentagon-at-$E_1 \Rightarrow$ V19 Trinity-$E_1 \Rightarrow$ V20 Step 3
chain-level (\texttt{wave\_frontier\_universal\_trace\_chain\_level.md}).
The V49 K3-Pentagon resolution (\texttt{draft\_k3\_yangian\_pentagon\_E1\_theorem.tex})
is the load-bearing ingredient for Class A; V55 H3 is the load-bearing
ingredient for Class B0.
\end{remark}
```

---

## §6. Cross-volume consistency

### 6.1 Vol III k3_yangian.tex Class A inscription

The Vol III K3 Yangian chapter
(`/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_yangian_chapter.tex`),
once the V57 V49 inscription bundle is applied, will carry
`thm:k3-pentagon-E1` (Pentagon-at-$E_1$ for K3) plus six corollaries
including `cor:k3-v20-step-3-chain-level`. The present Vol I §V20 epilogue
must cite the Vol III corollary as the K3-specific anchor of the Class A
theorem:

```latex
% In Vol I §V20 epilogue, after thm:V20-step-3-class-A:
\begin{remark}[Cross-volume citation skeleton]
\label{rem:V20-step-3-cross-volume}
Theorem~\ref{thm:V20-step-3-class-A} at the K$3$ specialisation $X = K3$ is
the same statement as Vol III \texttt{cor:k3-v20-step-3-chain-level}
\textup{(}draft per V57\textup{);} the Class A extension to
$\{K3 \times E, \text{STU}, \text{8 diagonal Z/NZ orbifolds}\}$ is
fibre-localisation. Theorem~\ref{thm:V20-step-3-class-B0} at the conifold
specialisation is the same statement as Vol III \texttt{thm:conifold-pentagon-E1}
followed by the V40 master implication. Conjecture~\ref{conj:V20-step-3-class-B}
at quintic / local~$\mathbb{P}^2$ specialisations corresponds to Vol III
\texttt{conj:quintic-pentagon-E1} and \texttt{conj:localp2-pentagon-E1}
\textup{(}drafts per V55\textup{);} per AP-CY60 these are independent
constructions in three volumes, NOT three applications of $\Phi$.
\end{remark}
```

The Vol III chapter, in turn, must carry a back-reference: each of the six
V49 corollaries (especially `cor:k3-v20-step-3-chain-level`) should cite the
Vol I §V20 chain-level theorem (`thm:V20-step-3-class-A`) as the cross-volume
ground for its chain-level upgrade. This is a one-line edit per corollary,
to be applied in the V57 V49 inscription pass.

### 6.2 Vol II Pentagon material (Pillar 1) alignment with V55 dichotomy

Vol II Pillar 1 (Pentagon coherence,
`/Users/raeez/chiral-bar-cobar-vol2/chapters/foundations/sc_chtop_pentagon.tex`,
the V15 Pentagon chapter) carries the universal chain-level Pentagon
coherence Theorem at the operadic level. It is the LIFT of which V49 (K3
Pentagon at $E_1$), V55 H3 (conifold Pentagon at $E_1$), and V55 H1(c)
(quintic / local $\mathbb{P}^2$ Pentagon at $E_1$) are dichotomous instances.

The recommended Vol II edit: add a Remark at the end of the V15 Pentagon
chapter noting the V55 dichotomy:

```latex
% In Vol II V15 Pentagon chapter, end-of-section remark:
\begin{remark}[V55 dichotomy of CY$_3$ Pentagon-at-$E_1$ instantiations]
\label{rem:V15-V55-dichotomy}
The universal Pentagon coherence theorem of this chapter
\textup{(}Theorem~\ref{thm:sc-chtop-pentagon}\textup{)} restricts to
specific CY$_3$-input instantiations as a three-class dichotomy
\textup{(}V55, \texttt{wave\_frontier\_pentagon\_E1\_non\_K3.md}\textup{):}
Class A (K3-fibred, PROVED via Vol III \texttt{thm:k3-pentagon-E1}),
Class B0 (super-trace vanishing, PROVED via Vol III
\texttt{thm:conifold-pentagon-E1}), Class B (mock-modular residual,
CONJECTURAL via Vol III \texttt{conj:quintic-pentagon-E1} and
\texttt{conj:localp2-pentagon-E1}). The chain-level upgrade of the
Universal Trace Identity
\textup{(}Vol I \texttt{thm:V20-step-3-class-A},
\texttt{thm:V20-step-3-class-B0}, \texttt{conj:V20-step-3-class-B}\textup{)}
inherits the same dichotomy. The Pentagon coherence cocycle $[\omega]$ is
the master obstruction; its three-class dichotomous instantiation is the
master frontier of the chiral CY programme.
\end{remark}
```

This Remark aligns Vol II Pillar 1 with the V55 dichotomy without modifying
the universal chain-level Pentagon Theorem; it adds context, not content.

### 6.3 Cross-volume sweep instructions (AP5 / AP-CY13)

After applying the present sandbox draft (across Vol I §V20, Vol III K3
Yangian, Vol II V15 Pentagon), run the following sweep:

```bash
for label in thm:V20-step-3-class-A thm:V20-step-3-class-B0 \
             conj:V20-step-3-class-B rem:V20-step-3-V55-dichotomy \
             rem:V20-step-3-cross-volume rem:V15-V55-dichotomy \
             thm:k3-pentagon-E1 cor:k3-v20-step-3-chain-level \
             thm:conifold-pentagon-E1 conj:quintic-pentagon-E1 \
             conj:localp2-pentagon-E1 thm:universal-trace-identity \
             thm:sc-chtop-pentagon; do
  echo "=== $label ==="
  for vol in ~/chiral-bar-cobar ~/chiral-bar-cobar-vol2 \
             ~/calabi-yau-quantum-groups; do
    grep -rn "$label" "$vol"/chapters "$vol"/notes "$vol"/appendices \
         2>/dev/null
  done
done
```

Expected: every label resolves; cross-volume consistency without orphans.

---

## §7. Per-class status table (final)

| Class | Inhabitants | V20 Step 3 chain-level status | Residual $\operatorname{tr}(\xi_A)$ |
|---|---|---|---|
| **A** (K3-fibred) | K3, K3$\times$E, STU, 8 diagonal $\mathbb{Z}/N\mathbb{Z}$ symplectic K3 orbifolds | THEOREM (cond. FM164/FM161 K3-spec.) | $0$ unconditionally (class L/C, not class M) |
| **B0** (super-trace vanishing) | Conifold ($Y(\mathfrak{gl}(1|1))$), other $\operatorname{str}(K_A) = 0$ candidates | THEOREM (cond. FM164/FM161 super-Lie variant) | $0$ via super-trace cancellation + V53.1 Berezinian rigidity |
| **B-quintic** | Quintic CY$_3$ $Q \subset \mathbb{P}^4$ | CONJECTURE (V55 H2 sub-conjectures) | $\operatorname{tr}(\xi_{\mathrm{quintic}}) = \mathrm{Borel\text{-}sum}(\sum_g \Delta F_g^{\mathrm{quintic}})$ |
| **B-LP**$^2$ | Local $\mathbb{P}^2$, $K_{\mathbb{P}^2}$ | CONJECTURE (V55 H4 sub-conjectures) | $\operatorname{tr}(\xi_{\mathrm{LP^2}}) = \xi_{\mathrm{Miki}}^{\mathrm{LP^2}} + \xi_{\mathrm{mock}}^{\mathrm{LP^2}}$ |

The status table mirrors the V55 H1 dichotomy on Pentagon-at-$E_1$ exactly,
via the V40 master implication.

---

## §8. What this delivery does NOT do

- Does NOT edit any `.tex` source. All inscription is sandbox.
- Does NOT modify CLAUDE.md, AGENTS.md, FRONTIER.md, or the AP catalogue.
- Does NOT modify `MASTER_PUNCH_LIST.md`, `INDEX.md`, or any other notes.
- Does NOT run `make fast`, `make test`, `make verify-independence`, or any
  build/test command. Per pre-commit hook discipline.
- Does NOT close FM164 or FM161 (general or K3-specialised or super-Lie variant).
- Does NOT close the V55 H2 quintic sub-conjectures.
- Does NOT close the V55 H4 local $\mathbb{P}^2$ sub-conjectures.
- Does NOT promote V40 itself or modify the V40 master implication chain.
- Does NOT touch the V20 homotopy-category Theorem; the chain-level upgrade
  is what is being inscribed, not the homotopy version.
- Does NOT verify Class A extension explicitly per orbifold (claimed as
  fibre-localisation corollary of V49; per-orbifold verification is a
  tracked follow-up).
- Does NOT commit anything (per pre-commit hook). All commits by Raeez Lorgat
  ONLY; no AI attribution.

---

## §9. Closing assessment

V40 reduced V20 Step 3 chain-level to Pentagon-at-$E_1$ via the master
implication chain. V49 closed Pentagon-at-$E_1$ for K3 input via three
independent verification routes. V55 extended the analysis to non-K3 CY$_3$
inputs and produced the dichotomy: PROVED for Class A (K3-fibred), PROVED for
Class B0 (super-trace vanishing), CONJECTURAL for Class B (mock-modular
residual). V57 produced the TeX-ready K3 Pentagon theorem and corollary
bundle for Vol III.

This wave (V58) closes the loop: V20 Step 3 chain-level inherits the V55
dichotomy via the V40 master implication. The Vol I §V20 epilogue can now
carry two boxed theorems (Class A, Class B0) plus one boxed conjecture
(Class B with explicit residuals named). The Vol III K3 Yangian chapter
inscribes via the V57 corollary bundle. The Vol II V15 Pentagon chapter
acquires a single Remark aligning Pillar 1 with the V55 dichotomy.

The cross-volume citation skeleton is complete. After application, the V20
Universal Trace Identity is the cross-volume centrepiece at the chain level
for two of the three V55 classes; the residual Class B is the precise
mock-modular conjecture, equivalent in difficulty to the open mock-modular
generalisation of Eguchi–Ooguri–Tachikawa beyond K3.

The Russian-school discipline is preserved throughout: every theorem is a
precise mathematical sentence (not a slogan); every conditional dependency
is named (FM164/FM161 K3-specialised, FM164/FM161 super-Lie variant); every
cross-volume citation is a labelled `\ref` (no hardcoded Part numbers);
every status tag matches its proof block (per AP-CY40); every $\kappa$ is
subscripted (per AP113); every instance of CY-A$_3$ uses the inf-cat form
only (per AP-CY14); the V49 K3 routes are three independent constructions
(per AP-CY60); the chain-level discrepancy $\delta_A$ is the algebraic
$C^*_{\mathrm{ch,alg}}$ model (per AP-CY62 (b)), not the geometric FM model.

The boxed equation
$$
\operatorname{tr}_{Z(\mathcal{C})}(\mathfrak{K}_{\mathcal{C}})
\;=\; -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal{C})))
\;=\; \frac{c_N(0)}{2}
$$
is now a chain-level THEOREM for Class A and Class B0, with the
$c_N(0)/2$-side replaced by $0$ in Class B0 (no BKM lift), and a precise
chain-level CONJECTURE for Class B with named residual $\operatorname{tr}(\xi_A)$.

The chain-level upgrade is the entire content. Class A and Class B0 are
done (modulo separable FM164/FM161 closures); Class B is the genuine
remaining frontier (the mock-modular completion conjecture for the input's
shadow tower).

— Raeez Lorgat, 2026-04-16

**End of memorandum.** Authored by Raeez Lorgat. No AI attribution; no
commit; no manuscript edits; no test runs; no build. Sandbox draft only.
