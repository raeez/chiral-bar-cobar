# Wave 7 — Adversarial audit of Vol I example chapters

**Scope.** `chapters/examples/{bershadsky_polyakov, beta_gamma, free_fields, kac_moody, heisenberg_eisenstein, level1_bridge, landscape_census}.tex` and the cross-referenced `standalone/bp_self_duality.tex`, `standalone/koszulness_fourteen_characterizations.tex`. Read-only audit (no edits, no commits). Methodology: AP126 (r-matrix level prefix), AP136 (harmonic numbers), AP39 (κ-formula taxonomy), AP4 (proof / claim alignment), AP-CY55 / AP55 / AP153 / AP155 (E_n scope, label/content, narration), AP151 (convention clash), and first-principles arithmetic verification of every displayed numerical step.

The headline finding: the example chapters are not the origin of the BP arithmetic bug, the βγ/bc complementarity bug, or the wrong central charge. **The chapters are mostly internally correct**; the bugs propagate from the *standalone* writeups (`standalone/bp_self_duality.tex` line 327 arithmetic; `standalone/koszulness_fourteen_characterizations.tex` line 1298 wrong c(k)) and from a **direct contradiction between the level-1 bridge chapter and the master κ table in landscape_census** that has gone uncaught for ≥ 12 commits. Fixing the standalones and reconciling the level-1 row of the census closes most of the wave-1 / wave-2 / wave-3 punch-list against this part of the landscape.

---

## §1. BP chapter audit

### §1.1 Central-charge formula

`chapters/examples/bershadsky_polyakov.tex` Eq. (eq:bp-central-charge) line 149-151 states
\[
c(k) \;=\; 2 - \frac{24(k+1)^2}{k+3}.
\]
This is the Fehily-Kawasetsu-Ridout (FKR) convention, cross-referenced to `\cite{FKR20}`.
- Verification at $k=-3/2$: $c = 2 - 24(1/4)/(3/2) = 2 - 4 = -2$. Matches the triplet value documented in line 167.  ✓
- Verification at $k=-1$: $c = 2 - 0 = 2$. (Trivial pole; admissible.)
- Verification at $k=-5$: $c = 2 - 24(16)/(-2) = 2 + 192 = 194$. Matches the gap structure described in remark `rem:bp-conductor-comparison` (line 248-252: "$c \le 2$ for $k > -3$ and $c \ge 194$ for $k < -3$").  ✓

Convention warning at lines 170-182 (Remark `rem:bp-convention`) is **honest and correct**: it documents a parallel formula $(k-15)/(k+3)$ that does **not** apply, gives a mismatch test at $k=-3/2$, and points at the compute module that uses each convention. This is exactly the discipline AP4 calls for.

**Verdict §1.1: Clean. Use this as a template for κ formulas in other example chapters.**

### §1.2 The wrong c(k) elsewhere

`standalone/koszulness_fourteen_characterizations.tex` line 1298 still carries the **wrong** central charge for BP:
\[
c(k) \;=\; \frac{(k-1)(6k+1)}{k+3} \qquad \text{(WRONG)}.
\]
- Test at $k=-3/2$: $(k-1)(6k+1)/(k+3) = (-5/2)(-8)/(3/2) = 20/(3/2) = 40/3 \neq -2$. **Disagrees with the triplet value the BP chapter uses to vindicate FKR**.
- Test at $k=0$: $(-1)(1)/(3) = -1/3$. The FKR formula gives $2 - 24/3 = -6$.

So this file is using a third convention different from both candidates the BP chapter discusses. In the BP chapter (line 280-282) the alternate is $c = 2 - 3(2k+3)^2/(k+3)$, which at $k=0$ gives $2 - 3\cdot 9/3 = -7$, not $-1/3$ either. So `koszulness_fourteen_characterizations.tex` line 1298 is genuinely wrong (it is not a re-parametrisation; it disagrees with **all** documented conventions at $k=-3/2$ and $k=0$).

**FIRST-PRINCIPLES analysis.**
- Ghost theorem: All three formulas are quadratic-in-k rational functions with a simple pole at $k=-3$ (as required: BP degenerates at the critical level $k=-h^\vee = -3$). They *can* be reconciled if and only if they differ by a constant or by a Sugawara-style additive shift.
- Precise error: The three rational functions disagree even at $k=-3/2$, so they are *different* mathematical objects, not different normalisations. The koszulness-14 formula is a fabricated-looking rational, plausibly transcribed from a paper that uses a different generator ordering.
- Correct relationship: only FKR ($c = 2 - 24(k+1)^2/(k+3)$) matches the triplet limit at $k=-3/2$.

**Action item (heal-not-downgrade):** Replace line 1298 with $c(k) = 2 - 24(k+1)^2/(k+3)$ and cite `\cite{FKR20}`. The Koszul-conductor downstream should then become $K_{\mathrm{BP}} = 196$ (matching the BP chapter), not whatever $K$ the wrong $c$ produces.

### §1.3 BP arithmetic Eq. 3.5 (signed DS sum)

The arithmetic bug **is in `standalone/bp_self_duality.tex` lines 315-329**, not in `bershadsky_polyakov.tex`. The standalone reads:

> the $T$-generator (weight 1) contributes $+1$, each $G^\pm$-ghost pair (weight $3/2$) contributes $-2/(3/2) = -4/3$, and the $J$-generator (weight $2$) contributes $+1/2$. The result is
> \[\varrho_{\cB} = 1 - \tfrac{4}{3} - \tfrac{4}{3} + \tfrac{1}{2} = \tfrac{1}{6}.\]

Two distinct errors compound:

(a) **Wrong weight assignment.** The standalone says $T$ has weight 1 and $J$ has weight 2. The BP chapter (lines 99-108, the canonical definition) is the standard FKR convention: $T$ weight 2, $J$ weight 1, $G^\pm$ weight 3/2.

(b) **Wrong arithmetic.** Even granting the standalone's inverted weight assignment, the displayed sum
\[
1 - \tfrac{4}{3} - \tfrac{4}{3} + \tfrac{1}{2} \;=\; \tfrac{6 - 8 - 8 + 3}{6} \;=\; -\tfrac{7}{6} \quad\not=\quad +\tfrac{1}{6}.
\]
Verified by direct rational arithmetic.

(c) **The two errors cancel.** Using the **correct** weights from the BP chapter (T=2, J=1, G±=3/2) and the signed contribution formula
\[
\rho \;=\; \sum_{\text{bosons}} \frac{1}{h} \;+\; \sum_{\text{fermions}} \frac{-1}{h}
\]
yields
\[
\frac{1}{1} + \frac{1}{2} - \frac{2}{3} - \frac{2}{3} \;=\; \frac{6 + 3 - 4 - 4}{6} \;=\; \frac{1}{6}.
\]
So the **answer** $\rho = 1/6$ is correct (matching the BP chapter line 268 and the principal-vs-minimal complementarity $\rho_{\mathrm{BP}} + \rho_{\mathcal{W}_3} = 1/6 + 5/6 = 1$). But the **proof shown in the standalone** is wrong on two counts that happen to compensate.

