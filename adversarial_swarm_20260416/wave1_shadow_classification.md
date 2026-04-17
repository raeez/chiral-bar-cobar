# Wave 1 — Adversarial Audit: Shadow Towers and the G/L/C/M Classification

**Target.** `standalone/shadow_towers.tex` (v1, 2318 ll), `shadow_towers_v2.tex` (782 ll, "Modular Koszul Duality and the Shadow Tower"), `shadow_towers_v3.tex` (4598 ll, "The Shadow Obstruction Tower"), `classification.tex` (1222 ll), `classification_trichotomy.tex` (518 ll), `N6_shadow_formality.tex` (704 ll), `computations.tex` (853 ll). Compute lib: `shadow_tower_ope_recursion.py`, `shadow_tower_recursive.py`, `conformal_block_shadow_integral_engine.py`, `virasoro_quartic_contact.py`, `feynman_bar_matching_engine.py`, `independent_verification.py`.
**Date.** 2026-04-16 — adversarial referee role.
**Tone.** Adversarial. The user wants the strongest correct version of every claim.

---

## Section 1. Triage of Major Claims

| # | Claim (locus) | Verdict | One-line attack |
|---|---|---|---|
| 1 | **Algebraicity of the shadow tower**: $H(t)^2 = t^4\,Q(t)$ with $Q$ quadratic, $H = t^2\sqrt Q$ (`shadow_towers_v3.tex` Thm 4.X; `v2` Thm 1.1(i); `classification.tex` §5) | **NEEDS-TIGHTENING** | Restated repeatedly, but the proof is recursive on the *primary line*. Off the primary line (multi-weight), this is *false*: see the cross-channel correction $\delta F_2(\mathcal W_3)\ne0$, which the manuscript itself documents. The "main theorem" elides this scope. |
| 2 | **Four-class partition $G/L/C/M$ exhausts the standard landscape** (`shadow_towers_v3.tex` §6, `classification.tex` Thm A, `N6_shadow_formality.tex` Cor 5.2) | **NEEDS-TIGHTENING** → likely WEAK at the boundary | The **single-line dichotomy** gives only $\{2,3,\infty\}$. Class C (`r_max = 4`) is grafted on by ad hoc "stratum separation". The proof that the gap *only* admits $\{0,1,2,\infty\}$ for algebraic depth (`shadow_towers_v3.tex` Prop 6.X "depth gap") is restricted to *standard-landscape*, *bosonic*, *single primary line* witnesses. Logarithmic / non-finite-type / triplet $\mathcal W(p)$ / admissible-level / fractional-level families are explicitly listed as **open**. |
| 3 | **$S_3(\mathrm{Vir}_c) = 2$ is $c$-independent** (`classification_trichotomy.tex` Thm 4.5; cross-cited `LorgatVirR`) | **SAFE** as a statement, **WEAK** as a "proof" inside the standalone file | The "proof" (`classification_trichotomy.tex` ll. 417–427) is the ratio $T_{(1)}T / T_{(3)}T = 2T/(c/2) \cdot \kappa(\Vir_c)/\kappa(\Vir_c) = 2$ — it does cancel $c$, but this is a one-line OPE coefficient extraction that *defines* $S_3$ on the Virasoro primary line. The "theorem status" upgrade is justified, but only because the underlying definition is a tautology (see issue 4). |
| 4 | **Shadow values $S_4 = 10/[c(5c+22)]$, $S_5,\ldots,S_8$ for Virasoro** (`classification.tex` (5.6)–(5.7); `shadow_towers_v3.tex` §A; `shadow_tower_ope_recursion.py`) | **WEAK / TAUTOLOGICAL** (AP-CY43, AP10) | All higher $S_r$ values come from the *same* MC recursion, and the engine `shadow_tower_ope_recursion.py` provides two "methods" — `mc_recursion_rational` and `sqrt_ql_rational` — that are mathematically the *same* identity ($H^2 = t^4 Q$ ↔ MC convolution). Their agreement is a sanity check on the implementation, not an independent verification. |
| 5 | **Shadow–formality identification** $\Sh_r = \ell_r^{(0),\text{tr}}$ (`N6_shadow_formality.tex` Thm 4.1) | **NEEDS-TIGHTENING** | The proof is induction with base $r=2,3,4$ and an inductive step "the trees are the same trees" (`N6_shadow_formality.tex` Step 3). The trees agreement is plausible but proven by gesture, not by a careful sign / weight comparison. There is no test against an *independently computed* $\ell_5^{(0),\text{tr}}$ via Kadeishvili–Merkulov on a specific dg Lie algebra (e.g. $L_\infty$ minimal model of polyvector fields on $\mathbb A^1$). |
| 6 | **Shadow-Feynman dictionary** "L-loop = $S_{L+1}$" (Vol III CLAUDE.md, asserted "PROVED"; not stated in this form in the standalone files surveyed) | **WEAK** at $L \ge 4$ (AP-CY43) | The Feynman side is computed via a recursion that internally invokes the shadow recursion; the loop = shadow identity is therefore tautological at $L \ge 4$. Vol III has independently verified $m_5$ via a 5-point Wick contraction; **Vol I has not done the analogous verification for $S_5$**. |
| 7 | **Trichotomy ↔ quadrichotomy resolution** (the standalone files oscillate: `shadow_towers_v3.tex` Thm 6.1 says "$r_{\max} \in \{2,3,\infty\}$"; `classification.tex` Def 5.1 says "$\{2,3,4,\infty\}$"; `classification_trichotomy.tex` titles itself "trichotomy" but enumerates *four* classes) | **WEAK** (terminology / scope mismatch) | The correct statement is: the **single-line shadow-metric dichotomy** is $\{2,3,\infty\}$; class C is **not** a single-line phenomenon. The papers should declare which classification (single-line vs. multi-stratum) is meant. |
| 8 | **Operator-order trichotomy** $k_{\max} \in \{0,1\}\cup\{3,4,\ldots\}$ with the gap at $k_{\max}=2$ (`classification_trichotomy.tex` Thm 4.1) | **NEEDS-TIGHTENING** | The proof excludes $k_{\max}=2$ by appealing to "bosonic locality" (half-integer weight excluded). The exclusion is genuine, but the theorem is *silently* restricted to bosonic algebras of finite type. Free fermion is *fermionic*; $N=2$ superconformal is *fermionic*; both have half-integer weights and break the gap. The statement should read "for bosonic chiral algebras with integer-spin generators". |
| 9 | **Fundamental relation $k_{\max} = p_{\max} - 1$** (`classification_trichotomy.tex` Prop 3.4) | **SAFE** (modulo notation) | This is the $d\log$ propagator weight. Two-line proof, no dependency. |
| 10 | **Class assignments** (Heisenberg=G, KM=L, $\beta\gamma$=C, Vir/$\mathcal W_N$=M) (`classification.tex` Tbl 6.1; `N6_shadow_formality.tex` §6) | **MIXED** | Heisenberg/KM/Vir: **safe**. $\beta\gamma$ as Class C: **NEEDS-TIGHTENING**, the assignment depends on a "stratum separation" ad hoc construct and cannot be derived from the single-line dichotomy. $\mathcal W(p)$, free fermion, lattice VOA: **WEAK** (see §4). |
| 11 | **Shadow growth rate $\rho$ → "the tower converges absolutely when $\rho<1$"** (`shadow_towers_v2.tex` (1.6); `shadow_towers_v3.tex` §11) | **WRONG** (or at best CONFUSED) | Vol III's AP-CY39 says class M is **Gevrey-1 / Borel summable, not convergent**. The Vol I file says "$S_r \sim \rho^r r^{-5/2}$, algebraic decay", which is *power-law-corrected exponential*, not factorial growth. But $S_r$ is not $F_g$. Conflating shadow-tower coefficient growth ($S_r$) with genus expansion growth ($F_g$) is a category error. The statement "shadow partition function is a resummation of factorially divergent string expansion converging on a domain" wants both at once. |
| 12 | **Universal factorization $S_r = \Delta\cdot R_r$ for $r\ge 4$** (`shadow_towers.tex` Thm 1.4(iv)) | **NEEDS-TIGHTENING** | Holds when $\sqrt Q$ is binomial-expanded around the *Gaussian envelope*, valid only when $(2\kappa+3\alpha t)^2$ is the dominant part. Fails when $\Delta$ and $\kappa$ have comparable magnitude (e.g., near a critical central charge). Stating "universal rational functions" without naming the field (where do the $R_r$ live?) is sloppy. |
| 13 | **Genus-2 cross-channel correction $\delta F_2(\mathcal W_3) = (c+204)/(16c)$** (`computations.tex` Thm 7.10; `shadow_towers_v2.tex` Thm 1.4) | **SAFE structurally**, **NEEDS-CHECKING** numerically | The graph-by-graph computation in `computations.tex` is explicit. The four nonzero amplitudes are consistent and add up correctly. But: every entry is "verified against the compute module `w3_genus2.py`", and the test value used is the *same arithmetic* — see §3. |

---

## Section 2. Per-Claim Detailed Analysis

### 2.1. Algebraicity ($H^2 = t^4 Q$): the "Riccati" theorem

**Claim** (`shadow_towers_v3.tex` Thm 4.1; abstract; `v2` Thm 1.1(i)): The weighted generating function $H(t) = \sum_{r\ge2} r\,S_r\,t^r$ on a primary line satisfies $H^2 = t^4\,Q(t)$ with $Q$ a fixed quadratic in $(\kappa,\alpha,S_4)$.

**Hypothesis the manuscript states.** "On a one-dimensional primary line $L \subset \Defcyc^{\text{mod}}(\cA)$ spanned by a single primary field $\eta$ of definite conformal weight."

**What is actually used.** The recursion (`shadow_tower_ope_recursion.py:85-115`) is *derived from* $H^2 = t^4 Q$ and gives identical numbers back. The *derivation* of $H^2 = t^4 Q$ is the MC equation projected to one-dimensional images; this is the genus-zero Maurer–Cartan recursion on a *scalar* lane. So "primary line" implicitly assumes:

  1. The lane has dimension exactly one (no off-diagonal tensor coupling).
  2. The conformal weight is *uniform* (no mixed-weight cross terms).
  3. The bracket $[-,-]$ closes on $L\otimes L \to L$ at every degree (not just at degree 2).

Hypothesis (3) is **non-trivial and not proved**. For a genuinely interacting algebra (e.g. $\mathcal W_3$ on a mixed $T+W$ lane), $[T,W]$ is a non-zero degree-1 bracket that does *not* close on a one-dimensional lane. The off-diagonal cross-channel correction $\delta F_2 = (c+204)/(16c)$ that `computations.tex` documents is direct evidence that the single-lane theorem fails as soon as the algebra has multiple primary fields — and this is acknowledged in the abstract of `shadow_towers_v2.tex`: "the multi-generator universality problem is resolved negatively".

**Strongest defense.** The theorem on the *single primary line* is correct: an MC recursion on a one-dimensional lane in a strict dg Lie algebra produces a quadratic generating identity, exactly as Riccati or Burgers reduces a hierarchy to two parameters. The proof in `shadow_towers.tex` ll. 944–1040 (lemma + closed form) is mechanically valid.

**Strongest attack.** As stated, the theorem reads as if it controls *the entire shadow tower of $\cA$*. It does not — it controls only one lane. The paper's own evidence (the `computations.tex` calculation for $\mathcal W_3$) shows the multi-lane object is *richer* than a single quadratic. Re-state the theorem as:

> *Single-line algebraicity.* For each one-dimensional primary lane $L$ closed under the genus-zero MC bracket, the lane-restricted generating function $H_L(t)$ satisfies $H_L(t)^2 = t^4\,Q_L(t)$ with $Q_L$ quadratic.

Then add a *non-vanishing-cross-term* corollary that says the global $\Theta_{\cA}$ is not a sum of single-lane Riccati data (witnessed by $\delta F_2(\mathcal W_3)$).

**Upgrade path.** State a multi-lane Riccati theorem: for each $k$-dimensional lane $L^{(k)}$ closed under brackets, the generating function $H_{L^{(k)}}$ satisfies a *system* of polynomial relations of total degree $2$ — a *quadric in $\mathbb P^k$*, not a binomial. This is the natural Annals-grade extension and would resolve the multi-generator universality problem positively at the level of *abstract structure* (the cross-channel correction sits inside the quadric). The matrix-Riccati framework of Eynard–Orantin is the natural tool.

### 2.2. The G/L/C/M classification: one trichotomy or two?

**The naming controversy.** `classification_trichotomy.tex` is *titled* trichotomy and announces "three regimes" $k_{\max}\in\{0,1,\ge3\}$, then in the very next section enumerates "the four shadow classes $G,L,C,M$". The two are **distinct** classifications:

- **Operator-order trichotomy**: by $k_{\max}$ (collision depth = OPE pole order minus one). Three values: $\{0,1,\ge3\}$, with $k_{\max}=2$ excluded by bosonic-integer-spin locality.
- **Shadow depth quadrichotomy**: by $r_{\max}$. Four values: $\{2,3,4,\infty\}$, with the value 4 reserved for class C.

These are two *different* invariants. The operator-order trichotomy is about *generator OPE poles*; the shadow depth is about *deformation tower truncation*. The $\beta\gamma$ system is the witness that they are not redundant: $(p_{\max},k_{\max},r_{\max})=(1,0,4)$.

The manuscript's confusion is partly historical (an earlier version had a true trichotomy $G/L/M$ on the single-line), partly real (the trichotomy/quadrichotomy distinction is genuine and underexplained).

**Strongest attack.** The reader is given two classifications under the same name. Section §5 of `classification.tex` declares "the single-line dichotomy" yielding the $\{G,L,C,M\}$ four-class partition; but `classification_trichotomy.tex` Thm 4.2 says the *single-line* dichotomy yields only $\{G,L,M\}$ (depth 2/3/$\infty$), and class C "escapes" by stratum separation. So is the four-class partition an axiom or a theorem? Currently it reads as an axiom (Definition 5.1 of `classification.tex`) with examples filled in.

**Upgrade path.** Cleanest restatement:

> *Theorem (Shadow Depth Trichotomy on a Primary Line).* For a chirally Koszul algebra and a one-dimensional primary lane with $\kappa\ne 0$, $r_{\max}|_L\in\{2,3,\infty\}$.
>
> *Theorem (Multi-Stratum Refinement).* For an algebra whose primary lanes are all in classes $G$ or $L$ ($\Delta=0$ on every lane) but admit a charged cross-stratum with non-vanishing quartic obstruction, $r_{\max}^{\text{global}} = 4$. This defines class C.
>
> *Conjecture (Exhaustion).* These are the only possibilities for finite-type bosonic chirally Koszul algebras.

This separates the *theorem* (single-line trichotomy) from the *refinement* (class C as a separate phenomenon) from the *open exhaustion conjecture*.

### 2.3. The $\beta\gamma$ class C assignment: the wobble

**The claim** (`classification.tex` Def 5.5; `shadow_towers_v3.tex` §6.2): $\beta\gamma$ is class C with $r_{\max}=4$ via "stratum separation": $\Delta=0$ on every primary lane, but the quartic contact invariant $S_4^{\text{cross}}\ne0$ lives on a charged stratum.

**Why this is uncomfortable.** The *single-line* analysis says $\beta\gamma$ has $\kappa = 6\lambda^2-6\lambda+1$ and $S_3=S_4=0$. By the dichotomy, this is class G (Gaussian). The class C label comes from a different stratum that the single-line theorem does not see. So:

1. The class C/G distinction for $\beta\gamma$ depends on which stratum one looks at.
2. The "shadow depth $r_{\max}=4$" is a *global* invariant in some unspecified sense.
3. The quartic contact $S_4^{\text{cross}}\propto(1-2\lambda)^2$ vanishes at $\lambda=1/2$ (symplectic boson) — does class C collapse to class G there? The papers do not address this.

**Strongest attack.** Class C is currently a *named exception*, not a derived structural class. The "exit by rank-one rigidity" argument (`shadow_towers_v3.tex` ll. 1306–1309, "the cross-channel self-bracket exits the two-field complex by dimensional constraint") is hand-waved. Where is the dimension count? What does "rank-one rigidity" mean for a rank-one bosonic ghost system? The argument as written is one sentence.

**Upgrade path.**

1. Write the *charged stratum* deformation complex explicitly: $\Defcyc^{\text{cross}}(\beta\gamma) = \mathrm{Hom}^\text{cyc}(B(\beta\gamma)|_{\text{charge}=q},\beta\gamma)$ with $q=\beta\otimes\gamma$ as the cross-charge, and compute its degree-5 cohomology (must vanish for $r_{\max}=4$ to hold).
2. State the assignment as $r_{\max}(\beta\gamma)=4$ *if and only if* a cross-stratum cohomology vanishes; verify this vanishing for $\lambda\ne1/2$ and explicitly handle $\lambda=1/2$.
3. Define class C *intrinsically*: an algebra is class C iff every single-line tower is class G or L *and* the global tower has $r_{\max}=4$ via cross-stratum quartic.
4. Prove no other algebra is class C (or describe the family of class C algebras).