**FIRST-PRINCIPLES analysis.**
- Ghost theorem: The signed contribution formula $\rho = \sum_{\mathrm{bos}} 1/h - \sum_{\mathrm{ferm}} 1/h$ for non-principal DS reductions is real (it is the cyclic-trace specialisation of the genus-1 universality theorem applied to the strong-generator weight spectrum).
- Precise error: The standalone applied the formula with weights swapped (T↔J), then wrote down a sum that does not arithmetic-evaluate to its claimed value, and the two errors cancel because $1/2 + 1/1 = 3/2 = 1 + 1/2$ (the bosonic contributions are unchanged under T↔J swap), but the fermionic contributions $-2 \cdot 1/(3/2) = -4/3$ are unchanged under T↔J because they only depend on the G± weights (not T/J). So the sum is the same up to ordering; the displayed sum is wrong because someone wrote $1 - 4/3 - 4/3 + 1/2$ when they meant $+1 + 1/2 - 2/3 - 2/3$ (different terms). The standalone wrote the four terms with the bosonic contributions taken as $1/h$ (giving $1/1$ and $1/2$) and the fermionic contributions taken as $2/(3/2) = 4/3$ (giving $-4/3, -4/3$): wait — that should be $-2/(3/2) = -4/3$ for each G±, but there are TWO G± so two copies of $-4/3$. Bosonic sum $1 + 1/2 = 3/2$; fermionic sum $-4/3 - 4/3 = -8/3$. Total: $3/2 - 8/3 = 9/6 - 16/6 = -7/6$. So the displayed sum is **arithmetically** $-7/6$, NOT $1/6$.

  The fix is *not* the arithmetic; it is the formula: the contribution of a fermionic generator at weight $h$ should be $-1/h$ (one fermion contributes $-1/h$, **not** $-2/h$). The "factor 2" the standalone put on the G± contributions ($-2/(3/2)$ each) is wrong. With the corrected formula:
  \[
  \rho = +\frac{1}{1} + \frac{1}{2} - \frac{1}{3/2} - \frac{1}{3/2} = 1 + \frac{1}{2} - \frac{2}{3} - \frac{2}{3} = \frac{6+3-4-4}{6} = \frac{1}{6}. \quad ✓
  \]
- Correct relationship: The signed contribution formula is one boson per generator at weight h contributes $+1/h$; one fermion at weight h contributes $-1/h$. The "$-2/(3/2) = -4/3$ each" in the standalone is mis-derived (perhaps confusing weight-vs-spin or spinor-pair vs single fermion).

**Action item:** Rewrite the standalone arithmetic with the **correct formula** (one fermion contributes $-1/h$, not $-2/h$) and the **correct weights from the BP chapter** (T=2, J=1, G±=3/2). The answer $\rho = 1/6$ stands.

### §1.4 Self-dual point κ(BP_{-3}) = 49/3

The BP chapter line 247-252 (rem:bp-conductor-comparison) and the standalone line 605-615 say the BP self-dual central charge is $c_{\mathrm{sd}} = K/2 = 98$, attained only at complex level $k = -3 \pm 2i$. **The user's prior finding "κ(BP_{-3}) = 49/3 is principal-value mean across pole" needs un-packing.**
- At $k = -3$ (critical level), $c(k) = 2 - 24(-2)^2/0 = 2 - 96/0$. Pole.
- Principal-value mean: $\lim_{\epsilon \to 0} \tfrac{1}{2}[c(-3+\epsilon) + c(-3-\epsilon)]$. Compute:
  - $c(-3+\epsilon) = 2 - 24(\epsilon-2)^2/\epsilon \approx -96/\epsilon + 96 + O(\epsilon)$ (dominant pole, sign).
  - $c(-3-\epsilon) = 2 - 24(-\epsilon-2)^2/(-\epsilon) \approx +96/\epsilon + \dots$
  - Mean: regular part is $96 + 2$ approximately; cancelling the pole gives a finite limit. Direct computation: $\tfrac{1}{2}[c(-3+\epsilon) + c(-3-\epsilon)] = 2 - 12\big[(\epsilon-2)^2/\epsilon - (\epsilon+2)^2/\epsilon\big] = 2 - 12 \cdot (-8\epsilon)/\epsilon = 2 + 96 = 98$. So the **principal-value mean is $c = 98$**, hence $\kappa = c/6 = 98/6 = 49/3$.

This is exactly the value the BP chapter would predict at the formal self-dual locus. The user's prior wave finding is correct: the value 49/3 lives at $k = -3$ only as a principal-value across the pole, not as a regular function value. The chapter does not state this explicitly.

**Action item (upgrade path).** Add a remark in `bershadsky_polyakov.tex` (or in `bp_self_duality.tex`) recording the principal-value identity $\lim_{\epsilon \to 0^+} \tfrac{1}{2}[c(-3\pm\epsilon)] = 98$. This makes the "self-dual point at complex level" statement (currently asserted via $k = -3 \pm 2i$) precise as a real-line phenomenon: the genuine Cauchy principal value at the critical pole is exactly the formal self-dual central charge.

### §1.5 Conductor K = 196 polynomial identity

BP chapter Proposition `prop:bp-self-duality` lines 209-218 verifies the conductor identity. The proof is a direct algebraic manipulation:
\[
c(k) + c(-k-6) = 4 + \tfrac{24[(k+5)^2 - (k+1)^2]}{k+3} = 4 + \tfrac{24 \cdot 8(k+3)}{k+3} = 4 + 192 = 196. ✓
\]
Verified independently: $(k+5)^2 - (k+1)^2 = (k^2 + 10k + 25) - (k^2 + 2k + 1) = 8k + 24 = 8(k+3)$. ✓ The "bring the second term over a common denominator with sign flip" step is correct because $-k - 3 = -(k+3)$ and the minus signs cancel from the squared numerator.

**Verdict §1.5: Clean.**

### §1.6 BP Summary

- The BP **chapter** itself is internally consistent, uses the correct FKR formula, and gives the correct conductor identity.
- The BP **standalone** has a wrong displayed signed-sum (right answer, wrong arithmetic, wrong contribution formula, swapped weights).
- The koszulness-14 standalone has a wrong $c(k)$ formula at line 1298.
- The 49/3 self-dual κ is correct as a principal-value statement, but this is not made explicit anywhere.

---

## §2. βγ chapter + free fields audit

### §2.1 βγ central charge formula

`chapters/examples/beta_gamma.tex` Theorem `thm:beta-gamma-stress` line 304-316:
\[
c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1), \qquad c_{bc} = 1 - 3(2\lambda-1)^2 = -2(6\lambda^2 - 6\lambda + 1).
\]
- Sanity: $c_{\beta\gamma} + c_{bc} = 0$. Always. So the **conductor** $K = c + c' = 0$. ✓
- Special values (line 318-330, comp:beta-gamma-central-charges):
  - $\lambda = 2$, $c_{bc} = 1 - 3(3)^2 = -26$: bosonic string ghosts. ✓
  - $\lambda = 1/2$, $c_{bc} = 1$: complex fermion pair. ✓
  - $\lambda = 1/2$, $c_{\beta\gamma} = -1$: symplectic bosons. ✓ (since $6 \cdot 1/4 - 3 + 1 = -1/2$, $c = 2 \cdot (-1/2) = -1$).
  - $\lambda = 0$ or $1$: $c_{\beta\gamma} = 2$. ✓