### 2.4. Class M as "convergent / Borel"

The manuscript contains *two contradictory statements* about class M asymptotic behaviour:

- `shadow_towers_v3.tex` §11 (Outlook): "shadow tower converges ($S_r \sim \rho^r r^{-5/2}$, algebraic decay) while string amplitudes grow factorially".
- Vol III CLAUDE.md AP-CY39: "Class M is Gevrey-1, Borel summable, NOT convergent".

These are both about the *same* sequence ($S_r$ for Virasoro at generic $c$). One says $S_r \sim \rho^r$ (geometric decay), one says $S_r \sim r!$ (factorial growth). One must be wrong.

The Vol I claim follows from the Riccati form: $S_r = \frac{1}{r}[t^{r-2}]\sqrt{Q(t)}$ where $Q$ is a fixed polynomial. By analytic combinatorics (Flajolet–Sedgewick) the Taylor coefficients of $\sqrt{Q}$ at a square-root branch point have asymptotic $\sim \rho^n n^{-3/2}$, and $S_r \sim \rho^r/r \cdot r^{-3/2} = \rho^r r^{-5/2}$ — the Vol I claim is internally consistent *if* the Riccati theorem holds (and it does on a single line).

But Vol III speaks of a *different* sequence, namely the $A_\infty$ products $m_k$ on the Yangian/derived center side. Shadow tower coefficients $S_r$ ≠ $A_\infty$ products $m_k$. The *shadow-Feynman* dictionary "$L$-loop = $S_{L+1}$" mixes the two scales.

**Strongest attack.** The manuscript should clearly distinguish:

  - $S_r$: shadow tower, decays geometrically ($\rho < 1$ regime) — proved on the primary line.
  - $F_g$: free energies, grow factorially in genus.
  - $m_k$: $A_\infty$ products, growth depends on family.

The shadow-Feynman dictionary asserts $S_{L+1}$ equals an $L$-loop graph sum. If the LHS is geometric and the RHS is factorial, the dictionary is *false* at large $L$, OR the RHS is NOT the full string $F_g$ but a *coefficient* in $F_g$ that is geometric. Currently the manuscript trades on the ambiguity.

**Upgrade path.** Write a single explicit equality at $L=5$ (or any specific $L$): on the LHS, $S_6(\Vir_c)$ evaluated as a rational function; on the RHS, the genus-5 sum-of-graphs evaluated by an *independent* enumeration; show they agree as rationals. Without this, the dictionary is rhetoric.

### 2.5. Faber–Pandharipande coefficients

`classification.tex` Tbl 5.4 lists $\lambda_g^{\text{FP}} = (2^{2g-1}-1)/(2^{2g-1}) \cdot |B_{2g}|/(2g)!$ from the generating function $\hat A(i\hbar) - 1$.

**Independent check:** $\lambda_2^{\text{FP}} = 7/5760$ (table value). Compute directly:
- $g=2$: $(2^3-1)/2^3 = 7/8$, $B_4 = -1/30$, $|B_4| = 1/30$, $(2g)! = 24$.
- $\lambda_2 = (7/8)\cdot(1/30)/24 = 7/(8\cdot 30\cdot 24) = 7/5760$. ✓

This part is **safe**. The use elsewhere ($F_2 = \kappa\cdot 7/5760$ for single-generator algebras) is also safe.

**Subtle issue.** AP-CY19 in the Vol III CLAUDE.md warns that $\hat A(x) = (x/2)/\sinh(x/2)$ has convergence radius $2\pi$, not $\pi$. The Vol I file uses $\hat A(i\hbar)$ which gives $(\hbar/2)/\sin(\hbar/2)$ with first pole at $\hbar = 2\pi$ (consistent). No bug here, but worth tagging as an FM24-style trap to avoid in future edits.

### 2.6. The shadow-formality identification

`N6_shadow_formality.tex` Thm 4.1: $\Sh_r(\cA) = \ell_r^{(0),\text{tr}}(\Theta^{\le r-1},\ldots,\Theta^{\le r-1})$ at all $r\ge 2$.

The base cases are reasonable. The inductive step "Step 3: Tree formula equals shadow graph sum" (`N6_shadow_formality.tex` ll. 473–501) asserts that the trees (Stasheff) and the genus-zero stable graphs are *the same* combinatorial data with *matching weights*. The proof is one paragraph and rests on three claims:

  (a) "a genus-zero stable graph with $r$ external legs is a planar rooted tree $T\in\Trees_r$ with valences determined by the graph";
  (b) "the shadow propagator $P_\cA = \nabla_H^{-1}$ corresponds to the homotopy $h$";
  (c) "the vertex evaluation $\Sh_j = \pi\circ\ell_j^{(0)}\circ\iota^{\otimes j}$ corresponds to the vertex decoration".

**Attacks.**

- (a): True up to *isomorphism class* of trees. But genus-zero stable graphs come with a *cyclic* ordering at each vertex (from the Riemann surface), Stasheff trees do not. The statement requires fixing planar embeddings consistently, which the manuscript does not do.
- (b): "Corresponds" is doing a lot of work. The shadow propagator is constructed from $\nabla_H$, the homotopy from $D_A^2 = 0$. They live in different complexes a priori. The identification $h = P_\cA$ requires a choice of section.
- (c): The "vertex decoration" in the Kadeishvili–Merkulov tree formula is the *binary* bracket $[-,-]$ at every internal vertex. The "vertex evaluation" $\Sh_j$ is a *higher* bracket (degree $j$). They are not the same per-vertex datum.

This means Step 3 elides a serious matching theorem. The base cases verify *evaluations*, not the *combinatorial machinery*. The induction needs at minimum a precise statement of the bijection between tree data and stable-graph data, with signs.