**Verdict §2.1: Clean.**

### §2.2 βγ kappa formula and AP39

The chapter says (Proposition `prop:betagamma-obstruction-coefficient`, line 1208-1221):
\[
\kappa(\beta\gamma) = c_{\beta\gamma}/2 = 6\lambda^2 - 6\lambda + 1.
\]
And $\kappa(bc) = c_{bc}/2 = -(6\lambda^2 - 6\lambda + 1)$, so $\kappa(\beta\gamma) + \kappa(bc) = 0$ exactly.

**AP39 cross-check.** AP39 says "$\kappa = c/2$ ONLY for Virasoro-rank-1." That is a Vol I rule about which family has *natively* the identity $\kappa = c/2$. βγ is **two-generator**, not Virasoro. So either:
(a) AP39 is too narrow (it forgot to enumerate βγ/bc), and the universal formula is "$\kappa = c/2$ for Virasoro AND for the βγ/bc family"; or
(b) The chapter's $\kappa(\beta\gamma) = c/2$ is an over-extension.

Resolving from first principles: the genus-1 obstruction coefficient $\kappa$ is the trace anomaly's coefficient against $\lambda_1$. For *any* two-field free system with stress tensor $T = (1-\lambda)\beta\partial\gamma - \lambda\partial\beta\gamma$, the Virasoro central charge is $c = \pm 2(6\lambda^2 - 6\lambda + 1)$. The genus-1 partition function carries the conformal anomaly with coefficient $c/12$ in $\partial_\tau \log Z$ (line 1195). Then $\kappa = c/2$ follows from the universality theorem **whenever** the algebra is "Virasoro-driven" at genus 1, which is the case here because the bar curvature picks up only the conformal anomaly.

So: AP39 should be amended to read "$\kappa = c/2$ for any algebra whose genus-1 bar curvature is exhausted by the Virasoro stress-tensor anomaly", which includes Vir, βγ, bc, free fermion at $\lambda = 1/2$ (one fermion: $c = 1/2$, $\kappa = 1/4$ — see free_fields.tex line 174). It does NOT include the Heisenberg ($\kappa = k$, NOT $c/2 = 1/2$ at $k=1$), KM (κ from dim·(k+h^v)/(2h^v)), or W-algebras with $\rho \ne 1/2$ (e.g. W_3 has $\rho = 5/6$).

**FIRST-PRINCIPLES analysis.**
- Ghost theorem: there is a universal "Virasoro-only-anomaly" subclass within free-field algebras for which $\kappa = c/2$, separate from the rank-driven Heisenberg/KM formulas.
- Precise error: AP39's enumeration ("Heis_k: κ=k, Vir: κ=c/2, KM: κ=dim(g)(k+h^v)/(2h^v)") is incomplete — it omits the βγ/bc family and the free fermion. These are not Virasoro but they share Virasoro's universal κ=c/2 because their genus-1 anomaly is purely conformal.
- Correct relationship: the universal taxonomy is *anomaly source*, not *family name*. Algebras whose bar curvature comes only from Virasoro stress-tensor anomaly satisfy $\kappa = c/2$. Algebras with additional source (KM double-pole carries $k\delta^{ab}$ that is not absorbed by the Sugawara $T$) don't.

**Action item:** Strengthen AP39 to add βγ, bc, free fermion. Add a rationale clause: "$\kappa = c/2$ for free-field Virasoro-anomaly-only algebras".

### §2.3 βγ/bc complementarity at λ=1/2 and λ=2

User's prior claim: "$\kappa(\beta\gamma) + \kappa(bc) = 0$ should fail at $\lambda = 1/2$ or $\lambda = 2$."

Direct verification:
- $\lambda = 1/2$: $\kappa(\beta\gamma) = 6(1/4) - 3 + 1 = -1/2$; $\kappa(bc) = +1/2$. Sum = 0. ✓
- $\lambda = 2$: $\kappa(\beta\gamma) = 24 - 12 + 1 = 13$; $\kappa(bc) = -13$. Sum = 0. ✓

The complementarity sum **is zero everywhere** in this chapter. The prior wave's "sum ≠ 0" finding was apparently a misidentification, or it was about a *different* sum (perhaps the conductor $c + c'$? — but that is also 0, see §2.1).

**Verdict §2.3: No bug. Prior wave finding was wrong.**

### §2.4 βγ r-matrix vs free_fields.tex contradiction

`chapters/examples/free_fields.tex` line 41-46 says the βγ modular Koszul triple has
\[
r(z) = 0.
\]
`chapters/examples/beta_gamma.tex` line 2819-2825 says the βγ r-matrix is
\[
r(z) \;=\; \sum_{n,m \ge 0} (-1)^n \binom{n+m}{m} \frac{\psi_n \otimes X_m - X_n \otimes \psi_m}{z^{n+m+1}}.
\]
These are not the same object. The reconciliation is the "$d\log$-absorption" remark in `heisenberg_eisenstein.tex` line 270-281: there is a "pre-extraction r-matrix" (the OPE itself) and a "post-extraction r-matrix" (after $d\log$ absorption). The βγ system has a simple-pole OPE; one $d\log$ absorption sends $1/z \mapsto 1/z^0 = 1$ (constant), which is what the free_fields chapter calls $r(z) = 0$ (no pole).

But the βγ chapter formula is *not* the post-$d\log$ r-matrix; it is the **rational coupling on the Koszul dual generators**, which has poles at all orders $1/z, 1/z^2, \ldots$ from the binomial sum.

**FIRST-PRINCIPLES analysis.**
- Ghost theorem: there are at least two distinct things called "the βγ r-matrix" in this manuscript: (i) the post-$d\log$ collision residue (zero for βγ); (ii) the formal Koszul-dual coupling $\sum (-1)^n \binom{n+m}{m} (\psi_n \otimes X_m - X_n \otimes \psi_m)/z^{n+m+1}$.
- Precise error: free_fields.tex calls (i) "$r(z)$" and beta_gamma.tex calls (ii) "$r(z)$". Both use the same notation for different objects.
- Correct relationship: rename or scope. (i) is the **collision** r-matrix; (ii) is the **dual-coupling** r-matrix or "Drinfeld-style r-matrix on $A^! \otimes A^!$".

**Action item:** introduce notation $r_{\mathrm{coll}}(z)$ vs $r_{\mathrm{dual}}(z)$ in both chapters and the modular Koszul triple definition. Or rename one of them. Currently they are just called $r(z)$ in both places.

### §2.5 Free fermion κ = 1/4 (consistency with AP39)

`free_fields.tex` lines 173-174, 230, 287-291: $\kappa(\mathcal{F}) = c/2 = 1/4$, with $c_\mathcal{F} = 1/2$. Matches §2.2 amended AP39.

The "$\rho = 1/2$ for single-generator algebras" justification (line 260) is the same Virasoro-only-anomaly argument. ✓

### §2.6 Free fermion class assignment via shadow tower

`free_fields.tex` Proposition `prop:fermion-shadow-invariants` (line 221-298) computes:
- $\kappa = 1/4$ (verified above)
- $S_3 = 0$ (fermionic antisymmetry kills cubic; verified by cube-root-of-unity argument lines 263-274)
- $S_4 = 0$ (consequence of $S_3 = 0$ via cubic gauge triviality)
- Class G, $r_{\max} = 2$.

This satisfies AP-CY12 (class assignment from full shadow tower computation, not generator counting). ✓

### §2.7 Triple-redundancy of free-field exactness (AP155 audit)

free_fields.tex remark `rem:free-fields-three-pillar` (line 93-126) describes free-field exactness in three pillars:
(i) strict homotopy chiral algebra ($j'_n = 0$)
(ii) formal convolution $sL_\infty$ ($\ell_k^{tr} = 0$)
(iii) classical FM compactification (no nodal divisor insertions).

The remark says "Free-field archetypes are the unique family where Pillar B is formal and Pillar C is classical simultaneously." This is strong language — but reading carefully, the three pillars are **manifestations** of the same underlying mechanism (no simple-pole OPE at high arity), not three independent theorems.

**AP155 risk.** Marketing this as "three independent confirmations" inflates evidence. Cache entry 52 explicitly flags this as ONE mechanism projected three ways.

**Verdict §2.7:** the chapter does not directly assert "three independent confirmations" — it says "Pillar B formal AND Pillar C classical simultaneously", which is closer to a one-mechanism statement. The wording is borderline. Suggested rewrite: "the underlying mechanism — absence of simple-pole OPE — manifests as Pillar B formality and Pillar C classicality simultaneously" makes the singularity explicit and avoids AP155.

---

## §3. KM chapter audit (AP126 r-matrix table)

### §3.1 r-matrix formulas in `kac_moody.tex`

Every r-matrix formula in `kac_moody.tex` carries an explicit level prefix or denominator:

| Line | Formula | Level dependence |
|------|---------|------------------|
| 92 | $r(z) = \Omega/((k+h^\vee) z)$ | denominator $k+h^\vee$ (KZ normalisation) |
| 114 | same | same |
| 743 | same | same |
| 1772 | same | same |
| 2080 | same | same |
| 2098 | $r(z) = \Omega/((k+2)z)$ | sl_2 specialisation |
| 2332 | same | same |
| 2361 | same | same |
| 3420 | $r(z) = \Omega/((k+h^\vee) z)$ | well-defined except at $k=-h^\vee$ |
| 5495 | same | same |
| 5641 | same | same |

**AP126 cross-check.** AP126 says $r(z) = k\Omega/z$ with verification "$k=0 \Rightarrow r = 0$." Here $r(z) = \Omega/((k+h^\vee) z)$. At $k=0$: $r(z) = \Omega/(h^\vee z) \neq 0$.

This is **the KZ normalisation**, not the bare classical r-matrix. The two are related by a rescaling: $r_{\mathrm{KZ}}(z) = r_{\mathrm{class}}(z)/(k+h^\vee)$. AP126's "classical r-matrix has level prefix" applies to the **bare** classical r-matrix on the loop algebra; the **KZ** normalisation absorbs the level shift into the denominator.

**FIRST-PRINCIPLES analysis.**
- Ghost theorem: there are two natural normalisations for the affine KM r-matrix: (i) bare classical $r_{\mathrm{class}}(z) = k\Omega/z$ (zero at critical level by construction); (ii) KZ normalisation $r_{\mathrm{KZ}}(z) = \Omega/((k+h^\vee) z)$ (singular at critical level; recovers KZ equations directly).
- Precise error: AP126 is *about* (i), but the kac_moody chapter uses (ii) throughout. Neither is wrong; they answer different questions. The chapter should state which.
- Correct relationship: $r_{\mathrm{KZ}} = r_{\mathrm{class}}/(k(k+h^\vee))$ (modulo a numerical factor). At $k=0$, both formulas have a simple-pole behaviour, but $r_{\mathrm{class}}(0) = 0$ while $r_{\mathrm{KZ}}(0) = \Omega/(h^\vee z)$.

**Verdict §3.1:** Not an AP126 violation, but a missing convention statement. The chapter should add a remark naming the convention as "KZ normalisation", contrast with the bare classical r-matrix, and note that AP126's $k=0$ test applies to the bare normalisation only. Computation `comp:sl2-collision-residue-kz` (line 2089-2099) explicitly says "Casimir r-matrix governing the KZ equation" — so the convention IS named there. Other occurrences should backfill the convention name.

### §3.2 Sugawara construction and $(k+h^\vee)$ normalisation

`kac_moody.tex` line 524 has the curvature
\[
m_0 = \frac{k+h^\vee}{2h^\vee} \cdot \kappa
\]
where $\kappa$ here is the *Casimir element* (not the modular characteristic — notation clash with the $\kappa$ used elsewhere; see AP151 risk below). At $k = -h^\vee$, $m_0 = 0$: the curvature vanishes at critical level, which matches the AP126 spirit (level prefix kills the curvature).

**AP151 violation alert.** In this chapter, $\kappa$ is used for both:
- the Killing form on $\mathfrak{g}$ (lines 364, 391, 405, 411-413, 417, etc.);
- the Casimir element $\sum J^a \otimes J_a$ (line 526);
- the modular characteristic $\kappa(\widehat{\mathfrak{g}}_k)$ (line 5, 12, 62, 87, etc.).

These are three different objects sharing the symbol $\kappa$. The Killing form is a bilinear form on $\mathfrak{g}$; the Casimir is an element of $U(\mathfrak{g}) \otimes U(\mathfrak{g})$ (or its dual); the modular characteristic is a scalar invariant of the chiral algebra. The reuse is standard in physics literature but creates AP151 risk: any reader not tracking which $\kappa$ is which can confuse the Casimir with the modular characteristic, especially in the formula $m_0 = ((k+h^\vee)/2h^\vee) \cdot \kappa$ where the RHS $\kappa$ is the Casimir but the LHS would be a modular invariant if read naively.

**Action item:** rename one of the three. Standard fixes: $\kappa_{\mathrm{Kill}}$ for the Killing form; $C$ or $\Omega$ for the Casimir (the chapter already uses $\Omega = \sum \kappa^{ab} I_a \otimes I_b$ at line 736, 755 — so just use $\Omega$ throughout); reserve $\kappa$ for the modular characteristic.

### §3.3 KM kappa formula at all levels

Line 135, 173, 268, 1313: $\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$.

AP39 cross-check: matches the AP39 entry for KM. ✓

**Sanity tests:**
- sl_2 ($\dim = 3$, $h^\vee = 2$) at $k=1$: $\kappa = 3 \cdot 3/4 = 9/4$. Matches landscape_census L615. ✓
- D_4 ($\dim = 28$, $h^\vee = 6$) at $k=1$: $\kappa = 28 \cdot 7/12 = 49/3$. Matches landscape_census L623. ✓
- E_8 ($\dim = 248$, $h^\vee = 30$) at $k=1$: $\kappa = 248 \cdot 31/60 = 7688/60 = 1922/15$. Matches landscape_census L633. ✓
- At critical level $k = -h^\vee$: $\kappa = 0$. ✓

**Verdict §3.3:** Clean.

### §3.4 Critical level handling

The chapter says (line 179, 526, 710-712) that at $k = -h^\vee$, $\kappa = 0$ and the bar complex is uncurved. The Feigin-Frenkel center emerges as the degree-zero cohomology (line 1278-1280 in landscape_census). ✓

---

## §4. Heisenberg-Eisenstein audit

### §4.1 Notation clash: κ as both level and characteristic

`heisenberg_eisenstein.tex` opens with $\mathcal{H}_\kappa$ (Heisenberg of level $\kappa$), then says "Modular characteristic $\kappa(\mathcal{H}_\kappa) = \kappa$". The level is denoted $\kappa$ AND the modular characteristic is $\kappa$. This is the AP151/V2-AP14 risk in pure form: same symbol for two distinct numerical quantities that *happen to be equal*.

The equality is true (Heisenberg level = modular characteristic, by AP39's "Heis_k: κ=k"), so substituting one for the other doesn't change values. But:
- A reader correcting an algebraic step might propagate the level into the modular-characteristic position (or vice versa) when they should not.
- Comparison across chapters becomes confusing: in landscape_census $\mathcal{H}_k$ is used (level $k$), here $\mathcal{H}_\kappa$ (level $\kappa$).

**Action item:** rename to $\mathcal{H}_k$ throughout this chapter, parallel to the rest of the manuscript. Reserve $\kappa$ for the modular characteristic. The identity $\kappa(\mathcal{H}_k) = k$ then becomes a theorem statement, not a definition trivially true.

### §4.2 r-matrix formula

Line 27, 41, 252: $r(z) = \kappa/z$. With $\kappa = $ Heisenberg level, this is $r(z) = k/z$, which **does** satisfy AP126's $k=0 \Rightarrow r = 0$ test. ✓

**FIRST-PRINCIPLES analysis.**
- Ghost theorem: the Heisenberg r-matrix is genuinely the "level-prefixed" object that AP126 cares about; in this case the level IS named $\kappa$ but it is the loop-algebra level $k$.
- Precise error: none mathematically; only notation.
- Correct relationship: $r(z) = k/z$ is the bare classical r-matrix on the abelian loop algebra; no KZ rescaling.

### §4.3 Curved vs linear

The user flagged "Heisenberg ordered bar: linear or curved?" The chapter is unambiguous: the bar complex is *curved* with curvature $m_0 = k \cdot \omega_g$ at genus $g$ (line 564-568). At $k=0$ the bar complex is *uncurved* (line 298). So:
- Generic $k \ne 0$: curved.
- $k = 0$: uncurved.

The "linear vs curved" dichotomy is resolved by level: linear at $k = 0$, curved otherwise.

The Koszul dual is $\mathcal{H}_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$ with curvature $m_0 = -k \cdot \omega_1$ (line 297). So both $\mathcal{H}_k$ and $\mathcal{H}_k^!$ are curved with **opposite** curvatures, summing to zero (free-field complementarity).

**Verdict §4.3:** Internally consistent; "linear" is a degenerate level, not a separate algebra.

### §4.4 Eisenstein series identification

Line 50-60: the Eisenstein series enter as Taylor coefficients of the genus-$g$ Green's function near the diagonal. Specifically, $E_4, E_6$ at genus 2 (line 525). At genus 1, the propagator picks up $E_2$ via $\theta_1'/\theta_1$ (cf. beta_gamma.tex line 1185, 1195).

**AP156 audit (Weierstrass P_1 convention).** The chapter writes $\theta_1'(z|\tau)/\theta_1(z|\tau)$ — this is the **logarithmic derivative of theta_1** convention (option (a) of AP156), not the Weierstrass $\zeta$ option (b). They differ by $-2\eta_1 z$. The chapter does not state which convention it uses; the formula at heisenberg_eisenstein.tex L52-60 shows the Taylor expansion $G(z,w) = \log(z-w) + \sum c_k (z-w)^{2k}$ with $c_k = G_{2k}$ (Eisenstein). This is consistent with the Weierstrass-zeta convention IF we interpret $G_{2k}$ as the "non-holomorphic Eisenstein" but the chapter says "Eisenstein series" without specifying.

Cross-check beta_gamma.tex L1280-1287:
\[
P^{(1)}(z,w|\tau) = \theta_1'(z-w|\tau)/\theta_1(z-w|\tau) = 1/(z-w) - (\pi^2/3) E_2(\tau)(z-w) + O((z-w)^3).
\]
The leading behaviour $1/(z-w)$ at the diagonal matches the genus-0 propagator. The $E_2$ correction with coefficient $-\pi^2/3$ is the standard Weierstrass-zeta-vs-theta-log-derivative shift. This is convention (a): $\theta_1'/\theta_1$.

**Verdict §4.4:** The chapter uses convention (a) (theta-log-derivative) consistently in beta_gamma and heisenberg_eisenstein. Should be stated explicitly per AP156.

### §4.5 Modular property explicit?

Line 489: "anomaly = $-6c\kappa/(\pi i) \cdot z_{12}$" — this is a B-cycle monodromy defect at genus 1.

Is the modular S-transformation explicit? The chapter computes $F_1 = \kappa/24$ (line 28, 567-568, etc.) and identifies it with the genus-1 free energy. The modular property $F_1$ transforms with weight 0 under $SL_2(\mathbb{Z})$ is implicit (genus-1 partition function modular invariance) but not proved in this chapter. It is delegated to genus-universality theorem.

---

## §5. Census table cross-check

### §5.1 Level-1 KM contradiction

This is the **biggest finding of this wave.**

`level1_bridge.tex` Proposition `prop:level1-kappa-reduction` (line 208-225) **proves** that
\[
\kappa(\widehat{\mathfrak{g}}_1) = \mathrm{rank}(\mathfrak{g}) \quad \text{(NOT $\dim(\mathfrak{g})(1+h^\vee)/(2h^\vee)$).}
\]
The chapter explicitly **lists the disagreement** at line 169-200:

| g | $\kappa^{\mathrm{KM}}$ | $\kappa^{\mathrm{lat}}$ | $c$ |
|---|---|---|---|
| sl_2 | 9/4 | 1 | 1 |
| sl_3 | 16/3 | 2 | 2 |
| D_4 | 49/3 | 4 | 4 |
| E_6 | 169/4 | 6 | 6 |
| E_7 | 2527/36 | 7 | 7 |
| E_8 | 1922/15 | 8 | 8 |

The chapter says "the lattice value is correct; the KM formula overcounts" (line 200-206).

**But `landscape_census.tex` lines 615-633 use the KM (overcounting) values for the level-1 table** — exactly the column the level-1 bridge chapter tells the reader is wrong.

This is the level-1 reduction bug propagated into the census. Either:
- (a) the level-1 bridge chapter is right (rank reduction at $k=1$), and the census should use `\kappa = rank`;
- (b) the census is right (KM formula at all levels), and the level-1 bridge chapter is over-claiming.

**Tracing the dispute.** The level-1 bridge chapter reasoning (line 227-269): at $k=1$ simply-laced, FKS identifies root currents $E_\alpha$ as composites of the Heisenberg generators; only the rank Heisenberg generators contribute to the bar curvature; the simple-pole structure constants $f^{abc}$ become exact (coboundaries) by lattice realisation. So $\kappa = \mathrm{rank}$.

The KM formula reasoning: at generic level, the KM formula is derived from the OPE of all $\dim\mathfrak{g}$ currents *treated as independent*. At $k=1$ the currents are no longer independent.

**Resolution:** the level-1 bridge chapter is right, **provided** the bar curvature calculation reduces consistent with FKS. The census table is wrong (uncritically applying the generic-level formula at $k=1$).

**Action item (HIGH PRIORITY):** Fix the level-1 row of `landscape_census.tex` lines 615-633. Replace each $\kappa$ with $\mathrm{rank}(\mathfrak{g})$:
- $\widehat{\mathfrak{sl}}_{2,1}$: $\kappa = 1$ (not 9/4)
- $\widehat{\mathfrak{sl}}_{3,1}$: $\kappa = 2$ (not 16/3)
- $\widehat{D}_{4,1}$: $\kappa = 4$ (not 49/3)
- $\widehat{E}_{6,1}$: $\kappa = 6$ (not 169/4)
- $\widehat{E}_{7,1}$: $\kappa = 7$ (not 2527/36)
- $\widehat{E}_{8,1}$: $\kappa = 8$ (not 1922/15)

Then the corresponding $F_1 = \kappa/24$ and $F_2 = 7\kappa/5760$ values must be recomputed.

For non-simply-laced types ($B_2$, $C_2$, $G_2$, $F_4$), the level-1 bridge chapter says (line 457-473) that FKS does **not** apply and $\kappa$ remains $\dim(\mathfrak{g})(1+h^\vee)/(2h^\vee)$. So the census rows for $B_2$, $C_2$, $F_4$, $G_2$ remain unchanged.

### §5.2 BP self-dual κ in census

Census line 705: "$\mathcal{W}_3, T$-line; $\mathcal{W}_3, W$-line" — does it have a BP row?

(Search by Grep) — the census table at L686-715 does not include a BP row. The BP row should be added to keep the census comprehensive. Reading the comparison table at `bershadsky_polyakov.tex` line 437-454, BP row should be:
- $c$: $2 - 24(k+1)^2/(k+3)$
- $\kappa$: $c/6$
- $\rho$: $1/6$
- Class: M (mixed: T-channel ∞, J-channel G)
- $K_{\mathrm{BP}} = 196$
- $\kappa + \kappa' = 98/3$

### §5.3 Internal consistency of complementarity sums

| Algebra | $\kappa$ | $\kappa + \kappa'$ | Check |
|---------|----------|-------------------|-------|
| Heisenberg $\mathcal{H}_k$ | $k$ | $0$ | $\mathcal{H}_k$ self-dual under $k \to -k$. ✓ |
| Free fermion | 1/4 | 0 | $\mathcal{F}^!$ has $\kappa = -1/4$ ✓ (free_fields L480-483) |
| βγ ($\lambda$) | $6\lambda^2 - 6\lambda + 1$ | 0 | bc partner. ✓ |
| bc ($\lambda$) | $-(6\lambda^2 - 6\lambda + 1)$ | 0 | βγ partner. ✓ |
| KM $\widehat{\mathfrak{g}}_k$ (k generic) | $\dim(g)(k+h^\vee)/(2h^\vee)$ | 0 | Feigin-Frenkel involution $k \to -k - 2h^\vee$. ✓ |
| Vir | $c/2$ | 13 | $\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c}) = c/2 + (26-c)/2 = 13$ ✓ |
| W_3 | $5c/6$ | 250/3 | $\kappa + \kappa' = 5c/6 + 5(100-c)/6 = 500/6 = 250/3$ ✓ (with K=100) |
| BP | $c/6$ | 98/3 | $\kappa + \kappa' = c/6 + (196-c)/6 = 196/6 = 98/3$ ✓ |
| Monster | 12 | 13 | Sum recorded as 13 (Vir-sector value) ✓ |