**Upgrade path.** Either (i) cite Loday–Vallette §10.3 for the tree formula and explicitly verify that the chiral propagator equals the deformation-complex homotopy, or (ii) extract the identification from a known operadic-modular-graph theorem (e.g., Kontsevich–Manin, Getzler–Kapranov) and state which one is being applied.

### 2.7. The genus-2 W3 computation

`computations.tex` §7 computes $\delta F_2(\mathcal W_3) = (c+204)/(16c)$ via stable graph summation over the 7 stable graphs of genus 2. The computation is *explicit* and *checked at 7 values of $c$* against `w3_genus2.py`. This is the strongest computation in the standalone files surveyed.

**Independence audit.** The OPE coefficients $C_{TTT}=c$, $C_{TWW}=c$, $C_{WWT}=c$ are derived from $T_{(1)}T = 2T$, $T_{(1)}W = 3W$, $W_{(3)}W = 2T$ (`computations.tex` ll. 105–112). These three OPEs are standard $\mathcal W_3$ data. The propagators $\eta^{TT}=2/c$, $\eta^{WW}=3/c$ come from the per-channel $\kappa_T = c/2$, $\kappa_W = c/3$. The amplitudes are products of these, divided by $|\Aut|$.

The "verification against `w3_genus2.py`" is the same arithmetic recomputed. Per AP10, the test is **internally consistent but not independently verified**.

**Independent verification path.**

  1. Compute $F_2(\mathcal W_3)$ from a *direct* genus-2 conformal block calculation (e.g., via the Zhu-algebra recursion or chiral correlator factorization). This bypasses the Frobenius-algebra Feynman rules entirely.
  2. Compute $\delta F_2$ from the *Pixton-relation matching* on $\overline{\cM}_2$: the $\mathcal W_3$ MC equation should give a tautological relation; check membership in the strata algebra.

Until this is done, the (c+204)/(16c) value is *consistent within the framework* but not *cross-validated*.

---

## Section 3. Tautological-Test Audit

For each shadow value with a numerical "expected" value, I list (i) derivation source, (ii) test source, (iii) independence verdict.

| Quantity | Derivation source | Test source | Verdict |
|---|---|---|---|
| $\kappa(\Vir_c) = c/2$ | OPE $T_{(3)}T = c/2$, by definition | `conformal_block_shadow_integral_engine.S2_virasoro` returns `kappa_virasoro(c) = c/2`. Tests check against this. | **Tautological** as stated. Independent path: extract $c/2$ from the genus-1 character $Z_1(\Vir_c) = q^{-c/24}/\eta(\tau)$, comparing the leading $q$-power. The two derivations are honest-to-goodness disjoint. |
| $\kappa(\widehat{\fg}_k) = \dim(\fg)(k+h^\vee)/(2h^\vee)$ | Sugawara construction | Numerical evaluation at specific $\fg, k$ | **Independent**: this can be cross-checked against the Kac–Wakimoto character formula at $k=1$. The classification table (e.g. $\widehat{E}_8$ at $k=1$ giving $\kappa = 62 \cdot 31/15$) does not appear to have such a cross-check in the engine; it is a single-source hardcode. |
| $S_3(\Vir_c) = 2$ | $T_{(1)}T / T_{(3)}T = 2T/(c/2) = 4T/c$, projection to primary line drops the $T$, $\kappa$ in num/denom cancels → 2 | `S3_virasoro()` returns `Rational(2)` literal. | **Tautological**. Independent path: compute $S_3$ as the $A_\infty$ ternary bracket on the transferred minimal model. The Kadeishvili formula gives an unambiguous integer; if a separate code path produces 2, that is the genuine verification. The current "test" is a constant comparison. |
| $S_4(\Vir_c) = 10/[c(5c+22)]$ | Quartic contact via $\Lambda = :TT: - (3/10)\partial^2 T$, BPZ norm $\langle\Lambda\Lambda\rangle = c(5c+22)/10$, plus a 3-point coupling $C_{TT\Lambda}$ | `S4_virasoro(c)` returns `10/(c*(5c+22))` literal. | **Tautological in test, partially independent in derivation**. The derivation in `virasoro_quartic_contact.py` ll. 70–179 is an *honest computation* of the Gram matrix at level 4 in the vacuum module; it independently produces $5c+22$ in the numerator. So the value 10/[c(5c+22)] *can* be verified by a Gram matrix computation. But if I only see the engine code returning the literal, I cannot tell from the test side that the Gram matrix path was actually executed. **Recommendation:** add a test that runs the Gram-matrix computation symbolically and confirms the result equals $S_4$. |
| $S_5,\ldots,S_8(\Vir_c)$ | MC recursion from $(\kappa, S_3, S_4)$ via `mc_recursion_rational` | `sqrt_ql_rational` computes the same numbers via $\sqrt Q$ Taylor expansion. Tests assert agreement. | **Both paths identical algebraically**. The two methods are restatements of the same identity $H^2 = t^4 Q$ (the recursion is just the convolution form of the identity). Their agreement at every $r$ is a *consistency check on the implementation*, not an independent verification. **Independent path:** for $S_5$ specifically, compute the 5-point genus-0 conformal block of $T(z_1)\ldots T(z_5)$ on the Riemann sphere, extract the coefficient of the contact configuration, and verify against the value from MC. This is the analog of Vol III's $m_5 = 775/5184$ computation from a 5-point Wick contraction. **This has not been done in Vol I.** |
| $F_2(\mathcal W_3)$ scalar = $7c/6912$ | $F_2 = \kappa\cdot\lambda_2^{\text{FP}} = (5c/6)\cdot(7/5760)$ | Same arithmetic in `w3_genus2.py` | **Tautological in test**. Independent path: numerical sample-curve calculation of the genus-2 partition function (via spectral methods on Schottky covers). |
| $\delta F_2(\mathcal W_3) = (c+204)/(16c)$ | Sum of 4 graph contributions: $3/c + 9/(2c) + 1/16 + 21/(4c)$ | Same sum in `w3_genus2.py` evaluated at $c\in\{1,2,4,13,26,50,100\}$ | **Tautological in test, structurally independent in derivation**. Each graph amplitude is a *separate* Feynman computation with its own Frobenius-algebra contraction. So the seven test values across seven $c$'s constitute seven instances of "did I add the four amplitudes correctly?" but *do* span the rational-function structure. **Genuine independent verification still missing.** |
| $\lambda_g^{\text{FP}}$ for $g=1,2,3,4,5$ | Bernoulli formula $(2^{2g-1}-1)/2^{2g-1}\cdot|B_{2g}|/(2g)!$ | Same formula in `genus_tautological.py` | **Both paths identical**. Independent path: numerical integration of $\int_{\overline{\cM}_g}\psi_1^{2g-2}\lambda_g$ via Faber's algorithm. |
| Critical central charge $c^*\approx 6.125$ | Positive root of $5c^3+22c^2-180c-872=0$ | Numerical root finding | **Independent** (the cubic is fixed by the shadow metric, the root is solved numerically). |
| $\Delta(\Vir_c)+\Delta(\Vir_{26-c}) = 6960/[(5c+22)(152-5c)]$ | Direct calculation $40/(5c+22)+40/(152-5c) = 40\cdot 2(c-13)/[\ldots]$, which is *not* what is claimed; let me check. | Test against the formula | **NEEDS RE-DERIVATION.** $\frac{40}{5c+22}+\frac{40}{5(26-c)+22} = \frac{40}{5c+22}+\frac{40}{152-5c}$. Common denom $(5c+22)(152-5c)$, numerators $40(152-5c)+40(5c+22) = 40\cdot 174 = 6960$. ✓ The formula is correct. |