All consistent. The BP entry should be added to the census table.

---

## §6. First-principles analyses (cache-write-back targets)

### §6.1 BP signed contribution formula (cache new entry 53)

**Wrong claim:** "Each fermion at weight $h$ contributes $-2/h$ to the anomaly ratio."

**Ghost theorem:** For a non-principal DS reduction with strong generators of weight $\{h_i\}$ and parity $\{\epsilon_i\}$ (boson +1, fermion -1), the anomaly ratio satisfies
\[
\rho = \sum_i \epsilon_i / h_i.
\]

**Precise error:** The factor 2 in the standalone bp_self_duality.tex L319 ($-2/(3/2) = -4/3$) is wrong. Each *individual* fermionic generator contributes $-1/h$, not $-2/h$.

**Correct relationship:** For BP with T(2), J(1), G^+(3/2), G^-(3/2):
\[
\rho_{\mathrm{BP}} = +1/2 + 1/1 - 1/(3/2) - 1/(3/2) = 1/2 + 1 - 2/3 - 2/3 = 1/6. ✓
\]

**Cross-check via principal exponents.** For W_3 (principal sl_3, exponents $\{1, 2\}$), $\rho = 1/2 + 1/3 = 5/6$. With BP being the "complementary" reduction (minimal sl_3), $\rho_{\mathrm{BP}} + \rho_{\mathrm{W_3}} = 1$ gives $\rho_{\mathrm{BP}} = 1/6$. ✓

### §6.2 βγ "kappa = c/2 for non-Virasoro" (cache new entry 54)

**Wrong claim (AP39 too narrow):** "$\kappa = c/2$ ONLY for Virasoro."

**Ghost theorem:** For algebras whose genus-1 bar curvature is exhausted by Virasoro stress-tensor anomaly (no additional KM-style double pole, no rank-driven shift), $\kappa = c/2$.

**Precise error:** AP39 enumerated only Heis, Vir, KM. Missed βγ, bc, free fermion. These are not Virasoro but they share its "$\kappa = c/2$" formula.

**Correct relationship:** The formula $\kappa = c/2$ holds when:
- Algebra has a Virasoro stress tensor;
- The Sugawara-style normalisation absorbs the entire double-pole anomaly.

Includes: Vir, bc, βγ, free fermion. Excludes: Heisenberg ($\kappa = k = c$, the level-rank coincidence at rank 1 makes $\kappa \ne c/2$), KM (extra $\dim(g)(k+h^\vee)/(2h^\vee)$ structure), W-algebras with $\rho \ne 1/2$.

**Action item:** Strengthen AP39. Add a "Virasoro-anomaly-only" subclass.

### §6.3 Level-1 κ reduction (cache new entry 55)

**Wrong claim (in landscape_census L615-633):** "$\kappa(\widehat{\mathfrak{g}}_1) = \dim(\mathfrak{g})(1+h^\vee)/(2h^\vee)$ at $k=1$ simply-laced."

**Ghost theorem:** The KM formula $\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$ is correct **only** when the $\dim(\mathfrak{g})$ currents are independent generators of the bar complex.

**Precise error:** At $k=1$ simply-laced, FKS realises root currents as composites $E_\alpha = Y(e^\alpha, z)$ of the rank Heisenberg generators. The bar complex factors through the lattice weight filtration; only the rank generators contribute. The generic-level formula overcounts.

**Correct relationship:**
\[
\kappa(\widehat{\mathfrak{g}}_1) = \mathrm{rank}(\mathfrak{g}) \qquad \text{(simply-laced)},
\]
\[
\kappa(\widehat{\mathfrak{g}}_1) = \dim(\mathfrak{g})(1+h^\vee)/(2h^\vee) \qquad \text{(non-simply-laced; FKS not applicable)}.
\]