**Summary of tautology audit.**

- 6 of the 11 audited quantities have derivation/test paths that are algebraically identical (tautological).
- 2 have honest dual derivations (Gram matrix vs. recursion for $S_4$; per-graph Feynman vs. arithmetic for $\delta F_2$) but the test cross-validation is still circular.
- 3 are safe (Bernoulli formula; cubic root finding; the duality sum check).

The most important missing verification is **independent computation of $S_5(\Vir_c)$ from a 5-point conformal-block recipe**. Vol III did this for $m_5$. Vol I has not done it.

---

## Section 4. Class Assignments Table (Standard Examples)

| Family | Claimed class | Source | Verdict | Adversarial alternative |
|---|---|---|---|---|
| Heisenberg $\cH_k$ | G | `classification.tex` Tbl 6.1 | **SAFE** | None |
| Lattice VOA $V_\Lambda$ | G | `classification.tex` Tbl 6.1 | **NEEDS-CHECK** | The "primary line" for $V_\Lambda$ is the Heisenberg sublattice. Whether class M data appears on *non-primary* lines (e.g., from non-trivial cocycle) is not addressed. Niemeier lattices have non-trivial automorphism groups; whether $r_{\max}>2$ on charged sectors is open. |
| Free fermion $\psi$ | G | `classification.tex` Tbl 6.1 | **NEEDS-CHECK** | Free fermion is *fermionic*, half-integer weight, breaks bosonic locality of the operator-order trichotomy. The primary line analysis assumes bosonic. Result *probably* still G but the proof needs adjustment. |
| $bc$ ghosts (weight $\lambda$) | G | `classification.tex` Tbl 6.1 | **WRONG?** | $bc$ ghosts are the *Koszul dual* of $\beta\gamma$. If $\beta\gamma$ is class C, $bc$ should be class C too (Koszul duality preserves class via the conductor formula). But the table lists $bc$ as class G. **Inconsistency.** |
| Affine $\widehat\fg_k$ (any simple Lie $\fg$) | L | Tbl 5.2/6.1 | **SAFE** | None at non-critical level. At critical level $k=-h^\vee$, $\kappa=0$ and the single-line dichotomy fails. The class assignment at critical level is undefined. |
| $\beta\gamma$ at generic $\lambda$ | C | Def 5.5 | **NEEDS-TIGHTENING** | See §2.3. |
| $\beta\gamma$ at $\lambda=1/2$ (symplectic boson) | not addressed | — | **OPEN** | $S_4^{\text{cross}}\propto(1-2\lambda)^2$ vanishes here. Class might collapse to G, but the manuscript is silent. |
| Virasoro $\Vir_c$ | M (generic $c$) | Tbl 6.1 | **SAFE** for generic $c$ | Special points: $c=0$ ($\kappa=0$, breaks dichotomy), $c=-22/5$ ($S_4$ pole), $c=1/2$ (Ising, unitary), $c=13$ (self-dual). At $c=0$: trivial. At $c=-22/5$: critical, $S_4$ undefined. The classification needs caveats. |
| $\mathcal W_3$ (generic $c$) | M | Tbl 6.1 | **SAFE on $T$-line, NEEDS-PROOF on $W$-line** | The $W$-line has $S_3=0$ by $\mathbb Z_2$ parity. Single-line dichotomy gives class G or class C. The $W$-line $S_4$ is not computed in the standalone files. Class is genuinely ambiguous on $W$-line. |
| $\mathcal W_N$ for $N\ge 4$ | M | Tbl 6.1 | **SAFE on $T$-line, OPEN elsewhere** | Class is asserted to be inherited from $\Vir$ subalgebra. Higher-spin lines untested. |
| $\mathcal W(p)$ triplet algebras | not addressed | — | **OPEN** | These are *logarithmic*. Bar cohomology may not concentrate in degree 1 (chiral Koszul fails). Classification scheme as stated may not apply at all. The abstract `chirally Koszul` hypothesis would rule them out. Acknowledge or extend. |
| Symplectic fermion | not addressed | — | **OPEN** | Fermionic + logarithmic. Same issue. |
| $N=2$ superconformal | not addressed | — | **OPEN** | Half-integer weight. Operator-order trichotomy breaks. |
| Local $\mathbb P^2$ chiral algebra | not in the standalone landscape | (Vol III: class M) | **NOT IN SCOPE** for Vol I files. Vol III says class M (infinite depth). Cross-check possible but not done here. |
| K3 chiral algebra | not in scope | (Vol III) | **NOT IN SCOPE** |
| BFN Coulomb branches | not addressed | — | **OPEN** |
| Drinfeld–Sokolov $\mathcal W(\fg)$ for non-principal nilpotent | "M (inherits from Virasoro)" implicit | — | **NEEDS-CHECK** | Non-principal DS reductions have non-trivial ghost grading. The principal-only argument of the gravity primitivity theorem (`computations.tex` §8) does not extend. Class assignment for non-principal $\mathcal W$-algebras is open. |