**Action item:** Census table needs row-by-row correction at the level-1 ADE entries.

### §6.4 r-matrix scoping (cache new entry 56)

**Wrong claim:** "βγ has $r(z) = 0$" (free_fields.tex L46) AND "βγ has $r(z) = \sum_{n,m} \cdots$" (beta_gamma.tex L2819) — same symbol, different objects.

**Ghost theorem:** There are at least two distinct objects called "the r-matrix" in this manuscript:
- (i) Collision r-matrix $r_{\mathrm{coll}}(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta)$, post-$d\log$ absorption.
- (ii) Dual-coupling r-matrix $r_{\mathrm{dual}}(z) \in A^! \otimes A^![[z, z^{-1}]]$, the formal Drinfeld-style coupling on the Koszul dual.

**Precise error:** Same notation $r(z)$ for both.

**Correct relationship:** They differ by one $d\log$ absorption (lowering pole order by 1) AND by being valued in different spaces ($A \otimes A$ vs $A^! \otimes A^!$).

**Action item:** Introduce notation $r_{\mathrm{coll}}$ and $r_{\mathrm{dual}}$ globally.

### §6.5 KM r-matrix two normalisations (cache new entry 57)

**Wrong claim (AP126 form):** "KM r-matrix is $k\Omega/z$, vanishing at $k=0$."

**Ghost theorem:** The "bare classical" r-matrix on the loop algebra $L\mathfrak{g}$ is $r_{\mathrm{class}}(z) = k\Omega/z$ (vanishing at $k=0$). The "KZ-normalised" r-matrix governing the KZ equation on the WZW model is $r_{\mathrm{KZ}}(z) = \Omega/((k+h^\vee) z)$ (singular at critical level).

**Precise error:** AP126 demands the bare normalisation; the KM chapter uses the KZ normalisation. Both are correct in their own scope, but should be distinguished.

**Correct relationship:** $r_{\mathrm{KZ}}(z) = (1/(k+h^\vee)) \cdot r_{\mathrm{class}}(z)/k = \Omega/((k+h^\vee) z)$ (when $k \ne 0$).

**Action item:** Strengthen AP126 to enumerate both normalisations, OR have the KM chapter explicitly tag every formula as "KZ-normalised".

---

## §7. Three upgrade paths (heal-not-downgrade)

### Upgrade path 1 — AP39 strengthening: the Virasoro-anomaly-only subclass.

**Statement:** Define the *Virasoro-anomaly-only subclass* $\mathcal{V}$ to be chiral algebras whose genus-1 bar curvature equals the conformal anomaly of their Virasoro stress tensor. Then $\kappa = c/2$ for every $\mathcal{A} \in \mathcal{V}$. The class $\mathcal{V}$ contains: $\mathrm{Vir}_c$, $bc_\lambda$, $\beta\gamma_\lambda$, free fermion, $\mathcal{F}^!$. It does NOT contain: $\mathcal{H}_k$ ($\kappa = c$, not $c/2$), $\widehat{\mathfrak{g}}_k$ (extra KM structure), $\mathcal{W}_N$ for $N \ge 3$ (extra higher-spin contributions, $\rho > 1/2$).

**Mechanism:** The bar curvature $m_0 = \kappa \cdot \omega_g$ at genus $g$ extracts the conformal anomaly of $\partial_\tau \log Z = (\pi i c/12) E_2$ at genus 1. When this is the *only* source of curvature, $\kappa = c/2$. Additional sources (KM double-pole structure, higher-spin self-OPEs, lattice sublattice rank effects) add corrections.

**Theorem (proposed):** $\mathcal{A} \in \mathcal{V}$ if and only if (i) the genus-1 bar curvature is a scalar multiple of $E_2$, and (ii) all higher-genus curvatures are determined by descent from the genus-1 anomaly via the universality theorem $m_0^{(g)} = \kappa \cdot \lambda_g$.

This subclass currently sits implicitly in the manuscript (every member has an individual proof of $\kappa = c/2$, but there is no unifying statement). Promoting it to an explicit theorem would close the AP39 generalisation gap, give βγ/bc/free-fermion a structural home, and establish a clean "conformal anomaly only ⇒ $\kappa = c/2$" principle for the modular Koszul programme.

### Upgrade path 2 — Level-1 reduction theorem promoted to category-level functor.

**Current status:** Proposition `prop:level1-kappa-reduction` (level1_bridge.tex L208) is `\ClaimStatusProvedHere`, but the proof relies on the curvature-braiding orthogonality theorem and the FKS isomorphism. It is local to the rank/dim distinction.

**Upgrade:** State the level-1 reduction as a **functorial** statement at the level of the bar-cobar pair. Define a functor $\mathrm{Lev}_1: \widehat{\mathfrak{g}}\text{-Mod}_{k=1}^{\mathrm{simply-laced}} \to V_{\Lambda_{\mathfrak{g}}}\text{-Mod}$ via FKS. Then the modular characteristic is functorial under $\mathrm{Lev}_1$:
\[
\kappa(\mathrm{Lev}_1(\widehat{\mathfrak{g}}_1)) = \kappa(V_{\Lambda_{\mathfrak{g}}}) = \mathrm{rank}(\Lambda_{\mathfrak{g}}) = \mathrm{rank}(\mathfrak{g}).
\]

This makes the rank reduction a *consequence* of categorical equivalence rather than a coincidence of two distinct calculations. It also gives a clean mechanism: the modular characteristic is preserved by the bar-cobar adjunction applied through FKS, so any value computed on either side is the value on both sides.

**Side benefit:** Forces the census table to be rewritten as "lattice presentation" vs "current presentation" with a single $\kappa$ per algebra (the lattice-presentation value), not two competing values.

### Upgrade path 3 — Conductor as a 2-cocycle in the Picard group of central extensions.

**Observation:** The Koszul conductor $K = \kappa(\mathcal{A}) + \kappa(\mathcal{A}^!)$ is family-dependent: $K = 0$ for KM, free fields, lattice VOAs; $K = 13$ for Vir; $K = 100$ for W_3; $K = 196$ for BP; $K = 246$ for W_4; $K = 4N^3 - 2N - 2$ for W_N (landscape_census L730-731). For lattice VOAs and free fields, $K = 0$ identifies $\mathcal{A}^! = \mathcal{A}^{\vee}$ in the Koszul-dual Picard group.

**Upgrade:** Reformulate $K$ as a 2-cocycle $K \in H^2(\mathrm{Iso}(\mathrm{Vir})/\mathrm{Aut}, \mathbb{C}^\times)$ (or a refinement) on the moduli of chiral algebras admitting a Virasoro action. The Feigin-Frenkel involution $k \mapsto -k - 2h^\vee$ on KM, and the corresponding involutions on W-algebras, become the central-extension cocycles. The harmonic-number formula $\rho_{\mathcal{W}_N} = H_N - 1$ (landscape_census L1245, L1260, L730) becomes the value of this cocycle on a specific generating loop in the moduli of W-algebras.

This path connects the Koszul conductor to known 2-cocycle structures in the literature (Feigin-Frenkel, Kazama-Suzuki) and gives a structural reason for the formulas $K_N = 4N^3 - 2N - 2$ and $\rho = H_N - 1$ (currently presented as computational outputs).

---

## §8. Punch list (priority-ordered)

**P0 (build correctness, immediate)**
1. **`standalone/koszulness_fourteen_characterizations.tex` L1298**: Replace wrong $c(k) = (k-1)(6k+1)/(k+3)$ with FKR $c(k) = 2 - 24(k+1)^2/(k+3)$. Verify downstream $K = c + c'$ identity rederives 196.
2. **`standalone/bp_self_duality.tex` L315-329**: Rewrite the signed-DS-sum derivation. Use the BP chapter's correct weight assignment (T=2, J=1, G±=3/2). Use the correct contribution formula (1 fermion → $-1/h$, not $-2/h$). The displayed sum $1 - 4/3 - 4/3 + 1/2$ must be replaced; it arithmetic-evaluates to $-7/6$, not the claimed $1/6$.

**P1 (consistency, high priority)**
3. **`landscape_census.tex` L615-633**: Apply level-1 reduction. Replace KM-formula $\kappa$ values with $\mathrm{rank}(\mathfrak{g})$ for simply-laced ADE entries. Recompute $F_1 = \kappa/24$ and $F_2 = 7\kappa/5760$. Leave non-simply-laced rows ($B_2$, $C_2$, $F_4$, $G_2$) unchanged (FKS does not apply). Add a footnote citing `prop:level1-kappa-reduction`.
4. **`landscape_census.tex` master table (L686-715 area)**: Add a BP row with $\kappa = c/6$, $K = 196$, $\rho = 1/6$, class M.

**P2 (notation hygiene)**
5. **`heisenberg_eisenstein.tex`**: Rename $\mathcal{H}_\kappa$ to $\mathcal{H}_k$ throughout. Reserve $\kappa$ for the modular characteristic. The identity $\kappa(\mathcal{H}_k) = k$ is then a theorem statement.
6. **`kac_moody.tex`**: Disambiguate three uses of $\kappa$ (Killing form, Casimir element, modular characteristic). Suggested: $\kappa_{\mathrm{Kill}}$ for the bilinear form; $\Omega$ for the Casimir (already used at L736, L755 — extend); $\kappa$ reserved for modular characteristic.
7. **`free_fields.tex` L41-46 vs `beta_gamma.tex` L2819**: Resolve "$r(z) = 0$" vs "$r(z) = \sum (-1)^n\binom{n+m}{m} \cdots / z^{n+m+1}$" by introducing $r_{\mathrm{coll}}$ vs $r_{\mathrm{dual}}$ notation. Update both chapters and `def:modular-koszul-triple`.

**P3 (convention statements)**
8. **`kac_moody.tex` L92, 114, 743, 1772, 2080, 3420, 5495, 5641**: Add "KZ normalisation" tag to each $r(z) = \Omega/((k+h^\vee)z)$ formula. Add a remark contrasting with the bare classical r-matrix $r_{\mathrm{class}}(z) = k\Omega/z$ (AP126's preferred normalisation), with the explicit relation $r_{\mathrm{KZ}} = r_{\mathrm{class}}/(k(k+h^\vee))$.
9. **`heisenberg_eisenstein.tex` L52-60 + `beta_gamma.tex` L1280-1287**: Explicitly state the convention $\theta_1'/\theta_1$ (logarithmic derivative of $\theta_1$, NOT Weierstrass $\zeta$). Per AP156, every $\wp_1$ or "first-order elliptic function" must specify this.

**P4 (anti-pattern strengthening)**
10. **`CLAUDE.md` AP39**: Strengthen the κ-formula taxonomy. Add the "Virasoro-anomaly-only" subclass enumeration: Vir, βγ, bc, free fermion → $\kappa = c/2$ universally (not just Vir). Add the mechanism (genus-1 bar curvature exhausted by Virasoro anomaly).
11. **`CLAUDE.md` AP126**: Strengthen the r-matrix level-prefix rule to enumerate two normalisations: (i) bare classical $r_{\mathrm{class}}(z) = k\Omega/z$ (AP126's $k=0$ test applies); (ii) KZ-normalised $r_{\mathrm{KZ}}(z) = \Omega/((k+h^\vee)z)$ (singular at critical level; KZ equation governing).

**P5 (documentation)**
12. **`bershadsky_polyakov.tex`**: Add a remark recording that the formal self-dual central charge $c = 98$ (and $\kappa = 49/3$) is the *Cauchy principal value* at the critical pole $k = -3$: $\lim_{\epsilon \to 0^+} \tfrac{1}{2}[c(-3+\epsilon) + c(-3-\epsilon)] = 98$. Currently this is implied but never stated.
13. **`free_fields.tex` rem:free-fields-three-pillar L93-126**: Soften "Pillar B formal AND Pillar C classical simultaneously" to make explicit that this is **one mechanism** (no simple-pole OPE at high arity) **manifest in two pillars**, not two independent confirmations.

---

## Headline summary

- **BP arithmetic**: bug is in `standalone/bp_self_duality.tex` L327, not in the chapter. Right answer (1/6), wrong derivation (swapped weights and wrong fermion factor).
- **BP central charge**: chapter is clean (FKR). Wrong formula in `standalone/koszulness_fourteen_characterizations.tex` L1298 — fix.
- **βγ/bc complementarity**: clean (sum = 0 everywhere). Prior wave's "sum ≠ 0" finding was incorrect.
- **κ = c/2 scoping (AP39)**: chapter usage is correct, AP39 is too narrow. Strengthen AP39 to enumerate the Virasoro-anomaly-only subclass.
- **KM r-matrix (AP126)**: chapter uses KZ normalisation throughout, with $\Omega/((k+h^\vee)z)$. AP126 demands bare normalisation, with $k\Omega/z$. Both correct in scope; chapter should tag every formula with the convention name.
- **Heisenberg ordered bar**: convention is "curved at $k\ne 0$, uncurved at $k = 0$" — internally consistent. Notation clash $\mathcal{H}_\kappa$ vs $\mathcal{H}_k$ should be resolved.
- **Level-1 KM/lattice contradiction**: BIGGEST FINDING. `level1_bridge.tex` proves $\kappa = \mathrm{rank}$ at $k=1$ simply-laced. `landscape_census.tex` L615-633 uses $\kappa = \dim(g)(1+h^\vee)/(2h^\vee)$ — the value the bridge chapter explicitly says is WRONG. Fix the census.
- **βγ r-matrix**: $r = 0$ vs $r = \sum (-1)^n \binom{n+m}{m} \cdots$ — same notation, different objects. Disambiguate to $r_{\mathrm{coll}}$ vs $r_{\mathrm{dual}}$.

The example chapters are 90% correct and 10% notation-clashed with each other. Healing requires 6 minor edits (rename $\mathcal{H}_\kappa \to \mathcal{H}_k$; introduce $r_{\mathrm{coll}}/r_{\mathrm{dual}}$; tag KZ normalisation; correct level-1 census rows; fix BP standalone arithmetic; fix koszulness-14 c(k)) and 2 anti-pattern strengthenings (AP39, AP126).

Cache write-back targets: 5 new entries (§6.1–§6.5) for the cross-programme first-principles cache.