**Pattern.** The table is **safe within the standard bosonic integer-spin Lie-theoretic landscape**, but the manuscript's claim of "all chirally Koszul algebras" or "the standard landscape" silently excludes everything else: logarithmic, fermionic, fractional level, non-principal $\mathcal W$, irrational. This scope restriction should be **explicit** in the theorem statements.

---

## Section 5. Consolidated Punch List (Ordered by Criticality)

1. **CRIT-1. Independent verification of $S_5(\Vir_c)$ missing (AP10).** Add a test that computes $S_5$ from a 5-point conformal block / Wick contraction, *without* invoking the MC recursion, and verifies agreement with the recursion-derived $S_5 = -48/[c^2(5c+22)]$. This is the analog of Vol III's $m_5 = 775/5184$ verification.

2. **CRIT-2. Class M asymptotics: contradictory statements.** Resolve `shadow_towers_v3.tex` §11 ("$S_r \sim \rho^r r^{-5/2}$, algebraic decay") vs. Vol III AP-CY39 ("class M is Borel summable, NOT convergent"). Distinguish $S_r$ behaviour from $F_g$ behaviour; state the shadow-Feynman dictionary precisely; verify at one specific genus.

3. **CRIT-3. Trichotomy/quadrichotomy terminology disaster.** Three standalone files use the word "trichotomy" while presenting four classes. Rewrite as: "Single-line shadow-depth trichotomy $\{2,3,\infty\}$ + Multi-stratum class C refinement $\to$ Quadrichotomy $\{2,3,4,\infty\}$".

4. **CRIT-4. $bc$ ghost class assignment inconsistency.** `classification.tex` Tbl 6.1 lists $bc$ as class G. But $bc$ is the Koszul dual of $\beta\gamma$, and Koszul duality should preserve class. Either $bc$ is class C, or the Koszul-preservation principle is wrong, or the $\beta\gamma$ class C assignment is wrong. **Pick one.**

5. **CRIT-5. Class C definition is structural ad-hoc-ery.** "Stratum separation" is invoked twice in different forms. Class C needs: (a) intrinsic structural definition independent of lane choice; (b) explicit cross-stratum cohomology computation; (c) handling of the symplectic boson degeneration $\lambda=1/2$.

6. **HIGH-1. Algebraicity scope.** The Riccati theorem $H^2 = t^4 Q$ holds *on a single primary lane* with closed bracket. Restate accordingly; flag the multi-lane case (cross-channel $\delta F_2$ for $\mathcal W_3$ already documents the failure).

7. **HIGH-2. Operator-order trichotomy bosonic-integer-spin restriction.** The exclusion of $k_{\max}=2$ uses $h\notin \mathbb Z + 1/2$. Add explicit hypothesis "for bosonic chiral algebras with integer-spin generators". Free fermion + $N=2$ supersymmetry break this and need separate treatment.

8. **HIGH-3. Shadow-formality identification, Step 3.** The "trees = stable graphs" matching in `N6_shadow_formality.tex` ll. 473–501 requires (a) cyclic-vs-planar order matching, (b) propagator-vs-homotopy identification, (c) higher-bracket-vs-binary-bracket clarification.

9. **HIGH-4. The MC ↔ $\sqrt{Q_L}$ "two methods" tautology.** `shadow_tower_ope_recursion.py` claims independence between `mc_recursion_rational` and `sqrt_ql_rational`. They are algebraically identical. Either rename `sqrt_ql_rational` as `mc_recursion_via_generating_function` (no claim of independence), or add a *third* genuinely independent method.

10. **MED-1. $\mathcal W_3$ $W$-line class is undetermined.** $S_3=0$ by $\mathbb Z_2$, $S_4$ not computed. Compute $S_4^W$ and assign class.

11. **MED-2. Lattice VOAs on charged stratum.** Niemeier and other non-Heisenberg lattice algebras have non-trivial cocycles; class G is asserted but only verified on the abelian Heisenberg lane.

12. **MED-3. Critical / fixed-point central charges.** Virasoro at $c=0$ ($\kappa=0$), $c=-22/5$ ($S_4$ pole), $c=13$ (self-dual): the dichotomy and table values need explicit handling.

13. **MED-4. Genus-2 $\delta F_2$ independent verification.** The 4-graph computation is internally consistent; cross-validate against either Pixton-relation matching or a numerical genus-2 partition function.

14. **MED-5. Logarithmic / fermionic / fractional / non-principal scope.** The "standard landscape" sweeps these under the rug. State the inclusion explicitly or write a "Limitations" remark naming each.

15. **LOW-1. The "descent fan" rhetoric (§3 of v3 outlook).** Three projections (categorical, spectral, modular) are advertised as descents of $\Theta_\cA$; the only proven case is lattice VOAs. State as conjecture.

16. **LOW-2. Pixton ideal generation conjecture.** "Whether the Virasoro MC tower generates the full Pixton ideal" is open. Don't claim "computational evidence at genera 2 and 3" without citing the engine that does the check.

17. **LOW-3. The depth gap proof for non-standard families.** `Proposition prop:depth-gap` says no value $\ge 3$ is realized. The proof is restricted to standard landscape. State "in the standard landscape" in the theorem itself.

18. **LOW-4. Faber–Pandharipande "are the genus-$g$ coefficients in $\hat A(i\hbar)-1$".** True; but $\hat A$ has convergence radius $2\pi$ — flag for AP-CY19 awareness (the manuscript does not currently note this).

---

## Section 6. Three Concrete Upgrade Paths (Annals-grade strengthenings)

### Upgrade Path A. **The Multi-Lane Riccati: a quadric in $\mathbb P^k$.**

*Status now.* Single-lane theorem $H^2 = t^4 Q$ with $Q$ quadratic. Multi-lane behavior treated as an *exception* (the $\delta F_2$ correction for $\mathcal W_3$).

*Upgrade.* For each $k$-dimensional sub-lane $L^{(k)}$ closed under the genus-zero bracket, prove that the *vector* of generating functions $(H_{L^{(k)},i})_{i=1}^k$ satisfies a *system* of polynomial relations of total degree 2 — i.e., the moduli of shadow data lies on a *quadric variety in $\mathbb P^{k+2}$*. The single-line case is the rank-1 quadric $H^2 = t^4 Q$.

For $\mathcal W_3$ on the $k=2$ lane $\langle T,W\rangle$, this would replace the per-channel Riccati with a $2\times 2$ matrix-Riccati. The cross-channel correction $\delta F_2 = (c+204)/(16c)$ should be computable as the off-diagonal entry of the matrix-quadric Hessian.

*Why it is Annals-grade.* This unifies the algebraicity theorem with the multi-generator universality result. It connects the single-line Riccati to the matrix-Riccati framework of Eynard–Orantin topological recursion. It would resolve the multi-generator universality problem positively (as a *quadric-variety statement*) rather than negatively (as an "exception").

### Upgrade Path B. **Shadow-Feynman dictionary, sharp form.**

*Status now.* "L-loop = $S_{L+1}$" is an asserted dictionary. At $L\ge 4$ both sides are computed via the same recursion (AP-CY43).

*Upgrade.* State the dictionary as an *equality of generating functions*:
$$
F(\hbar,\cA) - F^{(0)}(\hbar,\cA) = \int_0^\infty H_\cA(\hbar t)\,K(t)\,dt
$$
for an explicit kernel $K$ (Borel transform), where $F$ is the genus expansion and $H_\cA$ is the shadow generating function. Then prove that the asymptotic expansion of the integral matches the genus expansion of $F$ term by term, using a single explicit verification at $L=5$ (independent computation of the 5-loop graph sum vs. the value of $S_6$).

*Why it is Annals-grade.* This establishes a Borel resummation principle for chiral string amplitudes, directly connecting the algebraicity of the shadow tower (geometric decay of $S_r$) to the factorial divergence of the $F_g$ series.

### Upgrade Path C. **Class C as intrinsic, with a complete classification.**

*Status now.* Class C is defined ad hoc via "stratum separation" with $\beta\gamma$ as the unique example.

*Upgrade.* Define class C as: a chirally Koszul algebra is class C iff every primary lane is in class G ∪ L *and* the global cyclic deformation complex $\Defcyc(\cA)$ has $H^2$ supported in *exactly one* charge sector with non-zero quartic obstruction. Then:

1. Prove that this intrinsic definition agrees with $r_{\max}^{\text{global}}=4$.
2. Classify all class-C algebras: show that class C is realized exactly by *bosonic ghost systems* (rank-one $\beta\gamma$, $bc$ at any conformal weight) and possibly free-field cosets thereof.
3. Treat the symplectic-boson degeneration $\lambda=1/2$: prove class C collapses to class G there iff the $\mathfrak{sp}(2)$-symmetry forces $S_4^{\text{cross}}=0$, and verify by explicit computation.
4. Prove $bc$ is class C (resolve CRIT-4 by the *correct* identification: class C is preserved by Koszul duality).

*Why it is Annals-grade.* Removes an ad-hoc class from a clean classification theorem and replaces it with a structural characterization. The resulting "complete G/L/C/M classification of bosonic chirally Koszul algebras of finite type" becomes a satisfying termini.

---

## Final adversarial summary

The shadow-tower programme has a strong single-line theorem (the Riccati algebraicity), a clean operator-order trichotomy, and an honest computation of $\delta F_2(\mathcal W_3)$. It also has:

- A naming problem (trichotomy vs. quadrichotomy) that confuses the reader.
- An ad-hoc class C grafted onto a clean dichotomy/trichotomy.
- A test infrastructure that is heavily tautological (two "methods" that are the same identity in disguise).
- Inconsistencies between Vol I and Vol III on class M asymptotics (convergent vs. Borel).
- Silent restriction to bosonic, integer-spin, finite-type, standard-landscape algebras dressed as universality.
- An $S_3(\Vir_c)=2$ "theorem" whose proof in the standalone file is a one-line OPE coefficient ratio.
- A shadow-formality identification (`N6_shadow_formality.tex`) whose inductive step elides a serious tree-vs-graph matching theorem.

None of these issues *invalidate* the core algebraicity theorem on a single primary line. They reflect the gap between "true on the canonical example" and "publication-grade theorem with stated hypotheses". The three upgrade paths in §6 turn the current set of partial results into a coherent Annals-grade story.

The single highest-leverage action: **independently verify $S_5(\Vir_c)$ from a 5-point Wick contraction or genus-0 conformal block calculation**, mirroring the Vol III $m_5$ verification. This single computation would convert the entire MC-recursion-derived $\{S_5,S_6,\ldots\}$ tower from a tautology into a verified sequence.
